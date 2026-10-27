"""Model routing, scope files and shared helpers for the finding and research-direction stages."""

import json
import os
import re

from beril_wiki.agentic import runtime as R
from beril_wiki.stages import cards


def test_card_steps_route_to_their_roles():
    assert R.role_for("headlines/truly_dark_genes") == "cards"
    assert R.role_for("headlines/truly_dark_genes/repair") == "cards"
    assert R.role_for("novelty/x--1a2b3c4d/judge") == "cards"
    assert R.role_for("novelty/x--1a2b3c4d/queries") == "queries"
    assert R.role_for("novelty/x--1a2b3c4d/agree") == "review"
    assert R.role_for("directions/topic") == "cards"
    assert R.role_for("directions/topic/science-review") == "review"
    assert R.role_for("directions/topic/verify") == "review"
    # Existing routes are untouched.
    assert R.role_for("lit/hub/queries") == "queries"
    assert R.role_for("conflicts/conflict--x") == "writing"


def test_card_files_do_not_rekey_jobs(tmp_path):
    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("rules")
    before = R.contract_manifest(tmp_path)
    (tmp_path / "contract/cards.yaml").write_text("topics: []\nreports: []\n")
    (tmp_path / "contract/novelty-decisions.yaml").write_text("decisions: []\n")
    assert R.contract_manifest(tmp_path) == before


def test_cards_effort_is_medium(tmp_path):
    agent = R.Runtime(
        {"root": str(tmp_path), "store": str(tmp_path), "run": "r", "max_tokens": 1, "max_jobs": 1}
    )
    assert agent.effort("headlines/x") == "medium"
    assert agent.effort("novelty/x/judge") == "medium"
    assert agent.effort("novelty/x/agree") is None
    assert agent.effort("conflicts/x") is None


def test_cards_role_is_configurable():
    policy = R.model_policy({"model": "m", "step_models": {"cards": "claude-sonnet-5-5"}})
    assert policy["cards"] == "claude-sonnet-5-5"


def blob(store, name, source, sha, findings, mtime):
    path = store / "evidence" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"coverage": [{"source": source, "sha256": sha}], "findings": findings})
    )
    os.utime(path, (mtime, mtime))


def test_source_evidence_requires_matching_hash(tmp_path):
    report = tmp_path / "wiki/sources/a__REPORT.md"
    report.parent.mkdir(parents=True)
    report.write_text("Yield was 42%.")
    current = R.file_hash(report)
    old = {"id": "a:0:0", "source": "a", "kind": "finding", "quote": "old"}
    new = {"id": "a:0:0", "source": "a", "kind": "finding", "quote": "Yield was 42%."}
    blob(tmp_path, "newer.json", "a__REPORT.md", "stale", [old], 200)
    blob(tmp_path, "older.json", "a__REPORT.md", current, [new], 100)
    assert cards.source_evidence(tmp_path, tmp_path, ["a"]) == {"a": [new]}
    report.write_text("Yield was 43%.")
    assert cards.source_evidence(tmp_path, tmp_path, ["a"]) == {}


def test_finding_id_ignores_chunk_offsets():
    assert cards.finding_id("a", "Yield  was\n42%.") == cards.finding_id("a", "yield was 42%.")
    assert cards.finding_id("a", "x") != cards.finding_id("b", "x")
    assert re.fullmatch(r"a--[0-9a-f]{8}", cards.finding_id("a", "x"))


def test_bullets_reads_numbered_and_dashed_items():
    text = (
        "# R\n\n## Future Directions\n\n1. **Structure**: run ESMFold\n   on 100 genes.\n"
        "2. Assay growth.\n\n## References\n\n- Price 2018\n\n## Open Directions\n- Re-run it.\n"
    )
    found = cards.bullets(text, re.compile(r"Future Directions|Open Directions"))
    assert found == ["**Structure**: run ESMFold on 100 genes.", "Assay growth.", "Re-run it."]


def test_new_figures_flags_new_numbers():
    pool = "Odds ratio 0.53 across 7,609 genes [src: a]"
    assert cards.new_figures("OR 0.53 in 7609 genes", pool) == []
    assert cards.new_figures("OR 0.61 in 7,609 genes", pool) == ["0.61"]


def test_topic_concepts_reads_curator_groups(tmp_path):
    (tmp_path / "state").mkdir()
    (tmp_path / "state/curator-topics.json").write_text(
        json.dumps({"groups": [{"title": "Functional Dark Matter", "concepts": ["b", "a"]}]})
    )
    assert cards.topic_concepts(tmp_path, "functional-dark-matter") == ["a", "b"]
    assert cards.topic_concepts(tmp_path, "other") == []


