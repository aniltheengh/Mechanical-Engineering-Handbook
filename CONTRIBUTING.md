# Editing and maintaining the handbook

Edit the authoritative files in `chapters/`. Do not edit generated files in `books/`, `CONTENTS.md`, or `catalog.json` directly. Each chapter must retain its ten section headings, two numbered examples, and three exercises with matching solutions.

For every equation, state variable meanings, units, sign convention, and conditions of validity nearby. Distinguish a definition, conservation law, constitutive assumption, approximation, and empirical correlation. Introduce property values as supplied assumptions or cite their traceable source. Do not claim compliance with a standard from a generic textbook equation.

Write original explanations and diagrams. Link external books at their legitimate publisher/author/institution pages and label access accurately: full text, course, data, preview, commercial standard, or unavailable. Never copy an entire commercial textbook or standard into this public repository. External material has its own license even when it is free to read.

When changing a worked example, update its numerical check. Prefer an independent balance, exact result, limiting case, or converged numerical comparison over a test that simply repeats the same expression with the same guessed constant. Numerical checks do not replace editorial or engineering review.

Run these commands from the repository root:

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

The optional figure generator requires NumPy and Matplotlib. Generated figures should be visually inspected after a change to labels, limits, or layout. See [the visual guide](VISUAL_GUIDE.md).

Before committing, inspect `git diff` and stage only intended files. Preserve user study notes separately from generated artifacts. Never put credentials, personal account details, private work drawings, or proprietary project information in this public repository. Record review limits honestly in `VALIDATION.md`.
