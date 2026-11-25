"""The score graph page: a weighted network graph of a dataset's R* scores, with a table of the same data."""
import json
import re

from playwright.sync_api import Page, expect

STORE_KEY = "rstar-chosen-scores-v1"

# A full set of choices for GHCN-Daily: R* = 0.40·60 + 0.30·75 + 0.20·(100 − 45) + 0.10·75 = 65.
ALL_CHOSEN = {
    "P-1": 35, "P-2": 0, "P-3": 25, "P-4": 15,
    "D-1": 30, "D-2": 0, "D-3": 20, "D-4": 0, "D-5": 10,
    "DIRS-1": 0, "DIRS-2": 25, "DIRS-3": 20, "DIRS-4": 15, "DIRS-5": 15,
    "RRS-1": 25, "RRS-2": 0, "RRS-3": 0, "RRS-4": 20, "RRS-5": 0,
}


def graph(page: Page):
    return page.get_by_role("group", name=re.compile(r"^R\* score graph for "))


def open_with_choices(page: Page, choices: dict):
    page.goto("/graph.html?dataset=ghcn-daily")
    page.evaluate(
        "([key, value]) => localStorage.setItem(key, value)",
        [STORE_KEY, json.dumps({"ghcn-daily": choices})],
    )
    page.reload()


def open_table(page: Page):
    page.get_by_role("button", name="The graph as a table").click()


def table_row(page: Page, node: str):
    return page.get_by_role("table", name=re.compile(r"as a table$")).get_by_role("row", name=re.compile(rf"^{re.escape(node)} "))


def test_header_links_to_the_graph(page: Page, console_errors):
    page.goto("/scores.html?dataset=ghcn-daily")

    page.get_by_role("navigation", name="Pages").get_by_role("link", name="Score graph").click()

    expect(page).to_have_url(re.compile(r"/graph\.html\?dataset=ghcn-daily$"))
    expect(page.get_by_role("heading", level=1, name="R* score graph")).to_be_visible()
    expect(page.get_by_role("navigation", name="Pages").get_by_role("link", name="Score graph")).to_have_attribute(
        "aria-current", "page"
    )
    assert console_errors == []


