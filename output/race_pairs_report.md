# Signal Race Pair Analysis

Total race pairs identified: 880

Race pairs are registered nodes where data inputs arrive at significantly
different combinatorial depths (diff >= 3 gates, max >= 4). On real hardware,
the late-arriving signal may not settle before the register samples, causing
behavior to differ from behavioral emulation by one dot.

PPU-related races: 463


## apu-ch1 (88 races)

### `cyto` (nor_latch) — diff=42, max=42
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bery` | 42 | or4 | apu-ch1 |
| `feku` | 0 | dffr | apu-ch1 |

### `havo` (dffsr) — diff=39, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `gyfu` | 16 | nor2 | apu-ch1 |
| `golo` | 14 | nand2 | apu-ch1 |
| `jule` | 4 | full_add | apu-ch1 |

### `hyka` (dffsr) — diff=38, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `efor` | 16 | nor2 | apu-ch1 |
| `gylu` | 14 | nand2 | apu-ch1 |
| `guxa` | 5 | full_add | apu-ch1 |

### `edul` (dffsr) — diff=35, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `gamo` | 16 | nor2 | apu-ch1 |
| `gope` | 14 | nand2 | apu-ch1 |
| `jory` | 8 | full_add | apu-ch1 |

### `fely` (dffsr) — diff=31, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `kapo` | 16 | nor2 | apu-ch1 |
| `kovu` | 14 | nand2 | apu-ch1 |
| `hexo` | 12 | full_add | apu-ch1 |

### `hopo` (dffsr) — diff=29, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `etek` | 24 | full_add | apu-ch1 |
| `esel` | 16 | nor2 | apu-ch1 |
| `etol` | 14 | nand2 | apu-ch1 |

### `jyka` (dffsr) — diff=29, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `gato` | 16 | nor2 | apu-ch1 |
| `geta` | 14 | nand2 | apu-ch1 |

### `holu` (dffsr) — diff=29, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `geva` | 16 | full_add | apu-ch1 |
| `kaju` | 16 | nor2 | apu-ch1 |
| `kypa` | 14 | nand2 | apu-ch1 |

### `hyxu` (dffsr) — diff=29, max=43
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boje` | 43 | and2 | apu-ch1 |
| `fego` | 20 | full_add | apu-ch1 |
| `eluf` | 16 | nor2 | apu-ch1 |
| `eler` | 14 | nand2 | apu-ch1 |

### `evab` (dffsr) — diff=27, max=41
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 41 | and3 | apu-ch1 |
| `dule` | 32 | full_add | apu-ch1 |
| `bovu` | 16 | nor2 | apu-ch1 |
| `budo` | 14 | nand2 | apu-ch1 |

### `dygy` (dffsr) — diff=27, max=41
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 41 | and3 | apu-ch1 |
| `dyxe` | 28 | full_add | apu-ch1 |
| `boxu` | 16 | nor2 | apu-ch1 |
| `bugu` | 14 | nand2 | apu-ch1 |

### `axan` (dffsr) — diff=27, max=41
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `buso` | 41 | and3 | apu-ch1 |
| `coru` | 36 | full_add | apu-ch1 |
| `apaj` | 16 | nor2 | apu-ch1 |
| `afeg` | 14 | nand2 | apu-ch1 |

### `boko` (drlatch_ee) — diff=15, max=15
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bamu` | 15 | not_x1 | apu-ch1 |
| `bage` | 14 | nand2 | apu-ch1 |
| `camy` | 9 | not_x1 | apu-ch1 |
| `bus:d6` | 0 |  | bus |

### `jusa` (drlatch_ee) — diff=14, max=14
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kygy` | 14 | not_x1 | apu-ch1 |
| `hafu` | 13 | and2 | apu-ch1 |
| `hato` | 9 | not_x1 | apu-ch1 |
| `bus:d0` | 0 |  | bus |

### `jaty` (drlatch_ee) — diff=14, max=14
Category: apu-ch1

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kagy` | 14 | not_x2 | apu-ch1 |
| `gaxu` | 13 | and2 | apu-ch1 |
| `hato` | 9 | not_x1 | apu-ch1 |
| `bus:d4` | 0 |  | bus |


## bus (40 races)

### `bus:~ma9` () — diff=27, max=32
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dafe` | 32 | not_if0 | ppu-bgscroll |
| `vulo` | 9 | not_if0 | ppu-window |
| `rese` | 7 | not_if0 | ppu-vram |
| `duve` | 6 | not_if0 | ppu-dma |
| `gotu` | 6 | not_if0 | ppu-ycomp |
| `reso` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma4` () — diff=27, max=32
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ajan` | 32 | not_if0 | ppu-bgscroll |
| `wuju` | 9 | not_if0 | ppu-window |
| `xeca` | 7 | not_if0 | ppu-vram |
| `famu` | 7 | not_if0 | ppu-ycomp |
| `damu` | 6 | not_if0 | ppu-dma |
| `vapy` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma8` () — diff=23, max=28
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ceta` | 28 | not_if0 | ppu-bgscroll |
| `vovo` | 9 | not_if0 | ppu-window |
| `rysu` | 7 | not_if0 | ppu-vram |
| `evax` | 6 | not_if0 | ppu-dma |
| `wune` | 6 | not_if0 | ppu-ycomp |
| `roha` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma3` () — diff=22, max=28
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `coly` | 28 | not_if0 | ppu-bgscroll |
| `dode` | 12 | not_if0 | ppu-bgscroll |
| `xulo` | 9 | not_if0 | ppu-window |
| `xody` | 7 | not_if0 | ppu-vram |
| `wolu` | 6 | not_if0 | ppu-window |
| `agag` | 6 | not_if0 | ppu-ycomp |
| `fyzy` | 6 | not_if0 | ppu-dma |

### `bus:~ma7` () — diff=19, max=24
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cypo` | 24 | not_if0 | ppu-bgscroll |
| `vace` | 9 | not_if0 | ppu-window |
| `xybo` | 7 | not_if0 | ppu-vram |
| `erew` | 6 | not_if0 | ppu-dma |
| `wyga` | 6 | not_if0 | ppu-ycomp |
| `rusa` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma2` () — diff=18, max=24
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alel` | 24 | not_if0 | ppu-bgscroll |
| `xahe` | 9 | not_if0 | ppu-window |
| `dahu` | 8 | not_if0 | ppu-bgscroll |
| `xyne` | 7 | not_if0 | ppu-vram |
| `wawe` | 6 | not_if0 | ppu-window |
| `aras` | 6 | not_if0 | ppu-ycomp |
| `fuhe` | 6 | not_if0 | ppu-dma |

### `bus:d7` () — diff=17, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `beda` | 18 | not_if0 |  |
| `tewa` | 17 | buf_if0 | bus-data |
| `raru` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `gazo` | 1 | not_if0 | apu-ch2 |

### `bus:d6` () — diff=17, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `arar` | 18 | not_if0 |  |
| `tazu` | 17 | buf_if0 | bus-data |
| `ryke` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `efab` | 1 | not_if1 | serial |

