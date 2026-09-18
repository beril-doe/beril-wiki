"""Packed-evidence prose: gates, one-turn review, paragraph patches, no-halt failures."""

import json
from types import SimpleNamespace

import pytest

from beril_wiki.agentic import prose as P

CONTRACT = P.Contract(
    rules=("Use only input figures.", "Begin with the H1."),
    words=(20, 60),
    headings=("## Sides",),
)
SOURCES = {"a": "Yield was 42%.", "b": "Yield was 56%."}
GOOD = (
    "# Title\n\nLead sentence about yield without figures here at all today.\n\n## Sides\n\n"
    "Yield was 42%. [src: a]\n\nYield was 56%. [src: b]\n\nClosing words to reach the range now."
)


class Stub:
    """A scripted runtime: replies by step, recording every prompt and job key."""

    def __init__(self, script):
        self.script, self.prompts, self.jobs = script, [], []

    def ask(self, messages, step):
        self.prompts.append((step, "\n".join(m["content"] for m in messages)))
        self.jobs.append(f"key:{step}")
        answer = self.script[step]
        return answer(messages) if callable(answer) else answer


def configure(monkeypatch, tmp_path, script, workers=1):
    stub = Stub(script)
    monkeypatch.setattr(P, "configured", lambda: True)
    # Every runtime() call is a fresh connection in production; the page must keep one.
    monkeypatch.setattr(P, "runtime", lambda: stub if stub.prompts == [] else Stub(script))
    monkeypatch.setattr(P, "runtime_config", lambda: {"store": str(tmp_path), "workers": workers})
    return stub


def run(step, **kwargs):
    return P.derived_page(
        step,
        CONTRACT,
        "Write it.",
        "EVIDENCE PACK",
        allowed=GOOD,
        sources=SOURCES,
        valid_ids={"a", "b"},
        **kwargs,
    )


def test_gate_reports_mechanical_issues_by_paragraph():
    text = (
        "Here is the page you asked for.\n\n# Title\n\nCoverage was 99% in the atlas. [src: c]"
        "\n\nRate was 42%.\n\nYield was 56%. [src: a]"
    )
    issues = P.gate(text, CONTRACT, allowed=GOOD, sources=SOURCES, valid_ids={"a", "b"})
    found = {(i.paragraph, i.category, i.quote) for i in issues}
    assert (0, "format", "Here is the page you asked for.") in found
    assert (None, "format", "") in found  # missing ## Sides
    assert (2, "number", "99%") in found  # imported figure
    assert (2, "citation", "[src: c]") in found
    assert (3, "citation", "Rate was 42%.") in found  # figure without a tag
    assert (4, "number", "56%") in found  # cited source a does not state 56%
    short = P.gate("# T\n\n## Sides\n\nShort.", CONTRACT, allowed="", sources={}, valid_ids=set())
    assert [i.category for i in short] == ["length"]
    assert P.gate(GOOD, CONTRACT, allowed=GOOD, sources=SOURCES, valid_ids={"a", "b"}) == []


def test_gate_failure_is_patched_before_any_review(monkeypatch, tmp_path):
    draft = GOOD.replace("Yield was 42%. [src: a]", "Yield was 42% of 8,314 loci. [src: a]")

    def fix(messages):
        assert '"quote": "8,314"' in messages[1]["content"]
        base = messages[1]["content"].split("base_hash ")[1].split(")")[0]
        return json.dumps({"base_hash": base, "paragraphs": {"3": "Yield was 42%. [src: a]"}})

    stub = configure(
        monkeypatch,
        tmp_path,
        {"x": draft, "x/patch/1": fix, "x/patch/1/review": '{"accepted": true, "issues": []}'},
    )
    assert run("x") == GOOD
    assert [s for s, _ in stub.prompts] == ["x", "x/patch/1", "x/patch/1/review"]
    assert "Review every paragraph." in stub.prompts[-1][1]


