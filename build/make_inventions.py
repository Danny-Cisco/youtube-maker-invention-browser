"""Turn a curation spec (inventions listed by video index) into data/<name>_inventions.py with stable video IDs.

Usage: python3 build/make_inventions.py SPEC.py data/NAME_videos.json data/NAME_inventions.py

SPEC.py defines CREATOR (dict), NOTE (docstring text) and SPEC: a list of
(name, kind, [indices into the videos file, oldest first], description[, [(label, url), ...]]).
"""
import importlib.util, json, sys

spec_path, videos_path, out_path = sys.argv[1:4]
s = importlib.util.spec_from_file_location("spec", spec_path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
V = json.load(open(videos_path))["videos"]
used = [i for row in m.SPEC for i in row[2]]
dups = sorted({i for i in used if used.count(i) > 1})
if dups: sys.exit(f"videos used twice: {dups}")
names = [row[0] for row in m.SPEC]
if len(names) != len(set(names)): sys.exit("duplicate invention names")
out = ['"""' + m.NOTE.strip(), '', 'Each invention lists its YouTube video IDs (title in the trailing comment). Every upload not',
       'listed here appears under "Other uploads" on the site.', '"""', '', 'CREATOR = ' + repr(m.CREATOR), '', 'INVENTIONS = [']
for row in m.SPEC:
    name, kind, idx, desc = row[:4]; links = row[4] if len(row) > 4 else []
    out += [f' dict(name={json.dumps(name)}, kind={json.dumps(kind)},', f'  desc={json.dumps(desc, ensure_ascii=False)},', '  videos=[']
    out += [f'   {json.dumps(V[i]["id"])},  # {V[i]["d"]} {V[i]["t"][:70]}' for i in sorted(idx)]
    out.append('  ],')
    out.append(('  links=[' + ', '.join(f'({json.dumps(l)}, {json.dumps(u)})' for l, u in links) + ']),') if links else ' ),')
out += [']', '', 'OTHER = None  # None = every upload not assigned above']
open(out_path, 'w').write('\n'.join(out) + '\n')
print(f"{out_path}: {len(m.SPEC)} inventions, {len(used)} videos assigned, {len(V) - len(used)} other")
