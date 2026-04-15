# Operational Critical Paths by Functional Area


## Sprite Control (3 paths, max depth 39)

### Path 1: depth 39 (195-585 ns, 491% half T-cycle)
```
[REGISTERED:dffr] muwy  — LY bit 0
  [not_x1] ebos  — Sprite Y Compare
    [full_add] eruc  — Sprite Y Compare
      [full_add] enef  — Sprite Y Compare
        [full_add] feco  — Sprite Y Compare
          [full_add] gyky  — Sprite Y Compare
            [full_add] gopu  — Sprite Y Compare
              [full_add] fuwa  — Sprite Y Compare
                [full_add] goju  — Sprite Y Compare
                  [full_add] wuhu  — Sprite Y Compare
                    [not_x1] gewy  — Sprite Y Compare
                      [nand6] wota  — Sprite Y Compare
                        [not_x1] gese  — Sprite Y Compare
                          [and3] care  — Sprite Control
                            [not_x2] dyty  — Sprite Control x2 fan-out=11
                              [REGISTERED:dffr] dezy  — Sprite Control
```

### Path 2: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [and2] xyvo  — LCD
    [not_x1] ales  — Sprite Control
      [and2] abov  — Sprite Control
        [REGISTERED:dffr] catu  — Sprite Control
```

### Path 3: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] fony  — Sprite Control
  [and4] feto  — Sprite Control
    [REGISTERED:dffr] byba  — Sprite Control
```


## Bus (465 paths, max depth 32)

### Path 1: depth 32 (160-480 ns, 403% half T-cycle)
```
[REGISTERED:drlatch_ee] daty  — BG Scroll
  [half_add] atad  — BG Scroll
    [full_add] behu  — BG Scroll
      [full_add] apyh  — BG Scroll
        [full_add] babe  — BG Scroll
          [full_add] abod  — BG Scroll
            [full_add] bewy  — BG Scroll
              [full_add] byca  — BG Scroll
                [full_add] acul  — BG Scroll
                  [not_if0] ajan  — BG Scroll
                    [BUS:] bus:~ma4  — VRAM addr bus MA4
```

### Path 2: depth 32 (160-480 ns, 403% half T-cycle)
```
[REGISTERED:drlatch_ee] gave  — BG Scroll
  [half_add] fafo  — BG Scroll
    [full_add] emux  — BG Scroll
      [full_add] ecab  — BG Scroll
        [full_add] etam  — BG Scroll
          [full_add] doto  — BG Scroll
            [full_add] daba  — BG Scroll
              [full_add] efyk  — BG Scroll
                [full_add] ejok  — BG Scroll
                  [not_if0] dafe  — BG Scroll
                    [BUS:] bus:~ma9  — VRAM addr bus MA9
```

### Path 3: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] zaro  — Sprite Store
                                      [BUS:] bus:oam_render_a2  — Sprite render data bit 2 fan-out=11
```

### Path 4: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] zojy  — Sprite Store
                                      [BUS:] bus:oam_render_a3  — Sprite render data bit 3 fan-out=11
```

### Path 5: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] ynev  — Sprite Store
                                      [BUS:] bus:oam_render_a4  — Sprite render data bit 4 fan-out=11
```

### Path 6: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] xyra  — Sprite Store
                                      [BUS:] bus:oam_render_a5  — Sprite render data bit 5 fan-out=11
```

### Path 7: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] yrad  — Sprite Store
                                      [BUS:] bus:oam_render_a6  — Sprite render data bit 6 fan-out=11
```

### Path 8: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] yhal  — Sprite Store
                                      [BUS:] bus:oam_render_a7  — Sprite render data bit 7 fan-out=11
```

### Path 9: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] byme  — Sprite Store
                                      [BUS:] bus:sprite_y_store0  — Sprite Y store bit 0 fan-out=11
```

### Path 10: depth 29 (145-435 ns, 365% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [not_x2] fado  — Sprite X Priority x2 fan-out=10
                                    [not_if0] gate  — Sprite Store
                                      [BUS:] bus:sprite_y_store1  — Sprite Y store bit 1 fan-out=11
```


## Sprite X Priority (10 paths, max depth 27)

### Path 1: depth 27 (135-405 ns, 340% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [or2] gyga  — Sprite X Priority
                                [nor2] guze  — Sprite X Priority
                                  [REGISTERED:dffr] fono  — Sprite X Priority
```

### Path 2: depth 25 (125-375 ns, 315% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [or2] favo  — Sprite X Priority
                              [nor2] foxa  — Sprite X Priority
                                [REGISTERED:dffr] exuq  — Sprite X Priority
```

### Path 3: depth 23 (115-345 ns, 289% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [or2] wyla  — Sprite X Priority
                            [nor2] gutu  — Sprite X Priority
                              [REGISTERED:dffr] wapo  — Sprite X Priority
