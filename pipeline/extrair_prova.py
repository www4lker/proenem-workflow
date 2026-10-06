"""
Pass 1 — extrai uma prova ENEM e gera as linhas de uma área em questoes_raw.csv.

Uso:
  python extrair_prova.py 2014/2014_PV_impresso_D1_CD1.pdf              # área CH (padrão)
  python extrair_prova.py 2019/2019_PV_impresso_D2_CD7.pdf --area CN    # outra área

O dia da prova e a faixa de questões da área naquele ano vêm de config/areas.yaml
(ver areas.py): CH é 1–45 até 2016 e 46–90 a partir de 2017, por exemplo. O script
avisa se o nome do PDF indicar outro dia que não o da área.

Pré-requisitos:
  pip install -r requirements.txt (pymupdf, pandas, pyyaml)
  poppler-utils instalado (pdftotext no PATH)

Convenção de gabarito:
  Espera o PDF do gabarito do mesmo dia no MESMO diretório da prova, ou via flag
  --gabarito. Se não achar, falha cedo com mensagem clara.

Schema de saída (corpus_enem/questoes_raw.csv):
  id, ano, caderno, area, numero, enunciado, fontes_citadas, alternativas,
  gabarito

Idempotência:
  Re-rodar a mesma prova NÃO duplica linhas (chave: id).
"""

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import pymupdf as fitz  # PyMuPDF (>= 1.24)
import pandas as pd

import areas


# ---------- CONFIG ----------

OUTPUT_DIR = Path("./corpus_enem")
OUTPUT_DIR.mkdir(exist_ok=True)
RAW_CSV = OUTPUT_DIR / "questoes_raw.csv"

# Padrões de ruído a remover de cada bloco
RUIDO_PATTERNS = [
    re.compile(r"(?:CH|LC|CN|MT)\s*-\s*\d+º?\s*dia\s*\|\s*Caderno\s*\d+\s*-\s*\w+\s*-\s*Página\s*\d+", re.IGNORECASE),
    re.compile(r"\*\w+\*"),  # marcas d'água tipo *AZUL75SAB3*
    re.compile(r"^\s*\d+\s*$", re.MULTILINE),  # números de página soltos
]


# ---------- EXTRAÇÃO DE TEXTO (POC v4) ----------

def calha_por_pagina(blocos, page_width):
    meio = page_width / 2
    centros = sorted(
        (b[0] + b[2]) / 2 for b in blocos
        if meio - 120 < (b[0] + b[2]) / 2 < meio + 120
    )
    if not centros:
        return meio
    pontos = [meio - 120] + centros + [meio + 120]
    melhor_gap, melhor_centro = 0, meio
    for i in range(len(pontos) - 1):
        gap = pontos[i + 1] - pontos[i]
        if gap > melhor_gap:
            melhor_gap, melhor_centro = gap, (pontos[i] + pontos[i + 1]) / 2
    return melhor_centro


def extrair_texto_ordenado(pdf_path: Path) -> str:
    """Concatena blocos da prova em ordem de leitura (coluna esq → dir, por página)."""
    doc = fitz.open(pdf_path)
    pedacos = []
    for page in doc:
        blocos = [b for b in page.get_text("blocks") if b[6] == 0]
        calha = calha_por_pagina(blocos, page.rect.width)
        col_esq = sorted([b for b in blocos if (b[0] + b[2]) / 2 < calha], key=lambda b: b[1])
        col_dir = sorted([b for b in blocos if (b[0] + b[2]) / 2 >= calha], key=lambda b: b[1])
        for col in (col_esq, col_dir):
            for b in col:
                pedacos.append(b[4])
    doc.close()
    return "\n".join(pedacos)


def limpar_ruido(texto: str) -> str:
    for pat in RUIDO_PATTERNS:
        texto = pat.sub("", texto)
    # colapsa múltiplas quebras
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


# ---------- FATIAMENTO DE QUESTÕES ----------

def fatiar_questoes(texto: str) -> dict[int, str]:
    """Devolve {numero: corpo_bruto} (enunciado + alternativas misturados)."""
    partes = re.split(r"(QUESTÃO\s+\d+)", texto, flags=re.IGNORECASE)
    questoes = {}
    for i in range(1, len(partes), 2):
        num = int(re.search(r"\d+", partes[i]).group())
        corpo = partes[i + 1].strip() if i + 1 < len(partes) else ""
        questoes[num] = limpar_ruido(corpo)
    return questoes


