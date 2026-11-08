"""Publish-time joins for finding and research-direction records.

The curator stages write each record alone; this step places them. It adds the
literature label from state/novelty.json, the topics a finding belongs to, the
conflicts and research directions related to it, and two texts a reader copies from
each direction: a prompt for BERIL and a handoff brief. It also writes a JSON export
for agents. Everything here is a deterministic join over pages the pipeline wrote,
so placement never costs a model call and never edits pages under wiki/.

Reanalysis proposals, which repeat or correct existing work, are listed per report
under data-issues/ for the reports' maintainers rather than as research.

ingest.py calls record() on each record page before its generic transforms (title,
[src:] links, dead-link repair) run.
"""

from __future__ import annotations

import json
import pathlib
import re

import yaml

DIRS = ("findings", "directions")
ISSUES = "data-issues"
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
SRC_TAG = re.compile(r"\[src:\s*([^\]]+)\]")
NOT_ASSESSED = "Not assessed"
PUBMED = "https://pubmed.ncbi.nlm.nih.gov/{}/"
# The guarded labels name the agreement that let them stand.
GUARDED = ("Candidate novel", "In tension with retrieved work")

# Reader-facing words for pipeline terms; record files keep the pipeline's own.
KIND_TEXT = {
    "observation": "Result",
    "inference": "Interpretation",
    "null result": "Null or missing result",
    "correction": "Correction",
}
# A listed null result is named by what its summary found; other nulls keep KIND_TEXT's.
NULL_CASE_TEXT = {
    "measured absence": "No effect found",
    "inconclusive test": "Inconclusive test",
}
CHIP = {
    "Candidate novel": "Novel",
    "Extends retrieved work": "Builds on PubMed work",
    "In tension with retrieved work": "Differs from PubMed abstracts",
    "Established in retrieved literature": "Similar result in PubMed",
}
LABEL_TEXT = CHIP | {"Insufficient literature evidence": "Too little published evidence to compare"}
# Home order: results PubMed abstracts hold least like them first.
INTEREST = [CHIP[k] for k in ("Candidate novel", "In tension with retrieved work")] + [
    CHIP["Extends retrieved work"]
]
CHIP_NOTE = (
    "An AI comparison with PubMed abstracts retrieved on {date}. "
    "It does not establish novelty or correctness."
)
# "Novel" alone would read as a verdict, so its note says what the search did and did not show.
NOVEL_NOTE = (
    "An AI search of PubMed abstracts, retrieved on {date}, found nothing close to this "
    "result, so it could be new. It does not establish novelty or correctness."
)
NEED = {
    "data in the lakehouse": ("data", "Data already in the lakehouse"),
    "needs compute": ("build", "Analysis to build"),
    "needs new measurements": ("measure", "New measurements"),
    "unknown": ("unclear", "Not yet clear"),
}
APPROACH_TEXT = {
    "lakehouse analysis": "Analysis of existing data",
    "experiment": "Experiment",
    "analysis then experiment": "Analysis, then experiment",
}
NOT_COMPARED = "Not compared yet"
# The Results picture's columns, most novel first; the last shows only when non-empty.
COMPARE_ORDER = [*CHIP.values(), LABEL_TEXT["Insufficient literature evidence"], NOT_COMPARED]
# What each Results picture column means, shown when a reader hovers or taps its heading.
COMPARE_NOTES = {
    CHIP["Candidate novel"]: (
        "An AI search of PubMed abstracts found nothing close to these results, so they "
        "could be new. It does not establish novelty or correctness."
    ),
    CHIP["Extends retrieved work"]: (
        "PubMed abstracts report related work, and these results add to it."
    ),
    CHIP["In tension with retrieved work"]: (
        "PubMed abstracts report something different from these results."
    ),
    CHIP["Established in retrieved literature"]: "PubMed abstracts report a similar result.",
    LABEL_TEXT["Insufficient literature evidence"]: (
        "PubMed abstracts hold too little on these topics to compare."
    ),
    NOT_COMPARED: "These results are waiting for their PubMed search.",
}
RELATION_TEXT = {
    "same result": "Same result in each project",
    "one extends the other": "One project extends the other's analysis",
    "same direction, different definitions": "Different definitions, same direction",
    "similar comparison, different scope": "A similar comparison on different data",
    "one measures what the other cannot": "One measures what the other cannot",
}
# Pipeline phrases that can sit inside free text a stage wrote, such as a readiness
# explanation or a check note, with the words a reader sees instead.
READER_TERMS = {
    "needs compute": "needs a new analysis",
    "lakehouse analysis": "analysis of existing data",
    "Research direction": "Open question",
    "research direction": "open question",
} | {label: text for label, text in LABEL_TEXT.items()}
STATS = re.compile(
    r"\bp\s*[=<>≤]|\b[rq]\s*=|ρ|\brho\b|\bAUC\b|χ²|\bFDR\b|×\s*10"
    r"|\b(Cohen|Mann-Whitney|Kruskal|Spearman|Pearson|Mantel)\b",
    re.I,
)
# A null result a home or topic card may show: only the ones that measured something.
SHOWN_CASES = ("measured absence", "inconclusive test")
SPOTLIGHT = ("null result", "correction")


