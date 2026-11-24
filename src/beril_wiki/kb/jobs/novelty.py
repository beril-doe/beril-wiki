"""Literature labels: where each finding of the run's report sits against PubMed.

Owed for a finding with no label, or one marked failed or never assessed. A label is
not judged again because it aged or because a prompt or model changed; ``lint`` can
report old labels and ``refresh`` is how one is redone. The label rules, the checks on
a judgment and the stored entry are the curator's (``stages.novelty``).

Three steps, each seeing what the one before stored: a model proposes PubMed queries;
code retrieves the abstracts and a model labels the finding from them; and a label that
claims novelty or tension stands only when a model of the other vendor assigns it too.
"""

from __future__ import annotations

import json
import threading
from pathlib import Path

from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.store import write_text
from beril_wiki.records import FINDINGS, caveat_quote, finding_text, source_path
from beril_wiki.stages import cards, novelty

retrieve = novelty.retrieve


def _notes(scope: Scope, fid: str) -> Path:
    """Where one finding's queries and first judgment wait between steps. Scratch:
    it lets a stopped run resume without asking for them again."""
    return scope.root / ".agentic" / "novelty" / f"{fid}.json"


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _owed(scope: Scope) -> dict[str, dict]:
    state = cards.load_state(scope.root / novelty.STATE)
    out = {}
    for page in sorted((scope.root / FINDINGS).glob(f"{scope.source}--*.md")):
        saved = state.get(page.stem) or {}
        label = saved.get("pipeline_label", saved.get("label"))
        if label and label != novelty.NOT_ASSESSED and not saved.get("failed"):
            continue
        fields, body = cards.read_page(page)
        out[page.stem] = finding_text(fields, body) | {"caveat_quote": caveat_quote(body)}
    return out


# The labels of every report are one file. A compile reads several reports' findings
# side by side, and this stage also writes that file while it lists its jobs, outside
# the run's lock.
STATE_LOCK = threading.Lock()


def _save(scope: Scope, fid: str, entry: dict) -> None:
    path = scope.root / novelty.STATE
    decision = novelty.load_decisions(scope.root).get(fid)
    with STATE_LOCK:
        state = cards.load_state(path)
        state[fid] = novelty.apply_decision(entry, decision)
        write_state(path, dict(sorted(state.items())))


def _cited(scope: Scope) -> list[str]:
    path = source_path(scope.root, scope.source)
    return novelty.cited_pmids(path.read_text(encoding="utf-8", errors="replace"))


def _entry(scope: Scope, notes: dict, label: str, other: str | None) -> dict:
    """The stored label, as ``novelty.judge`` and ``novelty.main`` build it."""
    judged = notes.get("judged") or {}
    kept = bool(judged) and label == judged["label"]
    titles = notes.get("titles", {})
    return {
        "queries": notes["queries"],
        "retrieved": len(notes.get("candidates", [])),
        "candidates": notes.get("candidates", []),
        "retrieved_on": notes["retrieved_on"],
        "abstracts_only": True,
        "judge_model": scope.models.get("cards", ""),
        "agree_model": scope.models.get("findings_review") if other else None,
        "agreed": (other == judged.get("label")) if other else None,
        "label": label,
        "pipeline_label": label,
        **({"judged_label": judged["label"]} if judged else {}),
        # A downgraded label has no supporting relations: they argued for the label
        # the other model did not confirm.
        "difference": judged.get("difference", "").strip() if kept else "",
        "closest": (
            [c | {"title": titles.get(c["pmid"], "")} for c in judged.get("closest", [])]
            if kept
            else []
        ),
        "input": f"kb:{scope.run}",
        "cited_pmids": notes["cited"],
    }


def queries(scope: Scope) -> list[Job]:
    owed = []
    for fid, finding in _owed(scope).items():
        path = _notes(scope, fid)
        if _read(path).get("queries"):
            continue

        def publish(record: dict, path: Path = path) -> None:
            write_text(path, json.dumps({"queries": record["queries"]}))

        owed.append(
            Job(
                stage="novelty",
                key=f"novelty/{fid}/queries",
                pack={"FINDING": finding},
                check=legacy(lambda raw: cards.parse_reply(raw, novelty.Queries)),
                publish=publish,
                writer="queries",
                reviewer="",
                skill="wiki-novelty-queries",
                schema=novelty.Queries.model_json_schema(),
            )
        )
    return owed


