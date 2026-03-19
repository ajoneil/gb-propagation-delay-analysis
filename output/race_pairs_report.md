# Signal Race Pairs

A race pair occurs when a registered element (DFF/latch) has two or more inputs
that arrive at significantly different combinatorial depths. In real hardware,
the late-arriving signal may not be stable when the DFF samples. A behavioral
emulator resolves all inputs instantly, hiding this timing asymmetry.

> **How to read this:** A depth differential of N means one input passes through
> N more gates than another before reaching the same decision point. At 5-15 ns
> per gate, a differential of 10 means one signal arrives 50-150 ns later.

Found **547** operational race points (depth diff >= 3, excluding reset chains).

### Top Race Pairs by Depth Differential

| Decision Point | Type | Depth Diff | Phase | Late Signal (depth) | Early Signal (depth) | Observable Effect |
|----------------|------|-----------|-------|--------------------|--------------------|-------------------|
| `BESU_SCAN_DONEn_odd` | nor_latch | **17** | ODD | `ASEN_SCAN_DONE_tp_odd_new` (17) | `CATU_LINE_ENDp_odd` (0) | OAM scan extends one dot beyond expected boundary |
| `LOVY_TFETCH_DONEp` | dff17 | **17** | ODD | `NYXU_BFETCH_RSTn` (17) | `LYRY_BFETCH_DONEp_odd@old` (0) | Tile fetch pipeline stays active one dot too long |
| `MESU_BFETCH_S1p_odd` | dff17_any | **17** | ODD | `NYXU_BFETCH_RSTn` (17) | `LAXU_BFETCH_S0p_odd` (0) | Tile fetch state machine runs one extra cycle before reset |
| `NYVA_BFETCH_S2p_odd` | dff17_any | **17** | ODD | `NYXU_BFETCH_RSTn` (17) | `MESU_BFETCH_S1p_odd` (0) | Tile fetch state machine runs one extra cycle before reset |
| `LONY_TFETCHINGp` | nand_latch | **16** |  | `NYXU_BFETCH_RSTn` (17) | `LURY_BG_FETCH_DONEn` (1) | Tile fetch pipeline stays active one dot too long |
| `XEPE_STORE0_X0p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `ZAGO_SPX0n_old` (1) | Sprite store 0 X-position off by one dot |
| `YLAH_STORE0_X1p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `ZOCY_SPX1n_old` (1) | Sprite store 0 X-position off by one dot |
| `ZOLA_STORE0_X2p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `YPUR_SPX2n_old` (1) | Sprite store 0 X-position off by one dot |
| `ZULU_STORE0_X3p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `YVOK_SPX3n_old` (1) | Sprite store 0 X-position off by one dot |
| `WELO_STORE0_X4p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `COSE_SPX4n_old` (1) | Sprite store 0 X-position off by one dot |
| `XUNY_STORE0_X5p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `AROP_SPX5n_old` (1) | Sprite store 0 X-position off by one dot |
| `WOTE_STORE0_X6p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `XATU_SPX6n_old` (1) | Sprite store 0 X-position off by one dot |
| `XAKO_STORE0_X7p` | dff9 | **16** |  | `DYNA_STORE0_RSTn` (17) | `BADY_SPX7n_old` (1) | Sprite store 0 X-position off by one dot |
| `DANY_STORE1_X0p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `ZAGO_SPX0n_old` (1) | Sprite store 1 X-position off by one dot |
| `DUKO_STORE1_X1p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `ZOCY_SPX1n_old` (1) | Sprite store 1 X-position off by one dot |
| `DESU_STORE1_X2p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `YPUR_SPX2n_old` (1) | Sprite store 1 X-position off by one dot |
| `DAZO_STORE1_X3p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `YVOK_SPX3n_old` (1) | Sprite store 1 X-position off by one dot |
| `DAKE_STORE1_X4p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `COSE_SPX4n_old` (1) | Sprite store 1 X-position off by one dot |
| `CESO_STORE1_X5p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `AROP_SPX5n_old` (1) | Sprite store 1 X-position off by one dot |
| `DYFU_STORE1_X6p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `XATU_SPX6n_old` (1) | Sprite store 1 X-position off by one dot |
| `CUSY_STORE1_X7p` | dff9 | **16** |  | `DOKU_STORE1_RSTn` (17) | `BADY_SPX7n_old` (1) | Sprite store 1 X-position off by one dot |
| `FOKA_STORE2_X0p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `ZAGO_SPX0n_old` (1) | Sprite store 2 X-position off by one dot |
| `FYTY_STORE2_X1p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `ZOCY_SPX1n_old` (1) | Sprite store 2 X-position off by one dot |
| `FUBY_STORE2_X2p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `YPUR_SPX2n_old` (1) | Sprite store 2 X-position off by one dot |
| `GOXU_STORE2_X3p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `YVOK_SPX3n_old` (1) | Sprite store 2 X-position off by one dot |
| `DUHY_STORE2_X4p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `COSE_SPX4n_old` (1) | Sprite store 2 X-position off by one dot |
| `EJUF_STORE2_X5p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `AROP_SPX5n_old` (1) | Sprite store 2 X-position off by one dot |
| `ENOR_STORE2_X6p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `XATU_SPX6n_old` (1) | Sprite store 2 X-position off by one dot |
| `DEPY_STORE2_X7p` | dff9 | **16** |  | `GAMY_STORE2_RSTn` (17) | `BADY_SPX7n_old` (1) | Sprite store 2 X-position off by one dot |
| `XOLY_STORE3_X0p` | dff9 | **16** |  | `WUPA_STORE3_RSTn` (17) | `ZAGO_SPX0n_old` (1) | Sprite store 3 X-position off by one dot |

### Observable Effects Guide

Grouped by the visible symptom an emulator would exhibit if it resolves
these races instantaneously (as all behavioral emulators do).

#### OAM scan extends one dot beyond expected boundary

**Affected decision points:** 3 | **Max depth differential:** 17 gates (85-255 ns)

The scan-done signal (depth 17) races against line-end (depth 0). OAM evaluation continues for one extra dot, potentially including one additional sprite in the scanline sprite buffer. Affects the mode 2 → mode 3 transition point, which shifts all subsequent mode timings by one dot. Most visible with exactly 10 sprites on a line (the hardware limit).

Decision points: `BESU_SCAN_DONEn_odd`, `BYBA_SCAN_DONEp_odd`, `DOBA_SCAN_DONEp_evn`

#### Tile fetch pipeline stays active one dot too long

**Affected decision points:** 2 | **Max depth differential:** 17 gates (85-255 ns)

The fetch-done or fetching flag reset (depth 17) arrives late. The pipeline continues fetching for one extra dot, consuming an additional VRAM cycle. Can shift the mode 3 / mode 0 boundary by one dot, affecting H-blank timing and any mid-scanline register writes that depend on precise mode transition timing.

Decision points: `LOVY_TFETCH_DONEp`, `LONY_TFETCHINGp`

#### Tile fetch state machine runs one extra cycle before reset

**Affected decision points:** 3 | **Max depth differential:** 17 gates (85-255 ns)

The fetch counter reset (NYXU_BFETCH_RSTn, depth 17) arrives after the fetch counter clock (depth 0). The state machine advances one extra state before resetting to S0. Visible as a corrupted tile at the left edge of the screen or at window/BG boundary transitions — the fetcher reads from the wrong VRAM address for one cycle.

Decision points: `MESU_BFETCH_S1p_odd`, `NYVA_BFETCH_S2p_odd`, `LYZU_BFETCH_S0p_D1`

#### Sprite store 0 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `XEPE_STORE0_X0p`, `YLAH_STORE0_X1p`, `ZOLA_STORE0_X2p`, `ZULU_STORE0_X3p`, `WELO_STORE0_X4p`, `XUNY_STORE0_X5p`, `WOTE_STORE0_X6p`, `XAKO_STORE0_X7p`

#### Sprite store 1 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `DANY_STORE1_X0p`, `DUKO_STORE1_X1p`, `DESU_STORE1_X2p`, `DAZO_STORE1_X3p`, `DAKE_STORE1_X4p`, `CESO_STORE1_X5p`, `DYFU_STORE1_X6p`, `CUSY_STORE1_X7p`

#### Sprite store 2 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `FOKA_STORE2_X0p`, `FYTY_STORE2_X1p`, `FUBY_STORE2_X2p`, `GOXU_STORE2_X3p`, `DUHY_STORE2_X4p`, `EJUF_STORE2_X5p`, `ENOR_STORE2_X6p`, `DEPY_STORE2_X7p`

#### Sprite store 3 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `XOLY_STORE3_X0p`, `XYBA_STORE3_X1p`, `XABE_STORE3_X2p`, `XEKA_STORE3_X3p`, `XOMY_STORE3_X4p`, `WUHA_STORE3_X5p`, `WYNA_STORE3_X6p`, `WECO_STORE3_X7p`

#### Sprite store 4 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `WEDU_STORE4_X0p`, `YGAJ_STORE4_X1p`, `ZYJO_STORE4_X2p`, `XURY_STORE4_X3p`, `YBED_STORE4_X4p`, `ZALA_STORE4_X5p`, `WYDE_STORE4_X6p`, `XEPA_STORE4_X7p`

#### Sprite store 5 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `FUSA_STORE5_X0p`, `FAXA_STORE5_X1p`, `FOZY_STORE5_X2p`, `FESY_STORE5_X3p`, `CYWE_STORE5_X4p`, `DYBY_STORE5_X5p`, `DURY_STORE5_X6p`, `CUVY_STORE5_X7p`

#### Sprite store 6 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `YCOL_STORE6_X0p`, `YRAC_STORE6_X1p`, `YMEM_STORE6_X2p`, `YVAG_STORE6_X3p`, `ZOLY_STORE6_X4p`, `ZOGO_STORE6_X5p`, `ZECU_STORE6_X6p`, `ZESA_STORE6_X7p`

#### Sprite store 7 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `ERAZ_STORE7_X0p`, `EPUM_STORE7_X1p`, `EROL_STORE7_X2p`, `EHYN_STORE7_X3p`, `FAZU_STORE7_X4p`, `FAXE_STORE7_X5p`, `EXUK_STORE7_X6p`, `FEDE_STORE7_X7p`

#### Sprite store 8 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `EZUF_STORE8_X0p`, `ENAD_STORE8_X1p`, `EBOW_STORE8_X2p`, `FYCA_STORE8_X3p`, `GAVY_STORE8_X4p`, `GYPU_STORE8_X5p`, `GADY_STORE8_X6p`, `GAZA_STORE8_X7p`

#### Sprite store 9 X-position off by one dot

**Affected decision points:** 8 | **Max depth differential:** 16 gates (80-240 ns)

The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

Decision points: `XUVY_STORE9_X0p`, `XERE_STORE9_X1p`, `XUZO_STORE9_X2p`, `XEXA_STORE9_X3p`, `YPOD_STORE9_X4p`, `YROP_STORE9_X5p`, `YNEP_STORE9_X6p`, `YZOF_STORE9_X7p`

#### Fine scroll match applies one dot late

**Affected decision points:** 4 | **Max depth differential:** 16 gates (80-240 ns)

The SCX fine scroll match signal settles at depth 0, but the pixel clock it gates (CLKPIPE) arrives at depth 16. Fine scroll effectively skips one fewer pixel than expected, shifting the background by one dot. Visible in games that use SCX fine scroll for smooth horizontal scrolling (most platformers).

Decision points: `PUXA_SCX_FINE_MATCH_evn`, `ROGA_FINE_CNT1_odd`, `RUBU_FINE_CNT2_odd`, `NYZE_SCX_FINE_MATCH_odd`

#### Pixel Counter timing off by one dot

**Affected decision points:** 1 | **Max depth differential:** 16 gates (80-240 ns)

Signal race with 16-gate differential at `PAHO_X8_SYNC`. The late-arriving signal (depth 16) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `PAHO_X8_SYNC`

#### Pixel data shifted one dot late relative to pipe clock

**Affected decision points:** 48 | **Max depth differential:** 16 gates (80-240 ns)

CLKPIPE (the pixel pipe shift clock) arrives through a 16-gate buffer chain, well after the pipe input data is ready. The pipe effectively shifts one propagation delay after data settles. Sprite and BG pixels may appear one dot to the right of their correct position.

Decision points (sample): `NURO_SPR_PIPE_A0`, `MASO_SPR_PIPE_A1`, `LEFE_SPR_PIPE_A2`, `LESU_SPR_PIPE_A3`, `WYHO_SPR_PIPE_A4`, ... and 43 more

#### Window trigger fires one dot late

**Affected decision points:** 14 | **Max depth differential:** 16 gates (80-240 ns)

Window match/fetch signals race with a 16-gate differential. The window may activate one dot later than expected, shifting all window content one pixel to the right. Affects games with split-screen effects using the window (status bars, dialogue boxes).

Decision points (sample): `PYCO_WIN_MATCHp_evn`, `RYFA_WIN_FETCHn_A`, `WODY_WIN_MAP_X1`, `WOBO_WIN_MAP_X2`, `WYKO_WIN_MAP_X3`, ... and 9 more

#### Mode transition boundary shifted by one dot

**Affected decision points:** 2 | **Max depth differential:** 15 gates (75-225 ns)

Mode flag races with a 15-gate differential. The mode 0/2/3 transition occurs one dot off from the expected position, affecting when the CPU can access VRAM/OAM and when H-blank begins.

Decision points: `XYMU_RENDERING_LATCHn`, `VOGA_HBLANKp_evn`

#### Pixel counter increment races with pipe clock

**Affected decision points:** 8 | **Max depth differential:** 15 gates (75-225 ns)

The pixel X counter races against CLKPIPE with a 15-gate differential. This shifts the X coordinate at which sprite/window comparisons trigger, potentially causing one-dot horizontal offsets.

Decision points: `SAVY_PX1p_odd`, `XODU_PX2p_odd`, `XYDO_PX3p_odd`, `TUHU_PX4p_odd`, `TUKY_PX5p_odd`, `TAKO_PX6p_odd`, `SYBE_PX7p_odd`, `XEHO_PX0p_odd`

#### Other timing off by one dot

**Affected decision points:** 63 | **Max depth differential:** 14 gates (70-210 ns)

Signal race with 14-gate differential at `AFER_SYS_RSTp`. The late-arriving signal (depth 14) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points (sample): `AFER_SYS_RSTp`, `CUXY_SPRITE_COUNT1_odd`, `BEGO_SPRITE_COUNT2_odd`, `DYBE_SPRITE_COUNT3_odd`, `BESE_SPRITE_COUNT0_odd`, ... and 58 more

#### Joypad timing off by one dot

**Affected decision points:** 5 | **Max depth differential:** 14 gates (70-210 ns)

Signal race with 14-gate differential at `AWOB_WAKE_CPU`. The late-arriving signal (depth 14) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `AWOB_WAKE_CPU`, `BATU_JP_GLITCH0`, `ACEF_JP_GLITCH1`, `AGEM_JP_GLITCH2`, `APUG_JP_GLITCH3`

#### Timer timing off by one dot

**Affected decision points:** 26 | **Max depth differential:** 14 gates (70-210 ns)

Signal race with 14-gate differential at `NYDU_TIMA7p_DELAY`. The late-arriving signal (depth 14) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points (sample): `NYDU_TIMA7p_DELAY`, `MOBA_TIMER_OVERFLOWp`, `POVY_TIMA1p`, `PERU_TIMA2p`, `RATE_TIMA3p`, ... and 21 more

#### Sprite Store/Match timing off by one dot

**Affected decision points:** 10 | **Max depth differential:** 14 gates (70-210 ns)

Signal race with 14-gate differential at `EBOJ_STORE0_RSTp`. The late-arriving signal (depth 14) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points (sample): `EBOJ_STORE0_RSTp`, `CEDY_STORE1_RSTp`, `EGAV_STORE2_RSTp`, `GOTA_STORE3_RSTp`, `XUDY_STORE4_RSTp`, ... and 5 more

#### Sprite Scanner timing off by one dot

**Affected decision points:** 5 | **Max depth differential:** 13 gates (65-195 ns)

Signal race with 13-gate differential at `WEWY_SCAN1_odd`. The late-arriving signal (depth 13) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `WEWY_SCAN1_odd`, `GOSO_SCAN2_odd`, `ELYN_SCAN3_odd`, `FAHA_SCAN4_odd`, `FONY_SCAN5_odd`

#### Sprite fetch timing shifted by one dot

**Affected decision points:** 9 | **Max depth differential:** 13 gates (65-195 ns)

Sprite fetch state machine races with a 13-gate differential. May cause the sprite fetch to start or complete one dot off, affecting mode 3 duration and sprite X positioning.

Decision points (sample): `TULY_SFETCH_S1p_evn`, `TESE_SFETCH_S2p_evn`, `TAKA_SFETCH_RUNNINGp_evn`, `SOBU_SFETCH_REQp_evn  `, `TOBU_SFETCH_S1p_D2_evn`, ... and 4 more

#### Interrupts timing off by one dot

**Affected decision points:** 5 | **Max depth differential:** 12 gates (60-180 ns)

Signal race with 12-gate differential at `LALU_FF0F_D1p`. The late-arriving signal (depth 12) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `LALU_FF0F_D1p`, `NYBO_FF0F_D2p`, `UBUL_FF0F_D3p`, `ULAK_FF0F_D4p`, `LOPE_FF0F_D0p`

#### STAT interrupt fires one dot early/late

**Affected decision points:** 6 | **Max depth differential:** 11 gates (55-165 ns)

LY/LYC match or STAT mode flag races with a 11-gate differential. The STAT interrupt may trigger one dot earlier or later than expected. Affects games that use mid-frame STAT interrupts for raster effects (wobble, palette changes).

Decision points: `RUPO_LYC_MATCHn`, `ROXE_STAT_HBI_ENp`, `RUFO_STAT_VBI_ENp`, `REFE_STAT_OAI_ENp`, `RUGU_STAT_LYI_ENp`, `ROPO_LY_MATCH_SYNCp`

#### PPU Registers timing off by one dot

**Affected decision points:** 64 | **Max depth differential:** 10 gates (50-150 ns)

Signal race with 10-gate differential at `PAVO_BGP_D0p`. The late-arriving signal (depth 10) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points (sample): `PAVO_BGP_D0p`, `NUSY_BGP_D1p`, `PYLU_BGP_D2p`, `MAXY_BGP_D3p`, `MUKE_BGP_D4p`, ... and 59 more

#### DMA transfer timing off by one cycle

**Affected decision points:** 20 | **Max depth differential:** 10 gates (50-150 ns)

DMA control signal races with a 10-gate differential. May affect when DMA releases the OAM bus back to the PPU.

Decision points (sample): `NAFA_DMA_A08p`, `PYNE_DMA_A09p`, `PARA_DMA_A10p`, `NYDO_DMA_A11p`, `NYGY_DMA_A12p`, ... and 15 more

#### LYC Register timing off by one dot

**Affected decision points:** 8 | **Max depth differential:** 10 gates (50-150 ns)

Signal race with 10-gate differential at `SYRY_LYC0p`. The late-arriving signal (depth 10) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `SYRY_LYC0p`, `VUCE_LYC1p`, `SEDY_LYC2p`, `SALO_LYC3p`, `SOTA_LYC4p`, `VAFA_LYC5p`, `VEVO_LYC6p`, `RAHA_LYC7p`

#### Internal line counter off by one dot

**Affected decision points:** 7 | **Max depth differential:** 10 gates (50-150 ns)

LX counter races with a 10-gate differential. Shifts all LX-derived timing signals (line end, scan triggers) by one dot.

Decision points: `TYPO_LX1p_odd`, `VYZO_LX2p_odd`, `TELU_LX3p_odd`, `SUDE_LX4p_odd`, `TAHA_LX5p_odd`, `TYRY_LX6p_odd`, `SAXO_LX0p_odd`

#### LY Counter timing off by one dot

**Affected decision points:** 8 | **Max depth differential:** 10 gates (50-150 ns)

Signal race with 10-gate differential at `MYRO_LY1p_odd`. The late-arriving signal (depth 10) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `MYRO_LY1p_odd`, `LEXA_LY2p_odd`, `LYDO_LY3p_odd`, `LOVU_LY4p_odd`, `LEMA_LY5p_odd`, `MATO_LY6p_odd`, `LAFO_LY7p_odd`, `KELY_JOYP_UDLRp`

#### OAM Bus timing off by one dot

**Affected decision points:** 32 | **Max depth differential:** 10 gates (50-150 ns)

Signal race with 10-gate differential at `XUSO_OAM_DA0n`. The late-arriving signal (depth 10) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points (sample): `XUSO_OAM_DA0n`, `XEGU_OAM_DA1n`, `YJEX_OAM_DA2n`, `XYJU_OAM_DA3n`, `YBOG_OAM_DA4n`, ... and 27 more

#### Tile Fetcher timing off by one dot

**Affected decision points:** 4 | **Max depth differential:** 7 gates (35-105 ns)

Signal race with 7-gate differential at `PORY_FETCH_DONEp_odd`. The late-arriving signal (depth 7) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `PORY_FETCH_DONEp_odd`, `PYGO_FETCH_DONEp_evn`, `NYKA_FETCH_DONEp_evn`, `LEGU_TILE_DA0p`

#### Sprite store index/line data captured with stale reset

**Affected decision points:** 100 | **Max depth differential:** 6 gates (30-90 ns)

Reset arrives 6 gates after data. May cause wrong tile or wrong line-within-sprite to render at scanline boundaries.

Decision points (sample): `CADU_STORE1_I0p`, `CEBO_STORE1_I1p`, `CUFA_STORE1_I2p`, `COMA_STORE1_I3p`, `CUZA_STORE1_I4p`, ... and 95 more

#### Window Logic timing off by one dot

**Affected decision points:** 1 | **Max depth differential:** 5 gates (25-75 ns)

Signal race with 5-gate differential at `SARY_WY_MATCHp_odd`. The late-arriving signal (depth 5) may not settle before the DFF samples, causing the captured value to differ from behavioral emulation.

Decision points: `SARY_WY_MATCHp_odd`


### Detailed Race Analysis

#### `BESU_SCAN_DONEn_odd` (diff: 17 gates, GateBoy.cpp:771)

Type: registered (nor_latch)
 | Active phase: **ODD**

**Observable effect:** OAM scan extends one dot beyond expected boundary

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `ASEN_SCAN_DONE_tp_odd_new` | 17 (85-255 ns) | or2 | ODD | **LATE** |
| `CATU_LINE_ENDp_odd` | 0 (0 ns) | registered | ODD | early |

The late-arriving signal reaches `BESU_SCAN_DONEn_odd` **85-255 ns** after the earliest input. 
This exceeds a half T-cycle (214%), meaning the late signal may not settle before the next clock edge.

> The scan-done signal (depth 17) races against line-end (depth 0). OAM evaluation continues for one extra dot, potentially including one additional sprite in the scanline sprite buffer. Affects the mode 2 → mode 3 transition point, which shifts all subsequent mode timings by one dot. Most visible with exactly 10 sprites on a line (the hardware limit).

#### `LOVY_TFETCH_DONEp` (diff: 17 gates, GateBoy.cpp:1193)

Type: registered (dff17)

**Observable effect:** Tile fetch pipeline stays active one dot too long

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `NYXU_BFETCH_RSTn` | 17 (85-255 ns) | nor3 | - | **LATE** |
| `MYVO_AxCxExGx` | 7 (35-105 ns) | not1 | AxCxExGx | mid |
| `LYRY_BFETCH_DONEp_odd@old` | 0 (0 ns) | registered | ODD | early |

The late-arriving signal reaches `LOVY_TFETCH_DONEp` **85-255 ns** after the earliest input. 
This exceeds a half T-cycle (214%), meaning the late signal may not settle before the next clock edge.

> The fetch-done or fetching flag reset (depth 17) arrives late. The pipeline continues fetching for one extra dot, consuming an additional VRAM cycle. Can shift the mode 3 / mode 0 boundary by one dot, affecting H-blank timing and any mid-scanline register writes that depend on precise mode transition timing.

#### `MESU_BFETCH_S1p_odd` (diff: 17 gates, GateBoy.cpp:1189)

Type: registered (dff17_any)
 | Active phase: **ODD**

**Observable effect:** Tile fetch state machine runs one extra cycle before reset

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `NYXU_BFETCH_RSTn` | 17 (85-255 ns) | nor3 | - | **LATE** |
| `LAXU_BFETCH_S0p_odd` | 0 (0 ns) | registered | ODD | early |

The late-arriving signal reaches `MESU_BFETCH_S1p_odd` **85-255 ns** after the earliest input. 
This exceeds a half T-cycle (214%), meaning the late signal may not settle before the next clock edge.

> The fetch counter reset (NYXU_BFETCH_RSTn, depth 17) arrives after the fetch counter clock (depth 0). The state machine advances one extra state before resetting to S0. Visible as a corrupted tile at the left edge of the screen or at window/BG boundary transitions — the fetcher reads from the wrong VRAM address for one cycle.

#### `NYVA_BFETCH_S2p_odd` (diff: 17 gates, GateBoy.cpp:1190)

Type: registered (dff17_any)
 | Active phase: **ODD**

**Observable effect:** Tile fetch state machine runs one extra cycle before reset

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `NYXU_BFETCH_RSTn` | 17 (85-255 ns) | nor3 | - | **LATE** |
| `MESU_BFETCH_S1p_odd` | 0 (0 ns) | registered | ODD | early |

The late-arriving signal reaches `NYVA_BFETCH_S2p_odd` **85-255 ns** after the earliest input. 
This exceeds a half T-cycle (214%), meaning the late signal may not settle before the next clock edge.

> The fetch counter reset (NYXU_BFETCH_RSTn, depth 17) arrives after the fetch counter clock (depth 0). The state machine advances one extra state before resetting to S0. Visible as a corrupted tile at the left edge of the screen or at window/BG boundary transitions — the fetcher reads from the wrong VRAM address for one cycle.

#### `LONY_TFETCHINGp` (diff: 16 gates, GateBoy.cpp:1199)

Type: registered (nand_latch)

**Observable effect:** Tile fetch pipeline stays active one dot too long

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `NYXU_BFETCH_RSTn` | 17 (85-255 ns) | nor3 | - | **LATE** |
| `LURY_BG_FETCH_DONEn` | 1 (5-15 ns) | and2 | - | early |

The late-arriving signal reaches `LONY_TFETCHINGp` **80-240 ns** after the earliest input. 
This exceeds a half T-cycle (201%), meaning the late signal may not settle before the next clock edge.

> The fetch-done or fetching flag reset (depth 17) arrives late. The pipeline continues fetching for one extra dot, consuming an additional VRAM cycle. Can shift the mode 3 / mode 0 boundary by one dot, affecting H-blank timing and any mid-scanline register writes that depend on precise mode transition timing.

#### `XEPE_STORE0_X0p` (diff: 16 gates, GateBoySpriteStore.cpp:105)

Type: registered (dff9)

**Observable effect:** Sprite store 0 X-position off by one dot

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `DYNA_STORE0_RSTn` | 17 (85-255 ns) | not1 | - | **LATE** |
| `FUXU_STORE0_CLKp` | 5 (25-75 ns) | not1 | - | mid |
| `ZAGO_SPX0n_old` | 1 (5-15 ns) | not1 | - | early |

The late-arriving signal reaches `XEPE_STORE0_X0p` **80-240 ns** after the earliest input. 
This exceeds a half T-cycle (201%), meaning the late signal may not settle before the next clock edge.

> The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

#### `YLAH_STORE0_X1p` (diff: 16 gates, GateBoySpriteStore.cpp:106)

Type: registered (dff9)

**Observable effect:** Sprite store 0 X-position off by one dot

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `DYNA_STORE0_RSTn` | 17 (85-255 ns) | not1 | - | **LATE** |
| `FUXU_STORE0_CLKp` | 5 (25-75 ns) | not1 | - | mid |
| `ZOCY_SPX1n_old` | 1 (5-15 ns) | not1 | - | early |

The late-arriving signal reaches `YLAH_STORE0_X1p` **80-240 ns** after the earliest input. 
This exceeds a half T-cycle (201%), meaning the late signal may not settle before the next clock edge.

> The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

#### `ZOLA_STORE0_X2p` (diff: 16 gates, GateBoySpriteStore.cpp:107)

Type: registered (dff9)

**Observable effect:** Sprite store 0 X-position off by one dot

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `DYNA_STORE0_RSTn` | 17 (85-255 ns) | not1 | - | **LATE** |
| `FUXU_STORE0_CLKp` | 5 (25-75 ns) | not1 | - | mid |
| `YPUR_SPX2n_old` | 1 (5-15 ns) | not1 | - | early |

The late-arriving signal reaches `ZOLA_STORE0_X2p` **80-240 ns** after the earliest input. 
This exceeds a half T-cycle (201%), meaning the late signal may not settle before the next clock edge.

> The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

#### `ZULU_STORE0_X3p` (diff: 16 gates, GateBoySpriteStore.cpp:108)

Type: registered (dff9)

**Observable effect:** Sprite store 0 X-position off by one dot

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `DYNA_STORE0_RSTn` | 17 (85-255 ns) | not1 | - | **LATE** |
| `FUXU_STORE0_CLKp` | 5 (25-75 ns) | not1 | - | mid |
| `YVOK_SPX3n_old` | 1 (5-15 ns) | not1 | - | early |

The late-arriving signal reaches `ZULU_STORE0_X3p` **80-240 ns** after the earliest input. 
This exceeds a half T-cycle (201%), meaning the late signal may not settle before the next clock edge.

> The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.

#### `WELO_STORE0_X4p` (diff: 16 gates, GateBoySpriteStore.cpp:109)

Type: registered (dff9)

**Observable effect:** Sprite store 0 X-position off by one dot

| Input | Depth | Gate | Phase | Role |
|-------|-------|------|-------|------|
| `DYNA_STORE0_RSTn` | 17 (85-255 ns) | not1 | - | **LATE** |
| `FUXU_STORE0_CLKp` | 5 (25-75 ns) | not1 | - | mid |
| `COSE_SPX4n_old` | 1 (5-15 ns) | not1 | - | early |

The late-arriving signal reaches `WELO_STORE0_X4p` **80-240 ns** after the earliest input. 
This exceeds a half T-cycle (201%), meaning the late signal may not settle before the next clock edge.

> The line-end reset signal (depth 17) arrives long after sprite X data from OAM (depth 1). At scanline boundaries, the store latch may capture the previous sprite's X coordinate instead of clearing. Visible as sprites shifting one dot horizontally at the start of a scanline, most noticeable with moving sprites near the left edge.
