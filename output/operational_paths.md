# Operational Paths (by functional area)

Paths that fire every dot or scanline during normal rendering.
These are the ones that cause observable timing discrepancies in emulators.

| Functional Area | Paths | Max Depth | Max Delay | Key Sinks |
|-----------------|-------|-----------|-----------|-----------|
| Clock Distribution | 13 | 17 | 255 ns | `SIG_CPU_BOWA_Axxxxxxx`, `SIG_CPU_BEDO_xBCDEFGH`, `SIG_CPU_BOMA_xBCDEFGH` |
| Timer | 30 | 14 | 210 ns | `UKUP_DIV00p`, `MOBA_TIMER_OVERFLOWp`, `NYDU_TIMA7p_DELAY` |
| Other | 223 | 14 | 210 ns | `AFER_SYS_RSTp`, `BUS_CPU_D02p`, `BUS_CPU_D03p` |
| Joypad | 7 | 14 | 210 ns | `AWOB_WAKE_CPU`, `BATU_JP_GLITCH0`, `ACEF_JP_GLITCH1` |
| VRAM Bus | 108 | 14 | 210 ns | `BUS_VRAM_D00p`, `BUS_VRAM_D01p`, `BUS_VRAM_D02p` |
| Interrupts | 13 | 12 | 180 ns | `LALU_FF0F_D1p`, `NYBO_FF0F_D2p`, `UBUL_FF0F_D3p` |
| STAT/LY Match | 7 | 11 | 165 ns | `RUPO_LYC_MATCHn`, `ROXE_STAT_HBI_ENp`, `RUFO_STAT_VBI_ENp` |
| OAM Bus | 102 | 11 | 165 ns | `SIG_OAM_WRn_B`, `SIG_OAM_WRn_A`, `SIG_OAM_OEn` |
| PPU Registers | 64 | 10 | 150 ns | `PAVO_BGP_D0p`, `NUSY_BGP_D1p`, `PYLU_BGP_D2p` |
| DMA | 15 | 10 | 150 ns | `NAFA_DMA_A08p`, `PYNE_DMA_A09p`, `PARA_DMA_A10p` |
| LYC Register | 8 | 10 | 150 ns | `SYRY_LYC0p`, `VUCE_LYC1p`, `SEDY_LYC2p` |
| Sprite Fetcher | 8 | 9 | 135 ns | `SOBU_SFETCH_REQp_evn  `, `TOBU_SFETCH_S1p_D2_evn`, `VONU_SFETCH_S1p_D4_evn` |
| Scroll/Fine Timing | 4 | 8 | 120 ns | `NYZE_SCX_FINE_MATCH_odd`, `PUXA_SCX_FINE_MATCH_evn`, `ROXY_FINE_SCROLL_DONEn` |
| Tile Fetcher | 10 | 8 | 120 ns | `PORY_FETCH_DONEp_odd`, `LOVY_TFETCH_DONEp`, `PYGO_FETCH_DONEp_evn` |
| Window Logic | 9 | 8 | 120 ns | `NUNU_WIN_MATCHp_odd`, `RENE_WIN_FETCHn_B`, `SOVY_WIN_HITp` |
| LY Counter | 3 | 7 | 105 ns | `KELY_JOYP_UDLRp`, `ALYR_EXT_ADDR_LATCH_02p`, `LYSA_EXT_ADDR_LATCH_09p` |
| Mode/Rendering Control | 3 | 7 | 105 ns | `VOGA_HBLANKp_evn`, `POPU_VBLANKp_odd   `, `XYMU_RENDERING_LATCHn` |
| Sprite Scanner | 3 | 7 | 105 ns | `DOBA_SCAN_DONEp_evn`, `BYBA_SCAN_DONEp_odd`, `CENO_SCAN_DONEn_odd` |
| Sprite Store/Match | 282 | 6 | 90 ns | `DANY_STORE1_X0p`, `DUKO_STORE1_X1p`, `DESU_STORE1_X2p` |
| Pixel Pipeline | 40 | 6 | 90 ns | `NYLU_SPR_PIPE_B0`, `VEZO_MASK_PIPE_0`, `RUGO_PAL_PIPE_D0` |
| Line Timing | 6 | 3 | 45 ns | `CATU_LINE_ENDp_odd`, `RUTU_LINE_ENDp_odd `, `ANEL_LINE_ENDp_odd` |
| Pixel Counter | 10 | 3 | 45 ns | `XYDO_PX3p_odd`, `SYBE_PX7p_odd`, `XODU_PX2p_odd` |
| LX Counter | 1 | 1 | 15 ns | `SAXO_LX0p_odd` |

### Key Bottleneck Nodes (highest fan-out)

These nodes drive the most downstream signals. Propagation delay
at these nodes has the widest impact on timing.

| Node | Fan-out | Type | Source |
|------|---------|------|--------|
| `SACU_CLKPIPE_odd_new` | 52 | or2 | GateBoy.cpp:1143 |
| `UNOR_MODE_DBG2p_new` | 26 | and2 | GateBoyPins.cpp:100 |
| `XYMU_RENDERING_LATCHn` | 25 | registered | GateBoy.cpp:827 |
| `SIG_VCC` | 24 | boundary | GateBoy.cpp:700 |
| `TEDO_CPU_RDp` | 19 | not1 | GateBoy.cpp:654 |
| `LUMA_DMA_CARTp_new` | 19 | not1 | GateBoyExtBus.cpp:172 |
| `TOVA_MODE_DBG2n_new` | 17 | not1 | GateBoyPins.cpp:102 |
| `TAPU_CPU_WRp` | 17 | not1 | GateBoy.cpp:715 |
| `RAHU_CBD_TO_VPDn_new` | 17 | not1 | GateBoyVramBus.cpp:610 |
| `BODE_OAM_OEp_new` | 17 | not1 | GateBoyOamBus.cpp:351 |
| `ZODO_OAM_OEn_new` | 17 | not1 | GateBoyOamBus.cpp:354 |
| `WALU_SYS_RSTn` | 16 | not1 | GateBoyPixPipe.cpp:21 |
| `LOZE_PIPE_A_LOADp_new` | 16 | not1 | GateBoyPixPipe.cpp:338 |
| `LUXA_PIPE_B_LOADp` | 16 | not1 | GateBoyPixPipe.cpp:379 |
| `CUNU_SYS_RSTn` | 16 | not1 | GateBoyVramBus.cpp:14 |
| `GOMO_OAM_DB4n` | 16 | registered | GateBoyOamBus.cpp:41 |
| `DEPO_OAM_DB7n` | 16 | registered | GateBoyOamBus.cpp:44 |
| `AZUL_CBD_TO_OBDn_new` | 16 | not1 | GateBoyOamBus.cpp:162 |
| `CEDE_EBD_TO_OBDn_new` | 16 | not1 | GateBoyOamBus.cpp:216 |
| `AZAR_VBD_TO_OBDn_new` | 16 | not1 | GateBoyOamBus.cpp:258 |

### Clock Distribution (max depth 17, 13 paths)

**Depth 17** (85-255 ns, 214% half T-cycle): `SIG_CPU_CLKREQ` -> `SIG_CPU_BOWA_Axxxxxxx` [sink @Axxxxxxx]

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyClocks.cpp:51)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:58)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:65)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:66)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:67)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:72)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:73)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:74)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:75)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:76)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:77)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:78)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:79)
                                [and2] BUVU_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:81)
                                  [not1] BYXO_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:82)
                                    [not1] BEDO_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:83)
                                      [not1] BOWA_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:84)
                                        [BOUNDARY] SIG_CPU_BOWA_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:88)
```

**Depth 16** (80-240 ns, 201% half T-cycle): `SIG_CPU_CLKREQ` -> `SIG_CPU_BEDO_xBCDEFGH` [sink @xBCDEFGH]

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyClocks.cpp:51)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:58)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:65)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:66)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:67)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:72)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:73)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:74)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:75)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:76)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:77)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:78)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:79)
                                [and2] BUVU_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:81)
                                  [not1] BYXO_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:82)
                                    [not1] BEDO_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:83)
                                      [BOUNDARY] SIG_CPU_BEDO_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:89)
```

**Depth 15** (75-225 ns, 189% half T-cycle): `SIG_CPU_CLKREQ` -> `SIG_CPU_BOMA_xBCDEFGH` [sink @xBCDEFGH]

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyClocks.cpp:51)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:58)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:65)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:66)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:67)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:72)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:73)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:74)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:75)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:76)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:77)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:78)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:79)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:85)
                                  [not1] BOMA_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:86)
                                    [BOUNDARY] SIG_CPU_BOMA_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:94)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `SIG_CPU_CLKREQ` -> `SIG_CPU_BOGA_Axxxxxxx` [sink @Axxxxxxx]

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyClocks.cpp:51)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:58)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:65)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyClocks.cpp:66)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyClocks.cpp:67)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:72)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:73)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyClocks.cpp:74)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:75)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:76)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:77)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:78)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyClocks.cpp:79)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:85)
                                  [BOUNDARY] SIG_CPU_BOGA_Axxxxxxx @Axxxxxxx  (GateBoyClocks.cpp:95)
