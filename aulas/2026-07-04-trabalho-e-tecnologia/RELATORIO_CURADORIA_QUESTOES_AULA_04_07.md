# Relatório de Curadoria Documental — Questões para 04/07/2026

Tema da aula: **Tempo, Tecnologia e Trabalho: da Revolução Industrial ao Debate da Escala 6x1**

Professores: professor de Geografia e professor de História

Objetivo desta rodada: recuperar e verificar documentalmente as questões mais promissoras identificadas no diagnóstico anterior, para apoiar a escolha de uma abertura, uma questão principal e uma questão reserva/síntese. Este relatório não é plano de aula, roteiro de fala, slide, folha de atividade ou material definitivo do estudante.

## 1. Estado Git no Início da Rodada

Primeira ação executada:

```bash
git status --short --branch
```

Resultado:

```text
## master
 M .claude/skills/gemini-delegate/SKILL.md
 M .gitignore
 M CLAUDE.md
 M COMPLEMENTO_handoff_tecnico.md
 M "DIAGN\303\223STICO_TURMAS_ProEnem2026.md"
 M analise/corpus_mestre.csv
 M analise/geopolitica_aula_04_07.csv
 M corpus_enem/batch_completo_clean.csv
 M corpus_enem/batch_completo_raw.csv
 M corpus_enem/questoes_raw.csv
 M corpus_enem/retry40_raw.csv
 M diagnostico_pdfs.md
 M extrair_prova.py
 M instancia-pedagogica.md
 M logs-handoffs/handoffs-velhos/HANDOFF_pipeline_enem.md
 M logs-handoffs/handoffs-velhos/handoff-novo.md
 M logs-handoffs/handoffs-velhos/handoff1.md
 M logs-handoffs/ho.md
 M logs-handoffs/logs/2026-05-15.md
 M logs-handoffs/logs/2026-05-16.md
 M poc_extracao.py
 M processar_recorte.py
 M prompts/classificar_questao.txt
 M scripts/analise_corpus.py
 M scripts/strip_and_parse.py
?? .claude/settings.local.json
?? AGENTS.md
?? HANDOFF_AGENTE_INICIO_2026-06-27.md
?? RELATORIO_DIAGNOSTICO_AULA_04_07_TRABALHO_TECNOLOGIA.md
?? plano_aula_04_07.md
?? prompts/aluno_arquetipico.txt
?? protocolo_feedback_aula.md
```

O repositório já estava sujo antes desta rodada. Nenhum arquivo existente foi revertido, limpo, reorganizado ou formatado.

## 2. Fontes Canônicas e Assets Gerados

PDFs oficiais de prova usados:

- 2013: `2013/dia1_caderno1_azul.pdf`
- 2014: `2014/2014_PV_impresso_D1_CD1.pdf`
- 2015: `2015/2015_PV_impresso_D1_CD1.pdf`
- 2016: `2016/2016_PV_impresso_D1_CD1.pdf`

PDFs oficiais de gabarito usados:

- 2013: `2013/dia1_azul.pdf`
- 2014: `2014/CADERNO_1_AZUL_SABADO.pdf`
- 2015: `2015/CADERNO_1_AZUL_SABADO.pdf`
- 2016: `2016/GAB_ENEM_2016_DIA_1_01_AZUL.pdf`

Assets visuais gerados a partir dos PDFs, sem alterar os PDFs originais:

- `curadoria_questoes_04_07_assets/2013_CH_017.png`
- `curadoria_questoes_04_07_assets/2015_CH_011.png`
- `curadoria_questoes_04_07_assets/2014_CH_005.png`

Observação: os PNGs são páginas oficiais inteiras em alta resolução. Eles contêm a questão-alvo completa e, em alguns casos, itens vizinhos na mesma página. O arquivo `2013/dia1_caderno1_azul.pdf` exibe marcações verdes de gabarito/correção em algumas alternativas na página renderizada; a página foi exportada como está no repositório.

## 3. Questão `2015_CH_002`

### Identificação documental

- ID interno: `2015_CH_002`
- Ano: 2015
- Número no corpus: 2
- Número oficial no caderno: Questão 02
- PDF de origem: `2015/2015_PV_impresso_D1_CD1.pdf`
- Caderno: 1
- Cor: Azul
- Página oficial: 2
- Posição: coluna esquerda, parte inferior
- Gabarito oficial: E
- PDF de gabarito: `2015/CADERNO_1_AZUL_SABADO.pdf`

### Conteúdo integral

**Texto de apoio**

