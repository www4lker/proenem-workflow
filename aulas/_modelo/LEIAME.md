# Modelo vazio de aula

Copie esta pasta para `aulas/AAAA-MM-DD-tema/` e siga a cadeia abaixo. Cada elo produz um arquivo e **para em
revisão do professor antes do próximo**. O exemplo completo é `aulas/2026-10-03-quem-paga-pelo-impacto/`
(Geografia): quando este modelo não bastar, copie e adapte o arquivo correspondente de lá.

```
fontes e checagem ─► argumento ─► plano de aula ─► roteiro de ensaio ─► slides ─► material complementar ─► página
fontes/checagem.md   aula/03-slides/ aula/02-LaTeX/   aula/05-roteiro-   aula/      aula/02-LaTeX/            aula/04-online/
fontes/questoes-     argumento.md    plano-de-aula/   de-ensaio.md       03-slides/ material-complementar/
selecionadas.md
```

| Elo | Arquivo aqui | O que é | Como se verifica |
|---|---|---|---|
| 0. Recorte | `aula/aproveitamento-ementa.md` | Ementa recebida, o que a aula cobre e o que deixa para outras aulas | Visto do professor |
| 1. Fontes e checagem | `fontes/checagem.md` | Tabela: cada número ou afirmação que pode ir à tela, com fonte e status | Nenhum item "a verificar" chega ao aluno |
| 2. Questões | `fontes/questoes-selecionadas.md`, `fontes/provas-recortes/` | Candidatas do corpus (`pipeline/`), conferidas no caderno oficial, recortadas em PNG | Prova, ano, número e gabarito conferidos; o resto é "(autoral)" |
| 3. Argumento | `aula/03-slides/argumento.md` | Blocos e relações da aula; esqueleto comum do plano e do deck | Visto do professor antes de qualquer coordenada |
| 4. Plano de aula | `aula/02-LaTeX/plano-de-aula/` | Documento para a coordenação (LaTeX, `aula-geo.sty`) | `latexmk -r latexmkrc plano-de-aula.tex` compila com `[final]` |
| 5. Roteiro de ensaio | `aula/05-roteiro-de-ensaio.md` | Divisão entre professores, tempos, falas de apoio (uso interno) | Visto de cada professor |
| 6. Slides | `aula/03-slides/` | `layout.json`, `content/`, `theme.css`, `assets/` (decks-impress) | `deck build` e `deck lint` sem erro; impresso com `deck impresso` |
| 7. Material complementar | `aula/02-LaTeX/material-complementar/` | Documento do aluno: resumo e questões com gabarito | Compila com `[final]` |
| 8. Página on-line | `aula/04-online/` | `index.html` + `montar.sh` → `publicar/` (copiar da aula modelo e adaptar) | Abre sem rede; botão do PDF funciona |
| 9. Registro | `README.md`, `HANDOFF.md`, log em `docs/logs/` | Estado de cada elo, decisões do professor com data | Atualizado ao encerrar |

## Regras que valem para qualquer disciplina

- Hierarquia de fontes e "nenhum número a verificar na tela": `docs/protocolo-de-fontes.md`.
- Questão de vestibular só com prova e ano conferidos; o resto é marcado **(autoral)**.
- Imagem só com origem e permissão em `CREDITOS.md` (raiz). O logo vem de `identidade/`, nunca copiado.
- O professor decide olhando: cada entregável para em revisão; a voz e as teses são dele.
- O que é da aula de Geografia e **não** se copia: o prisma 3D, as cores por eixo e os quatro eixos do deck.

## O que já funciona neste modelo, sem editar nada

```bash
cd aulas/_modelo/aula/02-LaTeX/plano-de-aula && latexmk -r latexmkrc plano-de-aula.tex            # build/plano-de-aula.pdf
cd aulas/_modelo/aula/02-LaTeX/material-complementar && latexmk -r latexmkrc material-complementar.tex
cd aulas/_modelo && ../../ferramentas/decks-impress/deck build aula/03-slides && ../../ferramentas/decks-impress/deck lint aula/03-slides
```

O estilo LaTeX (`aula/02-LaTeX/estilo/aula-geo.sty`) é, por enquanto, um link para o da aula modelo; a tarefa
F12 (`docs/FILA.md`) o substitui por um pacote comum a aula, apostila e slides. Os PDFs em `build/` e o
`dist/` do deck não vão para o git.
