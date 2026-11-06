"""The gists stage: plain summaries checked by code, then by a reviewer."""

import json

import pytest

from beril_wiki.agentic import curator
from beril_wiki.agentic.runtime import CONTENT_FLAG, CandidateError, JobFailed
from beril_wiki.stages import cards, gists
from card_fakes import FakeAgent, install

FID = "a--1a2b3c4d"
STEP = f"gists/{FID}"
QUOTE = "20% of genes (177/866) were depleted."
GOOD = (
    "Roughly 20% of genes were depleted in this archaeon, which hints at fragile stress responses."
)


def reply(gist=GOOD, case="", title="", repeats=""):
    return json.dumps({"gist": gist, "case": case, "title": title, "repeats": repeats})


def page(root, title="Genes were depleted", result="observation", quote=QUOTE):
    cards.write_page(
        root / "wiki/findings" / f"{FID}.md",
        {
            "type": "Finding",
            "description": "Dark genes were depleted.",
            "result": result,
            "source": "a",
            "caveat": "One strain only.",
        },
        f"# {title}\n\nDark genes were depleted. [src: a]\n\n## Evidence\n\n> {quote} [src: a]\n\n"
        "## Caveat\n\nOne strain only. [src: a]\n\n> Only strain X was tested. [src: a]\n",
    )
    summary = root / "wiki/summaries/a__REPORT.md"
    summary.parent.mkdir(parents=True, exist_ok=True)
    summary.write_text("# Archaeal stress\n")


def run(tmp_path, monkeypatch, replies, **kwargs):
    page(tmp_path, **{k: kwargs.pop(k) for k in ("title", "result", "quote") if k in kwargs})
    agent = FakeAgent(tmp_path / "store", {STEP: [], f"{STEP}/repair": []} | replies, **kwargs)
    install(monkeypatch, agent)
    assert gists.main(tmp_path) == 0
    path = tmp_path / "state/gists.json"
    return (json.loads(path.read_text()) if path.exists() else {}), agent


def test_accepted_gist_is_saved_with_its_input_key(tmp_path, monkeypatch):
    state, agent = run(tmp_path, monkeypatch, {STEP: [reply()]})
    assert state[FID]["gist"] == GOOD and state[FID]["input"]
    assert state[FID]["case"] == "" and state[FID]["model"] == "claude-sonnet-5-5"
    assert agent.asked == [STEP, f"{STEP}/science-review"]


def test_statistics_and_new_figures_go_back_to_the_writer(tmp_path, monkeypatch):
    replies = {
        STEP: [reply("Genes were depleted in this archaeon (p = 0.01) under stress conditions.")],
        f"{STEP}/repair": [
            reply("About 177% of genes were depleted in this archaeon under stress conditions."),
            reply(),
        ],
    }
    state, agent = run(tmp_path, monkeypatch, replies)
    assert state[FID]["gist"] == GOOD
    assert agent.asked.count(f"{STEP}/repair") == 2


def test_rhodanobacter_and_neighbourhood_are_not_statistics():
    parse = gists.checker({"result": "observation", "claim": "Rhodanobacter genes"}, "Plain")
    text = "Rhodanobacter genomes in GT2 neighbourhoods carry more genes than their relatives do."
    assert parse(reply(text)).gist == text


def test_null_needs_a_case_and_others_do_not():
    null = gists.checker({"result": "null result", "quote": QUOTE}, "Plain")
    with pytest.raises(CandidateError, match="needs a case"):
        null(reply())
    assert null(reply(case="missing data")).case == "missing data"
    observed = gists.checker({"result": "observation", "quote": QUOTE}, "Plain")
    with pytest.raises(CandidateError, match="null results only"):
        observed(reply(case="missing data"))


def test_title_only_when_stored_title_has_statistics():
    stats = gists.checker(
        {"result": "observation", "quote": QUOTE}, "Few modules survive FDR correction"
    )
    with pytest.raises(CandidateError, match="plain title"):
        stats(reply())
    with pytest.raises(CandidateError, match="title contains a statistic"):
        stats(reply(title="Few modules survive FDR"))
    assert stats(reply(title="Few modules hold up after correction")).title
    plain = gists.checker({"result": "observation", "quote": QUOTE}, "Genes were depleted")
    with pytest.raises(CandidateError, match="leave title empty"):
        plain(reply(title="Another title"))


