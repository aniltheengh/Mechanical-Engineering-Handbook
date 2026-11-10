# Pump suction — NPSHA scenario and margin

**Question.** How is NPSHA screened for an open suction tank feeding a centrifugal pump?

**Inputs (illustrative only):** atmospheric head `10.33 m of pumped liquid`, level above pump datum `+1.50 m`, total suction friction/minor loss `0.60 m`, vapor-pressure head `0.32 m`. All heads use a consistent reference datum and density.

```text
NPSHA = H_atm + z_free_surface - H_suction_loss - H_vapor
      = 10.33 + 1.50 - 0.60 - 0.32
      = 10.91 m
```

At a lower liquid level of `−3.0 m` instead of `+1.50 m`, and otherwise unchanged, NPSHA would be `6.41 m`.

**Decision:** NPSHA must be compared at each relevant operating point with the actual pump NPSHR/NPSH3 curve and **required margin** appropriate to service. The mere arithmetic result is not a cavitation approval.

**Failure/limits:** warmer liquids increase vapor pressure; clogged suction screens increase losses; lower site atmospheric pressure reduces available head. For pressurized feed tanks the available pressure term changes. See [Hydraulic Institute pump principles](https://datatool.pumps.org/pump-fundamentals/pump-principles) and PK-0010.
