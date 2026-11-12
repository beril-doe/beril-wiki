"""The directions stage: research questions grounded in findings, never reanalysis."""

import json
import shutil

import pytest

from beril_wiki.agentic.runtime import JobFailed, Refused
from beril_wiki.stages import cards, directions
from beril_wiki.wording import asks_to_redo, is_reanalysis
from card_fakes import FakeAgent, install, report, scope

TOPIC = "dark-matter"
FID = "a--1a2b3c4d"
CONFLICT = "conflict--gap--1234abcd"


def corpus(root):
    (root / "state").mkdir(parents=True, exist_ok=True)
    (root / "state/curator-topics.json").write_text(
        json.dumps({"groups": [{"title": "Dark Matter", "concepts": ["gap"]}]})
    )
    (root / "wiki/concepts").mkdir(parents=True)
    (root / "wiki/concepts/gap.md").write_text(
        "# Gap\n\nDark genes. [src: a]\n\n## Open Directions\n\n"
        "- Recompute the stress rates per experiment. [src: a]\n"
        "- Test whether dark genes encode transporters. [src: a]\n"
    )
    (root / "wiki/conflicts").mkdir(parents=True)
    (root / "wiki/conflicts" / f"{CONFLICT}.md").write_text(
        "<!-- tension-hash: 1 -->\n# Stress dominance versus depletion\n\n"
        "Two projects disagree about stress (28.7% vs 43.2%). [src: a, b]\n\n"
        "## Evidence Sides\n\nSide A says stress dominates. [src: b]\n"
    )
    (root / "wiki/data").mkdir(parents=True)
    (root / "wiki/data/kbase-ke-pangenome.md").write_text("# KBase pangenome\n")
    cards.write_page(
        root / "wiki/findings" / f"{FID}.md",
        {
            "description": "Truly dark genes are depleted in stress (28.7% vs 43.2%).",
            "source": "a",
            "result": "null result",
            "caveat": "Only 48 organisms.",
        },
        "# Dark genes avoid stress\n\nClaim. [src: a]\n",
    )
    (root / "state/novelty.json").write_text(
        json.dumps(
            {
                FID: {
                    "label": "Candidate novel",
                    "retrieved_on": "2026-10-23",
                    "difference": "No paper compares conditions.",
                    "closest": [
                        {"pmid": "29769716", "title": "Mutant phenotypes", "relation": "related"}
                    ],
                    "candidates": ["29769716"],
                }
            }
        )
    )
    report(root, "a", "# A\n")
    report(root, "b", "# B\n")
    scope(root, reports=["a"], topics=[TOPIC])


def direction(**kw):
    return {
        "id": "D1",
        "title": "Are dark genes nutrient and community-interaction genes?",
        "question": "Do dark genes with strong phenotypes act in nutrient uptake?",
        "hypothesis": "Their fitness profiles co-vary with known transporter genes.",
        "why_it_matters": "It would move annotation screens toward nutrient conditions.",
        "test": "Cofitness of dark genes with transporter genes across Fitness Browser organisms.",
        "outcomes": "Higher cofitness with transporters supports it; none refutes it.",
        "approach": "lakehouse analysis",
        "collections": ["kbase_ke_pangenome"],
        "readiness": "data in the lakehouse",
        "readiness_basis": "Fitness data are in the lakehouse.",
        "findings": [FID],
        "conflicts": [CONFLICT],
        "papers": ["29769716"],
        "prior_work": "PMID 29769716 maps phenotypes but not condition classes.",
    } | kw


def reply(*items):
    return json.dumps({"directions": list(items)})


THREE = reply(
    direction(),
    direction(
        id="D2",
        title="Is iron limitation the niche of truly dark genes?",
        question="Is iron the niche?",
    ),
    direction(
        id="D3",
        title="Do community interaction genes hide among hypotheticals?",
        question="Do they mediate interactions?",
    ),
)


