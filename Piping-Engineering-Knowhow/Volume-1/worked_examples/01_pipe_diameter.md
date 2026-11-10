# Pipe size screening — diameter, speed and straight-pipe loss

**Question.** For 50 m³/h of water through 50 m of pipe, how much does changing the internal diameter change velocity and straight-pipe loss?

**Inputs (illustrative):** `Q = 50 m³/h = 0.01388889 m³/s`, `L = 50 m`, `f_Darcy = 0.020` (assumed constant only for comparison), `g=9.80665 m/s²`; candidate internal diameters `D1=0.0779 m`, `D2=0.1023 m`. The nominal labels DN80/DN100 are *not* exact IDs.

**Equations**

```text
A = pi D² / 4
v = Q / A
h_f = f (L/D) [v²/(2g)]     (Darcy–Weisbach)
```

**Computed outputs** (reproduce using `python tools/piping_calc.py`):

| Internal D | Average velocity | Straight-pipe friction head |
|---:|---:|---:|
| 77.9 mm | 2.914 m/s | 5.560 m |
| 102.3 mm | 1.690 m/s | 1.423 m |

**Interpretation.** Under these assumptions, choosing the larger ID reduces this one loss component by around 74%. It does *not* alone prove a larger pipe is optimal.

**Required before project decision:** evaluate Reynolds number and roughness-dependent friction factor, actual ID/tolerance, valve and fitting loss coefficients, pressure allowance, capital cost, allowable velocity, transients, pump curve and design flow range. See PK-0006, PK-0007.