> Dominar a luz implica tanto um avanço tecnológico quanto uma certa liberação dos ritmos cíclicos da natureza, com a passagem das estações e as alternâncias de dia e noite. Com a iluminação noturna, a escuridão vai cedendo lugar à claridade, e a percepção temporal começa a se pautar pela marcação do relógio. Se a luz invade a noite, perde sentido a separação tradicional entre trabalho e descanso — todas as partes do dia podem ser aproveitadas produtivamente.

Fonte citada:

> SILVA FILHO, A. L. M. *Fortaleza: imagens da cidade*. Fortaleza: Museu do Ceará; Secult-CE, 2001 (adaptado).

**Comando**

> Em relação ao mundo do trabalho, a transformação apontada no texto teve como consequência a

**Alternativas**

A. melhoria da qualidade da produção industrial.

B. redução da oferta de emprego nas zonas rurais.

C. permissão ao trabalhador para controlar seus próprios horários.

D. diminuição das exigências de esforço no trabalho com máquinas.

E. ampliação do período disponível para a jornada de trabalho.

### Comparação com os CSVs

`corpus_enem/questoes_raw.csv`: texto, comando, alternativas e gabarito correspondem ao PDF oficial. Extração limpa.

`analise/corpus_mestre.csv`:

- Disciplina atribuída: Sociologia
- Tema: `Sociologia do trabalho > impactos da tecnologia na jornada de trabalho`
- Subtema: `Tecnologia e sociedade`
- Ancoragem: `texto_analitico`
- Tipo cognitivo: `analise`
- Competência: `5.0`
- Habilidade: `H1`

Não foram identificados ruídos ou omissões relevantes.

### O que a questão exige?

- Informação explícita no texto: sim, especialmente a perda da separação entre trabalho e descanso.
- Inferência: sim, ligar iluminação/relógio ao prolongamento produtivo do dia.
- Conhecimento histórico: baixo.
- Conhecimento geográfico: baixo.
- Interpretação visual: não.
- Reconhecimento conceitual: sim, jornada de trabalho, tempo social, produtividade.
- Eliminação de distratores: sim.

### Conteúdo mínimo antes

- Noção de jornada de trabalho.
- Diferença entre tempo natural e tempo cronometrado/social.
- Ideia básica de tecnologia como transformação das condições de produção.

### Conteúdo que pode emergir na correção

- Industrialização e disciplina do tempo.
- Relógio, iluminação e extensão do tempo produtivo.
- Relação entre produtividade e apropriação do tempo do trabalhador.
- Ponte direta para escala 6x1 e disputa pela redução da jornada.

### Funcionamento dos distratores

- A: pode parecer correta porque tecnologia costuma ser associada a melhoria produtiva, mas o texto trata de tempo disponível para trabalhar, não qualidade da produção.
- B: pode atrair quem pensa em modernização agrícola, mas o texto não fala de campo ou emprego rural.
- C: é o oposto da tese do texto; a iluminação amplia o controle produtivo do tempo, não a autonomia do trabalhador.
- D: associa tecnologia a menor esforço físico, mas a evidência textual é sobre extensão temporal, não intensidade corporal.

### Dificuldade real

- Extensão textual: média.
- Vocabulário: médio.
- Abstração: média.
- Conhecimento prévio: baixo.
- Dificuldade global para as turmas: média.

Justificativa: o texto é curto e diretamente relacionado à tese, mas exige perceber uma consequência social indireta da tecnologia. A alternativa correta é clara se o aluno identifica “trabalho e descanso” como eixo do item.

### Tempo em sala

- Leitura individual: 2 a 3 min.
- Discussão em dupla: 3 a 4 min.
- Correção comentada: 6 a 8 min.
- Total realista: 11 a 15 min.

### Relação com a tese da aula

Relação: **direta**.

A questão mostra que uma inovação técnica pode ampliar o tempo produtivo disponível em vez de reduzir automaticamente a jornada. Serve como ponte quase imediata para a ideia de que ganho tecnológico não vira tempo livre sem disputa social e proteção coletiva.

### Função pedagógica recomendada

- Demonstração guiada.
- Questão principal em dupla.
- Síntese curta.

## 4. Questão `2013_CH_017`

### Identificação documental

- ID interno: `2013_CH_017`
- Ano: 2013
- Número no corpus: 17
- Número oficial no caderno: Questão 17
- PDF de origem: `2013/dia1_caderno1_azul.pdf`
- Caderno: 1
- Cor: Azul
- Página oficial: 6
- Posição: coluna direita, parte superior
- Gabarito oficial: D
- PDF de gabarito: `2013/dia1_azul.pdf`
- PNG: `curadoria_questoes_04_07_assets/2013_CH_017.png`

