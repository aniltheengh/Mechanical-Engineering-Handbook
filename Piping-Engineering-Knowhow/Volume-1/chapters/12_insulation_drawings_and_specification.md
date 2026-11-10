# Chapter 12 — Insulation, drawings and specification

> Scope: general educational engineering baseline, **not** a project-accepted design or substitute for the governing code and manufacturer documents.

<a id="pk-0045"></a>

## PK-0045 — Insulation can conceal corrosion and defects

**Engineering mechanism.** Cladding, wet insulation and hidden attachments alter access and inspection needs.

**Decision procedure.** Select insulation details for the thermal duty while planning water ingress protection and inspection/removal access.

**Verification / closeout.** Review supports, low points and penetrations for water traps and material compatibility.

**Failure mode or limitation.** Assuming a line is protected solely because it is insulated can conceal degradation.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0046"></a>

## PK-0046 — P&ID is functional, model is spatial

**Engineering mechanism.** A P&ID represents system connectivity, valves, instrumentation and operating intent; 3D resolves real geometry and placement.

**Decision procedure.** Reconcile tag, line number, valve function, connection direction and normally open/closed logic between documents.

**Verification / closeout.** Run line-by-line walkdowns for revisions, bypasses, drains, vents and instruments.

**Failure mode or limitation.** An isometric or ortho can be geometrically accurate but functionally wrong.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0047"></a>

## PK-0047 — Line class links design to procurement

**Engineering mechanism.** A pipe specification class collects allowed pipe, fittings, flanges, valves, material, rating and joining rules for a service envelope.

**Decision procedure.** Freeze approved line classes and match each model component to its intended spec and requisition.

**Verification / closeout.** Compare line list, spec assignment, BOM and vendor data for mismatches.

**Failure mode or limitation.** A model that silently switches spec can introduce incompatible parts.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313), [B16.5](../reference/SOURCES.md#b165), [B16.9](../reference/SOURCES.md#b169).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---

<a id="pk-0048"></a>

## PK-0048 — Isometric is a manufacturing deliverable

**Engineering mechanism.** An isometric communicates dimensions, cut lengths, elevations, welds, fittings, bill of materials and fabrication limits.

**Decision procedure.** Check dimensions, support callouts, field welds, spool split and tie-ins before IFC issue.

**Verification / closeout.** Perform drawing-model-P&ID reconciliation with revision and change control.

**Failure mode or limitation.** Iso-generation software does not validate engineering correctness.

**Reference anchors.** [B31.3](../reference/SOURCES.md#b313).

**Entry state:** `BASELINE-RESEARCHED`; **project acceptance:** `NOT ASSESSED`.

---
