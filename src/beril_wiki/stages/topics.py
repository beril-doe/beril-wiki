#!/usr/bin/env python3
"""Generate the narrative hub layer: ~12 topic pages + a home page, v2-style.

Sits ON TOP of the compiled wiki (reads wiki/concepts + wiki/entities), writes
wiki/topics/ and the home page wiki/index.md; the compiler never touches either.
The agentic runner selects topic membership and names. API mode uses Louvain
over the concept co-source/wikilink graph and model-generated names. Both write
hub prose citing only what the member concept pages already cite, from a
packed evidence prompt that agentic.prose gates, reviews and patches.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python -m beril_wiki.stages.topics
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import sys

import networkx as nx

from beril_wiki import compiler as C
from beril_wiki.agentic.prose import (
    NO_PREAMBLE,
    PLATFORM,
    Contract,
    PageFailure,
    derived_page,
    excerpts,
    failed_pages,
    limit,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import atomic_json, completion, configured
from beril_wiki.check import source_ids
from beril_wiki.paths import ROOT
from beril_wiki.publish import ingest

OUT = ROOT / "wiki"
HUB_MODEL = os.environ.get("HUB_MODEL", os.environ.get("WIKI_MODEL", "openai/gpt-5.6-luna"))
MIN_CLUSTER = 3
FORCE = "--force" in sys.argv
PACK_CHARS = 110_000  # member pages packed into one hub prompt
MAX_CONFLICTS = 40

CONTRACT = Contract(
    rules=(
        "Write 900-1400 words in total (the code gate allows 10% either way).",
        "Sections in this order: an H1 topic title; one lead paragraph saying what the topic "
        "is and why this corpus speaks to it; ## What the Corpus Shows, arguing across the "
        "member concepts as one narrative in 3-6 bold-led sub-themes; ## Tensions and Caveats, "
        "the real disagreements between projects and the load-bearing limitations, cited; "
        "## Where to Go Deeper, a reading path of 4-8 bullets '[[concepts/<stem>]] — why you "
        "would read it next', then key entities [[entities/<stem>]] and reports "
        "[[summaries/<id>__REPORT]].",
        "Use only figures that appear in the MEMBER CONCEPT PAGES or CONFLICT PAGES, copied "
        "exactly; never round, compute or import one.",
        "Cite every factual claim with [src: <project id>] tags copied from the member pages; "
        "a tag holds only project ids from PROJECTS IN SCOPE, comma-separated, never concept "
        "names or page paths.",
        "Figures in the lead must carry their [src:] tags or be counts of this page's own "
        "sections.",
        "Link every member concept at least once as [[concepts/<stem>]]; reference conflict "
        "pages only as [[conflicts/<stem>]] wikilinks.",
        "Keep each claim's direction, denominator, threshold and caveat as the member page "
        "states it; a null result stays null.",
        "Define specialist terms and abbreviations at first use; write for a scientist-engineer "
        "who knows biology but not this corpus.",
        NO_PREAMBLE.format(first="the H1"),
        PLATFORM,
    ),
    words=(900, 1400),
    headings=("## What the Corpus Shows", "## Tensions and Caveats", "## Where to Go Deeper"),
)
TASK = (
    "Write the TOPIC HUB page for the TOPIC named below: the entry point a scientist reads "
    "first to learn what the corpus says about this topic before opening the finer-grained "
    "concept pages."
)
HOME = Contract(
    rules=(
        "Sections in this order: the H1 'BERIL Knowledge Wiki'; 2-3 paragraphs introducing the "
        "BERIL Research Observatory corpus (AI-conducted microbial-biology research over the "
        "KBase Data Lakehouse) and how to read the wiki (topics are the entry points; "
        "concepts, entities and summaries are the reference layers); ## Topics, presenting "
        "each topic as a '- [[topics/<slug>|<title>]] (<n> concepts): <hook>' list item; "
        "## Corpus, one line with the given counts; ## Browse, linking "
        "[[catalog|Full page catalog]], [[summaries/discoveries|Discoveries digest]], "
        "[[summaries/pitfalls|Pitfalls digest]], [[authors/index|Authors]] and "
        "[[data/index|Data collections]].",
        "Base every topic hook on the given hub leads; invent no findings and no figures.",
        "Plain, concrete English in the active voice with a clear subject. No em dashes or en "
        "dashes. No inflated framing ('serves as', 'stands as', 'plays a key role', "
        "'underscores', 'highlights', 'showcases', 'reflects a broader'), no sales words "
        "(vibrant, rich, powerful, comprehensive, seamless, robust), no forced groups of "
        "three, no closing flourish about the future: end on the last real fact.",
        NO_PREAMBLE.format(first="the H1"),
        PLATFORM,
    ),
    headings=("## Topics", "## Corpus", "## Browse"),
    first="# BERIL Knowledge Wiki",
    cite=False,
)


def src_id(entry: str) -> str:
    """A `sources:` frontmatter entry -> the project id used in [src:] tags.

    Must match wiki_check.cited_ids' normalization. The old code extracted only
    `summaries/<id>__REPORT` and fell back to the RAW quoted string when a page
    had none, so a concept sourced solely from a digest put the literal
    "summaries/discoveries.md" into the valid-id set. bad_src_ids then accepted
    `[src: summaries/discoveries.md]` in a hub, which check rejects as an
    unknown source id — 8 publish-blocking errors from one format mismatch."""
    return re.sub(r"__REPORT$", "", entry.strip().rsplit("/", 1)[-1].removesuffix(".md"))


def parse_page(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^sources:\s*\[(.*?)\]", text, re.M)
    if m:
        raw = re.findall(r'"([^"]+)"', m.group(1))
    else:
        m2 = re.search(r"^sources:\n((?:\s+-\s.*\n)+)", text, re.M)
        raw = re.findall(r'-\s*"?([^"\n]+?)"?\s*$', m2.group(1), re.M) if m2 else []
    sources = [src_id(s) for s in raw]
    h1 = re.search(r"^# (.+)$", text, re.M)
    desc = re.search(r'^description:\s*"?(.*?)"?$', text, re.M)
    links = set(re.findall(r"\[\[concepts/([\w.-]+?)(?:\|[^\]]*)?\]\]", text))
    return {
        "stem": path.stem,
        "title": h1.group(1).strip() if h1 else path.stem,
        "desc": desc.group(1).strip() if desc else "",
        "sources": set(sources),
        "links": links,
        "text": text,
    }


def cluster_concepts(concepts: dict[str, dict]) -> list[list[str]]:
    g = nx.Graph()
    g.add_nodes_from(concepts)
    stems = list(concepts)
    for i, a in enumerate(stems):
        for b in stems[i + 1 :]:
            w = len(concepts[a]["sources"] & concepts[b]["sources"])
            w += 2 * ((b in concepts[a]["links"]) + (a in concepts[b]["links"]))
            if w:
                g.add_edge(a, b, weight=w)
    # resolution=2.0 -> ~14 topics of 3-9 concepts on this corpus (default 1.0 gave 4 mega-hubs)
    if not g.edges:
        return [sorted(g)] if g else []
    comms = [
        set(c)
        for c in nx.community.louvain_communities(g, weight="weight", seed=42, resolution=2.0)
    ]
    # Fold tiny clusters into the neighbor cluster with the strongest total edge weight.
    big = [c for c in comms if len(c) >= MIN_CLUSTER]
    if not big:
        return [sorted(g)]
    for small in (c for c in comms if len(c) < MIN_CLUSTER):

        def pull(target: set, small: set = small) -> float:
            return sum(g[u][v]["weight"] for u in small for v in g.neighbors(u) if v in target)

        best = max(big, key=pull, default=None)
        (best if best is not None else big[0] if big else comms[0]).update(small)
    return [sorted(c) for c in sorted(big, key=len, reverse=True)]


def llm(prompt: str, *, step: str) -> str:
    """A mechanical (unreviewed) call; hub prose goes through agentic.prose instead."""
    resp = completion(
        step=step,
        review=False,
        model=HUB_MODEL,
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        timeout=600,
    )
    return resp.choices[0].message.content


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


SRC_TAG = re.compile(r"\[src:\s*([^\]]+)\]")


def bad_src_ids(page: str, valid: set[str]) -> list[str]:
    return sorted(
        {
            re.sub(r"__REPORT$", "", p.strip())
            for m in SRC_TAG.finditer(page)
            for p in re.split(r"[,;]", m.group(1))
            if re.sub(r"__REPORT$", "", p.strip()) not in valid
        }
    )


def strip_bad_src(page: str, valid: set[str]) -> str:
    """Last-resort repair: drop invalid ids from [src:] tags (whole tag if none
    survive) — the claim's real citations live on the linked concept pages."""

    def repl(m: re.Match) -> str:
        keep = [
            p.strip()
            for p in re.split(r"[,;]", m.group(1))
            if re.sub(r"__REPORT$", "", p.strip()) in valid
        ]
        return f"[src: {', '.join(keep)}]" if keep else ""

    return SRC_TAG.sub(repl, page)


