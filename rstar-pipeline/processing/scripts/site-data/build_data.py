"""Build app/data/rstar-data.js for the R* categorization viewer.

Reads, all under rstar-pipeline/: the R* definitions (input/framework/definitions/*.md), the point values and
group weights (input/framework/how_to_score_rstar.md), dataset names (input/dataset-metadata/), the saved-file
format's fixed parts (input/framework/assessment-form/example_rstar_json.json) and the categorization JSON files
(output/categories/<dataset>/*.json). It works out each dataset's group totals and R* from the subcategory scores
in that JSON, and writes them as one JavaScript file, app/data/rstar-data.js, which the pages load with a <script>
tag. That keeps the site working when opened straight from disk (file://), where fetch() is blocked.

Usage (from anywhere):
    python3 rstar-pipeline/processing/scripts/site-data/build_data.py
"""
import json
import re
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[3]  # rstar-pipeline/
ROOT = PIPELINE.parent
FRAMEWORK = PIPELINE / "input" / "framework"
OUT = ROOT / "app" / "data" / "rstar-data.js"
# The colleague's R* form: the viewer's saved files copy its "formula" and "framework" blocks and its
# component letters (D, P, RRS, DIRS).
FORM_EXAMPLE = FRAMEWORK / "assessment-form" / "example_rstar_json.json"

# Category key -> (definition file, page file, id prefix, score variable).
# The id prefix is also the component key in the saved JSON (components.D, components.P, ...).
CATEGORIES = [
    ("people_risk", "p-rstar_people_risk_queries.md", "people-risk.html", "P", "p"),
    ("data_risk", "d-rstar-data_risk_queries.md", "data-risk.html", "D", "d"),
    ("dep_infra_resilience", "dirs-rstar_dependent_infrastructure_resilience_queries.md",
     "dependent-infrastructure.html", "DIRS", "dirs"),
    ("repo_resilience", "rrs-rstar_repository_resilience_queries.md",
     "repository-resilience.html", "RRS", "rrs"),
]

# Short names for the cards; the full title comes from each file's H1.
SHORT_TITLES = {
    "people_risk": "People risk",
    "data_risk": "Data risk",
    "dep_infra_resilience": "Dependent infrastructure resilience",
    "repo_resilience": "Repository resilience",
}


def clean(text):
    """Collapse a markdown block into one paragraph of plain text."""
    return " ".join(line.strip() for line in text.strip().splitlines() if line.strip())


def section(text, heading_re):
    """Return the text after a heading line up to the next heading of the same or higher level."""
    m = re.search(heading_re, text, flags=re.M)
    if not m:
        return ""
    level = len(m.group(0)) - len(m.group(0).lstrip("#"))
    rest = text[m.end():]
    stop = re.search(rf"^#{{1,{level}}} ", rest, flags=re.M)
    return rest[: stop.start()] if stop else rest


def parse_definitions(path):
    text = path.read_text(encoding="utf-8")
    # Paragraphs of the "... defined" section: the first is the short definition (landing card),
    # the rest (for example DIRS's scope note) show only on the category page.
    defined = [clean(p) for p in re.split(r"\n\s*\n", section(text, r"^## .*defined\s*$")) if p.strip()]
    subs_text = section(text, r"^## Subcategories\s*$")
    subs = []
    for m in re.finditer(r"^### (\S+)\s*$", subs_text, flags=re.M):
        sid = m.group(1)
        block = section(subs_text[m.start():], rf"^### {re.escape(sid)}\s*$")
        desc_lines = [l.strip() for l in section(block, r"^#### Description\s*$").strip().splitlines()]
        desc_lines = [l for l in desc_lines if l]
        title = desc_lines[0] if desc_lines else sid
        description = " ".join(desc_lines[1:])
        how = clean(section(block, r"^#### How to find\s*$"))
        # "What counts as evidence" is the reader's version of "How to find" (the search instructions).
        counts = clean(section(block, r"^#### What counts as evidence\s*$"))
        subs.append({"id": sid, "title": title, "description": description, "how_to_find": how,
                     "what_counts": counts})
    return defined, subs


def parse_weights(path):
    text = path.read_text(encoding="utf-8")
    points = {f"{v.upper()}-{n}": int(p)
              for v, n, p in re.findall(r"^(p|d|rrs|dirs)_(\d+)\s*=\s*\{0,\s*(\d+)\}", text, flags=re.M)}
    group = {v: float(w) for v, w in re.findall(r"(p|d|rrs|dirs)_total\)?\s*\*\s*([\d.]+)", text)}
    return points, group


def dataset_name(folder):
    meta = PIPELINE / "input" / "dataset-metadata" / f"{folder}_dataset-metadata.json"
    if not meta.exists():
        return folder, {}
    full = json.loads(meta.read_text(encoding="utf-8"))
    dash = full.get("dashboard", {})
    keep = ["name", "data_archive", "doi", "curator", "update_status", "period_of_record",
            "spatial_coverage", "temporal_frequency", "precipitation_basis"]
    info = {k: dash.get(k, "") for k in keep}
    info["identifier"] = dataset_identifier(full)
    return dash.get("name", folder), info


