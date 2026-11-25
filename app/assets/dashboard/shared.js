/* Helpers used by both the dashboard (dashboard.js) and the archive page
 * (archive.js). Loaded first, as a plain script.
 */

const DATA_PATH = "data/datasets.json";
const ARCHIVES_PATH = "data/archives.json";
const ARCHIVE_LINKS_PATH = "data/archive_links.json";
const DATASET_PAGES_PATH = "data/dataset_pages.json";

// Dashboard URL parameters. The archive page passes these back to
// index.html, and drops anything else it was given.
const DASHBOARD_PARAMS = ["q", "category", "coverage", "open"];

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

// "no-cache" makes the browser check for a newer file each time, so an
// edited data file shows up on a normal reload.
async function fetchJson(path) {
  const res = await fetch(path, { cache: "no-cache" });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

// Message shown when a data file can't be loaded (most often because the
// page was opened as a file instead of through a web server).
function loadErrorHtml(path, err) {
  return `<p class="status-message">Could not load <code>${escapeHtml(path)}</code>
      (${escapeHtml(err.message)}).
      Open this page through a local web server started from the <code>app</code> folder,
      for example <code>python3 -m http.server 3000 --bind 127.0.0.1</code>,
      then visit <code>http://127.0.0.1:3000/</code>.</p>`;
}

// The "data_archive" text can name several archives, separated by ";".
const splitArchiveNames = text =>
  String(text || "").split(";").map(s => s.trim()).filter(Boolean);

// The archive (from archives.json) that a name in "data_archive" refers
// to, or undefined if that archive has no page yet.
function findArchive(archives, name) {
  return archives.find(a => (a.data_archive_names || [a.name]).includes(name));
}

// Keep only the dashboard's own parameters from a query string.
function dashboardQuery(search) {
  const from = new URLSearchParams(search);
  const kept = new URLSearchParams();
  DASHBOARD_PARAMS.forEach(k => { if (from.get(k)) kept.set(k, from.get(k)); });
  return kept.toString();
}