def run(tmp_path, monkeypatch, replies, **kw):
    corpus(tmp_path)
    agent = FakeAgent(tmp_path / "store", replies, **kw)
    install(monkeypatch, agent)
    assert directions.main(tmp_path) == 0
    return agent


def test_directions_writes_grounded_pages(tmp_path, monkeypatch):
    agent = run(tmp_path, monkeypatch, {f"directions/{TOPIC}": [THREE]})
    pages = sorted((tmp_path / "wiki/directions").glob("*.md"))
    assert len(pages) == 3
    fields, body = cards.read_page(pages[0])
    assert fields["type"] == "Research direction" and fields["topics"] == [TOPIC]
    assert (
        f"findings/{FID}" in fields["builds_on"] and f"conflicts/{CONFLICT}" in fields["builds_on"]
    )
    assert "## Hypothesis" in body and "## Closest published work" in body
    assert "[[data/kbase-ke-pangenome|KBase pangenome]]" in body
    assert f"directions/{TOPIC}/science-review" in agent.asked


def test_pack_leaves_reanalysis_proposals_out(tmp_path):
    corpus(tmp_path)
    pack = directions.topic_pack(tmp_path, TOPIC, ["a"])
    assert pack["PROPOSALS"] == ["Test whether dark genes encode transporters. [src: a]"]
    assert [f["id"] for f in pack["FINDINGS"]] == [FID]
    assert pack["PAPERS"] == [{"pmid": "29769716", "title": "Mutant phenotypes"}]


@pytest.mark.parametrize(
    ("change", "message"),
    [
        ({"title": "Recompute stress rates per experiment"}, "repeats or corrects"),
        (
            {"question": "Should we re-run the comparison with one threshold?"},
            "repeats or corrects",
        ),
        ({"findings": [], "conflicts": []}, "builds on no finding"),
        ({"findings": ["a--deadbeef"]}, "unknown finding ids"),
        ({"papers": ["11111111"]}, "not in PAPERS"),
        ({"prior_work": "PMID 22222222 already did this."}, "not in PAPERS"),
        ({"collections": ["kbase_made_up"]}, "not in COLLECTIONS"),
        ({"hypothesis": "Depletion reaches 61.5% in iron."}, "61.5"),
    ],
)
def test_checker_rejects(tmp_path, change, message):
    corpus(tmp_path)
    parse = directions.checker(directions.topic_pack(tmp_path, TOPIC, ["a"]))
    bad = reply(direction(**change), *json.loads(THREE)["directions"][1:])
    with pytest.raises(cards.CandidateError, match=message):
        parse(bad)
    assert parse(THREE).directions


def test_salvage_drops_only_named_directions(tmp_path, monkeypatch):
    objection = ["Direction 2 overstates the iron enrichment"]
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": objection},
        still_open={f"directions/{TOPIC}": objection},
    )
    titles = [
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    ]
    # "Direction 2" is index 1 counted from 1 and index 2 from 0: both are dropped.
    assert titles == ["# Are dark genes nutrient and community-interaction genes?"]


def test_unchanged_input_makes_no_calls_and_rerenders_from_reply(tmp_path, monkeypatch):
    agent = run(tmp_path, monkeypatch, {f"directions/{TOPIC}": [THREE]})
    calls = len(agent.asked)
    page = next((tmp_path / "wiki/directions").glob("*.md"))
    page.write_text("edited")
    assert directions.main(tmp_path) == 0
    assert len(agent.asked) == calls
    assert "## Hypothesis" in page.read_text()


def test_is_reanalysis_reads_the_opening_clause():
    assert is_reanalysis("Using the metadata, recompute rates per experiment.")
    assert is_reanalysis("Reconcile the two counts.")
    assert not is_reanalysis("Test whether dark genes encode transporters across 48 organisms.")


