import json, sys, os, importlib.util
src, data, out = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("c", src); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
d = json.load(open(data)); V = {v["id"]: v for v in d["videos"]}
used = [i for inv in c.INVENTIONS for i in inv["videos"]] + c.OTHER
missing = set(V) - set(used); unknown = set(used) - set(V); dup = {i for i in used if used.count(i) > 1}
assert not missing and not unknown and not dup, (missing, unknown, dup)
invs = []
for inv in c.INVENTIONS:
    vs = sorted((V[i] for i in inv["videos"]), key=lambda v: v["d"])
    hero = max(vs, key=lambda v: (v["s"] > 70, v["v"]))
    invs.append(dict(name=inv["name"], kind=inv["kind"], desc=inv["desc"], hero=hero["id"],
        start=vs[0]["d"], views=sum(v["v"] for v in vs),
        videos=[dict(id=v["id"], t=v["t"], d=v["d"], v=v["v"], short=v["s"] <= 70) for v in vs],
        links=[dict(label=l, url=u) for l, u in inv.get("links", [])]))
other = [dict(id=i, t=V[i]["t"], d=V[i]["d"]) for i in sorted(c.OTHER, key=lambda i: V[i]["d"])]
payload = dict(creator=dict(name="Emily The Engineer", handle="@emilytheengineer", url="https://www.youtube.com/@emilytheengineer",
    tagline="engineer by degree, unhinged by nature", subs=int(d["stats"]["subscriberCount"]), uploads=len(V),
    since=min(v["d"] for v in V.values())), inventions=invs, other=other,
    uploads=[dict(d=v["d"], short=v["s"] <= 70) for v in sorted(V.values(), key=lambda v: v["d"])])
tpl = open(os.path.join(os.path.dirname(__file__), "template.html")).read()
open(out, "w").write(tpl.replace("/*DATA*/null", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")))
print(len(invs), "inventions,", len(other), "other uploads")
