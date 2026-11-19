"""Curated inventions for Shawn Hymel (@shawnhymel).

Drafted by build/auto_inventions.py (builds grouped by shared key words, livestreams included, descriptions in the
maker's own words). Every upload not listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'shawn-hymel', 'name': 'Shawn Hymel', 'person': 'Shawn Hymel', 'tagline': 'Embedded machine learning and small robots.', 'other_label': 'Other uploads: Shorts, updates and other videos'}

INVENTIONS = [
 dict(name="Micro:bit Tutorial Series", kind="Build",
  desc="Get started using the micro:bit with BBC's online MicroPython code editor.",
  videos=[
   "ZIW_6rxYNBg",  # 2016-08-15 micro:bit Tutorial Series Part 1: Getting Started
   "XMr6Fg74fZY",  # 2016-08-29 micro:bit Tutorial Series Part 2: Images, Buttons, and Conditionals
  ],
 ),
 dict(name="How to Create a Web Server Using an ESP32 in Arduino", kind="Build",
  desc="Note that we use the ESP32 as an access point (AP) here to simplify the process.",
  videos=[
   "ZbX-l1Dl4N4",  # 2018-11-01 How to Make an Arduino WebSocket Server with an ESP32
   "mkXsmCgvy0k",  # 2019-09-09 How to Create a Web Server (with WebSockets) Using an ESP32 in Arduino
  ],
 ),
 dict(name="Hack a Pumpkin", kind="Build",
  desc="Hack a Pumpkin: Spoopy Poopy, the Gaseous Gourd.",
  videos=[
   "IYvLr-H5bME",  # 2019-10-28 Hack a Pumpkin: Spoopy Poopy, the Gaseous Gourd
  ],
 ),
 dict(name="Getting Started with Mozilla WebThings", kind="Build",
  desc="Mozilla (the makers of Firefox) have created a custom Internet of Things (IoT) hub that can run on a single-board computer (SBC).",
  videos=[
   "WHite8vdcbE",  # 2019-12-20 Getting Started with Mozilla WebThings Part 1: Setup on a Raspberry Pi
   "papxaeII0vo",  # 2019-12-23 Getting Started with Mozilla WebThings Part 2: Building an ESP8266 Tem
  ],
 ),
 dict(name="ESP32 - Getting Started with ESP-IDF", kind="Build",
  desc="I'll show you how to get started with the Espressif IoT Development Framework (ESP-IDF), the official Espressif toolset for building professional, production-ready firmware for the ESP32.",
  videos=[
   "h7VfpoJvIpg",  # 2025-08-12 ESP32 - Getting Started with ESP-IDF
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
