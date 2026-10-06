---
gerado: 2026-09-30
origem: pipeline/analise/corpus_mestre.csv (sha256 4749df4a5bd1…; repositório com árvore suja, versão de trabalho)
script: fontes/filtrar_corpus_proenem.py
status: TRIAGEM. Nenhuma questão conferida. Não citar, não usar em slide.
---

# Candidatas do corpus PROENEM (geografia)

Corpus: 355 questões rotuladas CH (caderno azul, 2013–2019 e 2025). **Só 2013–2016 são CH de fato**: as linhas de 2017, 2018, 2019 e 2025 são Linguagens (ver `conferencia-inep-candidatas.md`) e foram excluídas. Geografia (principal ou secundária) em 2013–2016: 62.

**Avisos**
- Tema, disciplina e gabarito vêm de extração automática e classificação por IA (rank 3). Servem para triar.
- Para tirar o rótulo **(autoral)** é preciso abrir o caderno oficial do INEP e confirmar ano, caderno, número, enunciado e gabarito, e então registrar em `fontes/checagem.md`.
- O corpus não cobre Ciências da Natureza nem 2020–2024, e o texto do PDF traz quebras (ex.: “intensifi c ação”). Cinco questões estão sem enunciado.
- A coluna “grupos” é busca por palavra-chave no tema (IA) e, marcada “(texto)”, no enunciado. Não é classificação. As alternativas não entram na busca.

## Resumo por grupo

| grupo | questões |
|---|---|
| energia | 4 |
| água | 9 |
| clima | 5 |
| relevo e solo | 8 |
| domínios e biomas | 8 |
| tecnologia e dados | 7 |
| território e infraestrutura | 8 |
| (nenhum grupo) | 32 |

## energia

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2013_CH_002 | 2013/2 | A | Geografia Urbana > Crescimento Urbano e Periferização | energia (texto), água (texto), território e infraestrutura (texto) | Mapa 2 Conﬂ itos em terras indígenas PRINCIPAIS ENVOLVIDOS EM CONFRONTOS COM ÍNDIOS NOS ÚLTIMOS ANOS PRINCIPAI… | a conferir |
| 2013_CH_043 | 2013/43 | C | geografia > fontes de energia > energia eólica | energia, tecnologia e dados (texto) | Empresa vai fornecer 230 turbinas para o segundo complexo de energia à base de ventos, no sudeste da Bahia. O … | a conferir |
| 2014_CH_034 | 2014/34 | C | geografia > energia e meio ambiente | energia, tecnologia e dados (texto) | Disponível em: www.banktrack.org. Acesso em: 7 maio 2013 (adaptado). A imagem indica pontos com ativo uso de t… | a conferir |
| 2016_CH_012 | 2016/12 | D | geopolitica > conflitos territoriais e recursos naturais | energia (texto), água (texto) | No início de maio de 2014, a instalação da plataforma petrolífera de perfuração HYSY-981 nas águas contestadas… | a conferir |

