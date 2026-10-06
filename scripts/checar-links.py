#!/usr/bin/env python3
"""Checa referências internas dos arquivos Markdown do repositório.

Acusa (1) links [texto](caminho) relativos cujo alvo não existe e (2) caminhos em crase que começam por uma
pasta da raiz (docs/, pipeline/, aulas/, apostila/, ferramentas/, identidade/, scripts/, .github/) e não existem.
Ignora docs/historico/ (registro, não instrução), pastas geradas e links externos.
Uso: python3 scripts/checar-links.py [raiz]   (sai com 1 se houver referência quebrada)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
IGNORAR = {".git", "node_modules", "dist", "build", "publicar", ".venv", "shots"}
PASTAS_RAIZ = ("docs/", "pipeline/", "aulas/", "apostila/", "ferramentas/", "identidade/", "scripts/", ".github/")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)(?:#[^)]*)?\)")
CRASE = re.compile(r"`([^`\n]+)`")


def quebrados_em(md):
    texto = md.read_text(encoding="utf-8", errors="replace")
    achados = []
    for m in LINK.finditer(texto):
        alvo = m.group(1)
        if re.match(r"^[a-z]+:", alvo):
            continue
        if not (md.parent / alvo).exists():
            achados.append(f"link ({alvo})")
    if md.name.startswith(("FILA", "HANDOFF")) or md.parts[-2].startswith("2026-07-04"):
        return achados  # fila e handoffs citam arquivos planejados; a aula de 04/07 é registro da origem
    for linha in texto.splitlines():
        if re.search(r"\btarefa\b", linha, re.I):
            continue  # "tarefa F7: `pipeline/config/areas.yaml`" é um arquivo planejado
        for m in CRASE.finditer(linha):
            alvo = m.group(1).strip()
            if not alvo.startswith(PASTAS_RAIZ) or not re.match(r"^[\w.\-/]+$", alvo) or "AAAA" in alvo:
                continue
            if not (RAIZ / alvo).exists() and not (md.parent / alvo).exists():
                achados.append(f"crase `{alvo}`")
    return achados


def main():
    total = 0
    for md in sorted(RAIZ.rglob("*.md")):
        rel = md.relative_to(RAIZ)
        if IGNORAR & set(rel.parts) or rel.parts[:2] == ("docs", "historico"):
            continue
        for a in quebrados_em(md):
            print(f"{rel}: {a}")
            total += 1
    print(f"{total} referência(s) quebrada(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
