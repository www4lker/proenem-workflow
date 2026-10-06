# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este repositório

Não é um projeto de software: é o material de planejamento e o protótipo técnico de uma apostila didática (ProENEM, disciplina de Geografia), produzida colaborativamente por uma equipe de professores voluntários.

Estrutura (dentro de `apostila/` no repositório unificado):
- `definicao.md` — definição do projeto em 300 caracteres + matriz SWOT.
- `latex/` — **a fonte LaTeX de trabalho, em arquivos soltos** (ver abaixo). Edite e compile diretamente aqui.
- `empacotar-overleaf.sh` — gera `projeto-overleaf-proenem.zip` a partir de `latex/` para upload no Overleaf. O ZIP é artefato: não vai para o git.
- `modelo-word-vazio.docx` / `modelo-word-preenchido.docx` — template Word de autoria (vazio e preenchido de exemplo).
- O PDF de demonstração não é versionado: compile `latex/main.tex`.
- Histórico editorial: `docs/historico/apostila-logs/` na raiz do repositório.

## Trabalhando com a fonte LaTeX

`latex/` contém:
```
main.tex                              # ponto de entrada da compilação
estilo-proenem.sty                    # template visual + ambientes pedagógicos (fonte única de verdade visual)
capitulos/tempo-tecnologia-trabalho.tex  # conteúdo de um subcapítulo (piloto)
referencias.bib                       # bibliografia (estilo autor-data, plainnat)
filtros/estilos.lua                   # filtro Lua para Pandoc (prova de conceito de conversão Word→LaTeX)
README.md                             # instruções de uso no Overleaf
MAPEAMENTO-WORD-LATEX.md              # tabela de correspondência Word → LaTeX
```

Edite os arquivos diretamente aí e compile localmente:

```bash
cd latex

latexmk -pdf -interaction=nonstopmode main.tex
# ou, sem latexmk (rodar 2x para sumário/citações + bibtex para bibliografia):
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

# limpar auxiliares do latexmk (mantém main.pdf)
latexmk -c
```

Quando o conteúdo estiver pronto para compartilhar/atualizar no Overleaf, regenere o ZIP a partir de `latex/`:

```bash
empacotar-overleaf.sh
```

O script exclui artefatos de build (`.aux`, `.log`, `.bbl`, `.fls`, `main.pdf` etc.) para manter o ZIP limpo. **Nunca edite dentro do ZIP** — ele é sempre derivado de `latex/`; editar só o ZIP cria divergência silenciosa na próxima vez que o script rodar.

Só usa pacotes comuns do TeX Live (nenhuma fonte de sistema, nenhuma imagem externa); o diagrama de rede é feito em TikZ, não é uma imagem importada.

## Arquitetura editorial: Word → LaTeX

O fluxo de autoria é o núcleo do projeto e determina como qualquer mudança deve ser feita:

1. **Word é a interface de autoria.** Professores escrevem no `modelo-word-*.docx` aplicando **estilos semânticos** do Word (ex.: "Questão central", "Conceito-chave", "Atividade") — não formatação manual.
2. **`estilo-proenem.sty` é o template visual único.** Toda mudança de aparência (cores, caixas, cabeçalho, tipografia) deve ser feita ali, nunca em um `capitulos/*.tex` individual — isso propaga a mudança para todos os capítulos de uma vez.
3. **Os arquivos `capitulos/*.tex` contêm só estrutura e conteúdo**, usando os ambientes definidos em `estilo-proenem.sty` (`questaocentral`, `conceito`, `frasechave`, `exemploconcreto`, `atividade`, `questao`, `resolucao`, `notaeditorial`).
4. A correspondência exata entre estilo do Word e ambiente/comando LaTeX está em `MAPEAMENTO-WORD-LATEX.md` — use-a como referência ao converter um capítulo novo.
5. `filtros/estilos.lua` é uma prova de conceito de conversão automática via Pandoc (`pandoc entrada.docx -f docx+styles -t latex --lua-filter=filtros/estilos.lua --extract-media=imagens -o convertido.tex`). Ainda **não trata** alternativas de questão, tabelas, figuras, citações bibliográficas nem notas — hoje a conversão de um capítulo real é feita manualmente.
6. **Depois que um capítulo é importado para o LaTeX, o `.docx` deixa de ser fonte de verdade.** Correções são feitas sobre o PDF revisado e incorporadas de volta ao `.tex` central — não gerar um novo Word integral substituindo o que já foi convertido, pois isso cria divergência silenciosa entre as duas fontes.

## Convenções do conteúdo

- Caixas `notaeditorial` (fundo vermelho) marcam pendências editoriais explícitas — ex.: o capítulo-piloto tem uma nota sinalizando inconsistência entre "ENEM 2015, questão 02" e "Questão 03" nas referências do plano original. Essas caixas **devem ser removidas antes da edição final para os estudantes**; não as trate como conteúdo definitivo nem as apague sem resolver a pendência que sinalizam.
- Entradas em `referencias.bib` frequentemente têm `note = {...}` sinalizando metadados a confirmar (edição, ano, acesso). Não finalize uma referência sem checar se essa nota de pendência ainda está lá.
- Citações usam `natbib` com `\citep{}` e estilo `plainnat` (autor-data). A adequação plena ao padrão ABNT ainda **não** está resolvida — é uma questão em aberto do projeto, não trate como decidida.

## Contexto e restrições do projeto

- O fluxo Word → LaTeX/Overleaf é um **protótipo em avaliação pela equipe**, não uma decisão definitiva do grupo. Não afirme que a adoção do LaTeX está decidida.
- O papel técnico (conversão, revisão, bibliografia, tratamento de imagens e manutenção) precisa ser dividido numa equipe editorial: o projeto não se sustenta concentrado numa pessoa.
- Autores/professores devem continuar podendo trabalhar só no Word — não exigir que aprendam LaTeX, Git ou instalação local.
- Há várias questões editoriais explicitamente em aberto (política de exercícios oficiais vs. autorais, sistema ABNT exato, política de proveniência de imagens/uso de IA, seção "Tira-dúvidas" ainda ausente do template Word v0.1, governança de acesso ao Overleaf). Ao propor mudanças estruturais, deixe claro quando algo implementa uma decisão já tomada pelo grupo e quando é uma recomendação técnica ainda sem aprovação coletiva.
