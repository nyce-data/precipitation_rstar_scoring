# Plan: evidence nodes on the score graph

Written 2026-11-24. Adds the "information nodes" from `docs/ideas/rstar_relationship_graph/rstar_graphs.md` to the
score graph (`app/graph.html`, `app/assets/graph.js`): one small node per evidence item, around its subcategory
node, with a switch to show or hide them. **Built 2026-11-24** with an on/off switch (the user's choice over a
three-step slider). As built, the rings are 13 px apart (dots 5.5 px) at 48, 61, 74, 87 and 100 px, so rings 1–3 hold
about 18 dots; the switch is also kept in the URL (`&evidence=on`). Later the same day the user asked for stance
colours instead of the category colour: "for" dots are green and "against" diamonds red, filled or outlined.

## What the data gives us

Each subcategory's HTML in the category JSON has `ul.evidence > li` items with `data-stance` (for, against, context),
`data-confidence` (high, moderate, low), `data-source` (research run) and, on RRS items, `data-repository`.
`graph.js` can read them from `ctx.subHtml()` the same way `coverage()` in `app.js` does, so **`build_data.py` does
not change**.

GHCN-Daily today: **210 items**, 5 (DIRS-4) to 16 (DIRS-2, DIRS-3) per subcategory. 127 of them set a score: high or
moderate confidence, and "for" or "against". The rest are context or low confidence. Up to 3 gaps per subcategory.

## The switch

- A switch in the options row above the graph, beside the RRS choice: **"Show evidence nodes"**, off by default.
  It's a `<button role="switch" aria-checked>` styled as a sliding toggle, so screen readers announce "on" and "off".
- Turning it on redraws the graph with the evidence layer and says so in a polite live region: "Showing 210
  evidence items; 127 set a score."
- The choice is kept while the page is open, like the RRS choice. It could also go in the URL
  (`graph.html?dataset=ghcn-daily&evidence=on`) so a link opens with it on.
- If the dataset isn't categorized there's no graph, so there's no switch either.

## How evidence nodes look

From the user's notes, an evidence node is "smaller than the subgroup node" and "the same color as the subgroup
node", with "lines of some neutral color".

| Evidence item | Node |
|---|---|
| Sets the score: "for", high or moderate | filled circle, category colour |
| Sets the score: "against", high or moderate | filled diamond, category colour |
| Doesn't set the score: low confidence | the same shape, outline only |
| Context | small hollow circle, muted grey |

- **Two encodings:** shape shows the stance and fill shows whether the item counts toward the score. Neither relies
  on colour alone. The notes' "contributing or not" becomes filled versus hollow.
- **Size:** dots have a radius of about 5 px; subcategory nodes have 31 px.
- **Lines:** one thin line (0.75 px, muted grey, partly see-through) from each dot to its subcategory node.
- **Lines from another dataset:** the notes ask for thick lines when the evidence comes from another dataset. No item
  carries that yet. Once the categorize scripts add an attribute for it (for example `data-from-dataset="gpcp-daily"`),
  those lines draw at a fixed thick width. Until then every line is thin.
- **How many dots:** a subcategory with many items gets a visibly bigger cluster. That is the notes' "quantity of
  information nodes" showing how much is known.

## Layout

Each subcategory node gets a **fan of dots on its outer side**, facing away from its category node:

```
                 · · · · · ·          ring 3 (r ≈ 68)
                · · · · · ·           ring 2 (r ≈ 56)
                 · · · · ·            ring 1 (r ≈ 44)
                  ( P-1 )             subcategory node (r = 31)
                     |
                  [  P  ]             category node
```

- **Rings:** each ring covers ±40° around the outward direction, with dots about 11 px apart. That gives roughly
  5, 7 and 9 dots for rings 1, 2 and 3, so 21 in all; the largest subcategory today has 16. If one ever has more, a
  fourth ring is added.
- **No overlap:** the subcategory nodes are 30° apart around their category. At ring 3 the neighbouring fans' centres
  are about 120 px apart and each fan is about 90 px wide, so they don't overlap.
- **Order:** dots are sorted for, against, then context, as on the cards, starting at the inner ring and going
  clockwise. Each stance therefore forms a visible group.
- **Size of the drawing:** the bounds are already worked out from the nodes (`grow()`), so the viewBox grows by about
  75 px on each side. Raise the graph's max width from 820 px to about 960 px while evidence is shown, so the text
  stays the same size.
- **Motion:** the dots fade in (about 150 ms), and not at all under `prefers-reduced-motion`.

## Details on hover

- **Hovering a dot:** the tooltip shows the stance, the confidence, and whether it sets the score. It also shows the
  repository (RRS items) and the first ~200 characters of the evidence text.
- **Dots are not tab stops.** 210 extra stops would make the page hard to use with a keyboard. Keyboard and
  screen-reader users get the same information from the subcategory node, which links to its card listing every item,
  and from the table (below).
- **Clicking a dot** opens its subcategory's card on the category page, like clicking the subcategory node.
- **Hovering or focusing a subcategory node** highlights its dots and dims the rest.
- **The subcategory tooltip** gains a counts line: "13 evidence items: 2 for, 4 against, 7 context; 6 set the score".

## Table and key

- **"The graph as a table":** add an **Evidence** column for each subcategory row, with the same counts as the
  tooltip. It's there whether or not the switch is on.
- **Graph key:** while the switch is on, it adds the four dot styles and the evidence line.
- **A note under the graph:** evidence nodes show the web research. A chosen score can differ from what the evidence
  implies; the card says which.

## Files

| File | Change |
|---|---|
| `app/assets/graph.js` | read the evidence items; work out fan positions; draw the evidence layer under the subcategory nodes; add the switch, the live message, the dot tooltips, the highlight on hover, the Evidence column and the key entries |
| `app/assets/styles.css` | switch styles; dot, diamond, hollow and context styles; evidence lines; dimming; fade-in; dark mode |
| `app/e2e/test_graph.py` | new tests (below) |
| `app/README.md`, `HANDOFF.md` | describe the evidence layer and the switch |

## Tests

- The switch starts off (`aria-checked="false"`) and no evidence nodes are drawn.
- Turning it on draws 210 evidence nodes for GHCN-Daily, and the live message says "Showing 210 evidence items; 137
  set a score". The dots are hidden from screen readers, so the test counts them with a `data-testid`.
- Turning it off removes them, and the RRS switch keeps the evidence setting.
- The table's Evidence column for P-1 reads "13: 2 for, 4 against, 7 context; 6 set the score".
- Clicking an evidence node opens its subcategory's card.
- No console errors, in Firefox and WebKit.

## Questions for the user

1. ~~**"Slider":** an on/off switch or a three-step slider?~~ On/off switch (2026-11-24).
2. **Gaps:** should gaps (up to 3 per subcategory) also show, for example as small dashed "?" nodes? This plan leaves
   them out.
3. **Evidence from another dataset:** what should mark it? This needs a new attribute in the categorize scripts
   before the thick lines can be drawn.
