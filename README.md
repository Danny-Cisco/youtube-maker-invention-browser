# YouTube Maker Invention Browser

A site for catching up on maker YouTubers: every invention grouped across all of its videos, with a short description, embedded videos, press coverage and files, a timeline of the whole channel, release-schedule stats, and a build history for each project.

Makers so far:

| Maker | Inventions | Uploads |
|---|---|---|
| Simone Giertz | 76 | 260 |
| Emily The Engineer | 44 | 83 |
| Look Mum No Computer | 107 | 857 |
| Stuff Made Here | 27 | 42 |
| Michael Reeves | 37 | 57 |
| Allen Pan | 54 | 128 |
| William Osman | 62 | 169 |
| The Backyard Scientist | 47 | 191 |
| Xyla Foxlin | 36 | 203 |
| Colin Furze | 133 | 414 |
| Laura Kampf | 42 | 556 |
| James Bruton | 60 | 802 |

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
| `data/<maker>_videos.json` | Every upload with title, date, views and duration, from the YouTube Data API |
| `data/<maker>_inventions.py` | The curated part: maker info, which videos belong to which invention, descriptions, and article/file links |
| `build/template.html` | Page layout, styles and scripts |
| `build/build.py` | Combines all makers into `index.html` and checks every upload is accounted for |
| `build/fetch_videos.py` | Refreshes a channel's video data |

Refresh a maker's videos (channel ID or @handle), then rebuild:

```bash
YOUTUBE_API_KEY=your-key python3 build/fetch_videos.py @LookMumNoComputer data/lmnc_videos.json
```

```bash
python3 build/build.py index.html data/simone data/emily data/lmnc data/smh data/reeves data/allen data/osman data/backyard data/xyla data/furze data/kampf data/bruton
```

To add a maker, fetch their videos to `data/<name>_videos.json`, write a curation spec and turn it into `data/<name>_inventions.py` with `build/make_inventions.py` (see its docstring), and add `data/<name>` to the build command.

For a maker whose `OTHER` is an explicit list (Emily), the build stops and lists any new uploads so they can be assigned. For a maker whose `OTHER` is `None` (Look Mum No Computer), unassigned uploads go to "Other uploads" automatically.
