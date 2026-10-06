# Relatório Diagnóstico — Aula 04/07/2026

Tema provisório: **Tempo, Tecnologia e Trabalho: da Revolução Industrial ao Debate da Escala 6x1**

## 1. Estado Git

Branch atual: `master`.

Árvore de trabalho: repositório sujo antes da rodada diagnóstica, tratado como trabalho em andamento.

Estado observado:

```text
M  .claude/skills/gemini-delegate/SKILL.md
M  .gitignore
M  CLAUDE.md
M  COMPLEMENTO_handoff_tecnico.md
M  DIAGNÓSTICO_TURMAS_ProEnem2026.md
M  analise/corpus_mestre.csv
M  analise/geopolitica_aula_04_07.csv
M  corpus_enem/batch_completo_clean.csv
M  corpus_enem/batch_completo_raw.csv
M  corpus_enem/questoes_raw.csv
M  corpus_enem/retry40_raw.csv
M  diagnostico_pdfs.md
M  extrair_prova.py
M  instancia-pedagogica.md
M  logs-handoffs/handoffs-velhos/*
M  logs-handoffs/ho.md
M  logs-handoffs/logs/2026-05-15.md
M  logs-handoffs/logs/2026-05-16.md
M  poc_extracao.py
M  processar_recorte.py
M  prompts/classificar_questao.txt
M  scripts/analise_corpus.py
M  scripts/strip_and_parse.py
?? .claude/settings.local.json
?? AGENTS.md
?? HANDOFF_AGENTE_INICIO_2026-06-27.md
?? plano_aula_04_07.md
?? prompts/aluno_arquetipico.txt
?? protocolo_feedback_aula.md
```

Resumo: 25 arquivos modificados, 6 não rastreados. Nada foi limpo, revertido ou commitado durante a rodada diagnóstica.

Últimos 8 commits:

```text
cb889a7 adiciona dois arquivos finais do trabalho de hoje...
8b3d88f §8.5 análise pedagógica: corpus mestre + filtro geopolítica 04/07
5d1c234 Pass 2 retry 40: batch_completo_clean.csv atualizado com retentas
e40fdc2 Cache Pass 2: versionar batch_completo_raw.csv
ef44130 Pass 2 calibração + batch
e927f42 Pass 1 fecha 2013-2019+2025
fc9770d Escala Pass 1 para o recorte CH 2013-2018
3853523 Pass 1 robusto
```

## 2. Arquivos e Scripts Relevantes

Arquivos explícitos sobre aula, 04/07 e pedagogia:

- `analise/geopolitica_aula_04_07.csv`
- `plano_aula_04_07.md`
- `instancia-pedagogica.md`
- `DIAGNÓSTICO_TURMAS_ProEnem2026.md`
- `protocolo_feedback_aula.md`

Para o novo tema trabalho, tecnologia, industrialização, jornada e precarização, não há arquivo dedicado à aula. O material está disperso principalmente em:

- `analise/corpus_mestre.csv`
- `corpus_enem/questoes_raw.csv`
- `corpus_enem/batch_completo_clean.csv`
- referências pontuais nos documentos pedagógicos

Scripts:

- `extrair_prova.py`: produz/atualiza `corpus_enem/questoes_raw.csv`; não executar em rodada apenas diagnóstica.
- `scripts/strip_and_parse.py`: produz CSV limpo a partir de raw Gemini; não executar em rodada apenas diagnóstica.
- `scripts/analise_corpus.py`: produz `analise/corpus_mestre.csv`, `analise/geopolitica_aula_04_07.csv`, rankings de ancoragem, heatmap competência x ano e top temas; não executar em rodada apenas diagnóstica porque grava CSV.

Esses scripts podem ser lidos em rodada diagnóstica, sem execução.

## 3. Estrutura dos CSVs

### `analise/corpus_mestre.csv`

Registros: 355.

Colunas:

```text
id, ano, caderno, area, numero, enunciado, fontes_citadas, alternativas,
gabarito, parse_ok, disciplina_principal, disciplinas_secundarias,
tema_principal, tema_secundario, tipo_cognitivo, competencia, habilidade,
ancoragem, classificado
```

### `corpus_enem/questoes_raw.csv`

Registros: 355.

Colunas:

```text
id, ano, caderno, area, numero, enunciado, fontes_citadas, alternativas, gabarito
```

### `corpus_enem/batch_completo_clean.csv`

Registros: 350.

Colunas:

```text
id, classificacao, parse_ok, erro
```

Chave de união: `id`.

Campos:

