"""Copy the dataset metadata JSON into the dashboard as dataset overview pages.

Reads every rstar-pipeline/input/dataset-metadata/*_dataset-metadata.json
(the user's master copies, kept out of git) and, for each one whose "id"
is in app/data/datasets.json:

  writes app/content/datasets/<id>/overview.json   the file without the
         working-only keys "source", "dashboard" and "review_notes"
  sets   "overview_url": "overview.html?id=<id>" on that dataset in
         app/data/datasets.json, so the panel shows "Dataset overview"

It then lists any field where a file's "dashboard" block differs from the
dataset's entry in datasets.json, so the two can be kept in step by hand
(about_url and overview_url are set by scripts and not compared).

Run from the project folder after editing the metadata JSON:

    python3 rstar-pipeline/processing/scripts/dashboard/import_dataset_overviews.py
"""

import json
from pathlib import Path

SOURCE = Path("rstar-pipeline/input/dataset-metadata")
DATASETS = Path("app/data/datasets.json")
CONTENT = Path("app/content/datasets")
WORKING_KEYS = ("source", "dashboard", "review_notes")
SCRIPT_KEYS = ("about_url", "overview_url")


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main():
    data = json.loads(DATASETS.read_text())
    by_id = {d["id"]: d for d in data["datasets"]}
    differences = []

    for src in sorted(SOURCE.glob("*_dataset-metadata.json")):
        meta = json.loads(src.read_text())
        ds_id = meta["id"]
        row = by_id.get(ds_id)
        if row is None:
            print(f"skipped {src.name}: no dataset with id {ds_id!r} in {DATASETS}")
            continue

        page = {k: v for k, v in meta.items() if k not in WORKING_KEYS}
        dest = CONTENT / ds_id / "overview.json"
        write_json(dest, page)
        row["overview_url"] = f"overview.html?id={ds_id}"
        print(f"wrote {dest}")

        block = meta.get("dashboard", {})
        for key in sorted(set(block) | set(row)):
            if key in SCRIPT_KEYS:
                continue
            if block.get(key) != row.get(key):
                differences.append(f"  {ds_id}: {key}")

    write_json(DATASETS, data)
    if differences:
        print("\n'dashboard' block differs from datasets.json for:")
        print("\n".join(differences))
    else:
        print("\nEvery 'dashboard' block matches datasets.json.")


if __name__ == "__main__":
    main()
