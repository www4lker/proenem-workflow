# Handoff — Pipeline ENEM CH para ProEnem 2026

Briefing consolidado para o Claude Code rodando em `pipeline`.
Walker (professor) está usando claude.ai como orquestrador e cola estes handoffs
aqui. Não chame APIs externas sem instrução explícita.

---

## Contexto

Walker dará 3 aulas no ProEnem 2026 (cursinho popular, volunteer):
- **04/07/26** — Interdisciplinar CH (recorte: Geopolítica/Ordem Mundial)
- **03/10/26** — Geografia e Natureza
- **10/10/26** — Sociologia e Filosofia (interdisciplinar)

Objetivo deste projeto: construir corpus estruturado de questões ENEM CH
2013-2018 para alimentar planejamento das aulas. Risco nomeado: armadilha C3
(perfeccionismo paralisante). Pipeline existe para servir aula, não vice-versa.

---

## Decisões fechadas

| Item | Valor |
|------|-------|
| Recorte | CH, 2013-2018 (6 anos, matriz nova) |
| Anos a baixar depois | 2019-2022, 2024 (não bloqueia início) |
| Caderno padrão | Azul |
| Pasta `210/` | = ENEM 2010 (fora do recorte) |
| Pasta `211/` | = ENEM 2011 (fora do recorte) |
| Pasta `2023/` | Conteúdo é 2013 — Walker vai renomear |
| Provas 2004-2008 | Fora (matriz antiga, delimitador inseguro) |
| Foco temático aula 04/07 | Geopolítica + Ordem Mundial |
| Foco aulas 03/10 e 10/10 | Tema dado pela ementa, não força Geopol/Pop |

---

## Diagnóstico técnico (já feito)

- Todos PDFs são **TEXTO_NATIVO** (vetorial, fontes embarcadas).
- LLM com visão **não é necessária** para extrair texto.
- Provas modernas: 32p, 2 colunas, delimitador `QUESTÃO N` (90 ocorrências exatas).
- Gabaritos: tabela extraível com `pdftotext -layout` + regex `^\s*\d{1,3}\s+[A-E]`.
- Imagens vêm como JPEGs separados por questão (não bitmap de página inteira).

---

## Arquitetura

```
Pass 1 — LOCAL, ZERO LLM:
  pdfplumber → corta página em 2 colunas → extrai texto → fatia por "QUESTÃO N"
  pdftotext -layout gabarito.pdf → regex → dict {n: letra}
  pdfimages → JPEGs com bbox → associa à questão por proximidade vertical
  Output: corpus_enem/questoes_raw.csv + corpus_enem/imagens/

Pass 2 — LLM, seletivo (só quando Pass 1 estiver validado):
  (a) Questões com figura → Gemini descreve a imagem
  (b) Classificação tema/competência/tipo cognitivo → Gemini ou Claude
  Output: corpus_enem/questoes_ch.csv
```

Schema da tabela final:

```
id              # ex: 2018_CH_023
ano             # 2018
caderno         # azul
area            # CH
numero          # 23
enunciado       # texto
fontes_citadas  # JSON list
alternativas    # JSON dict {A:..., B:..., ...}
gabarito        # letra
disciplina_principal   # geografia | história | sociologia | filosofia
disciplinas_secundarias # JSON list
tema_principal  # "geopolítica > blocos econômicos"
tema_secundario # opcional
tipo_cognitivo  # recuperação | aplicação | análise | síntese
competencia     # 1-6 (Matriz CH 2009)
habilidade      # H1-H30
```

---

## Estado atual e próximo passo

**Aguardando:** saída da POC abaixo rodada em `2014/dia1...azul.pdf`.

```bash
pip install pdfplumber
```

**Script: `poc_extracao.py`**

```python
"""
POC de extração de prova ENEM (matriz nova, 2 colunas).
Roda em 1 arquivo, mostra primeiras 3 questões na ordem correta.
"""
import sys, re
import pdfplumber
from pathlib import Path

PDF = Path(sys.argv[1])

questoes = []

with pdfplumber.open(PDF) as pdf:
    for page in pdf.pages:
        meio = page.width / 2
        col_esq = page.crop((0, 0, meio, page.height))
        col_dir = page.crop((meio, 0, page.width, page.height))

        for col in (col_esq, col_dir):
            texto = col.extract_text() or ""
            partes = re.split(r"(QUESTÃO\s+\d+)", texto)
            for i in range(1, len(partes), 2):
                cabecalho = partes[i]
                corpo = partes[i + 1] if i + 1 < len(partes) else ""
                num = int(re.search(r"\d+", cabecalho).group())
                questoes.append((num, corpo.strip()))

questoes_unicas = dict(questoes)
print(f"Total questões: {len(questoes_unicas)}")
print(f"Numeração: {min(questoes_unicas)} a {max(questoes_unicas)}")
faltando = sorted(set(range(min(questoes_unicas), max(questoes_unicas)+1)) - set(questoes_unicas))
print(f"Faltando: {faltando}")

print("\n--- QUESTÃO 1 ---")
print(questoes_unicas.get(1, "[NÃO ENCONTRADA]")[:500])
print("\n--- QUESTÃO 2 ---")
print(questoes_unicas.get(2, "[NÃO ENCONTRADA]")[:500])
print("\n--- QUESTÃO 3 ---")
print(questoes_unicas.get(3, "[NÃO ENCONTRADA]")[:500])
```

**Rodar:**
```bash
python poc_extracao.py 2014/dia1_caderno1_azul.pdf
```

**Critérios de sucesso:**
1. Total = 90 questões
2. Numeração contínua sem buracos
3. Cada questão termina com 5 alternativas (A-E)
4. Sem questão começando no meio de outra

**Critérios de falha (reportar qual):**
- Duplicatas/buracos → divisão de colunas errada
- Texto de uma questão invadindo outra → regex pega referências cruzadas
- Alternativas perdidas → corte cortou pé da questão

**Reportar de volta no chat do claude.ai:**
1. Saída completa do script
2. Se falhou: qual critério e amostra do erro
3. Não tentar consertar — só reportar

---

## Roadmap pós-POC

1. POC valida → escalar para script que processa 1 prova inteira (todas 90 questões + gabarito + cruzamento)
2. Script de 1 prova roda em 6 provas → corpus raw completo
3. Pass 2 LLM (classificação) em batch sobre corpus raw
4. Análises pedagógicas em cima do corpus final (frequência de temas, heatmap
   competência × ano, distribuição por disciplina, etc.)
5. Material didático específico para aula de 04/07 (Geopolítica)

---

## Princípios operacionais

- **Local-first**: tudo que pode ser feito sem LLM, será.
- **Checkpoint everywhere**: pipeline deve ser retomável após falha.
- **Validação amostral manual** obrigatória antes de confiar em qualquer
  classificação subjetiva.
- **Não invente dado**: se a extração falhar para uma questão, registra como
  falha e segue. Não preenche com plausível.
- **Versionar `questoes_raw.csv` no git**.
