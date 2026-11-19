"""Hand review: read every upload of a channel and label each video.

Labels: invention (grouped into named inventions), repair, tutorial, workshop, other.
  invention - something the maker designed and made, including tools, jigs and machines for their own shop, and
              repairs of things they built themselves
  repair    - fixing or restoring something they didn't make
  tutorial  - how-tos, techniques, salvage/teardown guides, explainers
  workshop  - shop tours, layouts, renovations, organisation, buying/installing commercial tools
  other     - everything else (vlogs, reviews, news, music, Q&As, kit assemblies, ...)

Usage:
  python3 build/review.py list data/NAME [FROM [TO]]   numbered uploads, oldest first
  python3 build/review.py write data/NAME SPEC.json      record the review and regenerate data/NAME_inventions.py

SPEC.json: {"inventions": [[name, kind, [numbers], description], ...],
            "repair": [numbers], "tutorial": [numbers], "workshop": [numbers],
            "creator": {optional overrides, e.g. "tagline"}}
Numbers not listed anywhere are labelled "other". The review is saved in data/review/<NAME>.json by video ID, so it
stays valid when new uploads arrive (new uploads simply aren't reviewed yet).
"""
import json, os, sys

mode, prefix = sys.argv[1], sys.argv[2]
V = sorted(json.load(open(prefix + "_videos.json"))["videos"], key=lambda v: (v["d"], v["id"]))
if mode == "list":
    a = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    b = int(sys.argv[4]) if len(sys.argv) > 4 else len(V)
    for i, v in enumerate(V[a:b], a):
        print(f'{i} {v["d"][2:7]} {"S" if v.get("vertical") else "L"}{v["s"] // 60:>4}m {v["v"]:>8} {v["t"][:80]}')
    sys.exit()

spec = json.load(open(sys.argv[3]))
old = {}; exec(open(prefix + "_inventions.py").read(), old)
C = {**old["CREATOR"], **spec.get("creator", {})}
labels, used = {}, set()
for name, kind, idx, desc in spec["inventions"]:
    dup = used & set(idx); assert not dup, f"{name}: already used {sorted(dup)}"
    used |= set(idx)
    for i in idx: labels[V[i]["id"]] = "invention"
for lab in ("repair", "tutorial", "workshop"):
    for i in spec.get(lab, []):
        assert i not in used, f"{lab}: {i} already an invention"
        labels[V[i]["id"]] = lab
for v in V: labels.setdefault(v["id"], "other")
os.makedirs(os.path.join(os.path.dirname(prefix), "review"), exist_ok=True)
rv = dict(channel=C["name"], videos=len(V), labels=labels,
          inventions={name: [V[i]["id"] for i in sorted(idx)] for name, _, idx, _ in spec["inventions"]})
json.dump(rv, open(os.path.join(os.path.dirname(prefix), "review", os.path.basename(prefix) + ".json"), "w"), indent=0)

L = [f'"""Inventions of {C["name"]}. Hand-grouped and hand-reviewed: every upload was read and labelled',
     '(invention / repair / tutorial / workshop / other, see data/review/). Only things the maker designed and made are',
     'listed here; every other upload appears under "Other uploads"."""', "", "CREATOR = " + repr(C), "", "INVENTIONS = ["]
for name, kind, idx, desc in spec["inventions"]:
    L += [f" dict(name={json.dumps(name, ensure_ascii=False)}, kind={json.dumps(kind)},", f"  desc={json.dumps(desc, ensure_ascii=False)},", "  videos=["]
    L += [f'   {json.dumps(V[i]["id"])},  # {V[i]["d"]} {V[i]["t"][:70]}' for i in sorted(idx)]
    L += ["  ],", " ),"]
L += ["]", "", "OTHER = None  # None = every upload not assigned above"]
open(prefix + "_inventions.py", "w").write("\n".join(L) + "\n")
n = {k: list(labels.values()).count(k) for k in ("invention", "repair", "tutorial", "workshop", "other")}
print(f'{C["name"]}: {len(spec["inventions"])} inventions; labels {n}')
