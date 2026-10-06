# HANDOFF: framework decks-impress (Frente 3)

Sessão de origem: `aulas/2026-10-03-quem-paga-pelo-impacto` (plano em
`~/.claude/plans/os-seus-achados-influenciam-dynamic-seal.md`). Esta sessão roda **em paralelo**
e é dona só do framework. Modelo sugerido: o mais forte disponível.

## Objetivo
Transformar `decks-impress.zip` (impress.js v2.0.0, decks espaciais estilo Prezi, offline) num
framework **reutilizável em outros projetos**, e liberar um deck novo para a aula sobre data
centers no Brasil (pré-vestibular, ENEM, ~50 min).

## Ponto de partida
- Zip: `aulas/2026-10-03-quem-paga-pelo-impacto/decks-impress.zip` (não rastreado no git da aula; não editar, não mover).
- Este diretório (`ferramentas/decks-impress/`) está vazio, exceto este arquivo. Ainda **sem git**.
- Node v20.20.2 e npm 10.8.2 instalados. **Playwright/Chromium não instalados** (`~/.cache/ms-playwright` não existe): avisar o professor antes de baixar o navegador; sem ele `lint` (checagens de navegador), `shots` e `pdf` não rodam.
- O zip traz `CLAUDE.md`, `README.md`, `docs/vocabulario.md`, `docs/gotchas.md`, `theme/theme.css`, `tools/*.mjs`, `vendor/impress.js` (MIT) e o deck `decks/demo`. **Leia o `CLAUDE.md` do zip primeiro.**

## Regras do zip que continuam valendo
- Fluxo: `argumento.md` → aprovação do professor → `layout.json` → `content/*.html`. Nunca editar `dist/`.
- Após cada mudança: `npm run build` e `npm run lint`; screenshot só do que mudou.
- Fonte ≥ 28px (`.fonte` ≥ 22px), tokens do tema, tudo offline. Não inventar referências (`[FONTE?]`).
- Registrar em `notas-de-processo.md` o que o professor repetir.
- Público: pesquisador de humanidades que pensa em argumento, não em CSS.

## Tarefas (em ordem)
1. **Extrair** o zip aqui, sem sobrescrever este `HANDOFF.md`. `git init` neste diretório. **Não fazer commit** até o professor pedir.
2. **Validar o ambiente** com o deck `demo`: `npm install`, `npm run build -- decks/demo`, `npm run lint -- decks/demo`. Registrar o que falhar (Chromium ausente, versões).
3. **Generalizar** (só o que o uso em vários projetos exigir, em patches mínimos):
   - separar ferramenta de conteúdo: `decks/` como área de conteúdo, `.gitignore` de `dist/` e `shots/`;
   - decidir e documentar como um projeto externo usa o framework (deck dentro do repo × repo de deck que aponta para o framework);
   - `README.md` curto em português com acentos, com o fluxo de ponta a ponta.
4. **Criar o deck vazio** `decks/aula-data-centers/` com `argumento.md` em branco (só cabeçalho e a legenda das relações contém / deriva / opõe-se / exemplifica). **Não preencher conteúdo da aula**: o argumento depende de decisões do professor (D1 fio condutor, D2 caso âncora) que estão na sessão da aula.
5. **Tema**: propor (sem aplicar) ajustes de tokens para sala de aula projetada (contraste, tamanho), como lista no fim deste arquivo. Não criar tema novo (fora de escopo do zip).
6. **Notas de processo**: manter `notas-de-processo.md` por deck. Uma futura skill será extraída dele; **não criar a skill agora**.

## Fora de escopo (do zip)
Editor por arrastar, conversor do Canvas do Obsidian, plugins extras, temas novos, exportar PPTX, 3D.

## Restrições herdadas do projeto da aula
- Não tocar em `pipeline/` (árvore suja do professor), em `[acervo pessoal do autor: NotebookLM]/` nem em `[acervo pessoal do autor, fora do repositório]/`.
- Nenhum LLM local/Ollama nem o motor de deliberação.
- Nada de conteúdo da aula no repositório do framework antes de o `argumento.md` ser aprovado.
- Português com acentos, nomes de arquivo em português, Markdown simples.

## Contrato de entrega (o que a sessão da aula espera)
- [x] `npm run build` e `npm run lint` passam no deck `demo` (0 erro, 0 aviso); `shots` e `pdf` também.
- [x] `decks/aula-data-centers/` existe e aceita o fluxo argumento → layout → content (testado com uma cópia descartável).
- [x] README explica o uso em 1 página.
- [x] Este arquivo atualizado.