def reader_terms(text: str) -> str:
    """Free text with pipeline phrases replaced by the reader-facing words."""
    for term, plain_words in READER_TERMS.items():
        text = text.replace(term, plain_words)
    return text


def kind_text(result: str, case: str = "") -> str:
    """The reader's words for a record's kind; a null result's come from its summary's case."""
    if result == "null result" and case in NULL_CASE_TEXT:
        return NULL_CASE_TEXT[case]
    return KIND_TEXT.get(result, result)


def compare_text(entry: dict | None) -> str:
    """The Results picture's column for a finding: how it compares with PubMed, or that
    it has not been compared (no label yet, a failed first search, or withdrawn)."""
    return LABEL_TEXT.get((entry or {}).get("label", NOT_ASSESSED), NOT_COMPARED)


DIGESTS = ("discoveries", "pitfalls")


def split(text: str) -> tuple[dict, str]:
    m = FM.match(text)
    return ((yaml.safe_load(m.group(1)) or {}), text[m.end() :]) if m else ({}, text)


def join(fields: dict, body: str) -> str:
    return "---\n" + "".join(f"{k}: {json.dumps(v)}\n" for k, v in fields.items()) + "---\n" + body


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def cited(text: str) -> set[str]:
    return {
        re.sub(r"__REPORT$", "", part.strip())
        for tag in SRC_TAG.finditer(text)
        for part in re.split(r"[,;]", tag.group(1))
        if part.strip()
    }


