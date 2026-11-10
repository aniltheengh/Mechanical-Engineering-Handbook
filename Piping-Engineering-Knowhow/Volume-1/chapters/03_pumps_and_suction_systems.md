# Chapter 03 — Pumps and suction systems

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0009"></a>

## PK-0009 — Pump duty point is an intersection

**Engineering mechanism.** A rotodynamic pump operates where its head-flow curve intersects the system curve; changing throttling, filter fouling or speed shifts the point.

**Decision procedure.** Model the system curve at clean and dirty filter conditions and overlay manufacturer pump performance curves.

**Verification / closeout.** Confirm acceptable operating region, motor load, NPSH and min-flow limits throughout the operating envelope.

**Failure mode or limitation.** A pump selected only at one tabulated Q,H point may operate far from its best efficiency region.

**Reference anchors.** [HI-SYSTEM](../reference/SOURCES.md#hisystem), [HI-CURVES](../reference/SOURCES.md#hicurves).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0010"></a>

## PK-0010 — Available NPSH is a suction-system property

**Engineering mechanism.** NPSHA depends on absolute inlet head relative to liquid vapor pressure, including elevation, atmospheric or vessel pressure, and suction losses.

**Decision procedure.** For an open tank, estimate NPSHA as atmospheric pressure head + liquid free-surface elevation above pump datum − suction losses − vapor-pressure head.

**Verification / closeout.** Compare at hot liquid, lowest tank level, maximum flow, highest site altitude and dirty strainers as relevant.

**Failure mode or limitation.** NPSHA merely exceeding NPSHR or NPSH3 does not itself guarantee trouble-free cavitation margin.

**Reference anchors.** [HI-NPSH](../reference/SOURCES.md#hinpsh), [HI-DEFS](../reference/SOURCES.md#hidefs).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0011"></a>

## PK-0011 — Pump suction geometry affects flow quality

**Engineering mechanism.** Elbows, reducers and nearby valves can create swirl, uneven velocity and air pockets entering a centrifugal pump.

**Decision procedure.** Follow the specific pump's suction piping instructions; ensure suitable upstream arrangement, reducer orientation, venting and independent supports.

**Verification / closeout.** Review manufacturer drawing, actual approach geometry and available suction head; verify after installation.

**Failure mode or limitation.** Do not treat a generic '5D' straight-run rule as universally mandatory or sufficient.

**Reference anchors.** [HI-FAQ](../reference/SOURCES.md#hifaq), [HI-NPSH](../reference/SOURCES.md#hinpsh).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0012"></a>

## PK-0012 — Pumping power depends on total required head

**Engineering mechanism.** Hydraulic power equals density times gravity times flow times total developed head; shaft power is higher because pump efficiency is below one.

**Decision procedure.** Calculate static and dynamic head at each duty point, then divide hydraulic power by pump efficiency from the actual performance curve.

**Verification / closeout.** Check maximum absorbed shaft power and motor sizing across pump operating range and liquid properties.

**Failure mode or limitation.** Confusing hydraulic and electrical power leads to under-sized drives.

**Reference anchors.** [HI-CURVES](../reference/SOURCES.md#hicurves), [HI-SYSTEM](../reference/SOURCES.md#hisystem).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
