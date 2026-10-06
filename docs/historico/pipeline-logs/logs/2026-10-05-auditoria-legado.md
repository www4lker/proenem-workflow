# Log 2026-10-05 — Repositórios privados e auditoria para o legado

## Contexto

O pesquisador quer legar o corpus ENEM e as apostilas ao PROENEM (cursinho onde é
voluntário) e colocar os dois projetos em repositórios privados no GitHub. A pergunta
desta sessão foi se uma equipe de outra área (Física, Biologia) conseguiria continuar
o workflow completo só com o que está nos repositórios. O pedido foi deixar tudo preparado,
sem executar as correções.

## Feito

1. **GitHub (privado), conta www4lker**
   - `ENEM/` → `proenem-enem` (branch `master`; já era repositório, com 16 commits locais
     e nenhum remoto). O `.git` vazio de `PROENEM/` foi removido; a pasta externa não é repositório.
   - `APOSTILAS-PROENEM/` → `proenem-apostilas` (branch `main`, commit inicial).
   - `.gitignore`: `.claude/settings.local.json` agora é ignorado de forma explícita (tinha a chave do
     Gemini em texto puro; o ignore global do usuário já o cobria). A exceção
     `!Resultado_Analise_PROENEM_2026/*.pdf` versiona os PDFs próprios. No apostilas, `*.mp3`
     fica fora (gravação de reunião).
   - `core.fileMode=false` no `ENEM`: a cópia entre discos tinha mudado só as permissões de 27 arquivos.
   - Varredura de chaves (`AIza…`) nos arquivos versionados e no histórico: nenhuma encontrada.
2. **Auditoria somente leitura** dos dois repositórios. Resultado e plano em
   `HANDOFF_legado_proenem.md`.

## Verificações executadas

- Contagens CSV: `questoes_raw` 355, `batch_completo_clean` 350, `corpus_mestre` 355 (bate
  com `AGENTS.md`).
- Duplicatas por md5: 19 PNGs repartidos em 7 conteúdos distintos (`aula-04-07/*` × `relatorios/*`).
- Ambiente: sem `.venv`; `import fitz` falha; `pdftotext` e `gemini` disponíveis. **O Pass 1 não
  roda na máquina de origem sem preparo.**
- Apostila: `latexmk -pdf` numa cópia em scratchpad → compila, 4 páginas, sem erros.
- PDFs de `Resultado_Analise_PROENEM_2026/`: só percentuais agregados, sem nomes de alunos.
- Busca de termos pessoais: autoanálise docente em `DIAGNÓSTICO_TURMAS_ProEnem2026.md`;
  transcrição com nomes e avaliações de terceiros e handoff XML com leituras interpessoais
  no `proenem-apostilas`.

## Achados principais (detalhe no handoff)

- Pipeline com a área fixa no código (CH, dia 1, Q1–45). Isso bloqueia CN e é a causa do bug de 2017+.
- Prompt, matriz de competências e análise só servem para Humanas. CN depende de visão, e o Gemini CLI
  headless não tem visão.
- Sem README, sem requirements, sem manifesto das provas. A montagem do `prompt_completo` não está em script.
- Documentação de entrada contraditória, com arquivos e caminhos inexistentes (`/mnt/supersupa`,
  `/data/Downloads`, `C:\Users\walke`, scripts em `/dados/10-PROJETOS/...`).
- O conteúdo pessoal e de terceiros já está no histórico remoto. Recomendado criar um repositório de
  entrega novo, com histórico limpo.

## Não feito (de propósito)

- Nenhuma higienização, renomeação ou remoção de arquivos.
- Nenhuma reescrita de histórico.
- Nenhuma chamada ao Gemini.
