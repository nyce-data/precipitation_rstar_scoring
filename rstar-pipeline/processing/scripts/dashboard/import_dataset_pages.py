"""Copy the dataset web research into the dashboard as dataset about pages.

Reads app/data/dataset_pages.json, which lists, for each dataset:

  { "id": "<dataset id in datasets.json>",
    "research_folder": "<folder under RESEARCH_ROOT>",
    "parts": [ { "part": 1, "topic": "Overview" }, ... ] }

For each part it finds RESEARCH_ROOT/<research_folder>/*-pt<N>/ (the
folder name must end in -pt<N>; the date in front doesn't matter) and
writes:

  app/content/datasets/<id>/pt<N>.md    the answer_*.md, cleaned: its
                                        first "# " heading, the "Saved in"
                                        paragraph, research-file sentences
                                        and tool notes removed
  app/content/datasets/<id>/pt<N>.json  { "question": ..., "searched_on": [...] }
                                        from query_questions.txt

It also sets "about_url" to "dataset.html?id=<id>" for each listed
dataset in app/data/datasets.json, so the panel shows "About dataset".

Run from the project folder after adding or editing research:

    python3 rstar-pipeline/processing/scripts/dashboard/import_dataset_pages.py

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
DATASETS = Path("app/data/datasets.json")
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


def part_folder(dataset: dict, part: int) -> Path:
    base = RESEARCH_ROOT / dataset["research_folder"]
    found = sorted(p for p in base.glob(f"*-pt{part}") if p.is_dir())
    if len(found) != 1:
        raise SystemExit(f"Expected one folder {base}/*-pt{part}, found {len(found)}")
    return found[0]


def import_part(dataset: dict, part: dict) -> None:
    folder = part_folder(dataset, part["part"])
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


def set_about_urls(ids: list[str]) -> None:
    data = json.loads(DATASETS.read_text(encoding="utf-8"))
    known = {d["id"] for d in data["datasets"]}
    for missing in sorted(set(ids) - known):
        print(f"Warning: no dataset with id {missing!r} in {DATASETS}", file=sys.stderr)
    for d in data["datasets"]:
        if d["id"] in ids:
            d["about_url"] = f"dataset.html?id={d['id']}"
    DATASETS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for dataset in manifest["datasets"]:
        for part in dataset["parts"]:
            import_part(dataset, part)
    set_about_urls([d["id"] for d in manifest["datasets"]])
    print(f"Set about_url in {DATASETS} for {len(manifest['datasets'])} datasets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