def test_review_rejection_patches_and_rereviews_only_changed_paragraphs(monkeypatch, tmp_path):
    verdicts = iter(
        [
            {
                "accepted": False,
                "issues": [
                    {
                        "paragraph": 4,
                        "category": "direction",
                        "quote": "Yield was 56%.",
                        "note": "inverted",
                    }
                ],
            },
            {"accepted": True, "issues": []},
        ]
    )

    def patch(messages):
        base = messages[1]["content"].split("base_hash ")[1].split(")")[0]
        return json.dumps({"base_hash": base, "paragraphs": {"4": "Yield fell to 56%. [src: b]"}})

    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": lambda m: json.dumps(next(verdicts)),
            "x/patch/1": patch,
            "x/patch/1/review": lambda m: json.dumps(next(verdicts)),
        },
    )
    assert "Yield fell to 56%. [src: b]" in run("x")
    assert "Review only paragraphs [4]" in stub.prompts[-1][1]
    assert "the rules allow 20-60; keep the patched page inside" in stub.prompts[-2][1]


def test_page_fails_after_two_rounds_and_keeps_its_job_keys(monkeypatch, tmp_path):
    reject = json.dumps(
        {
            "accepted": False,
            "issues": [
                {
                    "paragraph": 1,
                    "category": "unsupported",
                    "quote": "Lead sentence",
                    "note": "no evidence",
                }
            ],
        }
    )

    def patch(messages):
        base = messages[1]["content"].split("base_hash ")[1].split(")")[0]
        return json.dumps({"base_hash": base, "paragraphs": {"1": "Another lead sentence."}})

    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            "x/patch/1": patch,
            "x/patch/1/review": reject,
            "x/patch/2": patch,
            "x/patch/2/review": reject,
        },
    )
    with pytest.raises(P.PageFailure) as failure:
        run("x")
    assert failure.value.issues[0]["category"] == "unsupported"
    assert failure.value.jobs == [f"key:{s}" for s, _ in stub.prompts]
    assert len(stub.prompts) == 6
    P.record_failure("conflicts/x", failure.value)
    saved = json.loads((tmp_path / "failures.json").read_text())
    assert saved["conflicts/x"]["jobs"] == failure.value.jobs
    P.prune_failures("conflicts/", set())
    assert json.loads((tmp_path / "failures.json").read_text()) == {}


def test_malformed_patch_or_stale_hash_is_a_page_failure(monkeypatch, tmp_path):
    configure(monkeypatch, tmp_path, {"x": "no heading at all", "x/patch/1": "not json"})
    with pytest.raises(P.PageFailure, match="patch not JSON"):
        run("x")
    configure(
        monkeypatch,
        tmp_path,
        {"x": "no heading at all", "x/patch/1": '{"base_hash": "old", "paragraphs": {"0": "x"}}'},
    )
    with pytest.raises(P.PageFailure, match="stale or empty"):
        run("x")


def test_parallel_yields_page_failures_and_raises_operational_errors():
    def work(item):
        if item == "bad":
            raise P.PageFailure("s", [P.Issue(category="length")], [])
        if item == "crash":
            raise RuntimeError("budget admission refused")
        return item.upper()

    results = dict(P.parallel(["a", "bad", "b"], work, 4))
    assert results["a"] == "A" and isinstance(results["bad"], P.PageFailure)
    with pytest.raises(RuntimeError, match="budget"):
        list(P.parallel(["a", "crash"], work, 4))


