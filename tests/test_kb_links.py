"""Scoped record jobs for related findings, project references and shared statements."""

from pathlib import Path

import pytest

from beril_wiki.kb.jobs import Scope, write_state
from beril_wiki.kb.jobs import links as links_jobs
from beril_wiki.kb.jobs import shared as shared_jobs
from beril_wiki.kb.tools import Rejected
from beril_wiki.stages import cards, links, shared

A, B, C, D = "alpha--11111111", "beta--22222222", "gamma--33333333", "delta--44444444"
PAIR_LABEL = "Both report how often essential genes are core"
REF_LABEL = "Uses the other project's gene fitness measurements"


def _put(root: Path, name: str, body: str) -> None:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def _finding(root: Path, fid: str, report: str) -> None:
    cards.write_page(
        root / "wiki" / "findings" / f"{fid}.md",
        {"source": report, "description": "Essential genes are mostly core genes."},
        "# Essential genes are mostly core\n\n## Evidence\n\n> Essential genes were 82% core.",
    )


@pytest.fixture
def scope(tmp_path: Path) -> Scope:
    for fid, sid, text in (
        (A, "alpha", "We use fitness measurements from beta."),
        (B, "beta", "A filename contains alpha."),
        (C, "gamma", "We compare a published result from delta."),
        (D, "delta", "We measured gene fitness."),
    ):
        _finding(tmp_path, fid, sid)
        _put(tmp_path, f"wiki/sources/{sid}__REPORT.md", f"# Report: {sid.title()} study\n\n{text}")
    for concept in ("core", "fitness"):
        _put(tmp_path, f"wiki/concepts/{concept}.md", "Results [src: alpha, beta].")
        _put(tmp_path, f"wiki/concepts/other-{concept}.md", "Results [src: gamma, delta].")
    write_state(
        tmp_path / "state/curator-topics.json",
        {
            "groups": [
                {"title": "Core", "concepts": ["core", "other-core"]},
                {"title": "Fitness", "concepts": ["fitness", "other-fitness"]},
            ]
        },
    )
    return Scope(root=tmp_path, source="alpha", reason="ingest", run="run-1")


def _reply(id_: str, relation: str, label: str) -> dict:
    return {"items": [{"id": id_, "relation": relation, "label": label}]}


def test_links_ask_only_unanswered_pairs_and_references_involving_this_report(scope: Scope):
    path = scope.root / links.STATE
    other = {"input": "old-curator-hash", "relation": "same result", "label": PAIR_LABEL}
    write_state(
        path,
        {"candidates": {f"pair:{D}|{C}": other, "ref:alpha>beta": {"failed": True}}},
    )

    pair, outgoing, incoming = links_jobs.jobs(scope)
    assert pair.key.startswith("links/pairs-")
    assert pair.pack["PAIRS"]["P1"]["B"]["report"] == "beta"
    assert outgoing.pack["REPORT"] == "Alpha study" and incoming.pack["REPORT"] == "Beta study"
    assert all(
        (job.writer, job.reviewer) == ("cards", "card_review") for job in (pair, outgoing, incoming)
    )

    with pytest.raises(Rejected) as rejected_pair:
        pair.check(_reply("P1", "same result", "Essential genes were 99% core in both projects"))
    assert "figures the inputs never state" in str(rejected_pair.value.objections)
    with pytest.raises(Rejected) as rejected_ref:
        outgoing.check(_reply("R1", "uses its data or methods", "Uses its fitness data"))
    assert "say whose data" in str(rejected_ref.value.objections)

    pair.publish(pair.check(_reply("P1", "same result", f" {PAIR_LABEL} ")))
    outgoing.publish(outgoing.check(_reply("R1", "uses its data or methods", REF_LABEL)))
    incoming.publish(incoming.check(_reply("R1", "not a reference", "")))
    state = cards.load_state(path)
    # A reference remembers the sentences it was judged from, so a revision that
    # rewrites them is asked again.
    assert all(
        bool(state["candidates"][key].pop("lines")) for key in ("ref:alpha>beta", "ref:beta>alpha")
    )
    assert state == {
        "candidates": {
            f"pair:{A}|{B}": {"input": "kb:run-1", "relation": "same result", "label": PAIR_LABEL},
            f"pair:{D}|{C}": other,
            "ref:alpha>beta": {
                "input": "kb:run-1",
                "relation": "uses its data or methods",
                "label": REF_LABEL,
            },
            "ref:beta>alpha": {"input": "kb:run-1", "relation": "not a reference", "label": ""},
        },
        "links": [
            {"a": A, "b": B, "level": "finding", "type": "same result", "label": PAIR_LABEL},
            {"a": D, "b": C, "level": "finding", "type": "same result", "label": PAIR_LABEL},
            {
                "a": "alpha",
                "b": "beta",
                "level": "project",
                "type": "uses its data or methods",
                "label": REF_LABEL,
            },
        ],
    }
    state = cards.load_state(path)
    state["candidates"][f"pair:{A}|{B}"]["input"] = "old-curator-hash"
    write_state(path, state)
    assert (
        links_jobs.jobs(Scope(scope.root, "alpha", "revise", run="run-2", models={"cards": "new"}))
        == []
    )

    (scope.root / "wiki" / "findings" / f"{A}.md").unlink()
    assert links_jobs.jobs(scope) == []
    links_jobs.after(scope, {})
    remaining = cards.load_state(path)
    assert [row["a"] for row in remaining["links"]] == [D, "alpha"]
    assert remaining["candidates"][f"pair:{D}|{C}"] == other


