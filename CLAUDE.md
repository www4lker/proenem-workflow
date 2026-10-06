# CLAUDE.md

Orientação para agentes (Claude Code e similares) que trabalham neste repositório.

## O que é

Acervo do workflow docente do PROENEM reunido a partir de quatro projetos que nasceram separados.
**Ainda não é um projeto unificado:** cada pasta preserva o layout de origem. A tarefa principal
pendente é a unificação; o plano está em `docs/HANDOFF-construcao.md` (leia inteiro antes de mexer
na estrutura).

## Protocolo de sessão

O trabalho anda em rodadas: uma sessão do agente executa a fila; depois o autor (com uma sessão local)
revisa, testa e incorpora; a próxima sessão recomeça do ponto registrado.

1. **Abrir.** Ler `docs/FILA.md` (o que fazer), o log mais recente em `docs/logs/` (onde parou) e este arquivo.
   Para contexto, os handoffs em `docs/` (que são registro; a fila é quem manda). `git status` e `git log -5`:
   edições humanas entre sessões são a versão válida.
2. **Branch.** Usar o branch que o ambiente atribuir (a sessão na nuvem só consegue enviar para ele); se puder
   escolher, `fable/AAAA-MM-DD` a partir de `main`. Nunca commitar direto em `main`.
3. **Trabalhar na ordem da fila**, pulando o que estiver bloqueado. Uma tarefa por commit, com o código da
   tarefa no título (ex.: `F2: adiciona requirements e checagem de ambiente`).
4. **Registrar durante, não só no fim.** Depois de cada tarefa: atualizar o estado na `docs/FILA.md` e o log da
   sessão, commitar e fazer push. Se a sessão for interrompida (créditos, tempo), o registro já está salvo.
5. **Decisão que não é sua** (pedagógica, de direitos, de custo, de arquitetura difícil de desfazer): não
   decidir. Registrar em "Decisões pendentes" da fila no formato pergunta → opções → recomendação, e seguir com
   outra tarefa.
6. **Fechar.** Log em `docs/logs/AAAA-MM-DD-fable.md` com: tarefas feitas (com commit), **como cada uma foi
   verificada**, o que não foi testado, decisões novas para o professor e o próximo passo. Abrir um pull request
   para `main` com o resumo. Não fazer o merge: a sessão local revisa, testa e incorpora (decisão de 06/10/2026).

## Mapa

- `pipeline/`: extração (`extrair_prova.py`), classificação via Gemini CLI (`prompts/`,
  `.claude/skills/gemini-delegate/`), corpus em `corpus_enem/`, análises em `analise/`.
  A área é parâmetro (`pipeline/config/areas.yaml`); hoje só CH tem corpus classificado.
- `aulas/AAAA-MM-DD-tema/`: uma pasta por aula. A de 03/10 é o modelo de referência.
- `apostila/`: tem `CLAUDE.md` próprio; leia antes de editar.
- `ferramentas/decks-impress/`: tem `CLAUDE.md` próprio. `montar.sh` da aula aponta para cá
  (sobrescrevível pela variável `DECKS_IMPRESS`).
- `identidade/`: logo canônico (`logo/logo-pro-enem-versao-latex.png`). Os builds o leem daqui; não criar cópias.
- `docs/historico/`: documentos e logs das fases anteriores. Consulta, não instrução.

## Regras

- **Nunca** versionar `.env`, `.claude/settings.local.json` nem chaves de API. Chamar o Gemini tem
  custo: só com confirmação humana.
- Nomes de colegas aparecem pseudonimizados (Professor A, B, C…). Não tentar reidentificar; ver
  `docs/higienizacao.md`.
- Imagens marcadas "Imagem de terceiro removida" são avisos de mesmo tamanho. Só trocar pela
  original com permissão registrada em `CREDITOS.md`.
- Auditoria: seguir `docs/auditoria.md`. Conferência de fonte só vale com prova anexada (sha256, script, diff);
  classificação e interpretação são auditadas pelo professor, não por outro agente.
- Fontes: seguir `docs/protocolo-de-fontes.md` (nenhum número "a verificar" chega ao aluno; síntese
  de IA nunca é citável).
- A voz, as teses e o recorte das aulas são dos professores. O agente cura, verifica, rascunha e
  examina; não decide pelo grupo. Separe "decisão já tomada" de "recomendação técnica".
- Português com acentos; nomes de arquivo em português; Markdown simples.