## água

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2013_CH_002 | 2013/2 | A | Geografia Urbana > Crescimento Urbano e Periferização | energia (texto), água (texto), território e infraestrutura (texto) | Mapa 2 Conﬂ itos em terras indígenas PRINCIPAIS ENVOLVIDOS EM CONFRONTOS COM ÍNDIOS NOS ÚLTIMOS ANOS PRINCIPAI… | a conferir |
| 2014_CH_003 | 2014/3 | B | geografia > impactos socioambientais > Mar de Aral | água (texto) | Os dois principais rios que alimentavam o Mar de Aral, Amurdarya e Sydarya, mantiveram o nível e o volume do m… | a conferir |
| 2014_CH_007 | 2014/7 | A | sociologia rural > desigualdade na distribuição da produção | água (texto) | Mas plantar pra dividir Não faço mais isso, não. Eu sou um pobre caboclo, Ganho a vida na enxada. O que eu col… | a conferir |
| 2015_CH_021 | 2015/21 | E | geopolitica > segurança de dados | água (texto), tecnologia e dados | Atualmente, as represálias econômicas contra as empresas de informática norte-americanas continuam. A Alemanha… | a conferir |
| 2015_CH_032 | 2015/32 | E | geografia > hidrografia > veredas e cerrado | água, clima (texto), relevo e solo (texto), domínios e biomas | Algumas regiões do Brasil passam por uma crise de água por causa da seca. Mas, uma região de Minas Gerais está… | a conferir |
| 2015_CH_033 | 2015/33 | A | geografia agraria > tecnologia e agricultura | água (texto), relevo e solo (texto), tecnologia e dados | Tanto potencial poderia ter ficado pelo caminho, se não fosse o reforço em tecnologia que um gaúcho buscou. Há… | a conferir |
| 2016_CH_012 | 2016/12 | D | geopolitica > conflitos territoriais e recursos naturais | energia (texto), água (texto) | No início de maio de 2014, a instalação da plataforma petrolífera de perfuração HYSY-981 nas águas contestadas… | a conferir |
| 2016_CH_036 | 2016/36 | C | geografia > recursos hídricos > escassez hídrica | água | Estados Unidos 5 653 941 | a conferir |
| 2016_CH_039 | 2016/39 | A | geografia > impactos ambientais > exploração de recursos marinhos | água (texto) | Pesca industrial provoca destruição na África O súbito desaparecimento do bacalhau dos grandes cardumes da Ter… | a conferir |

## clima

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2014_CH_020 | 2014/20 | E | geografia ambiental > combate a desertificacao | clima | Antes de o sol começar a esquentar as terras da faixa ao sul do Saara conhecida como Sahel, duas dezenas de mu… | a conferir |
| 2014_CH_035 | 2014/35 | E | geografia > clima > dinâmica atmosférica > Amazônia | clima, domínios e biomas | A convecção na Região Amazônica é um importante mecanismo da atmosfera tropical e sua variação, em termos de i… | a conferir |
| 2015_CH_030 | 2015/30 | B | geografia física > geomorfologia > movimentos de massa | clima (texto), relevo e solo | Os movimentos de massa constituem-se no deslocamento de material (solo e rocha) vertente abaixo pela influênci… | a conferir |
| 2015_CH_032 | 2015/32 | E | geografia > hidrografia > veredas e cerrado | água, clima (texto), relevo e solo (texto), domínios e biomas | Algumas regiões do Brasil passam por uma crise de água por causa da seca. Mas, uma região de Minas Gerais está… | a conferir |
| 2016_CH_018 | 2016/18 | D | geopolitica > meio ambiente > Protocolo de Quioto | clima (texto), domínios e biomas (texto), tecnologia e dados (texto), território e infraestrutura (texto) | Segundo a Conferência de Quioto, os países centrais industrializados, responsáveis históricos pela poluição, d… | a conferir |

## relevo e solo

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2013_CH_014 | 2013/14 | A | biogeografia > biomas brasileiros > caatinga | relevo e solo (texto), domínios e biomas | Então, a travessia das veredas sertanejas é mais exaustiva que a de uma estepe nua. Nesta, ao menos, o viajant… | a conferir |
| 2013_CH_028 | 2013/28 | A | geografia > agricultura > técnicas de conservação do solo | relevo e solo | Disponível em: http://BP.blogspot.com. Acesso em: 24 ago. 2011. Na imagem, visualiza-se um método de cultivo e… | a conferir |
| 2014_CH_036 | 2014/36 | D | geografia fisica > tectonica de placas | relevo e solo | Disponível em: www.telescopionaescola.pro.br. Acesso em: 3 abr. 2014 (adaptado). A partir da análise da imagem… | a conferir |
| 2015_CH_030 | 2015/30 | B | geografia física > geomorfologia > movimentos de massa | clima (texto), relevo e solo | Os movimentos de massa constituem-se no deslocamento de material (solo e rocha) vertente abaixo pela influênci… | a conferir |
| 2015_CH_031 | 2015/31 | C | geografia física > geomorfologia > erosão fluvial | relevo e solo | SUERTEGARAY, D. M. A. (Org.).Terra: feições ilustradas. Porto Alegre: EdUFRGS, 2003 (adaptado). A imagem repre… | a conferir |
| 2015_CH_032 | 2015/32 | E | geografia > hidrografia > veredas e cerrado | água, clima (texto), relevo e solo (texto), domínios e biomas | Algumas regiões do Brasil passam por uma crise de água por causa da seca. Mas, uma região de Minas Gerais está… | a conferir |
| 2015_CH_033 | 2015/33 | A | geografia agraria > tecnologia e agricultura | água (texto), relevo e solo (texto), tecnologia e dados | Tanto potencial poderia ter ficado pelo caminho, se não fosse o reforço em tecnologia que um gaúcho buscou. Há… | a conferir |
| 2016_CH_029 | 2016/29 | A | geografia urbana > função social da cidade e políticas públicas | relevo e solo (texto) | O conceito de função social da cidade incorpora a organização do espaço físico como fruto da regulação social,… | a conferir |

