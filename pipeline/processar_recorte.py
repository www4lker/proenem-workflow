"""Processa todas as provas de uma área nos anos do recorte (Pass 1 em lote).

Uso (de dentro de pipeline/): python processar_recorte.py [--area CH] [--anos 2013 2014 ...]

Para cada ano, escolhe em <ano>/ o PDF da prova do dia que config/areas.yaml indica para a área
(heurística de nome e tamanho: "d1"/"dia1"/"sabado" ou "d2"/"dia2"/"domingo", caderno azul, > 2 MB)
e chama extrair_prova.processar. Os PDFs do INEP não são versionados (ver docs/FILA.md, F9).
"""
import argparse
from pathlib import Path

import areas
from extrair_prova import detectar_dia, processar

ANOS = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2025]
BASE = Path(".")


def encontrar_prova(ano: int, dia: int) -> Path | None:
    """Heurística: PDF do ano com marca do dia pedido no nome, azul/caderno 1, tamanho de prova."""
    pasta = BASE / str(ano)
    if not pasta.exists():
        return None
    candidatos = []
    for p in pasta.glob("*.pdf"):
        nome = p.name.lower().replace("_", "").replace("-", "").replace("á", "a")
        score = 0
        dia_pdf = detectar_dia(p)
        if dia_pdf == dia: score += 10
        if dia_pdf == 3 - dia: score -= 20
        if "azul" in nome or "cd1" in nome or "caderno1" in nome: score += 5
        if "gab" in nome and "gabarito" not in nome: score -= 10
        if "gabarito" in nome: score -= 10
        tamanho_mb = p.stat().st_size / 1_000_000
        if tamanho_mb < 0.5:
            score -= 15  # provavelmente gabarito
        elif tamanho_mb > 2:
            score += 3   # provavelmente prova
        if score > 0:
            candidatos.append((score, p))
    if not candidatos:
        return None
    return max(candidatos, key=lambda x: x[0])[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--area", default="CH", choices=areas.siglas())
    ap.add_argument("--anos", type=int, nargs="*", default=ANOS)
    args = ap.parse_args()

    for ano in args.anos:
        dia = areas.faixa(args.area, ano).dia
        prova = encontrar_prova(ano, dia)
        if not prova:
            print(f"[{ano}] ❌ prova do dia {dia} ({args.area}) não encontrada em {BASE / str(ano)} — pular")
            continue
        print(f"\n[{ano}] processando {prova.name} ({args.area}, dia {dia})")
        try:
            processar(prova, area=args.area)
        except Exception as e:
            print(f"[{ano}] ❌ falhou: {e}")


if __name__ == "__main__":
    main()