```

**Depth 5** (25-75 ns, 63% half T-cycle): `ALEF_xBCDExxx` -> `SIG_CPU_BUKE_AxxxxxGH` [src @xBCDExxx, sink @AxxxxxGH]

```
    [REGISTERED] ALEF_xBCDExxx @xBCDExxx  (GateBoyClocks.cpp:47)
      [not1] AFEP_AxxxxFGH @AxxxxFGH  (GateBoyClocks.cpp:55)
        [not1] BUGO_xBCDExxx @xBCDExxx  (GateBoyClocks.cpp:61)
          [nor3] BATE_AxxxxxGH @AxxxxxGH  (GateBoyClocks.cpp:62)
            [not1] BASU_xBCDEFxx @xBCDEFxx  (GateBoyClocks.cpp:63)
              [not1] BUKE_AxxxxxGH @AxxxxxGH  (GateBoyClocks.cpp:64)
                [BOUNDARY] SIG_CPU_BUKE_AxxxxxGH @AxxxxxGH  (GateBoyClocks.cpp:93)
```

*...and 8 more paths in this category.*

### Timer (max depth 14, 30 paths)

**Depth 14** (70-210 ns, 176% half T-cycle): `SIG_CPU_CLKREQ` -> `UKUP_DIV00p`

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyTimer.cpp:94)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyTimer.cpp:99)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyTimer.cpp:102)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyTimer.cpp:103)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyTimer.cpp:104)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyTimer.cpp:108)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyTimer.cpp:109)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyTimer.cpp:110)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyTimer.cpp:111)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyTimer.cpp:112)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:113)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:114)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyTimer.cpp:115)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:116)
                                  [REGISTERED] UKUP_DIV00p  (GateBoyTimer.cpp:40)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `SIG_CPU_CLKREQ` -> `MOBA_TIMER_OVERFLOWp`

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyTimer.cpp:94)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyTimer.cpp:99)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyTimer.cpp:102)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyTimer.cpp:103)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyTimer.cpp:104)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyTimer.cpp:108)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyTimer.cpp:109)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyTimer.cpp:110)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyTimer.cpp:111)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyTimer.cpp:112)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:113)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:114)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyTimer.cpp:115)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:116)
                                  [REGISTERED] MOBA_TIMER_OVERFLOWp  (GateBoyTimer.cpp:134)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `SIG_CPU_CLKREQ` -> `NYDU_TIMA7p_DELAY`

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyTimer.cpp:94)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyTimer.cpp:99)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyTimer.cpp:102)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyTimer.cpp:103)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyTimer.cpp:104)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyTimer.cpp:108)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyTimer.cpp:109)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyTimer.cpp:110)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyTimer.cpp:111)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyTimer.cpp:112)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:113)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:114)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyTimer.cpp:115)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyTimer.cpp:116)
                                  [REGISTERED] NYDU_TIMA7p_DELAY  (GateBoyTimer.cpp:141)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ADYK_xxxDEFGx` -> `REGA_TIMA0p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [nand4] TOPE_FF05_WRn_new  (GateBoyTimer.cpp:136)
                    [or2] MUZU_CPU_LOAD_TIMAn_new  (GateBoyTimer.cpp:137)
                      [nand3] MEXU_TIMA_LOADp_new  (GateBoyTimer.cpp:139)
                        [REGISTERED] REGA_TIMA0p  (GateBoyTimer.cpp:172)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ADYK_xxxDEFGx` -> `POVY_TIMA1p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [nand4] TOPE_FF05_WRn_new  (GateBoyTimer.cpp:136)
                    [or2] MUZU_CPU_LOAD_TIMAn_new  (GateBoyTimer.cpp:137)
                      [nand3] MEXU_TIMA_LOADp_new  (GateBoyTimer.cpp:139)
                        [REGISTERED] POVY_TIMA1p  (GateBoyTimer.cpp:173)
```

*...and 25 more paths in this category.*

### Other (max depth 14, 223 paths)

**Depth 14** (70-210 ns, 176% half T-cycle): `SIG_CPU_CLKREQ` -> `AFER_SYS_RSTp`

```
    [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
      [not1] ABOL_CLKREQn  (GateBoyReset.cpp:11)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyReset.cpp:19)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyReset.cpp:20)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyReset.cpp:21)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyReset.cpp:22)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyReset.cpp:24)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyReset.cpp:25)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyReset.cpp:26)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyReset.cpp:27)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyReset.cpp:28)
                          [not1] BELE_Axxxxxxx_new @Axxxxxxx  (GateBoyReset.cpp:29)
                            [or2] BYJU_Axxxxxxx_new @Axxxxxxx  (GateBoyReset.cpp:30)
                              [not1] BALY_xBCDEFGH_new @xBCDEFGH  (GateBoyReset.cpp:31)
                                [not1] BOGA_Axxxxxxx_new @Axxxxxxx  (GateBoyReset.cpp:32)
                                  [REGISTERED] AFER_SYS_RSTp (fan-out: 13)  (GateBoyReset.cpp:34)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `TUNA_0000_FDFF_new` -> `BUS_CPU_D02p`

```
    [nand7] TUNA_0000_FDFF_new  (GateBoyCpuBus.cpp:172)
      [nor2] SYKE_ADDR_HIp_new  (GateBoyCpuBus.cpp:194)
        [nand3] WUTU_ADDR_PPUn_new  (GateBoyCpuBus.cpp:251)
          [not1] WERO_ADDR_PPUp_new (fan-out: 12)  (GateBoyCpuBus.cpp:252)
            [nand5] WATE_FF46n_new  (GateBoyCpuBus.cpp:231)
              [not1] XEDA_FF46p_new  (GateBoyCpuBus.cpp:244)
                [and2] MOLU_FF46_RDp_new  (GateBoyDMA.cpp:79)
                  [not1] NYGO_FF46_RDn_new  (GateBoyDMA.cpp:80)
                    [not1] PUSY_FF46_RDp_new  (GateBoyDMA.cpp:81)
                      [tri6_pn] REMA_DMA2_TO_CD2_new  (GateBoyDMA.cpp:85)
                        [BUS] BUS_CPU_D02p (fan-out: 10)  (GateBoyLCD.cpp:71)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `TUNA_0000_FDFF_new` -> `BUS_CPU_D03p`

```
    [nand7] TUNA_0000_FDFF_new  (GateBoyCpuBus.cpp:172)
      [nor2] SYKE_ADDR_HIp_new  (GateBoyCpuBus.cpp:194)
        [nand3] WUTU_ADDR_PPUn_new  (GateBoyCpuBus.cpp:251)
          [not1] WERO_ADDR_PPUp_new (fan-out: 12)  (GateBoyCpuBus.cpp:252)
            [nand5] WATE_FF46n_new  (GateBoyCpuBus.cpp:231)
              [not1] XEDA_FF46p_new  (GateBoyCpuBus.cpp:244)
                [and2] MOLU_FF46_RDp_new  (GateBoyDMA.cpp:79)
                  [not1] NYGO_FF46_RDn_new  (GateBoyDMA.cpp:80)
                    [not1] PUSY_FF46_RDp_new  (GateBoyDMA.cpp:81)
                      [tri6_pn] PANE_DMA3_TO_CD3_new  (GateBoyDMA.cpp:86)
                        [BUS] BUS_CPU_D03p (fan-out: 10)  (GateBoyLCD.cpp:72)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `TUNA_0000_FDFF_new` -> `BUS_CPU_D04p`

```
    [nand7] TUNA_0000_FDFF_new  (GateBoyCpuBus.cpp:172)
      [nor2] SYKE_ADDR_HIp_new  (GateBoyCpuBus.cpp:194)
        [nand3] WUTU_ADDR_PPUn_new  (GateBoyCpuBus.cpp:251)
          [not1] WERO_ADDR_PPUp_new (fan-out: 12)  (GateBoyCpuBus.cpp:252)
            [nand5] WATE_FF46n_new  (GateBoyCpuBus.cpp:231)
              [not1] XEDA_FF46p_new  (GateBoyCpuBus.cpp:244)
                [and2] MOLU_FF46_RDp_new  (GateBoyDMA.cpp:79)
                  [not1] NYGO_FF46_RDn_new  (GateBoyDMA.cpp:80)
                    [not1] PUSY_FF46_RDp_new  (GateBoyDMA.cpp:81)
                      [tri6_pn] PARE_DMA4_TO_CD4_new  (GateBoyDMA.cpp:87)
                        [BUS] BUS_CPU_D04p (fan-out: 10)  (GateBoyLCD.cpp:73)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `TUNA_0000_FDFF_new` -> `BUS_CPU_D05p`

```
    [nand7] TUNA_0000_FDFF_new  (GateBoyCpuBus.cpp:172)
      [nor2] SYKE_ADDR_HIp_new  (GateBoyCpuBus.cpp:194)
        [nand3] WUTU_ADDR_PPUn_new  (GateBoyCpuBus.cpp:251)
          [not1] WERO_ADDR_PPUp_new (fan-out: 12)  (GateBoyCpuBus.cpp:252)
            [nand5] WATE_FF46n_new  (GateBoyCpuBus.cpp:231)
              [not1] XEDA_FF46p_new  (GateBoyCpuBus.cpp:244)
                [and2] MOLU_FF46_RDp_new  (GateBoyDMA.cpp:79)
                  [not1] NYGO_FF46_RDn_new  (GateBoyDMA.cpp:80)
                    [not1] PUSY_FF46_RDp_new  (GateBoyDMA.cpp:81)
                      [tri6_pn] RALY_DMA5_TO_CD5_new  (GateBoyDMA.cpp:88)
                        [BUS] BUS_CPU_D05p  (GateBoyLCD.cpp:74)
```