def dataset_identifier(meta):
    """The saved file's dataset.identifier: the DOI, else a data endpoint URL (primary first), else ""."""
    dash = meta.get("dashboard", {})
    doi = dash.get("doi") or meta.get("identification", {}).get("doi")
    if doi:
        return doi
    endpoints = dash.get("access_endpoints") or meta.get("access_endpoints") or []
    endpoints = sorted(endpoints, key=lambda e: e.get("role") != "primary")
    return next((e["url"] for e in endpoints if e.get("url")), "")


DIV_ATTRS = re.compile(r'^<div class="[^"]+"([^>]*)>')


def sub_score(html):
    """The subcategory's score from its div: an int, or "NA" (also when the div has no score)."""
    m = DIV_ATTRS.match(html or "")
    attrs = dict(re.findall(r'(data-[\w-]+)="([^"]*)"', m.group(1))) if m else {}
    raw = attrs.get("data-score", "NA")
    return {
        "score": int(raw) if raw.isdigit() else "NA",
        "basis": attrs.get("data-score-basis", "none"),
        "status": attrs.get("data-status", ""),
    }


def dataset_scores(categorizations, categories):
    """Group totals and R*. A total is NA if any of its subcategories is NA; R* is NA if any total is."""
    subs, groups = {}, {}
    for cat in categories:
        entries = [sub_score(categorizations.get(cat["key"], {}).get(s["id"])) for s in cat["subcategories"]]
        for s, e in zip(cat["subcategories"], entries):
            subs[s["id"]] = e
        known = [e["score"] for e in entries if e["score"] != "NA"]
        groups[cat["key"]] = {
            "total": sum(known) if len(known) == len(entries) else "NA",
            "scored": len(known),
            "of": len(entries),
            "known_points": sum(known),
            "max_points": sum(s["points"] or 0 for s in cat["subcategories"]),
        }
    if all(g["total"] != "NA" for g in groups.values()):
        t = {c["key"]: groups[c["key"]]["total"] for c in categories}
        w = {c["key"]: c["weight"] for c in categories}
        rstar = round(sum(
            w[k] * (100 - t[k] if k == "repo_resilience" else t[k]) for k in t), 1)
    else:
        rstar = "NA"
    return {"rstar": rstar, "groups": groups, "subcategories": subs}


def main():
    points, group = parse_weights(FRAMEWORK / "how_to_score_rstar.md")
    categories = []
    for key, deffile, page, prefix, var in CATEGORIES:
        path = FRAMEWORK / "definitions" / deffile
        defined, subs = parse_definitions(path)
        h1 = re.search(r"^# (.+)$", path.read_text(encoding="utf-8"), flags=re.M)
        for s in subs:
            s["points"] = points.get(s["id"])
        categories.append({
            "key": key,
            "prefix": prefix,
            "title": SHORT_TITLES[key],
            "heading": h1.group(1).strip() if h1 else SHORT_TITLES[key],
            "page": page,
            "definition": defined[0] if defined else "",
            "definition_more": defined[1:],
            "weight": group.get(var),
            "subcategories": subs,
            "source_file": str(path.relative_to(ROOT)),
        })

    datasets = []
    ds_root = PIPELINE / "output" / "categories"
    for folder in sorted(p for p in ds_root.iterdir() if p.is_dir()):
        files = sorted(folder.glob("*.json"))
        name, meta = dataset_name(folder.name)
        entry = {"id": folder.name, "name": name, "meta": meta, "file": None, "categorizations": None,
                 "scores": None}
        if files:
            entry["file"] = str(files[0].relative_to(ROOT))
            entry["categorizations"] = json.loads(files[0].read_text(encoding="utf-8"))
            entry["scores"] = dataset_scores(entry["categorizations"], categories)
        datasets.append(entry)

    example = json.loads(FORM_EXAMPLE.read_text(encoding="utf-8"))
    form = {"formula": example["formula"], "framework": example["framework"]}
    data = {"categories": categories, "datasets": datasets, "form": form}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "// GENERATED by rstar-pipeline/processing/scripts/site-data/build_data.py. Do not edit by hand; re-run the script.\n"
        "window.RSTAR_DATA = " + json.dumps(data, indent=1, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    n_subs = sum(len(c["subcategories"]) for c in categories)
    done = [d["id"] for d in datasets if d["categorizations"]]
    for d in datasets:
        if d["scores"]:
            na = sum(1 for e in d["scores"]["subcategories"].values() if e["score"] == "NA")
            print(f'{d["id"]}: R* {d["scores"]["rstar"]}, {na} of {len(d["scores"]["subcategories"])} subcategories NA')
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(categories)} categories, {n_subs} subcategories, "
          f"{len(datasets)} datasets ({len(done)} categorized: {', '.join(done) or 'none'}).")


if __name__ == "__main__":
    main()
