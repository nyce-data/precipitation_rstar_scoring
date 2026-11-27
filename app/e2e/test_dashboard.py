"""The dashboard (index.html): dataset cards, search and filters, and the trip to a dataset's R* scores and back."""
import re

import pytest
from playwright.sync_api import Page, expect

DATASETS = {
    "ghcn-daily": "GHCN-D: Global Historical Climatology Network Daily",
    "gpcp-daily": "GPCP Daily v3.3: Global Precipitation Climatology Project",
    "imerg-late-run": "IMERG Late Run V07: Integrated Multi-satellitE Retrievals for GPM",
    "persiann-cdr-daily": "PERSIANN-CDR v1r1 Daily",
    "cocorahs": "CoCoRaHS: Community Collaborative Rain, Hail and Snow Network",
    "uscrn-daily": "USCRN Daily: U.S. Climate Reference Network Daily Products",
    "asos": "ASOS: Automated Surface Observing System",
}


def card(page: Page, dataset_id: str):
    return page.locator(f"#dataset-{dataset_id}")


def toggle(page: Page, dataset_id: str):
    return page.get_by_role("button", name=DATASETS[dataset_id], exact=True)


def test_dashboard_shows_a_card_per_dataset(page: Page, console_errors):
    page.goto("/")

    expect(page).to_have_title("Precipitation Workshop Datasets")
    expect(page.get_by_role("heading", level=1, name="Precipitation Datasets")).to_be_visible()
    for dataset_id in DATASETS:
        expect(toggle(page, dataset_id)).to_be_visible()
    expect(page.locator("#datasetCount")).to_have_text("07 OF 7 DATASETS")
    assert console_errors == []


def test_search_and_filter_narrow_the_cards_and_stay_in_the_url(page: Page):
    page.goto("/")

    page.get_by_role("button", name=re.compile(r"^Satellite")).click()
    expect(page.locator("#datasetCount")).to_have_text("03 OF 7 DATASETS")
    page.get_by_role("searchbox", name="Search datasets").fill("persiann")

    expect(page.locator("#datasetCount")).to_have_text("01 OF 7 DATASETS")
    expect(card(page, "persiann-cdr-daily")).to_be_visible()
    expect(card(page, "ghcn-daily")).to_be_hidden()
    expect(page).to_have_url(re.compile(r"\?q=persiann&category=satellite$"))


def test_card_links_to_its_rstar_scores_without_opening(page: Page):
    page.goto("/")

    card(page, "ghcn-daily").get_by_role("link", name="R* scores", exact=True).click()

    expect(page).to_have_url(re.compile(r"/scores\.html\?dataset=ghcn-daily&open=ghcn-daily$"))
    expect(page.get_by_role("heading", level=1, name="R* Scores")).to_be_visible()
    expect(page.get_by_role("combobox", name="Dataset")).to_have_value("ghcn-daily")


def test_rstar_link_is_on_the_card_not_in_its_panel(page: Page):
    page.goto("/")

    toggle(page, "ghcn-daily").click()

    expect(toggle(page, "ghcn-daily")).to_have_attribute("aria-expanded", "true")
    expect(card(page, "ghcn-daily").locator(".dataset-header").get_by_role("link", name="R* scores")).to_be_visible()
    expect(card(page, "ghcn-daily").locator(".dataset-details").get_by_role("link", name="R* scores")).to_have_count(0)


def test_cards_say_when_a_dataset_has_no_rstar_scores_yet(page: Page, uncategorized):
    page.goto("/")

    expect(card(page, uncategorized).get_by_role("link", name="R* scores")).to_be_visible()
    expect(card(page, uncategorized).get_by_text("Not categorized yet")).to_be_visible()
    # A categorized dataset's card links to its scores with no note.
    expect(card(page, "imerg-late-run").get_by_role("link", name="R* scores")).to_be_visible()
    expect(card(page, "imerg-late-run").get_by_text("Not categorized yet")).to_have_count(0)
    expect(card(page, "imerg-late-run").get_by_text("R* scores: NA")).to_have_count(0)
    # PERSIANN-CDR Daily was categorized on 2026-11-27.
    expect(card(page, "persiann-cdr-daily").get_by_role("link", name="R* scores")).to_be_visible()
    expect(card(page, "persiann-cdr-daily").get_by_text("Not categorized yet")).to_have_count(0)


