/* Dataset overview pages: overview.html?id=<dataset id>
 *
 * Shows everything in content/datasets/<id>/overview.json (copied from
 * the user's metadata JSON by rstar-pipeline/processing/scripts/dashboard/import_dataset_overviews.py) as
 * sections: summary, people, time, space, instruments, data format,
 * versions, archives, access, related products and references. Empty
 * fields and sections are left out. Fields the page doesn't know yet are
 * still shown (text and numbers only), labeled from their key, so new
 * metadata appears without a code change.
 *
 * The dashboard's own parameters (q, category, coverage, open) ride along
 * in the URL, so "Back to dashboard" returns to the same search and
 * filters, with this dataset's card open.
 */

const params = new URLSearchParams(location.search);
const datasetId = params.get("id") || "";
const backQuery = dashboardQuery(location.search);

const $ = id => document.getElementById(id);
const e = escapeHtml;

// Dashboard address with this dataset's card open, scrolled to it.
function dashboardHref() {
  const p = new URLSearchParams(backQuery);
  const open = new Set((p.get("open") || "").split(",").filter(Boolean));
  open.add(datasetId);
  p.set("open", [...open].sort().join(","));
  return `index.html?${p}#dataset-${encodeURIComponent(datasetId)}`;
}

/* ---------- Formatting ---------- */

const MONTHS = ["January", "February", "March", "April", "May", "June", "July",
  "August", "September", "October", "November", "December"];

// "1880-01-01" -> "1 January 1880", "1998-01" -> "January 1998",
// "present" -> "Present"; anything else is shown as it is.
function formatDate(value) {
  if (!value) return "";
  if (/^present$/i.test(value)) return "Present";
  const m = /^(\d{4})-(\d{2})(?:-(\d{2}))?$/.exec(value);
  if (!m) return value;
  const month = MONTHS[Number(m[2]) - 1];
  return m[3] ? `${Number(m[3])} ${month} ${m[1]}` : `${month} ${m[1]}`;
}

// "land_ocean" -> "Land ocean", "access-service" -> "Access service"
function humanize(key) {
  const s = String(key).replace(/[_-]+/g, " ").trim();
  return s.charAt(0).toUpperCase() + s.slice(1);
}

const lat = v => (v < 0 ? `${-v}°S` : v > 0 ? `${v}°N` : "0°");
const lon = v => (v < 0 ? `${-v}°W` : v > 0 ? `${v}°E` : "0°");

function extentText(x) {
  if (!x) return "";
  const lats = `${lat(x.lat_min)}–${lat(x.lat_max)}`;
  const lons = x.lon_max > 180 ? `${x.lon_min}°–${x.lon_max}° longitude` : `${lon(x.lon_min)}–${lon(x.lon_max)}`;
  return `${lats}; ${lons}`;
}

function gridText(g) {
  if (!g) return "";
  const parts = [];
  if (g.spacing_deg) parts.push(`${g.spacing_deg}° spacing`);
  if (g.dimensions) parts.push(g.dimensions);
  if (g.type) parts.push(g.type);
  if (g.approx_km) parts.push(`about ${g.approx_km} km`);
  if (g.approx_km_at_equator) parts.push(`about ${g.approx_km_at_equator} km at the equator`);
  return parts.join("; ");
}

/* ---------- HTML pieces ---------- */

