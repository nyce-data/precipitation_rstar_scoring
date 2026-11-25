"""R* score page (scores.html): reach every category, see the dataset, jump to a subcategory."""
import re

from playwright.sync_api import Page, expect

CATEGORIES = ["People risk", "Data risk", "Dependent infrastructure resilience", "Repository resilience"]


def test_landing_links_to_all_four_categories(page: Page, console_errors):
    page.goto("/scores.html")

    expect(page.get_by_role("heading", level=1, name="R* Scores")).to_be_visible()
    expect(page).to_have_title("R* Scores")
    for name in CATEGORIES:
        expect(page.get_by_role("link", name=f"Open {name} →")).to_be_visible()
    assert console_errors == []


def test_landing_shows_the_selected_dataset(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    expect(page.get_by_role("heading", name="GHCN-D: Global Historical Climatology Network Daily", exact=True)).to_be_visible()
    expect(page.get_by_role("combobox", name="Dataset")).to_have_value("ghcn-daily")


def test_category_link_opens_the_category_page(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    page.get_by_role("link", name="Open Data risk →").click()

    expect(page).to_have_url(re.compile(r"/data-risk\.html\?dataset=ghcn-daily$"))
    expect(page.get_by_role("heading", level=1, name="D: Data Risk")).to_be_visible()


def test_subcategory_chip_opens_that_card(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    page.get_by_role("link", name=re.compile(r"^P-3 \(\d+ evidence items")).click()

    expect(page).to_have_url(re.compile(r"/people-risk\.html\?dataset=ghcn-daily#P-3$"))
    expect(page.get_by_role("button", name="Hide categorization for P-3")).to_have_attribute("aria-expanded", "true")
    expect(page.get_by_role("region", name=re.compile(r"^P-3 Critical undocumented knowledge"))).to_be_visible()


def test_switching_dataset_updates_links_and_details(page: Page, uncategorized):
    page.goto("/scores.html?dataset=ghcn-daily")

    page.get_by_role("combobox", name="Dataset").select_option(uncategorized)

    expect(page).to_have_url(re.compile(rf"\?dataset={uncategorized}$"))
    expect(page.get_by_text("This dataset has no categorization file yet.")).to_be_visible()
    nav = page.get_by_role("navigation", name="Pages")
    expect(nav.get_by_role("link", name="Data risk")).to_have_attribute("href", f"data-risk.html?dataset={uncategorized}")


def test_landing_has_a_key_to_the_tags_and_scores(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    key = page.get_by_role("region", name="How to read the tags and scores")
    expect(key.get_by_role("table", name="Tags on each evidence item")).to_contain_text("For, Against, Context")
    scoring = key.get_by_role("table", name="How a subcategory is scored")
    expect(scoring.get_by_role("row", name=re.compile(r"Both “for” and “against” items NA"))).to_be_visible()


def test_landing_shows_rstar_and_category_scores(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    scores = page.get_by_role("region", name=re.compile(r"^R\* score for GHCN-D"))
    expect(scores.get_by_text("Repository resilience", exact=True)).to_be_visible()
    expect(scores.get_by_text("2 of 5 subcategories scored · out of 100 points")).to_be_visible()
    details_button = scores.get_by_role("button", name="Score details")
    expect(details_button).to_have_attribute("aria-expanded", "false")
    expect(page.get_by_role("region", name="Score details")).to_be_hidden()

    details_button.click()

    details = page.get_by_role("region", name="Score details")
    expect(details_button).to_have_attribute("aria-expanded", "true")
    expect(details.get_by_role("link", name=re.compile(r"^(P|D|DIRS|RRS)-\d$"))).to_have_count(19)
    expect(details.get_by_role("row", name=re.compile(r"^RRS-2 Regular backup integrity verification 20 0$"))).to_be_visible()

    details.get_by_role("link", name="RRS-2").click()
    expect(page).to_have_url(re.compile(r"/repository-resilience\.html\?dataset=ghcn-daily#RRS-2$"))


def test_landing_says_when_producer_and_repository_are_the_same(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    expect(page.get_by_text("The producer and repository are the same organization")).to_be_visible()

    page.get_by_role("combobox", name="Dataset").select_option("gpcp-daily")

    expect(page.get_by_text("The producer and repository are the same organization")).to_have_count(0)
    expect(page.get_by_role("region", name=re.compile(r"^R\* score for GPCP Daily"))).to_be_visible()
