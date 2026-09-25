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
    assert "Review every paragraph." in stub.prompts[-1][1]  # a repair is no verdict on the rest


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
            "x/patch/1/verify": _ok(),
        },
    )
    assert "Yield fell to 56%. [src: b]" in run("x")
    assert '"category": "direction"' in stub.prompts[-1][1]  # verify is told what to check
    assert "the rules allow 20-60; keep the patched page inside" in stub.prompts[-2][1]


def test_page_that_cannot_be_salvaged_fails_and_keeps_its_job_keys(monkeypatch, tmp_path):
    """Every paragraph objected to, so nothing is left to publish: the page fails."""
    issues = [
        {"paragraph": n, "category": "unsupported", "quote": "q", "note": "no evidence"}
        for n in (1, 3, 4, 5)
    ]
    script = {"x": GOOD, "x/review": json.dumps({"accepted": False, "issues": issues})}
    for n in range(1, P.PATCH_ROUNDS + 1):
        script[f"x/patch/{n}"] = lambda m: _patch_reply(m, {"1": "Another lead sentence."})
        script[f"x/patch/{n}/verify"] = _still(issues)
    stub = configure(monkeypatch, tmp_path, script)
    with pytest.raises(P.PageFailure) as failure:
        run("x")
    assert failure.value.issues[0]["category"] == "unsupported"
    assert failure.value.jobs == [f"key:{s}" for s, _ in stub.prompts]
    # draft + review + five (patch, verify) pairs
    assert len(stub.prompts) == 2 + 2 * P.PATCH_ROUNDS
    P.record_failure("conflicts/x", failure.value)
    saved = json.loads((tmp_path / "failures.json").read_text())
    assert saved["conflicts/x"]["jobs"] == failure.value.jobs
    P.prune_failures("conflicts/", set())
    assert json.loads((tmp_path / "failures.json").read_text()) == {}


def test_unresolved_paragraph_is_dropped_and_the_page_still_publishes(monkeypatch, tmp_path):
    """The reader keeps the page and is told something was removed."""
    stuck = [{"paragraph": 4, "category": "unsupported", "quote": "56%", "note": "no evidence"}]
    script = {"x": GOOD, "x/review": json.dumps({"accepted": False, "issues": stuck})}
    for n in range(1, P.PATCH_ROUNDS + 1):
        script[f"x/patch/{n}"] = lambda m: _patch_reply(m, {"4": "Yield was 56%. [src: b]"})
        script[f"x/patch/{n}/verify"] = _still(stuck)
    configure(monkeypatch, tmp_path, script)
    out = run("x")
    assert "Yield was 56%" not in out  # the objected paragraph is gone
    assert "Yield was 42%. [src: a]" in out  # the rest of the page survives
    assert "Editorial note" in out and "unsupported" in out
    assert "# Title" in out and "## Sides" in out  # headings are never dropped
    ledger = json.loads((tmp_path / "salvaged.json").read_text())
    assert ledger["x"]["removed"] == ["Yield was 56%. [src: b]"]  # the material, not a count
    assert ledger["x"]["issues"][0]["category"] == "unsupported"
    assert ledger["x"]["jobs"] and all(j.startswith("key:") for j in ledger["x"]["jobs"])


def test_salvage_refuses_when_removal_would_break_a_gate(monkeypatch, tmp_path):
    """A removal that costs a required heading is not publishable."""
    parts = P.blocks(GOOD)
    issues = [P.Issue(paragraph=2, category="unsupported")]  # paragraph 2 is '## Sides'
    assert (
        P.salvage(
            parts, issues, CONTRACT, allowed=GOOD, sources=SOURCES, valid_ids={"a", "b"}, extra=None
        )
        is None
    )


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
        {
            "accepted": False,
            "issues": [
                {"paragraph": n, "category": "caveat", "quote": "Lead"} for n in range(1, 40)
            ],
        }
    )

    class Script(dict):
        def __missing__(self, step):
            if step.endswith("/verify"):
                return _still(json.loads(reject)["issues"]) if "two" in step else _ok()
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


def _ok():
    """A verification that every issue is closed."""
    return '{"resolved": [0], "open": []}'


def _still(issues):
    """A verification that leaves issues open."""
    return json.dumps({"resolved": [], "open": issues})


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
    checks = iter(
        [
            json.dumps(
                {
                    "resolved": [0],  # the unsupported lead was fixed
                    "open": [{"paragraph": 4, "category": "direction", "quote": "56%"}],
                }
            ),
            _ok(),
        ]
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": json.dumps(first),
            "x/patch/1": lambda m: _patch_reply(m, {"1": "A lead that is supported."}),
            "x/patch/1/verify": lambda m: next(checks),
            "x/patch/2": lambda m: _patch_reply(m, {"4": "Yield rose to 56%. [src: b]"}),
            "x/patch/2/verify": lambda m: next(checks),
        },
    )
    out = run("x")
    assert "Yield rose to 56%." in out and "A lead that is supported." in out
    # both objections travel into the first verification, only the open one into the second
    assert '"category": "unsupported"' in stub.prompts[2][1]
    assert '"category": "direction"' in stub.prompts[2][1]
    assert '"category": "unsupported"' not in stub.prompts[4][1]


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
            "x/patch/2/verify": _ok(),
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


