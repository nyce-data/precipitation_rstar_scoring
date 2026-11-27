"""Category pages: subcategory cards open and close to show the categorization."""
import re

from playwright.sync_api import Page, expect


def toggle(page: Page, sub_id: str):
    return page.get_by_role("button", name=re.compile(rf"^(Show|Hide) categorization for {re.escape(sub_id)}$"))


def panel(page: Page, sub_id: str):
    return page.get_by_role("region", name=re.compile(rf"^{re.escape(sub_id)} "))


def test_cards_show_description_and_what_counts_and_start_closed(page: Page, console_errors):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    expect(page.get_by_role("heading", level=2, name=re.compile(r"^P-\d "))).to_have_count(4)
    expect(page.get_by_role("heading", level=3, name="What counts as evidence")).to_have_count(4)
    expect(page.get_by_text("A written succession plan, or documentation")).to_be_visible()
    expect(page.get_by_role("heading", name="How to find")).to_have_count(0)
    expect(page.get_by_text("No written plan identifies a successor")).to_be_visible()
    expect(page.get_by_role("button", name=re.compile(r"^Show categorization for P-"))).to_have_count(4)
    expect(page.get_by_role("region")).to_have_count(0)
    assert console_errors == []


def test_arrow_button_opens_and_closes_the_panel(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    toggle(page, "P-1").click()

    expect(toggle(page, "P-1")).to_have_attribute("aria-expanded", "true")
    expect(panel(page, "P-1")).to_be_visible()
    expect(panel(page, "P-1").get_by_role("heading", name="Evidence")).to_be_visible()
    expect(panel(page, "P-1").get_by_text("high confidence").first).to_be_visible()

    toggle(page, "P-1").click()

    expect(toggle(page, "P-1")).to_have_attribute("aria-expanded", "false")
    expect(panel(page, "P-1")).to_be_hidden()


def test_evidence_is_tagged_and_sorted_for_against_context(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily#P-1")

    p = panel(page, "P-1")
    expect(p.get_by_text(re.compile(r"tagged for, against or context .*\d+ for · \d+ against · \d+ context\."))).to_be_visible()
    items = "ul.evidence > li"
    expect(p.locator(f"{items} .stance").first).to_have_text(re.compile(r"^(For|Against|Context)$"))
    # Every item has a tag, and no item comes after one that should sort below it.
    # (Locator checks, not all_text_contents(): that call crashes this page in Playwright's Firefox.)
    expect(p.locator(f"{items}:not(:has(.stance))")).to_have_count(0)
    expect(p.locator(f"{items}:has(.stance.against) ~ li:has(.stance.for)")).to_have_count(0)
    expect(p.locator(f"{items}:has(.stance.context) ~ li:has(.stance.for)")).to_have_count(0)
    expect(p.locator(f"{items}:has(.stance.context) ~ li:has(.stance.against)")).to_have_count(0)
    expect(p.get_by_text("Neutral", exact=True)).to_have_count(0)
    # The research run folder names mean nothing to readers, so items don't show them.
    expect(p.get_by_text(re.compile(r"^(about|repository|people|infrastructure)-pt\d+$"))).to_have_count(0)


def test_each_card_says_why_the_research_scored_it(page: Page):
    page.goto("/repository-resilience.html?dataset=ghcn-daily")

    rrs2 = page.get_by_role("listitem").filter(has=page.get_by_role("heading", name=re.compile(r"^RRS-2 ")))
    expect(rrs2.get_by_text("High or moderate “against” web evidence and no “for” web evidence: score = 0", exact=True)).to_be_visible()
    rrs1 = page.get_by_role("listitem").filter(has=page.get_by_role("heading", name=re.compile(r"^RRS-1 ")))
    expect(rrs1.get_by_text("Both “for” and “against” web evidence (high or moderate): score = NA", exact=True)).to_be_visible()
    expect(page.get_by_text("needs a decision")).to_have_count(0)
    # The research score itself shows only as the radio the card starts on, not as a badge.
    expect(page.get_by_text(re.compile(r"^Research score"))).to_have_count(0)


def test_repository_cards_name_the_repositories(page: Page):
    page.goto("/repository-resilience.html?dataset=ghcn-daily")

    expect(page.get_by_text(re.compile(r"^3 repositories: NOAA NCEI archive \(parent\)"))).to_have_count(5)


def test_gaps_have_a_status_and_rrs_items_a_repository(page: Page):
    page.goto("/repository-resilience.html?dataset=ghcn-daily#RRS-2")

    p = panel(page, "RRS-2")
    expect(p.get_by_role("listitem").filter(has_text="SOP 60-6-015")).to_contain_text("Not public")
    expect(p.get_by_text("Repository: NCEI").first).to_be_visible()


def test_clicking_the_card_header_opens_the_panel(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    page.get_by_text("Key personnel retirement-eligible").click()

    expect(panel(page, "P-2")).to_be_visible()
    expect(page).to_have_url(re.compile(r"#P-2$"))


def test_keyboard_enter_and_space_toggle_the_panel(page: Page):
    page.goto("/data-risk.html?dataset=ghcn-daily")

    toggle(page, "D-2").focus()
    page.keyboard.press("Enter")
    expect(panel(page, "D-2")).to_be_visible()

    page.keyboard.press("Space")
    expect(panel(page, "D-2")).to_be_hidden()


def test_expand_all_and_collapse_all(page: Page):
    page.goto("/data-risk.html?dataset=ghcn-daily")

    page.get_by_role("button", name="Expand all").click()
    expect(page.get_by_role("region")).to_have_count(5)

    page.get_by_role("button", name="Collapse all").click()
    expect(page.get_by_role("region")).to_have_count(0)


def test_deep_link_opens_that_card(page: Page):
    page.goto("/dependent-infrastructure.html?dataset=ghcn-daily#DIRS-3")

    expect(panel(page, "DIRS-3")).to_be_visible()
    expect(page.get_by_role("region")).to_have_count(1)


def test_evidence_links_open_in_a_new_tab(page: Page):
    page.goto("/data-risk.html?dataset=ghcn-daily#D-1")

    link = panel(page, "D-1").get_by_role("link").first
    expect(link).to_have_attribute("target", "_blank")
    expect(link).to_have_attribute("rel", "noopener noreferrer")


def test_subcategory_with_no_evidence_says_so(page: Page):
    # Every GHCN-Daily subcategory has evidence now, so serve the data with RRS-2 emptied.
    def empty_rrs2(route):
        body = route.fetch().text()
        # Start at GHCN-Daily's entry: datasets are listed by id, and others (CoCoRaHS) come first.
        start = body.index('"id": "ghcn-daily"')
        body = body[:start] + re.sub(r'"RRS-2": "<div class=\\"rrs-2\\"[^>]*>.*?</div>"',
                                     r'"RRS-2": "<div class=\\"rrs-2\\"></div>"', body[start:], count=1)
        route.fulfill(body=body, content_type="application/javascript")

    page.route("**/data/rstar-data.js", empty_rrs2)
    page.goto("/repository-resilience.html?dataset=ghcn-daily")

    expect(page.get_by_role("listitem").filter(has=page.get_by_role("heading", name=re.compile(r"^RRS-2 ")))
           ).to_contain_text("No evidence found")
    toggle(page, "RRS-2").click()

    expect(panel(page, "RRS-2")).to_have_text("The research had nothing relevant to this subcategory.")


def test_dataset_without_categorization_says_so(page: Page, uncategorized):
    page.goto(f"/data-risk.html?dataset={uncategorized}")

    expect(page.get_by_text("Not categorized yet for this dataset")).to_have_count(5)
    toggle(page, "D-1").click()

    expect(panel(page, "D-1")).to_have_text(re.compile(r"has not been categorized yet\.$"))


def test_breadcrumb_returns_to_the_score_page_with_dataset(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    page.get_by_role("navigation", name="Breadcrumb").get_by_role("link", name="All categories").click()

    expect(page).to_have_url(re.compile(r"/scores\.html\?dataset=ghcn-daily$"))


def test_phone_width_has_no_sideways_scroll(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto("/people-risk.html?dataset=ghcn-daily#P-1")

    expect(panel(page, "P-1")).to_be_visible()
    overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    assert overflow <= 0
