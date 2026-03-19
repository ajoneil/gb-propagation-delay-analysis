# GateBoy PPU Critical Combinatorial Paths

Ranked by combinatorial gate depth between registered elements.

Showing top 30 of 1270 paths with depth >= 1.

## Timing Reference

- Game Boy master clock: 4.194304 MHz
- T-cycle period: ~238.4 ns
- Half T-cycle: ~119.2 ns
- Estimated gate delay (Sharp CMOS): 5-15 ns per gate
- Paths exceeding ~8-24 gates may cause signals to arrive late

## Depth Distribution

| Depth | Count | Est. Delay (min) | Est. Delay (max) | % of Half T-cycle |
|-------|-------|-------------------|-------------------|--------------------|
| 19 | 1 | 95 ns | 285 ns | 239% **CRITICAL** |
| 17 | 87 | 85 ns | 255 ns | 214% **CRITICAL** |
| 16 | 57 | 80 ns | 240 ns | 201% **CRITICAL** |
| 15 | 12 | 75 ns | 225 ns | 189% **CRITICAL** |
| 14 | 29 | 70 ns | 210 ns | 176% **CRITICAL** |
| 13 | 23 | 65 ns | 195 ns | 164% **CRITICAL** |
| 12 | 1 | 60 ns | 180 ns | 151% **CRITICAL** |
| 11 | 7 | 55 ns | 165 ns | 138% **CRITICAL** |
| 10 | 130 | 50 ns | 150 ns | 126% **CRITICAL** |
| 9 | 44 | 45 ns | 135 ns | 113% **CRITICAL** |
| 8 | 45 | 40 ns | 120 ns | 101% **CRITICAL** |
| 7 | 71 | 35 ns | 105 ns | 88% **CRITICAL** |
| 6 | 314 | 30 ns | 90 ns | 76% **CRITICAL** |
| 5 | 73 | 25 ns | 75 ns | 63% **CRITICAL** |
| 4 | 53 | 20 ns | 60 ns | 50% **CRITICAL** |
| 3 | 24 | 15 ns | 45 ns | 38% |
| 2 | 181 | 10 ns | 30 ns | 25% |
| 1 | 118 | 5 ns | 15 ns | 13% |

## Top 30 Deepest Paths

### Path 1: Depth 19 (95-285 ns, 239% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `LAXU_BFETCH_S0p_odd` (registered, dff17_any)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [nor2] ANOM_LINE_RSTn_odd_new  (GateBoy.cpp:754)
                              [not1] BALU_LINE_RSTp_odd_new  (GateBoy.cpp:755)
                                [or3] BEBU_SCAN_DONE_tn_odd_new  (GateBoy.cpp:767)
                                  [not1] AVAP_SCAN_DONE_tp_odd  (GateBoy.cpp:768)
                                    [nor3] NYXU_BFETCH_RSTn  (GateBoy.cpp:1181)
                                      [nand3] MOCE_BFETCH_DONEn  (GateBoy.cpp:1195)
                                        [nand2] LEBO_ODD  (GateBoy.cpp:1185)
                                          [REGISTERED] LAXU_BFETCH_S0p_odd  (GateBoy.cpp:1188)
```

### Path 2: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `SIG_CPU_CLKREQ` (boundary, )
**Sink:** `SIG_CPU_BOWA_Axxxxxxx` (boundary, )
**Source file:** `GateBoy.cpp:685`

```
  [BOUNDARY] SIG_CPU_CLKREQ  (GateBoy.cpp:685)
    [not1] ABOL_CLKREQn  (GateBoyClocks.cpp:51)
      [nor3] BAPY_xxxxxxGH  (GateBoyClocks.cpp:58)
        [not1] BERU_ABCDEFxx  (GateBoyClocks.cpp:65)
          [not1] BUFA_xxxxxxGH  (GateBoyClocks.cpp:66)
            [not1] BOLO_ABCDEFxx  (GateBoyClocks.cpp:67)
              [nand4] BEJA_xxxxEFGH  (GateBoyClocks.cpp:72)
                [not1] BANE_ABCDxxxx  (GateBoyClocks.cpp:73)
                  [not1] BELO_xxxxEFGH  (GateBoyClocks.cpp:74)
                    [not1] BAZE_ABCDxxxx  (GateBoyClocks.cpp:75)
                      [nand3] BUTO_xBCDEFGH  (GateBoyClocks.cpp:76)
                        [not1] BELE_Axxxxxxx  (GateBoyClocks.cpp:77)
                          [or2] BYJU_Axxxxxxx  (GateBoyClocks.cpp:78)
                            [not1] BALY_xBCDEFGH  (GateBoyClocks.cpp:79)
                              [and2] BUVU_Axxxxxxx  (GateBoyClocks.cpp:81)
                                [not1] BYXO_xBCDEFGH  (GateBoyClocks.cpp:82)
                                  [not1] BEDO_Axxxxxxx  (GateBoyClocks.cpp:83)
                                    [not1] BOWA_xBCDEFGH  (GateBoyClocks.cpp:84)
                                      [BOUNDARY] SIG_CPU_BOWA_Axxxxxxx  (GateBoyClocks.cpp:88)
