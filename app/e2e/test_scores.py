"""Choosing scores: radio buttons on each card, the category's score panel, and R* on the landing page."""
import json
import re

from playwright.sync_api import Page, expect

STORE_KEY = "rstar-chosen-scores-v1"


def choices(page: Page, sub_id: str):
    return page.get_by_role("group", name=f"Your score for {sub_id}")


def score_panel(page: Page, title: str):
    return page.get_by_role("complementary", name=title)


def total(page: Page, title: str):
    return score_panel(page, title).get_by_role("row", name=re.compile(r"^Raw total "))


def contribution(page: Page, title: str, category: str):
    return score_panel(page, title).get_by_role("row", name=re.compile(rf"^{category} contribution "))


def test_radios_start_on_the_research_score(page: Page, console_errors):
    page.goto("/repository-resilience.html?dataset=ghcn-daily")

    rrs2 = choices(page, "RRS-2")
    expect(rrs2.get_by_role("radio")).to_have_count(3)
    expect(rrs2.get_by_role("radio", name="20", exact=True)).not_to_be_checked()
    expect(rrs2.get_by_role("radio", name="0", exact=True)).to_be_checked()
    expect(choices(page, "RRS-1").get_by_role("radio", name="NA", exact=True)).to_be_checked()
    expect(rrs2).to_have_accessible_description(re.compile(r"“against” web evidence and no “for” web evidence: score = 0$"))
    assert console_errors == []


