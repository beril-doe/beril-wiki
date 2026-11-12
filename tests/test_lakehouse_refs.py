"""Done check 2: every database and table a question names passes the committed catalog,
an *existing* verdict always names one, and the publish rule never shows a guess as
*existing*. No LLM calls, no network.

uv run pytest tests/test_lakehouse_refs.py
"""

from __future__ import annotations

import json

import pytest

from beril_wiki import lakehouse
from beril_wiki.agentic.runtime import CandidateError
from beril_wiki.paths import ROOT
from beril_wiki.publish.cards.corpus import Corpus, join, split
from beril_wiki.publish.cards.export import export
from beril_wiki.publish.cards.pages import beril_prompt, direction_page, follow_fields
from beril_wiki.stages import cards as cards_stage
from beril_wiki.stages import classify, followups
from test_reader_pages import card_corpus

DID = "transport--abc123"
TABLE = "kescience.fitnessbrowser.experiment"


def reply(**fields) -> str:
    base = {
        "need": "existing",
        "first_step_existing": False,
        "data_unclear": False,
        "reason": "The fitness experiment table decides whether the genes move nutrients.",
        "tables": [TABLE],
    }
    return json.dumps(base | fields)


def test_committed_names_pass_the_catalog():
    cat = lakehouse.load(ROOT)
    for page in (ROOT / "wiki/directions").glob("*.md"):
        fields, _ = cards_stage.read_page(page)
        for name in (fields.get("databases") or []) + (fields.get("tables") or []):
            assert cat.exists(name), (page.name, name)
    for qid, entry in json.loads((ROOT / "state/followups.json").read_text()).items():
        for name in entry.get("tables") or []:
            assert cat.exists(name), (qid, name)


def test_every_existing_verdict_names_a_table():
    c = Corpus(ROOT)
    for did, (fields, _) in c.directions.items():
        f = follow_fields(fields | {"_id": did}, c)
        if f["follow"] == "existing":
            assert f["tables"], did
    # Raw entries keyed for today's pack must name one too; pre-rerun entries carry older keys.
    cat = lakehouse.load(ROOT)
    state = json.loads((ROOT / "state/followups.json").read_text())
    policy = cards_stage.policy(classify.status_config(ROOT), ("labels", "card_review"))
    for qid, pack in followups.packs(ROOT, cat).items():
        entry = state.get(qid, {})
        current = entry.get("input") == classify.item_key(pack, followups.PROMPT_TAG, policy)
        if current and entry.get("need") == "existing" and not entry.get("failed"):
            assert entry.get("tables"), qid


def test_checker_rejects_missing_tables_and_absence_claims():
    parse = followups.checker({}, lakehouse.load(ROOT))
    with pytest.raises(CandidateError, match="kescience.fitnessbrowser.no_such_table"):
        parse(reply(tables=["kescience.fitnessbrowser.no_such_table"]))
    with pytest.raises(CandidateError, match="lakehouse lacks data"):
        parse(
            reply(
                need="outside",
                tables=[],
                reason="Deciding it needs isolates, and the lakehouse does not hold them.",
            )
        )


@pytest.mark.parametrize(
    "entry",
    [
        None,
        {"need": "existing", "tables": [TABLE], "reason": "r", "failed": True},
        {"need": "existing", "tables": [], "reason": "r"},
        # A followups@1 answer, made before the catalog existed, has no tables field.
        {"need": "experiment", "first_step_existing": True, "data_unclear": True, "reason": "r"},
    ],
    ids=["missing", "failed", "no-table", "pre-catalog"],
)
def test_unchecked_never_reads_existing(tmp_path, entry):
    kb = tmp_path / "kb"
    card_corpus(kb)
    page = kb / f"wiki/directions/{DID}.md"
    fields, body = split(page.read_text())
    assert fields["approach"] == "lakehouse analysis" and fields["tables"] == [TABLE]
    # A pre-catalog readiness note that claims absence, on the page's Data line too.
    absent = "Fitness data under these conditions are not in the lakehouse."
    fields["readiness_basis"] = absent
    data = f"\n## Data\n\nApproach: lakehouse analysis. Readiness: needs compute. {absent}\n"
    page.write_text(join(fields, body + data))
    if entry is not None:
        (kb / "state/followups.json").write_text(json.dumps({DID: entry}))
    c = Corpus(kb)
    f = follow_fields(fields | {"_id": DID}, c)
    assert f["follow"] == "unchecked" and f["follow_text"] == "Not checked yet"
    assert f["first_step"] is False and f["data_unclear"] is False
    # Not checked yet makes no data claim: no table list, hedge, named data or readiness note.
    published, text = split(direction_page(DID, c))
    assert published["tables"] == [] and published["databases"] == []
    assert "readiness_basis" not in published
    assert "Databases: none named; tables: none named." in published["beril_prompt"]
    assert "An AI model matched" not in text and "`experiment`" not in text
    out = export(c)["research_directions"][0]
    assert out["tables"] == [] and out["databases"] == [] and out["readiness_basis"] is None
    for where in (text, published["beril_prompt"], published["brief"], json.dumps(out)):
        assert "not in the lakehouse" not in where and TABLE not in where


def test_prompt_and_export_carry_the_tables(tmp_path):
    kb = tmp_path / "kb"
    card_corpus(kb)
    page = kb / f"wiki/directions/{DID}.md"
    fields, body = split(page.read_text())
    # Only the followup names the table, so the prompt and export must read the checked list.
    page.write_text(
        join({k: v for k, v in fields.items() if k not in ("databases", "tables")}, body)
    )
    entry = json.loads(reply()) | {"tables": [TABLE]}
    (kb / "state/followups.json").write_text(json.dumps({DID: entry}))
    c = Corpus(kb)
    fields, body = c.directions[DID]
    prompt = beril_prompt(fields | {"_id": DID}, body, c)
    assert f"Databases: kescience.fitnessbrowser; tables: {TABLE}." in prompt
    out = export(c)["research_directions"][0]
    assert out["tables"] == [TABLE] and out["databases"] == ["kescience.fitnessbrowser"]
    assert out["follow"] == "existing" and "collections" not in out
