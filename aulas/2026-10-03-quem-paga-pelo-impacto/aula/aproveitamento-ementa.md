# Aproveitamento: da aula "data centers" para a aula "Geografia e Natureza"

Branch `ementa-geo-natureza`, aberto em 02/10/2026. O trabalho até 30/09 está intacto no `master` e na
tag `v3-data-centers` (plano v3, complementar v3 e deck, todos com visto).

## 1. A nova orientação (triangulada)

**Ementa recebida:** Questões e impactos ambientais; Sustentabilidade; Resíduos sólidos; Ecologia.
Data centers: no máximo 20% da aula (~10 de 50 min).

**O cronograma do ProEnem** (`fontes/CRONOGRAMA - APOSTILA GEOGRAFIA PROENEM.md`) confirma e acrescenta:
- Aula de **3 de outubro**, "Geografia e Natureza", Professor A e Professora B. Item 12 da ementa do curso.
- Incidência no ENEM, segundo o próprio cronograma: sustentabilidade e resíduos sólidos 2× em 2025;
  questões ambientais (impactos) 3× em 2024 e 1× em 2023.
- **Regras dos slides:** temas diretos; sem textões; imagens para interpretação visual; citar autores da
  área; gráficos, charges ou mapas; **terminar com pelo menos 4 questões de ENEMs recentes, 10 minutos,
  resolvidas com a turma**; enfatizar o Estuda.com.

**As 10 aulas anteriores** (`fontes/aulas-texto/`): 14 a 58 slides, 1.000 a 2.400 palavras no total, ou
seja, ~30 a 50 palavras por slide, muito apoio visual. O que já foi dado e não deve ser repetido:
- efeito estufa e mudanças climáticas: Climatologia (10 e 6 menções);
- impactos nos domínios, desmatamento, queimadas: Domínios (13 menções a "impacto");
- impactos sobre água e solo, agrotóxicos: Água e Solo.

**Lacunas que a nossa aula preenche:** resíduos sólidos (aterro, chorume, reciclagem: **zero** menções
nas 10 aulas); acordos e conferências (Quioto, Paris, COP: uma menção só); ecologia (ecossistema: 3).

**Orçamento de tempo proposto (50 min):** ~30 min para os quatro eixos da ementa · ~10 min para data
centers como estudo de caso que amarra os quatro · ~10 min para as 4 questões finais.

## 2. O que se salva

### 2.1 Infraestrutura: salva inteira
| O quê | Onde |
|---|---|
| Estilo LaTeX (compila em pdfLaTeX e LuaLaTeX, TeXstudio e Kile) | `aula/02-LaTeX/estilo/` |
| Esqueleto do plano: identificação, justificativa, objetivos, habilidades, metodologia, roteiro, avaliação, referências ABNT | `plano-de-aula.tex` (a forma; o conteúdo se refaz) |
| Esqueleto do complementar: questões em grupos, gabarito, folha de redação de 30 linhas | `material-complementar.tex` (idem) |
| Tema do deck: fontes embutidas, logo, rodapé "Pro Enem • Geografia", classes `.questao`, `.lado`, `.grupos`, `.numero` | `aula/03-slides/theme.css`, `assets/fonts/`, `assets/img/logo-pro-enem.png` |
| Pipeline do deck: build, lint, shots, impresso em PDF | `ferramentas/decks-impress` |
| Recorte de questões e conferência com o INEP | `fontes/provas-recortes/`, `fontes/conferir_candidatas_inep.py`, `fontes/filtrar_corpus_proenem.py` |
| Método de fonte: ranks, `checagem.md`, "cortar em vez de verificar" | `CLAUDE.md`, `fontes/checagem.md` |

### 2.2 Conteúdo: serve à nova ementa
**Bloco data centers (~10 min), condensado de 24 passos para ~4 ou 5:**