### `bus:d4` () — diff=17, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `benu` | 18 | not_if0 |  |
| `tahy` | 17 | buf_if0 | bus-data |
| `reka` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `pegy` | 1 | not_if1 | int |

### `bus:d1` () — diff=16, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataj` | 18 | not_if0 |  |
| `sosa` | 17 | buf_if0 | bus-data |
| `ryne` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `desy` | 2 | not_if1 | apu-ch3 |

### `bus:d2` () — diff=16, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ajec` | 18 | not_if0 |  |
| `sedu` | 17 | buf_if0 | bus-data |
| `rejy` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `ypon` | 2 | buf_if0 | ppu-ycomp |

### `bus:d3` () — diff=16, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `asuz` | 18 | not_if0 |  |
| `taxo` | 17 | buf_if0 | bus-data |
| `rase` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `koge` | 2 | not_if0 | apu-control |

### `bus:d5` () — diff=16, max=18
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `akaj` | 18 | not_if0 |  |
| `tesu` | 17 | buf_if0 | bus-data |
| `rowe` | 15 | not_if1 | bus-data |
| `cpu` | 4 | sm83 |  |
| `deve` | 2 | buf_if0 | ppu-xcomp |

### `bus:~ma6` () — diff=15, max=20
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `case` | 20 | not_if0 | ppu-bgscroll |
| `veha` | 9 | not_if0 | ppu-window |
| `xopo` | 7 | not_if0 | ppu-vram |
| `eteg` | 6 | not_if0 | ppu-dma |
| `gavo` | 6 | not_if0 | ppu-ycomp |
| `vejy` | 5 | not_if1 | ppu-bgfifo |

### `bus:~ma1` () — diff=14, max=20
Category: bus

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `afeb` | 20 | not_if0 | ppu-bgscroll |
| `xamo` | 9 | not_if0 | ppu-window |
| `evad` | 8 | not_if0 | ppu-bgscroll |
| `xuxu` | 7 | not_if0 | ppu-vram |
| `wudo` | 6 | not_if0 | ppu-window |
| `baxe` | 6 | not_if0 | ppu-ycomp |
| `egez` | 6 | not_if0 | ppu-dma |


## Sprite Store (98 races)

### `fofo` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehen` | 24 | not_x1 | ppu-objctl |
| `faka` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `dysy` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehen` | 24 | not_x1 | ppu-objctl |
| `faka` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `xufo` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wara` | 24 | not_x1 | ppu-objctl |
| `wufa` | 23 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0 |  | bus |

### `yzor` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wara` | 24 | not_x1 | ppu-objctl |
| `wufa` | 23 | not_x1 | ppu-objctl |
| `bus:oam_render_a3` | 0 |  | bus |

### `zury` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zesy` | 24 | not_x1 | ppu-objctl |
| `xyha` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `zylu` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zesy` | 24 | not_x1 | ppu-objctl |
| `xyha` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `zene` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zesy` | 24 | not_x1 | ppu-objctl |
| `xyha` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `dese` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 24 | not_x1 | ppu-objctl |
| `feka` | 23 | not_x1 | ppu-objctl |
| `bus:oam_render_a3` | 0 |  | bus |

### `dafu` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ebeb` | 24 | not_x1 | ppu-objctl |
| `feka` | 23 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0 |  | bus |

### `ykuk` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wuma` | 24 | not_x1 | ppu-objctl |
| `fuke` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store3` | 0 |  | bus |

### `xazy` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wuma` | 24 | not_x1 | ppu-objctl |
| `fuke` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |

### `xosy` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wuma` | 24 | not_x1 | ppu-objctl |
| `fuke` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store1` | 0 |  | bus |

### `byhu` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `beke` | 24 | not_x1 | ppu-objctl |
| `buzy` | 23 | not_x1 | ppu-objctl |
| `bus:oam_render_a3` | 0 |  | bus |

### `boxa` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `beke` | 24 | not_x1 | ppu-objctl |
| `buzy` | 23 | not_x1 | ppu-objctl |
| `bus:oam_render_a7` | 0 |  | bus |

### `bozu` (dlatch_ee) — diff=24, max=24
Category: ppu-objreg

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `doby` | 24 | not_x1 | ppu-objctl |
| `enob` | 23 | not_x1 | ppu-objctl |
| `bus:sprite_y_store2` | 0 |  | bus |


## Sprite X Match (107 races)

### `xexa` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 24 | not_x1 | ppu-objctl |
| `weme` | 23 | not_x1 | ppu-objctl |
| `dosy` | 21 | not_x1 | ppu-xprio |
| `yvok` | 1 | not_x1 | ppu-xcomp |

### `fyty` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 24 | not_x1 | ppu-objctl |
| `cacu` | 23 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |

### `xere` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 24 | not_x1 | ppu-objctl |
| `weme` | 23 | not_x1 | ppu-objctl |
| `dosy` | 21 | not_x1 | ppu-xprio |
| `zocy` | 1 | not_x1 | ppu-xcomp |

### `depy` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 24 | not_x1 | ppu-objctl |
| `cacu` | 23 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `yzof` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 24 | not_x1 | ppu-objctl |
| `weme` | 23 | not_x1 | ppu-objctl |
| `dosy` | 21 | not_x1 | ppu-xprio |
| `bady` | 1 | not_x1 | ppu-xcomp |

### `fuby` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 24 | not_x1 | ppu-objctl |
| `cacu` | 23 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `ypur` | 1 | not_x1 | ppu-xcomp |

### `xuzo` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 24 | not_x1 | ppu-objctl |
| `weme` | 23 | not_x1 | ppu-objctl |
| `dosy` | 21 | not_x1 | ppu-xprio |
| `ypur` | 1 | not_x1 | ppu-xcomp |

### `yrop` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 24 | not_x1 | ppu-objctl |
| `weme` | 23 | not_x1 | ppu-objctl |
| `dosy` | 21 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `ejuf` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 24 | not_x1 | ppu-objctl |
| `cacu` | 23 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `arop` | 1 | not_x1 | ppu-xcomp |

### `duhy` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 24 | not_x1 | ppu-objctl |
| `cacu` | 23 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `ypod` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 24 | not_x1 | ppu-objctl |
| `weme` | 23 | not_x1 | ppu-objctl |
| `dosy` | 21 | not_x1 | ppu-xprio |
| `cose` | 1 | not_x1 | ppu-xcomp |

### `xepe` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gery` | 24 | not_x1 | ppu-objctl |
| `fuxu` | 23 | not_x1 | ppu-objctl |
| `zago` | 1 | not_x1 | ppu-xcomp |

### `foka` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 24 | not_x1 | ppu-objctl |
| `cacu` | 23 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `zago` | 1 | not_x1 | ppu-xcomp |

### `enor` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `code` | 24 | not_x1 | ppu-objctl |
| `cacu` | 23 | not_x1 | ppu-objctl |
| `gamy` | 21 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |

