# Vocabulário: o que o usuário diz → o que fazer

Regra geral: o menor patch que produza o efeito, depois build + lint. Se a fala for ambígua, aplique a leitura padrão abaixo **e diga qual leitura usou**; só pergunte quando errar custar caro.

| O usuário diz | Operação em `layout.json` / `content/` |
|---|---|
| "mais perto de X" / "mais longe de X" | Mover 100–200 em x ou y na direção de X (ou oposta), respeitando a distância mínima (2000 em x, 1200 em y). Se já está no mínimo, diga. |
| "maior", "mais importante" | Subir um nível de escala (1→2→4) e reposicionar: a área no mundo quadruplica por nível, então vizinhos podem precisar se afastar. Avise. |
| "menor", "é detalhe" | Descer um nível de escala; se for detalhe de outro passo, colocá-lo abaixo dele. |
| "agrupa A e B" / "isso é um bloco só" | Criar moldura `fit` com A e B, posicionada na ordem de navegação logo antes do primeiro. |
| "esse vem antes" | Reordenar no array `steps` (posição no mundo não muda). Confira se o caminho da câmera ficou longo ou cruzado. |
| "está apertado" / "precisa respirar" | Cortar texto ou dividir o passo. Nunca reduzir a fonte. |
| "tá torto" / "estranho" | Rodar lint e `--only=id`. Se o lint está limpo, perguntar o que incomoda (alinhamento? proporção? vazio?). |
| "tira a rotação" | `rotate` → 0 (remover a chave). |
| "esse vídeo toca sozinho ao chegar" | `"media": {"autoplay": true, "autostop": true}`. `autopause` em vez de `autostop` para retomar de onde parou. |
| "põe a imagem aqui" | Pedir o arquivo (nome em `assets/`). Não baixar da web sem informar fonte e licença; crédito vai em `figcaption.fonte`. |
| "cor / fonte / clima" | Alterar tokens em `theme/theme.css`, ou `decks/<nome>/theme.css` se for só desta deck. Não espalhar valores nos passos. |
| "volta ao anterior" | Desfazer com git no arquivo em questão (`git restore`). |
| "quero ver o todo" | `--mapa`, ou peça que ele abra `debug.html` e aperte `m`. |

## Perguntas úteis na fase de argumento (uma rodada, curta)
- Quais são os blocos? (um nome curto cada)
- Quais relações entre eles importam para a fala: contém, deriva de, opõe-se a, exemplifica?
- Onde você quer que a plateia veja o todo antes do detalhe?
- Há trechos que são só sequência (primeiro isto, depois aquilo)? Esses ficam lineares.
