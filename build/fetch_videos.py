"""Download a channel's full upload list (titles, dates, views, durations) via the YouTube Data API.

Usage:
  YOUTUBE_API_KEY=... python3 build/fetch_videos.py CHANNEL_ID_OR_@HANDLE data/NAME_videos.json
The key is read from the environment and never written to disk.
"""
import json, os, re, sys, urllib.parse, urllib.request

KEY = os.environ.get("YOUTUBE_API_KEY") or sys.exit("Set YOUTUBE_API_KEY first.")
channel, out = sys.argv[1], sys.argv[2]

def yt(path, **q):
    q["key"] = KEY
    return json.load(urllib.request.urlopen("https://www.googleapis.com/youtube/v3/" + path + "?" + urllib.parse.urlencode(q)))

ch = yt("channels", part="snippet,contentDetails,statistics", **({"forHandle": channel} if channel.startswith("@") else {"id": channel}))["items"][0]
uploads, ids, tok = ch["contentDetails"]["relatedPlaylists"]["uploads"], [], None
while True:
    q = dict(part="contentDetails", playlistId=uploads, maxResults=50, **({"pageToken": tok} if tok else {}))
    page = yt("playlistItems", **q)
    ids += [i["contentDetails"]["videoId"] for i in page["items"]]
    tok = page.get("nextPageToken")
    if not tok: break
videos = []
for i in range(0, len(ids), 50):
    # "player" with maxWidth returns the embed size scaled to the video's real aspect ratio,
    # which is the only way the API reveals whether a video is vertical (needed to tell Shorts apart).
    for v in yt("videos", part="snippet,statistics,contentDetails,player", maxWidth=1000, id=",".join(ids[i:i + 50]))["items"]:
        m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", v["contentDetails"]["duration"])
        secs = sum(int(x or 0) * k for x, k in zip(m.groups(), (86400, 3600, 60, 1)))
        pw, ph = int(v["player"].get("embedWidth") or 0), int(v["player"].get("embedHeight") or 0)
        videos.append(dict(id=v["id"], t=v["snippet"]["title"], d=v["snippet"]["publishedAt"][:10],
                           v=int(v["statistics"].get("viewCount", 0)), s=secs,
                           vertical=(ph >= pw) if pw and ph else None, desc=v["snippet"]["description"][:600]))
videos.sort(key=lambda x: x["d"])
sn = ch["snippet"]
channel_info = dict(id=ch["id"], title=sn["title"], handle=sn.get("customUrl", ""), description=sn.get("description", "")[:400],
                    since=sn["publishedAt"][:10], avatar=sn["thumbnails"].get("high", sn["thumbnails"]["default"])["url"])
json.dump(dict(channel=channel_info, stats=ch["statistics"], videos=videos), open(out, "w"), indent=1)
print(f"{len(videos)} videos -> {out}")