## domínios e biomas

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2013_CH_014 | 2013/14 | A | biogeografia > biomas brasileiros > caatinga | relevo e solo (texto), domínios e biomas | Então, a travessia das veredas sertanejas é mais exaustiva que a de uma estepe nua. Nesta, ao menos, o viajant… | a conferir |
| 2013_CH_037 | 2013/37 | C | geografia > impactos socioeconômicos e ambientais > infraestrutura na Amazônia | domínios e biomas, território e infraestrutura | Nos últimos decênios, o território conhece grandes mudanças em função de acréscimos técnicos que renovam a sua… | a conferir |
| 2014_CH_035 | 2014/35 | E | geografia > clima > dinâmica atmosférica > Amazônia | clima, domínios e biomas | A convecção na Região Amazônica é um importante mecanismo da atmosfera tropical e sua variação, em termos de i… | a conferir |
| 2015_CH_001 | 2015/1 | A | geografia fisica > biomas e problemas ambientais | domínios e biomas | BRASIL. Ministério do Meio Ambiente/IBGE. Biomas. 2004 (adaptado). No mapa estão representados os biomas brasi… | a conferir |
| 2015_CH_015 | 2015/15 | D | Geografia Humana > Territorialidade e identidades coletivas | domínios e biomas (texto) | O Projeto Nova Cartografia Social da Amazônia ensina indígenas, quilombolas e outros grupos tradicionais a emp… | a conferir |
| 2015_CH_032 | 2015/32 | E | geografia > hidrografia > veredas e cerrado | água, clima (texto), relevo e solo (texto), domínios e biomas | Algumas regiões do Brasil passam por uma crise de água por causa da seca. Mas, uma região de Minas Gerais está… | a conferir |
| 2016_CH_018 | 2016/18 | D | geopolitica > meio ambiente > Protocolo de Quioto | clima (texto), domínios e biomas (texto), tecnologia e dados (texto), território e infraestrutura (texto) | Segundo a Conferência de Quioto, os países centrais industrializados, responsáveis históricos pela poluição, d… | a conferir |
| 2016_CH_030 | 2016/30 | E | Geografia Agrária > Expansão da fronteira agrícola e impactos ambientais | domínios e biomas (texto), território e infraestrutura | O bioma Cerrado foi considerado recentemente um dos 25 hotspots de biodiversidade do mundo, segundo uma anális… | a conferir |

