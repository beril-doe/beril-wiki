#!/usr/bin/env python3
"""Shared results: one plain statement for results that two or more projects reached.

Groups are connected components over the links stage's related-result links: 2 to 4
results from two or more projects whose projects together feed two or more main topics.
Code sets each group's relation (the weakest of its links). Claude writes a title, a
sentence, the question the projects asked, a short label per result and how the results
relate; code rejects statistics, new figures and any wording that one project confirms
another; GPT reviews faithfulness to every member. A failure fails only its group.

Output: state/shared.json, joined into the home page at publish.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from beril_wiki.agentic.prose import (
    PageFailure,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import CandidateError, atomic_json, digest, prompt
from beril_wiki.paths import ROOT
from beril_wiki.publish.cards import STATS
from beril_wiki.stages import cards, links
from beril_wiki.stages.gists import report_title

STATE = Path("state/shared.json")
LINKS = Path("state/links.json")
PROMPT_TAG = "shared@2"
MAX_MEMBERS = 4
# Strongest first; a group takes the weakest relation among its links.
RELATIONS = (
    "same result",
    "one extends the other",
    "same direction, different definitions",
    "similar comparison, different scope",
    "one measures what the other cannot",
)
LIMITS = {"title": 12, "sentence": 45, "question": 14, "how": 50}


class Group(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    sentence: str
    question: str
    lanes: dict[str, str]
    how: str


PROMPT = prompt(
    PROMPT_TAG,
    "RESULTS holds two to four results from different microbial-biology research projects "
    "that a reviewer linked, with the RELATION between them. Write for a microbiologist "
    "who does not read statistics, in plain biological words.\n"
    "'title': at most 12 words naming what the projects found. 'sentence': one or two "
    "sentences, at most 45 words, saying what the projects found and why it is "
    "interesting. 'question': at most 14 words, ending with '?', the question the projects "
    "asked. 'lanes': for each result id, at most 8 words naming what that project "
    "compared or measured. 'how': at most two sentences, 50 words, saying how the results "
    "relate, following the RELATION; when the results report identical figures or one "
    "project uses another's data, say they share an analysis or data, in the sentence as "
    "well as in 'how'.\n"
    "When the results reach different conclusions (one finds a pattern, the other does "
    "not, or they differ in direction), the title and sentence say what differs; never "
    "present them as one result. Claim nothing the results did not test: a comparison of "
    "how common genes are does not show what niche they serve.\n"
    "Never say or imply that the projects confirm, corroborate, validate, reproduce, "
    "replicate or agree with each other, or that they are independent. Do not write "
    "caveats, limitations or 'however' clauses, or 'novel', 'first' or 'breakthrough'. "
    "Use no statistics and no figure the results do not state. Make no claim about "
    "people.\n"
    'Return only JSON {"title": "...", "sentence": "...", "question": "...", '
    '"lanes": {"<result id>": "..."}, "how": "..."}.\n',
)


def words(text: str) -> int:
    return len(text.split())


def components(edges: list[tuple[str, str]]) -> list[list[str]]:
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        parent[find(a)] = find(b)
    groups: dict[str, list[str]] = {}
    for x in parent:
        groups.setdefault(find(x), []).append(x)
    return sorted(sorted(g) for g in groups.values())


def group_topics(root: Path, projects: list[str]) -> list[str]:
    """The union of the projects' main topics."""
    groups = cards.topic_groups(root)
    cites = cards.concept_citations(root)
    return sorted({t for sid in projects for t in cards.main_topics(sid, groups, cites)})


def checker(members: dict[str, dict]) -> Callable[[str], Group]:
    pool = " ".join(
        " ".join(map(str, (f["claim"], f["quote"], f["quantities"]))) for f in members.values()
    )

    def parse(raw: str) -> Group:
        reply = cards.parse_reply(raw, Group)
        assert isinstance(reply, Group)
        problems = []
        texts = {k: getattr(reply, k).strip() for k in LIMITS}
        for field, limit in LIMITS.items():
            if not 3 <= words(texts[field]) <= limit:
                problems.append(f"{field} needs 3 to {limit} words")
        if not texts["question"].endswith("?"):
            problems.append("question must end with '?'")
        if sorted(reply.lanes) != sorted(members):
            problems.append(f"lanes must name exactly these result ids: {sorted(members)}")
        for fid, lane in reply.lanes.items():
            if not 2 <= words(lane) <= 8:
                problems.append(f"lane {fid} needs 2 to 8 words")
            texts[f"lane {fid}"] = lane
        for field, text in texts.items():
            if STATS.search(text):
                problems.append(f"{field} contains a statistic; say it in words")
            if extra := cards.new_figures(text, pool):
                problems.append(f"{field} uses figures the results never state: {extra}")
            if links.STAT_WORDS.search(text):
                problems.append(f"{field} uses significance or power wording; say it in words")
            if banned := links.BANNED.search(text):
                problems.append(
                    f"{field} says '{banned.group(0)}'; say how the results relate without "
                    "claiming one confirms or matches the other"
                )
        if problems:
            raise CandidateError("; ".join(problems))
        return reply.model_copy(
            update={k: v for k, v in texts.items() if k in LIMITS}
            | {"lanes": {k: v.strip() for k, v in reply.lanes.items()}}
        )

    return parse


