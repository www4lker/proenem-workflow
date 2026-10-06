#!/usr/bin/env bash
# Monta a pasta estática para hospedar: material complementar + slides navegáveis em casa + PDF (o botão da página
# baixa esta cópia; sem ela o botão quebra).
# Uso: bash aula/04-online/montar.sh [--sem-pdf]
# Saída: aula/04-online/publicar/ (fora do git). Suba o conteúdo dessa pasta inteira.
set -euo pipefail

AQUI="$(cd "$(dirname "$0")" && pwd)"
RAIZ="$(cd "$AQUI/../.." && pwd)"
DECK="$RAIZ/aula/03-slides"
FW="${DECKS_IMPRESS:-$RAIZ/../../ferramentas/decks-impress}"
SAIDA="$AQUI/publicar"
PDF_NOME="slides-quem-paga-pelo-impacto.pdf"

sem_pdf=0
[[ "${1:-}" == "--sem-pdf" ]] && sem_pdf=1

# dist/ do zero: o build não apaga assets que saíram do deck (eles iriam parar no publicar/).
rm -rf "$DECK/dist"
"$FW/deck" build "$DECK"
if (( ! sem_pdf )); then
  "$FW/deck" impresso "$DECK"
fi

rm -rf "$SAIDA"
mkdir -p "$SAIDA/slides" "$SAIDA/questoes"

# Slides: só o index (sem debug.html nem impresso.html), vendor e assets.
cp "$DECK/dist/index.html" "$SAIDA/slides/index.html"
cp -r "$DECK/dist/vendor" "$DECK/dist/assets" "$SAIDA/slides/"

if [[ -f "$DECK/shots/impresso.pdf" ]]; then
  cp "$DECK/shots/impresso.pdf" "$SAIDA/$PDF_NOME"
else
  echo "erro: $DECK/shots/impresso.pdf não existe; o botão de PDF ficaria quebrado" >&2
  exit 1
fi

# Material complementar e os recortes das questões que ele usa.
cp "$AQUI/index.html" "$SAIDA/index.html"
grep -o 'questoes/[0-9]\{4\}_CH_[0-9]\{3\}\.png' "$AQUI/index.html" | sort -u | while read -r q; do
  cp "$RAIZ/fontes/provas-recortes/$(basename "$q")" "$SAIDA/$q"
done

# Navegação "de casa" injetada na cópia dos slides (o deck da sala fica como está).
python3 - "$SAIDA/slides/index.html" <<'PY'
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
s = s.replace('<meta name="viewport" content="width=1920">',
              '<meta name="viewport" content="width=device-width, initial-scale=1">', 1)
casa = r'''
<div class="impress-progressbar"><div></div></div>
<nav id="casa" aria-label="Navegação dos slides">
  <a href="../index.html">← Material</a>
  <span class="casa-meio">
    <button type="button" id="casa-ant" aria-label="Slide anterior">‹</button>
    <span id="casa-n" aria-live="polite">1 / 1</span>
    <button type="button" id="casa-prox" aria-label="Próximo slide">›</button>
  </span>
  <span class="casa-dica">setas, espaço ou deslize</span>
</nav>
<div id="casa-gire" role="note"><p>Gire o celular para ver os slides na horizontal.</p><button type="button">Continuar assim</button></div>
<style>
#casa { position: fixed; left: 0; right: 0; bottom: 0; z-index: 1000; display: flex; align-items: center;
  justify-content: space-between; gap: 12px; padding: 8px 16px; background: rgba(29,29,31,.88); color: #f6f3ec;
  font: 15px/1.2 "Inter", "Helvetica Neue", Arial, sans-serif; transition: opacity .4s; }
#casa.quieto { opacity: 0; pointer-events: none; }
#casa a { color: #f6f3ec; text-decoration: none; font-weight: 600; }
#casa .casa-meio { display: flex; align-items: center; gap: 10px; }
#casa button { font: 600 22px/1 "Inter", Arial, sans-serif; width: 44px; height: 36px; border-radius: 6px;
  border: 1px solid rgba(246,243,236,.4); background: transparent; color: #f6f3ec; cursor: pointer; }
#casa button:hover { background: rgba(246,243,236,.12); }
#casa-n { min-width: 4.5em; text-align: center; font-variant-numeric: tabular-nums; }
#casa .casa-dica { opacity: .7; font-size: 13px; }
.impress-progressbar { position: fixed; left: 0; right: 0; top: 0; height: 4px; z-index: 1000; background: rgba(246,243,236,.15); }
.impress-progressbar div { height: 100%; width: 0; background: #8a3b12; transition: width .6s; }
#casa-gire { display: none; }
@media (orientation: portrait) and (max-width: 700px) {
  #casa-gire { display: flex; position: fixed; inset: 0; z-index: 1001; flex-direction: column; align-items: center;
    justify-content: center; gap: 16px; padding: 24px; background: rgba(29,29,31,.94); color: #f6f3ec; text-align: center;
    font: 18px/1.4 "Inter", Arial, sans-serif; }
  #casa-gire button { font: 600 15px "Inter", Arial, sans-serif; padding: 10px 16px; border-radius: 6px;
    border: 1px solid #f6f3ec; background: transparent; color: #f6f3ec; }
  #casa-gire.fechado { display: none; }
  #casa .casa-dica { display: none; }
}
</style>
<script>
(function () {
  var passos = Array.prototype.slice.call(document.querySelectorAll('#impress .step'));
  var n = document.getElementById('casa-n');
  var barra = document.querySelector('.impress-progressbar div');
  function marcar(el) {
    var i = passos.indexOf(el) + 1;
    n.textContent = i + ' / ' + passos.length;
    barra.style.width = (100 * i / passos.length) + '%';
  }
  document.addEventListener('impress:stepenter', function (e) { marcar(e.target); });
  var ativo = document.querySelector('#impress .step.active');
  if (ativo) marcar(ativo);
  document.getElementById('casa-ant').addEventListener('click', function () { impress().prev(); });
  document.getElementById('casa-prox').addEventListener('click', function () { impress().next(); });
  // A barra some depois de 3 s parada (não cobre o rodapé) e volta ao mexer o mouse, tocar ou teclar.
  var nav = document.getElementById('casa'), t;
  function acordar() { nav.classList.remove('quieto'); clearTimeout(t); t = setTimeout(function () { nav.classList.add('quieto'); }, 3000); }
  ['mousemove', 'touchstart', 'keydown'].forEach(function (ev) { document.addEventListener(ev, acordar, { passive: true }); });
  nav.addEventListener('mouseenter', function () { clearTimeout(t); });
  acordar();
  var gire = document.getElementById('casa-gire');
  gire.querySelector('button').addEventListener('click', function () { gire.classList.add('fechado'); });
})();
</script>
'''
if '</body>' not in s:
    sys.exit('slides/index.html sem </body>: não injetei a navegação')
s = s.replace('</body>', casa + '</body>', 1)
open(p, 'w', encoding='utf-8').write(s)
PY

echo "Pronto: $SAIDA"
du -sh "$SAIDA"
