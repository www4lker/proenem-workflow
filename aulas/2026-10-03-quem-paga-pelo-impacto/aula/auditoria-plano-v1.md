# Auditoria do plano de aula v1

Objeto: `aula/02-LaTeX/plano-de-aula/plano-de-aula.tex` (v1, 30/09/2026). As referências `.tex:Lnn` apontam
para linhas desse arquivo; `Lnnnn` sem prefixo aponta para a transcrição do webinar.
Feita em 30/09/2026 e cruzada com:
- `argumento.md` v1 e `layout.json`;
- `fontes/checagem.md` (#1–50);
- a transcrição, lida de novo nos trechos que o plano cita;
- `fontes/aulas-atlas.md` e os quatro arquivos em `ATLAS-OF-AI-CAP/aulas-/` (S1–S4, só leitura);
- `fontes/ponte-atlas-ia.md`;
- o índice `atlas_ia` do Notebooklm-central (só leitura; consultei apenas os trechos `kind: source`);
- os recortes das provas.

**O `.tex` não foi alterado.** Este arquivo reúne propostas; quem decide é o professor.

## Veredito

O plano está de pé. As citações do webinar que conferi na transcrição batem:
- a garrafa d'água (L393–412);
- "processar pra quê?" (L448–451);
- as cinco camadas (L698–712);
- a margem ociosa do RS e o cluster de São Paulo (L1670, L1680);
- a distinção entre cloud e IA (L2020–2035);
- os fatores de competitividade (L2044–2052).

A regra sobre Milton Santos é respeitada (`.tex:L177`, `L222`). Os gabaritos conferem com `enem-25-selecionadas.md`, e os tempos somam 50 minutos.

Há cinco problemas que mudam conteúdo ou violam regra do projeto. O plano também não incorpora o que entrou na checagem depois de ser escrito (itens #31–50, os slides do ciclo e o alerta sobre o "R$ 500 bi").

## Graves (mudam o conteúdo ou quebram regra)

**G1. Falta o recorte "trabalho".**
O `CLAUDE.md` diz: "a aula mostra os três recortes lado a lado". Os três são:
- água e energia;
- trabalho;
- comando e resistência.

O plano cobre o primeiro (`limpa-x-emissoes`, `sobra-x-diesel`) e o terceiro (`quem-esta-no-mapa`, A3). Não há nenhum passo sobre quem trabalha.

*Proposta:* abrir `quem-esta-no-mapa` com as três perguntas de `ponte-atlas-ia.md` (quem fornece água e energia? quem trabalha? quem decide e quem resiste?). Não usar número de empregos: o #42 (37 mil postos) está divergente. Custo: nenhum minuto a mais.

**G2. A lista de fatores atribuída à EPE não é a da EPE.**
`.tex:L124` escreve "energia, transmissão, fibra, água, terra, incentivo". A lista real está na fala (L2044–2052) e no slide de Victer (S2, p. 14). São doze fatores, agrupados em custo, disponibilidade e prazo. **Não há "água" nem "terra".** Há três itens que o plano omite:
- restrições socioambientais;
- mão de obra;
- demanda e continuidade.

Isso tem duas consequências:
- **A2 perde o contraste.** O plano usa a A2 para mostrar "outro fator (mão de obra) [que] decide outro serviço" (`.tex:L125`), mas a mão de obra também está na lista da EPE. *Proposta:* reescrever o papel da A2. O mesmo fator pesa de forma diferente: nos call centers, a mão de obra decide; no data center de IA, a energia decide.
- **A virada precisa de outro argumento.** A EPE já trata unidades de conservação, terras indígenas e quilombos como camada de "restrição socioambiental" (L975–984). A virada não é "o mapa não mostra essa gente". É que o planejador vê essa gente como *restrição*, isto é, como custo e prazo. O mapa da EPE não mostra outras coisas: a mancha da enchente de 2024, o uso local da água, quem mora ali. Isso muda a redação da recomendação para a D6 (`.tex:L142–143`).

`argumento.md` (L50–51) repete a lista errada; é preciso avisar a sessão dos slides. A fonte para citar é o S2, p. 14 (rank 2, texto legível), junto da nota técnica da EPE, que ainda falta buscar.

**G3. Números fora da trava ou já divergentes.**
- `.tex:L164` (ficha de lugar) traz "seis linhas (525 e 230 kV) a cerca de 0,5–1,6 km" **sem `\averificar`**. Esses números são o #29, ainda "a verificar". Com `[final]`, o LaTeX **não** barraria esse trecho. *Proposta:* `\averificar{29}` no lugar dos números.
- A lista de cuidados (`.tex:L220–221`) vai só até o #30. Faltam os itens #31–50.
- O #6 (93%) está **divergente** do #47 (88,2%, BEN 2025). `matriz` e `limpa-x-emissoes` dependem dele. O plano diz "a verificar", mas o status certo é "divergente".
- A linha "Caso âncora" (`.tex:L31`) cita só o #22 e o #30. Não traz o alerta da D2: o "R$ 500 bi" é fala condicional e provavelmente se refere ao setor inteiro (#33, #41), não ao projeto. Também faltam o #31 (R$ 3 bi, 54 MW), o #36 e o #45 (terreno "seco"), e o #46 (lei que dispensou estudo urbanístico).
- A mesma potência de 4,75 GW aparece com três comparações diferentes (#22, #34, #44). Se `escala-consumo` ficar, a conta do #9 serve de modelo para as três.

**G4. A A4 não cobra "guerra dos lugares".**
O texto da questão (Santos e Silveira, *O Brasil*, Record, 2004, conferido no recorte) trata de "acréscimos técnicos que renovam a sua materialidade". O conceito cobrado é o de objeto técnico (meio técnico). A guerra dos lugares não aparece.

Pôr a A4 sob `guerra-dos-lugares` quebra a regra do argumento: cada questão fica "logo abaixo do conceito que ela cobra". Além disso, o meio técnico-científico-informacional, que o plano promete "reapresentar em uma frase" (`.tex:L46`), **não aparece em nenhum passo do roteiro**.

*Proposta:* a A4 (5 min, comentada) vira o lugar dessa frase. Há duas saídas:
- (a) levar a A4 para logo depois do `caso-ancora`: o data center como novo "acréscimo técnico";
- (b) manter a posição e abrir o passo com os acréscimos técnicos, para só depois chegar à disputa entre lugares.

O distrator D ("cabos para uma rede informatizada") é o melhor gancho para comentar: por que a resposta não é a da rede de dados?

**G5. Cinquenta minutos sem folga e questões de 1 minuto.**
O roteiro soma exatamente 50 minutos e não reserva tempo para entrada, chamada ou transições. Quatro questões do ENEM levam 1 minuto cada, com texto, cinco alternativas e, na A2 e na A5, mapa. No exame, a média é de cerca de 3 minutos por questão.

*Proposta:* contar 2 minutos por questão de checagem, o que soma +4. Os primeiros 4 minutos liberados pela ordem de corte (`.tex:L95–100`) iriam para essa folga, não para a atividade. Outra saída é assumir que A1–A3 são "leitura guiada" projetada, feita pelo professor e não pela turma.

## Médios

**M1. Cloud × IA generalizado demais.**
Victer apresenta a distinção como leitura pessoal ("como eu pessoalmente estava enxergando", L2018–2019). O #38 separa dois casos: o treinamento aceita distância, a inferência exige proximidade. O objetivo 2 (`.tex:L67`) e o passo `objeto` (`.tex:L113`) deveriam dizer "**treinamento** de IA" e atribuir a leitura a Victer. Victer diz "barato e confiável"; o plano escreve "firme", que é termo técnico do setor.

**M2. "Depende do lugar" é leitura nossa.**
Steibel diz que depende de várias coisas: circuito aberto ou fechado, prédio novo ou velho e, "a mesma coisa", a localização (L405–410). Ele chama o mito de exagero de uma "pesquisa super pequenininha". *Proposta* para `.tex:L87` e `L107`: "depende do resfriamento, da idade do prédio e do lugar; a aula olha o lugar". Assim a turma não sai achando que a água não importa.

**M3. Exemplos de "guerra dos lugares" que não são do caso âncora.**
A ZPE (`.tex:L176`) é de N. Sra. do Socorro. Em Eldorado do Sul, o governador *nega* incentivo fiscal especial (#37). Os mecanismos do caso são outros, todos "a verificar":
- licenciamento como distrito industrial;
- a lei que dispensou o estudo urbanístico (#46);
- a maior reserva de capacidade do MME (#46).

O ReData (#40) disputa em outra escala, a do Brasil contra o exterior (#43). É um bom gancho de escala.

Nas referências falta a obra do conceito: *A Natureza do Espaço*, seção "A produtividade espacial e a guerra dos lugares" (índice `a5330f7f036dbd0e#418`, rank 1; paginar na edição impressa).

**M4. A tese coincide com a do Observatório.**
O objetivo declarado do S3 é "quem paga o custo territorial da transformação digital e quem recebe seus benefícios". A tese do plano (`.tex:L30`) é quase igual. O professor precisa saber disso: pode assumir a convergência ou reformular a tese.

O plano também não traz o contra-argumento de Victer: o grande consumidor sem subsídio "ajuda a pagar a conta" (L1930–1940), e o erro de planejamento é pago "pelo brasileiro" (~L1860). Para a redação, isso rende o parágrafo de contra-argumento em `processar-pra-que`.

**M5. Os slides do ciclo não foram usados.**
Nenhum dos quatro arquivos aparece no plano. O que cada um oferece:
- **S2, p. 10:** a renovável está longe da carga, e isso gera gargalo de escoamento e corte de usinas. Dá para ir a `sobra-x-diesel` **sem número**, como fala atribuída.
- **S2, p. 14:** a fonte de G2.
- **S4, p. 2:** o ciclo de políticas públicas em cinco etapas, que serve de esqueleto para a proposta de intervenção.
- **S4, p. 10:** as contrapartidas do ReData (#50), como repertório da redação ("a verificar").
- **S3, p. 23:** material para a ficha de Eldorado do Sul (#45, #46).
- **S1, sl. 29:** fonte visual para `cinco-camadas`.

A procedência de S3 e S4 continua pendente (handoff, seção 3, item 6).

**M6. Falta a habilidade H6.**
A H6 trata de interpretar representações cartográficas. É o centro do objetivo 4 e de `atividade-mapa`, e não está na lista (`.tex:L76–79`). O texto literal de todas as habilidades segue pendente na Matriz do INEP.

**M7. Referências com erro, e duas pendências que já dá para fechar.**
- **Webinar (`.tex:L251`):** o plano escreve "ITS Rio e EPE" e "transcrição de 29/09/2026". Pelo índice e pelos arquivos, é a aula 1 de 3 do curso do ITS Rio "Data Center e Desenvolvimento Nacional", de 14/09/2026 (data que está no S1 e no S2).
- **Nomes dos palestrantes:** Fabro Steibel e Francisco Abreu Victer (EPE; FGV Energia). O cargo de Steibel no ITS vem só do índice e ainda precisa ser conferido.
- **Edição de Santos e Silveira (`.tex:L252`):** Rio de Janeiro, Record, 2004, como está impresso na própria A4.
- **Crawford:** o trecho da epígrafe existe na obra (índice `6c37b2ec21b0f0d1#50`, "The cloud is… made of rocks and lithium brine and crude oil"), mas em inglês. Precisa de página e da marca "tradução nossa".

## Leves

- **L1.** "23 passos" (`.tex:L32`, `argumento.md`, `README.md`) não bate com o deck. O `layout.json` tem 25 passos: 22 de conteúdo e 3 molduras.
- **L2.** A linha "Slides" do quadro de decisões (`.tex:L236`) está vencida: o `layout.json` já existe.
- **L3.** `argumento.md` (L57) ainda escreve "TI". O plano pede "terra indígena" por extenso (`.tex:L149`). É preciso avisar a sessão dos slides.
- **L4.** Se `escala-consumo` for cortado, a linha "Escala e cálculo" (`.tex:L48`) perde o passo que a sustenta.
- **L5.** A nota "Correção ao rascunho v0" (`.tex:L60–61`) é assunto interno; sai da versão final.
- **L6.** O plano já marca como hipótese que clima quente encarece o resfriamento (`.tex:L51`). Deve continuar fora dos slides até haver fonte técnica.

## Notebooklm-central (rank 3): o que foi e o que não foi usado

Só consultei trechos `kind: source` (obras). Não usei nenhuma nota, nem nada da denylist. O plano não cita nenhuma nota do NotebookLM. "A Superindústria do Imaginário" não aparece no plano; a D5 continua aberta.

## Ordem sugerida para o v2 (depois do visto do professor)

1. Decidir G4 (onde fica a A4) e G5 (folga); os dois mexem no `layout.json`.
2. Aplicar G1–G3 e M1–M3 no `.tex`, sem minuto a mais.
3. Fechar as referências (M7) e as habilidades (M6).
4. Avisar a sessão dos slides: lista de fatores, "TI" e, se a A4 mudar, a posição dela.
