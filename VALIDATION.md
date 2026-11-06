# Validation record

Expanded edition: 7 November 2026. This original AI-assisted educational reference has automated numerical checks and a targeted second-agent review of the first edition. It has not undergone comprehensive independent professional peer review or validation against hardware.

## Numerical verification

| Script | Scope | Result |
|---|---|---|
| `verify_foundations.py` | Chapters 01–03, 34–35 and capstone: units, uncertainty, mathematical response, numerical integration, friction/wear, system interaction, schedule, energy/cost, water mass, expansion, sensor scaling | 41 checks passed |
| `verify_mechanics.py` | All 20 worked examples in chapters 04–07 and 18–23; equilibrium, energy, compatibility, independent derivative/response comparisons | 20 examples; 115 numerical and physical-identity checks passed |
| `verify_thermal.py` | All 20 worked examples in chapters 08–17; recalculated values matched to printed source sections and selected balances | 20 examples; 57 printed numerical results passed |
| `verify_systems.py` | All 20 worked examples in chapters 24–33; balances, compatibility, inverse kinematics, constraints, discounted cash flow | 20 examples passed |
| `verify_advanced_mechanics.py` | Chapters 36–37; intensity/energy, Paris integration checked by quadrature, laminate stiffness assembly, recovered ply loads and energy, thickness scaling | 4 examples and 6 exercises; 78 checks passed |
| `verify_gas_acoustics.py` | Chapters 38–39; nozzle flow, shock mass/momentum/enthalpy, logarithmic versus mean-square pressure calculations, transmission and resonance | 4 examples and 6 exercises; 44 checks passed |
| `verify_corrosion_welding.py` | Chapters 40–41; charge loss versus current density and coupon-unit conversion, cell free energy, heat-input and weld-load balances | 4 examples and 6 exercises; 36 checks passed |

The scripts cover all **82 numbered worked examples**. They check all 18 new exercise solutions in chapters 36–41 and selected earlier exercises and capstone results, but do not machine-verify every one of the **123 exercise solutions**. The new verifiers also require key checked values to appear in their published example sections. A separate read-only review of the first edition checked all 54 exercise/solution pairs in chapters 04–15 and 18–23; no material numerical mismatch was found. The resulting conceptual wording corrections were incorporated. The new specialist chapters have numerical and editorial review but have not received comprehensive independent specialist peer review.

## Document and equation checks

`check_repository.py` checks the chapter files against unique volume assignments, required section order, two examples and three exercise/solution pairs per chapter, balanced display-math delimiters, reading links, local links, README/catalog totals, and synchronization of generated books with authoritative chapter files. It rejects obvious unfinished placeholders and unexpectedly short chapters.

`check_math.cjs` uses **KaTeX 0.19.1**, with parse errors enabled, to render every identified inline/display TeX expression in the chapters, capstone, and visual guide to HTML and MathML. This verifies renderer syntax, not mathematical truth or exact equivalence to GitHub's renderer.

Historical first-edition audit (6 November): **35 chapters, 38,643 source words, 70 worked examples, 105 solved exercises, 373 displayed equation blocks, and 219 local file links** passed. Its renderer check passed **1,902 TeX expressions** across 37 source documents. These counts include inline variables and are not counts of distinct engineering formulas. The current expanded-edition totals are recorded in `catalog.json` and printed by the check scripts.

The expanded edition has 41 chapters, 82 worked examples, and 123 solved exercises. Its new numerical suites add 158 checks across 12 examples and all 18 new exercise solutions. Final chapter words, equation blocks, local links, and renderer totals are reported by the reproducible checks rather than inferred from chapter count.

Six original quantitative figures were generated from their stated equations and saved as PNG/SVG pairs. The original four were visually inspected in a combined overview; the two new fracture/acoustics figures were inspected individually for labels, units, annotations, legends, and clipping. They show hypothetical/modelled behaviour, not measurements.

The [open library](references/OPEN_LIBRARY.md) records live publisher/institution access observations and distinctions among full books, courses, data, and previews. Some large PDFs were reachable but not fully extracted; limitations are disclosed. Not every page of every external resource has been reviewed.

## Reproduce the checks

From the repository root with Python 3.10 or later:

```powershell
python scripts/verify_foundations.py
python scripts/verify_mechanics.py
python scripts/verify_thermal.py
python scripts/verify_systems.py
python scripts/verify_advanced_mechanics.py
python scripts/verify_gas_acoustics.py
python scripts/verify_corrosion_welding.py
python scripts/build_books.py
python scripts/check_repository.py
```

Optional equation check using Node.js and the official npm registry:

```powershell
npm install --prefix .tools --no-package-lock --ignore-scripts katex@0.19.1
node scripts/check_math.cjs
```

If a cloud-synchronized folder cannot reliably unpack npm packages, install to local temporary storage and set `HANDBOOK_KATEX_DIR` to that installation prefix. This package is a test dependency, not bundled book content. No installation is required to read the books on GitHub.

The [GitHub Actions workflow](.github/workflows/check.yml) reruns numerical, equation-syntax, and repository checks on pushes and pull requests. Its current result is visible on the repository's Actions tab. Passing these checks does not certify a physical design.

## Remaining limits

No real-fluid property database, CAD solid kernel, commercial FEA/CFD package, experimental apparatus, or production equipment was used to validate this handbook. Formula assumptions, empirical ranges, property values, and current design requirements must still be checked for each actual application. See [coverage and known gaps](COVERAGE.md).