## Registro da sessão (30/09/26)
- **Feito:**
  - Zip extraído aqui (sem sobrescrever este arquivo); `git init` feito, **sem commit**.
  - `npm i` (playwright 1.63.0). Chromium do Playwright **não baixado**: não foi preciso.
    O lint, os shots e o PDF rodam com o Edge e o Brave do sistema.
  - Generalização (patches mínimos):
    - `tools/browser.mjs`: navegador em cascata (`CHROMIUM_PATH` → Chromium do Playwright →
      Chrome/Chromium/Edge/Brave do sistema);
    - `deck` (script na raiz): `deck <build|dev|lint|shots|pdf> <pasta>` de qualquer
      diretório, para decks em qualquer projeto;
    - `tools/common.mjs`: deck sem `layout.json` dá mensagem do fluxo em vez de erro cru;
      deck com `steps` vazio não quebra o mapa de depuração;
    - `.gitignore`: `decks/` é área de conteúdo; o git do framework só versiona `decks/demo`;
    - `README.md` reescrito (1 página, fluxo de ponta a ponta); `CLAUDE.md`: só o bloco de comandos.
  - `decks/aula-data-centers/`: `argumento.md` só com cabeçalho e legenda das relações,
    `content/`, `assets/`, `notas-de-processo.md`. **Sem `layout.json` e sem conteúdo da aula.**
- **Pendente:**
  - Primeiro commit do framework (esperando o pedido do professor).
  - Preencher `argumento.md` depois de D1 e D2 (sessão da aula).
- **Decisões do professor (30/09/26):**
  - Deck da aula movido para `aula-geo-natureza/aula/03-slides/` (versionado lá; `dist/` e
    `shots/` no `.gitignore` da aula). Build: `…/decks-impress/deck build aula/03-slides`.
  - O esqueleto vazio virou `decks/modelo/` (versionado no framework) para decks novos.
  - D3: impress.js é o formato principal.
- **Dúvidas originais (já respondidas):**
  1. **Onde mora o deck da aula?** Recomendo mover `decks/aula-data-centers/` para
     `aula-geo-natureza/aula/03-slides/` (a pasta existe e está vazia), versionado com a aula,
     e rodar `…/decks-impress/deck build aula/03-slides`. Não movi porque a pasta pertence à
     sessão da aula. `dist/` e `shots/` precisariam entrar no `.gitignore` da aula.
  2. **D3 (formato dos slides)** do handoff da aula continua aberta: este framework é uma
     terceira opção ao lado de `.pptx` e deck Artifact.
  3. Commit inicial do framework: quando quiser.

## Tema: propostas para sala projetada (não aplicadas)
Contraste medido contra `--bg` `#f6f3ec`: `--fg` 15,2:1 · `--fg-soft` 7,0:1 · `--accent` 7,0:1 ·
`--accent-2` 7,8:1 · `--rule` 1,4:1. O texto passa com folga (AA pede 4,5:1); o problema é o que é fino ou pequeno.
1. **Fontes embutidas.** `Inter` e `Source Serif 4` estão instaladas nesta máquina, mas não no
   deck: no computador da sala o texto cai para Arial/Georgia ou DejaVu e as quebras mudam.
   Proposta: `.woff2` das duas (licença OFL) em `theme/fonts/` + `@font-face` no tema global.
   É a mudança mais importante da lista.
2. **`--rule` `#d8d2c4` → `#a89f8c`** (~2,5:1): linhas e bordas finas somem no projetor.
3. **`--fs-source` 24px → 26px** e mínimo do lint 22 → 24: créditos a 24px não se leem do fundo
   da sala. (Não mexe no mínimo de 28px do corpo.)
4. **`--fg-soft` `#55524b` → `#48453f`**: projetor lava tons médios; subir para ~9:1.
5. **Opacidade dos passos inativos 0,2 → 0,12** (em `.step`): no projetor, os vizinhos a 20%
   competem com o passo ativo nas transições. Testar na sala antes.
6. Manter fundo claro: em sala iluminada, fundo escuro projetado perde contraste.

## Recados da sessão da aula (30/09/26, resposta ao `HANDOFF-slides.md`)
- **Recortes das questões prontos:** `aula-geo-natureza/aula/03-slides/assets/questoes/a1.png` … `a5.png`
  (PNG de 545–1175 px de largura, 150 dpi, recortados do PDF oficial do INEP; nada a copiar).
  Mapa: a1 = ENEM 2013/43, a2 = 2014/9, a3 = 2015/15, a4 = 2013/37, a5 = 2014/38.
  Os 25 recortes estão em `aula-geo-natureza/fontes/provas-recortes/` (script `fontes/recortar_questoes_inep.py`).
- **Correção ao `argumento.md` v1:** quem tem figura são **A2** (mapa-múndi com o círculo da Ásia) e
  **A5** (mapa do Aquífero Alter do Chão, legenda pequena); a **A1 é só texto**. A frase "A1 e A5
  têm figura" deve virar "A2 e A5".