### Conteúdo integral

**Componente visual**

A imagem compara dois modelos de produção.

No Modelo 1, a sequência aparece como:

> Fornecedor -> Estoque -> Produção -> Estoque -> Cliente

No Modelo 2, a sequência aparece orientada pela demanda:

> Cliente -> Produção -> Fornecedor

Entre cliente, produção e fornecedor aparecem setas de “Requisição” e “Entrega”, indicando fluxo puxado por demanda e menor centralidade de estoque.

Fonte citada:

> Disponível em: http://ensino.univates.br. Acesso em: 11 maio 2013 (adaptado).

**Comando**

> Na imagem, estão representados dois modelos de produção. A possibilidade de uma crise de superprodução é distinta entre eles em função do seguinte fator:

**Alternativas**

A. Origem da matéria-prima.

B. Qualificação da mão de obra.

C. Velocidade de processamento.

D. Necessidade de armazenamento.

E. Amplitude do mercado consumidor.

### Comparação com os CSVs

`corpus_enem/questoes_raw.csv`: preserva os rótulos principais do diagrama em texto, o comando, as alternativas e o gabarito. A extração não inclui a imagem real; transforma o artefato em sequência textual.

`analise/corpus_mestre.csv`:

- Disciplina atribuída: Geografia
- Tema: `Geografia Econômica > Modelos de Produção`
- Ancoragem: `artefato_visual`
- Tipo cognitivo: `aplicacao`
- Competência: `4.0`
- Habilidade: `H1`

Diferença relevante: para uso em sala, o PNG/PDF é necessário. O CSV permite entender a lógica geral, mas não substitui a força visual do item.

### O que a questão exige?

- Informação explícita no visual: sim.
- Inferência: sim, relacionar estoque ao risco de superprodução.
- Conhecimento histórico: baixo a médio.
- Conhecimento geográfico/econômico: médio.
- Interpretação visual: alta.
- Reconhecimento conceitual: modelos produtivos, estoque, demanda.
- Eliminação de distratores: sim.

### Conteúdo mínimo antes

- O que é produção em estoque.
- O que é produzir sob demanda.
- Ideia básica de superprodução.

### Conteúdo que pode emergir na correção

- Fordismo e produção em massa.
- Toyotismo/just in time como produção orientada por demanda.
- Estoque, demanda, produtividade e risco econômico.
- Organização espacial e logística da produção.

### Funcionamento dos distratores

- A: parece plausível porque fornecedor aparece no diagrama, mas a origem da matéria-prima não explica superprodução.
- B: parece plausível porque mão de obra é elemento produtivo, mas o diagrama não trata de qualificação.
- C: parece plausível porque há fluxo e setas, mas a crise de superprodução depende mais do acúmulo de estoque do que da velocidade em si.
- E: parece plausível porque cliente/mercado aparecem, mas o fator visualmente contrastado é a presença ou ausência de armazenamento intermediário.

### Dificuldade real

- Extensão textual: baixa.
- Vocabulário: baixo a médio.
- Abstração: média.
- Conhecimento prévio: médio.
- Dificuldade global para as turmas: média.

Justificativa: a questão é visual e curta, o que favorece entrada concreta. A dificuldade está em nomear o fator econômico correto: o estudante precisa perceber que estoque é a chave do contraste.

### Tempo em sala

- Leitura individual: 1 a 2 min.
- Discussão em dupla: 3 a 5 min.
- Correção comentada: 7 a 10 min.
- Total realista: 12 a 17 min.

### Relação com a tese da aula

Relação: **forte, mas parcial**.

A questão aborda organização produtiva e crise de superprodução, mas não trata diretamente de jornada ou proteção coletiva. Serve muito bem para explicar o lado “produtividade/modelo técnico”, mas precisa ser conectada depois à disputa política sobre tempo de trabalho.

### Função pedagógica recomendada

- Abertura.
- Questão principal em dupla.
- Reserva visual.

## 5. Questão `2015_CH_011`

### Identificação documental

- ID interno: `2015_CH_011`
- Ano: 2015
- Número no corpus: 11
- Número oficial no caderno: Questão 11
- PDF de origem: `2015/2015_PV_impresso_D1_CD1.pdf`
- Caderno: 1
- Cor: Azul
- Página oficial: 5
- Posição: topo da página, item em largura quase total
- Gabarito oficial: D
- PDF de gabarito: `2015/CADERNO_1_AZUL_SABADO.pdf`
- PNG: `curadoria_questoes_04_07_assets/2015_CH_011.png`

### Conteúdo integral

**Componente visual**

