"""Text clean-up shared by the import scripts.

strip_tool_notes(text) removes notes about how the research tool read a
source, which readers don't need, for example:

    [GAO report](https://...) (read via WebFetch)       -> [GAO report](https://...)
    [CEOS deliverable](https://...), WebFetch only      -> [CEOS deliverable](https://...)
    (aggregator, read via extract)                       -> (aggregator)
    ... the Oct 2025 shutdown, read only as a WebFetch extract, says ...
                                                         -> ... the Oct 2025 shutdown says ...

Sentences that discuss the evidence itself (e.g. in a "Gaps" section) are
left alone; run the script with --report to list the lines that still
mention a tool so they can be checked by hand.
"""

import re

# Words that mark a note about how a page was read.
_TOOL = r"(?:WebFetch|extract(?:ion)?|subagent|summary only)"

# One note: "read via WebFetch", "WebFetch only", "read by extraction",
# "read through a WebFetch summary only", "subagent report", "extract", ...
_NOTE = (
    r"(?:read\s+(?:only\s+)?(?:via|by|through|as|from)\s+(?:an?\s+|the\s+)?[^,;().]*?" + _TOOL + r"[^,;().]*"
    r"|WebFetch(?:'s copy)?(?:\s+(?:extract|summary))?(?:\s+only)?"
    r"|(?:WebFetch\s+)?extract(?:ion)?(?:\s+only)?"
    r"|subagent\s+report"
    r"|read\s+via\s+a\s+subagent)"
)

# A whole bracketed note, e.g. " (read via WebFetch)" or " (WebFetch extract)".
_PAREN_NOTE = re.compile(r"\s*\(\s*" + _NOTE + r"\s*\)", re.I)
# A note inside a longer bracket: "(aggregator, read via extract)" ->
# "(aggregator)"; "(read via WebFetch, HTML version)" -> "(HTML version)".
_INNER_AFTER = re.compile(r"(?:,|;)\s*" + _NOTE + r"\s*(?=\))", re.I)
_INNER_BEFORE = re.compile(r"(?<=\()\s*" + _NOTE + r"\s*[,;]\s*", re.I)
# A trailing ", WebFetch only" after a link or at the end of a list item.
_TRAILING_NOTE = re.compile(r",\s*" + _NOTE + r"\s*(?=\.?$|\s*[·;]|\s*\)?\s*$)", re.I)
# A note set off by commas in a sentence: "X, read only as a WebFetch extract, says".
_COMMA_NOTE = re.compile(
    r",\s*read\s+(?:only\s+)?(?:via|by|through|as)\s+(?:an?\s+|the\s+)?[^,;()]*?" + _TOOL + r"[^,;()]*,", re.I)

# "briefings article read as a WebFetch extract; ..." -> "briefings article; ..."
_INLINE_NOTE = re.compile(r"\s+read\s+(?:only\s+)?(?:via|by|through|as)\s+(?:an?\s+)?WebFetch\s+extract(?=[;,)])", re.I)

_MENTION = re.compile(r"WebFetch|subagent|\bextract(?:ion)?\b", re.I)


def strip_tool_notes(text: str) -> str:
    out = []
    for line in text.splitlines():
        line = _COMMA_NOTE.sub("", line)
        line = _INLINE_NOTE.sub("", line)
        line = _PAREN_NOTE.sub("", line)
        line = _INNER_AFTER.sub("", line)
        line = _INNER_BEFORE.sub("", line)
        line = _TRAILING_NOTE.sub("", line)
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def tool_mentions(text: str) -> list[tuple[int, str]]:
    """Lines (number, text) that still name a tool, for checking by hand."""
    return [(i, line) for i, line in enumerate(text.splitlines(), 1) if _MENTION.search(line)]
