# Chapter 05 — Valves and protection

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0017"></a>

## PK-0017 — Valve function determines valve type

**Engineering mechanism.** Isolation, throttling, nonreturn, pressure control and overpressure protection are distinct functions; some valves perform more than one poorly.

**Decision procedure.** Identify process function first, then select shutoff performance, differential pressure, actuation, fail state and maintenance needs.

**Verification / closeout.** Check valve datasheet, leakage class if relevant, required travel and operating modes.

**Failure mode or limitation.** A valve that fits the line size may be inappropriate for throttling, solids, or rapid closure.

**Reference anchors.** [AWWA](../reference/SOURCES.md#awwa), [EPA-VALVES](../reference/SOURCES.md#epavalves).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0018"></a>

## PK-0018 — Check-valve behavior must include transients

**Engineering mechanism.** A check valve's closure dynamics interact with flow reversal, moving water columns and pump shutdown.

**Decision procedure.** Evaluate non-slam behavior, line velocity, installed orientation and backflow consequence when selecting a check valve.

**Verification / closeout.** Review emergency power-failure and shutdown scenarios; use transient analysis when consequences justify it.

**Failure mode or limitation.** Installing any check valve does not automatically prevent water hammer.

**Reference anchors.** [EPA-SURGE](../reference/SOURCES.md#epasurge), [EPA-MAIN](../reference/SOURCES.md#epamain).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0019"></a>

## PK-0019 — Air-release and vacuum functions are different

**Engineering mechanism.** Small-orifice air release removes accumulated gas in service; air/vacuum features address large volumes while filling and draining.

**Decision procedure.** Review elevation profile, pressure regimes, sanitary protection, maintenance and sizing of air-management devices.

**Verification / closeout.** Check filling rates, negative-pressure risk, discharge arrangements and manufacturer curves.

**Failure mode or limitation.** A single small vent at the highest visible location may be inadequate for a long profile.

**Reference anchors.** [AWWA](../reference/SOURCES.md#awwa), [EPA-SURGE](../reference/SOURCES.md#epasurge), [EPA-MAIN](../reference/SOURCES.md#epamain).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0020"></a>

## PK-0020 — Strainer location and fouling allowance

**Engineering mechanism.** Strainers trap debris but cause pressure loss, which grows with contamination and can reduce pump suction margin.

**Decision procedure.** Locate and size strainers per equipment requirements; provide differential-pressure monitoring, isolation and cleaning access where required.

**Verification / closeout.** Verify clean/dirty pressure drop and maintainability, particularly on suction service.

**Failure mode or limitation.** Treating a clean strainer as zero-loss can invalidate NPSH assessment.

**Reference anchors.** [HI-FAQ](../reference/SOURCES.md#hifaq), [HI-NPSH](../reference/SOURCES.md#hinpsh).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
