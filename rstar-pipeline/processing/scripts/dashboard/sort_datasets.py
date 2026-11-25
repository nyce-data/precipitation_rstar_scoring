"""Sort app/data/datasets.json by the card tags (data source, then coverage,
alphabetical by label), then by name. Mirrors CATEGORIES/COVERAGES in app/assets/dashboard/dashboard.js.
Run from the project folder: python3 rstar-pipeline/processing/scripts/dashboard/sort_datasets.py"""
import json, re
P = "app/data/datasets.json"
I = re.I

def category(d):
    b, c = d.get("precipitation_basis", ""), d.get("formal_cdr", "")
    if re.search(r"\b(blend|merged)", b, I): return "Merged / blended"
    if re.search(r"reanalysis", b + " " + c, I): return "Reanalysis"
    if re.search(r"satellite|microwave|\bIR\b", b, I): return "Satellite"
    return "Gauge-based"

def coverage(d):
    t = d.get("spatial_coverage", "")
    if re.search(r"united states|\bCONUS\b", t, I): return "CONUS"
    if re.search(r"north america|canada", t, I): return "North America"
    if re.search(r"^(global )?land\b", t, I) and not re.search("ocean", t, I): return "Global land"
    if re.search(r"quasi|near-global|\d+°S\s*[-–]\s*\d+°N", t, I) and "90°S" not in t: return "Quasi-global"
    return "Global"

data = json.load(open(P))
data["datasets"].sort(key=lambda d: (category(d).lower(), coverage(d).lower(), d["name"].lower()))
with open(P, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False); f.write("\n")
for d in data["datasets"]: print(f"{category(d):17} {coverage(d):14} {d['name']}")
