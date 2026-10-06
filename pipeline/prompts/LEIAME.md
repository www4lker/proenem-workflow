# Prompts de classificação (Pass 2), um por área

| Arquivo | Área | Estado |
|---|---|---|
| `classificar_questao.txt` | CH | Em uso desde 05/2026 (350 questões classificadas; ver `docs/historico/pipeline-logs/logs/2026-05-16.md`) |
| `classificar_questao_CN.txt` | CN | **Esqueleto, não executável:** esquema de saída e definições de ancoragem adaptadas; a matriz (competências 1–8 e habilidades H1–H30) está marcada "A PREENCHER" |
| `aluno_arquetipico.txt` | CH | Persona de aluno para ensaio de aula (não é classificador) |

`config/areas.yaml` aponta o prompt de cada área (`prompt:`); CN fica `null` até a matriz ser preenchida, e
assim `montar_prompts.py --area CN` se recusa a montar um lote com o esqueleto.

## Como preencher a matriz de CN (tarefa F10, parte que falta)

1. Fonte: a **Matriz de Referência do ENEM** publicada pelo INEP (documento oficial em `download.inep.gov.br`;
   a sessão na nuvem não alcança o site, então a conferência é da sessão local). Nenhuma lista de memória ou de
   site de cursinho: ver `docs/protocolo-de-fontes.md`.
2. Transcrever as 8 competências de área de Ciências da Natureza e suas Tecnologias com rótulos curtos (como
   as 6 de CH no prompt atual) e as 30 habilidades, nos dois blocos "A PREENCHER".
3. Registrar no cabeçalho do prompt a fonte e a data da conferência, e preencher `competencias:` de CN em
   `config/areas.yaml` (os mesmos rótulos, para as análises).
4. Trocar `prompt: null` por `prompts/classificar_questao_CN.txt` em `areas.yaml`.
5. Só então rodar um piloto (um ano; custo autorizado pelo professor) e medir quantas questões saem com
   `tem_imagem_obrigatoria = true`: é o dado que decide se vale uma variante com visão.

O campo `tem_imagem_obrigatoria` e a ancoragem `fenomeno_experimento` são recomendações técnicas (do
`docs/HANDOFF-construcao.md` e do `docs/PLANO_PRODUTO_PROENEM.md`), não decisões do grupo: podem mudar.
