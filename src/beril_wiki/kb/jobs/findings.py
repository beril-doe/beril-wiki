"""Headline findings: at most six per report, each a page under ``wiki/findings``.

Owed when a report is ingested, and on a revision only when a stored headline rests on
a claim the revision withdrew. The checks, the page layout and the state record are the
curator's (``stages.headlines``). A headline whose claim was withdrawn does not stay
published while its replacement is pending: ``after`` removes its page.
"""

from __future__ import annotations

import datetime
from pathlib import Path

from beril_wiki.agentic.runtime import file_hash
from beril_wiki.kb.jobs import Job, Scope, evidence, forget_findings, legacy, write_state
from beril_wiki.kb.store import DIGESTS
from beril_wiki.records import caveat_quote, finding_text, source_path, source_title, title_of
from beril_wiki.stages import cards, headlines


def _said(out: Path, sid: str) -> dict[str, tuple]:
    """Finding id -> what its page says, as the stages that describe it read it."""
    said = {}
    for page in headlines.pages_of(out, sid):
        fields, body = cards.read_page(page)
        said[page.stem] = (finding_text(fields, body), title_of(body, ""), caveat_quote(body))
    return said


def jobs(scope: Scope) -> list[Job]:
    root, sid = scope.root, scope.source
    if sid in DIGESTS:
        return []
    records = evidence(scope.store, sid)
    # A headline restates one finding and the caveat that travels with it.
    kinds = {r["kind"] for r in records}
    if not kinds & {"finding", "null"} or "caveat" not in kinds:
        return []
    state_path = root / headlines.STATE
    saved = cards.load_state(state_path).get(sid, {})
    # An empty reply is what ``after`` leaves when every headline lost its claim.
    if (saved.get("reply") or {}).get("headlines") and not saved.get("failed"):
        live = {r["id"] for r in records}
        cited = {
            h[k]
            for h in saved["reply"].get("headlines", [])
            for k in ("evidence", "caveat_evidence")
        }
        # Accepted headlines stand until a claim under one of them is withdrawn.
        if cited <= live and scope.reason != "refresh":
            return []
    out = root / headlines.OUT

    def publish(record: dict) -> None:
        reply = headlines.Reply.model_validate(record)
        before = _said(out, sid)
        previous = {p.stem: cards.read_page(p)[0] for p in headlines.pages_of(out, sid)}
        today = datetime.date.today().isoformat()
        source_hash = file_hash(source_path(root, sid))
        names = set()
        for h in reply.headlines:
            quote = next(r for r in records if r["id"] == h.evidence)["quote"]
            first = previous.get(cards.finding_id(sid, quote), {}).get("first_added", today)
            fid, fields, body = headlines.render(sid, h, records, first, source_hash)
            cards.write_page(out / f"{fid}.md", fields, body)
            names.add(f"{fid}.md")
        for stale in headlines.pages_of(out, sid):
            if stale.name not in names:
                stale.unlink()
        state = cards.load_state(state_path)
        state[sid] = {
            "input": f"kb:{scope.run}",
            "render": headlines.RENDER,
            "reply": reply.model_dump(),
            "pages": {p.name: file_hash(p) for p in headlines.pages_of(out, sid)},
        }
        write_state(state_path, state)
        now = _said(out, sid)
        forget_findings(root, {fid for fid, said in before.items() if now.get(fid) != said})

    return [
        Job(
            stage="findings",
            key=f"findings/{sid}",
            pack=headlines.pack(sid, source_title(root, sid), records),
            check=legacy(headlines.checker(records)),
            publish=publish,
            reviewer="findings_review",
            schema=headlines.Reply.model_json_schema(),
        )
    ]


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """Remove the headlines a withdrawn claim leaves standing.

    That is every case in which no accepted reply replaced them: the revised report
    has no finding and caveat left to pair, or the replacement failed its checks or its
    review. The page would otherwise quote text its report no longer contains.
    """
    root, sid = scope.root, scope.source
    if not sid or sid in DIGESTS or any(o["status"] == "accepted" for o in outcomes.values()):
        return
    state_path = root / headlines.STATE
    state = cards.load_state(state_path)
    saved = state.get(sid, {})
    headlines_ = (saved.get("reply") or {}).get("headlines", [])
    quotes = {c["id"]: c["quote"] for c in scope.store.claims(sid)}
    live = {r["id"] for r in evidence(scope.store, sid)}
    kept, gone = [], set()
    for h in headlines_:
        cited = {h["evidence"], h["caveat_evidence"]}
        # Only a claim on record as withdrawn retires a headline; an id the claim
        # records never held says nothing about it.
        if cited <= live or not cited <= quotes.keys():
            kept.append(h)
        else:
            gone.add(cards.finding_id(sid, quotes[h["evidence"]]))
    if len(kept) == len(headlines_):
        return
    out = root / headlines.OUT
    for fid in gone:
        (out / f"{fid}.md").unlink(missing_ok=True)
    pages = {name: sha for name, sha in (saved.get("pages") or {}).items() if (out / name).exists()}
    state[sid] = saved | {"reply": saved["reply"] | {"headlines": kept}, "pages": pages}
    write_state(state_path, state)
    forget_findings(root, gone)