def test_landing_score_panel_links_to_the_graph(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    page.get_by_role("link", name="See the score graph →").click()

    expect(page).to_have_url(re.compile(r"/graph\.html\?dataset=ghcn-daily$"))


def test_graph_starts_from_the_web_evidence_scores(page: Page, console_errors):
    page.goto("/graph.html?dataset=ghcn-daily")

    expect(page.get_by_text(re.compile(r"^R\* is NA: 17 of 19 subcategories are NA"))).to_be_visible()
    # 19 subcategory nodes and 4 category nodes, each a link.
    expect(graph(page).get_by_role("link")).to_have_count(23)
    expect(graph(page).get_by_role("link", name=re.compile(r"^RRS-2 Regular backup integrity verification: score 0 of 20\."))).to_be_visible()
    expect(graph(page).get_by_role("link", name=re.compile(r"^People risk: total NA of 100"))).to_be_visible()
    assert console_errors == []


def test_graph_uses_the_chosen_scores(page: Page):
    open_with_choices(page, ALL_CHOSEN)

    expect(page.get_by_text("R* is 65 (triage: Stabilize and mirror). Every subcategory has a score.")).to_be_visible()
    expect(graph(page).get_by_role("link", name=re.compile(r"^P-1 No documented succession plan: score 35 of 35\."))).to_be_visible()
    open_table(page)
    expect(table_row(page, "P-1")).to_have_text(re.compile(r"35\s*35\s*7 px"))


def test_category_lines_show_their_weighted_share_of_rstar(page: Page):
    open_with_choices(page, ALL_CHOSEN)
    open_table(page)

    # Width = share of R* ÷ 4: P adds 0.30 × 75 = 22.5, RRS adds 0.20 × (100 − 45) = 11.
    expect(table_row(page, "P")).to_have_text(re.compile(r"75\s*100\s*5.6 px \(adds 22.5 to R\*\)"))
    expect(table_row(page, "RRS")).to_have_text(re.compile(r"45\s*100\s*2.8 px \(adds 11 to R\*\)"))
    expect(graph(page).get_by_role("link", name=re.compile(r"^Data risk: total 60 of 100, .* adds 24 to R\*\."))).to_be_visible()

    # The RRS switch changes only the subcategory lines.
    page.get_by_role("radio", name="Its score").check()
    expect(table_row(page, "RRS")).to_have_text(re.compile(r"2.8 px \(adds 11 to R\*\)"))


def test_one_na_subcategory_makes_its_category_and_rstar_na(page: Page):
    open_with_choices(page, {**ALL_CHOSEN, "DIRS-4": "NA"})

    expect(page.get_by_text(re.compile(r"^R\* is NA: 1 of 19 subcategories is NA, so its category"))).to_be_visible()
    open_table(page)
    expect(table_row(page, "DIRS-4")).to_have_text(re.compile(r"NA\s*15\s*dashed \(NA\)"))


def test_repository_lines_show_risk_or_score(page: Page):
    open_with_choices(page, ALL_CHOSEN)
    open_table(page)
    row = table_row(page, "RRS-1")
    expect(page.get_by_role("radio", name="The risk it adds (points − score)")).to_be_checked()
    expect(row).to_have_text(re.compile(r"1 px \(risk 0 = 25 − 25\)"))

    page.get_by_role("radio", name="Its score").check()

    expect(page.get_by_role("radio", name="Its score")).to_be_checked()
    # The page redraws; the table stays open.
    expect(row).to_have_text(re.compile(r"25\s*25\s*5 px"))


def test_a_subcategory_node_opens_its_card(page: Page):
    page.goto("/graph.html?dataset=ghcn-daily")

    graph(page).get_by_role("link", name=re.compile(r"^P-3 ")).click()

    expect(page).to_have_url(re.compile(r"/people-risk\.html\?dataset=ghcn-daily#P-3$"))
    expect(page.get_by_role("button", name="Hide categorization for P-3")).to_have_attribute("aria-expanded", "true")


def test_uncategorized_dataset_has_no_graph(page: Page, uncategorized):
    page.goto(f"/graph.html?dataset={uncategorized}")

    expect(page.get_by_text(re.compile(r"has no categorization file yet, so it has no scores to graph\."))).to_be_visible()
    expect(graph(page)).to_have_count(0)


def rstar_fill(page: Page) -> str:
    # The R* node is drawn for sighted readers only (the summary sentence says the same), so it has no role to find
    # it by; its fill colour is what this test is about.
    return page.locator("svg .g-center circle").evaluate("c => getComputedStyle(c).fill")


def test_rstar_node_is_black_when_na_and_red_with_a_value(page: Page):
    page.emulate_media(color_scheme="light")
    page.goto("/graph.html?dataset=ghcn-daily")
    expect(page.get_by_text(re.compile(r"^R\* is NA"))).to_be_visible()
    assert rstar_fill(page) == "rgb(0, 0, 0)"

    open_with_choices(page, ALL_CHOSEN)

    expect(page.get_by_text(re.compile(r"^R\* is 65"))).to_be_visible()
    assert rstar_fill(page) == "rgb(198, 40, 40)"


# ---------------------------------------------------------------- evidence nodes
# Evidence nodes are hidden from screen readers (the same items are on the category pages, and the table gives
# the counts), so the tests find them by test id.

def evidence_switch(page: Page):
    return page.get_by_role("switch", name="Show evidence nodes")


def test_evidence_switch_shows_and_hides_the_evidence_nodes(page: Page, console_errors):
    page.goto("/graph.html?dataset=ghcn-daily")
    expect(evidence_switch(page)).to_have_attribute("aria-checked", "false")
    expect(page.get_by_test_id("evidence-node")).to_have_count(0)

    evidence_switch(page).click()

    expect(evidence_switch(page)).to_have_attribute("aria-checked", "true")
    expect(evidence_switch(page)).to_be_focused()
    expect(page.get_by_test_id("evidence-node")).to_have_count(210)
    expect(page.get_by_role("status")).to_have_text("Showing 210 evidence items; 127 set a score.")
    expect(page).to_have_url(re.compile(r"\?dataset=ghcn-daily&evidence=on$"))

    evidence_switch(page).click()

    expect(evidence_switch(page)).to_have_attribute("aria-checked", "false")
    expect(page.get_by_test_id("evidence-node")).to_have_count(0)
    expect(page).to_have_url(re.compile(r"\?dataset=ghcn-daily$"))
    assert console_errors == []


def test_evidence_stays_on_when_the_repository_lines_change(page: Page):
    page.goto("/graph.html?dataset=ghcn-daily&evidence=on")
    expect(evidence_switch(page)).to_have_attribute("aria-checked", "true")

    page.get_by_role("radio", name="Its score").check()

    expect(evidence_switch(page)).to_have_attribute("aria-checked", "true")
    expect(page.get_by_test_id("evidence-node")).to_have_count(210)


def test_table_counts_the_evidence(page: Page):
    page.goto("/graph.html?dataset=ghcn-daily")
    open_table(page)

    expect(table_row(page, "P-1")).to_contain_text("13: 2 for, 4 against, 7 context; 6 set the score")
    expect(table_row(page, "P")).to_contain_text("44: 12 for, 14 against, 18 context; 23 set the score")


def test_an_evidence_node_opens_its_card(page: Page):
    page.goto("/graph.html?dataset=ghcn-daily&evidence=on")
    p3_evidence = page.get_by_test_id("evidence-node").and_(page.locator('[data-sub="P-3"]'))
    expect(p3_evidence).to_have_count(11)

    # Any of P-3's evidence nodes opens the P-3 card; the first is as good as any.
    p3_evidence.first.click()

    expect(page).to_have_url(re.compile(r"/people-risk\.html\?dataset=ghcn-daily#P-3$"))
    expect(page.get_by_role("button", name="Hide categorization for P-3")).to_have_attribute("aria-expanded", "true")


def test_for_evidence_is_green_and_against_evidence_is_red(page: Page):
    page.emulate_media(color_scheme="light")
    page.goto("/graph.html?dataset=ghcn-daily&evidence=on")
    nodes = page.get_by_test_id("evidence-node")
    expect(nodes).to_have_count(210)

    # The colour is what this test is about, so it reads the marks' fills (shape: circle for, diamond against).
    fills = nodes.evaluate_all(
        """dots => dots.map(d => d.querySelector('.g-ev'))
              .filter(m => !m.classList.contains('hollow') && !m.classList.contains('context'))
              .map(m => [m.tagName, getComputedStyle(m).fill])"""
    )
    assert {tuple(f) for f in fills} == {("circle", "rgb(29, 122, 70)"), ("polygon", "rgb(198, 40, 40)")}
