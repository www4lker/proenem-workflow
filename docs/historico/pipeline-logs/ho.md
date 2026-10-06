# Diagnóstico

Dois problemas pequenos, isolados:

1. **Calha global é cega para variação por página.** O `min=max=319` confirma que a detecção sempre retornou o mesmo valor — porque a janela de busca era estreita (±60) e a função reduziu pra densidade ao redor de 319. Na página de abertura, a coluna esquerda se estende além de 319 porque a calha **real** dessa página é mais à direita. Solução: detectar **por página**, com janela larger, procurando o **maior gap entre palavras** (não menor densidade).

2. **`tol_linha=3` separa letra da alternativa do corpo.** Letra em top=534, corpo em top=536-537 cai em buckets `534` e `537` (diferentes). Com `tol_linha=6`, ambos viram bucket `534`. Resolvido.

# Handoff para Claude Code

---

**POC v3: calha por página via maior gap. Substitui `poc_extracao.py`.**

```python
"""
POC v3 — calha detectada por página pelo maior gap entre palavras na janela
central. Resolve truncamento residual em páginas de abertura de seção.
"""
import sys, re
import pdfplumber
from collections import Counter
from pathlib import Path

PDF = Path(sys.argv[1])

def detectar_calha(page, busca_margem=120):
    """
    Maior gap entre centros de palavras numa janela ao redor do meio da página.
    Retorna o x do meio desse gap.
    """
    palavras = page.extract_words()
    meio = page.width / 2
    if not palavras:
        return meio
    centros = sorted(
        (w['x0'] + w['x1']) / 2 for w in palavras
        if meio - busca_margem < (w['x0'] + w['x1']) / 2 < meio + busca_margem
    )
    if not centros:
        return meio
    pontos = [meio - busca_margem] + centros + [meio + busca_margem]
    melhor_gap, melhor_centro = 0, meio
    for i in range(len(pontos) - 1):
        gap = pontos[i+1] - pontos[i]
        if gap > melhor_gap:
            melhor_gap = gap
            melhor_centro = (pontos[i] + pontos[i+1]) / 2
    return melhor_centro

def reconstruir_texto(palavras, tol_linha=6):
    if not palavras:
        return ""
    linhas = {}
    for w in palavras:
        chave = round(w['top'] / tol_linha) * tol_linha
        linhas.setdefault(chave, []).append(w)
    saida = []
    for top in sorted(linhas):
        words_ord = sorted(linhas[top], key=lambda w: w['x0'])
        saida.append(' '.join(w['text'] for w in words_ord))
    return '\n'.join(saida)

questoes = []
calhas_por_pagina = []

with pdfplumber.open(PDF) as pdf:
    for idx, page in enumerate(pdf.pages, 1):
        calha = detectar_calha(page)
        calhas_por_pagina.append((idx, round(calha, 1)))
        palavras = page.extract_words()
        col_esq = [w for w in palavras if (w['x0'] + w['x1']) / 2 < calha]
        col_dir = [w for w in palavras if (w['x0'] + w['x1']) / 2 >= calha]
        for words in (col_esq, col_dir):
            texto = reconstruir_texto(words)
            partes = re.split(r"(QUESTÃO\s+\d+)", texto)
            for i in range(1, len(partes), 2):
                num = int(re.search(r"\d+", partes[i]).group())
                corpo = partes[i + 1].strip() if i + 1 < len(partes) else ""
                questoes.append((num, corpo))

questoes_unicas = dict(questoes)
print(f"Calhas por página: {calhas_por_pagina}")
print(f"Distribuição: {Counter(c for _, c in calhas_por_pagina).most_common()}")
print(f"\nTotal questões: {len(questoes_unicas)}")
print(f"Numeração: {min(questoes_unicas)} a {max(questoes_unicas)}")
faltando = sorted(set(range(min(questoes_unicas), max(questoes_unicas)+1)) - set(questoes_unicas))
print(f"Faltando: {faltando}")

# amostra incluindo a Q1 problemática e questões aleatórias
for n in (1, 2, 3, 23, 45, 67, 89, 90):
    print(f"\n--- QUESTÃO {n} ---")
    print(questoes_unicas.get(n, "[NÃO ENCONTRADA]")[:800])
```

**Rodar:**
```bash
python poc_extracao.py 2014/dia1_caderno1_azul.pdf
```

**Critérios:**
1. Total = 90, sem buracos
2. **Q1 alternativas C/D/E completas** (`distintos.`, `norte do país.`, `território nacional.`)
3. **Letra e corpo da alternativa na mesma linha** (`A permitiria...` e não `A` numa linha e `permitiria...` em outra)
4. Calhas por página: variação esperada — algumas páginas em ~319, outras (abertura de seção) em valor diferente
5. Sem regressão nas questões já íntegras (Q2, Q3, Q45, Q90)

**Reportar:**
- Saída completa (especialmente Q1 inteira)
- Distribuição de calhas (quantas páginas em cada valor)
- Se Q1 ainda truncada: ver se a calha dessa página específica mudou ou continuou em 319

Não conserta — só reporta.

---

Se v3 fechar, escalamos: script processa as 6 provas, gera `questoes_raw.csv`, parser de gabarito, cruzamento. Se v3 falhar de novo, mudamos de biblioteca (PyMuPDF tem extração por blocos que já agrupa 2 colunas automaticamente — última cartada se pdfplumber não der).