def test_check_flags_card_errors(tmp_path):
    from beril_wiki.check import card_errors

    source = "Dark genes were depleted (odds ratio 0.53) across 7,609 genes."
    wiki = tmp_path / "wiki"
    cards.write_page(
        wiki / "findings/a--1a2b3c4d.md",
        {"finding_id": "a--1a2b3c4d", "source": "a", "quantities": [{"value": "0.61"}]},
        "# T\n\n## Evidence\n\n> Dark genes were depleted (odds ratio 0.53) [src: a]\n",
    )
    cards.write_page(
        wiki / "directions/s--abc123.md",
        {"collections": ["kbase-nope"], "builds_on": ["findings/gone"], "papers": ["777"]},
        "# Recompute the stress rates\n\nWhy?\n",
    )
    (wiki / "data").mkdir()
    (tmp_path / "state").mkdir()
    (tmp_path / "state/novelty.json").write_text(
        json.dumps(
            {
                "a--1a2b3c4d": {"label": "Novel!", "closest": [{"pmid": "9"}], "candidates": []},
                "a--gone0000": {"label": "Not assessed"},
            }
        )
    )
    errors = "\n".join(card_errors(tmp_path, {"a": source}))
    assert "key figure '0.61'" in errors
    assert "unknown label 'Novel!'" in errors
    assert "PMID 9 was not retrieved" in errors
    assert "a--gone0000: no such finding" in errors
    assert "collection 'kbase-nope'" in errors
    assert "builds on 'findings/gone'" in errors
    assert "PMID 777 is not a closest paper" in errors
    assert "asks to redo existing work" in errors
    assert "quote is not verbatim" not in errors


def test_existing_stage_revisions_ignore_cards_module(tmp_path, monkeypatch):
    """Editing the card helpers must not make conflicts, topics, literature or authors stale."""
    from beril_wiki.agentic import curator as C

    (tmp_path / "contract").mkdir()
    config = {"model": "m"}
    before = {name: C.stage_revision(tmp_path, name, config) for name in C.EDITORIAL}
    real = C.Path.read_text

    def edited(self, *args, **kwargs):
        text = real(self, *args, **kwargs)
        return text + "\nEDITED = 1\n" if self.name == "cards.py" else text

    monkeypatch.setattr(C.Path, "read_text", edited)
    after = {name: C.stage_revision(tmp_path, name, config) for name in C.EDITORIAL}
    for name in ("conflicts", "topics", "literature", "authors"):
        assert after[name] == before[name]
    for name in C.CARD_STAGES:
        assert after[name] != before[name]


def test_cards_command_runs_only_card_stages(tmp_path, monkeypatch):
    from beril_wiki.agentic import __main__ as cli

    (tmp_path / "state").mkdir()
    (tmp_path / "state/agentic.json").write_text('{"accepted": true}')
    calls = []
    monkeypatch.setattr(
        cli, "run_stage", lambda root, path, name, module, args: calls.append((name, args))
    )
    config = {"model": "m", "max_tokens": 10, "max_jobs": 1, "cli": "unused"}
    cli.run_cards(tmp_path, config)
    assert calls == [
        ("headlines", []),
        ("novelty", []),
        ("directions", []),
        ("check", [str(tmp_path), "--strict"]),
    ]
    assert (tmp_path / "state/agentic.json").read_text() == '{"accepted": true}'
    saved = json.loads((tmp_path / ".agentic/config.json").read_text())
    assert saved["root"] == str(tmp_path) and saved["run"]


def test_parse_reply_reads_the_first_of_repeated_objects():
    from beril_wiki.stages.novelty import Queries

    raw = '{"queries": ["a"]}\n{"queries": ["b"]}'
    assert cards.parse_reply(raw, Queries).queries == ["a"]


def test_cli_imports_in_a_fresh_interpreter():
    """stages.topics imports publish.ingest, which reaches the card helpers: no cycle."""
    import subprocess
    import sys

    for module in (
        "beril_wiki.agentic.__main__",
        "beril_wiki.stages.topics",
        "beril_wiki.publish.ingest",
    ):
        done = subprocess.run(
            [sys.executable, "-c", f"import {module}"], capture_output=True, text=True
        )
        assert done.returncode == 0, done.stderr[-800:]


def test_scope_all_resolves_to_every_report_and_topic(tmp_path):
    (tmp_path / "wiki/sources").mkdir(parents=True)
    for sid in ("b", "a"):
        (tmp_path / "wiki/sources" / f"{sid}__REPORT.md").write_text("# R\n")
    (tmp_path / "wiki/sources/a__notes.md").write_text("not a report\n")
    (tmp_path / "state").mkdir()
    (tmp_path / "state/curator-topics.json").write_text(
        json.dumps({"groups": [{"title": "Dark Matter", "concepts": ["gap"]}]})
    )
    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/cards.yaml").write_text("topics: all\nreports: all\n")
    scope = cards.load_scope(tmp_path)
    assert scope is not None
    assert scope.reports == ["a", "b"] and scope.topics == ["dark-matter"]