def uncited_figures(page: str) -> list[str]:
    """Paragraphs stating figures without a [src:] tag; the contract requires both."""
    from beril_wiki.check import NUMBER, cited_ids, paragraphs, prose_only

    # The reading path names pages, not claims; check already treats it as a warning.
    body = re.sub(r"^## Where to Go Deeper\s*\n.*?(?=\n## |\Z)", "", page, flags=re.M | re.S)
    return [
        f"no [src:] tag beside figures: {par[:120]!r}"
        for par in paragraphs(body)
        if NUMBER.findall(prose_only(par)) and not cited_ids(par)
    ]


def link_missing_members(page: str, members: list[str], concepts: dict) -> str:
    """Append assigned concepts the writer left unlinked, so every member stays reachable."""
    missing = [m for m in members if f"[[concepts/{m}" not in page]
    if not missing:
        return page
    bullets = "\n".join(
        f"- [[concepts/{m}]] — {concepts[m].get('desc') or concepts[m]['title']}" for m in missing
    )
    section = re.search(r"^## Where to Go Deeper[^\n]*\n.*?(?=^## |\Z)", page, re.M | re.S)
    if section:
        return (
            page[: section.end()].rstrip("\n")
            + "\n"
            + bullets
            + "\n\n"
            + page[section.end() :].lstrip("\n")
        )
    return page.rstrip("\n") + "\n\n## Where to Go Deeper\n\n" + bullets + "\n"


