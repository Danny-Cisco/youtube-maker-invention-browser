"""Curated restorations for CuriousMarc (Marc Verdiell, @curiousmarc). He restores rather than invents; his long restoration series are grouped by machine.
kind: Space hardware | Computer | Instrument | Robot

Each invention lists its YouTube video IDs (title in the trailing comment). Every upload not
listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'curiousmarc', 'name': 'CuriousMarc', 'person': 'Marc Verdiell', 'tagline': 'Bringing historic machines back to life: the Apollo Guidance Computer, Soyuz Globus and vintage IBM.', 'other_label': 'Other uploads: one-off repairs, explainers, museum visits and teardowns'}

INVENTIONS = [
 dict(name="Apollo Guidance Computer", kind="Space hardware",
  desc="Restoring an Apollo Guidance Computer to run again, with core rope memory and fly-by-wire follow-ups.",
  videos=[
   "2KSahAoOLdU",  # 2018-11-14 Apollo Guidance Computer Part 1: Restoring the computer that put man o
   "9Ys-VshuOLQ",  # 2018-11-18 Apollo Guidance Computer Part 2: Power supplies test
   "vfUhF3BJoBc",  # 2018-11-27 Apollo Guidance Computer Part 3: Main Bus B Undervolt
   "qpDvp7puMBI",  # 2018-12-06 Apollo Guidance Computer Part 4: We are "go" for power up
   "OBVtB-Nt6Dw",  # 2018-12-07 Apollo Guidance Computer Part 4 ½: Bonus material, full Logic Analyzer
   "hEKdzpcbh-U",  # 2018-12-23 Apollo Guidance Computer Part 5: We run a chunk of original Apollo cod
   "GTJLaSJwjAg",  # 2019-01-18 Apollo Guidance Computer Part 6: Restoration update, a new sponsor, an
   "uyxQmb2u6Hk",  # 2019-03-13 Apollo Guidance Computer Part 7: Memory Module B12
   "ThOXgcOOA1M",  # 2019-04-05 Apollo Guidance Computer Part 8: a Blinkenlight AGC! (and help from Sa
   "lXe2OS4nwnQ",  # 2019-05-15 Apollo Guidance Computer Part 9: Apollo Gyroscope
   "RWkSH0wxy80",  # 2019-06-03 Apollo Guidance Computer Part 10: Mike flies Apollo 11’s P63, lunar la
   "is1b6mqzxFA",  # 2019-06-10 Apollo Guidance Computer Part 11: Samtec manufactures NASA-spec contac
   "ip5d7LSTb7Q",  # 2019-06-21 Apollo Guidance Computer Part 12: Return of the AGC
   "HpIwQZaEvV0",  # 2019-06-26 Apollo Guidance Computer Part 13: The AGC passes self test under emula
   "2qe4W_USweE",  # 2019-07-01 Apollo Guidance Computer Part 14: Bringing up fixed rope memory
   "NNlgJ52wuGE",  # 2019-07-02 Apollo Guidance Computer Part 14 ½: Bonus Material
   "fTbuPih0rOg",  # 2019-07-08 Apollo Guidance Computer Part 15: Recovering lost Apollo software at t
   "I7VLIjsKxkU",  # 2019-07-09 Apollo Guidance Computer Part 16: Digging into potted module B11
   "cPxaGrcimMQ",  # 2019-07-10 Apollo Guidance Computer Part 17: main connector, DSKY hook up, and Ke
   "m1l04ph6CjU",  # 2019-07-11 Apollo Guidance Computer Part 18: Module B11 rescue, Apollo 13 style
   "AhVKYDVZxWQ",  # 2019-07-12 Apollo Guidance Computer Part 19: It finally works!
   "2zXfO571Tio",  # 2019-07-16 Apollo Guidance Computer Part 21: Playing moon landing on our restored
   "-f7SE-dDNA0",  # 2019-07-16 Apollo Guidance Computer Part 20: electroluminescent panel for our DSK
   "r_eBGSe5zEQ",  # 2019-07-17 Flying the Apollo 11 Moon Landing with the Original AGC Code (Apollo G
   "-3xK0O7lnNs",  # 2019-07-17 Apollo Guidance Computer Part 22: Module B11 fails again!
   "9iavKBdPo4U",  # 2019-07-27 Apollo Guidance Computer Part 24: the restored AGC does Moon landings 
   "wcV_TV1Gccc",  # 2019-09-06 Apollo Guidance Computer Part 25: Dan Lickly and Charles Simonyi Refle
   "84sI8GQ8o34",  # 2019-10-08 Apollo Guidance Computer Part 26: We open and identify the AGC for sal
   "-JTa1RQxU04",  # 2020-06-07 Apollo Guidance Computer Part 27: Recovering the Lost Apollo 10 LM Sof
   "feRCZyLzAwA",  # 2021-07-27 Apollo Guidance Computer Part 28: real DSKY display works again after 
   "IsIXrveEL1M",  # 2023-01-28 Apollo Guidance Computer Part 29: Mikes Scores a Coupling Data Unit (C
   "hckwxq8rnr0",  # 2023-10-27 Apollo Core Rope Memory (Apollo Guidance Computer Part 30)
   "k2Ji-55FOGQ",  # 2024-02-19 F8 Fly-By-Wire System (Apollo Guidance Computer Part 31)
   "3CqGq-_cW1k",  # 2026-02-15 Apollo Comms Part 38: Return of the AGC (we hook up our Apollo Guidanc
  ],
 ),
 dict(name="Apollo DSKY & Hand Controllers", kind="Space hardware",
  desc="A real Apollo DSKY and hand controllers.",
  videos=[
   "JB4x6Uy50sY",  # 2025-01-13 Apollo DSKY - part 1: we have a real (and broken) DSKY!
   "vA0l_xvBmug",  # 2025-03-15 Genuine NASA Apollo DSKY Full Restoration (Apollo DSKY - part 2)
   "NfaZBYNEgxY",  # 2026-09-20 Apollo Hand Controllers - Part 1: we look at the "sticks" that were us
   "LsTtaUW5V-I",  # 2026-09-23 Apollo Hand Controllers - Part 2: A Field Trip to Lumafield
   "4-4Cr_pgCLU",  # 2026-10-08 Apollo Hand Controllers - Part 3: Trying to repair the LM hand control
  ],
 ),
 dict(name="Apollo Comms", kind="Space hardware",
  desc="Bringing up Apollo's S-band communications equipment over dozens of parts.",
  videos=[
   "v49ucdZcx9s",  # 2021-09-17 Apollo Comms Part 1: Opening the S-Band Transponder and Amplifier
   "laYpGB1pWAc",  # 2021-10-07 Apollo Comms Part 2: Inside the Traveling Wave Amplifier
   "J8gND82t6G4",  # 2021-11-07 Apollo Comms Part 3: Inside the S-Band Transponder
   "X0GhLIJdNhM",  # 2021-11-25 Apollo Comms Part 4: Transponder power up preparation, and more origin
   "E4iUO03E92g",  # 2021-11-29 Apollo Comms Part 5: Transponder first power on.
   "cQlbtUdbYJs",  # 2021-12-02 Apollo Comms Part 6: First tone transmission, to the Moon and back!
   "87qA41A_Ies",  # 2021-12-05 Apollo Comms Part 7: NASA phase modulated receiver
   "-esdoTUZoHA",  # 2021-12-14 Apollo Comms Part 8: Which Crystal?
   "VReePQJRRI0",  # 2022-01-18 Apollo Comms Part 9: Mystery Up-Data Link Test Set
   "uvUq81jIzPg",  # 2022-02-17 Apollo Comms Part 10: Apollo SDR reboot and first voice transmission!
   "s6R992dgtAY",  # 2022-02-22 Apollo Comms Part 11: Missing PM Transmitter Found!
   "ctNmYFfxI7w",  # 2022-02-28 Apollo Comms Part 12: Building an Apollo transmit station with Keysigh
   "hBKHNADtNPs",  # 2022-03-03 Apollo Comms Part 13: We successfully repair both our NASA transmitter
   "sv0aFLQvFxc",  # 2022-03-24 Apollo Comms Part 14: Reverse Engineering NASA's Up Data Link test box
   "ztnct4r-U1w",  # 2022-03-28 Apollo Comms Part 15: Combining Voice, Data and Ranging
   "Zj3ZuphVxsE",  # 2022-05-07 Apollo Comms Part 16: Stanford Dish’s Apollo Past
   "-D_0BdCWHDY",  # 2022-06-07 Apollo Comms Part 17: Opening the Pre-Modulation Processor
   "iegf7ZU6ciM",  # 2022-07-03 Apollo Comms Part 18: Solving the mystery of NASA's Updata Link box mi
   "EYovBJR6l5U",  # 2022-07-23 Apollo Comms Part 19: Pre-Modulation Processor Grand Explanation
   "66LK1UxKHAM",  # 2022-07-25 Apollo Comms Part 20: Pre-Modulation Processor Power Up
   "YBpleXMTuz8",  # 2022-08-21 Apollo Comms Part 21: TV from the Moon
   "msWnY2zKS9o",  # 2022-10-02 Apollo Comms Part 22: How NASA Upgraded the Moon TV to Color
   "ZS27M2NNQlY",  # 2022-11-11 Apollo Comms Part 23: making connectors and a control panel
   "08RBYePw5mA",  # 2022-12-09 Apollo Comms Part 24: Interface Simulator bring up
   "GkLLCv1meyU",  # 2023-03-11 Apollo Comms Part 25: Apollo-HP Nixie Space Clock
   "2tShJwG0pVs",  # 2023-04-17 Apollo Comms Part 26: Full system integration, Morse, TV, and upvoice 
   "rAAFkjYxWj4",  # 2023-04-29 Apollo Comms Part 27: Quindar Tones Microphone Hack
   "ZUeFwyicV8o",  # 2023-06-02 Apollo 13 accident: understanding Houston’s real time debug (Apollo Co
   "h83vhUx3nPY",  # 2023-12-22 Apollo Comms Part 29: Downvoice
   "us5t_XESsr8",  # 2024-05-11 Apollo Comms Part 30: We explain and debug modern (CD4046B) and vintag
   "06evyO7aUVU",  # 2024-06-25 Apollo Comms Part 31: UDL Grand Opening and Power Up
   "tBy1j9cTYKc",  # 2024-07-12 Apollo Comms Part 32: Breaking the Updata Link Code
   "HFqWvtVVbgk",  # 2024-07-26 Apollo Comms Part 33: Is there something wrong with our NASA Up Data L
   "2Jt0PsxLM7k",  # 2024-10-08 Apollo Comms Part 34: Trying every function of the Apollo command syst
   "F2u5QUE4KgA",  # 2025-09-21 Apollo Comms Part 35: PCM Telemetry - Power Up
   "56lfdHR-3mY",  # 2025-12-10 Apollo Comms Part 36: PCM pinout discovery saved by "SCE to AUX"
   "I6lNQU7pchM",  # 2026-01-04 Apollo Comms Part 37: Apollo's weirdest (but genius) analog circuit
   "d95qM3CiPhA",  # 2026-03-25 Apollo Comms Part 39: Rebuilding the digital data demodulator
   "VdJBgpocB7I",  # 2026-05-17 Apollo Comms Part 40: how NASA performed a nav update from the Houston
  ],
 ),
 dict(name="Soyuz Clock & Globus", kind="Space hardware",
  desc="A Soyuz spacecraft clock and the mechanical Globus navigation instrument.",
  videos=[
   "JBIhzEZkWEA",  # 2019-12-07 Soyuz Clock Part 1: Looking Inside a Flown Soyuz Space Clock
   "GmetgNPL-HQ",  # 2020-01-21 Soyuz Clock Part 2: Reverse Engineering Update
   "isS204aBjTQ",  # 2020-02-15 Soyuz Clock Part 3: Powering Up!
   "HKsjwT53yXw",  # 2020-03-04 Soyuz Clock Part 4: How accurate is it?
   "g_Vcspuwp-w",  # 2020-04-01 Soyuz Clock Part 5: Spaceship Connections
   "ZbQ1_sW9zK8",  # 2020-04-06 Soyuz Clock Part 6: International Atomic Space Clock
   "ad8azNovsF8",  # 2020-09-02 Soyuz Clock Part 7: Taming the Glitches in our Space Clock Crystal Osc
   "wrfKSTYntGc",  # 2021-02-14 Soyuz Space Clock Livestream Replay
   "N4K1QMTNw8A",  # 2021-02-14 Soyuz Electro-Mechanical Space Clock - Part I: Grand Opening
   "LYmrnHSe9bg",  # 2021-03-02 Soyuz Electro-Mechanical Space Clock - Part 2: We try every function!
   "WVz0jfgIqyM",  # 2021-06-29 Soyuz Electro-Mechanical Clock - Part 3: clock driver build and 100W b
   "dmHaCQ8Ul6E",  # 2023-02-16 Soyuz "Globus" Mechanical Navigation Computer Part 1: Grand Opening
   "vCogLM-R8FU",  # 2023-02-18 A few orbits with the Soyuz Globus #Short #InTheRightOrientation
   "nDHtJy9cpC0",  # 2023-02-28 7 Orbits with the Soyuz Globus Mechanical Computer #Short #InTheRightO
   "CP5dfjxdkQ4",  # 2023-02-28 Soyuz "Globus" Mechanical Navigation Computer Part 2: Powering Up
   "eG29HrU6Slw",  # 2023-03-26 Soyuz "Globus" Mechanical Navigation Computer Part 3: Landing Function
  ],
 ),
 dict(name="Xerox Alto", kind="Computer",
  desc="Restoring a Xerox Alto.",
  videos=[
   "YupOC_6bfMI",  # 2016-05-12 Seminal Xerox Alto arrives for restoration
   "xPyqQXFC2yw",  # 2016-06-13 Xerox Alto Restoration Part 1 - power supply restoration, disk drive s
   "MDKxOmVDapQ",  # 2016-06-25 Xerox Alto Restoration Part 2 - monitor restoration
   "PR5LkQugBE0",  # 2016-07-05 Xerox Alto Restoration Part 3 - disk drive bring up
   "EDw8U1a6s78",  # 2016-07-31 Xerox Alto Restoration Part 4 - first signs of processor life
   "Wr7vDZpniNI",  # 2016-09-03 Xerox Alto Restoration Part 5 - hooking up the logic analyzer
   "b7yVhMT7tr4",  # 2016-09-10 Xerox Alto Restoration Part 6 - debug leads us to a failed IC
   "c0sL_FwPVwM",  # 2016-09-17 Xerox Alto Restoration Part 7 - developing tools while waiting for new
   "9OQMhvArI9g",  # 2016-09-27 Xerox Alto Restoration Part 8 - Alto finally boots
   "VWQ7hbV7bN0",  # 2016-10-12 Xerox Alto Restoration Part 9 - debug session leads us closer to crash
   "GMp5EAq-Elo",  # 2016-10-16 Xerox Alto Restoration Part 10 - solving the crashes, first look at th
   "OKakermaQ68",  # 2016-11-23 Xerox Alto Restoration Part 11 - exploring Draw and Bravo
   "XhIohWr10kU",  # 2016-12-09 Xerox Alto Restoration Part 12 - Ethernet pioneers and the first optic
   "5f43fmZcj9Y",  # 2017-02-19 Alto Restoration Part 13  - Tools Development Struggle
   "LxFv2JNNW-A",  # 2017-02-20 Xerox Alto Restoration Part 14 - playing Astroroids
   "Grl0KCFiJLs",  # 2017-06-17 Xerox Alto Restoration Part 15 - Ethernet mysteries solved, Alto back 
   "adEr2aRwHnI",  # 2017-06-18 Xerox Alto Restoration Part 16 - our disk goes down, the Alto connects
   "9H79_kKzmFs",  # 2017-08-13 Xerox Alto Restoration Part 17 - Xerox Alto Demo
   "qnjtna0tRhg",  # 2017-08-14 Vintage Computer Festival 2017: Xerox Alto meets its inventors, wins a
   "JSPlr4AZsKQ",  # 2017-10-23 Digibarn Alto Part 1: Another Xerox Alto arrives for restoration
   "G_gKIvDgBHs",  # 2018-01-24 Alto Restoration Part 18 - We crash our disk drive. Mill to the rescue
  ],
 ),
 dict(name="IBM Mainframes", kind="Computer",
  desc="Debugging and running vintage IBM machines: the 1401, 729 tape drives, System/360, 705, 650 and the 029 keypunch.",
  videos=[
   "xUQnVt5qS-Y",  # 2014-04-20 IBM 1401 French Presentation with English Subtitles
   "Ey0FOmqONys",  # 2014-08-30 IBM 029 Card Punch Arrives for Restoration
   "b5P5bBv_wNk",  # 2014-08-31 IBM 029 Keyunch Restoration 2: First signs of life
   "6XpR4cwCado",  # 2014-08-31 IBM 029 Card Punch Restoration 1: First power up - no smoke, but not m
   "zIOx0ZaJQqY",  # 2014-09-01 IBM 029 Keypunch Restoration 3 - Debugging pinpoints first failure
   "hNhM3kjrYgI",  # 2014-09-02 IBM 029 Keypunch Restoration 4 - Fixing cam contacts
   "FkM_FRXNXqU",  # 2014-09-04 IBM 029 Keypunch Restoration 6 - Insanely Complicated Keyboard
   "2_A_PfLSYOM",  # 2014-09-05 IBM 029 Keypunch Restoration 7 - Print Head
   "YnnGbcM-H8c",  # 2014-09-07 1964 IBM 029 Keypunch Card Punching Demonstration
   "IojweEfXlxg",  # 2014-09-07 IBM 029 Keypunch Restoration 8 - Restoring the Programming Drum
   "PwftXqJu8hs",  # 2015-10-04 Debugging the 1959 IBM 1401 Computer at the Computer History Museum
   "7Lh4CMz_Z6M",  # 2016-04-21 Debugging the 1959 IBM 729 Vacuum Column Tape Drive at the Computer Hi
   "WS-WtjwAAO0",  # 2017-02-01 IBM System/360 Front Panel
   "buN6AzdngZQ",  # 2017-04-24 IBM 1401 Restoration Team: A Day at the Office
   "5p5e_70711E",  # 2017-12-09 The IBM 1401 Mainframe Computer Wishes you a Merry Christmas
   "zOlI1_i2HwQ",  # 2017-12-25 Powering a 1955 IBM 705 Vacuum Tube Logic Module
   "uFQ3sajIdaM",  # 2018-02-02 The IBM 1401 compiles and runs FORTRAN II
   "LtlrITxB5qg",  # 2018-06-02 The IBM 1401 mainframe runs "Edith"
   "dc5PpE56qPw",  # 2019-07-20 The IBM 1401 mainframe commemorates the Apollo 11 Moon landing
   "8qZEQIX7VY8",  # 2022-06-02 IBM 729 Tape Drive Magnetic Clutch Job
   "ZWLptl0cKSc",  # 2022-11-19 The IBM 029 keypunch mechanical keyboard: insanely complicated!
   "qMPggC9LxPo",  # 2026-09-07 Looking inside the IBM 650, 1950's most successful computer
  ],
 ),
 dict(name="Bendix Air Data Computer", kind="Instrument",
  desc="A Bendix air data computer.",
  videos=[
   "D-wHIDnnQwQ",  # 2023-02-03 Bendix Air Data Computer - Part 1: First Look Inside
   "bbOMHQMohc0",  # 2023-04-23 Bendix Air Data Computer - Part 2: Master Ken Explains How It Works
   "8QvoY4_xBjw",  # 2023-04-25 Bendix Air Data Computer - Part 3: Intro to Synchros
   "8nh26lRmRdQ",  # 2023-08-03 Bendix Air Data Computer - Part 4: Magnetic Amplifier Magic
   "LQkDi3cjY3U",  # 2024-01-17 Bendix Air Data Computer - Part 5: Restoration Finished, It Works!
  ],
 ),
 dict(name="B-52 Astro Tracker", kind="Instrument",
  desc="A B-52 bomber astro tracker.",
  videos=[
   "nkvN74wuT8w",  # 2024-12-08 B-52 Bomber Astro Tracker - Part 1: Grand Opening (ft. Le Labo de Mich
   "GkEjLqu-JH0",  # 2025-01-07 B-52 Bomber Astro Tracker - Part 2: Power up and gyro-stabilization
   "aPIZwqq_W_k",  # 2025-03-05 B-52 Bomber Astro Tracker - Part 3: Figuring out the optical system
  ],
 ),
 dict(name="Mechanical Calculators", kind="Computer",
  desc="Friden and other mechanical calculators.",
  videos=[
   "1X3ivZfSfW4",  # 2014-11-02 Restoring a 1956 Friden STW 10 Mechanical Calculator
   "qKm9eM2BuM0",  # 2014-11-03 Friden STW 10 Mechanical Calculator Demo
   "7Kd3R_RlXgc",  # 2016-06-14 Divide by Zero on the Friden STW10 Mechanical Calculator
   "Sk7yftG248s",  # 2016-09-02 Summer Interns vs. Friden H8 Mechanical Calculator
   "WN1l1h5qR38",  # 2017-10-10 My 1957 Friden Mechanical Calculator goes on Japanese TV
   "-MLQ0yI1BrQ",  # 2020-09-22 The Friden STW-10 Calculator Plays The Friden March
   "-1Jz5X5Cr4Q",  # 2020-09-24 Explaining the Friden Mechanical Calculator (while fixing it)
   "h84JonY0Jho",  # 2023-11-19 My 1956 STW-10 Friden Calculator
  ],
 ),
 dict(name="Solari Flip Clock", kind="Instrument",
  desc="Restoring a Solari flip clock.",
  videos=[
   "vwUnUvzNho4",  # 2014-05-01 Solari Udine Dator 10 Flip Clock Restoration Part 2
   "cqsWC4tSLPI",  # 2014-05-01 Solari Udine Dator 10 Flip Clock Restoration Part 1
   "Dw59ToripKE",  # 2014-07-30 Solari Udine Dator 10 Flip Clock Restoration Part 4 Final
   "fbsXvy5lUvk",  # 2014-07-30 Solari Udine Dator 10 Flip Clock Restoration Part 3
   "RF5sGjat9eY",  # 2017-01-01 New Year Flip on the Solari Dator 10 Flip Clock
  ],
 ),
 dict(name="R2-D2 Builds", kind="Robot",
  desc="Star Wars R2 droid builders.",
  videos=[
   "EI7Otnw2_cU",  # 2010-05-20 R2-D2 2-3-2 mechanism demo
   "hQVfnH7tWpY",  # 2010-06-02 R2-D2 Shoulder Actuator 2
   "I0Tbxe9PSAI",  # 2010-06-02 R2-D2 Shoulder Actuator 1
   "iENKltSEFTU",  # 2010-06-03 R2-D2 2-3-2 center leg lift mechanism
   "h0PsRGC3G8M",  # 2010-06-07 R2-D2 Power System
   "h5_6tm1ntPQ",  # 2010-06-09 R2-D2 Charger Bay
   "v9vhstzh6Ok",  # 2010-10-04 R2-D2 robot 2-3-2 transistion first try
   "88Fy_gqdy7U",  # 2010-10-18 R2LA 2010 Chicken Race
   "7y_JOvsoHAE",  # 2010-11-24 R2-D2 Controller Demo
   "ocYDqE_7WQo",  # 2010-11-24 R2-D2 controller demo
   "4DXPPaPp11E",  # 2011-03-21 R2-D2 Progress Update
   "Mc98Q7CZW2E",  # 2011-03-21 R2-D2 First stroll out of the lab
   "SQMiM1S4mwg",  # 2011-04-16 R2-D2 Dome Pie Panels open
   "SGnyKI_9yA0",  # 2011-11-06 R2-D2 2-3-2 center leg lift with electro-magnetic brake
   "3l5V-8fSCcg",  # 2011-11-14 R2-D2 Leg Lift Directional Spring Brake
   "AKPmsR3Bb28",  # 2012-02-25 CuriousMarc's HoloLight (for R2-D2 Building)
   "NniWhi313cI",  # 2012-03-02 R2-D2 Dome Panel Servo Trial
   "vl5WqwpIXOg",  # 2012-03-02 R2-D2 movable dome pie panel with servo
   "S4QRGenCePg",  # 2012-03-06 R2-D2 Dome Magic/Picture Panel
   "Em0EFcLLnvo",  # 2012-03-09 TV Projection Screen as material for R2-D2 Dome Magic Panel
   "Tw1PkHXAK3Y",  # 2012-03-27 R2 Dome Panel Servo-Hinge Mechanism
   "BSlTbdqa1hY",  # 2012-03-28 R2-D2 Dome Panel Test
   "xvhA0ftJQyI",  # 2012-03-28 R2 Dome Lower Panel
   "6tR6cmHCNas",  # 2012-03-30 Animated Holoprojectors on R2-D2 Dome
   "n5922ZWvors",  # 2012-04-01 R2 Dome Panel Test #2
   "cK7BtHfwNmM",  # 2012-04-04 R2-D2 Dome PSI lights
   "O5ckrb-tDow",  # 2012-05-06 R2 showing off at R2LA build day
   "gftrTzidfas",  # 2012-05-09 R2LA Build Day 2012
   "g-1gfuSoAD8",  # 2012-05-25 R2 Builders' Group at Maker Faire 2012
   "LnrhO9S0sjI",  # 2012-07-26 R2-D2 Dome Panel Control - more details
   "vryj6a7as4o",  # 2012-08-01 R2-D2 Pie Panel Music
   "TDOPcuqudTE",  # 2012-08-18 R2-D2 Dome Automation with iPhone
   "kMx5zWbi7Ag",  # 2012-08-28 R2-D2 Dome Magic Panel Added
   "q8Zgysq0DwY",  # 2012-08-28 Swarovski Crystal R2 Dome
   "_Yh-pIBjUao",  # 2012-12-26 R2 iPhone App GUI Concept
   "w58oTCkZQGw",  # 2013-01-03 R2-D2 iPhone App!
   "D65RMAYseDw",  # 2013-01-06 MarcDuino v1 Boards for R2-D2 Animatronics
   "AUod3LRQ1DI",  # 2013-03-14 R2 Touch iPhone App Update
   "RoXNL9BV9Is",  # 2013-04-20 LiPo power system for R2-D2
   "X8uUQQGV1nc",  # 2013-05-04 R2-D2 Dykem Blue Painting Tutorial
   "T5xpfs5WBZw",  # 2013-05-04 R2-D2 Dykem Blue
   "_Xv3d5xiO2Q",  # 2013-05-20 R2 showing some tricks at Maker Faire 2013
   "DVa9BGLV1Fs",  # 2013-06-23 R2 Gadget Reference ROTJ R2 Zapped Scene
   "QGJxY8zrJ7Y",  # 2013-06-30 Machining R2-D2 Shoulder Hydraulics on my lathe Part 1
   "m9NJy_Np4vc",  # 2013-07-01 Machining R2-D2 Shoulder Hydraulics on my lathe Part 2
   "PQSUL4MeTzY",  # 2013-09-20 MP3Trigger sound for the R2Touch iPhone App Preview
   "LYUTc3k4voo",  # 2013-11-26 Teeces with R2 Touch
   "jeGLv9i5Izk",  # 2014-11-07 MarcDuino v2 Master Board for R2-D2 animatronics
   "jT8Hrke5wpc",  # 2014-12-22 MarcDuino v2 Slave Board for R2-D2 animatronics
   "AMhTqBdphEI",  # 2015-04-14 R2-D2 Building and Preparation for Star Wars Celebration Anaheim
   "RkJIt5-IqVw",  # 2015-04-14 CuriousMarc's R2-D2 Quick Demo (April 2015)
   "2KnXNfRovls",  # 2015-04-16 R2 Builders Club setting up at Star Wars Celebration Anaheim
   "CJgjEc8CEs0",  # 2015-04-24 R2-D2's Day at Star Wars Celebration Anaheim 2015
   "HBjIBquIQrs",  # 2015-04-30 R2-D2 build detail: tie rod anchors
   "910UMrXTbx0",  # 2016-08-15 R2-D2 Build Day Aug  13 2016
   "REd3jthn0tk",  # 2017-05-29 R2-D2 at Maker Faire Bay Area 2017
   "RbjNjRZE0A8",  # 2017-05-29 Inside the dome: R2-D2 emergency  repair
   "b06b33iN6Ak",  # 2017-06-16 Working on my R2-D2 Skins
   "R2twrM3OeSI",  # 2017-09-27 R2LA 2017: Star Wars robot builders meeting
  ],
 ),
 dict(name="Teletype as Linux Terminal", kind="Computer",
  desc="A 1930 Teletype as a Linux terminal.",
  videos=[
   "_NuvwndwYSY",  # 2018-07-06 Teletype Model 19 - Part 1: A Teletype Arrives for Restoration
   "ug5lUI-hs3s",  # 2018-07-07 Teletype Model 19 Part 2: Baudot Teletype Intro and Demo
   "Rm-hglBgN7M",  # 2018-07-11 Teletype Model 19 Part 3: Teardown time!
   "WX74GoHuwHk",  # 2018-07-13 Teletype Model 19 Part 4: Thyratron Power Supply
   "9O5AAG8nJRE",  # 2018-07-22 Teletype Model 19 Part 5: We make vintage baudot bits!
   "25hqGj2OY_E",  # 2018-07-29 Teletype Model 19 Part 6: Fixing the keyboard counter, filter and repe
   "xDZkqIIWofk",  # 2018-08-04 Teletype Model 19 Part 7: Our First Intergalactic Transmission Attempt
   "0SgIMJPnYPk",  # 2018-08-11 Teletype Model 19 Part 8: Printer Restoration (and a Teletype-quarium)
   "FUWn7AAqBU8",  # 2018-08-15 Teletype Model 19 Part 9: Fixing the Model 15
   "QwFm5A0anhY",  # 2018-08-19 Teletype Model 19 Part 10: Restoring the Transmitter/Distributor
   "-LD872EWKaE",  # 2018-08-28 Teletype Model 19 Part 11: A Visit to Mr. RTTY
   "7RmMJRj8Dc4",  # 2018-09-30 Teletype Model 19 Part 12: Reassembling the Transmitter/Distributor
   "7msEgegcHxA",  # 2018-10-28 Teletype Model 19 Part 13: Table rewiring and putting the teletype all
   "9Qct8HWnXmY",  # 2018-11-11 Teletype Model 19 Part 14: Final Stretch, Pimping Up the Teletype
   "jxkygWI-Wfs",  # 2018-12-10 Teletype Model 19 (and Model 15) Demonstration
   "Jhn3AYHwSqg",  # 2019-03-18 Teletype Model 14 Reperforator
   "QzfjT1mCRww",  # 2019-09-24 Teletype 33 ASR Part 1: Restoration Begins
   "DrbyQOHhs50",  # 2019-10-01 Teletype 33 ASR Part 2: Chasing Bugs in the Transmit Section
   "r1tdMPFK9MA",  # 2019-10-05 Teletype ASR 33 Part 3: 20 mA Test Loop with the Vintage HP 2645 Termi
   "Z5dgjT-ZYeM",  # 2019-10-13 Teletype ASR 33 Part 4: Returning the print section to life
   "hkB5YRpSWnI",  # 2019-10-23 Teletype ASR 33 Part 5: Working on the Keyboards
   "x_Di7KpHubc",  # 2019-10-28 Teletype ASR 33 Part 6: Print Head Mechanism
   "yG7sHxCRfoY",  # 2019-12-17 Teletype ASR 33 Part 7: Receive Section Fixed!
   "yzulZaJbdUU",  # 2020-02-03 Teletype ASR 33 Part 8: Paper Tape Punch
   "S81GyMKH7zw",  # 2020-02-05 ASR 33 Teletype demo  (restoration Part 10)
   "VvAwcK6d8dg",  # 2020-02-05 Teletype ASR 33 Part 9: "Automatic" Tape Reader
   "2XLZ4Z8LpEE",  # 2020-04-13 Using a 1930 Teletype as a Linux Terminal
   "b2QPy-igBLA",  # 2020-04-25 Teletype Music? The Model 15 performs the TTY March!
   "X904FYolBs0",  # 2020-04-27 Tweeting from the Teletype: How To
   "9TGQ4pnVWSQ",  # 2020-04-27 Tweeting from the Teletype
   "DchXxsqa0BE",  # 2021-11-27 TI Silent 703 Terminal - Texas Instruments’ slick answer to clunky Tel
   "6HlSyW0pijQ",  # 2022-07-11 Nevada Haul: 1950's Mil Radios, Teletype and HP Goodness
   "FxBgTDpsUC0",  # 2022-12-11 Military Teletype TE-50B Toolkit Unboxing
   "4ta-AWDALyY",  # 2023-09-03 Whisper Writer Telex to Radio Teletype Conversion
   "Mt4EDsT7Gto",  # 2023-12-25 Teletype Music! A mechanical Christmas song.
  ],
 ),
 dict(name="Bubble LED Clock", kind="Instrument",
  desc="A bubble LED clock hack with 1970s tech.",
  videos=[
   "m_juPAK7I_I",  # 2022-01-08 Bubble LED clock hack with 1970's tech
  ],
 ),
 dict(name="Gyroscopes", kind="Instrument",
  desc="Spinning up inertial and WWII gyroscopes.",
  videos=[
   "wYsG-lXfih8",  # 2019-03-16 Inertial Gyroscope Spin Up and Demo
   "pz-LA71tMWw",  # 2021-08-19 WWII USAF Gyroscope Spin Up and Turntable Test
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
