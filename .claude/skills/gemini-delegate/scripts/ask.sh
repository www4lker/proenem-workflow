#!/usr/bin/env bash
# ask.sh — delega um prompt de TEXTO ao Gemini CLI.
# Imprime apenas a resposta do Gemini no stdout (sem prefixo, sem wrapper).
#
#   ./ask.sh "Resuma em 3 linhas: ..."
#   echo "texto longo" | ./ask.sh --stdin "Resuma em 3 bullets"
#
# Flags: --model (default gemini-2.5-flash), --timeout (segundos, default 120),
#        --stdin (anexa o stdin ao prompt).
set -uo pipefail

MODEL="gemini-2.5-flash"
TIMEOUT=120
USE_STDIN=0
ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --model)   MODEL="${2:?--model requer valor}";   shift 2 ;;
    --timeout) TIMEOUT="${2:?--timeout requer valor}"; shift 2 ;;
    --stdin)   USE_STDIN=1; shift ;;
    *)         ARGS+=("$1"); shift ;;
  esac
done

# Carrega GEMINI_API_KEY de .env da skill, se existir (opcional: o CLI também
# autentica via OAuth/login Google — a chave é registro adicional).
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -f "$SKILL_DIR/.env" ]]; then set -a; source "$SKILL_DIR/.env"; set +a; fi

command -v gemini >/dev/null 2>&1 || {
  echo "erro: 'gemini' CLI não encontrado no PATH" >&2; exit 1; }

PROMPT="${ARGS[*]:-}"
[[ -n "$PROMPT" ]] || { echo "erro: prompt vazio" >&2; exit 1; }

ERRF="$(mktemp)"
trap 'rm -f "$ERRF"' EXIT

if [[ $USE_STDIN -eq 1 ]]; then
  OUT="$(timeout "$TIMEOUT" gemini --skip-trust -m "$MODEL" -p "$PROMPT" 2>"$ERRF")"
else
  OUT="$(timeout "$TIMEOUT" gemini --skip-trust -m "$MODEL" -p "$PROMPT" </dev/null 2>"$ERRF")"
fi
RC=$?

if [[ $RC -ne 0 ]]; then
  echo "erro: gemini falhou (exit $RC)" >&2
  tail -n 3 "$ERRF" >&2
  exit "$RC"
fi
printf '%s\n' "$OUT"