- `enunciado`: contém texto de apoio + comando, sem separação estrutural.
- `alternativas`: JSON em uma célula com chaves `A` a `E`.
- `gabarito`: contém a letra correta.
- `disciplina_principal`, `tema_principal`, `tema_secundario`, `ancoragem`, `tipo_cognitivo`, `competencia`, `habilidade`: vêm da classificação.
- Não há campo de justificativa pedagógica; há apenas classificação estruturada.

Representação de imagens, mapas, charges, gráficos e tabelas: não há imagem embutida. O corpus registra indícios em `fontes_citadas` e texto residual/caption no `enunciado`. Para questão visual, o conteúdo oficial integral pode exigir voltar ao PDF.

Ausências e inconsistências relevantes:

- Enunciado ausente: `2013_CH_042`, `2014_CH_016`, `2016_CH_035`, `2025_CH_005`, `2025_CH_040`.
- Sem classificação válida: esses 5 + `2013_CH_020`, `2018_CH_009`.
- Alternativas: todas parseiam como JSON A-E.
- Ruído textual detectado em 14 IDs, sobretudo 2025, com marcas como `ENEM2025`; relevante se a questão escolhida vier de 2025.

Amostra curta de linha:

```text
id=2015_CH_002
ano=2015
numero=2
enunciado=<texto de apoio + comando>
alternativas={"A":..., "B":..., "C":..., "D":..., "E":...}
gabarito=E
disciplina=sociologia
tema=Sociologia do trabalho > impactos da tecnologia na jornada de trabalho
ancoragem=texto_analitico
```

## 4. Método Usado na Busca

A busca usou leitura de CSV com parser, juntando em memória `tema_principal`, `tema_secundario`, `enunciado` e alternativas.

Foram combinados termos diretos e relações semânticas:

- trabalho
- jornada
- tecnologia
- industrialização
- controle
- produtividade
- desemprego
- fordismo
- taylorismo
- produção
- cadeias globais
- direitos
- sindicatos
- lazer
- tempo

Depois foi feita inspeção qualitativa das melhores candidatas, sem depender apenas das tags automáticas.

## 5. Questões Candidatas

| ID | Classificação e ancoragem | Núcleo e comando | Uso possível / risco / confiança |
|---|---|---|---|
| `2015_CH_002` | Sociologia; tecnologia e jornada; `texto_analitico`; gab. E | Iluminação artificial dissolve fronteira entre trabalho e descanso; pergunta consequência no mundo do trabalho. Alternativas contrastam qualidade, emprego, controle do horário, esforço e ampliação da jornada. | Abertura ou resolução guiada. Conecta diretamente com escala 6x1. Risco: texto abstrato. Confiança alta. |
| `2016_CH_040` | Geografia; globalização e reestruturação do trabalho; `texto_analitico`; gab. C | Produtividade aumenta com técnica digital, mas renda segue mal distribuída; comando pede explicação das mudanças em emprego e renda. | Questão de síntese forte para tese da aula. Risco: Francisco de Oliveira é denso. Confiança alta. |
| `2016_CH_009` | História; capitalismo/grande transformação; subtema trabalho como mercadoria; `texto_analitico`; gab. C | Produção industrial exige transformar trabalho, terra e dinheiro em mercadorias; pergunta consequência socioeconômica. | Principal em duplas ou síntese histórica. Risco: Polanyi exige mediação. Confiança alta. |
| `2013_CH_016` | Sociologia; controle e flexibilidade; `texto_analitico`; gab. E | Trabalho flexível descentraliza local, mas intensifica controle por resultados; menciona taylorismo/fordismo. | Resolução guiada para ponte com home office/plataformas. Risco: vocabulário conceitual alto. Confiança alta. |
| `2015_CH_029` | Geografia; globalização, trabalho e produção; `texto_analitico`; gab. E | Técnicas da informação e globalização perversa; pergunta consequência para setor produtivo e mundo do trabalho. | Síntese ou reserva. Risco: Milton Santos e alternativas densas. Confiança alta. |
| `2013_CH_017` | Geografia; modelos de produção; `artefato_visual`; gab. D | Imagem compara dois modelos produtivos e crise de superprodução; alternativas sobre matéria-prima, mão de obra, processamento, estoque e mercado. | Boa questão de abertura visual ou duplas. Precisa recuperar imagem oficial. Confiança alta. |
| `2014_CH_005` | Sociologia; tecnologia e organização do trabalho; `artefato_visual`; gab. A | Cartum “Engraxate”; comando pergunta pessimismo sobre tecnologia e trabalho. | Abertura forte por imagem. Risco: sem o cartum no CSV, precisa PDF. Confiança média-alta. |
| `2019_CH_044` | Sociologia/História; trabalho urbano e industrialização; `evento_narrativo`; gab. E | Poema com sirene, fábrica, fiação, patrão; comando real é linguístico, sobre formas verbais/pronominais. | Útil para estudo do professor ou abertura literária, inadequada como questão principal de CH. Confiança média. |
| `2015_CH_038` | Geografia; globalização e cadeias produtivas; `texto_analitico`; gab. D | Carro global financiado, projetado, montado e vendido em vários países; pergunta pressuposto do processo produtivo. | Questão de síntese geográfica. Boa ponte para cadeias globais. Risco: menos foco em jornada. Confiança alta. |
| `2014_CH_010` | Geografia; migração de mão de obra qualificada; `evento_narrativo`; gab. C | Jovem espanhol desempregado migra por falta de futuro profissional; comando pede implicação da crise. | Questão de abertura por personagem. Conecta emprego/qualificação, menos diretamente 6x1. Confiança média. |
| `2014_CH_007` | Sociologia rural; desigualdade na distribuição da produção; `evento_narrativo`; gab. A | Canção sobre trabalhador rural que planta e divide com quem não planta; comando pergunta insatisfação. | Boa abertura concreta para exploração/distribuição. Risco: rural desloca da tecnologia industrial. Confiança média. |
| `2013_CH_039` | História; desenvolvimentismo JK; `artefato_visual`; gab. C | Charge ironiza automóvel/estradas versus fome; comando trata contradições socioespaciais do crescimento. | Boa ponte História-Geografia sobre industrialização. Precisa charge oficial. Confiança média-alta. |
| `2015_CH_011` | História; concepções de tempo; `artefato_visual`; gab. D | Calendário medieval liga tempo e trabalho sazonal; comando pede concepção de tempo. | Boa abertura histórica para “tempo antes do relógio industrial”. Precisa imagem. Confiança média-alta. |
| `2014_CH_006` | História; crise de 1929 e industrialização; `texto_analitico`; gab. D | Celso Furtado sobre crise cafeeira; comando pede resposta do Estado brasileiro. | Reserva para contexto histórico industrialização brasileira. Risco: distante da jornada/trabalho. Confiança média. |
| `2025_CH_037` | História/cultura; subtema trabalho; `evento_narrativo`; gab. A | Compara Hércules a João que faz vários bicos; comando é sobre intertextualidade. | Útil para professor ou abertura provocativa sobre múltiplos trabalhos, mas inadequada como questão principal. Confiança baixa-média. |

