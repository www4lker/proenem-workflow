// Uso: node tools/build.mjs [decks/<nome>] [--watch]
// Gera decks/<nome>/dist/index.html (apresentação) e dist/debug.html (ids, HUD, mapa).
import fs from 'node:fs';
import path from 'node:path';
import { ROOT, parseArgs, deckPath, loadLayout, contentFile, staticChecks, printIssues } from './common.mjs';

const { opts, pos } = parseArgs();
const dir = deckPath(pos);
const read = (p) => fs.readFileSync(p, 'utf8');
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');

function stepHtml(s, dir) {
  const a = [
    `id="${s.id}"`,
    `class="${['step', s.frame ? 'frame' : '', s.class || ''].filter(Boolean).join(' ')}"`,
    `data-x="${s.x}"`,
    `data-y="${s.y}"`,
    `data-z="${s.z || 0}"`, // sempre: sem ele, o plugin rel do impress herda o z do passo anterior (decks 3D)
    `data-scale="${s.scale}"`,
    s.rotate ? `data-rotate="${s.rotate}"` : '',
    s.rotateX ? `data-rotate-x="${s.rotateX}"` : '',
    s.rotateY ? `data-rotate-y="${s.rotateY}"` : '',
    s.contains ? `data-contains="${s.contains.join(',')}"` : '',
    s.transicao ? `data-transition-duration="${s.transicao}"` : '',
    s.sobre ? `data-sobre="${s.sobre}"` : '',
  ];
  if (s.media) {
    if (s.media.autoplay) a.push('data-media-autoplay="true"');
    if (s.media.autostop) a.push('data-media-autostop="true"');
    if (s.media.autopause) a.push('data-media-autopause="true"');
  }
  const f = contentFile(dir, s);
  const inner = fs.existsSync(f) ? read(f) : '';
  return `<div ${a.filter(Boolean).join(' ')}>\n<div class="step-inner">\n${inner}\n</div>\n</div>`;
}

function page({ layout, debug }) {
  const { meta, steps } = layout;
  const theme = read(path.join(ROOT, 'theme/theme.css')) + (fs.existsSync(path.join(dir, 'theme.css')) ? '\n' + read(path.join(dir, 'theme.css')) : '');
  return `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=${meta.stepW}">
<title>${esc(meta.title)}${debug ? ' [debug]' : ''}</title>
<style>${theme}</style>
${debug ? `<style>${read(path.join(ROOT, 'tools/debug.css'))}</style>` : ''}
</head>
<body class="${debug ? 'debug' : ''}">
<div id="impress" data-width="${meta.stepW}" data-height="${meta.stepH}" data-max-scale="20" data-transition-duration="${meta.transitionMs}"${meta.perspective ? ` data-perspective="${meta.perspective}"` : ''}>
${steps.map((s) => stepHtml(s, dir)).join('\n')}
</div>
<script src="vendor/impress.js"></script>
<script>${read(path.join(ROOT, 'tools/runtime.js'))}</script>
${debug ? `<script>${read(path.join(ROOT, 'tools/debug.js'))}</script>` : ''}
</body>
</html>
`;
}

// Versão para imprimir: passos de conteúdo em sequência (sem molduras, sem impress.js),
// um por folha A4 paisagem, texto vetorial. Imprime com Ctrl+P ou `deck impresso`.
function printPage({ layout }) {
  const { meta, steps } = layout;
  const theme = read(path.join(ROOT, 'theme/theme.css')) + (fs.existsSync(path.join(dir, 'theme.css')) ? '\n' + read(path.join(dir, 'theme.css')) : '');
  const body = steps.filter((s) => !s.frame && !s.sobre); // detalhe de mergulho já está no passo pai
  const folha = (s, i) => {
    const f = contentFile(dir, s);
    const inner = fs.existsSync(f) ? read(f) : '';
    return `<section class="folha"><div id="${s.id}" class="step ${s.class || ''}"><div class="step-inner">\n${inner}\n</div></div><div class="rodape">${esc(meta.title)} · ${i + 1}/${body.length}</div></section>`;
  };
  return `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>${esc(meta.title)} [impresso]</title>
<style>${theme}</style>
<style>${read(path.join(ROOT, 'tools/print.css'))}</style>
</head>
<body class="impresso">
${body.map(folha).join('\n')}
</body>
</html>
`;
}

function build() {
  try {
    const layout = loadLayout(dir);
    const issues = staticChecks(layout);
    const errors = issues.filter((i) => i.level === 'erro');
    if (errors.length) {
      console.log('Build abortado (erros estáticos):');
      printIssues(issues, layout.steps);
      return false;
    }
    const out = path.join(dir, 'dist');
    fs.mkdirSync(path.join(out, 'vendor'), { recursive: true });
    fs.copyFileSync(path.join(ROOT, 'vendor/impress.js'), path.join(out, 'vendor/impress.js'));
    if (fs.existsSync(path.join(dir, 'assets'))) fs.cpSync(path.join(dir, 'assets'), path.join(out, 'assets'), { recursive: true });
    fs.writeFileSync(path.join(out, 'index.html'), page({ layout, debug: false }));
    fs.writeFileSync(path.join(out, 'debug.html'), page({ layout: loadLayout(dir, { mapa: true }), debug: true }));
    fs.writeFileSync(path.join(out, 'impresso.html'), printPage({ layout }));
    console.log(`ok  ${path.relative(process.cwd(), out)}/index.html  (${layout.steps.length} passos; ${issues.length} aviso(s) estático(s) — rode o lint)`);
    return true;
  } catch (e) {
    console.error('Falha no build:', e.message);
    return false;
  }
}

const ok = build();
if (opts.watch) {
  let t;
  const again = (_, f) => {
    if (f && /^(dist|shots)[\\/]/.test(f)) return;
    clearTimeout(t);
    t = setTimeout(build, 150);
  };
  fs.watch(dir, { recursive: true }, again);
  fs.watch(path.join(ROOT, 'theme'), again);
  console.log('observando alterações… (Ctrl+C para sair; recarregue o navegador com F5)');
} else if (!ok) process.exit(1);
