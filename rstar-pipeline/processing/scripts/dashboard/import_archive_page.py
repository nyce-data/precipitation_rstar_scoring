"""Copy a research answer (Markdown) into the dashboard as an archive page.

The answers come from a separate research project and mention files that
only exist there. This script copies one answer into app/content/ and
drops those parts:

  - the closing "Saved in ..." paragraph and anything after it
  - list items that point to the research project's own files
    (see DROP_ITEM_PREFIXES)
  - sentences that name one of those files, e.g. "Each figure's file and
    passage is in `results.csv`." (see RESEARCH_FILES)
  - notes on how a source was read, e.g. "(read via WebFetch)"
    (see scripts/research_text.py)

With --replace OLD NEW (repeatable), each OLD text is replaced by NEW
after cleaning, e.g. to point a link at another dashboard page.

With --record, it also reads the answer's research-record.json and writes
the fields the page shows to a small JSON file next to DEST (same name,
.json ending):

  { "question": <the record's "question">,
    "searched_on": [<each "question" in the record's "subquestions">] }

With --query, it copies the R* query statement the research started from
(rstar_query.md) to DEST's name with a .query.md ending.

Usage (from the project folder):

    python3 rstar-pipeline/processing/scripts/dashboard/import_archive_page.py SOURCE.md DEST.md \
      [--record research-record.json] [--query rstar_query.md] \
      [--replace OLD NEW ...]

Example:

    python3 rstar-pipeline/processing/scripts/dashboard/import_archive_page.py \
      rstar-pipeline/input/web-research/archives/noaa-ncei/2026-11-17_noaa-ncei-threats/answer_A1_Rstar_query_chatgpt-noaa_ncei.md \
      app/content/archives/noaa-ncei/threats-2026-11-17.md \
      --record rstar-pipeline/input/web-research/archives/noaa-ncei/2026-11-17_noaa-ncei-threats/research-record.json \
      --query rstar-pipeline/input/web-research/archives/noaa-ncei/2026-11-17_noaa-ncei-threats/A1_Rstar_query_chatgpt-noaa_ncei.md

After a new page is copied in, add it to the archive's "pages" list in
app/data/archives.json ("file" for the .md, "record" for the .json,
"query" for the .query.md).
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from research_text import strip_tool_notes  # noqa: E402

# A line starting with this ends the content we keep.
STOP_PREFIX = "Saved in "

# List items starting with any of these are dropped.
DROP_ITEM_PREFIXES = (
    "- **Pages to check by hand:**",
    "- **Sites to trust:**",
    "- Pages to check by hand",
    "- **Pages to check by hand.**",
    "- **Sandbox:**",
    "- **Hosts refused.**",
    "- **The token budget ended the research**",  # GPCP pt6, GHCN-D pt3 (user asked 2026-11-20)
    "- [check-by-hand.md](",  # GPCP pt7 (2026-11-27): a link to the research file starts the bullet
    "- [sites-to-trust.md](",
    "- `check-by-hand.md`",  # 2026-11-27: bullets about the research files left "- md` lists …" fragments
    "- `sites-to-trust.md`",
    "- **Earlier copies:**",  # CoCoRaHS pt3, pt4 (2026-11-27): notes on the research project's query_answers copies
    "- **Earlier runs' copies.**",
)

# Files that exist only in the research project. A sentence that names
# one of them (in backticks) is dropped.
RESEARCH_FILES = ("results.csv", "check-by-hand.md", "sites-to-trust.md", "left-out.md", "method.md")
_FILE_SENTENCE = re.compile(
    r"\s*[^.]*`(?:" + "|".join(re.escape(f) for f in RESEARCH_FILES) + r")`(?:[^.(]|\([^)]*\))*\."
)


# A list item's leading "- " and bold label, e.g. "- **Pages not read:** ".
_ITEM_LABEL = re.compile(r"^(\s*(?:[-*]\s+)?(?:\*\*[^*]+\*\*\s*)?)")


def drop_file_sentences(line: str) -> str:
    """Remove the sentences in one line that name a research-project file.

    A list item's "- **Label:**" start is kept when other text remains
    (GHCN-Daily pt1, 2026-11-27: "- **Pages not read:** 3 are listed in
    `check-by-hand.md`. The AMS journal page …" lost its label). If
    nothing but the label is left, the line is emptied as before.
    """
    head = _ITEM_LABEL.match(line).group(1)
    body = line[len(head):]
    cleaned = _FILE_SENTENCE.sub("", body)
    if cleaned == body:
        return line
    cleaned = cleaned.strip()
    return head + cleaned if cleaned else ""


# A list item telling the researcher to check refused hosts against the
# sandbox's allowed domains (2026-11-27: GPCP pt3, IMERG pt3 and pt7,
# PERSIANN pt2). The whole item is about the research setup, so it goes.
_SANDBOX_ITEM = re.compile(r"^\s*[-*]\s.*\byour (?:sandbox's )?allowed domains\b", re.I)


def clean(text: str) -> str:
    kept = []
    for line in text.splitlines():
        if line.startswith(STOP_PREFIX):
            break
        if line.lstrip().startswith(DROP_ITEM_PREFIXES) or _SANDBOX_ITEM.match(line):
            continue
        kept.append(drop_file_sentences(line))
    return strip_tool_notes("\n".join(kept).rstrip() + "\n")


def record_fields(record: dict) -> dict:
    return {
        "question": record["question"],
        "searched_on": [s["question"] for s in record.get("subquestions", [])],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("source", type=Path, help="research answer (.md)")
    parser.add_argument("dest", type=Path, help="where to write it under app/content/")
    parser.add_argument("--record", type=Path, help="the answer's research-record.json")
    parser.add_argument("--query", type=Path, help="the R* query statement (rstar_query.md)")
    parser.add_argument("--replace", nargs=2, action="append", default=[], metavar=("OLD", "NEW"),
                        help="replace OLD with NEW in the copied page (repeatable)")
    args = parser.parse_args()

    cleaned = clean(args.source.read_text(encoding="utf-8"))
    for old, new in args.replace:
        if old not in cleaned:
            print(f"Warning: --replace text not found: {old}", file=sys.stderr)
        cleaned = cleaned.replace(old, new)
    args.dest.parent.mkdir(parents=True, exist_ok=True)
    args.dest.write_text(cleaned, encoding="utf-8")
    print(f"Wrote {args.dest} ({len(cleaned.splitlines())} lines)")

    if args.record:
        fields = record_fields(json.loads(args.record.read_text(encoding="utf-8")))
        out = args.dest.with_suffix(".json")
        out.write_text(json.dumps(fields, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {out} (question + {len(fields['searched_on'])} searched-on items)")

    if args.query:
        out = args.dest.with_suffix(".query.md")
        out.write_text(args.query.read_text(encoding="utf-8").rstrip() + "\n", encoding="utf-8")
        print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
