"""The finding, research-direction and data-issue pages a reader opens."""

from __future__ import annotations

import json
import pathlib
import re

from beril_wiki import records
from beril_wiki.publish.cards.corpus import Corpus, eligible, finding_title, join, result_type
from beril_wiki.publish.cards.links import related_results
from beril_wiki.publish.cards.picks import home_questions, pick_lists
from beril_wiki.publish.cards.text import (
    CHIP,
    FIRST_STEP_TEXT,
    FOLLOW_TEXT,
    GUARDED,
    LABEL_TEXT,
    NOT_ASSESSED,
    PUBMED,
    TYPE_TEXT,
    UNCLEAR_TEXT,
    chip_note,
    chip_of,
    compare_text,
    follow_of,
    label_note,
    reader_terms,
)
from beril_wiki.records import title_of


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


def finding_page(fid: str, c: Corpus) -> str:
    fields, body = c.findings[fid]
    entry = c.labels.get(fid)
    sid = fields.get("source", "")
    topics = c.topics_of(sid)
    gist = c.gists.get(fid, {})
    listed = eligible(c, fid)
    # An unlisted correction is a bookkeeping fix: no revision note and no PubMed verdict.
    revises = fields.get("result") == "correction"
    shown = listed or not revises
    chip = chip_of(entry, fields.get("result", "")) if shown else ""
    home, by_topic = pick_lists(c)
    ranks = {t: ids.index(fid) + 1 for t, ids in by_topic.items() if fid in ids}
    fields = fields | {
        "label": (entry or {}).get("label", NOT_ASSESSED),
        "label_date": (entry or {}).get("retrieved_on", ""),
        "topics": topics,
        "rtype": result_type(c, fid),
        "kind_text": TYPE_TEXT.get(result_type(c, fid), ""),
        # A listed correction reports a result; its card says it revises an earlier claim.
        "updates_claim": listed and revises,
        "chip": chip,
        "compare_text": compare_text(entry),
        "chip_note": chip_note(entry, fields.get("result", "")) if shown else "",
        "listed": listed,
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
        f"Collections: {data}. {follow_line(follow_fields(fields, c))} "
        f"{fields.get('readiness_basis', '')}",
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
        f"**What following up needs.** {follow_line(follow_fields(fields, c))} "
        f"{fields.get('readiness_basis', '')}",
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


def follow_line(follow: dict) -> str:
    """What following up needs, as the question page's Data section states it."""
    parts = [f"Following up: {FOLLOW_TEXT[follow['follow']].lower()}."]
    if follow.get("first_step"):
        parts.append(f"{FIRST_STEP_TEXT}.")
    if follow.get("data_unclear"):
        parts.append(f"{UNCLEAR_TEXT}.")
    return " ".join(parts)


def reader_words(body: str, follow: dict | None = None) -> str:
    """The generated body with pipeline terms replaced by the reader-facing ones."""

    def approach(m: re.Match) -> str:
        return follow_line(follow) + " " if follow else ""

    def suffix(m: re.Match) -> str:
        chip = CHIP.get(m.group(2))
        return f"{m.group(1)} ({chip})" if chip else m.group(1)

    return LABEL_SUFFIX.sub(suffix, APPROACH_LINE.sub(approach, body))


def follow_fields(fields: dict, c: Corpus) -> dict:
    """A question's follow-up need for its page: column, words and the two markers."""
    entry = c.followups.get(fields.get("_id", ""))
    follow = follow_of(entry, fields.get("approach", ""))
    first = (
        bool(entry.get("first_step_existing"))
        if entry
        else (follow == "experiment" and fields.get("approach") == "analysis then experiment")
    )
    unclear = bool(entry.get("data_unclear")) if entry else fields.get("readiness") == "unknown"
    return {
        "follow": follow,
        "follow_text": FOLLOW_TEXT[follow],
        "first_step": first and follow == "experiment",
        "data_unclear": unclear,
    }


def direction_page(did: str, c: Corpus) -> str:
    fields, body = c.directions[did]
    topics = fields.get("topics") or []
    keyed = fields | {"_id": did}
    follow = follow_fields(keyed, c)
    extra = {
        "beril_prompt": beril_prompt(keyed, body, c),
        "brief": brief(keyed, body, c),
        **follow,
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
    return join(fields | extra, reader_terms(reader_words(body, follow)).rstrip() + "\n")


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
        text = records.SRC.sub(
            lambda m: "(" + ", ".join(x.strip() for x in m.group(1).split(",")) + ")", b["text"]
        )
        lines.append(f"- {text} From {where}.")
    return "\n".join(lines) + "\n"


def record(rel: pathlib.Path, c: Corpus) -> str:
    """A record page's source text with its joins, before ingest's generic transforms."""
    return finding_page(rel.stem, c) if rel.parts[0] == "findings" else direction_page(rel.stem, c)
