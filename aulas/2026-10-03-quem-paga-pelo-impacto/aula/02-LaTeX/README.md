# LaTeX: plano de aula e material complementar

Dois documentos separados com um estilo comum. Não segue a ABNT: é um estilo de apostila limpo,
em A4, com as cores do deck.

| Documento | Arquivo | Leitor | Conteúdo vem de |
|---|---|---|---|
| Plano de aula | `plano-de-aula/plano-de-aula.tex` | professor, coordenação | escrito direto no `.tex` (v1); `aula/01-plano-de-aula.md` é o histórico do v0 |
| Material complementar | `material-complementar/material-complementar.tex` | aluno | as 19 questões "C" de `fontes/enem-25-selecionadas.md` + redação |

O plano é escrito direto no `.tex`: é a fonte do plano a partir do v1, e o Markdown do v0 não é mais atualizado.
O material complementar ainda parte de `fontes/enem-25-selecionadas.md`; o texto de apoio à redação vai para
`aula/06-apoio-redacao.md` e depois para o `.tex`.

## Compilar
Use sempre `-interaction=nonstopmode`: sem ele, um erro de LaTeX deixa o `lualatex` esperando resposta no terminal
e o processo parece travado.
Precisa de TeX Live com `lualatex` e `latexmk` (as fontes TeX Gyre Pagella e Heros vêm com ele).
```
cd plano-de-aula && latexmk -interaction=nonstopmode -halt-on-error plano-de-aula.tex
cd material-complementar && latexmk -interaction=nonstopmode -halt-on-error material-complementar.tex
```
O PDF sai em `<documento>/build/`, que fica fora do git. Limpar: `latexmk -C`.

## Estilo comum (`estilo/`)
- `metadados.tex`: título, público, data e professor, iguais nos dois documentos.
- `aula-geo.sty`: fontes, cores, cabeçalho, caixas e macros:
  - `\averificar{9}`: marca vermelha no lugar de número ainda "a verificar" em `fontes/checagem.md`;
  - `\pendente{…}` e `\figura{…}`: trecho ou figura por fazer;
  - `\fonte{…}`, `\checagem{n}`, `\autoral`;
  - caixas `destaque` (o argumento é opção do tcolorbox: título com `[title={…}]`), `redacao` e `notaprofessor` (título como argumento);
  - `\questaoenem{id}{ano}{nº}{gabarito}`: recorte da prova oficial (`fontes/provas-recortes/<id>.png`);
  - ambiente `questaoautoral{gabarito}` e `\alternativas … \fimalternativas`;
  - `\imprimirgabarito`: tabela com as questões na ordem em que aparecem;
  - ambiente `roteiro`: tabela minuto · momento · conteúdo · recurso.

## Versão final
No `\usepackage{aula-geo}` do documento, use `\usepackage[final]{aula-geo}`. Aí qualquer
`\averificar`, `\pendente` ou `\figura` **impede a compilação**, e nada "a verificar" chega ao
papel. Sem `final`, o rodapé mostra "rascunho" e a versão.
