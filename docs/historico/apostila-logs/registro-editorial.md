# Registro editorial

Histórico cronológico do andamento do projeto. Ver `README.md` nesta pasta para o que entra aqui.

## 2026-08-16

- Reorganização da estrutura de pastas: `docs/` (handoff, transcrição, kit de distribuição) e `logs/` criadas na raiz. A fonte LaTeX foi extraída do ZIP para `proenem-reuniao/LaTeX-apostila/latex/`, que passa a ser a cópia de trabalho local editável diretamente (o ZIP `projeto-overleaf-proenem.zip`, na pasta acima, passa a ser gerado a partir dela via `empacotar-overleaf.sh` sempre que for preciso compartilhar/atualizar o Overleaf).

## 2026-10-05

- Projeto versionado no GitHub em repositório privado `www4lker/proenem-apostilas` (branch `main`). `audio-reunniao.mp3` fica fora do git (`.gitignore`), só no disco local.
- Auditoria para o legado ao PROENEM (detalhe em `proenem-enem/HANDOFF_legado_proenem.md`). Achados deste repositório:
  - `docs/transcricao-reuniao-proenem-geografia.md` traz nomes e avaliações de colegas e estudantes; já está no histórico remoto. Recomendação: tirar do repositório de entrega e deixar só uma ata de decisões sem nomes.
  - `docs/handoff-apostila-proenem-geografia.xml` e `CLAUDE.md` (l. 83) contêm leituras interpessoais e limites pessoais; reescrever em tom neutro antes de compartilhar com o grupo.
  - `docs/kit-prototipo-proenem.zip` e `projeto-overleaf-proenem.zip` duplicam arquivos já versionados; candidatos a release do GitHub.
  - `CLAUDE.md` ainda descreve o `.mp3`, que não está mais versionado.
  - A fonte LaTeX compila sem erros (`latexmk -pdf`, 4 páginas).
  - Falta ligar o corpus ENEM curado aos ambientes `questao`/`resolucao` do `estilo-proenem.sty`.
- Nada foi corrigido nesta sessão; só registrado.
