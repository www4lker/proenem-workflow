# COMPLEMENTO ao HANDOFF TÉCNICO — correções pré-Pass 2

> Anexo ao HANDOFF_TECNICO_chat_novo.md. Resultado de revisão crítica.
> Cinco pontos cegos avaliados; quatro geram ação, um vira pergunta.
> Hierarquizados por peso real, não tratados como equivalentes.
> NÃO altera o §4 (fix Bloco 1) — esse segue inalterado e é o primeiro
> movimento. Este complemento age sobre o Pass 2 e adiante.

---

## C1. [BLOQUEADOR PASS 2] Taxonomia de `ancoragem` — substitui a binária do §7

O §7 do handoff principal definiu `ancoragem` como binária (evento concreto vs.
sistema conceitual). **Isso está errado e quebra o filtro mais importante do
corpus.** Questões ENEM CH raramente são puras; a categoria mais frequente —
artefato visual (mapa/charge/gráfico/tabela) — não é nem evento narrativo nem
texto abstrato. Uma binária classificaria uma questão de geopolítica com mapa
de blocos como "conceitual" e o filtro a descartaria, justamente a questão que
a turma processa MELHOR (diagnóstico: visual/concreto = desempenho alto).

**Taxonomia correta para o campo `ancoragem` no Pass 2 (4 valores):**

| valor | definição | exemplo ENEM |
|-------|-----------|--------------|
| `evento_narrativo` | personagem, acontecimento datado, conflito localizado | charge histórica + pergunta sobre o contexto |
| `artefato_visual` | mapa, gráfico, tabela, charge como âncora central | mapa de blocos econômicos + análise |
| `texto_analitico` | fragmento teórico, conceito explícito, definição | trecho de Arendt + interpretação conceitual |
| `composto` | combina ≥2 dos acima sem um dominante | texto teórico + gráfico de apoio |

O prompt de classificação do Pass 2 DEVE usar esses 4 valores. O filtro
pedagógico para a aula 04/07 não será "geopolítica + concreto" mas
"geopolítica + ancoragem ∈ {evento_narrativo, artefato_visual, composto}".
`texto_analitico` puro é o que a turma trava — esse é o conjunto a EVITAR como
porta de entrada, não a descartar do corpus (ainda serve como ponto de chegada).

Substitui a definição de `ancoragem` no §6 e §7 do handoff principal.

---

## C2. [GATE PRÉ-BATCH] Critério de abort do Gemini-delegate

A skill nunca foi validada e processa 355 questões no Pass 2. Sem critério de
parada definido ANTES do dado, viés de confirmação leva a rodar o batch mesmo
com calibração ruim. Definir o gate agora:

**Após a amostra de calibração de 10 questões (§8.2), Walker inspeciona
manualmente. Concordância = quantas das 10 ele aprovaria sem correção.**

- **≥ 8/10** → prossegue para batch completo.
- **6-7/10** → itera o prompt UMA vez, re-roda as 10. Se não chegar a 8/10 na
  segunda, cai para plano B.
- **< 6/10** → não roda batch. Plano B direto.

**Plano B (documentado, não improvisado):**
1. Para a aula de 04/07 especificamente: classificar manualmente só as questões
   de geopolítica (estimativa: 15-30 questões em 8 anos). Volume tratável à mão
   numa sessão. Desbloqueia a entrega primária sem o batch.
2. Para o corpus completo (não urgente): Claude classifica em lotes de ~30 na
   conversa. Mais caro em contexto, mas controlável e inspecionável lote a lote.

O plano B nº 1 é também a resposta ao C3 (ver C3 abaixo): a aula não depende do
batch funcionar.

---

## C3. [DECISÃO FORÇADA — responder antes de iniciar Pass 2] C3 técnico no pipeline

O pipeline tem 5 etapas pós-Bloco 1 antes de qualquer plano de aula existir. O
risco: o projeto serve à sensação de progresso técnico em vez da entrega
pedagógica, com a aula de 04/07 refém de um pipeline longo. Isso é o padrão C3
de Walker manifestado em código.

**Pergunta que Walker DEVE responder antes do orquestrador iniciar §8.2:**

> Você conseguiria montar uma aula de 50 min razoável sobre geopolítica usando
> APENAS o corpus Pass 1 (355 questões, CSV com enunciado/alternativas/gabarito,
> sem classificação) + busca manual por palavra-chave (grep "geopolítica",
> "fronteira", "OTAN", "BRICS" etc.)?

