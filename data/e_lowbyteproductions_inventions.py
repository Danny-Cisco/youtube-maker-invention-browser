"""Curated inventions for Low Byte Productions (@lowbyteproductions).

Drafted by build/auto_inventions.py (long-form builds, series merged, descriptions in the maker's own words),
then reviewed. Every upload not listed here appears under "Other uploads" on the site.
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
  ],
 ),
 dict(name="Classes, mapping, and generic parsers", kind="Build",
  desc="In this episode we'll create a Parser class and implement map, a method that will allow us to apply arbitrary structure as we parse.",
  videos=[
   "xB7lFPMN4dU",  # 2019-08-06 Classes, mapping, and generic parsers [Parser Combinators From Scratch
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
 dict(name="Memory Access and Branching", kind="Build",
  desc="In this video we establish the core instruction set of the VM, give the VM the capabilities to read and write to main memory, and also to make decisions about how the program should proceed with branching instructions.",
  videos=[
   "wJ-pu6Iq0B8",  # 2019-10-15 Memory Access and Branching (16-Bit VM in JavaScript 002)
  ],
 ),
 dict(name="What is the Stack and why do we need it", kind="Build",
  desc="In this episode we understand what a stack is, how it can be implemented on the lowest level, and how it can then be harnessed to allow the Virtual Machine to run subroutines without losing state.",
  videos=[
   "mamop8aqFNk",  # 2019-10-31 What is the Stack and why do we need it? (16-Bit VM in JavaScript 003)
  ],
 ),
 dict(name="Implementing Stack Mechanics", kind="Build",
  desc="This series is all about building a powerful virtual machine in JavaScript with the following features:",
  videos=[
   "zAsn8q-X9HM",  # 2019-11-13 Implementing Stack Mechanics (16-Bit VM in JavaScript 004)
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
 dict(name="What is Memory Mapped I/O", kind="Build",
  desc="This this episode we implement memory mapped I/O, where the address space is utilised as common bus for components to communicate.",
  videos=[
   "hLYGTpvoMgE",  # 2019-12-25 What is Memory Mapped I/O? (16-Bit VM in JavaScript 005)
  ],
 ),
 dict(name="Making WAVs: Understanding, Parsing, and Creating WAV Files in JavaScr", kind="Build",
  desc="The WAVE file format is a binary format that encodes high fidelity audio data.",
  videos=[
   "udbA7u1zYfc",  # 2020-08-26 Making WAVs: Understanding, Parsing, and Creating WAV Files in JavaScr
  ],
 ),
 dict(name="How Do Regular Expressions Really Work", kind="Build",
  desc="In this video we're going to build a basic regular expression engine from scratch, in order to illustrate the underlying mechanisms that make them tick.",
  videos=[
   "u01jb8YN2Lw",  # 2020-10-20 How Do Regular Expressions Really Work?
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
   "ER7h4ZTe19A",  # 2021-10-07 Building The Worlds First CPU in TypeScript? (No Really!)
  ],
 ),
 dict(name="Hardware RISC-V CPU in TypeScript", kind="Build",
  desc="Hardware RISC-V CPU in TypeScript: First Steps.",
  videos=[
   "Vat4p2idDOA",  # 2021-10-07 Hardware RISC-V CPU in TypeScript: First Steps
  ],
 ),
 dict(name="Building an ENCODER for the \"Quite OK Image Format\"", kind="Build",
  desc="The \"Quite OK Image Format\" (qoi) is a lossless compression image format that has similar performance to PNG, but with substantially faster encoding and decoding, making it a great choice for embedded systems.",
  videos=[
   "GgsRQuGSrc0",  # 2021-12-25 Building an ENCODER for the "Quite OK Image Format" (QOI)
  ],
 ),
 dict(name="File System Hacking", kind="Build",
  desc="[stream] File System Hacking: Building A FAT32 Layer On Top Of The SD-Card Driver.",
  videos=[
   "GMkjey1FTe0",  # 2022-02-12 [stream] File System Hacking: Building A FAT32 Layer On Top Of The SD-
   "giVfqICb2J4",  # 2022-02-20 [stream] File System Hacking: FAT32 Deep Dive
  ],
 ),
 dict(name="USB: Reverse Engineering and Writing Drivers", kind="Build",
  desc="Book: USB Complete by Jan Axelson",
  videos=[
   "is9wVOKeIjQ",  # 2022-02-26 [stream] USB: Reverse Engineering and Writing Drivers
  ],
 ),
 dict(name="More USB Reverse Engineering + Drivers", kind="Build",
  desc="Book: USB Complete by Jan Axelson",
  videos=[
   "7Zo3bdaqfbo",  # 2022-03-12 [stream] More USB Reverse Engineering + Drivers
  ],
 ),
 dict(name="The End Of Low Level JavaScript", kind="Build",
  desc="Low Level JavaScript is no more.",
  videos=[
   "cpb02XgX_FA",  # 2022-10-09 The End Of Low Level JavaScript
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
 dict(name="Bare Metal Programming Series 0", kind="Build",
  desc="This is episode 0 of the bare metal programming series!",
  videos=[
   "uQQsDWLRDuI",  # 2023-03-12 Bare Metal Programming Series 0
  ],
 ),
 dict(name="Hello World Blinky! Bare Metal Programming Series 1", kind="Build",
  desc="This is episode 1 of the bare metal programming series!",
  videos=[
   "06ICtJjPKlA",  # 2023-03-12 Hello World Blinky! Bare Metal Programming Series 1
  ],
 ),
 dict(name="Interrupts and Memory Mapped I/O", kind="Build",
  desc="This is episode 2 of the bare metal programming series!",
  videos=[
   "S92ltJ0C59k",  # 2023-03-21 Interrupts and Memory Mapped I/O :: Bare Metal Programming Series 2
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
 dict(name="UART Driver From Scratch", kind="Build",
  desc="In this episode of the bare metal programming series, we're building a UART driver - an API to the peripheral which will facilitate the fundamental communications we'll need for firmware updates in the bootloader!",
  videos=[
   "qSUbe_a54gY",  # 2023-04-30 UART Driver From Scratch :: Bare Metal Programming Series 5
  ],
 ),
 dict(name="Interrupt Safe Ring Buffer", kind="Build",
  desc="In this episode of the bare metal programming series, we're building a ring buffer to back our UART driver.",
  videos=[
   "uIJnATS9j_0",  # 2023-05-08 Interrupt Safe Ring Buffer :: Bare Metal Programming Series 6
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
 dict(name="Fixed-point math is better than floating point", kind="Build",
  desc="In this video, we're learning about fixed-point: A different method for doing non-integer arithmetic without floats!",
  videos=[
   "i1phJl-0v54",  # 2024-06-22 Fixed-point math is better than floating point (sometimes)
  ],
 ),
]

OTHER = None  # None = every upload not assigned above
