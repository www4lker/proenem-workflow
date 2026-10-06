#!/usr/bin/env bash
# Diz o que está instalado e o que falta para trabalhar neste repositório.
# Uso: bash scripts/checar-ambiente.sh      (sai com 1 se faltar algo obrigatório)
# Não instala nada e não chama nenhuma API.
set -u

falta=0
ok()    { printf '  ok      %s\n' "$1"; }
falha() { printf '  FALTA   %s\n' "$1"; falta=1; }
aviso() { printf '  opcional %s\n' "$1"; }

ver_cmd() {  # ver_cmd <comando> <descrição> [obrigatório=1]
  if command -v "$1" > /dev/null 2>&1; then ok "$2 ($(command -v "$1"))"
  elif [[ "${3:-1}" == 1 ]]; then falha "$2"
  else aviso "$2: não encontrado"
  fi
}

echo "Python (pipeline do corpus)"
if command -v python3 > /dev/null 2>&1; then
  v=$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')
  if python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then ok "python3 $v"
  else falha "python3 $v (precisa de 3.10+)"; fi
  for mod in fitz pandas PIL; do
    if python3 -c "import $mod" > /dev/null 2>&1; then ok "módulo $mod"
    else falha "módulo $mod (pip install -r requirements.txt)"; fi
  done
else
  falha "python3"
fi

echo "PDF"
ver_cmd pdftotext "pdftotext (poppler-utils)"

echo "LaTeX (apostila: pdflatex; aula: lualatex)"
ver_cmd latexmk "latexmk"
ver_cmd pdflatex "pdflatex"
ver_cmd lualatex "lualatex"
if command -v kpsewhich > /dev/null 2>&1; then
  for pkg in tcolorbox.sty titlesec.sty microtype.sty tgpagella.sty babel.sty; do
    if kpsewhich "$pkg" > /dev/null 2>&1; then ok "pacote $pkg"; else falha "pacote $pkg (texlive-latex-extra, texlive-fonts-recommended, tex-gyre)"; fi
  done
  if command -v fc-list > /dev/null 2>&1 && fc-list 2>/dev/null | grep -qi 'texgyrepagella-regular.otf'; then ok "fonte TeX Gyre Pagella (OpenType, para lualatex)"
  else falha "fonte TeX Gyre Pagella em OpenType (fonts-texgyre); sem ela o lualatex da aula para"; fi
else
  falha "kpsewhich (TeX Live)"
fi

echo "Slides (ferramentas/decks-impress)"
if command -v node > /dev/null 2>&1; then
  nv=$(node -p 'process.versions.node')
  if node -e 'const [a,b]=process.versions.node.split(".").map(Number); process.exit(a>20||(a==20&&b>=11)?0:1)'; then ok "node $nv"
  else falha "node $nv (precisa de 20.11+)"; fi
else
  falha "node (20.11+)"
fi
ver_cmd npm "npm"
if [[ -d ferramentas/decks-impress/node_modules/playwright ]]; then ok "dependências do decks-impress (node_modules)"
else falha "dependências do decks-impress: cd ferramentas/decks-impress && npm ci"; fi
chromium=""
for c in "${CHROMIUM_PATH:-}" chromium chromium-browser google-chrome google-chrome-stable; do
  [[ -n "$c" ]] && command -v "$c" > /dev/null 2>&1 && { chromium="$c"; break; }
done
if [[ -z "$chromium" && -n "${PLAYWRIGHT_BROWSERS_PATH:-}" ]]; then
  c=$(ls -d "$PLAYWRIGHT_BROWSERS_PATH"/chromium* 2>/dev/null | head -1)
  [[ -n "$c" ]] && chromium="$c"
fi
if [[ -n "$chromium" ]]; then ok "Chromium ($chromium) para lint, capturas e PDF do deck"
else aviso "Chromium: deck build funciona; lint no navegador, shots e impresso não. Defina CHROMIUM_PATH ou use o Chromium do Playwright."; fi

echo "Classificação (Gemini, opcional e pago)"
ver_cmd gemini "gemini CLI" 0
if [[ -n "${GEMINI_API_KEY:-}" ]]; then ok "GEMINI_API_KEY definida no ambiente"
elif [[ -f .env ]] && grep -q '^GEMINI_API_KEY=.\+' .env; then ok "GEMINI_API_KEY em .env"
else aviso "GEMINI_API_KEY ausente (só precisa para classificar; ver .env.example)"; fi

echo
if (( falta )); then echo "Falta algo obrigatório (ver acima). Instalação: seção 'Instalação' do README.md."; exit 1
else echo "Ambiente completo."; fi