// An outside link, opened in a new tab. Only http(s) addresses become
// links; anything else is shown as text.
function extLink(url, text) {
  if (!url || !/^https?:\/\//i.test(url)) return e(text || url || "");
  return `<a href="${e(url)}" target="_blank" rel="noopener noreferrer">${e(text || url)}<span class="visually-hidden"> (opens in a new tab)</span></a>`;
}

const doiLink = doi => (doi ? extLink(`https://doi.org/${doi}`, doi) : "");
const displayAddress = url => url.replace(/^https?:\/\//i, "").replace(/\/$/, "");

const listHtml = items => (items && items.length
  ? `<ul>${items.map(i => `<li>${e(i)}</li>`).join("")}</ul>` : "");
const paragraph = text => (text ? `<p>${e(text)}</p>` : "");

// Label / value table. rows: [label, html]; empty values are left out.
function factsTable(rows, label) {
  const shown = rows.filter(([, html]) => html);
  if (!shown.length) return "";
  return `
    <table class="facts-table" aria-label="${e(label)}">
      <tbody>${shown.map(([k, v]) => `
        <tr><th scope="row">${e(k)}</th><td>${v}</td></tr>`).join("")}
      </tbody>
    </table>`;
}

// Rows for an object's known fields, in the given order, then any other
// text or number fields it has. known: [key, label, format?]
function factRows(obj, known, skip = []) {
  if (!obj) return [];
  const rows = known.map(([key, label, fmt]) =>
    [label, obj[key] == null || obj[key] === "" ? "" : (fmt ? fmt(obj[key]) : e(obj[key]))]);
  const done = new Set([...known.map(k => k[0]), ...skip]);
  Object.entries(obj).forEach(([key, value]) => {
    if (done.has(key)) return;
    if (typeof value === "string" || typeof value === "number") rows.push([humanize(key), e(value)]);
  });
  return rows;
}

// Table with a column for each field that at least one item has.
// columns: [heading, (item) => html]
function dataTable(items, columns, label) {
  if (!items || !items.length) return "";
  const used = columns.filter(([, cell]) => items.some(item => cell(item)));
  return `
    <div class="table-scroll">
      <table aria-label="${e(label)}">
        <thead><tr>${used.map(([h]) => `<th scope="col">${e(h)}</th>`).join("")}</tr></thead>
        <tbody>${items.map(item => `
          <tr>${used.map(([, cell]) => `<td>${cell(item) || ""}</td>`).join("")}</tr>`).join("")}
        </tbody>
      </table>
    </div>`;
}

const field = key => item => (item[key] ? e(item[key]) : "");

/* ---------- Sections ---------- */

function summarySection(m) {
  const id = m.identification || {};
  const status = m.status || {};
  const shortNames = id.short_names
    ? Object.entries(id.short_names).map(([k, v]) => `${humanize(k)}: ${v}`).join("; ") : "";
  const otherDois = (id.other_dois || [])
    .map(d => `${doiLink(d.doi)}${d.issuer ? ` (${e(d.issuer)})` : ""}`).join("<br>");
  const citation = id.citation
    ? `${e(id.citation)}${id.citation_source ? `<br><span class="fact-note">Source: ${extLink(id.citation_source, "dataset metadata page")}</span>` : ""}` : "";

  const facts = factRows(id, [
    ["full_name", "Full name"],
    ["abbreviations", "Also called", v => e(v.join(", "))],
    ["version", "Version"],
    ["dataset_type", "Data type"],
    ["processing_level", "Processing level"],
    ["product", "Product"],
    ["project", "Project"],
    ["data_provider", "Data provider"],
    ["publisher", "Publisher"],
    ["publication_date", "Published", formatDate],
    ["doi", "DOI", doiLink],
    ["doi_note", "About the DOI"],
    ["doi_source", "DOI source", url => extLink(url, displayAddress(url))],
  ], ["description", "doi_url", "short_names", "other_dois", "citation", "citation_source"]);
  facts.splice(3, 0, ["Status", e(status.label || status.state || "")]);
  facts.push(["Short names", e(shortNames)], ["Other DOIs", otherDois], ["How to cite", citation]);

  const evidence = status.evidence && status.evidence.length
    ? `<h3>Why it counts as ${e((status.state || "ongoing").toLowerCase())}</h3>${listHtml(status.evidence)}` : "";

  return paragraph(id.description) + factsTable(facts, "Dataset facts") + paragraph(status.purpose) + evidence;
}

function peopleSection(p) {
  if (!p) return "";
  const c = p.curator || {};
  const curator = c.name
    ? `${e(c.name)}${c.organization && c.organization !== c.name ? `, ${e(c.organization)}` : ""}${c.role ? `<br><span class="fact-note">${e(c.role)}</span>` : ""}`
    : "";
  const contributors = (p.contributors || []).join(", ");
  const facts = factsTable([["Curator", curator], ["Contributors", e(contributors)]], "Curator and contributors");
  const leads = p.leads && p.leads.length
    ? `<h3>Scientific leads</h3>${dataTable(p.leads, [
      ["Name", field("name")], ["Organization", field("organization")], ["Role", field("role")]], "Scientific leads")}`
    : "";
  return facts + leads + paragraph(p.note);
}

function timeSection(t) {
  if (!t) return "";
  const rows = factRows(t, [
    ["start", "Start", formatDate],
    ["start_note", "About the start"],
    ["earliest_observation", "Earliest observation", formatDate],
    ["end", "End", formatDate],
    ["end_note", "About the end"],
    ["frequency", "Frequency"],
    ["input_frequency", "Input frequency"],
    ["accumulation_period", "Accumulation period"],
    ["update_frequency", "Update frequency"],
    ["latency", "Latency"],
    ["record_length", "Record length"],
  ], ["note", "other_frequencies", "latest_data_check"]);
  const check = t.latest_data_check;
  if (check) {
    rows.push(["Latest data", `${e(check.note || "")}${(check.urls || []).map(u =>
      `<br>${extLink(u, displayAddress(u))}`).join("")}`]);
  }
  const other = t.other_frequencies && t.other_frequencies.length
    ? `<h3>Other time steps</h3>${dataTable(t.other_frequencies, [
      ["Time step", field("frequency")], ["Availability", field("availability")]], "Other time steps")}`
    : "";
  return factsTable(rows, "Time") + paragraph(t.note) + other;
}

function spaceSection(s) {
  if (!s) return "";
  return factsTable(factRows(s, [
    ["coverage", "Coverage"],
    ["extent", "Extent", extentText],
    ["land_ocean", "Land or ocean"],
    ["resolution", "Resolution"],
    ["grid", "Grid", gridText],
    ["station_count", "Stations"],
    ["countries", "Countries and territories"],
  ], ["note"]), "Space") + paragraph(s.note);
}

function instrumentsSection(i) {
  if (!i) return "";
  const parts = [paragraph(i.summary)];
  if (i.categories && i.categories.length) {
    parts.push(dataTable(i.categories, [
      ["Instrument or source", field("name")], ["Type", field("type")], ["Role", field("role")]],
    "Instruments"));
  }
  if (i.platforms && i.platforms.length) {
    parts.push(`<h3>Satellites and sensors</h3>${dataTable(i.platforms, [
      ["Platform", field("platform")], ["Instrument", field("instrument")], ["Type", field("type")]],
    "Satellites and sensors")}`);
  }
  if (i.gauge_adjustment) parts.push(factsTable([["Gauge adjustment", e(i.gauge_adjustment)]], "Gauge adjustment"));
  if (i.input_products && i.input_products.length) parts.push(`<h3>Input data products</h3>${listHtml(i.input_products)}`);
  if (i.processing_chain && i.processing_chain.length) {
    parts.push(`<h3>Processing steps</h3><ol>${i.processing_chain.map(s => `<li>${e(s)}</li>`).join("")}</ol>`);
  }
  if (i.legacy_inputs && i.legacy_inputs.items) {
    parts.push(`<h3>Inputs in ${e(i.legacy_inputs.version || "earlier versions")}</h3>${listHtml(i.legacy_inputs.items)}`);
  }
  parts.push(paragraph(i.note));
  return parts.join("");
}

function formatSection(f) {
  if (!f) return "";
  const table = f.formats && f.formats.length
    ? dataTable(f.formats, [
      ["Format", field("format")], ["Extension", item => (item.extension ? `<code>${e(item.extension)}</code>` : "")],
      ["Description", field("description")]], "File formats")
    : "";
  return factsTable(factRows(f, [
    ["format", "Format"], ["variable", "Variable"], ["units", "Units"],
  ], ["formats", "note"]).filter(([label]) => !(table && label === "Format")), "Data format") + table + paragraph(f.note);
}

function versionsSection(v) {
  return dataTable(v, [
    ["Version", field("version")],
    ["Status", item => (item.status ? e(humanize(item.status)) : "")],
    ["DOI", item => doiLink(item.doi)],
    ["Resolution", field("resolution")],
    ["Starts", item => e(formatDate(item.start || ""))],
    ["Note", field("note")],
  ], "Versions");
}

function archivesSection(a) {
  return dataTable(a, [
    ["Archive", field("name")],
    ["Role", item => (item.role ? e(humanize(item.role)) : "")],
    ["Description", field("description")],
  ], "Archives");
}

function endpointNotes(ep) {
  const notes = [];
  if (ep.role === "primary") notes.push("<strong>Primary</strong>");
  if (ep.purpose) notes.push(e(ep.purpose));
  else if (ep.type) notes.push(e(humanize(ep.type)));
  if (ep.details) {
    notes.push(Object.entries(ep.details).map(([k, v]) => `${e(humanize(k))}: ${e(v)}`).join("<br>"));
  }
  return notes.join("<br>");
}

function accessSection(m) {
  const eps = m.access_endpoints || [];
  const columns = [
    ["Name", field("name")],
    ["Link address", ep => extLink(ep.url, displayAddress(ep.url))],
    ["Notes", endpointNotes],
  ];
  const docs = eps.filter(ep => ep.role === "documentation");
  const data = eps.filter(ep => ep.role !== "documentation");
  return paragraph(m.access_note)
    + (data.length ? `<h3>Get the data</h3>${dataTable(data, columns, "Data access endpoints")}` : "")
    + (docs.length ? `<h3>Documentation</h3>${dataTable(docs, columns, "Documentation")}` : "");
}

function relatedSection(r) {
  if (!r || !r.length) return "";
  return `<ul>${r.map(p => `<li><strong>${e(p.name)}</strong>${p.difference ? `: ${e(p.difference)}` : ""}</li>`).join("")}</ul>`;
}

function referencesSection(refs) {
  if (!refs || !refs.length) return "";
  return `<ul class="reference-list">${refs.map(r => {
    const doi = r.doi && !(r.url || "").includes(r.doi) ? ` DOI: ${doiLink(r.doi)}` : "";
    return `<li>${extLink(r.url, r.title)}${doi}</li>`;
  }).join("")}</ul>`;
}

/* ---------- Page ---------- */

function splitName(name) {
  const i = name.indexOf(": ");
  return i < 0 ? { short: name, full: "" } : { short: name.slice(0, i), full: name.slice(i + 2) };
}

function render(meta, row) {
  const names = splitName(row.name);
  document.title = `${names.short}: Overview — Precipitation Workshop Datasets`;
  $("pageTitle").textContent = `${names.short}: Overview`;
  $("pageSubtitle").textContent = names.full;
  const version = meta.identification && meta.identification.version;
  const state = meta.status && meta.status.state;
  $("pageMeta").textContent = [state, version && `Version ${version}`].filter(Boolean).join(" · ").toUpperCase();

  const sections = [
    ["summary", "Summary", summarySection(meta)],
    ["people", "People", peopleSection(meta.people)],
    ["time", "Time", timeSection(meta.temporal)],
    ["space", "Space", spaceSection(meta.spatial)],
    ["instruments", "Instruments and inputs", instrumentsSection(meta.instruments)],
    ["data-format", "Data format", formatSection(meta.data_format)],
    ["versions", "Versions", versionsSection(meta.versions)],
    ["archives", "Archives", archivesSection(meta.archives)],
    ["access", "Data access", accessSection(meta)],
    ["related", "Related products", relatedSection(meta.related_products)],
    ["references", "References", referencesSection(meta.references)],
  ].filter(([, , html]) => html.replace(/<[^>]*>/g, "").trim());

  const research = row.about_url
    ? `<p class="summary-link"><a href="${e(`${row.about_url}${backQuery ? `&${backQuery}` : ""}`)}">${e(names.short)} web research</a></p>`
    : "";
  const toc = `
    <nav class="overview-toc" aria-label="On this page">
      <h2 class="overview-toc-heading">On this page</h2>
      <ul>${sections.map(([id, title]) => `<li><a href="#${id}">${e(title)}</a></li>`).join("")}</ul>
    </nav>`;

  $("pageContent").innerHTML = `
    <div class="prose dataset-prose overview-prose">
      ${research}
      ${toc}
      ${sections.map(([id, title, html]) => `
      <section class="overview-section" aria-labelledby="${id}">
        <h2 id="${id}">${e(title)}</h2>
        ${html}
      </section>`).join("")}
    </div>`;

  // The content arrives after the page loads, so jump to the #section here.
  const target = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (target) target.scrollIntoView();
}

function notFound(message) {
  $("pageTitle").textContent = "Page not found";
  $("pageContent").innerHTML = `<p class="status-message">${message}
    Use “Back to dashboard” to return to the dataset list.</p>`;
}

async function init() {
  $("backLink").href = dashboardHref();

  let datasets;
  try {
    datasets = await fetchJson(DATA_PATH);
  } catch (err) {
    $("pageContent").innerHTML = loadErrorHtml(DATA_PATH, err);
    return;
  }
  const row = datasets.datasets.find(d => d.id === datasetId);
  if (!row || !row.overview_url) {
    notFound(`There is no overview for the dataset
      <code>${e(datasetId || "(none given)")}</code>.`);
    return;
  }

  const file = `content/datasets/${encodeURIComponent(datasetId)}/overview.json`;
  let meta;
  try {
    meta = await fetchJson(file);
  } catch (err) {
    $("pageContent").innerHTML = loadErrorHtml(file, err);
    return;
  }
  render(meta, row);
}

init();
