"""Offline tests replay page sessions from recorded replies instead of starting the SDK."""

import pytest

from agentic_recording import page_session
from beril_wiki.agentic import page_agent


@pytest.fixture(autouse=True)
def recorded_page_sessions(monkeypatch):
    monkeypatch.setattr(page_agent, "run", page_session)
