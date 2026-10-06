#!/usr/bin/env python3
"""Amostra cega para medir a concordância entre o professor e a classificação do Gemini (CH).

Dois comandos:
  sortear  -> grava a ficha (questões + matriz oficial, sem a classificação do Gemini) e a lista de ids;
  comparar -> lê as respostas que o professor escreveu na ficha e grava o resultado.

Uso (da raiz do repositório):
  python3 pipeline/scripts/amostra_cega.py sortear docs/auditoria/amostra-ch-01
  python3 pipeline/scripts/amostra_cega.py comparar docs/auditoria/amostra-ch-01

Política e critério de leitura do resultado: docs/auditoria.md.
"""
import argparse
import csv
import json
import random
import re
import subprocess
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CORPUS = RAIZ / "pipeline/analise/corpus_mestre.csv"
MATRIZ = RAIZ / "pipeline/fontes/matriz-ch-inep-2026.json"
MANIFESTO = RAIZ / "pipeline/fontes/MANIFESTO.csv"

SEMENTE = 20261006
# Questões por competência atribuída pelo Gemini: proporcional ao corpus confiável, mínimo de 2 por estrato.
COTAS = {1: 3, 2: 2, 3: 2, 4: 4, 5: 7, 6: 2}


def ler_corpus():
    with CORPUS.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def competencia_gemini(linha):
    try:
        return int(float(linha["competencia"]))
    except (TypeError, ValueError):
        return None


def numero_oficial(ano, numero):
    """CH ocupa 1–45 do dia 1 até 2016 e 46–90 a partir de 2017."""
    return int(numero) + (45 if int(ano) >= 2017 else 0)


def caderno_dia1(ano):
    with MANIFESTO.open(encoding="utf-8", newline="") as f:
        for m in csv.DictReader(f):
            if m["ano"] == str(ano) and m["dia"] == "1" and m["tipo"] == "prova":
                return f"pipeline/{ano}/{m['nome_esperado']}"
    return None


def pagina_da_questao(pdf, numero):
    """Página (1, 2, …) do título 'Questão nn' no PDF; None se o PDF faltar ou o título não for achado."""
    caminho = RAIZ / pdf if pdf else None
    if not caminho or not caminho.exists():
        return None
    texto = subprocess.run(["pdftotext", str(caminho), "-"], capture_output=True, text=True).stdout
    for i, pagina in enumerate(texto.split("\f"), start=1):
        if re.search(rf"quest[ãa]o\s+0*{numero}\b", pagina, re.I):
            return i
    return None


def sortear(pasta):
    linhas = [x for x in ler_corpus()
              if x["area_confiavel"].lower() == "true" and x["enunciado"].strip() and competencia_gemini(x)]
    por_comp = defaultdict(list)
    for x in linhas:
        por_comp[competencia_gemini(x)].append(x)
    rng = random.Random(SEMENTE)
    escolhidas = []
    for c, n in sorted(COTAS.items()):
        escolhidas += rng.sample(sorted(por_comp[c], key=lambda x: x["id"]), n)
    rng.shuffle(escolhidas)  # a ordem da ficha não revela o estrato

    matriz = json.loads(MATRIZ.read_text(encoding="utf-8"))
    pasta.mkdir(parents=True, exist_ok=True)
    out = [
        "---", f"gerado: {date.today().isoformat()}", "script: pipeline/scripts/amostra_cega.py sortear",
        f"semente: {SEMENTE}", "---", "",
        "# Amostra cega CH nº 1: ficha do professor", "",
        "Para cada questão, escreva o número da competência e da habilidade da **matriz oficial** (abaixo) nas "
        "linhas `Competência:` e `Habilidade:`. Uma resposta por linha, só o número (ex.: `Competência: 3`, "
        "`Habilidade: 12`). Se ficar em dúvida entre duas, escreva a principal e explique em `Nota:`. "
        "Deixar em branco = não classificada (não entra na conta).", "",
        "Imagens, mapas e gráficos não estão aqui: abra o PDF indicado na página indicada.", "",
        f"## Matriz de referência oficial de CH ({matriz['fonte']})", "",
    ]
    for c, texto in matriz["competencias"].items():
        out.append(f"- **C{c}.** {texto}")
    out += ["", "<details><summary>Habilidades H1–H30</summary>", ""]
    for h, texto in matriz["habilidades"].items():
        out.append(f"- **H{h}.** {texto}")
    out += ["", "</details>", "", "## Questões", ""]

    pdfs = {}
    for i, x in enumerate(escolhidas, start=1):
        ano, n = x["ano"], numero_oficial(x["ano"], x["numero"])
        pdf = pdfs.setdefault(ano, caderno_dia1(ano))
        pg = pagina_da_questao(pdf, n)
        local = f"`{pdf}`, Questão {n}" + (f", p. {pg}" if pg else "")
        out += [f"### {i:02d} · ENEM {ano}, questão {n}", "", f"Fonte: {local}", ""]
        out += ["> " + l if l.strip() else ">" for l in x["enunciado"].strip().splitlines()]
        out.append("")
        try:
            alternativas = json.loads(x["alternativas"] or "{}")
        except json.JSONDecodeError:
            alternativas = {}
        for letra, texto in alternativas.items():
            out.append(f"- **{letra})** {texto}")
        if x["fontes_citadas"] and any(k in x["fontes_citadas"] for k in ("mapa", "gráfico", "grafico", "imagem",
                                                                           "charge", "tabela", "foto", "figura")):
            out += ["", "*Tem elemento visual: conferir no PDF.*"]
        out += ["", "Competência: ", "Habilidade: ", "Nota: ", ""]
    (pasta / "ficha.md").write_text("\n".join(out), encoding="utf-8")
    (pasta / "ids.csv").write_text(
        "ordem,id\n" + "".join(f"{i},{x['id']}\n" for i, x in enumerate(escolhidas, start=1)), encoding="utf-8")
    print(f"escrito {pasta / 'ficha.md'} ({len(escolhidas)} questões)")


