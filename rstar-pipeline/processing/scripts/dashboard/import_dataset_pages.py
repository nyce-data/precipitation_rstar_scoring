"""Copy the dataset web research into the dashboard as dataset about pages.

Reads app/data/dataset_pages.json, which lists, for each dataset:

  { "id": "<dataset id, as in its metadata file>",
    "research_folder": "<folder under RESEARCH_ROOT>",
    "parts": [ { "part": 1, "topic": "Overview" }, ... ] }

For each part it finds RESEARCH_ROOT/<research_folder>/*-pt<N>/ (the
folder name must end in -pt<N>; the date in front doesn't matter). A part
can instead name its run folder with "folder", for when one query file
held several runs and their folders share a -pt<N> ending, e.g.

  { "part": 8, "topic": "...", "folder": "2026-11-24_gpcp-daily-calibration-copies-pt7" }

It writes:

  app/content/datasets/<id>/pt<N>.md    the answer_*.md, cleaned: its
                                        first "# " heading, the "Saved in"
                                        paragraph, research-file sentences
                                        and tool notes removed
  app/content/datasets/<id>/pt<N>.json  { "question": ..., "searched_on": [...] }
                                        from query_questions.txt

build_datasets.py reads the same list to set each card's "about_url", so
the panel shows "About dataset". Run from the project folder after adding
or editing research, then rebuild the card list:

    python3 rstar-pipeline/processing/scripts/dashboard/import_dataset_pages.py
    python3 rstar-pipeline/processing/scripts/dashboard/build_datasets.py

It prints any lines that still mention a research tool (WebFetch,
subagent, extract) or link to a research-project file, to check by hand.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from import_archive_page import clean  # noqa: E402  (also strips tool notes)
from research_text import tool_mentions  # noqa: E402

RESEARCH_ROOT = Path("rstar-pipeline/input/web-research/about-datasets")
MANIFEST = Path("app/data/dataset_pages.json")
CONTENT = Path("app/content/datasets")

# Links that only work inside the research project.
_LOCAL_LINK = re.compile(r"\]\((?:\./|web_search_results/)[^)]*\)")


def read_questions(path: Path) -> dict:
    """query_questions.txt: lines under <Question> and <Searched on>."""
    question, searched, current = [], [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if text == "<Question>":
            current = question
        elif text == "<Searched on>":
            current = searched
        elif text and current is not None:
            current.append(text)
    return {"question": " ".join(question), "searched_on": searched}


def drop_title(text: str) -> str:
    """Remove the answer's first "# " heading; the page shows its own title."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            del lines[i]
            break
    return "\n".join(lines).lstrip("\n").rstrip() + "\n"


def part_folder(dataset: dict, part: dict) -> Path:
    base = RESEARCH_ROOT / dataset["research_folder"]
    if "folder" in part:
        folder = base / part["folder"]
        if not folder.is_dir():
            raise SystemExit(f"No folder {folder} (part {part['part']}'s \"folder\")")
        return folder
    n = part["part"]
    found = sorted(p for p in base.glob(f"*-pt{n}") if p.is_dir())
    if len(found) != 1:
        names = ", ".join(p.name for p in found)
        raise SystemExit(f"Expected one folder {base}/*-pt{n}, found {len(found)}"
                         + (f" ({names}); name one with \"folder\"" if found else ""))
    return found[0]


def import_part(dataset: dict, part: dict) -> None:
    folder = part_folder(dataset, part)
    answers = sorted(folder.glob("answer*.md"))
    if len(answers) != 1:
        raise SystemExit(f"Expected one answer*.md in {folder}, found {len(answers)}")

    text = drop_title(clean(answers[0].read_text(encoding="utf-8")))
    dest = CONTENT / dataset["id"] / f"pt{part['part']}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")

    questions = read_questions(folder / "query_questions.txt")
    dest.with_suffix(".json").write_text(
        json.dumps(questions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {dest} (+ .json, {len(questions['searched_on'])} searched-on items)")

    for n, line in tool_mentions(text):
        print(f"  check: line {n} mentions a research tool: {line.strip()[:120]}")
    for n, line in enumerate(text.splitlines(), 1):
        if _LOCAL_LINK.search(line):
            print(f"  check: line {n} links to a research-project file: {line.strip()[:120]}")


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for dataset in manifest["datasets"]:
        for part in dataset["parts"]:
            import_part(dataset, part)
    print("\nNow run build_datasets.py to update the card list.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
