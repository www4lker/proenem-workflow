# Provas e gabaritos do INEP

Os PDFs não são versionados (`pipeline/.gitignore`): ficam em `pipeline/<ano>/` na máquina de quem roda o
pipeline. `MANIFESTO.csv` diz o que o corpus usa e de onde vem; `pipeline/scripts/baixar_provas.py` baixa e confere.

| Coluna | Significado |
|---|---|
| `ano`, `dia`, `caderno`, `cor`, `tipo` | Caderno regular azul (caderno 1); `tipo` = prova ou gabarito |
| `url_oficial` | URL padronizada do INEP (`download.inep.gov.br/enem/provas_e_gabaritos/<ano>_PV|GB_impresso_D<dia>_CD1.pdf`) |
| `status_url` | `a verificar` (ninguém conferiu ainda) · `conferida AAAA-MM-DD` · `inválida: <nota>` |
| `nome_esperado` | Nome que os scripts procuram em `pipeline/<ano>/` (os de 2013 e os gabaritos antigos vêm de downloads anteriores, com nomes da época) |
| `sha256` | Do arquivo baixado; vazio até a primeira conferência. Com ele, `baixar_provas.py` recusa arquivo diferente |
| `usado_por` | Dia 1 = corpus atual (CH); dia 2 = piloto CN de 2017+ (ainda não usado) |

**Estado (06/10/2026):** a sessão na nuvem não alcança o site do INEP, então nenhuma URL foi conferida e nenhum
sha256 foi registrado. Tarefa para a sessão **local**, que tem os PDFs:

```bash
cd pipeline
python scripts/baixar_provas.py --so-conferir        # compara os arquivos locais com o manifesto e preenche sha256
python scripts/baixar_provas.py --anos 2019          # baixa o que falta de um ano (e confere o sha, se houver)
```

Uso dos materiais do INEP: provas e gabaritos são documentos públicos; o repositório guarda só o texto extraído
e recortes para uso didático interno do cursinho. Uma nota formal de licença está pendente
(`docs/PLANO_PRODUTO_PROENEM.md`, §5).