## 6. Três Mais Promissoras, Sem Decisão Final

### `2015_CH_002`

Mais alinhada à tese “tecnologia aumenta produtividade/tempo disponível, mas pode ampliar jornada”. É direta para escala 6x1.

### `2016_CH_040`

Melhor para formular a tese em termos geográficos contemporâneos: tecnologia, produtividade, renda, estrutura produtiva e transferência dos ganhos.

### `2013_CH_017`

Melhor entrada visual sobre modelos produtivos, estoque/superprodução e organização da produção. Exige recuperar a imagem oficial.

## 7. Limitações Encontradas

- O corpus não separa texto de apoio e comando; ambos ficam em `enunciado`.
- Questões visuais não têm a imagem oficial embutida; mapas, charges, cartuns e calendários precisam ser recuperados do PDF.
- A classificação é automática; tema e ancoragem são úteis, mas precisam validação humana.
- Há ruído em alguns itens de 2025.
- O corpus mistura questões do intervalo dia 1 que podem ter perfil mais Linguagens, embora estejam no recorte `CH`; `2019_CH_044` e `2025_CH_037` mostram esse risco.

## 8. Perguntas Para o Orquestrador

1. A aula deve priorizar “escala 6x1” como debate contemporâneo ou usar isso só como chegada?
2. Podemos recuperar imagens dos PDFs na próxima rodada se a candidata visual for escolhida?
3. A questão principal deve ser resolvida inteira em sala ou algumas podem servir apenas como disparador?
4. Os dois professores querem uma questão mais sociológica (`2015_CH_002`) ou uma ponte mais História-Geografia (`2013_CH_017` / `2016_CH_009`)?
5. Pode haver uso de questão com comando de Linguagens se o texto for pedagogicamente forte, ou devemos restringir a CH estrita?

## 9. Confirmação da Rodada Diagnóstica

Na rodada diagnóstica original não foram criados arquivos, não foram editados arquivos, não foi executado Gemini, não houve chamada externa, não houve reprocessamento de provas, CSVs não foram regravados, não houve commit e o estado do repositório não foi alterado.

Este documento Markdown foi criado posteriormente a pedido explícito do usuário para transcrever o relatório.
