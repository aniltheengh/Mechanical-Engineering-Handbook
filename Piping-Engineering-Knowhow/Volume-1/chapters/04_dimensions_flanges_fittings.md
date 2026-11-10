# Chapter 04 — Dimensions, flanges, fittings

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0013"></a>

## PK-0013 — Steel nominal size is not actual bore

**Engineering mechanism.** Nominal pipe size and schedule determine a family of outside dimensions and wall thicknesses; true ID sets flow area.

**Decision procedure.** Obtain OD and wall from an approved dimensional standard and pipe specification; compute ID=OD−2t where appropriate.

**Verification / closeout.** Cross-check catalog, schedule, corrosion allowance and material selection before 3D spec release.

**Failure mode or limitation.** Assuming DN100 means 100 mm internal diameter can materially alter pressure-loss calculations.

**Reference anchors.** [B36.10](../reference/SOURCES.md#b3610).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0014"></a>

## PK-0014 — Fittings must match dimensional and material specification

**Engineering mechanism.** An elbow is defined by more than its angle: radius, end preparation, diameter, thickness, metallurgy and product specification also matter.

**Decision procedure.** Select the approved specification and ensure line class joins compatible fittings.

**Verification / closeout.** Compare procurement BOM against piping class, fitting standard, and geometric envelope.

**Failure mode or limitation.** A visually fitting 3D component can have incorrect end type or wall thickness.

**Reference anchors.** [B16.9](../reference/SOURCES.md#b169), [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0015"></a>

## PK-0015 — Flange pressure class is temperature-dependent

**Engineering mechanism.** ASME flange class names are ratings designations, not direct allowable working pressures in psi.

**Decision procedure.** Select flange material group and rating from the applicable standard's pressure-temperature table for the design condition.

**Verification / closeout.** Check gasket, bolting, valve flanges, facing, mating drilling and temperatures against line specification.

**Failure mode or limitation.** “Class 150 = 150 psi” is a common and potentially serious error.

**Reference anchors.** [B16.5](../reference/SOURCES.md#b165).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0016"></a>

## PK-0016 — Gasket is part of the pressure boundary

**Engineering mechanism.** Flange tightness depends on compatible gasket material, surface finish, bolt loading, flange stiffness and process fluid.

**Decision procedure.** Specify gasket as part of a joint assembly; require a documented bolting method and material compatibility.

**Verification / closeout.** Check approved gasket type, facing, pressure/temperature limits and flange joint procedure.

**Failure mode or limitation.** Choosing a gasket by nominal size alone can cause leaks even with the correct flange class.

**Reference anchors.** [B16.5](../reference/SOURCES.md#b165), [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