### `ynep` (drlatch_ee) — diff=23, max=24
Category: ppu-xcomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wyxa` | 24 | not_x1 | ppu-objctl |
| `weme` | 23 | not_x1 | ppu-objctl |
| `dosy` | 21 | not_x1 | ppu-xprio |
| `xatu` | 1 | not_x1 | ppu-xcomp |


## BG Pixel Shifter (32 races)

### `nozo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nexa` | 22 | nand2 | ppu-bgfifo |
| `nyxo` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `myde` | 0 | dffsr | ppu-bgfifo |

### `taca` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `seno` | 22 | nand2 | ppu-bgfifo |
| `soly` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `tomy` | 0 | dffsr | ppu-bgfifo |

### `moju` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lutu` | 22 | nand2 | ppu-bgfifo |
| `loto` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nozo` | 0 | dffsr | ppu-bgfifo |

### `sady` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruce` | 22 | nand2 | ppu-bgfifo |
| `sure` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `taca` | 0 | dffsr | ppu-bgfifo |

### `macu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lydu` | 22 | nand2 | ppu-bgfifo |
| `luja` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `moju` | 0 | dffsr | ppu-bgfifo |

### `rysa` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryja` | 22 | nand2 | ppu-bgfifo |
| `sebo` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `sady` | 0 | dffsr | ppu-bgfifo |

### `nepo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myvy` | 22 | nand2 | ppu-bgfifo |
| `mosy` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `macu` | 0 | dffsr | ppu-bgfifo |

### `sobo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ruto` | 22 | nand2 | ppu-bgfifo |
| `suca` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `rysa` | 0 | dffsr | ppu-bgfifo |

### `modu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lodo` | 22 | nand2 | ppu-bgfifo |
| `leru` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nepo` | 0 | dffsr | ppu-bgfifo |

### `setu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `raja` | 22 | nand2 | ppu-bgfifo |
| `sywe` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `sobo` | 0 | dffsr | ppu-bgfifo |

### `neda` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyha` | 22 | nand2 | ppu-bgfifo |
| `nute` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `modu` | 0 | dffsr | ppu-bgfifo |

### `ralu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rajo` | 22 | nand2 | ppu-bgfifo |
| `supu` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `setu` | 0 | dffsr | ppu-bgfifo |

### `pybo` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nady` | 22 | nand2 | ppu-bgfifo |
| `naja` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `neda` | 0 | dffsr | ppu-bgfifo |

### `sohu` (dffsr) — diff=22, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryjy` | 22 | nand2 | ppu-bgfifo |
| `raga` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `ralu` | 0 | dffsr | ppu-bgfifo |

### `myde` (dffsr) — diff=20, max=22
Category: ppu-bgfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `laky` | 22 | nand2 | ppu-bgfifo |
| `loty` | 22 | nand2 | ppu-bgfifo |
| `sacu` | 2 | or2 | ppu-cycles |


## Sprite X Priority (10 races)

### `exuq` (dffr) — diff=21, max=25
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `foxa` | 25 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wapo` (dffr) — diff=19, max=23
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gutu` | 23 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `womy` (dffr) — diff=17, max=21
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xoja` | 21 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `wafy` (dffr) — diff=15, max=19
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gega` | 19 | nor2 | ppu-xprio |
| `byva` | 17 | not_x1 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `fono` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `guze` | 10 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `egav` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `emol` | 6 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `eboj` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `guva` | 8 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `cedy` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `enut` | 11 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `gota` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `gyfy` | 15 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |

### `xudy` (dffr) — diff=13, max=17
Category: ppu-xprio

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byva` | 17 | not_x1 | ppu-xprio |
| `gono` | 17 | nor2 | ppu-xprio |
| `wuty` | 4 | not_x2 | ppu-ycomp |


## Sprite Control (16 races)

### `besu` (nor_latch) — diff=21, max=21
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `asen` | 21 | or2 | ppu-objctl |
| `catu` | 0 | dffr | ppu-objctl |

### `doba` (dffr) — diff=17, max=17
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 17 | not_x1 | ppu-objctl |
| `alet` | 7 | not_x2 | ppu-control |
| `byba` | 0 | dffr | ppu-objctl |

### `byba` (dffr) — diff=16, max=17
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bagy` | 17 | not_x1 | ppu-objctl |
| `feto` | 2 | and4 | ppu-objctl |
| `xupy` | 1 | not_x2 | ppu-oam |

### `cuxy` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `bese` | 0 | dffr | ppu-objctl |

### `faha` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `elyn` | 0 | dffr | ppu-objctl |

### `bego` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `cuxy` | 0 | dffr | ppu-objctl |

### `fony` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `faha` | 0 | dffr | ppu-objctl |

### `dybe` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `bego` | 0 | dffr | ppu-objctl |

### `wewy` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `yfel` | 0 | dffr | ppu-objctl |

### `goso` (dffr) — diff=15, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `wewy` | 0 | dffr | ppu-objctl |

### `dezy` (dffr) — diff=13, max=19
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyty` | 19 | not_x2 | ppu-objctl |
| `xapo` | 9 | not_x2 | ppu-control |
| `zeme` | 6 | not_x4 | ppu-control |

### `bese` (dffr) — diff=13, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `azyb` | 15 | not_x1 | ppu-objctl |
| `cake` | 2 | or2 | ppu-objctl |

### `yfel` (dffr) — diff=11, max=15
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `anom` | 15 | nor2 | ppu-objctl |
| `gava` | 4 | or2 | ppu-objctl |

### `anel` (dffr) — diff=11, max=11
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `abez` | 11 | not_x1 | ppu-objctl |
| `awoh` | 2 | not_x1 | ppu-objctl |
| `catu` | 0 | dffr | ppu-objctl |

### `ceno` (dffr) — diff=11, max=11
Category: ppu-objctl

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `abez` | 11 | not_x1 | ppu-objctl |
| `xupy` | 1 | not_x2 | ppu-oam |
| `besu` | 0 | nor_latch | ppu-objctl |


## BG/Win Cycles (18 races)

### `mesu` (dffr) — diff=20, max=20
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 20 | nor3 | ppu-cycles |
| `laxu` | 0 | dffr | ppu-cycles |

### `lony` (nand_latch) — diff=18, max=20
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nyxu` | 20 | nor3 | ppu-cycles |
| `lury` | 2 | and2 | ppu-cycles |

### `paho` (dffr) — diff=16, max=16
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roxo` | 16 | not_x1 | ppu-cycles |
| `xydo` | 0 | dffr | ppu-stat |
| `xymu` | 0 | nor_latch | ppu-stat |

### `pynu` (nor_latch) — diff=16, max=16
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xofo` | 16 | nand3 | ppu-cycles |
| `nunu` | 0 | dffr | ppu-cycles |

### `nyka` (dffr) — diff=15, max=22
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 22 | not_x1 | ppu-cycles |
| `alet` | 7 | not_x2 | ppu-control |

### `lovy` (dffr) — diff=14, max=22
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyry` | 22 | not_x1 | ppu-cycles |
| `nyxu` | 20 | nor3 | ppu-cycles |
| `myvo` | 8 | not_x1 | ppu-cycles |

### `ryku` (dffr) — diff=13, max=17
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pecu` | 17 | nand2 | ppu-cycles |
| `paso` | 4 | nor2 | ppu-cycles |

