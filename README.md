# proenem-workflow

Workflow docente do **PROENEM** (pré-vestibular comunitário): do diagnóstico da turma à aula pronta,
com o corpus de questões do ENEM e a apostila no meio do caminho. Material produzido de forma
voluntária por Walker (professor de Geografia) e legado ao cursinho.

> **Estado:** acervo reunido e higienizado, **ainda não unificado**. Cada pasta mantém o layout do
> projeto de origem. A unificação (ferramentas comuns, área de conhecimento como parâmetro) está
> descrita em [`docs/HANDOFF-construcao.md`](docs/HANDOFF-construcao.md).

## O workflow em uma linha

```
diagnóstico da turma → corpus ENEM (seleção de questões) → plano de aula → materiais (LaTeX, slides, página) → apostila
```

| Etapa | Pasta | O que tem | Estado |
|---|---|---|---|
| Diagnóstico | [`diagnostico-turmas/`](diagnostico-turmas/) | Resultado agregado da prova diagnóstica 2026, por disciplina | Pronto (só percentuais, sem alunos) |
| Corpus ENEM | [`pipeline/`](pipeline/) | Extração e classificação de questões (Python + Gemini CLI) | Funciona só para Ciências Humanas; ver handoff |
| Aula (modelo) | [`aulas/2026-10-03-quem-paga-pelo-impacto/`](aulas/2026-10-03-quem-paga-pelo-impacto/) | Plano, roteiro de ensaio, PDFs LaTeX, deck de slides, página online | **Estudo de caso completo**; comece por aqui |
| Aula (anterior) | [`aulas/2026-07-04-trabalho-e-tecnologia/`](aulas/2026-07-04-trabalho-e-tecnologia/) | Curadoria de questões e kit de ensaio | Primeira versão do processo |
| Apostila | [`apostila/`](apostila/) | Protótipo Word → LaTeX/Overleaf | Protótipo em avaliação pela equipe |
| Ferramenta | [`ferramentas/decks-impress/`](ferramentas/decks-impress/) | Gerador de slides (impress.js) usado pela aula modelo | Funciona (Node 20.11+) |
| Identidade | [`identidade/`](identidade/) | Logo do PROENEM | Logo canônico definido (versão LaTeX) |
| Documentação | [`docs/`](docs/) | Handoffs, plano de produto, protocolos, histórico | — |

## Por onde começar

0. **O que falta fazer:** [`docs/FILA.md`](docs/FILA.md), a fonte única das tarefas abertas. **O workflow ponta a
   ponta**, etapa por etapa, com "como adicionar uma área": [`docs/workflow.md`](docs/workflow.md).
1. **Professor de outra área** (Física, Biologia…): leia [`docs/HANDOFF-kit-de-aula.md`](docs/HANDOFF-kit-de-aula.md)
   e abra a aula modelo. O processo vale para qualquer disciplina; o pipeline do corpus ainda não.
2. **Quem vai construir o projeto unificado** (pessoa ou agente): leia [`CLAUDE.md`](CLAUDE.md) e
   [`docs/HANDOFF-construcao.md`](docs/HANDOFF-construcao.md).
3. **Regras de fonte e de crédito:** [`docs/protocolo-de-fontes.md`](docs/protocolo-de-fontes.md) e
   [`CREDITOS.md`](CREDITOS.md).

## Instalação

Testado em Ubuntu 24.04 (é o que a sessão na nuvem e o GitHub Actions usam). O que cada parte precisa:

| Parte | Precisa de |
|---|---|
| Pipeline do corpus (`pipeline/`) | Python 3.10+ com `requirements.txt`; `pdftotext` (poppler-utils) |
| Apostila e PDFs da aula (LaTeX) | TeX Live com `latexmk`, `pdflatex` (apostila) e `lualatex` (aula); fontes TeX Gyre em OpenType |
| Slides (`ferramentas/decks-impress`) | Node 20.11+; Chromium para o lint no navegador, capturas e PDF |
| Classificação das questões (opcional, **paga**) | Gemini CLI e uma chave própria em `.env` (modelo em `.env.example`) |

```bash
# Ubuntu/Debian
sudo apt-get install -y --no-install-recommends python3-venv poppler-utils \
  texlive-luatex texlive-latex-extra texlive-fonts-recommended texlive-lang-portuguese \
  texlive-plain-generic tex-gyre fonts-texgyre latexmk

# Python
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

# Slides (uma vez)
(cd ferramentas/decks-impress && npm ci)

# O que falta?
bash scripts/checar-ambiente.sh
```

`scripts/checar-ambiente.sh` lista o que está instalado e o que falta, sem instalar nada. Se o Chromium não
estiver no PATH, aponte-o em `CHROMIUM_PATH` (o Chromium do Playwright também serve).

## Compilar o que já existe

```bash
# Apostila (pdflatex)
cd apostila/latex && latexmk -pdf main.tex

# PDFs da aula modelo (lualatex; saída em build/)
cd aulas/2026-10-03-quem-paga-pelo-impacto/aula/02-LaTeX/plano-de-aula && latexmk -r latexmkrc plano-de-aula.tex
cd aulas/2026-10-03-quem-paga-pelo-impacto/aula/02-LaTeX/material-complementar && latexmk -r latexmkrc material-complementar.tex

# Slides da aula modelo
cd aulas/2026-10-03-quem-paga-pelo-impacto
../../ferramentas/decks-impress/deck build aula/03-slides
../../ferramentas/decks-impress/deck lint aula/03-slides
```

O logo que os três usam é o de `identidade/` (ver `identidade/LEIAME.md`). O pipeline do corpus precisa da chave
**própria** do Gemini só na etapa de classificação; nenhuma chave está neste repositório.

## Privacidade

Este repositório passou por higienização antes do primeiro commit: nomes de colegas pseudonimizados,
material de terceiros sem permissão registrada removido ou substituído por aviso, caminhos de máquina
retirados. O que saiu e por quê: [`docs/higienizacao.md`](docs/higienizacao.md).