- **Se SIM** → Pass 2 é OTIMIZAÇÃO, não bloqueador. Reordenar: a aula 04/07
  vira entregável primário e é construída JÁ, com Pass 1 + curadoria manual. O
  Pass 2 roda em paralelo/depois como melhoria. O caminho crítico encurta de
  5 etapas para ~1.
- **Se NÃO** (falta a classificação para achar as questões certas) →
  identificar EXATAMENTE qual campo do Pass 2 é indispensável para a aula
  (provavelmente só `tema_principal` + `ancoragem`, não toda a taxonomia) e
  classificar SÓ as questões de geopolítica à mão (15-30 itens). Pass 2
  completo continua sendo melhoria assíncrona.

Em nenhum cenário a aula de 04/07 deve esperar o Pass 2 completo + validação
amostral das 355. Documentar a resposta de Walker no handoff seguinte — não
deixar implícita.

---

## C4. [CAVEAT — não bloqueia, mas registrar] Status epistemológico do diagnóstico

O §7 trata o diagnóstico da turma como fundação arquitetural mas não documenta
o instrumento. Os números (64,6%, 27,7%, 22,1%) podem ter precisão espúria.

**Perguntas a Walker (não bloqueiam Bloco 1; bloqueiam tratar os números como
métricas finas):**
- Quantos alunos no diagnóstico? (N)
- Que instrumento? (simulado completo? questões avulsas? quantas?)
- Quando aplicado, em que condições?

**Regra de uso até resposta:**
- Se **N ≥ 15** → números utilizáveis como sinal direcional (não como medida de
  2 casas decimais — "geopolítica é cluster fraco" sim; "27,7%" não).
- Se **N < 15** → tratar TUDO do §7 como sinalizador qualitativo. A DIREÇÃO
  (turma processa concreto, trava em abstrato) permanece válida porque é
  consistente com a literatura de ensino médio público e com o risco já
  nomeado da formação de Walker — mas nenhuma decisão deve depender de número
  específico.

A arquitetura (C1, taxonomia de ancoragem) NÃO desaba se os números forem
imprecisos — ela depende da direção, não da magnitude. Por isso é caveat, não
bloqueador.

---

## C5. [PERGUNTA DE UMA LINHA — sem ação até resposta] Heterogeneidade dos 5 grupos

Walker tem 5 grupos de ~30. O projeto assume turma-alvo homogênea. Construir
"camada de flexibilidade no filtro" agora seria over-engineering de problema
hipotético. Ação proporcional = perguntar, não codar.

**Pergunta a Walker:**
> O diagnóstico do §7 é de qual(is) grupo(s)? A aula de 04/07 é para os 5
> grupos ou para um específico?

- Resposta "5 grupos similares / diagnóstico agregado" → ponto evapora, nada muda.
- Resposta "grupos heterogêneos" → REABRIR reativamente, com o dado na mão.
  Possível consequência: o filtro precisa de parâmetro de dificuldade variável.
  Mas só projetar isso DEPOIS de confirmar que o problema existe.

Zero código novo até a resposta.

---

## ORDEM DE INCORPORAÇÃO (não altera o primeiro movimento)

1. **Primeiro movimento do chat novo permanece o §4** (fix Bloco 1, fechar
   Pass 1). Este complemento NÃO toca nisso.
2. Após Pass 1 fechado e antes de §8.1, o orquestrador faz a Walker as
   perguntas de **C3 (decisão forçada), C4 (3 perguntas), C5 (1 pergunta)**
   num único bloco. São 5 perguntas, respondíveis rápido.
3. As respostas reordenam o roadmap (C3 pode encurtá-lo drasticamente).
4. C1 (taxonomia de 4 valores) e C2 (gate de abort) entram no desenho do
   prompt de Pass 2 — independente das respostas, são corretos por si.

## SÍNTESE DAS INTERCONEXÕES

- C1+C4 são o mesmo erro em dois momentos: diagnóstico fracamente documentado
  (C4) gerou taxonomia subdimensionada (C1). Corrigir C1 não depende de
  resolver C4 — a taxonomia de 4 valores é correta independente do N do
  diagnóstico, porque deriva da estrutura das questões ENEM, não dos números
  da turma.
- C2+C3 puxam em direções opostas e se equilibram: C3 quer encurtar o pipeline
  (menos C3-técnico), C2 quer robustez no ponto frágil (fallback). O plano B do
  C2 (classificar geopolítica à mão) É a manifestação concreta do "sim" do C3
  — encurtar e dar robustez são a mesma ação aqui.
- C5 é o único isolado. Se a resposta for "homogêneo", custo zero. Se não,
  afeta a premissa pedagógica central — mas reativamente, não agora.
