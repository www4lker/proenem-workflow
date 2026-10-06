# HANDOFF — Preparar o legado dos projetos ao PROENEM

> **Registro (06/10/2026).** Os itens abertos deste documento foram levados para [`docs/FILA.md`](FILA.md), que passa a ser a fonte única do que falta fazer. Este arquivo fica como contexto.

Data: 2026-10-05
Escopo: `proenem-enem` (este repositório) e `proenem-apostilas` (repositório irmão).
Origem: auditoria somente leitura feita em 05/10/2026 (log em
`logs-handoffs/logs/2026-10-05-auditoria-legado.md`). Nada foi corrigido na auditoria.
Este documento diz o que a próxima sessão deve fazer.

> **Leia antes:** este handoff foi escrito sobre os repositórios de origem (`proenem-enem`,
> `proenem-apostilas`, `aula-geo-natureza`, `decks-impress`). Os caminhos citados abaixo são os de
> origem; a correspondência com este repositório está em `docs/higienizacao.md`. As decisões 1 e 2 das
> "Decisões pendentes" já foram tomadas: repositório unificado com histórico limpo, higienizado localmente.

## Pergunta que orienta o trabalho

> Uma equipe de outra área (por exemplo, Física ou Biologia) consegue, só com o que está
> nos repositórios, reconstruir e continuar o workflow completo?

**Resposta hoje: não.** Uma pessoa com perfil técnico reconstruiria com esforço, lendo
código e logs. Um professor sem perfil técnico não conseguiria. Os motivos estão abaixo,
do mais grave para o menos grave.

## O workflow completo (como ele existe, espalhado)

```
PDFs INEP ─► Pass 1: extração ─► Pass 2: classificação ─► análise ─► curadoria/kit de aula ─► apostila
(fora do git) extrair_prova.py    Gemini CLI + prompt     scripts/     aula-04-07/ (manual)    proenem-apostilas
              processar_recorte   (montagem do prompt     analise_                              (LaTeX, manual)
                                   não está em script)    corpus.py
```

Nenhum documento descreve esse fluxo de ponta a ponta. As duas últimas etapas, kit e
apostila, são feitas à mão e não há ligação entre os dois repositórios.

## Bloqueios para outra área (Física/Biologia = Ciências da Natureza)

1. **O pipeline só funciona para Ciências Humanas, e a área está fixa no código.**
   - `extrair_prova.py` → `detectar_intervalo_ch()` sempre devolve `1, 45` e grava `area="CH"`
     e `id=AAAA_CH_NNN`. Isso também causa o bug de 2017+ (ver
     `HANDOFF_corpus_2017_linguagens.md`).
   - `processar_recorte.py` só procura provas do **dia 1**.
   - Numeração real de CN no caderno 1 azul: **2009–2016 → dia 1, Q46–90**;
     **2017+ → dia 2, Q91–135**. Hoje nada disso está parametrizado.
   - `prompts/classificar_questao.txt` só cobre Humanas: disciplinas, competências C1–C6
     da Matriz CH e habilidades H1–H30. CN tem outra matriz (C1–C8, H1–H30).
   - `scripts/analise_corpus.py` usa a lista fixa `['geografia','historia','sociologia','filosofia']`
     e o número 348 em texto.
2. **CN depende de fórmulas e figuras.** O Pass 1 extrai só a camada de texto. O Pass 2 usa
   o Gemini CLI em modo headless, que não tem visão (está documentado na skill). Em Física,
   Química e Biologia, muitas questões perdem fórmulas, gráficos e esquemas. É preciso
   avaliar uma variante com visão (SDK `google-genai`) ou marcar `tem_imagem_obrigatoria`.
3. **Não dá para instalar.** Não há `README.md`, `requirements.txt`/`pyproject.toml`
   nem instruções de ambiente. Na máquina de origem não existe `.venv` e o PyMuPDF (`fitz`)
   não está instalado. Dependências reais: Python 3.10+, `pymupdf`, `pandas`, `poppler-utils`
   (`pdftotext`), `gemini` CLI e uma chave própria do Gemini.