*...and 218 more paths in this category.*

### Joypad (max depth 14, 7 paths)

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `AWOB_WAKE_CPU` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:149)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:153)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:156)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:157)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:158)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:161)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:162)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:163)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:164)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:165)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:166)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:167)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:168)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:169)
                                  [REGISTERED] AWOB_WAKE_CPU  (GateBoyJoypad.cpp:171)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `BATU_JP_GLITCH0` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:149)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:153)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:156)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:157)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:158)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:161)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:162)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:163)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:164)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:165)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:166)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:167)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:168)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:169)
                                  [REGISTERED] BATU_JP_GLITCH0  (GateBoyJoypad.cpp:174)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `ACEF_JP_GLITCH1` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:149)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:153)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:156)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:157)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:158)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:161)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:162)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:163)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:164)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:165)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:166)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:167)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:168)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:169)
                                  [REGISTERED] ACEF_JP_GLITCH1  (GateBoyJoypad.cpp:175)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `AGEM_JP_GLITCH2` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:149)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:153)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:156)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:157)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:158)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:161)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:162)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:163)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:164)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:165)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:166)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:167)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:168)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:169)
                                  [REGISTERED] AGEM_JP_GLITCH2  (GateBoyJoypad.cpp:176)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `APUG_JP_GLITCH3` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:149)
        [nor3] BAPY_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:153)
          [not1] BERU_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:156)
            [not1] BUFA_xxxxxxGH @xxxxxxGH  (GateBoyJoypad.cpp:157)
              [not1] BOLO_ABCDEFxx @ABCDEFxx  (GateBoyJoypad.cpp:158)
                [nand4] BEJA_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:161)
                  [not1] BANE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:162)
                    [not1] BELO_xxxxEFGH @xxxxEFGH  (GateBoyJoypad.cpp:163)
                      [not1] BAZE_ABCDxxxx @ABCDxxxx  (GateBoyJoypad.cpp:164)
                        [nand3] BUTO_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:165)
                          [not1] BELE_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:166)
                            [or2] BYJU_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:167)
                              [not1] BALY_xBCDEFGH @xBCDEFGH  (GateBoyJoypad.cpp:168)
                                [not1] BOGA_Axxxxxxx @Axxxxxxx  (GateBoyJoypad.cpp:169)
                                  [REGISTERED] APUG_JP_GLITCH3  (GateBoyJoypad.cpp:177)
```

### VRAM Bus (max depth 14, 108 paths)

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `BUS_VRAM_D00p` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:976)
        [not1] AJAX_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:720)
          [or_and3] AGUT_xxCDEFGH @xxCDEFGH  (GateBoy.cpp:722)
            [nor2] AWOD_ABxxxxxx @ABxxxxxx  (GateBoy.cpp:723)
              [not1] ABUZ_EXT_RAM_CS_CLK  (GateBoy.cpp:724)
                [nand2] TUCA_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:520)
                  [not1] TOLE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:521)
                    [and2] SERE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:523)
                      [and2] SAZO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:525)
                        [not1] RYJE_CBD_TO_VPDn_new  (GateBoyVramBus.cpp:526)
                          [not1] REVO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:527)
                            [and2] ROCY_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:609)
                              [not1] RAHU_CBD_TO_VPDn_new (fan-out: 17)  (GateBoyVramBus.cpp:610)
                                [tri10_np] TEME_CD0_TO_VD0_new  (GateBoyVramBus.cpp:613)
                                  [BUS] BUS_VRAM_D00p  (GateBoyVramBus.cpp:622)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `BUS_VRAM_D01p` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:976)
        [not1] AJAX_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:720)
          [or_and3] AGUT_xxCDEFGH @xxCDEFGH  (GateBoy.cpp:722)
            [nor2] AWOD_ABxxxxxx @ABxxxxxx  (GateBoy.cpp:723)
              [not1] ABUZ_EXT_RAM_CS_CLK  (GateBoy.cpp:724)
                [nand2] TUCA_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:520)
                  [not1] TOLE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:521)
                    [and2] SERE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:523)
                      [and2] SAZO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:525)
                        [not1] RYJE_CBD_TO_VPDn_new  (GateBoyVramBus.cpp:526)
                          [not1] REVO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:527)
                            [and2] ROCY_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:609)
                              [not1] RAHU_CBD_TO_VPDn_new (fan-out: 17)  (GateBoyVramBus.cpp:610)
                                [tri10_np] TEWU_CD1_TO_VD1_new  (GateBoyVramBus.cpp:614)
                                  [BUS] BUS_VRAM_D01p  (GateBoyVramBus.cpp:623)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `BUS_VRAM_D02p` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:976)
        [not1] AJAX_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:720)
          [or_and3] AGUT_xxCDEFGH @xxCDEFGH  (GateBoy.cpp:722)
            [nor2] AWOD_ABxxxxxx @ABxxxxxx  (GateBoy.cpp:723)
              [not1] ABUZ_EXT_RAM_CS_CLK  (GateBoy.cpp:724)
                [nand2] TUCA_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:520)
                  [not1] TOLE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:521)
                    [and2] SERE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:523)
                      [and2] SAZO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:525)
                        [not1] RYJE_CBD_TO_VPDn_new  (GateBoyVramBus.cpp:526)
                          [not1] REVO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:527)
                            [and2] ROCY_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:609)
                              [not1] RAHU_CBD_TO_VPDn_new (fan-out: 17)  (GateBoyVramBus.cpp:610)
                                [tri10_np] TYGO_CD2_TO_VD2_new  (GateBoyVramBus.cpp:615)
                                  [BUS] BUS_VRAM_D02p  (GateBoyVramBus.cpp:624)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `BUS_VRAM_D03p` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:976)
        [not1] AJAX_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:720)
          [or_and3] AGUT_xxCDEFGH @xxCDEFGH  (GateBoy.cpp:722)
            [nor2] AWOD_ABxxxxxx @ABxxxxxx  (GateBoy.cpp:723)
              [not1] ABUZ_EXT_RAM_CS_CLK  (GateBoy.cpp:724)
                [nand2] TUCA_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:520)
                  [not1] TOLE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:521)
                    [and2] SERE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:523)
                      [and2] SAZO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:525)
                        [not1] RYJE_CBD_TO_VPDn_new  (GateBoyVramBus.cpp:526)
                          [not1] REVO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:527)
                            [and2] ROCY_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:609)
                              [not1] RAHU_CBD_TO_VPDn_new (fan-out: 17)  (GateBoyVramBus.cpp:610)
                                [tri10_np] SOTE_CD3_TO_VD3_new  (GateBoyVramBus.cpp:616)
                                  [BUS] BUS_VRAM_D03p  (GateBoyVramBus.cpp:625)
```

**Depth 14** (70-210 ns, 176% half T-cycle): `AFUR_ABCDxxxx` -> `BUS_VRAM_D04p` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:976)
        [not1] AJAX_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:720)
          [or_and3] AGUT_xxCDEFGH @xxCDEFGH  (GateBoy.cpp:722)
            [nor2] AWOD_ABxxxxxx @ABxxxxxx  (GateBoy.cpp:723)
              [not1] ABUZ_EXT_RAM_CS_CLK  (GateBoy.cpp:724)
                [nand2] TUCA_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:520)
                  [not1] TOLE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:521)
                    [and2] SERE_CPU_VRAM_RDp_new  (GateBoyVramBus.cpp:523)
                      [and2] SAZO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:525)
                        [not1] RYJE_CBD_TO_VPDn_new  (GateBoyVramBus.cpp:526)
                          [not1] REVO_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:527)
                            [and2] ROCY_CBD_TO_VPDp_new  (GateBoyVramBus.cpp:609)
                              [not1] RAHU_CBD_TO_VPDn_new (fan-out: 17)  (GateBoyVramBus.cpp:610)
                                [tri10_np] SEKE_CD4_TO_VD4_new  (GateBoyVramBus.cpp:617)
                                  [BUS] BUS_VRAM_D04p  (GateBoyVramBus.cpp:626)