# ---------- SEPARAÇÃO ENUNCIADO ↔ ALTERNATIVAS ----------

# Marca de alternativa: letra A-E no início de linha, opcionalmente seguida por
# espaço ou newline (cobre o caso "letra+corpo separados") e depois texto.
# Negative lookahead evita pegar A) ou A. de citações dentro do enunciado.
ALT_PATTERN = re.compile(
    r"(?m)^\s*([A-E])(?:\s+|\n+)(.+?)(?=^\s*[A-E](?:\s+|\n+)|\Z)",
    re.DOTALL,
)


def separar_enunciado_alternativas(corpo: str) -> tuple[str, dict[str, str]]:
    """
    Acha a posição da primeira alternativa 'A' válida e divide.
    'Válida' = primeira ocorrência de 'A' no começo de linha seguida por
    pelo menos uma sequência B, C, D, E também no começo de linha em até
    ~3000 chars (sanity check).
    """
    # heurística: procura o bloco com 5 marcas A..E em ordem
    matches = list(ALT_PATTERN.finditer(corpo))
    if len(matches) < 5:
        return corpo, {}

    # encontra sequência consecutiva A,B,C,D,E
    for i in range(len(matches) - 4):
        seq = [matches[i + k].group(1) for k in range(5)]
        if seq == ["A", "B", "C", "D", "E"]:
            inicio_alts = matches[i].start()
            enunciado = corpo[:inicio_alts].strip()
            alternativas = {}
            for k in range(5):
                letra = matches[i + k].group(1)
                bruto = matches[i + k].group(2)
                if letra == "E":
                    bruto = _truncar_ultima_alt(bruto)  # corta ANTES de colapsar \n
                alternativas[letra] = _limpar_texto_alt(bruto)
            return enunciado, alternativas

    return corpo, {}


SECAO_RUIDO = re.compile(
    r"\s*(CIÊNCIAS\s+DA\s+NATUREZA|CIÊNCIAS\s+HUMANAS|LINGUAGENS|MATEMÁTICA"
    r"|Questões\s+de\s+\d+\s+a\s+\d+)"
    r"(\s+E\s+SUAS\s+TECNOLOGIAS)?\s*$",
    re.IGNORECASE,
)


def _limpar_texto_alt(t: str) -> str:
    """Normaliza alternativa: une linhas internas, remove rodapé residual."""
    t = limpar_ruido(t)
    t = re.sub(r"\s+", " ", t)  # une quebras internas
    t = SECAO_RUIDO.sub("", t)  # remove cabeçalho de seção que vazou
    return t.strip()


# Atribuição em CAIXA ALTA no início de linha ("PEPE ESCOBAR." ou "ARENDT,") —
# indica que o que vem depois é fonte/citação, não parte da alternativa E.
ATRIBUICAO = re.compile(
    r"\n\s*[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{3,}(?:\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,})*[,\.]"
)


FIM_SECAO_CH = re.compile(
    r"\n\s*(INSTRUÇÕES\s+PARA\s+A\s+REDAÇÃO|PROPOSTA\s+DE\s+REDAÇÃO"
    r"|REDAÇÃO\s*\n|TEXTO\s+[IVX]+\s*\n.*?INSTRUÇÕES)",
    re.IGNORECASE | re.DOTALL,
)


def _truncar_ultima_alt(texto: str, max_chars: int = 600) -> str:
    """Corta a cauda da alternativa E: fim de seção CH, atribuição ou cap de chars."""
    m_secao = FIM_SECAO_CH.search(texto)
    if m_secao:
        texto = texto[:m_secao.start()]
    m_atrib = ATRIBUICAO.search(texto)
    if m_atrib:
        texto = texto[:m_atrib.start()]
    if len(texto) > max_chars:
        texto = texto[:max_chars]
    return texto.strip()


# ---------- FONTES CITADAS (heurística) ----------

FONTE_HINTS = [
    (r"Disponível em[^.]+", "link"),
    (r"Adaptado\.?", "adaptação"),
    (r"\bMAPA\b", "mapa"),
    (r"\bTABELA\b|\bQuadro\b", "tabela"),
    (r"\bGRÁFICO\b", "gráfico"),
    (r"\bFigura\b|\bImagem\b|\bFoto\b", "imagem"),
    (r"\bCharge\b|\bCartum\b", "charge"),
]


