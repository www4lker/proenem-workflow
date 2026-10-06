# Handoff da frente de slides (sessão paralela)

> **Registro (06/10/2026).** Os itens abertos deste documento foram levados para [`docs/FILA.md`](../../../../docs/FILA.md), que passa a ser a fonte única do que falta fazer. Este arquivo fica como contexto.

> **02/10/26, branch `ementa-geo-natureza`:** o deck foi refeito como "Quem paga pelo impacto?" (ementa
> Geografia e Natureza). O esqueleto vigente é `argumento.md` v3; o estado está no `HANDOFF.md` da raiz. O que segue
> abaixo descreve o deck de data centers (no `master` e na tag `v3-data-centers`) e fica como histórico.
>
> **02/10/26, depois do visto:** mergulhos (`"sobre": "<pai>"`, classe `mergulho`, escala 0.25–0.35) e transição por
> passo (`"transicao": ms`) dependem de patches **sem commit** no framework (`tools/common.mjs`, `build.mjs`,
> `runtime.js`). O último passo (`material-online`) mostra `assets/img/qr-material.png`, hoje provisório. A cópia
> navegável de casa é montada por `aula/04-online/montar.sh`.
>
> **02/10/26, tratamento final:** a geometria sai de `octogono.py`, que reescreve x, y e rotate no `layout.json`. Cada
> bloco ocupa um lado de um octógono (rotate de −315 a 0, +45 por lado), com o título no centro e `material-online` logo
> abaixo. Para mudar um passo de lado, edite `LADOS` e rode `python3 octogono.py`. `meta.maxRotate` vale 360. Saíram
> `mapa-inicial` e as molduras de eixo; só fica `mapa-final`. Aberturas `abertura-*` com imagem em `assets/img/dk/`
> (fotos do livro físico; mapa em `fontes/dk-ecologia-mapa.md`). Cor por eixo pelas classes `eixo-*`.
>
> **02/10/26, prisma 3D:** `octogono.py` saiu (a versão plana fica no commit `faf27d2`). A geometria agora sai de
> `prisma.py`, que grava x, y, z, rotateX e rotateY no `layout.json`. Cada bloco ocupa uma face de um prisma octogonal
> em pé (apótema 2700, rotateY 0 a 315); os slides descem pela face e as aberturas formam o anel de cima. O título e
> `material-online` ficam deitados na tampa (rotateX 90). A moldura `mapa-final` usa `camera` (vista de cima, rotateX 40,
> escala 7). Para mudar um passo de face, edite `FACES` e rode `python3 prisma.py`. As cores das faixas (`--c-barra`)
> e dos títulos (`--c-eixo`) vêm da ilustração de cada abertura. Patches 3D no framework (sem commit): `data-rotate-x`,
> `data-rotate-y`, `data-z` sempre emitido (o plugin `rel` do impress herda o z do passo anterior),
> `meta.perspective`, `camera` em molduras e isenção de sobreposição e de grade para passos 3D.
>
> **02/10/26, um QR só:** `material-online` mostra só `qr-material.png` (QR real do Netlify, classe `.qr-unico`); o QR do
> PDF saiu, porque a página on-line já tem o botão do PDF (o PDF também fica no Netlify, dentro de `publicar/`). O `montar.sh` apaga o `dist/` antes do build: o build não
> remove assets que saíram do deck.

Atualizado em 30/09/26. Esta sessão cuida de `aula/03-slides/` e do framework
`ferramentas/decks-impress/` (commits `1f3fede`, `e306bea`). **Não faz commit no repo da
aula:** os arquivos daqui ficam soltos até a sessão da aula commitar.

