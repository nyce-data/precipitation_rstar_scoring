/* Dataset web research pages: dataset.html?id=<dataset id>[&part=<N>]
 *
 * Without "part": the summary page, one section per research part (its
 * topic, a link to its page, the question and the "Searched on" list).
 * With "part": that part's page: question, "Searched on", then the
 * answer text, with previous / next links at the bottom.
 *
 * The parts are listed in data/dataset_pages.json; their text is in
 * content/datasets/<id>/pt<N>.md and their questions in pt<N>.json, both
 * written by rstar-pipeline/processing/scripts/dashboard/import_dataset_pages.py.
 *
 * The dashboard's own parameters (q, category, coverage, open) ride along
 * in the URL, so "Back to dashboard" returns to the same search and
 * filters, with this dataset's card open.
 *
 * The search box searches this dataset's research only; see
 * dataset-search.js. Its words are kept in the URL as "rq".
 */

const params = new URLSearchParams(location.search);
const datasetId = params.get("id") || "";
const partParam = params.get("part");
const backQuery = dashboardQuery(location.search);
let researchQuery = (params.get("rq") || "").trim();

const $ = id => document.getElementById(id);

// Dashboard address with this dataset's card open, scrolled to it
// (see jumpToCard in dashboard.js).
function dashboardHref() {
  const p = new URLSearchParams(backQuery);
  const open = new Set((p.get("open") || "").split(",").filter(Boolean));
  open.add(datasetId);
  p.set("open", [...open].sort().join(","));
  return `index.html?${p}#dataset-${encodeURIComponent(datasetId)}`;
}

// Address of the summary page (no part) or of one part, keeping the
// dashboard state; rq carries the research search, hash a section id.
function pageHref(part, { rq = "", hash = "" } = {}) {
  const p = new URLSearchParams({ id: datasetId });
  if (part) p.set("part", String(part.part));
  if (rq) p.set("rq", rq);
  return `dataset.html?${p}${backQuery ? `&${backQuery}` : ""}${hash ? `#${encodeURIComponent(hash)}` : ""}`;
}

// The search box changed: keep its words in the URL, and in the
// previous / next links. With no words, the page's search note goes.
function setResearchQuery(query) {
  if (query === researchQuery) return;
  researchQuery = query;
  const p = new URLSearchParams(location.search);
  if (query) p.set("rq", query); else p.delete("rq");
  history.replaceState(null, "", `?${p}${location.hash}`);
  document.querySelectorAll("a[data-part]").forEach(a => {
    const part = currentEntry.parts.find(x => String(x.part) === a.dataset.part);
    a.href = pageHref(part, { rq: query });
  });
  if (!query) document.querySelectorAll(".search-note").forEach(n => n.remove());
}

let currentEntry = null;

const partFile = (part, ext) =>
  `content/datasets/${encodeURIComponent(datasetId)}/pt${part.part}.${ext}`;

// "GPCP Daily v3.3: Global Precipitation Climatology Project" ->
// short "GPCP Daily v3.3", full "Global Precipitation Climatology Project".
function splitName(name) {
  const i = name.indexOf(": ");
  return i < 0 ? { short: name, full: "" } : { short: name.slice(0, i), full: name.slice(i + 2) };
}

// Question and "Searched on" list. headingTag is the level of the
// "Searched on" heading, so headings stay in order on each page.
function questionsHtml(q, headingTag) {
  if (!q) return "";
  const question = q.question
    ? `<p class="research-question"><strong>Question:</strong> ${escapeHtml(q.question)}</p>`
    : "";
  const items = q.searched_on || [];
  const searched = items.length ? `
    <${headingTag} class="searched-on-heading">Searched on</${headingTag}>
    <ul class="searched-on">${items.map(s => `<li>${escapeHtml(s)}</li>`).join("")}</ul>` : "";
  return question + searched;
}

// On a part's page: a "Question" <h2> with the question as a paragraph,
// then a "Searched on" <h3> and list.
function partQuestionsHtml(q) {
  if (!q) return "";
  const question = q.question ? `
    <h2 class="question-heading">Question</h2>
    <p class="research-question">${escapeHtml(q.question)}</p>` : "";
  const items = q.searched_on || [];
  const searched = items.length ? `
    <h3 class="searched-on-heading">Searched on</h3>
    <ul class="searched-on">${items.map(s => `<li>${escapeHtml(s)}</li>`).join("")}</ul>` : "";
  return question + searched;
}

async function loadQuestions(part) {
  try {
    return await fetchJson(partFile(part, "json"));
  } catch {
    return null;
  }
}

/* ---------- Summary page ---------- */

async function showSummary(entry, names) {
  document.title = `${names.short}: Web research — Precipitation Workshop Datasets`;
  $("pageTitle").textContent = `${names.short}: Web research`;
  const n = entry.parts.length;
  $("pageMeta").textContent = `${n} ${n === 1 ? "PAGE" : "PAGES"} OF WEB RESEARCH`;

  const questions = await Promise.all(entry.parts.map(loadQuestions));
  const sections = entry.parts.map((part, i) => {
    const headingId = `part-${part.part}`;
    return `
    <section class="research-part" aria-labelledby="${headingId}">
      <h2 id="${headingId}">${escapeHtml(part.topic)}</h2>
      <p class="research-part-link"><a href="${escapeHtml(pageHref(part))}">Read the web research: ${escapeHtml(part.topic)}</a></p>
      ${questionsHtml(questions[i], "h3")}
    </section>`;
  }).join("");
  $("pageContent").innerHTML = `<div class="prose dataset-prose">${sections}</div>`;
}

