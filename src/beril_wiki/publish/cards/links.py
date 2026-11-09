"""Links between results and projects, and the shared results they support."""

from __future__ import annotations

from beril_wiki import records
from beril_wiki.publish.cards.corpus import Corpus, eligible, finding_title
from beril_wiki.publish.cards.text import RELATION_TEXT, chip_note, chip_of
from beril_wiki.records import title_of


def links_index(c: Corpus) -> list[dict]:
    """Every current link a reader can follow, with both ends present.

    Families: r, related results; q, cited by the same open question (read from the
    question records, so the ringed questions and these links always agree); p, one
    project's report uses or cites another's."""
    out: list[dict] = []
    projects = c.projects()
    for x in c.link_records:
        a, b = x.get("a", ""), x.get("b", "")
        if x.get("level") == "project":
            # A report that only lists another among its references does nothing with it.
            if x.get("type") == "lists it as a reference only":
                continue
            if a in projects and b in projects:
                out.append({"pa": a, "pb": b, "family": "p", "label": x.get("label", "")})
        elif a in c.findings and b in c.findings:
            out.append(
                {"a": a, "b": b, "family": "r", "label": x.get("label", "")}
                | {
                    "pa": c.findings[a][0].get("source", ""),
                    "pb": c.findings[b][0].get("source", ""),
                }
            )
    pairs: dict[tuple[str, str], list[str]] = {}
    for did in c.directions:
        by = c.cross_projects(did)
        members = sorted((fid, sid) for sid, fids in by.items() for fid in fids)
        for i, (fa, sa) in enumerate(members):
            for fb, sb in members[i + 1 :]:
                if sa != sb:
                    pairs.setdefault((fa, fb), []).append(title_of(c.directions[did][1], did))
    for (a, b), questions in sorted(pairs.items()):
        out.append(
            {"a": a, "b": b, "family": "q", "questions": questions}
            | {"pa": c.findings[a][0].get("source", ""), "pb": c.findings[b][0].get("source", "")}
        )
    return out


def related_components(c: Corpus) -> set[frozenset[str]]:
    """The result groups the current related-result links join, as the shared stage forms them."""
    edges = [
        (x["a"], x["b"])
        for x in c.link_records
        if x.get("level") == "finding"
        and x.get("type") in RELATION_TEXT
        and x.get("a", "") in c.findings
        and x.get("b", "") in c.findings
    ]
    return {frozenset(g) for g in records.components(edges)}


def relation_of(c: Corpus, members: list[str]) -> str:
    """How the current links relate a group's results: the weakest relation among
    them, as the shared stage sets it (RELATION_TEXT lists the relations strongest
    first)."""
    order = list(RELATION_TEXT)
    inner = [
        x["type"]
        for x in c.link_records
        if x.get("level") == "finding"
        and x.get("type") in RELATION_TEXT
        and x.get("a") in members
        and x.get("b") in members
    ]
    return max(inner, key=order.index) if inner else ""


def related_results(c: Corpus, fid: str) -> list[tuple[str, str]]:
    """Listed results in other projects that a current related-result link joins to this
    one, each with the relation's reader words, by project title, then result title.

    Unlisted results keep their pages but are hidden from readers, so they are left out."""
    sid = c.findings[fid][0].get("source", "")
    others = {
        x["b"] if x.get("a") == fid else x["a"]
        for x in c.link_records
        if x.get("level") == "finding"
        and x.get("type") in RELATION_TEXT
        and fid in (x.get("a"), x.get("b"))
        and x.get("a") != x.get("b")
    }
    keep = [
        o
        for o in others
        if o in c.findings and c.findings[o][0].get("source", "") != sid and eligible(c, o)
    ]
    keep.sort(
        key=lambda o: (c.report_title(c.findings[o][0].get("source", "")), finding_title(c, o), o)
    )
    return [(o, RELATION_TEXT[relation_of(c, [fid, o])]) for o in keep]


def shared_index(c: Corpus) -> list[dict]:
    """Accepted shared results whose members are all listed and still form one group of
    current related-result links, those spanning the most topics first. A links refresh
    that drops a link retires the statement at once, before the shared stage runs again."""
    groups = []
    current = related_components(c)
    for gid, g in sorted(c.shared_records.items()):
        members = g.get("members") or []
        if g.get("failed") or not members or any(m not in c.findings for m in members):
            continue
        # The statement speaks for every member, so one the Results page hides retires it.
        if not all(eligible(c, m) for m in members):
            continue
        if frozenset(members) not in current:
            continue
        # Text written for how the results related before a links refresh waits for the
        # shared stage to rewrite it.
        if relation_of(c, members) != g.get("relation"):
            continue
        sids = sorted({c.findings[m][0].get("source", "") for m in members})
        topics = c.group_topics(sids)
        if len(sids) < 2 or len(topics) < 2:
            continue
        groups.append(
            {
                "id": gid,
                "title": g["title"],
                "sentence": g["sentence"],
                "question": g["question"],
                "how": g["how"],
                "relation": RELATION_TEXT.get(g.get("relation", ""), ""),
                "projects": [c.report_title(sid) for sid in sids],
                "sources": sids,
                "topics": topics,
                "members": [
                    {
                        "id": m,
                        "title": finding_title(c, m),
                        "gist": c.gists.get(m, {}).get("gist", ""),
                        "lane": (g.get("lanes") or {}).get(m, ""),
                        "source": c.findings[m][0].get("source", ""),
                        "report_title": c.report_title(c.findings[m][0].get("source", "")),
                        "chip": chip_of(c.labels.get(m), c.findings[m][0].get("result", "")),
                        "chip_note": chip_note(c.labels.get(m), c.findings[m][0].get("result", "")),
                    }
                    for m in members
                ],
            }
        )
    groups.sort(key=lambda g: (-len(g["topics"]), -len(g["sources"]), g["id"]))
    return groups
