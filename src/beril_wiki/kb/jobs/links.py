"""Related findings and project references for the report this run touches."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, get_args

from beril_wiki.agentic.runtime import digest
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.jobs.conflicts import tension_groups
from beril_wiki.stages import cards, links


@dataclass(frozen=True)
class _Candidate:
    kind: Literal["pair", "ref"]
    a: str
    b: str
    pack: dict

    @property
    def key(self) -> str:
        return f"pair:{self.a}|{self.b}" if self.kind == "pair" else f"ref:{self.a}>{self.b}"

    @property
    def reports(self) -> tuple[str, str]:
        if self.kind == "pair":
            return self.pack["A"]["report"], self.pack["B"]["report"]
        return self.a, self.b


def _candidates(root: Path, corpus: bool = False) -> list[_Candidate]:
    findings = links.read_findings(root)
    titles = links.report_titles(root)
    memberships = links.memberships(root)
    if corpus:
        # The conflict stage runs later, but its pages can cite these projects together.
        groups, _ = tension_groups(root)
        memberships.extend(set().union(*(block["projects"] for block in g)) for g in groups)
    pairs = [
        _Candidate(
            "pair", a, b, {"A": links.pair_text(findings[a]), "B": links.pair_text(findings[b])}
        )
        for a, b in links.pair_candidates(findings, memberships)
    ]
    refs = [
        _Candidate(
            "ref", sid, target, {"REPORT": titles[sid], "NAMED": titles[target], "LINES": lines}
        )
        for (sid, target), lines in sorted(links.reference_candidates(root, titles).items())
    ]
    return pairs + refs


def _basis(candidate: _Candidate) -> str:
    """The sentences a project reference was judged from. A pair is judged from two
    findings, and a finding that changes takes its answers with it (``forget_findings``)."""
    return digest(candidate.pack["LINES"])[:12] if candidate.kind == "ref" else ""


def _answered(entry: dict, candidate: _Candidate | None = None) -> bool:
    if not entry.get("relation") or entry.get("failed"):
        return False
    # An answer imported from the curator carries no lines; it stands.
    return candidate is None or entry.get("lines", _basis(candidate)) == _basis(candidate)


def _current_links(current: list[_Candidate], entries: dict) -> list[dict]:
    result = []
    for candidate in current:
        entry = entries.get(candidate.key, {})
        if _answered(entry, candidate) and entry["relation"] not in links.DROPPED:
            result.append(
                {
                    "a": candidate.a,
                    "b": candidate.b,
                    "level": "finding" if candidate.kind == "pair" else "project",
                    "type": entry["relation"],
                    "label": entry["label"],
                }
            )
    return result


def _batch(scope: Scope, current: list[_Candidate], chunk: list[_Candidate]) -> Job:
    path = scope.root / links.STATE
    first = chunk[0]
    prefix = "P" if first.kind == "pair" else "R"
    local = {f"{prefix}{i}": candidate for i, candidate in enumerate(chunk, 1)}
    keys = [candidate.key for candidate in chunk]
    if first.kind == "pair":
        key = f"links/pairs-{digest(keys)[:10]}"
        pack = {"PAIRS": {name: candidate.pack for name, candidate in local.items()}}
        relations = get_args(links.PairRelation)
        pools = {
            name: " ".join(
                " ".join(map(str, (result["claim"], result["quote"], result["quantities"])))
                for result in candidate.pack.values()
            )
            for name, candidate in local.items()
        }
    else:
        key = f"links/refs-{first.a}-{digest(keys)[:6]}"
        pack = {
            "REPORT": first.pack["REPORT"],
            "NAMED": {
                name: {"project": candidate.pack["NAMED"], "lines": candidate.pack["LINES"]}
                for name, candidate in local.items()
            },
        }
        relations = get_args(links.RefRelation)
        pools = {name: " ".join(candidate.pack["LINES"]) for name, candidate in local.items()}

    def publish(record: dict) -> None:
        state = cards.load_state(path)
        entries = state.setdefault("candidates", {})
        for item in record["items"]:
            candidate = local[item["id"]]
            entries[candidate.key] = {
                "input": f"kb:{scope.run}",
                "relation": item["relation"],
                "label": item["label"].strip(),
                **({"lines": _basis(candidate)} if candidate.kind == "ref" else {}),
            }
        state["links"] = _current_links(current, entries)
        write_state(path, state)

    return Job(
        stage="links",
        key=key,
        pack=pack,
        check=legacy(links.checker(list(local), relations, pools)),
        publish=publish,
        schema=links.Reply.model_json_schema(),
    )


def jobs(scope: Scope) -> list[Job]:
    """Batch unanswered candidates for this report or the whole corpus."""
    corpus = scope.reason == "compile" and not scope.source
    current = _candidates(scope.root, corpus)
    entries = cards.load_state(scope.root / links.STATE).get("candidates", {})
    pairs = []
    refs: dict[str, list[_Candidate]] = {}
    for candidate in current:
        entry = entries.get(candidate.key, {})
        if _answered(entry, candidate) or (not corpus and scope.source not in candidate.reports):
            continue
        if candidate.kind == "pair":
            pairs.append(candidate)
        else:
            refs.setdefault(candidate.a, []).append(candidate)
    return [
        _batch(scope, current, batch[i : i + links.BATCH])
        for batch in [pairs, *refs.values()]
        for i in range(0, len(batch), links.BATCH)
    ]


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """Publish the derived links when no accepted batch has published them."""
    path = scope.root / links.STATE
    if not path.exists() or any(o["status"] == "accepted" for o in outcomes.values()):
        return
    state = cards.load_state(path)
    current = _current_links(
        _candidates(scope.root, scope.reason == "compile" and not scope.source),
        state.get("candidates", {}),
    )
    if state.get("links") != current:
        write_state(path, state | {"links": current})