@pytest.mark.parametrize(
    "error",
    [
        JobFailed("Codex turn failed: This content was flagged for possible biological risk."),
        Refused("refused on claude-opus-5", "claude-opus-5"),
    ],
)
def test_content_refusal_fails_only_its_topic(tmp_path, monkeypatch, capsys, error):
    agent = run(
        tmp_path,
        monkeypatch,
        {f"directions/{TOPIC}": [THREE]},
        review_error={f"directions/{TOPIC}": error},
    )
    assert f"directions/{TOPIC}/science-review" in agent.asked
    assert not list((tmp_path / "wiki/directions").glob("*.md"))
    assert f"[FAILED] directions/{TOPIC}" in capsys.readouterr().out


def test_other_job_failures_still_stop_the_stage(tmp_path, monkeypatch):
    with pytest.raises(JobFailed, match="transport"):
        run(
            tmp_path,
            monkeypatch,
            {f"directions/{TOPIC}": [THREE]},
            review_error={f"directions/{TOPIC}": JobFailed("Codex transport failed: reset")},
        )


def renamed(n, title):
    items = json.loads(THREE)["directions"]
    items[n] = items[n] | {"title": title, "question": "A rewritten question about it?"}
    return reply(*items)


def test_salvage_follows_a_rewritten_direction_by_id(tmp_path, monkeypatch):
    objection = ["D2 overstates the iron enrichment"]
    rewritten = renamed(1, "Does iron scarcity select for truly dark genes?")
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [rewritten] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": objection},
        still_open={f"directions/{TOPIC}": objection},
    )
    titles = sorted(
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    )
    assert titles == [
        "# Are dark genes nutrient and community-interaction genes?",
        "# Do community interaction genes hide among hypotheticals?",
    ]


def test_salvage_reads_a_restated_issue_through_its_original(tmp_path, monkeypatch):
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D3 has no decisive test"]},
        still_open={f"directions/{TOPIC}": ["Issue 0 remains: the test is still not decisive"]},
    )
    titles = sorted(
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    )
    assert "# Do community interaction genes hide among hypotheticals?" not in titles
    assert len(titles) == 2


def test_checker_rejects_repeated_ids(tmp_path):
    corpus(tmp_path)
    parse = directions.checker(directions.topic_pack(tmp_path, TOPIC, ["a"]))
    items = json.loads(THREE)["directions"]
    with pytest.raises(cards.CandidateError, match="repeated"):
        parse(reply(items[0], items[1] | {"id": "D1"}, items[2]))


def test_a_refused_verification_fails_the_topic_without_salvage(tmp_path, monkeypatch, capsys):
    refusal = JobFailed("Codex turn failed: flagged for possible biological risk")
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D2 overstates the iron enrichment"]},
        review_error={},
        verify_error={f"directions/{TOPIC}": refusal},
    )
    out = capsys.readouterr().out
    assert "[SALVAGED]" not in out and f"[FAILED] directions/{TOPIC}" in out
    assert not list((tmp_path / "wiki/directions").glob("*.md"))


def test_a_new_objection_that_mentions_an_old_issue_names_its_own_item(tmp_path, monkeypatch):
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D2 overstates the iron enrichment"]},
        still_open={
            f"directions/{TOPIC}": ["D3 adds an unsupported mechanism while fixing issue 0"]
        },
    )
    titles = sorted(
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    )
    assert titles == [
        "# Are dark genes nutrient and community-interaction genes?",
        "# Is iron limitation the niche of truly dark genes?",
    ]


def test_an_unresolvable_restatement_fails_the_topic(tmp_path, monkeypatch, capsys):
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D2 overstates the iron enrichment"]},
        still_open={f"directions/{TOPIC}": ["Issue 7 remains: the test is not decisive"]},
    )
    assert f"[FAILED] directions/{TOPIC}" in capsys.readouterr().out