| Passo atual | Eixo da ementa | Uso na nova aula |
|---|---|---|
| `provocacao` (garrafa d'água, Steibel) | impactos | abertura do bloco: o consumo depende do lugar |
| `epigrafe` (Crawford: pedras, lítio, petróleo) | impactos, resíduos | a nuvem é material: extração na entrada |
| `cinco-camadas` (nota do lixo eletrônico) | resíduos sólidos | **a ponte natural**: chips com vida útil curta viram lixo eletrônico |
| `matriz` + `limpa-x-emissoes` (88,2%; desmatamento) | sustentabilidade | "limpa em relação a quê?", fundidos num passo |
| `caso-ancora` (Eldorado do Sul: R$ 3 bi, 68 dias, 8 em 10) | impactos, risco | o caso, em um passo, sem a atividade de mapa antes |

**Fora do bloco data centers, mas reaproveitável:**
- `quem-esta-no-mapa` → justiça ambiental: quem recebe o impacto (serve aos quatro eixos).
- `processar-pra-que` → proposta de intervenção em 5 elementos: fecho de redação, com tema ambiental.
- Ficha de lugar e climogramas de Cuiabá (`fontes/ficha-lugar/`, INMET): impacto e água no lugar da turma.
- Checagem: os 4 números conferidos continuam válidos.

**Questões já recortadas e conferidas que servem à ementa (10 de 25):**

| Questão | Tema | Eixo |
|---|---|---|
| ENEM 2016/18 (reserva atual) | Quioto, créditos de carbono | sustentabilidade |
| ENEM 2014/3 | Mar de Aral, salinização | impactos |
| ENEM 2015/1 | desertificação | impactos |
| ENEM 2016/30 | Cerrado, fronteira agrícola | impactos, ecologia |
| ENEM 2015/32 | veredas, recarga no Cerrado | ecologia |
| ENEM 2016/36 | escassez de água potável | sustentabilidade |
| ENEM 2014/34 | geração de energia e alteração do ecossistema | impactos, ecologia |
| ENEM 2013/43 (Q1 atual) | eólica, renováveis | sustentabilidade |
| ENEM 2013/37 (Q4 atual) | hidrelétricas na Amazônia Legal | impactos |
| ENEM 2014/38 | gestão participativa da água | sustentabilidade |

**Atenção:** todas são de 2013 a 2016. O cronograma pede "ENEMs recentes", e nenhuma das 25 trata de
**resíduos sólidos**. As do corpus PROENEM de 2017 em diante não servem (são de Linguagens).

### 2.3 Sai da nova aula (fica no `master`)
- Parte cartográfica do planejador: `objeto`, `fatores-locacionais`, `camada`, `atividade-mapa`,
  `atividade-local`, mapas da EPE e de Victer (`fontes/epe-rs/`, `assets/mapa/`).
- Questões Q2 (call centers), Q3 (Nova Cartografia Social); `guerra-dos-lugares`; a virada em dois
  andares e o layout de 27 passos.
- Proposta de redação "Desafios da expansão dos data centers no território brasileiro" e as 20
  questões do complementar ligadas a energia, redes e meio técnico.

**Conta grossa:** do deck, ~7 de 24 passos aproveitáveis (~30%), quase todos encolhendo; do plano e do
complementar, a forma inteira e ~20% do conteúdo; das questões, 10 de 25; da infraestrutura, 100%.

## 3. O que falta e não temos
- **Resíduos sólidos:** fonte de base (Política Nacional de Resíduos Sólidos, Lei 12.305/2010; lixão ×
  aterro; reciclagem e catadores) e uma questão ENEM.
- **Ecologia:** conceitos básicos (ecossistema, biodiversidade, cadeia) só aparecem de passagem.
- **Sustentabilidade:** linha do tempo dos acordos (Estocolmo 1972, Rio-92, Quioto, Paris, Agenda 2030).
- **Questões recentes (2023–2025)** sobre os quatro eixos: exigem as provas do INEP.