class Corpus:
    """What the joins read: topic membership, citations, labels and the records."""

    def __init__(self, kb: pathlib.Path):
        self.kb = kb
        wiki = kb / "wiki"
        groups_path = kb / "state" / "curator-topics.json"
        groups = json.loads(groups_path.read_text())["groups"] if groups_path.exists() else []
        self.topic_concepts = {slugify(g["title"]): set(g["concepts"]) for g in groups}
        self.topic_titles = {slugify(g["title"]): g["title"] for g in groups}
        self.concept_titles = {
            f"concepts/{p.stem}": title_of(p.read_text(encoding="utf-8", errors="replace"), p.stem)
            for p in (wiki / "concepts").glob("*.md")
        }
        self.concept_cites = {
            p.stem: cited(p.read_text(encoding="utf-8", errors="replace"))
            for p in (wiki / "concepts").glob("*.md")
        }
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
        from beril_wiki.stages.cards import main_topics

        if sid not in self._topics:
            self._topics[sid] = main_topics(sid, self.topic_concepts, self.concept_cites)
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
        for name in (f"{sid}__REPORT.md", f"{sid}.md"):
            path = self.kb / "wiki" / "summaries" / name
            if path.exists():
                # Some report titles carry Markdown emphasis; a card footer shows plain text.
                title = title_of(path.read_text(encoding="utf-8", errors="replace"), sid)
                return re.sub(r"\*+", "", title).strip()
        return sid

    def related_conflicts(self, sid: str, topics: list[str]) -> list[str]:
        concepts = (
            set().union(*(self.topic_concepts.get(t, set()) for t in topics)) if topics else set()
        )
        return [
            stem
            for stem, text in self.conflicts.items()
            if stem.split("--")[1] in concepts and sid in cited(text)
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
    # Imported here: stages.topics imports this module through publish.ingest.
    from beril_wiki.stages import cards

    scope = cards.load_scope(kb)
    if scope is None:
        return {}
    out: dict[str, list[dict]] = {}
    seen: set[tuple[str, str]] = set()
    for topic in scope.topics:
        for b in cards.forward_bullets(kb, topic, scope.reports):
            if not cards.is_reanalysis(b["text"]):
                continue
            for sid in b["projects"]:
                if sid in cards.DIGESTS or (sid, b["text"]) in seen:
                    continue
                seen.add((sid, b["text"]))
                out.setdefault(sid, []).append(b)
    return dict(sorted(out.items()))


def title_of(body: str, fallback: str) -> str:
    m = re.search(r"^# +(.+)$", body, re.M)
    return m.group(1).strip() if m else fallback


def chip_note(entry: dict | None, result: str = "") -> str:
    """What a PubMed chip means and when it was checked; empty when there is no chip."""
    if not entry or not chip_of(entry, result):
        return ""
    return label_note(entry)


def label_note(entry: dict) -> str:
    """The note for a pipeline label, dated by its PubMed retrieval."""
    note = NOVEL_NOTE if entry.get("label") == "Candidate novel" else CHIP_NOTE
    return note.format(date=entry.get("retrieved_on", ""))


def chip_of(entry: dict | None, result: str = "") -> str:
    """The comparison chip a card shows; empty unless a pipeline label says something.

    A correction revises the project's own earlier analysis, so how PubMed relates to it
    says nothing a reader can use, and a chip there reads as a verdict on the error."""
    if not entry or entry.get("override") or result == "correction":
        return ""
    return CHIP.get(entry.get("label", NOT_ASSESSED), "")


def literature_section(entry: dict | None) -> str:
    """The label in plain words, then how it was reached, collapsed for readers."""
    heading = "## Compared with published work"
    if not entry or entry.get("label", NOT_ASSESSED) == NOT_ASSESSED:
        why = (entry or {}).get("override")
        return f"{heading}\n\n**Not assessed.** " + (
            f"A person withdrew the pipeline's label: {why}"
            if why
            else "The literature check has not run on this finding."
        )
    label = LABEL_TEXT.get(entry["label"], entry["label"])
    if not entry.get("retrieved_on"):
        # A label a person pinned on a finding the pipeline never reached.
        return (
            f"{heading}\n\n**{label}.** A person set this label: "
            f"{entry.get('override', '')} The pipeline has not retrieved literature for this "
            "finding."
        )
    lines = [heading, "", f"**{label}.**"]
    if entry.get("override"):
        lines[-1] += f" A person set this label: {entry['override']}"
    elif not entry.get("retrieved"):
        lines[-1] += f" PubMed searches on {entry['retrieved_on']} found no abstracts to compare."
    else:
        lines[-1] += " " + label_note(entry)
    # An unconfirmed judgment's difference and closest papers argued for the label the
    # other model rejected, so they would contradict the label shown.
    confirmed = entry.get("agreed") is not False
    if entry.get("difference") and confirmed:
        lines += ["", entry["difference"]]
    closest = [
        f"- [PMID {x['pmid']}]({PUBMED.format(x['pmid'])}) {x.get('title', '')} ({x['relation']})"
        for x in (entry.get("closest", []) if confirmed else [])
    ]
    if closest:
        lines += ["", "Closest papers:", "", *closest]
    queries = "; ".join(f"“{q}”" for q in entry.get("queries", []))
    how = [
        f"- Searched: {queries}, plus the papers the report cites; "
        f"{entry.get('retrieved', 0)} papers with abstracts were compared."
    ]
    if entry["label"] in GUARDED and entry.get("agreed"):
        how.append(f"- Confirmed independently by {entry.get('agree_model')}.")
    if entry.get("agreed") is False:
        proposed = LABEL_TEXT.get(entry.get("judged_label", ""), entry.get("judged_label"))
        how.append(
            f"- {entry.get('judge_model')} proposed “{proposed}”, which "
            f"{entry.get('agree_model')} did not confirm, so the weaker label shows."
        )
    lines += ["", "<details><summary>How this was checked</summary>", "", *how, "", "</details>"]
    return "\n".join(lines)


FROM_REPORT = re.compile(r"^From the report .*$", re.M)


def measured_and_limits(body: str) -> tuple[str, list[str], str, list[str]]:
    """Split a stored finding body into its title line, claim, sections and report line."""
    text = body.strip()
    h1 = ""
    if text.startswith("# "):
        h1, _, text = text.partition("\n")
    claim, _, tail = ("\n" + text).partition("\n## ")
    sec = sections("## " + tail) if tail else {}
    evidence = sec.pop("Evidence", "")
    report_line = FROM_REPORT.search(evidence)
    evidence = FROM_REPORT.sub("", evidence).strip()
    figures = sec.pop("Key figures", "")
    caveat = sec.pop("Caveat", "")
    others = sec.pop("Other caveats in this report", "")
    measured = ["## What the report measured", ""]
    if claim.strip():
        measured += [claim.strip(), ""]
    if figures:
        measured += ["**Key figures**", "", figures, ""]
    if evidence:
        measured += ["**Evidence from the report**", "", evidence, ""]
    limits: list[str] = []
    if caveat or others:
        limits = ["## Limits", ""]
        if caveat:
            limits += [caveat, ""]
        if others:
            # Report-wide caveats, most about other results; folded so the finding's own
            # caveat reads first, and kept so no caveat drops off the page.
            limits += [
                "<details><summary>Other caveats in this report, not specific to this "
                "result</summary>",
                "",
                others,
                "",
                "</details>",
                "",
            ]
    extra = [x for k, v in sec.items() for x in (f"## {k}", "", v, "")]
    return (
        h1,
        measured,
        "\n".join(limits + extra).strip(),
        [report_line.group(0)] if report_line else [],
    )


def eligible(c: Corpus, fid: str) -> bool:
    """Whether a finding is listed: on the Results page, in counts, the picture and picks.

    It needs an accepted plain summary that does not repeat an earlier finding from its
    report, and a null result must have measured something: missing data and an analysis
    that never ran are not results. An unlisted finding keeps its page, so links to it
    still resolve."""
    gist = c.gists.get(fid, {})
    if not gist.get("gist") or gist.get("repeats"):
        return False
    if c.findings[fid][0].get("result") == "null result":
        return gist.get("case") in SHOWN_CASES
    return True


def _picks(c: Corpus) -> tuple[list[str], dict[str, list[str]]]:
    if c._picks is None:
        ids = [f for f in sorted(c.findings) if eligible(c, f)]
        project = {f: c.findings[f][0].get("source", "") for f in ids}
        # The home shows results only from projects that feed two or more topics.
        broad = [f for f in ids if len(c.topics_of(project[f])) >= 2]
        home = _home(c, broad, project)
        topics: dict[str, list[str]] = {}
        for t in sorted({t for f in ids for t in c.topics_of(project[f])}):
            members = [f for f in ids if t in c.topics_of(project[f])]
            picked: list[str] = []
            for f in members:
                if len(picked) < 3 and project[f] not in {project[p] for p in picked}:
                    picked.append(f)
            if len(picked) == 3 and not any(
                c.findings[f][0].get("result") in SPOTLIGHT for f in picked
            ):
                used = {project[f] for f in picked[:-1]}
                swap = next(
                    (
                        f
                        for f in members
                        if c.findings[f][0].get("result") in SPOTLIGHT and project[f] not in used
                    ),
                    None,
                )
                if swap:
                    picked[-1] = swap
            topics[t] = picked
        c._picks = (home, topics)
    return c._picks


def _home(c: Corpus, ids: list[str], project: dict[str, str], n: int = 3) -> list[str]:
    """The n most interesting results, each from its own project and topic.

    Most interesting: furthest from PubMed abstracts (novel, then differs, then
    builds on), then linked to the most other projects, then a result before a null or
    correction, then from the project in the most topics."""
    tier = {text: i for i, text in enumerate(INTEREST)}
    others: dict[str, set[str]] = {}
    for link in links_index(c):
        if "a" in link and link["pa"] != link["pb"]:
            others.setdefault(link["a"], set()).add(link["pb"])
            others.setdefault(link["b"], set()).add(link["pa"])

    def rank(f: str) -> tuple:
        return (
            tier.get(compare_text(c.labels.get(f)), len(tier)),
            -len(others.get(f, ())),
            c.findings[f][0].get("result") in SPOTLIGHT,
            -len(c.topics_of(project[f])),
            f,
        )

    chosen: list[str] = []
    for f in sorted(ids, key=rank):
        if len(chosen) == n:
            break
        if project[f] in {project[x] for x in chosen}:
            continue
        if c.display_topic(project[f]) in {c.display_topic(project[x]) for x in chosen}:
            continue
        chosen.append(f)
    return chosen


def home_picks(c: Corpus, n: int = 3) -> list[str]:
    """Finding ids for the home page: the most interesting, from distinct topics and projects."""
    return _picks(c)[0][:n]


def topic_picks(c: Corpus, topic: str, n: int = 3) -> list[str]:
    """Up to n findings in a topic, by id, at most one per project."""
    return _picks(c)[1].get(topic, [])[:n]


def finding_title(c: Corpus, fid: str) -> str:
    return c.gists.get(fid, {}).get("title") or title_of(c.findings[fid][1], fid)


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
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x in c.link_records:
        a, b = x.get("a", ""), x.get("b", "")
        if x.get("level") == "finding" and x.get("type") in RELATION_TEXT:
            if a in c.findings and b in c.findings:
                parent[find(a)] = find(b)
    groups: dict[str, set[str]] = {}
    for x in parent:
        groups.setdefault(find(x), set()).add(x)
    return {frozenset(g) for g in groups.values()}


def relation_of(c: Corpus, members: list[str]) -> str:
    """How the current links relate a group's results: the strongest relation among
    them, in the order the shared stage ranks them (RELATION_TEXT's order)."""
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
    """Accepted shared results whose members still exist and still form one group of
    current related-result links, those spanning the most topics first. A links refresh
    that drops a link retires the statement at once, before the shared stage runs again."""
    groups = []
    current = related_components(c)
    for gid, g in sorted(c.shared_records.items()):
        members = g.get("members") or []
        if g.get("failed") or not members or any(m not in c.findings for m in members):
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


def home_questions(c: Corpus, n: int = 3) -> list[str]:
    """Cross-project questions for the home: most projects, then most topics; no project twice."""
    ranked = sorted(
        (d for d in c.directions if c.cross_projects(d)),
        key=lambda d: (
            -len(c.cross_projects(d)),
            -len(c.group_topics(list(c.cross_projects(d)))),
            d,
        ),
    )
    chosen: list[str] = []
    used: set[str] = set()
    for d in ranked:
        sids = set(c.cross_projects(d))
        if len(chosen) < n and not used & sids:
            chosen.append(d)
            used |= sids
    return chosen


def finding_page(fid: str, c: Corpus) -> str:
    fields, body = c.findings[fid]
    entry = c.labels.get(fid)
    sid = fields.get("source", "")
    topics = c.topics_of(sid)
    gist = c.gists.get(fid, {})
    chip = chip_of(entry, fields.get("result", ""))
    home, by_topic = _picks(c)
    ranks = {t: ids.index(fid) + 1 for t, ids in by_topic.items() if fid in ids}
    fields = fields | {
        "label": (entry or {}).get("label", NOT_ASSESSED),
        "label_date": (entry or {}).get("retrieved_on", ""),
        "topics": topics,
        "kind_text": kind_text(fields.get("result", ""), gist.get("case", "")),
        "chip": chip,
        "compare_text": compare_text(entry),
        "chip_note": chip_note(entry, fields.get("result", "")),
        "listed": eligible(c, fid),
        "gist": gist.get("gist", ""),
        "gist_case": gist.get("case", ""),
        "topic": c.display_topic(sid),
        "report_title": c.report_title(sid),
        "topic_ranks": ranks,
    }
    if fid in home:
        fields["home_rank"] = home.index(fid) + 1
    related = related_results(c, fid)
    if related:
        fields["related"] = [o for o, _ in related]
    h1, measured, limits, report = measured_and_limits(body)
    if gist.get("title"):
        h1 = f"# {gist['title']}"
    parts = [h1 or f"# {title_of(body, fid)}", ""]
    if gist.get("gist"):
        parts += [gist["gist"], ""]
    parts += measured
    if limits:
        parts += [limits, ""]
    parts += [literature_section(entry)]
    directions = c.directions_on(fid)
    if directions:
        parts += ["", "## Open questions that build on this", ""]
        parts += [f"- [[directions/{d}|{title_of(c.directions[d][1], d)}]]" for d in directions]
    if related:
        parts += ["", "## Related results in other projects", ""]
        parts += [
            f"- [[findings/{o}|{finding_title(c, o)}]] · "
            f"{c.report_title(c.findings[o][0].get('source', ''))} · {relation}"
            for o, relation in related
        ]
    conflicts = c.related_conflicts(sid, topics)
    if conflicts:
        parts += ["", "## Related conflicts", ""]
        parts += [f"- [[conflicts/{s}|{title_of(c.conflicts[s], s)}]]" for s in conflicts]
    parts += ["", *report]
    return join(fields, "\n".join(parts).rstrip() + "\n")


def sections(body: str) -> dict[str, str]:
    return {
        k.strip(): v.strip()
        for k, v in re.findall(r"^## (.+?)\n+(.*?)(?=\n## |\Z)", body, re.M | re.S)
    }


def plain(text: str) -> str:
    """Markdown link syntax as reading text, for text a reader pastes elsewhere."""
    text = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).rsplit("/", 1)[-1], text)
    return re.sub(r"\[(PMID \d+)\]\([^)]+\)", r"\1", text)


