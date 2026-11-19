"""Inventions of Jeff Geerling. Hand-grouped and hand-reviewed: every upload was read and labelled
(invention / repair / tutorial / workshop / other, see data/review/). Only things the maker designed and made are
listed here; every other upload appears under "Other uploads"."""

CREATOR = {'slug': 'jeff-geerling', 'name': 'Jeff Geerling', 'person': 'Jeff Geerling', 'tagline': 'Raspberry Pi clusters, petabyte NAS boxes and a mini rack homelab.', 'other_label': 'Other uploads: reviews, tutorials, news and Ansible lessons'}

INVENTIONS = [
 dict(name="Raspberry Pi Clusters", kind="Cluster",
  desc="Raspberry Pi clusters: a cluster series, 64-core Pi blades, the Turing Pi, a NanoCluster and AI clusters.",
  videos=[
   "7Tf2f5gdO4I",  # 2015-07-27 Nginx Load Balancer Visualization on a Raspberry Pi Cluster
   "1SvNkdTzUng",  # 2016-05-05 Let's Build a Raspberry Pi Cluster (Pi Dramble #1)
   "wgMFt2menlw",  # 2016-05-24 Provision LEMP with Ansible on a Raspberry Pi Cluster (Pi Dramble #4)
   "p4O0VW0qPVE",  # 2016-05-26 Highly Available Drupal on a Raspberry Pi Cluster - php[tek] 2016
   "S6WkYzF6I4A",  # 2017-03-08 Deploy Drupal 8 with Ansible on a Raspberry Pi Cluster (Pi Dramble #5)
   "kgVz4-SEhbE",  # 2020-04-29 Raspberry Pi Cluster Ep 1 - Introduction to Clustering
   "xNndbfxMCLo",  # 2020-05-08 Raspberry Pi Cluster Ep 2 - Setting up the Cluster
   "N4bfNefjBSw",  # 2020-05-21 Raspberry Pi Cluster Ep 3 - Installing Kubernetes (K3s) on the Turing 
   "IafVCHkJbtI",  # 2020-06-05 Raspberry Pi Cluster Ep 4 - Minecraft, Pi-hole, Grafana + MORE!
   "TMUPrSnwSW0",  # 2020-06-15 Pi 4 Winner and 30k Turing Pi Giveaway!
   "IoMxpndlDWI",  # 2020-06-29 Raspberry Pi Cluster Ep 5 - Benchmarking the Turing Pi
   "aApByQWqnV0",  # 2020-07-30 Raspberry Pi Cluster Ep 6 - Turing Pi Review
   "LcuNc4jz-iU",  # 2021-05-20 Raspberry Pi Rack - 6 node 3D Printed 1U Pi cluster
   "zH9GwYZu_aE",  # 2021-08-04 Raspberry Pi Blade crams 64 ARM cores and NVMe in 1U!
   "8zXG4ySy1m8",  # 2021-08-11 Why would you build a Raspberry Pi Cluster?
   "IUPYpZBfsMU",  # 2021-12-01 4 Pis on a mini ITX board! The Turing Pi 2
   "RijuRF0ITdE",  # 2022-01-05 Racking up a Raspberry Pi cluster!
   "akJ97oqmQlU",  # 2022-09-23 Homelab upgrade: New Raspberry Pi Cluster rackmount
   "UEtpaiODNs0",  # 2025-06-06 Cute, but powerful: meet NanoCluster, a tiny supercomputer
   "N5xhOqlvRh4",  # 2025-08-07 I built a private AI mini-cluster with Framework Desktop
   "8SiB-bNyP5E",  # 2025-09-19 I regret building a $3000 Pi AI Cluster
  ],
 ),
 dict(name="Raspberry Pi NAS", kind="Storage",
  desc="The best Raspberry Pi NAS, the Petabyte Pi project and mini NAS builds.",
  videos=[
   "oWev1THtA04",  # 2020-12-04 I built the fastest Raspberry Pi SATA RAID NAS!
   "Zpfq8ZC2hyI",  # 2021-02-26 Hardware RAID for the fastest Raspberry Pi CM4 NAS!
   "vBccak8f-VY",  # 2021-03-26 Raspberry Pi vs ASUSTOR NAS Head-to-Head Part 1 - Hardware
   "KhHAf7mTxkk",  # 2021-04-02 Raspberry Pi vs ASUSTOR NAS Head-to-Head Part 2 - the VERDICT!
   "7Li7Nh9V74I",  # 2021-05-06 New Raspberry Pi Projects - CM4 NAS, Piunora, and Seaberry!
   "ahrdx3TYxZc",  # 2021-06-10 Building the best Raspberry Pi NAS - Wiretrustee SATA
   "G_px298IF2k",  # 2021-11-17 I built a $5,000 Raspberry Pi server (Radxa Taco NAS)
   "V3jwQzb46Zc",  # 2021-12-22 Raspberry Pi vs ASUSTOR NAS – Round II
   "BBnomwpF_uY",  # 2022-05-18 The Petabyte Pi Project
   "R2S2RMNv7OU",  # 2022-06-22 I made the Petabyte Raspberry Pi even faster!
   "xvE4HNJZeIg",  # 2022-07-20 Scrapyard Server: Fastest all-SSD NAS!
   "4VkY1vTpCJY",  # 2022-10-27 Better than Disney+: Jellyfin on my NAS
   "5QH8Dj6g_Nk",  # 2023-07-10 All-flash NAS fight: DIY or Buy – Round III!
   "Hz5k5WgTkcc",  # 2024-02-11 How efficient can I build the 100% Arm NAS?
   "iD9awxmOGG4",  # 2024-02-29 Silencing the 100% Arm NAS—while making it FASTER!
   "l30sADfDiM8",  # 2024-04-04 The ULTIMATE Raspberry Pi 5 NAS
   "D8EIs8s303k",  # 2024-05-03 Big NAS, Lil NAS (moving 13)
   "etayojgChDM",  # 2025-02-11 AMD NASes give us everything we ever wanted
   "M_Ft8OAPQ3g",  # 2025-04-17 Is this the perfect Mini NAS?
   "TlsIuA8rBRg",  # 2025-04-25 I fixed the perfect Mini NAS!
   "8VBnxEQKG3o",  # 2025-07-04 The Mini NAS has arrived! (mini homelab)
   "XvaXemGDSpk",  # 2025-08-28 TrueNAS on a custom Raspberry Pi NAS
  ],
 ),
 dict(name="Pi Routers & Starlink", kind="Network",
  desc="Tiny Raspberry Pi routers and Starlink projects.",
  videos=[
   "U-VfAFj4jYw",  # 2021-04-09 I took SpaceX's Starlink 'Dishy' to my cousin's farm!
   "ynsCVOz7jv4",  # 2021-04-13 SpaceX Starlink satellite internet - Roof mount install
   "Xx4s02w4kgA",  # 2021-04-14 Set up OctoPrint on a Raspberry Pi - LIVE via Starlink!
   "w7teLVwi408",  # 2021-05-28 You call THAT a router?! 2 Tiny Raspberry Pi Routers
   "spD4FLfi2a4",  # 2021-07-22 SpaceX's Starlink Reviewed: How is it after 4 months?
   "MDvwwpX1y9g",  # 2022-02-02 I took down Starlink
   "I9zqGeH8EIs",  # 2022-05-04 Elon never delivered... SO I DID!
   "6-q1fcOa8P4",  # 2022-07-27 Starlink is getting slower
   "3D5q3NWEMZY",  # 2026-01-02 $1m server vs $600 router
  ],
 ),
 dict(name="Mini Rack Homelab", kind="Cluster",
  desc="Project Mini Rack: a homelab revolution.",
  videos=[
   "y1GCIwLm3is",  # 2025-01-17 Project MINI RACK - a Homelab Revolution!
  ],
 ),
 dict(name="Pi Media Centres", kind="Media",
  desc="Replacing an Apple TV and smart TV with Raspberry Pis, and Jellyfin.",
  videos=[
   "-epPf7D8oMk",  # 2022-06-08 Smarter than a Smart TV! (Raspberry Pi Inside)
   "3hFas54xFtg",  # 2024-05-31 I replaced my Apple TV—with a Raspberry Pi
  ],
 ),
 dict(name="Pi GPUs", kind="Cluster",
  desc="Plugging AMD and other GPUs into a Raspberry Pi.",
  videos=[
   "PuDxASIVsqE",  # 2017-12-23 2011 MacBook Pro with Radeon GPU glitch rebooting constantly
   "ikpgZu6kLKE",  # 2020-10-27 GPUs on a Raspberry Pi Compute Module 4!
   "MxcafwjWw24",  # 2021-04-23 Will ANY GPUs work on the Raspberry Pi?
   "1hFPnpVqzkw",  # 2021-05-13 Raspberry Pi GPU Bringup LIVE - Nvidia GeForce GTX 1080
   "LO7Ip9VbOLY",  # 2021-09-12 I plugged the AMD Radeon RX 6700 XT into a Raspberry Pi
   "crnEygp4C6g",  # 2022-04-27 It took me TWO YEARS to get this working! (GPU on Pi)
   "P6fRJLN9VDw",  # 2022-05-11 Nvidia Open-Sourced their Linux GPU Kernel Driver!
   "l9dItRUjQ0k",  # 2023-04-13 I tested EVERY graphics card on a Raspberry Pi!
   "wl5H5rT87JE",  # 2023-04-21 This Mac Pro killer runs a GPU—and Windows on Arm!
   "BLg-1w2QayU",  # 2023-11-28 You can use external GPUs on the Raspberry Pi 5
   "7Qx_bdFSSuc",  # 2024-11-15 My Raspberry Pi has a better GPU than Apple's M4 Pro
   "AyR7iCS7gNI",  # 2024-11-19 A GPU-powered Pi for more efficient AI?
   "Q3bY0qHl8gw",  # 2025-10-04 Can we get Intel Arc GPUs working on a Pi before Nvidia kills them?
   "ewDJpxQEGo4",  # 2025-11-13 Every Intel GPU runs on a Raspberry Pi
   "SPTYjF8qH0A",  # 2025-11-26 Nvidia GPU on Raspberry Pi—it WORKS!
   "8X2Y62JGDCo",  # 2025-12-20 Do you need a whole PC to run a GPU?
  ],
 ),
 dict(name="Retro Console", kind="Media",
  desc="Building a retro game console.",
  videos=[
   "9zu3pjvdSHI",  # 2021-11-03 Build your OWN retro game console with a Raspberry Pi!
  ],
 ),
 dict(name="Pi KVM", kind="Network",
  desc="Controlling any computer with Pi KVMs.",
  videos=[
   "TIrkEr2AeDY",  # 2021-09-22 Control ANY COMPUTER with these Pi KVMs!
  ],
 ),
 dict(name="Raspberry Pi Bell Slapper", kind="Build",
  desc="A software-controlled bell-ringing contraption driven by a Raspberry Pi.",
  videos=[
   "Etr7uIL9spg",  # 2020-12-15 The Raspberry Pi Bell Slapper - a software-controlled bell
  ],
 ),
 dict(name="Tiniest NVMe SSD RAID Array", kind="Build",
  desc="A tiny multi-drive NVMe RAID array built on a Raspberry Pi Compute Module.",
  videos=[
   "AoNxDe1a-X8",  # 2021-03-19 I built the world's TINIEST NVMe SSD RAID array!
  ],
 ),
 dict(name="Computer Inside a Computer", kind="Build",
  desc="A Raspberry Pi computer built to plug into a PC slot and a graphics card.",
  videos=[
   "cVWF3u-y-Zg",  # 2022-09-15 I put a computer in my computer
   "YaqJginb4go",  # 2023-04-14 I made a computer you plug into a graphics card #shorts
  ],
 ),
 dict(name="Pi Pico W Garage Door Opener", kind="Build",
  desc="Hacking the garage door opener with a Raspberry Pi Pico W.",
  videos=[
   "dFDGtlSi9Eg",  # 2022-11-11 Hacking my garage door with the Raspberry Pi Pico W
  ],
 ),
 dict(name="Modded Williams Screwdriver", kind="Build",
  desc="Modifying a Williams screwdriver to make it better.",
  videos=[
   "WzV84Qj2bL0",  # 2023-02-17 Hacking the Williams! Making a good screwdriver better #shorts
  ],
 ),
 dict(name="100-SBC 1-to-100 Game", kind="Build",
  desc="A game rig built from 100 single-board computers.",
  videos=[
   "C9oDWjBk45g",  # 2023-05-27 Building Mr. Beast's 1-100 game with 100 SBCs! #shorts
  ],
 ),
 dict(name="Talking Hot Dog AM Radio", kind="Build",
  desc="Making a hot dog talk by transmitting through it with AM radio.",
  videos=[
   "WerKkrkuwHg",  # 2024-03-31 We made a hot dog talk—with AM radio!
  ],
 ),
 dict(name="Floor Lamp Homelab", kind="Build",
  desc="A floor lamp turned into a homelab rack.",
  videos=[
   "CE6MTBxDSpE",  # 2025-04-01 I Turned my Floor Lamp into a Homelab
  ],
 ),
 dict(name="Homemade Clock", kind="Build",
  desc="A new clock built by Jeff.",
  videos=[
   "7r-cH1tcl_g",  # 2026-03-06 I built a new clock, and now I'm not sure what time it is
  ],
 ),
 dict(name="Tiny Supercomputer", kind="Build",
  desc="A tiny Raspberry Pi supercomputer built to race college students.",
  videos=[
   "AjmKpDNsTa8",  # 2026-05-01 Building a Tiny Supercomputer to beat college students
  ],
 ),
 dict(name="DIY 20TB Snowball", kind="Build",
  desc="A homemade 20TB data-transfer appliance after Amazon refused to send a Snowball.",
  videos=[
   "v0DEI4Ad7Ik",  # 2026-06-26 Amazon wouldn't let me, so I built my own 20TB Snowball
  ],
 ),
 dict(name="Modded GPS Time Server", kind="Build",
  desc="Modifying a 30-year-old GPS time server.",
  videos=[
   "CivRNW0b1H8",  # 2026-09-04 I modded a 30-year-old GPS Time Server (Telstra should've)
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
