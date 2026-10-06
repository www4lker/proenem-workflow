# Amostra cega CH nº 1

Mede se a classificação de competência e habilidade feita pelo Gemini no corpus de CH concorda com a leitura
do professor. Política e critério de leitura: `docs/auditoria.md`.

## O que fazer (professor)

1. Abrir `ficha.md` (no Obsidian ou em qualquer editor).
2. Em cada uma das 20 questões, preencher `Competência:` e `Habilidade:` com o número, pela matriz oficial que está
   no topo da ficha. `Nota:` é livre (dúvida, segunda opção, problema no enunciado).
3. Questões com mapa, gráfico ou imagem: abrir o PDF indicado na página indicada (os PDFs ficam em `pipeline/<ano>/`
   na máquina local; não são versionados).
4. Avisar a sessão local; ela roda a comparação e registra o resultado.

**Para a amostra continuar cega:** não abrir `pipeline/analise/corpus_mestre.csv` nem o `resultado.md` antes de
terminar. `ids.csv` só liga o número da ficha ao id do corpus (não mostra a classificação).

## Como foi feita

- 20 questões das 171 linhas confiáveis de CH (2013–2016) com enunciado e competência atribuída.
- Estratos pela competência do Gemini: C1 3, C2 2, C3 2, C4 4, C5 7, C6 2 (proporcional, mínimo 2). Ordem
  embaralhada. Semente `20261006`: o sorteio é reproduzível.
- O texto vem do corpus (extraído dos PDFs oficiais, conferidos por sha256); a página foi localizada no caderno.

## Comparar (sessão local)

```bash
python3 pipeline/scripts/amostra_cega.py comparar docs/auditoria/amostra-ch-01
```

Gera `resultado.md`: concordância exata, kappa de Cohen (concordância descontado o acaso) e a matriz de confusão
por competência.

## Atenção ao ler o resultado

O prompt que o Gemini usou trazia rótulos de competência diferentes dos oficiais (ver `docs/auditoria.md`).
Concordância baixa pode vir desse rótulo errado, e não de uma leitura ruim da questão; a matriz de confusão
ajuda a separar os dois casos (um deslocamento sistemático, como "Gemini C5 → professor C6", indica rótulo).