def test_presentation_only_objections_publish_the_page_intact(monkeypatch, tmp_path):
    """A subject must not lose its page over an undefined acronym."""
    fmt = [{"paragraph": 1, "category": "format", "quote": "SNIPE", "note": "undefined"}]
    script = {"x": GOOD, "x/review": json.dumps({"accepted": False, "issues": fmt})}
    for n in range(1, P.PATCH_ROUNDS + 1):
        script[f"x/patch/{n}"] = lambda m: _patch_reply(m, {"1": "A lead that is supported."})
        script[f"x/patch/{n}/verify"] = _still(fmt)
    configure(monkeypatch, tmp_path, script)
    out = run("x")
    assert "A lead that is supported." in out
    assert "Editorial note" not in out  # presentational: nothing is dropped


def test_substantive_objection_drops_its_paragraph_rather_than_the_page(monkeypatch, tmp_path):
    """The page survives; the claim the evidence does not support does not."""
    bad = [{"paragraph": 1, "category": "unsupported", "quote": "Lead", "note": "no evidence"}]
    script = {"x": GOOD, "x/review": json.dumps({"accepted": False, "issues": bad})}
    for n in range(1, P.PATCH_ROUNDS + 1):
        script[f"x/patch/{n}"] = lambda m: _patch_reply(m, {"1": "A lead that is supported."})
        script[f"x/patch/{n}/verify"] = _still(bad)
    configure(monkeypatch, tmp_path, script)
    out = run("x")
    assert "A lead that is supported." not in out  # the objected paragraph is removed
    assert "Editorial note" in out and "unsupported" in out
    assert "Yield was 42%. [src: a]" in out  # the rest of the page stands


def test_scoped_review_shows_only_the_scope_its_neighbours_and_headings():
    parts = P.blocks(GOOD)  # [0] # Title, [1] lead, [2] ## Sides, [3] 42%, [4] 56%, [5] closing
    shown = P.scoped(parts, [4])
    assert "[3] Yield was 42%" in shown and "[4] Yield was 56%" in shown  # scope + neighbour
    assert "[5] Closing words" in shown  # neighbour
    assert "[0] # Title" in shown and "[2] ## Sides" in shown  # headings always
    assert "Lead sentence" not in shown  # accepted earlier, not a neighbour: omitted
    assert "[4]" in shown  # original index preserved


def test_scoped_verification_omits_paragraphs_accepted_earlier(monkeypatch, tmp_path):
    stuck = [{"paragraph": 4, "category": "direction", "quote": "56%"}]
    checks = iter([_still(stuck), _ok()])
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": json.dumps({"accepted": False, "issues": stuck}),
            "x/patch/1": lambda m: _patch_reply(m, {"4": "Yield rose to 56%. [src: b]"}),
            "x/patch/1/verify": lambda m: next(checks),
            "x/patch/2": lambda m: _patch_reply(m, {"4": "Yield fell to 56%. [src: b]"}),
            "x/patch/2/verify": lambda m: next(checks),
        },
    )
    run("x")
    full, scoped_prompt = stub.prompts[1][1], stub.prompts[3][1]
    assert "Lead sentence" in full  # the one open review sees the whole page
    assert "Review only paragraphs [4]" in scoped_prompt
    assert "Lead sentence" not in scoped_prompt  # accepted, not adjacent: dropped
    assert "Yield rose to 56%" in scoped_prompt and "[4]" in scoped_prompt


# --- findings of the independent review of cf12b31..f62839f -------------------


def test_gates_failing_every_round_never_publish(monkeypatch, tmp_path):
    """A page nobody reviewed cannot publish, however many repairs it had."""
    draft = GOOD.replace("Yield was 42%. [src: a]", "Yield was 42% of 8,314 loci. [src: a]")
    script = {"x": draft}
    for n in range(1, P.PATCH_ROUNDS + 1):  # every repair leaves the imported figure in place
        script[f"x/patch/{n}"] = lambda m: _patch_reply(
            m, {"3": "Yield was 42% of 8,314 loci. [src: a]"}
        )
    stub = configure(monkeypatch, tmp_path, script)
    with pytest.raises(P.PageFailure):
        run("x")
    assert not any("review" in st or "verify" in st for st, _ in stub.prompts)


def test_empty_verification_is_not_a_verdict(monkeypatch, tmp_path):
    reject = json.dumps(
        {"accepted": False, "issues": [{"paragraph": 4, "category": "direction", "quote": "56%"}]}
    )
    configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            "x/patch/1": lambda m: _patch_reply(m, {"4": "Yield fell to 56%. [src: b]"}),
            "x/patch/1/verify": "{}",
            "x/patch/1/verify/again": '{"accepted": false, "issues": []}',  # the old shape
        },
    )
    with pytest.raises(P.PageFailure, match="no usable verdict"):
        run("x")