def test_a_topic_that_loses_its_evidence_loses_its_directions(tmp_path, monkeypatch):
    run(tmp_path, monkeypatch, {f"directions/{TOPIC}": [THREE]})
    assert list((tmp_path / "wiki/directions").glob("*.md"))
    (tmp_path / "wiki/findings" / f"{FID}.md").unlink()
    (tmp_path / "wiki/conflicts" / f"{CONFLICT}.md").unlink()
    assert directions.main(tmp_path) == 0
    assert not list((tmp_path / "wiki/directions").glob("*.md"))
    state = json.loads((tmp_path / "state/directions.json").read_text())
    assert TOPIC not in state


def test_a_failed_topic_lists_only_its_own_jobs(tmp_path, monkeypatch):
    """F5: retrying one failed topic must not reject another topic's reviewed jobs."""
    corpus(tmp_path)
    (tmp_path / "state/curator-topics.json").write_text(
        json.dumps(
            {
                "groups": [
                    {"title": "Dark Matter", "concepts": ["gap"]},
                    {"title": "Light Matter", "concepts": ["gap"]},
                ]
            }
        )
    )
    scope(tmp_path, reports=["a"], topics=[TOPIC, "light-matter"])
    agent = FakeAgent(
        tmp_path / "store",
        {f"directions/{TOPIC}": [THREE], "directions/light-matter": [THREE]},
        review_error={
            "directions/light-matter": JobFailed(
                "Codex turn failed: flagged for possible biological risk."
            )
        },
    )
    install(monkeypatch, agent)
    recorded = {}
    monkeypatch.setattr(
        directions, "record_failure", lambda step, result: recorded.__setitem__(step, result)
    )
    assert directions.main(tmp_path) == 0
    failed = recorded["directions/light-matter"]
    assert failed.jobs and all("light-matter" in job for job in failed.jobs)


def test_a_failed_refresh_retires_pages_that_build_on_removed_work(tmp_path, monkeypatch, capsys):
    """A refused redraft keeps old pages only while everything they build on still exists."""
    run(tmp_path, monkeypatch, {f"directions/{TOPIC}": [THREE]})
    assert len(list((tmp_path / "wiki/directions").glob("*.md"))) == 3
    # A headlines rerun replaced the finding every page builds on with a new one.
    new = "a--9f8e7d6c"
    old_page = tmp_path / "wiki/findings" / f"{FID}.md"
    old_page.rename(old_page.with_name(f"{new}.md"))
    novelty = tmp_path / "state/novelty.json"
    novelty.write_text(novelty.read_text().replace(FID, new))
    error = Refused("refused on claude-opus-5", "claude-opus-5")
    agent = FakeAgent(
        tmp_path / "store2",
        {f"directions/{TOPIC}": [THREE.replace(FID, new)]},
        review_error={f"directions/{TOPIC}": error},
    )
    install(monkeypatch, agent)
    capsys.readouterr()
    assert directions.main(tmp_path) == 0
    assert f"[FAILED] directions/{TOPIC}" in capsys.readouterr().out
    assert not list((tmp_path / "wiki/directions").glob("*.md"))


def test_two_topics_with_the_same_direction_keep_their_own_pages(tmp_path, monkeypatch):
    corpus(tmp_path)
    (tmp_path / "state/curator-topics.json").write_text(
        json.dumps(
            {
                "groups": [
                    {"title": "Dark Matter", "concepts": ["gap"]},
                    {"title": "Light Matter", "concepts": ["gap"]},
                ]
            }
        )
    )
    scope(tmp_path, reports=["a"], topics=[TOPIC, "light-matter"])
    replies = {f"directions/{TOPIC}": [THREE], "directions/light-matter": [THREE]}
    agent = FakeAgent(tmp_path / "store", replies)
    install(monkeypatch, agent)
    assert directions.main(tmp_path) == 0
    out = tmp_path / "wiki/directions"
    assert len(directions.pages_for(out, TOPIC)) == 3
    assert len(directions.pages_for(out, "light-matter")) == 3
    # A second run finds both topics current and rewrites nothing.
    hashes = {p.name: p.read_bytes() for p in out.glob("*.md")}
    asked = len(agent.asked)
    assert directions.main(tmp_path) == 0
    assert len(agent.asked) == asked
    assert {p.name: p.read_bytes() for p in out.glob("*.md")} == hashes