def grounding(fields: dict, c: Corpus) -> list[str]:
    lines = []
    for f in fields.get("findings") or []:
        if f in c.findings:
            meta = c.findings[f][0]
            lines.append(f"- Finding ({meta.get('source', '')}): {meta.get('description', '')}")
    for k in fields.get("conflicts") or []:
        if k in c.conflicts:
            lines.append(f"- Conflict: {title_of(c.conflicts[k], k)}")
    return lines


def beril_prompt(fields: dict, body: str, c: Corpus) -> str:
    """What a reader pastes into BERIL to start the project."""
    sec = sections(body)
    data = ", ".join(fields.get("collections") or []) or "none named"
    lines = [
        "I want to pursue this research direction with BERIL on the KBase Data Lakehouse.",
        "",
        f"Question: {fields.get('description', '')}",
        f"Hypothesis: {fields.get('hypothesis', '')}",
        f"Proposed test: {sec.get('How to test it', '')}",
        f"What would support or refute it: {sec.get('What would support or refute it', '')}",
        f"Collections: {data} (readiness: {fields.get('readiness', 'unknown')}; "
        f"{fields.get('readiness_basis', '')})",
        "",
        "It builds on these results from the BERIL wiki:",
        *grounding(fields, c),
        "",
        "Before running anything, check that the data the test needs is in the lakehouse, "
        "then propose an analysis plan and its first query.",
    ]
    return plain("\n".join(lines))