## tecnologia e dados

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2013_CH_043 | 2013/43 | C | geografia > fontes de energia > energia eólica | energia, tecnologia e dados (texto) | Empresa vai fornecer 230 turbinas para o segundo complexo de energia à base de ventos, no sudeste da Bahia. O … | a conferir |
| 2014_CH_034 | 2014/34 | C | geografia > energia e meio ambiente | energia, tecnologia e dados (texto) | Disponível em: www.banktrack.org. Acesso em: 7 maio 2013 (adaptado). A imagem indica pontos com ativo uso de t… | a conferir |
| 2015_CH_021 | 2015/21 | E | geopolitica > segurança de dados | água (texto), tecnologia e dados | Atualmente, as represálias econômicas contra as empresas de informática norte-americanas continuam. A Alemanha… | a conferir |
| 2015_CH_029 | 2015/29 | E | geografia econômica > globalização > impactos no trabalho e produção | tecnologia e dados (texto) | No final do século XX e em razão dos avanços da ciência, produziu-se um sistema presidido pelas técnicas da in… | a conferir |
| 2015_CH_033 | 2015/33 | A | geografia agraria > tecnologia e agricultura | água (texto), relevo e solo (texto), tecnologia e dados | Tanto potencial poderia ter ficado pelo caminho, se não fosse o reforço em tecnologia que um gaúcho buscou. Há… | a conferir |
| 2016_CH_018 | 2016/18 | D | geopolitica > meio ambiente > Protocolo de Quioto | clima (texto), domínios e biomas (texto), tecnologia e dados (texto), território e infraestrutura (texto) | Segundo a Conferência de Quioto, os países centrais industrializados, responsáveis históricos pela poluição, d… | a conferir |
| 2016_CH_040 | 2016/40 | C | geopolítica > globalização e reestruturação do trabalho | tecnologia e dados (texto) | A mundialização introduz o aumento da produtividade do trabalho sem acumulação de capital, justamente pelo car… | a conferir |

## território e infraestrutura

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2013_CH_001 | 2013/1 | E | geografia > demografia > distribuição populacional e urbanização | território e infraestrutura | Mapa 1 Distribuição espacial atual da população brasileira THÉRY, H. As boas-novas sobre a população brasileir… | a conferir |
| 2013_CH_002 | 2013/2 | A | Geografia Urbana > Crescimento Urbano e Periferização | energia (texto), água (texto), território e infraestrutura (texto) | Mapa 2 Conﬂ itos em terras indígenas PRINCIPAIS ENVOLVIDOS EM CONFRONTOS COM ÍNDIOS NOS ÚLTIMOS ANOS PRINCIPAI… | a conferir |
| 2013_CH_034 | 2013/34 | C | geografia urbana > urbanização em países em desenvolvimento | território e infraestrutura | Embora haja dados comuns que dão unidade ao fenômeno da urbanização na África, na Ásia e na América Latina, os… | a conferir |
| 2013_CH_037 | 2013/37 | C | geografia > impactos socioeconômicos e ambientais > infraestrutura na Amazônia | domínios e biomas, território e infraestrutura | Nos últimos decênios, o território conhece grandes mudanças em função de acréscimos técnicos que renovam a sua… | a conferir |
| 2014_CH_027 | 2014/27 | E | geografia urbana > transporte e rodoviarismo | território e infraestrutura | A urbanização brasileira, no início da segunda metade do século XX, promoveu uma radical alteração nas cidades… | a conferir |
| 2015_CH_012 | 2015/12 | E | geografia urbana > dinâmica populacional | território e infraestrutura (texto) | O processo de concentração urbana no Brasil em determinados locais teve momentos de maior intensidade e, ao qu… | a conferir |
| 2016_CH_018 | 2016/18 | D | geopolitica > meio ambiente > Protocolo de Quioto | clima (texto), domínios e biomas (texto), tecnologia e dados (texto), território e infraestrutura (texto) | Segundo a Conferência de Quioto, os países centrais industrializados, responsáveis históricos pela poluição, d… | a conferir |
| 2016_CH_030 | 2016/30 | E | Geografia Agrária > Expansão da fronteira agrícola e impactos ambientais | domínios e biomas (texto), território e infraestrutura | O bioma Cerrado foi considerado recentemente um dos 25 hotspots de biodiversidade do mundo, segundo uma anális… | a conferir |

## Geografia sem gancho por palavra-chave

