// Utilidades compartilhadas: argumentos, leitura do layout.json, resolução de molduras (fit)
// e checagens estáticas (sem navegador).
import fs from 'node:fs';
import path from 'node:path';

export const ROOT = path.resolve(import.meta.dirname, '..');

export function parseArgs(argv = process.argv) {
  const opts = {};
  const pos = [];
  for (const a of argv.slice(2)) {
    if (a.startsWith('--')) {
      const [k, ...v] = a.slice(2).split('=');
      opts[k] = v.length ? v.join('=') : true;
    } else pos.push(a);
  }
  return { opts, pos };
}

export const deckPath = (pos) => path.resolve(pos[0] || process.env.DECK || 'decks/demo');

export const DEFAULT_META = {
  title: 'Apresentação',
  stepW: 1920,
  stepH: 1080,
  minFontPx: 28, // texto de corpo
  minFontSourcePx: 22, // .fonte (créditos, referências)
  marginPx: 48, // margem interna mínima para texto
  gridPx: 100,
  minGapPx: 80, // folga mínima entre passos no mundo
  transitionMs: 1000,
  scales: [1, 2, 4, 8],
  maxRotate: 15,
};

// Retângulo (AABB) de um passo no espaço-mundo. Passo de escala s ocupa stepW*s × stepH*s.
export function rectOf(s, meta) {
  const w = meta.stepW * s.scale;
  const h = meta.stepH * s.scale;
  const a = ((s.rotate || 0) * Math.PI) / 180;
  const c = Math.abs(Math.cos(a));
  const sn = Math.abs(Math.sin(a));
  const bw = w * c + h * sn;
  const bh = w * sn + h * c;
  return { x0: s.x - bw / 2, y0: s.y - bh / 2, x1: s.x + bw / 2, y1: s.y + bh / 2 };
}

export function loadLayout(dir, { mapa = false } = {}) {
  if (!fs.existsSync(path.join(dir, 'layout.json'))) {
    throw new Error(`${dir} ainda não tem layout.json. Fluxo: argumento.md aprovado → layout.json → content/.`);
  }
  const raw = JSON.parse(fs.readFileSync(path.join(dir, 'layout.json'), 'utf8'));
  const meta = { ...DEFAULT_META, ...(raw.meta || {}) };
  const steps = (raw.steps || []).map((s) => ({ x: 0, y: 0, z: 0, scale: 1, rotate: 0, ...s }));
  if (mapa && steps.length) {
    steps.push({ id: '__mapa', fit: '*', pad: 300, x: 0, y: 0, z: 0, scale: 1, rotate: 0, why: 'mapa de depuração' });
  }
  const byId = new Map(steps.map((s) => [s.id, s]));
  const frames = steps.filter((s) => s.fit);
  for (const f of frames) {
    f.frame = true;
    f.rotate = 0;
  }
  const done = new Set();
  while (done.size < frames.length) {
    let progress = false;
    for (const f of frames) {
      if (done.has(f.id)) continue;
      const ids = f.fit === '*' ? steps.filter((s) => !s.fit).map((s) => s.id) : f.fit;
      if (!Array.isArray(ids) || ids.length === 0) throw new Error(`moldura "${f.id}": fit vazio ou inválido`);
      const kids = ids.map((id) => byId.get(id));
      const missing = ids.filter((_, i) => !kids[i]);
      if (missing.length) throw new Error(`moldura "${f.id}": fit referencia id inexistente: ${missing.join(', ')}`);
      if (kids.some((k) => k.fit && !done.has(k.id))) continue;
      const rs = kids.map((k) => rectOf(k, meta));
      const pad = f.pad ?? 200;
      const x0 = Math.min(...rs.map((r) => r.x0)) - pad;
      const x1 = Math.max(...rs.map((r) => r.x1)) + pad;
      const y0 = Math.min(...rs.map((r) => r.y0)) - pad;
      const y1 = Math.max(...rs.map((r) => r.y1)) + pad;
      f.scale = Math.ceil(Math.max((x1 - x0) / meta.stepW, (y1 - y0) / meta.stepH) * 100) / 100;
      f.x = Math.round((x0 + x1) / 2);
      f.y = Math.round((y0 + y1) / 2);
      f.contains = ids;
      // Câmera fixa (decks 3D): a moldura ainda acende todos os passos, mas a posição, a escala e os giros vêm do layout.
      if (f.camera) Object.assign(f, f.camera);
      done.add(f.id);
      progress = true;
    }
    if (!progress) throw new Error('fit circular entre molduras');
  }
  return { meta, steps, dir };
}

export function contentFile(dir, s) {
  return path.join(dir, 'content', `${s.file || s.id}.html`);
}

