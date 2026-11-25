/* Precipitation workshop dataset dashboard.
 *
 * Loads the dataset JSON, builds one card per dataset, and wires up search,
 * filters and the expandable detail panels. The current search, filters
 * and open cards are kept in the URL query string, so a reload (or coming
 * back from a future dataset page) shows the dashboard as it was.
 */

// DATA_PATH, ARCHIVES_PATH, escapeHtml and the archive helpers are in
// shared.js, which index.html loads first.

// Archives that have their own page (from data/archives.json). Filled in
// by init(); stays empty if that file can't be loaded.
let archives = [];

// Website for each archive name (from data/archive_links.json), e.g.
// { "NOAA NCEI": "https://www.ncei.noaa.gov/" }. A blank or missing
// address shows as a "#" placeholder link.
let archiveLinks = {};

// Field names in datasets.json, in one place so a renamed field is a
// one-line change. Each dataset also has an "access_endpoints" list of
// { name, url, role } objects (role: primary, alternative or mirror).
const COL = {
  name: "name",
  archive: "data_archive",
  basis: "precipitation_basis",
  period: "period_of_record",
  cdr: "formal_cdr",
  update: "update_status",
  coverage: "spatial_coverage",
  resolution: "resolution",
  frequency: "temporal_frequency",
  curator: "curator",
  doi: "doi",
  notes: "notes",
  // Address of the dataset's "Dataset web research" page (optional; set by
  // rstar-pipeline/processing/scripts/dashboard/import_dataset_pages.py). Without it the panel shows NA.
  about: "about_url",
  // Address of the dataset's overview page (optional; set by
  // rstar-pipeline/processing/scripts/dashboard/import_dataset_overviews.py). Without it the panel shows NA.
  overview: "overview_url",
};

// Fields shown in the metadata grid of the detail panel, in order.
// The data archive(s) have their own table below the grid.
const METADATA_FIELDS = [
  ["Period of record", COL.period],
  ["Spatial coverage", COL.coverage],
  ["Resolution", COL.resolution],
  ["Temporal frequency", COL.frequency],
  ["Formal CDR status", COL.cdr],
  ["Curator", COL.curator],
  ["DOI", COL.doi],
];

// One metadata value as HTML: archive names may link to archive pages,
// a DOI becomes a doi.org link.
function metadataValueHtml(col, value) {
  const e = escapeHtml;
  if (!value) return "NA";
  if (col === COL.doi) {
    const url = /^https?:\/\//.test(value) ? value : `https://doi.org/${value}`;
    return `<a href="${e(url)}">${e(value)}</a>`;
  }
  return e(value);
}

/* ---------- Derived categories ----------
 * The data has no category field, so the data-source type and coverage
 * are worked out from the text. The first matching rule wins.
 */

const CATEGORIES = [
  { id: "merged", label: "Merged / blended",
    test: r => /\b(blend|merged)/i.test(r[COL.basis]) },
  { id: "reanalysis", label: "Reanalysis",
    test: r => /reanalysis/i.test(r[COL.basis] + " " + r[COL.cdr]) },
  { id: "satellite", label: "Satellite",
    test: r => /satellite|microwave|\bIR\b/i.test(r[COL.basis]) },
  { id: "gauge", label: "Gauge-based",
    test: () => true },
];

const COVERAGES = [
  { id: "conus", label: "CONUS",
    test: t => /united states|\bCONUS\b/i.test(t) },
  { id: "north-america", label: "North America",
    test: t => /north america|canada/i.test(t) },
  { id: "global-land", label: "Global land",
    test: t => /^(global )?land\b/i.test(t) && !/ocean/i.test(t) },
  { id: "quasi-global", label: "Quasi-global",
    test: t => /quasi|near-global|\d+°S\s*[-–]\s*\d+°N/i.test(t) && !/90°S/.test(t) },
  { id: "global", label: "Global",
    test: () => true },
];

function categoryOf(row) {
  return CATEGORIES.find(c => c.test(row));
}

function coverageOf(row) {
  return COVERAGES.find(c => c.test(row[COL.coverage]));
}

function isFormalCDR(row) {
  return /^yes/i.test((row[COL.cdr] || "").trim());
}