| id | ano/nº | gab. | tema (IA) | grupos | início do enunciado | conferência |
|---|---|---|---|---|---|---|
| 2013_CH_003 | 2013/3 | E | geografia urbana > patrimônio cultural e paisagem | - | No dia 1º de julho de 2012, a cidade do Rio de Janeiro tornou-se a primeira do mundo a receber o título da Une… | a conferir |
| 2013_CH_009 | 2013/9 | B | demografia > taxas de fecundidade | - | Taxa de fecundidade total – Brasil – 1940-2010 6,16 6,21 6,28 5,76 4,35 2,85 2,38 1,90 IBGE. Censo demográfico… | a conferir |
| 2013_CH_017 | 2013/17 | D | Geografia Econômica > Modelos de Produção | - | Modelo 1 Fornecedor Estoque Produção Estoque Cliente Modelo 2 Requisição Requisição Entrega Entrega Cliente Pr… | a conferir |
| 2013_CH_022 | 2013/22 | D | geopolitica > economia global | - | Na canção, ressalta-se a coexistência, no contexto internacional atual, das seguintes situações: | a conferir |
| 2013_CH_030 | 2013/30 | E | reforma agrária > conflitos agrários e função social da terra | - | TEXTO I A nossa luta é pela democratização da propriedade da terra, cada vez mais concentrada em nosso país. C… | a conferir |
| 2013_CH_039 | 2013/39 | C | história do Brasil > desenvolvimentismo JK > contradições socioeconômicas | - | Meta de Faminto JK — Você agora tem automóvel brasileiro, para correr em estradas pavimentadas com asfalto bra… | a conferir |
| 2014_CH_001 | 2014/1 | E | historia do brasil > republica velha > modernizacao e comunicacao | - | A charge, datada de 1910, ao retratar a implantação da rede telefônica no Brasil, indica que esta | a conferir |
| 2014_CH_009 | 2014/9 | E | Geografia Econômica > Globalização e terceirização de serviços | - | TEXTO I Disponível em: http://twistedsifter.com. Acesso em: 5 nov. 2013 (adaptado). TEXTO II A Índia deu um pa… | a conferir |
| 2014_CH_010 | 2014/10 | C | geografia humana > migrações > emigração de mão de obra qualificada | - | O jovem espanhol Daniel se sente perdido. Seu diploma de desenhista industrial e seu alto conhecimento de ingl… | a conferir |
| 2014_CH_013 | 2014/13 | B | geografia física > movimentos da Terra > fusos horários | - | Quando é meio-dia nos Estados Unidos, o Sol, todo mundo sabe, está se deitando na França. Bastaria ir à França… | a conferir |
| 2014_CH_022 | 2014/22 | D | geografia urbana > segregação socioespacial | - | No século XIX, o preço mais alto dos terrenos situados no centro das cidades é causa da especialização dos bai… | a conferir |
| 2014_CH_026 | 2014/26 | D | geografia urbana > dinâmica populacional e conurbação | - | Confins Ribeirão das Neves Vespasiano Santa Luzia Sabará Contagem Belo Horizonte Betim Ibirité Nova Lima Saldo… | a conferir |
| 2014_CH_031 | 2014/31 | A | história urbana > memória e simbolismo | - | A Praça da Concórdia, antiga Praça Luís XV, é a maior praça pública de Paris. Inaugurada em 1763, tinha em seu… | a conferir |
| 2014_CH_037 | 2014/37 | C | geopolitica > blocos economicos / organismos internacionais | - | Na imagem, é ressaltado, em tom mais escuro, um grupo de países que na atualidade possuem características polí… | a conferir |
| 2014_CH_038 | 2014/38 | E | Geografia > Sustentabilidade e gestão ambiental | - | A preservação da sustentabilidade do recurso natural exposto pressupõe | a conferir |
| 2015_CH_004 | 2015/4 | E | geografia agrária > agrotóxicos e impactos ambientais | - | AMARILDO. Disponível em: www.amarildo.com.br. Acesso em: 3 mar. 2013. Na charge há uma crítica ao processo pro… | a conferir |
| 2015_CH_007 | 2015/7 | E | historia contemporanea > china e socialismo de mercado | - | O principal articulador do atual modelo econômico chinês argumenta que o mercado é só um instrumento econômico… | a conferir |
| 2015_CH_008 | 2015/8 | C | Economia Global > Crises Financeiras > Crise do Subprime de 2008 | - | Até o fim de 2007, quase 2 milhões de pessoas perderam suas casas e outros 4 milhões corriam o risco de ser de… | a conferir |
| 2015_CH_027 | 2015/27 | D | geografia fisica > intemperismo | - | 1. Muito Fraco Temperatura (°C) | a conferir |
| 2015_CH_038 | 2015/38 | D | geopolitica > globalização e cadeias produtivas | - | Um carro esportivo é financiado pelo Japão, projetado na Itália e montado em Indiana, México e França, usando … | a conferir |
| 2015_CH_044 | 2015/44 | B | historia > patrimonio cultural > conflitos e destruicao | - | A Unesco condenou a destruição da antiga capital assíria de Nimrod, no Iraque, pelo Estado Islâmico, com a agê… | a conferir |
| 2015_CH_045 | 2015/45 | D | geografia > questão ambiental > preservação ambiental | - | A questão ambiental, uma das principais pautas contemporâneas, possibilitou o surgimento de concepções polític… | a conferir |
| 2016_CH_003 | 2016/3 | B | geografia urbana > mobilidade urbana > movimento pendular | - | Os moradores de Andalsnes, na Noruega, poderiam se dar ao luxo de morar perto do trabalho nos dias úteis e de … | a conferir |
| 2016_CH_004 | 2016/4 | C | geografia urbana > redes urbanas e polarização | - | O Rio de Janeiro tem projeção imediata no próprio estado e no Espírito Santo, em parcela do sul do estado da B… | a conferir |
| 2016_CH_016 | 2016/16 | E | geopolitica > blocos economicos | - | Parceria Transpacífica Japão Vietnã Cingapura Brunei Darussalam Malásia Austrália Nova Zelândia Dentro das atu… | a conferir |
| 2016_CH_019 | 2016/19 | B | geografia > globalização > migrações internacionais e remessas | - | Dados recentes mostram que muitos são os países periféricos que dependem dos recursos enviados pelos imigrante… | a conferir |
| 2016_CH_031 | 2016/31 | E | geopolítica > fluxos migratórios e políticas de fronteira | - | TEXTO I Mais de 50 mil refugiados entraram no território húngaro apenas no primeiro semestre de 2015. Budapest… | a conferir |
| 2016_CH_034 | 2016/34 | A | historia ambiental > pensamento ambiental brasileiro (séculos XVIII-XIX) | - | A linhagem dos primeiros críticos ambientais brasileiros não praticou o elogio laudatório da beleza e da grand… | a conferir |
| 2016_CH_038 | 2016/38 | D | historia do brasil > transformacoes socioeconomicas > desigualdade regional | - | O Cruzeiro, década de 1960. Disponível em: www.memoriaviva.com.br. Acesso em: 28 fev. 2012 (adaptado). No anún… | a conferir |
| 2016_CH_043 | 2016/43 | D | historia econômica > economia cafeeira e comércio internacional | - | Uma scena franco-brazileira: “franco” — pelo local e os personagens, o local que é Paris e os personagens que … | a conferir |
| 2016_CH_044 | 2016/44 | B | sociedade > transformações rurais e cultura | - | Participei de uma entrevista com o músico Renato Teixeira. Certa hora, alguém pediu para listar as diferenças … | a conferir |
| 2016_CH_045 | 2016/45 | A | demografia > transição demográfica > consequências socioeconômicas | - | O número de ﬁ lhos por casal diminui rapidamente. Para a maioria dos economistas, isso representa um alerta pa… | a conferir |

## Sem enunciado no corpus

2013_CH_042, 2014_CH_016, 2016_CH_035, 2025_CH_005, 2025_CH_040
