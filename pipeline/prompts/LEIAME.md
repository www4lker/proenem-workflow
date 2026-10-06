# Prompts de classificação (Pass 2), um por área

| Arquivo | Área | Estado |
|---|---|---|
| `classificar_questao.txt` | CH | Em uso desde 05/2026 (350 questões classificadas; ver `docs/historico/pipeline-logs/logs/2026-05-16.md`) |
| `classificar_questao_CN.txt` | CN | **Pronto, nunca executado.** Matriz oficial (competências 1–8, H1–H30) transcrita da edição INEP de 2026 em 06/10/2026; fonte e sha256 no cabeçalho. Rodar exige autorização de custo |
| `aluno_arquetipico.txt` | CH | Persona de aluno para ensaio de aula (não é classificador) |

`config/areas.yaml` aponta o prompt de cada área (`prompt:`); áreas com `null` (LC, MT) fazem
`montar_prompts.py` recusar o lote.

## Matriz de CN (tarefa F10, feita em 06/10/2026)

- Fonte: INEP, *Matrizes de Referência* (publicada on-line em abril de 2026), link da página "Outros documentos"
  do Enem em gov.br/inep. URL e sha256 no cabeçalho do prompt. Comparada à edição de 2012
  (`download.inep.gov.br/download/enem/matriz_referencia.pdf`): mesmas 8 competências e 30 habilidades; as
  diferenças são só de revisão (vírgulas, "e/ou" → "e(ou)", crase em H30). Vale a de 2026.
- Transcrição feita por script (texto extraído do PDF e comparado entre as duas edições, item a item), com
  correção de duas hifenizações de quebra de linha. Os rótulos curtos de `areas.yaml` são do agente, para as
  análises; o texto integral está no prompt.
- Teste sem custo: `extrair_prova.py --area CN` na prova de 2019 (dia 2, caderno 7) numa cópia do pipeline
  extraiu 44 de 45 (Q126 sem alternativas em texto) e `montar_prompts.py --area CN` montou 43 prompts (Q94 sem
  enunciado). Nada foi enviado ao Gemini.
- Próximo passo (custo autorizado pelo professor): piloto de um ano e medir quantas questões saem com
  `tem_imagem_obrigatoria = true`. A extração de 2019 já mostra a perda: fórmulas, sobrescritos e tabelas
  chegam truncados (ex.: o símbolo E° vira "E").

O campo `tem_imagem_obrigatoria` e a ancoragem `fenomeno_experimento` são recomendações técnicas (do
`docs/HANDOFF-construcao.md` e do `docs/PLANO_PRODUTO_PROENEM.md`), não decisões do grupo: podem mudar.
