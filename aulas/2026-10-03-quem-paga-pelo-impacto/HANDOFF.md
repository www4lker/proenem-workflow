# Handoff: aula "Quem paga pelo impacto?" (Geografia e Natureza)

> **Registro (06/10/2026).** Os itens abertos deste documento foram levados para [`docs/FILA.md`](../../docs/FILA.md), que passa a ser a fonte única do que falta fazer. Este arquivo fica como contexto.

Estado em 02/10/2026, no branch `v3-tres-professores` (saiu de `ementa-geo-natureza`). Este arquivo tem só o estado e os próximos passos. O que aconteceu, e
por quê, estava em `logs/` (sessão de 02/10). A aula é em **3/10/2026**.
> *(06/10/2026: os logs da aula ficaram fora do repositório unificado, ver `docs/higienizacao.md`; o processo está em
> `docs/HANDOFF-kit-de-aula.md`. Também ficaram fora `impar-aulas/`, `fontes/aulas-texto/` e o `.docx` do roteiro.)*

## 1. Estado

- **v3, três professores (02/10, com visto do professor nos slides e no roteiro):** Professor A 40% (Ecologia 3–9, Impactos 9–17, Caso 34–40), Professora B 40%
  (Abertura 0–3, Questões 40–48, Fechamento 48–50), Professora C 20% (Resíduos 24–34). Sustentabilidade (17–24)
  é dividida entre Professora B e Professor A; a divisão dos passos é dos dois (roteiro sugere trocas às 19:00 ou 21:30).
  - Face de Resíduos com 6 passos: `abertura-residuos`, `residuos` (lixo × resíduo × rejeito, art. 3º),
    `residuos-4r` (foto DK p. 331 + ordem do art. 9º), `residuos-charge` (Gilmar: "mudar os hábitos de quem?"), `residuos-mapa` (IBGE, MUNIC 2023), `residuos-logistica`
    (art. 33, ponte para o caso). Lei 12.305 conferida no Planalto; nenhum número do PDF dela na tela.
  - Foto dos 4R inserida pelo professor (`assets/img/dk/4r.jpeg`).
  - Roteiro v3 (`aula/05-roteiro-de-ensaio.md` e `aula/roteiro-de-ensaio.docx`, regerado no mesmo nome): nomes
    preenchidos, seção 4 de insumos da Professora C.
  - Página on-line: créditos com os três, resíduos com a lei e o mapa, referências novas. `publicar/` remontado; zip não.
  - Material da Professora C em material da Professora C (fora do repositório) (áudios e PDF), fora do git até o professor decidir.
- **Rumo (02/10):** ementa "Questões e impactos ambientais; Sustentabilidade; Resíduos sólidos; Ecologia", com data centers
  em até 20% da aula. A versão data centers está intacta no `master` e na tag `v3-data-centers`.
- **Argumento v3** (`aula/03-slides/argumento.md`): pergunta-guia "Quem paga pelo impacto?". Sem mudança.
- **Deck** (`aula/03-slides/`): visto do professor em 02/10, no conteúdo e, depois, no tratamento final (prisma 3D):
  - Prisma octogonal 3D, gerado por `prisma.py` (pedido do professor em 02/10, no lugar do octógono plano, que fica no
    commit `faf27d2`):
    - uma face por bloco; os slides descem pela face; as aberturas formam o anel de cima;
    - giro de 45° em volta do eixo vertical a cada troca de eixo, sempre no mesmo sentido;
    - título deitado na tampa; a panorâmica final olha de cima (40°) e mostra o objeto inteiro, com a pergunta na tampa.
  - Uma só panorâmica: `mapa-final`, seguida de `material-online`, com **um só QR**, que leva ao material complementar
    no Netlify (`https://geografia-e-natureza-proenem-2026.netlify.app/`). O PDF se baixa de lá.
  - Aberturas dos quatro eixos e do caso com ilustração de *O livro da ecologia*.
  - Imagens também em `quem-paga` e `sustentavel`.
  - Cor por eixo tirada da ilustração de cada abertura (faixa na cor viva; títulos na mesma cor escurecida).
  - Total: 35 passos (34 de conteúdo e 1 moldura) na v3.
  - Mergulhos conferidos no navegador.
  - Lint: 0 erro e 0 aviso.
  - Impresso: 30 páginas na v3.
- **Imagens DK:** as sete em `aula/03-slides/assets/img/dk/` são as reais. O professor fotografou no livro físico
  (`fontes/imagens/final/`, fora do git); recortei as bordas. Mapa em `fontes/dk-ecologia-mapa.md`.
  - `residuos.jpg` é pequena (332×432) e aparece ampliada cerca de 1,9×. Se ficar borrada no projetor, refotografar a p. 330.
- **QR:** `assets/img/qr-material.png` é o do professor (`fontes/qr-code/`, fora do git) e foi lido: aponta para o Netlify.
- **Frase do caso, escrita por mim, aguarda visto:** "Os quatro eixos num caso só: onde fica a nuvem?"
  (`content/abertura-caso.html`).
- **Material complementar on-line** (`aula/04-online/index.html`): página única, sóbria, com resumo dos quatro eixos e do
  caso, 11 questões (4 ENEM da aula + autoral + 6 ENEM 2013–2016 para treinar) com correção ao clicar, comentário, placar e
  acertos por eixo (salvos só no aparelho), repertório para a redação e referências. Já está no ar (o professor subiu).
