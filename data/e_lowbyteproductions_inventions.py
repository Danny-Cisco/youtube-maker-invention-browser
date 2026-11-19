"""Curated inventions for Low Byte Productions (@lowbyteproductions).

Drafted by build/auto_inventions.py (builds grouped by shared key words, livestreams included, descriptions in the
maker's own words). Every upload not listed here appears under "Other uploads" on the site.
"""

CREATOR = {'slug': 'low-byte-productions', 'name': 'Low Byte Productions', 'person': 'Low Byte Productions', 'tagline': 'Deep dives into low-level hardware and firmware.', 'other_label': 'Other uploads: Shorts, updates and other videos'}

INVENTIONS = [
 dict(name="How Parser Combinators Work", kind="Build",
  desc="In this episode we dive into what a parser combinator library is, and how it is used in practice.",
  videos=[
   "6oQLRhw5Ah0",  # 2019-07-22 How Parser Combinators Work [Parser Combinators From Scratch] Episode 
  ],
 ),
 dict(name="Implementing the mechanics", kind="Build",
  desc="In this episode we explore how the primary mechanism of parser combinators works: A function that transforms one parser state into another.",
  videos=[
   "1axJDmK_pnE",  # 2019-07-30 Implementing the mechanics [Parser Combinators From Scratch] Episode 2
   "zAsn8q-X9HM",  # 2019-11-13 Implementing Stack Mechanics (16-Bit VM in JavaScript 004)
  ],
 ),
 dict(name="Classes, mapping, and generic parsers", kind="Build",
  desc="In this episode we'll create a Parser class and implement map, a method that will allow us to apply arbitrary structure as we parse.",
  videos=[
   "xB7lFPMN4dU",  # 2019-08-06 Classes, mapping, and generic parsers [Parser Combinators From Scratch
  ],
 ),
 dict(name="Contextual Parsing With The Chain Method", kind="Build",
  desc="In this episode we will write the method `Parser.chain(fn)` which utilises functional programming concepts to empower our system with contextual abilities!",
  videos=[
   "nqNzWgSRCeg",  # 2019-08-13 Contextual Parsing With The Chain Method  [Parser Combinators From Scr
  ],
 ),
 dict(name="Building A Language Parser and Interpreter", kind="Build",
  desc="In this episode we dive into parsing recursive structures, and build a very simple functional language parser and interpreter.",
  videos=[
   "PzodUuERBZc",  # 2019-08-20 Building A Language Parser and Interpreter [Parser Combinators from Sc
  ],
 ),
 dict(name="JavaScript Is Weird", kind="Build",
  desc="To offset some of the banana-based JavaScript \"weirdness\" that's making the rounds, I'm bring you a 40 line JSFuck compiler that turns innocent looking JS into a mess of obfuscated symbols.",
  videos=[
   "sRWE5tnaxlI",  # 2019-08-23 JavaScript Is Weird (EXTREME EDITION)
  ],
 ),
 dict(name="Ones and Zeros", kind="Build",
  desc="In this episode the parser combinator system is turned on binary data.",
  videos=[
   "ZgHlc3Q2YjU",  # 2019-08-27 Ones and Zeros: Binary Part 1 [Parser Combinators from Scratch] Episod
  ],
 ),
 dict(name="Why 0.1 + 0.2 === 0.30000000000000004", kind="Build",
  desc="Floating point math is tricky.",
  videos=[
   "wPBjd-vb9eI",  # 2019-09-18 Why 0.1 + 0.2 === 0.30000000000000004: Implementing IEEE 754 in JS
  ],
 ),
 dict(name="16-Bit Virtual Machine in JavaScript 001", kind="Build",
  desc="In this episode we begin implementing a 16-bit virtual machine from scratch in JavaScript.",
  videos=[
   "fTBwD3sb5mw",  # 2019-10-01 16-Bit Virtual Machine in JavaScript 001
  ],
 ),
 dict(name="Memory Access and Branching Bit VM in JavaScript 002)", kind="Build",
  desc="In this video we establish the core instruction set of the VM, give the VM the capabilities to read and write to main memory, and also to make decisions about how the program should proceed with branching instructions.",
  videos=[
   "wJ-pu6Iq0B8",  # 2019-10-15 Memory Access and Branching (16-Bit VM in JavaScript 002)
  ],
 ),
 dict(name="What is the Stack and why do we need it? Bit VM in JavaScript 003)", kind="Build",
  desc="In this episode we understand what a stack is, how it can be implemented on the lowest level, and how it can then be harnessed to allow the Virtual Machine to run subroutines without losing state.",
  videos=[
   "mamop8aqFNk",  # 2019-10-31 What is the Stack and why do we need it? (16-Bit VM in JavaScript 003)
  ],
 ),
 dict(name="Promises From Scratch In A Post-Apocalyptic Future", kind="Build",
  desc="In this installment of Low Level JavaScript we build a Promise implementation from scratch in order to understand exactly how asynchronous abstractions can be built on top of lower level primitives like callbacks.",
  videos=[
   "4GpwM8FmVgQ",  # 2019-11-27 Promises From Scratch In A Post-Apocalyptic Future
  ],
 ),
 dict(name="Building Async/Await FROM SCRATCH using Generators", kind="Build",
  desc="In this episode we build on the Promise abstraction we built in the previous episode to create async/await from scratch using generator functions.",
  videos=[
   "Em2jqwROdZc",  # 2019-12-11 Building Async/Await FROM SCRATCH using Generators
  ],
 ),
 dict(name="Interrupts and Memory Mapped I/O", kind="Build",
  desc="This is episode 2 of the bare metal programming series!",
  videos=[
   "hLYGTpvoMgE",  # 2019-12-25 What is Memory Mapped I/O? (16-Bit VM in JavaScript 005)
   "S92ltJ0C59k",  # 2023-03-21 Interrupts and Memory Mapped I/O :: Bare Metal Programming Series 2
  ],
 ),
 dict(name="Powering Up With New Instructions Bit VM in JavaScript 006)", kind="Build",
  desc="In this episode we add new instructions and capabilities to the VM, including:",
  videos=[
   "1-1wWZdgZRI",  # 2020-02-05 Powering Up With New Instructions (16-Bit VM in JavaScript 006)
  ],
 ),
 dict(name="Tour Through The Assembly Language and The Assembler Bit VM in JavaScr", kind="Build",
  desc="This series is all about building a powerful virtual machine in JavaScript with the following features:",
  videos=[
   "KhKq8a1m8r8",  # 2020-03-29 Tour Through The Assembly Language and The Assembler (16-Bit VM in Jav
  ],
 ),
 dict(name="How Are State Machines Used In Parsing? Bit VM in JavaScript 008)", kind="Build",
  desc="In this episode we begin building the parser for this VMs assembly language.",
  videos=[
   "ai63l4OUxSs",  # 2020-04-09 How Are State Machines Used In Parsing? (16-Bit VM in JavaScript 008)
  ],
 ),
 dict(name="A parser for every instruction? Bit VM in JavaScript 010)", kind="Build",
  desc="This series is all about building a powerful virtual machine in JavaScript with the following features:",
  videos=[
   "YYZopr1dr_E",  # 2020-05-22 A parser for every instruction? (16-Bit VM in JavaScript 010)
  ],
 ),
 dict(name="Generating Machine Code Bit VM in JavaScript 011)", kind="Build",
  desc="This series is all about building a powerful virtual machine in JavaScript with the following features:",
  videos=[
   "5PXMwvUkOKI",  # 2020-06-06 Generating Machine Code (16-Bit VM in JavaScript 011)
  ],
 ),
 dict(name="Bits! [The Bits And Bytes Of Binary", kind="Build",
  desc="This mini series is all about binary.",
  videos=[
   "TdPQ-1TEiNI",  # 2020-06-26 Unsigned Numbers! [The Bits And Bytes Of Binary ep. 3]
   "a23wQcaBfpc",  # 2020-06-26 Operations! [The Bits And Bytes Of Binary ep.2]
   "pOM86M1pGb4",  # 2020-06-26 Bits! [The Bits And Bytes Of Binary ep.1]
  ],
 ),
 dict(name="Expanding Beyond 64kb of Memory with Bank Switching Bit VM in JavaScri", kind="Build",
  desc="In this episode we're learning about memory bank switching - a technique common in the retro game console days - that allows us to address more memory than the limited address space that 16 bits provides!",
  videos=[
   "araYkE3KAms",  # 2020-07-28 Expanding Beyond 64kb of Memory with Bank Switching (16-Bit VM in Java
  ],
 ),
 dict(name="Interrupt Safe Ring Buffer", kind="Build",
  desc="In this episode of the bare metal programming series, we're building a ring buffer to back our UART driver.",
  videos=[
   "9KQ7a-0cSdk",  # 2020-08-11 Interrupts (16-Bit VM in JavaScript 013)
   "uIJnATS9j_0",  # 2023-05-08 Interrupt Safe Ring Buffer :: Bare Metal Programming Series 6
  ],
 ),
 dict(name="Making WAVs: Understanding, Parsing, and Creating WAV Files in JavaScr", kind="Build",
  desc="The WAVE file format is a binary format that encodes high fidelity audio data.",
  videos=[
   "udbA7u1zYfc",  # 2020-08-26 Making WAVs: Understanding, Parsing, and Creating WAV Files in JavaScr
  ],
 ),
 dict(name="Assembler Hacking", kind="Build",
  desc="In this episode, we're going to implement structures.",
  videos=[
   "TXSgQZsVW8w",  # 2020-09-16 Assembler Hacking: Inline Data And Constants (16-Bit VM in JavaScript 
   "GkipKe0S_5E",  # 2020-10-05 Assembler Hacking: Structures (16-Bit VM in JavaScript 015)
  ],
 ),
 dict(name="How Do Regular Expressions Really Work", kind="Build",
  desc="In this video we're going to build a basic regular expression engine from scratch, in order to illustrate the underlying mechanisms that make them tick.",
  videos=[
   "u01jb8YN2Lw",  # 2020-10-20 How Do Regular Expressions Really Work?
  ],
 ),
 dict(name="Building A Fantasy Game Console Emulator", kind="Build",
  desc="In this video we explore the details of the fantasy game console, based on the 16 Bit Virtual Machine - and begin coding the graphics pipeline.",
  videos=[
   "g29vCtzZPuk",  # 2020-12-15 Building A Fantasy Game Console Emulator: System Overview and Graphics
   "Dq_cpyrYI70",  # 2021-01-01 "Live" Coding A NES Emulator in C++!
   "uQXY27d8Pao",  # 2021-01-29 C++ NES Emulator: Investigating The Memory Map
   "USvkqF6bMZ4",  # 2021-03-09 Fantasy Console Emulator: System Integration
   "_eu8hFZP0oU",  # 2021-06-22 Writing A Game For The Fantasy Console Emulator
   "QmHAN1vOtjs",  # 2022-05-18 The Emulator Is Done?!: RISC-V ep.12
  ],
 ),
 dict(name="Building FPGA Hardware Using TypeScript", kind="Build",
  desc="In this video we're taking a look at gateware-ts, a TypeScript library for describing and building digital hardware for FPGAs in TypeScript.",
  videos=[
   "Otx96lJnLeo",  # 2021-01-14 Building FPGA Hardware Using TypeScript: Driving An RGB LED Panel
  ],
 ),
 dict(name="Frogger In Assembly", kind="Build",
  desc="In this installment of the Fantasy Game Console Series (an extension to the 16-Bit Virtual Machine Series), we're creating a game in assembly!",
  videos=[
   "UkPB1ukAgbI",  # 2021-03-24 Frogger In Assembly: Fantasy Console Part 3
  ],
 ),
 dict(name="Mage ASCII Game Engine", kind="Build",
  desc="In this video we're creating an ASCII game engine that runs in the browser!",
  videos=[
   "B3uH517XbPs",  # 2021-04-13 Mage ASCII Game Engine
  ],
 ),
 dict(name="Building The Worlds First CPU in TypeScript", kind="Build",
  desc="Building The Worlds First CPU in TypeScript? (No Really!).",
  videos=[
   "Vat4p2idDOA",  # 2021-10-07 Hardware RISC-V CPU in TypeScript: First Steps
   "ER7h4ZTe19A",  # 2021-10-07 Building The Worlds First CPU in TypeScript? (No Really!)
  ],
 ),
 dict(name="RISC-V Processor In TS", kind="Build",
  desc="RISC-V Processor In TS: ALU (part 2).",
  videos=[
   "ppRzESGUspI",  # 2021-10-19 RISC-V Processor In TS: ALU (part 2)
  ],
 ),
 dict(name="Control and Status Registers", kind="Build",
  desc="Control and Status Registers (CSRs): RISC-V ep.8.",
  videos=[
   "ykbAKu77n5Q",  # 2021-12-01 Control and Status Registers (CSRs): RISC-V ep.8
  ],
 ),
 dict(name="Command Line Hex Editor in TypeScript", kind="Build",
  desc="In this video we're spite-coding a command line hex editor that allows the editing of binary files in a simple and friendly interface like nano.",
  videos=[
   "132wDVovzhw",  # 2021-12-09 Command Line Hex Editor in TypeScript 🧙🏻
  ],
 ),
 dict(name="Building an ENCODER for the \"Quite OK Image Format\"", kind="Build",
  desc="The \"Quite OK Image Format\" (qoi) is a lossless compression image format that has similar performance to PNG, but with substantially faster encoding and decoding, making it a great choice for embedded systems.",
  videos=[
   "GgsRQuGSrc0",  # 2021-12-25 Building an ENCODER for the "Quite OK Image Format" (QOI)
  ],
 ),
 dict(name="Building an DECODER for QOI Images", kind="Build",
  desc="The \"Quite OK Image Format\" (qoi) is a lossless compression image format that has similar performance to PNG, but with substantially faster encoding and decoding, making it a great choice for embedded systems.",
  videos=[
   "5bWopQj-oQs",  # 2022-01-04 Building an DECODER for QOI Images (Quite OK Image Format)
  ],
 ),
 dict(name="Packing Bits For Compression", kind="Build",
  desc="In this video, we're writing a \"Bit Packer\" - a tool that takes data that does not make use of every single bit in its representation, and \"packs\" it into a buffer that takes up the minimal amount of space.",
  videos=[
   "74co_YG39Bw",  # 2022-01-12 Packing Bits For Compression
  ],
 ),
 dict(name="Implementing A Generic Priority Queue", kind="Build",
  desc="In this video we're going to be building a priority queue - a data structure which allows us to add items and retrieve the highest priority item in an extremely fast and efficient manner.",
  videos=[
   "M6OW0KNkhhs",  # 2022-02-01 Implementing A Generic Priority Queue
  ],
 ),
 dict(name="Writing a SPI SD-Card driver in TypeScript", kind="Build",
  desc="[stream] Writing a SPI SD-Card driver in TypeScript.",
  videos=[
   "SIIde33EZrA",  # 2022-02-05 [stream] Writing a SPI SD-Card driver in TypeScript
  ],
 ),
 dict(name="File System Hacking", kind="Build",
  desc="[stream] File System Hacking: FAT32 Deep Dive.",
  videos=[
   "GMkjey1FTe0",  # 2022-02-12 [stream] File System Hacking: Building A FAT32 Layer On Top Of The SD-
   "giVfqICb2J4",  # 2022-02-20 [stream] File System Hacking: FAT32 Deep Dive
  ],
 ),
 dict(name="USB: Reverse Engineering and Writing Drivers", kind="Build",
  desc="Book: USB Complete by Jan Axelson",
  videos=[
   "is9wVOKeIjQ",  # 2022-02-26 [stream] USB: Reverse Engineering and Writing Drivers
   "7Zo3bdaqfbo",  # 2022-03-12 [stream] More USB Reverse Engineering + Drivers
  ],
 ),
 dict(name="Exploring the FT232H and Node Native Addons", kind="Build",
  desc="[stream] Exploring the FT232H and Node Native Addons.",
  videos=[
   "DJ-SO0d3sYY",  # 2022-03-27 [stream] Exploring the FT232H and Node Native Addons
  ],
 ),
 dict(name="The End Of Low Level JavaScript", kind="Build",
  desc="Low Level JavaScript is no more.",
  videos=[
   "cpb02XgX_FA",  # 2022-10-09 The End Of Low Level JavaScript
  ],
 ),
 dict(name="Binary Patching", kind="Build",
  desc="In this video, we're taking a deep dive into the IPS format, and building a compliant parser and patcher in the C programming language!",
  videos=[
   "R-TGJ-9QSP4",  # 2022-10-20 Binary Patching: How The IPS Format Works
   "EDsW08Z-Iak",  # 2022-11-01 ROM Hacking: Exploring The BPS Binary Patch Format
  ],
 ),
 dict(name="I wrote a GameBoy game in TypeScript", kind="Build",
  desc="I wrote a GameBoy game in TypeScript  (And it runs on real hardware!).",
  videos=[
   "TIlx5nBnx-o",  # 2022-11-28 I wrote a GameBoy game in TypeScript  (And it runs on real hardware!)
  ],
 ),
 dict(name="Dumping GameBoy Cartridges The INTERESTING Way", kind="Build",
  desc="In this video we're dumping GameBoy cartridges using a non-conventional method; One that uses the GameBoy itself to exfiltrate the data out from under it!",
  videos=[
   "rORPp6vYMsw",  # 2022-12-13 Dumping GameBoy Cartridges The INTERESTING Way
  ],
 ),
 dict(name="Hiding Data In Sound", kind="Build",
  desc="In this video, we're learning about steganography: the art of hiding data inside other data.",
  videos=[
   "sn9mKSpOcFM",  # 2023-01-19 Hiding Data In Sound
  ],
 ),
 dict(name="Bare Metal Programming Series 0", kind="Build",
  desc="This is episode 0 of the bare metal programming series!",
  videos=[
   "06ICtJjPKlA",  # 2023-03-12 Hello World Blinky! Bare Metal Programming Series 1
   "uQQsDWLRDuI",  # 2023-03-12 Bare Metal Programming Series 0
  ],
 ),
 dict(name="PWM and Timers", kind="Build",
  desc="in this episode of the bare metal programming series, we're examining PWM, or pulse width modulation: a technique for creating repeating square-wave like signals with a variable duty cycle.",
  videos=[
   "kHUGY05ImWU",  # 2023-04-09 PWM and Timers :: Bare Metal Programming Series 3
  ],
 ),
 dict(name="Worlds Simplest Bootloader", kind="Build",
  desc="Worlds Simplest Bootloader :: Bare Metal Programming Series 4.",
  videos=[
   "cfNJ85cX-ms",  # 2023-04-16 Worlds Simplest Bootloader :: Bare Metal Programming Series 4
  ],
 ),
 dict(name="Understanding Assembly Generated From C", kind="Build",
  desc="In this (micro) episode of the bare metal programming series, we're looking at different ways of expressing the same idea in C, and reading the resulting assembly code in order to make sense of any differences.",
  videos=[
   "nnnEy0w-l_A",  # 2023-04-22 Understanding Assembly Generated From C :: Bare Metal Programming Seri
  ],
 ),
 dict(name="UART Driver From Scratch", kind="Build",
  desc="In this episode of the bare metal programming series, we're building a UART driver - an API to the peripheral which will facilitate the fundamental communications we'll need for firmware updates in the bootloader!",
  videos=[
   "qSUbe_a54gY",  # 2023-04-30 UART Driver From Scratch :: Bare Metal Programming Series 5
  ],
 ),
 dict(name="Designing A Packet Protocol", kind="Build",
  desc="In this episode of the bare metal programming series, we're going over the design of a packet protocol, that runs on top of the UART physical layer we've been building up over the last few videos.",
  videos=[
   "VzOPdQukW1Q",  # 2023-05-15 Designing A Packet Protocol :: Bare Metal Programming Series 7.1
  ],
 ),
 dict(name="Bootloader Packet Protocol Implementation", kind="Build",
  desc="In this episode of the bare metal programming series, we're implementing the packet protocol we looked at in the previous video inside the bootloader.",
  videos=[
   "RrUyS-gixWk",  # 2023-05-22 Bootloader Packet Protocol Implementation :: Bare Metal Programming Se
  ],
 ),
 dict(name="Testing the Packet Protocol", kind="Build",
  desc="In this installment of the bare metal programming series, we're testing the packet protocol implementation we wrote in the bootloader, using a PC side application which will eventually become the firmware updater!",
  videos=[
   "rG1Faau2QuM",  # 2023-05-30 Testing the Packet Protocol :: Bare Metal Programming Series 7.3
  ],
 ),
 dict(name="Programmatic Flash Control", kind="Build",
  desc="In this installment of the bare metal programming series, we're diving into how the flash peripheral of the STM32F401 chip works, and building out a little layer to be able to write a new main application from the boo…",
  videos=[
   "QcE3Y_8hroU",  # 2023-06-06 Programmatic Flash Control :: Bare Metal Programming Series 8
  ],
 ),
 dict(name="Simple Timer API", kind="Build",
  desc="In this installment of the bare metal programming series, we're taking a minute to build a very simple timer API, allowing us to quickly setup, check, and reset software based timers - accounting for any drift that ma…",
  videos=[
   "g4TLA_R_Tk4",  # 2023-06-17 Simple Timer API :: Bare Metal Programming Series 9
  ],
 ),
 dict(name="Bootloader Firmware Update Mechanism", kind="Build",
  desc="In this episode, we're finally building the core firmware update mechanism in the bootloader!",
  videos=[
   "_hd6FITV_Hw",  # 2023-06-24 Bootloader Firmware Update Mechanism :: Bare Metal Programming Series 
  ],
 ),
 dict(name="First Successful Firmware Update", kind="Build",
  desc="In this episode, we're building the firmware updater application, which communicates with the bootloader in order to send a firmware update reliably over USB/UART.",
  videos=[
   "fnulMkctAWk",  # 2023-07-02 First Successful Firmware Update! :: Bare Metal Programming Series 11
  ],
 ),
 dict(name="Understanding AES Encryption Mechanics", kind="Build",
  desc="In this video we're taking some time to grok the mechanics of AES.",
  videos=[
   "OnhtzFJW_4I",  # 2023-07-29 Understanding AES Encryption Mechanics: BMPS
  ],
 ),
 dict(name="Cryptographically Signed Firmware", kind="Build",
  desc="In the final episode of the Bare Metal Programming Series, we're implementing signed firmware updates!",
  videos=[
   "Veu_fDPecM8",  # 2023-08-06 Cryptographically Signed Firmware :: Bare Metal Programming Series 14
  ],
 ),
 dict(name="How does an OS boot? //Source Dive// 001", kind="Build",
  desc="In this installment of //Source Dive//, we're learning about the xv6 Operating System; Specifically the low-level boot code that gets the CPU in the correct state to run the OS!",
  videos=[
   "KkenLT8S9Hs",  # 2023-09-09 How does an OS boot? //Source Dive// 001
  ],
 ),
 dict(name="What is a spinlock? //Source Dive// 002", kind="Build",
  desc="In this installment of //Source Dive//, we're back in the xv6 OS codebase, exploring timers, the early boot process, and a very useful concurrency primitive: The Spinlock!",
  videos=[
   "ZE9OODanrDA",  # 2023-09-16 What is a spinlock? //Source Dive// 002
  ],
 ),
 dict(name="Programmatic Painting", kind="Build",
  desc="In this video, we're drawing generative art in the form of flow fields!",
  videos=[
   "M_SUcX66SDA",  # 2023-09-23 Programmatic Painting: Flow Fields
  ],
 ),
 dict(name="Virtual Console and printf //Source Dive// 003", kind="Build",
  desc="In this installment of //Source Dive//, we're back in xv6, looking at how the operating system layers abstractions.",
  videos=[
   "uNp4DElDQyY",  # 2023-09-30 Virtual Console and printf() //Source Dive// 003
  ],
 ),
 dict(name="How does KERNEL memory allocation work? //Source Dive// 004", kind="Build",
  desc="In this installment of //Source Dive//, we're deep in the xv6 operating system, trying to understand how physical memory of the system is tracked, distributed, and returned to the kernel.",
  videos=[
   "NC_qkXznvkg",  # 2023-10-13 How does KERNEL memory allocation work? //Source Dive// 004
  ],
 ),
 dict(name="Turning Pixels Into Waves", kind="Build",
  desc="In this video, we're building an awesome graphical effect, where an image is processed into a series of animated waves.",
  videos=[
   "5vzMgNAzEuA",  # 2023-10-21 Turning Pixels Into Waves
  ],
 ),
 dict(name="The mechanics of VIRTUAL MEMORY //Source Dive// 005", kind="Build",
  desc="In this installment of //Source Dive//, we're back in xv6, learning how address translation works with the virtual memory subsystem.",
  videos=[
   "iTic6EV4DP8",  # 2023-10-28 The mechanics of VIRTUAL MEMORY //Source Dive// 005
  ],
 ),
 dict(name="Getting up in another processes memory", kind="Build",
  desc="In this video, we learn how we can read memory belonging to other processes by building a memory dumper from scratch.",
  videos=[
   "0ihChIaN8d0",  # 2023-11-04 Getting up in another processes memory
  ],
 ),
 dict(name="Bare Metal Bit Banging", kind="Build",
  desc="In this video, we examine the WS2812B RGB LED device, and write a bit-banged driver from scratch for an STM32 microcontroller.",
  videos=[
   "KUklOA91nk0",  # 2023-12-30 Bare Metal Bit Banging: WS2812B Driver
  ],
 ),
 dict(name="Rendering 3D Graphics On An Oscilloscope", kind="Build",
  desc="In this video, we're learning how to draw on an oscilloscope.",
  videos=[
   "TAfWea21ooM",  # 2024-03-08 Rendering 3D Graphics On An Oscilloscope
  ],
 ),
 dict(name="Fixed-point math is better than floating point", kind="Build",
  desc="In this video, we're learning about fixed-point: A different method for doing non-integer arithmetic without floats!",
  videos=[
   "i1phJl-0v54",  # 2024-06-22 Fixed-point math is better than floating point (sometimes)
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