def test_back_to_dashboard_restores_search_filters_and_open_card(page: Page):
    page.goto("/?q=daily&category=gauge")
    toggle(page, "ghcn-daily").click()
    card(page, "ghcn-daily").get_by_role("link", name="R* scores", exact=True).click()

    # Carry the dashboard state through a category page and the graph, then go back.
    page.get_by_role("navigation", name="Pages").get_by_role("link", name="People risk").click()
    expect(page).to_have_url(re.compile(r"/people-risk\.html\?"))
    page.get_by_role("navigation", name="Pages").get_by_role("link", name="Score graph").click()
    expect(page).to_have_url(re.compile(r"/graph\.html\?"))
    page.get_by_role("link", name="Back to dashboard").click()

    expect(page).to_have_url(re.compile(r"/index\.html\?q=daily&category=gauge&open=ghcn-daily$"))
    expect(page.get_by_role("searchbox", name="Search datasets")).to_have_value("daily")
    expect(page.get_by_role("button", name=re.compile(r"^Gauge-based"))).to_have_attribute("aria-pressed", "true")
    expect(toggle(page, "ghcn-daily")).to_have_attribute("aria-expanded", "true")
    expect(toggle(page, "ghcn-daily")).to_be_focused()


def test_back_to_dashboard_opens_the_dataset_picked_on_the_rstar_page(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily&open=ghcn-daily")

    page.get_by_role("combobox", name="Dataset").select_option("persiann-cdr-daily")
    page.get_by_role("link", name="Back to dashboard").click()

    expect(toggle(page, "persiann-cdr-daily")).to_have_attribute("aria-expanded", "true")
    expect(toggle(page, "persiann-cdr-daily")).to_be_focused()


@pytest.mark.parametrize(
    "path, heading",
    [
        ("/overview.html?id=imerg-late-run&open=imerg-late-run", "IMERG Late Run V07: Overview"),
        ("/dataset.html?id=ghcn-daily&open=ghcn-daily", "GHCN-D: Web research"),
        ("/dataset.html?id=persiann-cdr-daily&part=2&open=persiann-cdr-daily",
         "PERSIANN-CDR v1r1 Daily: Quality control and formats"),
        ("/overview.html?id=cocorahs&open=cocorahs", "CoCoRaHS: Overview"),
        ("/overview.html?id=uscrn-daily&open=uscrn-daily", "USCRN Daily: Overview"),
        ("/overview.html?id=asos&open=asos", "ASOS: Overview"),
        ("/archive.html?id=noaa-ncei", "NOAA NCEI"),
        ("/archive.html?id=noaa-satellites", "NOAA Satellites"),
    ],
)
def test_dataset_and_archive_pages_load_and_go_back(page: Page, console_errors, path, heading):
    page.goto(path)

    expect(page.get_by_role("heading", level=1, name=heading)).to_be_visible()
    page.get_by_role("link", name="Back to dashboard").click()
    expect(page).to_have_url(re.compile(r"/index\.html"))
    expect(page.locator("#datasetCount")).to_have_text("07 OF 7 DATASETS")
    assert console_errors == []


@pytest.mark.parametrize("dataset_id", ["cocorahs", "uscrn-daily", "asos"])
def test_new_datasets_have_cards_and_five_web_research_parts(page: Page, console_errors, dataset_id):
    page.goto("/")

    expect(card(page, dataset_id).get_by_role("link", name="R* scores")).to_be_visible()
    expect(card(page, dataset_id).get_by_text("Not categorized yet")).to_be_visible()
    short = DATASETS[dataset_id].split(":")[0]
    topics = ["Overview", "Quality control and formats", "People and funding", "Threats and news",
              "Threats to inputs"]
    for part, topic in enumerate(topics, start=1):
        page.goto(f"/dataset.html?id={dataset_id}&part={part}")
        expect(page.get_by_role("heading", level=1, name=f"{short}: {topic}")).to_be_visible()
        expect(page.get_by_text("Searched on", exact=False).first).to_be_visible()
    # Moving on before a web font finishes loading makes Firefox log "downloadable font: download failed".
    assert [e for e in console_errors if "downloadable font" not in e] == []
