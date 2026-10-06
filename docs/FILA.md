# Fila de trabalho

**Fonte única do que está aberto neste repositório.** Os handoffs antigos (`docs/HANDOFF-construcao.md`,
`docs/HANDOFF-kit-de-aula.md`, os handoffs da aula de 03/10 e do pipeline) ficam como registro e contexto:
o que eles tinham de aberto foi trazido para cá em 06/10/2026. Quando um handoff antigo e esta fila
divergirem, vale a fila.

Como trabalhar com ela: ver "Protocolo de sessão" em `CLAUDE.md`.

**Legenda de dono:** **Fable** = sessão na nuvem · **Professor** = decisão ou ação do autor ·
**Local** = sessão na máquina do autor (tem acesso às origens, aos PDFs do INEP e ao Chromium).
**Estado:** aberta · em andamento (branch) · feita (commit) · bloqueada (por qual decisão).

---

## Decisões já tomadas

| Data | Decisão |
|---|---|
| 2026-10-06 | Repositório único `proenem-workflow`, com histórico limpo e higienizado antes do envio (§7.1 do kit). |
| 2026-10-06 | Correções do decks-impress com commit na origem (`3e17e14`); a cópia em `ferramentas/` já as inclui (§7.8 do kit). |
| 2026-10-06 | **Logo canônico: `identidade/logo/logo-pro-enem-versao-latex.png`.** A versão de slides sai de uso. |
| 2026-10-06 | O nome do autor (Walker) permanece como crédito. |
| 2026-10-06 | **Incorporação (opção A):** o agente entrega por pull request; a sessão local revisa, testa e faz o merge quando os testes passam e o PR não fecha decisão do professor. Se fechar, pergunta antes. |
| 2026-10-06 | **D6:** as linhas CH de 2017+ são marcadas como não confiáveis agora (F6), sem custo; a reextração fica para quando o professor autorizar o Gemini. |
| 2026-10-06 | **D7:** aplicar a correção mínima nº 1 (texto alternativo da abertura de Ecologia), em F5. |
| 2026-10-06 | Rodada 1 do Fable (F1–F11, PR #1) revisada localmente e incorporada em `658568a`. Registro: `docs/logs/2026-10-06-revisao.md`. |
| 2026-10-06 | **Política de auditoria** (`docs/auditoria.md`): quatro classes de erro, cada uma com seu auditor (CI; agente com prova anexada; professor por amostra cega; colegas e PROENEM). A profundidade da revisão de um PR segue o risco. Critério de quando o ciclo com o Fable vira manutenção. |

## Decisões pendentes do professor

Cada uma traz a recomendação. O Fable **não** decide por elas: pula as tarefas bloqueadas e segue.

| # | Pergunta | Opções (a primeira é a recomendada) | Bloqueia |
|---|---|---|---|
| D1 | Para quem é a primeira versão do kit? | Professores do PROENEM que usam um agente, com o autor como guia · só o autor e o agente · qualquer professor, sem terminal (outro projeto) | F13, F14 |
| D2 | Agentes | Formato aberto (`AGENTS.md` + skills) para Claude Code e Codex · só Claude Code | F15 |
| D3 | LaTeX da aula e da apostila | Um estilo base comum com uma camada por disciplina · estilos separados | F12 |
| D4 | Hospedagem das aulas | Um site do PROENEM com todas as aulas (médio prazo) · um site Netlify por aula (como hoje) | F16 |
| D5 | Teste de transmissão | Qual disciplina e qual professor adaptam o kit primeiro? | F17 |
| D8 | Competências de CH: o prompt e `areas.yaml` usam rótulos que não são os da matriz oficial (ver `docs/auditoria.md`) | Esperar o resultado da amostra CH nº 1, então corrigir o prompt e reclassificar (custo do Gemini) · corrigir o prompt já e reclassificar junto com a reextração de 2017+ · manter e anotar a ressalva | Uso das colunas de competência e habilidade |

## Tarefas do Fable

Fazer na ordem, pulando o que estiver bloqueado. Cada tarefa tem **critério de pronto**: sem ele cumprido
(ou sem registrar no log por que não foi possível verificar), a tarefa não está feita.

### Fase 1: fundação (nada bloqueado)

- **F1 · Logo canônico nos builds.** `aula-geo.sty` (as três cópias) e o deck (`content/titulo.html`) passam a usar
  `identidade/logo/logo-pro-enem-versao-latex.png`, de preferência por referência e não por cópia (se o build exigir
  cópia, que o script a faça a partir de `identidade/`). Remover as cópias soltas do logo e a versão de slides.
  Atualizar `identidade/LEIAME.md`. *Pronto:* plano, complementar e deck compilam; nenhum outro arquivo de logo no
  repositório além de `identidade/`. Estado: feita (1cb9cf5, 06/10/2026).
- **F2 · Ambiente reproduzível.** `requirements.txt` (Python 3.10+, `pymupdf`, `pandas`), `.env.example`
  (`GEMINI_API_KEY=`), `scripts/checar-ambiente.sh` (Python, módulos, `pdftotext`, TeX Live, Node ≥ 20.11, Chromium,
  `gemini`), e a seção "Instalação" no `README.md`. *Pronto:* o script roda na nuvem e diz o que falta. Estado: feita (e9c21ed, 06/10/2026).
- **F3 · Verificação automática (GitHub Actions).** Compilar a apostila, o plano e o complementar; `deck build` e
  `deck lint` da aula de 03/10; `python -m py_compile` em todos os `.py`. *Pronto:* workflow verde num PR. Estado: feita (c68d121, 06/10/2026).
- **F4 · Scripts com caminho novo.** Conferir `aulas/2026-10-03-…/fontes/conferir_candidatas_inep.py` e
  `filtrar_corpus_proenem.py` (agora apontam para `pipeline/` via `Path(__file__).resolve().parents[3]`). O que
  depender de PDF do INEP, marcar como "precisa de F9". *Pronto:* o que não depende de PDF roda. Estado: feita (676f3b1, 06/10/2026).
- **F5 · Arrumar a documentação.** Um `docs/workflow.md` ponta a ponta (diagnóstico → corpus → aula → apostila), com
  "como adicionar uma área". Corrigir referências quebradas da montagem (ex.: o handoff da aula cita `logs/` e
  `HANDOFF-kit.md`, que aqui são `docs/HANDOFF-kit-de-aula.md`; `decks-impress-patches.diff` ficou obsoleto e pode
  sair). Aplicar a correção mínima nº 1 de `aulas/2026-10-03-…/HANDOFF-minimos.md` (decisão D7) e marcá-la como
  aplicada lá. Não reescrever `docs/historico/`. *Pronto:* nenhum link interno quebrado (checar com script). Estado: feita (557a85d, 06/10/2026).
- **F6 · Marcar a qualidade do corpus.** Em `pipeline/analise/corpus_mestre.csv`: uma coluna `area_confiavel`
  (`false` nas linhas CH de 2017, 2018, 2019 e 2025, cuja faixa 1–45 é Linguagens) e um campo de observação para os
  5 enunciados vazios e os 2 itens sem classificação. **Sem chamar o Gemini.** `analise_corpus.py` passa a ignorar as
  não confiáveis por padrão. *Pronto:* contagens antes e depois no log. Estado: feita (93ab9a0, 06/10/2026).

### Fase 2: generalizar o pipeline

- **F7 · Área como parâmetro.** `pipeline/config/areas.yaml` (dia e faixa de questões por ano e área: CH, CN, LC, MT;
  ver a tabela em `docs/HANDOFF-construcao.md` e `pipeline/HANDOFF_corpus_2017_linguagens.md`). `extrair_prova.py`,
  `processar_recorte.py` e `analise_corpus.py` leem dela. Corrige no código o erro de 2017+. *Pronto:* testes de
  unidade da escolha de faixa por ano e área. Estado: feita (6dba23b, 06/10/2026).
- **F8 · Montagem do prompt em script.** `pipeline/scripts/montar_prompts.py`, reconstruído a partir de
  `docs/historico/pipeline-logs/logs/2026-05-16.md`. *Pronto:* reproduz a coluna `prompt_completo` de
  `batch_completo_raw.csv` numa amostra. Estado: feita (9295ad8, 06/10/2026).
- **F9 · Manifesto das provas.** `pipeline/fontes/MANIFESTO.csv` (ano, dia, caderno, cor, URL oficial do INEP, nome
  esperado, sha256) e `pipeline/scripts/baixar_provas.py`. Se a nuvem não tiver acesso ao site do INEP, deixar as URLs
  com status "a verificar" e a tarefa de baixar para **Local**. *Pronto:* manifesto cobre os anos do corpus atual.
  Estado: feita (nuvem f13b22d; local 5ed249d, 06/10/2026). As URLs presumidas estavam erradas (dia 2 é o caderno 7); 32 arquivos conferidos com sha256 e faixas de área conferidas nos cadernos.
- **F10 · Prompt e matriz de Ciências da Natureza.** `pipeline/prompts/` por área; matriz de CN (C1–C8, H1–H30) só com
  fonte oficial conferida (ver `docs/protocolo-de-fontes.md`). Sem executar o Gemini. Estado: feita (nuvem 66b37cf; local, matriz oficial INEP 2026, 06/10/2026). Executar exige autorização de custo.

### Fase 3: kit de aula (depende das decisões)

- **F11 · Modelo vazio de aula.** `aulas/_modelo/` com as pastas da aula de 03/10 e um `LEIAME.md` que explica a
  cadeia (fontes e checagem → argumento → plano → roteiro → slides → complementar → página). Estado: feita (6fbda81, 06/10/2026).
- **F12 · Identidade única.** Um pacote LaTeX base e um `theme.css` derivados da mesma paleta e do logo canônico,
  consumidos por aula, apostila e slides. Estado: bloqueada (D3).
- **F13 · Método.** `docs/metodo/` a partir do §2 de `docs/HANDOFF-kit-de-aula.md` e do histórico: etapas, vistos,
  onde houve retrabalho. Estado: bloqueada (D1).
- **F14 · Exportador corpus → apostila.** Uma questão curada de `corpus_mestre.csv` vira ambiente `questao`/`resolucao`
  de `estilo-proenem.sty`. Estado: bloqueada (D1).
- **F15 · Portas de entrada para agentes.** `AGENTS.md` e skills. Estado: bloqueada (D2).
- **F16 · Publicação das aulas.** Estado: bloqueada (D4).
- **F17 · Teste de transmissão.** Estado: bloqueada (D5).

## Ações do professor (fora do alcance do Fable)

- Pedir consentimento aos colegas pseudonimizados (para restaurar nomes) e permissões das imagens listadas em
  `CREDITOS.md`.
- Se possível, obter o logo em vetor (SVG ou PDF) com o PROENEM.
- Se quiser o piloto de CN ou a reextração de 2017+: autorizar o custo e cadastrar a chave do Gemini como segredo do
  ambiente da nuvem (nunca em arquivo).
- Responder D1–D5 e D8.
- **Preencher a amostra cega CH nº 1** (`docs/auditoria/amostra-ch-01/ficha.md`; instruções no `LEIAME.md` da
  pasta). A comparação é tarefa **Local**, depois do preenchimento.

## Fora do escopo do Fable

- Chamar o Gemini ou qualquer API paga.
- Repor material de terceiros removido ou tentar reidentificar colegas.
- Generalizar o prisma, as cores ou os eixos da aula de 03/10 antes de existir uma segunda disciplina.
- Reescrever `docs/historico/`, reescrever histórico do git ou fazer force push.
