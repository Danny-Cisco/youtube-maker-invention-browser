"""Inventions of Samy Kamkar. Hand-grouped and hand-reviewed: every upload was read and labelled
(invention / repair / tutorial / workshop / other, see data/review/). Only things the maker designed and made are
listed here; every other upload appears under "Other uploads"."""

CREATOR = {'slug': 'samy-kamkar', 'name': 'Samy Kamkar', 'person': 'Samy Kamkar', 'tagline': 'Hardware hacking and experiments, from lasers to sputter chambers.', 'other_label': 'Other uploads: Shorts, updates and other videos'}

INVENTIONS = [
 dict(name="SkyJack", kind="Drone hack",
  desc="An autonomous drone that hunts and takes over other drones, built on a Raspberry Pi.",
  videos=[
   "EHKV01YQX_w",  # 2013-12-03 SkyJack - autonomous drone hacking w/Raspberry Pi, aircrack & Javascri
  ],
 ),
 dict(name="Digital Ding Dong Ditch", kind="Hack",
  desc="Hacking wireless doorbells with an Arduino and an RTL-SDR.",
  videos=[
   "BnwBdeQB7vQ",  # 2014-12-11 Digital Ding Dong Ditch Prank - hacking wireless doorbells w/Arduino a
  ],
 ),
 dict(name="USBdriveby", kind="Hack",
  desc="A USB device that exploits a computer in seconds.",
  videos=[
   "aSLEq7-hlmo",  # 2014-12-17 USBdriveby - exploiting USB in style
  ],
 ),
 dict(name="KeySweeper", kind="Hack",
  desc="A covert wireless keyboard sniffer disguised as a USB charger.",
  videos=[
   "WqkmGG0biXc",  # 2015-01-12 KeySweeper - covert Microsoft wireless keyboard sniffer using Arduino 
  ],
 ),
 dict(name="Combo Breaker", kind="Machine",
  desc="A motorised device that cracks Master combination locks.",
  videos=[
   "YcpSvHpbHQ4",  # 2015-05-14 Combo Breaker - motorized combo lock cracking device
  ],
 ),
 dict(name="OpenSesame", kind="Hack",
  desc="Opening fixed-code garages in seconds with a hacked Mattel toy.",
  videos=[
   "iSSRaIU9_Vc",  # 2015-06-04 OpenSesame - hacking garages in seconds using a Mattel toy
  ],
 ),
 dict(name="OwnStar", kind="Hack",
  desc="A device that locates, unlocks and starts OnStar cars.",
  videos=[
   "3olXUbS-prU",  # 2015-07-30 OwnStar - hacking cars with OnStar to locate, unlock and remote start 
  ],
 ),
 dict(name="MagSpoof", kind="Hack",
  desc="A magnetic-stripe spoofer that emulates credit cards wirelessly.",
  videos=[
   "UHSFf0Lz1qc",  # 2015-11-24 MagSpoof - magnetic stripe spoofer / credit card magstripe emulator
  ],
 ),
 dict(name="PoisonTap", kind="Hack",
  desc="A Raspberry Pi Zero that hijacks locked computers.",
  videos=[
   "Aatp5gCskvk",  # 2016-11-16 PoisonTap - exploiting locked machines w/Raspberry Pi Zero
  ],
 ),
 dict(name="Sputter Chamber", kind="Machine",
  desc="A homemade sputter chamber, first test.",
  videos=[
   "yL4SHtTE3Ik",  # 2020-01-19 Sputter chamber v1; first test
  ],
 ),
 dict(name="ESP32 Self-Balancing Cube", kind="Robot",
  desc="A cube that balances on its corner.",
  videos=[
   "ol9q6mtPqq4",  # 2026-07-13 ESP32 self balancing cube
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
