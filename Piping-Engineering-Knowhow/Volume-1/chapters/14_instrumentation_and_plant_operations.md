# Chapter 14 — Instrumentation and plant operations

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0053"></a>

## PK-0053 — Instrument taps alter local performance

**Engineering mechanism.** Pressure taps, flowmeter straight-run requirements, impulse lines and sampling points all impose geometry and maintenance constraints.

**Decision procedure.** Use actual instrument vendor installation requirements for orientation and upstream/downstream layout.

**Verification / closeout.** Check calibration/inspection access, pressure rating, dead legs and sample safety.

**Failure mode or limitation.** Copying a generic flowmeter straight length across different technologies is unreliable.

**Reference anchors.** [AWWA](../reference/SOURCES.md#awwa).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0054"></a>

## PK-0054 — Filter vessels require pressure-drop allowance

**Engineering mechanism.** A filter has a clean and fouled differential-pressure envelope; backwash or cleaning changes flow paths.

**Decision procedure.** Use vendor curves for service and backwash states, then check pump operating range and relief/isolation design.

**Verification / closeout.** Validate high dP alarm/trip philosophy and maintainable valve sequence.

**Failure mode or limitation.** Sizing pipe using only clean filter data leads to low flow late in run.

**Reference anchors.** [HI-SYSTEM](../reference/SOURCES.md#hisystem).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0055"></a>

## PK-0055 — A bypass is not free extra functionality

**Engineering mechanism.** Bypasses can undermine control, permit contamination paths or create uncontrolled recirculation and unexpected valve states.

**Decision procedure.** Add a bypass only for documented operations, testing or maintenance cases with suitable isolation/control logic.

**Verification / closeout.** Review minimum flow, deadheading, backflow and cross-connection scenarios.

**Failure mode or limitation.** A bypass incorrectly left open can defeat treatment or protection.

**Reference anchors.** [EPA-VALVES](../reference/SOURCES.md#epavalves), [HI-SYSTEM](../reference/SOURCES.md#hisystem).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0056"></a>

## PK-0056 — Pressure relief is a system decision

**Engineering mechanism.** Pressure sources include pumps, thermal expansion of blocked-in liquid, gas regulation and external heat; a relief device requires a safe destination.

**Decision procedure.** Identify credible overpressure scenarios and hand off setpoint/capacity/discharge design to the responsible specialist.

**Verification / closeout.** Confirm protected boundaries, design pressures, bypasses, isolation and relief discharge acceptability.

**Failure mode or limitation.** A single relief valve near the pump may not protect every trapped segment.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