4. **As provas de origem não estão no git e não há manifesto.** O `.gitignore` exclui PDFs.
   Os nomes dos arquivos variam por ano, e o `processar_recorte.py` escolhe o arquivo
   por heurística de nome e tamanho. Falta um `fontes/MANIFESTO.csv`
   (ano, dia, caderno, cor, URL oficial do INEP, nome esperado, sha256) e um script de download.
5. **Parte do Pass 2 não está versionada.** A montagem da coluna `prompt_completo`
   (prompt + JSON da questão) só aparece descrita em `logs-handoffs/logs/2026-05-16.md:50`.
   Não há script para isso.
6. **A documentação de entrada se contradiz e aponta para lugares que não existem.**
   - `CLAUDE.md` diz "Not a code repository — an archive of 46 ENEM exam PDFs" e descreve
     pastas `210/`, `211/` que não existem.
   - `AGENTS.md` manda ler `HANDOFF_AGENTE_INICIO_2026-06-27.md`, que não existe, e
     indica o diretório `/mnt/supersupa/Users/walke/...`.
   - `instancia-pedagogica.md` cita `pipeline`. `aula-04-07/PROJETO_SLIDES_*.md`
     cita `C:\Users\walke\...`.
   - `HANDOFF_corpus_2017_linguagens.md` usa scripts **fora do repositório**
     (`aulas/2026-10-03-quem-paga-pelo-impacto/fontes/conferir_candidatas_inep.py`).
   - `continue-essa-conversa.md` guarda um ID de sessão do Codex e não tem valor para terceiros.
7. **A qualidade do corpus atual não está marcada.** Há 174 linhas de Linguagens rotuladas
   como CH em 2017–2019+2025, 5 enunciados vazios e 2 itens sem classificação. Ainda não
   existem os campos de confiança propostos em `PLANO_PRODUTO_PROENEM.md`.

## Conteúdo pessoal ou de terceiros

**Já tratado neste repositório** (higienização local de 06/10/2026, antes do primeiro envio). O que saiu, e
por quê, está em `docs/higienizacao.md` e `docs/_excluidos.tsv`. Os repositórios de origem continuam
existindo como acervo pessoal do autor e não fazem parte desta entrega.

## Redundâncias

- **PNGs triplicados:** `aula-04-07/assets_questoes_visuais/`, `aula-04-07/curadoria_questoes_04_07_assets/`,
  `aula-04-07/kit_ensaio_04_07_assets/` e `relatorios/*` são cópias idênticas (md5). A pasta
  `relatorios/` inteira duplica `aula-04-07/`.
- **Documentos de estado sobrepostos:** `CLAUDE.md`, `AGENTS.md`, `instancia-pedagogica.md`,
  `COMPLEMENTO_handoff_tecnico.md`, `PLANO_PRODUTO_PROENEM.md`, `logs-handoffs/ho.md`,
  `logs-handoffs/handoffs-velhos/*` e dois `HANDOFF_*.md` na raiz. Cada um repete
  números do corpus (355/348) e alguns já estão desatualizados.
- **`plano_aula_04_07.md` está na raiz** em vez de `aula-04-07/`.
- **`poc_extracao.py`** é uma prova de conceito superada por `extrair_prova.py`.
- **CSVs:** `batch_completo_raw.csv` (1,2 MB) repete o prompt inteiro em cada linha. Pode ser
  mantido como cache de custo, mas a documentação deve dizer que ele é cache, não fonte.
- **apostilas:** `docs/kit-prototipo-proenem.zip` empacota arquivos que já estão versionados
  (os dois `.docx`, o PDF e o outro ZIP). `projeto-overleaf-proenem.zip` é gerado a partir de `latex/`.
  Os dois são artefatos e deveriam ser releases do GitHub, não arquivos versionados.
