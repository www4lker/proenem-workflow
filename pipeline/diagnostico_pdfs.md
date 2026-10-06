# Diagnóstico do corpus de PDFs ENEM

Gerado com poppler-utils (pdfinfo, pdftotext, pdffonts, pdfimages). 46 PDFs, 0 código.

## 1. Inventário
46 PDFs. Padrão: arquivos de **32 páginas** (ou 20–23 nas provas antigas) são
**provas**; arquivos de **1–2 páginas** são **gabaritos**.

| Grupo | Provas (32p) | Gabaritos (1–2p) | Ano real |
|-------|--------------|------------------|----------|
| raiz `2004..2008_amarela.pdf` | 5 (20–23p) | — | 2004–2008 |
| raiz `dia1/dia2_caderno*.pdf` + `gabarito_dia1/2.pdf` | 2 | 2 | **2009** |
| `210/` | 4 (2 normais + 2 `_com_gab`) | — | **2010** |
| `211/` | 2 (`dia1...`, `222.pdf`) | 2 | **2011** |
| `2012/` | 2 | 2 (`dia1_azul`, `dia2_amarelo`) | 2012 |
| `2014/`,`2015/`,`2016/`,`2017/`,`2018/`,`2023/` | 2 cada | 2 cada | conf. pasta |
| `a_redacao_no_enem_2025_cartilha...pdf` | cartilha 78p | — | 2025 |
| `2008provas-e-gabaritos.html` | página HTML | — | 2008 |

Tamanhos: provas 3–8 MB; `2014/*` são 13–15 MB (alta resolução). `2018/2DIA_05_
AMARELO_BAIXA.pdf` é versão "baixa" (708 KB) da prova do dia 2.

## 2. Camada de texto
Todos os PDFs testados têm **TEXTO_NATIVO** — `pdftotext` extrai texto limpo.
Nenhum `IMAGEM_PURA`, nenhum `OCR_PRESENTE`.

- `TEXTO_NATIVO`: 2004, 2014, 2023, raiz 2009, cartilha 2025 (todos amostrados).
- Ressalva de **ordem de leitura**: provas em 2 colunas (2014+, 2023) saem com as
  colunas **interleavadas** — ex.: "QUESTÃO 05" aparece antes de "QUESTÃO 03".
  Provas antigas (2004) saem em fluxo mais linear. Parser precisará reordenar por
  coordenada (`pdftotext -bbox`/`-layout`) ou processar coluna a coluna.

## 3. Fontes
- **2004**: fontes Arial/TimesNewRoman TrueType, **todas embarcadas** (`emb yes`)
  e subsetadas → PDF vetorial gerado digitalmente.
- **2023/dia1**: Arial *não* embarcada + algumas Type 1C/CID embarcadas (incl.
  fonte de código de barras `C39HrP36DlTt`) → vetorial, gerado digitalmente.
- **2018/2DIA_05**: mix TrueType/CID, embarcadas → vetorial.
- Nenhum PDF é Type 3 puro nem sem fontes → **nada é escaneado**.

## 4. Imagens por página
Imagens chegam como **figuras separadas por questão**, não como bitmap de página
inteira. Ex. `2023/dia1` p3–6: JPEGs pequenos (~370x406, 33 KB) — gráficos/charges
embutidos. `2018/2DIA_05` p3: 1 imagem 284x122. Média baixa (0–2 imagens/página).
**Gabaritos não têm imagem nenhuma** (`pdfimages -list` vazio) — são só texto/vetor.

## 5. Gabaritos — formato
Dois layouts em tabela, ambos extraíveis com `pdftotext -layout`:

- **2009 (`gabarito_dia1.pdf`)**: tabela larga `Questão | Caderno1 Azul | Caderno2
  Amarelo | Caderno3 Branco | Caderno4 Rosa`, linhas `N  LETRA` repetidas por cor.
- **2012/2017**: tabela por área de conhecimento (`CIÊNCIAS HUMANAS` |
  `CIÊNCIAS DA NATUREZA`), colunas `QUESTÃO  GABARITO`; 2017 ainda separa
  `INGLÊS / ESPANHOL` nas questões 1–5.

Parser de gabarito: simples, baseado em regex `^\s*\d{1,3}\s+[A-E]` sobre saída
`-layout`. Complexidade baixa.

## 6. Variação entre anos
| Ano | Páginas | Delimitador de questão | Colunas | Observação |
|-----|---------|------------------------|---------|------------|
| 2004 | 20–23 | `N.` (numérico) | ~linear | matriz antiga, < 2009 |
| 2014 | 32 | `QUESTÃO N` | 2 colunas | matriz nova |
| 2023 | 32 | `QUESTÃO N` | 2 colunas | matriz nova |

Confirma a mudança de formato a partir de 2009 (nova matriz): provas antigas têm
menos páginas e numeração `N.`; provas modernas têm 32p e cabeçalho `QUESTÃO N`.

## 7. Delimitadores de questão
Contagem de `grep` na saída de `pdftotext`:

- **2014, 2023** → `^QUESTÃO\s+\d+` casa **exatamente 90 vezes** (90 questões/dia).
  Delimitador **confiável** para provas da matriz nova.
- **2009** (raiz `dia1_caderno1_azul.pdf`) → cabeçalho é a palavra `Questão` numa
  linha e o número na linha seguinte; regex `^Questão$` casou só 7x (quebra de
  página atrapalha) — precisa de regex multilinha `Questão\s*\n\s*\d+`.
- **2004** → `^\d{1,2}\.$` casa 75x, mas com **falsos positivos** (datas, citações).
  Delimitador antigo **não confiável** sozinho — exige validação por contexto.

## 8. Anomalias e dúvidas
- **`210/` = ENEM 2010, `211/` = ENEM 2011** (confirmado no texto da p1). `211/
  222.pdf` é a prova do dia 2 (caderno amarelo, contém Proposta de Redação).
  `210/*_com_gab.pdf` são provas com gabarito embarcado.
- **`2023/dia1_caderno1_azul.pdf` parece mal-rotulado**: o texto interno diz
  "2013" e tem a marca d'água `*AZUL75SAB3*` (mesma de 2014/2013). Verificar se o
  conteúdo é realmente 2013 e não 2023.
- `2008provas-e-gabaritos.html` é página de listagem, não prova.
- Provas de `2014/` são bem mais pesadas (13–15 MB) que as demais — imagens em
  resolução alta; pode valer recomprimir antes de processar.

## Conclusão para o pipeline
`pdftotext` resolve a **camada estrutural** (texto e gabaritos são 100% nativos —
LLM com visão NÃO é necessário para o texto). Os dois desafios reais são:
(1) reordenar as 2 colunas das provas modernas; (2) associar as figuras JPEG
(`pdfimages`) à questão correta. Visão só seria útil para descrever o conteúdo
das figuras, não para ler o enunciado.
