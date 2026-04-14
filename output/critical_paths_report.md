# Game Boy (DMG-CPU B) Propagation Path Analysis

Static analysis of the DMG-CPU B gate-level netlist identifying deep
combinatorial paths that cause propagation delay on real hardware.
Data source: [msinger/dmg-schematics](https://github.com/msinger/dmg-schematics).

## Timing Reference

| Parameter | Value |
|-----------|-------|
| Master clock | 4.194304 MHz |
| T-cycle (one dot) | ~238.4 ns |
| Half T-cycle | ~119.2 ns |
| Gate delay (Sharp ~5 um CMOS) | 5-15 ns |
| Gate-equivalent counting | NOT=1, AND/OR=2, MUX=3, XOR=3, full_add=4 |

## Overview

**4102 cells** analyzed across the full DMG-CPU B chip
(974 registered,
2970 combinatorial).

| Category | Paths | Max Depth | Worst-case Delay |
|----------|-------|-----------|-----------------|
| **Operational** | 788 | 39 ge | 585 ns (491% half T-cycle) |
| Reset-only | 20 | 45 ge | 675 ns |
| **Total paths** | 808 | | |
| **Race pairs** | 975 (491 PPU) | max diff 51 | |

## Key Findings

### 1. The VRAM Address Adder Is the Deepest Operational Path

The longest operational combinatorial chain is the 8-bit ripple carry adder
that computes the VRAM tile map address from the current scanline (LY) plus
the scroll register (SCY or SCX). The carry propagates through a half_adder
+ 7 full_adders, each costing 4 gate-equivalents, for a total depth of ~32 ge.

This means the VRAM address may not settle until 160-480 ns after LY/SCY
change — well beyond one full T-cycle. In practice, the scroll registers
are stable for the entire scanline, so the adder output settles before the
first tile fetch. But mid-scanline SCX writes (used by some games for
split-scroll effects) may not take effect for 2+ dots.

### 2. CLKPIPE (sacu) Is the Critical Fan-out Bottleneck

The pixel pipe shift clock `sacu` (OR2 gate, depth 19, fan-out **53**)
drives every pixel-level decision: BG pipe shift, sprite pipe shift, sprite X
match, mask pipe, and pixel counter increment. All pipe data is ready at depth
0-5, but CLKPIPE arrives at depth ~19, creating a systematic race at every pipe DFF.

This is the single most impactful signal for emulator timing. A behavioral emulator
resolves CLKPIPE and data simultaneously, but on real hardware the pipe effectively
shifts 95-285 ns after data settles.

### 3. Sprite Store Races Are Universal and Severe

All 10 sprite stores exhibit identical timing races (diff=44).
The sprite control signal (from the Y comparator carry chain) arrives at
depth 44 while OAM data arrives at depth 0.
At scanline boundaries, the stores may capture stale data instead of
clearing, causing wrong sprite position, tile index, or attribute flags
for one dot at the start of the next scanline.

### 4. Sprite X Match Has Massive Depth Differential

The 112 sprite X comparator races (max diff=43) arise because
the X comparison depends on the pixel counter, which is clocked by CLKPIPE.
The comparator output settles at a different time than the pixel pipe data,
causing sprites to potentially trigger fetch one dot early or late.

### 5. Window Trigger Races Affect Split-screen Games

Window logic has 30 races (max diff=17). The WX/WY comparison
and window activation signals race against the rendering pipeline, potentially
shifting window content by one pixel. This affects games that use the window
for status bars or dialogue boxes.

## Critical Paths by Functional Area

| Area | Paths | Max Depth | Max Delay | Key Race |
|------|-------|-----------|-----------|----------|
| Sprite Control | 3 | 39 ge | 585 ns | diff=33 (17 races) |
| test | 17 | 32 ge | 480 ns | diff=12 (8 races) |
| bus | 432 | 32 ge | 480 ns | diff=27 (55 races) |
| VRAM Interface | 37 | 29 ge | 435 ns | diff=3 (8 races) |
| Sprite X Priority | 10 | 27 ge | 405 ns | diff=23 (10 races) |
| Data Bus | 16 | 19 ge | 285 ns | diff=9 (8 races) |
| DMA | 2 | 16 ge | 240 ns | diff=17 (21 races) |
| Timer | 9 | 15 ge | 225 ns | diff=16 (21 races) |
| apu-ch2 | 22 | 15 ge | 225 ns | diff=17 (56 races) |
| apu-ch1 | 41 | 15 ge | 225 ns | diff=51 (102 races) |
| apu-ch4 | 15 | 15 ge | 225 ns | diff=17 (68 races) |
| apu-ch3 | 24 | 15 ge | 225 ns | diff=17 (59 races) |
| Address Bus | 16 | 15 ge | 225 ns | diff=12 (15 races) |
| LCD Output | 10 | 14 ge | 210 ns | diff=11 (17 races) |
| STAT/LY | 8 | 13 ge | 195 ns | diff=18 (33 races) |
| Sprite Pixel Shifter | 16 | 9 ge | 135 ns | diff=19 (16 races) |
| BG/Win Cycles | 3 | 8 ge | 120 ns | diff=20 (20 races) |
| Window Logic | 1 | 7 ge | 105 ns | diff=17 (30 races) |
| Clock Distribution | 1 | 6 ge | 90 ns | diff=14 (21 races) |
| apu-control | 1 | 5 ge | 75 ns | diff=16 (27 races) |
| Serial | 5 | 5 ge | 75 ns | diff=14 (17 races) |
| Joypad | 12 | 3 ge | 45 ns | diff=12 (11 races) |
| bootrom | 1 | 2 ge | 30 ns | diff=10 (1 races) |
| Sprite X Match | 80 | 1 ge | 15 ns | diff=43 (112 races) |
| OAM Interface | 6 | 1 ge | 15 ns | diff=4 (1 races) |

## High Fan-out Signals (>= 20 outputs)

These signals drive many downstream gates. High fan-out combined with deep
combinatorial depth means the signal arrives late at many destinations simultaneously.

| Signal | Fan-out | Depth | Cell Type | Category |
|--------|---------|-------|-----------|----------|
| `keba` | 100 | 8 ge | not_x6 | apu-control |
| `sacu` | 53 | 19 ge | or2 | ppu-cycles |
| `alur` | 48 | 3 ge | not_x2 | clocks |
| `bus:d0` | 46 | 0 ge |  | bus |
| `bus:d1` | 44 | 0 ge |  | bus |
| `bus:d2` | 43 | 0 ge |  | bus |
| `cpu` | 42 | 6 ge | sm83 |  |
| `bus:d6` | 41 | 0 ge |  | bus |
| `bus:d7` | 41 | 0 ge |  | bus |
| `bus:d4` | 40 | 0 ge |  | bus |
| `bus:d3` | 39 | 0 ge |  | bus |
| `bus:d5` | 39 | 0 ge |  | bus |
| `bogy` | 37 | 13 ge | not_x6 | apu-control |
| `unor` | 34 | 3 ge | and2 | test |
| `tova` | 32 | 4 ge | not_x1 | bus-adr |
| `aguz` | 30 | 10 ge | not_x6 | apu-control |
| `adad` | 29 | 1 ge | not_x4 | apu-ch1 |
| `cunu` | 24 | 5 ge | not_x2 | ppu-control |
| `xymu` | 23 | 0 ge | nor_latch | ppu-stat |
| `bus:a1` | 23 | 0 ge |  | bus |

## APU Timing

The APU has 312 timing races (max diff=51). These are primarily
in the channel frequency counters and length timers, where the CPU data bus
write path races against the channel's internal clock. APU timing races are
less audible than PPU races are visible, but may affect cycle-accurate audio
emulation — particularly for games that modify channel registers mid-note.

## Implications for Emulator Developers

### What This Analysis Shows

Behavioral emulators resolve all combinatorial logic instantaneously within a
single tick. On real hardware, signals propagate through chains of gates with
finite delay. When two signals that should be sampled simultaneously arrive at
different depths, the hardware captures a value that differs from what an
emulator computes — typically by one dot (one T-cycle).

### What to Do About It

1. **CLKPIPE races**: The pixel pipe shift clock arrives ~19 gate-equivalents
   late. Consider delaying pipe shift by one dot relative to data loading.
2. **Sprite store races**: All 10 stores have identical races. If sprite
   position is off by one dot at scanline start, this is the likely cause.
3. **Scroll adder latency**: Mid-scanline SCX writes take 2+ dots to affect
   the VRAM address. Don't apply scroll changes instantly.
4. **Window activation**: Window trigger may fire one dot late. If window
   content is shifted right by one pixel, this is the likely cause.
5. **Mode transitions**: The mode 2→3 and mode 3→0 boundaries may shift by
   one dot due to OAM scan done and tile fetch completion races.
