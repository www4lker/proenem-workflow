# Plano de Produto — PROENEM Comunidade Docente

Data: 2026-07-01

## Diagnóstico

O projeto já tem um núcleo pedagógico forte: transforma corpus ENEM, diagnóstico
de turma e curadoria docente em kits de aula. Hoje, porém, ainda funciona mais
como laboratório técnico-pedagógico do Walker do que como produto comunitário.

Para virar produto entregável ao PROENEM, a mudança central é sair de
scripts, CSVs e handoffs para um fluxo que qualquer professor consiga usar:

> escolher área, tema e perfil da turma; receber questões ENEM curadas,
> roteiro de aula, material de projeção/impressão e protocolo de feedback.

## Promessa do Produto

Em até 15 minutos, um professor do PROENEM deve conseguir gerar ou adaptar um
kit de aula ENEM para sua área, sem precisar conhecer o pipeline técnico.

Saída mínima esperada:

- roteiro do professor;
- questões selecionadas;
- gabarito comentado;
- versão do aluno;
- imagens ou slides essenciais;
- plano B para aula sem internet/projetor;
- protocolo breve de feedback pós-aula.

## Estado Atual

- Corpus de Ciências Humanas com 355 questões extraídas.
- 348 questões classificadas com disciplina, tema, ancoragem, competência,
  habilidade e tipo cognitivo.
- Diagnóstico pedagógico das turmas do PROENEM 2026 documentado.
- Um fluxo de curadoria aplicado a aulas reais, especialmente Geografia.
- Kits e assets já produzidos para a aula de 04/07.
- Scripts de extração, classificação e análise ainda orientados a uso técnico.

## Lacunas Para Produto Entregável

### 1. Interface de uso docente

O professor não deve precisar abrir CSV, editar script ou entender Gemini.
Precisa de um fluxo simples:

1. escolher área;
2. escolher tema;
3. escolher perfil da turma;
4. selecionar duração da aula;
5. receber kit pronto.

MVP aceitável: Streamlit local, página HTML simples, notebook guiado ou CLI
com perguntas. O importante é reduzir atrito para professor não técnico.

### 2. Generalização pedagógica por área

O princípio atual funciona bem para Geografia:

> evento concreto -> tensão narrativa -> conceito

Para virar produto multiárea, criar templates equivalentes:

- História: personagem/evento -> conflito/processo -> conceito histórico.
- Sociologia: situação cotidiana -> conflito social -> categoria analítica.
- Filosofia: dilema/personagem -> problema -> conceito.
- Linguagens: gênero/situação comunicativa -> recurso expressivo -> interpretação.
- Matemática: situação-problema -> procedimento -> abstração.
- Natureza: fenômeno/experimento -> modelo -> conceito.

### 3. Qualidade e auditoria do corpus

O corpus atual é bom para protótipo, mas produto precisa sinalizar confiança.
Adicionar campos ou relatório de revisão:

- `ok_para_uso_em_sala`;
- `precisa_revisao_humana`;
- `tem_imagem_obrigatoria`;
- `classificacao_confiavel`;
- `conteudo_revisado_por_professor`;
- `observacao_pedagogica`.

Questões com enunciado ausente, classificação falha ou ruído textual não devem
entrar automaticamente em kits finais.

### 4. Padronização dos kits

Todo kit gerado deve seguir o mesmo contrato:

- objetivo da aula;
- perfil presumido da turma;
- questão-âncora;
- sequência minuto a minuto;
- vocabulário crítico;
- armadilhas prováveis das alternativas;
- gabarito comentado;
- material do estudante;
- material do professor;
- feedback pós-aula.

### 5. Documentação comunitária

Criar documentação mínima para professores e colaboradores:

- `README.md`: o que é, para quem é, como usar.
- `requirements.txt` ou `pyproject.toml`: instalação técnica.
- `CONTRIBUTING.md`: como sugerir temas, corrigir questões e revisar kits.
- `LICENSE`: licença do código e nota sobre uso de materiais oficiais do ENEM.
- Guia de privacidade: como tratar diagnósticos de turma e dados de alunos.

### 6. Validação com professores reais

Antes de chamar de produto, testar com pelo menos 3 professores que não
participaram da construção:

- um de Humanas;
- um de Linguagens;
- um de Matemática ou Natureza.

Critério de sucesso: o professor consegue gerar ou adaptar uma aula útil sem
mediação técnica do Walker.

## Roadmap Now / Next / Later

### Now

- Definir o produto como Gerador de Kit de Aula ENEM para professores do PROENEM.
- Criar README de uso docente.
- Padronizar o template de kit.
- Marcar qualidade das questões do corpus de Ciências Humanas.
- Montar MVP inicial apenas para Ciências Humanas.

### Next

- Criar interface simples de seleção de área, tema, turma e duração.
- Separar versão do professor e versão do estudante.
- Criar exportação Markdown/PDF.
- Registrar feedback pós-aula de modo reaproveitável.
- Validar o fluxo com professores de Humanas.

### Later

- Expandir para Linguagens, Matemática e Natureza.
- Criar banco comunitário de kits revisados.
- Permitir diagnóstico por turma.
- Gerar trilhas por dificuldade e perfil cognitivo.
- Criar governança de revisão por professores do PROENEM.

## Definição de Entregável

O projeto será produto comunitário quando um professor do PROENEM conseguir,
sem conhecer o pipeline técnico, produzir um kit de aula revisável e utilizável
em sala a partir de tema, área e perfil da turma.

O marco de entrega não é ter mais classificações. É tornar a inteligência
pedagógica já existente compartilhável, confiável e operável.
