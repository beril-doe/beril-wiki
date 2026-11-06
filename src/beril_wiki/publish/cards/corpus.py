"""What the publish-time joins read: the records, their labels and topic membership.

Corpus loads the finding and direction records, the stage state that joins them
(literature labels, plain summaries, links and shared results) and the topic and
citation data that place them. Nothing here writes a file.
"""

from __future__ import annotations

import json
import pathlib
import re

import yaml

from beril_wiki import records
from beril_wiki.records import DIGESTS, title_of
from beril_wiki.wording import is_reanalysis

DIRS = ("findings", "directions")
ISSUES = "data-issues"
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def split(text: str) -> tuple[dict, str]:
    m = FM.match(text)
    return ((yaml.safe_load(m.group(1)) or {}), text[m.end() :]) if m else ({}, text)


def join(fields: dict, body: str) -> str:
    return "---\n" + "".join(f"{k}: {json.dumps(v)}\n" for k, v in fields.items()) + "---\n" + body


class Corpus:
    """What the joins read: topic membership, citations, labels and the records."""

    def __init__(self, kb: pathlib.Path):
        self.kb = kb
        wiki = kb / "wiki"
        self.topic_concepts = records.topic_groups(kb)
        self.topic_titles = {
            records.slugify(g["title"]): g["title"] for g in records.curator_groups(kb)
        }
        self.concept_titles = {
            f"concepts/{p.stem}": title_of(p.read_text(encoding="utf-8", errors="replace"), p.stem)
            for p in (wiki / "concepts").glob("*.md")
        }
        self.concept_cites = records.concept_citations(kb)
        self.conflicts = {
            p.stem: (p.read_text(encoding="utf-8", errors="replace"))
            for p in sorted((wiki / "conflicts").glob("*.md"))
        }
        labels_path = kb / "state" / "novelty.json"
        self.labels = json.loads(labels_path.read_text()) if labels_path.exists() else {}
        gists_path = kb / "state" / "gists.json"
        # A failed rewrite keeps its old summary in state for recovery, but that text no
        # longer passes the current rules (or no longer matches the finding), so the
        # card shows the finding's own title instead.
        self.gists: dict[str, dict] = {
            fid: g
            for fid, g in (
                json.loads(gists_path.read_text()) if gists_path.exists() else {}
            ).items()
            if not g.get("failed")
        }
        links_path = kb / "state" / "links.json"
        self.link_records: list[dict] = (
            json.loads(links_path.read_text()).get("links", []) if links_path.exists() else []
        )
        shared_path = kb / "state" / "shared.json"
        self.shared_records: dict[str, dict] = (
            json.loads(shared_path.read_text()) if shared_path.exists() else {}
        )
        self._topics: dict[str, list[str]] = {}
        self._picks: tuple[list[str], dict[str, list[str]]] | None = None
        self.findings = {
            p.stem: split(p.read_text(encoding="utf-8"))
            for p in sorted((wiki / "findings").glob("*.md"))
        }
        self.directions = {
            p.stem: split(p.read_text(encoding="utf-8"))
            for p in sorted((wiki / "directions").glob("*.md"))
        }
        self.issues = data_issues(kb)

    def topics_of(self, sid: str) -> list[str]:
        if sid not in self._topics:
            self._topics[sid] = records.main_topics(sid, self.topic_concepts, self.concept_cites)
        return self._topics[sid]

    def citing(self, sid: str, topic: str) -> int:
        """How many of a topic's concepts cite a report."""
        return sum(sid in self.concept_cites.get(c, set()) for c in self.topic_concepts[topic])

    def display_topic(self, sid: str) -> str:
        """The main topic whose concepts cite the report most; ties go alphabetically.
        The first main topic alphabetically filed 56 results under one topic."""
        tops = self.topics_of(sid)
        return min(tops, key=lambda t: (-self.citing(sid, t), t)) if tops else ""

    def report_title(self, sid: str) -> str:
        # Some report titles carry Markdown emphasis; a card footer shows plain text.
        return re.sub(r"\*+", "", records.summary_title(self.kb, sid)).strip()

    def related_conflicts(self, sid: str, topics: list[str]) -> list[str]:
        concepts = (
            set().union(*(self.topic_concepts.get(t, set()) for t in topics)) if topics else set()
        )
        return [
            stem
            for stem, text in self.conflicts.items()
            if stem.split("--")[1] in concepts and sid in records.projects_in(text)
        ]

    def projects(self) -> set[str]:
        """Every project with a report, results or not."""
        return {
            p.name.removesuffix("__REPORT.md")
            for p in (self.kb / "wiki" / "sources").glob("*__REPORT.md")
        } - set(DIGESTS)

    def group_topics(self, sids: list[str]) -> list[str]:
        """The union of the projects' main topics, those more of them feed first."""
        count: dict[str, int] = {}
        for sid in sids:
            for t in self.topics_of(sid):
                count[t] = count.get(t, 0) + 1
        return sorted(count, key=lambda t: (-count[t], t))

    def cross_projects(self, did: str) -> dict[str, list[str]]:
        """Project -> the results it contributes, for a question citing two or more projects."""
        by: dict[str, list[str]] = {}
        for fid in self.directions[did][0].get("findings") or []:
            if fid in self.findings:
                by.setdefault(self.findings[fid][0].get("source", ""), []).append(fid)
        return by if len(by) >= 2 else {}

    def directions_on(self, fid: str) -> list[str]:
        return [
            d
            for d, (f, _) in self.directions.items()
            if f"findings/{fid}" in (f.get("builds_on") or [])
        ]


def data_issues(kb: pathlib.Path) -> dict[str, list[dict]]:
    """Report id -> the in-scope proposals that would redo or correct its work."""
    scope = records.load_scope(kb)
    if scope is None:
        return {}
    out: dict[str, list[dict]] = {}
    seen: set[tuple[str, str]] = set()
    for topic in scope.topics:
        for b in records.forward_bullets(kb, topic, scope.reports):
            if not is_reanalysis(b["text"]):
                continue
            for sid in b["projects"]:
                if sid in DIGESTS or (sid, b["text"]) in seen:
                    continue
                seen.add((sid, b["text"]))
                out.setdefault(sid, []).append(b)
    return dict(sorted(out.items()))


def finding_title(c: Corpus, fid: str) -> str:
    return c.gists.get(fid, {}).get("title") or title_of(c.findings[fid][1], fid)