O item apresenta um calendário medieval do século XV, composto por doze imagens, uma para cada mês. As cenas mostram atividades ligadas ao ciclo anual, sobretudo trabalhos rurais e sazonais: preparo da terra, poda, cuidado com animais, colheita, debulha/beneficiamento, caça e tarefas associadas às estações.

Fonte citada:

> Disponível em: www.ac-grenoble.fr. Acesso em: 10 maio 2012.

**Texto de apoio e comando**

> Os calendários são fontes históricas importantes, na medida em que expressam a concepção de tempo das sociedades. Essas imagens compõem um calendário medieval (1460-1475) e cada uma delas representa um mês, de janeiro a dezembro. Com base na análise do calendário, apreende-se uma concepção de tempo

**Alternativas**

A. cíclica, marcada pelo mito arcaico do eterno retorno.

B. humanista, identificada pelo controle das horas de atividade por parte do trabalhador.

C. escatológica, associada a uma visão religiosa sobre o trabalho.

D. natural, expressa pelo trabalho realizado de acordo com as estações do ano.

E. romântica, definida por uma visão bucólica da sociedade.

### Comparação com os CSVs

`corpus_enem/questoes_raw.csv`: preserva o título, o texto de apoio, o comando, as alternativas e o gabarito. Não preserva o conteúdo visual das doze imagens.

`analise/corpus_mestre.csv`:

- Disciplina atribuída: História
- Tema: `historia medieval > concepções de tempo`
- Subtema: `trabalho e sociedade`
- Ancoragem: `artefato_visual`
- Tipo cognitivo: `analise`
- Competência: `1.0`
- Habilidade: `H1`

Diferença relevante: sem o PNG/PDF, o aluno não consegue resolver plenamente, porque a evidência está nas imagens do calendário.

### O que a questão exige?

- Informação explícita no visual: sim.
- Inferência: sim, associar meses/estações a trabalho.
- Conhecimento histórico: médio.
- Conhecimento geográfico: baixo.
- Interpretação visual: alta.
- Reconhecimento conceitual: concepção de tempo, trabalho sazonal.
- Eliminação de distratores: sim.

### Conteúdo mínimo antes

- O que é sociedade agrária.
- Diferença entre tempo natural/sazonal e tempo cronometrado.
- Ideia simples de Idade Média como mundo majoritariamente rural.

### Conteúdo que pode emergir na correção

- Tempo da natureza x tempo do relógio.
- Trabalho agrícola sazonal.
- Transição histórica para disciplina industrial do tempo.
- Como sociedades organizam trabalho conforme técnica e ambiente.

### Funcionamento dos distratores

- A: pode parecer correta porque calendários repetem ciclos, mas a alternativa puxa para mito arcaico, não para trabalho concreto nas estações.
- B: usa “controle das horas” e “trabalhador”, o que dialoga com a aula, mas não corresponde ao calendário medieval; é mais próximo da temporalidade moderna/industrial.
- C: é plausível por se tratar da Idade Média, mas o item visual enfatiza atividades produtivas sazonais, não escatologia.
- E: pode atrair pela aparência rural/bucólica das imagens, mas “romântica” é leitura estética posterior, não a concepção de tempo exigida.

### Dificuldade real

- Extensão textual: baixa.
- Vocabulário: médio.
- Abstração: média.
- Conhecimento prévio: médio.
- Dificuldade global para as turmas: média.

Justificativa: o item é visualmente acessível, mas a alternativa correta exige transformar observação de imagens em categoria histórica. A alternativa B é um distrator útil para discutir o nascimento do tempo industrial, embora não seja resposta.

### Tempo em sala

- Leitura individual: 2 min.
- Discussão em dupla: 3 a 4 min.
- Correção comentada: 6 a 8 min.
- Total realista: 11 a 14 min.

### Relação com a tese da aula

Relação: **forte, mas parcial**.

A questão ajuda a construir o contraste histórico entre tempo natural/sazonal e tempo moderno-industrial. Não aborda diretamente tecnologia contemporânea nem escala 6x1, mas pode preparar o terreno para a pergunta: quando o trabalho deixa de seguir a estação e passa a seguir o relógio?

### Função pedagógica recomendada

- Abertura.
- Demonstração guiada.
- Estudo prévio do professor.

## 6. Questão `2016_CH_040`

### Identificação documental

- ID interno: `2016_CH_040`
- Ano: 2016
- Número no corpus: 40
- Número oficial no caderno: Questão 40
- PDF de origem: `2016/2016_PV_impresso_D1_CD1.pdf`
- Caderno: 1
- Cor: Azul
- Página oficial: 13
- Posição: coluna direita, parte média/inferior
- Gabarito oficial: C
- PDF de gabarito: `2016/GAB_ENEM_2016_DIA_1_01_AZUL.pdf`