```

*...and 103 more paths in this category.*

### Interrupts (max depth 12, 13 paths)

**Depth 12** (60-180 ns, 151% half T-cycle): `XEHO_PX0p_odd` -> `LALU_FF0F_D1p` [src @ODD]

```
    [REGISTERED] XEHO_PX0p_odd @ODD  (GateBoy.cpp:1094)
      [not1] ACAM_PX0n_odd @ODD (fan-out: 10)  (GateBoySpriteStore.cpp:349)
        [xor2] ZOGY_STORE0_MATCH0n  (GateBoySpriteStore.cpp:358)
          [nor4] ZAKO_STORE0_MATCHAp  (GateBoySpriteStore.cpp:448)
            [nand3] YDUG_STORE0_MATCHn  (GateBoySpriteStore.cpp:469)
              [nand5] FEFY_STORE_MATCHp  (GateBoySpriteStore.cpp:480)
                [or2] FEPO_STORE_MATCHp_odd @ODD  (GateBoySpriteStore.cpp:482)
                  [not1] XENA_STORE_MATCHn_odd @ODD  (GateBoy.cpp:1121)
                    [and2] WODU_HBLANK_GATEp_odd @ODD  (GateBoy.cpp:1129)
                      [and2] TARU_INT_HBL_new  (GateBoyInterrupts.cpp:77)
                        [amux4] SUKO_INT_STATp_new  (GateBoyInterrupts.cpp:78)
                          [not1] TUVA_INT_STATn_new  (GateBoyInterrupts.cpp:85)
                            [not1] VOTY_INT_STATp_new  (GateBoyInterrupts.cpp:86)
                              [REGISTERED] LALU_FF0F_D1p  (GateBoyInterrupts.cpp:122)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ADYK_xxxDEFGx` -> `NYBO_FF0F_D2p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [nand4] REFA_FF0F_WRn_new  (GateBoyInterrupts.cpp:90)
                    [not1] ROTU_FF0F_WRp  (GateBoyInterrupts.cpp:102)
                      [nand3] PYHU_FF0F_SET2n  (GateBoyInterrupts.cpp:105)
                        [REGISTERED] NYBO_FF0F_D2p  (GateBoyInterrupts.cpp:123)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ADYK_xxxDEFGx` -> `UBUL_FF0F_D3p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [nand4] REFA_FF0F_WRn_new  (GateBoyInterrupts.cpp:90)
                    [not1] ROTU_FF0F_WRp  (GateBoyInterrupts.cpp:102)
                      [nand3] TOME_FF0F_SET3n  (GateBoyInterrupts.cpp:106)
                        [REGISTERED] UBUL_FF0F_D3p  (GateBoyInterrupts.cpp:127)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ADYK_xxxDEFGx` -> `ULAK_FF0F_D4p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [nand4] REFA_FF0F_WRn_new  (GateBoyInterrupts.cpp:90)
                    [not1] ROTU_FF0F_WRp  (GateBoyInterrupts.cpp:102)
                      [nand3] TOGA_FF0F_SET4n  (GateBoyInterrupts.cpp:107)
                        [REGISTERED] ULAK_FF0F_D4p  (GateBoyInterrupts.cpp:128)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ADYK_xxxDEFGx` -> `LOPE_FF0F_D0p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [nand4] REFA_FF0F_WRn_new  (GateBoyInterrupts.cpp:90)
                    [not1] ROTU_FF0F_WRp  (GateBoyInterrupts.cpp:102)
                      [nand3] MYZU_FF0F_SET0n  (GateBoyInterrupts.cpp:103)
                        [REGISTERED] LOPE_FF0F_D0p  (GateBoyInterrupts.cpp:121)
```

*...and 8 more paths in this category.*

### STAT/LY Match (max depth 11, 7 paths)

**Depth 11** (55-165 ns, 138% half T-cycle): `ADYK_xxxDEFGx` -> `RUPO_LYC_MATCHn` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyLCD.cpp:20)
                    [not1] CUPA_CPU_WRp_new  (GateBoyLCD.cpp:21)
                      [and2] SEPA_FF41_WRp_new  (GateBoyLCD.cpp:80)
                        [not1] RYJU_FF41_WRn_new  (GateBoyLCD.cpp:81)
                          [or2] PAGO_LYC_MATCH_RST_new  (GateBoyLCD.cpp:82)
                            [REGISTERED] RUPO_LYC_MATCHn  (GateBoyLCD.cpp:83)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `ROXE_STAT_HBI_ENp` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyInterrupts.cpp:31)
                    [not1] CUPA_CPU_WRp_new  (GateBoyInterrupts.cpp:32)
                      [and2] SEPA_FF41_WRp_new  (GateBoyInterrupts.cpp:34)
                        [not1] RYVE_FF41_WRn_new  (GateBoyInterrupts.cpp:35)
                          [REGISTERED] ROXE_STAT_HBI_ENp  (GateBoyInterrupts.cpp:43)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `RUFO_STAT_VBI_ENp` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyInterrupts.cpp:31)
                    [not1] CUPA_CPU_WRp_new  (GateBoyInterrupts.cpp:32)
                      [and2] SEPA_FF41_WRp_new  (GateBoyInterrupts.cpp:34)
                        [not1] RYVE_FF41_WRn_new  (GateBoyInterrupts.cpp:35)
                          [REGISTERED] RUFO_STAT_VBI_ENp  (GateBoyInterrupts.cpp:44)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `REFE_STAT_OAI_ENp` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyInterrupts.cpp:31)
                    [not1] CUPA_CPU_WRp_new  (GateBoyInterrupts.cpp:32)
                      [and2] SEPA_FF41_WRp_new  (GateBoyInterrupts.cpp:34)
                        [not1] RYVE_FF41_WRn_new  (GateBoyInterrupts.cpp:35)
                          [REGISTERED] REFE_STAT_OAI_ENp  (GateBoyInterrupts.cpp:45)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `RUGU_STAT_LYI_ENp` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyInterrupts.cpp:31)
                    [not1] CUPA_CPU_WRp_new  (GateBoyInterrupts.cpp:32)
                      [and2] SEPA_FF41_WRp_new  (GateBoyInterrupts.cpp:34)
                        [not1] RYVE_FF41_WRn_new  (GateBoyInterrupts.cpp:35)
                          [REGISTERED] RUGU_STAT_LYI_ENp  (GateBoyInterrupts.cpp:46)
```

*...and 2 more paths in this category.*

### OAM Bus (max depth 11, 102 paths)

**Depth 11** (55-165 ns, 138% half T-cycle): `ADYK_xxxDEFGx` -> `SIG_OAM_WRn_B` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyOamBus.cpp:152)
                    [not1] CUPA_CPU_WRp_new  (GateBoyOamBus.cpp:153)
                      [and_or3] WYJA_OAM_WRp_new  (GateBoyOamBus.cpp:326)
                        [and2] YLYC_OAM_B_WRp_new  (GateBoyOamBus.cpp:328)
                          [not1] ZONE_OAM_B_WRn_new  (GateBoyOamBus.cpp:330)
                            [BOUNDARY] SIG_OAM_WRn_B  (GateBoyOamBus.cpp:333)
```

**Depth 11** (55-165 ns, 138% half T-cycle): `ADYK_xxxDEFGx` -> `SIG_OAM_WRn_A` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyOamBus.cpp:152)
                    [not1] CUPA_CPU_WRp_new  (GateBoyOamBus.cpp:153)
                      [and_or3] WYJA_OAM_WRp_new  (GateBoyOamBus.cpp:326)
                        [and2] YNYC_OAM_A_WRp_new  (GateBoyOamBus.cpp:327)
                          [not1] ZOFE_OAM_A_WRn_new  (GateBoyOamBus.cpp:329)
                            [BOUNDARY] SIG_OAM_WRn_A  (GateBoyOamBus.cpp:332)
```

**Depth 11** (55-165 ns, 138% half T-cycle): `TUNA_0000_FDFF_new` -> `SIG_OAM_OEn`

```
    [nand7] TUNA_0000_FDFF_new  (GateBoyCpuBus.cpp:172)
      [nor2] SYKE_ADDR_HIp_new  (GateBoyCpuBus.cpp:194)
        [not1] SOHA_ADDR_HIn_new  (GateBoyCpuBus.cpp:207)
          [nand2] ROPE_ADDR_OAMn_new  (GateBoyCpuBus.cpp:222)
            [not1] SARO_ADDR_OAMp_new  (GateBoyCpuBus.cpp:223)
              [nand3] BOTA_OAM_OEn_new  (GateBoyOamBus.cpp:348)
                [and3] ASYT_OAM_OEn_new  (GateBoyOamBus.cpp:349)
                  [not1] BODE_OAM_OEp_new (fan-out: 17)  (GateBoyOamBus.cpp:351)
                    [not1] YVAL_OAM_OEn_new  (GateBoyOamBus.cpp:352)
                      [not1] YRYV_OAM_OEp_new  (GateBoyOamBus.cpp:353)
                        [not1] ZODO_OAM_OEn_new (fan-out: 17)  (GateBoyOamBus.cpp:354)
                          [BOUNDARY] SIG_OAM_OEn  (GateBoyOamBus.cpp:355)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `AFUR_ABCDxxxx` -> `XUSO_OAM_DA0n` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:976)
        [nor2] BELU_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:977)
          [not1] BYRY_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:978)
            [not1] BUDE_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:979)
              [not1] UVYT_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:980)
                [not1] MOPA_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:981)
                  [not_or_and3] CUFE_OAM_CLKp  (GateBoy.cpp:983)
                    [nand3] BYCU_OAM_CLKp  (GateBoy.cpp:993)
                      [not1] COTA_OAM_CLKn  (GateBoy.cpp:994)
                        [not1] YWOK_OAM_CLKp  (GateBoyOamBus.cpp:15)
                          [REGISTERED] XUSO_OAM_DA0n  (GateBoyOamBus.cpp:19)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `AFUR_ABCDxxxx` -> `XEGU_OAM_DA1n` [src @ABCDxxxx]

```
    [REGISTERED] AFUR_ABCDxxxx @ABCDxxxx  (GateBoyClocks.cpp:46)
      [not1] ATYP_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:976)
        [nor2] BELU_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:977)
          [not1] BYRY_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:978)
            [not1] BUDE_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:979)
              [not1] UVYT_ABCDxxxx @ABCDxxxx  (GateBoy.cpp:980)
                [not1] MOPA_xxxxEFGH @xxxxEFGH  (GateBoy.cpp:981)
                  [not_or_and3] CUFE_OAM_CLKp  (GateBoy.cpp:983)
                    [nand3] BYCU_OAM_CLKp  (GateBoy.cpp:993)
                      [not1] COTA_OAM_CLKn  (GateBoy.cpp:994)
                        [not1] YWOK_OAM_CLKp  (GateBoyOamBus.cpp:15)
                          [REGISTERED] XEGU_OAM_DA1n  (GateBoyOamBus.cpp:20)
