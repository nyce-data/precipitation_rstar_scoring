"""Build the dashboard's card list, app/data/datasets.json, from the dataset metadata.

Each rstar-pipeline/input/dataset-metadata/<id>_dataset-metadata.json has a
"dashboard" block holding that dataset's card. That block is the only place
to edit a card; this script copies every block into the card list and:

  sets  "about_url"    to "dataset.html?id=<id>" when the dataset is listed in
                       app/data/dataset_pages.json (it has web research pages),
                       else ""
  sets  "overview_url" to "overview.html?id=<id>" when
                       app/content/datasets/<id>/overview.json exists (written
                       by import_dataset_overviews.py), else ""
  sorts the cards by data source, then coverage, then name (the tags the
                       dashboard shows; mirrors CATEGORIES/COVERAGES in
                       app/assets/dashboard/dashboard.js)

Run from the project folder after editing a metadata file, or after
import_dataset_pages.py or import_dataset_overviews.py:

    python3 rstar-pipeline/processing/scripts/dashboard/build_datasets.py
"""

import json
import re
import sys
from pathlib import Path

METADATA = Path("rstar-pipeline/input/dataset-metadata")
PAGES = Path("app/data/dataset_pages.json")
CONTENT = Path("app/content/datasets")
DATASETS = Path("app/data/datasets.json")
I = re.I


def category(card: dict) -> str:
    """The card's data-source tag."""
    basis, cdr = card.get("precipitation_basis", ""), card.get("formal_cdr", "")
    if re.search(r"\b(blend|merged)", basis, I):
        return "Merged / blended"
    if re.search(r"reanalysis", basis + " " + cdr, I):
        return "Reanalysis"
    if re.search(r"satellite|microwave|\bIR\b", basis, I):
        return "Satellite"
    return "Gauge-based"


def coverage(card: dict) -> str:
    """The card's coverage tag."""
    text = card.get("spatial_coverage", "")
    if re.search(r"united states|\bCONUS\b", text, I):
        return "CONUS"
    if re.search(r"north america|canada", text, I):
        return "North America"
    if re.search(r"^(global )?land\b", text, I) and not re.search("ocean", text, I):
        return "Global land"
    if re.search(r"quasi|near-global|\d+°S\s*[-–]\s*\d+°N", text, I) and "90°S" not in text:
        return "Quasi-global"
    return "Global"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    with_pages = {d["id"] for d in read_json(PAGES)["datasets"]}
    cards, problems = [], []

    for src in sorted(METADATA.glob("*_dataset-metadata.json")):
        meta = read_json(src)
        card = dict(meta.get("dashboard") or {})
        if not card:
            problems.append(f"{src.name}: no 'dashboard' block")
            continue
        ds_id = card.get("id")
        if ds_id != meta.get("id"):
            problems.append(f"{src.name}: dashboard id {ds_id!r} differs from the file's id {meta.get('id')!r}")
            continue
        card["about_url"] = f"dataset.html?id={ds_id}" if ds_id in with_pages else ""
        has_overview = (CONTENT / ds_id / "overview.json").is_file()
        card["overview_url"] = f"overview.html?id={ds_id}" if has_overview else ""
        if not has_overview:
            print(f"note: {ds_id} has no overview page yet (run import_dataset_overviews.py)")
        cards.append(card)

    ids = [c["id"] for c in cards]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        problems.append(f"id {dup!r} is used by more than one metadata file")
    for missing in sorted(with_pages - set(ids)):
        print(f"warning: {PAGES} lists {missing!r}, which has no metadata file (no card)", file=sys.stderr)
    if problems:
        print("Not written; fix these first:", *problems, sep="\n  ", file=sys.stderr)
        return 1

    cards.sort(key=lambda c: (category(c).lower(), coverage(c).lower(), c["name"].lower()))
    DATASETS.write_text(json.dumps({"datasets": cards}, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    print(f"Wrote {DATASETS} ({len(cards)} cards):")
    for c in cards:
        print(f"  {category(c):17} {coverage(c):14} {c['name']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