def corpus_stats(root: pathlib.Path) -> str:
    """The corpus line, counted from the files, in code.

    Count published pages, excluding the single-source entities hidden by
    publish.ingest. Compute these counts directly so the home page does not
    rely on a model to transcribe them."""
    summaries = list((root / "wiki" / "summaries").glob("*.md"))
    digests = sum(
        (root / "wiki" / "summaries" / f"{d}.md").exists() for d in ("discoveries", "pitfalls")
    )
    hidden = ingest.single_source_entities(root)
    entities = [f for f in (root / "wiki" / "entities").glob("*.md") if f.stem not in hidden]
    return (
        f"{len(summaries) - digests} project reports + {digests} cross-project digests, "
        f"{len(list((root / 'wiki' / 'concepts').glob('*.md')))} concepts, "
        f"{len(entities)} entities, "
        f"{len(list((root / 'wiki' / 'topics').glob('*.md')))} topics"
    )


def refresh_corpus_line(path: pathlib.Path, stats: str) -> bool:
    """Overwrite the '## Corpus' line with the counted truth. True if changed.

    Runs on every invocation, not only when the home page is regenerated: the
    page is rewritten only when a hub changes, so a concept merge left the old
    figure on the front page (it said 93 concepts against 92 real ones)."""
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    new = re.sub(
        r"(^## Corpus\s*\n\n).*?(?=\n)",
        lambda m: m.group(1) + stats,
        text,
        count=1,
        flags=re.M | re.S,
    )
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