```

### Path 3: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `BESU_SCAN_DONEn_odd` (registered, nor_latch)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [nor2] ANOM_LINE_RSTn_odd_new  (GateBoy.cpp:754)
                              [not1] BALU_LINE_RSTp_odd_new  (GateBoy.cpp:755)
                                [or3] BEBU_SCAN_DONE_tn_odd_new  (GateBoy.cpp:767)
                                  [not1] AVAP_SCAN_DONE_tp_odd  (GateBoy.cpp:768)
                                    [or2] ASEN_SCAN_DONE_tp_odd_new  (GateBoy.cpp:770)
                                      [REGISTERED] BESU_SCAN_DONEn_odd  (GateBoy.cpp:771)
```

### Path 4: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `LOVY_TFETCH_DONEp` (registered, dff17)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [nor2] ANOM_LINE_RSTn_odd_new  (GateBoy.cpp:754)
                              [not1] BALU_LINE_RSTp_odd_new  (GateBoy.cpp:755)
                                [or3] BEBU_SCAN_DONE_tn_odd_new  (GateBoy.cpp:767)
                                  [not1] AVAP_SCAN_DONE_tp_odd  (GateBoy.cpp:768)
                                    [nor3] NYXU_BFETCH_RSTn  (GateBoy.cpp:1181)
                                      [REGISTERED] LOVY_TFETCH_DONEp  (GateBoy.cpp:1193)
```

### Path 5: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `LAXU_BFETCH_S0p_odd` (registered, dff17_any)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [nor2] ANOM_LINE_RSTn_odd_new  (GateBoy.cpp:754)
                              [not1] BALU_LINE_RSTp_odd_new  (GateBoy.cpp:755)
                                [or3] BEBU_SCAN_DONE_tn_odd_new  (GateBoy.cpp:767)
                                  [not1] AVAP_SCAN_DONE_tp_odd  (GateBoy.cpp:768)
                                    [nor3] NYXU_BFETCH_RSTn  (GateBoy.cpp:1181)
                                      [REGISTERED] LAXU_BFETCH_S0p_odd  (GateBoy.cpp:1188)
```

### Path 6: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `LONY_TFETCHINGp` (registered, nand_latch)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [nor2] ANOM_LINE_RSTn_odd_new  (GateBoy.cpp:754)
                              [not1] BALU_LINE_RSTp_odd_new  (GateBoy.cpp:755)
                                [or3] BEBU_SCAN_DONE_tn_odd_new  (GateBoy.cpp:767)
                                  [not1] AVAP_SCAN_DONE_tp_odd  (GateBoy.cpp:768)
                                    [nor3] NYXU_BFETCH_RSTn  (GateBoy.cpp:1181)
                                      [REGISTERED] LONY_TFETCHINGp  (GateBoy.cpp:1199)
```

### Path 7: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `XEPE_STORE0_X0p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] XEPE_STORE0_X0p  (GateBoySpriteStore.cpp:105)
```

### Path 8: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `YLAH_STORE0_X1p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] YLAH_STORE0_X1p  (GateBoySpriteStore.cpp:106)
```

### Path 9: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `ZOLA_STORE0_X2p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] ZOLA_STORE0_X2p  (GateBoySpriteStore.cpp:107)
```

### Path 10: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `ZULU_STORE0_X3p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] ZULU_STORE0_X3p  (GateBoySpriteStore.cpp:108)
```

### Path 11: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `WELO_STORE0_X4p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] WELO_STORE0_X4p  (GateBoySpriteStore.cpp:109)
```

### Path 12: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `XUNY_STORE0_X5p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] XUNY_STORE0_X5p  (GateBoySpriteStore.cpp:110)
```

### Path 13: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `WOTE_STORE0_X6p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] WOTE_STORE0_X6p  (GateBoySpriteStore.cpp:111)
```

### Path 14: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `XAKO_STORE0_X7p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] DYWE_STORE0_RSTp  (GateBoySpriteStore.cpp:72)
                                    [not1] DYNA_STORE0_RSTn  (GateBoySpriteStore.cpp:83)
                                      [REGISTERED] XAKO_STORE0_X7p  (GateBoySpriteStore.cpp:112)