### Conteúdo integral

**Texto de apoio**

> A mundialização introduz o aumento da produtividade do trabalho sem acumulação de capital, justamente pelo caráter divisível da forma técnica molecular-digital do que resulta a permanência da má distribuição da renda: exemplificando mais uma vez, os vendedores de refrigerantes às portas dos estádios viram sua produtividade aumentada graças ao just in time dos fabricantes e distribuidores de bebidas, mas para realizar o valor de tais mercadorias, a forma do trabalho dos vendedores é a mais primitiva. Combinam-se, pois, acumulação molecular-digital com o puro uso da força de trabalho.

Fonte citada:

> OLIVEIRA, F. *Crítica à razão dualista e o ornitorrinco*. Campinas: Boitempo, 2003.

**Comando**

> Os aspectos destacados no texto afetam diretamente questões como emprego e renda, sendo possível explicar essas transformações pelo(a)

**Alternativas**

A. crise bancária e o fortalecimento do capital industrial.

B. inovação toyotista e a regularização do trabalho formal.

C. impacto da tecnologia e as modificações na estrutura produtiva.

D. emergência da globalização e a expansão do setor secundário.

E. diminuição do tempo de trabalho e a necessidade de diploma superior.

### Comparação com os CSVs

`corpus_enem/questoes_raw.csv`: texto, comando, alternativas e gabarito correspondem ao PDF oficial. Extração limpa.

`analise/corpus_mestre.csv`:

- Disciplina atribuída: Geografia
- Tema: `geopolítica > globalização e reestruturação do trabalho`
- Ancoragem: `texto_analitico`
- Tipo cognitivo: `análise`
- Competência: `6.0`
- Habilidade: `H30`

Não foram identificadas diferenças relevantes. O item está bem preservado no corpus.

### O que a questão exige?

- Informação explícita no texto: sim, produtividade, técnica molecular-digital, just in time, emprego e renda.
- Inferência: alta.
- Conhecimento histórico: médio.
- Conhecimento geográfico: médio a alto.
- Interpretação visual: não.
- Reconhecimento conceitual: globalização, tecnologia, estrutura produtiva, trabalho informal/primitivo.
- Eliminação de distratores: sim.

### Conteúdo mínimo antes

- Noção de globalização/mundialização.
- Ideia básica de produtividade.
- Noção mínima de just in time ou produção flexível.
- Relação entre tecnologia, emprego e renda.

### Conteúdo que pode emergir na correção

- Reestruturação produtiva.
- Trabalho informal e precarização.
- Produtividade sem distribuição de ganhos.
- Tecnologia incorporada à cadeia produtiva sem redução automática do esforço ou do tempo de trabalho.

### Funcionamento dos distratores

- A: parece plausível por falar em capital industrial, mas o texto não trata de crise bancária.
- B: menciona toyotismo e formalização; o just in time aparece, mas a regularização do trabalho formal contradiz o exemplo do vendedor.
- D: globalização aparece no texto, mas a expansão do setor secundário não é a transformação central.
- E: menciona diminuição do tempo de trabalho, que dialoga com a aula, mas o texto mostra produtividade combinada com trabalho primitivo, não redução de jornada nem exigência de diploma.

### Dificuldade real

- Extensão textual: média.
- Vocabulário: alto.
- Abstração: alta.
- Conhecimento prévio: médio a alto.
- Dificuldade global para as turmas: alta.

Justificativa: é talvez a questão mais alinhada à tese sociogeográfica, mas o texto é denso e abstrato. Exige forte mediação para não virar uma explicação professoral longa.

### Tempo em sala

- Leitura individual: 3 a 4 min.
- Discussão em dupla: 5 a 6 min.
- Correção comentada: 10 a 12 min.
- Total realista: 18 a 22 min.

### Relação com a tese da aula

Relação: **direta**.

A questão formula exatamente o problema da produtividade tecnológica sem distribuição justa de renda e sem melhoria proporcional das condições de trabalho. É forte para síntese conceitual, mas pesada como abertura.

### Função pedagógica recomendada

- Demonstração guiada.
- Síntese.
- Questão reserva de alto nível.

## 7. Questão `2016_CH_009`

### Identificação documental

