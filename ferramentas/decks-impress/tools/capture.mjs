// Uso: node tools/capture.mjs [decks/<nome>] [--only=id1,id2] [--mapa] [--pdf]
//   (sem flags)  → screenshot de todos os passos, em ordem
//   --only=a,b   → só esses passos (use isto nas iterações: economiza tokens)
//   --mapa       → só o mapa espacial (usa debug.html)
//   --pdf        → todos os passos em ordem → shots/deck.pdf (cópia de segurança; perde o movimento)
//   --impresso   → dist/impresso.html → shots/impresso.pdf (A4 paisagem, texto vetorial, para o aluno)
// Saída: decks/<nome>/shots/<id>.png (1920x1080)
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { parseArgs, deckPath, loadLayout } from './common.mjs';
import { withPage, openDeck, goto } from './browser.mjs';

const { opts, pos } = parseArgs();
const dir = deckPath(pos);
const { steps } = loadLayout(dir);
const shots = path.join(dir, 'shots');
fs.mkdirSync(shots, { recursive: true });

try {
await withPage(async (page) => {
  if (opts.impresso) {
    await page.goto(pathToFileURL(path.join(dir, 'dist', 'impresso.html')).href);
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: path.join(shots, 'impresso.pdf'), preferCSSPageSize: true, printBackground: true });
    console.log('shots/impresso.pdf');
    return;
  }
  if (opts.mapa) {
    await openDeck(page, dir, 'debug.html');
    await goto(page, '__mapa');
    await page.screenshot({ path: path.join(shots, '__mapa.png') });
    console.log('shots/__mapa.png');
    return;
  }
  await openDeck(page, dir);
  let ids = steps.map((s) => s.id);
  if (opts.only) {
    const want = String(opts.only).split(',');
    const bad = want.filter((w) => !ids.includes(w));
    if (bad.length) throw new Error(`ids inexistentes: ${bad.join(', ')}`);
    ids = want;
  }
  for (const id of ids) {
    await goto(page, id);
    await page.screenshot({ path: path.join(shots, `${id}.png`) });
    console.log(`shots/${id}.png`);
  }
  if (opts.pdf) {
    const html = path.join(shots, '_deck.html');
    fs.writeFileSync(
      html,
      `<!doctype html><meta charset="utf-8"><style>@page{size:1920px 1080px;margin:0}html,body{margin:0}img{display:block;width:1920px;height:1080px;page-break-after:always}</style>` +
        steps.map((s) => `<img src="${s.id}.png">`).join(''),
    );
    await page.goto(pathToFileURL(html).href);
    await page.pdf({ path: path.join(shots, 'deck.pdf'), width: '1920px', height: '1080px', printBackground: true });
    fs.unlinkSync(html);
    console.log('shots/deck.pdf');
  }
});
} catch (e) {
  console.error('Erro:', e.message);
  process.exit(1);
}