def judgments(scope: Scope) -> list[Job]:
    owed: list[Job] = []
    waiting = _owed(scope)
    if not waiting:
        # Also the digests, which have no findings and no report mirror to read.
        return owed
    cited = _cited(scope)
    for fid, finding in waiting.items():
        path = _notes(scope, fid)
        notes = _read(path)
        if not notes.get("queries") or notes.get("judged"):
            continue
        try:
            papers, stamp = retrieve(scope.root / ".agentic", notes["queries"], cited)
        except Exception as exc:  # any PubMed fault belongs to this finding, not the run
            print(f"  novelty/{fid}: retrieval failed ({type(exc).__name__}: {exc}); label kept")
            state_path = scope.root / novelty.STATE
            with STATE_LOCK:
                state = cards.load_state(state_path)
                kept = state.get(fid) or {
                    "label": novelty.NOT_ASSESSED,
                    "pipeline_label": novelty.NOT_ASSESSED,
                }
                state[fid] = kept | {"failed": True}
                write_state(state_path, dict(sorted(state.items())))
            continue
        notes |= {
            "candidates": sorted(papers),
            "titles": {pid: text.split("\n", 1)[0] for pid, text in papers.items()},
            "retrieved_on": stamp,
            "cited": cited,
        }
        if not papers:
            # An empty search never earns a label from a model.
            _save(scope, fid, _entry(scope, notes, novelty.INSUFFICIENT, None))
            path.unlink(missing_ok=True)
            continue
        write_text(path, json.dumps(notes))
        pack = {
            "FINDING": finding,
            "CANDIDATE PAPERS": {
                pid: text[: novelty.ABSTRACT_CHARS] for pid, text in papers.items()
            },
        }

        def publish(record: dict, fid: str = fid, path: Path = path, pack: dict = pack) -> None:
            now = _read(path) | {"judged": record, "pack": pack}
            if record["label"] in novelty.GUARDED:
                write_text(path, json.dumps(now))
                return
            _save(scope, fid, _entry(scope, now, record["label"], None))
            path.unlink(missing_ok=True)

        owed.append(
            Job(
                stage="novelty",
                key=f"novelty/{fid}/judge",
                pack=pack,
                check=legacy(novelty.judgment_checker(papers)),
                publish=publish,
                writer="cards",
                reviewer="",
                skill="wiki-novelty",
                schema=novelty.Judgment.model_json_schema(),
            )
        )
    return owed


def agreements(scope: Scope) -> list[Job]:
    owed = []
    for fid in _owed(scope):
        path = _notes(scope, fid)
        notes = _read(path)
        judged = notes.get("judged")
        if not judged or judged["label"] not in novelty.GUARDED:
            continue

        def publish(record: dict, fid: str = fid, path: Path = path) -> None:
            now = _read(path)
            first = now["judged"]["label"]
            other = record["label"]
            label = first if other == first else novelty.weaker(other)
            _save(scope, fid, _entry(scope, now, label, other))
            path.unlink(missing_ok=True)

        owed.append(
            Job(
                stage="novelty",
                key=f"novelty/{fid}/agree",
                pack=notes["pack"] | {"PROPOSED": judged},
                check=legacy(lambda raw: cards.parse_reply(raw, novelty.Agreement)),
                publish=publish,
                writer="findings_review",
                reviewer="",
                skill="wiki-novelty-agree",
                schema=novelty.Agreement.model_json_schema(),
            )
        )
    return owed


PHASES = (queries, judgments, agreements)
jobs = queries


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """Drop the labels of findings that no longer exist, as the curator does; the
    strict check rejects a label with no finding."""
    path = scope.root / novelty.STATE
    with STATE_LOCK:
        state = cards.load_state(path)
        live = {page.stem for page in (scope.root / FINDINGS).glob("*.md")}
        if state.keys() - live:
            write_state(path, {f: entry for f, entry in sorted(state.items()) if f in live})
