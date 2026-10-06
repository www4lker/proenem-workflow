#!/usr/bin/env python3
"""Monta a coluna `prompt_completo` do Pass 2: prompt da área + "INPUT:" + JSON da questão.

Reconstruído (06/10/2026) a partir do registro em docs/historico/pipeline-logs/logs/2026-05-16.md e
conferido contra corpus_enem/batch_completo_raw.csv: reproduz as 350 linhas byte a byte
(teste em pipeline/tests/test_montar_prompts.py).

Uso (de dentro de pipeline/):
  python scripts/montar_prompts.py --output corpus_enem/prompts_CH.csv            # todas as linhas CH
  python scripts/montar_prompts.py --area CN --input corpus_enem/questoes_raw.csv --output prompts_CN.csv
  python scripts/montar_prompts.py --ids 2013_CH_001 2013_CH_002 --output amostra.csv

Depois: ask_batch.py --input <saída> --template "{prompt_completo}" --output <raw> --field-out classificacao
--id-field id   (custa dinheiro: só com confirmação humana). Linhas sem enunciado ficam de fora e são listadas.
Nada aqui chama o Gemini.
"""
import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import areas  # noqa: E402

SEPARADOR = "\n\n\nINPUT:\n"   # prompt sem o "\n" final + 3 quebras + rótulo


def montar_prompt(prompt_texto: str, linha: dict) -> str:
    """prompt + INPUT + JSON {id, enunciado, alternativas (objeto), gabarito}, como no Pass 2 de 05/2026."""
    alternativas = linha["alternativas"]
    if isinstance(alternativas, str):
        alternativas = json.loads(alternativas)
    payload = {
        "id": linha["id"],
        "enunciado": linha["enunciado"],
        "alternativas": alternativas,
        "gabarito": linha.get("gabarito") or "",
    }
    return prompt_texto.rstrip() + SEPARADOR + json.dumps(payload, ensure_ascii=False)


def ler_questoes(caminho: Path, area: str, ids: set[str] | None):
    with open(caminho, encoding="utf-8", newline="") as f:
        for linha in csv.DictReader(f):
            if linha.get("area") != area:
                continue
            if ids is not None and linha["id"] not in ids:
                continue
            yield linha


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--area", default="CH", choices=areas.siglas())
    ap.add_argument("--input", type=Path, default=Path("corpus_enem/questoes_raw.csv"))
    ap.add_argument("--output", type=Path, required=True, help="CSV com colunas id, prompt_completo")
    ap.add_argument("--prompt", type=Path, help="arquivo de prompt (padrão: o da área em config/areas.yaml)")
    ap.add_argument("--ids", nargs="*", help="só estes ids")
    args = ap.parse_args()

    prompt_path = args.prompt or areas.prompt(args.area)
    if not prompt_path or not Path(prompt_path).exists():
        sys.exit(f"não há prompt para a área {args.area} (config/areas.yaml) e --prompt não foi dado")
    prompt_texto = Path(prompt_path).read_text(encoding="utf-8")

    ids = set(args.ids) if args.ids else None
    montados, sem_enunciado = [], []
    for linha in ler_questoes(args.input, args.area, ids):
        if not (linha.get("enunciado") or "").strip():
            sem_enunciado.append(linha["id"])
            continue
        montados.append({"id": linha["id"], "prompt_completo": montar_prompt(prompt_texto, linha)})

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "prompt_completo"])
        w.writeheader()
        w.writerows(montados)
    print(f"{len(montados)} prompts em {args.output} (prompt: {prompt_path})")
    if sem_enunciado:
        print(f"{len(sem_enunciado)} sem enunciado, fora do lote: {', '.join(sem_enunciado)}")


if __name__ == "__main__":
    main()