@pytest.mark.parametrize(
    ("change", "message"),
    [
        ({"title": "Dark genes are nutrient genes"}, "question ending in"),
        ({"hypothesis": "Dark genes co-vary with transporters (rho = 0.41)."}, "statistic"),
        ({"hypothesis": "Dark genes significantly co-vary with transporter genes."}, "statistic"),
        ({"test": "Join ecotype_env_reanalysis to the Fitness Browser organisms."}, "identifiers"),
        ({"test": "Rerun the cofitness the report describes as pending."}, "'the report'"),
    ],
)
def test_reader_text_is_plain_and_titles_are_questions(tmp_path, change, message):
    corpus(tmp_path)
    parse = directions.checker(directions.topic_pack(tmp_path, TOPIC, ["a"]))
    items = json.loads(THREE)["directions"]
    with pytest.raises(cards.CandidateError, match=message):
        parse(reply(items[0] | change, items[1], items[2]))


def test_a_direction_on_another_topics_evidence_goes_back(tmp_path, monkeypatch):
    corpus(tmp_path)
    monkeypatch.setattr(directions, "SAME_EVIDENCE_MIN", 2)
    pack = directions.topic_pack(tmp_path, TOPIC, ["a"])
    pack["OTHER_TOPICS"] = [
        {"topic": "light-matter", "title": "Do dark genes do it?"}
        | {"findings": [FID], "conflicts": [CONFLICT]}
    ]
    with pytest.raises(cards.CandidateError, match="same evidence as 'Do dark genes do it"):
        directions.checker(pack)(THREE)
    # Within one reply the second of two same-evidence directions goes back too.
    pack["OTHER_TOPICS"] = []
    with pytest.raises(cards.CandidateError, match="same evidence as D1"):
        directions.checker(pack)(THREE)


def test_another_topics_rewrite_does_not_make_a_topic_stale(tmp_path, monkeypatch):
    corpus(tmp_path)
    (tmp_path / "state/curator-topics.json").write_text(
        json.dumps(
            {
                "groups": [
                    {"title": "Dark Matter", "concepts": ["gap"]},
                    {"title": "Light Matter", "concepts": ["gap"]},
                ]
            }
        )
    )
    scope(tmp_path, reports=["a"], topics=[TOPIC, "light-matter"])
    agent = FakeAgent(
        tmp_path / "store", {f"directions/{TOPIC}": [THREE], "directions/light-matter": [THREE]}
    )
    install(monkeypatch, agent)
    assert directions.main(tmp_path) == 0
    path = tmp_path / "state/directions.json"
    state = json.loads(path.read_text())
    state["light-matter"]["reply"]["directions"][0]["title"] = "Is light the niche?"
    path.write_text(json.dumps(state))
    asked = len(agent.asked)
    assert directions.main(tmp_path) == 0
    assert len(agent.asked) == asked


def test_prompt_asks_for_plain_questions_and_new_projects():
    """Content review, Nov 2026: statistics, ids and re-run projects on question pages."""
    assert "The title is a question ending in '?'" in directions.PROMPT
    assert "is a re-analysis, not a new project" in directions.PROMPT
    assert "OTHER_TOPICS lists the directions other topics" in directions.PROMPT


