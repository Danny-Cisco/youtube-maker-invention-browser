"""Inventions of Les' Lab. Hand-grouped and hand-reviewed: every upload was read and labelled
(invention / repair / tutorial / workshop / other, see data/review/). Only things the maker designed and made are
listed here; every other upload appears under "Other uploads"."""

CREATOR = {'slug': 'les-lab', 'name': "Les' Lab", 'person': "Les' Lab", 'tagline': 'Amateur science: home-made lasers, electronics and computers.', 'other_label': 'Other uploads: Shorts, updates and other videos'}

INVENTIONS = [
 dict(name="Homemade TEA Nitrogen and Dye Laser", kind="Laser",
  desc="A high-performance home-made TEA nitrogen laser driving a home-made dye laser, and how it's built.",
  videos=[
   "US3vLJIUGoU",  # 2020-07-04 Nitrogen Laser tear down, power up, and Home Made Dye Laser Demonstrat
   "pCnXftuJ9Zo",  # 2020-08-06 DIY Home made High Performance TEA Nitrogen Laser and Dye Laser!
   "AyN1o_3XaTw",  # 2020-08-11 Tear down of the DIY  High Performance TEA Nitrogen Laser, how to buil
  ],
 ),
 dict(name="Tunable Dye Laser", kind="Laser",
  desc="A DIY tunable dye laser.",
  videos=[
   "q9zQ3_Kjxd8",  # 2020-09-05 DIY Tunable Dye Laser!
   "-ny_-Y1MpRY",  # 2020-09-06 DIY Tunable Dye Laser! (HD 60FPS re-encoded video)
   "ERNVgGmjALY",  # 2020-09-23 Dye Laser Teardown and Demonstration
  ],
 ),
 dict(name="30 kV ZVS Power Supply", kind="Electronics",
  desc="A home-made 30 kV ZVS high-voltage supply.",
  videos=[
   "GbQEan4gwWM",  # 2020-09-14 Home Made 30 kV ZVS High Voltage Power Supply and Tear-down
  ],
 ),
 dict(name="HeNe Laser Power Supply", kind="Electronics",
  desc="A DIY helium-neon laser power supply.",
  videos=[
   "ZYzuInzSt7Y",  # 2020-11-03 How to build a DIY  Helium Neon laser power supply
  ],
 ),
 dict(name="Inexpensive Nitrogen Laser Capacitors", kind="Electronics",
  desc="Cheap home-made capacitors for nitrogen lasers.",
  videos=[
   "8wUxYVe98Uo",  # 2020-12-22 How to make Inexpensive Nitrogen Laser Capacitors!
   "NEHiv4lv68U",  # 2021-02-13 Wire Ended to Doorknob Capacitor Modification (Inexpensive Nitrogen La
  ],
 ),
 dict(name="MNL-100 Fibre-Optic Interface", kind="Mod",
  desc="An RS-232 fibre-optic interface hack for an MNL-100 nitrogen laser.",
  videos=[
   "k5MOAKHPVG8",  # 2021-01-13 Hacking a Laser! MNL-100 Nitrogen Laser RS-232 Fibre Optic Interface H
  ],
 ),
 dict(name="Raspberry Pi Spectrometer", kind="Instrument",
  desc="A DIY spectrometer on a Raspberry Pi with a PiCamera, through a miniature version and new software.",
  videos=[
   "T_goVwwxKE4",  # 2021-04-17 How to build a DIY Raspberry Pi Spectrometer using a Picamera and Spec
   "dm3woVQp8Xc",  # 2021-05-03 How to build a DIY Raspberry Pi Spectrometer. Part 2, Software update 
   "vEqj33MGwmc",  # 2021-05-16 How to measure Dye Laser Tuning curves with a  DIY Raspberry Pi Spectr
   "Tw3HJEhE2dI",  # 2021-06-20 How to build a MINIATURE Spectrometer  for the Raspberry Pi
   "jAV7bnNrE-M",  # 2021-10-31 Raspberry Pi Zero 2 W Spectrometer!
   "SCp9T8NKfnM",  # 2022-10-22 DIY Raspberry Pi Spectrometer NEW SOFTWARE!
  ],
 ),
 dict(name="Barcode Scanner Laser Show", kind="Mod",
  desc="Barcode scanners hacked into a laser light show.",
  videos=[
   "Em6pVB7z9lA",  # 2021-06-15 Laser Barcode Scanner Teardown How to hack it into Laser Light Show!
   "O6eFNKaFXCk",  # 2021-07-03 Supermarket Barcode Scanner Teardown and hack!
  ],
 ),
 dict(name="Acousto-Optic Controller", kind="Electronics",
  desc="A home-made acousto-optic controller for under $100.",
  videos=[
   "iOB8jyYetvw",  # 2021-09-06 Homemade Acousto-optic controller for Under $100!
  ],
 ),
 dict(name="Integrating Sphere", kind="Instrument",
  desc="A home-made integrating (Ulbricht) sphere.",
  videos=[
   "BtMqx5P74n4",  # 2022-02-05 Home Made Integrating or Ulbricht Sphere
  ],
 ),
 dict(name="Triggered Spark Gap", kind="Electronics",
  desc="A triggered spark gap for high-voltage lasers and Marx generators.",
  videos=[
   "ma-xpn1WPuI",  # 2022-03-12 How to make a Triggered Spark Gap for High Voltage Lasers and Marx Gen
  ],
 ),
 dict(name="10W Laser Diode Power Supply", kind="Electronics",
  desc="A high-power laser diode power supply.",
  videos=[
   "WQhi3bTNnF4",  # 2022-05-11 High Power Laser Diode Power Supply 10W and Laser Safety
  ],
 ),
 dict(name="Industrial CO2 Coder to Engraver", kind="Mod",
  desc="An industrial CO2 laser coder repaired and hacked into an engraver.",
  videos=[
   "_i1J7TGpPnQ",  # 2022-06-10 Industrial CO2 Laser Coder TEARDOWN and repair! Part 1!
   "w4mWgVDPIiQ",  # 2022-07-13 CO2 Laser Engraver. Industrial Laser Coder Hacked! Part 2!
  ],
 ),
 dict(name="1 GHz Tektronix Scope Hack", kind="Mod",
  desc="Hacking a Tektronix oscilloscope up to 1 GHz.",
  videos=[
   "pZWq-u2lOu8",  # 2023-02-26 Hacking a Tektronix Oscilloscope to1GHz!
  ],
 ),
 dict(name="DIY Raman Laser", kind="Laser",
  desc="A Raman laser made by shaking molecules until laser light comes out.",
  videos=[
   "L6JiVzpxVc8",  # 2023-12-09 Shaking molecules until Laser Light comes out. DIY Raman Laser!
  ],
 ),
 dict(name="Home-Grown Crystal Light Modulator", kind="Instrument",
  desc="Controlling light with a crystal he grew himself.",
  videos=[
   "RxjqMh3gkx8",  # 2025-06-25 Controlling Light with a Home-Grown Crystal
  ],
 ),
 dict(name="High-Current Trigger Transformer", kind="Electronics",
  desc="A trigger transformer that survives hundreds of amps.",
  videos=[
   "C_Ci-ufpkdM",  # 2026-06-30 A Trigger transformer that survives HUNDREDS of Amps!
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