- ID interno: `2016_CH_009`
- Ano: 2016
- Número no corpus: 9
- Número oficial no caderno: Questão 09
- PDF de origem: `2016/2016_PV_impresso_D1_CD1.pdf`
- Caderno: 1
- Cor: Azul
- Página oficial: 4
- Posição: coluna direita, parte superior
- Gabarito oficial: C
- PDF de gabarito: `2016/GAB_ENEM_2016_DIA_1_01_AZUL.pdf`

### Conteúdo integral

**Texto de apoio**

> Quanto mais complicada se tornou a produção industrial, mais numerosos passaram a ser os elementos da indústria que exigiam garantia de fornecimento. Três deles eram de importância fundamental: o trabalho, a terra e o dinheiro. Numa sociedade comercial, esse fornecimento só poderia ser organizado de uma forma: tornando-os disponíveis à compra. Agora eles tinham que ser organizados para a venda no mercado. Isso estava de acordo com a exigência de um sistema de mercado. Sabemos que em um sistema como esse, os lucros só podem ser assegurados se se garante a autorregulação por meio de mercados competitivos interdependentes.

Fonte citada:

> POLANYI, K. *A grande transformação: as origens de nossa época*. Rio de Janeiro: Campus, 2000 (adaptado).

**Comando**

> A consequência do processo de transformação socioeconômica abordado no texto é a

**Alternativas**

A. expansão das terras comunais.

B. limitação do mercado como meio de especulação.

C. consolidação da força de trabalho como mercadoria.

D. diminuição do comércio como efeito da industrialização.

E. adequação do dinheiro como elemento padrão das transações.

### Comparação com os CSVs

`corpus_enem/questoes_raw.csv`: texto, comando, alternativas e gabarito correspondem ao PDF oficial. Extração limpa.

`analise/corpus_mestre.csv`:

- Disciplina atribuída: História
- Tema: `capitalismo > grande transformacao`
- Subtema: `trabalho > comodificacao`
- Ancoragem: `texto_analitico`
- Tipo cognitivo: `analise`
- Competência: `5.0`
- Habilidade: `H20`

Não foram identificadas diferenças relevantes.

### O que a questão exige?

- Informação explícita no texto: sim, trabalho, terra e dinheiro organizados para venda.
- Inferência: média.
- Conhecimento histórico: médio.
- Conhecimento geográfico: baixo.
- Interpretação visual: não.
- Reconhecimento conceitual: capitalismo, mercado, mercadoria, força de trabalho.
- Eliminação de distratores: sim.

### Conteúdo mínimo antes

- Revolução Industrial como reorganização da produção.
- Mercado de trabalho.
- Diferença entre trabalho como atividade humana e força de trabalho como mercadoria.

### Conteúdo que pode emergir na correção

- Mercantilização do trabalho.
- Formação do capitalismo industrial.
- Relação entre lucro, mercado e controle da força de trabalho.
- Por que direitos trabalhistas são resposta política a uma relação assimétrica.

### Funcionamento dos distratores

- A: contradiz o texto; terras comunais tendem a ser dissolvidas, não expandidas, no processo descrito.
- B: usa “mercado”, mas o texto fala de expansão/regulação pelo mercado, não limitação.
- D: menciona industrialização, mas o texto aponta ampliação de relações mercantis, não diminuição do comércio.
- E: dinheiro aparece no texto, mas a pergunta pede a consequência central do processo; a alternativa reduz o problema ao padrão monetário.

### Dificuldade real

- Extensão textual: média.
- Vocabulário: médio a alto.
- Abstração: alta.
- Conhecimento prévio: médio.
- Dificuldade global para as turmas: alta.

Justificativa: a resposta é conceitualmente precisa, mas “força de trabalho como mercadoria” é uma formulação abstrata. Funciona melhor depois de alguma concretização histórica.

### Tempo em sala

- Leitura individual: 3 min.
- Discussão em dupla: 5 min.
- Correção comentada: 9 a 12 min.
- Total realista: 17 a 20 min.

### Relação com a tese da aula

Relação: **forte, mas parcial**.

A questão fundamenta a parte histórica da tese: o trabalho entra no mercado como mercadoria. Não trata diretamente de tecnologia nem de jornada, mas ajuda a explicar por que a redução de jornada depende de conflito político e proteção coletiva.

### Função pedagógica recomendada

- Questão principal em dupla, se a aula puxar mais para História.
- Síntese conceitual.
- Estudo prévio do professor.

## 8. Questão `2014_CH_005`

### Identificação documental

