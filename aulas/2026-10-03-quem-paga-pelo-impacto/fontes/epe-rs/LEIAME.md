# Capturas do WebMap EPE: Eldorado do Sul (RS)

**Origem:** WebMap EPE ("Sistema de Informações Geográficas do Setor Energético Brasileiro", epe.gov.br),
capturado pelo professor em **30/09/2026**, entre 10h27 e 10h39. Dado de rank 2: para virar número em slide,
entra em `fontes/checagem.md` (#25–#30) com o visto do professor. Atribuição no slide: "EPE, WebMap EPE
(captura em 30/09/2026)". O mapa-base é da Esri; o `.jpg` traz a atribuição no canto.

**Não editar os originais.** Recortes e cortes para o deck são cópias derivadas
(por exemplo em `aula/03-slides/assets/mapa/`).

## O que as capturas cobrem, e o que não cobrem

- Cobrem **uma camada só**: "Linhas de Transmissão – Base Existente" (com subestações), sobre o mapa-base
  (rodovias, hidrografia, relevo sombreado, limites municipais, bairros).
- **Não aparecem** camada de geração (fontes), fibra óptica, unidades de conservação, terras indígenas
  nem quilombos, e **nenhuma captura mostra a legenda ou o painel de camadas**. A atividade de
  sobreposição de camadas (`atividade-mapa`) ainda depende de capturas dessas camadas (ver "Falta capturar").
- **Nenhuma imagem marca um data center.** A afirmação "o polo fica no entroncamento das rodovias 401 e 290"
  vem do professor (a partir de reportagens) e está em `checagem.md` #30, ainda sem fonte anexada.
- Coordenadas no canto inferior esquerdo (`-51,279 -30,019 Graus`) são a **posição do cursor**, não do
  objeto; não usar como localização.

## Catálogo

Ordem de leitura de "perto da cidade" para "perto do local apontado". Há duas sequências: a do
município (10h27) e a do entroncamento (10h38).

| Arquivo | Escala (barra) | O que mostra |
|---|---|---|
| `Captura de tela_2026-09-30_10-27-08.png` | 0,4 km | Área urbana de Eldorado do Sul. Popup: **LT 230 kV Cidade Industrial – Guaíba 2, C1**, entrada em operação 2012, agente CEEE GT, 230 kV, 38,23 km. SE Eldorado do Sul ao sul; BR-116 e "290" (rótulo) a leste |
| `Captura de tela_2026-09-30_10-27-50.png` | 0,4 km | A mesma vista, sem popup. Legível: a LT 230 kV Eldorado do Sul – Porto Alegre 9, C1, o distrito Industrial (o rótulo "Dell" é do mapa-base, **não** é dado da EPE) e a margem do Guaíba |
| `Captura de tela_2026-09-30_10-28-23.png` | 6 km | Visão regional: Charqueadas, Eldorado do Sul, Guaíba, Porto Alegre, Canoas, Nova Santa Rita. Linhas **verdes** e **vermelhas** (a cor não aparece em legenda: pelos popups, verde = 230 kV e vermelha = 525 kV). Subestações rotuladas (Guaíba 3, Nova Santa Rita, Polo Petroquímico, Eldorado do Sul etc.) |
| `rCaptura de tela_2026-09-30_10-38-05.png` | 2 km | **Entroncamento das rodovias "401" (norte–sul) e "290" (leste–oeste)** e a SE Guaíba 3 logo ao norte. Muitas lagoas pequenas, limites municipais tracejados (rótulos "Charqueadas" e "Eldorado do Sul" ao norte) e loteamentos (Parque Eldorado) a oeste. Feixes de LT de 525 kV e de 230 kV convergem para a SE. O "r" no início do nome é da captura, não tem função |
| `Captura de tela_2026-09-30_10-38-20.png` | 2 km | Mesma vista. Popup: **LT 230 kV Guaíba 2 – Guaíba 3, C2 (CD)**, 2022, Chimarrão Transmissora de Energia S.A., 230 kV, 17,55 km |
| `Captura de tela_2026-09-30_10-38-39.png` | 2 km | Popup: **LT 230 kV Camaquã 3 – Nova Santa Rita, C1**, 2014, TSBE (Transmissora Sul Brasileira de Energia), 230 kV, 122,81 km |
| `Captura de tela_2026-09-30_10-38-54.png` | 2 km | Popup: **LT 525 kV Guaíba 3 – Povo Novo, C1**, 2023, CGT Eletrosul, 525 kV, 236,84 km |
| `Captura de tela_2026-09-30_10-39-27.png` | 0,2 km | Zoom máximo no entroncamento 401 × 290 (trevo). Quatro linhas de 525 kV e duas de 230 kV cruzam a BR-290 entre ~0,5 e ~1,6 km do trevo (estimativa pela barra de escala, 95 px = 0,2 km), cada uma com o nome no traçado. É a imagem mais limpa: sem popup nem SE |
| `_ags_4d64e448-bcdb-11f1-9ef1-00155dc8467c.jpg` | sem barra | 670 × 500 px. Eldorado do Sul e Porto Alegre com a LT 230 kV Cidade Industrial – Guaíba 2 e as SEs de Eldorado do Sul, Porto Alegre 4/9/21 e Canoas 1. **Origem confirmada pelo professor (30/09/2026):** o WebMap da EPE (mapa online ArcGIS no site oficial); o prefixo `_ags_` é de ArcGIS Server, com atribuição Esri/HERE/Garmin/USGS/NGA. Sem legenda, sem data da impressão, sem escala |

## Como usar na aula

1. **Zoom de escala (o impress.js faz de graça):** regional (6 km, captura 10h28) → entroncamento (2 km, 10h38)
   → detalhe (0,2 km, 10h39). Os alunos já viram escala e `E = d/D` na Cartografia; aqui a escala vira
   hierarquia visual.
2. **Leitura do mapa da EPE como o planejador lê** (bloco `onde-cabe`): o entroncamento reúne duas rodovias
   e feixes de transmissão de 525 e 230 kV a cerca de 0,5 a 1,6 km (10h39, estimativa pela barra de escala; conferir com a
   ferramenta de medir do WebMap). Isso é "energia + transmissão + acesso", três dos fatores locacionais.
3. **Virada** (`quem-esta-no-mapa`, `caso-ancora`): o que o mapa da EPE não mostra (água, gente, o Guaíba
   que transbordou em 2024) é o que a virada pergunta. Nada disso está nas capturas: vem de outras fontes
   (#22 e mapa de inundação, ainda a buscar).
4. **Popups** (2012, 2014, 2022, 2023; agentes; km): boa leitura de tabela para a turma, mas cada número segue
   "a verificar" em `checagem.md` até o professor dar o visto.

## Cuidados

- O texto das imagens é pequeno; para slide, recortar e ampliar sem redesenhar. Se for redesenhar (por
  exemplo, esconder rótulos de município), dizer no crédito "adaptado de".
- Não reter rótulos como "Dell" ou nomes de bairros num recorte que afirme algo sobre eles.
- Em texto de slide, "TI" = **terra indígena**, por extenso.
- A designação "401" é a que o mapa mostra no escudo da rodovia; **confirmar** se é BR ou RS antes de escrever.
- O entroncamento fica perto do limite entre Eldorado do Sul e Charqueadas (rótulos ao norte da SE Guaíba 3).
  Em qual município está o local, **não dá para ler nas capturas**: conferir no IBGE antes de dizer "Eldorado do Sul".
- Distância ao núcleo urbano de Eldorado do Sul: da ordem de 20 km em linha reta pela captura de 6 km
  (estimativa). No caso âncora, "Eldorado do Sul" é o município, não a cidade que aparece nas fotos das
  enchentes de 2024.

## Falta capturar (pedido ao professor)

- **Painel de camadas e legenda** do WebMap (para dizer o que são verde, vermelho, tracejado, cor-de-rosa etc.).
- As camadas da atividade: **geração**, **fibra**, **unidades de conservação**, **terras indígenas**, **quilombos**,
  na mesma vista regional (6 km) da captura de 10h28. Sem elas a atividade fica só com transmissão.
- Se existir, camada de **mancha de inundação** ou de risco (outra fonte, não é da EPE; datar).
- ~~Onde veio o arquivo `_ags_….jpg`~~: WebMap da EPE (resposta do professor, 30/09/2026).

**Decisão do professor (30/09/2026):** não recapturar camadas. A atividade usa os mapas que Victer já
mostrou (S2 pp. 2, 9 e 11) numa análise abrangente, nacional e regional, e estas capturas ficam para o
caso-âncora (zoom de escala em Eldorado do Sul).