// Short "start–end" label for the period-of-record tag, e.g. "1979–present".
// Start is the first year mentioned (the main record is listed first);
// the full text is in the detail panel.
function shortPeriod(text) {
  text = text || "";
  const years = (text.match(/\b(1[89]\d\d|20\d\d)\b/g) || []).map(Number);
  if (years.length === 0) return text;
  const start = years[0];
  const ongoing = /present|onward|ongoing|most recent/i.test(text);
  const end = ongoing ? "present" : Math.max(...years);
  return start === end ? String(start) : `${start}–${end}`;
}

/* ---------- Rendering ---------- */

const pad3 = n => String(n).padStart(3, "0");

// Link text for an endpoint: the address without "https://" or a trailing "/".
const displayUrl = url => url.replace(/^https?:\/\//, "").replace(/\/$/, "");

// The "Data archive(s)" section: a table with one row per archive name.
// "Archive" links to the archive's website (from archive_links.json; "#"
// until the address is filled in). "About" links to the archive's own
// page when there is one ("NA" otherwise); that link carries only this
// card as the open card (see archiveHref).
function archivesTableHtml(text, datasetId) {
  const e = escapeHtml;
  const names = splitArchiveNames(text);
  const rows = names.length === 0
    ? `
      <tr><td>NA</td><td>NA</td></tr>`
    : names.map(name => {
        const url = archiveLinks[name] || "#";
        const archive = findArchive(archives, name);
        const about = archive
          ? `<a class="archive-link" data-archive="${e(archive.id)}" data-dataset="${e(datasetId)}"
               href="${e(archiveHref(archive.id, datasetId))}">About archive</a>`
          : "NA";
        return `
      <tr>
        <td><a href="${e(url)}">${e(name)}</a></td>
        <td>${about}</td>
      </tr>`;
      }).join("");
  return `
          <div class="section-divider"></div>

          <h4 class="details-heading caps">Data archive(s)</h4>
          <table class="endpoints-table archives-table">
            <thead>
              <tr><th scope="col">Archive</th><th scope="col">About</th></tr>
            </thead>
            <tbody>${rows}
            </tbody>
          </table>`;
}

// Address of an archive page, carrying the dashboard's search and filters
// so its "Back to dashboard" link returns here as things were. Links in a
// dataset panel pass that dataset's id, and only that card is sent as
// open; the "R* metadata" links send every open card.
function archiveHref(id, datasetId) {
  const p = new URLSearchParams(dashboardQuery(location.search));
  if (datasetId) p.set("open", datasetId);
  const back = p.toString();
  return `archive.html?id=${encodeURIComponent(id)}${back ? `&${back}` : ""}`;
}

// Link to a dataset's about page (its about_url or overview_url). A page
// on this site (dataset.html, overview.html) gets
// the search and filters, with only this card as the open card, so its
// "Back to dashboard" returns here; other addresses are used as they are.
function aboutHref(url, datasetId) {
  if (!/^[\w-]+\.html\?/.test(url)) return url;
  const p = new URLSearchParams(dashboardQuery(location.search));
  p.set("open", datasetId);
  return `${url}&${p}`;
}

// The "R* scores" block on the right half of a card's header. A dataset in the R* data
// (data/rstar-data.js, built by rstar-pipeline/processing/scripts/site-data/build_data.py; same dataset ids as datasets.json) links to
// its R* score page, carrying the dashboard state like the panel's links; one not categorized yet says
// so under the link. A dataset that isn't in the R* data at all shows "R* scores: NA", not a link.
// The link sits above the title button's click area (see .card-rstar in dashboard.css), so clicking it
// follows the link instead of opening the card.
function rstarScoresHtml(datasetId) {
  const e = escapeHtml;
  const entry = ((window.RSTAR_DATA || {}).datasets || []).find(d => d.id === datasetId);
  if (!entry) {
    return `
      <div class="card-rstar">
        <p class="card-rstar-na">R* scores: NA</p>
        <p class="card-rstar-note">Not scored yet</p>
      </div>`;
  }
  const url = `scores.html?dataset=${encodeURIComponent(datasetId)}`;
  return `
      <div class="card-rstar">
        <a class="dataset-about-link card-rstar-link" data-about="${e(url)}" data-dataset="${e(datasetId)}"
           href="${e(aboutHref(url, datasetId))}">R* scores<span class="card-rstar-arrow" aria-hidden="true"> →</span></a>
        ${entry.categorizations ? "" : '<p class="card-rstar-note">Not categorized yet</p>'}
      </div>`;
}

function endpointsHtml(endpoints) {
  const e = escapeHtml;
  if (!endpoints || endpoints.length === 0) return "";
  const rows = endpoints.map(ep => `
      <tr>
        <td>${e(ep.name)}</td>
        <td><a href="${e(ep.url)}" target="_blank" rel="noopener noreferrer">${e(displayUrl(ep.url))}<span class="visually-hidden"> (opens in a new tab)</span></a></td>
      </tr>`).join("");
  return `
          <div class="section-divider"></div>

          <h4 class="details-heading caps">Data access endpoints</h4>
          <table class="endpoints-table">
            <thead>
              <tr><th scope="col">Name</th><th scope="col">Link address</th></tr>
            </thead>
            <tbody>${rows}
            </tbody>
          </table>`;
}

function cardHtml(ds) {
  const r = ds.row;
  const e = escapeHtml;
  const panelId = `details-${ds.id}`;

  const metadata = METADATA_FIELDS.map(([label, col]) => `
    <div class="metadata-item">
      <dt>${e(label)}</dt>
      <dd>${metadataValueHtml(col, r[col])}</dd>
    </div>`).join("");

  return `
  <article class="dataset-card" id="dataset-${ds.id}" data-id="${ds.id}">
    <div class="dataset-header">
      <div class="dataset-number">Dataset ${pad3(ds.number)} / ${e(ds.category.label)}</div>
      <h3 class="dataset-title">
        <button class="dataset-toggle" type="button"
                aria-expanded="false" aria-controls="${panelId}">${e(r[COL.name])}</button>
      </h3>
      <p class="dataset-description">${e(r[COL.basis])}</p>
      <div class="dataset-tags">
        <span class="tag tag-${ds.category.id}">${e(ds.category.label)}</span>
        <span class="tag tag-slate">${e(ds.coverage.label)}</span>
        <span class="tag tag-neutral">${e(shortPeriod(r[COL.period]))}</span>
        ${ds.cdr ? '<span class="tag tag-cdr">NOAA CDR</span>' : ""}
      </div>
${rstarScoresHtml(ds.id)}
      <svg class="expand-icon" viewBox="0 0 24 24" aria-hidden="true">
        <g class="icon-open"><line x1="12" y1="4" x2="12" y2="20"/><line x1="4" y1="12" x2="20" y2="12"/></g>
        <polyline class="icon-close" points="5,15 12,8 19,15"/>
      </svg>
    </div>

    <div class="dataset-details" id="${panelId}">
      <div class="details-inner">
        <div class="details-content">
          <h4 class="details-heading caps">Dataset</h4>
          <p class="details-description dataset-full-name">${e(r[COL.name])}</p>
          <p class="details-description">${r[COL.overview]
            ? `<a class="dataset-about-link" data-about="${e(r[COL.overview])}" data-dataset="${e(ds.id)}"
                 href="${e(aboutHref(r[COL.overview], ds.id))}">Dataset overview</a>`
            : "<strong>Dataset overview:</strong> NA"}</p>
          <p class="details-description">${r[COL.about]
            ? `<a class="dataset-about-link" data-about="${e(r[COL.about])}" data-dataset="${e(ds.id)}"
                 href="${e(aboutHref(r[COL.about], ds.id))}">Dataset web research</a>`
            : "<strong>Dataset web research:</strong> NA"}</p>

          <h5 class="details-heading details-subheading">Update status</h5>
          <p class="details-description">${e(r[COL.update] || "NA")}</p>

          <div class="section-divider"></div>

          <h4 class="details-heading caps">Dataset metadata</h4>
          <dl class="metadata-grid">${metadata}</dl>
${archivesTableHtml(r[COL.archive], ds.id)}

          <div class="section-divider"></div>

          <h4 class="details-heading caps">Notes</h4>
          <p class="details-description">${e(r[COL.notes] || "NA")}</p>
${endpointsHtml(r.access_endpoints)}
        </div>
      </div>
    </div>
  </article>`;
}

function filterButtonsHtml(groupName, options, datasets) {
  const all = `<button type="button" class="filter-button" data-group="${groupName}"
     data-value="all" aria-pressed="true">All datasets<span class="filter-count">${datasets.length}</span></button>`;
  const rest = options
    .map(o => ({ ...o, n: datasets.filter(d => d[groupName].id === o.id).length }))
    .filter(o => o.n > 0)
    .map(o => `<button type="button" class="filter-button" data-group="${groupName}"
       data-value="${o.id}" aria-pressed="false">${escapeHtml(o.label)}<span class="filter-count">${o.n}</span></button>`)
    .join("");
  return all + rest;
}

/* ---------- State (kept in the URL) ---------- */

// Each filter group holds a set of selected option ids; an empty set
// means "All datasets". Options in one group combine with OR, and the
// two groups combine with AND.
const FILTER_GROUPS = ["category", "coverage"];

const state = { search: "", category: new Set(), coverage: new Set(), open: new Set() };

const listParam = value => (value || "").split(",").filter(Boolean);

function readStateFromUrl() {
  const p = new URLSearchParams(location.search);
  state.search = p.get("q") || "";
  FILTER_GROUPS.forEach(g => { state[g] = new Set(listParam(p.get(g))); });
  state.open = new Set(listParam(p.get("open")));
}

function writeStateToUrl() {
  const p = new URLSearchParams();
  if (state.search) p.set("q", state.search);
  FILTER_GROUPS.forEach(g => { if (state[g].size) p.set(g, [...state[g]].join(",")); });
  if (state.open.size) p.set("open", [...state.open].sort().join(","));
  const qs = p.toString();
  history.replaceState(null, "", qs ? `?${qs}` : location.pathname);
  document.querySelectorAll(".archive-link").forEach(a => {
    a.href = archiveHref(a.dataset.archive, a.dataset.dataset);
  });
  document.querySelectorAll(".dataset-about-link").forEach(a => {
    a.href = aboutHref(a.dataset.about, a.dataset.dataset);
  });
}

/* ---------- Behaviour ---------- */

function applyFilters(datasets) {
  const terms = state.search.toLowerCase().split(/\s+/).filter(Boolean);
  let shown = 0;

  datasets.forEach(ds => {
    const visible =
      FILTER_GROUPS.every(g => state[g].size === 0 || state[g].has(ds[g].id)) &&
      terms.every(t => ds.searchText.includes(t));
    ds.card.hidden = !visible;
    if (visible) shown++;
  });

  document.getElementById("datasetCount").textContent =
    `${String(shown).padStart(2, "0")} OF ${datasets.length} DATASETS`;
  document.getElementById("noResults").hidden = shown > 0;

  document.querySelectorAll(".filter-button").forEach(btn => {
    const selected = state[btn.dataset.group];
    const pressed = btn.dataset.value === "all"
      ? selected.size === 0
      : selected.has(btn.dataset.value);
    btn.setAttribute("aria-pressed", String(pressed));
  });

  writeStateToUrl();
}

function setExpanded(card, expanded) {
  card.classList.toggle("expanded", expanded);
  card.querySelector(".dataset-toggle").setAttribute("aria-expanded", String(expanded));
  const id = card.dataset.id;
  if (expanded) state.open.add(id); else state.open.delete(id);
}

// Text the search box matches against: every text field, plus the
// endpoint names and addresses.
function searchTextOf(row) {
  const fields = Object.values(row).filter(v => typeof v === "string");
  const endpoints = (row.access_endpoints || []).flatMap(ep => [ep.name, ep.url]);
  return [...fields, ...endpoints].join(" ").toLowerCase();
}

// Scroll to the card with dataset id `id` and put keyboard focus on its
// title. If the search or filters hide that card, they are cleared first.
function jumpToCard(datasets, id, searchInput) {
  const target = datasets.find(ds => ds.id === id);
  if (!target) return;
  if (target.card.hidden) {
    state.search = "";
    searchInput.value = "";
    FILTER_GROUPS.forEach(g => state[g].clear());
    applyFilters(datasets);
  }
  target.card.scrollIntoView({ block: "start" });
  target.card.querySelector(".dataset-toggle").focus({ preventScroll: true });
}

async function init() {
  const list = document.getElementById("datasetList");

  let rows;
  try {
    rows = (await fetchJson(DATA_PATH)).datasets;
  } catch (err) {
    list.innerHTML = loadErrorHtml(DATA_PATH, err);
    return;
  }

  // Archive pages are extra: without archives.json the archive names
  // just show as plain text.
  try {
    archives = (await fetchJson(ARCHIVES_PATH)).archives;
  } catch {
    archives = [];
  }
  try {
    archiveLinks = (await fetchJson(ARCHIVE_LINKS_PATH)).archive_links || {};
  } catch {
    archiveLinks = {};
  }

  const datasets = rows.map((row, i) => ({
    // Card links and the URL use the dataset's id, so they keep pointing
    // at the same dataset when datasets are added, removed or re-sorted.
    // The number is only the "Dataset 001" label on the card.
    id: row.id,
    number: i + 1,
    row,
    category: categoryOf(row),
    coverage: coverageOf(row),
    cdr: isFormalCDR(row),
    searchText: searchTextOf(row),
  }));
  datasets.forEach(ds => {
    ds.searchText += " " + [ds.category.label, ds.coverage.label, ds.cdr ? "noaa cdr" : ""]
      .join(" ").toLowerCase();
  });

  document.getElementById("totalCount").textContent = `${datasets.length} DATASETS`;
  document.getElementById("categoryFilters").innerHTML =
    filterButtonsHtml("category", CATEGORIES, datasets);
  document.getElementById("coverageFilters").innerHTML =
    filterButtonsHtml("coverage", COVERAGES, datasets);

  // "R* metadata" row: one link per archive or instrument page. The archive-link class
  // makes writeStateToUrl() keep the href carrying the dashboard state.
  if (archives.length) {
    document.getElementById("rstarLinks").innerHTML = archives.map(a =>
      `<li><a class="archive-link" data-archive="${escapeHtml(a.id)}"
         href="${escapeHtml(archiveHref(a.id))}">${escapeHtml(a.name)} — about this ${a.kind === "instrument" ? "instrument" : "archive"}</a></li>`
    ).join("");
    document.getElementById("rstarGroup").hidden = false;
  }

  list.innerHTML = datasets.map(cardHtml).join("") +
    `<p class="status-message" id="noResults" hidden>
       No datasets match the current search and filters.</p>`;
  datasets.forEach(ds => {
    ds.card = list.querySelector(`[data-id="${ds.id}"]`);
  });

  // Restore state from the URL. A "#dataset-<id>" hash (used by the links on
  // the archive page) scrolls to that card; read it now, because
  // writeStateToUrl() rewrites the address without it.
  readStateFromUrl();
  // Drop open-card ids that match no dataset (e.g. card numbers such as
  // "21" left in old bookmarks from before ids were used), so they stop
  // riding along in the archive-page links.
  const knownIds = new Set(datasets.map(ds => ds.id));
  state.open = new Set([...state.open].filter(id => knownIds.has(id)));
  const jumpTo = (location.hash.match(/^#dataset-([a-z0-9-]+)$/) || [])[1];
  const searchInput = document.getElementById("searchInput");
  searchInput.value = state.search;
  datasets.forEach(ds => {
    if (state.open.has(ds.id)) setExpanded(ds.card, true);
  });
  applyFilters(datasets);
  jumpToCard(datasets, jumpTo, searchInput);

  // Search
  searchInput.addEventListener("input", () => {
    state.search = searchInput.value.trim();
    applyFilters(datasets);
  });

  // Filter buttons (one listener for both groups). An option button
  // toggles that option; "All datasets" clears the group's selections.
  document.querySelector(".filter-section").addEventListener("click", ev => {
    const btn = ev.target.closest(".filter-button");
    if (!btn) return;
    const selected = state[btn.dataset.group];
    const value = btn.dataset.value;
    if (value === "all") selected.clear();
    else if (selected.has(value)) selected.delete(value);
    else selected.add(value);
    applyFilters(datasets);
  });

  // Expand / collapse dataset cards
  list.addEventListener("click", ev => {
    // Archive websites not filled in yet (href="#"): don't jump to the top.
    if (ev.target.closest('a[href="#"]')) {
      ev.preventDefault();
      return;
    }
    const toggle = ev.target.closest(".dataset-toggle");
    if (!toggle) return;
    const card = toggle.closest(".dataset-card");
    setExpanded(card, !card.classList.contains("expanded"));
    writeStateToUrl();
  });
}

init();
