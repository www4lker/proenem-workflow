INSUMO PEDAGÓGICO — Corpus ENEM CH para aula 04/07/2026
Para: instância pedagógica (planejamento de aula)
De: instância técnica (pipeline corpus)
Estado: corpus Pass 2 fechado, HEAD 8b3d88f

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CORPUS — NÚMEROS FINAIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

355 questões ENEM CH extraídas (2013–2019 + 2025, caderno azul, dia 1).
348 classificadas com: disciplina, tema, ancoragem, competência,
habilidade, tipo cognitivo.
7 sem classificação (5 enunciado NaN + 2 falhas persistentes de API).

Arquivos no repo pipeline:
  analise/corpus_mestre.csv         — corpus completo com classificações
  analise/geopolitica_aula_04_07.csv — subconjunto filtrado (ver abaixo)
  corpus_enem/questoes_raw.csv      — fonte: enunciado + alternativas + gabarito

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTRUTURA DE ANCORAGEM DO CORPUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Global (348 questões):
  texto_analitico:  200 (57,5%)  ← maioria absoluta
  evento_narrativo:  84 (24,1%)
  artefato_visual:   55 (15,8%)
  composto:           9  (2,6%)

IMPLICAÇÃO: o ENEM CH é dominantemente texto_analitico. A turma que
processa por narrativa/concreto está em desvantagem estrutural na prova
— não é percepção do professor, é dado do corpus.

Por disciplina — o que é processável pela turma
(evento_narrativo + artefato_visual + composto):
  História:   56/101 (55%) ← mais processável
  Geografia:  25/56  (45%)
  Sociologia: 55/133 (41%)
  Filosofia:  12/58  (21%) ← menos processável — quase tudo texto_analitico

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HEATMAP COMPETÊNCIA × ANO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

            2013 2014 2015 2016 2017 2018 2019 2025  TOTAL
  C1           5    7    9    3    5    7    7    5     48
  C2           4    3    3    2    7    3    4    5     31
  C3           0    0    3    2    2    1    1    1     10
  C4          10   11    8    8    1    1    1    0     40
  C5          18   21   16   19   30   32   32   32    200
  C6           2    2    6    9    0    0    0    0     19

LEITURA PARA PLANEJAMENTO:
  C5 (Indivíduo/sociedade/natureza/cultura): domina 2017–2025.
  58% de todas as questões dos últimos 4 anos cobertos são C5.
  
  C6 (Geopolítica/mundialização): presente 2013–2016, zera depois.
  CAVEAT IMPORTANTE: isso pode ser artifact de classificação do Gemini
  defaultando para C5 em questões ambíguas — não tratar como "geopolítica
  saiu do ENEM". Tratar como: C6 era label explícito até 2016; depois
  o tema migrou para C5 ou a classificação automática perdeu precisão.
  Verificar manualmente 2–3 questões de 2017–2025 com tema geopolítico
  antes de usar este dado como argumento curricular.

  C4 (Produção/apropriação do espaço): forte 2013–2016, quase desaparece
  depois. Padrão real, consistente com a virada temática da prova.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUESTÕES PARA A AULA 04/07 — SUBCONJUNTO LIMPO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6 questões geopolítica com ancoragem processável pela turma.
(2025_CH_022 removida — falso positivo: artesanato, não geopolítica.)

Ordenadas por potencial pedagógico para esta turma:

── TIER 1 — ENTRADA FORTE (narrativa + C6 explícito) ──

2016_CH_031 | evento_narrativo | C6 | H1 | análise
  Tema: fluxos migratórios e políticas de fronteira
  Gabarito: E
  → Crise dos refugiados sírios / fechamento da fronteira húngara (2015).
    Personagem identificável, conflito datado, tensão territorial concreta.
    Entra direto no princípio evento→tensão→conceito. Melhor candidata
    para abrir a aula.

2015_CH_021 | evento_narrativo | C6 | H30 | análise
  Tema: geopolítica > segurança de dados
  Gabarito: E
  → Provavelmente espionagem NSA/Snowden (2013). Evento com personagem,
    dimensão de soberania nacional, relevante para turma de 2026.

2014_CH_023 | evento_narrativo | C6 | H3 | análise
  Tema: imperialismo > causas da 1ª Guerra Mundial
  Gabarito: B
  → Narrativa histórica com personagens e conflito datado. Risco: distância
    temporal pode reduzir identificação. Útil como ponto de chegada
    conceitual (imperialismo), não como abertura.

── TIER 2 — ARTEFATO VISUAL (mapa/imagem como âncora) ──

2014_CH_037 | artefato_visual | C6 | H1 | análise
  Tema: blocos econômicos / organismos internacionais
  Gabarito: C
  → Mapa de blocos. Funciona como âncora visual antes de nomear conceitos.
    Sequência sugerida: mostrar mapa → "o que você já ouviu falar desses
    grupos?" → nomear os blocos → conceito de multipolaridade.

2018_CH_022 | artefato_visual | C2 | H1 | análise
  Tema: fronteiras e diversidade cultural
  Gabarito: B
  → Região de Foz do Iguaçu / tríplice fronteira. Concreta, visual,
    próxima geograficamente (Mato Grosso → Centro-Oeste → Sul).
    Boa para introduzir "fronteira" como conceito vivo.

── TIER 3 — COMPOSTO (útil mas exige mais mediação) ──

2014_CH_026 | artefato_visual | C4 | H1 | análise
  Tema: dinâmica populacional e conurbação
  Gabarito: D
  → Geograficamente geopolítica apenas de forma indireta. Usar só se
    a aula expandir para urbanização como fenômeno de ordem mundial.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEMAS MAIS FREQUENTES — REFERÊNCIA PARA AULAS 2 E 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GEOGRAFIA (56q): geografia urbana e periferização dominam (11q).
  Geopolítica aparece 10x (termos geopolítica + geopolitica somados).
  
HISTÓRIA (101q): Brasil colônia/império forte. Arte e cultura ~6q.
  Mundo contemporâneo distribuído — sem tema dominante único.

SOCIOLOGIA (133q): disciplina mais representada no corpus.
  Trabalho, cultura, movimentos sociais são núcleos recorrentes.

FILOSOFIA (58q): 79% texto_analitico — disciplina mais hostil
  ao perfil cognitivo da turma. Abordagem via personagem
  (Sócrates, sofistas, Iluminismo como evento) é o único caminho
  consistente com os dados do diagnóstico.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LIMITAÇÕES DO CORPUS — NÃO IGNORAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Classificação automática (Gemini). Tema e ancoragem são probabilísticos.
   Habilidade (H1–H30) é não-confiável — o modelo defaultou H1 em ~60%
   dos casos. Usar tema e ancoragem; ignorar habilidade para decisões finas.

2. Normalização de temas incompleta. "geografia física" e "geografia fisica"
   aparecem como temas distintos. O corpus_mestre.csv reflete isso.
   Para análises quantitativas de tema, somar variantes manualmente.

3. C6 pós-2016 suspeito. Ver caveat no heatmap acima.

4. 2020/2022/2023/2024 ausentes. O corpus cobre 8 anos mas com lacuna
   de 4 anos recentes. Questões de 2025 estão presentes (45 questões).

5. 5 questões com enunciado ausente + 2 sem classificação = 7/355 (2%).
   Aceitável para uso pedagógico.