## Para a sessão da aula (recados)
- **Argumento:** v0 aprovado pelo professor em 30/09/26. O v1 (`argumento.md`) já aplica a sua
  revisão: questões A1–A5 como passos abaixo dos conceitos, `paradoxo` dividido em
  `limpa-x-emissoes` (#6, #7) e `sobra-x-diesel` (#10, #15), `mato-grosso` fundido no
  `fechamento`, premissa de #9 na tela, nó `enem` substituído por `questao-a4` comentada.
- **Plano v1:** os tempos do `argumento.md` são os do plano v0. A redistribuição de ~6 min e o
  corte fino (23 passos em 50 min) são seus, no `01-plano-de-aula.md`. Se o plano cortar um
  bloco, avise aqui: o `layout.json` segue os ids.
- **Recortes das questões:** quando estiverem prontos, o deck espera imagens em
  `aula/03-slides/assets/questoes/` com nomes `a1.png` … `a5.png` (PNG, largura até ~2400 px).
  Se preferir deixar em `fontes/provas-recortes/`, eu copio.
- **Checagem:** o deck nunca mostra número "a verificar"; no protótipo aparece a marca
  `[#n a verificar]`. Quando um item virar "ok" em `fontes/checagem.md`, o número entra no passo.
- **Material impresso:** o build gera `dist/impresso.html` (um passo por folha A4, texto de
  verdade) para o aluno que prefere papel. É o equivalente impresso dos slides; o plano de aula e
  o material complementar (LaTeX) continuam com vocês.
- **.gitignore da aula:** já ignora `aula/03-slides/dist/` e `aula/03-slides/shots/`.

## Da sessão da aula para os slides (30/09/26, plano v2)
O plano v2 pedia (o v3 é documento final e não traz mais essa seção; rastreio em `aula/rastreio-plano.md`), com as decisões do professor D6–D8:
- **Sair da apresentação:** `escala-consumo`, `aglomeracao` (vira uma frase em `fatores-locacionais`) e `questao-a5`
  (vai para o material complementar). Ficam 22 passos (19 de conteúdo + 3 molduras).
- **A4 muda de lugar (D7):** sai de baixo de `guerra-dos-lugares` e vai para logo depois de `caso-ancora`, antes de
  `guerra-dos-lugares`. Ela cobra "acréscimos técnicos" (objeto técnico), não guerra dos lugares.
- **D6 = surpresa:** `atividade-mapa` sem nomes de municípios nem entroncamento destacado; o nome aparece em `caso-ancora`.
- **`argumento.md`:** a lista de `fatores-locacionais` está errada; usar a de Victer (S2, p. 14; 11 itens em custo,
  disponibilidade e prazo, sem "água" nem "terra"); trocar "TI" por "terra indígena"; `quem-esta-no-mapa` passa a ter
  três perguntas (água e energia; trabalho; quem decide e quem resiste). Tempos: tabela da seção 4 do plano.
- Nada disso foi aplicado no deck: é da sessão dos slides, depois do visto do professor no plano v2.

## Comandos
```
ferramentas/decks-impress/deck build aula/03-slides      # dist/index.html, debug.html, impresso.html
ferramentas/decks-impress/deck lint aula/03-slides
ferramentas/decks-impress/deck impresso aula/03-slides   # shots/impresso.pdf
```

## Estado
- 30/09/26: plano v3 e complementar v3 com visto. `argumento.md` **v2** alinhado ao plano v3 e `layout.json`
  refeito (26 passos: 23 de conteúdo + molduras `onde-cabe`, `virada`, `mapa-final`). Questões com os nomes do
  plano (`questao-q1`…`q4`, `questao-reserva`, última na navegação); imagens em `assets/questoes/q1..q4.png` e
  `reserva.png`, copiadas de `fontes/provas-recortes/`. Saíram `escala-consumo`, `aglomeracao`, `questao-a5`;
  entraram `epigrafe`, `atividade-local`, `ficha-de-lugar`. Build e lint: 0 erro, 0 aviso.
- Visto do professor no layout (30/09). **Conteúdo escrito** nos 24 passos, só com o plano v3 e os 4 números (88,2%;
  R$ 3 bi; 68 dias; 8 em cada 10), cada um com a fonte no passo. Novo passo `climogramas` logo abaixo de
  `ficha-de-lugar` (ficha e climogramas não cabiam juntos): 27 passos (24 de conteúdo + 3 molduras).
- `theme.css` do deck: Inter e Source Serif 4 embutidas (`assets/fonts/`), rodapé "Pro Enem • Geografia" com o logo
  (também no impresso), classes `.questao`, `.lado`, `.grupos`, `.ficha`, `.numero`. Mapas em `assets/mapa/`
  (cópias reduzidas; originais em `fontes/epe-rs/` e nos PDFs de Victer), climogramas em `assets/img/`.
- Build e lint: 0 erro, 0 aviso. Impresso: 24 pp. A4. Ênfases (`em`, `strong`) são `inline-block` porque o lint mede
  mal um elemento inline quebrado em duas linhas (falso positivo `elemento-fora-do-passo`).
- Visto do professor no conteúdo (30/09). O impresso vai à turma em PDF (`shots/impresso.pdf`, 24 pp., 8,5 MB).
- **Próximo:** zoom estilo Prezi/Sozi em 3 ou 4 pontos (ver `HANDOFF.md`, passo 3); lugares escolhidos com o professor.

## Respostas do professor (30/09/26, rodada de perguntas objetivas)

- **Fontes:** embutir Inter e Source Serif 4 no tema do deck (não depender da máquina da sala); testar em 1024×768 e 1920×1080.
- **`camada`:** exemplo = recorte do WebMap EPE mostrado por Victer (S2 p. 2, Sudeste). O slide original não tem legenda:
  mostrar a densidade de camadas, sem nomear cores. Crédito: "Victer (EPE), slide 2, 14/09/2026, a partir do WebMap EPE".
- **`atividade-mapa`:** no comando, a rede de transmissão (S2 p. 9, só o mapa) e os pedidos de conexão por estado (S2 p. 11)
  com os **rótulos em GW e nº de projetos tarjados** (sem checagem). Depois, o recorte local sem nomes (D6). Sem novas capturas.
- **`quem-esta-no-mapa`:** a 3ª pergunta vira "Quem vive ao lado, quem decide e quem resiste?" e nomeia povos indígenas
  (Anacé), quilombolas (só camada da EPE) e a vizinhança pobre (pergunta, sem caso).
- **`processar-pra-que`:** expositivo; a proposta de redação vai para o complementar.

## Identidade do curso (30/09/2026)

- Rótulo: "Pro Enem • Geografia" (não "Pré-vestibular ENEM").
- Logo: `identidade/logo/logo-pro-enem-versao-latex.png` (desde 06/10/2026; antes, `aula/02-LaTeX/estilo/logo-pro-enem.png`) (fundo limpo a partir de `fontes/asset1.jpeg`; o `asset2.jpeg` tem o
  xadrez de transparência gravado na imagem e não serve). Entra no título e, discreto, no rodapé dos slides e da versão imprimível.
- O deck tem de rodar sem internet e sem áudio: mapas como capturas locais, nada carregado de CDN na hora da aula.
