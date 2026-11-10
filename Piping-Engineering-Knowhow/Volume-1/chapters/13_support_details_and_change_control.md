# Chapter 13 — Support details and change control

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0049"></a>

## PK-0049 — Support drawings need real structural context

**Engineering mechanism.** A pipe support detail must connect with steel/concrete designed for loads and movement, not only match the pipe OD.

**Decision procedure.** Include support tag, type, pipe location, elevation, restraint functions and structural interface.

**Verification / closeout.** Coordinate loads and permissible construction details with structural design.

**Failure mode or limitation.** A support modeled at a convenient point may obstruct equipment maintenance or conflict with building movement.

**Reference anchors.** [EXP](../reference/SOURCES.md#exp).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0050"></a>

## PK-0050 — 3D clash-checking must include operating states

**Engineering mechanism.** Cold and hot pipe positions, expansion, thermal lag, insulation, actuator travel and removable envelopes may differ from neutral CAD position.

**Decision procedure.** Clash-check cold/install, operating and maintenance envelopes for critical lines.

**Verification / closeout.** Record allowances and review deviations with piping stress, operations and maintenance.

**Failure mode or limitation.** Zero static collisions is not evidence of no future interference.

**Reference anchors.** [EXP](../reference/SOURCES.md#exp), [SWAGE](../reference/SOURCES.md#swage).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0051"></a>

## PK-0051 — Piping changes need a formal review chain

**Engineering mechanism.** Small routing edits can affect hydraulics, flexibility, supports, valve access, existing spools and documentation.

**Decision procedure.** Use documented change requests with discipline impact checks and traceable approval.

**Verification / closeout.** Update P&ID, line list, model, isometrics, stress/support records and BOM as applicable.

**Failure mode or limitation.** Undocumented late changes create mismatched as-builts and installation risk.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0052"></a>

## PK-0052 — Equipment isolation must be maintainable

**Engineering mechanism.** Isolation boundaries can retain trapped pressure/liquid and may require bypass, drain, vent or positive isolation depending on hazard.

**Decision procedure.** Review the operating and maintenance isolation philosophy with operations and safety staff.

**Verification / closeout.** Simulate isolation steps, depressurization, lockout and safe draining on P&ID.

**Failure mode or limitation.** One closed block valve may not be adequate for every hazardous maintenance activity.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
