#!/usr/bin/env python3
"""
ask_batch.py — delega classificação/extração linha a linha de um CSV ao Gemini CLI.

Resiliente: o próprio arquivo de --output é o checkpoint. Cada linha é gravada
e dada flush imediatamente; ao reexecutar, as linhas já presentes na saída são
puladas. Interromper com Ctrl+C e rodar de novo processa só o que falta.

Exemplo:
  python ask_batch.py \\
    --input questoes_raw.csv \\
    --template "Classifique o tema em uma palavra: {enunciado}" \\
    --output questoes_classif.csv \\
    --field-out tema --id-field id

Sequencial (sem paralelismo). Falha numa linha → grava resultado vazio e segue
(não inventa dado); reexecutar NÃO retenta falhas (remova-as da saída p/ retentar).
"""
import argparse
import csv
import subprocess
import sys
from pathlib import Path


def call_gemini(prompt: str, model: str, timeout: int) -> str:
    try:
        r = subprocess.run(
            ["gemini", "--skip-trust", "-m", model, "-p", prompt],
            capture_output=True, text=True, timeout=timeout,
            stdin=subprocess.DEVNULL,  # senão gemini bloqueia lendo stdin
        )
    except FileNotFoundError:
        sys.exit("erro: 'gemini' CLI não encontrado no PATH")
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"timeout após {timeout}s")
    if r.returncode != 0:
        raise RuntimeError((r.stderr.strip() or "gemini retornou erro")[-300:])
    return r.stdout.strip()


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Batch resiliente de delegação ao Gemini CLI.")
    ap.add_argument("--input", required=True, help="CSV de entrada")
    ap.add_argument("--template", required=True,
                    help="prompt com {coluna} interpolando campos da linha")
    ap.add_argument("--output", required=True, help="CSV de saída (= checkpoint)")
    ap.add_argument("--field-out", default="resultado",
                    help="nome da coluna de resultado (default: resultado)")
    ap.add_argument("--id-field",
                    help="coluna identificadora p/ retomada (default: índice da linha)")
    ap.add_argument("--model", default="gemini-2.5-flash")
    ap.add_argument("--timeout", type=int, default=120)
    args = ap.parse_args()

    inp = Path(args.input)
    if not inp.exists():
        sys.exit(f"erro: entrada não encontrada: {inp}")
    with inp.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("erro: CSV de entrada vazio")

    if args.id_field and args.id_field not in rows[0]:
        sys.exit(f"erro: coluna --id-field '{args.id_field}' não existe na entrada")

    fieldnames = list(rows[0].keys())
    if args.field_out not in fieldnames:
        fieldnames.append(args.field_out)

    def row_id(idx: int, row: dict) -> str:
        return row[args.id_field] if args.id_field else str(idx)

    outp = Path(args.output)
    done: set[str] = set()
    if outp.exists() and outp.stat().st_size > 0:
        with outp.open(encoding="utf-8") as f:
            for idx, r in enumerate(csv.DictReader(f)):
                done.add(r[args.id_field] if args.id_field else str(idx))

    restantes = len(rows) - len(done)
    print(f"[batch] {len(rows)} linhas | {len(done)} já feitas | "
          f"{restantes} restantes", file=sys.stderr)

    write_header = not (outp.exists() and outp.stat().st_size > 0)
    try:
        with outp.open("a", newline="", encoding="utf-8") as fout:
            writer = csv.DictWriter(fout, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            for idx, row in enumerate(rows):
                rid = row_id(idx, row)
                if rid in done:
                    continue
                try:
                    prompt = args.template.format(**row)
                except KeyError as e:
                    sys.exit(f"erro: template referencia coluna inexistente: {e}")
                try:
                    resultado = call_gemini(prompt, args.model, args.timeout)
                    status = "ok"
                except RuntimeError as e:
                    resultado = ""  # falha registrada como vazia — não inventa dado
                    status = f"FALHOU ({e})"
                out_row = dict(row)
                out_row[args.field_out] = resultado
                writer.writerow(out_row)
                fout.flush()
                print(f"[batch] {rid}: {status}", file=sys.stderr)
    except KeyboardInterrupt:
        sys.exit("\n[batch] interrompido — reexecute para retomar de onde parou")
    print("[batch] concluído", file=sys.stderr)


if __name__ == "__main__":
    main()
