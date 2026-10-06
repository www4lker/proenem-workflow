# O workflow, ponta a ponta

Do diagnóstico da turma à apostila, com o que cada etapa recebe, produz e com que ferramenta. Escrito em
06/10/2026 sobre o que existe no repositório; o que ainda não existe está marcado com a tarefa da
[`FILA.md`](FILA.md) que o cria. Regras de fonte e de crédito: [`protocolo-de-fontes.md`](protocolo-de-fontes.md).

```
1. diagnóstico ─► 2. corpus ENEM ─────────────► 3. aula ──────────────────────► 4. apostila
   da turma         2a. extração (Pass 1)          fontes e checagem                capítulo .tex
   (percentuais     2b. classificação (Pass 2)     argumento → plano → roteiro      estilo-proenem.sty
    por tópico)     2c. análise e corpus mestre    slides → complementar → página   Overleaf
```

Hoje as etapas 1 e 2 são de Ciências Humanas; a etapa 3 tem um caso completo (Geografia, 03/10/2026); a 4 é
um protótipo com um subcapítulo. As ligações entre 2 → 3 (seleção de questões) e 3 → 4 (capítulo) são manuais.

## 1. Diagnóstico da turma

- **Entrada:** prova diagnóstica aplicada pelo cursinho.
- **Saída:** [`diagnostico-turmas/DIAGNÓSTICO_TURMAS_ProEnem2026.md`](../diagnostico-turmas/DIAGNÓSTICO_TURMAS_ProEnem2026.md)
  e os PDFs por disciplina em `diagnostico-turmas/Resultado_Analise_PROENEM_2026/` (percentuais de acerto por
  tópico geral e específico; nenhum aluno identificável).
- **Para que serve:** escolher o recorte da aula e o peso de cada tópico. Vale para todas as disciplinas da prova
  (Biologia, Física, Química, Matemática, Linguagens, História, Geografia, Filosofia, Sociologia).

## 2. Corpus ENEM (`pipeline/`)

Precisa do ambiente Python do `requirements.txt` e dos PDFs do INEP em `pipeline/<ano>/` (não versionados;
o manifesto e o download são a tarefa F9).

### 2a. Extração (Pass 1): PDF → `corpus_enem/questoes_raw.csv`

```bash
cd pipeline
python extrair_prova.py 2014/2014_PV_impresso_D1_CD1.pdf   # uma prova; gabarito no mesmo diretório ou --gabarito
python processar_recorte.py                                # todas as provas do dia 1 dos anos da lista ANOS
```

`extrair_prova.py` lê a camada de texto com PyMuPDF (duas colunas, calha detectada por página), separa as
questões por título, limpa o ruído do cabeçalho e junta o gabarito oficial (`pdftotext`). É idempotente pelo `id`
(`AAAA_<área>_NNN`). A área é parâmetro (`--area CH|CN|LC|MT`, padrão CH): o dia da prova e a faixa de questões
por ano vêm de `pipeline/config/areas.yaml`, lido por `pipeline/areas.py` (testes em `pipeline/tests/`). Isso
corrige no código o erro de 2017+ (ver 2c), mas o corpus atual ainda é o extraído antes da correção.
**Limites conhecidos:** só texto (fórmulas, gráficos e figuras não entram); `processar_recorte.py` escolhe o PDF
por heurística de nome e tamanho.

### 2b. Classificação (Pass 2): questão → JSON de classificação (Gemini, pago)

1. Montar, para cada linha de `questoes_raw.csv`, a coluna `prompt_completo` = `prompts/classificar_questao.txt`
   + JSON da questão. **Ainda não há script para isso** (tarefa F8); a montagem está descrita em
   [`historico/pipeline-logs/logs/2026-05-16.md`](historico/pipeline-logs/logs/2026-05-16.md).
2. Rodar o lote com checkpoint: `.claude/skills/gemini-delegate/scripts/ask_batch.py --input <csv>
   --template "{prompt_completo}" --output corpus_enem/batch_completo_raw.csv --field-out classificacao --id-field id`.
   O CSV de saída guarda o prompt inteiro em cada linha: é **cache de custo**, não fonte.
3. `python scripts/strip_and_parse.py corpus_enem/batch_completo_raw.csv corpus_enem/batch_completo_clean.csv`
   tira o fence de markdown e valida o JSON (`parse_ok`).

Custa dinheiro e exige chave própria em `.env` (ver `.env.example`): **só com confirmação humana**. O prompt e a
matriz (C1–C6, H1–H30) são de Ciências Humanas; o CLI do Gemini não tem visão, então questões que dependem de
figura ou fórmula são classificadas pelo texto que sobrou.

### 2c. Análise e corpus mestre

```bash
cd pipeline && python scripts/analise_corpus.py
```

Junta `questoes_raw.csv` e `batch_completo_clean.csv` em `analise/corpus_mestre.csv` (355 linhas: 2013–2019 e
2025, caderno azul, dia 1), imprime as análises (ancoragem, competência × ano, temas, filtro de geopolítica) e
exporta a seleção da aula de 04/07. **Marcação de qualidade (tarefa F6):** as linhas CH de 2017, 2018, 2019 e
2025 são, na verdade, Linguagens (a faixa 1–45 do dia 1 passou a ser Linguagens em 2017); elas recebem
`area_confiavel = false` e ficam fora das análises por padrão. Detalhes em
[`../pipeline/HANDOFF_corpus_2017_linguagens.md`](../pipeline/HANDOFF_corpus_2017_linguagens.md).

