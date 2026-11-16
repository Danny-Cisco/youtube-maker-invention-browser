"""Curated projects for CNC Kitchen (Stefan Hermann, @cnckitchen). A 3D-printing testing channel: listed are the techniques and builds he developed or tested in depth; reviews stay under Other uploads.
kind: Technique | Recycling | Build

Each invention lists its YouTube video IDs (title in the trailing comment). Every upload not
listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'cnc-kitchen', 'name': 'CNC Kitchen', 'person': 'Stefan Hermann', 'tagline': '3D-printing science: gradient infill, brick layers, annealing and turning waste back into filament.', 'other_label': 'Other uploads: reviews, strength tests, trade-show tours and guides'}

INVENTIONS = [
 dict(name="3D Printed RC Airplane", kind="Build",
  desc="How to 3D print your own RC airplane.",
  videos=[
   "Ztygn--BsjI",  # 2018-05-20 HOW TO 3D PRINT your own RC AIRPLANE
  ],
 ),
 dict(name="Filament Recycling", kind="Recycling",
  desc="Recycling failed prints into new filament, all his Benchys, PET bottle filament, and a DIY recycling setup.",
  videos=[
   "vqWwUx8l_Io",  # 2018-11-10 Recycle your failed 3D prints! Make new filament at home.
   "Dwlr2yKlq6w",  # 2021-07-10 Recycling all my 3DBenchys into new Filament
   "N06FWr06iOI",  # 2022-01-22 HOW STRONG is PET Bottle Filament?
   "1yIe1Pp_Nrg",  # 2023-09-16 PET Bottle Recycling: Waste to 3D Printing Filament
   "O6d1RKYapFI",  # 2023-11-04 Turning 3D Print Waste into New Filament!
   "BT04glGDjB4",  # 2023-12-09 Recycling Failed 3D Prints with a DIY Filament Extruder: Artme3D
  ],
 ),
 dict(name="3D Printed Knife Sharpener", kind="Build",
  desc="Perfectly sharp knives with a 3D-printed sharpener.",
  videos=[
   "IM2il-zT2fA",  # 2019-05-18 PERFECTLY sharp knifes! 3D PRINTED sharpening tool 🍴
  ],
 ),
 dict(name="Gradient Infill", kind="Technique",
  desc="Gradient infill: a new efficient infill.",
  videos=[
   "hq53gsYREHU",  # 2020-01-11 Gradient Infill - NEW efficient infill for 3D prints!
  ],
 ),
 dict(name="Annealing & Remelting for Strength", kind="Technique",
  desc="Tripling layer strength by annealing, and prints remelted in salt.",
  videos=[
   "bG8dlxTX3AI",  # 2020-09-19 Triple (x3) your Layer Strength by Annealing 3D Prints in Plaster!
   "DyAKtS1b3SQ",  # 2020-10-24 The STRENGTH of 3D prints REMELTED in SALT
  ],
 ),
 dict(name="Trimmer Line & Hot Glue Printing", kind="Technique",
  desc="Can you 3D print with trimmer line, or hot glue?",
  videos=[
   "XsrkFIuQEZM",  # 2020-11-14 Can you 3D Print with Trimmer Line?!
   "alwsRqh5W8M",  # 2024-03-23 Can you 3D Print with Hot Glue?
  ],
 ),
 dict(name="Bi-Metallic Heat Breaks & High-Flow Nozzles", kind="Technique",
  desc="Bi-metallic heat breaks and his own high-flow nozzle.",
  videos=[
   "xAiUZ7HDhdM",  # 2021-02-20 Bi-Metallic Heat Breaks - A (R)Evolution?!
   "UNJdv5bFGOg",  # 2021-10-23 Does This make Volcano Hotends Obsolete? Bondtech CHT Review
   "RWDErj-pE1c",  # 2021-11-20 My High Flow Nozzle is better than a Volcano hotend!
  ],
 ),
 dict(name="Mini Open-Source CoreXY", kind="Build",
  desc="A mini, fast, open-source CoreXY printer.",
  videos=[
   "4VSu_gG-nlk",  # 2021-03-13 Mini, Fast & Open-Source Core XY - The VORON 0
  ],
 ),
 dict(name="Texturing for Strength", kind="Technique",
  desc="Texturing prints for strength, and an alternative to fuzzy skin.",
  videos=[
   "3-ygdNQThAs",  # 2021-04-24 Texturing 3D Prints for Strength!
   "rTBkjR7JvzI",  # 2026-04-04 Stop Using Fuzzy Skin - I made something better!
  ],
 ),
 dict(name="Micro 3D Printing", kind="Technique",
  desc="Micro 3D printing with a 0.1 mm nozzle.",
  videos=[
   "ngpw0ojHODA",  # 2021-11-06 MICRO 3D Printing with a 0.1 mm nozzle
  ],
 ),
 dict(name="Transparent FDM Prints", kind="Technique",
  desc="Clear transparent FDM prints.",
  videos=[
   "9qb25Gi4Jv0",  # 2022-09-10 Transparent FDM 3D Prints are Clearly Stronger!
  ],
 ),
 dict(name="Non-Planar & Conical Slicing", kind="Technique",
  desc="4-axis non-planar printing and conical slicing.",
  videos=[
   "7LRWuccMGjc",  # 2022-10-08 Impressive 4-Axis Non-Planar 3D Printing
   "1i-1TEdByZY",  # 2022-11-12 Conical Slicing: A different angle of 3D printing
  ],
 ),
 dict(name="Arc Overhangs", kind="Technique",
  desc="Arc overhangs that make supports obsolete.",
  videos=[
   "B0yo-o47688",  # 2022-12-10 Arc Overhangs make Supports Obsolete!
  ],
 ),
 dict(name="Brick Layers", kind="Technique",
  desc="Brick layers: why did no one do this before?",
  videos=[
   "5hGm6cubFVs",  # 2024-02-17 Brick Layers - Why did no one do this before?
  ],
 ),
 dict(name="Solid-State Dehumidifier", kind="Build",
  desc="The ultimate solid-state filament dehumidifier.",
  videos=[
   "n7EWexck8NE",  # 2024-02-24 Solid-State Dehumidifier: The Ultimate Filament Dry Box
  ],
 ),
 dict(name="Custom Filament", kind="Recycling",
  desc="Making custom 3D-printing filament.",
  videos=[
   "CQ-N1fr4N0w",  # 2024-04-20 I made custom 3D printing filament with my Logo inside!
  ],
 ),
 dict(name="Injection Molding With a 3D Printer", kind="Technique",
  desc="Injection moulding using a 3D printer.",
  videos=[
   "4xXs9go-Ieg",  # 2024-06-22 I tried Injection Molding using a 3D Printer!
  ],
 ),
 dict(name="45\u00b0 Printing", kind="Technique",
  desc="The 45° secret for stronger prints.",
  videos=[
   "7aJ4dDyyf20",  # 2025-10-26 Stop Printing Flat: The 45° Secret for Stronger Parts
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