# Where the data came from. This is a standing fact about the corpus, not a
# sentence for a model to rephrase: a regenerated home page would otherwise
# drop the credit and the link, which is how an acknowledgement quietly
# disappears. Most projects analysed lakehouse data, not all of them, so the
# wording does not claim every one.
ACKNOWLEDGEMENT = (
    "Most of these projects analysed data already in the "
    "[KBase Data Lakehouse](https://hub.berdl.kbase.us); a few brought their own. "
    "See [[about|About This Wiki]] for what that means for citing anything here."
)


def refresh_acknowledgement(path: pathlib.Path) -> bool:
    """Put the standing acknowledgement under the H1. True if the file changed."""
    text = path.read_text(encoding="utf-8")
    body = re.sub(r"\n" + re.escape(ACKNOWLEDGEMENT) + r"\n", "\n", text)
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            lines.insert(i + 1, "")
            lines.insert(i + 2, ACKNOWLEDGEMENT)
            break
    else:
        return False
    new = "\n".join(lines).rstrip() + "\n"
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def write_home(hubs: list[tuple], stats: str) -> bool:
    hub_list = "\n".join(
        f"- [[topics/{slug}|{t}]] ({n} concepts): {lead}" for t, slug, lead, n in hubs
    )
    pack = f"TOPIC HUBS (title, slug, lead, concept count):\n{hub_list}\n\nCORPUS COUNTS:\n{stats}"
    try:
        home = derived_page(
            "home",
            HOME,
            "Write the HOME page of this research wiki.",
            pack,
            allowed=pack,
            sources={},
            valid_ids=set(),
            targets=C.wikilink_targets(ROOT) | {"about"},
        )
    except PageFailure as exc:
        record_failure("index.md", exc)
        print(f"  [FAILED] home: {exc}")
        return False
    (OUT / "index.md").write_text(home.strip() + "\n", encoding="utf-8")
    # The model was given the stats, but it must not own them.
    refresh_corpus_line(OUT / "index.md", stats)
    refresh_acknowledgement(OUT / "index.md")
    record_failure("index.md", None)
    print(f"wrote index.md; {stats}")
    return True


def conflict_lead(text: str) -> str:
    """Title and lead paragraph only: enough to anchor and link a hub's Tensions section.

    The evidence itself already reaches the hub through its member concepts, so
    packing Evidence Sides again only inflates every draft, patch and review."""
    body = re.sub(r"^<!--.*?-->\n?", "", text, flags=re.M)
    m = re.search(r"^(# .+?)\n+(.+?)(?:\n\n|\n#|\Z)", body, re.S)
    return f"{m.group(1)}\n{m.group(2).strip()}"[:1500] if m else body[:600]


def hub_entry(topic: str, slug: str, members: list[str]) -> tuple:
    page = (OUT / "topics" / f"{slug}.md").read_text(encoding="utf-8")
    lead = re.search(r"^# .+?\n+(.+?)(?:\n\n|\n#)", page, re.S)
    return (topic, slug, (lead.group(1).strip() if lead else "")[:400], len(members))


def hubs_from_disk(out: pathlib.Path) -> list[tuple]:
    """The published hubs, read from the pages rather than re-derived.

    Regenerating only the home page must not re-cluster: clustering depends on
    the current concept set, so any run after a concept merge produces a
    different hub set and rewrites pages nobody asked to change. This reads
    what is already on disk."""
    hubs = []
    for f in sorted(out.glob("topics/*.md")):
        if f.stem == "index":
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        title = re.search(r"^# (.+)$", text, re.M)
        members = len(set(re.findall(r"\[\[concepts/([\w.-]+)", text)))
        hubs.append(hub_entry(title.group(1).strip() if title else f.stem, f.stem, [""] * members))
    return hubs


