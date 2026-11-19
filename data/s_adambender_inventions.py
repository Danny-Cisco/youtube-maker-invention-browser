"""Inventions of Adam Bender. Hand-grouped and hand-reviewed: every upload was read and labelled
(invention / repair / tutorial / workshop / other, see data/review/). Only things the maker designed and made are
listed here; every other upload appears under "Other uploads"."""

CREATOR = {'slug': 'adam-bender', 'name': 'Adam Bender', 'person': 'Adam Bender', 'tagline': 'Engineering and science builds made to promote education.', 'other_label': 'Other uploads: Shorts, updates and other videos'}

INVENTIONS = [
 dict(name="Homemade CNC Machine", kind="Machine",
  desc="A homemade CNC machine, engraving.",
  videos=[
   "axLIIfqhN_U",  # 2012-11-07 Homemade CNC Machine Engraving
   "hKbwETd0xQw",  # 2012-11-07 DIY CNC Quick look at engraving
  ],
 ),
 dict(name="Delta 3D Printer", kind="Machine",
  desc="A delta printer he built, testing its kinematics.",
  videos=[
   "4fh7HhWTf0w",  # 2013-08-20 Delta Printer in Action, Testing Kinematics
  ],
 ),
 dict(name="One-Wheel Balancing Robot", kind="Robot",
  desc="A robot that balances on one wheel.",
  videos=[
   "I-xwtTATRLM",  # 2014-07-31 One Wheel Balancing Robot
  ],
 ),
 dict(name="Epoxy Granite Machine Base", kind="Shop build",
  desc="An epoxy-granite base for a machine.",
  videos=[
   "4aBVAbfxLJw",  # 2019-05-25 How to Build Epoxy Granite Machine Base
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