def test_conflicts_stage_continues_past_a_failed_page(monkeypatch, tmp_path):
    from beril_wiki.stages import conflicts as CB

    for folder in ("wiki/concepts", "wiki/sources", "wiki/conflicts"):
        (tmp_path / folder).mkdir(parents=True)
    for sid, value in SOURCES.items():
        (tmp_path / f"wiki/sources/{sid}__REPORT.md").write_text(value)
    tension = "Yield was 42%. [src: a] Yield was 56%. [src: b]"
    for stem in ("one", "two"):
        (tmp_path / f"wiki/concepts/{stem}.md").write_text(
            f"# {stem.title()}\n\nLead. [src: a]\n\n## Tensions\n\n{tension} On {stem}."
        )
    monkeypatch.setattr(CB, "ROOT", tmp_path)
    monkeypatch.setattr(CB, "OUT", tmp_path / "wiki/conflicts")
    page = (
        "# Yield tension\n\nLead about the disagreement, see [[concepts/one]].\n\n"
        "## Evidence Sides\n\n**A.** Yield was 42%. [src: a]\n\n**B.** Yield was 56%. [src: b]\n\n"
        "## Possible Reconciliations\n\nHypothesis: conditions.\n\n## Resolving Work\n\n- Redo."
    )
    page = page + ("\n\n" + "Conditions were compared without new figures. " * 12) * 5
    reject = json.dumps(
        {"accepted": False, "issues": [{"paragraph": 1, "category": "caveat", "quote": "Lead"}]}
    )

    class Script(dict):
        def __missing__(self, step):
            if step.endswith("/review"):
                return reject if "two" in step else '{"accepted": true, "issues": []}'
            if "/patch/" in step:
                return lambda m: json.dumps(
                    {
                        "base_hash": m[1]["content"].split("base_hash ")[1].split(")")[0],
                        "paragraphs": {"1": "Lead again, see [[concepts/two]]."},
                    }
                )
            return page

    configure(monkeypatch, tmp_path, Script(), workers=2)
    (tmp_path / "wiki/conflicts/conflict--old--00000000.md").write_text("stale")
    monkeypatch.setattr(CB.sys, "argv", ["conflicts", "--limit", "1"])
    assert CB.main() == 0
    assert (tmp_path / "wiki/conflicts/conflict--old--00000000.md").exists()  # capped: no reaping
    assert len(list((tmp_path / "wiki/conflicts").glob("conflict--one--*.md"))) == 1
    for stale in (tmp_path / "wiki/conflicts").glob("*.md"):
        stale.unlink()
    (tmp_path / "wiki/conflicts/conflict--old--00000000.md").write_text("predecessor")
    monkeypatch.setattr(CB.sys, "argv", ["conflicts"])
    assert CB.main() == 0
    written = sorted(p.name for p in (tmp_path / "wiki/conflicts").glob("*.md"))
    # The failed page's predecessor (under its old slug) survives a pass with failures.
    assert written[0] == "conflict--old--00000000.md" and written[1].startswith("conflict--one--")
    assert len(written) == 2
    failures = json.loads((tmp_path / "failures.json").read_text())
    assert list(failures) and list(failures)[0].startswith("conflicts/conflict--two--")
    monkeypatch.setattr(P, "runtime_config", lambda: {"store": str(tmp_path), "strict_pages": 1})
    assert CB.main() == 1


def test_excerpts_mark_truncation_and_source_excerpts_follow_figures():
    packed = P.excerpts({"a": "x" * 100, "b": "y" * 10}, budget=80, per_page=64)
    assert "[TRUNCATED: a continues" in packed and "yyyyyyyyyy" in packed
    sources = {"p": "Intro.\n\nCoverage was 7,609 genes.\n\nOther 1.5% detail.", "q": "Nothing."}
    pack = P.source_excerpts("Coverage reached 7,609 genes. [src: p, q]", ["p", "q"], sources)
    assert "Coverage was 7,609 genes." in pack and "Other 1.5% detail" not in pack
    assert "[source: q]\nNothing." in pack


def test_clean_strips_fences_and_legacy_names():
    text = P.clean("```markdown\n# T\n\nData in BERDL and [[concepts/x]].\n```", {"concepts/y"})
    assert text == "# T\n\nData in the KBase Data Lakehouse and x."
    assert SimpleNamespace  # keep the import honest for the stub type


def _patch_reply(messages, edits):
    base = messages[1]["content"].split("base_hash ")[1].split(")")[0]
    return json.dumps({"base_hash": base, "paragraphs": edits})


def test_unresolved_and_unreviewed_paragraphs_stay_in_scope(monkeypatch, tmp_path):
    """A patch that fixes one of two objections must not retire the other one."""
    first = {
        "accepted": False,
        "issues": [
            {"paragraph": 1, "category": "unsupported", "quote": "Lead"},
            {"paragraph": 4, "category": "direction", "quote": "56%"},
        ],
    }
    verdicts = iter(
        [
            first,
            {
                "accepted": False,
                "issues": [{"paragraph": 4, "category": "direction", "quote": "56%"}],
            },
            {"accepted": True, "issues": []},
        ]
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": lambda m: json.dumps(next(verdicts)),
            "x/patch/1": lambda m: _patch_reply(m, {"1": "A lead that is supported."}),
            "x/patch/1/review": lambda m: json.dumps(next(verdicts)),
            "x/patch/2": lambda m: _patch_reply(m, {"4": "Yield rose to 56%. [src: b]"}),
            "x/patch/2/review": lambda m: json.dumps(next(verdicts)),
        },
    )
    out = run("x")
    assert "Yield rose to 56%." in out and "A lead that is supported." in out
    assert "Review only paragraphs [1, 4]" in stub.prompts[3][1]  # the unfixed objection follows
    assert "Review only paragraphs [4]" in stub.prompts[5][1]


