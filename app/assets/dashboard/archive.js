/* Archive page: archive.html?id=<archive id>[&page=<page id>]
 *
 * Shows the pages listed for one archive in data/archives.json (each a
 * Markdown file under content/), as tabs once there are two or more, and
 * lists the dashboard datasets held in that archive.
 *
 * Entries with "kind": "instrument" (e.g. NOAA Satellites) use the same
 * page, labelled "Instrument", without the dataset list.
 *
 * The dashboard's own parameters (q, category, coverage, open) ride along
 * in this page's URL, so "Back to dashboard" returns to the same search,
 * filters and open cards.
 */

const params = new URLSearchParams(location.search);
const archiveId = params.get("id") || "";
const backQuery = dashboardQuery(location.search);

const $ = id => document.getElementById(id);

// Words for the page's labels, by the entry's "kind" in archives.json.
const KIND_LABELS = {
  archive: { title: "Data archive", noun: "archive" },
  instrument: { title: "Instrument", noun: "instrument" },
};

function formatDate(iso) {
  const d = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });
}

function setPageParam(pageId) {
  const p = new URLSearchParams(location.search);
  p.set("page", pageId);
  history.replaceState(null, "", `?${p}`);
}

/* ---------- Pages and tabs ---------- */

async function showPage(archive, page) {
  const panel = $("archiveContent");
  panel.setAttribute("aria-busy", "true");
  let text;
  try {
    const res = await fetch(page.file, { cache: "no-cache" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    text = await res.text();
  } catch (err) {
    panel.innerHTML = loadErrorHtml(page.file, err);
    panel.removeAttribute("aria-busy");
    return;
  }
  const date = page.as_of
    ? `<p class="page-date">As of <time datetime="${escapeHtml(page.as_of)}">${escapeHtml(formatDate(page.as_of))}</time></p>`
    : "";
  // renderMarkdown escapes the file's text before adding markup.
  panel.innerHTML = `<article class="prose">${date}${renderMarkdown(text, { headingOffset: 1 })}</article>`;
  // Links in the text to another archive page keep the dashboard state,
  // so "Back to dashboard" still returns to the same view from there.
  if (backQuery) {
    panel.querySelectorAll('a[href^="archive.html?"]').forEach(a => {
      a.href = `${a.getAttribute("href")}&${backQuery}`;
    });
  }

  // Under the page's title (its first <h2>): the R* query the research
  // started from, then the research question and what was searched.
  const [query, scope] = await Promise.all([rstarQueryHtml(page), researchScopeHtml(page)]);
  const title = panel.querySelector(".prose h2");
  if (title && (query || scope)) title.insertAdjacentHTML("afterend", query + scope);
  panel.removeAttribute("aria-busy");
}

// The page's "query" file (rstar_query.md, copied in by the import
// script), rendered from Markdown; its "###" heading becomes an <h3>
// under the page title. Returns "" if there is none or it can't load.
async function rstarQueryHtml(page) {
  if (!page.query) return "";
  try {
    const res = await fetch(page.query, { cache: "no-cache" });
    if (!res.ok) return "";
    return `<div class="rstar-query">${renderMarkdown(await res.text())}</div>`;
  } catch {
    return "";
  }
}

// From the page's "record" file (written by rstar-pipeline/processing/scripts/dashboard/import_archive_page.py
// from the research-record.json): the question asked and the
// subquestions searched. Returns "" if the page has no record or it
// can't be loaded.
async function researchScopeHtml(page) {
  if (!page.record) return "";
  let rec;
  try {
    rec = await fetchJson(page.record);
  } catch {
    return "";
  }
  // Headings under the report's <h2> title: "Question" <h3>, "Searched
  // on" <h4>, drawn at the same sizes as on the dataset pages.
  const question = rec.question ? `
    <h3 class="question-heading">Question</h3>
    <p class="research-question">${escapeHtml(rec.question)}</p>` : "";
  const items = rec.searched_on || [];
  const searched = items.length ? `
    <h4 class="searched-on-heading">Searched on</h4>
    <ul class="searched-on">${items.map(q => `<li>${escapeHtml(q)}</li>`).join("")}</ul>` : "";
  return question || searched ? `<div class="research-scope">${question}${searched}</div>` : "";
}

// Tabs follow the WAI-ARIA tabs pattern: the selected tab is the only one
// in the Tab order, and the arrow keys (plus Home/End) move between tabs.
function buildTabs(archive, selected) {
  const tablist = $("archiveTabs");
  const panel = $("archiveContent");
  if (archive.pages.length < 2) return;

  tablist.hidden = false;
  tablist.innerHTML = archive.pages.map(p => `
    <button type="button" role="tab" class="archive-tab" id="tab-${escapeHtml(p.id)}"
            data-page="${escapeHtml(p.id)}" aria-controls="archiveContent">${escapeHtml(p.title)}</button>`).join("");
  panel.setAttribute("role", "tabpanel");

  const tabs = [...tablist.querySelectorAll('[role="tab"]')];

  function select(tab, focus) {
    tabs.forEach(t => {
      const on = t === tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
    });
    panel.setAttribute("aria-labelledby", tab.id);
    if (focus) tab.focus();
    const page = archive.pages.find(p => p.id === tab.dataset.page);
    setPageParam(page.id);
    showPage(archive, page);
  }

  tablist.addEventListener("click", ev => {
    const tab = ev.target.closest('[role="tab"]');
    if (tab) select(tab, false);
  });

  tablist.addEventListener("keydown", ev => {
    const i = tabs.indexOf(document.activeElement);
    if (i < 0) return;
    const next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[ev.key];
    if (next === undefined) return;
    ev.preventDefault();
    select(tabs[(next + tabs.length) % tabs.length], true);
  });

  select(tabs[archive.pages.indexOf(selected)], false);
}

/* ---------- Datasets in this archive ---------- */

// Link to one dataset on the dashboard: the dashboard comes back as it
// was, with this dataset's card also open, and scrolls to that card
// (see jumpToCard in dashboard.js).
function datasetHref(id) {
  const p = new URLSearchParams(backQuery);
  const open = new Set((p.get("open") || "").split(",").filter(Boolean));
  open.add(id);
  p.set("open", [...open].sort().join(","));
  return `index.html?${p}#dataset-${id}`;
}

function showDatasets(archive, rows, archives) {
  const matches = rows
    .filter(row => splitArchiveNames(row.data_archive)
      .some(name => findArchive(archives, name) === archive));

  $("archiveDatasetCount").textContent =
    `${matches.length} ${matches.length === 1 ? "DATASET" : "DATASETS"} ON THE DASHBOARD`;
  if (matches.length === 0) return;

  $("archiveDatasetList").innerHTML = matches.map(row => `
    <li><a href="${escapeHtml(datasetHref(row.id))}">${escapeHtml(row.name)}</a>
      <span class="archive-dataset-archives">${escapeHtml(row.data_archive)}</span></li>`).join("");
  $("archiveDatasets").hidden = false;
}

/* ---------- Start ---------- */

async function init() {
  $("backLink").href = backQuery ? `index.html?${backQuery}` : "index.html";

  let archives;
  try {
    archives = (await fetchJson(ARCHIVES_PATH)).archives;
  } catch (err) {
    $("archiveContent").innerHTML = loadErrorHtml(ARCHIVES_PATH, err);
    return;
  }

  const archive = archives.find(a => a.id === archiveId);
  if (!archive) {
    $("archiveTitle").textContent = "Archive not found";
    $("archiveContent").innerHTML = `<p class="status-message">There is no page for
      the archive <code>${escapeHtml(archiveId || "(none given)")}</code>.
      Use “Back to dashboard” to return to the dataset list.</p>`;
    return;
  }

  const kind = KIND_LABELS[archive.kind] || KIND_LABELS.archive;
  document.title = `${archive.name} — Precipitation Workshop Datasets`;
  $("kindLabel").textContent = `Precipitation workshop / ${kind.title}`;
  $("archiveTabs").setAttribute("aria-label", `Pages about this ${kind.noun}`);
  $("archiveTitle").textContent = archive.name;
  $("archiveFullName").textContent = archive.full_name || "";
  const n = archive.pages.length;
  $("archivePageCount").textContent =
    `${n} ${n === 1 ? "PAGE" : "PAGES"} ABOUT THIS ${kind.noun.toUpperCase()}`;

  const selected = archive.pages.find(p => p.id === params.get("page")) || archive.pages[0];
  if (!selected) {
    $("archiveContent").innerHTML = `<p class="status-message">No pages about this archive yet.</p>`;
  } else if (n > 1) {
    buildTabs(archive, selected);
  } else {
    showPage(archive, selected);
  }

  // The dataset list is extra; the page still works without it.
  // Instruments have no dataset field to match on yet, so no list.
  if (archive.kind === "instrument") return;
  try {
    showDatasets(archive, (await fetchJson(DATA_PATH)).datasets, archives);
  } catch {
    /* leave the dataset section hidden */
  }
}

init();
