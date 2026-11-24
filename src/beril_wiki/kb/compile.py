"""Compile the whole wiki from its reports in one run.

``ingest`` reads one report into a wiki that exists. Running it once per report would
rewrite a shared page every time another report touched it, and the page list would
depend on the order the reports arrived in. ``compile`` does each kind of work once:

1. every report is extracted into claims, in parallel;
2. each report proposes the concept and entity pages its claims belong on;
3. the proposals of all reports are merged into one page list (``knowledge/catalog.json``);
4. each report's claims are routed to that list (``knowledge/routes/``);
5. every page is written once from all the claims routed to it, in passes of
   ``PASS`` claims, and reviewed by the other vendor;
6. the record stages run for each report and then once for the corpus.

A session gets its whole input in the task message and has one tool, so it reads
nothing twice. The writer cites claims by tag (``[C4]``); the published page shows the
report (``[src: id]``) and the sidecar keeps which claims each section rests on.

Every step is recorded in the run, so the same command resumes a stopped compile and
pays for nothing a second time.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from typing import Any

from beril_wiki.compiler import rebuild_index
from beril_wiki.kb import index, jobs, pages
from beril_wiki.kb.store import (
    DIGESTS,
    HEADING,
    Busy,
    Store,
    blocks,
    checkout_lock,
    sha256,
    write_jsonl,
    write_text,
)
from beril_wiki.kb.tools import (
    CLAIM_TAG,
    ENTITY_TYPES,
    FORWARD,
    NOT_PLACED,
    REJECTIONS,
    Rejected,
    page_candidate,
    statement_texts,
    statements,
    tags_in,
)
from beril_wiki.kb.workflow import (
    Config,
    Launch,
    Runner,
    Stop,
    mirror_report,
    queue_rows,
    tidy,
)

# Claims one writing session integrates. The curator measured that a page written from
# more than this in one go drops evidence.
PASS = 60
MAX_PASSES = {"summaries": 3, "concepts": 6, "entities": 4}
# A report with more claims than three passes hold gets a summary written part by part:
# an overview, then one section for each part of the report, each from all the claims of
# that part. Written as one page in eight passes from a sample of the claims, the three
# longest sources of the second pilot scored 4 to 5 of 10 on fidelity (lists cut short
# by the sampling, the page patched eight times) against 9 to 10 for the short reports.
SECTIONED = PASS * 3
PART_CLAIMS = 50
OVERVIEW = 60
# In the result of a compile that stopped where --claims-only, --routes-only or
# --pages-only asked it to: the run is left open, and the command did what it was asked.
CHECKPOINT = {"checkpoint": True}
# Characters in the heading of one part of a long summary.
TITLE = 90
# Step numbers of the parts of a sectioned summary; the passes of a page count from 0.
PART_STEPS = 100
# A page with less evidence than this is not worth a page; its claims stay in the
# summaries of their reports.
MIN_CLAIMS = {"concepts": 3, "entities": 2}
# Characters of a report one session reads into claims, and of its opening shown to the
# sessions that read later parts.
PART = 8_000
OPENING = 1_500
PAGES_PER_CLAIM = 3
# Page names the site generates itself.
RESERVED = ("index", "lead")
REQUIRED = {"concepts": ["Open Directions"], "summaries": ["Key Findings"]}
REPORT_STAGES = ("findings", "gists", "outcomes", "novelty")
REPORTS_AT_ONCE = 4
# Pages written in this run before the share that failed is judged; more than half of
# the last twenty stops the run, so a fault in a skill or a check costs twenty pages.
CANARY = 10
CORPUS_STAGES = tuple(s for s in jobs.STAGES if s not in REPORT_STAGES)


def topics(store: Store) -> list[dict]:
    """The fixed topic list: ``[{"slug", "title", "scope"}]``."""
    path = store.dir / "topics.json"
    if not path.exists():
        raise Stop("knowledge/topics.json is missing; a compile needs the topic list")
    return json.loads(path.read_text(encoding="utf-8"))


def catalog(store: Store) -> dict[str, dict]:
    path = store.dir / "catalog.json"
    return json.loads(path.read_text(encoding="utf-8"))["pages"] if path.exists() else {}


def routes(store: Store, source: str) -> list[dict]:
    path = store.dir / "routes" / f"{source}.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def active(store: Store, source: str) -> list[dict]:
    return [c for c in store.claims(source) if c.get("status", "active") == "active"]


def short(claim_id: str) -> str:
    return claim_id.rsplit(":", 1)[-1]


def report_title(store: Store, source: str) -> str:
    title = HEADING.search(store.source_text(source))
    return re.sub(r"^Report:\s*", "", title.group(2)).strip() if title else source


LONG_FORM = re.compile(
    r"((?:[A-Za-z][\w'’-]*[ -]){1,7}[A-Za-z][\w'’-]*)\s+\(([A-Z][A-Za-z0-9-]{1,11}?)s?\)"
)


def glossary(store: Store, sources: list[str]) -> dict[str, dict[str, list[str]]]:
    """Abbreviations the reports expand themselves: ``{abbr: {long form: [reports]}}``.

    A writer may expand an abbreviation only as a report does, and a reviewer cannot
    check an expansion against a claim that never spells it out. Reading the pattern
    "long form (ABBR)" off the reports gives both the same list.
    """
    out: dict[str, dict[str, list[str]]] = {}
    for source in sources:
        for m in LONG_FORM.finditer(store.source_text(source)):
            words, abbr = re.split(r"[ -]+", m.group(1)), m.group(2)
            letters = [c for c in abbr if c.isalpha()]
            if len(letters) < 2 or len(words) < len(letters):
                continue
            tail = words[-len(letters) :]
            if [w[0].lower() for w in tail] != [c.lower() for c in letters]:
                continue
            long = " ".join(tail)
            reports = out.setdefault(abbr, {}).setdefault(long, [])
            if source not in reports:
                reports.append(source)
    return out


ABBREVIATION = re.compile(
    r"(?<![\w-])([A-Z][A-Za-z0-9]*[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*)(?![\w-])"
)
GLOSSARY_TERMS = 300


def glossary_job(store: Store, sources: list[str]) -> jobs.Job | None:
    """One reviewed list of expansions for the abbreviations the claims use.

    A page that expands FDR from memory may expand it wrongly, and two pages may expand
    it differently. One list, proposed by one vendor and checked by the other, gives
    every writer and every reviewer the same answer.
    """
    given = glossary(store, sources)
    counts: dict[str, int] = {}
    seen_in: dict[str, list[str]] = {}
    for source in sources:
        for c in active(store, source):
            for abbr in set(ABBREVIATION.findall(c["text"])):
                abbr = abbr[:-1] if abbr.endswith("s") and abbr[:-1].isupper() else abbr
                counts[abbr] = counts.get(abbr, 0) + 1
                if len(seen_in.setdefault(abbr, [])) < 2:
                    seen_in[abbr].append(c["text"][:220])
    wanted = sorted(counts, key=lambda a: (-counts[a], a))
    wanted = [a for a in wanted if counts[a] >= 2 or a in given][:GLOSSARY_TERMS]
    if not wanted:
        return None

    def check(record: dict) -> dict:
        problems: list[str] = []
        terms: dict[str, str] = {}
        listed_terms = record.get("terms")
        if not isinstance(listed_terms, list):
            raise Rejected("the record needs a terms list", ['use {"terms": [...], "skip": [...]}'])
        for item in listed_terms:
            if not isinstance(item, dict):
                continue
            abbr = str(item.get("abbr", "")).strip()
            long = " ".join(str(item.get("long", "")).split())
            if abbr not in counts:
                problems.append(f"{abbr!r} is not in the list")
            elif not 3 <= len(long) <= 90 or long.lower() == abbr.lower():
                problems.append(f"{abbr}: the expansion must be 3 to 90 characters")
            else:
                terms[abbr] = long
        skipped = {str(a).strip() for a in record.get("skip") or []}
        both = sorted(skipped & set(terms))
        if both:
            problems.append("both expanded and skipped: " + ", ".join(both[:20]))
        for abbr, long in terms.items():
            said = {form.lower() for form in given.get(abbr, {})}
            if len(said) == 1 and long.lower() not in said:
                problems.append(f"{abbr}: the reports expand it as {next(iter(said))!r}")
        left = [a for a in wanted if a not in terms and a not in skipped]
        if left:
            problems.append("neither expanded nor skipped: " + ", ".join(left[:40]))
        if problems:
            raise Rejected("the glossary fails its checks", problems[:20])
        return {"terms": [{"abbr": a, "long": terms[a]} for a in sorted(terms)]}

    def publish(record: dict) -> None:
        terms = {t["abbr"]: t["long"] for t in record["terms"]}
        write_text(
            store.dir / "glossary.json",
            json.dumps(terms, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
        )

    rows = []
    for abbr in wanted:
        row: dict[str, Any] = {"abbr": abbr, "claims": counts[abbr], "used_in": seen_in[abbr]}
        if abbr in given:
            row["reports_expand_it_as"] = sorted(given[abbr])
        rows.append(row)
    return jobs.Job(
        stage="glossary",
        key="glossary/corpus",
        pack={"abbreviations": rows},
        check=check,
        publish=publish,
        writer="curate",
        reviewer="review",
        skill="wiki-glossary",
        review_skill="wiki-glossary-review",
    )


def settled_glossary(store: Store, sources: list[str]) -> dict[str, str]:
    """The reviewed glossary, or without one the expansions the reports agree on."""
    path = store.dir / "glossary.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        abbr: next(iter(forms))
        for abbr, forms in glossary(store, sources).items()
        if len({f.lower() for f in forms}) == 1
    }


def expansions(terms: dict[str, str], rows: list[dict]) -> dict[str, str]:
    """The glossary entries for the abbreviations a page's claims use."""
    text = " ".join(f"{c['text']} {c['quote']}" for c in rows)
    return {
        abbr: long
        for abbr, long in sorted(terms.items())
        if re.search(rf"(?<![\w-]){re.escape(abbr)}s?(?![\w-])", text)
    }


# Step 1: extraction


