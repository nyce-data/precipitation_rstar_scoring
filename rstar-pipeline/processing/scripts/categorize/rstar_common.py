"""Shared helpers for the build_<id>.py categorization scripts.

Each dataset script holds its hand-sorted evidence and calls write_categories(), which scores every
subcategory and writes rstar-pipeline/output/categories/<id>/<id>_rstar-categories.json.

Evidence item: (confidence, source run, text, stance) or, for RRS, (confidence, source run, text, stance, repository).
  confidence: "high", "moderate" or "low" (inferences are always low);
  stance: "F" for, "A" against, "C" context (toward the subcategory's statement).
Gap item: (status, text), status "S" searched and none found, "P" not public, "U" not searched.

Scoring (rstar-pipeline/input/framework/how_to_score_rstar.md): only high and moderate "for" and "against" items
count. For only gives full points, against only gives 0, and both or neither gives NA.

The rules for filing evidence are in rstar-pipeline/input/framework/rstar-categorization-decisions.md.
"""

import html
import json
import re
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[3]  # rstar-pipeline/
SCORING = PIPELINE / "input" / "framework" / "how_to_score_rstar.md"

H, M, L = "high", "moderate", "low"

STANCE_NAME = {"F": "for", "A": "against", "C": "context"}
STANCE_ORDER = {"for": 0, "against": 1, "context": 2}
GAP_STATUS = {"S": "searched-none-found", "P": "not-public", "U": "not-searched"}

CATEGORY_IDS = {
    "people_risk": ["P-1", "P-2", "P-3", "P-4"],
    "data_risk": ["D-1", "D-2", "D-3", "D-4", "D-5"],
    "dep_infra_resilience": ["DIRS-1", "DIRS-2", "DIRS-3", "DIRS-4", "DIRS-5"],
    "repo_resilience": ["RRS-1", "RRS-2", "RRS-3", "RRS-4", "RRS-5"],
}

LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def fmt(text):
    """Escape text for HTML, turning markdown links [label](url) into <a> tags."""
    out, pos = [], 0
    for m in LINK.finditer(text):
        out.append(html.escape(text[pos:m.start()]))
        out.append(f'<a href="{html.escape(m.group(2))}">{html.escape(m.group(1))}</a>')
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return "".join(out)


def read_points():
    """Points per subcategory from the scoring doc, e.g. {"P-1": 35, ...}."""
    text = SCORING.read_text(encoding="utf-8")
    return {f"{v.upper()}-{n}": int(p)
            for v, n, p in re.findall(r"^(p|d|rrs|dirs)_(\d+)\s*=\s*\{0,\s*(\d+)\}", text, flags=re.M)}


def score(evidence, points):
    """Return (score, basis): score is the points, 0 or "NA"; basis says why."""
    counted = {STANCE_NAME[e[3]] for e in evidence if e[0] in (H, M)}
    has_for, has_against = "for" in counted, "against" in counted
    if has_for and not has_against:
        return points, "for-only"
    if has_against and not has_for:
        return 0, "against-only"
    if has_for and has_against:
        return "NA", "both"
    return "NA", "none"


def status(evidence, gaps):
    """Subcategory status: found if there is any evidence, else the strongest gap status."""
    if evidence:
        return "found"
    codes = {g[0] for g in gaps}
    for code in ("P", "S"):
        if code in codes:
            return GAP_STATUS[code]
    return "not-searched"


def div(key, evidence, gaps, points, repositories=None):
    """The subcategory's HTML: Evidence and Gaps lists inside <div class="<key>" data-score=...>."""
    cls = key.lower()
    sc, basis = score(evidence, points)
    attrs = f'class="{cls}" data-score="{sc}" data-score-basis="{basis}" data-status="{status(evidence, gaps)}"'
    if repositories:
        attrs += f' data-repositories="{html.escape("; ".join(repositories))}"'
    if not evidence and not gaps:
        return f"<div {attrs}></div>"
    # Sort by stance (for, against, context); Python's sort keeps the original order within a group.
    items = sorted(evidence, key=lambda e: STANCE_ORDER[STANCE_NAME[e[3]]])
    parts = [f"<div {attrs}>"]
    if evidence:
        parts.append('<h4>Evidence</h4><ul class="evidence">')
        for item in items:
            conf, src, text, s = item[:4]
            repo = f' data-repository="{html.escape(item[4])}"' if len(item) > 4 else ""
            parts.append(
                f'<li data-stance="{STANCE_NAME[s]}" data-confidence="{conf}" data-source="{src}"{repo}>{fmt(text)} '
                f'<span class="confidence">({conf})</span></li>'
            )
        parts.append("</ul>")
    if gaps:
        parts.append('<h4>Gaps</h4><ul class="gaps">')
        parts.extend(f'<li data-status="{GAP_STATUS[code]}">{fmt(text)}</li>' for code, text in gaps)
        parts.append("</ul>")
    parts.append("</div>")
    return "".join(parts)


def write_categories(dataset_id, subcategories, dataset_info):
    """Write the category JSON.

    subcategories: {"P-1": (evidence, gaps), ...} for all 19 ids.
    dataset_info: {"producer": str, "producer_is_repository": bool,
                   "repositories": [{"name": str, "role": "parent" | "child" | "producer site"}]}.
    """
    points = read_points()
    repos = [f'{r["name"]} ({r["role"]})' for r in dataset_info["repositories"]]
    data = {}
    for group, ids in CATEGORY_IDS.items():
        data[group] = {}
        for sid in ids:
            evidence, gaps = subcategories[sid]
            data[group][sid] = div(sid, evidence, gaps, points[sid], repos if group == "repo_resilience" else None)
    data["dataset"] = dataset_info

    out = PIPELINE / "output" / "categories" / dataset_id / f"{dataset_id}_rstar-categories.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(out.relative_to(PIPELINE.parent))
    for sid, (evidence, gaps) in subcategories.items():
        counts = {n: sum(1 for e in evidence if STANCE_NAME[e[3]] == n) for n in ("for", "against", "context")}
        sc, basis = score(evidence, points[sid])
        print(f"  {sid:7} {len(evidence):2} items {counts}  score {sc} ({basis})")
