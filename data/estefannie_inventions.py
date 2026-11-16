"""Curated inventions for Estefannie (@estefannie).
kind: Robot | Gadget | Wearable

Each invention lists its YouTube video IDs (title in the trailing comment). Every upload not
listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'estefannie', 'name': 'Estefannie', 'person': 'Estefannie', 'tagline': 'Software engineer making a robot with anxiety, an AI litterbox and a Daft Punk helmet.', 'other_label': 'Other uploads: early computer-science lessons and Shorts'}

INVENTIONS = [
 dict(name="Daft Punk Helmet", kind="Wearable",
  desc="A 3D-printed Daft Punk helmet in three parts.",
  videos=[
   "slq8gh6M62U",  # 2018-06-15 How to make a 3D Printed Daft Punk Helmet 1 // MAKE SOMETHING
   "gU3bOE3rxOI",  # 2018-07-03 How to make a 3D Printed Daft Punk Helmet 2 // MAKE SOMETHING
   "NLSYOH14mAs",  # 2018-08-02 How to make a 3D Printed Daft Punk Helmet 3 // MAKE SOMETHING
  ],
 ),
 dict(name="Instagram Like Light", kind="Gadget",
  desc="A light that reacts to Instagram likes.",
  videos=[
   "aNKmiXIaMiI",  # 2019-12-22 Making a light work with Instagram likes
  ],
 ),
 dict(name="Robot With Anxiety", kind="Robot",
  desc="A robot with depression and anxiety.",
  videos=[
   "AO4P768-GCo",  # 2020-12-23 I BUILT A ROBOT WITH DEPRESSION AND ANXIETY
  ],
 ),
 dict(name="Tarot Video Game", kind="Gadget",
  desc="A tarot video game that tells your future.",
  videos=[
   "UZfD8xsISR0",  # 2021-12-23 I made a tarot video game that tells you your future
  ],
 ),
 dict(name="AI Litterbox", kind="Gadget",
  desc="An AI litterbox trained on 5,000 pictures.",
  videos=[
   "6jDDZjSyXpc",  # 2022-08-28 I made an ai litterbox with 5000 pictures of poop
  ],
 ),
 dict(name="AI Microwave", kind="Gadget",
  desc="An AI microwave.",
  videos=[
   "BDSZU3YZNPs",  # 2025-03-18 I made an ai microewe
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
