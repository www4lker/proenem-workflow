#!/usr/bin/env bash
# Gera projeto-overleaf-proenem.zip a partir da pasta latex/ para upload/atualização no Overleaf.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LATEX_DIR="$SCRIPT_DIR/latex"
ZIP_PATH="$SCRIPT_DIR/projeto-overleaf-proenem.zip"

if [ ! -d "$LATEX_DIR" ]; then
  echo "Pasta não encontrada: $LATEX_DIR" >&2
  exit 1
fi

rm -f "$ZIP_PATH"
cd "$LATEX_DIR"
zip -rq "$ZIP_PATH" . \
  -x '*.aux' '*.log' '*.out' '*.bbl' '*.bcf' '*.blg' '*.fls' \
  -x '*.fdb_latexmk' '*.synctex.gz' '*.toc' '*.run.xml' '.DS_Store' 'main.pdf'

echo "ZIP atualizado: $ZIP_PATH"
