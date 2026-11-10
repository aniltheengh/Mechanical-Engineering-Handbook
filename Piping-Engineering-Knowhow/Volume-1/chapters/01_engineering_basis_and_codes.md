# Chapter 01 — Engineering basis and codes

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0001"></a>

## PK-0001 — System boundary and design basis

**Engineering mechanism.** A piping line cannot be judged without fluid, composition, normal and design pressures, temperature, flow range, elevation, operating mode, and upset scenarios.

**Decision procedure.** Record a line list and design basis before assigning diameter, material, rating, or location; keep assumptions traceable to a process deliverable.

**Verification / closeout.** Confirm agreed design cases, minimum/maximum temperatures, pressure source, control philosophy and owner requirements.

**Failure mode or limitation.** A visually correct model can fail when an alternate operating state is omitted.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0002"></a>

## PK-0002 — Operating pressure versus design pressure

**Engineering mechanism.** Normal pressure is a typical operating condition; design pressure is an approved envelope used for mechanical design, often affected by shutoff and transients.

**Decision procedure.** Obtain the designated design pressure from the responsible process/mechanical engineer rather than automatically equating it to the pump duty pressure.

**Verification / closeout.** Check scenarios such as pump shutoff, trapped-liquid thermal expansion, blocked outlets and relief-system philosophy.

**Failure mode or limitation.** Design pressure is not universally the highest observed instrument reading or a simple fixed safety multiplier.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0003"></a>

## PK-0003 — Pressure at an elevation change

**Engineering mechanism.** For a static liquid, pressure changes approximately with density times gravity times elevation difference; dynamic losses also contribute during flow.

**Decision procedure.** Evaluate the highest and lowest points for minimum absolute pressure and maximum local pressure, not only line endpoints.

**Verification / closeout.** Review hydraulic grade line and elevation profile at minimum and maximum flow; assess vacuum and vaporization.

**Failure mode or limitation.** Assuming all points share the same operating pressure conceals air ingress and overpressure risks.

**Reference anchors.** [EPA-MAIN](../reference/SOURCES.md#epamain).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0004"></a>

## PK-0004 — Select the governing piping code

**Engineering mechanism.** An ASME B31 code or other governing system depends on service, facility type, regulatory jurisdiction and contractual requirements.

**Decision procedure.** Use a code applicability matrix; distinguish process piping, power piping, building services, municipal waterworks and other applications.

**Verification / closeout.** Owner/authority approval of code, edition, exclusions and material/component specifications is required.

**Failure mode or limitation.** Calling every plant water line “B31.3” without checking scope can misapply requirements.

**Reference anchors.** [ASME-B31](../reference/SOURCES.md#asmeb31), [B31.3](../reference/SOURCES.md#b313), [B31.1](../reference/SOURCES.md#b311), [B31.9](../reference/SOURCES.md#b319), [AWWA](../reference/SOURCES.md#awwa).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