### `pyco` (dffr) — diff=9, max=16
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `roco` | 16 | not_x1 | ppu-cycles |
| `xapo` | 9 | not_x2 | ppu-control |
| `nuko` | 7 | not_x1 | ppu-window |

### `nunu` (dffr) — diff=9, max=9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xapo` | 9 | not_x2 | ppu-control |
| `mehe` | 8 | not_x1 | ppu-cycles |
| `pyco` | 0 | dffr | ppu-cycles |

### `nopa` (dffr) — diff=9, max=9
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xapo` | 9 | not_x2 | ppu-control |
| `alet` | 7 | not_x2 | ppu-control |
| `pynu` | 0 | nor_latch | ppu-cycles |

### `nyze` (dffr) — diff=8, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `moxe` | 8 | not_x1 | ppu-cycles |
| `puxa` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `ryfa` (dffr) — diff=8, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pany` | 8 | nor2 | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `pory` (dffr) — diff=8, max=8
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myvo` | 8 | not_x1 | ppu-cycles |
| `nyka` | 0 | dffr | ppu-cycles |

### `rene` (dffr) — diff=7, max=7
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alet` | 7 | not_x2 | ppu-control |
| `ryfa` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |

### `lyzu` (dffr) — diff=7, max=7
Category: ppu-cycles

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `alet` | 7 | not_x2 | ppu-control |
| `laxu` | 0 | dffr | ppu-cycles |
| `xymu` | 0 | nor_latch | ppu-stat |


## Window Logic (31 races)

### `wody` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wyka` | 0 | dffr | ppu-window |

### `wobo` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wody` | 0 | dffr | ppu-window |

### `wyko` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wobo` | 0 | dffr | ppu-window |

### `xolo` (dffr) — diff=17, max=17
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xaco` | 17 | not_x1 | ppu-cycles |
| `wyko` | 0 | dffr | ppu-window |

### `myce` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d5` | 0 |  | bus |

### `mypa` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d0` | 0 |  | bus |

### `noke` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d2` | 0 |  | bus |

### `nofe` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d1` | 0 |  | bus |

### `muvo` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d6` | 0 |  | bus |

### `meby` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d3` | 0 |  | bus |

### `nuku` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d7` | 0 |  | bus |

### `mypu` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mare` | 15 | not_x1 | ppu-window |
| `voxu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d4` | 0 |  | bus |

### `nene` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 15 | not_x1 | ppu-window |
| `vefu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d5` | 0 |  | bus |

### `nulo` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 15 | not_x1 | ppu-window |
| `vefu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d4` | 0 |  | bus |

### `nyro` (drlatch_ee) — diff=15, max=15
Category: ppu-window

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `nuta` | 15 | not_x1 | ppu-window |
| `vefu` | 14 | not_x1 | ppu-window |
| `walu` | 7 | not_x2 | ppu-window |
| `bus:d1` | 0 |  | bus |


## STAT/LY (29 races)

### `rupo` (nor_latch) — diff=16, max=16
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pago` | 16 | or2 | ppu-stat |
| `ropo` | 0 | dffr | ppu-stat |

### `rufo` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d4` | 0 |  | bus |

### `roxe` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d3` | 0 |  | bus |

### `refe` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d5` | 0 |  | bus |

### `rugu` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pupu` | 15 | not_x1 | ppu-stat |
| `ryve` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d6` | 0 |  | bus |

### `sota` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d4` | 0 |  | bus |

### `raha` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d7` | 0 |  | bus |

### `syry` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d0` | 0 |  | bus |

### `vevo` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d6` | 0 |  | bus |

### `sedy` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d2` | 0 |  | bus |

### `vuce` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d1` | 0 |  | bus |

### `salo` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d3` | 0 |  | bus |

### `vafa` (drlatch_ee) — diff=15, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voze` | 15 | not_x1 | ppu-stat |
| `wane` | 14 | not_x1 | ppu-stat |
| `wesy` | 7 | not_x2 | ppu-stat |
| `bus:d5` | 0 |  | bus |

### `tuhu` (dffr) — diff=14, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 15 | nor2 | ppu-stat |
| `toca` | 1 | not_x1 | ppu-stat |

### `tuky` (dffr) — diff=14, max=15
Category: ppu-stat

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tady` | 15 | nor2 | ppu-stat |
| `sake` | 3 | xor | ppu-stat |
| `toca` | 1 | not_x1 | ppu-stat |


## Sprite Y Compare (21 races)

### `sobu` (dffr) — diff=15, max=24
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `teky` | 24 | and4 | ppu-ycomp |
| `tava` | 9 | not_x1 | ppu-ycomp |

### `tese` (dffr) — diff=15, max=15
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `seca` | 15 | nor3 | ppu-ycomp |
| `tuly` | 0 | dffr | ppu-ycomp |

### `zaxe` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d4` | 0 |  | bus |

### `wone` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d3` | 0 |  | bus |

### `yses` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d6` | 0 |  | bus |

### `zeca` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d7` | 0 |  | bus |

### `ydyv` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d0` | 0 |  | bus |

### `xafu` (dlatch) — diff=13, max=13
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bode` | 13 | not_x1 | ppu-oam |
| `bus:~oam_b_d5` | 0 |  | bus |

### `xote` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `yses` | 0 | dlatch | ppu-ycomp |

### `xuso` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `ydyv` | 0 | dlatch | ppu-ycomp |

### `xyju` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `wone` | 0 | dlatch | ppu-ycomp |

### `ybog` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `zaxe` | 0 | dlatch | ppu-ycomp |

### `yjex` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `zuca` | 0 | dlatch | ppu-ycomp |

### `yzab` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `zeca` | 0 | dlatch | ppu-ycomp |

### `wyso` (dlatch_ee) — diff=11, max=11
Category: ppu-ycomp

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ysum` | 11 | not_x1 | ppu-ycomp |
| `ywok` | 10 | not_x1 | ppu-ycomp |
| `xafu` | 0 | dlatch | ppu-ycomp |


## DMA (20 races)

### `nydo` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d3` | 0 |  | bus |

### `para` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d2` | 0 |  | bus |

### `nafa` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d0` | 0 |  | bus |

### `nygy` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d4` | 0 |  | bus |

### `maru` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d7` | 0 |  | bus |

### `pyne` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d1` | 0 |  | bus |

### `poku` (dlatch_ee) — diff=15, max=15
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pysu` | 15 | not_x1 | ppu-dma |
| `loru` | 14 | not_x1 | ppu-dma |
| `bus:d6` | 0 |  | bus |

### `luvy` (dffr) — diff=13, max=14
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lupa` | 14 | nor2 | ppu-dma |
| `cunu` | 5 | not_x2 | ppu-control |
| `uvyt` | 1 | not_x2 | clocks |

