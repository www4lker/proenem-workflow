# Identidade visual

Lugar único dos elementos de identidade do PROENEM. Novos materiais devem buscar o logo **aqui**, não
em cópias espalhadas.

| Arquivo | Tamanho | Uso |
|---|---|---|
| `logo/logo-pro-enem-versao-latex.png` | 691 × 970 | **Logo canônico** (decisão de 06/10/2026). PDFs LaTeX e deck de slides da aula modelo |
| `logo/origem/asset1.jpeg`, `asset2.jpeg` | — | Arquivos recebidos, sem tratamento |

## Como os builds chegam até aqui

Nenhum build copia o logo para dentro da aula; todos o leem desta pasta.

- **LaTeX da aula** (`aula-geo.sty`): `\aulalogo` aponta para `identidade/logo/logo-pro-enem-versao-latex.png`
  por caminho relativo à pasta de compilação. Para compilar uma aula fora do repositório, redefina `\aulalogo`
  no preâmbulo.
- **Deck de slides**: `aula/03-slides/assets/img/logo-pro-enem.png` é um link simbólico para o arquivo canônico.
  O `deck build` segue o link e grava o arquivo real em `dist/`, que continua autossuficiente para publicar.
- **Apostila** (`estilo-proenem.sty`): ainda não usa logo.

A versão de slides (399 × 560) saiu de uso em 06/10/2026 (tarefa F1). O logo tem 691 px de largura e aparece com
~200 px no título do deck: o lint do deck emite um aviso de imagem grande, que fica até existir uma versão vetorial.
Desejável: obter o logo em SVG ou PDF com o PROENEM.

O logo pertence ao PROENEM; uso restrito ao material do cursinho (ver `CREDITOS.md`).