def reads_badly(group: dict) -> bool:
    """Accepted text that today's word checks would reject."""
    texts = [str(group.get(k, "")) for k in LIMITS] + list((group.get("lanes") or {}).values())
    return any(
        STATS.search(t) or links.STAT_WORDS.search(t) or links.BANNED.search(t) for t in texts
    )


def status(root: Path = ROOT) -> int:
    path = root / STATE
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    accepted = [g for g in state.values() if not g.get("failed")]
    failed = len(state) - len(accepted)
    print(f"shared: {len(accepted)} accepted, {failed} failed")
    for g in accepted:
        print(f"  {len(g['projects'])} projects, {len(g['topics'])} topics: {g['title']}")
    return 0


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    args = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    args.add_argument("--status", action="store_true", help="count groups; run nothing")
    if args.parse_args(argv or []).status:
        return status(root)
    if not cards.require_runtime("shared"):
        return 0
    state_path = root / STATE
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    link_path = root / LINKS
    saved_links = json.loads(link_path.read_text(encoding="utf-8")) if link_path.exists() else {}
    if "links" not in saved_links:
        # No finished links checkpoint yet: building groups from none would prune them all.
        print("shared: no current links to group; nothing changed")
        return 0
    current = saved_links["links"]
    findings = links.read_findings(root)
    related = [
        x
        for x in current
        if x["level"] == "finding"
        and x["type"] in RELATIONS
        and x["a"] in findings
        and x["b"] in findings
    ]
    config = cards.runtime().config
    policy = cards.policy(config, ("cards", "card_review"))

    todo = []
    groups: dict[str, dict] = {}
    for members in components([(x["a"], x["b"]) for x in related]):
        projects = sorted({findings[f]["report"] for f in members})
        if len(members) > MAX_MEMBERS:
            print(f"  shared: skipped a group of {len(members)} results: {members}")
            continue
        if len(projects) < 2:
            continue
        topics = group_topics(root, projects)
        if len(topics) < 2:
            continue
        inner = [x for x in related if x["a"] in members and x["b"] in members]
        relation = max((x["type"] for x in inner), key=RELATIONS.index)
        gid = "g-" + digest(members)[:10]
        texts = {
            f: {k: findings[f][k] for k in ("title", "claim", "quote", "quantities")}
            | {"project": report_title(root, findings[f]["report"])}
            for f in members
        }
        pack = {"RESULTS": texts, "RELATION": relation, "LINKS": [x["label"] for x in inner]}
        key = digest([pack, PROMPT_TAG, policy])
        groups[gid] = {"members": members, "projects": projects, "topics": topics}
        groups[gid] |= {"relation": relation, "input": key}
        prev = state.get(gid, {})
        if prev.get("input") == key and not prev.get("failed") and not reads_badly(prev):
            continue
        todo.append((gid, pack, {f: findings[f] for f in members}))

    # Before any job can stop the run, no group outside the current links and no text
    # written for older inputs stays publishable.
    for gid in list(state):
        if gid not in groups:
            state.pop(gid)
        elif state[gid].get("input") != groups[gid]["input"] or reads_badly(state[gid]):
            state[gid] = {"input": "", "failed": True}
    atomic_json(state_path, dict(sorted(state.items())))

    def write(item: tuple) -> dict:
        gid, pack, members = item
        mine = cards.runtime()  # a ledger connection belongs to the thread that opened it
        step = f"shared/{gid}"
        try:
            reply = cards.reviewed(
                [{"role": "user", "content": PROMPT + json.dumps(pack, ensure_ascii=False)}],
                step,
                checker(members),
                agent=mine,
            )
        except CandidateError as exc:
            raise cards.failure(step, exc, mine) from exc
        return reply.model_dump()

    done = failed = 0
    for (gid, *_), result in parallel(todo, write, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"shared/{gid}", result)
            print(f"  [FAILED] shared/{gid}: {result}")
            state[gid] = {"input": groups[gid]["input"], "failed": True}
        else:
            state[gid] = groups[gid] | result
            record_failure(f"shared/{gid}", None)
            done += 1
        # Saved per group, so a run stopped by its budget keeps what it finished.
        atomic_json(state_path, dict(sorted(state.items())))
    for gid in list(state):
        if gid not in groups:
            state.pop(gid)
        elif not state[gid].get("failed"):
            # Topic membership can move without changing what the model read.
            state[gid] |= groups[gid]
    atomic_json(state_path, dict(sorted(state.items())))
    prune_failures("shared/", {f"shared/{gid}" for gid in groups})
    print(f"shared: {done} written, {len(groups) - len(todo)} current, {failed} failed")
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
