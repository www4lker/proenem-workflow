---
name: gemini-delegate
description: Delega tarefas de TEXTO com muito input e pouco output ao Gemini CLI, retornando só o resultado compacto ao contexto do Claude para economizar tokens. Use ao resumir/extrair de texto ou arquivos de texto longos (>5k tokens), ao classificar lotes (>20 itens) com critérios fixos, ou em qualquer padrão "ler muito, devolver pouco". Não use para imagens/PDF (o CLI não tem visão), geração de código ou conversa iterativa.
---

# gemini-delegate

Delega trabalho de **input grande / output pequeno** ao `gemini` CLI via
subprocesso. O Claude só vê o resultado compacto — o texto volumoso nunca entra
no contexto do Claude.

## Quando usar
- Resumir ou extrair de texto longo, ou de arquivos `.txt`/`.md`/`.csv` longos.
- Classificar em batch (>20 itens) com critérios fixos.
- Padrão "ler muito, devolver pouco".

## Quando NÃO usar
- **Imagens, PDFs, OCR** — o `gemini` CLI em modo headless **não tem visão**;
  só processa texto. (Para isso seria preciso o SDK `google-genai` com chave.)
- Geração de código.
- Conversa iterativa que precisa de contexto compartilhado.
- Tarefa pequena onde o overhead do subprocesso supera o custo de o Claude ler direto.

## Scripts

### `scripts/ask.sh` — prompt único
```bash
.claude/skills/gemini-delegate/scripts/ask.sh "Resuma em 3 linhas: <texto>"
cat texto_longo.txt | .claude/skills/gemini-delegate/scripts/ask.sh --stdin "Resuma em 5 bullets"
```
Flags: `--model` (default `gemini-2.5-flash`), `--timeout` (s, default 120),
`--stdin`. Imprime só a resposta no stdout; erro → exit ≠ 0 + mensagem no stderr.

### `scripts/ask_batch.py` — batch resiliente sobre CSV
```bash
python .claude/skills/gemini-delegate/scripts/ask_batch.py \
  --input dados.csv \
  --template "Classifique em uma palavra: {coluna}" \
  --output resultado.csv \
  --field-out classificacao --id-field id
```
O arquivo `--output` é o checkpoint: cada linha é gravada na hora; reexecutar
pula o que já está feito (resiliente a Ctrl+C / falha). Sequencial.

## Exemplos

**1. Resumir um arquivo de texto longo**
```bash
cat notas_reuniao.md | .claude/skills/gemini-delegate/scripts/ask.sh --stdin \
  "Liste em 5 bullets as decisões e responsáveis."
```

**2. Pass 2 do pipeline ENEM — classificar questões (texto puro)**
Sobre `corpus_enem/questoes_raw.csv` (coluna `enunciado`), classificar tema:
```bash
python .claude/skills/gemini-delegate/scripts/ask_batch.py \
  --input corpus_enem/questoes_raw.csv \
  --template "Você classifica questões do ENEM de Ciências Humanas. Responda APENAS no formato 'disciplina|tema|tipo_cognitivo'. Disciplina: geografia/história/sociologia/filosofia. Tipo: recuperação/aplicação/análise/síntese. Questão: {enunciado}" \
  --output corpus_enem/questoes_classif.csv \
  --field-out classificacao --id-field id
```

**3. Classificar um CSV genérico linha a linha**
```bash
python .claude/skills/gemini-delegate/scripts/ask_batch.py \
  --input feedback.csv \
  --template "Sentimento (positivo/neutro/negativo) deste comentário: {texto}" \
  --output feedback_classif.csv --field-out sentimento --id-field id
```

## Notas de implementação
- Toda chamada usa `gemini --skip-trust` (o diretório de trabalho não é trusted).
- Autenticação: via API key. O `.env` na pasta da skill com
  `GEMINI_API_KEY=...` é a fonte de autenticação (carregado por `ask.sh` e
  herdado por `ask_batch.py`); `.env` é git-ignorado.
- `ask_file.sh` foi tirado do escopo: anexar PDF/imagem exigiria visão, que o CLI
  headless não tem. Quando necessário, virará `ask_image.py` sobre o SDK.
- Em batch, uma linha que falha grava resultado vazio e segue (não inventa dado).
