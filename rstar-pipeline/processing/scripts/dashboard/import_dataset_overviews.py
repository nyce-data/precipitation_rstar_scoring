"""Copy the dataset metadata JSON into the dashboard as dataset overview pages.

Reads every rstar-pipeline/input/dataset-metadata/*_dataset-metadata.json
and writes

  app/content/datasets/<id>/overview.json   the file without the
         working-only keys "source", "dashboard" and "review_notes"

build_datasets.py sets each card's "overview_url" when this page exists, so
the panel shows "Dataset overview". Run from the project folder after
editing the metadata JSON, then rebuild the card list:

    python3 rstar-pipeline/processing/scripts/dashboard/import_dataset_overviews.py
    python3 rstar-pipeline/processing/scripts/dashboard/build_datasets.py
"""

import json
from pathlib import Path

SOURCE = Path("rstar-pipeline/input/dataset-metadata")
CONTENT = Path("app/content/datasets")
WORKING_KEYS = ("source", "dashboard", "review_notes")


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main():
    for src in sorted(SOURCE.glob("*_dataset-metadata.json")):
        meta = json.loads(src.read_text())
        page = {k: v for k, v in meta.items() if k not in WORKING_KEYS}
        dest = CONTENT / meta["id"] / "overview.json"
        write_json(dest, page)
        print(f"wrote {dest}")
    print("\nNow run build_datasets.py to update the card list.")


if __name__ == "__main__":
    main()
