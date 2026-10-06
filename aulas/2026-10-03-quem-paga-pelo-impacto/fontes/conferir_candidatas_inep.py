#!/usr/bin/env python3
"""Confere as candidatas de geografia do corpus PROENEM contra os PDFs oficiais (somente leitura).

Para cada questão de geografia do corpus, compara:
  1. o gabarito do corpus com o gabarito oficial (PDF do INEP guardado no PROENEM);
  2. o enunciado do corpus com o texto do caderno da prova, exigindo que o título "Questão nn"
     esteja na mesma página (±1). Detecta linhas de Linguagens rotuladas como CH.
Grava fontes/conferencia-inep-candidatas.md. Nada é escrito no PROENEM.
Esta checagem é automática. Questões com figura ou mapa ainda pedem olhar humano.
"""
import csv
import re
import subprocess
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3] / "pipeline"
CORPUS = RAIZ / "analise/corpus_mestre.csv"
SAIDA = Path(__file__).resolve().parent / "conferencia-inep-candidatas.md"

# ano -> (caderno da prova, gabarito oficial), ambos do 1º dia, caderno 1 azul.
ARQUIVOS = {
    "2013": ("2013/dia1_caderno1_azul.pdf", "2013/dia1_azul.pdf"),
    "2014": ("2014/2014_PV_impresso_D1_CD1.pdf", "2014/CADERNO_1_AZUL_SABADO.pdf"),
    "2015": ("2015/2015_PV_impresso_D1_CD1.pdf", "2015/CADERNO_1_AZUL_SABADO.pdf"),
    "2016": ("2016/2016_PV_impresso_D1_CD1.pdf", "2016/GAB_ENEM_2016_DIA_1_01_AZUL.pdf"),
    "2017": ("2017/2017_PV_impresso_D1_CD1.pdf", "2017/cad_1_gabarito_azul_5112017.pdf"),
    "2018": ("2018/2018_PV_impresso_D1_CD1.pdf", "2018/GAB_ENEM_2018_DIA_1_AZUL.pdf"),
    "2019": ("2019/2019_PV_impresso_D1_CD1.pdf", "2019/gabarito_1_dia_caderno_1_azul_aplicacao_regular.pdf"),
    "2025": ("2025/2025_PV_impresso_D1_CD1.pdf", "2025/2025_GB_impresso_D1_CD1.pdf"),
}
JANELA = 25  # caracteres sem espaço por trecho comparado


def texto_pdf(caminho, layout=False):
    args = ["pdftotext"] + (["-layout"] if layout else []) + [str(RAIZ / caminho), "-"]
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def chave(texto):
    """Minúsculas, sem acentos, sem espaço e sem pontuação (robusto a quebras do PDF)."""
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", texto.lower())


def numero_oficial(ano, numero):
    """Até 2016 a CH ocupa 1–45; de 2017 em diante ocupa 46–90 (dia 1 começa por Linguagens)."""
    return int(numero) + (45 if int(ano) >= 2017 else 0)


def gabarito_oficial(ano):
    faixa = range(46, 91) if int(ano) >= 2017 else range(1, 46)
    achados = {}
    for n, letra in re.findall(r"\b(\d{1,3})\s+([A-E])\b", texto_pdf(ARQUIVOS[ano][1], layout=True)):
        if int(n) in faixa:
            achados.setdefault(int(n), letra)
    return achados


def paginas_prova(ano):
    """Devolve (chaves das páginas, números de 'Questão nn' em cada página).

    O pdftotext embaralha a ordem dentro de uma página de duas colunas, então a conferência é por
    página: o texto do enunciado e o título da questão devem cair na mesma página (±1).
    """
    paginas = texto_pdf(ARQUIVOS[ano][0]).split("\f")
    chaves = [chave(p) for p in paginas]
    titulos = [{int(n) for n in re.findall(r"quest[ãa]o\s+0*(\d{1,3})", p, re.I)} for p in paginas]
    return chaves, titulos