def ler_respostas(ficha):
    """Devolve {ordem: (competência, habilidade, nota)} a partir dos campos preenchidos na ficha."""
    respostas, atual = {}, None
    for linha in ficha.read_text(encoding="utf-8").splitlines():
        m = re.match(r"###\s+(\d+)\s+·", linha)
        if m:
            atual = int(m.group(1))
            respostas[atual] = [None, None, ""]
            continue
        if atual is None:
            continue
        m = re.match(r"(Competência|Habilidade|Nota):\s*(.*)$", linha.strip())
        if not m:
            continue
        campo, valor = m.groups()
        if campo == "Nota":
            respostas[atual][2] = valor.strip()
        else:
            num = re.search(r"\d+", valor)
            respostas[atual][0 if campo == "Competência" else 1] = int(num.group()) if num else None
    return respostas


def kappa(pares):
    """Kappa de Cohen: concordância corrigida pelo acaso (1 = total; 0 = o que se esperaria por sorte)."""
    n = len(pares)
    if not n:
        return None
    obs = sum(a == b for a, b in pares) / n
    ca, cb = Counter(a for a, _ in pares), Counter(b for _, b in pares)
    esp = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return None if esp == 1 else (obs - esp) / (1 - esp)


def comparar(pasta):
    corpus = {x["id"]: x for x in ler_corpus()}
    with (pasta / "ids.csv").open(encoding="utf-8", newline="") as f:
        ids = {int(r["ordem"]): r["id"] for r in csv.DictReader(f)}
    respostas = ler_respostas(pasta / "ficha.md")

    linhas, pares_c, pares_h = [], [], []
    for ordem, id_ in sorted(ids.items()):
        x = corpus[id_]
        gc = competencia_gemini(x)
        gh = int(m.group(1)) if (m := re.search(r"(\d+)", x["habilidade"] or "")) else None
        pc, ph, nota = respostas.get(ordem, [None, None, ""])
        if pc is not None:
            pares_c.append((pc, gc))
        if ph is not None:
            pares_h.append((ph, gh))
        linhas.append((ordem, id_, pc, gc, ph, gh, nota))

    def pct(pares):
        return f"{sum(a == b for a, b in pares)}/{len(pares)} ({sum(a == b for a, b in pares) / len(pares):.0%})" \
            if pares else "sem respostas"

    def fmt(v):
        return "–" if v is None else f"{v:.2f}"

    out = [
        "---", f"gerado: {date.today().isoformat()}", "script: pipeline/scripts/amostra_cega.py comparar", "---", "",
        "# Amostra cega CH nº 1: resultado", "",
        "Professor = classificação na ficha, pela matriz oficial. Gemini = coluna do corpus, gerada com o prompt "
        "`pipeline/prompts/classificar_questao.txt` (rótulos de competência que não são os oficiais; ver "
        "`docs/auditoria.md`).", "",
        "| medida | competência | habilidade |", "|---|---|---|",
        f"| concordância exata | {pct(pares_c)} | {pct(pares_h)} |",
        f"| kappa de Cohen | {fmt(kappa(pares_c))} | {fmt(kappa(pares_h))} |", "",
        "## Confusão de competências (linhas = professor, colunas = Gemini)", "",
        "| | " + " | ".join(f"G{c}" for c in range(1, 7)) + " |", "|---" * 7 + "|",
    ]
    conf = Counter(pares_c)
    for p in range(1, 7):
        out.append(f"| P{p} | " + " | ".join(str(conf[(p, g)] or "") for g in range(1, 7)) + " |")
    out += ["", "## Questão a questão", "", "| nº | id | prof. C | Gemini C | prof. H | Gemini H | nota |",
            "|---|---|---|---|---|---|---|"]
    for ordem, id_, pc, gc, ph, gh, nota in linhas:
        out.append(f"| {ordem} | {id_} | {pc or ''} | {gc or ''} | {ph or ''} | {gh or ''} | {nota} |")
    (pasta / "resultado.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"escrito {pasta / 'resultado.md'}: competência {pct(pares_c)}, habilidade {pct(pares_h)}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("comando", choices=["sortear", "comparar"])
    p.add_argument("pasta", type=Path)
    a = p.parse_args()
    pasta = a.pasta if a.pasta.is_absolute() else Path.cwd() / a.pasta
    if a.comando == "sortear":
        if (pasta / "ficha.md").exists():
            raise SystemExit(f"{pasta / 'ficha.md'} já existe: não sobrescrevo respostas. Use outra pasta.")
        sortear(pasta)
    else:
        comparar(pasta)


if __name__ == "__main__":
    main()
