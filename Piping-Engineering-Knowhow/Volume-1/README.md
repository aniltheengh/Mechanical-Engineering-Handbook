# Piping Engineering Know-How Encyclopedia

**Volume 1: Water and Process Piping — Reusable Design Decisions**  
**Version:** 1.0.0 (scope-frozen teaching/research baseline)  
**Release date:** 2026-11-10  
**Status:** Author-produced, arithmetic-checked educational baseline; **NOT independently engineering-approved or code-compliant by assertion**.

## What's actually delivered

- **60 substantive know-how entries** across **15 chapters**, each with mechanism, decision procedure, acceptance/verification question, failure mode and source anchors.
- **6 reproducible, worked numerical cases** and accompanying executable Python standard-library calculator and tests.
- **4 engineering review checklists**, an integrated **water-treatment pump-to-filter case**, source register, scope boundaries, change-control policy, and a roadmap.
- Git-ready Markdown; no proprietary code extracts, no fabricated code-acceptance rules.

## How to use a knowledge entry

1. Open [INDEX.md](INDEX.md) and find the design question.
2. Check the **mechanism**, then follow the **decision procedure** for the actual system.
3. Check **failure modes**, equipment OEM instructions, and project-selected code/edition.
4. Record the input conditions, calculations, references and decision in [DECISION_RECORD_TEMPLATE.md](governance/DECISION_RECORD_TEMPLATE.md).
5. **Reopen only** when conditions, code edition, manufacturer data, evidence or an error changes. A completed record avoids researching the same baseline again.

## Scope and non-scope

**In scope for Volume 1:** ordinary liquid-water and general process-piping engineering decision workflows; high-level codes and specs mapping; hydraulic calculations; pump interfaces; supports, thermal motion, QA, construction review and troubleshooting.

**Not complete / not in scope:** full code rules and tables, hazardous chemical compatibility signoff, pressure vessel design, detailed CFD/FEA/stress analysis, pipe network simulation, seismic qualification, regulated approval, manufacturer-specific design, and detailed Japanese legal compliance. See [OPEN_ITEMS.md](governance/OPEN_ITEMS.md).

## Acceptance gates

- **Content gate:** 60/60 entries exist and each entry has all required fields.
- **Math gate:** examples are reproducible using [tools/piping_calc.py](tools/piping_calc.py), with [tests/test_piping_calc.py](tests/test_piping_calc.py).
- **Evidence gate:** factual code applicability and rating references point to authoritative public catalogues; complete code clauses are **not** claimed verified.
- **Engineering gate:** NOT passed; requires the actual project documents, OEM curves and qualified reviewer if used for design release.

Run tests: `python -m unittest discover -s tests -v`.

## Copyright and compliance

Written as an original synthesis. It provides pointers to standards but **does not reproduce proprietary code text**. If an adopted governing code disagrees with this baseline, the governing code and approved project documents control. Do not use this work as sole basis for safety-critical procurement, fabrication, operation or pressure testing.

## Start here

- [60-entry index](INDEX.md)
- [Worked examples](worked_examples/README.md)
- [Integrated water-treatment case](worked_examples/WATER_TREATMENT_CASE.md)
- [Design reviews](checklists/)
- [Sources](reference/SOURCES.md)
- [Scope and change control](governance/RELEASE_POLICY.md)
- [Future roadmap](ROADMAP.md)
