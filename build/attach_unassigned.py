"""For a hand-curated maker: put unassigned build videos (livestreams included) where they belong, keeping the curation.

Usage: python3 build/attach_unassigned.py data/NAME [--apply]

Only livestreams are moved (the hand curation already decided about everything else), using the same title rules
as auto_inventions.py:
- an unassigned video joins an existing invention when its key words match that invention's (its name plus the words
  most of its videos share), e.g. "Vibraphone Holders Part 4 | Marble Machine Live" joins Marble Machine 3;
- unassigned livestreams that form a multi-part series of their own (with any matching non-live parts) ("Prusa i3 MK2 clone live assembly: p1 ... p6")
  become a new invention;
- one-off videos with no match stay in Other uploads, as the hand curation decided.
Without --apply it only prints the plan. With --apply it rewrites data/NAME_inventions.py (names, descriptions,
links and the docstring are kept; an explicit OTHER list is updated).
"""
import ast, collections, json, os, re, sys

prefix, apply = sys.argv[1], "--apply" in sys.argv
# --join REGEX / --new REGEX: when applying, keep only joins to inventions, and new series, whose names match (after review)
opt = lambda k: re.compile(sys.argv[sys.argv.index(k) + 1], re.I) if k in sys.argv else None
here = os.path.dirname(os.path.abspath(__file__))
src = open(prefix + "_inventions.py").read()
mod = {}; exec(src, mod)
C, INV, OTHER = mod["CREATOR"], mod["INVENTIONS"], mod.get("OTHER")
V = json.load(open(prefix + "_videos.json"))["videos"]
byid = {v["id"]: v for v in V}

# borrow the title rules from auto_inventions.py
argv, sys.argv = sys.argv, ["x", prefix + "_videos.json", os.devnull, C["slug"], C["name"], C.get("tagline", "")]
exec(open(os.path.join(here, "auto_inventions.py")).read().split("ONLY = re.compile")[0])
sys.argv = argv

assigned = {i for x in INV for i in x["videos"]}
cores = []
for x in INV:
    cnt = collections.Counter(w for i in x["videos"] if i in byid for w in key_tokens(byid[i]["t"]))
    n = max(1, len([i for i in x["videos"] if i in byid]))
    cores.append((x, frozenset(w for w, c in cnt.items() if c >= max(2, n / 2)) | tokens(x["name"])))

def match(tk):
    best, score = None, 0
    for x, core in cores:
        if not core: continue
        common = len(core & tk)
        if common >= 2 and common / min(len(core), len(tk)) >= 0.75 or (common >= 1 and tk <= core and len(tk) >= 1 and min(map(len, tk)) >= 5):
            sc = common / len(tk)
            if sc > score: best, score = x, sc
    return best

add, rest = collections.defaultdict(list), []
for v in V:
    if v["id"] in assigned or NON_BUILD.search(strip_live(v["t"])): continue
    tk = key_tokens(v["t"])
    if not tk: continue
    x = match(tk) if LIVE.search(v["t"]) else None
    if x: add[x["name"]].append(v["id"])
    elif not v.get("vertical"): rest.append((v, tk, bool(SERIES.search(strip_live(v["t"])))))

# new inventions: multi-part series among the leftovers
clusters = []
for v, tk, head in sorted(rest, key=lambda r: (not r[2], r[0]["d"])):
    best = None
    for cl in clusters:
        common = len(cl["core"] & tk)
        if tk == cl["core"] or (common >= 2 and common / min(len(cl["core"]), len(tk)) >= 0.75): best = cl; break
    if best: best["videos"].append(v)
    else: clusters.append(dict(core=tk, head=head, videos=[v]))
new = [cl for cl in clusters if len(cl["videos"]) >= 2 and any(LIVE.search(v["t"]) for v in cl["videos"])]

print(f"== {C['name']}: {sum(map(len, add.values()))} videos join existing inventions, {len(new)} new series")
for n, ids in add.items():
    print(f"  + {n}: " + " | ".join(byid[i]["t"][:50] for i in ids[:4]) + (" …" if len(ids) > 4 else ""))
for cl in new:
    vs = sorted(cl["videos"], key=lambda v: v["d"])
    print(f"  NEW {clean_title(vs[0]['t'])[:50]} ({len(vs)}): " + " | ".join(v["t"][:40] for v in vs[:3]))
if not apply: sys.exit()
J, N = opt("--join"), opt("--new")
add = {n: ids for n, ids in add.items() if J and J.search(n)}
new = [cl for cl in new if N and N.search(clean_title(sorted(cl["videos"], key=lambda v: v["d"])[0]["t"]))]

for x in INV:
    if x["name"] in add: x["videos"] = sorted(set(x["videos"]) | set(add[x["name"]]), key=lambda i: byid[i]["d"] if i in byid else "")
for cl in new:
    vs = sorted(cl["videos"], key=lambda v: v["d"])
    top = max(vs, key=lambda v: (not LIVE.search(v["t"]), v["v"]))
    nm = clean_title(top["t"]); nm = nm.title() if nm.isupper() else nm[:1].upper() + nm[1:]
    INV.append(dict(name=nm[:70], kind="Build", desc=first_sentence(top.get("desc", "")) or top["t"].strip() + ".", videos=[v["id"] for v in vs]))
moved = {i for ids in add.values() for i in ids} | {v["id"] for cl in new for v in cl["videos"]}
if isinstance(OTHER, list): OTHER = [i for i in OTHER if i not in moved]

doc = ast.get_docstring(ast.parse(src)) or f"Curated inventions for {C['name']}."
L = ['"""' + doc.replace('"""', "'''") + '\n\nLivestreams and series videos attached by build/attach_unassigned.py."""', "", "CREATOR = " + repr(C), "", "INVENTIONS = ["]
for x in INV:
    L += [f' dict(name={json.dumps(x["name"], ensure_ascii=False)}, kind={json.dumps(x.get("kind", "Build"))},', f'  desc={json.dumps(x["desc"], ensure_ascii=False)},', "  videos=["]
    L += [f'   {json.dumps(i)},  # {byid[i]["d"]} {byid[i]["t"][:70]}' if i in byid else f'   {json.dumps(i)},' for i in x["videos"]]
    L += ["  ],"]
    if x.get("links"): L += ["  links=" + repr([tuple(l) for l in x["links"]]) + ","]
    L += [" ),"]
L += ["]", ""]
L += ["OTHER = None  # None = every upload not assigned above"] if OTHER is None else ["OTHER = ["] + [f'   {json.dumps(i)},  # {byid[i]["d"]} {byid[i]["t"][:70]}' if i in byid else f'   {json.dumps(i)},' for i in OTHER] + ["]"]
open(prefix + "_inventions.py", "w").write("\n".join(L) + "\n")
print("  written")
