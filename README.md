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
| Wintergatan | 5 | 501 |
| Integza | 17 | 278 |
| Hacksmith Industries | 46 | 1,380 |
| Mark Rober | 40 | 277 |
| I Did A Thing | 54 | 126 |
| Nerdforge | 32 | 207 |
| DIY Perks | 32 | 123 |
| styropyro | 26 | 205 |
| Unnecessary Inventions | 60 | 545 |
| Crescent Shay | 20 | 63 |
| This Old Tony | 48 | 234 |
| Becky Stern | 55 | 354 |
| Kids Invent Stuff | 73 | 577 |
| Brothers Make | 24 | 206 |
| Littlejem | 18 | 293 |
| Mr. Volt | 15 | 57 |
| Estefannie | 6 | 29 |
| Adam Savage (Tested) | 19 | 7,071 |
| Jimmy DiResta | 28 | 910 |
| Austin Bradley | 13 | 160 |
| Thea Ulrich | 9 | 19 |
| Jabrils | 25 | 238 |
| Ali Spagnola | 25 | 750 |
| Nate From the Internet | 12 | 367 |
| NileRed | 17 | 402 |
| Alex Ernst | 7 | 119 |
| ElectroBOOM | 26 | 395 |
| CuriousMarc | 14 | 678 |
| Applied Science | 30 | 280 |
| Breaking Taps | 25 | 107 |
| Jeff Geerling | 8 | 585 |
| CNC Kitchen | 18 | 258 |
| Made with Layers | 7 | 597 |
| 3D Printing Nerd | 10 | 1,525 |

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
python3 build/build.py index.html $(cat build/makers.txt)
```

To add a maker, fetch their videos to `data/<name>_videos.json`, write a curation spec and turn it into `data/<name>_inventions.py` with `build/make_inventions.py` (see its docstring), and add `data/<name>` to `build/makers.txt`, which lists every maker in front-page order.

For a maker whose `OTHER` is an explicit list (Emily), the build stops and lists any new uploads so they can be assigned. For a maker whose `OTHER` is `None` (Look Mum No Computer), unassigned uploads go to "Other uploads" automatically.
