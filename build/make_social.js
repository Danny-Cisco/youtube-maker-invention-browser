// Renders the link-preview image (assets/og-image.jpg, 1200×630) and the app icons from the built site.
// Run after build.py whenever makers are added, so the numbers on the card stay current:
//   node build/make_social.js
// Needs Playwright (preinstalled in Claude Code cloud sessions; otherwise `npm i playwright`).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..'), assets = path.join(root, 'assets');
const logo = fs.readFileSync(path.join(assets, 'logo.svg'), 'utf8');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.route(/^https?:/, r => r.abort());                       // no network needed
  await p.goto('file://' + path.join(root, 'index.html'));
  const d = await p.evaluate(() => {
    const inv = DATA.creators.flatMap(c => c.inventions.map(x => [Date.parse(x.start), Math.max(1, x.views)]));
    return { makers: DATA.creators.length, inventions: inv.length, videos: DATA.creators.reduce((a, c) => a + c.uploads.length, 0), inv };
  });

  // Background: one dot per invention, date across, views up (log), the 25 biggest in red.
  const W = 1200, H = 630, t0 = Math.min(...d.inv.map(i => i[0])), t1 = Math.max(...d.inv.map(i => i[0]));
  const lo = Math.log10(Math.min(...d.inv.map(i => i[1]))), hi = Math.log10(Math.max(...d.inv.map(i => i[1])));
  const big = new Set([...d.inv].sort((a, b) => b[1] - a[1]).slice(0, 25));
  const dots = d.inv.map(i => { const x = 40 + (i[0] - t0) / (t1 - t0) * (W - 80), y = H - 40 - (Math.log10(i[1]) - lo) / (hi - lo) * (H - 80);
    return big.has(i) ? `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="5" fill="#e62e25"/>` : `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="3" fill="#f1f0ec" fill-opacity=".22"/>`; }).join('');
  const n = v => v.toLocaleString('en');

  await p.setContent(`<!doctype html><html><head><style>
    *{margin:0;box-sizing:border-box} body{width:${W}px;height:${H}px;background:#111110;color:#f1f0ec;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow:hidden;position:relative}
    .dots{position:absolute;inset:0;-webkit-mask-image:linear-gradient(90deg,transparent 18%,#000 62%);mask-image:linear-gradient(90deg,transparent 18%,#000 62%)}
    .glow{position:absolute;left:-160px;top:-120px;width:760px;height:760px;background:radial-gradient(circle,rgba(230,46,37,.22),transparent 62%)}
    .c{position:absolute;left:84px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:0}
    .logo{width:150px;height:150px;margin:0 0 18px -18px}
    h1{font-size:86px;line-height:.98;font-weight:800;letter-spacing:-.04em} h1 em{font-style:normal;color:#ff4a3d;display:block}
    p{margin-top:24px;font-size:32px;color:#c4c2b9;letter-spacing:-.01em}
    .s{display:flex;gap:30px;margin-top:34px;font-size:25px;color:#8d8b83} .s b{color:#f1f0ec;font-weight:700}
  </style></head><body>
    <svg class="dots" width="${W}" height="${H}">${dots}</svg><div class="glow"></div>
    <div class="c">${logo.replace('<svg', '<svg class="logo"')}<h1><em>YouTuber</em>Invention Catalogue</h1>
      <p>What YouTube's makers actually built</p>
      <div class="s"><span><b>${n(d.makers)}</b> makers</span><span><b>${n(d.inventions)}</b> inventions</span><span><b>${n(d.videos)}</b> videos</span></div></div>
  </body></html>`);
  await p.screenshot({ path: path.join(assets, 'og-image.jpg'), type: 'jpeg', quality: 86 });

  // App icons: the bulb on the site's dark background (iOS home screen / iMessage), and a 32 px favicon.
  for (const [file, size, bg, pad] of [['apple-touch-icon.png', 180, '#111110', 22], ['favicon-32.png', 32, 'transparent', 0]]) {
    await p.setViewportSize({ width: size, height: size });
    await p.setContent(`<html><body style="margin:0;width:${size}px;height:${size}px;background:${bg};display:grid;place-items:center">${logo.replace('<svg', `<svg style="width:${size - 2 * pad}px;height:${size - 2 * pad}px"`)}</body></html>`);
    await p.screenshot({ path: path.join(assets, file), omitBackground: bg === 'transparent' });
  }
  console.log(`og-image.jpg: ${d.makers} makers, ${d.inventions} inventions, ${d.videos} videos; icons written`);
  await b.close();
})();
