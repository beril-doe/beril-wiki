#!/usr/bin/env python3
"""Generate the narrative hub layer: ~12 topic pages + a home page, v2-style.

Sits ON TOP of the compiled wiki (reads wiki/concepts + wiki/entities), writes
wiki/topics/ and the home page wiki/index.md; the compiler never touches either.
Topic membership is deterministic (Louvain over the concept co-source/wikilink
graph); an LLM names the topics and writes the hub prose, citing only what the
member concept pages already cite.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python -m beril_wiki.stages.topics

Model comes from HUB_MODEL below (hub pages are the showcase — Sonnet by decision).
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import sys

import networkx as nx
from litellm import completion

from beril_wiki import compiler as C
from beril_wiki.check import source_ids
from beril_wiki.paths import ROOT
from beril_wiki.publish import ingest

OUT = ROOT / "wiki"
HUB_MODEL = os.environ.get("HUB_MODEL", os.environ.get("WIKI_MODEL", "openai/gpt-5.6-luna"))
# The home page is one call, and it is the page every reader lands on first, so
# it is worth a stronger model than the bulk stages: a few cents against prose
# that frames the whole site. Override like any other stage.
HOME_MODEL = os.environ.get("HOME_MODEL", "openai/claude-opus-5")
MIN_CLUSTER = 3
FORCE = "--force" in sys.argv
PER_PAGE_CHARS = 7000  # truncate very long concept pages in hub context

TEMPLATE = """You are writing a TOPIC HUB page for the BERIL Research Observatory wiki — the
entry point a scientist reads first to learn what the corpus says about this topic,
before drilling into the finer-grained concept pages.

Write markdown with exactly these sections:
# <Topic Title>
(one-paragraph lead: what this topic is and why this corpus speaks to it)
## What the Corpus Shows
(the heart of the page: argue ACROSS the member concepts/projects as one narrative,
 organized into 3-6 bold-led sub-themes; cite every factual claim with [src: project_id]
 tags COPIED from the member pages — never invent numbers or citations; link liberally
 to member pages with [[concepts/<file-stem>]] wikilinks where a claim is elaborated)
## Tensions and Caveats
(real disagreements between projects and the load-bearing limitations, cited)
## Where to Go Deeper
(a guided reading path: 4-8 bullets, each "[[concepts/x]] — why you'd read it next";
 then a short list of key entities [[entities/y]] and project reports [[summaries/z__REPORT]])

