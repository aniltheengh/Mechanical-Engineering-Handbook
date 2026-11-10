# Chapter 09 — Structural and dynamic response

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0033"></a>

## PK-0033 — Anchors transmit loads to structures

**Engineering mechanism.** A theoretical anchor is only valid if supporting steel and concrete can resist the resulting forces and moments.

**Decision procedure.** Coordinate anchor reactions, load combinations, baseplate/foundation design and thermal load path with structural engineering.

**Verification / closeout.** Check structural calculation, bolts, welds and differential settlement.

**Failure mode or limitation.** A 'fixed support' in simulation can be inaccurate if the real support frame is flexible.

**Reference anchors.** [EXP](../reference/SOURCES.md#exp).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0034"></a>

## PK-0034 — Water hammer is a dynamic phenomenon

**Engineering mechanism.** Rapid velocity changes generate pressure waves; the Joukowsky approximation is DeltaP=rho*a*DeltaV for a rapid idealized event.

**Decision procedure.** Screen pump-trip, fast-closure and column-separation scenarios; perform a transient analysis when the risk is material.

**Verification / closeout.** Check both maximum positive and minimum absolute pressure along the full profile.

**Failure mode or limitation.** Steady-state pressure-loss calculations cannot predict transient peaks and vacuum.

**Reference anchors.** [EPA-SURGE](../reference/SOURCES.md#epasurge), [EPA-MAIN](../reference/SOURCES.md#epamain).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0035"></a>

## PK-0035 — Vibration requires source diagnosis

**Engineering mechanism.** Pulsation, turbulence, cavitation, rotating equipment and support resonance can all produce pipe motion.

**Decision procedure.** Determine excitation frequencies and dynamic behavior before adding random stiffeners or supports.

**Verification / closeout.** Measure frequency/response when available; assess fatigue at branch connections and instrument taps.

**Failure mode or limitation.** Adding a rigid restraint may move the resonance rather than remove the cause.

**Reference anchors.** [HI-NPSH](../reference/SOURCES.md#hinpsh), [EXP](../reference/SOURCES.md#exp).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0036"></a>

## PK-0036 — Corrosion mechanism depends on environment

**Engineering mechanism.** Material loss may be uniform, crevice, galvanic, microbial, chloride-driven or erosion-corrosion; different mechanisms require different controls.

**Decision procedure.** Specify fluid chemistry, temperature, velocity, oxygen and material contacts; choose compatible alloys, linings, treatments and inspection method.

**Verification / closeout.** Review water analysis, material certificates, welding condition and monitoring points.

**Failure mode or limitation.** Stainless steel is not universally immune to corrosion or chloride attack.

**Reference anchors.** [AWWA](../reference/SOURCES.md#awwa), [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