def localizar(enunciado, chaves):
    """Fração de trechos achados no caderno todo e página do primeiro trecho achado."""
    base = chave(enunciado)
    trechos = [base[i:i + JANELA] for i in range(0, len(base) - JANELA + 1, JANELA)]
    if not trechos:
        return None, None
    achados = 0
    pagina = None
    for t in trechos:
        for i, pg in enumerate(chaves):
            if t in pg:
                achados += 1
                pagina = i if pagina is None else pagina
                break
    return achados / len(trechos), pagina


def veredito(ano, n_oficial, cob, pagina, titulos):
    if cob is None:
        return "sem enunciado no corpus: conferir à mão"
    if cob < 0.8:
        return "enunciado não localizado no caderno: conferir à mão"
    vizinhas = set().union(*titulos[max(pagina - 1, 0):pagina + 2])
    if n_oficial in vizinhas:
        return "texto e número conferem"
    if int(ano) >= 2017 and n_oficial - 45 in vizinhas:
        return f"ÁREA ERRADA: é Linguagens (Questão {n_oficial - 45}), não CH"
    return "texto achado, mas o número não bate: conferir à mão"


def eh_geografia(linha):
    return linha["disciplina_principal"] == "geografia" or "geografia" in (linha["disciplinas_secundarias"] or "")


def main():
    with CORPUS.open(encoding="utf-8", newline="") as f:
        linhas = list(csv.DictReader(f))
    oficiais = {a: gabarito_oficial(a) for a in ARQUIVOS}
    provas = {a: paginas_prova(a) for a in ARQUIVOS}

    resultado, resumo = [], defaultdict(Counter)
    for x in linhas:
        ano, n = x["ano"], numero_oficial(x["ano"], x["numero"])
        chaves, titulos = provas[ano]
        cob, pagina = localizar(x["enunciado"], chaves)
        v = veredito(ano, n, cob, pagina, titulos)
        oficial = oficiais[ano].get(n)
        gab_ok = oficial is not None and oficial == x["gabarito"]
        resumo[ano]["total"] += 1
        resumo[ano]["texto e número conferem"] += v == "texto e número conferem"
        resumo[ano]["gabarito confere (nº esperado)"] += gab_ok
        resumo[ano]["área errada (Linguagens)"] += v.startswith("ÁREA ERRADA")
        if eh_geografia(x):
            resultado.append((x, n, oficial, gab_ok, cob, v))

    out = [
        "---", f"gerado: {date.today().isoformat()}",
        "script: fontes/conferir_candidatas_inep.py",
        "fonte da conferência: PDFs de prova e gabarito guardados no PROENEM (nome de arquivo indica INEP; "
        "origem não verificada por hash)",
        "status: conferência AUTOMÁTICA. Questões com figura/mapa pedem olhar humano antes de virar slide.",
        "---", "", "# Conferência das candidatas de geografia contra as provas oficiais", "",
        "Numeração: CH = 1–45 até 2016 e 46–90 a partir de 2017. “Enunciado” = fração de trechos de "
        f"{JANELA} caracteres do corpus encontrados no caderno; o título da questão precisa estar na mesma página (±1).",
        "", "## Validação do método (corpus inteiro, 355 questões)", "",
        "| ano | questões | texto e número conferem | área errada (Linguagens) | gabarito confere |",
        "|---|---|---|---|---|",
    ]
    for ano in sorted(resumo):
        r = resumo[ano]
        out.append(
            f"| {ano} | {r['total']} | {r['texto e número conferem']} | {r['área errada (Linguagens)']} "
            f"| {r['gabarito confere (nº esperado)']} |"
        )
    out += ["", "## Geografia", "",
            "| id | prova nº | gab. corpus | gab. oficial | enunciado | veredito |", "|---|---|---|---|---|---|"]
    for x, n, oficial, gab_ok, cob, v in sorted(resultado, key=lambda t: t[0]["id"]):
        pct = "-" if cob is None else f"{cob:.0%}"
        if v == "texto e número conferem" and not gab_ok:
            v = "GABARITO DIVERGE (usar o oficial); " + v
        elif v == "texto e número conferem":
            v = "conferido (gabarito, texto, número); olhar figura, se houver"
        out.append(f"| {x['id']} | {n} | {x['gabarito']} | {oficial or '?'} | {pct} | {v} |")
    SAIDA.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"escrito {SAIDA}")


if __name__ == "__main__":
    main()
