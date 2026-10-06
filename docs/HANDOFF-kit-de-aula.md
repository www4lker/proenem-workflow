# Handoff: kit de aulas reprodutível (prancheta)

> **Registro (06/10/2026).** Os itens abertos deste documento foram levados para [`docs/FILA.md`](FILA.md), que passa a ser a fonte única do que falta fazer. Este arquivo fica como contexto.

Aberto em 02/10/2026, véspera da aula "Quem paga pelo impacto?". **Estado: prancheta.** Nada daqui foi construído. Este
documento registra o problema, o que já existe, os riscos que dá para antecipar e as decisões que cabem ao professor.
Quem assumir este trabalho deve começar por aqui. O trabalho começa **depois da aula de 3/10**.

## 1. O problema

O professor considera a aula um sucesso, e ela produziu um conjunto completo:
- plano de aula e material complementar em LaTeX (documento para a coordenação);
- slides espaciais em impress.js, com versão impressa em PDF;
- uma página on-line (SPA) com questões corrigidas, slides navegáveis e o PDF, hospedada no Netlify.

Hoje esse resultado depende de três coisas que não se transmitem:
- a memória do agente;
- patches sem commit;
- caminhos desta máquina.

O objetivo é que outro professor, de outra disciplina, consiga repetir o processo **com ajuda de um agente** (não à mão),
partindo de um kit: um modelo de projeto, scripts, ambiente declarado e skills específicas.

## 2. O que esta aula provou: o processo real

Cada etapa produziu um arquivo e só avançou com o visto do professor.

| Etapa | Artefato nesta aula | Ferramenta | Visto |
|---|---|---|---|
| Ementa e recorte | `aula/aproveitamento-ementa.md` | agente | sim |
| Fontes e checagem | `fontes/checagem.md` (rank 1–3; número "a verificar" não vai ao aluno) | agente | por item |
| Questões | `fontes/provas-recortes/`, `recortar_questoes_inep.py` | Python + PDFs do INEP | sim |
| Argumento | `aula/03-slides/argumento.md` | agente | sim |
| Plano de aula | `aula/02-LaTeX/plano-de-aula/` | LaTeX (pdfLaTeX e LuaLaTeX) | sim |
| Slides | `aula/03-slides/` (`layout.json`, `content/`, `theme.css`, `prisma.py`) | decks-impress (Node + Chromium) | sim |
| Impresso | `shots/impresso.pdf` | decks-impress | junto com os slides |
| Página on-line | `aula/04-online/index.html`, `montar.sh` → `publicar.zip` | HTML estático + Netlify | sim |
| Registro | `logs/AAAA-MM-DD-sessao.md`, `HANDOFF.md`, `README.md`, commits | git | ao encerrar |

**O método está nas regras, não nas ferramentas.** Cinco delas fizeram a diferença:
- um entregável por vez, com visto;
- hierarquia de fontes;
- cortar o número em vez de verificar;
- questão de vestibular só com prova e ano conferidos;
- documento final sem rótulos internos.

O kit precisa carregar essas regras.

## 3. O ecossistema

| Peça | Onde | Papel | Git |
|---|---|---|---|
| Motor de análise de provas | `pipeline/` | corpus ENEM 2004–2025; 355 questões de Humanas extraídas e 348 classificadas; plano de produto ("kit de aula em 15 min") | 16 commits |
| Apostilas ProEnem | `apostila/` | apostila coletiva de Geografia; `estilo-proenem.sty`, Overleaf, conversão Word → LaTeX via Pandoc | **sem git** |
| decks-impress | `ferramentas/decks-impress/` | framework de slides: build, lint, shots e impresso | 2 commits + **patches sem commit** |
| SPA-HTML-NETLIFY | fora deste repositório | só um `index.html` | **sem git** |
| Esta aula | `aulas/2026-10-03-quem-paga-pelo-impacto/` | primeira aula completa: o **caso de referência** | sim |

Como as peças se ligam:

```
motor de provas ──questões classificadas──▶ aula ◀──capítulo / conteúdo──▶ apostila
                                              │
                         ┌────────────────────┼─────────────────────┐
                    LaTeX (plano,        decks-impress           página SPA
                    complementar)        (slides + PDF)          (Netlify)
```

O plano de produto do motor de provas já promete o que este kit entregaria: roteiro, questões, gabarito comentado,
versão do aluno, slides, plano B sem internet e protocolo de feedback. **O kit não é um projeto novo: é a ponte entre
esse plano e o que esta aula mostrou que funciona.**

## 4. Problemas a antecipar

Em ordem de gravidade.

1. **Perda de trabalho no framework.** O decks-impress tem patches sem commit: mergulhos, transição por passo, suporte 3D,
   `data-z` sempre emitido e as isenções do lint. Sem eles, este deck não compila. Se a pasta se perder, o deck da aula
   não se reconstrói.
2. **Peças sem git.** As apostilas e o SPA-HTML-NETLIFY não têm histórico. A apostila é coletiva: sem git, a versão
   válida fica ambígua.