```

### Path 4: depth 21 (105-315 ns, 264% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [or2] weja  — Sprite X Priority
                          [nor2] xoja  — Sprite X Priority
                            [REGISTERED:dffr] womy  — Sprite X Priority
```

### Path 5: depth 19 (95-285 ns, 239% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [or2] xyla  — Sprite X Priority
                        [nor2] gega  — Sprite X Priority
                          [REGISTERED:dffr] wafy  — Sprite X Priority
```

### Path 6: depth 17 (85-255 ns, 214% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [or2] wuto  — Sprite X Priority
                      [nor2] gono  — Sprite X Priority
                        [REGISTERED:dffr] xudy  — Sprite X Priority
```

### Path 7: depth 15 (75-225 ns, 189% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [or2] gede  — Sprite X Priority
                    [nor2] gyfy  — Sprite X Priority
                      [REGISTERED:dffr] gota  — Sprite X Priority
```

### Path 8: depth 13 (65-195 ns, 164% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [or2] fuma  — Sprite X Priority
                  [nor2] emol  — Sprite X Priority
                    [REGISTERED:dffr] egav  — Sprite X Priority
```

### Path 9: depth 11 (55-165 ns, 138% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [not_x1] wefu  — Sprite X Priority
              [or2] geze  — Sprite X Priority
                [nor2] enut  — Sprite X Priority
                  [REGISTERED:dffr] cedy  — Sprite X Priority
```

### Path 10: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] ydug  — Sprite X Priority
            [nor2] guva  — Sprite X Priority
              [REGISTERED:dffr] eboj  — Sprite X Priority
```


## VRAM Interface (37 paths, max depth 26)

### Path 1: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] sefa  — VRAM
                                [not_x2] rege  — VRAM x2
                                  [PAD:pad_bidir_pu] md0  — VRAM
```

### Path 2: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] sogo  — VRAM
                                [not_x2] ryky  — VRAM x2
                                  [PAD:pad_bidir_pu] md1  — VRAM
```

### Path 3: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] sefu  — VRAM
                                [not_x2] razo  — VRAM x2
                                  [PAD:pad_bidir_pu] md2  — VRAM
```

### Path 4: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] suna  — VRAM
                                [not_x2] rada  — VRAM x2
                                  [PAD:pad_bidir_pu] md3  — VRAM
```

### Path 5: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] sumo  — VRAM
                                [not_x2] ryro  — VRAM x2
                                  [PAD:pad_bidir_pu] md4  — VRAM
```

### Path 6: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] sazu  — VRAM
                                [not_x2] revu  — VRAM x2
                                  [PAD:pad_bidir_pu] md5  — VRAM
```

### Path 7: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] samo  — VRAM
                                [not_x2] reku  — VRAM x2
                                  [PAD:pad_bidir_pu] md6  — VRAM
```

### Path 8: depth 26 (130-390 ns, 327% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [not_x1] rove  — VRAM
                              [and2] suke  — VRAM
                                [not_x2] ryze  — VRAM x2
                                  [PAD:pad_bidir_pu] md7  — VRAM
```

### Path 9: depth 25 (125-375 ns, 315% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [or2] synu  — VRAM
                              [not_x2] rura  — VRAM x2
                                [PAD:pad_bidir_pu] md0  — VRAM
```

### Path 10: depth 25 (125-375 ns, 315% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [nor2] tefa  — VRAM
          [and2] sose  — VRAM
            [and2] tuca  — VRAM
              [mux] tole  — VRAM
                [and2] sere  — VRAM
                  [and2] sazo  — VRAM
                    [not_x1] ryje  — VRAM
                      [not_x1] revo  — VRAM
                        [and2] rocy  — VRAM
                          [not_x3] rahu  — VRAM x3 fan-out=17
                            [or2] syma  — VRAM
                              [not_x2] ruly  — VRAM x2
                                [PAD:pad_bidir_pu] md1  — VRAM
```


## Test Mode (13 paths, max depth 23)

### Path 1: depth 23 (115-345 ns, 289% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x2] ajas  — PPU Control x2
            [not_x4] asot  — PPU Control x4 fan-out=14
              [nand3] bota  — OAM
                [and3] asyt  — OAM
                  [not_x1] bode  — OAM fan-out=17
                    [not_x1] yval  — OAM
                      [not_x1] yryv  — OAM
                        [not_x2] zodo  — OAM x2
                          [not_x1] wusu  — OAM
                            [or3] wazo  — OAM
                              [nand2] wujy  — OAM
                                [not_x3] wahe  — OAM x3
                                  [nand2] wycy  — OAM
                                    [not_x2] wory  — OAM x2
                                      [not_x2] wame  — OAM x2
                                        [BOUNDARY:oam] oam_a
