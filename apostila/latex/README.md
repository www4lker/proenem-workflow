# Protótipo de apostila ProENEM

## Como abrir no Overleaf

1. Compacte ou use diretamente o arquivo ZIP entregue com este projeto.
2. No Overleaf, selecione **New Project > Upload Project**.
3. Envie o ZIP.
4. Mantenha `main.tex` como documento principal.
5. Use o compilador **pdfLaTeX**.

O projeto usa apenas pacotes comuns do TeX Live e não depende de fontes do
sistema nem de imagens externas. O diagrama da rede é desenhado em TikZ.

## Estrutura

- `main.tex`: ponto de entrada da compilação;
- `estilo-proenem.sty`: aparência global e ambientes pedagógicos;
- `capitulos/tempo-tecnologia-trabalho.tex`: conteúdo do subcapítulo;
- `referencias.bib`: base bibliográfica provisória;
- `MAPEAMENTO-WORD-LATEX.md`: correspondência entre os estilos do Word e os
  comandos LaTeX;
- `filtros/estilos.lua`: prova de conceito para uma futura conversão com Pandoc.

## Decisões ainda provisórias

- formato A4 e margens;
- paleta em azul-petróleo, ocre e verde;
- corpo em uma coluna;
- estilo bibliográfico autor-data ainda não ajustado integralmente à ABNT;
- nomes e quantidade dos boxes;
- permanência ou remoção da nota editorial no PDF dos estudantes.

Alterações visuais devem ser feitas prioritariamente em
`estilo-proenem.sty`. Assim, todos os capítulos são atualizados de uma vez.