- **Uso do recorte:** o professor ainda vai olhar as imagens; até o visto dele em `fontes/checagem.md`,
  trate como provisório. O recorte já vem **sem o gabarito** (o PDF de 2013 traz um círculo verde na
  resposta; foi retirado). Revelar a alternativa certa é decisão do passo (`why`), não da imagem.
- **Ainda não está pronto do lado da aula:** plano v1 (tempos e corte fino dos 23 passos), D2, D4 e a
  checagem de #6, #7, #9, #10, #15, #21–23. O `layout.json` segue os ids do `argumento.md`; se o
  plano cortar um bloco, eu avisaria no `HANDOFF-slides.md`.
- **Material complementar (LaTeX, 19 questões):** frente separada e posterior; **não faz parte do deck**.
- **Fontes do tema (Inter, Source Serif 4):** a autorização de baixar é do professor; o pedido está no
  `HANDOFF-slides.md`.
- **Commits:** a aula commita o que estiver solto em `aula/03-slides/` quando o professor pedir;
  o framework só a pedido dele.
- **Decisões do professor em 30/09/26 (chat da aula):** `argumento.md` v1 **confirmado como está** (pode
  propor o `layout.json`); D2 = **Eldorado do Sul (RS)** para `caso-ancora` (números de #22 seguem
  "a verificar": sem número no passo); D4 = recorte do WebMap EPE, que o professor está capturando
  (chega em `aula/03-slides/assets/mapa/`); tempo: as questões saem metade do `objeto`
  (`cinco-camadas` a ~1 min) e metade da atividade, e A5 sai primeiro se não couber. O plano v1
  (sessão da aula) vai fixar os minutos por passo.

## Capturas do WebMap EPE: leia antes de propor o `layout.json` (sessão da aula, 30/09/26)
O professor capturou o WebMap EPE. **Ficam em `aula-geo-natureza/fontes/epe-rs/`** (9 arquivos, nomes com
espaços: use aspas), **não** em `aula/03-slides/assets/mapa/` como eu disse acima. **Leia
`fontes/epe-rs/LEIAME.md` primeiro** (catálogo de cada imagem, cautelas e o que falta). Resumo:
- **O que são:** Eldorado do Sul (RS) e a região do **entroncamento das rodovias 401 e 290**, onde o professor
  diz que fica o polo de data centers (D2, `caso-ancora`; afirmação ainda sem fonte, `checagem.md` #30). Mostram a
  **camada de transmissão** da EPE com subestações, popups de quatro linhas (ano, agente, tensão, km) e o mapa-base.
- **O que não são:** nenhuma imagem marca um data center; nenhuma tem legenda; só há a camada de transmissão
  (a `atividade-mapa` fala em fontes, fibra, UC, terras indígenas, quilombos: **não existem ainda como captura**).
  O professor será avisado; até lá, planeje o passo com o que existe e deixe o resto como `[CAPTURA?]`.
- **Uso que propus:** (1) sequência de **zoom de escala** 6 km (`…10-28-23.png`) → 2 km (`rCaptura…10-38-05.png`) →
  0,2 km (`…10-39-27.png`), que casa com o impress.js; (2) leitura do mapa como o planejador lê, em `onde-cabe` /
  `atividade-mapa`; (3) `caso-ancora`: o que o mapa não mostra. A decisão de **onde entra cada captura é sua**
  (o `layout.json`); o plano v1 (LaTeX) só recomenda.
- **Pergunta aberta ao professor:** Eldorado do Sul é a resposta certa da atividade ou a surpresa da virada?
  Se for surpresa, o recorte da atividade não deve mostrar o entroncamento nem os nomes; não decida sozinho.
- **Cautelas de fonte:** cada captura é rank 2, com data (30/09/2026) e crédito "EPE, WebMap EPE". Números dos popups
  (2012, 2014, 2022, 2023; kV; km) estão em `checagem.md` #25–#28 como "a verificar": **não vão para slide** antes do
  visto. O rótulo "Dell" e os bairros são do mapa-base, não da EPE. "TI" = **terra indígena**, por extenso.
  Os originais não se editam: recorte e ampliação são cópias em `assets/`, com "adaptado de" se algo for removido.
- **Análise das imagens:** o texto é pequeno e as cores não têm legenda. Se precisar de leitura fina de uma
  imagem, use um modelo forte e confira contra o `LEIAME.md`; não acrescente ao catálogo o que não estiver visível.
- **Plano de aula:** passa a ser escrito em LaTeX (`aula-geo-natureza/aula/02-LaTeX/plano-de-aula/`). Quando o
  v1 fixar minutos e cortes, os ids do `argumento.md` continuam valendo; se algum bloco sair, eu registro
  aqui e no `HANDOFF-slides.md`.