```

### Path 2: depth 23 (115-345 ns, 289% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x2] ajas  — PPU Control x2
            [not_x4] asot  — PPU Control x4 fan-out=14
              [nand3] bota  — OAM
                [and3] asyt  — OAM
                  [not_x1] bode  — OAM fan-out=17
                    [not_x1] yval  — OAM
                      [not_x1] yryv  — OAM
                        [not_x2] zodo  — OAM x2
                          [not_x1] wusu  — OAM
                            [or3] wazo  — OAM
                              [nand2] wujy  — OAM
                                [not_x3] wahe  — OAM x3
                                  [nand2] wycy  — OAM
                                    [not_x2] wory  — OAM x2
                                      [not_x2] wame  — OAM x2
                                        [BOUNDARY:oam] oam_b
```

### Path 3: depth 22 (110-330 ns, 277% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x2] ajas  — PPU Control x2
            [not_x4] asot  — PPU Control x4 fan-out=14
              [nand3] bota  — OAM
                [and3] asyt  — OAM
                  [not_x1] bode  — OAM fan-out=17
                    [not_x1] yval  — OAM
                      [not_x1] yryv  — OAM
                        [not_x2] zodo  — OAM x2
                          [not_x1] wusu  — OAM
                            [or3] wazo  — OAM
                              [nand2] wujy  — OAM
                                [not_x3] wahe  — OAM x3
                                  [nand2] wega  — OAM
                                    [not_x2] wejy  — OAM x2
                                      [BOUNDARY:oam] oam_a
```

### Path 4: depth 22 (110-330 ns, 277% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x2] ajas  — PPU Control x2
            [not_x4] asot  — PPU Control x4 fan-out=14
              [nand3] bota  — OAM
                [and3] asyt  — OAM
                  [not_x1] bode  — OAM fan-out=17
                    [not_x1] yval  — OAM
                      [not_x1] yryv  — OAM
                        [not_x2] zodo  — OAM x2
                          [not_x1] wusu  — OAM
                            [or3] wazo  — OAM
                              [nand2] wujy  — OAM
                                [not_x3] wahe  — OAM x3
                                  [nand2] wema  — OAM
                                    [not_x2] wexa  — OAM x2
                                      [BOUNDARY:oam] oam_b
```

### Path 5: depth 20 (100-300 ns, 252% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x2] ajas  — PPU Control x2
            [not_x4] asot  — PPU Control x4 fan-out=14
              [nand3] bota  — OAM
                [and3] asyt  — OAM
                  [not_x1] bode  — OAM fan-out=17
                    [not_x1] yval  — OAM
                      [not_x1] yryv  — OAM
                        [not_x2] zodo  — OAM x2
                          [not_x1] wusu  — OAM
                            [or3] wazo  — OAM
                              [nand2] wujy  — OAM
                                [not_x3] wahe  — OAM x3
                                  [BOUNDARY:oam] oam_a
```

### Path 6: depth 20 (100-300 ns, 252% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [not_x2] ajas  — PPU Control x2
            [not_x4] asot  — PPU Control x4 fan-out=14
              [nand3] bota  — OAM
                [and3] asyt  — OAM
                  [not_x1] bode  — OAM fan-out=17
                    [not_x1] yval  — OAM
                      [not_x1] yryv  — OAM
                        [not_x2] zodo  — OAM x2
                          [not_x1] wusu  — OAM
                            [or3] wazo  — OAM
                              [nand2] wujy  — OAM
                                [not_x3] wahe  — OAM x3
                                  [BOUNDARY:oam] oam_b
```

### Path 7: depth 11 (55-165 ns, 138% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [and3] yula
            [nand2] zado
              [not_x1] zery
                [not_x1] zoku
                  [BOUNDARY:boot_rom] boot_rom
```

### Path 8: depth 10 (50-150 ns, 126% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [and3] yula
            [nand2] zado
              [not_x1] zery
                [BOUNDARY:boot_rom] boot_rom
```

### Path 9: depth 9 (45-135 ns, 113% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [nand2] abuf
            [not_x2] apow x2
              [not_x1] anyk
                [BOUNDARY:high_ram] high_ram
```

### Path 10: depth 8 (40-120 ns, 101% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [muxi] ujyv
        [not_x3] tedo x3 fan-out=14
          [nand2] abuf
            [not_x2] apow x2
              [BOUNDARY:high_ram] high_ram
```


## Data Bus (16 paths, max depth 16)

### Path 1: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] ruxa
                      [PAD:pad_bidir_pu] d0
```

### Path 2: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] ruja
                      [PAD:pad_bidir_pu] d1
```

### Path 3: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] raby
                      [PAD:pad_bidir_pu] d2
```

### Path 4: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] rera
                      [PAD:pad_bidir_pu] d3
```

