"""Curated builds for Made with Layers (Thomas Sanladerer, @madewithlayers). A 3D-printing tutorial and review channel; only builds are listed.
kind: Build | Technique

Each invention lists its YouTube video IDs (title in the trailing comment). Every upload not
listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'made-with-layers', 'name': 'Made with Layers', 'person': 'Thomas Sanladerer', 'tagline': '3D-printing explainer who also built a CNC mill from a printer and a budget Prusa.', 'other_label': 'Other uploads: guides, reviews and 3D-printing explainers'}

INVENTIONS = [
 dict(name="CNC Mill From a 3D Printer", kind="Build",
  desc="A CNC mill built from a 3D printer.",
  videos=[
   "MDz1A1XDOt8",  # 2017-01-12 CNC mill built from a 3D Printer!
  ],
 ),
 dict(name="Cheapest Possible Prusa", kind="Build",
  desc="Building the cheapest possible Prusa.",
  videos=[
   "oVWLpvekby0",  # 2017-02-23 Building the cheapest possible Prusa i3 MK2 clone: [01] Electronics an
  ],
 ),
 dict(name="Transparent 3D Prints", kind="Technique",
  desc="How to create transparent 3D prints.",
  videos=[
   "QkfQri2B0PY",  # 2017-04-29 How to create transparent 3D prints!
  ],
 ),
 dict(name="Topology-Optimised Shelves", kind="Technique",
  desc="Making strong shelves with topology optimisation.",
  videos=[
   "3smr5CEdksc",  # 2019-07-26 Making STRONG shelves with Topology Optimization
  ],
 ),
 dict(name="Digital Dashboard", kind="Build",
  desc="A digital dashboard.",
  videos=[
   "BR_yko0gr-Y",  # 2019-09-19 Making a Digital Dashboard! (w/ Google Calendar integration)
  ],
 ),
 dict(name="Crisp PCBs Fast", kind="Technique",
  desc="The fastest way to make crisp PCBs at home.",
  videos=[
   "RudStbSApdE",  # 2021-12-27 The fastest way to make crisp PCBs at home!
  ],
 ),
 dict(name="Toy Printer Upgrades", kind="Build",
  desc="How far he could upgrade a toy 3D printer.",
  videos=[
   "D4m5dA50QYE",  # 2024-06-08 How far can I upgrade this toy 3D printer?
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
