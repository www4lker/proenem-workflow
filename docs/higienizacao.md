# Higienização (2026-10-06)

Este repositório foi montado do zero, com histórico novo, a partir de quatro projetos de origem. Nada
foi apagado nas origens: elas continuam com o autor. Abaixo, o que entrou, o que saiu e por quê.

## Origem → destino

| Origem | Destino | Como entrou |
|---|---|---|
| `proenem-enem` (repositório privado) | `pipeline/`, `diagnostico-turmas/`, `aulas/2026-07-04-trabalho-e-tecnologia/`, `docs/` | Arquivos com commit (`git archive HEAD`) |
| `proenem-apostilas` (repositório privado) | `apostila/`, `docs/historico/apostila-logs/` | Arquivos com commit |
| `aula-geo-natureza` (repositório local) | `aulas/2026-10-03-quem-paga-pelo-impacto/`, `docs/HANDOFF-kit-de-aula.md` | Arquivos com commit |
| `decks-impress` (repositório local) | `ferramentas/decks-impress/` | Árvore de trabalho, incluindo correções ainda sem commit na origem |
| Logo (pasta isolada) | `identidade/logo/` | Cópia |

A lista item a item do que ficou de fora está em [`_excluidos.tsv`](_excluidos.tsv).

## Regras aplicadas

1. **Colegas pseudonimizados.** Em cada aula, os professores aparecem como "Professor A",
   "Professora B" etc., ou por função ("o professor de História"). A chave de correspondência **não**
   está no repositório.
2. **Sem autoavaliação ou leitura interpessoal.** Saíram trechos de diagnóstico sobre o próprio
   professor, a transcrição da reunião da apostila e o handoff com leituras sobre colegas.
3. **Material de terceiros sem permissão registrada:** imagens trocadas por aviso do mesmo tamanho
   (para os builds não quebrarem); textos de aulas de colegas e a transcrição de webinar ficaram fora.
   Detalhes em `CREDITOS.md`.
4. **Acervo pessoal do autor** (pesquisa acadêmica, cadernos do NotebookLM): referências trocadas
   por "[acervo pessoal do autor]"; o conteúdo não entrou.
5. **Caminhos de máquina** (`/dados/…`, `/media/…`, pendrive) trocados por caminhos relativos.
6. **Artefatos gerados** (ZIPs, PDF compilado da apostila, `node_modules`, `build/`) fora; são
   regeneráveis.
7. **Segredos:** nenhum `.env` nem `settings.local.json`; varredura por chaves `AIza…` sem ocorrências.

## O que permanece de propósito

- O nome do autor (Walker) em documentos de projeto e no histórico, como crédito.
- Nomes de autores, cartunistas e palestrantes **citados como fonte** (crédito, não exposição).
- Diagnóstico das turmas: apenas percentuais agregados; nenhum aluno é identificável.

## Decisões em aberto

- Restaurar nomes reais de colegas que consentirem.
- Obter permissões das imagens removidas ou substituí-las.
- Definir o logo canônico.
