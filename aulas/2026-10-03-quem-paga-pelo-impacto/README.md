# Aula: data centers no Brasil, uma leitura geográfica (ENEM)

> Retomada: ver `HANDOFF.md`. Registro da sessão de 02/10/2026: `logs/2026-10-02-sessao.md`.
>
> **Branch `ementa-geo-natureza` (02/10/2026):** a aula foi refeita para a ementa Geografia e Natureza ("Quem paga pelo
> impacto?"), com data centers como estudo de caso de ~14% do tempo. A versão data centers está no `master` e na tag `v3-data-centers`.

Uma aula de ~50 min de pré-vestibular (Geografia/Natureza), construída sobre o webinar
"Data Centers e Economia Digital" (ITS Rio, aula 1 de 3) e o corpus do projeto Atlas da IA,
com uma camada de **apoio à redação** (repertório, eixos, proposta de intervenção).

## Status

| Etapa | Arquivo | Status |
|---|---|---|
| Log da sessão | `logs/2026-10-02-sessao.md` | ok (rumo da ementa; anterior: `logs/2026-09-30-sessao.md`) |
| Transcrição do webinar | `impar-aulas/Webinar - … (transcrição 2026-09-29).txt` | ok (whisper large-v3, sem revisão humana) |
| Texto das aulas existentes | `fontes/aulas-texto/` | ok (10 extrações) |
| Índice do webinar | `fontes/webinar-indice.md` | ok |
| Checagem de dados | `fontes/checagem.md` | **fechada** (30/09/2026): só o que está na tela foi conferido e tem visto; os demais itens ficam "fora da aula: não verificar" |
| Capturas do WebMap EPE (Eldorado do Sul) | `fontes/epe-rs/` | 9 capturas catalogadas em `LEIAME.md`; faltam legenda e as camadas da atividade |
| Aulas do Atlas (slides de palestrantes) | `fontes/aulas-atlas.md` | lido o texto; regras de citação; gráficos em imagem não lidos |
| Plano de leitura (geografia física) | `fontes/plano-leitura-geo-fisica.md` | executado (passadas 1–3) |
| Base de geografia física | `fontes/base-geo-fisica.md` | ok; páginas de imagem restantes listadas na seção 7 |
| Triagem de questões (PROENEM, só leitura) | `fontes/candidatas-enem-proenem.md` | triagem feita; conferência por script em `fontes/conferencia-inep-candidatas.md` (só 2013–2016 são CH de fato); falta olhar figuras e registrar em `checagem.md` |
| Seleção de 25 questões ENEM | `fontes/enem-25-selecionadas.md` | 5 marcadas para a aula, 19 para o complementar; falta olhar figuras |
| Ponte com o Atlas da IA | `fontes/ponte-atlas-ia.md` | ok |
| Plano de aula | `aula/02-LaTeX/plano-de-aula/plano-de-aula.tex` | **v4 (9 pp., `[final]`, 02/10), com visto**: "Quem paga pelo impacto?", segue o deck; 4 questões ENEM + 1 autoral com gabarito (v3 data centers no `master`) |
| Material complementar | `aula/02-LaTeX/material-complementar/material-complementar.tex` | **a refazer** para a ementa (depois da aula); o conteúdo atual é o v3 de data centers (com visto no `master`) e não deve ser distribuído deste branch |
| Roteiro de ensaio | `aula/05-roteiro-de-ensaio.md` e `aula/roteiro-de-ensaio.docx` | **v3 com visto (02/10/26)**: três professores (Professor A 40%, Professora B 40%, Professora C 20%), nomes e tempos preenchidos, insumos da Professora C (resíduos); v2 com visto |
| Slides | `aula/03-slides/` | **v3 com visto (02/10):** face de Resíduos com 6 passos (lei 12.305 conferida, 4R do DK p. 331, charge do Gilmar, mapa IBGE MUNIC 2023, logística reversa); 35 passos, impresso 30 pp., lint 0/0. Antes: deck "Quem paga pelo impacto?" com visto (02/10), também no tratamento final: prisma octogonal 3D (`prisma.py`; uma face por bloco, giro de 45° a cada eixo, título na tampa, panorâmica de cima), aberturas de eixo com ilustração DK, cor por eixo tirada de cada imagem e um só QR no fim (material complementar no Netlify). 31 passos (30 + 1 moldura); lint 0/0. Imagens DK reais |
| Material complementar on-line | `aula/04-online/` | no ar (Netlify): página única (`index.html`) com resumo, 11 questões com correção e placar, redação e referências; PDF hospedado junto, no Netlify (o Dropbox saiu); referência de *O livro da ecologia* (edição brasileira). `montar.sh` gera `publicar/` (complementar + slides navegáveis); o professor sobe `publicar.zip` no Netlify |
| Ilustrações DK | `fontes/dk-ecologia-mapa.md` | mapa das 7 imagens, reservas e filtro das 15 fotos; imagens extraídas e referência da edição brasileira (Globo Livros, 2020) aplicadas |
| Banco de questões | `aula/04-banco-questoes.md` | a fazer |
| Material do aluno | `aula/05-material-aluno.md` | a fazer |
| Apoio à redação | `aula/06-apoio-redacao.md` | a fazer |

## Pastas

- `impar-aulas/`: PDFs das aulas do Ímpar/ProEnem 2026 (fora do git, 317 MB) e a cópia da
  transcrição. O original e o áudio estão em `[acervo pessoal do autor]/`.
- `fontes/aulas-texto/`: `pdftotext -layout` de cada PDF. O texto extraível é bom; **não
  precisa de OCR**. As duas "Cartografia" têm o mesmo conteúdo (exportações diferentes).
- `fontes/`: índices, checagem e ponte com as fontes externas.
- `aula/`: os entregáveis.

## Fontes externas (só leitura)

- `[acervo pessoal do autor: NotebookLM]/` (índice `atlas_ia`: notebooks "O Atlas da IA" e
  "Milton Santos")
- `[acervo pessoal do autor, fora do repositório]/` (texto "A nuvem tem território" e agenda de
  casos brasileiros)