def spans_of(text: str) -> list[list[int]]:
    """A report cut into parts of about ``PART`` characters, at its headings and, inside
    a section longer than that, at its paragraph breaks."""
    cuts: list[int] = []
    for start, end, _ in blocks(text):
        cuts.append(start)
        at = start
        while end - at > PART * 3 // 2:
            # The paragraph break nearest a part's length on; none means a table or a
            # list that long, which stays whole.
            near = text.find("\n\n", at + PART, end)
            if near < 0 or end - near < PART // 4:
                break
            at = near + 2
            cuts.append(at)
    out: list[list[int]] = []
    for start, end in zip(cuts, [*cuts[1:], len(text)], strict=True):
        if out and end - out[-1][0] <= PART:
            out[-1][1] = end
        else:
            out.append([start, end])
    out[0][0] = 0
    return out


def extract_part(runner: Runner, source: str, n: int, span: list[int], parts: int) -> list[dict]:
    """The claims of one part of a report, as its session staged them.

    The part is in the task message and the session has the one tool that records
    claims. An extractor that read the report through a tool re-sent everything it had
    read with each call: 119,000 tokens a session in the first compile pilot.
    """
    store = runner.store
    text = store.source_text(source)

    def make() -> list[dict]:
        outline = [
            f"{'>' if span[0] <= m.start() < span[1] else ' '} {m.group(0).strip()[:100]}"
            for m in HEADING.finditer(text)
        ]
        lines = [
            f"Report id: {source}",
            f"Title: {report_title(store, source)}",
            f"This is part {n + 1} of {parts}: characters {span[0]}-{span[1]} of {len(text)}.",
            "",
            "REPORT OUTLINE (> marks the headings inside this part)",
            *outline[:200],
        ]
        if span[0]:
            lines += ["", "OPENING OF THE REPORT (context only)", text[:OPENING].strip()]
        lines += ["", "PART TO EXTRACT", text[span[0] : span[1]]]
        session, run = runner.dispatch(
            f"extract-{source}-{n}of{parts}",
            "extract",
            {"source": source, "spans": [span]},
            "\n".join(lines),
            tools="claims",
            skill="wiki-extract-part",
        )
        if not run.ok and not session.finished:
            raise Stop(run.error or "the extractor stopped before it recorded the part")
        if not (session.finished or session.claims):
            raise Stop("the extractor recorded nothing for the part")
        refused = session.rejections.get("claims", 0)
        if refused:
            # Claims the checks still refused when the session ended are not in the
            # wiki. The count is kept so a reader of the run can see how many.
            with runner.lock:
                runner.state.setdefault("refused_claims", {})[f"{source}-{n}of{parts}"] = refused
        return session.claims

    # Named by the number of parts, so a run begun under another cut reads again.
    return runner.step(f"extract-{source}-{n}of{parts}", make)


def extract_all(runner: Runner, sources: list[str]) -> dict[str, int | str]:
    """Claims of every report on disk. The parts of a long report are read by separate
    sessions at the same time, and numbered afterwards in the order of the report."""
    store = runner.store
    work = []
    for source in sources:
        mirror_report(store, source)
        if source in DIGESTS:
            # A digest's summary names this copy as its full text.
            write_text(store.root / "wiki" / "sources" / f"{source}.md", store.source_text(source))
        parts = spans_of(store.source_text(source))
        work += [(source, n, span, len(parts)) for n, span in enumerate(parts)]

    read_parts: list[int] = []

    def read(item: tuple[str, int, list[int], int]) -> tuple[str, list[dict] | str]:
        try:
            return item[0], extract_part(runner, *item)
        except Stop as exc:
            return item[0], str(exc)
        finally:
            read_parts.append(item[1])
            runner.stage("extract (parts of reports)", len(read_parts), len(work))

    found: dict[str, list[dict]] = {s: [] for s in sources}
    out: dict[str, int | str] = {}
    for source, result in each(runner, work, read):
        if isinstance(result, str):
            out[source] = result
        else:
            found[source] += result
    for source in sources:
        if source in out:
            continue
        # Two parts overlap at no character, so a repeat is the same claim staged twice.
        # One passage may still carry two claims of a kind, told apart by their text.
        seen: set[tuple[str, str, str]] = set()
        claims: list[dict] = []
        for claim in sorted(found[source], key=lambda c: (c["start"], c["end"])):
            if (claim["quote"], claim["kind"], claim["text"]) in seen:
                continue
            seen.add((claim["quote"], claim["kind"], claim["text"]))
            claims.append(
                {**claim, "id": f"{source}:n{len(claims)}", "added": date.today().isoformat()}
            )
        store.write_claims(source, claims)
        out[source] = len(claims)
    return out


# Steps 2 to 4: the page list and the routing table


def listed(claims: list[dict]) -> str:
    return "\n".join(f"{short(c['id'])} [{c['kind']}] {c['text']}" for c in claims)


def claim_ids(
    source: str, values: Any, known: set[str], problems: list[str], where: str
) -> list[str]:
    out = []
    for value in values if isinstance(values, list) else []:
        cid = str(value).strip()
        cid = cid if ":" in cid else f"{source}:{cid}"
        if cid in known:
            out.append(cid)
        else:
            problems.append(f"{where}: {value!r} is not a claim id of this report")
    return sorted(set(out), key=lambda c: int(short(c)[1:]))


