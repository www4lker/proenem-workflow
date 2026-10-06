# decks-impress

Apresentações espaciais (estilo Prezi) em impress.js, feitas com um agente (Claude Code) e
verificadas por script. Tudo offline: o produto é uma pasta `dist/` que abre em qualquer navegador.

## Instalar (uma vez por máquina)
```
cd ferramentas/decks-impress && npm i     # Node >= 20.11
```
Lint, screenshots e PDF precisam de um navegador Chromium. O framework usa, nesta ordem:
`CHROMIUM_PATH`, o Chromium do Playwright (`npx playwright install chromium`, ~150 MB) ou
um navegador do sistema (Chrome, Chromium, Edge, Brave). Nesta máquina, o Edge basta.

## Onde mora o deck
O framework é a **ferramenta**; o deck é **conteúdo** e mora no projeto dele.

- **Recomendado:** a pasta do deck fica no repositório do projeto (ex.:
  `aula-geo-natureza/aula/03-slides/`) e é versionada lá. As ferramentas rodam por caminho:
  `…/decks-impress/deck build aula/03-slides`.
- **Rascunho rápido:** `decks/<nome>/` aqui dentro. O git do framework ignora tudo em `decks/`
  exceto `decks/demo` e `decks/modelo`; mova a pasta para o projeto quando ela virar coisa séria.

Só duas coisas são globais: `theme/theme.css` (tokens) e `vendor/impress.js`. Um deck pode
sobrepor tokens com o seu próprio `theme.css`.

## Fluxo de ponta a ponta
1. **Novo deck:** `cp -r decks/modelo <destino>` (esqueleto vazio) ou copie `decks/demo`
   e apague `content/*`, `assets/*` e os passos.
2. **Argumento:** preencha `argumento.md` com o agente (blocos + relações: contém, deriva,
   opõe-se, exemplifica). Você aprova.
3. **Layout:** o agente propõe `layout.json` (posição, escala, ordem e um `why` por passo). Você aprova.
4. **Conteúdo:** o agente escreve `content/<id>.html`, um passo por vez.
5. **Olhar e corrigir:** `deck dev <pasta>` reconstrói ao salvar; abra `dist/debug.html`
   (ids sobre os passos, `m` = mapa, `0` = início, `#/id` abre num passo), comente em
   português, dê F5.

## Comandos
```
deck build <pasta>                # dist/index.html (apresentar) e dist/debug.html (revisar)
deck dev   <pasta>                # rebuild ao salvar
deck lint  <pasta>                # texto: fonte, overflow, sobreposição, mídia; exit 1 se ERRO
deck shots <pasta> --only=a,b     # ou --mapa; PNGs em <pasta>/shots/
deck pdf   <pasta>                # <pasta>/shots/deck.pdf (reserva, sem movimento)
deck impresso <pasta>             # <pasta>/shots/impresso.pdf (A4 paisagem, para o aluno)
```
`deck` é o script na raiz deste repositório (use o caminho completo, ou um alias). Dentro
dele, `npm run build -- decks/<nome>` faz o mesmo.

## Versão impressa (para o aluno)
O build gera também `dist/impresso.html`: os passos de conteúdo em sequência, um por folha A4
paisagem, fundo branco, texto de verdade (não imagem). Imprime com Ctrl+P de qualquer navegador,
ou `deck impresso <pasta>` salva o PDF. Vídeo não sai no papel. Para texto que só vale num
dos meios: `<p class="so-impresso">` (só no papel, ex.: o que o vídeo mostra) e
`<p class="so-tela">` (só na projeção). O `deck pdf` continua sendo a reserva da projeção
(imagens 16:9, inclui as molduras).

## Quem edita o quê
| Você | Agente |
|---|---|
| decide o argumento e aprova o mapa | propõe e ajusta `layout.json`, escreve `content/*.html` |
| olha `debug.html` e comenta em português | traduz em patch mínimo, roda build + lint |
| escolhe cores/tipografia (`theme/theme.css`) | usa só os tokens |
| decide o que vira skill (`notas-de-processo.md`) | anota o que você precisou repetir |

## Antes de apresentar
- `deck lint <pasta>` sem ERRO; `deck pdf <pasta>` como reserva.
- Leve a pasta `dist/` inteira e abra `index.html` **no computador e navegador da sala**, com o vídeo que vai usar.

Detalhes: `CLAUDE.md` (regras do agente), `docs/vocabulario.md`, `docs/gotchas.md`.
Licenças: `vendor/impress.js` é MIT (Bartek Szopka, ver `vendor/impress.LICENSE`).
