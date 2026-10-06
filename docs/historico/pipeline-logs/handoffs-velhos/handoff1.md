# O que o diagnóstico muda

**LLM-com-visão é desnecessária para texto.** Tudo é vetorial nativo. Gemini fica reservado para (a) descrever figuras quando a questão pedir leitura visual, (b) classificação pedagógica (pass 2). Economia: ~80% do custo previsto.

**Recorte real disponível.** Cruzando com seu `ls`:
- Tem: 2014, 2015, 2016, 2017, 2018, **2023(?)** — 6 anos
- Falta: 2019, 2020, 2021, 2022, 2024 — 5 anos
- **Bandeira vermelha**: `2023/dia1_caderno1_azul.pdf` tem marca d'água `*AZUL75SAB3*` que bate com 2013/2014. Pode ser 2013 mal rotulado. **Confere antes de processar** (abra o PDF e veja se a página de rosto diz 2013 ou 2023).

**Provas antigas (2004-2008) ficam fora** — matriz pré-2009, delimitador `N.` ambíguo, e você já tinha cortado o recorte em 2014.

# Nova arquitetura

```
Pass 1 (LOCAL, ZERO LLM):
  pdfplumber → extrai texto por bbox → reordena 2 colunas → fatia por "QUESTÃO N"
  pdftotext -layout gabarito.pdf → regex → dict {n: letra}
  pdfimages → extrai JPEGs com bbox → associa à questão por proximidade vertical
  Output: questoes_raw.csv + pasta de imagens/

Pass 2 (LLM, seletivo):
  (a) Questões cuja extração de texto inclui token "[IMAGEM]" → Gemini descreve a figura
  (b) Classificação tema/competência/tipo cognitivo → Gemini OU Claude
```

Custo total estimado: **<$2** para o corpus completo. Local-first, reproducível, sem dependência de rede para o miolo.

# POC antes de escrever pipeline completo

Antes de eu te entregar 200 linhas de novo, vale testar a parte difícil — **reordenação de 2 colunas** — em 1 prova só. Se isso funciona, o resto é boilerplate. Cola pro Claude Code:

---

**POC: extração de uma prova ENEM moderna sem LLM. Objetivo: validar que conseguimos fatiar uma prova em questões com texto limpo e ordem correta.**

```bash
pip install pdfplumber
```

**Script: `poc_extracao.py`**

```python
"""
POC de extração de prova ENEM (matriz nova, 2 colunas).
Roda em 1 arquivo, mostra primeiras 3 questões na ordem correta.
"""
import sys
import re
import pdfplumber
from pathlib import Path

PDF = Path(sys.argv[1])  # ex: ./2018/dia1_caderno1_azul.pdf

questoes = []  # lista de (numero, texto)

with pdfplumber.open(PDF) as pdf:
    for page in pdf.pages:
        # divide a página ao meio (provas ENEM têm 2 colunas simétricas)
        meio = page.width / 2
        col_esq = page.crop((0, 0, meio, page.height))
        col_dir = page.crop((meio, 0, page.width, page.height))

        for col in (col_esq, col_dir):
            texto = col.extract_text() or ""
            # fatia por "QUESTÃO N"
            partes = re.split(r"(QUESTÃO\s+\d+)", texto)
            for i in range(1, len(partes), 2):
                cabecalho = partes[i]
                corpo = partes[i + 1] if i + 1 < len(partes) else ""
                num = int(re.search(r"\d+", cabecalho).group())
                questoes.append((num, corpo.strip()))

# ordena por número e remove duplicatas
questoes_unicas = dict(questoes)  # último wins em duplicata
print(f"Total questões: {len(questoes_unicas)}")
print(f"Numeração: {min(questoes_unicas)} a {max(questoes_unicas)}")
print(f"Faltando: {sorted(set(range(min(questoes_unicas), max(questoes_unicas)+1)) - set(questoes_unicas))}")

print("\n--- QUESTÃO 1 ---")
print(questoes_unicas.get(1, "[NÃO ENCONTRADA]")[:500])
print("\n--- QUESTÃO 2 ---")
print(questoes_unicas.get(2, "[NÃO ENCONTRADA]")[:500])
print("\n--- QUESTÃO 3 ---")
print(questoes_unicas.get(3, "[NÃO ENCONTRADA]")[:500])
```

**Rodar:**
```bash
python poc_extracao.py 2018/dia1_caderno1_azul.pdf
```

**Critério de sucesso:**
1. Total de questões = 90 (ENEM dia 1)
2. Numeração contínua, sem buracos
3. Cada questão mostrada termina com 5 alternativas (A-E) ou linha sobre "(A)... (B)..."
4. Nada de questão começando no meio de outra

**Critério de falha:**
- Duplicatas/buracos na numeração → a divisão por meio da página tá errada (talvez colunas não simétricas)
- Texto de uma questão invadindo outra → regex `QUESTÃO\s+\d+` pega referências cruzadas
- Alternativas perdidas → corte por coluna cortou alternativas que ficam embaixo

**Cola aqui:**
1. A saída do script
2. Se falhou: qual critério falhou e amostra do que veio errado

Não tenta consertar nada, só reporta.

---


Recorte ativo: **2013, 2014, 2015, 2016, 2017, 2018** (6 anos, todos matriz nova).

Roda a POC em `2014/dia1...azul.pdf` — é o ano que o diagnóstico já validou com 90 questões. 