def brief(fields: dict, body: str, c: Corpus) -> str:
    """The Markdown a reader copies to hand a direction to a collaborator or a lab."""
    sec = sections(body)
    lines = [
        f"# {title_of(body, 'Research direction')}",
        "",
        f"**Question.** {fields.get('description', '')}",
        "",
        f"**Hypothesis.** {fields.get('hypothesis', '')}",
        "",
        f"**Why it matters.** {sec.get('Why it matters', '')}",
        "",
        f"**How to test it.** {sec.get('How to test it', '')}",
        "",
        f"**What would support or refute it.** {sec.get('What would support or refute it', '')}",
        "",
        f"**Approach and data.** {fields.get('approach', '')}; readiness: "
        f"{fields.get('readiness', 'unknown')}. {fields.get('readiness_basis', '')}",
        "",
        "**Builds on**",
        *grounding(fields, c),
    ]
    if sec.get("Closest published work"):
        lines += ["", "**Closest published work**", sec["Closest published work"]]
    lines += [
        "",
        "Source: the BERIL wiki, an AI-generated wiki compiled from AI-conducted research "
        "reports. No person reviewed this direction.",
    ]
    return plain("\n".join(lines))


APPROACH_LINE = re.compile(r"^Approach: (.+?)\. Readiness: (.+?)\. ", re.M)
LABEL_SUFFIX = re.compile(
    r"^(- Finding: .*) \((" + "|".join(map(re.escape, [*LABEL_TEXT, NOT_ASSESSED])) + r")\)$", re.M
)


