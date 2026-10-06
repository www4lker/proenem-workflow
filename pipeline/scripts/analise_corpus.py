import pandas as pd
import json
import re
from pathlib import Path
from collections import Counter

# ── 1. Carregar e juntar ───────────────────────────────────────────────────

raw   = pd.read_csv('corpus_enem/questoes_raw.csv')
clean = pd.read_csv('corpus_enem/batch_completo_clean.csv')

# Expandir o JSON de classificação para colunas
def parse_class(row):
    if not row['parse_ok']:
        return {}
    try:
        return json.loads(row['classificacao'])
    except Exception:
        return {}

class_expanded = clean.apply(parse_class, axis=1, result_type='expand')
# O JSON de classificação traz seu próprio campo 'id'; remover para não
# duplicar a coluna 'id' no concat (quebraria o merge a seguir).
class_expanded = class_expanded.drop(columns=['id'], errors='ignore')
clean = pd.concat([clean[['id','parse_ok']], class_expanded], axis=1)

# Join com o raw pelo id
corpus = raw.merge(clean, on='id', how='left')

# Anotar questões sem classificação válida
corpus['classificado'] = corpus['parse_ok'].fillna(False).astype(bool)

print(f"\n{'='*60}")
print(f"CORPUS MESTRE: {len(corpus)} questões totais")
print(f"  Classificadas: {corpus['classificado'].sum()}")
print(f"  Sem classificação: {(~corpus['classificado']).sum()}")


# ── 2. ANÁLISE A — Distribuição geral de ancoragens ───────────────────────

print(f"\n{'='*60}")
print("ANÁLISE A — DISTRIBUIÇÃO DE ANCORAGENS")
print(f"{'='*60}")

df = corpus[corpus['classificado']].copy()

# Global
anc_global = df['ancoragem'].value_counts()
print("\nGlobal (348 questões):")
for anc, n in anc_global.items():
    pct = n / len(df) * 100
    print(f"  {anc:20s}: {n:3d} ({pct:.1f}%)")

# Por disciplina
print("\nPor disciplina:")
for disc in ['geografia','historia','sociologia','filosofia']:
    sub = df[df['disciplina_principal']==disc]
    if sub.empty:
        continue
    ancs = sub['ancoragem'].value_counts()
    print(f"\n  {disc.upper()} ({len(sub)} questões):")
    for anc, n in ancs.items():
        pct = n / len(sub) * 100
        print(f"    {anc:20s}: {n:3d} ({pct:.1f}%)")

# Por ano
print("\nAncoragem por ano (evento_narrativo + artefato_visual = 'processável'):")
for ano in sorted(df['ano'].unique()):
    sub = df[df['ano']==ano]
    processavel = sub[sub['ancoragem'].isin(
        ['evento_narrativo','artefato_visual','composto']
    )]
    pct = len(processavel) / len(sub) * 100
    print(f"  {ano}: {len(processavel):2d}/{len(sub):2d} processáveis ({pct:.0f}%)")


# ── 3. ANÁLISE B — Heatmap competência × ano ──────────────────────────────

print(f"\n{'='*60}")
print("ANÁLISE B — HEATMAP COMPETÊNCIA × ANO")
print(f"{'='*60}")

# Normalizar competencia para int onde possível
df['comp_num'] = pd.to_numeric(df['competencia'], errors='coerce')

pivot = df.pivot_table(
    index='comp_num',
    columns='ano',
    values='id',
    aggfunc='count',
    fill_value=0
)
print("\nContagem de questões por Competência (linhas) × Ano (colunas):")
print(pivot.to_string())

# Totais por competência
print("\nTotal por competência (todos os anos):")
for comp in sorted(df['comp_num'].dropna().unique()):
    n = (df['comp_num'] == comp).sum()
    desc = {
        1: "Linguagens/espaço-tempo",
        2: "Território/diversidade cultural",
        3: "Autonomia/projeto de vida",
        4: "Produção/apropriação do espaço",
        5: "Indivíduo/sociedade/natureza",
        6: "Geopolítica/mundialização"
    }.get(int(comp), "?")
    print(f"  C{int(comp)} ({desc}): {n}")


# ── 4. ANÁLISE C — Filtro geopolítica refinado ────────────────────────────

print(f"\n{'='*60}")
print("ANÁLISE C — QUESTÕES DE GEOPOLÍTICA/ORDEM MUNDIAL")
print(f"{'='*60}")

# Termos no tema_principal apenas (não concatenar tema_secundario —
# reduz ruído de falsos positivos por "conflito" em outros contextos)
TERMOS_GEO = [
    'geopolit',           # geopolítica, geopolitica
    'ordem mundial',
    'blocos econom',      # blocos econômicos, economicos
    'organismo internac', # organismos internacionais
    'guerra fria',
    'otan', 'nato',
    'brics',
    'onu',
    'imperialismo',       # imperialismo moderno/contemporâneo
    'hegemonia',
    'multipolaridade', 'unipolar',
    'globaliz',           # globalização e geopolítica
    'fluxo migrat',       # migrações forçadas/políticas
    'fronteira',
    'soberania',
    'potência',           # potência regional/mundial
    'segurança internac',
    'protocolo de quioto','acordo de paris',
    'crise do subprime',  # como evento de ordem econômica mundial
]