### `wuje` (nor_latch) — diff=10, max=13
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xuto` | 13 | and2 | ppu-oam |
| `xyny` | 3 | not_x1 | ppu-dma |

### `pyro` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `naky` | 0 | dffr | ppu-dma |

### `nefy` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `pyro` | 0 | dffr | ppu-dma |

### `muty` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `nefy` | 0 | dffr | ppu-dma |

### `nyko` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `muty` | 0 | dffr | ppu-dma |

### `pylo` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `nyko` | 0 | dffr | ppu-dma |

### `nuto` (dffr) — diff=7, max=7
Category: ppu-dma

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lapa` | 7 | not_x1 | ppu-dma |
| `pylo` | 0 | dffr | ppu-dma |


## BG Scrolling (16 races)

### `cabu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `bake` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `daty` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `gubo` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d3` | 0 |  | bus |

### `bemy` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `cyxu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `cuzy` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d5` | 0 |  | bus |

### `duzu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bofo` | 15 | not_x1 | ppu-bgscroll |
| `amun` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `foha` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `fezu` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `fymo` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `fujo` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d3` | 0 |  | bus |

### `gave` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `dede` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `funy` (drlatch_ee) — diff=15, max=15
Category: ppu-bgscroll

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ehor` | 15 | not_x1 | ppu-bgscroll |
| `cavo` | 14 | not_x1 | ppu-bgscroll |
| `cunu` | 5 | not_x2 | ppu-control |
| `bus:d7` | 0 |  | bus |


## Palettes (24 races)

### `pavo` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d0` | 0 |  | bus |

### `mogy` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d6` | 0 |  | bus |

### `mena` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d7` | 0 |  | bus |

### `muke` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d4` | 0 |  | bus |

### `pylu` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d2` | 0 |  | bus |

### `moru` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d5` | 0 |  | bus |

### `nusy` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d1` | 0 |  | bus |

### `maxy` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfa` | 15 | not_x1 | ppu-pal |
| `tepo` | 14 | not_x1 | ppu-pal |
| `bus:d3` | 0 |  | bus |

### `xana` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 15 | not_x1 | ppu-pal |
| `xelo` | 14 | not_x1 | ppu-pal |
| `bus:d7` | 0 |  | bus |

### `xeru` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 15 | not_x1 | ppu-pal |
| `xelo` | 14 | not_x1 | ppu-pal |
| `bus:d4` | 0 |  | bus |

### `xuky` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 15 | not_x1 | ppu-pal |
| `xelo` | 14 | not_x1 | ppu-pal |
| `bus:d1` | 0 |  | bus |

### `xova` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 15 | not_x1 | ppu-pal |
| `xelo` | 14 | not_x1 | ppu-pal |
| `bus:d2` | 0 |  | bus |

### `xufu` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 15 | not_x1 | ppu-pal |
| `xelo` | 14 | not_x1 | ppu-pal |
| `bus:d0` | 0 |  | bus |

### `xalo` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 15 | not_x1 | ppu-pal |
| `xelo` | 14 | not_x1 | ppu-pal |
| `bus:d3` | 0 |  | bus |

### `xupo` (dlatch_ee) — diff=15, max=15
Category: ppu-pal

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xojo` | 15 | not_x1 | ppu-pal |
| `xelo` | 14 | not_x1 | ppu-pal |
| `bus:d6` | 0 |  | bus |


## PPU Control (8 races)

### `xona` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d7` | 0 |  | bus |

### `vyxe` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d0` | 0 |  | bus |

### `wexu` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d4` | 0 |  | bus |

### `xylo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d1` | 0 |  | bus |

### `xymo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d2` | 0 |  | bus |

### `woky` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d6` | 0 |  | bus |

### `xafo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d3` | 0 |  | bus |

### `wymo` (drlatch_ee) — diff=15, max=15
Category: ppu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `xure` | 15 | not_x1 | ppu-control |
| `xubo` | 14 | not_x1 | ppu-control |
| `xare` | 7 | not_x1 | ppu-control |
| `bus:d5` | 0 |  | bus |


## Other (3 races)

### `high_ram` (high_ram) — diff=15, max=15
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `wuly` | 15 | not_x2 | hram |
| `abev` | 13 | not_x2 | hram |
| `apuh` | 11 | not_x2 | hram |
| `anyk` | 10 | not_x1 | hram |
| `apow` | 9 | not_x2 | hram |
| `wuta` | 4 | not_x2 | hram |
| `ajom` | 3 | and2 | hram |
| `axyc` | 3 | and2 | hram |
| `avub` | 3 | and2 | hram |
| `apul` | 2 | and2 | hram |
| `weju` | 1 | not_x1 | hram |
| `wady` | 1 | not_x1 | hram |
| `woce` | 1 | not_x1 | hram |
| `webe` | 1 | not_x1 | hram |
| `wehu` | 1 | not_x1 | hram |
| `bus:a6` | 0 |  | bus |
| `bus:a5` | 0 |  | bus |
| `bus:a4` | 0 |  | bus |
| `bus:a3` | 0 |  | bus |
| `bus:a2` | 0 |  | bus |

### `boot_rom` (boot_rom) — diff=12, max=12
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zoku` | 12 | not_x1 | bootrom |
| `zery` | 11 | not_x1 | bootrom |
| `zyro` | 4 | not_x1 | bootrom |
| `zefu` | 4 | not_x1 | bootrom |
| `zete` | 4 | not_x1 | bootrom |
| `zapa` | 3 | not_x1 | bootrom |
| `zovy` | 3 | and2 | bootrom |
| `zyga` | 3 | and2 | bootrom |
| `zyky` | 3 | and2 | bootrom |
| `zuko` | 2 | and2 | bootrom |
| `zoke` | 1 | not_x1 | bootrom |
| `zabu` | 1 | not_x1 | bootrom |
| `zage` | 1 | not_x1 | bootrom |
| `zyra` | 1 | not_x1 | bootrom |
| `bus:a7` | 0 |  | bus |
| `bus:a6` | 0 |  | bus |
| `bus:a3` | 0 |  | bus |
| `bus:a2` | 0 |  | bus |

### `wave_ram` (wave_ram) — diff=6, max=6
Category: 

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ymul` | 6 | or2 | apu-ch3 |
| `bus:d0` | 0 |  | bus |
| `bus:d6` | 0 |  | bus |
| `bus:d7` | 0 |  | bus |


## apu-ch2 (50 races)

### `emer` (drlatch_ee) — diff=15, max=15
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `duso` | 15 | not_x1 | apu-ch2 |
| `evyf` | 14 | nand2 | apu-ch2 |
| `fazo` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `fore` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d3` | 0 |  | bus |

### `gufe` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d5` | 0 |  | bus |

### `hore` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `jede` | 14 | not_x1 | apu-ch2 |
| `gere` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d1` | 0 |  | bus |

### `hyfu` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `jede` | 14 | not_x1 | apu-ch2 |
| `gere` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d0` | 0 |  | bus |

### `gura` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `hava` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `jede` | 14 | not_x1 | apu-ch2 |
| `gere` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d2` | 0 |  | bus |

### `gata` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d4` | 0 |  | bus |

