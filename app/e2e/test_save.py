"""Saving scores: the landing page's Save button downloads a JSON file in the colleague's R* form format."""
import json
import re
from pathlib import Path

from playwright.sync_api import Page, expect

ROOT = Path(__file__).resolve().parents[2]
FORM = ROOT / "rstar-pipeline" / "input" / "framework" / "assessment-form" / "example_rstar_json.json"
EXAMPLE = json.loads(FORM.read_text(encoding="utf-8"))
TOP_KEYS = ["assessmentTimestamp", "dataset", "primaryDataCurator", "assessor", "rStarCompositeScore",
            "triageTier", "formula", "components", "framework"]


def radio(page: Page, sub_id: str, value: str):
    return page.get_by_role("group", name=f"Your score for {sub_id}").get_by_role("radio", name=value, exact=True)


def fill_assessor(page: Page, name="Jane Smith", email="jane@example.org", role="Expert"):
    page.get_by_label("Your name (required)").fill(name)
    page.get_by_label("Email (optional)").fill(email)
    page.get_by_label("Role").select_option(label=role)


def save(page: Page):
    with page.expect_download() as info:
        page.get_by_role("button", name="Save scores to a file").click()
    download = info.value
    return download.suggested_filename, json.loads(Path(download.path()).read_text(encoding="utf-8"))


def set_all_full_points(page: Page):
    page.evaluate("""() => {
        const all = {};
        RSTAR_DATA.categories.forEach(c => c.subcategories.forEach(s => all[s.id] = s.points));
        localStorage.setItem("rstar-chosen-scores-v1", JSON.stringify({"ghcn-daily": all}));
    }""")
    page.reload()


def test_saved_file_has_the_forms_shape_and_the_choices(page: Page, console_errors):
    page.goto("/people-risk.html?dataset=ghcn-daily")
    radio(page, "P-1", "35").check()
    radio(page, "P-2", "0").check()
    page.get_by_label("Your notes for P-1").fill("Team of four; the lead retires in 2027.")
    page.get_by_role("link", name="All categories").click()
    fill_assessor(page)

    filename, data = save(page)

    assert re.fullmatch(r"ghcn-daily_rstar_jane-smith_\d{4}-\d\d-\d\dT\d{6}Z\.json", filename)
    assert list(data) == TOP_KEYS
    assert re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z", data["assessmentTimestamp"])
    assert data["dataset"] == {"name": "GHCN-D: Global Historical Climatology Network Daily",
                               "identifier": "10.7289/V5D21VHZ"}
    assert data["primaryDataCurator"] == {"name": "NOAA NCEI GHCNd Operations Team", "email": ""}
    assert data["assessor"] == {"name": "Jane Smith", "email": "jane@example.org", "role": "expert"}
    assert data["formula"] == EXAMPLE["formula"]
    assert data["framework"] == EXAMPLE["framework"]

    p = data["components"]["P"]
    assert p["scoringMethod"] == ""
    assert p["justification"] == "P-1: Team of four; the lead retires in 2027."
    assert p["factors"]["no_documented_succession_plan"] == {
        "condition": "No documented succession plan", "present": True, "points": 35, "maxPoints": 35}
    assert p["factors"]["key_personnel_retirement_eligible"]["present"] is False
    assert p["factors"]["key_personnel_retirement_eligible"]["points"] == 0
    # NA is saved as null, and so are the totals and R* that depend on it.
    assert p["factors"]["critical_undocumented_knowledge"]["present"] is None
    assert p["factors"]["critical_undocumented_knowledge"]["points"] is None
    assert p["rawScore"] is None and p["weightedContribution"] is None
    assert data["rStarCompositeScore"] is None and data["triageTier"] is None

    expect(page.get_by_role("status")).to_contain_text(f"Saved {filename}")
    expect(page.get_by_role("status")).to_contain_text("NA values are included (15 of 19)")
    assert console_errors == []


def test_components_match_the_example_form(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")
    fill_assessor(page)

    _, data = save(page)

    assert list(data["components"]) == list(EXAMPLE["components"])
    for key, comp in data["components"].items():
        ex = EXAMPLE["components"][key]
        assert list(comp) == list(ex), key
        assert comp["label"] == ex["label"]
        assert comp["definition"] == ex["definition"]
        assert comp["weight"] == ex["weight"]
        assert list(comp["factors"]) == list(ex["factors"]), key
        for fk, factor in comp["factors"].items():
            assert factor["condition"] == ex["factors"][fk]["condition"]
            assert factor["maxPoints"] == ex["factors"][fk]["maxPoints"], fk


def test_full_scores_give_rstar_and_triage_tier(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")
    set_all_full_points(page)
    expect(page.get_by_text("NA values are included")).to_have_count(0)
    fill_assessor(page)

    _, data = save(page)

    # 0.40 × 100 + 0.30 × 100 + 0.20 × (100 − 100) + 0.10 × 100
    assert data["rStarCompositeScore"] == 80
    assert data["triageTier"] == "Mirror now"
    assert data["components"]["D"]["rawScore"] == 100
    assert data["components"]["D"]["weightedContribution"] == 40
    assert data["components"]["RRS"]["weightedContribution"] == 0
    expect(page.get_by_role("status")).not_to_contain_text("NA values")


def test_landing_says_when_na_values_are_included(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")

    expect(page.get_by_text(re.compile(r"^NA values are included: 17 of 19 subcategories are NA\."))).to_be_visible()


def test_save_needs_a_name(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")
    downloads = []
    page.on("download", lambda d: downloads.append(d))

    page.get_by_role("button", name="Save scores to a file").click()

    name = page.get_by_label("Your name (required)")
    expect(page.get_by_text("Enter your name to save.")).to_be_visible()
    expect(name).to_be_focused()
    expect(name).to_have_attribute("aria-invalid", "true")
    assert downloads == []


def test_name_is_remembered_and_last_save_is_shown(page: Page):
    page.goto("/scores.html?dataset=ghcn-daily")
    expect(page.get_by_text("Not saved yet from this browser.")).to_be_visible()
    fill_assessor(page, role="Workshop participant")

    filename, data = save(page)

    assert data["assessor"]["role"] == "workshop_participant"
    expect(page.get_by_text(re.compile(rf"^Last saved .* as {re.escape(filename)}\.$"))).to_be_visible()

    page.goto("/data-risk.html?dataset=ghcn-daily")
    radio(page, "D-1", "30").check()
    page.goto("/scores.html?dataset=ghcn-daily")

    expect(page.get_by_label("Your name (required)")).to_have_value("Jane Smith")
    expect(page.get_by_text(re.compile(r"You have changes since then\.$"))).to_be_visible()


def test_notes_box_does_not_open_the_card(page: Page):
    page.goto("/people-risk.html?dataset=ghcn-daily")

    page.get_by_label("Your notes for P-2").click()
    page.keyboard.type("Two staff near retirement")

    expect(page.get_by_role("region")).to_have_count(0)
    page.reload()
    expect(page.get_by_label("Your notes for P-2")).to_have_value("Two staff near retirement")
