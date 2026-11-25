/* A small Markdown-to-HTML renderer for the archive pages.
 *
 * It covers what the research answers use: headings, paragraphs,
 * **bold**, `code`, [links](url), bulleted and numbered lists (nested by
 * indenting two or more spaces) and pipe tables. All text is HTML-escaped
 * before any markup is added, so raw HTML in a file shows as text and
 * can't run. Links are only kept for http(s), mailto and relative
 * addresses.
 *
 * renderMarkdown(text, { headingOffset, headingIds }) returns an HTML
 * string. headingOffset shifts heading levels (1 turns "#" into <h2>),
 * so a page's own <h1> stays the only one. headingIds gives each heading
 * an id from its text (see headingIds below), so links can jump to it.
 *
 * Also exported: markdownPlainText(text), the text without markup or
 * link addresses (used by the dataset research search), and
 * markdownHeadingIds(), which makes the same ids the renderer does.
 */

(function () {
  const esc = s => String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");

  const SAFE_URL = /^(https?:\/\/|mailto:|#|\.{0,2}\/|[\w-]+[\w./-]*(\?|#|$))/i;

  // Inline markup. Code spans and links become placeholders first so the
  // bold rule can't reach into their text or addresses.
  function inline(text) {
    const slots = [];
    const hold = html => `\u0000${slots.push(html) - 1}\u0000`;

    let s = text.replace(/`([^`]+)`/g, (_, code) => hold(`<code>${esc(code)}</code>`));

    s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (whole, label, url) => {
      if (!SAFE_URL.test(url)) return whole;
      const external = /^https?:\/\//i.test(url);
      const attrs = external ? ' target="_blank" rel="noopener noreferrer"' : "";
      const note = external ? '<span class="visually-hidden"> (opens in a new tab)</span>' : "";
      return hold(`<a href="${esc(url)}"${attrs}>${bold(esc(label))}${note}</a>`);
    });

    s = bold(esc(s));
    return s.replace(/\u0000(\d+)\u0000/g, (_, i) => slots[Number(i)]);
  }

  function bold(html) {
    return html.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  }

  const splitRow = line => line.trim().replace(/^\|/, "").replace(/\|$/, "")
    .split("|").map(c => c.trim());
  const isTableSep = line => /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$/.test(line);
  const LIST_ITEM = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/;

  function table(lines) {
    const head = splitRow(lines[0]);
    const body = lines.slice(2).map(splitRow);
    const th = head.map(c => `<th scope="col">${inline(c)}</th>`).join("");
    const rows = body.map(r =>
      `<tr>${head.map((_, i) => `<td>${inline(r[i] || "")}</td>`).join("")}</tr>`).join("\n");
    // The wrapper scrolls sideways on narrow screens; tabindex lets
    // keyboard users scroll it too.
    return `<div class="table-scroll" role="region" aria-label="Table" tabindex="0">
<table><thead><tr>${th}</tr></thead>
<tbody>
${rows}
</tbody></table></div>`;
  }

  // Lists: items are grouped by indentation into nested <ul>/<ol>.
  function list(lines) {
    const items = lines.map(l => {
      const m = l.match(LIST_ITEM);
      if (m) return { indent: m[1].length, ordered: /\d/.test(m[2]), text: m[3] };
      return { cont: l.trim() };   // wrapped continuation of the item above
    });

    let html = "";
    const stack = [];   // open lists: { indent, tag }
    let itemOpen = false;

    for (const it of items) {
      if (it.cont !== undefined) { html += " " + inline(it.cont); continue; }
      while (stack.length && it.indent < stack[stack.length - 1].indent) {
        html += `</li></${stack.pop().tag}>`;
      }
      const top = stack[stack.length - 1];
      if (!top || it.indent > top.indent) {
        const tag = it.ordered ? "ol" : "ul";
        stack.push({ indent: it.indent, tag });
        html += `<${tag}>`;
      } else if (itemOpen) {
        html += "</li>";
      }
      html += `<li>${inline(it.text)}`;
      itemOpen = true;
    }
    while (stack.length) html += `</li></${stack.pop().tag}>`;
    return html;
  }

  // Text without Markdown markup; links keep their label, not the address.
  function plainText(text) {
    return String(text)
      .replace(/\[([^\]]+)\]\([^)\s]+\)/g, "$1")
      .replace(/\*\*|`/g, "")
      .replace(/^\s*\|?\s*:?-{3,}.*$/gm, "")
      .replace(/^\s*#{1,6}\s+/gm, "")
      .replace(/\|/g, " ")
      .replace(/[ \t]+/g, " ");
  }

  // Ids for headings, from their text: "Funding routes and their status"
  // -> "sec-funding-routes-and-their-status"; repeats get "-2", "-3".
  // Call once per page and pass every heading in order.
  function headingIds() {
    const seen = new Map();
    return heading => {
      const base = "sec-" + (plainText(heading).toLowerCase()
        .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "section");
      const n = (seen.get(base) || 0) + 1;
      seen.set(base, n);
      return n === 1 ? base : `${base}-${n}`;
    };
  }

  function renderMarkdown(text, { headingOffset = 0, headingIds: withIds = false } = {}) {
    const lines = text.replace(/\r\n?/g, "\n").split("\n");
    const out = [];
    const idFor = withIds ? headingIds() : null;
    let i = 0;

    while (i < lines.length) {
      const line = lines[i];

      if (!line.trim()) { i++; continue; }

      const h = line.match(/^(#{1,6})\s+(.*?)\s*#*\s*$/);
      if (h) {
        const level = Math.min(6, h[1].length + headingOffset);
        const id = idFor ? ` id="${esc(idFor(h[2]))}"` : "";
        out.push(`<h${level}${id}>${inline(h[2])}</h${level}>`);
        i++;
        continue;
      }

      if (line.includes("|") && i + 1 < lines.length && isTableSep(lines[i + 1])) {
        const block = [];
        while (i < lines.length && lines[i].includes("|")) block.push(lines[i++]);
        out.push(table(block));
        continue;
      }

      if (LIST_ITEM.test(line)) {
        const block = [];
        while (i < lines.length && lines[i].trim() &&
               (LIST_ITEM.test(lines[i]) || /^\s+\S/.test(lines[i]))) {
          block.push(lines[i++]);
        }
        out.push(list(block));
        continue;
      }

      if (/^\s*(-{3,}|\*{3,})\s*$/.test(line)) { out.push("<hr>"); i++; continue; }

      const para = [];
      while (i < lines.length && lines[i].trim() &&
             !/^#{1,6}\s/.test(lines[i]) && !LIST_ITEM.test(lines[i])) {
        para.push(lines[i++].trim());
      }
      out.push(`<p>${inline(para.join(" "))}</p>`);
    }
    return out.join("\n");
  }

  window.renderMarkdown = renderMarkdown;
  window.markdownPlainText = plainText;
  window.markdownHeadingIds = headingIds;
})();
