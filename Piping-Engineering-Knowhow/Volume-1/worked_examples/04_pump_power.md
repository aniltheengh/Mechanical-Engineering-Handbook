# Pump and system head — screening of shaft power

**Question.** At 50 m³/h, what pump shaft power would be implied by an estimated 24.2 m total differential head?

**Inputs (illustrative):** elevation/static head `12.0 m`; piping friction `5.0 m`; fitting/valve loss `1.2 m`; filter loss `6.0 m` (all measured at that one flow); water density `1000 kg/m³`; pump hydraulic efficiency `65%` assumed **for illustration**.

```text
Total differential head = 12 + 5 + 1.2 + 6 = 24.2 m
P_hydraulic = rho g Q H = 1000×9.80665×(50/3600)×24.2
P_shaft = P_hydraulic / 0.65
```

**Outputs:** Hydraulic power `3.296 kW`; calculated shaft power `5.071 kW` (rounded). This does **not** specify a motor size.

**Before selection:** obtain actual Q-H, efficiency and NPSHR curves; assess fouled filters, shutoff, runout, min-flow, largest absorbed power, variable speed, motor/drive efficiency, service factor and specified operating region. See [HI combined curves](https://datatool.pumps.org/pump-fundamentals/combined.html) and PK-0009, PK-0012.
