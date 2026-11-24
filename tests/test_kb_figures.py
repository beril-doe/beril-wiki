"""Check figure scheduling, the record gate and the publisher's input offline."""

import json
from hashlib import sha256
from pathlib import Path

import pytest

from beril_wiki.kb.jobs import Scope
from beril_wiki.kb.jobs import figures as jobs
from beril_wiki.kb.tools import Rejected, rehome_figures
from beril_wiki.publish.ingest import splice_figures

SUMMARY = "summaries/alpha__REPORT"
TOPIC = "topics/yields"
CONFLICT = "conflicts/yield-disagreement"
PAGE = "# Growth yield\n\nThe assay measured growth [src: alpha].\n"
EMBED = "runs/assay/out/yield.png"
CAPTION = "Distribution of growth yields"
CONTEXT = "The assay measured growth."


def put(root: Path, name: str, text: str) -> Path:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


@pytest.fixture
def scope(tmp_path: Path) -> Scope:
    put(tmp_path, f"wiki/{SUMMARY}.md", PAGE)
    report = f"# Report\n\n{CONTEXT}\n![{CAPTION}]({EMBED})\n"
    put(tmp_path, "corpus/projects/alpha/REPORT.md", report)
    put(tmp_path, f"corpus/projects/alpha/{EMBED}", "figure bytes")
    return Scope(tmp_path, "alpha", "ingest", run="test", created=[SUMMARY])


def test_only_touched_eligible_pages_without_current_placements_are_owed(scope: Scope) -> None:
    root = scope.root
    put(root, f"wiki/{TOPIC}.md", PAGE)
    conflict = put(root, f"wiki/{CONFLICT}.md", PAGE)
    put(root, "wiki/summaries/other__REPORT.md", PAGE)
    put(root, "wiki/concepts/growth.md", PAGE)
    scope.edited = [f"{TOPIC}#lead", f"{TOPIC}#results", f"{CONFLICT}#lead", "concepts/growth#lead"]
    placements = {
        f"{page}.md": {"page_hash": sha256(PAGE.encode()).hexdigest()[:16], "placements": []}
        for page in (TOPIC, CONFLICT)
    }
    put(root, "state/figures-placements.json", json.dumps(placements))

    edited = PAGE + "\nA second paragraph.\n"
    rehome_figures(scope.store, TOPIC, PAGE, edited)
    put(root, f"wiki/{TOPIC}.md", edited)
    conflict.write_text(edited, encoding="utf-8")
    owed = jobs.jobs(scope)
    assert [job.key for job in owed] == [f"figures/{CONFLICT}", f"figures/{SUMMARY}"]
    assert owed[0].pack["CANDIDATE_FIGURES"][0]["project"] == "alpha"

    for job in owed:
        job.publish(job.check({"placements": []}))
    assert jobs.jobs(scope) == []


@pytest.mark.parametrize(
    "record",
    [
        {"placements": [{"figure": 1, "after_paragraph": 0}]},
        {"placements": [{"figure": 0, "after_paragraph": 2}]},
        {"placements": [{"figure": True, "after_paragraph": 0}]},
        {"placements": [], "csv_flags": [42]},
    ],
    ids=["unknown-figure", "unknown-paragraph", "boolean-index", "non-string-flag"],
)
def test_job_gate_rejects_invalid_curator_replies(scope: Scope, record: dict) -> None:
    (job,) = jobs.jobs(scope)
    with pytest.raises(Rejected, match="the record fails its checks") as caught:
        job.check(record)
    assert caught.value.objections == ["invalid placement schema or indices"]


def test_publish_preserves_the_curator_shapes_and_publisher_can_splice(scope: Scope) -> None:
    root = scope.root
    other = "topics/unrelated.md"
    prior = {"page_hash": "keep", "placements": [], "csv_flags": []}
    path = put(root, "state/figures-placements.json", json.dumps({other: prior}))
    state = put(root, "state/figures-state.json", json.dumps({other: "existing"}))
    old_manifest = {"beta": [{"file": "figures/other.png", "caption": "Other", "context": ""}]}
    manifest = put(root, "state/figures-manifest.json", json.dumps(old_manifest))
    legacy = put(
        root,
        "state/agentic.json",
        json.dumps({"core_outputs": {}, "figure_outputs": {"state/figures-placements.json": ""}}),
    )

    (job,) = jobs.jobs(scope)
    assert (job.writer, job.reviewer) == ("figures", "")
    assert json.loads(manifest.read_text()) == old_manifest | {
        "alpha": [{"file": EMBED, "caption": CAPTION, "context": CONTEXT}],
    }
    assert (root / "wiki/figures/alpha" / EMBED).read_bytes() == b"figure bytes"
    placement = {"figure": 0, "after_paragraph": 1, "caption": "Writer-supplied caption"}
    job.publish(job.check({"placements": [placement] * 3, "csv_flags": ["Plot the counts."] * 4}))

    entry = {
        "page_hash": sha256(PAGE.encode()).hexdigest()[:16],
        "placements": [
            {"project": "alpha", "file": EMBED, "after_paragraph": 1, "caption": CAPTION}
        ]
        * 2,
        "csv_flags": ["Plot the counts."] * 3,
    }
    assert json.loads(path.read_text()) == {other: prior, f"{SUMMARY}.md": entry}
    assert json.loads(state.read_text()) == {other: "existing", f"{SUMMARY}.md": "kb:test"}
    accepted = json.loads(legacy.read_text())
    assert accepted["core_outputs"][f"wiki/{SUMMARY}.md"] == sha256(PAGE.encode()).hexdigest()
    assert (
        accepted["figure_outputs"]["state/figures-placements.json"]
        == sha256(path.read_bytes()).hexdigest()
    )
    out = root / "published"
    rendered = splice_figures(PAGE, entry, root, out)
    assert f"![{CAPTION}](../figures/alpha/{EMBED})" in rendered
    assert (out / "figures/alpha" / EMBED).read_bytes() == b"figure bytes"
