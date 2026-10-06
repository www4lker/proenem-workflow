// Uso: node tools/lint.mjs [decks/<nome>] [--json]
// Checagens estáticas (layout.json/arquivos) + medições no navegador (overflow, fonte, mídia).
// Saída em texto, legível por qualquer modelo (não depende de visão). Exit 1 se houver ERRO.
import fs from 'node:fs';
import path from 'node:path';
import { parseArgs, deckPath, loadLayout, staticChecks, printIssues } from './common.mjs';
import { withPage, openDeck, goto } from './browser.mjs';

const { opts, pos } = parseArgs();
const dir = deckPath(pos);
const layout = loadLayout(dir);
const { meta, steps } = layout;
const issues = staticChecks(layout);

if (!fs.existsSync(path.join(dir, 'dist/index.html'))) {
  console.error('dist/index.html não existe. Rode o build antes: npm run build -- ' + path.relative(process.cwd(), dir));
  process.exit(2);
}

// Medição no navegador. Usa offsetLeft/Top/Width/Height (imunes a transform/escala/rotação do passo).
function measure(cfg) {
  const out = [];
  const rel = (el, step) => {
    let x = 0, y = 0, n = el;
    while (n && n !== step) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; }
    return n === step ? { x, y, w: el.offsetWidth, h: el.offsetHeight } : null;
  };
  for (const step of document.querySelectorAll('.step')) {
    if (step.classList.contains('frame')) continue;
    const id = step.id;
    const add = (level, rule, msg) => out.push({ level, id, rule, msg });
    const W = step.offsetWidth, H = step.offsetHeight;
    const inner = step.querySelector('.step-inner');
    if (inner && (inner.scrollHeight > inner.clientHeight + 2 || inner.scrollWidth > inner.clientWidth + 2)) {
      add('erro', 'overflow', `conteúdo maior que o passo (scroll ${inner.scrollWidth}x${inner.scrollHeight} > ${inner.clientWidth}x${inner.clientHeight}); corte texto ou divida o passo`);
    }
    const small = [], clipped = [], margin = [];
    let hasContent = false;
    for (const el of step.querySelectorAll('*')) {
      if (el === inner) continue;
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      const r = rel(el, step);
      if (!r || (r.w === 0 && r.h === 0)) continue;
      const label = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : '');
      if (r.x < -2 || r.y < -2 || r.x + r.w > W + 2 || r.y + r.h > H + 2) clipped.push(label);
      const hasText = [...el.childNodes].some((c) => c.nodeType === 3 && c.textContent.trim());
      if (hasText) {
        hasContent = true;
        const fs = parseFloat(cs.fontSize);
        const min = el.closest('.fonte') ? cfg.minFontSourcePx : cfg.minFontPx;
        if (fs < min) small.push(`${label} ${fs}px<${min} "${el.textContent.trim().slice(0, 28)}"`);
        if (r.x < cfg.marginPx || r.y < cfg.marginPx || r.x + r.w > W - cfg.marginPx || r.y + r.h > H - cfg.marginPx) margin.push(label);
      }
      if (el.tagName === 'IMG') {
        hasContent = true;
        const src = el.getAttribute('src') || '';
        const svg = /\.svg(\?|#|$)/i.test(src);
        if (!el.complete || (el.naturalWidth === 0 && !svg)) add('erro', 'imagem-quebrada', src);
        else if (!svg && el.naturalWidth > 2.5 * r.w) add('aviso', 'imagem-grande', `${src}: ${el.naturalWidth}px naturais para ${Math.round(r.w)}px exibidos`);
        if (!el.hasAttribute('alt')) add('aviso', 'sem-alt', src);
      }
      if (el.tagName === 'VIDEO' || el.tagName === 'AUDIO') {
        hasContent = true;
        if (el.error || el.networkState === 3) add('aviso', 'midia-nao-carrega', `${el.currentSrc || el.getAttribute('src')} (arquivo ausente ou codec não suportado neste Chromium)`);
      }
      if (['SVG', 'svg', 'CANVAS', 'IFRAME'].includes(el.tagName)) hasContent = true;
    }
    if (small.length) add('erro', 'fonte-pequena', `${small.length} elemento(s): ${small.slice(0, 3).join(' | ')}`);
    if (clipped.length) add('erro', 'elemento-fora-do-passo', `${clipped.length}: ${[...new Set(clipped)].slice(0, 4).join(', ')}`);
    if (margin.length) add('aviso', 'margem', `texto a menos de ${cfg.marginPx}px da borda: ${[...new Set(margin)].slice(0, 4).join(', ')}`);
    if (!hasContent) add('aviso', 'passo-vazio', 'sem texto, imagem ou mídia');
  }
  return out;
}

await withPage(async (page) => {
  await openDeck(page, dir);
  await page.waitForTimeout(500);
  issues.push(...(await page.evaluate(measure, meta)));
  // Mídia com autoplay: entrar no passo e conferir se o vídeo realmente toca.
  for (const s of steps.filter((x) => x.media?.autoplay)) {
    await goto(page, s.id);
    const playing = await page.evaluate((id) => [...document.querySelectorAll(`#${id} video, #${id} audio`)].some((m) => !m.paused), s.id);
    if (!playing) issues.push({ level: 'aviso', id: s.id, rule: 'autoplay-falhou', msg: 'mídia não tocou ao entrar no passo (arquivo/codec? no navegador da sala pode diferir)' });
  }
});

if (opts.json) console.log(JSON.stringify(issues, null, 2));
else {
  const nBody = steps.filter((s) => !s.frame).length;
  console.log(`${path.relative(process.cwd(), dir)} — ${steps.length} passos (${nBody} de conteúdo, ${steps.length - nBody} moldura)\n`);
  if (!issues.length) console.log('nenhum problema encontrado');
}
const errors = opts.json ? issues.filter((i) => i.level === 'erro').length : printIssues(issues, steps);
process.exit(errors ? 1 : 0);