- **apostilas** `CLAUDE.md` ainda descreve `audio-reunniao.mp3`, que agora fica fora do git.

## O que funciona e pode ser aproveitado

- A apostila LaTeX **compila sem erros** (`latexmk -pdf`, 4 páginas, testado numa cópia em 05/10/2026).
  A arquitetura Word semântico → `estilo-proenem.sty` está bem documentada no `CLAUDE.md` dela.
- `ask_batch.py` é genérico, tem checkpoint e é reutilizável para qualquer área.
- O `parse_gabarito` já aceita a numeração 1–180, então serve para o dia 2.
- `PLANO_PRODUTO_PROENEM.md` já define o produto (um gerador de kit de aula) e os templates
  pedagógicos por área, inclusive "Natureza: fenômeno/experimento → modelo → conceito".
- O diagnóstico agregado das turmas e a taxonomia de `ancoragem` valem para qualquer área.

## Plano para a próxima sessão (em ordem)

Antes de tudo, rode `git status` nos dois repositórios. Não chame o Gemini sem confirmação.

1. **Decidir a forma de entrega** (Opção A ou B acima) com o pesquisador.
2. **Higienizar** (separar conteúdo pessoal e de terceiros; tabela acima). Aplicar primeiro
   no repositório de entrega.
3. **Uma porta de entrada única:** `README.md` com o workflow ponta a ponta (o diagrama
   acima), público-alvo, instalação e "como adicionar uma área". Reescrever `CLAUDE.md`/`AGENTS.md`
   a partir dele e mover o resto para `docs/historico/`.
4. **Ambiente:** `requirements.txt`, `.env.example` (`GEMINI_API_KEY=`) e um teste de fumaça
   que rode o Pass 1 em uma prova.
5. **Fontes:** `fontes/MANIFESTO.csv` + `scripts/baixar_provas.py`.
6. **Parametrizar a área:** um arquivo `config/areas.yaml` com dia e intervalo de questões por
   ano e área (CH, CN, LC, MT), prompt por área e matriz por área.
   Isso corrige junto o bug de 2017+ (CH = Q46–90 do dia 1 a partir de 2017).
7. **Versionar a montagem do `prompt_completo`** como script (`scripts/montar_prompts.py`).
8. **Piloto CN:** rodar um ano (por exemplo 2019, dia 2, Q91–135) e medir quantas questões perdem
   informação sem visão, antes de escalar.
9. **Ligar com a apostila:** definir como uma questão curada vira um ambiente `questao`/`resolucao`
   do `estilo-proenem.sty` (exportador Markdown/LaTeX a partir do `corpus_mestre.csv`).
10. **Tirar duplicatas:** ficar com uma pasta de assets por aula e transformar os ZIPs em releases.
11. **Licença e nota de uso** dos materiais do INEP (pendente desde `PLANO_PRODUTO_PROENEM.md` §5).

## Critério de pronto

Um voluntário de Física ou Biologia clona o repositório de entrega, segue só o `README.md`
e, com a própria chave do Gemini, gera o corpus classificado de **um ano de CN** e um kit
de aula, sem falar com o autor original.

---

## Atualização 2026-10-06: premissa da nuvem e estrutura unificada (proposta, pendente de decisão)

### Premissa

O projeto unificado será **construído pelo Fable numa sessão em nuvem ligada ao GitHub**. Só depois
dessa construção se decide compartilhar com o PROENEM. Consequência prática: **o que não estiver
no repositório não existe para o Fable.** Isso torna obrigatórios os itens 3–7 do plano acima e
acrescenta três exigências:

- **Higienização antes do envio, não depois.** O Fable não deve receber conteúdo pessoal ou de
  terceiros para "limpar": tudo que vai ao GitHub fica no histórico.
- **Ambiente reproduzível na nuvem:** script de preparo (Python + `pymupdf` + `pandas`,
  `poppler-utils`, TeX Live) e verificações automáticas (GitHub Actions) para a apostila compilar
  e o Pass 1 rodar numa prova, para o Fable conseguir testar o que constrói.