def main() -> int:
    # --home-only rewrites index.md from the hubs already published and touches
    # nothing else. Used to refresh the landing page's prose without letting a
    # re-clustering run churn every hub.
    if "--home-only" in sys.argv:
        hubs = hubs_from_disk(OUT)
        if not hubs:
            print("stages.topics: no hubs on disk; run the full stage first")
            return 1
        return 0 if write_home(hubs, corpus_stats(ROOT)) or not strict_pages() else 1
    src_texts = source_ids(ROOT)
    targets = C.wikilink_targets(ROOT)
    concepts = {p.stem: parse_page(p) for p in sorted((ROOT / "wiki/concepts").glob("*.md"))}
    entities = {p.stem: parse_page(p) for p in sorted((ROOT / "wiki/entities").glob("*.md"))}
    groups = None
    if configured():
        from beril_wiki.agentic.topics import load_groups

        groups = load_groups(ROOT)
    clusters = (
        [group["concepts"] for group in groups]
        if groups is not None
        else cluster_concepts(concepts)
    )
    print(f"{len(concepts)} concepts -> {len(clusters)} clusters: {[len(c) for c in clusters]}")

    (OUT / "topics").mkdir(parents=True, exist_ok=True)
    state_path = ROOT / "state" / "topics-state.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    if FORCE:
        # Keep __names__ so topic identity (and therefore page slugs) stays put;
        # drop only the content digests so every hub regenerates.
        state = {"__names__": state.get("__names__", {})}
        print("  --force: ignoring cached hub digests")

    # Topic names are cached by member set so identical clusters never get
    # renamed (renames churn page identity and force needless hub regens).
    name_cache: dict[str, str] = state.setdefault("__names__", {})
    keys = [hashlib.sha256(",".join(c).encode()).hexdigest()[:12] for c in clusters]
    unnamed = [i for i, k in enumerate(keys) if k not in name_cache] if groups is None else []
    if unnamed:
        listing = "\n".join(
            f"CLUSTER {i}:\n"
            + "\n".join(f"  - {concepts[s]['title']}: {concepts[s]['desc']}" for s in clusters[i])
            for i in unnamed
        )
        reply = llm(
            "Name each cluster of research-wiki concepts as a scientific TOPIC (2-4 words, "
            "noun phrase, distinctive). Reply with ONLY a JSON object mapping cluster number "
            f"(string) to topic name.\n\n{listing}",
            step="topics/names",
        )
        m = re.search(r"\{.*\}", reply, re.S)
        if not m:
            raise ValueError(f"topic naming reply carried no JSON object: {reply[:200]!r}")
        fresh = json.loads(m.group(0))
        for i in unnamed:
            if str(i) in fresh:
                name_cache[keys[i]] = fresh[str(i)]
    names = (
        {str(i): group["title"] for i, group in enumerate(groups)}
        if groups is not None
        else {str(i): name_cache.get(k, f"Topic {i}") for i, k in enumerate(keys)}
    )
    conflicts = (
        {
            p.stem: p.read_text(encoding="utf-8", errors="replace")
            for p in sorted((OUT / "conflicts").glob("*.md"))
        }
        if (OUT / "conflicts").is_dir()
        else {}
    )

    todo, planned = [], []
    for i, members in enumerate(clusters):
        topic = names.get(str(i), f"Topic {i}")
        slug = slugify(topic)
        planned.append((topic, slug, list(members)))
        srcs = set().union(*(concepts[s]["sources"] for s in members))
        # A conflict page belongs to a hub when it links one of the hub's concepts.
        rel_conflicts = [
            c
            for c, t in conflicts.items()
            if any(f"[[concepts/{s}]]" in t or f"[[concepts/{s}|" in t for s in members)
        ][:MAX_CONFLICTS]
        digest = hashlib.sha256(
            (
                topic
                + "\n"
                + "\n".join(concepts[s]["text"] for s in members)
                + "".join(conflicts[c] for c in rel_conflicts)
            ).encode()
        ).hexdigest()[:16]
        if state.get(slug) == digest and (OUT / "topics" / f"{slug}.md").exists():
            print(f"  unchanged topics/{slug}.md")
            continue
        todo.append((topic, slug, list(members), srcs, rel_conflicts, digest))

    def write(item: tuple) -> str:
        topic, slug, members, srcs, rel_conflicts, _ = item
        bodies = {f"concepts/{s}": C.parse_fm(concepts[s]["text"])[1] for s in members}
        leads = "\n\n".join(
            f"[conflicts/{c}]\n{conflict_lead(conflicts[c])}" for c in rel_conflicts
        )
        ents = sorted(entities, key=lambda e: -len(entities[e]["sources"] & srcs))[:10]
        pack = (
            f"TOPIC: {topic}\n\nMEMBER CONCEPT PAGES:\n\n{excerpts(bodies, PACK_CHARS)}\n\n"
            + (
                "CONFLICT PAGES (anchor the Tensions section on these; link them as "
                f"[[conflicts/<stem>]]):\n{leads}\n\n"
                if leads
                else ""
            )
            + "RELATED ENTITY PAGES (link candidates): "
            f"{', '.join('entities/' + e for e in ents)}\n"
            "PROJECTS IN SCOPE (for [src:] tags and [[summaries/<id>__REPORT]] links): "
            f"{', '.join(sorted(srcs))}"
        )
        return derived_page(
            f"topics/{slug}",
            CONTRACT,
            TASK,
            pack,
            allowed="\n".join(bodies.values()) + "\n".join(conflicts[c] for c in rel_conflicts),
            sources=src_texts,
            valid_ids=set(srcs),
            targets=targets | {f"topics/{slug}"},
            # Code guarantees member links; run it before gates so it never costs a round.
            normalize=lambda page: link_missing_members(page, members, concepts),
        )

    cap = limit(sys.argv)
    if cap is not None:
        print(f"  --limit {cap}: writing at most {cap} hub(s), retiring none")
        todo = todo[:cap]
    any_changed = False
    failed = 0
    for (_, slug, members, _, rel_conflicts, digest), result in parallel(todo, write, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"topics/{slug}", result)
            print(f"  [FAILED] topics/{slug}: {result}")
            continue
        (OUT / "topics" / f"{slug}.md").write_text(result.strip() + "\n", encoding="utf-8")
        state[slug] = digest
        any_changed = True
        record_failure(f"topics/{slug}", None)
        print(f"  wrote topics/{slug}.md ({len(members)} concepts, {len(rel_conflicts)} conflicts)")
    atomic_json(state_path, state)
    # Retire hub pages for topics that no longer exist after re-clustering, unless a
    # hub failed this pass: its predecessor under an old title is the kept version.
    live = {slug for _, slug, _ in planned}
    if failed:
        print(f"  {failed} hub(s) failed: retiring nothing this pass")
    for stale in [] if cap is not None or failed else (OUT / "topics").glob("*.md"):
        if stale.stem not in live:
            stale.unlink()
            any_changed = True
            print(f"  removed stale topics/{stale.stem}.md")
    prune_failures("topics/", {f"topics/{slug}" for slug in live})
    # A retried home failure must reach write_home even when no hub changed.
    refresh_home = "--refresh-home" in sys.argv or "index.md" in failed_pages()
    if not any_changed and (OUT / "index.md").exists() and not refresh_home:
        if refresh_corpus_line(OUT / "index.md", corpus_stats(ROOT)):
            print("home unchanged; corpus counts refreshed")
        else:
            print("home unchanged; done")
        return 1 if failed and strict_pages() else 0

    hubs = [
        hub_entry(topic, slug, members)
        for topic, slug, members in planned
        if (OUT / "topics" / f"{slug}.md").exists()
    ]
    if not write_home(hubs, corpus_stats(ROOT)):
        failed += 1
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main())