def test_a_curator_reschedule_keeps_saved_replies_and_asks_nothing(tmp_path, monkeypatch):
    """PR #20 review: clearing state/directions.json on a code change emptied OTHER_TOPICS,
    which changed the drafts' text and bought them again."""
    from beril_wiki.agentic import curator

    corpus(tmp_path)
    agent = FakeAgent(tmp_path / "store", {f"directions/{TOPIC}": [THREE]})
    install(monkeypatch, agent)
    assert directions.main(tmp_path) == 0
    saved = json.loads((tmp_path / "state/directions.json").read_text())
    curator.invalidate_outputs(
        tmp_path,
        "directions",
        {"semantic": "old", "outputs": {}},
        {"semantic": "new", "outputs": {}},
    )
    assert json.loads((tmp_path / "state/directions.json").read_text()) == saved
    asked = len(agent.asked)
    assert directions.main(tmp_path) == 0
    assert len(agent.asked) == asked


def test_a_saved_reply_todays_checks_reject_is_drafted_again(tmp_path, monkeypatch):
    corpus(tmp_path)
    agent = FakeAgent(tmp_path / "store", {f"directions/{TOPIC}": [THREE, THREE]})
    install(monkeypatch, agent)
    assert directions.main(tmp_path) == 0
    path = tmp_path / "state/directions.json"
    state = json.loads(path.read_text())
    # A reply accepted before titles had to be questions.
    state[TOPIC]["reply"]["directions"][0]["title"] = "Dark genes are nutrient genes"
    path.write_text(json.dumps(state))
    asked = agent.asked.count(f"directions/{TOPIC}")
    assert directions.main(tmp_path) == 0
    assert agent.asked.count(f"directions/{TOPIC}") == asked + 1


def test_a_question_may_name_redone_work_as_context():
    """Rerun, Nov 2026: 'after reannotation' sent a real question back four times."""
    assert not asks_to_redo(
        "Do genes that stay dark after reannotation mediate contact with other microbes?"
    )
    assert asks_to_redo("Recompute the stress rates per experiment")
    assert asks_to_redo("Does re-running the cofitness change the modules?")


def test_a_question_title_may_run_a_few_words_past_the_prompt_limit(tmp_path):
    corpus(tmp_path)
    parse = directions.checker(directions.topic_pack(tmp_path, TOPIC, ["a"]))
    items = json.loads(THREE)["directions"]
    long = (
        "Does adding an amino acid to soil erode that amino acid's synthesis genes in the"
        " community?"
    )
    assert parse(reply(items[0] | {"title": long}, items[1], items[2]))


@pytest.mark.parametrize(("expect", "asked"), [("b", False), (None, True)])
def test_a_run_for_one_project_leaves_a_failed_topic(tmp_path, monkeypatch, expect, asked):
    """Sol review of edcce0b: a researcher's run starts from a fresh job store, so a topic
    failure kept only in failures.json was re-asked and, refused again, failed the run
    under --strict-pages. The failure is read from the committed state, so no run for one
    project re-asks it; a maintainer run does, and its accepted reply clears the mark."""
    main_root, researcher = tmp_path / "main", tmp_path / "researcher"
    main_root.mkdir()
    corpus(main_root)
    error = Refused("refused on claude-opus-5", "claude-opus-5")
    agent = FakeAgent(
        tmp_path / "store-a",
        {f"directions/{TOPIC}": [THREE]},
        review_error={f"directions/{TOPIC}": error},
    )
    install(monkeypatch, agent)
    assert directions.main(main_root) == 0
    assert json.loads((main_root / directions.STATE).read_text())[TOPIC]["failed"] is True
    shutil.copytree(main_root, researcher)
    before = (researcher / directions.STATE).read_text()
    agent = FakeAgent(tmp_path / "store-b", {f"directions/{TOPIC}": [THREE]})
    if expect:
        agent.config["expect_source"] = expect
    install(monkeypatch, agent)
    monkeypatch.setattr(cards, "strict_pages", lambda: True)
    assert directions.main(researcher) == 0
    after = (researcher / directions.STATE).read_text()
    if asked:
        assert f"directions/{TOPIC}/science-review" in agent.asked
        assert "failed" not in json.loads(after)[TOPIC]
    else:
        assert agent.asked == [] and after == before
