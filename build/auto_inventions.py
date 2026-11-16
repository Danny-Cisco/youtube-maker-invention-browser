"""Draft a curation for a smaller maker automatically, for review before publishing.

Usage: python3 build/auto_inventions.py data/NAME_videos.json data/NAME_inventions.py SLUG "Display Name" "Tagline" [max_inventions]

How it works:
- Only long-form (horizontal) videos are considered (Shorts too when a channel has fewer than 15 long-form); obvious non-builds (Q&As, vlogs, updates, reviews,
  unboxings, tours, livestreams...) are skipped.
- Multi-part series ("Part 2", "Ep. 3", "#4", "Pt 1") are merged into one invention by their shared title.
- Each invention's description is the first real sentence the maker wrote in the earliest video's
  description (links, sponsor and subscribe lines are skipped), so the words are the maker's own.
- At most max_inventions (default 60) are kept, by total views; the rest stay under Other uploads.
The output has the same format as hand-curated files, so it can be edited by hand afterwards.
"""
import json, os, re, sys

src, out, slug, name, tagline = sys.argv[1:6]
limit = int(sys.argv[6]) if len(sys.argv) > 6 else 60
data = json.load(open(src))
V = data["videos"]

NON_BUILD = re.compile(r"\b(q\s?&\s?a|q and a|vlog|update|unbox|review|tour|live ?stream|livestream|podcast|announce|trailer|"
                       r"giveaway|haul|react|subscriber|merch|sponsor|channel|tutorial for beginners|ama|stream highlights|"
                       r"what'?s in my|my (top|favou?rite)|interview|talk|panel|teaser|install|setup|guide|preview|overview|tuning|for dummies|\blive\b|공지|"
                       r"리뷰|언박싱|소개|구입|추천)", re.I)
SERIES = re.compile(r"\s*(\(|\[)?\b(part|pt\.?|ep\.?|episode|chapter|vol\.?|volume|day)\s*\d+\b(\)|\])?|\s#\d+\b|\s\d+/\d+\b", re.I)
EMOJI = re.compile(r"[\U0001F000-\U0001FFFF☀-➿️]")
SKIP_LINE = re.compile(r"http|www\.|sponsor|patreon|subscribe|use code|discount|affiliate|merch|instagram|tiktok|twitter|"
                       r"facebook|discord|business|email|@|#|links?:|music:|^edit|^update|thanks to|thank you|support|gear|amazon|^\W*$", re.I)

def clean_title(t):
    t = re.sub(r"#\w+", "", EMOJI.sub("", t))
    t = SERIES.sub("", t)
    t = re.sub(r"\s*[\(\[][^()\[\]]*[\)\]]\s*", " ", t)          # drop bracketed asides
    parts = re.split(r"\s+[|–—-]\s+|:\s+", t)
    t = parts[0] if len(parts[0]) >= 14 or len(parts) == 1 else t
    t = re.sub(r"\s+", " ", t).strip(" -|:.,!?")
    return t

def key(t):
    return re.sub(r"[^a-z0-9]+", " ", clean_title(t).lower()).strip()

def first_sentence(desc):
    for line in desc.splitlines():
        line = line.strip()
        if len(line) < 25 or SKIP_LINE.search(line) or EMOJI.search(line) or sum(c.isupper() for c in line) > 0.6 * sum(c.isalpha() for c in line) \
                or re.match(r"^[\d\W]", line) or len(line.split()) < 6:
            continue
        s = re.split(r"(?<=[.!?])\s", line)[0]
        return (s[:217] + "…") if len(s) > 220 else s
    return ""

# Channels that are mostly Shorts (fewer than 15 long-form videos) get their Shorts considered too.
ONLY = re.compile(os.environ["ONLY"], re.I) if os.environ.get("ONLY") else None   # optional: keep only matching titles
few_long = sum(not v.get("vertical") for v in V) < 15
groups = {}
for i, v in enumerate(V):
    if (v.get("vertical") and not few_long) or NON_BUILD.search(v["t"]) or (ONLY and not ONLY.search(v["t"])):
        continue
    groups.setdefault(key(v["t"]), []).append(i)

inv = []
for k, idx in groups.items():
    if not k:
        continue
    vs = [V[i] for i in idx]
    first = min(vs, key=lambda v: v["d"])
    nm = clean_title(first["t"])
    nm = nm[:1].upper() + nm[1:] if nm.isupper() is False else nm.title()
    desc = first_sentence(first.get("desc", "")) or f"{first['t'].strip()}."
    inv.append(dict(name=nm[:70], views=sum(v["v"] for v in vs), videos=sorted(idx, key=lambda i: V[i]["d"]), desc=desc))

inv.sort(key=lambda x: -x["views"])
inv = inv[:limit]
names = set()
for x in inv:                                                  # keep names unique
    base, n = x["name"], 2
    while x["name"].lower() in names:
        x["name"] = f"{base} ({n})"; n += 1
    names.add(x["name"].lower())
inv.sort(key=lambda x: V[x["videos"][0]]["d"])

lines = ['"""Curated inventions for ' + name + ' (' + data["channel"]["handle"] + ').', '',
         'Drafted by build/auto_inventions.py (long-form builds, series merged, descriptions in the maker\'s own words),',
         'then reviewed. Every upload not listed here appears under "Other uploads" on the site.', '"""', '',
         'CREATOR = ' + repr(dict(slug=slug, name=name, person=name, tagline=tagline,
                                  other_label="Other uploads: Shorts, updates and other videos")), '', 'INVENTIONS = [']
for x in inv:
    lines += [f' dict(name={json.dumps(x["name"], ensure_ascii=False)}, kind="Build",',
              f'  desc={json.dumps(x["desc"], ensure_ascii=False)},', '  videos=[']
    lines += [f'   {json.dumps(V[i]["id"])},  # {V[i]["d"]} {V[i]["t"][:70]}' for i in x["videos"]]
    lines += ['  ],', ' ),']
lines += [']', '', 'OTHER = None  # None = every upload not assigned above']
open(out, "w").write("\n".join(lines) + "\n")
print(f"{name}: {len(inv)} inventions from {sum(len(x['videos']) for x in inv)} videos ({len(V)} uploads)")
