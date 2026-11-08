# Mechanical Engineering Handbook

**Theory, formulas, derivations, and worked problems across 44 mechanical engineering subjects.**

An original, editable, AI-assisted educational reference maintained by **aniltheengh**. The expanded edition contains ten theory volumes, a consolidated formula handbook, 88 worked examples, 132 exercises with explained solutions, and an integrated water-pumping capstone. Chapters use SI units and define assumptions and model limits. First published **6 November 2026**; expanded **8 November 2026**.

**[Read the full contents](CONTENTS.md) · [Open the formula handbook](books/09-formula-handbook.md) · [Find full open textbooks](references/OPEN_LIBRARY.md) · [Start learning](STUDY_GUIDE.md)**

The latest expansion adds continuum mechanics, multiphase flow, and process-plant engineering, with worked calculations and quantitative diagrams. See [what changed](CHANGELOG.md).

## The books

| Book | Subjects | Read |
|---|---|---|
| 1. Engineering foundations | Units, dimensional analysis, mathematics, numerical methods | [Theory book](books/01-foundations.md) |
| 2. Mechanics and design | Statics, dynamics, strength, materials, machine design, mechanisms, vibration, tribology | [Theory book](books/02-mechanics-and-design.md) |
| 3. Thermal engineering | Thermodynamics, power cycles, heat transfer, heat exchangers, refrigeration/HVAC, combustion and engines | [Theory book](books/03-thermal-engineering.md) |
| 4. Fluid engineering | Fluid mechanics, piping and pumps, turbomachinery, mass transfer | [Theory book](books/04-fluid-engineering.md) |
| 5. Manufacturing | Manufacturing processes, metrology, CAD and engineering drawing | [Theory book](books/05-manufacturing.md) |
| 6. Computational engineering | FEA, CFD, design and optimization | [Theory book](books/06-computational-engineering.md) |
| 7. Electromechanical systems | Electrical engineering, controls, mechatronics, robotics | [Theory book](books/07-electromechanical-systems.md) |
| 8. Engineering practice | Reliability, maintenance, economics, energy/environment, systems engineering | [Theory book](books/08-engineering-practice.md) |
| 9. Formula handbook | Formula sections gathered from every chapter | [Formula reference](books/09-formula-handbook.md) |
| 10. Specialist foundations | Fracture mechanics, composites, compressible flow, acoustics, corrosion, welding | [Theory book](books/10-specialist-foundations.md) |
| 11. Continuum, multiphase, and plants | Deformation and stress tensors, phase fractions and settling, plant balances and tank dynamics | [Theory book](books/11-continuum-multiphase-and-plants.md) |

## What every chapter contains

Each chapter has a learning map, connected theory, a formula handbook with definitions and assumptions, a derivation, two worked examples, three exercises, explained solutions, common mistakes, applications and limits, and further reading. The [individual chapter files](chapters) are the authoritative editable sources. The books are compiled from them and can be regenerated.

This is a broad undergraduate **handbook edition**, not an exhaustive substitute for full textbooks in every specialization. Read [coverage and known gaps](COVERAGE.md) before relying on its scope. The [open library](references/OPEN_LIBRARY.md) supplies longer publisher-hosted books and courses for deeper study. Commercial textbooks and design standards are linked only where relevant, not reproduced.

## Begin with a concrete project

The [water-pumping capstone](CAPSTONE.md) connects flow, pipe losses, power, thermal expansion, supports, control, maintenance, and lifecycle cost. All inputs are declared teaching assumptions. The [visual guide](VISUAL_GUIDE.md) shows how operating points, transient response, and numerical error connect to the equations.

## Read, download, and edit

Read the Markdown pages directly on GitHub; equations render in the normal file view. To keep an editable local copy, choose **Code → Download ZIP**, or clone this repository:

```powershell
git clone https://github.com/aniltheengh/Mechanical-Engineering-Handbook.git
cd Mechanical-Engineering-Handbook
```

No installation is needed to read. The verification and Markdown build use Python 3.10 or later and its standard library:

```powershell
python scripts/verify_foundations.py
python scripts/verify_mechanics.py
python scripts/verify_thermal.py
python scripts/verify_systems.py
python scripts/verify_advanced_mechanics.py
python scripts/verify_gas_acoustics.py
python scripts/verify_corrosion_welding.py
python scripts/verify_continuum.py
python scripts/verify_multiphase.py
python scripts/verify_process_plant.py
python scripts/build_books.py
python scripts/check_repository.py
```

See [contribution and editing instructions](CONTRIBUTING.md) and the [validation record](VALIDATION.md). Automated checks verify selected numerical results and document structure; they do not certify all theory or a real design.

## License

Original text and illustrations: **CC BY 4.0**. Scripts: **MIT**. External references retain their own terms. See [licensing and authorship](LICENSE.md).
