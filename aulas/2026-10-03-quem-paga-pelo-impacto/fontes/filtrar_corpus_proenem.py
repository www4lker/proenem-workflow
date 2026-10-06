#!/usr/bin/env python3
"""Tria candidatas de geografia no corpus do PROENEM (somente leitura).

Lê pipeline/analise/corpus_mestre.csv e grava
fontes/candidatas-enem-proenem.md. Nada é escrito no PROENEM.

A classificação do corpus é de IA (rank 3): serve para triar, nunca para citar.
Toda candidata sai com "a conferir" até prova, ano, caderno, número e gabarito
serem confirmados no caderno oficial do INEP.
"""
import csv
import hashlib
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

CORPUS = Path(__file__).resolve().parents[3] / "pipeline/analise/corpus_mestre.csv"
SAIDA = Path(__file__).resolve().parent / "candidatas-enem-proenem.md"

# Grupos ligados aos ganchos da aula (base-geo-fisica.md, seção 6).
GRUPOS = {
    "energia": r"energi|hidrel|usina|eolic|solar|petrole|combustiv|matriz energ",
    "água": r"\bagua|hidrograf|bacia hidro|reservatorio|irrigac|represa|hidrovia|recursos hidricos",
    "clima": r"clima|chuva|precipitac|aquecimento global|efeito estufa|estiagem|desertifica",
    "relevo e solo": r"relevo|declivi|inunda|enchente|erosao|\bsolos?\b|tectonic|movimentos? de massa",
    "domínios e biomas": r"cerrado|caatinga|amazoni|pantanal|pampa|mata atlantica|bioma|dominio morfo",
    "tecnologia e dados": r"internet|digital|tecnolog|informacao|informacional|telecom|seguranca de dados|banco de dados",
    "território e infraestrutura": r"infraestrutura|urbaniz|metropol|industrializ|fronteira agricola|logistic|transporte",
}


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto or "")
    return "".join(c for c in texto if not unicodedata.combining(c)).lower()


def secundarias(valor):
    try:
        return json.loads((valor or "[]").replace("'", '"'))
    except json.JSONDecodeError:
        return []


def grupos_da_questao(linha):
    """Grupos pelo tema (IA) ou, se só pelo enunciado, marcados com (texto)."""
    tema = normalizar(linha["tema_principal"] + " " + linha["tema_secundario"])
    texto = normalizar(linha["enunciado"])
    achados = []
    for nome, padrao in GRUPOS.items():
        if re.search(padrao, tema):
            achados.append(nome)
        elif re.search(padrao, texto):
            achados.append(f"{nome} (texto)")
    return achados


def resumo(linha, limite=110):
    texto = re.sub(r"\s+", " ", linha["enunciado"] or "").strip()
    return (texto[:limite] + "…") if len(texto) > limite else texto or "(sem enunciado)"


def carregar():
    with CORPUS.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


# De 2017 em diante as linhas "CH" do corpus são, na verdade, as questões 1–45 de Linguagens
# (conferido contra os cadernos em conferir_candidatas_inep.py). Só 2013–2016 são CH de fato.
ULTIMO_ANO_VALIDO = 2016


def eh_geografia(linha):
    if int(linha["ano"]) > ULTIMO_ANO_VALIDO:
        return False
    return linha["disciplina_principal"] == "geografia" or "geografia" in secundarias(
        linha["disciplinas_secundarias"]
    )


def montar(linhas):
    total = len(linhas)
    geo = [x for x in linhas if eh_geografia(x)]
    sha = hashlib.sha256(CORPUS.read_bytes()).hexdigest()[:12]
    saida = [
        "---",
        f"gerado: {date.today().isoformat()}",
        f"origem: {CORPUS} (sha256 {sha}…; repositório com árvore suja, versão de trabalho)",
        "script: fontes/filtrar_corpus_proenem.py",
        "status: TRIAGEM. Nenhuma questão conferida. Não citar, não usar em slide.",
        "---",
        "",
        "# Candidatas do corpus PROENEM (geografia)",
        "",
        f"Corpus: {total} questões rotuladas CH (caderno azul, 2013–2019 e 2025). "
        f"**Só 2013–2016 são CH de fato**: as linhas de 2017, 2018, 2019 e 2025 são Linguagens "
        f"(ver `conferencia-inep-candidatas.md`) e foram excluídas. "
        f"Geografia (principal ou secundária) em 2013–2016: {len(geo)}.",
        "",
        "**Avisos**",
        "- Tema, disciplina e gabarito vêm de extração automática e classificação por IA (rank 3). "
        "Servem para triar.",
        "- Para tirar o rótulo **(autoral)** é preciso abrir o caderno oficial do INEP e confirmar "
        "ano, caderno, número, enunciado e gabarito, e então registrar em `fontes/checagem.md`.",
        "- O corpus não cobre Ciências da Natureza nem 2020–2024, e o texto do PDF traz quebras "
        "(ex.: “intensifi c ação”). Cinco questões estão sem enunciado.",
        "- A coluna “grupos” é busca por palavra-chave no tema (IA) e, marcada “(texto)”, no enunciado. Não é classificação. As alternativas não entram na busca.",
        "",
    ]
    sem_grupo = []
    por_grupo = {nome: [] for nome in GRUPOS}
    for linha in geo:
        grupos = grupos_da_questao(linha)
        if not grupos:
            sem_grupo.append(linha)
        for g in grupos:
            por_grupo[g.replace(" (texto)", "")].append(linha)

    def tabela(itens):
        cab = ["| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |",
               "|---|---|---|---|---|---|---|"]
        for x in itens:
            cab.append(
                "| {id} | {ano}/{n} | {gab} | {tema} | {gr} | {res} | a conferir |".format(
                    id=x["id"], ano=x["ano"], n=x["numero"], gab=x["gabarito"] or "?",
                    tema=(x["tema_principal"] or "?").replace("|", "/"),
                    gr=", ".join(grupos_da_questao(x)) or "-",
                    res=resumo(x).replace("|", "/"),
                )
            )
        return cab

    saida += ["## Resumo por grupo", "", "| grupo | questões |", "|---|---|"]
    saida += [f"| {g} | {len(v)} |" for g, v in por_grupo.items()]
    saida += [f"| (nenhum grupo) | {len(sem_grupo)} |", ""]
    for nome, itens in por_grupo.items():
        if itens:
            saida += [f"## {nome}", ""] + tabela(sorted(itens, key=lambda x: x["id"])) + [""]
    if sem_grupo:
        saida += ["## Geografia sem gancho por palavra-chave", ""] + tabela(sem_grupo) + [""]
    vazias = [x["id"] for x in linhas if not (x["enunciado"] or "").strip()]
    saida += ["## Sem enunciado no corpus", "", ", ".join(vazias) or "nenhuma", ""]
    return "\n".join(saida)


def main():
    linhas = carregar()
    SAIDA.write_text(montar(linhas), encoding="utf-8")
    print(f"{len(linhas)} linhas lidas; saída em {SAIDA}")


if __name__ == "__main__":
    main()