### Do corpus para a aula

Os scripts em `aulas/2026-10-03-quem-paga-pelo-impacto/fontes/` mostram a ponte: `filtrar_corpus_proenem.py`
tria candidatas por tema (só com o corpus), `conferir_candidatas_inep.py` confere gabarito, texto e número contra
os PDFs oficiais e `recortar_questoes_inep.py` recorta a imagem da questão para slide e material (os dois últimos
precisam dos PDFs). Classificação de IA é rank 3: serve para triar, nunca para citar.

## 3. Aula (`aulas/AAAA-MM-DD-tema/`)

Modelo: [`aulas/2026-10-03-quem-paga-pelo-impacto/`](../aulas/2026-10-03-quem-paga-pelo-impacto/). A cadeia,
cada elo parado em revisão do professor antes do próximo:

| Elo | Arquivo na aula modelo | Ferramenta |
|---|---|---|
| Ementa e recorte | `aula/aproveitamento-ementa.md` | texto |
| Fontes e checagem | `fontes/checagem.md` (status de cada número) | texto |
| Questões | `fontes/enem-25-selecionadas.md`, `fontes/provas-recortes/` | scripts acima |
| Argumento | `aula/03-slides/argumento.md` | texto |
| Plano de aula | `aula/02-LaTeX/plano-de-aula/` (`aula-geo.sty`) | `latexmk -r latexmkrc` (lualatex) |
| Roteiro de ensaio | `aula/05-roteiro-de-ensaio.md` | texto (o `.docx` é gerado com pandoc) |
| Slides | `aula/03-slides/` (`layout.json`, `content/`, `theme.css`) | `ferramentas/decks-impress/deck build|lint|impresso` |
| Material complementar | `aula/02-LaTeX/material-complementar/` | lualatex |
| Página on-line | `aula/04-online/index.html` + `montar.sh` → `publicar/` | HTML estático; o professor sobe no Netlify |

O logo vem de `identidade/` (ver [`../identidade/LEIAME.md`](../identidade/LEIAME.md)). Um modelo vazio para
copiar é a tarefa F11; a identidade única (um `.sty` e um `theme.css` para aula, apostila e slides) é a F12.

## 4. Apostila (`apostila/`)

Professores escrevem no Word com estilos semânticos (`modelo-word-vazio.docx`); a conversão para
`latex/capitulos/*.tex` ainda é manual (`latex/MAPEAMENTO-WORD-LATEX.md`; `filtros/estilos.lua` é prova de
conceito com Pandoc). `estilo-proenem.sty` define os ambientes (`questaocentral`, `conceito`, `questao`,
`resolucao`...). Compila com `latexmk -pdf main.tex`; `empacotar-overleaf.sh` gera o ZIP para o Overleaf.
Leia [`../apostila/CLAUDE.md`](../apostila/CLAUDE.md) antes de editar: o fluxo é um protótipo em avaliação pela
equipe. A ponte corpus → apostila (uma questão curada vira `questao`/`resolucao`) é a tarefa F14.

## Como adicionar uma área (por exemplo, Ciências da Natureza)

O que já vale sem mudança: o diagnóstico (etapa 1), o método da aula (etapa 3, salvo o prisma, as cores e os
eixos, que são da aula de Geografia) e a apostila (etapa 4). O que precisa mudar está no pipeline:

1. **Dia e faixa de questões por ano e área.** Em `pipeline/config/areas.yaml`, lido por `extrair_prova.py`,
   `processar_recorte.py` e `analise_corpus.py` (F7, feita). Numeração do caderno regular:

   | Área | 2009–2016 | 2017 em diante |
   |---|---|---|
   | CH | dia 1, Q1–45 | dia 1, Q46–90 |
   | CN | dia 1, Q46–90 | dia 2, Q91–135 |
   | LC | dia 2, Q91–135 | dia 1, Q1–45 |
   | MT | dia 2, Q136–180 | dia 2, Q136–180 |

   Só as linhas de CH foram conferidas contra os PDFs oficiais; as demais estão marcadas "a conferir" no YAML e
   precisam da conferência antes de uma questão virar aula (`protocolo-de-fontes.md`).
2. **Provas.** Acrescentar ao manifesto (F9) as provas do dia certo e baixá-las para `pipeline/<ano>/`.
3. **Prompt e matriz da área.** Um prompt por área em `pipeline/prompts/` (F10), com a matriz oficial de
   competências e habilidades (CN: C1–C8, H1–H30) só de fonte conferida.
4. **Figuras e fórmulas.** Em CN muitas questões dependem delas e o Pass 1 só extrai texto. Antes de escalar,
   rodar um piloto de um ano e medir quantas questões perdem informação; avaliar uma variante com visão ou marcar
   `tem_imagem_obrigatoria`. Decisão de custo do professor.
5. **Análise.** `analise_corpus.py --area CN` lê as disciplinas e os rótulos de competência de `areas.yaml`
   (para CN, preencher junto com F10).
6. **Aula.** Copiar o modelo vazio (F11) e seguir a cadeia da etapa 3.

## Registros

- O que falta fazer: [`FILA.md`](FILA.md). Logs de sessão: `logs/`. Contexto: `HANDOFF-construcao.md`,
  `HANDOFF-kit-de-aula.md`, `PLANO_PRODUTO_PROENEM.md` e `historico/`.
- Verificação automática do que compila: `.github/workflows/verificar.yml`. Ambiente: `scripts/checar-ambiente.sh`.
