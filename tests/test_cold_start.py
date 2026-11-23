"""A checkout without an accepted run refuses to curate unless the cold start is meant."""

from __future__ import annotations

import json

import pytest

from beril_wiki.agentic import runner

CONFIG = {"cli": "unused", "model": "claude-test"}


def test_run_refuses_without_accepted_state_or_the_override(tmp_path, monkeypatch):
    monkeypatch.delenv("BERIL_WIKI_ALLOW_COLD_START", raising=False)
    with pytest.raises(runner.WorkflowError, match="re-integrate every source"):
        runner.check_warm_start(tmp_path)
    with pytest.raises(runner.WorkflowError, match="BERIL_WIKI_ALLOW_COLD_START"):
        runner.run(tmp_path, tmp_path / "checkout", CONFIG)
    (tmp_path / "state").mkdir()
    (tmp_path / "state/agentic.json").write_text("{}")
    runner.check_warm_start(tmp_path)  # the volume is mounted: fine
    (tmp_path / "state/agentic.json").unlink()
    monkeypatch.setenv("BERIL_WIKI_ALLOW_COLD_START", "1")
    runner.check_warm_start(tmp_path)  # deliberate first run


@pytest.mark.parametrize("value", ["0", "false", "no", "off", "", " "])
def test_a_false_override_keeps_the_guard(tmp_path, monkeypatch, value):
    monkeypatch.setenv("BERIL_WIKI_ALLOW_COLD_START", value)
    with pytest.raises(runner.WorkflowError, match="re-integrate every source"):
        runner.check_warm_start(tmp_path)
    monkeypatch.setenv("BERIL_WIKI_ALLOW_COLD_START", "TRUE")
    runner.check_warm_start(tmp_path)


def test_an_interrupted_promotion_is_recovered_before_the_guard(tmp_path, monkeypatch):
    """Killed between promotion's renames, the accepted state sits in .agentic/work;
    that is a recovery, not a cold start."""
    monkeypatch.delenv("BERIL_WIKI_ALLOW_COLD_START", raising=False)
    work = tmp_path / ".agentic/work"
    for folder in runner.TREES:
        (work / folder).mkdir(parents=True)
    (work / "state/agentic.json").write_text(json.dumps({"fingerprint": "f1"}))
    candidate = {folder: runner.manifest(work, (folder,)) for folder in runner.TREES}
    (tmp_path / ".agentic/promotion.json").write_text(
        json.dumps({"candidate": candidate, "before": {f: {} for f in runner.TREES}})
    )
    with pytest.raises(Exception) as caught:
        runner.run(tmp_path, tmp_path / "checkout", CONFIG)
    assert "re-integrate every source" not in str(caught.value)
    assert json.loads((tmp_path / "state/agentic.json").read_text()) == {"fingerprint": "f1"}
    assert not (tmp_path / ".agentic/promotion.json").exists()