### Path 5: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] rory
                      [PAD:pad_bidir_pu] d4
```

### Path 6: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] ryvo
                      [PAD:pad_bidir_pu] d5
```

### Path 7: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] rafy
                      [PAD:pad_bidir_pu] d6
```

### Path 8: depth 16 (80-240 ns, 201% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [nand2] ravu
                      [PAD:pad_bidir_pu] d7
```

### Path 9: depth 15 (75-225 ns, 189% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [PAD:pad_bidir_pu] d0
```

### Path 10: depth 15 (75-225 ns, 189% half T-cycle)
```
[BUS:] bus:a15  — CPU addr bus A15
  [not_x1] sore
    [or3] tevy
      [and2] texo
        [not_x1] levo
          [ao21] lagu
            [not_x1] lywe
              [or2] moty
                [mux] roru fan-out=10
                  [not_x1] lula fan-out=16
                    [PAD:pad_bidir_pu] d1
```


## LCD Output (10 paths, max depth 14)

### Path 1: depth 14 (70-210 ns, 176% half T-cycle)
```
[REGISTERED:dffsr] pybo  — BG FIFO
  [and2] rajy  — Pixel Mux
    [and2] ryfu  — Pixel Mux
      [nor3] poka  — Pixel Mux
        [nand2] leka  — Pixel Mux
          [not_x1] luku  — Pixel Mux
            [and3] lyky  — Pixel Mux
              [ao2222] mufa  — Pixel Mux
                [or3] pero  — Pixel Mux
                  [not_x2] remy  — Pixel Mux x2
                    [PAD:pad_out] ld0  — LCD
```

### Path 2: depth 14 (70-210 ns, 176% half T-cycle)
```
[REGISTERED:dffsr] pybo  — BG FIFO
  [and2] rajy  — Pixel Mux
    [and2] ryfu  — Pixel Mux
      [nor3] poka  — Pixel Mux
        [nand2] leka  — Pixel Mux
          [not_x1] luku  — Pixel Mux
            [and3] lyky  — Pixel Mux
              [ao2222] moka  — Pixel Mux
                [or3] paty  — Pixel Mux
                  [not_x2] ravo  — Pixel Mux x2
                    [PAD:pad_out] ld1  — LCD
```

### Path 3: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:dffr] luca  — LCD
  [xor] magu  — LCD
    [not_x3] meco  — LCD x3
      [not_x1] kebo  — LCD
        [ao22] kupa  — LCD
          [not_x3] kofo  — LCD x3
            [PAD:pad_out] fr  — LCD
```

### Path 4: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] rutu  — LCD
  [or2] ryno  — LCD
    [not_x2] pogu  — LCD x2
      [PAD:pad_out] cpg  — LCD
```

### Path 5: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] taha  — LCD
  [not_x1] tafy  — LCD
    [nand7] tebo  — LCD
      [nand4] tegy  — LCD
        [REGISTERED:dffr] sygu  — LCD
```

### Path 6: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [and4] noko  — LCD
    [REGISTERED:dffr] myta  — LCD
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [and2] xyvo  — LCD
    [REGISTERED:dffr] popu  — LCD
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] saxo  — LCD
  [and4] sanu  — LCD
    [REGISTERED:dffr] rutu  — LCD
```

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] lafo  — LY bit 7
  [nor8] neru  — LCD
    [REGISTERED:dffr] meda  — LCD
```

### Path 10: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] meda  — LCD
  [not_x3] mure  — LCD x3
    [PAD:pad_out] s  — LCD
```


## STAT/LY (8 paths, max depth 13)

### Path 1: depth 13 (65-195 ns, 164% half T-cycle)
```
[REGISTERED:dffr] ceno  — Scan Active
  [not_x2] ceha  — Sprite Control x2
    [not_x1] byjo  — Sprite Control
      [and2] azem  — Sprite Control
        [and2] aror  — Sprite X Priority fan-out=10
          [nand3] dego  — Sprite X Priority
            [nand5] fefy  — Sprite X Priority
              [or2] fepo  — Sprite X Priority
                [not_x1] xena  — STAT/LY
                  [and2] wodu  — STAT/LY
                    [REGISTERED:dffr] voga  — STAT/LY
```

### Path 2: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] tuhu  — STAT/LY
  [and2] tyba  — STAT/LY
    [and2] sury  — STAT/LY
      [xor] roku  — STAT/LY
        [REGISTERED:dffr] sybe  — STAT/LY
```

### Path 3: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] savy  — Pixel X bit 1
  [and2] xuke  — STAT/LY
    [and2] xyle  — STAT/LY
      [xor] xora  — STAT/LY
        [REGISTERED:dffr] xydo  — Pixel X bit 3