def é_geopolitica(tema):
    if not isinstance(tema, str):
        return False
    t = tema.lower()
    return any(term in t for term in TERMOS_GEO)

mask_geo = df['tema_principal'].apply(é_geopolitica)
geo = df[mask_geo].copy()

print(f"\nTotal questões geopolítica/afins: {len(geo)}")
print("\nPor ancoragem:")
for anc, n in geo['ancoragem'].value_counts().items():
    print(f"  {anc}: {n}")

print("\nLista completa (ordenada por ancoragem pedagógica, depois ano):")

# Ordem pedagógica: melhor para a turma primeiro
ordem_anc = {'evento_narrativo':0,'artefato_visual':1,'composto':2,'texto_analitico':3}
geo['ord_anc'] = geo['ancoragem'].map(ordem_anc).fillna(9)
geo_sorted = geo.sort_values(['ord_anc','ano'])

for _, r in geo_sorted.iterrows():
    flag = ""
    if r['ancoragem'] == 'texto_analitico':
        flag = "  ← ENTRADA DIFÍCIL p/ turma"
    print(f"  {r['id']} | {str(r['ano'])} | {r['ancoragem']:20s} | "
          f"C{r['competencia']} | {r['tema_principal']}{flag}")

# Subconjunto recomendado (ancoragem processável pela turma)
processavel_geo = geo[geo['ancoragem'].isin(
    ['evento_narrativo','artefato_visual','composto']
)]
print(f"\n── SUBCONJUNTO RECOMENDADO PARA AULA 04/07 ──")
print(f"Questões geopolítica com ancoragem processável pela turma: "
      f"{len(processavel_geo)}")

for _, r in processavel_geo.sort_values(['ord_anc','ano']).iterrows():
    print(f"\n  {'─'*55}")
    print(f"  ID: {r['id']}  |  Ano: {r['ano']}  |  "
          f"Ancoragem: {r['ancoragem']}")
    print(f"  Tema: {r['tema_principal']}")
    print(f"  Competência: C{r['competencia']} | "
          f"Habilidade: {r['habilidade']} | "
          f"Cognitivo: {r['tipo_cognitivo']}")

    # Buscar enunciado no raw para prévia
    raw_row = raw[raw['id']==r['id']]
    if not raw_row.empty and isinstance(raw_row.iloc[0]['enunciado'], str):
        enunciado_preview = raw_row.iloc[0]['enunciado'][:300].replace('\n',' ')
        print(f"  Enunciado (300 chars): {enunciado_preview}...")
    else:
        print(f"  Enunciado: NÃO DISPONÍVEL")

    # Gabarito
    gab = raw_row.iloc[0]['gabarito'] if not raw_row.empty else '?'
    print(f"  Gabarito: {gab}")


# ── 5. ANÁLISE D — Frequência de temas CH por disciplina (top 10 cada) ────

print(f"\n{'='*60}")
print("ANÁLISE D — TEMAS MAIS FREQUENTES POR DISCIPLINA")
print(f"{'='*60}")

for disc in ['geografia','historia','sociologia','filosofia']:
    sub = df[df['disciplina_principal']==disc]
    if sub.empty:
        continue

    # Normalizar tema: lowercase, sem acento de grau, trim
    temas = sub['tema_principal'].dropna().str.lower().str.strip()

    # Nível 1 do tema (antes do primeiro '>') para agregação
    nivel1 = temas.str.split('>').str[0].str.strip()
    top10 = nivel1.value_counts().head(10)

    print(f"\n  {disc.upper()} — top 10 temas (nível 1):")
    for tema, n in top10.items():
        pct = n / len(sub) * 100
        print(f"    {n:3d} ({pct:4.1f}%)  {tema}")


# ── 6. SALVAR OUTPUTS ──────────────────────────────────────────────────────

Path('analise').mkdir(exist_ok=True)

# Corpus mestre completo
corpus.to_csv('analise/corpus_mestre.csv', index=False)

# Questões geopolítica com ancoragem processável (para a aula)
cols_export = ['id','ano','enunciado','alternativas','gabarito',
               'disciplina_principal','tema_principal','ancoragem',
               'competencia','habilidade','tipo_cognitivo']
cols_exist = [c for c in cols_export if c in processavel_geo.columns
              or c in raw.columns]

# Juntar com enunciados para exportação completa
export = processavel_geo.merge(
    raw[['id','enunciado','alternativas','gabarito']],
    on='id', how='left',
    suffixes=('_class','')
)
export_cols = ['id','ano','enunciado','alternativas','gabarito',
               'disciplina_principal','tema_principal','ancoragem',
               'competencia','habilidade','tipo_cognitivo']
export_cols = [c for c in export_cols if c in export.columns]
export[export_cols].to_csv(
    'analise/geopolitica_aula_04_07.csv', index=False
)

print(f"\n{'='*60}")
print("OUTPUTS SALVOS:")
print(f"  analise/corpus_mestre.csv — corpus completo com classificações")
print(f"  analise/geopolitica_aula_04_07.csv — questões para 04/07")
print(f"{'='*60}")