- **Fontes acessíveis na nuvem:** PDFs do INEP como *release* do próprio repositório privado (não
  depender do site do INEP nem de acesso à rede na nuvem); a chave do Gemini como segredo do
  ambiente da nuvem, nunca em arquivo.

### Terceiro projeto que pertence ao workflow

`aulas/2026-10-03-quem-paga-pelo-impacto/` (git próprio, remoto só no pendrive, 473 MB em disco,
166 arquivos versionados) é a etapa "aula" do workflow e não entrou em nenhum repositório:

- contém o **logo do PROENEM em duas versões diferentes** (`aula/02-LaTeX/estilo/` e
  `aula/03-slides/assets/img/`, md5 distintos) e cópias geradas em `dist/` e `publicar/`;
- contém `fontes/conferir_candidatas_inep.py` e `filtrar_corpus_proenem.py`, citados pelo
  `HANDOFF_corpus_2017_linguagens.md`;
- contém o cronograma da apostila de Geografia;
- contém **material de terceiros**: PDFs de aulas de colegas (`impar-aulas/`, fora do git, 317 MB)
  e suas extrações em texto (`fontes/aulas-texto/`, versionadas), páginas fotografadas de livro
  (Crawford) e ilustrações DK; o roteiro de ensaio nomeia colegas.

### Estrutura proposta para o repositório unificado

```
proenem-workflow/
  README.md              porta de entrada para pessoas
  CLAUDE.md              porta de entrada para agentes (curta; aponta para docs/)
  docs/                  workflow ponta a ponta, "como adicionar uma área", decisões, historico/
  identidade/            logo canônico, paleta, fontes + CREDITOS.md   ← única cópia
  pipeline/              código de extração, classificação e análise
    config/areas.yaml    dia e intervalo de questões por ano e área
    prompts/             um prompt por área
  dados/                 manifesto das provas + CSVs canônicos (sem PDFs)
  aulas/AAAA-MM-DD-tema/ plano, slides, material e imagens próprias da aula
  apostila/              LaTeX; estilo-proenem.sty lê o logo de identidade/
  fontes-terceiros/      só o que tiver permissão registrada em CREDITOS.md
  .github/workflows/     compilar apostila, teste de fumaça do pipeline
```

Regras de assets:

1. **Identidade** (logo, paleta, fontes): uma cópia canônica em `identidade/`; slides, LaTeX e
   página on-line apontam para ela, nunca copiam.
2. **Imagens de conteúdo**: ficam junto da aula ou capítulo que as usa; uma cópia só.
3. **Todo asset tem procedência registrada** (`CREDITOS.md`: autor, origem, permissão/licença, data).
   É o que transforma uma contribuição em contribuição creditada e compartilhável.
4. **Material de terceiros só entra com permissão.** Sem ela, entra apenas a referência bibliográfica.
5. **Artefatos gerados** (`dist/`, `publicar/`, ZIPs, PDFs compilados) não vão para o git: são
   gerados pelas Actions ou publicados como *release*.

### Decisões pendentes do pesquisador

1. Topologia: repositório novo e unificado com histórico limpo (recomendado) × manter repositórios separados.
2. Quem higieniza: sessão local antes do envio (recomendado) × Fable na nuvem.
3. Permissões de terceiros: colegas autores das aulas em `impar-aulas/`, coautores citados nos roteiros,
   uso do logo; livros (DK, Crawford) só como referência.
4. Logo canônico: qual das duas versões.

---

## Atualização 2026-10-06 (2): `aula-geo-natureza` como modelo de referência da etapa "aula"

O pesquisador corrigiu o enquadramento: `aula-geo-natureza` não é um resto a recolher, é **o estudo de
caso que prova que a etapa final do workflow já foi feita de ponta a ponta num repositório só**. O
repositório unificado deve partir dele como modelo do "kit de aula" previsto em `PLANO_PRODUTO_PROENEM.md`.