def test_patch_that_fails_a_gate_keeps_its_changes_unreviewed(monkeypatch, tmp_path):
    reject = json.dumps(
        {
            "accepted": False,
            "issues": [{"paragraph": 1, "category": "unsupported", "quote": "Lead"}],
        }
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            # Fixes paragraph 1 but imports a figure into paragraph 3: the gate rejects it.
            "x/patch/1": lambda m: _patch_reply(
                m, {"1": "Supported lead.", "3": "Yield was 42% of 8,314 loci. [src: a]"}
            ),
            "x/patch/2": lambda m: _patch_reply(m, {"3": "Yield was 42%. [src: a]"}),
            "x/patch/2/review": '{"accepted": true, "issues": []}',
        },
    )
    run("x")
    assert "Review only paragraphs [1, 3]" in stub.prompts[-1][1]


def test_invalid_patch_index_is_a_page_failure(monkeypatch, tmp_path):
    reject = json.dumps(
        {
            "accepted": False,
            "issues": [{"paragraph": 1, "category": "unsupported", "quote": "Lead"}],
        }
    )
    configure(
        monkeypatch,
        tmp_path,
        {"x": GOOD, "x/review": reject, "x/patch/1": lambda m: _patch_reply(m, {"999": "x"})},
    )
    with pytest.raises(P.PageFailure, match="do not exist"):
        run("x")


def test_contradictory_or_malformed_verdict_is_asked_again_then_fails(monkeypatch, tmp_path):
    stub = configure(
        monkeypatch,
        tmp_path,
        {"x": GOOD, "x/review": '{"accepted": false, "issues": []}', "x/review/again": "nonsense"},
    )
    with pytest.raises(P.PageFailure, match="no usable verdict"):
        run("x")
    assert [s for s, _ in stub.prompts] == ["x", "x/review", "x/review/again"]
    configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": "nonsense",
            "x/review/again": json.dumps(
                {
                    "accepted": False,
                    "issues": [{"paragraph": None, "category": "length", "quote": "too long"}],
                }
            ),
        },
    )
    assert run("x") == GOOD  # a reviewer word count is code-owned and never patched


def test_normalize_runs_before_gates_and_review(monkeypatch, tmp_path):
    draft = GOOD.replace("## Sides", "## Sides\n\nSee [[concepts/missing]].")
    stub = configure(
        monkeypatch, tmp_path, {"x": draft, "x/review": '{"accepted": true, "issues": []}'}
    )
    out = P.derived_page(
        "x",
        CONTRACT,
        "t",
        "pack",
        allowed=GOOD,
        sources=SOURCES,
        valid_ids={"a", "b"},
        targets=set(),
        normalize=lambda t: t.replace("See missing.", "See [[concepts/a]]."),
    )
    assert "See [[concepts/a]]." in out and "[[concepts/a]]" in stub.prompts[-1][1]


def test_owning_stage_maps_failed_pages():
    assert [
        P.owning_stage(p) for p in ("conflicts/x", "topics/y", "index.md", "lit/z", "authors/w")
    ] == [
        "conflicts",
        "topics",
        "topics",
        "literature",
        "authors",
    ]


