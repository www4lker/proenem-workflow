# Provas e gabaritos do INEP

Os PDFs não são versionados (`pipeline/.gitignore`): ficam em `pipeline/<ano>/` na máquina de quem roda o
pipeline. `MANIFESTO.csv` diz o que o corpus usa e de onde vem; `pipeline/scripts/baixar_provas.py` baixa e confere.

| Coluna | Significado |
|---|---|
| `ano`, `dia`, `caderno`, `cor`, `tipo` | Caderno regular azul: **caderno 1 no dia 1, caderno 7 no dia 2** (a numeração do dia 2 recomeça em 5; o azul é o 7). `tipo` = prova ou gabarito |
| `url_oficial` | Link copiado da página de cada ano em gov.br/inep (Provas e Gabaritos). Não há padrão único: até 2019 os arquivos ficam em `educacao_basica/enem/provas/<ano>/` e `.../gabaritos/<ano>/`, com nomes da época; a partir de 2025, em `enem/provas_e_gabaritos/` |
| `status_url` | `a verificar` · `conferida AAAA-MM-DD` (baixada do INEP nessa data) · `inválida: <nota>` |
| `nome_esperado` | Nome do arquivo em `pipeline/<ano>/`; é o mesmo do link oficial |
| `sha256` | Do arquivo oficial baixado. `baixar_provas.py` recusa arquivo com sha diferente |
| `usado_por` | Dia 1 = corpus atual (CH); dia 2 = piloto CN de 2017+ (ainda não usado) |

**Estado (06/10/2026, sessão local):** as 32 linhas (2013–2019 e 2025, dias 1 e 2, prova e gabarito) foram
baixadas do INEP e têm sha256 registrado. Os PDFs do dia 1 que já estavam na máquina do autor, de onde saiu o
corpus, são idênticos byte a byte aos oficiais, exceto a prova de 2025: o INEP republicou o arquivo em 09/07/2026
(muda a data de modificação do PDF); o texto extraído é idêntico, então o corpus não muda.

O servidor do INEP não envia o certificado intermediário da cadeia TLS; `fontes/inep-ca-intermediaria.pem`
(RNP ICPEdu GR46 OV TLS CA 2025, válido até 2030, obtido da GlobalSign) é somado às autoridades do sistema
pelo script. A verificação de certificado continua ligada.

```bash
cd pipeline
python scripts/baixar_provas.py                      # baixa o que falta e confere o sha256 de tudo
python scripts/baixar_provas.py --so-conferir        # só confere os arquivos locais
python scripts/baixar_provas.py --anos 2019 --dias 2 # um recorte
```

Uso dos materiais do INEP: provas e gabaritos são documentos públicos; o repositório guarda só o texto extraído
e recortes para uso didático interno do cursinho. Uma nota formal de licença está pendente
(`docs/PLANO_PRODUTO_PROENEM.md`, §5).