def test_length_sentences_and_banned_words():
    parse = gists.checker({"result": "observation", "quote": QUOTE}, "Plain")
    for bad in (
        "Too short.",
        " ".join(["word"] * 46),
        "First sentence is here now. Second one follows it. A third sentence arrives too.",
        "This is a novel observation about genes in archaea today.",
        "Genes were depleted in this archaeon, however the sample was small and strain X only.",
        "Caveat: genes were depleted in this archaeon across all of the strains we tested here.",
    ):
        with pytest.raises(CandidateError):
            parse(reply(bad))


def test_unchanged_finding_costs_nothing(tmp_path, monkeypatch):
    run(tmp_path, monkeypatch, {STEP: [reply()]})
    state, agent = run(tmp_path, monkeypatch, {})
    assert agent.asked == [] and state[FID]["gist"] == GOOD


def test_refusal_fails_one_finding_and_keeps_its_previous_gist(tmp_path, monkeypatch, capsys):
    run(tmp_path, monkeypatch, {STEP: [reply()]})
    page(tmp_path, title="Genes were lost")
    refusal = JobFailed(f"Codex turn failed: {CONTENT_FLAG}")
    agent = FakeAgent(tmp_path / "store", {STEP: [reply()]}, review_error={STEP: refusal})
    install(monkeypatch, agent)
    gists.main(tmp_path)
    state = json.loads((tmp_path / "state/gists.json").read_text())
    assert state[FID]["gist"] == GOOD and state[FID]["failed"] is True
    assert f"[FAILED] {STEP}" in capsys.readouterr().out


def test_new_failed_finding_is_marked_failed_only(tmp_path, monkeypatch):
    refusal = JobFailed(f"Codex turn failed: {CONTENT_FLAG}")
    state, _ = run(tmp_path, monkeypatch, {STEP: [reply()]}, review_error={STEP: refusal})
    assert state[FID] == {"failed": True}


def test_caveat_quote_and_report_title(tmp_path):
    page(tmp_path)
    _, body = cards.read_page(tmp_path / "wiki/findings" / f"{FID}.md")
    assert gists.caveat_quote(body) == "Only strain X was tested."
    assert gists.report_title(tmp_path, "a") == "Archaeal stress"
    assert gists.report_title(tmp_path, "missing") == "missing"


def test_card_stage_revisions_ignore_other_stage_files_but_not_shared_ones(tmp_path, monkeypatch):
    """F7: the check can fail. Another card stage's own file leaves headlines, novelty
    and directions untouched; a change to the shared stages/cards.py reschedules them."""
    import pathlib

    config = {"model": "claude-sonnet-5-5", "step_models": {"review": "gpt-6.1-sol"}}
    names = ("headlines", "novelty", "directions")
    before = {n: curator.stage_revision(tmp_path, n, config) for n in names}
    real = pathlib.Path.read_text

    def edited(target):
        def read_text(self, *args, **kwargs):
            text = real(self, *args, **kwargs)
            return text + "\nEDITED = 1\n" if self.as_posix().endswith(target) else text

        return read_text

    monkeypatch.setattr(pathlib.Path, "read_text", edited("stages/gists.py"))
    assert {n: curator.stage_revision(tmp_path, n, config) for n in names} == before
    monkeypatch.setattr(pathlib.Path, "read_text", edited("stages/cards.py"))
    after = {n: curator.stage_revision(tmp_path, n, config) for n in names}
    assert all(after[n] != before[n] for n in names)
    monkeypatch.undo()
    assert curator.EDITORIAL["gists"][3] is None
    assert curator.EDITORIAL["gists"][2] == ("headlines",)
    assert "gists" in curator.CARD_STAGES


def test_plan_lists_stale_editorial_stages_without_model_calls(tmp_path):
    from beril_wiki.agentic import __main__ as cli

    (tmp_path / "state").mkdir()
    (tmp_path / "state/agentic.json").write_text(json.dumps({"editorial": {}}))
    (tmp_path / "agentic.yaml").write_text((cli.ROOT / "agentic.yaml").read_text())
    shown = cli.plan(tmp_path)
    assert shown["changed_sources"] == []
    assert "gists" in shown["pending_editorial"]


def test_gists_jobs_route_to_the_cards_and_review_roles():
    from beril_wiki.agentic.runtime import model_for, role_for

    config = {"model": "claude-opus-5-5", "step_models": {"cards": "claude-sonnet-5-5"}}
    for step in ("gists/x", "gists/x/repair"):
        assert role_for(step) == "cards"
        assert model_for(config, step) == "claude-sonnet-5-5"
    assert role_for("gists/x/science-review") == "review"
    assert role_for("gists/x/verify") == "review"