- **Hospedagem: tudo no Netlify** (decisão do professor em 02/10; o Dropbox saiu):
  - material complementar, slides navegáveis e o PDF (`slides-quem-paga-pelo-impacto.pdf`, 26 pp.), que o botão da página
    baixa direto, pelo mesmo endereço;
  - `bash aula/04-online/montar.sh` apaga o `dist/`, refaz o build e o impresso e gera `aula/04-online/publicar/` (fora
    do git, ~12 MB); sem o PDF, ele para com erro;
  - para atualizar, o professor sobe de novo `aula/04-online/publicar.zip` (fora do git), feito com
    `cd aula/04-online && zip -qr publicar.zip publicar`. O PDF sai sempre igual aos slides.
- **Referência DK** em `aula/04-online/index.html`: edição brasileira (Globo Livros, 2020), pela ficha catalográfica.
- **Framework decks-impress:** patches **sem commit** no repositório do framework (não é deste repo): `sobre` (mergulho),
  `transicao` por passo e o suporte 3D (`rotateX`, `rotateY`, `data-z` sempre emitido, `meta.perspective`, `camera` em
  molduras, isenção 3D no lint) em `tools/common.mjs`, `tools/build.mjs`, `tools/runtime.js`, e uma linha em `CLAUDE.md`.
  Sem eles o build deste deck falha ou sai plano.
- **Plano v4:** com visto. Material complementar LaTeX antigo (data centers): não distribuir deste branch.
- **Números na tela e na página:** só os 4 conferidos (88,2%; R$ 3 bi; 68 dias; 8 em cada 10).
- **Zip do relatório:** foi para a lixeira (as imagens usadas já estão no git).
- **Roteiro de ensaio:** `aula/05-roteiro-de-ensaio.md`; o `.docx` é `aula/roteiro-de-ensaio.docx` (o nome é a mudança do
  professor; regerar com `pandoc aula/05-roteiro-de-ensaio.md -o aula/roteiro-de-ensaio.docx`). v3 com visto (02/10).
- **Correções mínimas:** `HANDOFF-minimos.md` (alt da abertura de Ecologia), à espera de visto; não aplicadas.
- **Cópia em pendrive:** usada na sala de aula; fora deste repositório.

## 2. Próximos passos (nesta ordem)

1. Professor, v3:
   - mandar o `.docx` à Professora B e à Professora C;
   - subir no Netlify o `aula/04-online/publicar.zip`, refeito com a v3 em 02/10;
   - decidir se a v3 volta para `ementa-geo-natureza` (material da Professora C (fora do repositório) segue fora do git: áudios e PDF de terceira).
   Professor, antes:
   - no site no ar, testar "Ver os slides" e "Baixar PDF dos slides" numa janela anônima;
   - o arquivo no Dropbox deixou de ser usado; apagar ou não é com ele;
   - visto na frase do caso ("Os quatro eixos num caso só: onde fica a nuvem?").
2. Aplicar ou não o `HANDOFF-minimos.md`.
3. Se ficar borrada no projetor, refotografar a p. 330 (`residuos.jpg`).
4. **Kit reprodutível (prancheta):** levar a aula para outras disciplinas. O estado, os riscos e as decisões pendentes
   estão em `docs/HANDOFF-kit-de-aula.md`. Começa depois da aula, pelas decisões do §7. Os patches do framework já
   estão em `ferramentas/decks-impress/` (o `decks-impress-patches.diff` saiu em 06/10/2026).
5. Depois da aula:
   - decidir como manter as duas versões (`master` data centers × `ementa-geo-natureza`);
   - decidir se os patches do framework viram commit lá.

## 3. Regras que não mudam (resumo do `CLAUDE.md`)

- Rank de fonte: 1 obra primária · 2 dado ou reportagem (datar em `checagem.md`) · 3 síntese de IA ou nota do NotebookLM (**nunca citável**).
- **Não atribuir a Milton Santos análise sobre IA ou data centers.** Rozely Ferreira dos Santos (2004) é outra autora.
- Questão de vestibular só com prova e ano conferidos; as demais, **(autoral)**. Só 2013–2016 valem.
- Só leitura: `[acervo pessoal do autor: NotebookLM]/`, `[acervo pessoal do autor, fora do repositório]/`, o projeto PROENEM. Não editar `impar-aulas/`.
- Não rodar o motor de deliberação nem LLM local (Ollama). Não decidir o P0 do artigo ATLAS.
- Fotos do relatório com pessoas identificáveis: não usar.

## 4. Como compilar e montar

```bash
cd aula/02-LaTeX/plano-de-aula
latexmk -interaction=nonstopmode -halt-on-error plano-de-aula.tex </dev/null
```
Deck: `ferramentas/decks-impress/deck build aula/03-slides` (também `lint`, `shots`, `impresso`). O framework é
repositório próprio: não commitar nele. **Não usar `pkill -f`.**

Página on-line: `bash aula/04-online/montar.sh`; para testar, `python3 -m http.server` dentro de `publicar/`.

## 5. Verificação rápida ao retomar

```bash
cd aulas/2026-10-03-quem-paga-pelo-impacto
git status --short && git log --oneline | head -5   # fora do git: decks-impress.zip, fontes/__pycache__/, fontes/imagens/, fontes/qr-code/
ls aula/03-slides/content | wc -l                    # 34
ferramentas/decks-impress/deck lint aula/03-slides   # 0 erro(s), 0 aviso(s)
```
