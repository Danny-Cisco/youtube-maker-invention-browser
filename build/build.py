"""Build index.html from one or more makers.

Usage:
  python3 build/build.py index.html data/emily data/lmnc

Each maker needs data/<name>_inventions.py (curated) and data/<name>_videos.json (from fetch_videos.py).
The build stops if a curated video ID is unknown or used twice, or (when OTHER is a list) if an upload
hasn't been assigned anywhere, so new uploads get noticed.
"""
import importlib.util, json, os, sys

out, prefixes = sys.argv[1], sys.argv[2:]
here = os.path.dirname(os.path.abspath(__file__))

def is_short(v):
    """Shorts are vertical (or square) videos; everything horizontal is a regular video. Orientation is
    used on its own rather than YouTube's current length cap, which has changed before. If orientation
    is missing (rare, e.g. some streams), fall back to guessing from length and hashtags."""
    if v.get("vertical") is not None:
        return v["vertical"]
    t = v["t"].lower()
    return v["s"] <= 60 or (v["s"] <= 180 and "#short" in t)

# Other platforms each maker links from their YouTube descriptions: {slug: [[platform, url], ...]} (see MAKER_PLATFORMS.md).
_soc = os.path.join(here, "..", "data", "socials.json")
SOCIALS = json.load(open(_soc)) if os.path.exists(_soc) else {}
# Each maker's country: {slug: [ISO alpha-2, "channel" (from their YouTube settings) or "manual"]}, and the world map outline.
_cty = os.path.join(here, "..", "data", "countries.json")
COUNTRIES = json.load(open(_cty)) if os.path.exists(_cty) else {}
WORLD = json.load(open(os.path.join(here, "world.json"))) if os.path.exists(os.path.join(here, "world.json")) else None

def load(prefix):
    spec = importlib.util.spec_from_file_location("inv", prefix + "_inventions.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    data = json.load(open(prefix + "_videos.json"))
    V = {v["id"]: v for v in data["videos"]}
    assigned = [i for inv in mod.INVENTIONS for i in inv["videos"]]
    other = mod.OTHER if mod.OTHER is not None else [i for i in V if i not in set(assigned)]
    used = assigned + list(other)
    unknown = set(used) - set(V)
    dup = {i for i in used if used.count(i) > 1}
    missing = set(V) - set(used)
    problems = []
    if unknown: problems.append(f"unknown video IDs: {sorted(unknown)}")
    if dup: problems.append(f"videos used twice: {sorted(dup)}")
    if missing: problems.append("new uploads not assigned to an invention or OTHER:\n" + "\n".join(f"  {i}  {V[i]['d']}  {V[i]['t']}" for i in sorted(missing, key=lambda i: V[i]["d"])))
    if problems: sys.exit(f"{prefix}: " + "\n".join(problems))
    invs = []
    for inv in mod.INVENTIONS:
        vs = sorted((V[i] for i in inv["videos"]), key=lambda v: v["d"])
        hero = max(vs, key=lambda v: (not is_short(v), v["v"]))
        invs.append(dict(name=inv["name"], kind=inv["kind"], desc=inv["desc"], hero=hero["id"],
            start=vs[0]["d"], views=sum(v["v"] for v in vs),
            videos=[dict(id=v["id"], t=v["t"], d=v["d"], v=v["v"], s=v["s"], short=is_short(v)) for v in vs],
            links=[dict(label=l, url=u) for l, u in inv.get("links", [])]))
    ch, C = data["channel"], mod.CREATOR
    creator = dict(slug=C["slug"], name=C["name"], person=C.get("person", ""), tagline=C["tagline"],
        otherLabel=C.get("other_label", "Other uploads"), handle=ch["handle"], url="https://www.youtube.com/" + ch["handle"],
        avatar=ch["avatar"], subs=int(data["stats"]["subscriberCount"]), uploadCount=len(V), since=min(v["d"] for v in V.values()),
        inventions=invs, links=SOCIALS.get(C["slug"], []), country=(COUNTRIES.get(C["slug"]) or [""])[0],
        other=sorted(other, key=lambda i: V[i]["d"]),
        uploads=[dict(id=v["id"], t=v["t"], d=v["d"], v=v["v"], s=v["s"], short=is_short(v)) for v in sorted(V.values(), key=lambda v: v["d"])])
    print(f"{C['name']}: {len(invs)} inventions, {len(assigned)} videos in inventions, {len(other)} other uploads")
    return creator

payload = dict(creators=[load(p) for p in prefixes], world=WORLD)
tpl = open(os.path.join(here, "template.html")).read()
open(out, "w").write(tpl.replace("/*DATA*/null", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")))