/* ---------- One part's page ---------- */

async function showPart(entry, names, part) {
  const index = entry.parts.indexOf(part);
  document.title = `${names.short}: ${part.topic} — Precipitation Workshop Datasets`;
  $("pageTitle").textContent = `${names.short}: ${part.topic}`;
  $("kindLabel").textContent = "Precipitation workshop / Dataset web research";
  $("pageMeta").textContent = `PART ${index + 1} OF ${entry.parts.length}`;

  const panel = $("pageContent");
  panel.setAttribute("aria-busy", "true");
  let text;
  const file = partFile(part, "md");
  try {
    const res = await fetch(file, { cache: "no-cache" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    text = await res.text();
  } catch (err) {
    panel.innerHTML = loadErrorHtml(file, err);
    panel.removeAttribute("aria-busy");
    return;
  }
  const q = await loadQuestions(part);

  const prev = entry.parts[index - 1];
  const next = entry.parts[index + 1];
  const nav = prev || next ? `
    <nav class="part-nav" aria-label="Other research pages for this dataset">
      ${prev ? `<a class="part-nav-prev" data-part="${prev.part}" href="${escapeHtml(pageHref(prev, { rq: researchQuery }))}"><span aria-hidden="true">←</span> ${escapeHtml(prev.topic)}</a>` : "<span></span>"}
      ${next ? `<a class="part-nav-next" data-part="${next.part}" href="${escapeHtml(pageHref(next, { rq: researchQuery }))}">${escapeHtml(next.topic)} <span aria-hidden="true">→</span></a>` : ""}
    </nav>` : "";

  // Opened from a search result: say what is highlighted, with a way
  // back to the results.
  const note = researchQuery ? `
      <p class="search-note">Matches for “${escapeHtml(researchQuery)}” are highlighted.
        <a href="${escapeHtml(pageHref(null, { rq: researchQuery }))}">Back to search results</a></p>` : "";

  // renderMarkdown escapes the file's text before adding markup. The
  // answer's "##" sections become <h2>s under the page's <h1>, with ids
  // that search results link to.
  panel.innerHTML = `
    <div class="prose dataset-prose">
      <p class="summary-link"><a href="${escapeHtml(pageHref(null))}"><span aria-hidden="true">←</span> Back to ${escapeHtml(names.short)} web research</a></p>
      ${note}
      <div class="research-scope" id="research-question">${partQuestionsHtml(q)}</div>
      <article>${renderMarkdown(text, { headingIds: true })}</article>
      ${nav}
    </div>`;
  panel.removeAttribute("aria-busy");

  if (researchQuery) {
    highlightMatches(panel.querySelector(".research-scope"), researchQuery);
    highlightMatches(panel.querySelector("article"), researchQuery);
  }
  // The text arrives after the page loads, so jump to the #section here:
  // to its first highlighted word if there is one, else its heading.
  const target = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (target) {
    const firstHit = [...panel.querySelectorAll("mark.search-hit")]
      .find(m => target.contains(m) || target.compareDocumentPosition(m) & Node.DOCUMENT_POSITION_FOLLOWING);
    if (firstHit) firstHit.scrollIntoView({ block: "center" });
    else target.scrollIntoView();
  }
}

/* ---------- Start ---------- */

function notFound(message) {
  $("pageTitle").textContent = "Page not found";
  $("pageContent").innerHTML = `<p class="status-message">${message}
    Use “Back to dashboard” to return to the dataset list.</p>`;
}

async function init() {
  $("backLink").href = dashboardHref();

  let pages, datasets;
  try {
    [pages, datasets] = await Promise.all([fetchJson(DATASET_PAGES_PATH), fetchJson(DATA_PATH)]);
  } catch (err) {
    $("pageContent").innerHTML = loadErrorHtml(DATASET_PAGES_PATH, err);
    return;
  }

  const entry = pages.datasets.find(d => d.id === datasetId);
  const row = datasets.datasets.find(d => d.id === datasetId);
  if (!entry || !row) {
    notFound(`There is no web research for the dataset
      <code>${escapeHtml(datasetId || "(none given)")}</code>.`);
    return;
  }

  const names = splitName(row.name);
  $("pageSubtitle").textContent = names.full;
  currentEntry = entry;

  if (partParam === null) {
    showSummary(entry, names);
    setupResearchSearch(entry, names, { showResultsNow: true });
    return;
  }
  const part = entry.parts.find(p => String(p.part) === partParam);
  if (!part) {
    notFound(`${escapeHtml(names.short)} has no research part
      <code>${escapeHtml(partParam)}</code>.`);
    return;
  }
  showPart(entry, names, part);
  setupResearchSearch(entry, names, { showResultsNow: false });
}

init();