def detectar_fontes(enunciado: str) -> list[str]:
    """Heurística leve: identifica indícios de fontes/recursos visuais."""
    achados = []
    for pat, nome in FONTE_HINTS:
        if re.search(pat, enunciado, re.IGNORECASE):
            achados.append(nome)
    # detecta atribuições "AUTOR, X. Y." no fim de citações
    if re.search(r"[A-Z][A-Z]+,\s+[A-Z]\.", enunciado):
        achados.append("texto citado")
    return list(set(achados))


# ---------- PARSER DE GABARITO ----------

def parse_gabarito(pdf_gab: Path, caderno: str = "azul") -> dict[int, str]:
    """
    Captura PARES (numero, letra) em qualquer posição da linha.
    Layouts cobertos:
      - 1 par por linha (2009)
      - 2+ pares por linha lado-a-lado (CH | CN, 2014+)
    Estratégia: regex global por linha, pega TODOS os pares.
    Sanity: número ∈ [1, 180], primeira letra após o número (caderno azul costuma
    ser a primeira coluna; se algum ano divergir, isolar).
    """
    r = subprocess.run(
        ["pdftotext", "-layout", str(pdf_gab), "-"],
        capture_output=True, text=True, check=True,
    )
    gab = {}
    par_pattern = re.compile(r"\b(\d{1,3})\s+([A-E])\b")

    for linha in r.stdout.splitlines():
        for m in par_pattern.finditer(linha):
            num, letra = int(m.group(1)), m.group(2)
            if 1 <= num <= 180 and num not in gab:
                gab[num] = letra
    return gab


# ---------- FILTRO POR ÁREA ----------

def detectar_dia(pdf_path: Path) -> int | None:
    """Dia indicado no nome do arquivo (D1/D2, dia1/dia2, sábado/domingo); None se o nome não disser."""
    norm = re.sub(r"[_\-\s]+", "", pdf_path.name.lower())
    norm = norm.replace("á", "a")
    # "(?<!c)d1": o "d1" de "cd1" é caderno 1, não dia 1.
    if re.search(r"(?<!c)d1(?!\d)|dia1|sabado", norm):
        return 1
    if re.search(r"(?<!c)d2(?!\d)|dia2|domingo", norm):
        return 2
    return None


def intervalo_da_area(area: str, ano: int, pdf_path: Path) -> tuple[int, int]:
    """Faixa de questões da área naquele ano (config/areas.yaml); avisa se o PDF parecer de outro dia."""
    f = areas.faixa(area, ano)
    dia_pdf = detectar_dia(pdf_path)
    if dia_pdf is not None and dia_pdf != f.dia:
        print(f"  ⚠ {area} em {ano} é prova do dia {f.dia}, mas o nome do PDF indica dia {dia_pdf}")
    return f.q_min, f.q_max


# ---------- ESCRITA DO CSV ----------

CSV_COLS = ["id", "ano", "caderno", "area", "numero", "enunciado",
            "fontes_citadas", "alternativas", "gabarito"]


def carregar_ids_existentes() -> set:
    if not RAW_CSV.exists():
        return set()
    return set(pd.read_csv(RAW_CSV, usecols=["id"])["id"].tolist())


def gravar_linhas(linhas: list[dict]):
    df = pd.DataFrame(linhas, columns=CSV_COLS)
    header = not RAW_CSV.exists()
    df.to_csv(RAW_CSV, mode="a", header=header, index=False)


# ---------- ORQUESTRAÇÃO ----------

def detectar_ano(pdf_path: Path) -> int:
    m = re.search(r"(20\d{2})", str(pdf_path))
    if not m:
        raise ValueError(f"Não consegui detectar ano em {pdf_path}")
    return int(m.group(1))


def detectar_caderno(pdf_path: Path) -> str:
    nome = pdf_path.name.lower()
    for cor in ["azul", "amarela", "amarelo", "branco", "branca", "rosa"]:
        if cor in nome:
            return cor.rstrip("oa")
    # default
    return "azul"


