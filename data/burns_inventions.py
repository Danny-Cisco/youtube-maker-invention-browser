"""Curated inventions for Thomas Burns (Workshop Nation, @ThomasBurns).
kind: Robot | Restoration | Gadget

Each invention lists its YouTube video IDs (title in the trailing comment). Every upload not
listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'thomas-burns', 'name': 'Thomas Burns', 'person': 'Thomas Burns', 'tagline': 'A love letter to vintage tech: Soviet CRTs and Nixie calculators restored, and an Alexa turned animatronic.', 'other_label': 'Other uploads: Shorts'}

INVENTIONS = [
 dict(name="Animatronic Alexa", kind="Robot",
  desc="An Amazon Echo turned into an animatronic robot face with face-tracking eyes (designed by Will Cogley). His most-watched build by far.",
  videos=[
   "QnVszYK1-fQ",  # 2023-01-11 Big things in the works for our next build!
   "ejHmpcbf4PA",  # 2023-01-24 Animatronic eye module complete! Next up: pairing with a face-tracking
   "bO-DWWFolPw",  # 2023-07-01 The coolest robot I've ever built!
   "axA5YjIpGXU",  # 2023-07-08 She’s alive! Come check out the build video! #robot #alexa
  ],
  links=[("Build instructions (Hackster)", "https://www.hackster.io/tmburns/breathing-life-into-an-amazon-echo-device-ed9ea3")]),
 dict(name="Vintage Robot Rescue", kind="Robot",
  desc="Moving across the globe, building a new workshop and rescuing a forgotten vintage robot.",
  videos=[
   "Nw5v5inCQQM",  # 2024-01-29 The Great Robot Rescue
   "afhKdjMVis8",  # 2024-02-14 Vintage Robot Rescue!
  ],
 ),
 dict(name="Rotary Phone Intercom", kind="Gadget",
  desc="An intercom built from vintage rotary phones.",
  videos=[
   "0nVkSxVJ2kk",  # 2022-11-04 I built an intercom from vintage rotary phones!
  ],
 ),
 dict(name="Soviet CRT Restorations", kind="Restoration",
  desc="Restoring a Soviet CRT television, getting Blade Runner onto it, and a Soviet CRT TV tester.",
  videos=[
   "MeNos5iXU5M",  # 2021-12-15 CRT Television Restoration, from the USSR!
   "Beup4VngfO0",  # 2022-05-08 CRT Restoration - How to get Blade Runner onto a Soviet Television
   "0cmK5fj6JsM",  # 2022-07-25 Soviet CRT TV tester — restoration and upgrades!
  ],
 ),
 dict(name="Retro Console Restoration", kind="Restoration",
  desc="Restoring a Video Sport 3 retro gaming console.",
  videos=[
   "9mqXT-zj47s",  # 2021-09-16 Retro Gaming Console Restoration! — Video Sport 3
  ],
 ),
 dict(name="Nixie Calculator Restoration", kind="Restoration",
  desc="Restoring an Iskra-121 Nixie tube calculator.",
  videos=[
   "ie-7WZTl4DA",  # 2022-01-26 Nixie Тube Calculator Restoration! — Искра-121
  ],
 ),
 dict(name="Flip Clock Repair", kind="Restoration",
  desc="Repairing an Emes Selecta flip clock and restoring its plastic.",
  videos=[
   "zx_TmIvfRvA",  # 2022-02-21 Flip Clock Repair and Plastic Restoration! — Emes Selection
  ],
 ),
 dict(name="Scientific Calculator Restoration", kind="Restoration",
  desc="Restoring a scientific calculator's display.",
  videos=[
   "FJMVs7ldxNA",  # 2022-06-25 Scientific calculator restoration! Will her display shine again?
  ],
 ),
 dict(name="Variac Upgrade", kind="Restoration",
  desc="Restoring and upgrading a variac transformer.",
  videos=[
   "2WKiUnRqCc8",  # 2022-07-17 Restoring and Upgrading a Variac Transformer!
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
