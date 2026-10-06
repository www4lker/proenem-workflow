// Playwright compartilhado por lint.mjs e capture.mjs.
// Ordem: CHROMIUM_PATH → Chromium do Playwright → navegador Chromium do sistema (Chrome, Chromium, Edge, Brave).
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { chromium } from 'playwright';

const SYSTEM_BROWSERS = [
  '/usr/bin/chromium', '/usr/bin/chromium-browser', '/snap/bin/chromium',
  '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable',
  '/usr/bin/microsoft-edge', '/usr/bin/brave-browser',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
];

function executablePath() {
  if (process.env.CHROMIUM_PATH) return process.env.CHROMIUM_PATH;
  if (fs.existsSync(chromium.executablePath())) return undefined;
  return SYSTEM_BROWSERS.find((p) => fs.existsSync(p));
}

export async function withPage(fn) {
  const browser = await chromium.launch({
    executablePath: executablePath(),
    args: ['--autoplay-policy=no-user-gesture-required'],
  });
  try {
    const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
    return await fn(await ctx.newPage());
  } finally {
    await browser.close();
  }
}

export async function openDeck(page, dir, file = 'index.html') {
  await page.goto(pathToFileURL(path.join(dir, 'dist', file)).href);
  await page.addStyleTag({ content: '*{transition:none !important;animation:none !important}' });
  await page.waitForSelector('body.impress-enabled', { timeout: 10000 });
  await page.evaluate(() => document.fonts.ready);
}

export async function goto(page, id) {
  await page.evaluate((i) => impress().goto(i, 0), id);
  await page.waitForTimeout(600);
}