def localizar_gabarito(pdf_prova: Path, override: Path | None, dia: int = 1) -> Path:
    if override:
        return override

    parent = pdf_prova.parent
    candidatos = [p for p in parent.glob("*.pdf") if p != pdf_prova]
    if not candidatos:
        raise FileNotFoundError(f"Nenhum PDF além da prova em {parent}")

    def score(p: Path) -> int:
        nome = p.name.lower()
        norm = re.sub(r"[_\-\s]+", "", nome)
        norm = norm.replace("á", "a").replace("é", "e")
        s = 0
        if "gabarito" in norm: s += 10
        if "gab" in norm: s += 5
        # NOVO: GB como abreviação de gabarito (2021_GB_impresso...)
        eh_gb = bool(re.search(r"\bgb\b|gb_|_gb|gbimpresso", nome))
        if eh_gb: s += 8
        if detectar_dia(p) == dia: s += 8
        if ("sabado" if dia == 1 else "domingo") in norm: s += 4
        if detectar_dia(p) == 3 - dia: s -= 8
        if "azul" in norm: s += 3
        if "prova" in norm: s -= 8
        # MODIFICADO: 'impresso' só penaliza se NÃO houver sinal de gabarito
        tem_sinal_gab = "gabarito" in norm or "gab" in norm or eh_gb
        if "impresso" in norm and not tem_sinal_gab: s -= 5
        if "caderno" in norm and not tem_sinal_gab: s -= 3
        if p.stat().st_size < 500_000: s += 3
        return s

    ranked = sorted(candidatos, key=score, reverse=True)
    melhor = ranked[0]
    if score(melhor) < 5:
        raise FileNotFoundError(
            f"Nenhum gabarito provável em {parent}.\n"
            f"PDFs disponíveis: {[p.name for p in candidatos]}\n"
            f"Melhor candidato: {melhor.name} (score={score(melhor)})\n"
            f"Use --gabarito."
        )
    return melhor


def processar(pdf_prova: Path, pdf_gab: Path | None = None, area: str = "CH"):
    ano = detectar_ano(pdf_prova)
    caderno = detectar_caderno(pdf_prova)
    faixa = areas.faixa(area, ano)
    gab_path = localizar_gabarito(pdf_prova, pdf_gab, dia=faixa.dia)

    print(f"[{pdf_prova.name}] ano={ano} caderno={caderno} área={area} (dia {faixa.dia})")
    print(f"  gabarito: {gab_path.name}")

    # 1. extrai texto ordenado
    texto = extrair_texto_ordenado(pdf_prova)
    questoes_brutas = fatiar_questoes(texto)
    print(f"  questões brutas: {len(questoes_brutas)} ({min(questoes_brutas)}-{max(questoes_brutas)})")

    # 2. gabarito
    gabaritos = parse_gabarito(gab_path)
    print(f"  gabaritos parseados: {len(gabaritos)}")

    # 3. filtro da área (config/areas.yaml)
    q_min, q_max = intervalo_da_area(area, ano, pdf_prova)
    print(f"  intervalo {area}: {q_min}-{q_max}")

    # 4. processa cada questão da área
    ids_existentes = carregar_ids_existentes()
    linhas = []
    falhas = []

    for num in sorted(questoes_brutas):
        if not (q_min <= num <= q_max):
            continue
        qid = f"{ano}_{area}_{num:03d}"
        if qid in ids_existentes:
            continue

        corpo = questoes_brutas[num]
        enunciado, alts = separar_enunciado_alternativas(corpo)

        if len(alts) != 5:
            falhas.append((num, f"alternativas={len(alts)}"))
            continue

        fontes = detectar_fontes(enunciado)
        gab = gabaritos.get(num, "")

        linhas.append({
            "id": qid,
            "ano": ano,
            "caderno": caderno,
            "area": area,
            "numero": num,
            "enunciado": enunciado,
            "fontes_citadas": json.dumps(fontes, ensure_ascii=False),
            "alternativas": json.dumps(alts, ensure_ascii=False),
            "gabarito": gab,
        })

    if linhas:
        gravar_linhas(linhas)

    print(f"  ✓ gravadas: {len(linhas)}")
    if falhas:
        print(f"  ⚠ falhas ({len(falhas)}):")
        for num, motivo in falhas:
            print(f"    Q{num}: {motivo}")

    # validação rápida
    sem_gab = [l["numero"] for l in linhas if not l["gabarito"]]
    if sem_gab:
        print(f"  ⚠ sem gabarito: {sem_gab}")


# ---------- CLI ----------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("prova", type=Path, help="PDF da prova (caderno regular)")
    p.add_argument("--gabarito", type=Path, help="PDF do gabarito (opcional)")
    p.add_argument("--area", default="CH", choices=areas.siglas(),
                   help="área a extrair; dia e faixa de questões vêm de config/areas.yaml (padrão: CH)")
    args = p.parse_args()

    if not args.prova.exists():
        print(f"ERRO: prova não encontrada: {args.prova}", file=sys.stderr)
        sys.exit(1)

    processar(args.prova, args.gabarito, area=args.area)


if __name__ == "__main__":
    main()
