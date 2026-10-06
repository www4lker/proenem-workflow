"""Processa todas as provas D1 do recorte 2013-2018."""
import sys
from pathlib import Path
from extrair_prova import processar

ANOS = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2025]
BASE = Path(".")

def encontrar_prova_d1(ano: int) -> Path | None:
    """Heurística: PDF do ano com 'd1', 'dia1' ou 'sabado' no nome, e azul/caderno1."""
    pasta = BASE / str(ano)
    if not pasta.exists():
        return None
    candidatos = []
    for p in pasta.glob("*.pdf"):
        nome = p.name.lower().replace("_", "").replace("-", "")
        score = 0
        if "d1" in nome or "dia1" in nome: score += 10
        if "sabado" in nome: score += 5
        if "azul" in nome or "cd1" in nome or "caderno1" in nome: score += 5
        if "gab" in nome and "gabarito" not in nome: score -= 10
        if "gabarito" in nome: score -= 10
        if "d2" in nome or "dia2" in nome or "domingo" in nome: score -= 20
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

for ano in ANOS:
    prova = encontrar_prova_d1(ano)
    if not prova:
        print(f"[{ano}] ❌ prova D1 não encontrada — pular")
        continue
    print(f"\n[{ano}] processando {prova.name}")
    try:
        processar(prova)
    except Exception as e:
        print(f"[{ano}] ❌ falhou: {e}")