def test_an_objection_stays_open_until_the_verifier_names_it_resolved(monkeypatch, tmp_path):
    reject = json.dumps(
        {"accepted": False, "issues": [{"paragraph": 4, "category": "direction", "quote": "56%"}]}
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            "x/patch/1": lambda m: _patch_reply(m, {"4": "Yield fell to 56%. [src: b]"}),
            "x/patch/1/verify": '{"resolved": [], "open": []}',  # silent on the objection
            "x/patch/2": lambda m: _patch_reply(m, {"4": "Yield rose to 56%. [src: b]"}),
            "x/patch/2/verify": _ok(),
        },
    )
    assert "Yield rose to 56%" in run("x")
    steps = [st for st, _ in stub.prompts]
    assert "x/patch/2" in steps  # silence cost another round rather than publishing
    assert '"category": "direction"' in stub.prompts[steps.index("x/patch/2/verify")][1]


def test_a_gate_only_round_keeps_the_reviewers_objections(monkeypatch, tmp_path):
    reject = json.dumps(
        {"accepted": False, "issues": [{"paragraph": 4, "category": "direction", "quote": "56%"}]}
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            # Ignores the objection and imports a figure into paragraph 3: a gate round follows.
            "x/patch/1": lambda m: _patch_reply(m, {"3": "Yield was 42% of 8,314 loci. [src: a]"}),
            "x/patch/2": lambda m: _patch_reply(m, {"3": "Yield was 42%. [src: a]"}),
            "x/patch/2/verify": _ok(),
        },
    )
    run("x")
    verify = stub.prompts[-1]
    assert verify[0] == "x/patch/2/verify"
    assert '"category": "direction"' in verify[1]  # survived the gate-only round
    assert '"paragraph": 4' in verify[1]


def test_verifier_receives_the_objections_note(monkeypatch, tmp_path):
    reject = json.dumps(
        {
            "accepted": False,
            "issues": [
                {
                    "paragraph": 4,
                    "category": "direction",
                    "quote": "56%",
                    "note": "the sign is inverted",
                }
            ],
        }
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            "x/patch/1": lambda m: _patch_reply(m, {"4": "Yield fell to 56%. [src: b]"}),
            "x/patch/1/verify": _ok(),
        },
    )
    run("x")
    assert '"note": "the sign is inverted"' in stub.prompts[-1][1]


def test_verification_drops_a_new_objection_outside_its_scope(monkeypatch, tmp_path):
    reject = json.dumps(
        {"accepted": False, "issues": [{"paragraph": 4, "category": "direction", "quote": "56%"}]}
    )
    stub = configure(
        monkeypatch,
        tmp_path,
        {
            "x": GOOD,
            "x/review": reject,
            "x/patch/1": lambda m: _patch_reply(m, {"4": "Yield fell to 56%. [src: b]"}),
            "x/patch/1/verify": json.dumps(
                {
                    "resolved": [0],
                    "open": [{"paragraph": 1, "category": "unsupported", "quote": "Lead"}],
                }
            ),
        },
    )
    out = run("x")
    assert "Yield fell to 56%" in out and "Lead sentence" in out  # accepted text untouched
    assert "x/patch/2" not in [st for st, _ in stub.prompts]


def test_salvage_refuses_an_undischarged_substantive_objection():
    parts = P.blocks(GOOD)
    body = P.Issue(paragraph=4, category="unsupported", quote="56%")
    heading = P.Issue(paragraph=2, category="unsupported", quote="Sides")
    nowhere = P.Issue(paragraph=None, category="caveat", quote="somewhere")

    def salvage(issues: list[P.Issue]) -> tuple[str, list[str]] | None:
        return P.salvage(
            parts, issues, CONTRACT, allowed=GOOD, sources=SOURCES, valid_ids={"a", "b"}, extra=None
        )

    assert salvage([body, heading]) is None
    assert salvage([body, nowhere]) is None
    result = salvage([body])
    assert result is not None
    text, removed = result
    assert removed == ["Yield was 56%. [src: b]"] and "Yield was 56%" not in text


def test_salvage_ledger_survives_concurrent_writers(monkeypatch, tmp_path):
    from concurrent.futures import ThreadPoolExecutor

    configure(monkeypatch, tmp_path, {})
    issue = P.Issue(category="unsupported", quote="q")
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(
            pool.map(
                lambda n: P.record_salvage(f"p{n}", [issue], [f"para {n}"], [f"key:{n}"]), range(16)
            )
        )
    ledger = json.loads((tmp_path / "salvaged.json").read_text())
    assert sorted(ledger) == sorted(f"p{n}" for n in range(16))
    assert ledger["p7"] == {
        "removed": ["para 7"],
        "issues": [issue.model_dump()],
        "jobs": ["key:7"],
    }