def test_links_split_oversized_batches_and_keep_references_with_their_citing_report(scope: Scope):
    for n in range(links.BATCH):
        _finding(scope.root, f"alpha--extra{n}", "alpha")
        sid = f"extra{n}"
        _put(scope.root, f"wiki/sources/{sid}__REPORT.md", f"# Report: {sid} study\n")
    targets = " ".join(f"extra{n}" for n in range(links.BATCH))
    _put(
        scope.root,
        "wiki/sources/alpha__REPORT.md",
        f"# Report: Alpha study\n\nCites beta and {targets}.",
    )

    jobs = links_jobs.jobs(scope)
    pair_batches = [job.pack["PAIRS"] for job in jobs if "PAIRS" in job.pack]
    assert [list(batch) for batch in pair_batches] == [
        [f"P{n}" for n in range(1, links.BATCH + 1)],
        ["P1"],
    ]
    refs = [(job.pack["REPORT"], list(job.pack["NAMED"])) for job in jobs if "NAMED" in job.pack]
    assert refs == [
        ("Alpha study", [f"R{n}" for n in range(1, links.BATCH + 1)]),
        ("Alpha study", ["R1"]),
        ("Beta study", ["R1"]),
    ]


def test_shared_checks_and_stores_only_missing_statements_for_this_reports_groups(scope: Scope):
    links_path = scope.root / links.STATE
    other_link = {"a": D, "b": C, "level": "finding", "type": "same result", "label": PAIR_LABEL}
    own_link = other_link | {"a": A, "b": B, "type": "similar comparison, different scope"}
    write_state(links_path, {"links": [own_link, other_link]})
    state_path = scope.root / shared.STATE
    group = shared.group_id([A, B])
    other_group = shared.group_id([D, C])
    unrelated = {"input": "old-curator-hash", "failed": True}
    write_state(state_path, {group: {"failed": True}, other_group: unrelated})

    (job,) = shared_jobs.jobs(scope)
    assert job.key == f"shared/{group}"
    assert (job.writer, job.reviewer) == ("cards", "card_review")
    assert list(job.pack["RESULTS"]) == [A, B]
    assert job.pack["RELATION"] == own_link["type"] and job.pack["LINKS"] == [PAIR_LABEL]
    reply = {
        "title": "Essential genes across genomes",
        "sentence": "The projects share an analysis of how often essential genes are core.",
        "question": "How often are essential genes core?",
        "lanes": {A: "Essential genes", B: "Core genes"},
        "how": "Both reports draw on the same analysis of shared data.",
    }
    with pytest.raises(Rejected) as rejected:
        job.check(reply | {"lanes": {A: "Essential genes"}})
    assert "lanes must name exactly these result ids" in str(rejected.value.objections)

    job.publish(job.check(reply))
    assert cards.load_state(state_path) == {
        group: reply
        | {
            "input": "kb:run-1",
            "members": [A, B],
            "projects": ["alpha", "beta"],
            "topics": ["core", "fitness"],
            "relation": "similar comparison, different scope",
        },
        other_group: unrelated,
    }
    assert shared_jobs.jobs(Scope(scope.root, "alpha", "revise", run="run-2")) == []
