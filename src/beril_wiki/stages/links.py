#!/usr/bin/env python3
"""Links between projects: related results, and reports that use or cite another project.

Code finds candidates; Claude sorts each into a relation with a short reader label;
GPT reviews every batch. Two kinds of candidate:

- a pair of results from different projects whose title and claim are lexically close
  (TF-IDF cosine at least 0.30) and whose projects a common concept or conflict cites;
- a source report line that names another project by id or exact report title.

Each candidate is cached under a digest of its own texts, so a corpus change re-asks
only the candidates whose texts changed. A failed batch leaves its candidates without
a current answer. Same-open-question links need no model: publish reads them from the
direction records.

Output: state/links.json, joined into the Results picture and home cards at publish.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from collections.abc import Callable
from itertools import combinations
from pathlib import Path
from typing import Literal, get_args

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
from beril_wiki.publish.cards import STATS, title_of
from beril_wiki.stages import cards
from beril_wiki.stages.novelty import finding_text

STATE = Path("state/links.json")
FINDINGS = Path("wiki/findings")
SOURCES = Path("wiki/sources")
PROMPT_TAG = "links@1"
THRESHOLD = 0.30
BATCH = 8
LINES_PER_TARGET = 6
MAX_LABEL_WORDS = 16
STOP = frozenset(
    "a an the and or of to in for with from by on at is are was were be this that these "
    "those as not no but its it their than more across both all each any which only into "
    "has have had can may after between using based".split()
)
# Wording that would read as two projects confirming each other, plus the gists list.
BANNED = re.compile(
    r"\b(?:confirm\w*|corroborat\w*|validat\w*|reproduc\w*|replicat\w*|independen\w*"
    r"|agree\w*|novel|first|breakthrough|caveats?|limitations?|however)\b"
    r"|support(?:s|ed)? each other",
    re.I,
)
# Statistical and power wording a reader should not meet in a link label or shared text.
STAT_WORDS = re.compile(
    r"\b(?:(?:non-?)?significan\w*|(?:under|low|statistical )power\w*|effect sizes?"
    r"|statistic\w*|p-?values?)\b",
    re.I,
)

PairRelation = Literal[
    "same result",
    "one extends the other",
    "same direction, different definitions",
    "similar comparison, different scope",
    "one measures what the other cannot",
    "not the same question",
]
RefRelation = Literal[
    "uses its data or methods",
    "compares with its results",
    "corrects it",
    "applies its warning",
    "audits it",
    "lists it as a reference only",
    "not a reference",
]
DROPPED = {"not the same question", "not a reference"}


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    relation: str
    label: str = ""


class Reply(BaseModel):
    model_config = ConfigDict(extra="forbid")
    items: list[Item]


PAIR_PROMPT = prompt(
    PROMPT_TAG + "/pairs",
    "Each PAIR holds two results from different microbial-biology research projects: "
    "each result's claim, the evidence quote and its key figures. For each pair, say how "
    "the two results relate. Choose 'relation' from exactly these: 'same result' (both "
    "report the same measured outcome), 'one extends the other' (one builds a further "
    "analysis on the other's result), 'same direction, different definitions' (both find "
    "the same direction of effect but define the compared groups differently), 'similar "
    "comparison, different scope' (similar comparison on different organisms, cohorts or "
    "baselines), 'one measures what the other cannot' (one covers cases the other's method "
    "cannot reach), or 'not the same question' (shared words but different questions).\n"
    "Write 'label': at most 16 words a microbiologist reads on a link between the two "
    "projects, saying how they relate in plain biological words. Never say or imply that "
    "the projects confirm, corroborate, validate, reproduce or agree with each other, or "
    "that they are independent: identical figures often mean shared data. Use no "
    "statistics and no figure the pair does not state. Leave 'label' empty for 'not the "
    "same question'.\n"
    'Return only JSON {"items": [{"id": "P1", "relation": "...", "label": "..."}]}, one '
    "item per pair.\n",
)
REF_PROMPT = prompt(
    PROMPT_TAG + "/references",
    "A REPORT from a microbial-biology research project names other projects. For each "
    "NAMED project you get the report lines that mention it, with a line of context. Say "
    "what the report does with that project. Choose 'relation' from exactly these: 'uses "
    "its data or methods', 'compares with its results', 'corrects it', 'applies its "
    "warning' (it applies a pitfall or warning the other project documented), 'audits it', "
    "'lists it as a reference only', or 'not a reference' (a file name, a generic phrase, "
    "or a proposal the report did not carry out).\n"
    "Write 'label': at most 16 words a microbiologist reads on the link, saying what the "
    "report did with the other project, in plain words. Never say or imply that the "
    "projects confirm, corroborate, validate, reproduce or agree with each other. Use no "
    "statistics and no figure the lines do not state. Leave 'label' empty for 'not a "
    "reference'.\n"
    'Return only JSON {"items": [{"id": "R1", "relation": "...", "label": "..."}]}, one '
    "item per named project.\n",
)


def words(text: str) -> int:
    return len(text.split())


def normalized(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def read_findings(root: Path) -> dict[str, dict]:
    out = {}
    for page in sorted((root / FINDINGS).glob("*.md")):
        fields, body = cards.read_page(page)
        out[page.stem] = finding_text(fields, body) | {"title": title_of(body, page.stem)}
    return out


def memberships(root: Path) -> list[set[str]]:
    """The project sets each concept or conflict page cites."""
    pages = sorted((root / "wiki/concepts").glob("*.md"))
    pages += sorted((root / "wiki/conflicts").glob("*.md"))
    return [set(cards.projects_in(p.read_text(encoding="utf-8", errors="replace"))) for p in pages]


def pair_candidates(findings: dict[str, dict], groups: list[set[str]]) -> list[tuple[str, str]]:
    """Cross-project result pairs at or above the cosine threshold that a page cites together."""
    docs = {
        fid: Counter(
            w
            for w in re.findall(r"[a-z][a-z0-9]+", (f["title"] + " " + f["claim"]).lower())
            if w not in STOP
        )
        for fid, f in findings.items()
    }
    df = Counter(w for doc in docs.values() for w in doc)
    n = len(docs)
    vectors = {
        fid: {w: (1 + math.log(c)) * (1 + math.log((1 + n) / (1 + df[w]))) for w, c in doc.items()}
        for fid, doc in docs.items()
    }
    norms = {
        fid: math.sqrt(sum(v * v for v in vec.values())) or 1.0 for fid, vec in vectors.items()
    }
    out = []
    for a, b in combinations(sorted(findings), 2):
        pa, pb = findings[a]["report"], findings[b]["report"]
        if pa == pb:
            continue
        va, vb = vectors[a], vectors[b]
        score = sum(v * vb.get(w, 0.0) for w, v in va.items()) / (norms[a] * norms[b])
        if score >= THRESHOLD and any({pa, pb} <= g for g in groups):
            out.append((a, b))
    return out


def report_titles(root: Path) -> dict[str, str]:
    out = {}
    for path in sorted((root / SOURCES).glob("*__REPORT.md")):
        sid = path.name.removesuffix("__REPORT.md")
        if sid in cards.DIGESTS:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        out[sid] = re.sub(r"^Report:\s*", "", title_of(text, sid)).strip()
    return out


def reference_candidates(root: Path, titles: dict[str, str]) -> dict[tuple[str, str], list[str]]:
    """(citing report, named project) -> up to six mentions, each with a line of context."""
    patterns = {}
    for target, title in titles.items():
        pats = [
            re.compile(r"(?<![a-z0-9_])" + re.escape(target) + r"(?![a-z0-9_])", re.I),
            re.compile(
                r"(?<![a-z0-9])" + re.escape(target.replace("_", " ")) + r"(?![a-z0-9])", re.I
            ),
        ]
        norm = normalized(title)
        if len(norm.split()) >= 3:
            pats.append(re.compile(r"(?<![a-z0-9])" + re.escape(norm) + r"(?![a-z0-9])"))
        patterns[target] = pats
    out: dict[tuple[str, str], list[str]] = {}
    for sid in titles:
        lines = (root / SOURCES / f"{sid}__REPORT.md").read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            norm = normalized(line)
            for target, pats in patterns.items():
                if target == sid or not any(
                    p.search(norm if k == 2 else line) for k, p in enumerate(pats)
                ):
                    continue
                found = out.setdefault((sid, target), [])
                if len(found) < LINES_PER_TARGET:
                    window = [x.strip() for x in lines[max(0, i - 1) : i + 2] if x.strip()]
                    found.append(" / ".join(window)[:1200])
    return out


def checker(
    ids: list[str], relations: tuple[str, ...], pools: dict[str, str]
) -> Callable[[str], Reply]:
    """Every id answered once, a known relation, and a plain, bounded, unconfirming label."""

    def parse(raw: str) -> Reply:
        reply = cards.parse_reply(raw, Reply)
        assert isinstance(reply, Reply)
        problems = []
        seen = [item.id for item in reply.items]
        if sorted(seen) != sorted(ids):
            problems.append(f"answer each of {', '.join(ids)} exactly once")
        for item in reply.items:
            if item.relation not in relations:
                problems.append(f"{item.id}: relation must be one of {list(relations)}")
                continue
            label = item.label.strip()
            if item.relation in DROPPED:
                continue
            if not 3 <= words(label) <= MAX_LABEL_WORDS:
                problems.append(f"{item.id}: label needs 3 to {MAX_LABEL_WORDS} words")
            if STATS.search(label) or STAT_WORDS.search(label):
                problems.append(f"{item.id}: label contains a statistic or significance wording")
            if extra := cards.new_figures(label, pools.get(item.id, "")):
                problems.append(f"{item.id}: label uses figures the inputs never state: {extra}")
            if banned := BANNED.search(label):
                problems.append(
                    f"{item.id}: label says '{banned.group(0)}'; describe how the results "
                    "relate without claiming one confirms or matches the other"
                )
        if problems:
            raise CandidateError("; ".join(problems))
        return reply

    return parse


def pair_text(f: dict) -> dict:
    return {k: f[k] for k in ("title", "claim", "quote", "quantities", "report")}


def status(root: Path = ROOT) -> int:
    path = root / STATE
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    entries = state.get("candidates", {})
    kept = Counter(
        e["relation"] for e in entries.values() if e.get("relation") and not e.get("failed")
    )
    failed = sum(1 for e in entries.values() if e.get("failed"))
    print(f"links: {len(state.get('links', []))} current, {failed} failed candidates; {dict(kept)}")
    return 0


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    args = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    args.add_argument("--status", action="store_true", help="count links; run nothing")
    if args.parse_args(argv or []).status:
        return status(root)
    if not cards.require_runtime("links"):
        return 0
    state_path = root / STATE
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    entries: dict[str, dict] = state.get("candidates", {})
    config = cards.runtime().config
    policy = cards.policy(config, ("cards", "review"))

    findings = read_findings(root)
    titles = report_titles(root)
    # Candidate id -> (kind, endpoints, the texts its answer depends on).
    current: dict[str, tuple[str, str, str, dict]] = {}
    for a, b in pair_candidates(findings, memberships(root)):
        pack = {"A": pair_text(findings[a]), "B": pair_text(findings[b])}
        current[f"pair:{a}|{b}"] = ("pair", a, b, pack)
    for (sid, target), lines in sorted(reference_candidates(root, titles).items()):
        pack = {"REPORT": titles[sid], "NAMED": titles[target], "LINES": lines}
        current[f"ref:{sid}>{target}"] = ("ref", sid, target, pack)
    keys = {cid: digest([pack, PROMPT_TAG, policy]) for cid, (*_, pack) in current.items()}

    def stale(cid: str) -> bool:
        """No current answer: none yet, failed, changed inputs, or a label today's check rejects."""
        entry = entries.get(cid, {})
        if entry.get("input") != keys[cid] or entry.get("failed"):
            return True
        label = entry.get("label", "")
        return entry.get("relation") not in DROPPED and bool(
            STATS.search(label) or STAT_WORDS.search(label) or BANNED.search(label)
        )

    def current_links() -> list[dict]:
        out = []
        for cid, (kind, a, b, _) in current.items():
            entry = entries.get(cid, {})
            if stale(cid) or entry["relation"] in DROPPED:
                continue
            out.append(
                {"a": a, "b": b, "level": "finding" if kind == "pair" else "project"}
                | {"type": entry["relation"], "label": entry["label"]}
            )
        return out

    def save() -> None:
        # Every checkpoint carries the links still current, so a run stopped by its
        # budget never leaves readers with none.
        atomic_json(
            state_path, {"candidates": dict(sorted(entries.items())), "links": current_links()}
        )

    todo = [cid for cid in current if stale(cid)]
    pair_ids = [c for c in todo if current[c][0] == "pair"]
    batches: list[tuple[str, list[str]]] = []
    for i in range(0, len(pair_ids), BATCH):
        chunk = pair_ids[i : i + BATCH]
        batches.append((f"links/pairs-{digest(chunk)[:10]}", chunk))
    by_report: dict[str, list[str]] = {}
    for cid in todo:
        if current[cid][0] == "ref":
            by_report.setdefault(current[cid][1], []).append(cid)
    for sid, ids in sorted(by_report.items()):
        for i in range(0, len(ids), BATCH):
            chunk = ids[i : i + BATCH]
            batches.append((f"links/refs-{sid}-{digest(chunk)[:6]}", chunk))

    def ask(batch: tuple[str, list[str]]) -> dict[str, dict]:
        step, ids = batch
        mine = cards.runtime()  # a ledger connection belongs to the thread that opened it
        kind = current[ids[0]][0]
        local = {cid: f"{'P' if kind == 'pair' else 'R'}{n + 1}" for n, cid in enumerate(ids)}
        if kind == "pair":
            body = {local[c]: current[c][3] for c in ids}
            message = PAIR_PROMPT + json.dumps({"PAIRS": body}, ensure_ascii=False)
            relations: tuple[str, ...] = get_args(PairRelation)
            pools = {
                local[c]: " ".join(
                    " ".join(map(str, (x["claim"], x["quote"], x["quantities"])))
                    for x in current[c][3].values()
                    if isinstance(x, dict)
                )
                for c in ids
            }
        else:
            body = {
                "REPORT": current[ids[0]][3]["REPORT"],
                "NAMED": {
                    local[c]: {"project": current[c][3]["NAMED"], "lines": current[c][3]["LINES"]}
                    for c in ids
                },
            }
            message = REF_PROMPT + json.dumps(body, ensure_ascii=False)
            relations = get_args(RefRelation)
            pools = {local[c]: " ".join(current[c][3]["LINES"]) for c in ids}
        try:
            reply = cards.reviewed(
                [{"role": "user", "content": message}],
                step,
                checker(list(local.values()), relations, pools),
                agent=mine,
            )
        except CandidateError as exc:
            raise cards.failure(step, exc, mine) from exc
        answers = {item.id: item for item in reply.items}
        return {
            cid: {"relation": answers[n].relation, "label": answers[n].label.strip()}
            for cid, n in local.items()
        }

    # Links whose inputs changed stop being current before any job can stop the run.
    save()
    done = failed = 0
    for (step, ids), result in parallel(batches, ask, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(step, result)
            print(f"  [FAILED] {step}: {result}")
            for cid in ids:
                entries[cid] = {"input": keys[cid], "failed": True}
        else:
            for cid, answer in result.items():
                entries[cid] = {"input": keys[cid], **answer}
            record_failure(step, None)
            done += 1
        save()

    # A candidate that left the list keeps its answer for when it returns; one whose
    # results or projects are gone is pruned.
    for cid in list(entries):
        kind, _, ends = cid.partition(":")
        a, b = re.split(r"[|>]", ends, maxsplit=1)
        alive = (
            (a in findings and b in findings) if kind == "pair" else (a in titles and b in titles)
        )
        if not alive:
            entries.pop(cid)
    save()
    links = current_links()
    prune_failures("links/", {step for step, _ in batches})
    print(
        f"links: {len(links)} current from {len(current)} candidates; "
        f"{done} batches asked, {failed} failed"
    )
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