### `goda` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 14 | not_x1 | apu-ch2 |
| `exuc` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d5` | 0 |  | bus |

### `fora` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d4` | 0 |  | bus |

### `fome` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d3` | 0 |  | bus |

### `gumy` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fyxo` | 14 | not_x1 | apu-ch2 |
| `exuc` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d6` | 0 |  | bus |

### `fova` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d1` | 0 |  | bus |

### `fedy` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d2` | 0 |  | bus |

### `fofe` (drlatch_ee) — diff=14, max=14
Category: apu-ch2

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `esur` | 14 | not_x2 | apu-ch2 |
| `dosa` | 13 | and2 | apu-ch2 |
| `hude` | 9 | not_x1 | apu-ch2 |
| `bus:d0` | 0 |  | bus |


## apu-ch4 (64 races)

### `cuny` (drlatch_ee) — diff=15, max=15
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `cazo` | 15 | not_x1 | apu-ch4 |
| `dulu` | 14 | nand2 | apu-ch4 |
| `cabe` | 9 | not_x1 | apu-ch4 |
| `bus:d6` | 0 |  | bus |

### `gedu` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d7` | 0 |  | bus |

### `etyj` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 14 | not_x1 | apu-ch4 |
| `daco` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d1` | 0 |  | bus |

### `gozo` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d6` | 0 |  | bus |

### `goky` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d5` | 0 |  | bus |

### `ezyk` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 14 | not_x1 | apu-ch4 |
| `daco` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d2` | 0 |  | bus |

### `geky` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `fupa` | 14 | not_x2 | apu-ch4 |
| `goko` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d3` | 0 |  | bus |

### `emok` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dyke` | 14 | not_x1 | apu-ch4 |
| `daco` | 13 | and2 | apu-ch4 |
| `fexo` | 9 | not_x1 | apu-ch4 |
| `bus:d0` | 0 |  | bus |

### `jaky` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 14 | not_x2 | apu-ch4 |
| `humo` | 13 | and2 | apu-ch4 |
| `kame` | 9 | not_x1 | apu-control |
| `bus:d2` | 0 |  | bus |

### `jare` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 14 | not_x2 | apu-ch4 |
| `humo` | 13 | and2 | apu-ch4 |
| `kame` | 9 | not_x1 | apu-control |
| `bus:d0` | 0 |  | bus |

### `jero` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hova` | 14 | not_x2 | apu-ch4 |
| `humo` | 13 | and2 | apu-ch4 |
| `kame` | 9 | not_x1 | apu-control |
| `bus:d1` | 0 |  | bus |

### `fyto` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d5` | 0 |  | bus |

### `gafo` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d7` | 0 |  | bus |

### `feta` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d4` | 0 |  | bus |

### `gogo` (drlatch_ee) — diff=14, max=14
Category: apu-ch4

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `efug` | 14 | not_x2 | apu-ch4 |
| `getu` | 13 | and2 | apu-ch4 |
| `dapa` | 9 | not_x2 | apu-control |
| `bus:d6` | 0 |  | bus |


## apu-ch3 (46 races)

### `hoto` (drlatch_ee) — diff=15, max=15
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gygu` | 15 | not_x1 | apu-ch3 |
| `fovo` | 14 | nand2 | apu-ch3 |
| `heky` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `gage` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `elas` | 14 | not_x2 | apu-ch2 |
| `enuf` | 13 | and2 | apu-ch2 |
| `jybu` | 9 | not_x1 | apu-ch2 |
| `bus:d7` | 0 |  | bus |

### `guxe` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `gucy` | 14 | not_x1 | apu-ch3 |
| `gejo` | 13 | and2 | apu-ch3 |
| `gove` | 9 | not_x1 | apu-ch3 |
| `bus:d7` | 0 |  | bus |

### `hody` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 14 | not_x1 | apu-ch3 |
| `haga` | 13 | and2 | apu-ch3 |
| `guro` | 9 | not_x1 | apu-ch3 |
| `bus:d5` | 0 |  | bus |

### `huky` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `guzu` | 14 | not_x1 | apu-ch3 |
| `haga` | 13 | and2 | apu-ch3 |
| `guro` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `jovy` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d1` | 0 |  | bus |

### `kana` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 14 | not_x1 | apu-ch3 |
| `kota` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d6` | 0 |  | bus |

### `kogu` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 14 | not_x1 | apu-ch3 |
| `kota` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d7` | 0 |  | bus |

### `jefe` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d3` | 0 |  | bus |

### `jove` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kyho` | 14 | not_x1 | apu-ch3 |
| `kota` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d5` | 0 |  | bus |

### `jypo` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d4` | 0 |  | bus |

### `jaxa` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d2` | 0 |  | bus |

### `koga` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `kuly` | 14 | not_x2 | apu-ch3 |
| `jafa` | 13 | and2 | apu-ch3 |
| `kuha` | 9 | not_x1 | apu-ch3 |
| `bus:d0` | 0 |  | bus |

### `jety` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 14 | not_x1 | apu-ch3 |
| `huda` | 13 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d1` | 0 |  | bus |

### `jemo` (drlatch_ee) — diff=14, max=14
Category: apu-ch3

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `hufa` | 14 | not_x1 | apu-ch3 |
| `huda` | 13 | and2 | apu-ch3 |
| `kopy` | 9 | not_x1 | apu-ch3 |
| `bus:d0` | 0 |  | bus |


## Interrupts (8 races)

### `ubul` (dffsr) — diff=14, max=14
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuny` | 14 | and3 | int |
| `tome` | 12 | nand3 | int |
| `caly` | 0 | dffr | serial |

### `nybo` (dffsr) — diff=14, max=14
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pyga` | 14 | and3 | int |
| `pyhu` | 12 | nand3 | int |
| `moba` | 0 | dffr | timer |

### `lope` (dffsr) — diff=11, max=14
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyta` | 14 | and3 | int |
| `myzu` | 12 | nand3 | int |
| `vypu` | 3 | not_x3 | ppu-stat |

### `nejy` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `ubul` | 0 | dffsr | int |

### `pavy` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `nybo` | 0 | dffsr | int |

### `maty` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `lope` | 0 | dffsr | int |

### `mopo` (dlatch) — diff=8, max=8
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rolo` | 8 | nand4 | int |
| `lalu` | 0 | dffsr | int |

### `lalu` (dffsr) — diff=5, max=17
Category: int

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `voty` | 17 | not_x3 | ppu-stat |
| `movu` | 14 | and3 | int |
| `mody` | 12 | nand3 | int |


## apu-control (27 races)

### `byga` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 14 | not_x2 | apu-control |
| `bowe` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d1` | 0 |  | bus |

### `ager` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 14 | not_x2 | apu-control |
| `bowe` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d2` | 0 |  | bus |

### `bumo` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d5` | 0 |  | bus |

### `atuf` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d3` | 0 |  | bus |

### `anev` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d0` | 0 |  | bus |

