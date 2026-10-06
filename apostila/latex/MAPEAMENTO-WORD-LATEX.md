# Mapeamento entre o modelo Word e o LaTeX

O modelo Word é a interface de autoria. O arquivo `estilo-proenem.sty` é o
template visual. O capítulo `.tex` contém apenas estrutura e conteúdo.

| Estilo no Word | Saída semântica no LaTeX |
|---|---|
| Title | título do subcapítulo |
| Subtitle | subtítulo |
| Heading 1 | `\\section{}` |
| Heading 2 | `\\subsection{}` |
| Questão central | `questaocentral` |
| Conceito-chave | `conceito` |
| Frase-chave | `frasechave` |
| Exemplo concreto | `exemploconcreto` |
| Atividade | `atividade` |
| Questão | `questao` |
| Resolução comentada | `resolucao` |
| Nota para diagramação | `notaeditorial` |
| Legenda de figura | `\\caption{}` |
| Fonte de figura | `\\fontefigura{}` |
| Referência | entrada em `referencias.bib` |

## Estado deste protótipo

A conversão do exemplo preenchido foi normalizada manualmente para que o
primeiro teste avalie o modelo editorial e o resultado visual. O filtro
`filtros/estilos.lua` demonstra que o Pandoc consegue reconhecer os estilos
personalizados e convertê-los em ambientes LaTeX, mas ainda não trata todos os
casos: alternativas, tabelas, figuras, citações bibliográficas e notas precisam
de regras adicionais antes da automação em escala.

## Regra de trabalho proposta

1. O professor escreve no Word e aplica estilos semânticos.
2. A equipe editorial encerra as alterações no Word.
3. A equipe técnica converte e normaliza o capítulo localmente.
4. Apenas o `.tex`, as imagens e a bibliografia entram no projeto Overleaf.
5. Correções posteriores são feitas sobre o PDF e incorporadas à fonte central.

