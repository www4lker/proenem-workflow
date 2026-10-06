# HANDOFF: linhas "CH" de 2017+ são Linguagens (achado de 30/09/2026)

Achado feito de fora, durante o projeto `aula-geo-natureza` (aula sobre data centers). **Nada
neste repositório foi alterado** por essa sessão, exceto este arquivo (novo, não rastreado).
Sem commit. Antes de tudo: `git status --short --branch` (AGENTS.md).

## O que está errado
Em `analise/corpus_mestre.csv` (355 linhas), as linhas rotuladas `area = CH` de **2017, 2018,
2019 e 2025** (174 de 180) são, na verdade, as **questões 1–45 de Linguagens** do caderno azul,
não as de Ciências Humanas.

- Sinais: enunciados em espanhol (língua estrangeira), textos de literatura e língua portuguesa;
  o texto aparece no PDF da prova antes do título "Ciências Humanas" (a 9%–54% do caderno,
  contra ~64% em que começa CH).
- Consequência: `disciplina_principal`, `tema_principal`, `ancoragem` etc. dessas linhas são
  classificações de IA sobre o texto errado. Qualquer análise por ano ou por disciplina que inclua
  2017+ está contaminada.
- **2013–2016 estão certas:** o gabarito do corpus bate com o oficial em 175/175, e texto e número
  da questão batem em 163/175.

## Causa provável (não verificada)
Para 2017+, o caderno 1 azul do dia 1 tem Linguagens em 1–45 e CH em **46–90**; para 2013–2016,
CH é 1–45. O extrator parece ter tomado a faixa 1–45 sempre. Conferir em `extrair_prova.py` e
`processar_recorte.py` a faixa de páginas/numeração por ano.

## Numeração oficial (para corrigir)
| anos | CH no caderno 1 azul (dia 1) |
|---|---|
| 2013–2016 | questões 1–45 |
| 2017 em diante | questões 46–90 |

## Como reproduzir a checagem (somente leitura)
Scripts em `aulas/2026-10-03-quem-paga-pelo-impacto/fontes/`:
- `conferir_candidatas_inep.py`: compara gabarito e texto do corpus com os PDFs oficiais deste
  repositório e imprime a tabela de validação por ano em `conferencia-inep-candidatas.md`.
- Gabaritos usados: `2013/dia1_azul.pdf`, `2014/CADERNO_1_AZUL_SABADO.pdf`,
  `2015/CADERNO_1_AZUL_SABADO.pdf`, `2016/GAB_ENEM_2016_DIA_1_01_AZUL.pdf`,
  `2017/cad_1_gabarito_azul_5112017.pdf`, `2018/GAB_ENEM_2018_DIA_1_AZUL.pdf`,
  `2019/gabarito_1_dia_caderno_1_azul_aplicacao_regular.pdf`, `2025/2025_GB_impresso_D1_CD1.pdf`.

## O que a próxima sessão deve fazer (em ordem)
1. Rodar `git status --short --branch` e **não tocar** no trabalho em andamento do professor.
2. Confirmar o achado abrindo 2 ou 3 questões de 2017 e de 2025 no PDF (ex.: `2017_CH_003`
   é texto em espanhol; `2025_CH_020` fala de rituais).
3. Perguntar ao professor se quer corrigir a extração agora. Se sim: refazer o Pass 1 de 2017,
   2018, 2019 e 2025 com a faixa 46–90; reclassificar (Pass 2) só essas linhas; conferir com o
   gabarito oficial antes de aceitar. Respeitar o gate de abort do Gemini
   (COMPLEMENTO_handoff_tecnico.md) e **não** reexecutar em massa scripts que regravam CSVs.
4. Se não: marcar as linhas 2017+ como `area_confiavel = false` (ou equivalente) para não
   entrarem em análise. Sem commit automático.
5. Há 4 anos ausentes do corpus (2020–2024) e o corpus só cobre CH; isso é escopo, não erro.

## Item adicional (30/09/2026): destino do projeto e versionamento
1. **Legado para o PROENEM.** O pesquisador está concebendo a ideia de legar este projeto (corpus
   ENEM) ao PROENEM, o cursinho em que trabalha como voluntário. Antes disso, precisa de um
   **inventário do que existe e do que falta** (dados, scripts, documentação, anos/áreas
   cobertos, pendências como a correção acima e os anos 2020–2024 ausentes) para dimensionar a
   entrega.
2. **O projeto de apostilas também é voluntário** (`../APOSTILAS-PROENEM/`) e segue o mesmo
   destino.
3. **Ambos devem ir para o GitHub em repositório privado.** Situação em 30/09/2026: `PROENEM/`
   tem uma pasta `.git` vazia (não é repositório válido); `APOSTILAS-PROENEM/`
   não tem git. Nenhum remoto configurado. Antes de subir: revisar segredos (chaves de API do
   Gemini etc.), PDFs pesados e dados privados; criar os repositórios privados só com
   confirmação do pesquisador.

### Atualização (05/10/2026): repositórios criados

- `ENEM/` → `github.com/www4lker/proenem-enem` (privado, branch `master`, histórico de 17 commits preservado). PDFs do INEP ficam fora; PDFs próprios de `Resultado_Analise_PROENEM_2026/` versionados por exceção.
- `APOSTILAS-PROENEM/` → `github.com/www4lker/proenem-apostilas` (privado, branch `main`). `audio-reunniao.mp3` fica fora (só disco local).
- Chaves do Gemini (`.env` e `.claude/settings.local.json`) excluídas; histórico verificado sem chaves.
- Pendente: inventário "o que tem / o que falta" para o legado ao PROENEM.
