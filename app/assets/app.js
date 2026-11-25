/* R* categorization viewer: renders the landing page and the category pages
   from window.RSTAR_DATA (built by rstar-pipeline/processing/scripts/site-data/build_data.py). */
(function () {
  "use strict";

  const DATA = window.RSTAR_DATA;
  const body = document.body;
  const main = document.getElementById("main");
  const header = document.getElementById("site-header");

  if (!DATA) {
    main.innerHTML =
      '<p class="notice">No data found. Run <code>python3 rstar-pipeline/processing/scripts/site-data/build_data.py</code> ' +
      "from the project folder, then reload this page.</p>";
    return;
  }

  // ------------------------------------------------------------ helpers
  function el(tag, attrs, children) {
    const node = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (v === null || v === undefined || v === false) continue;
      if (k === "class") node.className = v;
      else if (k === "text") node.textContent = v;
      else if (k.startsWith("on")) node.addEventListener(k.slice(2), v);
      else node.setAttribute(k, v === true ? "" : v);
    }
    for (const c of [].concat(children || [])) {
      if (c === null || c === undefined) continue;
      node.append(c instanceof Node ? c : document.createTextNode(String(c)));
    }
    return node;
  }

  const params = new URLSearchParams(location.search);
  const categorized = DATA.datasets.filter((d) => d.categorizations);
  let dataset =
    DATA.datasets.find((d) => d.id === params.get("dataset")) || categorized[0] || DATA.datasets[0];

  // The dashboard's (index.html) search, filters and open cards. They ride along on every R* link, so "Back to
  // dashboard" returns to it as it was. Same names as DASHBOARD_PARAMS in assets/dashboard/shared.js.
  const DASHBOARD_PARAMS = ["q", "category", "coverage", "open"];

  function dashboardParams() {
    const kept = new URLSearchParams();
    for (const k of DASHBOARD_PARAMS) if (params.get(k)) kept.set(k, params.get(k));
    return kept;
  }

  function withDataset(href) {
    const [path, hash] = href.split("#");
    const p = dashboardParams();
    p.set("dataset", dataset.id);
    return `${path}?${p}${hash ? "#" + hash : ""}`;
  }

  // The dashboard with this dataset's card open (added to any already open) and scrolled to.
  function dashboardHref() {
    const p = dashboardParams();
    const open = new Set((p.get("open") || "").split(",").filter(Boolean));
    open.add(dataset.id);
    p.set("open", [...open].sort().join(","));
    return `index.html?${p}#dataset-${encodeURIComponent(dataset.id)}`;
  }

  function weightLabel(cat) {
    if (cat.weight == null) return "";
    const pct = Math.round(cat.weight * 100) + "% of R*";
    return cat.key === "repo_resilience" ? pct + " (scored as 100 − total)" : pct;
  }

  function subHtml(catKey, subId) {
    const c = dataset.categorizations;
    if (!c || !c[catKey]) return null;
    return c[catKey][subId] ?? null;
  }

  // Count evidence items and gaps in a subcategory's HTML.
  function coverage(html) {
    if (html === null) return { status: "none", evidence: 0, gaps: 0 };
    const tpl = document.createElement("template");
    tpl.innerHTML = html;
    const evidence = tpl.content.querySelectorAll("ul.evidence > li").length;
    const gaps = tpl.content.querySelectorAll("ul.gaps > li").length;
    const status = evidence === 0 ? "empty" : evidence <= 3 ? "thin" : "filled";
    return { status, evidence, gaps };
  }

  function coverageText(cov) {
    if (cov.status === "none") return "Not categorized yet for this dataset";
    if (cov.status === "empty")
      return cov.gaps ? `No evidence found · ${cov.gaps} gap${cov.gaps === 1 ? "" : "s"}` : "No evidence found";
    const e = `${cov.evidence} evidence item${cov.evidence === 1 ? "" : "s"}`;
    return cov.gaps ? `${e} · ${cov.gaps} gap${cov.gaps === 1 ? "" : "s"}` : e;
  }

  // ------------------------------------------------------------- scores
  // Scores come from data-score on each subcategory's div (rstar-pipeline/input/framework/how_to_score_rstar.md);
  // build_data.py adds the group totals and R*. "NA" means a person has to decide.
  const STATUS_LABELS = {
    found: "Found",
    "searched-none-found": "Searched, none found",
    "not-public": "Not public",
    "not-searched": "Not searched",
  };
  // The score the web evidence implies, and why. "score = 35" uses the subcategory's full points.
  const BASIS_TEXT = {
    "for-only": (pts) => `High or moderate “for” web evidence and no “against” web evidence: score = ${pts ?? "full points"}`,
    "against-only": () => "High or moderate “against” web evidence and no “for” web evidence: score = 0",
    both: () => "Both “for” and “against” web evidence (high or moderate): score = NA",
    none: () => "No high or moderate “for” or “against” web evidence: score = NA",
  };

  function basisText(basis, points) {
    return BASIS_TEXT[basis] ? BASIS_TEXT[basis](points) : "";
  }

  function isNA(v) {
    return v === "NA" || v === null || v === undefined;
  }

  function scoreValue(v, extraClass) {
    return el("span", { class: `score-value ${isNA(v) ? "na" : "num"} ${extraClass || ""}`.trim(), text: isNA(v) ? "NA" : String(v) });
  }

  function subScore(subId) {
    return dataset.scores ? dataset.scores.subcategories[subId] : null;
  }

  function datasetInfo() {
    return (dataset.categorizations && dataset.categorizations.dataset) || null;
  }

  // ------------------------------------------------------ chosen scores
  // After reading the evidence, a person picks each subcategory's score: full points, 0 or NA.
  // Choices live in this browser's localStorage until they are saved to a file, in the shape
  // { "<dataset id>": { "P-1": 35, "P-2": 0, "P-3": "NA", ... } }. A subcategory with no choice
  // uses its research score.
  const STORE_KEY = "rstar-chosen-scores-v1";
  // Notes per subcategory: { "<dataset id>": { "P-1": "text", ... } }.
  const NOTES_KEY = "rstar-notes-v1";
  // Who is scoring: { name, email, role }. Remembered so a scorer types it once.
  const ASSESSOR_KEY = "rstar-assessor-v1";
  // The last file saved per dataset: { "<dataset id>": { timestamp, filename, state } }.
  const SAVES_KEY = "rstar-last-save-v1";
  const STORAGE_KEYS = [STORE_KEY, NOTES_KEY, ASSESSOR_KEY, SAVES_KEY];
  const memory = {}; // used when localStorage is unavailable (for example, some private windows)

  function readKey(key) {
    try {
      const saved = JSON.parse(localStorage.getItem(key));
      return saved && typeof saved === "object" ? saved : {};
    } catch {
      return memory[key] || {};
    }
  }

  function writeKey(key, value) {
    memory[key] = value;
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {
      /* keep the in-memory copy */
    }
  }

  const readStore = () => readKey(STORE_KEY);
  const writeStore = (all) => writeKey(STORE_KEY, all);

  function datasetNotes() {
    return readKey(NOTES_KEY)[dataset.id] || {};
  }

  function setNote(subId, text) {
    const all = readKey(NOTES_KEY);
    const mine = { ...(all[dataset.id] || {}) };
    if (text.trim()) mine[subId] = text;
    else delete mine[subId];
    all[dataset.id] = mine;
    writeKey(NOTES_KEY, all);
  }

  function researchScore(subId) {
    const e = subScore(subId);
    return e ? e.score : "NA";
  }

  function scoreOptions(sub) {
    return [sub.points, 0, "NA"].filter((v, i, a) => v !== null && v !== undefined && a.indexOf(v) === i);
  }

  function chosenScore(sub) {
    const choice = (readStore()[dataset.id] || {})[sub.id];
    return choice !== undefined && scoreOptions(sub).includes(choice) ? choice : researchScore(sub.id);
  }

  function setChoice(sub, value) {
    const all = readStore();
    all[dataset.id] = { ...(all[dataset.id] || {}), [sub.id]: value };
    writeStore(all);
  }

  // Clear the choices for these subcategories (one category, or all of them) so they use the web evidence scores.
  function clearChoices(subIds) {
    const all = readStore();
    const mine = { ...(all[dataset.id] || {}) };
    subIds.forEach((id) => delete mine[id]);
    if (Object.keys(mine).length) all[dataset.id] = mine;
    else delete all[dataset.id];
    writeStore(all);
  }

  function changedCount() {
    return DATA.categories
      .flatMap((c) => c.subcategories)
      .filter((s) => chosenScore(s) !== researchScore(s.id)).length;
  }

  // Group totals and R* from the chosen scores, the same way build_data.py works them out from the
  // research scores: a total is NA if any of its subcategories is NA, and R* is NA if any total is.
  function currentScores() {
    if (!dataset.scores) return null;
    const subs = {};
    const groups = {};
    for (const cat of DATA.categories) {
      const values = cat.subcategories.map((s) => (subs[s.id] = chosenScore(s)));
      const known = values.filter((v) => !isNA(v));
      groups[cat.key] = {
        total: known.length === values.length ? known.reduce((a, b) => a + b, 0) : "NA",
        scored: known.length,
        of: values.length,
        max_points: cat.subcategories.reduce((a, s) => a + (s.points || 0), 0),
      };
    }
    let rstar = "NA";
    if (DATA.categories.every((c) => !isNA(groups[c.key].total))) {
      const sum = DATA.categories.reduce((acc, c) => {
        const t = groups[c.key].total;
        return acc + c.weight * (c.key === "repo_resilience" ? 100 - t : t);
      }, 0);
      rstar = Math.round(sum * 10) / 10;
    }
    return { rstar, groups, subcategories: subs };
  }

  // What a category adds to R*: weight × raw total, or for repository resilience weight × (100 − raw total).
  // Rounded to one decimal, like R*. NA when the raw total is NA.
  function categoryContribution(cat, total) {
    if (isNA(total)) return "NA";
    return Math.round(cat.weight * (cat.key === "repo_resilience" ? 100 - total : total) * 10) / 10;
  }

  function contributionRule(cat) {
    const w = cat.weight.toFixed(2);
    return cat.key === "repo_resilience" ? `${w} × (100 − raw total)` : `${w} × raw total`;
  }

  // ------------------------------------------------------- saved files
  // One JSON file per save, in the format of the colleague's R* form (rstar-pipeline/input/framework/assessment-form/example_rstar_json.json)
  // plus an "assessor" block. NA is saved as null. Plan: notes/rstar-score-json-save-plan.md.
  const COMPONENT_ORDER = ["D", "P", "RRS", "DIRS"];
  const ROLES = [
    ["expert", "Expert"],
    ["workshop_participant", "Workshop participant"],
    ["workshop_group", "Workshop group"],
  ];

  function factorKey(title) {
    return title.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "");
  }

  function triageTier(rstar) {
    if (isNA(rstar)) return null;
    if (rstar >= 70) return "Mirror now";
    if (rstar >= 40) return "Stabilize and mirror";
    return "Monitor";
  }

  const round2 = (x) => Math.round(x * 100) / 100;

  // The chosen scores and notes, to tell whether anything changed since the last save.
  function saveState() {
    const s = currentScores();
    return JSON.stringify({ scores: s ? s.subcategories : null, notes: datasetNotes() });
  }

  function buildAssessment(assessor, now) {
    const s = currentScores();
    const m = dataset.meta || {};
    const notes = datasetNotes();
    const components = {};
    for (const prefix of COMPONENT_ORDER) {
      const cat = DATA.categories.find((c) => c.prefix === prefix);
      const total = s.groups[cat.key].total;
      const raw = isNA(total) ? null : total;
      const factors = {};
      for (const sub of cat.subcategories) {
        const v = s.subcategories[sub.id];
        factors[factorKey(sub.title)] = {
          condition: sub.title,
          present: isNA(v) ? null : v > 0,
          points: isNA(v) ? null : v,
          maxPoints: sub.points,
        };
      }
      components[prefix] = {
        label: cat.title,
        definition: cat.definition,
        rawScore: raw,
        weight: cat.weight,
        weightedContribution:
          raw === null ? null : round2(cat.weight * (cat.key === "repo_resilience" ? 100 - raw : raw)),
        scoringMethod: "",
        justification: cat.subcategories
          .filter((sub) => notes[sub.id] && notes[sub.id].trim())
          .map((sub) => `${sub.id}: ${notes[sub.id].trim()}`)
          .join("\n"),
        factors,
      };
    }
    return {
      assessmentTimestamp: now.toISOString(),
      dataset: { name: dataset.name, identifier: m.identifier || "" },
      primaryDataCurator: { name: m.curator || "", email: "" },
      assessor: { name: assessor.name.trim(), email: (assessor.email || "").trim(), role: assessor.role || "" },
      rStarCompositeScore: isNA(s.rstar) ? null : s.rstar,
      triageTier: triageTier(s.rstar),
      formula: DATA.form ? DATA.form.formula : "",
      components,
      framework: DATA.form ? DATA.form.framework : {},
    };
  }

  // ghcn-daily_rstar_jane-smith_2026-11-23T232937Z.json (no colons: some systems refuse them in file names).
  function saveFileName(assessor, now) {
    const who =
      assessor.name
        .toLowerCase()
        .normalize("NFKD")
        .replace(/[̀-ͯ]/g, "")
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-+|-+$/g, "") || "scorer";
    const stamp = now.toISOString().replace(/\.\d+Z$/, "Z").replace(/:/g, "");
    return `${dataset.id}_rstar_${who}_${stamp}.json`;
  }

  function downloadJson(obj, filename) {
    const blob = new Blob([JSON.stringify(obj, null, 2) + "\n"], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = el("a", { href: url, download: filename, hidden: true });
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  function naCount() {
    const s = currentScores();
    return s ? Object.values(s.subcategories).filter(isNA).length : 0;
  }

  // ------------------------------------------------------------- header
  function renderHeader() {
    const current = body.dataset.category;
    const nav = el("nav", { class: "cat-nav", "aria-label": "Pages" }, [
      el("a", {
        href: withDataset("scores.html"),
        "aria-current": body.dataset.page === "scores" ? "page" : null,
        text: "R* score",
      }),
      ...DATA.categories.map((c) =>
        el("a", { href: withDataset(c.page), "aria-current": c.key === current ? "page" : null, text: c.title })
      ),
      el("a", {
        href: withDataset("graph.html"),
        "aria-current": body.dataset.page === "graph" ? "page" : null,
        text: "Score graph",
      }),
    ]);
    const select = el(
      "select",
      { id: "dataset-select" },
      DATA.datasets.map((d) =>
        el(
          "option",
          { value: d.id, selected: d.id === dataset.id },
          d.categorizations ? d.name : `${d.name} (not categorized yet)`
        )
      )
    );
    select.addEventListener("change", () => {
      dataset = DATA.datasets.find((d) => d.id === select.value);
      const url = new URL(location.href);
      url.searchParams.set("dataset", dataset.id);
      history.replaceState(null, "", url);
      render();
    });
    // Laid out like the dashboard's header band (assets/dashboard/dashboard.css): a label row, the site name, a
    // rule, then the page links.
    header.replaceChildren(
      el("div", { class: "header-top" }, [
        el("a", { class: "back-link", href: dashboardHref() }, [
          el("span", { "aria-hidden": "true", text: "← " }),
          "Back to dashboard",
        ]),
        el("span", { class: "header-label", text: "Precipitation workshop / R* scores" }),
      ]),
      el("div", { class: "rstar-bar" }, [
        el("a", { class: "brand", href: withDataset("scores.html") }, [el("span", { text: "R*" }), " Scores"]),
        el("div", { class: "dataset-picker" }, [el("label", { for: "dataset-select", text: "Dataset" }), select]),
      ]),
      el("div", { class: "header-divider" }),
      nav
    );
  }

  // ------------------------------------------------------------ landing
  function datasetStrip() {
    const m = dataset.meta || {};
    const fields = [
      ["Archive", m.data_archive],
      ["Curator", m.curator],
      ["DOI", m.doi],
      ["Period", m.period_of_record],
      ["Updates", m.update_status],
    ].filter(([, v]) => v);
    const info = datasetInfo();
    return el("section", { class: "dataset-strip", "aria-label": "Dataset details" }, [
      el("h2", { text: dataset.name }),
      dataset.categorizations
        ? null
        : el("p", { class: "notice", text: "This dataset has no categorization file yet." }),
      fields.length
        ? el("dl", {}, fields.map(([k, v]) => el("div", {}, [el("dt", { text: k }), el("dd", { text: v })])))
        : null,
      info && info.producer_is_repository
        ? el("p", { class: "same-org" }, [
            el("strong", { text: "The producer and repository are the same organization" }),
            `: ${info.producer}. Its funding and staff facts appear in several subcategories.`,
          ])
        : null,
    ]);
  }

  // The key: what the tags mean and how scores are set.
  function keySection() {
    const table = (caption, head, rows) =>
      el("table", { class: "key-table" }, [
        el("caption", { text: caption }),
        el("thead", {}, el("tr", {}, head.map((h) => el("th", { scope: "col", text: h })))),
        el("tbody", {}, rows.map((r) => el("tr", {}, r.map((c, i) => el(i === 0 ? "th" : "td", i === 0 ? { scope: "row", text: c } : { text: c }))))),
      ]);
    return el("section", { class: "key", "aria-labelledby": "key-title" }, [
      el("h2", { id: "key-title", text: "How to read the tags and scores" }),
      el("div", { class: "key-grid" }, [
        table("Tags on each evidence item", ["Tag", "Values", "Meaning"], [
          ["Stance", "For, Against, Context", "How the item bears on the subcategory description. Context is background that is not directly tied to the dataset, or doesn't show the description true or false."],
          ["Confidence", "High, moderate, low", "How well the source supports the item. Inferences are always low."],
          ["Status", "Found; searched, none found; not public; not searched", "Every evidence item is found. Each gap gets one of the other three."],
          ["Repository", "Repository name", "Repository resilience items only: which repository the item is about."],
        ]),
        table("How a subcategory is scored", ["High or moderate evidence", "Score"], [
          ["“For” items and no “against” items", "Full points"],
          ["“Against” items and no “for” items", "0"],
          ["Both “for” and “against” items", "NA"],
          ["None: only context, only low confidence, or no evidence", "NA"],
        ]),
      ]),
      el("p", {
        class: "key-note",
        text:
          "Low-confidence and context items stay in the evidence but don't set a score. NA means there isn't enough " +
          "information and a person has to decide. A category total is NA if any of its subcategories is NA, and R* is " +
          "NA if any category total is NA. For repository resilience, “for” means resilient, so a higher score lowers R*.",
      }),
    ]);
  }

  // R* and the four category totals, with a panel listing every subcategory score.
  function scoreSection() {
    const s = currentScores();
    if (!s) return null;
    const changed = changedCount();
    const tiles = [
      el("div", { class: "score-tile total" }, [
        el("span", { class: "score-label", text: "R*" }),
        scoreValue(s.rstar, "big"),
        el("span", { class: "score-note", text: "0.40 D + 0.30 P + 0.20 (100 − RRS) + 0.10 DIRS" }),
      ]),
      ...DATA.categories.map((cat) => {
        const g = s.groups[cat.key];
        return el("div", { class: "score-tile" }, [
          el("span", { class: "score-label", text: cat.title }),
          scoreValue(g.total),
          el("span", {
            class: "score-note",
            text: `${g.scored} of ${g.of} subcategories scored · out of ${g.max_points} points`,
          }),
        ]);
      }),
    ];

    const tables = DATA.categories.map((cat) =>
      el("table", { class: "score-table" }, [
        el("caption", {}, [cat.title, " · total ", scoreValue(s.groups[cat.key].total, "small")]),
        el("thead", {}, el("tr", {}, ["Subcategory", "Statement", "Points", "Score"].map((h) => el("th", { scope: "col", text: h })))),
        el(
          "tbody",
          {},
          cat.subcategories.map((sub) => {
            return el("tr", {}, [
              el("th", { scope: "row" }, el("a", { href: withDataset(`${cat.page}#${sub.id}`), text: sub.id })),
              el("td", { text: sub.title }),
              el("td", { text: sub.points != null ? String(sub.points) : "—" }),
              el("td", {}, scoreValue(s.subcategories[sub.id], "small")),
            ]);
          })
        ),
      ])
    );

    const details = el("div", { class: "score-details", id: "score-details", role: "region", "aria-labelledby": "score-details-btn", hidden: true }, tables);
    const btn = el("button", {
      class: "details-toggle",
      id: "score-details-btn",
      type: "button",
      "aria-expanded": "false",
      "aria-controls": "score-details",
    });
    btn.innerHTML = CHEVRON;
    btn.append(el("span", { text: "Score details" }));
    btn.addEventListener("click", () => {
      const open = btn.getAttribute("aria-expanded") !== "true";
      btn.setAttribute("aria-expanded", String(open));
      details.hidden = !open;
    });

    return el("section", { class: "score-panel", "aria-labelledby": "score-title" }, [
      el("h2", { id: "score-title", text: `R* score for ${dataset.name}` }),
      el("p", {
        class: "score-intro",
        text:
          "Each subcategory starts with the score worked out from the web research evidence. After reading it on " +
          "the category page, you can set it to full points, 0 or NA; your choices are saved in this browser. NA " +
          "marks a score that still needs a decision.",
      }),
      el("p", {
        class: "score-intro changed-count",
        text:
          changed === 0
            ? "All scores are the web evidence scores."
            : `You changed ${changed} of ${Object.keys(s.subcategories).length} subcategory scores from the web evidence scores.`,
      }),
      el("div", { class: "score-row" }, tiles),
      el("div", { class: "score-actions" }, [
        btn,
        resetAllButton(),
        el("a", { class: "graph-link", href: withDataset("graph.html"), text: "See the score graph →" }),
      ]),
      details,
      savePanel(),
    ]);
  }

  // Resets every category's scores for this dataset to the web evidence scores (notes are kept).
  function resetAllButton() {
    const changed = changedCount();
    const reset = el("button", { class: "btn", type: "button", text: "Reset scores", disabled: changed === 0 });
    reset.addEventListener("click", () => {
      const n = changedCount();
      const ask =
        `Reset ${n} changed score${n === 1 ? "" : "s"} in all categories for ${dataset.name} ` +
        "to the web evidence scores? Your notes are kept.";
      if (!window.confirm(ask)) return;
      clearChoices(DATA.categories.flatMap((c) => c.subcategories.map((s) => s.id)));
      render();
      document.getElementById("score-details-btn").focus();
    });
    return reset;
  }

  function formatTime(iso) {
    return new Date(iso).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
  }

  // Name, email and role, then a button that downloads the scores as a JSON file.
  function savePanel() {
    const who = readKey(ASSESSOR_KEY);
    const field = (id, label, input, hint) =>
      el("div", { class: "field" }, [el("label", { for: id, text: label }), hint || null, input]);

    const nameError = el("p", { class: "field-error", id: "assessor-name-error", hidden: true, text: "Enter your name to save." });
    const nameIn = el("input", {
      id: "assessor-name",
      type: "text",
      autocomplete: "name",
      required: true,
      "aria-describedby": "assessor-name-error",
    });
    const emailIn = el("input", { id: "assessor-email", type: "email", autocomplete: "email" });
    const roleIn = el(
      "select",
      { id: "assessor-role" },
      [el("option", { value: "", text: "Choose a role" }), ...ROLES.map(([v, t]) => el("option", { value: v, text: t }))]
    );
    nameIn.value = who.name || "";
    emailIn.value = who.email || "";
    roleIn.value = who.role || "";

    const remember = () =>
      writeKey(ASSESSOR_KEY, { name: nameIn.value, email: emailIn.value, role: roleIn.value });
    [nameIn, emailIn].forEach((i) => i.addEventListener("input", remember));
    roleIn.addEventListener("change", remember);
    nameIn.addEventListener("input", () => {
      if (nameIn.value.trim()) {
        nameError.hidden = true;
        nameIn.removeAttribute("aria-invalid");
      }
    });

    const na = naCount();
    const total = Object.keys(currentScores().subcategories).length;
    const naNote = na
      ? el("p", {
          class: "na-note",
          text:
            `NA values are included: ${na} of ${total} subcategories are NA. They are saved as null, and so is ` +
            "each category total that has an NA, and R* if any total is NA.",
        })
      : null;

    const lastLine = el("p", { class: "save-last" });
    const status = el("p", { class: "save-status", role: "status" });

    function showLast() {
      const last = readKey(SAVES_KEY)[dataset.id];
      if (!last) {
        lastLine.textContent = "Not saved yet from this browser.";
        return;
      }
      lastLine.textContent =
        `Last saved ${formatTime(last.timestamp)} as ${last.filename}.` +
        (last.state !== saveState() ? " You have changes since then." : "");
    }

    const saveBtn = el("button", { class: "btn primary", type: "button", text: "Save scores to a file" });
    saveBtn.addEventListener("click", () => {
      if (!nameIn.value.trim()) {
        nameError.hidden = false;
        nameIn.setAttribute("aria-invalid", "true");
        nameIn.focus();
        return;
      }
      const now = new Date();
      const assessor = { name: nameIn.value, email: emailIn.value, role: roleIn.value };
      const filename = saveFileName(assessor, now);
      downloadJson(buildAssessment(assessor, now), filename);
      const saves = readKey(SAVES_KEY);
      saves[dataset.id] = { timestamp: now.toISOString(), filename, state: saveState() };
      writeKey(SAVES_KEY, saves);
      showLast();
      status.textContent =
        `Saved ${filename} to your downloads.` + (na ? ` NA values are included (${na} of ${total}).` : "");
    });
    showLast();

    return el("section", { class: "save-panel", "aria-labelledby": "save-title" }, [
      el("h3", { id: "save-title", text: "Save your scores" }),
      el("p", {
        class: "score-intro",
        text:
          "Saves this dataset's scores and your notes as a JSON file on your computer, with the date and time. " +
          "Each save makes a new file, so earlier ones are kept. Send the file to the person collecting the scores.",
      }),
      el("div", { class: "save-fields" }, [
        field("assessor-name", "Your name (required)", nameIn),
        field("assessor-email", "Email (optional)", emailIn),
        field("assessor-role", "Role", roleIn),
      ]),
      nameError,
      naNote,
      el("div", { class: "save-actions" }, [saveBtn, lastLine]),
      status,
    ]);
  }

  function renderLanding() {
    const cards = DATA.categories.map((cat) => {
      const chips = cat.subcategories.map((s) => {
        const cov = coverage(subHtml(cat.key, s.id));
        return el("li", {}, [
          el(
            "a",
            {
              class: "chip",
              href: withDataset(`${cat.page}#${s.id}`),
              title: `${s.id}: ${s.title} — ${coverageText(cov)}`,
            },
            [
              el("span", { class: `dot ${cov.status}`, "aria-hidden": "true" }),
              s.id,
              el("span", { class: "sr-only", text: `(${coverageText(cov)})` }),
            ]
          ),
        ]);
      });
      return el("article", { class: "cat-card" }, [
        el("h2", {}, el("a", { href: withDataset(cat.page), text: cat.heading })),
        el("span", { class: "weight", text: weightLabel(cat) }),
        el("p", { text: cat.definition }),
        el("ul", { class: "chips", "aria-label": `${cat.title} subcategories` }, chips),
        el("a", { class: "cat-link", href: withDataset(cat.page) }, `Open ${cat.title} →`),
      ]);
    });

    main.replaceChildren(
      el("h1", { text: "R* Scores" }),
      el("p", {
        class: "lede",
        text:
          "Web research on each dataset, sorted into the R* subcategories. Pick a category to read " +
          "the evidence behind each subcategory, or click a subcategory chip to jump straight to it.",
      }),
      datasetStrip(),
      scoreSection(),
      keySection(),
      el("div", { class: "cat-grid" }, cards),
      el("p", { class: "legend" }, [
        el("span", {}, [el("span", { class: "dot filled" }), "4+ evidence items"]),
        el("span", {}, [el("span", { class: "dot thin" }), "1–3 items"]),
        el("span", {}, [el("span", { class: "dot empty" }), "no evidence"]),
        el("span", {}, [el("span", { class: "dot none" }), "not categorized"]),
      ])
    );
    document.title = "R* Scores";
  }

  // ----------------------------------------------------------- category
  const CHEVRON =
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>';

  // Each evidence item may carry data-stance: how it bears on the subcategory's description.
  const STANCES = {
    for: { label: "For", title: "Supports the subcategory description" },
    against: { label: "Against", title: "Contradicts the subcategory description" },
    context: { label: "Context", title: "Background: not directly tied to the dataset, or doesn't show the description true or false" },
  };
  const STANCE_ORDER = ["for", "against", "context"];

  // Sort items for, against, context (keeping their order within a group) and say so above the list.
  function sortAndSummarizeByStance(ul) {
    const items = [...ul.children];
    if (!items.some((li) => STANCES[li.dataset.stance])) return;
    const rank = (li) => {
      const i = STANCE_ORDER.indexOf(li.dataset.stance);
      return i === -1 ? STANCE_ORDER.length : i;
    };
    items
      .map((li, i) => ({ li, i }))
      .sort((a, b) => rank(a.li) - rank(b.li) || a.i - b.i)
      .forEach(({ li }) => ul.append(li));
    const counts = STANCE_ORDER.map((s) => `${items.filter((li) => li.dataset.stance === s).length} ${s}`);
    ul.before(
      el("p", {
        class: "stance-summary",
        text: `Each item is tagged for, against or context toward the description above, and sorted in that order: ${counts.join(" · ")}.`,
      })
    );
  }

  function decoratePanel(panel) {
    // The JSON uses h4 for Evidence and Gaps; on this page they sit under an h2 card title.
    panel.querySelectorAll("h4").forEach((h) => {
      const h3 = el("h3", { text: h.textContent });
      h.replaceWith(h3);
    });
    panel.querySelectorAll("a[href]").forEach((a) => {
      a.target = "_blank";
      a.rel = "noopener noreferrer";
    });
    panel.querySelectorAll("ul.evidence").forEach(sortAndSummarizeByStance);
    panel.querySelectorAll("ul.evidence > li").forEach((li) => {
      const conf = li.dataset.confidence;
      const stance = li.dataset.stance;
      const old = li.querySelector(":scope > span.confidence");
      if (old) old.remove();
      const meta = el("span", { class: "item-meta" });
      if (STANCES[stance])
        meta.append(el("span", { class: `stance ${stance}`, title: STANCES[stance].title, text: STANCES[stance].label }));
      if (conf) meta.append(el("span", { class: `badge ${conf}`, text: `${conf} confidence` }));
      if (li.dataset.repository)
        meta.append(el("span", { class: "repo-tag", text: `Repository: ${li.dataset.repository}` }));
      li.append(meta);
    });
    panel.querySelectorAll("ul.gaps > li").forEach((li) => {
      const label = STATUS_LABELS[li.dataset.status];
      if (label) li.append(" ", el("span", { class: `gap-status ${li.dataset.status}`, text: label }));
    });
  }

  function setOpen(card, open) {
    const btn = card.querySelector(".toggle");
    const panel = card.querySelector(".sub-panel");
    btn.setAttribute("aria-expanded", String(open));
    btn.setAttribute("aria-label", `${open ? "Hide" : "Show"} categorization for ${card.id}`);
    panel.hidden = !open;
    card.classList.toggle("is-open", open);
  }

  // The score the web evidence implies and why; the radios start on that score.
  function scoreWhy(s) {
    const e = subScore(s.id);
    const text = e ? basisText(e.basis, s.points) : "";
    if (!text) return null;
    return el("p", { class: "score-why", id: `score-why-${s.id}`, text });
  }

  // "Your score": radio buttons for full points, 0 and NA. Starts on the web evidence score.
  function scoreChoice(sub) {
    if (!dataset.scores) return null;
    const current = chosenScore(sub);
    const options = scoreOptions(sub).map((v) => {
      const input = el("input", {
        type: "radio",
        name: `score-${sub.id}`,
        value: String(v),
        checked: v === current,
      });
      input.addEventListener("change", () => {
        if (!input.checked) return;
        setChoice(sub, v);
        refreshCategoryPanel();
      });
      return el("label", { class: "choice" }, [input, el("span", { text: isNA(v) ? "NA" : String(v) })]);
    });
    const why = subScore(sub.id) && BASIS_TEXT[subScore(sub.id).basis] ? `score-why-${sub.id}` : null;
    return el("fieldset", { class: "score-choice no-toggle", "aria-describedby": why }, [
      el("legend", {}, ["Your score", el("span", { class: "sr-only", text: ` for ${sub.id}` })]),
      el("div", { class: "choices" }, options),
    ]);
  }

  // "Your notes": inside knowledge or reasons for the score. Saved into the category's "justification".
  function notesBox(sub) {
    if (!dataset.scores) return null;
    const id = `notes-${sub.id}`;
    const area = el("textarea", { id, class: "notes-input", rows: "2", "aria-describedby": `${id}-hint` });
    area.value = datasetNotes()[sub.id] || "";
    area.addEventListener("input", () => setNote(sub.id, area.value));
    return el("div", { class: "notes no-toggle" }, [
      el("label", { for: id }, ["Your notes", el("span", { class: "sr-only", text: ` for ${sub.id}` })]),
      el("p", {
        class: "notes-hint",
        id: `${id}-hint`,
        text: "Optional. Inside knowledge or reasons for your score. Saved in the file with your scores.",
      }),
      area,
    ]);
  }

  // Bring the radios and notes in line with what is stored (after a reset, or a change in another tab).
  function syncChoices() {
    const cat = DATA.categories.find((c) => c.key === body.dataset.category);
    if (!cat) return;
    const notes = datasetNotes();
    for (const sub of cat.subcategories) {
      const current = String(chosenScore(sub));
      document.querySelectorAll(`input[name="score-${sub.id}"]`).forEach((input) => {
        input.checked = input.value === current;
      });
      const area = document.getElementById(`notes-${sub.id}`);
      if (area && area !== document.activeElement) area.value = notes[sub.id] || "";
    }
    refreshCategoryPanel();
  }

  // The category's scores beside its description: every subcategory and the total, kept up to date.
  let refreshCategoryPanel = () => {};

  function categoryScorePanel(cat) {
    if (!dataset.scores) return null;
    const tbody = el("tbody");
    const totalCell = el("td");
    const contribCell = el("td");
    const changedNote = el("p", { class: "cat-scores-note" });
    const live = el("p", { class: "sr-only", "aria-live": "polite" });
    const resetBtn = el("button", { class: "btn small", type: "button", text: "Reset scores" });

    function update(announce) {
      const s = currentScores();
      const g = s.groups[cat.key];
      tbody.replaceChildren(
        ...cat.subcategories.map((sub) =>
          el("tr", {}, [
            el("th", { scope: "row" }, el("a", { href: `#${sub.id}`, text: sub.id })),
            el("td", { text: sub.points != null ? String(sub.points) : "—" }),
            el("td", {}, scoreValue(s.subcategories[sub.id], "small")),
          ])
        )
      );
      totalCell.replaceChildren(scoreValue(g.total, "small"));
      const contrib = categoryContribution(cat, g.total);
      contribCell.replaceChildren(scoreValue(contrib, "small"));
      const changed = cat.subcategories.filter((sub) => chosenScore(sub) !== researchScore(sub.id)).length;
      changedNote.textContent =
        changed === 0
          ? "All are the web evidence scores."
          : `${changed} changed from the web evidence score${changed === 1 ? "" : "s"}.`;
      resetBtn.disabled = changed === 0;
      if (announce)
        live.textContent =
          `${cat.title} raw total: ${isNA(g.total) ? "NA" : g.total} of ${g.max_points}. ` +
          `${cat.title} contribution to R*: ${contrib}.`;
    }

    resetBtn.addEventListener("click", () => {
      // Only this category: the other categories keep their choices.
      clearChoices(cat.subcategories.map((sub) => sub.id));
      syncChoices();
      live.textContent = `Reset to the web evidence scores. ${live.textContent}`;
    });

    refreshCategoryPanel = () => update(true);
    update(false);

    return el("aside", { class: "cat-scores", "aria-labelledby": "cat-scores-title" }, [
      el("h2", { id: "cat-scores-title", text: `${cat.title} scores` }),
      el("table", { class: "score-table compact" }, [
        el("caption", { class: "sr-only", text: `${cat.title} subcategory scores for ${dataset.name}` }),
        el("thead", {}, el("tr", {}, ["Subcategory", "Points", "Score"].map((h) => el("th", { scope: "col", text: h })))),
        tbody,
        el("tfoot", {}, [
          // The category's score before its weight is applied.
          el("tr", {}, [
            el("th", { scope: "row", text: "Raw total" }),
            el("td", { text: String(cat.subcategories.reduce((a, s) => a + (s.points || 0), 0)) }),
            totalCell,
          ]),
          // What it adds to R*; the points column holds the most it can add.
          el("tr", { class: "contribution" }, [
            el("th", { scope: "row", text: `${cat.title} contribution` }),
            el("td", { text: String(Math.round(cat.weight * 100)) }),
            contribCell,
          ]),
        ]),
      ]),
      el("p", {
        class: "cat-scores-note",
        text:
          `The raw total is NA if any subcategory is NA. The contribution is ${contributionRule(cat)}: ` +
          `the part of R* that comes from ${cat.title.toLowerCase()}.`,
      }),
      changedNote,
      resetBtn,
      live,
    ]);
  }

  function repositoryLine() {
    const info = datasetInfo();
    if (!info || !info.repositories || !info.repositories.length) return null;
    const n = info.repositories.length;
    return el("p", { class: "repo-line" }, [
      el("strong", { text: n === 1 ? "One repository" : `${n} repositories` }),
      `: ${info.repositories.map((r) => `${r.name} (${r.role})`).join("; ")}.`,
      n > 1 ? " The score is pooled across them." : "",
    ]);
  }

  function subCard(cat, s) {
    const html = subHtml(cat.key, s.id);
    const cov = coverage(html);
    const panelId = `panel-${s.id}`;
    const titleId = `title-${s.id}`;

    const toggle = el("button", {
      class: "toggle",
      type: "button",
      "aria-expanded": "false",
      "aria-controls": panelId,
      "aria-label": `Show categorization for ${s.id}`,
    });
    toggle.innerHTML = CHEVRON;

    const head = el("div", { class: "sub-head" }, [
      el("div", {}, [
        el("h2", { class: "sub-titleline", id: titleId }, [
          // The spaces keep the accessible name readable ("P-1 No documented ..."); flex ignores them.
          el("span", { class: "sub-id", text: s.id }),
          " ",
          el("span", { class: "sub-title", text: s.title }),
          s.points != null ? " " : null,
          s.points != null ? el("span", { class: "points", text: `${s.points} points` }) : null,
        ]),
        el("div", { class: "sub-text" }, [
          el("div", {}, [el("h3", { text: "Description" }), el("p", { text: s.description || "—" })]),
          el("div", {}, [el("h3", { text: "What counts as evidence" }), el("p", { text: s.what_counts || "—" })]),
        ]),
        scoreWhy(s),
        scoreChoice(s),
        notesBox(s),
        el("p", { class: "coverage" }, [
          el("span", { class: `dot ${cov.status}`, "aria-hidden": "true" }),
          coverageText(cov),
          subScore(s.id) && STATUS_LABELS[subScore(s.id).status] ? ` · Status: ${STATUS_LABELS[subScore(s.id).status]}` : null,
        ]),
        cat.key === "repo_resilience" ? repositoryLine() : null,
      ]),
      toggle,
    ]);

    const panel = el("div", { class: "sub-panel", id: panelId, role: "region", "aria-labelledby": titleId, hidden: true });
    if (cov.status === "none") {
      panel.append(el("p", { class: "panel-empty", text: `${dataset.name} has not been categorized yet.` }));
    } else if (cov.status === "empty" && cov.gaps === 0) {
      panel.append(el("p", { class: "panel-empty", text: "The research had nothing relevant to this subcategory." }));
    } else {
      // Our own generated HTML from rstar-pipeline/output/categories/; not user input.
      panel.innerHTML = html;
      decoratePanel(panel);
    }

    const card = el("li", { class: "sub-card", id: s.id }, [head, panel]);

    // The button is the accessible control; clicking anywhere on the header also toggles,
    // except on a link, the score choices or notes, or when selecting text.
    head.addEventListener("click", (e) => {
      if (e.target.closest("a, .no-toggle")) return;
      if (e.target !== toggle && !toggle.contains(e.target) && String(window.getSelection())) return;
      const open = toggle.getAttribute("aria-expanded") !== "true";
      setOpen(card, open);
      if (open) history.replaceState(null, "", `#${s.id}`);
    });
    return card;
  }

  function renderCategory() {
    const cat = DATA.categories.find((c) => c.key === body.dataset.category);
    if (!cat) {
      main.replaceChildren(el("p", { class: "notice", text: "Unknown category." }));
      return;
    }
    const list = el("ol", { class: "sub-list" }, cat.subcategories.map((s) => subCard(cat, s)));
    const setAll = (open) => list.querySelectorAll(".sub-card").forEach((c) => setOpen(c, open));
    refreshCategoryPanel = () => {};
    const scores = categoryScorePanel(cat);

    main.replaceChildren(
      el("nav", { class: "breadcrumb", "aria-label": "Breadcrumb" }, [
        el("a", { href: withDataset("scores.html"), text: "All categories" }),
        " / ",
        cat.title,
      ]),
      el("h1", { text: cat.heading }),
      el("div", { class: scores ? "cat-intro" : "cat-intro no-scores" }, [
        el("div", {}, [
          el("span", { class: "weight", text: weightLabel(cat) }),
          el("p", { class: "lede", text: cat.definition }),
          ...(cat.definition_more || []).map((t) => el("p", { class: "lede", text: t })),
          el("p", { class: "lede" }, [
            "Showing ",
            el("strong", { text: dataset.name }),
            scores
              ? ". Click a card to see the evidence sorted into it, then choose its score under “Your score”."
              : ". Click a card to see the evidence sorted into it.",
          ]),
        ]),
        scores,
      ]),
      el("div", { class: "toolbar" }, [
        el("button", { class: "btn", type: "button", onclick: () => setAll(true), text: "Expand all" }),
        el("button", { class: "btn", type: "button", onclick: () => setAll(false), text: "Collapse all" }),
      ]),
      list
    );
    document.title = `${cat.title} · R* Scores`;
    openFromHash();
  }

  function openFromHash() {
    const id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    const card = document.getElementById(id);
    if (card && card.classList.contains("sub-card")) {
      setOpen(card, true);
      card.scrollIntoView({ block: "start" });
      card.querySelector(".toggle").focus({ preventScroll: true });
    }
  }

  // The score graph page (assets/graph.js) gets the helpers it needs from here.
  function renderGraph() {
    if (!window.RSTAR_GRAPH) {
      main.replaceChildren(el("p", { class: "notice", text: "The graph script (assets/graph.js) did not load." }));
      return;
    }
    window.RSTAR_GRAPH.render({
      DATA,
      dataset,
      main,
      el,
      isNA,
      withDataset,
      currentScores,
      subScore,
      basisText,
      coverage,
      coverageText,
      subHtml,
      weightLabel,
      triageTier,
      scoreValue,
      CHEVRON,
    });
  }

  function render() {
    renderHeader();
    if (body.dataset.page === "category") renderCategory();
    else if (body.dataset.page === "graph") renderGraph();
    else renderLanding();
  }

  window.addEventListener("hashchange", openFromHash);
  // Show the latest choices when the page comes back from the browser's back/forward cache
  // or another tab changes them.
  window.addEventListener("pageshow", (e) => {
    if (!e.persisted) return;
    if (body.dataset.page === "category") syncChoices();
    else render();
  });
  window.addEventListener("storage", (e) => {
    if (e.key !== null && !STORAGE_KEYS.includes(e.key)) return;
    if (body.dataset.page === "category") syncChoices();
    else render();
  });
  render();
})();