3. **Ambiente não declarado.** Não há lista de versões nem script que confira o ambiente. Hoje funcionam:
   - TeX Live 2023 (Debian), com pdfLaTeX e LuaLaTeX;
   - Node 20 + Chromium (o Edge serve), para lint, shots e PDF;
   - Python 3.12 + Pillow;
   - poppler-utils (PDFs do INEP);
   - `libzbar`, para ler QR, e `qrencode`/`qrcode`, para gerar.
4. **Caminhos desta máquina.** `ferramentas/decks-impress/deck` aparece no `montar.sh`, nos handoffs e nos
   comandos.
5. **Conhecimento só na memória do agente.** Várias regras moram em `~/.claude/projects/…/memory/`, que não acompanha o
   projeto:
   - "LaTeX é documento final";
   - "o professor edita o `.tex` no TeXstudio/Kile";
   - "fonte proporcional ao pré-vestibular";
   - "leitor externo, sem rótulo interno";
   - "corpus PROENEM 2017+ de CH está errado".
6. **Geografia embutida no código.** Estão escritos para esta disciplina:
   - eixos, cores e o rodapé "Pro Enem • Geografia";
   - o estilo `aula-geo.sty`;
   - a regra sobre Milton Santos;
   - a geometria do prisma, ligada aos 8 blocos.
   O que é disciplina e o que é método ainda não está separado.
7. **Dois estilos LaTeX.** `aula-geo.sty` (aula) e `estilo-proenem.sty` (apostila) tendem a divergir.
8. **Direitos.** O kit não pode trazer o conteúdo desta aula como modelo distribuível sem antes decidir os direitos de:
   - as fotos de *O livro da ecologia*;
   - os recortes de prova do INEP;
   - o PDF não oficial usado só para localizar imagens.
9. **Erros conhecidos no motor de provas.** As linhas de "CH" de 2017, 2018, 2019 e 2025 são de Linguagens. O kit tem de
   carregar esse aviso, ou a próxima disciplina vai usar questões erradas.
10. **Dependência de agente.** Sem agente, hoje nada anda. É razoável que redação, curadoria e diagramação usem agente.
    Já build, lint, impresso, montagem e QR têm de rodar **sem** agente, com um comando.
11. **Agentes diferentes.** Há `AGENTS.md` (Codex) e `CLAUDE.md` (Claude Code) lado a lado. Uma skill escrita só para um
    agente prende o kit a ele.
12. **Quem vai usar.** Os professores voluntários usam Word e Overleaf e não usam git. Um kit que exija terminal e git
    atende um público pequeno.
13. **Publicação manual.** Hoje se publica no Netlify subindo um zip à mão, um site por aula. Com muitas aulas, isso vira
    dispersão.

## 5. Uma skill "faz tudo" teria utilidade?

**Não como uma skill única. Sim como um conjunto de skills pequenas, uma por etapa.**

**Por que não uma só.** O que funcionou nesta aula foi o ciclo "entregável → visto → próximo". Uma skill que faz tudo:
- tende a pular o visto;
- vira um prompt enorme, difícil de manter;
- mistura etapas determinísticas com etapas de juízo;
- falha em bloco: quando erra, erra tudo.

**O que serve.** Cada skill cobre uma etapa e tem quatro partes:
- entrada;
- saída;
- verificação automática;
- ponto de visto.

O "fazer tudo" fica com uma skill de orquestração, que só lê o `HANDOFF.md` e diz qual é a próxima etapa.

Esboço (nomes provisórios):

| Skill | Faz | Verificação | Visto |
|---|---|---|---|
| `aula-iniciar` | cria o projeto a partir do modelo; pergunta disciplina, data, dupla e ementa; gera `CLAUDE.md`/`AGENTS.md`, `HANDOFF.md`, `README.md` e `checagem.md` | estrutura criada | recorte |
| `aula-fontes` | curadoria com ranks; `checagem.md` | nenhum número "a verificar" no material do aluno | por item |
| `aula-questoes` | consulta o motor de provas, recorta do INEP, confere prova e ano e marca as autorais | gabarito × recorte | lista |
| `aula-argumento` | `argumento.md`: blocos, relações e tempos | soma dos tempos | sim |
| `aula-latex` | plano e complementar como documento final | compila em pdfLaTeX e em LuaLaTeX; nenhum rótulo interno | sim |
| `aula-deck` | layout, conteúdo e geometria (plana, octógono, prisma) | lint 0/0, shots, impresso | sim |
| `aula-online` | página SPA, `montar.sh`, zip e QR (gera e **lê** o QR) | links locais, QR lido, 375 px sem rolagem | sim |
| `aula-encerrar` | log, handoff, README e commit | `git status` limpo | — |
| `aula-proxima` | lê o handoff e diz a próxima etapa | — | — |

As skills seriam escritas no formato `SKILL.md`, para funcionar no Claude Code e caber num `AGENTS.md`. Juntas, podem
virar um plugin.

## 6. Arquitetura proposta

Proposta de prancheta: tudo a decidir.

