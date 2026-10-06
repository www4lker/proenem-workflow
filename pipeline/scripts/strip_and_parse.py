import pandas as pd, json, re, sys

input_csv  = sys.argv[1]   # amostra_calibracao_pass2.csv
output_csv = sys.argv[2]   # amostra_calibracao_pass2_clean.csv

df = pd.read_csv(input_csv)

def strip_fence(s):
    if not isinstance(s, str):
        return s
    s = s.strip()
    s = re.sub(r'^```json\s*', '', s)
    s = re.sub(r'^```\s*',     '', s)
    s = re.sub(r'\s*```$',     '', s)
    return s.strip()

results = []
for _, row in df.iterrows():
    raw = strip_fence(row['classificacao'])
    try:
        parsed = json.loads(raw)
        results.append({'id': row['id'], 'classificacao': json.dumps(parsed, ensure_ascii=False), 'parse_ok': True})
    except Exception as e:
        raw_str = raw[:200] if isinstance(raw, str) else ''
        results.append({'id': row['id'], 'classificacao': raw_str, 'parse_ok': False, 'erro': str(e)})

out = pd.DataFrame(results)
out.to_csv(output_csv, index=False)
print(f"Total: {len(out)} | OK: {out['parse_ok'].sum()} | Erros: {(~out['parse_ok']).sum()}")
