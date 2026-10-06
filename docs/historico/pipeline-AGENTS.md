# AGENTS.md

Guia operacional para agentes trabalhando neste repositório ENEM / ProEnem 2026.

## Contexto do projeto

Este repositório contém o corpus ENEM e um pipeline de extração, classificação e
análise pedagógica de questões de Ciências Humanas para o ProEnem 2026.

O projeto não é apenas um arquivo morto de PDFs. O estado atual inclui:

- PDFs e HTMLs de origem do ENEM.
- Pass 1 de extração em `extrair_prova.py` e `processar_recorte.py`.
- Pass 2 de classificação via Gemini em `corpus_enem/*`.
- Análises pedagógicas em `scripts/analise_corpus.py` e `analise/*`.
- Materiais de aula e handoffs em Markdown.

O diretório Linux esperado é:

```bash
pipeline
```

## Primeira ação de qualquer sessão

Antes de editar ou rodar pipeline:

```bash
git status --short --branch
```

O repositório pode estar sujo por trabalho em andamento de Walker. Não trate
arquivos modificados ou não rastreados como lixo.

Não fazer sem pedido explícito:

- `git checkout` para reverter arquivos.
- `git reset`.
- limpeza de untracked.
- formatação em massa.
- commits automáticos.
- reexecução ampla de scripts que regravam CSVs.

## Leitura inicial recomendada

Leia nesta ordem antes de mexer no pipeline:

```bash
sed -n '1,260p' HANDOFF_AGENTE_INICIO_2026-06-27.md
sed -n '1,260p' CLAUDE.md
sed -n '1,280p' COMPLEMENTO_handoff_tecnico.md
sed -n '1,260p' logs-handoffs/logs/2026-05-15.md
sed -n '1,300p' logs-handoffs/logs/2026-05-16.md
sed -n '1,240p' extrair_prova.py
sed -n '1,220p' processar_recorte.py
sed -n '1,260p' scripts/analise_corpus.py
```

Nota: `CLAUDE.md` está parcialmente defasado; ainda é útil para histórico e
layout dos PDFs, mas não descreve todo o estado atual do pipeline.

## Estado factual verificado em 2026-06-27

- Branch observada: `master`.
- `corpus_enem/questoes_raw.csv`: 355 questões.
- `corpus_enem/batch_completo_clean.csv`: 350 linhas, 348 com `parse_ok=True`.
- `analise/corpus_mestre.csv`: 355 questões.
- `analise/geopolitica_aula_04_07.csv`: 7 questões.
- `2019_CH_045` está limpa de rodapé/cabeçalho residual.

Questões com `enunciado` ausente no Pass 1:

```text
2013_CH_042
2014_CH_016
2016_CH_035
2025_CH_005
2025_CH_040
```

Questões presentes no Pass 1, mas sem classificação válida no Pass 2:

```text
2013_CH_020
2018_CH_009
```

## Pipeline

### Pass 1: extração

Arquivos principais:

- `extrair_prova.py`: extrai uma prova ENEM dia 1 e grava
  `corpus_enem/questoes_raw.csv`.
- `processar_recorte.py`: processa o recorte de anos configurado em `ANOS`.

Cuidados:

- `processar_recorte.py` chama `processar()` e pode regravar/alterar
  `corpus_enem/questoes_raw.csv`; não rode antes de entender o diff.
- A regex de remoção de rodapé já foi generalizada para `CH|LC|CN|MT` em
  `extrair_prova.py`. Não reaplique esse fix cegamente.
- Use parser CSV para contagens, não `wc -l`.

Verificação rápida segura:

```bash
python3 - <<'PY'
import csv
from pathlib import Path
for rel in ['corpus_enem/questoes_raw.csv','corpus_enem/batch_completo_clean.csv','analise/corpus_mestre.csv','analise/geopolitica_aula_04_07.csv']:
    with Path(rel).open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    print(rel, len(rows))
PY
```

### Pass 2: classificação Gemini

Arquivos principais:

- `prompts/classificar_questao.txt`
- `.claude/skills/gemini-delegate/scripts/ask_batch.py`
- `scripts/strip_and_parse.py`
- `corpus_enem/batch_completo_raw.csv`
- `corpus_enem/batch_completo_clean.csv`
- `corpus_enem/retry40_raw.csv`

Não rodar Gemini ou chamadas externas sem confirmar intenção. Pass 2 tem custo
externo e já há 348 classificações válidas.

O padrão usado no Pass 2 foi pré-montar uma coluna `prompt_completo` e chamar
`ask_batch.py --template "{prompt_completo}"`, para evitar que chaves JSON do
prompt sejam reinterpretadas por `str.format`.

Taxonomia atual de `ancoragem`:

- `evento_narrativo`
- `artefato_visual`
- `texto_analitico`
- `composto`

## Análise pedagógica

Arquivo principal:

```bash
scripts/analise_corpus.py
```

Ele junta `questoes_raw.csv` com `batch_completo_clean.csv`, salva
`analise/corpus_mestre.csv` e exporta o subconjunto de geopolítica em
`analise/geopolitica_aula_04_07.csv`.

Subconjunto recomendado para aula de 04/07/2026:

```text
2014_CH_023
2015_CH_021
2016_CH_031
2014_CH_026
2014_CH_037
2018_CH_022
2025_CH_022
```

A premissa pedagógica registrada é: a turma processa melhor entradas narrativas,
visuais ou compostas; `texto_analitico` puro deve ser ponto de chegada, não
porta de entrada.

## Versionamento e arquivos sensíveis

`.gitignore` ignora PDFs, HTMLs, `.env`, ambientes virtuais, caches e a maior
parte dos CSVs geráveis.

Exceções versionadas/canônicas em `corpus_enem/`:

- `questoes_raw.csv`
- `batch_completo_raw.csv`
- `batch_completo_clean.csv`
- `retry40_raw.csv`

Não exibir nem commitar:

- `.env`
- chaves Gemini
- credenciais
- `.claude/settings.local.json` sem revisão explícita

PDFs e CSVs grandes podem ser fonte de verdade ou artefatos caros. Não apagar.

## Comandos úteis

Diagnóstico:

```bash
git status --short --branch
git log --oneline -12
git diff --stat
git diff -- extrair_prova.py processar_recorte.py scripts/analise_corpus.py scripts/strip_and_parse.py
```

Regerar análise pedagógica, se Walker pedir:

```bash
.venv/bin/python scripts/analise_corpus.py
```

Parsear saída raw do Gemini:

```bash
.venv/bin/python scripts/strip_and_parse.py IN OUT
```

## Prioridade recomendada ao retomar

1. Diagnosticar o estado Git atual.
2. Separar mentalmente bugfix de Pass 1, artefatos de Pass 2 e material
   pedagógico.
3. Não chamar Gemini na primeira passada.
4. Se o objetivo for técnico, fechar o bugfix Pass 1 e validar CSVs.
5. Se o objetivo for pedagógico, trabalhar a aula a partir de
   `analise/geopolitica_aula_04_07.csv` e `plano_aula_04_07.md`.