### A cadeia que ele já implementa

```
fontes + checagem ─► argumento ─► plano de aula ─► roteiro de ensaio ─► slides ─► material complementar ─► página SPA
fontes/checagem.md   argumento.md  02-LaTeX/        05-roteiro-de-      03-slides/  02-LaTeX/material-      04-online/
(status de cada                    plano-de-aula    ensaio.md + .docx   (decks-    complementar           index.html + montar.sh
 número)                           (LaTeX)          (divisão entre      impress)   (LaTeX)                → Netlify
                                                    professores)
```

Além dos entregáveis, o **método** é o ativo mais transferível. Está em `aula-geo-natureza/CLAUDE.md`:
hierarquia de fontes (obra primária > dado conferido e datado > síntese de IA, que nunca é citável),
"nenhum número em slide sem visto em `checagem.md`", questão de vestibular só com prova e ano conferidos
(as outras marcadas como autorais), cada entregável parado em revisão antes do próximo, e a voz e as teses
do professor preservadas. Isso deve virar o protocolo geral de `docs/` e valer para qualquer área.

### O que hoje impede reproduzir o modelo fora desta máquina

1. **Framework de slides fora de qualquer repositório remoto.** `ferramentas/decks-impress/`
   (git local, **sem remoto**) tem alterações **sem commit** em `tools/build.mjs`, `tools/common.mjs` e
   `tools/runtime.js`, das quais dependem o prisma 3D, os mergulhos e as transições do deck atual. **Só
   existe uma cópia, neste disco.** `montar.sh` aponta para `ferramentas/decks-impress` por padrão.
   Também precisa de Node ≥ 20.11 e Chromium (lint, capturas, PDF).
2. **Dois estilos LaTeX para a mesma identidade:** `aula-geo.sty` (plano e complementar, copiado dentro de
   cada pasta) × `estilo-proenem.sty` (apostila). Há dois logos diferentes, e a paleta dos slides está
   em `theme.css`. No repositório unificado: um só pacote de identidade, que os três consomem.
3. **Dependências externas declaradas no próprio projeto:** `[acervo pessoal do autor: NotebookLM]/`,
   `[acervo pessoal do autor, fora do repositório]/` (dissertação, pessoal) e a transcrição original do webinar
   em `~/Transcrições/`. São do acervo do pesquisador e não entram; o modelo precisa funcionar sem elas.
4. **Material de terceiros e pessoal:** aulas de colegas (`impar-aulas/`, `fontes/aulas-texto/`), páginas
   de livros (DK, Crawford), nomes de colegas no roteiro, `fontes/NOTAS-WALKER-51.md` (sem commit).
5. **Estado em andamento:** branch atual `v3-tres-professores`, com arquivos sem commit; as versões anteriores
   estão no `master` e na tag `v3-data-centers`. Remoto só no pendrive.
6. **Artefatos de build misturados com a fonte:** `.aux`, `.log`, `.pdf` e `build/` dentro das pastas LaTeX.

### Como ele entra no repositório unificado (proposta)

- `aulas/2026-10-quem-paga-pelo-impacto/` passa a ser **o exemplo completo** (higienizado), com
  `fontes/checagem.md`, plano, roteiro, slides, complementar e SPA, e um `LEIAME.md` que explica a cadeia.
- `ferramentas/decks-impress/` (ou repositório próprio, como dependência) **com os patches em commit**.
- `identidade/`: um `.sty` e um `theme.css` derivados da mesma paleta e do logo canônico.
- `docs/protocolo-de-fontes.md`: o método acima, sem as referências à dissertação.
- Um modelo vazio, `aulas/_modelo/`, com as mesmas pastas: é o que outra área copia para começar.

### Ação de proteção recomendada (independe das demais decisões)

Fazer commit dos patches do `decks-impress` e levar o repositório a um remoto privado. É a única cópia
da ferramenta que gera os slides.
