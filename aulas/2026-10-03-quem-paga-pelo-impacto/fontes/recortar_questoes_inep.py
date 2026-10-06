#!/usr/bin/env python3
"""Recorta do PDF oficial (caderno 1 azul, 1º dia) a imagem de cada questão selecionada.

Somente leitura no PROENEM: lê os PDFs de `pipeline` e grava PNG em
`fontes/provas-recortes/`. Uso: `python3 recortar_questoes_inep.py [id ...]` (sem ids, todas as
que estão em `enem-25-selecionadas.md`).

Os cadernos de 2013 trazem o gabarito como anotação (círculo verde); `-hide-annotations` a tira.
Método: `pdftotext -bbox-layout` acha o título "QUESTÃO nn" e a coluna (a prova tem duas). O recorte
vai do título até o próximo título na ordem de leitura (coluna esquerda, direita, página seguinte),
e os pedaços são empilhados. Cabeçalho e rodapé da página ficam de fora por margens fixas.
A conferência final é visual: abrir o PNG.
"""
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image

from conferir_candidatas_inep import ARQUIVOS, RAIZ

AQUI = Path(__file__).resolve().parent
SAIDA = AQUI / "provas-recortes"
DPI = 150
MARGEM_TOPO = 58     # pontos: abaixo do cabeçalho corrente da página
MARGEM_BASE = 44     # pontos: acima do rodapé
BORDA_ESQ = 50       # pontos: fora da orelha escura do canto
BORDA_DIR = 25
CALHA = 2            # meia largura da faixa central (a calha real vai de mid-6 a mid+6)
FOLGA = 4