```

*...and 97 more paths in this category.*

### PPU Registers (max depth 10, 64 paths)

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `PAVO_BGP_D0p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyPixPipe.cpp:141)
                    [not1] CUPA_CPU_WRp_new  (GateBoyPixPipe.cpp:142)
                      [and2] VELY_FF47_WRp_new  (GateBoyPixPipe.cpp:518)
                        [not1] TEPO_FF47_WRp_new  (GateBoyPixPipe.cpp:519)
                          [REGISTERED] PAVO_BGP_D0p  (GateBoyPixPipe.cpp:521)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `NUSY_BGP_D1p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyPixPipe.cpp:141)
                    [not1] CUPA_CPU_WRp_new  (GateBoyPixPipe.cpp:142)
                      [and2] VELY_FF47_WRp_new  (GateBoyPixPipe.cpp:518)
                        [not1] TEPO_FF47_WRp_new  (GateBoyPixPipe.cpp:519)
                          [REGISTERED] NUSY_BGP_D1p  (GateBoyPixPipe.cpp:522)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `PYLU_BGP_D2p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyPixPipe.cpp:141)
                    [not1] CUPA_CPU_WRp_new  (GateBoyPixPipe.cpp:142)
                      [and2] VELY_FF47_WRp_new  (GateBoyPixPipe.cpp:518)
                        [not1] TEPO_FF47_WRp_new  (GateBoyPixPipe.cpp:519)
                          [REGISTERED] PYLU_BGP_D2p  (GateBoyPixPipe.cpp:523)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `MAXY_BGP_D3p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyPixPipe.cpp:141)
                    [not1] CUPA_CPU_WRp_new  (GateBoyPixPipe.cpp:142)
                      [and2] VELY_FF47_WRp_new  (GateBoyPixPipe.cpp:518)
                        [not1] TEPO_FF47_WRp_new  (GateBoyPixPipe.cpp:519)
                          [REGISTERED] MAXY_BGP_D3p  (GateBoyPixPipe.cpp:524)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `MUKE_BGP_D4p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyPixPipe.cpp:141)
                    [not1] CUPA_CPU_WRp_new  (GateBoyPixPipe.cpp:142)
                      [and2] VELY_FF47_WRp_new  (GateBoyPixPipe.cpp:518)
                        [not1] TEPO_FF47_WRp_new  (GateBoyPixPipe.cpp:519)
                          [REGISTERED] MUKE_BGP_D4p  (GateBoyPixPipe.cpp:525)
```

*...and 59 more paths in this category.*

### DMA (max depth 10, 15 paths)

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `NAFA_DMA_A08p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyDMA.cpp:24)
                    [not1] CUPA_CPU_WRp_new  (GateBoyDMA.cpp:25)
                      [and2] LAVY_FF46_WRp_new  (GateBoyDMA.cpp:27)
                        [not1] LORU_FF46_WRn_new  (GateBoyDMA.cpp:28)
                          [REGISTERED] NAFA_DMA_A08p  (GateBoyDMA.cpp:29)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `PYNE_DMA_A09p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyDMA.cpp:24)
                    [not1] CUPA_CPU_WRp_new  (GateBoyDMA.cpp:25)
                      [and2] LAVY_FF46_WRp_new  (GateBoyDMA.cpp:27)
                        [not1] LORU_FF46_WRn_new  (GateBoyDMA.cpp:28)
                          [REGISTERED] PYNE_DMA_A09p  (GateBoyDMA.cpp:30)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `PARA_DMA_A10p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyDMA.cpp:24)
                    [not1] CUPA_CPU_WRp_new  (GateBoyDMA.cpp:25)
                      [and2] LAVY_FF46_WRp_new  (GateBoyDMA.cpp:27)
                        [not1] LORU_FF46_WRn_new  (GateBoyDMA.cpp:28)
                          [REGISTERED] PARA_DMA_A10p  (GateBoyDMA.cpp:31)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `NYDO_DMA_A11p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyDMA.cpp:24)
                    [not1] CUPA_CPU_WRp_new  (GateBoyDMA.cpp:25)
                      [and2] LAVY_FF46_WRp_new  (GateBoyDMA.cpp:27)
                        [not1] LORU_FF46_WRn_new  (GateBoyDMA.cpp:28)
                          [REGISTERED] NYDO_DMA_A11p  (GateBoyDMA.cpp:32)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `NYGY_DMA_A12p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyDMA.cpp:24)
                    [not1] CUPA_CPU_WRp_new  (GateBoyDMA.cpp:25)
                      [and2] LAVY_FF46_WRp_new  (GateBoyDMA.cpp:27)
                        [not1] LORU_FF46_WRn_new  (GateBoyDMA.cpp:28)
                          [REGISTERED] NYGY_DMA_A12p  (GateBoyDMA.cpp:33)
```

*...and 10 more paths in this category.*

### LYC Register (max depth 10, 8 paths)

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `SYRY_LYC0p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyLCD.cpp:20)
                    [not1] CUPA_CPU_WRp_new  (GateBoyLCD.cpp:21)
                      [and2] XUFA_FF45_WRn_new  (GateBoyLCD.cpp:44)
                        [not1] WANE_FF45_WRp_new  (GateBoyLCD.cpp:45)
                          [REGISTERED] SYRY_LYC0p  (GateBoyLCD.cpp:46)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `VUCE_LYC1p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyLCD.cpp:20)
                    [not1] CUPA_CPU_WRp_new  (GateBoyLCD.cpp:21)
                      [and2] XUFA_FF45_WRn_new  (GateBoyLCD.cpp:44)
                        [not1] WANE_FF45_WRp_new  (GateBoyLCD.cpp:45)
                          [REGISTERED] VUCE_LYC1p  (GateBoyLCD.cpp:47)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `SEDY_LYC2p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyLCD.cpp:20)
                    [not1] CUPA_CPU_WRp_new  (GateBoyLCD.cpp:21)
                      [and2] XUFA_FF45_WRn_new  (GateBoyLCD.cpp:44)
                        [not1] WANE_FF45_WRp_new  (GateBoyLCD.cpp:45)
                          [REGISTERED] SEDY_LYC2p  (GateBoyLCD.cpp:48)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `SALO_LYC3p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyLCD.cpp:20)
                    [not1] CUPA_CPU_WRp_new  (GateBoyLCD.cpp:21)
                      [and2] XUFA_FF45_WRn_new  (GateBoyLCD.cpp:44)
                        [not1] WANE_FF45_WRp_new  (GateBoyLCD.cpp:45)
                          [REGISTERED] SALO_LYC3p  (GateBoyLCD.cpp:49)
```

**Depth 10** (50-150 ns, 126% half T-cycle): `ADYK_xxxDEFGx` -> `SOTA_LYC4p` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [not1] DYKY_CPU_WRn_new  (GateBoyLCD.cpp:20)
                    [not1] CUPA_CPU_WRp_new  (GateBoyLCD.cpp:21)
                      [and2] XUFA_FF45_WRn_new  (GateBoyLCD.cpp:44)
                        [not1] WANE_FF45_WRp_new  (GateBoyLCD.cpp:45)
                          [REGISTERED] SOTA_LYC4p  (GateBoyLCD.cpp:50)
```

*...and 3 more paths in this category.*

### Sprite Fetcher (max depth 9, 8 paths)

**Depth 9** (45-135 ns, 113% half T-cycle): `ARYS_xBxDxFxH` -> `SOBU_SFETCH_REQp_evn  ` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] LAPE_AxCxExGx @AxCxExGx  (GateBoy.cpp:744)
                    [not1] TAVA_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:745)
                      [REGISTERED] SOBU_SFETCH_REQp_evn   @EVN  (GateBoy.cpp:841)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ARYS_xBxDxFxH` -> `TOBU_SFETCH_S1p_D2_evn` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] LAPE_AxCxExGx @AxCxExGx  (GateBoy.cpp:744)
                    [not1] TAVA_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:745)
                      [REGISTERED] TOBU_SFETCH_S1p_D2_evn @EVN  (GateBoy.cpp:844)
```

**Depth 9** (45-135 ns, 113% half T-cycle): `ARYS_xBxDxFxH` -> `VONU_SFETCH_S1p_D4_evn` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] LAPE_AxCxExGx @AxCxExGx  (GateBoy.cpp:744)
                    [not1] TAVA_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:745)
                      [REGISTERED] VONU_SFETCH_S1p_D4_evn @EVN  (GateBoy.cpp:845)
```

**Depth 8** (40-120 ns, 101% half T-cycle): `ARYS_xBxDxFxH` -> `SUDA_SFETCH_REQp_odd  ` [src @xBxDxFxH, sink @ODD]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] LAPE_AxCxExGx @AxCxExGx  (GateBoy.cpp:744)
                    [REGISTERED] SUDA_SFETCH_REQp_odd   @ODD  (GateBoy.cpp:842)
