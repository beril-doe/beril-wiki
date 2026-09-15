"""Model-selected topic membership and its existing cached prose writer."""

import json

import pytest

from beril_wiki.agentic import runtime as R
from beril_wiki.agentic import topics as T
from beril_wiki.stages import topics as stage


def corpus(root):
    folder = root / "wiki/concepts"
    folder.mkdir(parents=True)
    for stem in ("a", "b", "c"):
        (folder / f"{stem}.md").write_text(
            f'---\ndescription: "Description {stem}"\n---\n# Concept {stem}\n\n'
            f"Private full body {stem}.\n"
        )


GROUPS = [
    {"title": "Chosen Pair", "concepts": ["a", "c"]},
    {"title": "Separate B", "concepts": ["b"]},
]


def save(root, groups=GROUPS):
    (root / "state").mkdir(exist_ok=True)
    (root / "state/curator-topics.json").write_text(
        json.dumps(
            dict(
                version=1,
                reason="Organize concepts",
                groups=groups,
                concepts=R.manifest(root, ("wiki/concepts",)),
            )
        )
    )


@pytest.mark.parametrize(
    "groups",
    [
        [],
        [{"title": "Missing", "concepts": ["a", "b"]}],
        [{"title": "Unknown", "concepts": ["a", "b", "c", "z"]}],
        [{"title": "Repeated", "concepts": ["a", "b", "c", "a"]}],
        [GROUPS[0], {"title": "chosen-pair", "concepts": ["b"]}],
        [{"title": "Index", "concepts": ["a", "b", "c"]}],
        [{"title": "...", "concepts": ["a", "b", "c"]}],
        [{"title": "Good", "concepts": ["a", "b", "c"], "extra": True}],
        [{"title": "Empty", "concepts": []}, *GROUPS],
        [{"title": "Bad\n# Heading", "concepts": ["a", "b", "c"]}],
        [{"title": 5, "concepts": ["a", "b", "c"]}],
    ],
)
def test_invalid_groups_fail_closed(tmp_path, groups):
    corpus(tmp_path)
    with pytest.raises(R.CandidateError):
        T.validate_groups(tmp_path, groups)


def test_inventory_is_compact_and_groups_are_normalized(tmp_path):
    corpus(tmp_path)
    (tmp_path / "wiki/concepts/a.md").write_text(
        '---\ndescription: "' + "x" * 500 + '"\n---\n# Alpha\n\nPrivate full body.'
    )
    inventory = T.topic_inventory(tmp_path)
    assert set(inventory[0]) == {"stem", "title", "description"}
    assert len(inventory[0]["description"]) == 300
    assert "Private full body" not in json.dumps(inventory)
    assert T.validate_groups(tmp_path, [{"title": "  All  ", "concepts": ["c", "a", "b"]}]) == [
        {"title": "All", "concepts": ["a", "b", "c"]}
    ]


@pytest.mark.parametrize("change", ["edit", "add", "delete", "version"])
def test_load_rejects_stale_or_unsupported_state(tmp_path, change):
    corpus(tmp_path)
    save(tmp_path)
    assert T.load_groups(tmp_path) == GROUPS
    if change == "delete":
        (tmp_path / "wiki/concepts/a.md").unlink()
    elif change == "version":
        path = tmp_path / "state/curator-topics.json"
        path.write_text(path.read_text().replace('"version": 1', '"version": 2'))
    else:
        (tmp_path / "wiki/concepts" / ("a.md" if change == "edit" else "d.md")).write_text("new")
    with pytest.raises(R.WorkflowError):
        T.load_groups(tmp_path)


