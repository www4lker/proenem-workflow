# CLAUDE.md

Orientação para agentes (Claude Code e similares) que trabalham neste repositório.

## O que é

Acervo do workflow docente do PROENEM reunido a partir de quatro projetos que nasceram separados.
**Ainda não é um projeto unificado:** cada pasta preserva o layout de origem. A tarefa principal
pendente é a unificação; o plano está em `docs/HANDOFF-construcao.md` (leia inteiro antes de mexer
na estrutura).

## Ao iniciar uma sessão

1. Ler `README.md`, `docs/HANDOFF-construcao.md` e, para a etapa aula, `docs/HANDOFF-kit-de-aula.md`.
2. `git status` e `git log -5`: edições humanas entre sessões são a versão válida.
3. Ao encerrar: registrar o que foi feito no handoff correspondente e fazer commit.

## Mapa

- `pipeline/`: extração (`extrair_prova.py`), classificação via Gemini CLI (`prompts/`,
  `.claude/skills/gemini-delegate/`), corpus em `corpus_enem/`, análises em `analise/`.
  **Área fixa em Ciências Humanas no código**; generalizar é a prioridade nº 1 do handoff.
- `aulas/AAAA-MM-DD-tema/`: uma pasta por aula. A de 03/10 é o modelo de referência.
- `apostila/`: tem `CLAUDE.md` próprio; leia antes de editar.
- `ferramentas/decks-impress/`: tem `CLAUDE.md` próprio. `montar.sh` da aula aponta para cá
  (sobrescrevível pela variável `DECKS_IMPRESS`).
- `identidade/`: logo. Não há logo canônico decidido; as cópias dentro da aula ficam até a decisão.
- `docs/historico/`: documentos e logs das fases anteriores. Consulta, não instrução.

## Regras

- **Nunca** versionar `.env`, `.claude/settings.local.json` nem chaves de API. Chamar o Gemini tem
  custo: só com confirmação humana.
- Nomes de colegas aparecem pseudonimizados (Professor A, B, C…). Não tentar reidentificar; ver
  `docs/higienizacao.md`.
- Imagens marcadas "Imagem de terceiro removida" são avisos de mesmo tamanho. Só trocar pela
  original com permissão registrada em `CREDITOS.md`.
- Fontes: seguir `docs/protocolo-de-fontes.md` (nenhum número "a verificar" chega ao aluno; síntese
  de IA nunca é citável).
- A voz, as teses e o recorte das aulas são dos professores. O agente cura, verifica, rascunha e
  examina; não decide pelo grupo. Separe "decisão já tomada" de "recomendação técnica".
- Português com acentos; nomes de arquivo em português; Markdown simples.
