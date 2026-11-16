"""Curated inventions for Integza (@integza). Builds are grouped by engine type using title patterns; Shorts stay under Other uploads.
kind: Rocket engine | Jet engine | Turbine | Engine | Gadget

Each invention lists its YouTube video IDs (title in the trailing comment). Every upload not
listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'integza', 'name': 'Integza', 'person': 'Integza', 'tagline': '3D-printed rocket engines, pulsejets and Tesla turbines, mostly working.', 'other_label': 'Other uploads: early science explainers, Shorts and odds and ends'}

INVENTIONS = [
 dict(name="Tesla Turbines", kind="Turbine",
  desc="3D-printed Tesla turbines, from v1 and v2 to a turbine boat, a golden-ratio turbine, a WWII V2 steam turbine and a turbine skateboard.",
  videos=[
   "bDUw91GEg7Q",  # 2018-10-07 Tesla Turbine [3D Printed]
   "Y9OwuECp6AA",  # 2018-10-21 DIY Digital Tachometer - Arduino|Photointerrupter  [Tesla Turbine]
   "n5KmpFRSXiA",  # 2019-02-02 Tesla Turbine v2.0 [3D Printed]
   "qL3kCawHMqk",  # 2020-03-20 Tesla Turbine [Smoke Flow Slow Mo]
   "BxNHOMJGcj0",  # 2020-08-07 Golden Ratio Turbine 3D Printed
   "CWWKcuVKErI",  # 2020-08-28 Tesla Turbine Boat 3D Printed (Lily Impeller)
   "RExAzZ9xNf0",  # 2021-11-30 Hyper Jet Steam Turbine (3D Printed)
   "A1H2mFEsbNk",  # 2022-04-06 I built the World War II V2 Rocket Steam Turbine
   "Tuzh9mHvzkk",  # 2023-07-31 Building Nikola Tesla's Bladeless Turbine
   "133es4O0AkE",  # 2024-03-20 I built a TURBINE Skateboard
  ],
 ),
 dict(name="Tesla Valve & Earthquake Machine", kind="Engine",
  desc="Nikola Tesla inventions, 3D printed: the Tesla valve, earthquake machine and a wireless-power Tesla coil.",
  videos=[
   "eBlI6OQ-i3s",  # 2019-01-09 3D Printing a 106 Years Old Invention - Testing the DT2234C
   "ct0tljBtjG0",  # 2019-05-26 Tesla Valve 3D Printed
   "l5rEW9QgJDc",  # 2019-09-29 Tesla Earthquake Machine [3D Printed]
   "ZITh9C_7hbg",  # 2020-02-08 Tesla Coil - Wireless Power Machine 3D Printed (ft .Plasma Channel)
  ],
 ),
 dict(name="Pulsejet Engines", kind="Jet engine",
  desc="Valveless and Tesla-valve pulsejets, 3D printed, then turbocharged, on a bicycle and with no moving parts.",
  videos=[
   "28XbT11lL24",  # 2019-12-22 Tesla Pulsejet Engine [3D Printed]
   "tI5ljulY-Xw",  # 2020-04-27 Tesla Pulsejet Valve (3D Printed)
   "GzHIrAapiFg",  # 2020-09-30 ThermoJet Engine 3D Printed (PulseJet)
   "QFKWZHB8-FQ",  # 2020-11-18 Cylindrical Tesla Valve Pulse Jet Engine (3D Printed)
   "YcmGN_c2Aq0",  # 2021-01-29 TurboCharged PulseJet Engine (3D Printed)
   "I7hsUvZmZ2k",  # 2023-09-30 JET ENGINE with NO MOVING PARTS (Pulsejet Engine)
  ],
 ),
 dict(name="Jet Engines", kind="Jet engine",
  desc="Turbojets in plastic and carbon fibre, plus turning a fan, a Dyson fan, Dyson and $20 hairdryers into jet engines, an electric jet engine and a levitating one.",
  videos=[
   "hk-fXjkV0ho",  # 2020-10-31 Carbon Fiber Jet Engine
   "qsvpU7G5IJg",  # 2021-02-28 TurboJet Engine (3D Printed)
   "C2OmUBpn66k",  # 2021-08-31 I turned my Fan into a Jet Engine (3D Printed EDF Afterburner)
   "jbXJa8osys0",  # 2022-01-26 I turned my Dyson Fan into a Bladeless Jet Engine
   "bha6yZsS7oY",  # 2022-02-28 I built an Electric Jet Engine from scratch
   "EOx9D6Zb__8",  # 2022-05-06 I put a Homemade Jet Engine on my Bicycle
   "FGGw-5dfNiM",  # 2022-05-26 Water-Cooled Jet Engine in Plastic
   "1zSU2kLLXQY",  # 2023-04-06 I turned my DYSON HAIRDRYER into a JET ENGINE
   "fwKuCoL9FlM",  # 2024-04-13 I Built a JET POWERED KNIFE
   "o-G45OOb32A",  # 2024-06-05 I turned my $20 Hairdryer into a JET ENGINE
   "viEYJnKVND4",  # 2026-04-17 I Built a LEVITATING JET ENGINE
  ],
 ),
 dict(name="Rocket Engines", kind="Rocket engine",
  desc="Dozens of rocket engines: aerospikes, vortex-cooled ceramic, metal-plated, self-consuming, glass, laminar-flow, venturi, water-burning, AI-designed, and finally a liquid rocket engine.",
  videos=[
   "1p-XWqYHez4",  # 2020-11-30 Aerospike Rocket Engine (3D Printed)
   "Qu79vUbcXCU",  # 2020-12-30 Vortex Cooled Ceramic Rocket Engine (3D Printed)
   "wQ8cIOtT3ug",  # 2021-03-16 Vortex Rocket V2.0 (3D Printed)
   "_Fw4CbsqCcM",  # 2021-03-31 Metal Plated Ceramic Rocket Engine (3D Printed)
   "bsmBur9iVxg",  # 2021-04-15 Rocket engine that uses itself as fuel! (3D Printed)
   "1sSkLdiiJoY",  # 2021-05-03 Aerospike Hybrid Rocket Engine (3D printed)
   "BBVHqDZwLwM",  # 2021-07-15 Water Rocket Skateboard (3D Printed)
   "tw9VF1V-Lzc",  # 2021-07-30 How I 3D Printed a Metal Aerospike Rocket at Home
   "mJJ1InbjkTk",  # 2021-08-15 The Forgotten Nazi Cold Rocket Engine (3D Printed)
   "vVven2CPaaw",  # 2021-09-30 Devil's Toothpaste Rocket Engine (3D Printed)
   "eYunjX5jLg0",  # 2021-10-15 I 3D printed a CO2 Rocket
   "fE8NJdfW8DY",  # 2021-11-03 GYROJET - The Spinning Rocket Bullet
   "ri-Jx5eeVIo",  # 2021-11-17 I turned Tomatoes into Rocket Propellant
   "0kPgw_S_pS4",  # 2021-12-31 I built a PULSED ROCKET ENGINE
   "pigwLELjaVw",  # 2022-11-26 I tested ALL the ROCKET PROPELLANTS I could find online
   "eHRyv7ARb5M",  # 2022-12-30 ELECTRIC SOLID PROPELLANTS
   "A6AZ1-msoyA",  # 2023-11-02 GLASS ROCKET ENGINE
   "nYUiOIrEY24",  # 2024-01-04 SUPER HEATED STEAM ROCKET ENGINE
   "1lvZNK9KyK8",  # 2024-02-17 How I made 100% PURE NITROGLYCERIN
   "7O2MZr9B9XM",  # 2024-07-15 ROCKET that LITERALLY BURNS WATER as FUEL
   "MWoFFoaL5aw",  # 2024-09-07 I Built The First LAMINAR FLOW ROCKET ENGINE
   "qyKideyU64c",  # 2025-05-24 I Built a ROCKET PROPELLER
   "qY9fpU8Vpig",  # 2025-12-11 I Built the FIRST VENTURI ROCKET ENGINE
   "6Xx1GXjRbMk",  # 2025-12-19 This ROCKET ENGINE WASN'T DESIGNED BY HUMANS
   "PsDpDB3neng",  # 2026-06-20 HYPERGOLIC : The Most FEARED WORD in ROCKET SCIENCE
   "Zb7YOf1aPnM",  # 2026-08-23 I built a VARIABLE ROCKET NOZZLE
   "1ZCKszfKBOE",  # 2026-11-03 I FINALLY BUILT a LIQUID ROCKET ENGINE!
  ],
 ),
 dict(name="Detonation Engines", kind="Engine",
  desc="Pulsed and rotating detonation engines.",
  videos=[
   "12NZCxUrMZQ",  # 2022-08-26 PULSED DETONATION ENGINE
   "fRMMSyCcTDI",  # 2022-09-27 ROTATING DETONATION ENGINE
  ],
 ),
 dict(name="Wankel & Rotary Engines", kind="Engine",
  desc="A compressed-air triangular Wankel engine, a Wankel RC car and a new rotary flap engine.",
  videos=[
   "b399G61Z3fo",  # 2021-05-15 Compressed Air Triangular Engine - Wankel Rotary (3D Printed)
   "ReK0r9OdCes",  # 2021-05-30 Rotary Wankel RC Car (3D Printed)
   "udI2dWmwMUE",  # 2024-12-15 I built a FLAP ENGINE (New Rotary Design)
  ],
 ),
 dict(name="Steam & Stirling Engines", kind="Engine",
  desc="A Stirling hot-air engine car, a 3D-printed steam engine and a magnetic air engine.",
  videos=[
   "lmncBzb2Xbg",  # 2020-06-20 Hot Air Engine Car (Stirling Engine 3D Printed)
   "DmOL2oB1d6w",  # 2021-12-15 STEAM ENGINE (3D PRINTED)
   "fE_LjQ4IBQQ",  # 2023-09-03 Magnetic Air Engine
  ],
 ),
 dict(name="Liquid Piston & Transparent Engines", kind="Engine",
  desc="A liquid piston engine, a transparent combustion engine and a tiny nitro engine on a bicycle.",
  videos=[
   "cBRo1uH5H6Y",  # 2022-06-30 I 3D Printed a Transparent Combustion Engine in Resin
   "eTaosDKHec0",  # 2022-07-30 I 3D Printed a Liquid Piston Engine
   "Yc17oucI6jM",  # 2023-07-07 THE LIQUID PISTON ENGINE
   "EXkV3dr5o94",  # 2024-01-31 Tiny 3.5 cc NITRO ENGINE on a BICYCLE
  ],
 ),
 dict(name="Ionic Plasma Thruster", kind="Engine",
  desc="An ionic plasma thruster (his most-watched video) and a toroid plasma reactor.",
  videos=[
   "mnCmvxt2jn8",  # 2023-08-15 I built an IONIC PLASMA THRUSTER (Best Design)
   "Rw3sfhW3Bt0",  # 2024-02-29 The Forgotten TOROID PLASMA REACTOR
  ],
 ),
 dict(name="Bladeless Fans", kind="Gadget",
  desc="A true bladeless fan and a 3D-printed electric motor fan.",
  videos=[
   "AJD_fiHleRM",  # 2022-10-31 I built a TRUE BLADELESS FAN
   "qhzhBDb9D7w",  # 2023-03-03 I 3D Printed an ELECTRIC MOTOR FAN
  ],
 ),
 dict(name="Wind & Water Rocket Vehicles", kind="Gadget",
  desc="A wind-powered car and a water-rocket skateboard.",
  videos=[
   "QHJka4_ZioU",  # 2021-06-30 Wind Powered Car (3D Printed)
  ],
 ),
 dict(name="Metal 3D Printer", kind="Gadget",
  desc="A metal 3D printer built from his welding machine.",
  videos=[
   "7w9hK8mh9-g",  # 2021-06-15 I built a Metal 3D Printer using my Welding Machine
  ],
 ),
 dict(name="Tools & Measuring Rigs", kind="Gadget",
  desc="A DIY Arduino tachometer and torquemeter for engine testing.",
  videos=[
   "NIpspXaPVcs",  # 2019-02-24 DIY Torquemeter - How to measure torque! [Arduino & 3D Printed]
  ],
 ),
 dict(name="Weapons", kind="Gadget",
  desc="A chain sword, a shotgun axe (twice) and a jet-powered knife.",
  videos=[
   "VxS9uVdvRgo",  # 2023-02-06 I built a CHAIN SWORD
   "_luBh6eFANU",  # 2025-03-06 I Built a SHOTGUN AXE
   "vICU4PTPbuo",  # 2025-09-30 I built a BETTER SHOTGUN AXE
  ],
 ),
 dict(name="Self-Punching Gaming Helmet", kind="Gadget",
  desc="A self-punching gaming helmet.",
  videos=[
   "oVpSxXS9Ftw",  # 2019-04-26 Self-Punching Gaming Helmet [Future Gadget #001]
  ],
 ),
 dict(name="3D-Printed Leg", kind="Gadget",
  desc="A 3D-printed leg for a Redditor.",
  videos=[
   "h975HYimtAc",  # 2019-08-20 I 3D Printed a Leg for a Redditor
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
