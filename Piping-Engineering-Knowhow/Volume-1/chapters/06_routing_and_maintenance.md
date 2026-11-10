# Chapter 06 — Routing and maintenance

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0021"></a>

## PK-0021 — Routing must consider constructability

**Engineering mechanism.** The lowest centerline clash-free route can be impossible to weld, lift, support, drain or inspect.

**Decision procedure.** Review erection sequence, equipment movement, spool breaks, weld access, lifting paths and future removal envelopes.

**Verification / closeout.** Conduct model walk-through against maintenance and installation work packs.

**Failure mode or limitation.** CAD interference-free status is necessary in many projects but not sufficient for engineering release.

**Reference anchors.** [SWAGE](../reference/SOURCES.md#swage), [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0022"></a>

## PK-0022 — High points can trap gas

**Engineering mechanism.** Free gas collects at local peaks and reduces hydraulic capacity, causes meter errors, or creates unstable flow.

**Decision procedure.** Check elevation/profile and specify vents or air valves when required by system behavior.

**Verification / closeout.** Review start-up filling, operating flow, shutdown and siphon conditions.

**Failure mode or limitation.** Blindly avoiding all high points may conflict with civil constraints; deliberate venting can be the solution.

**Reference anchors.** [EPA-MAIN](../reference/SOURCES.md#epamain), [AWWA](../reference/SOURCES.md#awwa).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0023"></a>

## PK-0023 — Low points may retain liquid or solids

**Engineering mechanism.** Depressions can prevent complete drainage, support sediment deposition, freeze or create corrosion under deposits.

**Decision procedure.** Identify drainable low points and provide slopes/drain connections according to process cleanliness and maintenance plans.

**Verification / closeout.** Verify isolation-and-drain paths, drain destination capacity and safe disposal.

**Failure mode or limitation.** Adding a drain to a hazardous or pressurized line without discharge design introduces new risks.

**Reference anchors.** [EPA-MAIN](../reference/SOURCES.md#epamain), [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0024"></a>

## PK-0024 — Maintainable valves need a human envelope

**Engineering mechanism.** A handwheel, lever or actuator needs clearance for operation, removal and access from a safe platform.

**Decision procedure.** Model realistic actuator geometry, access reach and removable spool lengths.

**Verification / closeout.** Review in 3D with maintenance and operations stakeholders; check lifting or chainwheel access.

**Failure mode or limitation.** A valve can fit geometrically while being impossible to operate or repair.

**Reference anchors.** [SWAGE](../reference/SOURCES.md#swage).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