// Checagens que não precisam de navegador. Retorna [{level:'erro'|'aviso', id, rule, msg}].
export function staticChecks({ meta, steps, dir }) {
  const issues = [];
  const add = (level, id, rule, msg) => issues.push({ level, id, rule, msg });
  const seen = new Set();
  for (const s of steps) {
    if (!/^(__mapa|[a-z0-9][a-z0-9-]*)$/.test(s.id)) add('erro', s.id, 'id-invalido', 'use kebab-case minúsculo (a-z, 0-9, -)');
    if (seen.has(s.id)) add('erro', s.id, 'id-duplicado', 'id repetido');
    seen.add(s.id);
  }
  const body = steps.filter((s) => !s.frame);
  const ids = new Set(steps.map((s) => s.id));
  for (const s of body) {
    if (s.sobre && !ids.has(s.sobre)) add('erro', s.id, 'sobre-inexistente', `"sobre": "${s.sobre}" não existe`);
    const f = contentFile(dir, s);
    let html = '';
    if (!fs.existsSync(f)) add('erro', s.id, 'conteudo-ausente', `falta ${path.relative(dir, f)}`);
    else html = fs.readFileSync(f, 'utf8');
    if (!s.why) add('aviso', s.id, 'sem-why', 'passo sem "why" (justificativa espacial) no layout.json');
    // Passos de decks 3D (rotateX/rotateY) ficam em coordenadas do sólido, não na grade do plano.
    if (!s.sobre && !s.rotateX && !s.rotateY && (s.x % meta.gridPx || s.y % meta.gridPx)) add('aviso', s.id, 'fora-da-grade', `x=${s.x}, y=${s.y} não são múltiplos de ${meta.gridPx}`);
    if (!meta.scales.includes(s.scale)) add('aviso', s.id, 'escala-fora-da-escala', `scale=${s.scale}; use ${meta.scales.join(', ')}`);
    if (Math.abs(s.rotate) > meta.maxRotate) add('aviso', s.id, 'rotacao-alta', `rotate=${s.rotate} (máx ±${meta.maxRotate})`);
    const hasVideo = /<video\b/i.test(html);
    if (s.rotate && hasVideo) add('erro', s.id, 'rotacao-com-video', 'passo com vídeo não deve ser rotacionado');
    if (s.media && !/<(video|audio)\b/i.test(html)) add('aviso', s.id, 'media-sem-elemento', '"media" definido mas não há <video>/<audio> no conteúdo');
    for (const m of html.matchAll(/\b(?:src|poster|href)="([^"]+)"/g)) {
      const u = m[1];
      if (/^(https?:)?\/\//i.test(u)) add('aviso', s.id, 'depende-de-rede', `${u} não funciona offline`);
      else if (u.startsWith('assets/')) {
        const p = path.join(dir, decodeURI(u.split(/[?#]/)[0]));
        if (!fs.existsSync(p)) add('erro', s.id, 'asset-ausente', u);
        else if (fs.statSync(p).size > 2 * 1024 * 1024 && !/\.(mp4|webm|mov|m4v)$/i.test(p)) add('aviso', s.id, 'asset-pesado', `${u} (${(fs.statSync(p).size / 1048576).toFixed(1)} MB)`);
      }
    }
  }
  for (let i = 0; i < body.length; i++) {
    for (let j = i + 1; j < body.length; j++) {
      // Mergulho: passo de detalhe declarado "sobre" o pai pode ficar dentro dele.
      const [p, q] = [body[i].sobre, body[j].sobre];
      if (p === body[j].id || q === body[i].id || (p && p === q)) continue;
      // Passos girados em X ou Y (decks 3D): a caixa no plano não diz se eles se tocam.
      if (body[i].rotateX || body[i].rotateY || body[j].rotateX || body[j].rotateY) continue;
      const a = rectOf(body[i], meta);
      const b = rectOf(body[j], meta);
      const g = meta.minGapPx;
      if (a.x0 < b.x1 + g && b.x0 < a.x1 + g && a.y0 < b.y1 + g && b.y0 < a.y1 + g) {
        add('erro', body[i].id, 'sobreposicao', `colide com "${body[j].id}" (folga < ${g}px)`);
      }
    }
  }
  return issues;
}

export function printIssues(issues, steps) {
  const order = new Map(steps.map((s, i) => [s.id, i]));
  issues.sort((a, b) => (order.get(a.id) ?? 999) - (order.get(b.id) ?? 999));
  for (const i of issues) {
    console.log(`${i.level === 'erro' ? 'ERRO ' : 'AVISO'}  ${i.id.padEnd(22)} ${i.rule.padEnd(22)} ${i.msg}`);
  }
  const e = issues.filter((i) => i.level === 'erro').length;
  const w = issues.length - e;
  console.log(`\n${e} erro(s), ${w} aviso(s)`);
  return e;
}