Rules: numbers must be copied exactly from the member pages; a claim you cannot
attribute must not be written; define specialist terms at first use; write for a
scientist-engineer who knows biology but not this corpus. 900-1400 words.
CITATION SYNTAX (strict): a [src: ...] tag contains ONLY project ids from the
PROJECTS IN SCOPE list, comma-separated — never concept names, conflict-page
paths, dashes, or prose. Conflict and concept pages are referenced only as
[[conflicts/...]] / [[concepts/...]] wikilinks, never inside [src: ...].
NAMING: the data platform is the KBase Data Lakehouse. Reports call it
BERDL or the BER Data Lakehouse; those are earlier names for the same
system and must not appear in a page you write. The project id
`berdl_data_atlas` and that project's title "BERDL Data Atlas" are names
of a project, not of the platform, and stay as they are.
"""


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
    comms = [
        set(c)
        for c in nx.community.louvain_communities(g, weight="weight", seed=42, resolution=2.0)
    ]
    # Fold tiny clusters into the neighbor cluster with the strongest total edge weight.
    big = [c for c in comms if len(c) >= MIN_CLUSTER]
    for small in (c for c in comms if len(c) < MIN_CLUSTER):

        def pull(target: set, small: set = small) -> float:
            return sum(g[u][v]["weight"] for u in small for v in g.neighbors(u) if v in target)

        best = max(big, key=pull, default=None)
        (best if best is not None else big[0] if big else comms[0]).update(small)
    return [sorted(c) for c in sorted(big, key=len, reverse=True)]


def llm(prompt: str, system: str = "", model: str | None = None) -> str:
    resp = completion(
        model=model or HUB_MODEL,
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
        messages=([{"role": "system", "content": system}] if system else [])
        + [{"role": "user", "content": prompt}],
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


def corpus_stats(root: pathlib.Path) -> str:
    """The corpus line, counted from the files, in code.

    Counts PUBLISHED pages: publish.ingest hides entities cited by only one
    project, so the raw 336 was a number no reader could reach. docs/design.md keeps
    the catalog and log deterministic "in code, not by LLM" for the same reason
    this line now is — a model transcribing a figure onto the home page is a
    figure nothing verifies."""
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


def write_home(hubs: list[tuple], stats: str) -> None:
    hub_list = "\n".join(
        f"- [[topics/{slug}|{t}]] ({n} concepts): {lead}" for t, slug, lead, n in hubs
    )
    style = (
        "\n\nSTYLE, follow exactly:\n"
        "- Plain, concrete English. Active voice with a clear subject: 'the pipeline "
        "compiles X', never 'X is compiled'.\n"
        "- No em dashes or en dashes anywhere. Use a comma, colon, or a second sentence.\n"
        "- No inflated framing: nothing 'serves as', 'stands as', 'plays a key role', "
        "'underscores', 'highlights', 'showcases', or 'reflects a broader' anything.\n"
        "- No sales words: vibrant, rich, powerful, comprehensive, seamless, robust.\n"
        "- Do not force ideas into groups of three.\n"
        "- Say what a thing is, not what it represents. Prefer 'is' and 'has' over "
        "'serves as' and 'boasts'.\n"
        "- No closing flourish about what the future holds. End on the last real fact."
    )
    home = llm(
        "Write the HOME page (markdown, H1 title 'BERIL Knowledge Wiki') for this research "
        "wiki: 2-3 paragraphs introducing the BERIL Research Observatory corpus (AI-conducted "
        "microbial-biology research over the KBase Data Lakehouse) and how to read the wiki "
        "(topics are the entry points; concepts/entities/summaries are the reference layers), "
        f"then a '## Topics' section presenting each topic with its one-line hook as a wikilink "
        f"list, then a '## Corpus' line with these stats: {stats}, then a '## Browse' section "
        "linking [[catalog|Full page catalog]], [[summaries/discoveries|Discoveries digest]], "
        "[[summaries/pitfalls|Pitfalls digest]], [[authors/index|Authors]], and "
        "[[data/index|Data collections]]. "
        f"Base every topic description on these leads, do not invent findings:\n\n{hub_list}"
        + style,
        model=HOME_MODEL,
    )
    (OUT / "index.md").write_text(home.strip() + "\n", encoding="utf-8")
    # The model was given the stats, but it must not own them.
    refresh_corpus_line(OUT / "index.md", stats)
    refresh_acknowledgement(OUT / "index.md")
    print(f"wrote index.md; {stats}")


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
        lead = re.search(r"^# .+?\n+(.+?)(?:\n\n|\n#)", text, re.S)
        members = len(set(re.findall(r"\[\[concepts/([\w.-]+)", text)))
        hubs.append(
            (
                title.group(1).strip() if title else f.stem,
                f.stem,
                (lead.group(1).strip() if lead else "")[:400],
                members,
            )
        )
    return hubs


def main() -> int:
    failures: list[str] = []
    # --home-only rewrites index.md from the hubs already published and touches
    # nothing else. Used to refresh the landing page's prose without letting a
    # re-clustering run churn every hub.
    if "--home-only" in sys.argv:
        hubs = hubs_from_disk(OUT)
        if not hubs:
            print("stages.topics: no hubs on disk; run the full stage first")
            return 1
        write_home(hubs, corpus_stats(ROOT))
        return 0
    src_texts = source_ids(ROOT)
    targets = C.wikilink_targets(ROOT)
    concepts = {p.stem: parse_page(p) for p in sorted((ROOT / "wiki/concepts").glob("*.md"))}
    entities = {p.stem: parse_page(p) for p in sorted((ROOT / "wiki/entities").glob("*.md"))}
    clusters = cluster_concepts(concepts)
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
    unnamed = [i for i, k in enumerate(keys) if k not in name_cache]
    if unnamed:
        listing = "\n".join(
            f"CLUSTER {i}:\n"
            + "\n".join(f"  - {concepts[s]['title']}: {concepts[s]['desc']}" for s in clusters[i])
            for i in unnamed
        )
        reply = llm(
            "Name each cluster of research-wiki concepts as a scientific TOPIC (2-4 words, "
            "noun phrase, distinctive). Reply with ONLY a JSON object mapping cluster number "
            f"(string) to topic name.\n\n{listing}"
        )
        m = re.search(r"\{.*\}", reply, re.S)
        if not m:
            raise ValueError(f"topic naming reply carried no JSON object: {reply[:200]!r}")
        fresh = json.loads(m.group(0))
        for i in unnamed:
            if str(i) in fresh:
                name_cache[keys[i]] = fresh[str(i)]
    names = {str(i): name_cache.get(k, f"Topic {i}") for i, k in enumerate(keys)}
    conflicts = (
        {
            p.stem: p.read_text(encoding="utf-8", errors="replace")
            for p in sorted((OUT / "conflicts").glob("*.md"))
        }
        if (OUT / "conflicts").is_dir()
        else {}
    )

    hubs = []
    any_changed = False
    for i, members in enumerate(clusters):
        topic = names.get(str(i), f"Topic {i}")
        slug = slugify(topic)
        srcs = set().union(*(concepts[s]["sources"] for s in members))
        rel_conflicts = [c for c, t in conflicts.items() if len({p for p in srcs if p in t}) >= 2]
        digest = hashlib.sha256(
            (
                "\n".join(concepts[s]["text"] for s in members)
                + "".join(conflicts[c] for c in rel_conflicts)
            ).encode()
        ).hexdigest()[:16]
        out_path = OUT / "topics" / f"{slug}.md"
        if state.get(slug) == digest and out_path.exists():
            page = out_path.read_text(encoding="utf-8")
            lead = re.search(r"^# .+?\n+(.+?)(?:\n\n|\n#)", page, re.S)
            hubs.append((topic, slug, (lead.group(1).strip() if lead else "")[:400], len(members)))
            print(f"  unchanged topics/{slug}.md")
            continue
        member_text = "\n\n---\n\n".join(
            f"[file: concepts/{s}]\n{concepts[s]['text'][:PER_PAGE_CHARS]}" for s in members
        )
        conflict_text = "\n\n".join(
            f"[conflict page: conflicts/{c}]\n{conflicts[c][:3000]}" for c in rel_conflicts
        )
        ents = sorted(entities, key=lambda e: -len(entities[e]["sources"] & srcs))[:10]
        prompt = (
            f"TOPIC: {topic}\n\nMEMBER CONCEPT PAGES:\n\n{member_text}\n\n"
            + (
                "PROMOTED CONFLICT PAGES (anchor the Tensions section on these; "
                f"link them as [[conflicts/<stem>]]):\n{conflict_text}\n\n"
                if conflict_text
                else ""
            )
            + "RELATED ENTITY PAGES (link candidates): "
            f"{', '.join('entities/' + e for e in ents)}\n"
            "PROJECTS IN SCOPE (for [src:] tags and [[summaries/<id>__REPORT]] links): "
            f"{', '.join(sorted(srcs))}"
        )
        page = llm(prompt, system=TEMPLATE)
        bad = bad_src_ids(page, srcs)
        if bad:  # one violation-quoting retry, then deterministic repair
            print(f"  ! topics/{slug}: invalid [src:] ids {bad} — retrying")
            page = llm(
                prompt + f"\n\nYOUR PREVIOUS ATTEMPT cited invalid [src:] ids: {bad}. "
                "[src:] tags may contain ONLY project ids from PROJECTS IN SCOPE — "
                "concept or conflict pages are referenced as [[wikilinks]], never inside [src:]. "
                "Rewrite the full page fixing every such tag.",
                system=TEMPLATE,
            )
            if bad_src_ids(page, srcs):
                print(f"  ! topics/{slug}: still invalid — stripping bad [src:] ids")
                page = strip_bad_src(page, srcs)
        # Same two guarantees generate_page gives every compile-written page:
        # figures traceable to a cited source, and no link to a page that does
        # not exist. One retry for numbers, then deterministic link repair.
        nv = C.prose_violations(page, src_texts)
        if nv:
            print(f"  ! topics/{slug}: {len(nv)} unsupported figure(s) — retrying")
            page = llm(
                prompt + "\n\nYOUR PREVIOUS ATTEMPT contained figures that appear in none "
                "of the cited sources:\n"
                + "\n".join(f"- {x}" for x in nv[:12])
                + "\nRewrite the full page. Every number must be copied exactly from a source "
                "you cite in the same paragraph; drop any figure you cannot attribute.",
                system=TEMPLATE,
            )
            page = strip_bad_src(page, srcs)
            # Revalidate the retry before accepting it. Writing the second
            # response unchecked meant a retry that fixed nothing was cached as
            # the current page, and the next pipeline check saw it only as a
            # warning.
            if C.prose_violations(page, src_texts):
                print(
                    f"  ! topics/{slug}: retry still unsupported — page rejected, keeping previous"
                )
                failures.append(f"topics/{slug}")
                continue
        page = C.downgrade_dead_links(page, targets | {f"topics/{slug}"})
        out_path.write_text(page.strip() + "\n", encoding="utf-8")
        state[slug] = digest
        any_changed = True
        lead = re.search(r"^# .+?\n+(.+?)(?:\n\n|\n#)", page, re.S)
        hubs.append((topic, slug, (lead.group(1).strip() if lead else "")[:400], len(members)))
        print(
            f"  wrote topics/{slug}.md ({len(members)} concepts, {len(srcs)} projects, "
            f"{len(rel_conflicts)} conflicts)"
        )
    state_path.write_text(json.dumps(state, indent=1))
    # Retire hub pages for topics that no longer exist after re-clustering.
    live = {slugify(names.get(str(i), f"Topic {i}")) for i in range(len(clusters))}
    for stale in (OUT / "topics").glob("*.md"):
        if stale.stem not in live:
            stale.unlink()
            any_changed = True
            print(f"  removed stale topics/{stale.stem}.md")
    if not any_changed and (OUT / "index.md").exists():
        if refresh_corpus_line(OUT / "index.md", corpus_stats(ROOT)):
            print("home unchanged; corpus counts refreshed")
        else:
            print("home unchanged; done")
        return 1 if failures else 0

    write_home(hubs, corpus_stats(ROOT))
    for f in failures:
        print(f"  [ERROR] rejected: {f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
