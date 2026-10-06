#!/usr/bin/env python3
"""Baixa (ou só confere) as provas e gabaritos do INEP listados em fontes/MANIFESTO.csv.

Uso (de dentro de pipeline/):
  python scripts/baixar_provas.py [--anos 2019 2025] [--dias 1] [--so-conferir] [--registrar-sha]

- Baixa para <ano>/<nome_esperado> o que não existe (URL de `url_oficial`, mesmo com status "a verificar":
  o download que der certo marca a URL como conferida quando --registrar-sha é dado).
- Confere o sha256 do arquivo local com o do manifesto; sem sha no manifesto, --registrar-sha grava o
  calculado (e a data em status_url). Arquivo com sha diferente é recusado e o erro é listado.
- Não chama API nenhuma; só HTTP ao INEP. Se a rede não alcançar o INEP, diz isso e sai com 2.
"""
import argparse
import csv
import hashlib
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
MANIFESTO = PIPELINE / "fontes" / "MANIFESTO.csv"
# O servidor do INEP não envia o certificado intermediário (RNP ICPEdu, emitido pela GlobalSign Root R46).
# Ele vai junto ao repositório e é somado às autoridades do sistema; a verificação continua ligada.
CA_INTERMEDIARIA = PIPELINE / "fontes" / "inep-ca-intermediaria.pem"


def contexto_tls() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    if CA_INTERMEDIARIA.exists():
        ctx.load_verify_locations(cafile=CA_INTERMEDIARIA)
    return ctx


def sha256(caminho: Path) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def baixar(url: str, destino: Path) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "proenem-workflow/baixar_provas"})
    with urllib.request.urlopen(req, timeout=60, context=contexto_tls()) as r, open(destino, "wb") as f:
        tipo = r.headers.get("Content-Type", "")
        if "pdf" not in tipo and "octet-stream" not in tipo:
            raise ValueError(f"resposta não é PDF ({tipo})")
        for bloco in iter(lambda: r.read(1 << 20), b""):
            f.write(bloco)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--anos", type=int, nargs="*")
    ap.add_argument("--dias", type=int, nargs="*", default=[1, 2])
    ap.add_argument("--so-conferir", action="store_true", help="não baixa; só confere o que já existe")
    ap.add_argument("--registrar-sha", action="store_true", help="grava no manifesto o sha256 dos arquivos conferidos")
    args = ap.parse_args()

    with open(MANIFESTO, encoding="utf-8", newline="") as f:
        linhas = list(csv.DictReader(f))
        campos = list(linhas[0].keys())

    erros, sem_rede = [], False
    for l in linhas:
        ano, dia = int(l["ano"]), int(l["dia"])
        if (args.anos and ano not in args.anos) or dia not in args.dias:
            continue
        destino = PIPELINE / str(ano) / l["nome_esperado"]
        rotulo = f"{ano} dia {dia} {l['tipo']:<8} {l['nome_esperado']}"

        if not destino.exists():
            if args.so_conferir:
                print(f"falta    {rotulo}")
                continue
            try:
                baixar(l["url_oficial"], destino)
                print(f"baixado  {rotulo}")
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
                erros.append(f"{rotulo}: {e}")
                destino.unlink(missing_ok=True)
                if isinstance(e, urllib.error.URLError) and not isinstance(e, urllib.error.HTTPError):
                    sem_rede = True
                continue
            if args.registrar_sha and l["status_url"] == "a verificar":
                l["status_url"] = f"conferida {date.today().isoformat()}"

        calculado = sha256(destino)
        if l["sha256"]:
            if calculado != l["sha256"]:
                erros.append(f"{rotulo}: sha256 difere do manifesto ({calculado[:12]}… ≠ {l['sha256'][:12]}…)")
                continue
            print(f"ok       {rotulo}")
        elif args.registrar_sha:
            l["sha256"] = calculado
            print(f"sha novo {rotulo} {calculado[:12]}…")
        else:
            print(f"sem sha  {rotulo} (use --registrar-sha para gravar {calculado[:12]}…)")

    if args.registrar_sha:
        with open(MANIFESTO, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=campos)
            w.writeheader()
            w.writerows(linhas)
        print(f"manifesto atualizado: {MANIFESTO}")

    for e in erros:
        print("ERRO", e, file=sys.stderr)
    if sem_rede:
        print("o INEP não respondeu: baixe pela sessão local (ver fontes/LEIAME.md)", file=sys.stderr)
        sys.exit(2)
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