def test_paced_get_retries_a_truncated_pubmed_read(monkeypatch):
    """One IncompleteRead must not kill a stage that has hours of accepted pages behind it."""
    import http.client
    from contextlib import contextmanager

    from beril_wiki.stages import literature

    attempts = []

    @contextmanager
    def flaky(url, timeout=None):
        attempts.append(url)
        if len(attempts) < 3:
            raise http.client.IncompleteRead(b"partial")

        class Response:
            def read(self, cap=None):
                return b"<PubmedArticleSet/>"

        yield Response()

    monkeypatch.setattr(literature.urllib.request, "urlopen", flaky)
    monkeypatch.setattr(literature, "pace", lambda: None)
    monkeypatch.setattr(literature.time, "sleep", lambda _: None)

    assert literature.paced_get("http://example/efetch", 2_000_001) == b"<PubmedArticleSet/>"
    assert len(attempts) == 3


def test_paced_get_gives_up_after_its_last_try(monkeypatch):
    import http.client
    from contextlib import contextmanager

    import pytest

    from beril_wiki.stages import literature

    @contextmanager
    def always_truncated(url, timeout=None):
        raise http.client.IncompleteRead(b"partial")
        yield  # pragma: no cover

    monkeypatch.setattr(literature.urllib.request, "urlopen", always_truncated)
    monkeypatch.setattr(literature, "pace", lambda: None)
    monkeypatch.setattr(literature.time, "sleep", lambda _: None)

    with pytest.raises(http.client.IncompleteRead):
        literature.paced_get("http://example/efetch")


def test_presentation_only_objections_publish_after_the_patch_rounds(monkeypatch, tmp_path):
    """A subject must not lose its last page over an undefined acronym."""
    reject = json.dumps(
        {
            "accepted": False,
            "issues": [
                {"paragraph": 1, "category": "format", "quote": "SNIPE", "note": "undefined"}
            ],
        }
    )
    configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            "x/patch/1": lambda m: _patch_reply(m, {"1": "A lead that is supported."}),
            "x/patch/1/review": reject,
            "x/patch/2": lambda m: _patch_reply(m, {"1": "A lead that is still supported."}),
            "x/patch/2/review": reject,
        },
    )
    out = run("x")
    assert "still supported" in out


def test_substantive_objections_still_withhold_the_page(monkeypatch, tmp_path):
    reject = json.dumps(
        {
            "accepted": False,
            "issues": [
                {"paragraph": 1, "category": "format", "quote": "SNIPE", "note": "undefined"},
                {"paragraph": 1, "category": "unsupported", "quote": "claim", "note": "no support"},
            ],
        }
    )
    configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            "x/patch/1": lambda m: _patch_reply(m, {"1": "A lead that is supported."}),
            "x/patch/1/review": reject,
            "x/patch/2": lambda m: _patch_reply(m, {"1": "A lead that is still supported."}),
            "x/patch/2/review": reject,
        },
    )
    with pytest.raises(P.PageFailure):
        run("x")


def test_scoped_review_shows_only_the_scope_its_neighbours_and_headings():
    parts = P.blocks(GOOD)  # [0] # Title, [1] lead, [2] ## Sides, [3] 42%, [4] 56%, [5] closing
    shown = P.scoped(parts, [4])
    assert "[3] Yield was 42%" in shown and "[4] Yield was 56%" in shown  # scope + neighbour
    assert "[5] Closing words" in shown  # neighbour
    assert "[0] # Title" in shown and "[2] ## Sides" in shown  # headings always
    assert "Lead sentence" not in shown  # accepted earlier, not a neighbour: omitted
    assert "[4]" in shown  # original index preserved


def test_scoped_re_review_omits_paragraphs_accepted_earlier(monkeypatch, tmp_path):
    verdicts = iter(
        [
            {
                "accepted": False,
                "issues": [{"paragraph": 4, "category": "direction", "quote": "56%"}],
            },
            {"accepted": True, "issues": []},
        ]
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": lambda m: json.dumps(next(verdicts)),
            "x/patch/1": lambda m: _patch_reply(m, {"4": "Yield rose to 56%. [src: b]"}),
            "x/patch/1/review": lambda m: json.dumps(next(verdicts)),
        },
    )
    run("x")
    full, scoped_prompt = stub.prompts[1][1], stub.prompts[3][1]
    assert "Lead sentence" in full  # the first review sees everything
    assert "Review only paragraphs [4]" in scoped_prompt
    assert "Lead sentence" not in scoped_prompt  # accepted, not adjacent: dropped
    assert "Yield rose to 56%" in scoped_prompt and "[4]" in scoped_prompt