def reader_words(body: str) -> str:
    """The generated body with pipeline terms replaced by the reader-facing ones."""

    def approach(m: re.Match) -> str:
        need = NEED.get(m.group(2), (None, m.group(2)))[1]
        return f"Approach: {APPROACH_TEXT.get(m.group(1), m.group(1))}. Needs: {need}. "

    def suffix(m: re.Match) -> str:
        chip = CHIP.get(m.group(2))
        return f"{m.group(1)} ({chip})" if chip else m.group(1)

    return LABEL_SUFFIX.sub(suffix, APPROACH_LINE.sub(approach, body))


def direction_page(did: str, c: Corpus) -> str:
    fields, body = c.directions[did]
    topics = fields.get("topics") or []
    need = NEED.get(fields.get("readiness", "unknown"), NEED["unknown"])
    extra = {
        "beril_prompt": beril_prompt(fields, body, c),
        "brief": brief(fields, body, c),
        "need": need[0],
        "need_text": need[1],
        "approach_text": APPROACH_TEXT.get(fields.get("approach", ""), fields.get("approach", "")),
        "topic": topics[0] if topics else "",
    }
    if fields.get("readiness_basis"):
        extra["readiness_basis"] = reader_terms(fields["readiness_basis"])
    by = c.cross_projects(did)
    if by:
        extra["cross"] = [
            {
                "source": sid,
                "title": c.report_title(sid),
                "topic": c.display_topic(sid),
                "results": [{"id": f, "title": finding_title(c, f)} for f in fids],
            }
            for sid, fids in sorted(by.items())
        ]
        extra["cross_topics"] = c.group_topics(sorted(by))
    if did in home_questions(c):
        extra["home_question_rank"] = home_questions(c).index(did) + 1
    return join(fields | extra, reader_terms(reader_words(body)).rstrip() + "\n")