```

**Depth 8** (40-120 ns, 101% half T-cycle): `ARYS_xBxDxFxH` -> `TYFO_SFETCH_S0p_D1_odd` [src @xBxDxFxH, sink @ODD]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] LAPE_AxCxExGx @AxCxExGx  (GateBoy.cpp:744)
                    [REGISTERED] TYFO_SFETCH_S0p_D1_odd @ODD  (GateBoy.cpp:843)
```

*...and 3 more paths in this category.*

### Scroll/Fine Timing (max depth 8, 4 paths)

**Depth 8** (40-120 ns, 101% half T-cycle): `ARYS_xBxDxFxH` -> `NYZE_SCX_FINE_MATCH_odd` [src @xBxDxFxH, sink @ODD]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] MOXE_AxCxExGx @AxCxExGx  (GateBoy.cpp:1075)
                    [REGISTERED] NYZE_SCX_FINE_MATCH_odd @ODD  (GateBoy.cpp:1078)
```

**Depth 3** (15-45 ns, 38% half T-cycle): `DATY_SCX0p@old` -> `PUXA_SCX_FINE_MATCH_evn` [sink @EVN]

```
    [REGISTERED] DATY_SCX0p@old  (GateBoy.cpp:1064)
      [xnor2] SUHA_SCX_FINE_MATCHp_old_odd @ODD  (GateBoy.cpp:1064)
        [nand4] RONE_SCX_FINE_MATCHn_old_odd @ODD  (GateBoy.cpp:1067)
          [not1] POHU_SCX_FINE_MATCHp_old_odd @ODD  (GateBoy.cpp:1068)
            [REGISTERED] PUXA_SCX_FINE_MATCH_evn @EVN  (GateBoy.cpp:1077)
```

**Depth 1** (5-15 ns, 13% half T-cycle): `XYMU_RENDERING_LATCHn` -> `ROXY_FINE_SCROLL_DONEn`

```
    [REGISTERED] XYMU_RENDERING_LATCHn (fan-out: 25)  (GateBoy.cpp:827)
      [not1] PAHA_RENDERINGn  (GateBoy.cpp:830)
        [REGISTERED] ROXY_FINE_SCROLL_DONEn  (GateBoy.cpp:1081)
```

### Tile Fetcher (max depth 8, 10 paths)

**Depth 8** (40-120 ns, 101% half T-cycle): `ARYS_xBxDxFxH` -> `PORY_FETCH_DONEp_odd` [src @xBxDxFxH, sink @ODD]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] MYVO_AxCxExGx @AxCxExGx  (GateBoy.cpp:900)
                    [REGISTERED] PORY_FETCH_DONEp_odd @ODD  (GateBoy.cpp:914)
```

**Depth 8** (40-120 ns, 101% half T-cycle): `ARYS_xBxDxFxH` -> `LOVY_TFETCH_DONEp` [src @xBxDxFxH]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] MYVO_AxCxExGx @AxCxExGx  (GateBoy.cpp:900)
                    [REGISTERED] LOVY_TFETCH_DONEp  (GateBoy.cpp:1193)
```

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `PYGO_FETCH_DONEp_evn` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [REGISTERED] PYGO_FETCH_DONEp_evn @EVN  (GateBoy.cpp:913)
```

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `LYZU_BFETCH_S0p_D1` [src @xBxDxFxH]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [REGISTERED] LYZU_BFETCH_S0p_D1  (GateBoy.cpp:1164)
```

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `NYKA_FETCH_DONEp_evn` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [REGISTERED] NYKA_FETCH_DONEp_evn @EVN  (GateBoy.cpp:915)
```

*...and 5 more paths in this category.*

### Window Logic (max depth 8, 9 paths)

**Depth 8** (40-120 ns, 101% half T-cycle): `ARYS_xBxDxFxH` -> `NUNU_WIN_MATCHp_odd` [src @xBxDxFxH, sink @ODD]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [not1] MEHE_AxCxExGx @AxCxExGx  (GateBoy.cpp:899)
                    [REGISTERED] NUNU_WIN_MATCHp_odd @ODD  (GateBoy.cpp:902)
```

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `RENE_WIN_FETCHn_B` [src @xBxDxFxH]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoyPixPipe.cpp:23)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoyPixPipe.cpp:24)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoyPixPipe.cpp:25)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoyPixPipe.cpp:26)
                [not1] ALET_xBxDxFxH @xBxDxFxH  (GateBoyPixPipe.cpp:27)
                  [REGISTERED] RENE_WIN_FETCHn_B  (GateBoyPixPipe.cpp:33)
```

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `SOVY_WIN_HITp` [src @xBxDxFxH]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [REGISTERED] SOVY_WIN_HITp  (GateBoy.cpp:940)
```

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `NOPA_WIN_MODE_Bp_evn` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [REGISTERED] NOPA_WIN_MODE_Bp_evn @EVN  (GateBoy.cpp:903)
```

**Depth 5** (25-75 ns, 63% half T-cycle): `LOVU_LY4p_odd` -> `SARY_WY_MATCHp_odd` [src @ODD, sink @ODD]

```
    [REGISTERED] LOVU_LY4p_odd @ODD  (GateBoyLCD.cpp:166)
      [xnor2] NOJO_WY_MATCH4p_odd_new @ODD  (GateBoyPixPipe.cpp:65)
        [nand5] PALO_WY_MATCHn_odd_new @ODD  (GateBoyPixPipe.cpp:79)
          [not1] NELE_WY_MATCHp_odd_new @ODD  (GateBoyPixPipe.cpp:80)
            [nand5] PAFU_WY_MATCHn_odd_new @ODD  (GateBoyPixPipe.cpp:81)
              [not1] ROGE_WY_MATCHp_odd @ODD  (GateBoyPixPipe.cpp:84)
                [REGISTERED] SARY_WY_MATCHp_odd @ODD  (GateBoyPixPipe.cpp:83)
```

*...and 4 more paths in this category.*

### LY Counter (max depth 7, 3 paths)

**Depth 7** (35-105 ns, 88% half T-cycle): `ADYK_xxxDEFGx` -> `KELY_JOYP_UDLRp` [src @xxxDEFGx]

```
    [REGISTERED] ADYK_xxxDEFGx @xxxDEFGx  (GateBoyClocks.cpp:49)
      [not1] ADAR_ABCxxxxH @ABCxxxxH  (GateBoy.cpp:709)
        [nor2] AFAS_xxxxEFGx @xxxxEFGx  (GateBoy.cpp:711)
          [nand2] AREV_CPU_WRn  (GateBoy.cpp:712)
            [not1] APOV_CPU_WRp  (GateBoy.cpp:713)
              [not1] UBAL_CPU_WRn  (GateBoy.cpp:714)
                [not1] TAPU_CPU_WRp (fan-out: 17)  (GateBoy.cpp:715)
                  [nand4] ATOZ_FF00_WRn_new  (GateBoyJoypad.cpp:34)
                    [REGISTERED] KELY_JOYP_UDLRp  (GateBoyJoypad.cpp:43)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `UVARp_new` -> `ALYR_EXT_ADDR_LATCH_02p`

```
    [not1] UVARp_new  (GateBoyPins.cpp:96)
      [and2] UMUT_MODE_DBG1p_new  (GateBoyPins.cpp:98)
        [not1] MULE_MODE_DBG1n_new  (GateBoyPins.cpp:99)
          [and_or3] LOXO_HOLDn_new  (GateBoyExtBus.cpp:182)
            [not1] LASY_HOLDp_new  (GateBoyExtBus.cpp:183)
              [not1] MATE_HOLDn_new (fan-out: 15)  (GateBoyExtBus.cpp:184)
                [REGISTERED] ALYR_EXT_ADDR_LATCH_02p  (GateBoyExtBus.cpp:215)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `UVARp_new` -> `LYSA_EXT_ADDR_LATCH_09p`

```
    [not1] UVARp_new  (GateBoyPins.cpp:96)
      [and2] UMUT_MODE_DBG1p_new  (GateBoyPins.cpp:98)
        [not1] MULE_MODE_DBG1n_new  (GateBoyPins.cpp:99)
          [and_or3] LOXO_HOLDn_new  (GateBoyExtBus.cpp:182)
            [not1] LASY_HOLDp_new  (GateBoyExtBus.cpp:183)
              [not1] MATE_HOLDn_new (fan-out: 15)  (GateBoyExtBus.cpp:184)
                [REGISTERED] LYSA_EXT_ADDR_LATCH_09p  (GateBoyExtBus.cpp:223)
```

### Mode/Rendering Control (max depth 7, 3 paths)

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `VOGA_HBLANKp_evn` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [REGISTERED] VOGA_HBLANKp_evn @EVN  (GateBoy.cpp:825)
```

**Depth 1** (5-15 ns, 13% half T-cycle): `LOVU_LY4p_odd@old` -> `POPU_VBLANKp_odd   ` [src @ODD, sink @ODD]

```
    [REGISTERED] LOVU_LY4p_odd@old @ODD  (GateBoyLCD.cpp:30)
      [and2] XYVO_y144p_old  (GateBoyLCD.cpp:96)
        [REGISTERED] POPU_VBLANKp_odd    @ODD  (GateBoyLCD.cpp:126)
