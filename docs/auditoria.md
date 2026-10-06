# Política de auditoria

Decidida em 06/10/2026. Responde a uma pergunta: **quem confere o quê**, dado que o trabalho é feito em
grande parte por agentes (o Fable na nuvem, a sessão local) e que o autor não lê código.

O princípio: cada tipo de erro tem um auditor que consegue de fato pegá-lo. IA conferindo IA serve para erros
mecânicos e de cópia; não serve para erros de interpretação, porque os dois tendem a errar do mesmo jeito.

## As quatro classes de erro

| Classe | Exemplos | Quem audita | Como |
|---|---|---|---|
| **Mecânica** | Script quebra, LaTeX não compila, link interno quebrado, deck com erro | CI (GitHub Actions) e testes | Automático em cada PR; vermelho bloqueia o merge |
| **Fidelidade à fonte** | Número copiado errado, PDF trocado, gabarito divergente, matriz transcrita errada | Agente, **com prova anexada** | sha256 do arquivo-fonte, script que reproduz a conferência, diff contra a origem. Sem prova, não vale como conferido |
| **Interpretação** | Competência ou habilidade atribuída, tema, recorte da aula, leitura de uma questão | **Professor**, por amostra | Amostra cega: o professor classifica sem ver a resposta da máquina; mede-se a concordância |
| **Uso e direitos** | Imagem de terceiro, nome de colega, logo, publicação | Colegas e PROENEM | Consentimento e permissão registrados em `CREDITOS.md` e `docs/higienizacao.md` |

## Profundidade da revisão dos PRs do Fable

Complementa a opção A (ver `docs/FILA.md`): o risco do PR define o quanto a sessão local confere.

| O PR… | Revisão local |
|---|---|
| Só mexe em código ou documentação, CI verde | Leve: ler o diff e o log, rodar os testes, merge |
| Toca fontes, números, corpus ou matriz | Completa: refazer a conferência com os arquivos originais (sha256, script), antes do merge |
| Fecha uma decisão do professor | Perguntar antes; não fazer o merge sozinho |

## O papel do autor

O autor não revisa código. Revisa **resultados** e as seções **"não testado"** dos logs: é ali que o agente diz
o que não conseguiu provar. O tempo dele vai para a classe de interpretação (as amostras cegas) e para as
decisões D1–D5.

## Amostras cegas

Ferramenta: `pipeline/scripts/amostra_cega.py` (`sortear` e `comparar`). Cada amostra fica em
`docs/auditoria/amostra-<área>-<nº>/` com `LEIAME.md`, a ficha e, depois, o resultado.

- **Tamanho e estratos:** 20 questões, estratificadas pela competência que o Gemini atribuiu (mínimo de 2 por
  competência), semente fixa. Com 20 questões, a medida tem margem larga (um acerto a mais ou a menos muda 5
  pontos): serve para detectar um problema grosso, não para certificar o corpus.
- **Leitura do resultado (recomendação técnica, não padrão estabelecido):** concordância de competência de 80%
  ou mais = a classificação automática serve para as análises; entre 60% e 80% = usar com ressalva e olhar a
  matriz de confusão; abaixo de 60% = refazer a classificação antes de usá-la em material de aula.
- A primeira amostra de CH: `docs/auditoria/amostra-ch-01/`.

### Problema conhecido antes da primeira amostra

O prompt de CH (`pipeline/prompts/classificar_questao.txt`) e `pipeline/config/areas.yaml` usam **rótulos de
competência que não são os da Matriz de Referência oficial** (por exemplo, "Autonomia/projeto de vida" como C3,
quando a C3 oficial trata de instituições sociais, políticas e econômicas), e listam as habilidades só como
"H1 a H30", sem defini-las. A coluna de competência e habilidade do corpus de CH foi, portanto, gerada contra
definições que não são as do INEP. A matriz oficial está transcrita em `pipeline/fontes/matriz-ch-inep-2026.json`
e é a que a ficha usa. A amostra mede o tamanho do problema; a correção do prompt e a reclassificação são decisão
do professor (custo do Gemini).

## Quando o ciclo com o Fable vira manutenção

1. Classes mecânica e de fidelidade automatizadas ou com prova anexada. **Feito em 06/10/2026** (CI; manifesto
   com sha256; conferência das candidatas por script).
2. Concordância da classificação medida e registrada (amostra CH nº 1; depois, CN, se houver piloto).
3. D1–D5 respondidas e F12–F17 executadas.
4. Teste de transmissão (D5) feito com um colega.
5. Permissões de uso resolvidas (colegas e imagens).

Depois do item 3, o Fable deixa de ter fila de construção: passa a receber só manutenção e tarefas pontuais.
