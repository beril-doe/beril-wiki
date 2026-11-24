"""Research directions for one report's main topic or for the whole corpus."""

from __future__ import annotations

import json
from collections.abc import Iterable
from typing import TypeVar

from beril_wiki import lakehouse, records
from beril_wiki.agentic.runtime import file_hash
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.tools import Rejected
from beril_wiki.stages import cards, directions, novelty

MAX_COMPILE_DIRECTIONS = 5
# In a compile each topic's proposals are checked against the directions every topic
# before it stored, so the topics run one at a time.
SERIAL = True
PACK_CHARS = 120_000
T = TypeVar("T")


def _under_budget(rows: Iterable[T], budget: int) -> list[T]:
    kept = []
    for row in rows:
        size = len(json.dumps(row, ensure_ascii=False)) + 2
        if size <= budget:
            kept.append(row)
            budget -= size
    return kept


def table_context(rows: list[dict], budget: int) -> dict:
    """Summarize matched schemas without sample values or unmatched catalog rows."""
    compact = (
        {
            "table": row["table"],
            "columns": row["columns"][:12],
            "columns_truncated": row["columns_truncated"] or len(row["columns"]) > 12,
        }
        for row in rows
    )
    shown = _under_budget(compact, budget)
    return {
        "DATABASES": sorted({str(row["table"]).rpartition(".")[0] for row in shown}),
        "TABLES": shown,
    }


def _compile_pack(pack: dict) -> None:
    """Keep complete evidence rows for the writer and the gate within the same budget."""
    # Spend the catalog budget on matched schemas before taking rows from the evidence.
    pack.update(table_context(pack["TABLES"], 10_000))
    pack["PROPOSALS"] = _under_budget(pack["PROPOSALS"], 12_000)
    by_report: dict[str, int] = {}

    def order(finding: dict) -> tuple[bool, int, str]:
        count = by_report.get(finding["report"], 0)
        by_report[finding["report"]] = count + 1
        preferred = finding["label"] in (novelty.NOVEL, novelty.TENSION)
        return not preferred, count, finding["id"]

    pack["FINDINGS"] = _under_budget(sorted(pack["FINDINGS"], key=order), 58_000)
    pack["_findings"] = {f["id"]: f for f in pack["FINDINGS"]}
    pack["CONFLICTS"] = _under_budget(pack["CONFLICTS"], 19_000)
    pack["_conflicts"] = {c["slug"]: pack["_conflicts"][c["slug"]] for c in pack["CONFLICTS"]}
    pmids = {pmid for f in pack["FINDINGS"] for pmid in f["closest"]}
    pack["PAPERS"] = _under_budget((p for p in pack["PAPERS"] if p["pmid"] in pmids), 13_000)
    shown = {p["pmid"] for p in pack["PAPERS"]}
    for finding in pack["FINDINGS"]:
        finding["closest"] = [p for p in finding["closest"] if p in shown]
    pack["OTHER_TOPICS"] = _under_budget(pack["OTHER_TOPICS"], 5_000)


def jobs(scope: Scope) -> list[Job]:
    """Return the topics that owe a direction proposal."""
    root, source = scope.root, scope.source
    groups = records.topic_groups(root)
    corpus = scope.reason == "compile" and not source
    if corpus:
        topics = sorted(groups)
    else:
        citations = records.concept_citations(root)
        touched = records.main_topics(source, groups, citations)
        cited = {concept for concept, sources in citations.items() if source in sources}
        topics = [min(touched, key=lambda t: (-len(groups[t] & cited), t))] if touched else []
    if not topics:
        return []
    state = cards.load_state(root / directions.STATE)
    config = None if corpus else records.load_scope(root)
    reports = scope.sources if corpus else (config.reports if config else [source])
    comparison_topics = config.topics if config else list(groups)
    cat = lakehouse.load(root)
    return [
        job
        for topic in topics
        if (job := _topic_job(scope, topic, reports, comparison_topics, state, cat, corpus))
    ]