```
kit-aulas-proenem/                 (nome a decidir)
  README.md                        o que é, para quem, como começar
  metodo/                          as regras do §2, escritas para quem não estava aqui
    regras-de-fonte.md             ranks, checagem, "cortar em vez de verificar"
    ciclo-de-visto.md              entregável → visto → próximo; o que vai ao log
    documento-final.md             LaTeX sem rótulos internos; leitor externo
    avisos-do-corpus.md            erros conhecidos do motor de provas
  modelo/                          esqueleto de uma aula (o que `aula-iniciar` copia)
    disciplina.yaml                nome, rótulo, logo, eixos, cores, regras próprias
    aula/02-LaTeX/  aula/03-slides/  aula/04-online/  fontes/  logs/
  estilos/                         um .sty base compartilhado com a apostila + camada por disciplina
  skills/                          as skills do §5
  ambiente/
    checar-ambiente.sh             confere versões e diz o que falta, sem instalar nada
    requisitos.md                  TeX Live, Node, Chromium, Python, poppler, zbar
  exemplos/
    geo-natureza/                  esta aula como caso de referência (sem o que tiver direito restrito)
```

**O decks-impress continua repositório próprio.** O kit fixa uma versão dele, por tag. **O motor de provas também.** O
kit lê o corpus por meio de um contrato simples (CSV com colunas definidas) e não pelos arquivos internos do motor.

**Reprodutibilidade em três níveis:**
1. **Ambiente:** `checar-ambiente.sh` com as versões testadas.
2. **Build:** um comando gera tudo a partir das fontes (PDFs LaTeX, deck, impresso, `publicar/`, zip), sem agente.
3. **Processo:** log e handoff com modelo fixo. Decisões do professor com data. Escolhas feitas sem pedido explícito,
   erros e testes em seções próprias. Esta aula já segue esse formato (`logs/2026-10-02-sessao.md`); falta escrever o
   modelo.

## 7. Decisões do professor

A primeira opção de cada pergunta é a recomendada.

1. **Onde mora o kit?**
   - Repositório novo (recomendado).
   - Dentro do motor de provas (`PROENEM/ENEM`).
   - Dentro do decks-impress.
2. **Para quem é a primeira versão?**
   - Professores do ProEnem que usam um agente, com o professor como guia (recomendado).
   - Só o professor e o agente.
   - Qualquer professor, sem terminal (exige interface: é outro projeto).
3. **Agentes:**
   - Formato aberto, que sirva ao Claude Code e ao Codex (recomendado).
   - Só Claude Code.
4. **LaTeX da aula e da apostila:**
   - Um estilo base compartilhado, com camada por disciplina (recomendado).
   - Estilos separados.
5. **Hospedagem:**
   - Um site do ProEnem com todas as aulas (recomendado a médio prazo).
   - Um site Netlify por aula (como hoje).
6. **Direitos:** o que do exemplo pode ir para um kit compartilhado? Ilustrações DK, recortes do INEP e textos.
7. **Teste de transmissão:** qual disciplina e qual professor adaptam primeiro?
8. **Patches do decks-impress:**
   - Commit num branch de lá (recomendado, e antes de qualquer outra coisa).
   - Deixar como está até o kit existir.

## 8. Próximos passos (nesta ordem, depois da aula)

1. **Proteger o que existe.** Isso depende das decisões 7.8 e 2:
   - commitar os patches do decks-impress;
   - pôr a apostila e o SPA no git.
   *(06/10/2026: feito. Os patches estão na origem, commit `3e17e14`, e em `ferramentas/decks-impress/`; o backup
   `aula/03-slides/decks-impress-patches.diff` foi removido.)*
2. **Retrospectiva de método.** Extrair dos logs (`logs/2026-09-30-sessao.md`, `logs/2026-10-02-sessao.md`) e do
   histórico do git:
   - o processo real: etapas, tempo de cada uma, onde houve retrabalho, quais vistos mudaram o rumo;
   - as regras que estão só na memória do agente.
   Resultado: `metodo/` em rascunho.
3. **Inventário de ambiente.** `checar-ambiente.sh`, rodado nesta máquina.
4. **Decisões do §7.**
5. **Esqueleto do kit + uma skill piloto:** `aula-online` ou `aula-encerrar`, as mais mecânicas, para testar o formato.
6. **Teste de transmissão:** outra disciplina monta uma aula com o kit. Anotar onde travou. Esse é o critério de sucesso:
   **outro professor, com um agente, produz plano, slides e página sem ter lido este repositório.**

## 9. O que não fazer

- Não construir o kit antes das decisões do §7: a prancheta existe para isso.
- Não generalizar o prisma, as cores ou os eixos antes de ver a segunda disciplina. Abstrair a partir de um caso só
  costuma errar o que é método e o que é disciplina.
- Não mexer no motor de provas nem nas apostilas a partir daqui. São projetos próprios: o kit só lê o que eles produzem.
- Não depender da memória do agente: toda regra que importa vai para `metodo/`.
