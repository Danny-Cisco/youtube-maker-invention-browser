# YouTube Maker Invention Browser

A portfolio site for catching up on maker YouTubers: every invention grouped across all of its videos, with a short description, embedded videos, press coverage and files, a timeline of the whole channel, release-schedule stats, and a build history for each project.

The first creator is **Emily The Engineer** (44 inventions from 83 uploads).

## View it

Open `index.html` through a web address, e.g. GitHub Pages (Settings → Pages → Deploy from branch → `main`), or locally:

```bash
python3 -m http.server 8000
```

then visit http://localhost:8000. YouTube only plays embedded videos on pages served over http/https; opened as a plain file, videos open on YouTube instead.

## How it's built

`index.html` is generated, so don't edit it by hand.

| File | What it is |
|---|---|
| `data/emily_videos.json` | Every upload with title, date, views and duration, from the YouTube Data API |
| `data/emily_inventions.py` | The curated part: which videos belong to which invention, descriptions, and article/file links |
| `build/template.html` | Page layout, styles and scripts |
| `build/build.py` | Combines the above into `index.html` and checks every upload is accounted for |
| `build/fetch_videos.py` | Refreshes a channel's video data |

Refresh view counts, then rebuild:

```bash
YOUTUBE_API_KEY=your-key python3 build/fetch_videos.py UC_4YBM08hcpJqLl3vvgTqXg data/emily_videos.json
```

```bash
python3 build/build.py data/emily_inventions.py data/emily_videos.json index.html
```

If new videos have been uploaded, the build stops and lists them so they can be added to an invention (or to `OTHER`) in `data/emily_inventions.py`.
