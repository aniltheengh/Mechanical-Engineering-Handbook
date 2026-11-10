# Chapter 02 — Fluid mechanics and sizing

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0005"></a>

## PK-0005 — Flow continuity and branch balance

**Engineering mechanism.** Mass is conserved; for steady incompressible flow at a junction, the sum of incoming volumetric flows equals outgoing flow if density stays nearly constant.

**Decision procedure.** Create a flow balance across pumps, treatment skids, bypasses and branches before pipe sizing.

**Verification / closeout.** Check min/normal/max operating cases, recirculation and simultaneous branches.

**Failure mode or limitation.** Using only nameplate peak flows can overestimate or underestimate actual concurrency.

**Reference anchors.** [HI-SYSTEM](../reference/SOURCES.md#hisystem).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0006"></a>

## PK-0006 — Select diameter from hydraulic and economic limits

**Engineering mechanism.** Smaller internal diameter increases velocity and usually friction loss; larger pipe costs more and has more fluid inventory.

**Decision procedure.** Compare candidate IDs using Darcy–Weisbach plus fittings, velocity, duty point, transients, erosion and total life-cycle cost.

**Verification / closeout.** Check actual pipe ID from chosen OD/schedule and material; sweep minimum and maximum flows.

**Failure mode or limitation.** A fixed 'standard velocity' is screening guidance, not a universal acceptance rule.

**Reference anchors.** [B36.10](../reference/SOURCES.md#b3610), [HI-SYSTEM](../reference/SOURCES.md#hisystem).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0007"></a>

## PK-0007 — Major and minor losses must both count

**Engineering mechanism.** Distributed wall friction and localized losses through elbows, tees, valves, reducers, meters and strainers both consume energy.

**Decision procedure.** Build a loss register with consistent Darcy friction factor and K or equivalent-length treatment; use vendor curves where available.

**Verification / closeout.** Trace each loss element to the P&ID and 3D isometric; check branch path losses independently.

**Failure mode or limitation.** Double-counting equivalent lengths and K factors or ignoring filter fouling produces poor pump sizing.

**Reference anchors.** [HI-SYSTEM](../reference/SOURCES.md#hisystem).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0008"></a>

## PK-0008 — Hydraulic grade line versus energy grade line

**Engineering mechanism.** The energy grade line includes velocity head; the hydraulic grade line excludes it, so diameter changes can change local pressure even without elevation changes.

**Decision procedure.** Sketch HGL/EGL from upstream reservoir to downstream outlet for representative flows.

**Verification / closeout.** Check pressure margins at peaks, valve throats, suction nozzles and high-loss devices.

**Failure mode or limitation.** A simple 'system pressure' label misses local vapor pressure and air pocket risks.

**Reference anchors.** [HI-SYSTEM](../reference/SOURCES.md#hisystem), [EPA-MAIN](../reference/SOURCES.md#epamain).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