def issues_page(sid: str, items: list[dict], provenance: str, titles: dict[str, str]) -> str:
    """One report's maintainer list: proposals that would redo or correct its work."""
    lines = [
        f'---\ntitle: {json.dumps(f"Data issues: {sid}")}\ntype: "Data issues"\n---',
        provenance,
        "",
        f"Proposals in the wiki that would repeat, correct or reconcile work in "
        f"[[summaries/{sid}|{sid}]]. They are for the report's maintainers, not research "
        "directions. Each names the page that proposes it.",
        "",
    ]
    for b in items:
        page = b["page"]
        if page.startswith("sources/"):
            where = f"[[summaries/{sid}|the report]] ({b['section']})"
        else:
            where = f"[[{page}|{titles.get(page, page.rsplit('/', 1)[-1])}]] ({b['section']})"
        text = SRC_TAG.sub(
            lambda m: "(" + ", ".join(x.strip() for x in m.group(1).split(",")) + ")", b["text"]
        )
        lines.append(f"- {text} From {where}.")
    return "\n".join(lines) + "\n"


INDEXES = {
    "findings": (
        "Results",
        "Results from the project reports, one per card.",
    ),
    "directions": (
        "Open questions",
        "Questions the project results leave open, by topic and by what answering them needs.",
    ),
}


