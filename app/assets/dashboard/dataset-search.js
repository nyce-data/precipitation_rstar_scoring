/* Search box on the dataset web research pages (dataset.html).
 *
 * It searches every research part of this one dataset (not the other
 * datasets, not the dashboard): each part's question, "Searched on" list
 * and answer text, split into sections at the answer's headings. A
 * section matches when it holds every word typed (case doesn't matter,
 * and part words count, so "fund" finds "funding"), the same rule as the
 * dashboard search. Link addresses are not searched, only their text.
 *
 * Results show in place of the page, grouped by part, one line per
 * section with a snippet; "Sources" sections are listed last. A result
 * opens that part at the section, with the words highlighted. The words
 * are kept in the URL as "rq" (research query), next to the dashboard's
 * own parameters.
 *
 * Loaded before dataset.js, which calls setupResearchSearch(); it uses
 * helpers from dataset.js (partFile, loadQuestions, pageHref, $).
 */

const SEARCH_MIN_LENGTH = 2;

const searchTerms = query => query.toLowerCase().split(/\s+/).filter(Boolean);

const escapeRegExp = s => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

// One pattern for all the words, longest first so "funding" wins over "fund".
function termsPattern(terms) {
  const sorted = [...new Set(terms)].sort((a, b) => b.length - a.length);
  return new RegExp(sorted.map(escapeRegExp).join("|"), "gi");
}

// Text as HTML with each match wrapped in <mark>.
function highlightHtml(text, pattern) {
  let html = "";
  let last = 0;
  for (const m of text.matchAll(pattern)) {
    html += escapeHtml(text.slice(last, m.index)) + `<mark>${escapeHtml(m[0])}</mark>`;
    last = m.index + m[0].length;
  }
  return html + escapeHtml(text.slice(last));
}

/* ---------- Index: every section of every part ---------- */