def propose_job(store: Store, source: str, run_dir: Path) -> jobs.Job:
    claims = [c for c in active(store, source) if c["kind"] != "figure"]
    known = {c["id"] for c in claims}
    topic_slugs = {t["slug"] for t in topics(store)}
    most = {
        "concepts": max(3, min(10, len(claims) // 20)),
        "entities": max(5, min(25, len(claims) // 8)),
    }

    def check(record: dict) -> dict:
        problems: list[str] = []
        out: dict[str, list[dict]] = {"concepts": [], "entities": []}
        for kind in out:
            items = record.get(kind)
            if not isinstance(items, list):
                problems.append(f"{kind} must be a list")
                continue
            if len(items) > most[kind]:
                problems.append(f"at most {most[kind]} {kind} for this report; keep the strongest")
            for item in items:
                title = " ".join(str(item.get("title", "")).split())
                where = f"{kind} {title[:40]!r}"
                scope = " ".join(str(item.get("scope", "")).split())
                if not 3 <= len(title) <= 110 or not pages.slug(title):
                    problems.append(f"{where}: title must be 3 to 110 characters")
                if pages.slug(title) in RESERVED:
                    problems.append(f"{where}: that title is reserved; name the subject")
                if not 20 <= len(scope) <= 300:
                    problems.append(f"{where}: scope must be one sentence of 20 to 300 characters")
                ids = claim_ids(source, item.get("claims"), known, problems, where)
                if not ids:
                    problems.append(f"{where}: needs at least one claim id")
                row: dict[str, Any] = {"title": title, "scope": scope, "claims": ids}
                if kind == "concepts":
                    row["topic"] = str(item.get("topic", "")).strip()
                    if row["topic"] not in topic_slugs:
                        problems.append(f"{where}: topic must be one of the listed topic slugs")
                    if re.search(re.escape(source.replace("_", " ")), title, re.I):
                        problems.append(f"{where}: a concept is not named after the project")
                else:
                    row["type"] = str(item.get("type", "")).strip()
                    if row["type"] not in ENTITY_TYPES:
                        problems.append(f"{where}: type must be one of {', '.join(ENTITY_TYPES)}")
                    aliases = item.get("aliases") or []
                    row["aliases"] = [" ".join(str(a).split()) for a in aliases][:8]
                out[kind].append(row)
        if problems:
            raise Rejected("the proposal fails its checks", problems[:20])
        return out

    def publish(record: dict) -> None:
        write_text(run_dir / "proposals" / f"{source}.json", json.dumps(record, ensure_ascii=False))

    pack = {
        "report": source,
        "title": report_title(store, source),
        "limits": most,
        "topics": [
            {"slug": t["slug"], "title": t["title"], "scope": t["scope"]} for t in topics(store)
        ],
        "claims": listed(claims),
    }
    return jobs.Job(
        stage="propose",
        key=f"propose/{source}",
        pack=pack,
        check=check,
        publish=publish,
        writer="curate",
        reviewer="",
        skill="wiki-propose",
    )


def normal(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def candidates(run_dir: Path, sources: list[str]) -> dict[str, list[dict]]:
    """Every proposal, with entities of the same name already merged in code."""
    concepts: list[dict] = []
    by_name: dict[str, dict] = {}
    for source in sources:
        path = run_dir / "proposals" / f"{source}.json"
        if not path.exists():
            continue
        record = json.loads(path.read_text(encoding="utf-8"))
        for item in record["concepts"]:
            concepts.append({**item, "reports": [source]})
        for item in record["entities"]:
            names = [normal(n) for n in [item["title"], *item.get("aliases", [])] if normal(n)]
            found = next((by_name[n] for n in names if n in by_name), None)
            if found is None:
                found = {**item, "reports": [], "claims": [], "aliases": []}
            found["reports"] = sorted({*found["reports"], source})
            found["claims"] = [*found["claims"], *item["claims"]]
            found["aliases"] = sorted(
                {*found["aliases"], *item.get("aliases", [])} - {found["title"]}
            )
            for n in names:
                by_name.setdefault(n, found)
    entities = list({id(e): e for e in by_name.values()}.values())
    for n, item in enumerate(concepts):
        item["id"] = f"K{n + 1}"
    for n, item in enumerate(sorted(entities, key=lambda e: normal(e["title"]))):
        item["id"] = f"E{n + 1}"
    return {"concepts": concepts, "entities": entities}


def consolidate_job(
    store: Store, kind: str, group: str, items: list[dict], run_dir: Path
) -> jobs.Job:
    by_id = {i["id"]: i for i in items}
    topic_slugs = {t["slug"] for t in topics(store)}

    def check(record: dict) -> dict:
        problems: list[str] = []
        seen: dict[str, str] = {}
        slugs: set[str] = set()
        out = []
        wanted = record.get("pages")
        if not isinstance(wanted, list) or not all(isinstance(x, dict) for x in wanted):
            raise Rejected("the record needs a pages list", ['use {"pages": [...]}'])
        for page in wanted:
            title = " ".join(str(page.get("title", "")).split())
            where = f"page {title[:40]!r}"
            scope = " ".join(str(page.get("scope", "")).split())
            slug = pages.slug(title)
            if not 3 <= len(title) <= 110 or not slug:
                problems.append(f"{where}: title must be 3 to 110 characters")
            if slug in RESERVED:
                problems.append(f"{where}: that title is reserved; name the subject")
            if slug in slugs:
                problems.append(f"{where}: two pages have the same title")
            slugs.add(slug)
            if not 20 <= len(scope) <= 300:
                problems.append(f"{where}: scope must be one sentence of 20 to 300 characters")
            members = [str(m).strip() for m in page.get("members") or []]
            if not members:
                problems.append(f"{where}: needs at least one member candidate id")
            for m in members:
                if m not in by_id:
                    problems.append(f"{where}: {m!r} is not a candidate id")
                elif m in seen:
                    problems.append(f"{m} is a member of both {seen[m]!r} and {title!r}")
                seen[m] = title
            row: dict[str, Any] = {"title": title, "scope": scope, "members": members}
            if kind == "concepts":
                row["topic"] = str(page.get("topic", "")).strip()
                if row["topic"] not in topic_slugs:
                    problems.append(f"{where}: topic must be one of the listed topic slugs")
            else:
                row["type"] = str(page.get("type", "")).strip()
                if row["type"] not in ENTITY_TYPES:
                    problems.append(f"{where}: type must be one of {', '.join(ENTITY_TYPES)}")
                row["aliases"] = [" ".join(str(a).split()) for a in page.get("aliases") or []][:10]
            out.append(row)
        listed = record.get("dropped") or []
        if not isinstance(listed, list) or not all(isinstance(x, dict) for x in listed):
            raise Rejected(
                "dropped must be a list of objects", ['use {"id": "K3", "reason": "..."}']
            )
        # Stored as checked: the id without stray spaces is the one later steps look up.
        dropped = [
            {"id": str(d.get("id", "")).strip(), "reason": str(d.get("reason", "")).strip()}
            for d in listed
        ]
        for item in dropped:
            cid = item["id"]
            if cid not in by_id:
                problems.append(f"dropped: {cid!r} is not a candidate id")
            elif cid in seen:
                problems.append(f"{cid} is both dropped and a member of {seen[cid]!r}")
            elif not item["reason"]:
                problems.append(f"dropped {cid}: needs a reason")
            seen[cid] = "dropped"
        if problems:
            raise Rejected("the page list fails its checks", problems[:25])
        # A candidate the list does not mention stays a page of its own, as proposed.
        # The model writes only what it merges or renames: a list that repeated every
        # candidate was 33,000 output tokens for about a hundred of them.
        named = {pages.slug(row["title"]): row for row in out}
        for cid in sorted(set(by_id) - set(seen), key=lambda c: int(c[1:])):
            item = by_id[cid]
            same = named.get(pages.slug(item["title"]))
            if same is not None:
                same["members"].append(cid)
                continue
            row = {"title": item["title"], "scope": item["scope"], "members": [cid]}
            if kind == "concepts":
                row["topic"] = item["topic"]
            else:
                row |= {"type": item["type"], "aliases": list(item.get("aliases", []))[:10]}
            named[pages.slug(item["title"])] = row
            out.append(row)
        return {"pages": out, "dropped": dropped}

    def publish(record: dict) -> None:
        write_text(
            run_dir / "catalog" / f"{kind}-{pages.slug(group) or 'all'}.json",
            json.dumps(record, ensure_ascii=False),
        )

    def unfaulted(refused: dict | None, objections: list[dict]) -> dict:
        """The list as last refused, without the pages the reviewer faulted: their
        members go back to being pages of their own. A merge nobody objected to is
        kept, where refusing the whole list would lose every one."""
        if refused is None:
            return check({"pages": [], "dropped": []})
        said = " ".join(f"{o.get('quote', '')} {o.get('problem', '')}" for o in objections)
        named = set(re.findall(r"\b[KE]\d+\b", said))
        titles = {pages.slug(str(o.get("quote", ""))) for o in objections}
        kept = [
            page
            for page in refused["pages"]
            if len(page["members"]) > 1
            and not named & set(page["members"])
            and pages.slug(page["title"]) not in titles
        ]
        dropped = [d for d in refused.get("dropped", []) if d.get("id") not in named]
        return check({"pages": kept, "dropped": dropped})

    rows = []
    for item in items:
        row = {
            "id": item["id"],
            "title": item["title"],
            "scope": item["scope"],
            "reports": item["reports"],
            "claims": len(item["claims"]),
        }
        if kind == "concepts":
            row["topic"] = item["topic"]
        else:
            row |= {"type": item["type"], "aliases": item.get("aliases", [])}
        rows.append(row)
    pack: dict[str, Any] = {"kind": kind, "group": group, "candidates": rows}
    if kind == "concepts":
        pack["topics"] = [{"slug": t["slug"], "title": t["title"]} for t in topics(store)]
    return jobs.Job(
        stage="consolidate",
        key=f"consolidate/{kind}/{pages.slug(group) or 'all'}",
        pack=pack,
        check=check,
        publish=publish,
        writer="curate",
        reviewer="review",
        skill="wiki-consolidate",
        review_skill="wiki-consolidate-review",
        fallback=unfaulted,
    )


def build_catalog(runner: Runner, sources: list[str]) -> dict:
    """Merge every report's proposals into one page list and the first routing rows."""
    store, run_dir = runner.store, runner.dir
    found = candidates(run_dir, sources)
    groups: list[tuple[str, str, list[dict]]] = []
    if len(found["concepts"]) <= 220:
        groups.append(("concepts", "all", found["concepts"]))
    else:
        for topic in topics(store):
            members = [c for c in found["concepts"] if c["topic"] == topic["slug"]]
            if members:
                groups.append(("concepts", topic["slug"], members))
    if len(found["entities"]) <= 220:
        groups.append(("entities", "all", found["entities"]))
    else:
        for kind in ENTITY_TYPES:
            members = [e for e in found["entities"] if e["type"] == kind]
            if members:
                groups.append(("entities", kind, members))
    todo = [consolidate_job(store, k, g, items, run_dir) for k, g, items in groups if items]
    outcomes = jobs.run_jobs(runner, todo)
    settled_ = ("accepted", "rejected", "fallback")
    bad = {k: o for k, o in outcomes.items() if o["status"] not in settled_}
    if bad:
        raise Stop(f"the page list was not settled: {bad}")
    by_id = {i["id"]: i for kind in found for i in found[kind]}
    listed_pages: dict[str, dict] = {}
    routed: dict[str, list[dict]] = {s: [] for s in sources}
    claimed: set[str] = set()
    merged = 0
    for kind, group, items in groups:
        path = run_dir / "catalog" / f"{kind}-{pages.slug(group) or 'all'}.json"
        if not path.exists():
            # Refused twice: each candidate stands as its own page rather than be lost.
            record: dict[str, Any] = {
                "pages": [
                    {**{k: v for k, v in i.items() if k != "id"}, "members": [i["id"]]}
                    for i in items
                ]
            }
        else:
            record = json.loads(path.read_text(encoding="utf-8"))
        for page in record["pages"]:
            page_id = f"{kind}/{pages.slug(str(page['title']))}"
            members = [by_id[m] for m in page["members"]]
            entry = listed_pages.setdefault(
                page_id,
                {
                    "kind": kind,
                    "title": page["title"],
                    "description": page["scope"],
                    "aliases": [],
                    "reports": [],
                },
            )
            # Two groups can each name a page the same; it is then one page, under the
            # topic or type of the group that named it first.
            merged += page_id in claimed
            claimed.add(page_id)
            if kind == "concepts":
                entry.setdefault("topic", page["topic"])
            else:
                entry.setdefault("type", page["type"])
                names = {
                    *page.get("aliases", []),
                    *(a for m in members for a in m.get("aliases", [])),
                }
                names |= {m["title"] for m in members}
                entry["aliases"] = sorted({*entry["aliases"], *names} - {page["title"]})
            for member in members:
                entry["reports"] = sorted({*entry["reports"], *member["reports"]})
                for cid in member["claims"]:
                    routed[cid.split(":")[0]].append(
                        {"claim": cid, "page": page_id, "by": "propose"}
                    )
    # A claim sits on at most PAGES_PER_CLAIM pages. Where the proposals put it on more,
    # concepts keep it before entities, and a small page before a large one.
    size: dict[str, int] = {}
    for rows in routed.values():
        for page_id in {(r["claim"], r["page"]) for r in rows}:
            size[page_id[1]] = size.get(page_id[1], 0) + 1
    trimmed = 0
    with runner.lock:
        write_text(
            store.dir / "catalog.json",
            json.dumps({"pages": dict(sorted(listed_pages.items()))}, ensure_ascii=False, indent=1)
            + "\n",
        )
        for source, rows in routed.items():
            by_claim: dict[str, list[str]] = {}
            for row in rows:
                if row["page"] not in by_claim.setdefault(row["claim"], []):
                    by_claim[row["claim"]].append(row["page"])
            keep = []
            for cid, targets in sorted(by_claim.items()):
                targets.sort(key=lambda p: (not p.startswith("concepts/"), size[p], p))
                trimmed += max(0, len(targets) - PAGES_PER_CLAIM)
                keep += [
                    {"claim": cid, "page": p, "by": "propose"} for p in targets[:PAGES_PER_CLAIM]
                ]
            write_jsonl(store.dir / "routes" / f"{source}.jsonl", keep)
            (store.dir / "routes" / f"{source}.done").unlink(missing_ok=True)
    return {
        "pages": len(listed_pages),
        "candidates": len(by_id),
        "same_name_merged": merged,
        "placements_trimmed": trimmed,
    }


def route_job(store: Store, source: str, listed_pages: dict[str, dict]) -> jobs.Job:
    claims = [c for c in active(store, source) if c["kind"] != "figure"]
    known = {c["id"] for c in claims}
    have = routes(store, source)
    alias = {f"P{n + 1}": page_id for n, page_id in enumerate(sorted(listed_pages))}

    def check(record: dict) -> dict:
        problems: list[str] = []
        count: dict[str, int] = {}
        for row in have:
            count[row["claim"]] = count.get(row["claim"], 0) + 1
        placed = {(r["claim"], r["page"]) for r in have}
        out = []
        wanted = record.get("routes")
        if not isinstance(wanted, list):
            raise Rejected("the record needs a routes list", ['use {"routes": [...]}'])
        for item in wanted:
            if not isinstance(item, dict):
                problems.append("each route is an object with page and claims")
                continue
            tag = str(item.get("page", "")).strip()
            page_id = alias.get(tag, tag)
            if page_id not in listed_pages:
                problems.append(f"{tag!r} is not a page of the list")
                continue
            for cid in claim_ids(source, item.get("claims"), known, problems, f"page {tag}"):
                if (cid, page_id) in placed:
                    continue
                count[cid] = count.get(cid, 0) + 1
                if count[cid] > PAGES_PER_CLAIM:
                    problems.append(
                        f"{short(cid)} would be on more than {PAGES_PER_CLAIM} pages; keep the "
                        "pages it is direct evidence for"
                    )
                placed.add((cid, page_id))
                out.append({"claim": cid, "page": page_id, "by": "route"})
        if problems:
            raise Rejected("the routes fail their checks", problems[:20])
        return {"routes": out}

    def publish(record: dict) -> None:
        keep = {(r["claim"], r["page"]): r for r in [*have, *record["routes"]]}
        write_jsonl(store.dir / "routes" / f"{source}.jsonl", [keep[k] for k in sorted(keep)])
        write_text(store.dir / "routes" / f"{source}.done", "")

    fed: dict[str, list[str]] = {}
    for row in have:
        fed.setdefault(row["page"], []).append(short(row["claim"]))
    lines = []
    for tag, page_id in alias.items():
        page = listed_pages[page_id]
        names = f" (also: {', '.join(page['aliases'][:4])})" if page.get("aliases") else ""
        mark = f" | already holds: {', '.join(fed[page_id])}" if page_id in fed else ""
        lines.append(
            f"{tag} {page['kind'][:-1]} | {page['title']}{names} | {page['description']}{mark}"
        )
    pack = {
        "report": source,
        "title": report_title(store, source),
        "pages": "\n".join(lines),
        "claims": listed(claims),
    }
    return jobs.Job(
        stage="route",
        key=f"route/{source}",
        pack=pack,
        check=check,
        publish=publish,
        writer="curate",
        reviewer="",
        skill="wiki-route",
    )


# Step 5: pages


# Headings under which a report gives its own account of what matters.
MAIN = re.compile(
    r"summary|abstract|key (findings|results)|main (findings|results)|conclusions?|highlights",
    re.I,
)


def main_spans(text: str) -> list[tuple[int, int]]:
    """The sections of a report whose heading says they hold its main points, each
    with its subsections."""
    heads = [(m.start(), len(m.group(1)), m.group(2)) for m in HEADING.finditer(text)]
    out = []
    for n, (start, level, title) in enumerate(heads):
        if level > 1 and MAIN.search(title):
            end = next((s for s, lv, _ in heads[n + 1 :] if lv <= level), len(text))
            out.append((start, end))
    return out


def spread(rows: list[dict], room: int) -> list[dict]:
    """At most ``room`` rows, taken evenly along the report, not from its start."""
    if len(rows) <= room:
        return rows
    return [rows[(n * len(rows)) // room] for n in range(room)] if room > 0 else []


def summary_claims(claims: list[dict]) -> list[dict]:
    """A report's claims in the order its summary takes them: the report's own. Figures
    are placed by their own stage."""
    return sorted((c for c in claims if c["kind"] != "figure"), key=lambda c: c["start"])


# Headings a part of a long summary may not take: the page's own sections, the lead's
# anchor, and the sections the gate does not read as evidence or a record stage adds.
RESERVED_HEADINGS = (
    pages.LEAD,
    "key-findings",
    "caveats-and-open-work",
    "slots-into",
    "data-and-methods",
    "figures",
    *(pages.slug(h) for h in FORWARD),
)


def report_parts(claims: list[dict], text: str) -> list[tuple[str, list[dict]]]:
    """A long report's claims, in its order, as parts of at most ``PART_CLAIMS``, each
    named after the report sections it covers. The last part may be up to a fifth
    longer: a tail shorter than that joins it.

    A part ends where the report starts a new section once the part is half full, at a
    new subsection once it is nearly full, and at the limit otherwise.
    """
    heads = [
        (m.start(), len(m.group(1)), re.sub(r"[*`#]|^\s*[\d.]+\s+", "", m.group(2)).strip())
        for m in HEADING.finditer(text)
    ]
    top = min((level for _, level, _ in heads if level > 1), default=2)

    def place(at: int) -> tuple[str, str]:
        section = sub = ""
        for start, level, title in heads:
            if start > at:
                break
            if level == top:
                section, sub = title, ""
            elif level == top + 1:
                sub = title
        return section, sub

    parts: list[list[tuple[dict, tuple[str, str]]]] = []
    current: list[tuple[dict, tuple[str, str]]] = []
    for claim in claims:
        where = place(claim["start"])
        if current:
            before = current[-1][1]
            if (
                len(current) >= PART_CLAIMS
                or (where[0] != before[0] and len(current) >= PART_CLAIMS // 2)
                or (where != before and len(current) >= PART_CLAIMS * 4 // 5)
            ):
                parts.append(current)
                current = []
        current.append((claim, where))
    if current:
        parts.append(current)
    if len(parts) > 1 and len(parts[-1]) < PART_CLAIMS // 5:
        tail = parts.pop()
        parts[-1] += tail
    out: list[tuple[str, list[dict]]] = []
    taken: set[str] = set()
    for part in parts:
        sections = list(dict.fromkeys(where[0] for _, where in part if where[0]))
        subs = Counter(where[1] for _, where in part if where[1])
        title = "; ".join(sections[:3]) or "Opening of the report"
        if len(sections) == 1 and subs:
            # Named after the subsection most of its claims come from.
            title = f"{sections[0]}: {subs.most_common(1)[0][0]}"
        if len(title) > TITLE:
            # A heading ends at a word, and says it was cut.
            title = title[:TITLE].rsplit(" ", 1)[0].rstrip(" ;:,([—-") + " …"
        if pages.slug(title) in RESERVED_HEADINGS or not pages.slug(title):
            title = f"Report section: {title or 'untitled'}"
        base, n = title, 2
        while pages.slug(title) in taken:
            title, n = f"{base} ({n})", n + 1
        taken.add(pages.slug(title))
        out.append((title, [claim for claim, _ in part]))
    return out


def page_claims(store: Store, sources: list[str]) -> dict[str, list[dict]]:
    """The claims each page is written from: every report's claims for its summary, the
    routing table for the rest."""
    out: dict[str, list[dict]] = {}
    for source in sources:
        claims = {c["id"]: c for c in active(store, source)}
        summary = f"summaries/{source}" if source in DIGESTS else f"summaries/{source}__REPORT"
        out[summary] = summary_claims(list(claims.values()))
        for row in routes(store, source):
            if row["claim"] in claims:
                out.setdefault(row["page"], []).append(claims[row["claim"]])
    return out


def page_meta(store: Store, page_id: str, listed_pages: dict[str, dict]) -> dict:
    kind, _, name = page_id.partition("/")
    if kind != "summaries":
        return {"kind": kind, **listed_pages[page_id]}
    source = name.removesuffix("__REPORT")
    title = report_title(store, source)
    return {
        "kind": kind,
        "title": title,
        "type": "Summary",
        "description": f"Summary of the project {title}.",
        "source": source,
    }


def front(page_id: str, meta: dict, cited: list[str]) -> str:
    kind = meta["kind"]
    fields: dict[str, Any] = {
        "type": "Concept" if kind == "concepts" else meta.get("type", "Other"),
        "description": meta["description"],
    }
    if kind == "summaries":
        source = meta["source"]
        suffix = "" if source in DIGESTS else "__REPORT"
        fields |= {"doc_type": "short", "full_text": f"sources/{source}{suffix}.md"}
    else:
        fields["sources"] = [
            f"summaries/{s}.md" if s in DIGESTS else f"summaries/{s}__REPORT.md"
            for s in sorted(cited)
        ]
        if meta.get("aliases"):
            fields["aliases"] = meta["aliases"]
    body = "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fields.items())
    return f"---\n{body}---\n"


def brief_page(
    page_id: str,
    meta: dict,
    task: dict,
    new: list[str],
    draft: str,
    links: dict[str, str],
    objections: list[dict] | None,
    refused: str,
) -> str:
    claims = task["claims"]
    terms = task.get("glossary", {})
    lines = [
        f"Page: {page_id}",
        f"Kind: {meta['kind'][:-1] if meta['kind'] != 'summaries' else 'summary'}",
        f"Title: {meta['title']}",
        f"What the page covers: {meta['description']}",
    ]
    if meta.get("aliases"):
        lines.append(f"Also known as: {', '.join(meta['aliases'])}")
    if task["required"]:
        lines.append(f"Required sections: {', '.join('## ' + h for h in task['required'])}")
    if task.get("note"):
        lines += ["", task["note"]]
    lines += ["", "CLAIMS (tag | report | kind | claim | verbatim quote)"]
    for tag in new:
        c = claims[tag]
        lines.append(f"{tag} | {c['source']} | {c['kind']} | {c['text']} | QUOTE: {c['quote']}")
    if draft:
        lines += [
            "",
            "The page below was accepted from earlier claims. Integrate the claims above into "
            "it: add to the sections they belong in, add a section when they open a new line "
            "of evidence, and correct the lead if they change the overall picture. Keep every "
            "statement and tag the page already has. Submit the whole page.",
            "",
            "ACCEPTED PAGE",
            draft,
        ]
    if terms:
        lines += ["", "GLOSSARY (how the reports expand these abbreviations; expand no other)"]
        lines += [f"{abbr} = {long}" for abbr, long in terms.items()]
    if links:
        lines += ["", "PAGES YOU MAY LINK (use [[id]] or [[id|words]]; link no other page)"]
        lines += [f"[[{pid}]] {title}" for pid, title in links.items()]
    if objections:
        lines += [
            "",
            "A reviewer returned your page with the objections below. Change only what they "
            "require and submit the whole page again.",
            *(f"- {o.get('quote', '')!r}: {o['problem']}" for o in objections),
            "",
            "YOUR PAGE AS REVIEWED",
            refused,
        ]
    return "\n".join(lines)


def brief_page_review(
    page_id: str,
    meta: dict,
    candidate: dict,
    task: dict,
    new: list[str],
    earlier: list[dict] | None,
) -> str:
    claims = task["claims"]
    lines = [
        f"Page under review: {page_id} ({meta['title']})",
        f"sha of the page: {candidate['sha']}",
        f"Accepted description of the page: {meta['description']}",
    ]
    if meta.get("aliases"):
        lines.append(f"Accepted other names: {', '.join(meta['aliases'])}")
    if task.get("glossary"):
        lines += ["", "GLOSSARY (expansions the reports give; accepted)"]
        lines += [f"{abbr} = {long}" for abbr, long in task["glossary"].items()]
    lines += ["", "CLAIMS the writer was given (tag | report | kind | claim | verbatim quote)"]
    for tag in new:
        c = claims[tag]
        lines.append(f"{tag} | {c['source']} | {c['kind']} | {c['text']} | QUOTE: {c['quote']}")
    older = [t for t in candidate["cited"] if t not in new]
    if older:
        lines += [
            "",
            "Statements that cite only these tags were accepted in an earlier pass and are "
            f"not under review: {', '.join(older)}",
        ]
    if candidate["declined"]:
        lines += ["", "Claims the writer declined to use:"]
        lines += [f"- {d.get('claim')}: {d.get('reason')}" for d in candidate["declined"]]
    lines += ["", "PAGE", candidate["body"]]
    if earlier:
        lines += ["", "Your earlier objections; check only whether each is resolved:"]
        lines += [f"- {o.get('quote', '')!r}: {o['problem']}" for o in earlier]
    return "\n".join(lines)


TAG_AT_END = re.compile(CLAIM_TAG.pattern + r"[.!?]?\s*$")


def strike(body: str, quotes: list[str]) -> str | None:
    """The page without the statements a reviewer still objects to, or None when a
    quoted passage cannot be tied to whole statements.

    A statement is a sentence with the tags that close it, a list item's sentence, or a
    table row. Removing it is the bounded way out of a disagreement two rounds did not
    settle: what stays is text the reviewer did not fault.
    """
    faulted: list[tuple[int, int]] = []
    for quote in quotes:
        at = body.find(quote)
        if not quote or at < 0:
            return None
        while at >= 0:
            faulted.append((at, at + len(quote)))
            at = body.find(quote, at + 1)
    out, pos = [], 0
    for line in body.splitlines(keepends=True):
        text = line.rstrip("\n")
        spans = statements(text)
        hit = [(a, b) for a, b in faulted if a < pos + len(text) and b > pos]
        if not hit:
            out.append(text)
        elif not spans:
            # The passage runs through a heading; there is no statement to remove.
            return None
        else:
            # A sentence can be cut in two at an abbreviation; its pieces run up to the
            # one that carries the closing tag, and they go or stay together.
            groups: list[tuple[int, int]] = []
            start = spans[0][0]
            for a, b in spans:
                if TAG_AT_END.search(text[a:b]) or (a, b) == spans[-1]:
                    groups.append((start, b))
                    start = b
            kept = [
                text[a:b].strip()
                for a, b in groups
                if not any(x < pos + b and y > pos + a for x, y in hit)
            ]
            if kept:
                out.append(text[: spans[0][0]] + " ".join(kept))
        pos += len(line)
    result = "\n".join(out)
    # A section left with nothing under its heading goes too.
    result = re.sub(r"^## [^\n]+\n+(?=## |\Z)", "", result.strip() + "\n", flags=re.M)
    result = re.sub(r"\n{3,}", "\n\n", result).strip()
    return None if any(q in result for q in quotes) else result


def journal_of(runner: Runner, page_id: str, n: int) -> Path:
    name = re.sub(r"[^a-z0-9]+", "-", page_id)[-70:]
    return runner.dir / "journal" / f"{name}-p{n}.json"


def write_pass(
    runner: Runner,
    page_id: str,
    meta: dict,
    task: dict,
    new: list[str],
    draft: str,
    links: dict[str, str],
    n: int,
) -> dict:
    """One pass over one page: write, review, at most ``rounds`` times, then strike
    whatever the reviewer still faults. Returns the accepted draft or why there is none.

    What the reviewer said survives a stop in the pass's journal, so a resumed run
    neither asks for a first opinion twice nor loses a refusal.
    """
    store, config = runner.store, runner.config
    name = re.sub(r"[^a-z0-9]+", "-", page_id)[-70:]
    journal = journal_of(runner, page_id, n)
    saved = json.loads(journal.read_text(encoding="utf-8")) if journal.exists() else {}
    objections: list[dict] | None = saved.get("objections")
    refused: str = saved.get("refused", "")
    candidate: dict | None = saved.get("candidate")
    accepted_before = set(statement_texts(draft))
    for round_ in range(saved.get("round", 0) + 1, config.rounds + 1):
        brief = brief_page(page_id, meta, task, new, draft, links, objections, refused)
        for again in ("", "b"):
            session, run = runner.dispatch(
                f"page-{name}-p{n}-write{round_}{again}",
                "write",
                {**task, "new": new},
                brief,
                tools="page",
                skill="wiki-page",
            )
            if runner.halted:
                return {"status": "budget", "detail": runner.halted}
            if session.used_calls or not run.ok or not run.text.strip():
                break
            # The writer answered with the page as text and called no tool. Asked once
            # more with its own text, it has only to submit it.
            brief = f"{brief}\n\n{UNSUBMITTED}\n{run.text.strip()}"
        candidate = session.candidates.get(page_id)
        if candidate is None and session.rejections.get(page_id, 0) >= REJECTIONS:
            # Every draft failed the checks. That is an answer, not an outage: asking
            # again on resume would buy the same refusals.
            return {"status": "rejected", "detail": ["no draft passed the page checks"]}
        if candidate is None:
            return {"status": "failed", "detail": run.error or "no page was submitted"}
        if candidate["body"] == refused:
            break
        # A statement the writer changed is reviewed with the claims it cites, also
        # when those were accepted in an earlier pass under other words.
        changed = {
            tag
            for text in statement_texts(candidate["body"])
            if text not in accepted_before
            for tag in tags_in(text)
        }
        under_review = [t for t in task["claims"] if t in changed or t in new]
        reviewed, review_run = runner.dispatch(
            f"page-{name}-p{n}-review{round_}",
            "review",
            {
                "section": page_id,
                "sha": candidate["sha"],
                "candidate": candidate["body"],
                "quoted": True,
            },
            brief_page_review(page_id, meta, candidate, task, under_review, objections),
            tools="verdict",
            skill="wiki-page-review",
        )
        if runner.halted:
            return {"status": "budget", "detail": runner.halted}
        verdict = reviewed.reviews.get(page_id)
        if verdict is None:
            return {"status": "unreviewed", "detail": review_run.error or "no verdict"}
        if verdict["verdict"] == "accept":
            return {"status": "accepted", "rounds": round_, "candidate": candidate}
        objections, refused = verdict["objections"], candidate["body"]
        write_text(
            journal,
            json.dumps(
                {
                    "round": round_,
                    "objections": objections,
                    "refused": refused,
                    "candidate": candidate,
                },
                ensure_ascii=False,
            ),
        )
    if candidate is None or not objections:
        return {"status": "failed", "detail": "no page was reviewed"}
    faults = [o["problem"] for o in objections]
    quotes = [str(o.get("quote", "")).strip() for o in objections]
    struck = strike(candidate["body"], quotes) if all(quotes) else None
    if not struck:
        return {"status": "rejected", "detail": faults}
    stock = ""
    if struck.lstrip().startswith("## "):
        # The reviewer faulted every sentence of the lead. What the page is about is
        # known without a claim, and a page with no lead is refused.
        stock = f"{meta['description'].strip().rstrip('.')}."
        struck = f"{stock}\n\n{struck.lstrip()}"
    gone = [t for t in candidate["cited"] if t not in tags_in(struck)]
    declined = [
        *candidate["declined"],
        *({"claim": t, "reason": "its statement was removed after review"} for t in gone),
    ]
    relaxed = {**task, "kept": [t for t in task["kept"] if t not in gone], "stock": stock}
    fixed, problems = page_candidate(store, relaxed, struck, declined)
    fixed.pop("left", None)
    if problems:
        return {"status": "rejected", "detail": faults + problems[:5]}
    return {"status": "accepted", "rounds": config.rounds, "candidate": fixed, "struck": faults}


def publish_page(runner: Runner, page_id: str, meta: dict, candidate: dict) -> None:
    """Write the page, its sidecar and its tagged draft. Safe to run again."""
    store = runner.store
    cited = sorted({cid.split(":")[0] for ids in candidate["sections"].values() for cid in ids})
    text = f"{front(page_id, meta, cited)}# {meta['title']}\n\n{candidate['rendered'].strip()}\n"
    stamp = {
        "run": runner.id,
        "at": date.today().isoformat(),
        "writer": str(runner.config.roles["write"]),
        "reviewer": str(runner.config.roles["review"]),
    }
    write_text(store.page_path(page_id), text)
    store.write_sidecar(
        page_id,
        {
            "sections": {
                anchor: {"claims": dict.fromkeys(sorted(ids), "edit"), "stamp": stamp}
                for anchor, ids in candidate["sections"].items()
            }
        },
    )
    write_text(runner.dir / "drafts" / f"{page_id}.md", candidate["body"])


def write_page(
    runner: Runner,
    page_id: str,
    meta: dict,
    rows: list[dict],
    links: dict[str, str],
    terms: dict[str, str],
) -> dict:
    """Every pass of one page, in order. A pass that is refused leaves the page as the
    pass before it left it. A pass that ends without an answer stops the page there, so
    the next run resumes from the same accepted text."""
    kind = meta["kind"]
    if kind == "summaries" and len(rows) > SECTIONED:
        return write_sectioned(runner, page_id, meta, rows, links, terms)
    limit = PASS * MAX_PASSES[kind]
    tags = {f"C{n + 1}": c for n, c in enumerate(rows[:limit])}
    task_claims = {
        t: {k: c[k] for k in ("id", "kind", "text", "quote")} | {"source": c["id"].split(":")[0]}
        for t, c in tags.items()
    }
    order = list(tags)
    passes = [order[i : i + PASS] for i in range(0, len(order), PASS)]
    outcome: dict[str, Any] = {"page": page_id, "claims": len(rows), "passes": [], "used": 0}
    outcome["unplaced"] = [c["id"] for c in rows[limit:]]
    draft_path = runner.dir / "drafts" / f"{page_id}.md"
    for n, new in enumerate(passes):
        key = f"page-{page_id}-p{n}"
        journal = journal_of(runner, page_id, n)

        def make(n: int = n, new: list[str] = new, journal: Path = journal) -> dict:
            saved = json.loads(journal.read_text(encoding="utf-8")) if journal.exists() else {}
            if "accepted" in saved:
                # The run died between the reviewer's accept and the end of publish.
                with runner.lock:
                    publish_page(runner, page_id, meta, saved["accepted"])
                return saved["result"]
            draft = draft_path.read_text(encoding="utf-8") if n and draft_path.exists() else ""
            kept = [t for t in tags_in(draft) if t in task_claims]
            task = {
                "page": page_id,
                "claims": {t: task_claims[t] for t in order if t in {*kept, *new}},
                "kept": kept,
                "links": sorted(links),
                "glossary": (words := expansions(terms, [tags[t] for t in {*kept, *new}])),
                "describes": " ".join(
                    [meta["title"], meta["description"], *meta.get("aliases", []), *words.values()]
                ),
                # Owed on every pass, so any accepted pass leaves a complete page.
                "required": REQUIRED.get(kind, []),
            }
            result = write_pass(runner, page_id, meta, task, new, draft, links, n)
            if result["status"] != "accepted":
                return result
            candidate = result.pop("candidate")
            result |= {
                "used": len(candidate["cited"]),
                "declined": len(candidate["declined"]),
                # Claims the writer never accounted for; the page was taken without them.
                "skipped": [
                    task_claims[d["claim"]]["id"]
                    for d in candidate["declined"]
                    if d.get("reason") == NOT_PLACED and d.get("claim") in task_claims
                ],
            }
            write_text(
                journal,
                json.dumps({"accepted": candidate, "result": result}, ensure_ascii=False),
            )
            with runner.lock:
                publish_page(runner, page_id, meta, candidate)
            return result

        # A pass on record from an earlier run says nothing about this run's health.
        fresh = key not in runner.state["steps"] and not journal.exists()
        result = runner.step(key, make)
        outcome["passes"].append(result["status"])
        if fresh:
            outcome.setdefault("fresh", []).append(result["status"])
        if result["status"] in ("budget", "failed", "unreviewed"):
            outcome["status"] = "budget" if result["status"] == "budget" else "failed"
            return outcome
        # Recorded, so the journal has done its work.
        journal.unlink(missing_ok=True)
        if result["status"] == "accepted":
            outcome["used"] = result.get("used", outcome["used"])
            outcome["struck"] = outcome.get("struck", 0) + len(result.get("struck", []))
            outcome["unplaced"] += result.get("skipped", [])
        else:
            outcome["unplaced"] += [task_claims[t]["id"] for t in new]
    outcome["status"] = "accepted" if "accepted" in outcome["passes"] else "rejected"
    return outcome


OVERVIEW_NOTE = (
    "This report is long, so its summary is written in parts. You write the opening of "
    "the page: the lead, ## Key Findings with the main results of the whole report by "
    "theme, ## Caveats and Open Work with the limits that bear on those results, and "
    "## Slots Into if concept pages are listed. Other sessions write one section for each "
    "part of the report, under these headings, after yours: {titles}. The claims below "
    "are a selection from the report. Do not say how many items a list, table or set has "
    "unless a claim states the number."
)
PART_NOTE = (
    "This report is long, so its summary is written in parts, and you write ONE SECTION "
    "of it: the part of the report under {where}. The page's lead and its Key Findings "
    "are written elsewhere. Kind of page: summary part. Use no ## heading and write no "
    "lead for the whole report; the section is placed under the heading '## {title}'. "
    "The claims below are every claim of this part of the report."
)
UNSUBMITTED = (
    "You answered with the page as text and did not call write_page, so nothing was "
    "submitted. Submit it now with write_page(body, declined): a reply in text is not "
    "read. Change the text only where a rule requires it.\n\nYOUR UNSUBMITTED REPLY"
)


def write_sectioned(
    runner: Runner,
    page_id: str,
    meta: dict,
    rows: list[dict],
    links: dict[str, str],
    terms: dict[str, str],
) -> dict:
    """The summary of a long report: an overview from the report's own summary sections
    and one section for each part of the report, each written and reviewed on its own
    from all the claims of its part, then put together in the report's order.

    No session rewrites the page, so a part costs the same wherever it sits, the parts
    are written side by side, and one that is refused leaves the others standing.
    """
    store = runner.store
    source = page_id.partition("/")[2].removesuffix("__REPORT")
    text = store.source_text(source)
    parts = report_parts(rows, text)
    spans = main_spans(text)
    said = [c for c in rows if any(a <= c["start"] < b for a, b in spans)]
    groups = [("", spread(said or rows, OVERVIEW)), *parts]
    tags: dict[str, dict] = {}
    plan: list[tuple[int, str, list[str]]] = []
    for n, (title, group) in enumerate(groups):
        own = []
        for claim in group:
            own.append(f"C{len(tags) + 1}")
            tags[own[-1]] = claim
        plan.append((n if not n else PART_STEPS + n - 1, title, own))
    task_claims = {
        t: {k: c[k] for k in ("id", "kind", "text", "quote")} | {"source": source}
        for t, c in tags.items()
    }
    titles = [title for title, _ in parts]

    def task_of(own: list[str], title: str) -> dict:
        words = expansions(terms, [tags[t] for t in own])
        note = (
            PART_NOTE.format(title=title, where=title)
            if title
            else OVERVIEW_NOTE.format(titles="; ".join(titles))
        )
        return {
            "page": page_id,
            "claims": {t: task_claims[t] for t in own},
            "kept": [],
            "links": sorted(links),
            "glossary": words,
            "describes": " ".join([meta["title"], meta["description"], title, *words.values()]),
            "required": [] if title else REQUIRED["summaries"],
            "part": bool(title),
            "note": note,
        }

    def written(item: tuple[int, str, list[str]]) -> tuple[dict, bool]:
        n, title, own = item
        key = f"page-{page_id}-p{n}"
        journal = journal_of(runner, page_id, n)
        # Which claim each tag of this step stands for. The parts are cut again on
        # every run, and a text written for other claims would be linked to these.
        of = sha256(json.dumps([[t, tags[t]["id"]] for t in own]))[:16]
        with runner.lock:
            kept = runner.state["steps"].get(key)
            if isinstance(kept, dict) and kept.get("of", of) != of:
                del runner.state["steps"][key]
                journal.unlink(missing_ok=True)
                runner.save()

        def make() -> dict:
            result = write_pass(runner, page_id, meta, task_of(own, title), own, "", links, n)
            if result["status"] != "accepted":
                return result | {"of": of}
            candidate = result.pop("candidate")
            # The part itself is the record: the page is put together from the parts.
            return result | {
                "of": of,
                "body": candidate["body"],
                "declined_claims": candidate["declined"],
            }

        fresh = key not in runner.state["steps"] and not journal.exists()
        result = runner.step(key, make)
        if result["status"] in ("accepted", "rejected"):
            journal.unlink(missing_ok=True)
        return result, fresh

    results = each(runner, plan, written)
    statuses = [r["status"] for r, _ in results]
    outcome: dict[str, Any] = {
        "page": page_id,
        "claims": len(rows),
        "passes": statuses,
        "used": 0,
        "unplaced": [],
        "fresh": [r["status"] for r, fresh in results if fresh],
    }
    if any(s in ("budget", "failed", "unreviewed") for s in statuses):
        outcome["status"] = "budget" if "budget" in statuses else "failed"
        return outcome
    overview, *sections = (r for r, _ in results)
    opening = overview["body"].strip() if overview["status"] == "accepted" else ""
    # A refused overview leaves the description as the lead; the parts still stand.
    stock = "" if opening else f"{meta['description'].strip().rstrip('.')}."
    opening = opening or stock
    # A part named like a section the overview wrote would share that section's record.
    taken = {pages.slug(h) for h in re.findall(r"^##[ \t]+(.+)$", opening, re.M)}
    blocks = []
    for (_, title, _), r in zip(plan[1:], sections, strict=True):
        if r["status"] != "accepted":
            continue
        if pages.slug(title) in taken:
            title = f"Report section: {title}"
        taken.add(pages.slug(title))
        blocks.append(f"## {title}\n\n{r['body'].strip()}")
    cut = min(
        (
            at
            for h in ("Caveats and Open Work", "Slots Into")
            if (at := opening.find(f"\n## {h}")) >= 0
        ),
        default=len(opening),
    )
    body = "\n\n".join([opening[:cut].strip(), *blocks, opening[cut:].strip()]).strip()
    done = [(own, r) for (_, _, own), r in zip(plan, (r for r, _ in results), strict=True)]
    held = [t for own, r in done if r["status"] == "accepted" for t in own]
    declined = [d for _, r in done if r["status"] == "accepted" for d in r["declined_claims"]]
    task = {
        "page": page_id,
        "claims": {t: task_claims[t] for t in held},
        "kept": [],
        "links": sorted(links),
        "describes": " ".join(
            [meta["title"], meta["description"], *expansions(terms, rows).values()]
        ),
        "required": REQUIRED["summaries"] if overview["status"] == "accepted" else [],
        "stock": stock,
    }
    candidate, problems = page_candidate(store, task, body, declined)
    candidate.pop("left", None)
    if problems:
        # A step that passed alone and fails here was accepted under an older check.
        # Recorded as refused, it is what --retry-rejected writes again.
        for (n, title, own), r in zip(plan, (r for r, _ in results), strict=True):
            if r["status"] != "accepted":
                continue
            alone = page_candidate(store, task_of(own, title), r["body"], r["declined_claims"])[1]
            if alone:
                with runner.lock:
                    runner.state["steps"][f"page-{page_id}-p{n}"] = {
                        "status": "rejected",
                        "detail": alone[:5],
                        **({"of": r["of"]} if "of" in r else {}),
                    }
                    runner.save()
    # With every part refused the overview still stands as a short summary.
    if problems or not (blocks or overview["status"] == "accepted"):
        outcome |= {"status": "rejected", "detail": problems[:8] or ["no part was accepted"]}
        outcome["unplaced"] = [c["id"] for c in rows]
        return outcome
    with runner.lock:
        publish_page(runner, page_id, meta, candidate)
    cited = {task_claims[t]["id"] for t in candidate["cited"]}
    outcome |= {
        "status": "accepted",
        "used": len(cited),
        "struck": sum(len(r.get("struck", [])) for _, r in done),
        "unplaced": sorted({c["id"] for c in rows} - cited),
    }
    return outcome


def link_targets(
    page_id: str, by_page: dict[str, list[dict]], listed_pages: dict[str, dict]
) -> dict[str, str]:
    """Pages this one may link: those that share its claims or its reports, nearest first."""
    mine = {c["id"] for c in by_page[page_id]}
    reports = {c["id"].split(":")[0] for c in by_page[page_id]}
    scored = []
    for other, rows in by_page.items():
        if other == page_id or other.startswith("summaries/"):
            continue
        shared = len(mine & {c["id"] for c in rows})
        near = len(reports & {c["id"].split(":")[0] for c in rows})
        if shared or (near and page_id.startswith("summaries/")):
            scored.append((-shared, -near, other))
    out = {other: listed_pages[other]["title"] for _, _, other in sorted(scored)[:30]}
    if not page_id.startswith("summaries/"):
        for source in sorted(reports):
            name = f"summaries/{source}" if source in DIGESTS else f"summaries/{source}__REPORT"
            out[name] = f"summary of {source}"
    return out


def unlink_missing(store: Store, written: list[str]) -> int:
    """Turn links to pages that were never written into plain words."""
    have = set(store.page_ids())
    changed = 0
    for page_id in written:
        path = store.page_path(page_id)
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")

        def fix(m: re.Match) -> str:
            target = m.group(1).strip().lstrip("/").removesuffix(".md")
            if target in have:
                return m.group(0)
            shown = m.group(0)[2:-2].split("|", 1)
            return shown[1] if len(shown) > 1 else target.split("/")[-1].replace("-", " ")

        fixed = pages.WIKILINK.sub(fix, text)
        if fixed != text:
            write_text(path, fixed)
            changed += 1
    return changed


def write_topic_state(store: Store, listed_pages: dict[str, dict]) -> None:
    """Which topic each written concept sits in, in the file the hub stage reads."""
    path = store.root / "state" / "curator-topics.json"
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    groups = []
    for topic in topics(store):
        members = sorted(
            page_id.split("/", 1)[1]
            for page_id, page in listed_pages.items()
            if page["kind"] == "concepts"
            and page.get("topic") == topic["slug"]
            and store.page_path(page_id).exists()
        )
        groups.append({"title": topic["title"], "concepts": members})
    state |= {"groups": groups, "version": state.get("version", 1)}
    state["concepts"] = {
        f"wiki/{page_id}.md": sha256(store.page_path(page_id).read_text(encoding="utf-8"))
        for page_id, page in sorted(listed_pages.items())
        if page["kind"] == "concepts" and store.page_path(page_id).exists()
    }
    state.setdefault("reason", "Membership was set when the wiki was compiled.")
    write_text(path, json.dumps(state, indent=2, sort_keys=True))


# The workflow


def pin_of(store: Store, sources: list[str]) -> str:
    """The reports a compile reads and how it cuts them. Claim ids follow the cut, and
    the page list and routes are keyed by claim id, so a run cannot resume under
    another one."""
    reports = "\n".join(f"{s}:{sha256(store.source_text(s))}" for s in sources)
    return sha256(f"part={PART}\n{reports}")


def compile_corpus(
    root: Path,
    config: Config,
    sources: list[str] | None = None,
    launch: Launch | None = None,
    records: bool = True,
    retry: bool = False,
    write: bool = True,
    route: bool = True,
) -> dict:
    """Build every page and record from the reports in ``corpus/``.

    ``write=False`` stops when the reports are read into claims, and ``records=False``
    when the pages are written; the same command without the flag goes on from there.

    ``retry`` writes again the page passes an earlier attempt of this run had refused,
    for use after the skill or the check that refused them has changed.
    """
    store = Store(root)
    chosen = sorted(sources or store.corpus_sources())
    missing = [s for s in chosen if not store.source_path(s).exists()]
    if missing:
        raise Stop(f"no report for: {', '.join(missing)}")
    config.check()
    pin = pin_of(store, chosen)
    for path in sorted((root / ".agentic" / "runs").glob("*-compile-corpus/run.json")):
        state = json.loads(path.read_text(encoding="utf-8"))
        refused = any(
            PASS_STEP.match(k) and isinstance(v, dict) and v.get("status") == "rejected"
            for k, v in state.get("steps", {}).items()
        )
        if state.get("pin") == pin and state.get("status") == "done" and retry and refused:
            # Reopened: its pages are rewritten, and the records that rest on them are
            # the ones on file.
            write_text(path, json.dumps(state | {"status": "stopped"}, ensure_ascii=False))
            continue
        if state.get("pin") == pin and state.get("status") == "done":
            raise Stop(
                f"these reports were compiled in run {state['run']}; a report that changes "
                "later is read with `beril-wiki ingest` or `revise`"
            )
        if state.get("pin") != pin and state.get("status") != "done":
            raise Stop(
                f"run {state['run']} is an unfinished compile of other reports or other "
                "revisions of them. Its claims, page list and pages are in this checkout; "
                "finish it with the same reports, or start from an empty wiki"
            )
    if Runner.open_run(root, "compile", "corpus", pin) is None:
        held = [
            name
            for name, found in (
                ("knowledge/claims", store.claim_sources()),
                ("knowledge/catalog.json", (store.dir / "catalog.json").exists()),
                *(
                    (f"wiki/{kind}", any((root / "wiki" / kind).glob("*.md")))
                    for kind in ("concepts", "entities", "summaries")
                ),
            )
            if found
        ]
        if held:
            raise Stop(
                "compile builds a wiki from nothing, and this checkout already holds "
                f"{', '.join(held)}. Read a new report with `beril-wiki ingest`, or compile "
                "in an empty checkout"
            )
    try:
        with checkout_lock(root):
            runner = Runner(root, config, "compile", "corpus", launch, pin)
            if retry:
                forget_refused_pages(runner)
            try:
                return _compile(runner, chosen, records, write, route)
            except Stop as exc:
                return runner.finish("stopped", reason=str(exc))
    except Busy as exc:
        raise Stop(str(exc)) from None


PASS_STEP = re.compile(r"^page-(.+)-p(\d+)$")


def forget_refused_pages(runner: Runner) -> int:
    """Drop the record of each page from its first refused pass on, so those passes
    are written again. A later pass built on the page as the refused pass left it;
    kept, it would stand while the rewritten earlier pass replaced the page under it.
    """
    steps = runner.state["steps"]
    first: dict[str, int] = {}
    for key, value in steps.items():
        match = PASS_STEP.match(key)
        if match and isinstance(value, dict) and value.get("status") == "rejected":
            page, n = match.group(1), int(match.group(2))
            first[page] = min(n, first.get(page, n))
    dropped = 0
    for key in list(steps):
        match = PASS_STEP.match(key)
        if not match or match.group(1) not in first:
            continue
        n, value = int(match.group(2)), steps[key]
        # The parts of a sectioned summary do not build on each other: only the
        # refused ones are written again.
        alone = n >= PART_STEPS or first[match.group(1)] >= PART_STEPS
        refused = isinstance(value, dict) and value.get("status") == "rejected"
        if refused if alone else n >= first[match.group(1)]:
            del steps[key]
            journal_of(runner, match.group(1), int(match.group(2))).unlink(missing_ok=True)
            dropped += 1
    runner.save()
    return dropped


def each(runner: Runner, items: list, work) -> list:
    with ThreadPoolExecutor(max_workers=max(1, runner.config.jobs)) as pool:
        return list(pool.map(work, items))


def _compile(
    runner: Runner, sources: list[str], records: bool, write: bool = True, pages_too: bool = True
) -> dict:
    store = runner.store
    summary: dict[str, Any] = {"reports": len(sources)}

    counts = extract_all(runner, sources)
    unread = {s: why for s, why in counts.items() if isinstance(why, str)}
    summary["claims"] = sum(n for n in counts.values() if isinstance(n, int))
    if unread:
        return runner.finish("stopped", **summary, reason=f"extraction failed: {unread}")
    summary["claims_refused"] = sum(runner.state.get("refused_claims", {}).values())
    if not write:
        return runner.finish(
            "stopped", **summary, reason="claims extracted; pages not written", **CHECKPOINT
        )

    runner.stage("glossary, page proposals, page list, routing")
    wording = glossary_job(store, sources)
    if wording is not None and not (store.dir / "glossary.json").exists():
        summary["glossary"] = jobs.run_jobs(runner, [wording])[wording.key]["status"]
        if summary["glossary"] not in ("accepted", "rejected"):
            return runner.finish("stopped", **summary, reason=unsettled(runner, "glossary"))

    proposals = jobs.run_jobs(runner, [propose_job(store, s, runner.dir) for s in sources])
    summary["proposals"] = tally(proposals)
    if not settled(runner, proposals):
        return runner.finish("stopped", **summary, reason=unsettled(runner, "proposals"))

    summary["catalog"] = runner.step("catalog", lambda: build_catalog(runner, sources))
    listed_pages = catalog(store)

    owed = [s for s in sources if not (store.dir / "routes" / f"{s}.done").exists()]
    routed = jobs.run_jobs(runner, [route_job(store, s, listed_pages) for s in owed])
    summary["routes"] = tally(routed)
    if not settled(runner, routed):
        return runner.finish("stopped", **summary, reason=unsettled(runner, "routing"))

    if not pages_too:
        return runner.finish(
            "stopped", **summary, reason="claims routed; pages not written", **CHECKPOINT
        )

    by_page = page_claims(store, sources)
    thin = {
        p: rows
        for p, rows in by_page.items()
        if len(rows) < MIN_CLAIMS.get(p.split("/")[0], 1)
        # The site shows an entity page only when two reports speak of the entity
        # (publish.ingest.single_source_entities); one report's account of it is in
        # that report's summary. The first pilot wrote 58 entity pages and showed 13.
        or (p.startswith("entities/") and len({c["id"].split(":")[0] for c in rows}) < 2)
    }
    for page_id in thin:
        del by_page[page_id]
    titles = {p: listed_pages[p] for p in by_page if not p.startswith("summaries/")}

    terms = settled_glossary(store, sources)

    seen: list[str] = []
    fresh: list[str] = []

    def written(page_id: str) -> dict:
        meta = page_meta(store, page_id, listed_pages)
        links = link_targets(page_id, by_page, titles)
        outcome = write_page(runner, page_id, meta, by_page[page_id], links, terms)
        seen.append(page_id)
        runner.stage("pages", len(seen), len(by_page))
        # Each pass this run wrote counts, so a page that kept an older accepted pass
        # does not hide the refusal of its newest one.
        fresh.extend(s for s in outcome.pop("fresh", []) if s in ("accepted", "rejected", "failed"))
        last = fresh[-2 * CANARY :]
        bad = len(last) - last.count("accepted")
        if len(last) >= CANARY and 2 * bad > len(last):
            with runner.lock:
                runner.halted = runner.halted or (
                    f"{bad} of the last {len(last)} page passes were not accepted, "
                    f"{page_id} the latest; nothing else was started. Each refusal is "
                    "under steps in the run's run.json, keyed page-<id>-p<n>. After a "
                    "fix, run the same command with --retry-rejected."
                )
        return outcome

    # Largest first, so the long pages are not what the run ends on.
    order = sorted(by_page, key=lambda p: -len(by_page[p]))
    runner.stage("pages", 0, len(by_page))
    outcomes = each(runner, order, written)
    summary["pages"] = {
        "listed": len(listed_pages),
        "too_thin": len(thin),
        **tally({o["page"]: o for o in outcomes}),
        "claims_routed": sum(o["claims"] for o in outcomes),
        "claims_used": sum(o["used"] for o in outcomes),
        "struck": sum(o.get("struck", 0) for o in outcomes),
        "unplaced": sum(len(o["unplaced"]) for o in outcomes),
    }
    write_text(runner.dir / "pages.json", json.dumps(outcomes, ensure_ascii=False, indent=1))
    # A claim routed to a page that no accepted pass took in is queued under its report,
    # so an operator can see which evidence a page is still missing.
    queued: dict[str, list[dict]] = {}
    for o in outcomes:
        why = "the page was full" if o["status"] == "accepted" else "the page was not accepted"
        if o["page"].startswith("summaries/"):
            # A summary is a digest of its report; what it leaves out is not owed to it.
            continue
        for cid in o["unplaced"]:
            source = cid.split(":")[0]
            queued.setdefault(source, []).extend(
                queue_rows(runner.id, source, o["page"], [cid], why)
            )
    left_out = {p: [c["id"] for c in rows] for p, rows in sorted(thin.items())}
    # A claim whose only page was not written is still told in its report's summary,
    # unless the summary was full or was not accepted. Those are queued, so a reader of
    # the backlog sees evidence the wiki shows nowhere.
    untold = {
        cid
        for o in outcomes
        if o["page"].startswith("summaries/")
        for cid in (
            [c["id"] for c in by_page[o["page"]]] if o["status"] != "accepted" else o["unplaced"]
        )
    }
    placed = {
        c["id"] for p, rows in by_page.items() if not p.startswith("summaries/") for c in rows
    }
    for page_id, ids in left_out.items():
        for cid in ids:
            if cid in untold and cid not in placed:
                source = cid.split(":")[0]
                queued.setdefault(source, []).extend(
                    queue_rows(runner.id, source, page_id, [cid], "no page was written for it")
                )
    # Which claims no page cites, read from what was published and not from what was
    # routed: a claim a writer declined, lost in a strike or never routed is on no page.
    linked = {
        cid
        for sidecar in store.sidecars().values()
        for section in sidecar.get("sections", {}).values()
        for cid in section.get("claims", {})
    }
    uncited = {
        source: missing
        for source in sources
        if (
            missing := sorted(
                c["id"]
                for c in store.claims(source)
                if c.get("status", "active") == "active"
                and c["kind"] != "figure"
                and c["id"] not in linked
            )
        )
    }
    summary["pages"]["claims_on_no_page"] = sum(len(ids) for ids in uncited.values())
    with runner.lock:
        for source in sources:
            # Rows this compile queued in an earlier pass are settled again from the
            # pages as they now stand; rows of other workflows are left alone.
            mine = {r["id"] for r in store.backlog(source) if r.get("run") == runner.id}
            store.unqueue(source, mine - {r["id"] for r in queued.get(source, [])})
        for source, rows in queued.items():
            store.queue(source, rows)
        write_text(
            store.dir / "routes" / "unwritten.json",
            json.dumps(left_out, ensure_ascii=False, indent=1) + "\n",
        )
        write_text(
            store.dir / "routes" / "uncited.json",
            json.dumps(uncited, ensure_ascii=False, indent=1) + "\n",
        )
    if runner.halted or any(o["status"] in ("budget", "failed") for o in outcomes):
        return runner.finish("stopped", **summary, reason=unsettled(runner, "pages"))
    done = [o["page"] for o in outcomes if o["status"] == "accepted"]
    with runner.lock:
        summary["links_removed"] = unlink_missing(store, done)
        write_topic_state(store, listed_pages)
        record_sources(runner, sources)
    if not records:
        # Left open, so the same command without --pages-only goes on to the records.
        return runner.finish(
            "stopped", **summary, reason="pages written; record stages not run", **CHECKPOINT
        )

    summary["records"] = run_records(runner, sources, outcomes)
    waiting = [
        name
        for name, counts_ in summary["records"].items()
        if any(counts_.get(s) for s in ("budget", "failed", "unreviewed"))
    ]
    if runner.halted or waiting:
        return runner.finish("stopped", **summary, reason=unsettled(runner, ", ".join(waiting)))
    return runner.finish("done", **summary)


def tally(outcomes: dict[str, dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for outcome in outcomes.values():
        counts[outcome["status"]] = counts.get(outcome["status"], 0) + 1
    return counts


def settled(runner: Runner, outcomes: dict[str, dict]) -> bool:
    return not runner.halted and all(
        o["status"] in ("accepted", "rejected") for o in outcomes.values()
    )


def unsettled(runner: Runner, what: str) -> str:
    return runner.halted or (
        f"{what}: some sessions failed or the budget was reached; run the same command "
        "again to retry them"
    )


def record_sources(runner: Runner, sources: list[str]) -> None:
    store = runner.store
    rows = store.sources()
    for source in sources:
        text = store.source_text(source)
        rows[source] = {
            "id": source,
            "sha256": sha256(text),
            "claims": len(active(store, source)),
            "blocks": [h for _, _, h in blocks(text)],
            "ingested": date.today().isoformat(),
            "run": runner.id,
        }
    store.write_sources(rows)


def run_records(runner: Runner, sources: list[str], outcomes: list[dict]) -> dict:
    """The record stages: per report first, then the ones that span the corpus."""
    store = runner.store
    models = {role: agent.model for role, agent in runner.config.roles.items()}
    summary: dict[str, dict] = {}
    runner.stage("author and data pages, titles, errata (code)", code=True)
    tidy(runner, sources[0])
    finished: list[str] = []

    def per_report(source: str) -> dict:
        if runner.halted:
            return {}
        scope = jobs.Scope(
            root=runner.root,
            source=source,
            reason="compile",
            run=runner.id,
            sources=sources,
            models=models,
        )
        counts = jobs.run_all(runner, scope, REPORT_STAGES)
        finished.append(source)
        runner.stage("records per report", len(finished), len(sources))
        return counts

    # A report's records rest on its own claims and summary, so reports run side by
    # side; the runner still starts no more than ``jobs`` sessions at once.
    runner.stage("records per report", 0, len(sources))
    with ThreadPoolExecutor(max_workers=REPORTS_AT_ONCE) as pool:
        for counted in pool.map(per_report, sources):
            for name, counts in counted.items():
                merged = summary.setdefault(name, {})
                for status, n in counts.items():
                    merged[status] = merged.get(status, 0) + n
    if runner.halted:
        return summary
    written = [o["page"] for o in outcomes if o["status"] == "accepted"]
    db = index.connect(runner.root)
    try:
        sections = [r[0] for r in db.execute("SELECT id FROM sections ORDER BY id")]
    finally:
        db.close()
    scope = jobs.Scope(
        root=runner.root,
        source="",
        reason="compile",
        run=runner.id,
        sources=sources,
        edited=[s for s in sections if s.split("#")[0] in set(written)],
        created=sorted(written),
        models=models,
    )
    before = tuple(s for s in CORPUS_STAGES if s != "figures")
    # The home page links the catalog, so it is listed before the hubs are written.
    rebuild_index(runner.root)
    summary |= jobs.run_all(runner, scope, before)
    unsearched = len(scope.notes.get("literature_unavailable", []))
    if unsearched:
        # PubMed did not answer; without this the compile would call itself done.
        found = summary.setdefault("literature", {})
        found["failed"] = found.get("failed", 0) + unsearched
    if runner.halted or any(c.get("budget") for c in summary.values()):
        return summary
    runner.stage("author and data pages, titles, errata (code)", code=True)
    tidy(runner, sources[0])
    with runner.lock:
        # Before figures, whose placements record the hash of the page they sit on.
        # Report mirrors are archived as written and keep their own links.
        unlink_missing(store, [p for p in store.page_ids() if not p.startswith("sources/")])
        rebuild_index(runner.root)
    summary |= jobs.run_all(runner, scope, ("figures",))
    return summary