def _topic_job(
    scope: Scope,
    topic: str,
    reports: list[str],
    topics: list[str],
    state: dict,
    cat: lakehouse.Catalog,
    corpus: bool,
) -> Job | None:
    root, source = scope.root, scope.source
    state_path = root / directions.STATE
    saved = state.get(topic, {})
    saved_reply = saved.get("reply") or {}
    saved_pages = saved.get("pages") or {}
    if (
        corpus
        and not saved.get("failed")
        and "directions" in saved_reply
        and len(saved_pages) == len(saved_reply["directions"])
        and all((root / directions.OUT / name).is_file() for name in saved_pages)
    ):
        return None
    # A direction whose finding or conflict page is gone was retired by ``after``
    # of an earlier run, or will be by this one; it is not offered to the writer.
    accepted = [
        d
        for d in saved_reply.get("directions", [])
        if all(
            (root / "wiki" / kind / f"{ref}.md").exists()
            for kind in ("findings", "conflicts")
            for ref in d.get(kind, [])
        )
    ]
    if accepted and not corpus and scope.reason != "ingest":
        return None

    pack = directions.topic_pack(root, topic, reports, cat)
    if not pack["FINDINGS"] and (corpus or not pack["CONFLICTS"]):
        return None
    pack["OTHER_TOPICS"] = directions.other_topics(state, topic, topics)
    for finding in pack["FINDINGS"]:
        _, body = cards.read_page(root / records.FINDINGS / f"{finding['id']}.md")
        finding["quote"] = records.finding_text({}, body)["quote"]
        finding["caveat_quote"] = records.caveat_quote(body)
    if corpus:
        _compile_pack(pack)
    public = {key: value for key, value in pack.items() if not key.startswith("_")}
    if corpus:
        public.update(TOPIC=topic, MAX_NEW=MAX_COMPILE_DIRECTIONS)
        assert len(json.dumps(public, ensure_ascii=False)) <= PACK_CHARS
    else:
        public.update(SOURCE=source, ACCEPTED=accepted)
    if accepted and not corpus:
        # Stated in the input so the reviewer reads the same rule the code enforces.
        public["RULES"] = (
            "Return every ACCEPTED direction unchanged. At most two new directions may "
            f"be added, and each must build on at least one finding of {source}."
        )

    gate = legacy(directions.checker(pack, cat, counted=not corpus))
    basis = pack["_findings"].keys() | pack["_conflicts"].keys()
    keep = {d["id"]: d for d in accepted if directions.builds_on(d) <= basis}
    source_findings = {f["id"] for f in pack["FINDINGS"] if f["report"] == source}

    def check(record: dict) -> dict:
        checked = gate(record)
        if corpus:
            if len(checked["directions"]) > MAX_COMPILE_DIRECTIONS:
                raise Rejected(f"give at most {MAX_COMPILE_DIRECTIONS} directions")
            return checked
        if not accepted:
            return checked
        submitted = {d["id"]: d for d in checked["directions"]}
        problems = [
            f"{id_}: return the accepted direction unchanged while its findings and conflicts stand"
            for id_, direction in keep.items()
            if submitted.get(id_) != direction
        ]
        new = [d for id_, d in submitted.items() if id_ not in keep]
        if len(new) > 2:
            problems.append("add at most two new directions")
        problems.extend(
            f"{d['id']}: a new direction must build on at least one finding of {source}"
            for d in new
            if not source_findings.intersection(d["findings"])
        )
        if problems:
            raise Rejected(
                "the record changes accepted directions or adds unsupported work", problems
            )
        return checked

    def publish(record: dict) -> None:
        reply = directions.Reply.model_validate(record)
        out = root / directions.OUT
        owned = {
            page
            for page in directions.pages_for(out, topic)
            if set(cards.read_page(page)[0].get("topics", [])) == {topic}
        }
        occupied = set(out.glob("*.md")) - owned
        pages = set()
        for direction in reply.directions:
            name, fields, body = directions.render(topic, direction, pack, cat)
            page = out / f"{name}.md"
            if page in occupied:
                stem = f"{name}-{topic[:24].rstrip('-')}"
                page = out / f"{stem}.md"
                suffix = 2
                while page in occupied:
                    page = out / f"{stem}-{suffix}.md"
                    suffix += 1
            cards.write_page(page, fields, body)
            occupied.add(page)
            pages.add(page)
        for stale in sorted(owned - pages):
            stale.unlink()
        current = cards.load_state(state_path)
        current[topic] = {
            "input": f"kb:{scope.run}",
            "render": directions.RENDER,
            "reply": reply.model_dump(),
            "pages": {page.name: file_hash(page) for page in sorted(pages)},
        }
        write_state(state_path, current)

    return Job(
        stage="directions",
        key=f"directions/{topic}",
        pack=public,
        check=check,
        publish=publish,
        writer="cards",
        reviewer="card_review",
        schema=directions.Reply.model_json_schema(),
    )


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """Retire every direction that builds on a finding or conflict this run removed,
    in any topic, whether or not a replacement was accepted (``retire_broken`` is the
    curator's rule). The strict check rejects such a page."""
    root = scope.root
    out = root / directions.OUT
    state_path = root / directions.STATE
    state = cards.load_state(state_path)
    changed = False
    for topic, saved in state.items():
        names = saved.get("pages") if isinstance(saved, dict) else None
        if not names:
            continue
        directions.retire_broken(root, out, topic)
        kept = {name: sha for name, sha in names.items() if (out / name).exists()}
        if kept != names:
            saved["pages"] = kept
            changed = True
    if changed:
        write_state(state_path, state)