def test_long_replacement_title_is_still_checked_for_statistics():
    stats = gists.checker({"result": "observation", "quote": QUOTE}, "Few modules survive FDR")
    long_title = (
        "Few modules survive FDR correction in any of the many tested conditions here (p = 0.01)"
    )
    with pytest.raises(CandidateError, match="words.*statistic"):
        stats(reply(title=long_title))


def test_caveat_wording_is_sent_back_with_a_reason():
    parse = gists.checker({"result": "observation", "quote": QUOTE}, "Plain")
    with pytest.raises(CandidateError, match="limits separately"):
        parse(
            reply("Many genes were depleted in this archaeon. Caveat: only one strain was tested.")
        )


def test_prompt_tag_is_bumped_and_forbids_caveats():
    assert gists.PROMPT_TAG == "gists@4"
    assert "do not repeat or paraphrase the caveat" in gists.PROMPT
    assert "never invent an organism" in gists.PROMPT
    # Content review, Nov 2026: cards claimed more than predictions, correlations and
    # relative comparisons show.
    assert "a prediction stays a prediction" in gists.PROMPT
    assert "say in plain words that the report gives both results" in gists.PROMPT


def test_statistical_wording_counts_as_a_statistic_in_gists_and_titles():
    parse = gists.checker({"result": "observation", "quote": QUOTE}, "Plain")
    for bad in (
        "Genes were significantly depleted in this archaeon under stress conditions.",
        "No depletion survived multiple-testing correction in this archaeon under stress.",
    ):
        with pytest.raises(CandidateError, match="statistical wording"):
            parse(reply(bad))
    titled = gists.checker({"result": "observation", "quote": QUOTE}, "No significant depletion")
    with pytest.raises(CandidateError, match="plain title"):
        titled(reply())
    assert titled(reply(title="Depletion held in only some strains")).title


def test_gist_keeps_at_most_one_standalone_number():
    pool = QUOTE + " 866 genes in 16S-typed K-12 strains."
    parse = gists.checker({"result": "observation", "quote": pool}, "Plain")
    with pytest.raises(CandidateError, match="2 numbers"):
        parse(reply("Roughly 20% of 866 genes were depleted in this archaeon under stress."))
    assert parse(reply("Roughly 20% of 16S-typed K-12 genes were depleted in this archaeon."))
    fell = "Fitness fell on acetate (-1.55) and succinate (-1.39)."
    signed = gists.checker({"result": "observation", "quote": fell}, "Plain")
    with pytest.raises(CandidateError, match="2 numbers"):
        signed(reply("Mutants lose most fitness on acetate (-1.55) and succinate (-1.39) here."))


def test_the_writer_is_told_when_the_title_needs_a_plain_replacement(tmp_path, monkeypatch):
    seen = []
    real = gists.cards.reviewed

    def spy(messages, *args, **kwargs):
        seen.append(messages[0]["content"])
        return real(messages, *args, **kwargs)

    monkeypatch.setattr(gists.cards, "reviewed", spy)
    run(tmp_path, monkeypatch, {STEP: [reply(title="Genes held up")]}, title="No significant loss")
    assert '"TITLE_NEEDS_PLAIN": true' in seen[0]


def test_jargon_goes_back_to_the_writer_and_needs_a_plain_title():
    parse = gists.checker({"result": "observation", "quote": QUOTE}, "Plain")
    for bad in (
        "Mobile SEED categories were enriched among depleted genes in this archaeon.",
        "Genes in the Pseudomonas_E lineage were depleted in this archaeon under stress.",
        "Depleted genes clustered in one ICA module in this archaeon under stress.",
    ):
        with pytest.raises(CandidateError, match="plain words"):
            parse(reply(bad))
    finding = {"result": "observation", "quote": QUOTE}
    titled = gists.checker(finding, "Compartment PERMANOVA effect")
    with pytest.raises(CandidateError, match="plain title"):
        titled(reply())
    assert titled(reply(title="Plant compartment effect came from a few species")).title
    # Hydrogen is not a hypothesis code.
    assert parse(reply("Hydrogen (H2) producers were depleted in this archaeon under stress."))


