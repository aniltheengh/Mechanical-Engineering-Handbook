"""Check required content, exercise counts, local links, and generated-book drift."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote
from build_books import build, VOLUMES

ROOT=Path(__file__).resolve().parents[1]
SECTIONS=["Learning map","Theory","Formula handbook","Derivation","Worked examples","Exercises","Solutions","Common mistakes","Applications and limits","Further reading"]
errors=[]
def require(condition,message):
    if not condition: errors.append(message)

chapters=sorted((ROOT/"chapters").glob("[0-9][0-9]-*.md"))
expected_numbers=[n for _,_,numbers in VOLUMES for n in numbers]
actual_numbers=[int(p.name[:2]) for p in chapters]
require(len(expected_numbers)==len(set(expected_numbers)),"Duplicate chapter assignment in volume catalog")
require(sorted(actual_numbers)==sorted(expected_numbers),"Chapter files must exactly match volume assignments")
examples=exercises=display=words=0
for path in chapters:
    text=path.read_text(encoding="utf-8")
    require(re.findall(r"^## (.+)$",text,re.M)==SECTIONS,f"{path.name}: section order mismatch")
    require(len(re.findall(r"^# ",text,re.M))==1,f"{path.name}: expected one H1")
    wc=len(text.split()); words+=wc
    require(wc>=850,f"{path.name}: unexpectedly short ({wc} source words)")
    delimiters=re.findall(r"^\$\$\s*$",text,re.M)
    require(len(delimiters)%2==0,f"{path.name}: unbalanced display-math delimiters")
    display+=len(delimiters)//2
    ex=re.findall(r"^(?:### Example|\*\*Example)\s+(\d+(?:-[AB])?)",text,re.M)
    expected_ids=[f"{path.name[:2]}-A",f"{path.name[:2]}-B"]
    require(ex==["1","2"] or ex==expected_ids,f"{path.name}: expected two sequential example identifiers, got {ex}")
    examples+=len(ex)
    for section in ("Exercises","Solutions"):
        if f"## {section}\n" not in text: continue
        content=text.split(f"## {section}\n",1)[1].split("\n## ",1)[0]
        nums=re.findall(r"^(\d+)\. ",content,re.M)
        require(nums==["1","2","3"],f"{path.name}: {section} numbered items {nums}")
        if section=="Exercises": exercises+=len(nums)
    require(len(re.findall(r"https?://",text.split("## Further reading")[-1]))>=2,f"{path.name}: expected at least two reading links")
    require(not re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b",text),f"{path.name}: unfinished placeholder")

generated=[ROOT/"CONTENTS.md",ROOT/"catalog.json"]+[ROOT/"books"/f"{slug}.md" for slug,_,_ in VOLUMES]+[ROOT/"books/09-formula-handbook.md"]
before={p:p.read_bytes() if p.exists() else None for p in generated}
if sorted(actual_numbers)==sorted(expected_numbers) and len(expected_numbers)==len(set(expected_numbers)):
    build()
    for p in generated: require(before[p]==p.read_bytes(),f"Generated file stale: {p.relative_to(ROOT)}; rebuild and rerun")

local_links=0
for path in sorted(ROOT.rglob("*.md")):
    if any(part.startswith(".") for part in path.relative_to(ROOT).parts): continue
    text=path.read_text(encoding="utf-8")
    for match in re.finditer(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)",text):
        target=match[1].strip("<>")
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:",target) or target.startswith("#"): continue
        filename=unquote(target.split("#",1)[0])
        resolved=(path.parent/filename).resolve()
        require(resolved.is_relative_to(ROOT),f"{path.name}: link escapes repository: {target}")
        require(resolved.exists(),f"{path.relative_to(ROOT)}: broken local link {target}")
        local_links+=1

for required in ["README.md","COVERAGE.md","STUDY_GUIDE.md","CAPSTONE.md","VALIDATION.md","LICENSE.md","CONTRIBUTING.md","VISUAL_GUIDE.md","references/OPEN_LIBRARY.md"]:
    require((ROOT/required).is_file(),f"Required document missing: {required}")
if errors:
    print("FAIL:\n"+"\n".join(errors)); sys.exit(1)
catalog=json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))
require(catalog["source_words"]==words,"Catalog total drift")
require(catalog["chapter_count"]==len(chapters),"Catalog chapter-count drift")
require(catalog["theory_volumes"]==len(VOLUMES),"Catalog volume-count drift")
readme=(ROOT/"README.md").read_text(encoding="utf-8")
require(f"across {len(chapters)} mechanical engineering subjects" in readme,"README chapter count is stale")
require(f"{examples} worked examples" in readme,"README worked-example count is stale")
require(f"{exercises} exercises with explained solutions" in readme,"README exercise count is stale")
if errors: print("FAIL:\n"+"\n".join(errors)); sys.exit(1)
print(f"PASS: {len(chapters)} chapters; {words:,} source words; {examples} worked examples; {exercises} solved exercises; {display} display-equation blocks; {local_links} local links.")
