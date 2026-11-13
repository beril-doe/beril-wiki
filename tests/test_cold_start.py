"""A checkout without an accepted run refuses to curate unless the cold start is meant."""

from __future__ import annotations

import pytest

from beril_wiki.agentic import runner


def test_run_refuses_without_accepted_state_or_the_override(tmp_path, monkeypatch):
    monkeypatch.delenv("BERIL_WIKI_ALLOW_COLD_START", raising=False)
    with pytest.raises(runner.WorkflowError, match="re-integrate every source"):
        runner.check_warm_start(tmp_path)
    with pytest.raises(runner.WorkflowError, match="BERIL_WIKI_ALLOW_COLD_START"):
        runner.run(tmp_path, tmp_path / "checkout", {"cli": "unused"})
    (tmp_path / "state").mkdir()
    (tmp_path / "state/agentic.json").write_text("{}")
    runner.check_warm_start(tmp_path)  # the volume is mounted: fine
    (tmp_path / "state/agentic.json").unlink()
    monkeypatch.setenv("BERIL_WIKI_ALLOW_COLD_START", "1")
    runner.check_warm_start(tmp_path)  # deliberate first run