### `bepu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 14 | not_x2 | apu-control |
| `byfa` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d7` | 0 |  | bus |

### `bofa` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 14 | not_x2 | apu-control |
| `byfa` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d5` | 0 |  | bus |

### `bedu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d7` | 0 |  | bus |

### `bafo` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d2` | 0 |  | bus |

### `apos` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 14 | not_x2 | apu-control |
| `bowe` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d3` | 0 |  | bus |

### `befo` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acyj` | 14 | not_x2 | apu-control |
| `byfa` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d6` | 0 |  | bus |

### `bogu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `acup` | 14 | not_x2 | apu-control |
| `bono` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d1` | 0 |  | bus |

### `byre` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d4` | 0 |  | bus |

### `apeg` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ataf` | 14 | not_x2 | apu-control |
| `bowe` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d0` | 0 |  | bus |

### `cozu` (drlatch_ee) — diff=14, max=14
Category: apu-control

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `bubu` | 14 | not_x2 | apu-control |
| `baxy` | 13 | not_x2 | apu-control |
| `kepy` | 7 | not_x3 | apu-control |
| `bus:d6` | 0 |  | bus |


## Timer (20 races)

### `peda` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pyma` | 13 | nor2 | timer |
| `rage` | 0 | tffnl | timer |

### `nuga` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pagu` | 13 | nor2 | timer |
| `peda` | 0 | tffnl | timer |

### `povy` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `nero` | 13 | nor2 | timer |
| `rega` | 0 | tffnl | timer |

### `peru` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `nada` | 13 | nor2 | timer |
| `povy` | 0 | tffnl | timer |

### `rate` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `repa` | 13 | nor2 | timer |
| `peru` | 0 | tffnl | timer |

### `ruby` (tffnl) — diff=13, max=13
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mexu` | 13 | nand3 | timer |
| `rolu` | 13 | nor2 | timer |
| `rate` | 0 | tffnl | timer |

### `samy` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sara` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `sabo` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sara` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d2` | 0 |  | bus |

### `sopu` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `sara` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `peto` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d6` | 0 |  | bus |

### `nyke` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `tyru` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d4` | 0 |  | bus |

### `muru` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d2` | 0 |  | bus |

### `tyva` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d3` | 0 |  | bus |

### `sufy` (dffr) — diff=10, max=10
Category: timer

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tyju` | 10 | nand4 | timer |
| `alur` | 3 | not_x2 | clocks |
| `bus:d5` | 0 |  | bus |


## Clock Distribution (18 races)

### `teka` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `subu` | 0 | dffr | clocks |

### `ufor` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `ukup` | 0 | dffr | clocks |

### `uket` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `teka` | 0 | dffr | clocks |

### `uner` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `ufor` | 0 | dffr | clocks |

### `upof` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `uket` | 0 | dffr | clocks |

### `tero` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `uner` | 0 | dffr | clocks |

### `unyk` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `tero` | 0 | dffr | clocks |

### `tama` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `unyk` | 0 | dffr | clocks |

### `tulu` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `ugot` | 0 | dffr | clocks |

### `tugo` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `tulu` | 0 | dffr | clocks |

### `tofe` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `tugo` | 0 | dffr | clocks |

### `teru` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `tofe` | 0 | dffr | clocks |

### `sola` (dffr) — diff=12, max=12
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ufol` | 12 | nor3 | clocks |
| `teru` | 0 | dffr | clocks |

### `afer` (dffr_cc) — diff=11, max=11
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boma` | 11 | not_x6 | clocks |
| `boga` | 10 | not_x6 | clocks |
| `upoj` | 2 | nand3 | test |
| `asol` | 0 | nor_latch | clocks |

### `afur` (drlatch_ee) — diff=4, max=4
Category: clocks

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `adeh` | 4 | not_x1 | clocks |
| `atal` | 3 | not_x2 | clocks |
| `upoj` | 2 | nand3 | test |
| `adyk` | 0 | drlatch_ee | clocks |


## Serial (13 races)

### `eder` (dffsr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `eguv` | 12 | oa21 | serial |
| `efef` | 12 | nand2 | serial |
| `epyt` | 4 | not_x2 | serial |
| `erod` | 0 | dffsr | serial |

### `cylo` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 12 | and2 | serial |
| `cafa` | 0 | dffr | serial |

### `cyde` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 12 | and2 | serial |
| `cylo` | 0 | dffr | serial |

### `caly` (dffr) — diff=12, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 12 | and2 | serial |
| `cyde` | 0 | dffr | serial |

### `cafa` (dffr) — diff=10, max=12
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `caro` | 12 | and2 | serial |
| `dawa` | 2 | or2 | serial |

### `culy` (dffr) — diff=10, max=10
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 10 | nand4 | serial |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `coty` (dffr) — diff=9, max=10
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `uwam` | 10 | nand4 | serial |
| `uvyn` | 1 | not_x1 | clocks |

### `degu` (dffsr) — diff=6, max=6
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dawe` | 6 | not_x2 | serial |
| `cuba` | 0 | dffsr | serial |

### `dyra` (dffsr) — diff=6, max=6
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dawe` | 6 | not_x2 | serial |
| `degu` | 0 | dffsr | serial |

### `dojo` (dffsr) — diff=6, max=6
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `dawe` | 6 | not_x2 | serial |
| `dyra` | 0 | dffsr | serial |

### `dovu` (dffsr) — diff=4, max=4
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `epyt` | 4 | not_x2 | serial |
| `dojo` | 0 | dffsr | serial |

### `ejab` (dffsr) — diff=4, max=4
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `epyt` | 4 | not_x2 | serial |
| `dovu` | 0 | dffsr | serial |

### `erod` (dffsr) — diff=4, max=4
Category: serial

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `epyt` | 4 | not_x2 | serial |
| `ejab` | 0 | dffsr | serial |


## LCD Output (17 races)

### `nype` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `talu` | 1 | not_x4 | ppu-lcd |
| `rutu` | 0 | dffr | ppu-lcd |

### `myta` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `noko` | 2 | and4 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `typo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `saxo` | 0 | dffr | ppu-lcd |

### `vyzo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `typo` | 0 | dffr | ppu-lcd |

### `telu` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `vyzo` | 0 | dffr | ppu-lcd |

### `sude` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `telu` | 0 | dffr | ppu-lcd |

### `taha` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `sude` | 0 | dffr | ppu-lcd |

### `tyry` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `taha` | 0 | dffr | ppu-lcd |

### `meda` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `neru` | 1 | nor8 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `popu` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `xyvo` | 2 | and2 | ppu-lcd |
| `nype` | 0 | dffr | ppu-lcd |

### `napo` (dffr) — diff=11, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `popu` | 0 | dffr | ppu-lcd |

### `luca` (dffr) — diff=10, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `lofu` | 1 | not_x1 | ppu-lcd |

### `saxo` (dffr) — diff=10, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mude` | 11 | nor2 | ppu-lcd |
| `talu` | 1 | not_x4 | ppu-lcd |

### `rutu` (dffr) — diff=9, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `sono` | 2 | not_x1 | ppu-lcd |