```

**Depth 1** (5-15 ns, 13% half T-cycle): `VOGA_HBLANKp_evn` -> `XYMU_RENDERING_LATCHn` [src @EVN]

```
    [REGISTERED] VOGA_HBLANKp_evn @EVN  (GateBoy.cpp:825)
      [or2] WEGO_HBLANKp_evn_new @EVN  (GateBoy.cpp:826)
        [REGISTERED] XYMU_RENDERING_LATCHn (fan-out: 25)  (GateBoy.cpp:827)
```

### Sprite Scanner (max depth 7, 3 paths)

**Depth 7** (35-105 ns, 88% half T-cycle): `ARYS_xBxDxFxH` -> `DOBA_SCAN_DONEp_evn` [src @xBxDxFxH, sink @EVN]

```
    [not1] ARYS_xBxDxFxH @xBxDxFxH  (GateBoyClocks.cpp:37)
      [nand2] AVET_AxCxExGx @AxCxExGx  (GateBoyClocks.cpp:40)
        [not1] ATAL_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:739)
          [not1] AZOF_AxCxExGx @AxCxExGx  (GateBoy.cpp:740)
            [not1] ZAXY_xBxDxFxH @xBxDxFxH  (GateBoy.cpp:741)
              [not1] ZEME_AxCxExGx @AxCxExGx  (GateBoy.cpp:742)
                [not1] ALET_xBxDxFxH @xBxDxFxH (fan-out: 12)  (GateBoy.cpp:743)
                  [REGISTERED] DOBA_SCAN_DONEp_evn @EVN  (GateBoy.cpp:765)
```

**Depth 1** (5-15 ns, 13% half T-cycle): `WUVU_ABxxEFxx` -> `BYBA_SCAN_DONEp_odd` [src @ABxxEFxx, sink @ODD]

```
    [REGISTERED] WUVU_ABxxEFxx @ABxxEFxx  (GateBoyClocks.cpp:112)
      [not1] XUPY_ABxxEFxx @ABxxEFxx  (GateBoy.cpp:763)
        [REGISTERED] BYBA_SCAN_DONEp_odd @ODD  (GateBoy.cpp:764)
```

**Depth 1** (5-15 ns, 13% half T-cycle): `WUVU_ABxxEFxx` -> `CENO_SCAN_DONEn_odd` [src @ABxxEFxx, sink @ODD]

```
    [REGISTERED] WUVU_ABxxEFxx @ABxxEFxx  (GateBoyClocks.cpp:112)
      [not1] XUPY_ABxxEFxx @ABxxEFxx  (GateBoy.cpp:763)
        [REGISTERED] CENO_SCAN_DONEn_odd @ODD  (GateBoy.cpp:772)
```

### Sprite Store/Match (max depth 6, 282 paths)

**Depth 6** (30-90 ns, 76% half T-cycle): `BESE_SPRITE_COUNT0_odd` -> `DANY_STORE1_X0p` [src @ODD]

```
    [REGISTERED] BESE_SPRITE_COUNT0_odd @ODD  (GateBoy.cpp:1029)
      [not1] EDEN_SPRITE_COUNT0n  (GateBoySpriteStore.cpp:17)
        [not1] FYCU_SPRITE_COUNT0p  (GateBoySpriteStore.cpp:22)
          [nand4] CUVA_STORE1_SELn  (GateBoySpriteStore.cpp:28)
            [or2] BYBY_STORE1_CLKp  (GateBoySpriteStore.cpp:39)
              [not1] BUCO_STORE1_CLKn  (GateBoySpriteStore.cpp:50)
                [not1] ASYS_STORE1_CLKp  (GateBoySpriteStore.cpp:61)
                  [REGISTERED] DANY_STORE1_X0p  (GateBoySpriteStore.cpp:114)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `BESE_SPRITE_COUNT0_odd` -> `DUKO_STORE1_X1p` [src @ODD]

```
    [REGISTERED] BESE_SPRITE_COUNT0_odd @ODD  (GateBoy.cpp:1029)
      [not1] EDEN_SPRITE_COUNT0n  (GateBoySpriteStore.cpp:17)
        [not1] FYCU_SPRITE_COUNT0p  (GateBoySpriteStore.cpp:22)
          [nand4] CUVA_STORE1_SELn  (GateBoySpriteStore.cpp:28)
            [or2] BYBY_STORE1_CLKp  (GateBoySpriteStore.cpp:39)
              [not1] BUCO_STORE1_CLKn  (GateBoySpriteStore.cpp:50)
                [not1] ASYS_STORE1_CLKp  (GateBoySpriteStore.cpp:61)
                  [REGISTERED] DUKO_STORE1_X1p  (GateBoySpriteStore.cpp:115)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `BESE_SPRITE_COUNT0_odd` -> `DESU_STORE1_X2p` [src @ODD]

```
    [REGISTERED] BESE_SPRITE_COUNT0_odd @ODD  (GateBoy.cpp:1029)
      [not1] EDEN_SPRITE_COUNT0n  (GateBoySpriteStore.cpp:17)
        [not1] FYCU_SPRITE_COUNT0p  (GateBoySpriteStore.cpp:22)
          [nand4] CUVA_STORE1_SELn  (GateBoySpriteStore.cpp:28)
            [or2] BYBY_STORE1_CLKp  (GateBoySpriteStore.cpp:39)
              [not1] BUCO_STORE1_CLKn  (GateBoySpriteStore.cpp:50)
                [not1] ASYS_STORE1_CLKp  (GateBoySpriteStore.cpp:61)
                  [REGISTERED] DESU_STORE1_X2p  (GateBoySpriteStore.cpp:116)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `BESE_SPRITE_COUNT0_odd` -> `DAZO_STORE1_X3p` [src @ODD]

```
    [REGISTERED] BESE_SPRITE_COUNT0_odd @ODD  (GateBoy.cpp:1029)
      [not1] EDEN_SPRITE_COUNT0n  (GateBoySpriteStore.cpp:17)
        [not1] FYCU_SPRITE_COUNT0p  (GateBoySpriteStore.cpp:22)
          [nand4] CUVA_STORE1_SELn  (GateBoySpriteStore.cpp:28)
            [or2] BYBY_STORE1_CLKp  (GateBoySpriteStore.cpp:39)
              [not1] BUCO_STORE1_CLKn  (GateBoySpriteStore.cpp:50)
                [not1] ASYS_STORE1_CLKp  (GateBoySpriteStore.cpp:61)
                  [REGISTERED] DAZO_STORE1_X3p  (GateBoySpriteStore.cpp:117)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `BESE_SPRITE_COUNT0_odd` -> `DAKE_STORE1_X4p` [src @ODD]

```
    [REGISTERED] BESE_SPRITE_COUNT0_odd @ODD  (GateBoy.cpp:1029)
      [not1] EDEN_SPRITE_COUNT0n  (GateBoySpriteStore.cpp:17)
        [not1] FYCU_SPRITE_COUNT0p  (GateBoySpriteStore.cpp:22)
          [nand4] CUVA_STORE1_SELn  (GateBoySpriteStore.cpp:28)
            [or2] BYBY_STORE1_CLKp  (GateBoySpriteStore.cpp:39)
              [not1] BUCO_STORE1_CLKn  (GateBoySpriteStore.cpp:50)
                [not1] ASYS_STORE1_CLKp  (GateBoySpriteStore.cpp:61)
                  [REGISTERED] DAKE_STORE1_X4p  (GateBoySpriteStore.cpp:118)
```

*...and 277 more paths in this category.*

### Pixel Pipeline (max depth 6, 40 paths)

**Depth 6** (30-90 ns, 76% half T-cycle): `TYFO_SFETCH_S0p_D1_odd` -> `NYLU_SPR_PIPE_B0` [src @ODD]

```
    [REGISTERED] TYFO_SFETCH_S0p_D1_odd @ODD  (GateBoy.cpp:843)
      [or2] VUSA_SPRITE_DONEn  (GateBoy.cpp:865)
        [not1] WUTY_SFETCH_DONE_TRIGp_odd @ODD (fan-out: 12)  (GateBoy.cpp:866)
          [not1] XEFY_SPRITE_DONEn_odd_new @ODD  (GateBoyPixPipe.cpp:239)
            [or3] MEFU_SPRITE_MASK0n_new  (GateBoyPixPipe.cpp:241)
              [not1] LESY_SPRITE_MASK0p_new  (GateBoyPixPipe.cpp:250)
                [nand2] MEZU_SPR_PIX_SET0_new  (GateBoyPixPipe.cpp:298)
                  [REGISTERED] NYLU_SPR_PIPE_B0  (GateBoyPixPipe.cpp:325)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `TYFO_SFETCH_S0p_D1_odd` -> `VEZO_MASK_PIPE_0` [src @ODD]

