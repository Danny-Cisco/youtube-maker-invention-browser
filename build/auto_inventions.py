"""Draft a curation for a maker automatically, grouping videos by invention.

Usage: python3 build/auto_inventions.py data/NAME_videos.json data/NAME_inventions.py SLUG "Display Name" "Tagline" [max_single]

How it works:
- Long-form (horizontal) videos start inventions. Shorts join an invention they clearly belong to; on channels with
  fewer than 15 long-form videos, Shorts can start inventions too.
- Livestreams are treated like any other video: the "LIVE" / "#livestream" / "[stream]" label is stripped and the
  video is judged by its subject, so a stream of "Building the Voron V2 Part 8" joins the Voron V2 invention.
- Videos that aren't builds are skipped, judged on whole words only: Q&As, chats and hangouts, podcasts, unboxings,
  reviews, launch events, listening parties, giveaways, trailers, guides and the like.
- Videos are grouped when their titles share the same key words (stems, ignoring filler like "part 3", "building",
  "live", "the"), so "Making a Feral Ghoul costume Part 13" and "Making Feral Ghoul part 3" are one invention.
- Every invention with two or more videos is kept. One-video inventions are added by views up to max_single
  (default 60); the rest stay under Other uploads.
- Each invention's description is the first real sentence the maker wrote in the earliest video's description.
The output has the same format as hand-curated files, so it can be edited by hand afterwards.
Set ONLY=<regex> to consider only matching titles (used for Kynosys, a tool-review channel).
"""
import json, os, re, sys, collections

src, out, slug, name, tagline = sys.argv[1:6]
max_single = int(sys.argv[6]) if len(sys.argv) > 6 else 60
data = json.load(open(src))
V = data["videos"]

W = lambda words: re.compile(r"(?<![\w])(?:" + words + r")(?![\w])", re.I)   # whole words only
LIVE = W(r"was live|live ?stream(?:ing)?(?: replay| vod)?|livestream(?:ing)?|live ?chat|live|stream(?:ing)?|vod|\[stream\]")
NON_BUILD = W(r"q\s?&\s?a|q\s?\+\s?a|q and a|ask me anything|ama|vlog|unboxing|unboxed|unbox|reviews?|reviewing|podcast|announcement|announcing|"
              r"trailer|teaser|giveaways?|haul|reacts?|reaction|merch|interview|panel discussion|chat|chats|chatting|chill|hangout|hang out|"
              r"listening party|launch (?:party|event)|supporters only|patreon only|members only|news|happy hour|this is only a test|"
              r"talking shop|talks|viewer mail|mini mail|mail ?bag|mail call|office hours|first impressions|first look|subscriber special|channel update|giveaway|tier list|top \d+|"
              r"guide|tutorial for beginners|how to install|installation|tuning|for dummies|basics|101|course|lesson|"
              r"apps? of the (?:week|day)|quick look|wrap-?up|highlights|promo|compilation|mashups?|"
              r"공지|리뷰|언박싱|소개|구입|추천")
SERIES = re.compile(r"\s*[(\[]?\b(?:part|pt\.?|ep\.?|episode|chapter|vol\.?|volume|day|session|stream)\s*#?\d+(?:\s*/\s*\d+)?\b[)\]]?|\s#\d+\b|\s\d+/\d+\b|\(\d+\s*[-–:]", re.I)
EMOJI = re.compile(r"[\U0001F000-\U0001FFFF☀-➿️]")
SKIP_LINE = re.compile(r"http|www\.|sponsor|patreon|subscribe|use code|discount|affiliate|merch|instagram|tiktok|twitter|"
                       r"facebook|discord|business|email|@|#|links?:|music:|^edit|^update|thanks to|thank you|support|gear|amazon|^\W*$", re.I)
STOP = set("""the a an of and or to in on for with my i im i'm we our your you is it its this that these those how what why when
 part pt ep episode build building built builds making make made makes new first final more again diy vs from at by up out
 into be can will just finally really very let lets let's s t live stream video videos full project projects ever world worlds
 here go going get got do doing did done one two three day days time""".split())
STEM = lambda w: re.sub(r"(ings?|ed|es|s)$", "", w) if len(w) > 4 else w

def strip_live(t):
    t = re.sub(r"#[A-Za-z_]\w*", "", EMOJI.sub("", t))   # word hashtags only; keep episode numbers like #11
    t = LIVE.sub(" ", t)
    return re.sub(r"\s+", " ", t).strip(" -|:!.,")

def clean_title(t):
    t = SERIES.sub("", strip_live(t))
    t = re.sub(r"\s*[\(\[][^()\[\]]*[\)\]]\s*", " ", t)          # drop bracketed asides
    parts = re.split(r"\s+[|–—-]\s+|:\s+", t)
    t = parts[0] if len(parts[0]) >= 14 or len(parts) == 1 else t
    return re.sub(r"\s+", " ", t).strip(" -|:.,!?")

maker_words = {STEM(w) for w in re.findall(r"[a-z0-9]+", name.lower())}
def tokens(t):
    ws = re.findall(r"[a-z0-9][a-z0-9.']*", clean_title(t).lower())
    ws = [w.strip(".'") for w in ws]
    return frozenset(STEM(w) for w in ws if w and w not in STOP and not w.isdigit() and not re.fullmatch(r"[\d\-/]+", w)) - maker_words

def key_tokens(t):
    """A numbered series ("libsurvive livestream #11 - Let's get our bearings") is keyed by its name before the number."""
    s = strip_live(t)
    m = SERIES.search(s)
    if m:
        head = tokens(s[:m.start()])
        if head: return head
    return tokens(t)

