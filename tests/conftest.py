"""Offline tests replay page sessions from recorded replies instead of starting the SDK."""

import pytest

from agentic_recording import page_session
from beril_wiki.agentic import page_agent


@pytest.fixture(autouse=True)
def recorded_page_sessions(monkeypatch):
    monkeypatch.setattr(page_agent, "run", page_session)


@pytest.fixture(autouse=True)
def cold_starts_are_deliberate(monkeypatch):
    """Every offline test starts from an empty tree; the runner's cold-start guard is for
    pods that lost their volume (tests/test_cold_start.py exercises it)."""
    monkeypatch.setenv("BERIL_WIKI_ALLOW_COLD_START", "1")