def palavras_por_pagina(pdf):
    xml = subprocess.run(["pdftotext", "-bbox-layout", str(RAIZ / pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    paginas = []
    for bloco in xml.split("<page ")[1:]:
        larg, alt = (float(v) for v in re.match(r'width="([\d.]+)" height="([\d.]+)"', bloco).groups())
        palavras = [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in
                    re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', bloco)]
        paginas.append((larg, alt, palavras))
    return paginas


def base_util(pagina):
    """Y onde termina o miolo da página: logo acima do rodapé 'CH - 1º dia | Caderno 1 - AZUL - Página n'."""
    _, alt, palavras = pagina
    rodape = [y for x, y, _, _, w in palavras if w == "Caderno" and y > alt * 0.85]
    return min(rodape) - 3 if rodape else alt - MARGEM_BASE


def titulos(paginas):
    """{numero: (pagina, coluna, y)} para cada 'QUESTÃO nn' (palavra em maiúsculas + número)."""
    achados = {}
    for p, (larg, _, palavras) in enumerate(paginas):
        for i, (x0, y0, _, _, t) in enumerate(palavras[:-1]):
            if t.upper() in ("QUESTÃO", "QUESTAO") and t[0].isupper():
                m = re.fullmatch(r"0*(\d{1,3})", palavras[i + 1][4])
                if m and abs(palavras[i + 1][1] - y0) < 4:
                    achados.setdefault(int(m.group(1)), (p, 0 if x0 < larg / 2 else 1, y0))
    return achados


def eh_larga(paginas, tits, numero):
    """A questão ocupa a largura toda? (há palavras na calha entre as colunas, abaixo do título)."""
    p, c, y0 = tits[numero]
    larg, alt, palavras = paginas[p]
    if c == 1:
        return False
    fim = min([y for n, (pp, cc, y) in tits.items() if pp == p and cc == 0 and y > y0] + [base_util(paginas[p])])
    meio = larg / 2
    return any(y0 <= ya < fim and xa < meio + CALHA and xb > meio - CALHA and xb - xa < 200
               for xa, ya, xb, yb, _ in palavras)


def segmentos(paginas, tits, numero):
    """Lista de (pagina, coluna, y_ini, y_fim) da questão; coluna 2 = largura toda."""
    p0, c0, y0 = tits[numero]
    if eh_larga(paginas, tits, numero):
        fim = min([y for n, (pp, cc, y) in tits.items() if pp == p0 and y > y0 and n != numero]
                  + [base_util(paginas[p0])])
        return [(p0, 2, y0 - FOLGA, fim - FOLGA if fim < base_util(paginas[p0]) else fim)]
    ordem = sorted(tits.items(), key=lambda kv: (kv[1][0], kv[1][1], kv[1][2]))
    chaves = [n for n, _ in ordem]
    idx = chaves.index(numero)
    prox = ordem[idx + 1][1] if idx + 1 < len(ordem) else None
    segs, p, c, y = [], p0, c0, y0 - FOLGA
    while True:
        alt = paginas[p][1]
        if prox and (p, c) == (prox[0], prox[1]):
            if prox[2] - FOLGA - y > 30:  # sem sobra do cabeçalho da página quando o título vem no topo
                segs.append((p, c, y, prox[2] - FOLGA))
            return segs
        segs.append((p, c, y, base_util(paginas[p])))
        if prox is None and p >= len(paginas) - 1 and c == 1:
            return segs
        p, c, y = (p, 1, MARGEM_TOPO) if c == 0 else (p + 1, 0, MARGEM_TOPO)
        if prox and (p, c) > (prox[0], prox[1]):
            return segs


def rasterizar(pdf, pagina, coluna, y0, y1, larg, tmp):
    esc = DPI / 72
    meio = larg / 2
    x0, x1 = {0: (BORDA_ESQ, meio - CALHA), 1: (meio + CALHA, larg - BORDA_DIR),
              2: (BORDA_ESQ, larg - BORDA_DIR)}[coluna]
    arq = tmp / f"seg_{pagina}_{coluna}_{int(y0)}"
    subprocess.run(["pdftoppm", "-png", "-hide-annotations", "-r", str(DPI), "-f", str(pagina + 1), "-l", str(pagina + 1),
                    "-x", str(int(x0 * esc)), "-y", str(int(y0 * esc)),
                    "-W", str(int((x1 - x0) * esc)), "-H", str(int((y1 - y0) * esc)),
                    "-singlefile", str(RAIZ / pdf), str(arq)], check=True)
    return Image.open(str(arq) + ".png")


def aparar(img):
    """Altura até o fim do conteúdo: para no primeiro vazio de 120 px ou mais (sobra do fim da coluna)."""
    cinza = img.convert("L")
    ultimo, vazio = 0, 0
    for y in range(cinza.height):
        if cinza.crop((0, y, cinza.width, y + 1)).getextrema()[0] < 200:
            ultimo, vazio = y, 0
        else:
            vazio += 1
            if vazio >= 120 and ultimo:
                break
    return min(cinza.height, ultimo + 12)


def recortar(id_questao, cache, tmp):
    ano, _, num = id_questao.split("_")
    pdf = ARQUIVOS[ano][0]
    if pdf not in cache:
        pag = palavras_por_pagina(pdf)
        cache[pdf] = (pag, titulos(pag))
    paginas, tits = cache[pdf]
    numero = int(num)  # até 2016 o número do corpus é o oficial
    if numero not in tits:
        return None
    imgs = [rasterizar(pdf, p, c, a, b, paginas[p][0], tmp) for p, c, a, b in segmentos(paginas, tits, numero)]
    larg = max(i.width for i in imgs)
    final = Image.new("RGB", (larg, sum(i.height for i in imgs)), "white")
    y = 0
    for i in imgs:
        final.paste(i, (0, y))
        y += i.height
    final = final.crop((0, 0, larg, aparar(final)))
    destino = SAIDA / f"{id_questao}.png"
    final.save(destino)
    return destino, len(imgs)


def ids_selecionados():
    texto = (AQUI / "enem-25-selecionadas.md").read_text(encoding="utf-8")
    return re.findall(r"\|\s*(20\d\d_CH_\d{3})\s*\|", texto)


def main():
    import tempfile
    SAIDA.mkdir(exist_ok=True)
    ids = sys.argv[1:] or ids_selecionados()
    cache = {}
    with tempfile.TemporaryDirectory() as t:
        for i in ids:
            r = recortar(i, cache, Path(t))
            print(i, "não achei o título" if r is None else f"{r[0].name} ({r[1]} trecho(s))")


if __name__ == "__main__":
    main()