```
    [REGISTERED] TYFO_SFETCH_S0p_D1_odd @ODD  (GateBoy.cpp:843)
      [or2] VUSA_SPRITE_DONEn  (GateBoy.cpp:865)
        [not1] WUTY_SFETCH_DONE_TRIGp_odd @ODD (fan-out: 12)  (GateBoy.cpp:866)
          [not1] XEFY_SPRITE_DONEn_odd_new @ODD  (GateBoyPixPipe.cpp:239)
            [or3] MEFU_SPRITE_MASK0n_new  (GateBoyPixPipe.cpp:241)
              [not1] LESY_SPRITE_MASK0p_new  (GateBoyPixPipe.cpp:250)
                [nand2] TEDE_MASK_PIPE_SET0_new  (GateBoyPixPipe.cpp:420)
                  [REGISTERED] VEZO_MASK_PIPE_0  (GateBoyPixPipe.cpp:447)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `TYFO_SFETCH_S0p_D1_odd` -> `RUGO_PAL_PIPE_D0` [src @ODD]

```
    [REGISTERED] TYFO_SFETCH_S0p_D1_odd @ODD  (GateBoy.cpp:843)
      [or2] VUSA_SPRITE_DONEn  (GateBoy.cpp:865)
        [not1] WUTY_SFETCH_DONE_TRIGp_odd @ODD (fan-out: 12)  (GateBoy.cpp:866)
          [not1] XEFY_SPRITE_DONEn_odd_new @ODD  (GateBoyPixPipe.cpp:239)
            [or3] MEFU_SPRITE_MASK0n_new  (GateBoyPixPipe.cpp:241)
              [not1] LESY_SPRITE_MASK0p_new  (GateBoyPixPipe.cpp:250)
                [nand2] PUME_PAL_PIPE_SET0_new  (GateBoyPixPipe.cpp:460)
                  [REGISTERED] RUGO_PAL_PIPE_D0  (GateBoyPixPipe.cpp:487)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `TYFO_SFETCH_S0p_D1_odd` -> `PEFU_SPR_PIPE_B1` [src @ODD]

```
    [REGISTERED] TYFO_SFETCH_S0p_D1_odd @ODD  (GateBoy.cpp:843)
      [or2] VUSA_SPRITE_DONEn  (GateBoy.cpp:865)
        [not1] WUTY_SFETCH_DONE_TRIGp_odd @ODD (fan-out: 12)  (GateBoy.cpp:866)
          [not1] XEFY_SPRITE_DONEn_odd_new @ODD  (GateBoyPixPipe.cpp:239)
            [or3] MEVE_SPRITE_MASK1n_new  (GateBoyPixPipe.cpp:242)
              [not1] LOTA_SPRITE_MASK1p_new  (GateBoyPixPipe.cpp:251)
                [nand2] RUSY_SPR_PIX_SET1_new  (GateBoyPixPipe.cpp:299)
                  [REGISTERED] PEFU_SPR_PIPE_B1  (GateBoyPixPipe.cpp:326)
```

**Depth 6** (30-90 ns, 76% half T-cycle): `TYFO_SFETCH_S0p_D1_odd` -> `WURU_MASK_PIPE_1` [src @ODD]

```
    [REGISTERED] TYFO_SFETCH_S0p_D1_odd @ODD  (GateBoy.cpp:843)
      [or2] VUSA_SPRITE_DONEn  (GateBoy.cpp:865)
        [not1] WUTY_SFETCH_DONE_TRIGp_odd @ODD (fan-out: 12)  (GateBoy.cpp:866)
          [not1] XEFY_SPRITE_DONEn_odd_new @ODD  (GateBoyPixPipe.cpp:239)
            [or3] MEVE_SPRITE_MASK1n_new  (GateBoyPixPipe.cpp:242)
              [not1] LOTA_SPRITE_MASK1p_new  (GateBoyPixPipe.cpp:251)
                [nand2] XALA_MASK_PIPE_SET1_new  (GateBoyPixPipe.cpp:421)
                  [REGISTERED] WURU_MASK_PIPE_1  (GateBoyPixPipe.cpp:448)
```

*...and 35 more paths in this category.*

### Line Timing (max depth 3, 6 paths)

**Depth 3** (15-45 ns, 38% half T-cycle): `LOVU_LY4p_odd@old` -> `CATU_LINE_ENDp_odd` [src @ODD, sink @ODD]

```
    [REGISTERED] LOVU_LY4p_odd@old @ODD  (GateBoyLCD.cpp:30)
      [and2] XYVO_y144p_old  (GateBoyLCD.cpp:96)
        [not1] ALES_FRAME_ENDn_old  (GateBoyLCD.cpp:108)
          [and2] ABOV_LINE_ENDp_old  (GateBoyLCD.cpp:110)
            [REGISTERED] CATU_LINE_ENDp_odd @ODD  (GateBoyLCD.cpp:111)
```

**Depth 2** (10-30 ns, 25% half T-cycle): `VENA_xxCDEFxx` -> `RUTU_LINE_ENDp_odd ` [src @xxCDEFxx, sink @ODD]

```
    [REGISTERED] VENA_xxCDEFxx @xxCDEFxx  (GateBoyClocks.cpp:113)
      [not1] TALU_xxCDEFxx @xxCDEFxx  (GateBoyLCD.cpp:92)
        [not1] SONO_ABxxxxGH @ABxxxxGH  (GateBoyLCD.cpp:93)
          [REGISTERED] RUTU_LINE_ENDp_odd  @ODD  (GateBoyLCD.cpp:124)
```

**Depth 2** (10-30 ns, 25% half T-cycle): `WUVU_ABxxEFxx` -> `ANEL_LINE_ENDp_odd` [src @ABxxEFxx, sink @ODD]

```
    [REGISTERED] WUVU_ABxxEFxx @ABxxEFxx  (GateBoyClocks.cpp:112)
      [not1] XUPY_ABxxEFxx @ABxxEFxx  (GateBoyLCD.cpp:103)
        [not1] AWOH_xxCDxxGH @xxCDxxGH  (GateBoyLCD.cpp:104)
          [REGISTERED] ANEL_LINE_ENDp_odd @ODD  (GateBoyLCD.cpp:105)
```

**Depth 1** (5-15 ns, 13% half T-cycle): `VENA_xxCDEFxx` -> `NYPE_LINE_ENDp_odd ` [src @xxCDEFxx, sink @ODD]

```
    [REGISTERED] VENA_xxCDEFxx @xxCDEFxx  (GateBoyClocks.cpp:113)
      [not1] TALU_xxCDEFxx @xxCDEFxx  (GateBoyLCD.cpp:92)
        [REGISTERED] NYPE_LINE_ENDp_odd  @ODD  (GateBoyLCD.cpp:125)
```

### Pixel Counter (max depth 3, 10 paths)

**Depth 3** (15-45 ns, 38% half T-cycle): `XEHO_PX0p_odd@old` -> `XYDO_PX3p_odd` [src @ODD, sink @ODD]

```
    [REGISTERED] XEHO_PX0p_odd@old @ODD  (GateBoy.cpp:1088)
      [and2] XUKE_old  (GateBoy.cpp:1089)
        [and2] XYLE_old  (GateBoy.cpp:1090)
          [xor2] XORA_old  (GateBoy.cpp:1092)
            [REGISTERED] XYDO_PX3p_odd @ODD  (GateBoy.cpp:1097)
```

**Depth 3** (15-45 ns, 38% half T-cycle): `TUHU_PX4p_odd@old` -> `SYBE_PX7p_odd` [src @ODD, sink @ODD]

```
    [REGISTERED] TUHU_PX4p_odd@old @ODD  (GateBoy.cpp:1100)
      [and2] TYBA_old  (GateBoy.cpp:1101)
        [and2] SURY_old  (GateBoy.cpp:1102)
          [xor2] ROKU_old  (GateBoy.cpp:1104)
            [REGISTERED] SYBE_PX7p_odd @ODD  (GateBoy.cpp:1109)
```

**Depth 2** (10-30 ns, 25% half T-cycle): `XEHO_PX0p_odd@old` -> `XODU_PX2p_odd` [src @ODD, sink @ODD]

```
    [REGISTERED] XEHO_PX0p_odd@old @ODD  (GateBoy.cpp:1088)
      [and2] XUKE_old  (GateBoy.cpp:1089)
        [xor2] XEGY_old  (GateBoy.cpp:1091)
          [REGISTERED] XODU_PX2p_odd @ODD  (GateBoy.cpp:1096)
```

**Depth 2** (10-30 ns, 25% half T-cycle): `TUHU_PX4p_odd@old` -> `TAKO_PX6p_odd` [src @ODD, sink @ODD]

```
    [REGISTERED] TUHU_PX4p_odd@old @ODD  (GateBoy.cpp:1100)
      [and2] TYBA_old  (GateBoy.cpp:1101)
        [xor2] TYGE_old  (GateBoy.cpp:1103)
          [REGISTERED] TAKO_PX6p_odd @ODD  (GateBoy.cpp:1108)
```

**Depth 1** (5-15 ns, 13% half T-cycle): `XEHO_PX0p_odd@old` -> `SAVY_PX1p_odd` [src @ODD, sink @ODD]

```
    [REGISTERED] XEHO_PX0p_odd@old @ODD  (GateBoy.cpp:1088)
      [xor2] RYBO_old  (GateBoy.cpp:1088)
        [REGISTERED] SAVY_PX1p_odd @ODD  (GateBoy.cpp:1095)
```

*...and 5 more paths in this category.*

### LX Counter (max depth 1, 1 paths)

**Depth 1** (5-15 ns, 13% half T-cycle): `VENA_xxCDEFxx` -> `SAXO_LX0p_odd` [src @xxCDEFxx, sink @ODD]

```
    [REGISTERED] VENA_xxCDEFxx @xxCDEFxx  (GateBoyClocks.cpp:113)
      [not1] TALU_xxCDEFxx @xxCDEFxx  (GateBoyLCD.cpp:92)
        [REGISTERED] SAXO_LX0p_odd @ODD  (GateBoyLCD.cpp:151)
```