def test_radio_labels_are_only_the_values(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    expect(choices(page, "P-1").locator("label")).to_have_text(["35", "0", "NA"])


def test_choosing_scores_updates_the_category_total(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")
    panel = score_panel(page, "People risk scores")
    expect(total(page, "People risk scores")).to_have_text(re.compile(r"Raw total\s*100\s*NA"))
    expect(contribution(page, "People risk scores", "People risk")).to_have_text(re.compile(r"People risk contribution\s*30\s*NA"))

    for sub_id, value in [("P-1", "35"), ("P-2", "0"), ("P-3", "25"), ("P-4", "15")]:
        choices(page, sub_id).get_by_role("radio", name=value, exact=True).check()

    expect(total(page, "People risk scores")).to_have_text(re.compile(r"Raw total\s*100\s*75"))
    # 0.30 × 75 = 22.5 of R*.
    expect(contribution(page, "People risk scores", "People risk")).to_have_text(re.compile(r"People risk contribution\s*30\s*22.5"))
    expect(panel.get_by_role("row", name=re.compile(r"^P-2 "))).to_have_text(re.compile(r"P-2\s*25\s*0"))
    expect(panel).to_contain_text("4 changed from the web evidence scores.")

    choices(page, "P-4").get_by_role("radio", name="NA", exact=True).check()

    expect(total(page, "People risk scores")).to_have_text(re.compile(r"Raw total\s*100\s*NA"))


def test_choosing_a_score_does_not_open_the_card(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    choices(page, "P-1").get_by_text("35", exact=True).click()

    expect(choices(page, "P-1").get_by_role("radio", name="35", exact=True)).to_be_checked()
    expect(page.get_by_role("region")).to_have_count(0)


def test_arrow_keys_move_between_choices(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    choices(page, "P-1").get_by_role("radio", name="NA", exact=True).focus()
    page.keyboard.press("ArrowLeft")

    expect(choices(page, "P-1").get_by_role("radio", name="0", exact=True)).to_be_checked()
    expect(page.get_by_role("region")).to_have_count(0)


def test_choices_show_on_the_landing_page_and_after_going_back(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")
    page.get_by_role("link", name="Open People risk →").click()
    for sub_id, value in [("P-1", "35"), ("P-2", "25"), ("P-3", "25"), ("P-4", "0")]:
        choices(page, sub_id).get_by_role("radio", name=value, exact=True).check()

    page.go_back()

    scores = page.get_by_role("region", name=re.compile(r"^R\* score for GHCN-D"))
    expect(scores.get_by_text("4 of 4 subcategories scored · out of 100 points")).to_be_visible()
    expect(scores).to_contain_text("You changed 4 of 19 subcategory scores")
    scores.get_by_role("button", name="Score details").click()
    expect(page.get_by_role("region", name="Score details").get_by_role("row", name=re.compile(r"^P-4 "))
           ).to_have_text(re.compile(r"15\s*0$"))

    page.get_by_role("navigation", name="Pages").get_by_role("link", name="People risk").click()
    expect(choices(page, "P-4").get_by_role("radio", name="0", exact=True)).to_be_checked()


def test_rstar_is_worked_out_when_every_score_is_chosen(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")
    page.evaluate(
        """key => {
            const all = {};
            RSTAR_DATA.categories.forEach(c => c.subcategories.forEach(s => all[s.id] = s.points));
            localStorage.setItem(key, JSON.stringify({"ghcn-daily": all}));
        }""",
        STORE_KEY,
    )
    page.reload()

    # 0.40 × 100 + 0.30 × 100 + 0.20 × (100 − 100) + 0.10 × 100
    rstar = page.locator(".score-tile.total .score-value")
    expect(rstar).to_have_text("80")


def test_reset_returns_to_the_research_scores(page: Page):
    page.goto("/repository-resilience.html?dataset=ghcn-daily")
    reset = score_panel(page, "Repository resilience scores").get_by_role("button", name="Reset scores")
    expect(reset).to_be_disabled()

    choices(page, "RRS-2").get_by_role("radio", name="20", exact=True).check()
    expect(reset).to_be_enabled()
    reset.click()

    expect(choices(page, "RRS-2").get_by_role("radio", name="0", exact=True)).to_be_checked()
    expect(reset).to_be_disabled()
    assert json.loads(page.evaluate(f"localStorage.getItem('{STORE_KEY}')")) == {}


def test_category_reset_keeps_other_categories(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")
    choices(page, "P-1").get_by_role("radio", name="0", exact=True).check()
    page.goto("/data-risk.html?dataset=ghcn-daily")
    choices(page, "D-1").get_by_role("radio", name="0", exact=True).check()
    dialogs = []
    page.on("dialog", lambda d: (dialogs.append(d.message), d.dismiss()))

    score_panel(page, "Data risk scores").get_by_role("button", name="Reset scores").click()

    expect(choices(page, "D-1").get_by_role("radio", name="NA", exact=True)).to_be_checked()
    assert dialogs == []
    page.goto("/people-risk.html?dataset=ghcn-daily")
    expect(choices(page, "P-1").get_by_role("radio", name="0", exact=True)).to_be_checked()


def test_landing_reset_clears_every_category_after_asking(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")
    scores = page.get_by_role("region", name=re.compile(r"^R\* score for GHCN-D"))
    reset = scores.get_by_role("button", name="Reset scores")
    expect(reset).to_be_disabled()
    page.goto("/people-risk.html?dataset=ghcn-daily")
    choices(page, "P-1").get_by_role("radio", name="0", exact=True).check()
    page.get_by_label("Your notes for P-1").fill("Kept after a reset")
    page.goto("/data-risk.html?dataset=ghcn-daily")
    choices(page, "D-1").get_by_role("radio", name="0", exact=True).check()
    page.goto("/scores.html?dataset=ghcn-daily")
    expect(scores).to_contain_text("You changed 2 of 19")

    page.once("dialog", lambda d: d.dismiss())
    reset.click()
    expect(scores).to_contain_text("You changed 2 of 19")

    page.once("dialog", lambda d: d.accept())
    reset.click()

    expect(scores).to_contain_text("All scores are the web evidence scores.")
    expect(reset).to_be_disabled()
    assert json.loads(page.evaluate(f"localStorage.getItem('{STORE_KEY}')")) == {}
    page.goto("/people-risk.html?dataset=ghcn-daily")
    expect(page.get_by_label("Your notes for P-1")).to_have_value("Kept after a reset")


def test_dataset_without_categorization_has_no_choices(page: Page, uncategorized):
    page.goto(f"/people-risk.html?dataset={uncategorized}")

    expect(page.get_by_role("radio")).to_have_count(0)
    expect(page.get_by_role("complementary")).to_have_count(0)


def test_key_comes_after_the_score_section(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    headings = page.locator("main section > h2")
    expect(headings).to_have_text([
        "GHCN-D: Global Historical Climatology Network Daily",
        re.compile(r"^R\* score for GHCN-D"),
        "How to read the tags and scores",
    ])


def test_repository_resilience_contribution_uses_100_minus_the_raw_total(page: Page):
    page.goto("/repository-resilience.html?dataset=ghcn-daily")
    panel = score_panel(page, "Repository resilience scores")
    expect(panel).to_contain_text("The contribution is 0.20 × (100 − raw total)")

    for sub_id, value in [("RRS-1", "25"), ("RRS-2", "20"), ("RRS-3", "20"), ("RRS-4", "0"), ("RRS-5", "15")]:
        choices(page, sub_id).get_by_role("radio", name=value, exact=True).check()

    # Raw total 80, so 0.20 × (100 − 80) = 4 of R*.
    expect(total(page, "Repository resilience scores")).to_have_text(re.compile(r"Raw total\s*100\s*80"))
    expect(contribution(page, "Repository resilience scores", "Repository resilience")).to_have_text(
        re.compile(r"Repository resilience contribution\s*20\s*4$")
    )
