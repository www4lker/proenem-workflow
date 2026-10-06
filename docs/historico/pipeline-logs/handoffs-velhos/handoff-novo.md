
# Handoff para Claude Code

---

**POC v2: extração com detecção de calha. Substitui `poc_extracao.py`.**

```python
"""
POC v2 — corrige truncamento horizontal detectando a calha real entre colunas.
"""
import sys, re
import pdfplumber
from collections import Counter
from pathlib import Path

PDF = Path(sys.argv[1])

def detectar_calha(page, margem=60, bucket=5):
    """
    Encontra o x da calha entre 2 colunas pela densidade de palavras.
    Busca o 'vale' (menor densidade) numa janela ao redor do centro.
    """
    palavras = page.extract_words()
    if not palavras:
        return page.width / 2
    centros = [int(((w['x0'] + w['x1']) / 2) / bucket) * bucket for w in palavras]
    contagem = Counter(centros)
    meio = page.width / 2
    candidatos = [
        (x, contagem.get(x, 0))
        for x in range(int(meio - margem), int(meio + margem) + 1, bucket)
    ]
    return min(candidatos, key=lambda c: (c[1], abs(c[0] - meio)))[0]

def reconstruir_texto(palavras, tol_linha=3):
    """
    Agrupa palavras por linha visual (top arredondado com tolerância)
    e ordena por x dentro da linha.
    """
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
calhas_detectadas = []

with pdfplumber.open(PDF) as pdf:
    for page in pdf.pages:
        calha = detectar_calha(page)
        calhas_detectadas.append(calha)
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
print(f"Calha detectada: min={min(calhas_detectadas)}, "
      f"max={max(calhas_detectadas)}, "
      f"moda={Counter(calhas_detectadas).most_common(1)[0][0]}")
print(f"Total questões: {len(questoes_unicas)}")
print(f"Numeração: {min(questoes_unicas)} a {max(questoes_unicas)}")
faltando = sorted(set(range(min(questoes_unicas), max(questoes_unicas)+1)) - set(questoes_unicas))
print(f"Faltando: {faltando}")

for n in (1, 2, 3, 45, 90):  # amostra incluindo meio e fim
    print(f"\n--- QUESTÃO {n} ---")
    print(questoes_unicas.get(n, "[NÃO ENCONTRADA]")[:600])
```

**Rodar:**
```bash
python poc_extracao.py 2014/dia1_caderno1_azul.pdf
```

**Critérios:**
1. Total = 90, sem buracos (mantém o que já funcionou)
2. **Palavras inteiras** nas alternativas — sem `red`, `indíge`, `terr` cortados
3. Calha detectada estável entre páginas (min/max próximos da moda; se variar muito, reportar)
4. Questão 45 (meio do corpus) e Questão 90 (fim) extraídas inteiras

**Reportar:**
- Saída completa
- Se palavras ainda truncadas: amostra de 3 trechos com x da calha por página
- Se questão sumiu/duplicou: número e contexto

Não conserta — só reporta.

