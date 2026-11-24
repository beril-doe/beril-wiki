"""Plain summaries: one or two sentences per finding, in ``state/gists.json``.

Owed for each finding of the run's report that has no accepted summary. The wording
checks are the curator's (``stages.gists``).
"""

from __future__ import annotations

from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.records import (
    FINDINGS,
    caveat_quote,
    finding_text,
    report_caveats,
    summary_title,
    title_of,
)
from beril_wiki.stages import cards, gists


def findings_of(scope: Scope) -> dict[str, tuple[dict, str, list[str]]]:
    """Finding id -> (the finding as the gist prompt reads it, its title, the report's
    other caveats), for the run's report."""
    out = {}
    for page in sorted((scope.root / FINDINGS).glob(f"{scope.source}--*.md")):
        fields, body = cards.read_page(page)
        finding = finding_text(fields, body) | {"caveat_quote": caveat_quote(body)}
        out[page.stem] = (finding, title_of(body, ""), report_caveats(body))
    return out


def jobs(scope: Scope) -> list[Job]:
    root = scope.root
    state_path = root / gists.STATE
    state = cards.load_state(state_path)
    findings = findings_of(scope)
    report = summary_title(root, scope.source)
    owed = []
    for fid, (finding, heading, caveats) in findings.items():
        saved = state.get(fid) or {}
        if saved.get("gist") and not saved.get("failed"):
            continue
        siblings = sorted(f for f in findings if f != fid)
        earlier = [f for f in siblings if f < fid]
        pack = {
            "FINDING": finding | {"title": heading, "report_title": report},
            "TITLE_NEEDS_PLAIN": not gists.plain_title(heading),
            "REPORT_CAVEATS": caveats,
            "SIBLINGS": [
                {"id": f, "title": findings[f][1], "claim": findings[f][0]["claim"]}
                for f in siblings
            ],
            "EARLIER": earlier,
        }

        def publish(record: dict, fid: str = fid) -> None:
            current = cards.load_state(state_path)
            current[fid] = {
                "input": f"kb:{scope.run}",
                **{k: record.get(k, "") for k in ("gist", "case", "title", "repeats")},
                "model": scope.models.get("cards", ""),
            }
            write_state(state_path, dict(sorted(current.items())))

        owed.append(
            Job(
                stage="gists",
                key=f"gists/{fid}",
                pack=pack,
                check=legacy(gists.checker(finding, heading, earlier)),
                publish=publish,
                schema=gists.Gist.model_json_schema(),
            )
        )
    return owed
