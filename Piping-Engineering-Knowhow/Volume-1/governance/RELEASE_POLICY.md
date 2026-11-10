# Release policy and engineering acceptance

## Definitions

- **BASELINE-RESEARCHED:** Engineering concept documented with traceable public authority or transparent analysis. This is the state of all 60 Volume 1 entries. It is not an independent peer review.
- **ARITHMETIC-TESTED:** Worked equations reproduced using published inputs and executed tests.
- **PROJECT-VERIFIED:** Actual plant conditions, specific code edition, supplier instructions and owner specifications checked and documented.
- **PROJECT-ACCEPTED:** Authorized engineer approves a decision for the actual project. This repository cannot grant that approval.

## Closure rule

An entry's *research question* is closed when it has: (1) defined scope; (2) mechanism; (3) decision method; (4) assumptions; (5) verification route; (6) limitations; (7) source anchors; (8) a revision. A project design question is closed only with its own acceptance record.

## Reopen triggers (and only these)

1. Discovery of a factual or calculation error.
2. New evidence, including updated primary references or manufacturer guidance.
3. Changed code edition, jurisdiction or owner requirements.
4. Changed fluid, operating conditions, equipment or construction method.
5. New failure or inspection evidence which invalidates prior assumptions.

## Change control

- Number entries permanently (PK-0001, etc.); never reuse an identifier.
- Log corrections in CHANGELOG.md with reason, impact and affected decisions.
- Keep old accepted decisions traceable; a revised general note must not silently change a released project.
- Do not claim code-compliant calculations without licensed code and a verified applicable section.

## Verification performed in release 1.0.0

- Automated checks of entry count/field presence and references.
- Standard-library numerical tests of worked examples.
- Official websites checked for the scope of cited standards, HI and waterworks references.

**Not performed:** independently licensed professional engineering peer review, full-text licensed code review, supplier design review or real-site inspection.
