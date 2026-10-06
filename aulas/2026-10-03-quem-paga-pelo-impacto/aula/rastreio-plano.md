# Rastreio do plano de aula (bastidor)

O `plano-de-aula.tex` é o documento final (coordenação, Professora B, arquivo) e não traz marcas internas.
Este arquivo guarda o que saiu dele em 30/09/2026 (v2 → v3): ids dos passos do deck, linhas da transcrição,
itens da checagem e cuidados de produção. A versão v2 completa está no git (commit `5dc0523`).

## Cortes de 30/09/2026 (rumo: fonte proporcional ao pré-vestibular)

Saíram do plano: 29,9% do mundo; 93% × 89,2% (e o BEN 2024); 54 MW; 32 km; 32.115/39.559; percentuais de relevo da
CORSAN; 3 km da aldeia; número da lei municipal; Konopacki inteiro (estudo de empregos, ReData, ciclo de políticas).
Na tela ficam 4 números: 88,2% (EPE 2025), R$ 3 bi e 68 dias (O Globo), 8 em 10 atingidos (Ipea). As colunas de
checagem abaixo são históricas: o que está "a verificar" nelas ficou fora da aula.

## Passos do deck × etapas do plano

| Etapa do plano | Passos (`layout.json`) | Min | Fontes internas | Checagem |
|---|---|---|---|---|
| Abertura | `titulo`, `provocacao` | 3 | Steibel L393–412 (garrafa d'água; resfriamento, prédio, localização L405–410); Observatório T2 L589–590 ("a nuvem não fica na nuvem") | — |
| O objeto | `objeto`, `cinco-camadas` | 3+1 | Victer L2018–2035 (leitura pessoal); T2 L217–242 (treinamento "não pode ser dividido"); Steibel L698–712, S1 slide 29; T2 L283–295 (vida útil dos chips) | #38 ok; #51 fora |
| Onde cabe? | `onde-cabe`, `matriz`, A1, `fatores-locacionais`, A2, `camada`, `atividade-mapa` | 4+2+2+2+2+6 | Victer L2044–2052, S2 p. 14 (lista); L1680 e L1670 (aglomeração); S2 pp. 2, 9, 11 | #6, #47 ok |
| Virada | `virada`, `quem-esta-no-mapa`, A3, `limpa-x-emissoes`, `sobra-x-diesel`, `caso-ancora` | 3+2+1+1+4 | T2 L592–624 (Dublin); L556–572 (EUA); L1305–1330 (emprego); S4 p. 9; L1201–1223 (Anacé); L814–829 (zonas de sacrifício); L484–505, L760–770, L1139–1243, L1415–1523 (Caucaia, Uberlândia); Victer S2 p. 10; T2 L1277–1282, L1283, L1390–1402 | #31, #35, #45 ok; #7, #10, #15, #42×#60, #57, #58, #61 a verificar |
| Objeto técnico e guerra dos lugares | A4, `guerra-dos-lugares` | 5+2 | T2 L463–464; L1374–1388 | #37 ok; #40, #46 a verificar |
| Fechamento | `processar-pra-que`, `fechamento` | 3+2 | Steibel L448–451; T2 L1404–1410; Victer L1930–1940, ~L1860; T2 L1575–1649 (10 medidas); S4 p. 2 (ciclo de políticas) | — |

Ficha de lugar: #62–66 ok; #22/#30 ok (lei municipal 5.949/2024 e Tekoa Pekuruty entram no caso e na ficha, v3 de 30/09); #29 (distâncias às linhas) a verificar e fora do plano.

## Cuidados de fonte que valiam no v2 (continuam valendo para os slides)

- Nenhum número com status "a verificar" ou "divergente". Divergentes tocados: #42 × #60 (empregos), #50 × #53
  (contrapartida do ReData), 4,75 GW com quatro comparações (#22, #34, #44, #55).
- "R$ 500 bi" do governador: fala condicional, parece ser a projeção do setor inteiro (#33, #41). Não usar.
- Falas de Victer, Steibel e do Observatório entram atribuídas. Transcrição automática: **no plano v3 as falas da
  transcrição estão parafraseadas**; aspas no slide só depois de ouvir o trecho.
- O "sonho" de 4.750 MW da Scala fica só na fala do professor (tirado do plano v3).
- Figuras de relevo do curso (p. 48 e 51) são "Gerada por IA": não reutilizar.
- Conflito dos PDFs (fertilidade do solo de Mares de Morros): a aula não toca em fertilidade.
- Fora da aula até haver fonte: estabilidade tectônica como fator locacional; clima quente encarecendo o resfriamento.
- Capturas do WebMap EPE: crédito "EPE, WebMap EPE (captura em 30/09/2026)"; ver `fontes/epe-rs/LEIAME.md`.
- Slides de Victer: tarjar os rótulos em GW e o número de projetos (S2 p. 11) enquanto não houver checagem.
- Escrever "terra indígena" por extenso ("TI" confunde com tecnologia da informação).

## Questões: estado interno

Recortes provisórios em `aula/03-slides/assets/questoes/`, sem gabarito na imagem; visto do professor opcional (A2 tem mapa).

## O que o v2 pedia ao deck

Está em `aula/03-slides/HANDOFF-slides.md`, seção "Da sessão da aula para os slides".