def test_a_repeat_must_name_an_earlier_finding_of_the_report():
    parse = gists.checker({"result": "observation", "quote": QUOTE}, "Plain", ["a--00000001"])
    assert parse(reply(repeats="a--00000001")).repeats == "a--00000001"
    with pytest.raises(CandidateError, match="not an EARLIER finding"):
        parse(reply(repeats="a--ffffffff"))


def sibling(root, fid, claim):
    cards.write_page(
        root / "wiki/findings" / f"{fid}.md",
        {"type": "Finding", "description": claim, "result": "observation", "source": "a"},
        f"# {claim}\n\n{claim} [src: a]\n\n## Evidence\n\n> {claim} [src: a]\n",
    )


def test_the_writer_sees_report_caveats_and_siblings_and_a_sibling_change_reruns(
    tmp_path, monkeypatch
):
    seen = []
    real = gists.cards.reviewed

    def spy(messages, step, *args, **kwargs):
        seen.append((step, messages[0]["content"]))
        return real(messages, step, *args, **kwargs)

    monkeypatch.setattr(gists.cards, "reviewed", spy)
    earlier, later = "a--00000001", "a--ffffffff"
    sibling(tmp_path, earlier, "Stress genes were enriched.")
    sibling(tmp_path, later, "Stress genes were depleted in the cold.")
    plain = reply("Stress genes stood out among the genes of this archaeon under stress.")
    replies = {f"gists/{earlier}": [plain], f"gists/{later}": [plain], STEP: [reply()]}
    run(tmp_path, monkeypatch, replies)
    # The report's other caveats reach only their own finding's request.
    path = tmp_path / "wiki/findings" / f"{FID}.md"
    path.write_text(
        path.read_text()
        + "\n## Other caveats in this report\n\n- Only one growth medium was used. [src: a]\n"
    )

    def again(replies):
        seen.clear()
        install(monkeypatch, FakeAgent(tmp_path / "store", replies))
        assert gists.main(tmp_path) == 0

    again({STEP: [reply(repeats=earlier)]})
    assert [step for step, _ in seen] == [STEP]
    content = seen[0][1]
    assert '"REPORT_CAVEATS": ["Only one growth medium was used."]' in content
    assert f'"EARLIER": ["{earlier}"]' in content and later in content
    state = json.loads((tmp_path / "state/gists.json").read_text())
    assert state[FID]["repeats"] == earlier
    # A sibling's new claim reruns every finding of the report.
    sibling(tmp_path, later, "Stress genes were depleted in the heat.")
    again({f"gists/{earlier}": [plain], f"gists/{later}": [plain], STEP: [reply()]})
    assert {step for step, _ in seen} == {STEP, f"gists/{earlier}", f"gists/{later}"}


def test_status_counts_without_the_runtime(tmp_path, monkeypatch, capsys):
    for name in ("a", "b", "c", "d"):
        (tmp_path / "wiki/findings").mkdir(parents=True, exist_ok=True)
        (tmp_path / "wiki/findings" / f"{name}.md").write_text("# T\n")
    state = {"a": {"gist": "x", "input": "k"}, "b": {"failed": True}, "gone": {"gist": "y"}}
    (tmp_path / "state").mkdir()
    (tmp_path / "state/gists.json").write_text(json.dumps(state))
    monkeypatch.setattr(cards, "runtime", lambda: pytest.fail("status touched the runtime"))
    monkeypatch.setattr(cards, "require_runtime", lambda stage: pytest.fail("needs runtime"))
    before = (tmp_path / "state/gists.json").read_text()
    assert gists.main(tmp_path, ["--status"]) == 0
    assert "1 accepted, 1 failed, 2 pending, 4 total" in capsys.readouterr().out
    assert (tmp_path / "state/gists.json").read_text() == before


def test_only_saved_gists_todays_checks_reject_are_written_again(tmp_path, monkeypatch):
    state, _ = run(tmp_path, monkeypatch, {STEP: [reply()]})
    _, agent = run(tmp_path, monkeypatch, {})
    assert agent.asked == []
    path = tmp_path / "state/gists.json"
    stored = json.loads(path.read_text())
    stored[FID]["gist"] = (
        "Depleted genes clustered in one ICA module in this archaeon under stress."
    )
    path.write_text(json.dumps(stored))
    state, agent = run(tmp_path, monkeypatch, {STEP: [reply()]})
    assert agent.asked == [STEP, f"{STEP}/science-review"] and state[FID]["gist"] == GOOD
