"""Write a hand-grouped inventions file for a Shorts-heavy maker whose titles vary too much for auto_inventions.py.

Usage:
  python3 build/hand_group.py list data/NAME            # print uploads, oldest first, numbered
  python3 build/hand_group.py write data/NAME SPEC.json # write data/NAME_inventions.py

SPEC.json: {"creator": {slug, name, tagline, other_label}, "groups": [[name, kind, [numbers from `list`], description], ...]}
Every upload not in a group appears under "Other uploads" on the site.
"""
import json, sys

mode, prefix = sys.argv[1], sys.argv[2]
V = sorted(json.load(open(prefix + "_videos.json"))["videos"], key=lambda v: (v["d"], v["id"]))
if mode == "list":
    for i, v in enumerate(V):
        print(f'{i} {v["d"][2:7]} {"S" if v.get("vertical") else "L"} {v["v"]:>7} {v["t"][:72]}')
    sys.exit()
spec = json.load(open(sys.argv[3]))
C, used = spec["creator"], set()
C.setdefault("person", C["name"])
L = [f'"""Curated inventions for {C["name"]}. Hand-grouped: most uploads are Shorts with varying titles, so the automatic',
     'drafter could not tell which videos belong to the same build. Every upload not listed here appears under "Other uploads"."""', "",
     "CREATOR = " + repr(C), "", "INVENTIONS = ["]
for name, kind, idx, desc in spec["groups"]:
    dup = used & set(idx)
    assert not dup, f"{name}: videos already used {sorted(dup)}"
    used |= set(idx)
    L += [f" dict(name={json.dumps(name, ensure_ascii=False)}, kind={json.dumps(kind)},", f"  desc={json.dumps(desc, ensure_ascii=False)},", "  videos=["]
    L += [f'   {json.dumps(V[i]["id"])},  # {V[i]["d"]} {V[i]["t"][:70]}' for i in sorted(idx)]
    L += ["  ],", " ),"]
L += ["]", "", "OTHER = None  # None = every upload not assigned above"]
open(prefix + "_inventions.py", "w").write("\n".join(L) + "\n")
print(f'{C["name"]}: {len(spec["groups"])} inventions from {len(used)} of {len(V)} uploads')