```

### Path 4: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr] lydo  — LY bit 3
  [xor] rasy  — STAT/LY
    [nor4] subo  — STAT/LY
      [nand2] rape  — STAT/LY
        [not_x1] paly  — STAT/LY
          [REGISTERED:dffr] ropo  — STAT/LY
```

### Path 5: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] tuhu  — STAT/LY
  [and2] tyba  — STAT/LY
    [xor] tyge  — STAT/LY
      [REGISTERED:dffr] tako  — STAT/LY
```

### Path 6: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] savy  — Pixel X bit 1
  [and2] xuke  — STAT/LY
    [xor] xegy  — STAT/LY
      [REGISTERED:dffr] xodu  — Pixel X bit 2
```

### Path 7: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] savy  — Pixel X bit 1
  [xor] rybo  — STAT/LY
    [REGISTERED:dffr] savy  — Pixel X bit 1
```

### Path 8: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] tuhu  — STAT/LY
  [xor] sake  — STAT/LY
    [REGISTERED:dffr] tuky  — STAT/LY
```


## Address Bus (15 paths, max depth 9)

### Path 1: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] amet
              [nor2] koty
                [PAD:pad_bidir] a0
```

### Path 2: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] atol
              [nand2] caba
                [PAD:pad_bidir] a1
```

### Path 3: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] pamy
              [nor2] rore
                [PAD:pad_bidir] a10
```

### Path 4: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] male
              [nand2] lepy
                [PAD:pad_bidir] a11
```

### Path 5: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] mojy
              [nor2] loso
                [PAD:pad_bidir] a12
```

### Path 6: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] muce
              [nand2] labe
                [PAD:pad_bidir] a13
```

### Path 7: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] pege
              [nor2] pahy
                [PAD:pad_bidir] a14
```

### Path 8: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] apok
              [nor2] bajo
                [PAD:pad_bidir] a2
```

### Path 9: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] amer
              [nor2] bola
                [PAD:pad_bidir] a3
```

### Path 10: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dlatch_ee] maru  — DMA
  [not_x1] lebu  — DMA
    [nor3] muda  — DMA
      [not_x1] logo  — DMA
        [nand2] mory  — DMA
          [not_x1] luma  — DMA fan-out=20
            [mux] atem
              [nor2] bevo
                [PAD:pad_bidir] a4
```


## Sprite Pixel Shifter (16 paths, max depth 9)

### Path 1: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pono  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] mofo  — Sprite FIFO
```

### Path 2: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pono  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] mytu  — Sprite FIFO
```

### Path 3: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pelo  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] peba  — Sprite FIFO
```

### Path 4: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pute  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] pefo  — Sprite FIFO
```

### Path 5: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pobe  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] pudu  — Sprite FIFO
```

### Path 6: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pawe  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] rama  — Sprite FIFO
```

### Path 7: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pobe  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] ramu  — Sprite FIFO
```

### Path 8: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pute  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] rewo  — Sprite FIFO
```

### Path 9: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] pelo  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] roka  — Sprite FIFO
```

### Path 10: depth 9 (45-135 ns, 113% half T-cycle)
```
[REGISTERED:dffr] tuly  — Sprite Y Compare
  [nor2] saky  — Sprite Y Compare
    [or2] tyso  — Sprite Y Compare
      [not_x2] texy  — Sprite Fetching x2
        [and2] xono  — Sprite FIFO
          [mux] puly  — Sprite FIFO
            [REGISTERED:dlatch_ee_q] rydu  — Sprite FIFO
```


## BG/Win Cycles (3 paths, max depth 8)

### Path 1: depth 8 (40-120 ns, 101% half T-cycle)
```
[REGISTERED:drlatch_ee] mypu  — Window
  [xnor] nezo  — Window
    [nand5] puky  — Window
      [not_x1] nufa  — Window
        [nand5] nogy  — Window
          [not_x1] nuko  — Window
            [nor2] pany  — BG/Win Cycles
              [REGISTERED:dffr] ryfa  — Window Y Match
```

### Path 2: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:drlatch_ee] mypu  — Window
  [xnor] nezo  — Window
    [nand5] puky  — Window
      [not_x1] nufa  — Window
        [nand5] nogy  — Window
          [not_x1] nuko  — Window
            [REGISTERED:dffr] pyco  — BG/Win Cycles
```

### Path 3: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:drlatch_ee] cyxu  — BG Scroll
  [xnor] sozu  — BG/Win Cycles
    [nand4] rone  — BG/Win Cycles
      [not_x1] pohu  — BG/Win Cycles
        [REGISTERED:dffr] puxa  — BG/Win Cycles
```


## Window Logic (1 paths, max depth 7)

### Path 1: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] lovu  — LY bit 4
  [xnor] nojo  — Window
    [nand5] palo  — Window
      [not_x1] nele  — Window
        [nand5] pafu  — Window
          [not_x1] roge  — Window
            [REGISTERED:dffr] sary  — Window
```


