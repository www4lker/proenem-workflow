# Decks em impress.js — orientações para o agente

Apresentações espaciais (estilo Prezi) em impress.js v2.0.0, offline. Produto final: `<pasta-do-deck>/dist/index.html`.
Este arquivo é lido a cada turno: mantenha-o curto. Detalhes em `docs/vocabulario.md` e `docs/gotchas.md` (leia só quando precisar).

## Quem é o usuário
Pesquisador em humanidades (filosofia, geografia cultural, estudos culturais). Pensa em argumento e relação, não em CSS. Fala português, em termos visuais ("mais perto", "maior", "esse vem antes"): traduza para patches (`docs/vocabulario.md`). Não peça que ele escreva coordenadas ou HTML. Vá direto, sem preâmbulo; se um layout enfraquece o argumento, diga.

## Fonte da verdade (edite só isto)
`decks/<nome>/`
- `argumento.md` — blocos e relações (contém / deriva / opõe-se / exemplifica); o usuário aprova antes de qualquer coordenada
- `layout.json` — x, y, escala, rotação, ordem, mídia e `why` (justificativa espacial) de cada passo
- `content/<id>.html` — HTML interno de um passo (sem o `<div class="step">`)
- `assets/` — imagens, vídeos, fontes; referenciar como `assets/...`
- `notas-de-processo.md` — ver "Registro"

Global: `theme/theme.css` (tokens). `dist/` e `shots/` são gerados: nunca edite nem leia `dist/`.

## Regras
1. **Argumento antes de espaço.** Numa deck nova: uma rodada curta de perguntas sobre blocos e relações → `argumento.md` → proposta de `layout.json` com `why` em cada passo → **pare e espere aprovação**. Se o argumento é essencialmente sequencial, diga que o zoom não agrega e proponha layout linear.
2. **Menor patch.** Um passo por vez. Nunca regenere arquivo inteiro nem reescreva `layout.json` para mover um passo (edite o bloco do id). IDs são estáveis (kebab-case): o usuário aponta por eles.
3. **Sem coordenada inventada.** Use as convenções abaixo. Grupos com `fit`, nunca calculados à mão.
4. **Números antes de imagens.** Depois de cada mudança: build → lint (texto, barato). Screenshot só do que mudou ou foi sinalizado (`--only=id`) ou do mapa (`--mapa`). Nunca diga "ficou bom" sem ter rodado o lint. Não gere screenshot de todos os passos a cada iteração.
5. **Gosto é do usuário.** Cores e tipografia vêm dos tokens de `theme/theme.css`; não invente valores fora deles. Falta um token? Proponha, não improvise.
6. **O usuário decide olhando** `dist/debug.html` (ids sobre os passos, HUD, tecla `m` = mapa, `#/id` abre no passo). Feedback dele em português → patch. Commit só quando ele pedir.

## Comandos (de qualquer diretório; o deck pode estar em qualquer projeto)
```
<framework>/deck build <pasta>            # gera dist/index.html e dist/debug.html
<framework>/deck dev   <pasta>            # rebuild ao salvar (usuário só dá F5)
<framework>/deck lint  <pasta>            # estático + navegador; exit 1 se houver ERRO
<framework>/deck shots <pasta> --only=a,b # ou --mapa
<framework>/deck pdf   <pasta>            # shots/deck.pdf (cópia de segurança; sem movimento)
<framework>/deck impresso <pasta>         # shots/impresso.pdf (A4, para o aluno; ver README)
```
`<framework>` = `ferramentas/decks-impress`. Da raiz dele, `npm run build -- decks/<nome>` equivale.
Primeira vez: `npm i`. Navegador: `CHROMIUM_PATH`, senão o Chromium do Playwright, senão Chrome/Edge/Brave do sistema.
`decks/` aqui é área de rascunho (ignorada pelo git, salvo `demo` e `modelo`); o deck definitivo é versionado no projeto dele.

## Convenções espaciais
- Passo = 1920×1080 (tela cheia). **Escala = hierarquia**: 1 (argumento), 2 (guarda-chuva), 4, 8. Escala maior = maior *no mundo*, não na tela (na tela, o passo ativo sempre ocupa a tela).
- (0,0) = título. Leitura esquerda→direita; aprofundamento/detalhe para baixo; objeção/contra-argumento para cima.
- Grade de 100 (x, y múltiplos de 100). Distância mínima entre centros de passos escala 1: **2000 em x ou 1200 em y**. Folga mínima 80px (o lint acusa).
- Moldura: `{ "id": "grupo-x", "fit": ["a","b"], "pad": 200 }` (ou `"fit": "*"`). O build calcula posição e escala; é invisível, vira parada da câmera e acende os filhos.
- Mergulho (zoom de detalhe): passo pequeno (`"scale": 0.25` ou `0.5`, com `meta.scales` ampliado no deck) dentro de outro, com `"sobre": "<id-pai>"` (o lint não acusa a sobreposição com o pai nem entre detalhes do mesmo pai, nem a grade; o pai fica aceso; o detalhe não sai no impresso). `"transicao": <ms>` muda a duração da câmera ao chegar no passo.
- Rotação 0 por padrão; máx ±15°, só para ênfase; nunca em passo com vídeo. Sem 3D (z, rotateX/Y) salvo pedido.
- A ordem de navegação é a ordem do array `steps`. Não reordene sem avisar.

## Conteúdo
- Fonte ≥ 28px (`.fonte` ≥ 22px). Não cabe? Corte texto ou divida o passo; **nunca reduza a fonte**.
- Um passo = uma ideia (~45 palavras + figura, no máximo).
- Imagem: em `assets/`, largura natural ≤ 2× a exibida, `alt` obrigatório, `<figure>` + `<figcaption class="fonte">` com crédito.
- Versão impressa (`dist/impresso.html`): vídeo não sai; passo com vídeo leva um `<p class="so-impresso">` dizendo o que ele mostra.
- Vídeo: arquivo local, `<video muted playsinline>`; comportamento em `layout.json`: `"media": {"autoplay": true, "autostop": true}` (plugin de mídia do impress.js). Nada de YouTube, CDN ou Google Fonts: tudo offline.
- Citações: `<blockquote>` + `<cite class="fonte">` com referência completa. **Não invente referência**; sem fonte, escreva `[FONTE?]` visível.

## Economia de tokens
- Leia só o trecho de `layout.json` e o `content/<id>.html` em pauta. Não cole HTML na conversa; responda com o que mudou + saída do lint.
- Mover, renomear, ajustar mídia e rodar o lint são tarefas mecânicas: adequadas a modelo menor. Planejar layout e discutir argumento pedem o modelo maior.
- Sugira `/clear` ao fechar cada fase (argumento aprovado; layout aprovado; conteúdo).
- Se seu modelo não recebe imagens, use só o lint e peça ao usuário que descreva o que vê em `debug.html`. Não simule julgamento visual.

## Registro
Sempre que o usuário repetir uma correção ou explicar a mesma coisa pela segunda vez, acrescente uma linha em `notas-de-processo.md`: `DD/MM/AA — o que ele disse — o que faltava aqui`. É a matéria-prima da futura skill.

## Fora de escopo (não construa sem pedido)
Modo de edição por arrastar; conversor do Canvas do Obsidian; plugins extras do impress.js; temas novos; exportar PPTX.
