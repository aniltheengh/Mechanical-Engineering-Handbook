"""Compile editable Markdown chapters into eight books and a formula reference.

Standard library only. Chapters are authoritative; books and catalog are generated.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
VOLUMES = [
    ("01-foundations", "Engineering foundations", [1, 2, 3]),
    ("02-mechanics-and-design", "Mechanics, materials, and machine design", [4, 5, 6, 7, 18, 19, 20, 34]),
    ("03-thermal-engineering", "Thermodynamics and thermal engineering", [8, 9, 12, 13, 15, 16]),
    ("04-fluid-engineering", "Fluid engineering and transport", [10, 11, 14, 17]),
    ("05-manufacturing", "Manufacturing, metrology, and CAD", [21, 22, 23]),
    ("06-computational-engineering", "Computational engineering and optimization", [24, 25, 30]),
    ("07-electromechanical-systems", "Electrical, control, mechatronics, and robotics", [26, 27, 28, 29]),
    ("08-engineering-practice", "Reliability, economics, energy, and systems", [31, 32, 33, 35]),
]


def chapter_title(text):
    return text.splitlines()[0].removeprefix("# ").strip()


def relocate_links(text):
    # Chapters and books are siblings; their ../ links already share a base.
    # Bare sibling-chapter links must instead point into chapters/.
    return re.sub(r"\]\((\d{2}-[^)\s]+\.md)(#[^)]*)?\)",
                  lambda m: f"](../chapters/{m[1]}{m[2] or ''})", text)


def build():
    books = ROOT / "books"
    books.mkdir(exist_ok=True)
    files = {int(p.name[:2]): p for p in sorted((ROOT / "chapters").glob("[0-9][0-9]-*.md"))}
    expected = [n for _, _, nums in VOLUMES for n in nums]
    if sorted(files) != list(range(1, 36)) or sorted(expected) != list(range(1, 36)):
        raise SystemExit("Expected exactly the 35 unique chapters before compiling.")
    catalog = []
    index = ["# Contents", "", "[Start page](README.md) · [Study route](STUDY_GUIDE.md) · [Coverage and limits](COVERAGE.md)", ""]
    formulas = ["# Mechanical Engineering Formula Handbook", "", "Generated from the 35 chapter formula sections. Read the linked chapter for derivations, examples, and additional assumptions. Symbols are local to each chapter; SI is the default. This reference does not supply code-compliant design rules or proprietary property tables.", ""]
    for slug, title, nums in VOLUMES:
        book = [f"# {title}", "", "Mechanical Engineering Handbook · First edition · 2026-11-06", "", "An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).", "", "## Chapters", ""]
        for n in nums:
            p = files[n]
            txt = p.read_text(encoding="utf-8")
            title_ch = chapter_title(txt)
            book.append(f"- [{title_ch}](../chapters/{p.name})")
        index += [f"## [{title}](books/{slug}.md)", ""]
        for n in nums:
            p = files[n]
            txt = p.read_text(encoding="utf-8")
            title_ch = chapter_title(txt)
            word_count = len(txt.split())
            catalog.append({"number": n, "title": title_ch, "path": f"chapters/{p.name}", "volume": slug, "source_words": word_count,
                            "worked_examples": len(re.findall(r"^(?:### Example|\*\*Example)\s+\d", txt, re.M)),
                            "display_equation_blocks": len(re.findall(r"^\$\$\s*$",txt,re.M)) // 2})
            index.append(f"- [{title_ch}](chapters/{p.name})")
            # Demote source headings by one level so the volume has one H1.
            body = re.sub(r"^(#{1,5}) ", r"\1# ", relocate_links(txt), flags=re.M)
            book += ["", "---", "", body.rstrip(), ""]
            formula = txt.split("## Formula handbook\n", 1)[1].split("\n## ", 1)[0].strip()
            formulas += [f"## {title_ch}", "", f"[Full chapter](../chapters/{p.name})", "", relocate_links(formula), ""]
        index.append("")
        (books / f"{slug}.md").write_text("\n".join(book), encoding="utf-8")
    catalog.sort(key=lambda x: x["number"])
    (ROOT / "catalog.json").write_text(json.dumps({"edition": "2026-11-06", "chapters": catalog, "source_words": sum(x["source_words"] for x in catalog)}, indent=2) + "\n", encoding="utf-8")
    (ROOT / "CONTENTS.md").write_text("\n".join(index), encoding="utf-8")
    (books / "09-formula-handbook.md").write_text("\n".join(formulas), encoding="utf-8")
    print(f"Built 8 theory volumes and 1 formula handbook from 35 chapters; {sum(x['source_words'] for x in catalog):,} source words (including equations and references).")


if __name__ == "__main__":
    build()