def first_sentence(desc):
    for line in desc.splitlines():
        line = line.strip()
        if len(line) < 25 or SKIP_LINE.search(line) or EMOJI.search(line) or sum(c.isupper() for c in line) > 0.6 * sum(c.isalpha() for c in line) \
                or re.match(r"^[\d\W]", line) or len(line.split()) < 6:
            continue
        s = re.split(r"(?<=[.!?])\s", line)[0]
        return (s[:217] + "…") if len(s) > 220 else s
    return ""

ONLY = re.compile(os.environ["ONLY"], re.I) if os.environ.get("ONLY") else None
few_long = sum(not v.get("vertical") for v in V) < 15
cand = []
for i, v in enumerate(V):
    if ONLY and not ONLY.search(v["t"]):
        continue
    if NON_BUILD.search(strip_live(v["t"])):
        continue
    tk = key_tokens(v["t"])
    if not tk:                                    # nothing left but a date or the maker's name: a general stream
        continue
    cand.append((i, tk, bool(SERIES.search(strip_live(v["t"])))))
# On channels with plenty of long-form videos, Shorts may join an invention but never start one.
joiner = lambda i: bool(V[i].get("vertical")) and not few_long

# Group around fixed cores (no chaining): a video joins a group when its key words mostly overlap the group's core,
# or when the core is a numbered series' one-word name ("libsurvive") that appears in its title.
df = collections.Counter(w for _, tk, _ in cand for w in tk)
rare = lambda w: df[w] <= max(12, len(cand) // 40)
clusters = []
for i, tk, head in sorted(cand, key=lambda c: (joiner(c[0]), not c[2], V[c[0]]["d"])):   # series names first, Shorts last
    best, score = None, 0
    for cl in clusters:
        core, common = cl["core"], len(cl["core"] & tk)
        small = min(len(core), len(tk))
        sc = 2 if tk == core else (common / small if common >= 2 and common / small >= 0.75 else 0)
        if not sc and cl["head"] and len(core) == 1 and core <= tk and len(next(iter(core))) >= 4 and rare(next(iter(core))): sc = 0.8
        if sc > score: best, score = cl, sc
    if best: best["videos"].append(i)
    elif not joiner(i): clusters.append(dict(core=tk, head=head, videos=[i]))
groups = {n: cl["videos"] for n, cl in enumerate(clusters)}

inv = []
for idx in groups.values():
    vs = [V[i] for i in idx]
    first = min(vs, key=lambda v: v["d"])
    top = max(vs, key=lambda v: (not v.get("vertical"), not LIVE.search(v["t"]), v["v"]))   # name it after its main edited video
    nm = clean_title(top["t"])
    mw = "|".join(map(re.escape, name.split()))
    nm = re.sub(r"^(?:(?:" + mw + r")\b\s*)+[:\-|–]+\s*", "", nm, flags=re.I) or nm          # drop "EVIL TED : " prefixes
    nm = re.sub(r"\s+(?:part|pt\.?|ep\.?|episode)\s*$", "", nm, flags=re.I)
    nm = nm.title() if nm.isupper() else nm[:1].upper() + nm[1:]
    desc = first_sentence(top.get("desc", "")) or first_sentence(first.get("desc", "")) or f"{top['t'].strip()}."
    inv.append(dict(name=nm[:70], views=sum(v["v"] for v in vs), videos=sorted(idx, key=lambda i: V[i]["d"]), desc=desc))

multi = [x for x in inv if len(x["videos"]) > 1]
single = sorted([x for x in inv if len(x["videos"]) == 1], key=lambda x: -x["views"])[:max_single]
inv = multi + single
names = set()
for x in sorted(inv, key=lambda x: -x["views"]):              # keep names unique
    base, n = x["name"], 2
    while x["name"].lower() in names:
        x["name"] = f"{base} ({n})"; n += 1
    names.add(x["name"].lower())
inv.sort(key=lambda x: V[x["videos"][0]]["d"])

prev = {}
if os.path.exists(out):                                       # keep the maker's display details from the existing file
    g = {}; exec(open(out).read(), g); prev = g.get("CREATOR", {})
creator = dict(slug=slug, name=name, person=name, tagline=tagline, other_label="Other uploads: Shorts, updates and other videos")
creator.update({k: prev[k] for k in ("person", "tagline", "other_label") if k in prev})
lines = ['"""Curated inventions for ' + name + ' (' + data["channel"]["handle"] + ').', '',
         'Drafted by build/auto_inventions.py (builds grouped by shared key words, livestreams included, descriptions in the',
         'maker\'s own words). Every upload not listed here appears under "Other uploads" on the site.', '"""', '',
         'CREATOR = ' + repr(creator), '', 'INVENTIONS = [']
for x in inv:
    lines += [f' dict(name={json.dumps(x["name"], ensure_ascii=False)}, kind="Build",',
              f'  desc={json.dumps(x["desc"], ensure_ascii=False)},', '  videos=[']
    lines += [f'   {json.dumps(V[i]["id"])},  # {V[i]["d"]} {V[i]["t"][:70]}' for i in x["videos"]]
    lines += ['  ],', ' ),']
lines += [']', '', 'OTHER = None  # None = every upload not assigned above']
open(out, "w").write("\n".join(lines) + "\n")
nl = sum(1 for x in inv for i in x["videos"] if LIVE.search(V[i]["t"]))
print(f"{name}: {len(inv)} inventions ({len(multi)} multi-video) from {sum(len(x['videos']) for x in inv)} of {len(V)} uploads, {nl} streams")