def test_proposal_repairs_membership_and_supplies_existing_hubs(tmp_path, monkeypatch):
    corpus(tmp_path)
    (tmp_path / "wiki/topics").mkdir()
    (tmp_path / "wiki/topics/old.md").write_text("# Old Name\n\n[[concepts/a]]")
    agent = R.Runtime.__new__(R.Runtime)
    agent._validator = agent._validation_context = None
    calls = []

    def ask(messages, step):
        calls.append((messages, step))
        return json.dumps(
            dict(reason="Retain an independent concept", groups=[] if len(calls) == 1 else GROUPS)
        )

    monkeypatch.setattr(agent, "ask", ask)
    T.propose_topics(tmp_path, agent)
    assert [step for _, step in calls] == ["curator/topics", "curator/topics/repair"]
    assert "missing" in calls[1][0][-1]["content"].lower()
    assert "Old Name" in calls[0][0][0]["content"]
    assert "Private full body" not in calls[0][0][0]["content"]
    assert T.load_groups(tmp_path) == GROUPS


def test_empty_corpus_does_not_generate(tmp_path):
    T.propose_topics(tmp_path, None)
    assert T.load_groups(tmp_path) == []


@pytest.mark.parametrize(
    "bad",
    [
        {"reason": "  ", "groups": GROUPS},
        {"reason": "Valid", "groups": GROUPS, "extra": True},
        {"reason": 5, "groups": GROUPS},
    ],
)
def test_invalid_proposal_stops_after_one_repair_without_replacing_state(
    tmp_path, monkeypatch, bad
):
    corpus(tmp_path)
    save(tmp_path)
    previous = (tmp_path / "state/curator-topics.json").read_bytes()
    agent = R.Runtime.__new__(R.Runtime)
    agent._validator = agent._validation_context = None
    calls = []

    def ask(messages, step):
        calls.append(step)
        assert "existing_groups" in messages[0]["content"]
        assert "Chosen Pair" in messages[0]["content"]
        return json.dumps(bad)

    monkeypatch.setattr(agent, "ask", ask)
    with pytest.raises(R.CandidateError):
        T.propose_topics(tmp_path, agent)
    assert calls == ["curator/topics", "curator/topics/repair"]
    assert (tmp_path / "state/curator-topics.json").read_bytes() == previous


def test_actual_writer_uses_selected_groups_names_cache_and_home_refresh(tmp_path, monkeypatch):
    corpus(tmp_path)
    save(tmp_path)
    assert stage.cluster_concepts(
        {p.stem: stage.parse_page(p) for p in (tmp_path / "wiki/concepts").glob("*.md")}
    ) == [["a", "b", "c"]]
    monkeypatch.setattr(stage, "ROOT", tmp_path)
    monkeypatch.setattr(stage, "OUT", tmp_path / "wiki")
    monkeypatch.setattr(stage, "FORCE", False)
    monkeypatch.setattr(stage, "configured", lambda: True)
    monkeypatch.setattr(stage.sys, "argv", ["topics"])

    def forbidden(*args, **kwargs):
        pytest.fail("Agentic topics must not use graph clustering or model naming")

    monkeypatch.setattr(stage, "cluster_concepts", forbidden)
    calls = []

    def llm(prompt, system="", **kwargs):
        assert kwargs.get("step") != "topics/names"
        calls.append(prompt)
        title = prompt.splitlines()[0].removeprefix("TOPIC: ")
        return f"# {title}\n\nA lead.\n\n## Where to Go Deeper\n"

    monkeypatch.setattr(stage, "llm", llm)
    homes = []

    def home(hubs, stats):
        homes.append(hubs)
        (tmp_path / "wiki/index.md").write_text("# Home\n")

    monkeypatch.setattr(stage, "write_home", home)
    assert stage.main() == 0
    assert len(calls) == 2
    assert "[file: concepts/a]" in calls[0] and "[file: concepts/c]" in calls[0]
    assert "[file: concepts/b]" not in calls[0]
    assert (tmp_path / "wiki/topics/chosen-pair.md").exists()
    assert stage.main() == 0
    assert len(calls) == 2 and len(homes) == 1
    monkeypatch.setattr(stage.sys, "argv", ["topics", "--refresh-home"])
    assert stage.main() == 0
    assert len(calls) == 2 and len(homes) == 2
    save(tmp_path, [{"title": "Chosen pair", "concepts": ["a", "c"]}, GROUPS[1]])
    assert stage.main() == 0
    assert len(calls) == 3
    assert (tmp_path / "wiki/topics/chosen-pair.md").read_text().startswith("# Chosen pair")
