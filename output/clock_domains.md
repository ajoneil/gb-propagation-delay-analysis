# Clock Domain Analysis

Structural analysis of the DMG-CPU B clock distribution network,
derived entirely from netlist connectivity.

Data source: [msinger/dmg-schematics](https://github.com/msinger/dmg-schematics).
No GateBoy-derived data is used — all classifications come from tracing
the `clk`/`ena`/`~ena` pin connectivity in the netlist.

## Clock Tree Overview

The DMG-CPU B has a single crystal oscillator (`ck1_ck2`) at 4.194 MHz.
All on-chip timing derives from this source through the following hierarchy:

```
Crystal (ck1_ck2, 4.194 MHz)
├── atal/adeh — 4 MHz complementary enables (via anos/avet feedback)
│   ├── Phase generators (AFUR/ALEF/APUK/ADYK) — drlatch_ee ring
│   │   ├── boga/boma — clk_1mhz / ~clk_1mhz
│   │   │   └── Drives: CPU, timer, joypad, APU registers
│   │   ├── bufa/byly — clk_t4 (write phase)
│   │   ├── bude/beva — data_phase
│   │   ├── bedo/bowa — exec_phase
│   │   └── buke — ~pch_phase (pixel clock)
│   └── azof — buffered 4 MHz (via zaxy/zeme/xyva)
│       ├── alet — PPU line timing
│       ├── xota — PPU video clock (non-inverted)
│       │   └── wuvu — video clock (dffr, clocked by xota)
│       │       └── vena — video clock (dffr, clocked by wuvu.~q)
│       └── xyfy — PPU video clock (inverted xota)
│           └── wosu — video clock (dffr, clocked by xyfy)
├── Timer divider chains (clk_1mhz → ukup → ufor → uner → ...)
│   └── 16 Hz to 262 kHz frequency outputs
└── Ripple counters (LY, BG fetch, sprite scan, APU)
```

## Summary

| Metric | Count |
|--------|-------|
| Total registered cells | 974 |
| With clock inputs traced | 944 |
| Without clock edges (SR latches) | 30 |
| Distinct clock configurations | 385 |

## Clock Domains by Root Source

Registers grouped by the root node of their clock chain (the registered
cell, pad, or boundary at the head of the combinational path driving their
clock pin). Roots with fewer than 3 registers are omitted (mostly ripple
counter chains).

| Root | Type | Clock Signals | Registers |
|------|------|--------------|-----------|
| `t1` (pad_in) | test-gated | 60 | 268 |
| `muwy` (dffr) | gated | 31 | 181 |
| `afer` (dffr_cc) | gated | 8 | 60 |
| `ck1_ck2` (pad_xtal) | crystal-derived | 18 | 35 |
| `byte` (dffr) | gated | 6 | 22 |
| `cpu` (sm83) | cpu-derived | 6 | 18 |
| `laxu` (dffr) | gated | 3 | 17 |
| `xymu` (nor_latch) | gated | 2 | 16 |
| `feta` (drlatch_ee) | gated | 4 | 16 |
| `anaz` (drlatch_ee) | gated | 4 | 12 |
| `avaf` (drlatch_ee) | gated | 2 | 11 |
| `wuvu` (dffr) | gated | 4 | 11 |
| `seba` (dffr) | gated | 1 | 10 |
| `coty` (dffr) | gated | 4 | 10 |
| `azus` (dffr) | gated | 4 | 8 |
| `ajer` (dffr) | ripple | 3 | 6 |
| `vena` (dffr) | gated | 2 | 6 |
| `caru` (dffr) | gated | 5 | 5 |
| `xydo` (dffr) | gated | 1 | 4 |
| `calo` (dffr) | gated | 2 | 4 |
| `bara` (dffr) | gated | 2 | 4 |
| `cery` (dffr) | gated | 3 | 4 |
| `bylu` (dffr) | gated | 4 | 4 |
| `cemo` (dffr) | ripple | 1 | 3 |
| `jeso` (dffr) | gated | 1 | 3 |
| `nype` (dffr) | ripple | 1 | 3 |
| `avok` (dffr) | gated | 3 | 3 |
| *194 other roots* | *ripple/gated* | *—* | *200* |

**Note on test-gated domains:** `t1` and `t2` are test pins held at static
logic levels during normal Game Boy operation. Registers whose clock chain
traces back to a test pin are actually clocked by the crystal-derived path
through the test gate — the test pin simply enables/disables the clock for
manufacturing test. In normal operation these registers behave identically
to crystal-derived registers; the test gate is always open.

**Note on `muwy` domain (181 registers):** `muwy` is LY bit 0 (the lowest
bit of the scanline counter). Its 181 registers are sprite store (100) and
sprite X match (80) banks, clocked by signals gated through the sprite Y
comparator chain. These registers update during OAM scan when the comparator
output (derived from the LY counter) enables the sprite store clock gates.

## Phase Generator Analysis

The CPU clock phase generators form a 4-stage `drlatch_ee` ring with
alternating enables. This is the core timing mechanism that determines
when registers throughout the chip update.

### Enable Signals

Both enables derive from the crystal via `ck1_ck2` → `anos` → `avet` → `atal`.
`adeh` is the complement of `atal` (a NOT gate).

| Latch | ena (transparent when high) | ~ena (transparent when low) | Data in | Data out |
|-------|---------------------------|---------------------------|---------|----------|
| `afur` | `atal` | `adeh` | `adyk.~q` | `alef.d` |
| `alef` | `adeh` | `atal` | `afur.q` | `apuk.d` |
| `apuk` | `atal` | `adeh` | `alef.q` | `adyk.d` |
| `adyk` | `adeh` | `atal` | `apuk.q` | `afur.d (via ~q)` |

When `atal` is high: `afur` and `apuk` are transparent (pass data through).
When `atal` is low (= `adeh` high): `alef` and `adyk` are transparent.

The ring shifts data each half-cycle of the 4 MHz clock, producing four
overlapping phase windows. Each latch's output drives combinational logic
that generates the clock distribution signals (`clk_1mhz`, `clk_t4`, etc.).

## PPU Video Clock Generators

The PPU has its own clock divider, separate from the CPU clock phases.
These are positive-edge-triggered `dffr` flip-flops derived from the
4 MHz buffered clock (`azof` → `zaxy` → `zeme` → `xyva` → `xota`/`xyfy`).

- **`wuvu`** (dffr): clocked by `xota` (positive edge)
- **`vena`** (dffr): clocked by `wuvu.~q` (inverted output → captures on wuvu falling edge)
- **`wosu`** (dffr): clocked by `xyfy` (inverted `xota` → captures on opposite edge to wuvu)

Note: `wosu` is NOT ripple-clocked from `wuvu`. It receives `wuvu.~q` as
its **data** input, but its clock comes independently from `xyfy`. This means
`wosu` samples `wuvu`'s output on the opposite clock edge, creating a
half-period timing constraint between them.

## Major Clock Groups

Clock signals driving 10 or more registers.

### `sacu` (or2) — 52 registers

Clock root: `afer` (dffr_cc) — gated, 16 gates deep — **inverted** from root

- **BG Pixel Shifter** (16): `macu`, `modu`, `moju`, `myde`, `neda`, `nepo`, `nozo`, `pybo`, `ralu`, `rysa`, `sady`, `setu`, `sobo`, `sohu`, `taca`, `tomy`
- **STAT/LY** (4): `savy`, `xeho`, `xodu`, `xydo`
- **Sprite Pixel Shifter** (16): `lefe`, `lesu`, `maso`, `naty`, `nuro`, `nylu`, `pefu`, `pyjo`, `vafo`, `vanu`, `vare`, `vupy`, `weba`, `wora`, `wufy`, `wyho`
- **Sprite X Match** (16): `lyme`, `moda`, `nuke`, `palu`, `rosa`, `rugo`, `sata`, `somy`, `vava`, `vezo`, `vosa`, `vumo`, `woda`, `wuru`, `wyfu`, `xete`

### `bode` (not_x1) — 16 registers

Clock root: `t1` (pad_in) — test-gated, 13 gates deep — **non-inverted** from root

- **Sprite X Match** (8): `cyra`, `eced`, `wyno`, `xyky`, `yrum`, `ysex`, `yvel`, `zuve`
- **Sprite Y Compare** (8): `wone`, `xafu`, `yceb`, `ydyv`, `yses`, `zaxe`, `zeca`, `zuca`

### `mate` (not_x1) — 15 registers

Clock root: `t1` (pad_in) — test-gated, 11 gates deep — **non-inverted** from root

- **Address Bus** (15): `alor`, `alyr`, `apur`, `aret`, `aros`, `arym`, `atev`, `avys`, `lobu`, `lonu`, `lumy`, `luno`, `lysa`, `nyre`, `pate`

### `wuty` (not_x2) — 10 registers

Clock source: `seba` → `tyno` → `vusa` → `wuty` — **non-inverted** from root

- **Sprite X Priority** (10): `cedy`, `eboj`, `egav`, `exuq`, `fono`, `gota`, `wafy`, `wapo`, `womy`, `xudy`

## Remaining Clock Groups (< 10 registers)

381 additional clock signals driving 851
registered cells. These are predominantly ripple counters (one register's
output clocking the next) and dedicated clock gates for small register banks.
Full details are in `clock_domains.json`.

## Emulation Implications

### Timing budgets for cross-domain paths

When a combinatorial path connects a source register to a sink register,
the available settling time depends on their clock relationship:

| Source → Sink Clocking | Available Budget | Notes |
|----------------------|-----------------|-------|
| Same clock signal | Full period (~238 ns) | Standard synchronous path |
| Same root, different gate | Depends on gate timing | Common in PPU — gate condition determines when path is live |
| atal → adeh (complementary) | Half period (~119 ns) | Phase generator cross-paths |
| Ripple chain | Parent CK→Q + budget | Ripple counters: child clocked by parent output |
| Unrelated domains | Async crossing | Rare on DMG; mainly CPU ↔ external |

### What this means for emulators

A behavioral emulator that updates all registers simultaneously on each
dot clock will get the right answer for same-domain paths. Cross-domain
paths are where real hardware may differ — the source register's output
may not have settled before the sink register samples it, causing the
sink to capture the *previous* value rather than the *current* one.

## Registers Without Clock Edges

These registered cells have no `clk`/`ena` inputs in the netlist.
They are SR latches whose timing is determined by their set/reset
input arrival times rather than a clock edge.

- **nand_latch** (7): `buta`, `femu`, `gexu`, `gugu`, `jery`, `lony`, `taka`
- **nor_latch** (23): `asol`, `besu`, `cyto`, `dala`, `dane`, `erox`, `fozu`, `fyfo`, `gena`, `gofy`, `hazo`, `jeme`, `kezu`, `lyxe`, `poky`, `pynu`, `rejo`, `roxy`, `rupo`, `tubo` … (+3 more)