## APU CH3 (Wave) (16 paths, max depth 7)

### Path 1: depth 7 (35-105 ns, 88% half T-cycle)
```
[REGISTERED:dffr] davo  — CH3
  [not_x2] coka  — CH3 x2 fan-out=13
    [mux] agyl  — CH3
      [not_x1] ynys  — CH3
        [and2] yfux  — CH3
          [BOUNDARY:wave_ram] wave_ram fan-out=16
```

### Path 2: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr] davo  — CH3
  [not_x2] coka  — CH3 x2 fan-out=13
    [mux] agyl  — CH3
      [and2] yjej  — CH3
        [BOUNDARY:wave_ram] wave_ram fan-out=16
```

### Path 3: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] davo  — CH3
  [not_x2] coka  — CH3 x2 fan-out=13
    [mux] axol  — CH3
      [not_x1] ynur  — CH3
        [BOUNDARY:wave_ram] wave_ram fan-out=16
```

### Path 4: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] huno  — CH3
  [not_x1] hema  — CH3
    [not_x1] gase  — CH3
      [nor2] hera  — CH3
        [not_x1] jera  — CH3
          [REGISTERED:tffnl] japu  — CH3
```

### Path 5: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] huno  — CH3
  [not_x1] hema  — CH3
    [not_x1] gase  — CH3
      [nor2] hera  — CH3
        [not_x1] kaso  — CH3
          [REGISTERED:tffnl] kafo  — CH3
```

### Path 6: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] huno  — CH3
  [not_x1] hema  — CH3
    [not_x1] gase  — CH3
      [nor2] hera  — CH3
        [not_x1] jera  — CH3
          [REGISTERED:tffnl] keju  — CH3
```

### Path 7: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] huno  — CH3
  [not_x1] hema  — CH3
    [not_x1] gase  — CH3
      [nor2] hera  — CH3
        [not_x1] kyko  — CH3
          [REGISTERED:tffnl] kemu  — CH3
```

### Path 8: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] huno  — CH3
  [not_x1] hema  — CH3
    [not_x1] gase  — CH3
      [nor2] hera  — CH3
        [not_x1] kaso  — CH3
          [REGISTERED:tffnl] keno  — CH3
```

### Path 9: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] huno  — CH3
  [not_x1] hema  — CH3
    [not_x1] gase  — CH3
      [nor2] hera  — CH3
        [not_x1] kaso  — CH3
          [REGISTERED:tffnl] kepa  — CH3
```

### Path 10: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] huno  — CH3
  [not_x1] hema  — CH3
    [not_x1] gase  — CH3
      [nor2] hera  — CH3
        [not_x1] jera  — CH3
          [REGISTERED:tffnl] keza  — CH3
```


## APU CH2 (Square) (17 paths, max depth 6)

### Path 1: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr_cc] cagy  — CH2
  [and2] dymu  — CH2
    [and2] egog  — CH2
      [ao2222] exes  — CH2
        [REGISTERED:dffr] dome  — CH2
```

### Path 2: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] cyvo  — CH2
```

### Path 3: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] done  — CH2
```

### Path 4: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] dynu  — CH2
```

### Path 5: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] cogu  — CH2
          [REGISTERED:tffnl] ezof  — CH2
```

### Path 6: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] erog  — CH2
          [REGISTERED:tffnl] fuxo  — CH2
```

### Path 7: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] erog  — CH2
          [REGISTERED:tffnl] gane  — CH2
```

### Path 8: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] erog  — CH2
          [REGISTERED:tffnl] gano  — CH2
```

### Path 9: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] gyko  — CH2
  [not_x1] etuk  — CH2
    [not_x1] davu  — CH2
      [nor2] duju  — CH2
        [not_x1] erog  — CH2
          [REGISTERED:tffnl] goca  — CH2
```

### Path 10: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:tffnl] fena  — CH2
  [nand5] erat  — CH2
    [not_x1] fyre  — CH2
      [or2] gufy  — CH2
        [REGISTERED:dffr] hepo  — CH2
```


## APU CH1 (Square+Sweep) (36 paths, max depth 6)

### Path 1: depth 6 (30-90 ns, 76% half T-cycle)
```
[REGISTERED:dffr_cc] dape  — CH1
  [and2] ezoz  — CH1
    [and2] enek  — CH1
      [ao2222] duna  — CH1
        [REGISTERED:dffr] duwo  — CH1
```

### Path 2: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dako  — CH1
          [REGISTERED:tffnl] copu  — CH1
```

### Path 3: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:drlatch_ee] avaf  — CH1
  [not_x3] aryl  — CH1 x3 fan-out=14
    [xor] cale  — CH1
      [REGISTERED:dffr_cc_q] defa  — CH1
