"""Research directions for the topic the run's report most directly feeds."""

from __future__ import annotations

from beril_wiki import lakehouse, records
from beril_wiki.agentic.runtime import file_hash
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.tools import Rejected
from beril_wiki.stages import cards, directions


def jobs(scope: Scope) -> list[Job]:
    """Return the one direction job owed by this report, if any."""
    root, source = scope.root, scope.source
    groups = records.topic_groups(root)
    citations = records.concept_citations(root)
    topics = records.main_topics(source, groups, citations)
    if not topics:
        return []
    cited = {concept for concept, sources in citations.items() if source in sources}
    topic = min(topics, key=lambda t: (-len(groups[t] & cited), t))
    state_path = root / directions.STATE
    state = cards.load_state(state_path)
    # A direction whose finding or conflict page is gone was retired by ``after``
    # of an earlier run, or will be by this one; it is not offered to the writer.
    accepted = [
        d
        for d in (state.get(topic, {}).get("reply") or {}).get("directions", [])
        if all(
            (root / "wiki" / kind / f"{ref}.md").exists()
            for kind in ("findings", "conflicts")
            for ref in d.get(kind, [])
        )
    ]
    if accepted and scope.reason != "ingest":
        return []

    config = records.load_scope(root)
    cat = lakehouse.load(root)
    pack = directions.topic_pack(root, topic, config.reports if config else [source], cat)
    if not pack["FINDINGS"] and not pack["CONFLICTS"]:
        return []
    pack["OTHER_TOPICS"] = directions.other_topics(
        state, topic, config.topics if config else list(groups)
    )
    public = {key: value for key, value in pack.items() if not key.startswith("_")}
    public.update(SOURCE=source, ACCEPTED=accepted)
    if accepted:
        # Stated in the input so the reviewer reads the same rule the code enforces.
        public["RULES"] = (
            "Return every ACCEPTED direction unchanged. At most two new directions may "
            f"be added, and each must build on at least one finding of {source}."
        )

    gate = legacy(directions.checker(pack, cat))
    basis = pack["_findings"].keys() | pack["_conflicts"].keys()
    keep = {d["id"]: d for d in accepted if directions.builds_on(d) <= basis}
    source_findings = {f["id"] for f in pack["FINDINGS"] if f["report"] == source}

    def check(record: dict) -> dict:
        checked = gate(record)
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

    return [
        Job(
            stage="directions",
            key=f"directions/{topic}",
            pack=public,
            check=check,
            publish=publish,
            writer="cards",
            reviewer="card_review",
            schema=directions.Reply.model_json_schema(),
        )
    ]


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
