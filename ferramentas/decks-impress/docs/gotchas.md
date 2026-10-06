# Gotchas do impress.js

Cada item traz a origem: **[testado]** neste repo (Chromium/Playwright, deck de exemplo), **[código]** lido no impress.js v2.0.0, **[Anticon]** relato do deck `almoretti/anticon-presentation` (não verificado por nós), **[não testado]**.

## Modelo espacial
- `data-x/y/scale/rotate` movem a **câmera/posição do passo**, não o conteúdo. Dentro de `.step`, CSS normal (flex, grid, position) funciona. [código][Anticon]
- `data-scale` de um passo é o tamanho dele no mundo. Na tela, o passo ativo sempre é ajustado à janela: um passo de escala 4 é 4× maior que os vizinhos de escala 1, mas ocupa a tela inteira quando ativo. [código]
- Passo posicionado pelo **centro** (x, y são o centro), não pelo canto. [código]
- `impress().goto("id", 0)` navega sem transição; útil para captura e lint. [testado]
- O impress.js v2.0.0 vem com plugin de mídia: `data-media-autoplay`, `data-media-autostop`, `data-media-autopause` no passo. [código][testado: autoplay de `.webm` funcionou ao entrar no passo, em Chromium com `--autoplay-policy=no-user-gesture-required`]
- Padrão do v2.0.0: `maxScale: 3` (limita o zoom-to-fit da janela, ex.: monitores muito grandes). O build define `data-max-scale="20"`. O relato da Anticon diz que o padrão cortava a slide de revelação dela; não sabemos se é a mesma causa. [código][Anticon]

## CSS
- `.step` tem `overflow: hidden` no nosso tema: conteúdo demais é **cortado em silêncio**. O lint acusa (`overflow`, `elemento-fora-do-passo`). [testado]
- Padding em % de elemento absolutamente posicionado resolve contra a largura do bloco de contenção, não a do elemento: use px ou em. [Anticon]
- Namespace de classes (`.titulo-postit`, não `.postit`): colisões silenciosas. [Anticon]
- Transform no estado base e transform no `.active` **substituem-se**, não se compõem. [Anticon]
- `background-size: 100% 100%` distorce imagens de proporção diferente; use `contain`/`cover`. [Anticon]

## Fontes e mídia (offline)
- Nada de Google Fonts/CDN. Fontes locais: `.woff2` em `decks/<nome>/assets/fonts/` + `@font-face` em `decks/<nome>/theme.css`. [design do repo]
- Vídeo: use `.webm` (VP8/VP9) ou `.mp4` (H.264). O Chromium do Playwright **não decodificou H.264**: um `.mp4` (libx264) gerou `midia-nao-carrega` e `autoplay-falhou` no lint, embora deva tocar no Chrome/Firefox da sala. Esses dois avisos em `.mp4` podem ser falso alarme; confirme no navegador real. Prefira `.webm` quando puder converter (`ffmpeg -i in.mp4 -c:v libvpx-vp9 -b:v 1M out.webm`, não testado com VP9). [testado]
- Navegadores bloqueiam autoplay **com som** sem interação prévia. `muted` sempre pode. Com som, a primeira tecla/clique do apresentador costuma liberar, mas confirme no computador da sala. [não testado nesta sala]
- Não rotacione passos com vídeo. [convenção do repo]

## Playwright / captura
- Tempo de assentamento: as transições do CSS são desligadas na captura e o `goto` espera 600 ms; se o deck ganhar animações próprias, aumente em `tools/browser.mjs`. [testado]
- Confie em screenshot, não em cálculo, para julgar layout. Mas o lint é mais barato: rode-o antes. [Anticon][decisão do repo]
- Bloquear teclas durante automação (uma tecla perdida navega). Nossos scripts não enviam teclas. [Anticon]
- A versão do pacote `playwright` precisa casar com o Chromium instalado: sem isso o lint falha com "Executable doesn't exist". Resolva com `npx playwright install chromium` ou aponte `CHROMIUM_PATH`. [testado]

## Revisão por subagente
O deck da Anticon usa um subagente que critica screenshots; o autor relata que uma sugestão dele **piorou** um slide. Trate crítica visual de modelo como sinal, não como veredito. [Anticon]