```

### Path 4: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:drlatch_ee] avaf  — CH1
  [not_x3] aryl  — CH1 x3 fan-out=14
    [xor] culu  — CH1
      [REGISTERED:dffr_cc_q] deva  — CH1
```

### Path 5: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:drlatch_ee] avaf  — CH1
  [not_x3] aryl  — CH1 x3 fan-out=14
    [xor] dyme  — CH1
      [REGISTERED:dffr_cc_q] edok  — CH1
```

### Path 6: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dega  — CH1
          [REGISTERED:tffnl] ekov  — CH1
```

### Path 7: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dako  — CH1
          [REGISTERED:tffnl] emus  — CH1
```

### Path 8: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:drlatch_ee] avaf  — CH1
  [not_x3] aryl  — CH1 x3 fan-out=14
    [xor] fure  — CH1
      [REGISTERED:dffr_cc_q] epyr  — CH1
```

### Path 9: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:drlatch_ee] avaf  — CH1
  [not_x3] aryl  — CH1 x3 fan-out=14
    [xor] dozy  — CH1
      [REGISTERED:dffr_cc_q] eter  — CH1
```

### Path 10: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:dffr] comy  — CH1
  [not_x1] cyte  — CH1
    [not_x1] cope  — CH1
      [nor2] epyk  — CH1
        [not_x1] dako  — CH1
          [REGISTERED:tffnl] evak  — CH1
```


## APU Control (1 paths, max depth 5)

### Path 1: depth 5 (25-75 ns, 63% half T-cycle)
```
[PAD:pad_in] t1
  [not_x1] ubet
    [and2] unor  — Test Mode Gate fan-out=34
      [and2] efop  — APU Control
        [REGISTERED:drlatch_ee] fero  — APU Control
```


## Serial (5 paths, max depth 5)

### Path 1: depth 5 (25-75 ns, 63% half T-cycle)
```
[REGISTERED:dffr] coty
  [muxi] cave
    [or2] dawa
      [nand2] kexu
        [PAD:pad_bidir_pu_latch] sck
```

### Path 2: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] jeva
    [nor2] kywe
      [PAD:pad_bidir_pu] sin
```

### Path 3: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro
  [muxi] kena
    [PAD:pad_out] sout
```

### Path 4: depth 1 (5-15 ns, 13% half T-cycle)
```
[PAD:pad_bidir_pu] sin
  [not_x1] cage
    [REGISTERED:dffsr] cuba
```

### Path 5: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] buro
  [nand2] kore
    [PAD:pad_bidir_pu] sin
```


## APU CH4 (Noise) (11 paths, max depth 4)

### Path 1: depth 4 (20-60 ns, 50% half T-cycle)
```
[REGISTERED:tffnl] faty  — CH4
  [nand5] cuty  — CH4
    [not_x1] dubo  — CH4
      [or2] evur  — CH4
        [REGISTERED:dffr] fyno  — CH4
```

### Path 2: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] hezu  — CH4
  [xnor] hura  — CH4
    [REGISTERED:dffr] joto  — CH4
```

### Path 3: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] fosy  — CH4
  [nor2] enec  — CH4
    [not_x1] dapy  — CH4
      [REGISTERED:tffnl] cofe  — CH4
```

### Path 4: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] fosy  — CH4
  [nor2] enec  — CH4
    [not_x1] dapy  — CH4
      [REGISTERED:tffnl] cuna  — CH4
```

### Path 5: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] fosy  — CH4
  [nor2] enec  — CH4
    [not_x1] dapy  — CH4
      [REGISTERED:tffnl] dogo  — CH4
```

### Path 6: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:tffnl] cofe  — CH4
  [and3] ejex  — CH4
    [REGISTERED:dffr] fosy  — CH4
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:tffnl] jyco  — CH4
  [and3] hyno  — CH4
    [REGISTERED:dffr] gary  — CH4
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:drlatch_ee] jamy  — CH4
  [ao22] kavu  — CH4
    [REGISTERED:dffr] jepe  — CH4
```

### Path 9: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] gary  — CH4
  [nor2] gofu  — CH4
    [not_x1] huce  — CH4
      [REGISTERED:tffnl] jyco  — CH4
```

### Path 10: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] gary  — CH4
  [nor2] gofu  — CH4
    [not_x1] huce  — CH4
      [REGISTERED:tffnl] jyfu  — CH4
```


## Boot ROM (2 paths, max depth 3)

### Path 1: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] tepu
  [not_x1] tera
    [and2] tutu
      [BOUNDARY:sm83] cpu fan-out=42
```

### Path 2: depth 2 (10-30 ns, 25% half T-cycle)
```
[BUS:] bus:d0  — CPU data bus D0 fan-out=46
  [or2] sato
    [REGISTERED:dffr] tepu