- ID interno: `2014_CH_005`
- Ano: 2014
- Número no corpus: 5
- Número oficial no caderno: Questão 05
- PDF de origem: `2014/2014_PV_impresso_D1_CD1.pdf`
- Caderno: 1
- Cor: Azul
- Página oficial: 3
- Posição: coluna direita, parte superior
- Gabarito oficial: A
- PDF de gabarito: `2014/CADERNO_1_AZUL_SABADO.pdf`
- PNG: `curadoria_questoes_04_07_assets/2014_CH_005.png`

### Conteúdo integral

**Componente visual**

Cartum de E. Neves, intitulado/referenciado como “Engraxate”. A imagem mostra um trabalhador engraxate sentado junto a uma placa com a inscrição “Não há vagas”. Ao fundo, máquinas/robôs e instalações industriais ocupam o espaço produtivo, sugerindo substituição ou marginalização do trabalho humano pela tecnologia.

Fonte citada:

> NEVES, E. *Engraxate*. Disponível em: www.grafar.blogspot.com. Acesso em: 15 fev. 2013.

**Comando**

> Considerando-se a dinâmica entre tecnologia e organização do trabalho, a representação contida no cartum é caracterizada pelo pessimismo em relação à

**Alternativas**

A. ideia de progresso.

B. concentração do capital.

C. noção de sustentabilidade.

D. organização dos sindicatos.

E. obsolescência dos equipamentos.

### Comparação com os CSVs

`corpus_enem/questoes_raw.csv`: preserva referência, comando, alternativas e gabarito. Não preserva a imagem do cartum, que é indispensável para resolver o item.

`analise/corpus_mestre.csv`:

- Disciplina atribuída: Sociologia
- Tema: `sociologia do trabalho > impacto da tecnologia e a ideia de progresso`
- Subtema: `crítica ao progresso`
- Ancoragem: `artefato_visual`
- Tipo cognitivo: `analise`
- Competência: `5.0`
- Habilidade: `H1`

Diferença relevante: sem o PNG/PDF, o item fica praticamente insolúvel, pois a crítica está no cartum.

### O que a questão exige?

- Informação explícita no visual: sim.
- Inferência: sim, ler o contraste entre máquinas, “não há vagas” e engraxate.
- Conhecimento histórico: baixo.
- Conhecimento geográfico: baixo.
- Interpretação visual: alta.
- Reconhecimento conceitual: tecnologia, progresso, trabalho.
- Eliminação de distratores: sim.

### Conteúdo mínimo antes

- Entender a ideia comum de progresso tecnológico.
- Perceber desemprego/exclusão como possível efeito social da automação.
- Saber que cartum faz crítica por ironia.

### Conteúdo que pode emergir na correção

- Tecnologia e desemprego.
- Crítica à ideia linear de progresso.
- Automação e substituição de trabalho.
- Relação com precarização e informalidade.

### Funcionamento dos distratores

- B: pode parecer correta porque capital e tecnologia se relacionam, mas o cartum critica mais diretamente a promessa de progresso.
- C: não há pista visual ou textual sobre sustentabilidade.
- D: sindicatos aparecem como tema possível de trabalho, mas não são representados no cartum.
- E: “obsolescência” se aproxima de tecnologia, mas o problema visual não é equipamento velho; é a exclusão humana em meio a máquinas modernas.

### Dificuldade real

- Extensão textual: baixa.
- Vocabulário: baixo.
- Abstração: baixa a média.
- Conhecimento prévio: baixo.
- Dificuldade global para as turmas: baixa a média.

Justificativa: a entrada visual é forte e o comando é curto. O risco está em o aluno escolher uma alternativa temática próxima, como capital, sem perceber que a crítica mais ampla é à ideia de progresso.

### Tempo em sala

- Leitura/observação individual: 1 a 2 min.
- Discussão em dupla: 3 min.
- Correção comentada: 5 a 7 min.
- Total realista: 9 a 12 min.

### Relação com a tese da aula

Relação: **forte, mas parcial**.

A questão dialoga bem com tecnologia e trabalho, especialmente com desemprego tecnológico e crítica ao progresso. Não aborda jornada nem disputa política diretamente, mas é excelente para abrir a pergunta: progresso para quem?

### Função pedagógica recomendada

- Abertura.
- Reserva visual.
- Demonstração guiada curta.

## 9. Comparação Final

| ID | Entrada concreta/visual | Relação com 6x1 | História-Geografia | Dificuldade | Tempo estimado | Função recomendada |
| -- | ----------------------: | --------------: | -----------------: | ----------- | -------------: | ------------------ |
| `2015_CH_002` | Baixa | Alta | Média | Média | 11-15 min | Principal guiada / síntese |
| `2013_CH_017` | Alta | Média | Alta | Média | 12-17 min | Abertura / dupla / reserva visual |
| `2015_CH_011` | Alta | Média | Alta | Média | 11-14 min | Abertura histórica / demonstração |
| `2016_CH_040` | Baixa | Alta | Alta | Alta | 18-22 min | Síntese / reserva de alto nível |
| `2016_CH_009` | Baixa | Média | Alta | Alta | 17-20 min | Principal histórica / síntese |
| `2014_CH_005` | Alta | Média | Média | Baixa-média | 9-12 min | Abertura / reserva visual |

