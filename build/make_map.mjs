// Generates build/world.json (the country map). One-off; needs: npm i world-atlas@2.0.2 topojson-client@3.1.0 d3-geo@3.1.1 i18n-iso-countries@7.14.0
// Usage: node build/make_map.mjs build/world.json
// Writes build/world.json: {w, h, countries: [[alpha2, name, svgPath], ...]} in a Natural Earth projection, Antarctica dropped.
import { readFileSync, writeFileSync } from "fs";
import { feature } from "topojson-client";
import { geoNaturalEarth1, geoPath } from "d3-geo";
import countries from "i18n-iso-countries";
import { createRequire } from "module";
const require = createRequire(import.meta.url);
countries.registerLocale(require("i18n-iso-countries/langs/en.json"));
const topo = JSON.parse(readFileSync(require.resolve("world-atlas/countries-110m.json")));
const fc = feature(topo, topo.objects.countries);
fc.features = fc.features.filter(f => f.properties.name !== "Antarctica");
const W = 1000, H = 470;
const proj = geoNaturalEarth1().fitExtent([[4, 4], [W - 4, H - 4]], fc);
const path = geoPath(proj);
const round = d => d.replace(/(\d+\.\d)\d+/g, "$1");
const out = [];
for (const f of fc.features) {
  const num = String(f.id || "").padStart(3, "0");
  let a2 = countries.numericToAlpha2(num) || "";
  if (!a2 && f.properties.name === "Kosovo") a2 = "XK";
  const d = path(f); if (!d) continue;
  out.push([a2, countries.getName(a2, "en") || f.properties.name, round(d)]);
}
// small countries the 110m map leaves out get a dot instead (centroid of their real location)
const dots = { MT: [14.4, 35.9], SG: [103.8, 1.35], HK: [114.2, 22.3], LU: [6.1, 49.8], BH: [50.6, 26.0], MO: [113.55, 22.17] };
const have = new Set(out.map(o => o[0]));
const extra = Object.entries(dots).filter(([k]) => !have.has(k)).map(([k, ll]) => { const [x, y] = proj(ll); return [k, countries.getName(k, "en"), null, Math.round(x * 10) / 10, Math.round(y * 10) / 10]; });
writeFileSync(process.argv[2], JSON.stringify({ w: W, h: H, countries: out, dots: extra }));
console.log(out.length, "countries,", extra.length, "dots,", Math.round(JSON.stringify(out).length / 1024), "KB");