```


## Joypad (12 paths, max depth 3)

### Path 1: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [or2] karu
      [PAD:pad_out_diff] p14
```

### Path 2: depth 3 (15-45 ns, 38% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [or2] cela
      [PAD:pad_out_diff] p15
```

### Path 3: depth 2 (10-30 ns, 25% half T-cycle)
```
[PAD:pad_bidir_pu] p10
  [or4] kery
    [REGISTERED:dlatch] awob
```

### Path 4: depth 2 (10-30 ns, 25% half T-cycle)
```
[PAD:pad_bidir_pu] p10
  [or4] kery
    [REGISTERED:dffr] batu
```

### Path 5: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kybu
      [PAD:pad_bidir_pu] p10
```

### Path 6: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kabu
      [PAD:pad_bidir_pu] p11
```

### Path 7: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kasy
      [PAD:pad_bidir_pu] p12
```

### Path 8: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] buro
  [not_x1] kura
    [nor2] kale
      [PAD:pad_bidir_pu] p13
```

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] buro
  [nand2] kole
    [PAD:pad_bidir_pu] p10
```

### Path 10: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dffr] buro
  [nand2] kyto
    [PAD:pad_bidir_pu] p11
```


## OAM Interface (7 paths, max depth 2)

### Path 1: depth 2 (10-30 ns, 25% half T-cycle)
```
[BUS:] bus:clk_t4  — Clock bus (clk_t4)
  [not_x1] decy  — OAM
    [not_x1] caty  — OAM
      [REGISTERED:dffr] maka  — OAM
```

### Path 2: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a2}_tri
  [not_x1] yfot  — OAM
    [REGISTERED:dffr_cc] xadu  — OAM
```

### Path 3: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a7}_tri
  [not_x1] yzet  — OAM
    [REGISTERED:dffr_cc] xecu  — OAM
```

### Path 4: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a3}_tri
  [not_x1] yfoc  — OAM
    [REGISTERED:dffr_cc] xedy  — OAM
```

### Path 5: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a5}_tri
  [not_x1] ymev  — OAM
    [REGISTERED:dffr_cc] xobe  — OAM
```

### Path 6: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a6}_tri
  [not_x1] xemu  — OAM
    [REGISTERED:dffr_cc] yduf  — OAM
```

### Path 7: depth 1 (5-15 ns, 13% half T-cycle)
```
[BUS:] bus:oam_~{a4}_tri
  [not_x1] yvom  — OAM
    [REGISTERED:dffr_cc] zuze  — OAM
```


## DMA (1 paths, max depth 2)

### Path 1: depth 2 (10-30 ns, 25% half T-cycle)
```
[REGISTERED:dffr] mugu  — DMA
  [nand6] navo  — DMA
    [not_x1] nolo  — DMA
      [REGISTERED:dffr] myte  — DMA
```


## Sprite X Match (80 paths, max depth 1)

### Path 1: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] baxo  — Sprite X Match
  [not_x1] arop  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] ceso  — Sprite X Match
```

### Path 2: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] depo  — Sprite X Match fan-out=17
  [not_x1] bady  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] cusy  — Sprite X Match
```

### Path 3: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] depo  — Sprite X Match fan-out=17
  [not_x1] bady  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] cuvy  — Sprite X Match
```

### Path 4: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo  — Sprite X Match fan-out=17
  [not_x1] cose  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] cywe  — Sprite X Match
```

### Path 5: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo  — Sprite X Match fan-out=17
  [not_x1] cose  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] dake  — Sprite X Match
```

### Path 6: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] ylor  — Sprite X Match
  [not_x1] zago  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] dany  — Sprite X Match
```

### Path 7: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] zezy  — Sprite X Match
  [not_x1] yvok  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] dazo  — Sprite X Match
```

### Path 8: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] depo  — Sprite X Match fan-out=17
  [not_x1] bady  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] depy  — Sprite X Match
```

### Path 9: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] zyve  — Sprite X Match
  [not_x1] ypur  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] desu  — Sprite X Match
```

### Path 10: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:dlatch_ee] gomo  — Sprite X Match fan-out=17
  [not_x1] cose  — Sprite X Match fan-out=10
    [REGISTERED:drlatch_ee] duhy  — Sprite X Match
```


## Other (1 paths, max depth 1)

### Path 1: depth 1 (5-15 ns, 13% half T-cycle)
```
[BOUNDARY:sm83] cpu fan-out=42
  [not_x1] lexy
    [PAD:pad_out] m1
```


## Timer (1 paths, max depth 1)

### Path 1: depth 1 (5-15 ns, 13% half T-cycle)
```
[REGISTERED:tffnl] nuga  — Timer
  [nor2] mery  — Timer
    [REGISTERED:dffr] moba  — Timer
```