```

### Path 15: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DANY_STORE1_X0p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] DANY_STORE1_X0p  (GateBoySpriteStore.cpp:114)
```

### Path 16: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DUKO_STORE1_X1p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] DUKO_STORE1_X1p  (GateBoySpriteStore.cpp:115)
```

### Path 17: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DESU_STORE1_X2p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] DESU_STORE1_X2p  (GateBoySpriteStore.cpp:116)
```

### Path 18: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DAZO_STORE1_X3p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] DAZO_STORE1_X3p  (GateBoySpriteStore.cpp:117)
```

### Path 19: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DAKE_STORE1_X4p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] DAKE_STORE1_X4p  (GateBoySpriteStore.cpp:118)
```

### Path 20: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `CESO_STORE1_X5p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] CESO_STORE1_X5p  (GateBoySpriteStore.cpp:119)
```

### Path 21: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DYFU_STORE1_X6p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] DYFU_STORE1_X6p  (GateBoySpriteStore.cpp:120)
```

### Path 22: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `CUSY_STORE1_X7p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] EFEV_STORE1_RSTp  (GateBoySpriteStore.cpp:73)
                                    [not1] DOKU_STORE1_RSTn  (GateBoySpriteStore.cpp:84)
                                      [REGISTERED] CUSY_STORE1_X7p  (GateBoySpriteStore.cpp:121)
```

### Path 23: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `FOKA_STORE2_X0p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] FOKA_STORE2_X0p  (GateBoySpriteStore.cpp:123)
```

### Path 24: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `FYTY_STORE2_X1p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] FYTY_STORE2_X1p  (GateBoySpriteStore.cpp:124)
```

### Path 25: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `FUBY_STORE2_X2p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] FUBY_STORE2_X2p  (GateBoySpriteStore.cpp:125)
```

### Path 26: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `GOXU_STORE2_X3p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] GOXU_STORE2_X3p  (GateBoySpriteStore.cpp:126)
```

### Path 27: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DUHY_STORE2_X4p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] DUHY_STORE2_X4p  (GateBoySpriteStore.cpp:127)
```

### Path 28: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `EJUF_STORE2_X5p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] EJUF_STORE2_X5p  (GateBoySpriteStore.cpp:128)
```

### Path 29: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `ENOR_STORE2_X6p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] ENOR_STORE2_X6p  (GateBoySpriteStore.cpp:129)
```

### Path 30: Depth 17 (85-255 ns, 214% of half T-cycle)
**Source:** `AFER_SYS_RSTp` (registered, dff13)
**Sink:** `DEPY_STORE2_X7p` (registered, dff9)
**Source file:** `GateBoyReset.cpp:34`

```
  [REGISTERED] AFER_SYS_RSTp  (GateBoyReset.cpp:34)
    [or2] AVOR_SYS_RSTp  (GateBoyState.cpp:14)
      [not1] ALUR_SYS_RSTn  (GateBoyState.cpp:14)
        [not1] DULA_SYS_RSTp  (GateBoyState.cpp:14)
          [not1] CUNU_SYS_RSTn  (GateBoyState.cpp:14)
            [not1] XORE_SYS_RSTp  (GateBoyState.cpp:14)
              [not1] XEBE_SYS_RSTn  (GateBoyState.cpp:14)
                [nand2] XODO_VID_RSTp  (GateBoyState.cpp:14)
                  [not1] XAPO_VID_RSTn_new  (GateBoyState.cpp:14)
                    [not1] ATAR_VID_RSTp_new  (GateBoyState.cpp:29)
                      [not1] ABEZ_VID_RSTn_new  (GateBoyState.cpp:32)
                        [or_and3] BYHA_LINE_RST_TRIGn_odd  (GateBoyLCD.cpp:121)
                          [not1] ATEJ_LINE_RST_TRIGp_odd  (GateBoyLCD.cpp:122)
                            [or2] ABAK_LINE_RSTp  (GateBoy.cpp:1035)
                              [not1] BYVA_LINE_RSTn  (GateBoy.cpp:1036)
                                [not1] DYBA_LINE_RSTp  (GateBoySpriteStore.cpp:71)
                                  [or2] FOKO_STORE2_RSTp  (GateBoySpriteStore.cpp:74)
                                    [not1] GAMY_STORE2_RSTn  (GateBoySpriteStore.cpp:85)
                                      [REGISTERED] DEPY_STORE2_X7p  (GateBoySpriteStore.cpp:130)
```
