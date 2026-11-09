"""Which results the home and topic pages show, and which questions the home shows."""

from __future__ import annotations

from beril_wiki.publish.cards.corpus import Corpus, eligible, result_type
from beril_wiki.publish.cards.links import links_index
from beril_wiki.publish.cards.text import INTEREST, compare_text

# A topic's three cards include one of these when the topic has one, so a negative
# result is as easy to find as a positive one.
SPOTLIGHT = ("negative",)


def pick_lists(c: Corpus) -> tuple[list[str], dict[str, list[str]]]:
    if c._picks is None:
        ids = [f for f in sorted(c.findings) if eligible(c, f)]
        project = {f: c.findings[f][0].get("source", "") for f in ids}
        # The home shows results only from projects that feed two or more topics.
        broad = [f for f in ids if len(c.topics_of(project[f])) >= 2]
        home = _home(c, broad, project)
        topics: dict[str, list[str]] = {}
        for t in sorted({t for f in ids for t in c.topics_of(project[f])}):
            members = [f for f in ids if t in c.topics_of(project[f])]
            picked: list[str] = []
            for f in members:
                if len(picked) < 3 and project[f] not in {project[p] for p in picked}:
                    picked.append(f)
            if len(picked) == 3 and not any(result_type(c, f) in SPOTLIGHT for f in picked):
                used = {project[f] for f in picked[:-1]}
                swap = next(
                    (
                        f
                        for f in members
                        if result_type(c, f) in SPOTLIGHT and project[f] not in used
                    ),
                    None,
                )
                if swap:
                    picked[-1] = swap
            topics[t] = picked
        c._picks = (home, topics)
    return c._picks


def _home(c: Corpus, ids: list[str], project: dict[str, str], n: int = 3) -> list[str]:
    """The n most interesting results, each from its own project and topic.

    Most interesting: furthest from PubMed abstracts (a new direction, then differs,
    then adds to), then linked to the most other projects, then a positive result before
    the other kinds, then from the project in the most topics."""
    tier = {text: i for i, text in enumerate(INTEREST)}
    others: dict[str, set[str]] = {}
    for link in links_index(c):
        if "a" in link and link["pa"] != link["pb"]:
            others.setdefault(link["a"], set()).add(link["pb"])
            others.setdefault(link["b"], set()).add(link["pa"])

    def rank(f: str) -> tuple:
        return (
            tier.get(compare_text(c.labels.get(f)), len(tier)),
            -len(others.get(f, ())),
            result_type(c, f) != "positive",
            -len(c.topics_of(project[f])),
            f,
        )

    chosen: list[str] = []
    for f in sorted(ids, key=rank):
        if len(chosen) == n:
            break
        if project[f] in {project[x] for x in chosen}:
            continue
        if c.display_topic(project[f]) in {c.display_topic(project[x]) for x in chosen}:
            continue
        chosen.append(f)
    return chosen


def home_picks(c: Corpus, n: int = 3) -> list[str]:
    """Finding ids for the home page: the most interesting, from distinct topics and projects."""
    return pick_lists(c)[0][:n]


def topic_picks(c: Corpus, topic: str, n: int = 3) -> list[str]:
    """Up to n findings in a topic, by id, at most one per project."""
    return pick_lists(c)[1].get(topic, [])[:n]


def home_questions(c: Corpus, n: int = 3) -> list[str]:
    """Cross-project questions for the home: most projects, then most topics; no project twice."""
    ranked = sorted(
        (d for d in c.directions if c.cross_projects(d)),
        key=lambda d: (
            -len(c.cross_projects(d)),
            -len(c.group_topics(list(c.cross_projects(d)))),
            d,
        ),
    )
    chosen: list[str] = []
    used: set[str] = set()
    for d in ranked:
        sids = set(c.cross_projects(d))
        if len(chosen) < n and not used & sids:
            chosen.append(d)
            used |= sids
    return chosen