### 1. Melhor questão principal

Recomendação provisória: **`2015_CH_002`**.

Justificativa: é a mais diretamente ligada à tese da aula e ao debate da escala 6x1. A questão permite discutir tecnologia, tempo produtivo, trabalho e descanso sem exigir entrada conceitual pesada. É menos visual, mas mais precisa para a pergunta central da aula.

### 2. Melhor abertura

Recomendação provisória: **`2014_CH_005`**, com `2015_CH_011` como alternativa se o professor de História quiser iniciar historicamente.

Justificativa: `2014_CH_005` oferece entrada visual imediata, comando curto e tema reconhecível: tecnologia pode excluir trabalhadores em vez de libertá-los. `2015_CH_011` é excelente para abrir a linha histórica do tempo do trabalho, mas exige leitura de imagem menos contemporânea.

### 3. Melhor reserva

Recomendação provisória: **`2013_CH_017`**.

Justificativa: visualmente forte, ligada a modelos produtivos e útil para explicar estoque, produção sob demanda e risco de superprodução. Funciona bem se a aula precisar migrar para organização produtiva sem entrar em texto abstrato.

### 4. Combinação que exige menos exposição abstrata do professor

Combinação provisória: **`2014_CH_005` + `2015_CH_002` + `2013_CH_017`**.

Motivo: começa por cartum, passa para texto curto sobre jornada e fecha com diagrama produtivo. Evita iniciar por Polanyi ou Francisco de Oliveira, que demandariam maior exposição conceitual.

### 5. Combinação que permite participação dos dois docentes

Combinação provisória: **`2015_CH_011` + `2015_CH_002` + `2016_CH_009`**.

Motivo: o professor de História pode conduzir a transição do tempo natural/sazonal para o capitalismo industrial e o professor pode articular tecnologia, produtividade e organização contemporânea do trabalho. O risco é elevar a abstração se `2016_CH_009` virar questão principal.

### 6. Questão com maior risco de desvio conceitual

**`2016_CH_040`**.

Motivo: é muito aderente à tese, mas o texto é denso e pode levar a uma explicação longa sobre mundialização, just in time, acumulação molecular-digital e reestruturação produtiva. Há risco de a aula sair da resolução de questão e virar exposição abstrata.

### 7. Questão a excluir apesar de sua relevância teórica

Exclusão provisória da aula principal: **`2016_CH_009`**, se houver apenas 70 minutos e a prioridade for escala 6x1.

Motivo: é teoricamente forte para História do capitalismo e mercantilização do trabalho, mas tem alta abstração. Pode ser mantida para estudo prévio dos professores ou como síntese se a turma estiver respondendo bem, mas não parece a melhor candidata para abrir nem para ser a questão principal em uma aula que precisa chegar ao debate contemporâneo da jornada.

## 10. Recomendação Provisória

Sem decisão definitiva, a combinação mais equilibrada para a aula parece ser:

1. Abertura visual: `2014_CH_005`
2. Questão principal: `2015_CH_002`
3. Reserva/síntese visual-produtiva: `2013_CH_017`

Essa combinação sustenta a tese sem exigir que a aula comece por conceitos abstratos. Ela permite passar por três degraus: crítica visual ao progresso tecnológico, ampliação da jornada pela tecnologia e reorganização dos modelos de produção.

Alternativa com maior participação histórica do professor de História:

1. Abertura histórica visual: `2015_CH_011`
2. Questão principal: `2015_CH_002`
3. Síntese histórica conceitual: `2016_CH_009`

Essa segunda combinação é mais elegante historicamente, mas mais abstrata e possivelmente mais lenta.

## 11. Confirmação de Escopo

Nesta rodada foram criados apenas:

- `RELATORIO_CURADORIA_QUESTOES_AULA_04_07.md`
- `curadoria_questoes_04_07_assets/2013_CH_017.png`
- `curadoria_questoes_04_07_assets/2015_CH_011.png`
- `curadoria_questoes_04_07_assets/2014_CH_005.png`

Não houve commit, chamada externa, execução de Gemini, reprocessamento de provas, criação de CSV, alteração de PDF ou limpeza/reversão de arquivos existentes.