### `sygu` (dffr) — diff=9, max=11
Category: ppu-lcd

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lyfe` | 11 | not_x1 | ppu-lcd |
| `tegy` | 3 | nand4 | ppu-lcd |
| `sono` | 2 | not_x1 | ppu-lcd |


## Address Bus (14 races)

### `lonu` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a13` | 0 |  | bus |

### `alor` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a0` | 0 |  | bus |

### `pate` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a10` | 0 |  | bus |

### `lobu` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a12` | 0 |  | bus |

### `nyre` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a14` | 0 |  | bus |

### `lumy` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a11` | 0 |  | bus |

### `lysa` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a9` | 0 |  | bus |

### `luno` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a8` | 0 |  | bus |

### `apur` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a1` | 0 |  | bus |

### `alyr` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a2` | 0 |  | bus |

### `aret` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a3` | 0 |  | bus |

### `avys` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a4` | 0 |  | bus |

### `atev` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a5` | 0 |  | bus |

### `aros` (dlatch) — diff=10, max=10
Category: bus-adr

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `mate` | 10 | not_x1 | bus-adr |
| `bus:a6` | 0 |  | bus |


## Joypad (11 races)

### `acef` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `batu` | 0 | dffr | joypad |

### `agem` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `acef` | 0 | dffr | joypad |

### `apug` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `alur` | 3 | not_x2 | clocks |
| `agem` | 0 | dffr | joypad |

### `kely` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d4` | 0 |  | bus |

### `cofy` (dffr) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d5` | 0 |  | bus |

### `keja` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p12` | 0 | pad_bidir_pu | joypad |

### `kolo` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p13` | 0 | pad_bidir_pu | joypad |

### `kevu` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p10` | 0 | pad_bidir_pu | joypad |

### `kapa` (dlatch) — diff=10, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `byzo` | 10 | not_x1 | joypad |
| `p11` | 0 | pad_bidir_pu | joypad |

### `awob` (dlatch) — diff=8, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `kery` | 2 | or4 | joypad |

### `batu` (dffr) — diff=8, max=10
Category: joypad

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `boga` | 10 | not_x6 | clocks |
| `kery` | 2 | or4 | joypad |


## test (7 races)

### `amut` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 10 | nand5 | test |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `buro` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `aper` | 10 | nand5 | test |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `kecy` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d1` | 0 |  | bus |

### `kuko` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d6` | 0 |  | bus |

### `keru` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d7` | 0 |  | bus |

### `jute` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d0` | 0 |  | bus |

### `kyme` (dffr) — diff=10, max=10
Category: test

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `atoz` | 10 | nand4 | joypad |
| `alur` | 3 | not_x2 | clocks |
| `bus:d3` | 0 |  | bus |


## Sprite Pixel Shifter (8 races)

### `maso` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `myto` | 9 | nand2 | ppu-objfifo |
| `mada` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `nuro` | 0 | dffsr | ppu-objfifo |

### `lefe` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lela` | 9 | nand2 | ppu-objfifo |
| `lyde` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `maso` | 0 | dffsr | ppu-objfifo |

### `lesu` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lufy` | 9 | nand2 | ppu-objfifo |
| `mame` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `lefe` | 0 | dffsr | ppu-objfifo |

### `wyho` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `vexu` | 9 | nand2 | ppu-objfifo |
| `xato` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `lesu` | 0 | dffsr | ppu-objfifo |

### `wora` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `vaby` | 9 | nand2 | ppu-objfifo |
| `xexu` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `wyho` | 0 | dffsr | ppu-objfifo |

### `vafo` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `tuxa` | 9 | nand2 | ppu-objfifo |
| `tupe` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `wora` | 0 | dffsr | ppu-objfifo |

### `vupy` (dffsr) — diff=9, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `teso` | 9 | nand2 | ppu-objfifo |
| `tula` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |
| `vanu` | 0 | dffsr | ppu-objfifo |

### `nuro` (dffsr) — diff=7, max=9
Category: ppu-objfifo

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `pabe` | 9 | nand2 | ppu-objfifo |
| `pyzu` | 9 | nand2 | ppu-objfifo |
| `sacu` | 2 | or2 | ppu-cycles |


## Data Bus (8 races)

### `selo` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d3` | 0 | pad_bidir_pu | bus-data |

### `raxy` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d2` | 0 | pad_bidir_pu | bus-data |

### `rony` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d1` | 0 | pad_bidir_pu | bus-data |

### `sazy` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d7` | 0 | pad_bidir_pu | bus-data |

### `soma` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d0` | 0 | pad_bidir_pu | bus-data |

### `sago` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d5` | 0 | pad_bidir_pu | bus-data |

### `sody` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d4` | 0 | pad_bidir_pu | bus-data |

### `rupa` (dlatch) — diff=7, max=7
Category: bus-data

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `lavo` | 7 | nand3 | bus-data |
| `d6` | 0 | pad_bidir_pu | bus-data |


## OAM Interface (1 races)

### `maka` (dffr) — diff=4, max=6
Category: ppu-oam

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `zeme` | 6 | not_x4 | ppu-control |
| `cunu` | 5 | not_x2 | ppu-control |
| `caty` | 2 | not_x1 | ppu-oam |


## VRAM Interface (7 races)

### `md2` (pad_bidir_pu) — diff=3, max=27
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `razo` | 27 | not_x2 | ppu-vram |
| `rare` | 26 | not_x2 | ppu-vram |
| `rofa` | 24 | not_x2 | ppu-vram |

### `md4` (pad_bidir_pu) — diff=3, max=27
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryro` | 27 | not_x2 | ppu-vram |
| `rube` | 26 | not_x2 | ppu-vram |
| `rofa` | 24 | not_x2 | ppu-vram |

### `md3` (pad_bidir_pu) — diff=3, max=27
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rada` | 27 | not_x2 | ppu-vram |
| `rodu` | 26 | not_x2 | ppu-vram |
| `rofa` | 24 | not_x2 | ppu-vram |

### `md7` (pad_bidir_pu) — diff=3, max=27
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryze` | 27 | not_x2 | ppu-vram |
| `rady` | 26 | not_x2 | ppu-vram |
| `rofa` | 24 | not_x2 | ppu-vram |

### `md1` (pad_bidir_pu) — diff=3, max=27
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `ryky` | 27 | not_x2 | ppu-vram |
| `ruly` | 26 | not_x2 | ppu-vram |
| `rofa` | 24 | not_x2 | ppu-vram |

### `md5` (pad_bidir_pu) — diff=3, max=27
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `revu` | 27 | not_x2 | ppu-vram |
| `rumu` | 26 | not_x2 | ppu-vram |
| `rofa` | 24 | not_x2 | ppu-vram |

### `md0` (pad_bidir_pu) — diff=3, max=27
Category: ppu-vram

| Input | Depth | Type | Category |
|-------|-------|------|----------|
| `rege` | 27 | not_x2 | ppu-vram |
| `rura` | 26 | not_x2 | ppu-vram |
| `rofa` | 24 | not_x2 | ppu-vram |