def export(c: Corpus) -> dict:
    """The same records as JSON, for agents."""
    findings = []
    for fid, (fields, body) in c.findings.items():
        entry = c.labels.get(fid, {})
        findings.append(
            {
                "id": fid,
                "url": f"findings/{fid}",
                "title": title_of(body, fid),
                "claim": fields.get("description"),
                "result": fields.get("result"),
                "source": fields.get("source"),
                "quantities": fields.get("quantities", []),
                "caveat": fields.get("caveat"),
                "topics": c.topics_of(fields.get("source", "")),
                "label": entry.get("label", NOT_ASSESSED),
                "label_date": entry.get("retrieved_on"),
                # An unconfirmed judgment's papers argued for the label that was rejected.
                "closest": entry.get("closest", []) if entry.get("agreed") is not False else [],
                "gist": c.gists.get(fid, {}).get("gist", ""),
            }
        )
    directions = [
        {"id": d, "url": f"directions/{d}", "title": title_of(body, d)}
        | {
            k: fields.get(k)
            for k in ("description", "hypothesis", "approach", "readiness", "readiness_basis")
        }
        | {
            k: fields.get(k, [])
            for k in ("collections", "findings", "conflicts", "papers", "projects", "topics")
        }
        for d, (fields, body) in c.directions.items()
    ]
    issues = {sid: [b["text"] for b in items] for sid, items in c.issues.items()}
    return {
        "findings": findings,
        "research_directions": directions,
        "data_issues": issues,
        "home": home_picks(c),
        "topic_picks": _picks(c)[1],
        "links": links_index(c),
        "shared": shared_index(c),
    }


def record(rel: pathlib.Path, c: Corpus) -> str:
    """A record page's source text with its joins, before ingest's generic transforms."""
    return finding_page(rel.stem, c) if rel.parts[0] == "findings" else direction_page(rel.stem, c)


def picture_data(c: Corpus) -> dict:
    """What the Results picture and the home cards read from the results index page."""
    links = links_index(c)
    named = {x[k] for x in links for k in ("pa", "pb")}
    return {
        "compare_order": COMPARE_ORDER,
        "compare_notes": {text: COMPARE_NOTES[text] for text in COMPARE_ORDER},
        "links": links,
        "shared": shared_index(c),
        "project_titles": {sid: c.report_title(sid) for sid in sorted(named)},
        "empty_topics": sorted(
            set(c.topic_titles)
            - {
                c.display_topic(c.findings[fid][0].get("source", ""))
                for fid in c.findings
                if eligible(c, fid)
            }
        ),
    }


def write_extras(dst: pathlib.Path, c: Corpus, provenance: str) -> int:
    """Collection landing pages and the JSON export; returns the pages written."""
    n = 0
    for folder, pages in (("findings", c.findings), ("directions", c.directions)):
        if pages:
            title, blurb = INDEXES[folder]
            fields: dict = {"title": title}
            if folder == "findings":
                fields |= picture_data(c)
            (dst / folder / "index.md").write_text(
                join(fields, f"{provenance}\n\n{blurb}\n"), encoding="utf-8"
            )
            n += 1
    if c.issues:
        (dst / ISSUES).mkdir(exist_ok=True)
        titles = {f"conflicts/{k}": title_of(v, k) for k, v in c.conflicts.items()}
        titles |= c.concept_titles
        for sid, items in c.issues.items():
            (dst / ISSUES / f"{sid}.md").write_text(
                issues_page(sid, items, provenance, titles), encoding="utf-8"
            )
        rows = "\n".join(
            f"- [[{ISSUES}/{sid}|{sid}]]: {len(items)} item(s)" for sid, items in c.issues.items()
        )
        (dst / ISSUES / "index.md").write_text(
            f'---\ntitle: "Data issues"\n---\n{provenance}\n\nProposals that would repeat, '
            "correct or reconcile existing analyses, grouped by the report they concern. They "
            f"are for the reports' maintainers, not research directions.\n\n{rows}\n",
            encoding="utf-8",
        )
        n += len(c.issues) + 1
    (dst / "cards.json").write_text(json.dumps(export(c), indent=1), encoding="utf-8")
    return n