const HEADING_LINE = /^(#{1,6})\s+(.*?)\s*#*\s*$/;

// The answer's sections. Text before the first heading is the
// "Introduction"; its link has no #section, so it opens at the top.
function answerSections(markdown) {
  const idFor = markdownHeadingIds();   // same ids the page's headings get
  const sections = [];
  let current = { heading: "Introduction", id: "", raw: "" };
  for (const line of markdown.split("\n")) {
    const h = line.match(HEADING_LINE);
    if (h) {
      sections.push(current);
      current = { heading: markdownPlainText(h[2]).trim(), id: idFor(h[2]), raw: "" };
    } else {
      current.raw += line + "\n";
    }
  }
  sections.push(current);
  return sections
    .map(s => ({ heading: s.heading, id: s.id, text: markdownPlainText(s.raw).replace(/\s+/g, " ").trim() }))
    .filter(s => s.text);
}

async function loadPartIndex(part) {
  const [md, q] = await Promise.all([
    fetch(partFile(part, "md"), { cache: "no-cache" }).then(r => (r.ok ? r.text() : "")).catch(() => ""),
    loadQuestions(part),
  ]);
  const sections = [];
  if (q) {
    sections.push({
      heading: "Question and Searched on",
      id: "research-question",
      text: [q.question, ...(q.searched_on || [])].join(" "),
    });
  }
  sections.push(...answerSections(md));
  return sections.map(s => ({ ...s, part, lower: s.text.toLowerCase(), sources: /^sources\b/i.test(s.heading) }));
}

let researchIndex = null;   // Promise of every section, loaded on first search

function loadResearchIndex(entry) {
  if (!researchIndex) {
    researchIndex = Promise.all(entry.parts.map(loadPartIndex)).then(parts => parts.flat());
  }
  return researchIndex;
}

/* ---------- Searching ---------- */

function countMatches(lower, terms) {
  let n = 0;
  for (const t of new Set(terms)) {
    for (let i = lower.indexOf(t); i >= 0; i = lower.indexOf(t, i + t.length)) n++;
  }
  return n;
}

// About 250 characters around the first match, cut at spaces.
function snippet(section, terms, pattern) {
  const first = Math.min(...terms.map(t => section.lower.indexOf(t)).filter(i => i >= 0));
  let start = Math.max(0, first - 90);
  let end = Math.min(section.text.length, first + 160);
  if (start > 0) start = section.text.indexOf(" ", start) + 1 || start;
  if (end < section.text.length) end = section.text.lastIndexOf(" ", end) > first ? section.text.lastIndexOf(" ", end) : end;
  const text = section.text.slice(start, end);
  return `${start > 0 ? "… " : ""}${highlightHtml(text, pattern)}${end < section.text.length ? " …" : ""}`;
}

function resultsHtml(entry, names, query, sections) {
  const terms = searchTerms(query);
  const pattern = termsPattern(terms);
  const hits = sections
    .filter(s => terms.every(t => s.lower.includes(t)))
    .map(s => ({ ...s, count: countMatches(s.lower, terms) }));

  const byPart = entry.parts
    .map(part => ({
      part,
      hits: hits.filter(h => h.part === part).sort((a, b) => a.sources - b.sources),
    }))
    .filter(g => g.hits.length);

  const pages = byPart.length;
  const summary = hits.length
    ? `Found in ${hits.length} ${hits.length === 1 ? "section" : "sections"} on ${pages} ${pages === 1 ? "page" : "pages"}`
    : `No matches for “${query}” in the ${names.short} web research`;

  const groups = byPart.map(({ part, hits: list }) => `
    <section class="search-group" aria-labelledby="search-part-${part.part}">
      <h3 id="search-part-${part.part}"><a href="${escapeHtml(pageHref(part, { rq: query }))}">${escapeHtml(part.topic)}</a></h3>
      <ul class="search-hits">${list.map(h => `
        <li>
          <a class="search-hit-link" href="${escapeHtml(pageHref(part, { rq: query, hash: h.id }))}">${escapeHtml(h.heading)}</a>
          <span class="search-hit-count">${h.count} ${h.count === 1 ? "match" : "matches"}</span>
          <p class="search-snippet">${snippet(h, terms, pattern)}</p>
        </li>`).join("")}
      </ul>
    </section>`).join("");

  return {
    summary,
    html: `
    <div class="prose dataset-prose search-results">
      <h2>Search results</h2>
      <p class="search-summary">${escapeHtml(summary)}</p>
      ${groups}
    </div>`,
  };
}

/* ---------- Highlighting on a part's page ---------- */

function highlightMatches(root, query) {
  const terms = searchTerms(query);
  if (!terms.length) return;
  const pattern = termsPattern(terms);
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) {
    pattern.lastIndex = 0;
    if (pattern.test(walker.currentNode.nodeValue)) nodes.push(walker.currentNode);
  }
  nodes.forEach(node => {
    const span = document.createElement("span");
    span.innerHTML = highlightHtml(node.nodeValue, pattern);
    node.replaceWith(...span.childNodes);
  });
  root.querySelectorAll("mark").forEach(m => m.classList.add("search-hit"));
}

function clearHighlights(root) {
  root.querySelectorAll("mark.search-hit").forEach(m => m.replaceWith(m.textContent));
  root.normalize();
}

/* ---------- The search box ---------- */

// showResultsNow: on the summary page a query in the URL shows its
// results at once; on a part's page the page shows (highlighted) until
// the reader edits the search.
function setupResearchSearch(entry, names, { showResultsNow }) {
  const input = $("researchSearch");
  const results = $("searchResults");
  const content = $("pageContent");
  const status = $("searchStatus");

  input.placeholder = `Search the ${names.short} web research…`;
  input.value = researchQuery;

  let timer = 0;
  let shown = "";

  async function run() {
    const query = input.value.trim();
    setResearchQuery(query.length >= SEARCH_MIN_LENGTH ? query : "");
    if (query.length < SEARCH_MIN_LENGTH) {
      results.hidden = true;
      results.innerHTML = "";
      content.hidden = false;
      clearHighlights(content);
      status.textContent = "";
      shown = "";
      return;
    }
    if (query === shown) return;
    shown = query;
    results.setAttribute("aria-busy", "true");
    const sections = await loadResearchIndex(entry);
    if (input.value.trim() !== query) return;   // the reader kept typing
    const { summary, html } = resultsHtml(entry, names, query, sections);
    results.innerHTML = html;
    results.removeAttribute("aria-busy");
    results.hidden = false;
    content.hidden = true;
    status.textContent = summary;
  }

  input.addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(run, 200);
  });

  if (showResultsNow && researchQuery) run();
}
