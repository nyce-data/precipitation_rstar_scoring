"""Serve app/ on 127.0.0.1 for the e2e tests and point Playwright's base_url at it."""
import json
import os
import socket
import subprocess
import sys
import time
from pathlib import Path

import pytest

APP_DIR = Path(__file__).resolve().parents[1]

# ~/.zshrc exports DYLD_LIBRARY_PATH=/opt/homebrew/lib. That overrides Firefox's own @rpath lookup, so
# Playwright's Firefox loads Homebrew's libnss3 and fails with "Symbol not found: _PR_GMTParameters".
# Drop it before pytest-playwright starts its driver, which the browsers inherit their environment from.
os.environ.pop("DYLD_LIBRARY_PATH", None)


def _free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.fixture(scope="session")
def base_url():
    port = _free_port()
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1", "--directory", str(APP_DIR)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    deadline = time.monotonic() + 10
    while True:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                break
        except OSError:
            if server.poll() is not None or time.monotonic() > deadline:
                server.kill()
                raise RuntimeError(f"Test server on port {port} did not start")
            time.sleep(0.05)
    yield f"http://127.0.0.1:{port}"
    server.terminate()
    server.wait(timeout=5)


# The dataset the "not categorized yet" tests treat as uncategorized. It is categorized for real, so the fake below is
# what the tests exercise, and they keep working once every dataset has been categorized.
UNCATEGORIZED = "gpcp-daily"


@pytest.fixture
def uncategorized(page):
    """Serve the R* data with UNCATEGORIZED's categorization taken out, as build_data.py writes a dataset folder that
    has no JSON file yet. Returns that dataset's id."""
    def strip_categorization(route):
        body = route.fetch().text()
        body += (
            "\n(function () {\n"
            f"  const d = window.RSTAR_DATA.datasets.find((x) => x.id === {json.dumps(UNCATEGORIZED)});\n"
            "  d.file = null;\n"
            "  d.categorizations = null;\n"
            "  d.scores = null;\n"
            "})();\n"
        )
        route.fulfill(body=body, content_type="application/javascript")

    page.route("**/data/rstar-data.js", strip_categorization)
    return UNCATEGORIZED


@pytest.fixture
def console_errors(page):
    """Collect console errors and uncaught page errors for a test to assert on."""
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda exc: errors.append(str(exc)))
    return errors
