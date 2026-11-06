"""Done checks for the links and shared stages (spec 2026-11-05-cross-project-design.md).

    uv run python scripts/check_links.py --reference PATH/links-audit.json
    uv run python scripts/check_links.py --shared

`--reference` compares the links stage with a hand audit of the same candidates: the
same-question pairs publish reads from the question records, how many audited
candidates the stage saw, and how often both kept or both dropped a candidate.
`--shared` re-runs the stages' code checks on every accepted shared result and link
label. Exit 0 when the check passes, 1 with one line per failure otherwise.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from beril_wiki.publish.cards import Corpus, links_index
from beril_wiki.stages import cards, links, shared
from beril_wiki.wording import LINK_BANNED, STAT_WORDS, STATS

ROOT = Path(__file__).resolve().parent.parent
SEEN = 0.90
AGREE = 0.85


def reference(path: Path) -> list[str]:
    audit = json.loads(path.read_text(encoding="utf-8"))
    state = json.loads((ROOT / links.STATE).read_text(encoding="utf-8"))["candidates"]
    failures = []
    reference_links = path.with_name("links.json")
    if reference_links.exists():
        want = {
            frozenset((x["a"], x["b"]))
            for x in json.loads(reference_links.read_text(encoding="utf-8"))
            if x["type"] == "shared-question"
        }
        got = {frozenset((x["a"], x["b"])) for x in links_index(Corpus(ROOT)) if x["family"] == "q"}
        print(f"same-question pairs: {len(got)} published, {len(want)} in the reference")
        if got != want:
            failures.append(f"same-question pairs differ: {len(got ^ want)} not in both")
    audited = {f"pair:{min(x['a'], x['b'])}|{max(x['a'], x['b'])}": x for x in audit["lexical"]}
    audited |= {f"ref:{x['a']}>{x['b']}": x for x in audit["project_references"]}
    seen = [cid for cid in audited if cid in state]
    answered = [cid for cid in seen if not state[cid].get("failed")]
    agree = sum(
        (state[cid]["relation"] in links.DROPPED) == (audited[cid]["type"] == "reject")
        for cid in answered
    )
    by_type: dict[str, int] = {}
    for x in state.values():
        if not x.get("failed"):
            by_type[x["relation"]] = by_type.get(x["relation"], 0) + 1
    print(f"stage relations: {json.dumps(by_type, sort_keys=True)}")
    print(
        f"audited candidates: {len(audited)}; seen by the stage {len(seen)}; answered "
        f"{len(answered)}; kept-or-dropped agreement {agree}/{len(answered)}"
    )
    if len(seen) < SEEN * len(audited):
        failures.append(f"the stage saw {len(seen)} of {len(audited)} audited candidates")
    if not answered or agree < AGREE * len(answered):
        failures.append(f"kept-or-dropped agreement {agree}/{len(answered)} is under {AGREE:.0%}")
    return failures


def shared_texts() -> list[str]:
    failures = []
    groups = json.loads((ROOT / shared.STATE).read_text(encoding="utf-8"))
    findings = links.read_findings(ROOT)
    accepted = [g for g in groups.values() if not g.get("failed")]
    print(f"shared results: {len(accepted)} accepted")
    if len(accepted) < 3:
        failures.append(f"only {len(accepted)} shared results accepted; 3 needed")
    for g in accepted:
        name = g["title"]
        if len(g["projects"]) < 2 or len(g["topics"]) < 2:
            failures.append(f"{name}: {len(g['projects'])} projects, {len(g['topics'])} topics")
        members = {f: findings[f] for f in g["members"] if f in findings}
        if len(members) != len(g["members"]):
            failures.append(f"{name}: a member result no longer exists")
            continue
        reply = {k: g[k] for k in ("title", "sentence", "question", "lanes", "how")}
        try:
            shared.checker(members)(json.dumps(reply))
        except cards.CandidateError as exc:
            failures.append(f"{name}: {exc}")
    for x in json.loads((ROOT / links.STATE).read_text(encoding="utf-8"))["links"]:
        label = x["label"]
        if LINK_BANNED.search(label) or STATS.search(label) or STAT_WORDS.search(label):
            failures.append(f"link label {x['a']} {x['b']}: {label}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--reference", type=Path, help="hand audit of the link candidates")
    parser.add_argument("--shared", action="store_true", help="re-check accepted shared texts")
    args = parser.parse_args()
    failures: list[str] = []
    if args.reference:
        failures += reference(args.reference)
    if args.shared:
        failures += shared_texts()
    if not (args.reference or args.shared):
        parser.error("give --reference PATH or --shared")
    for line in failures:
        print(f"FAIL {line}")
    print("PASS" if not failures else f"{len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
