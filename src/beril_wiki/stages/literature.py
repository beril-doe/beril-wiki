#!/usr/bin/env python3
"""Literature-review stage: place the corpus in the context of published work.

Runs after topic hubs are (re)generated. Per hub page (hash-cached on the
page WITHOUT its review section, so a regenerated hub automatically earns a
fresh review and an unchanged one is a no-op):

  1. the model proposes 2 PubMed queries for the topic,
  2. NCBI eutils fetches candidate papers (esearch + esummary, stdlib urllib),
  3. the model writes a "## Literature Context" review — what is established
     in the field and where this corpus's findings sit (novel / confirming /
     contrasting) — citing ONLY candidates, as [PMID 123...](pubmed url),
     from a packed prompt that agentic.prose gates, reviews and patches,
  4. code verifies every cited PMID is in the candidate set before any review;
     a section that does not converge is recorded as a failure and skipped,
  5. the section is spliced directly under the hub's lead paragraph.

check skips this section: its numbers come from external papers, not
corpus sources. State: state/litcontext.json.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python -m beril_wiki.stages.literature [--root DIR]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
import threading
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from beril_wiki import compiler as C
from beril_wiki.agentic.prose import (
    NO_PREAMBLE,
    PLATFORM,
    Contract,
    Issue,
    PageFailure,
    derived_page,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import WorkflowError, atomic_json, configured, digest, runtime
from beril_wiki.paths import ROOT

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SECTION = re.compile(r"^## Literature Context\s*\n.*?(?=\n## |\Z)", re.M | re.S)
PMID_LINK = re.compile(r"\[PMID (\d+)\]")
MAX_PAPERS = 20
NCBI = threading.Lock()  # parallel hubs must still respect NCBI's request rate

CONTRACT = Contract(
    rules=(
        "Write 300-500 words in 2-4 paragraphs (the code gate allows 10% either way).",
        "Begin with the heading '## Literature Context' and write nothing before it.",
        "First establish what is known in the field from the CANDIDATE PAPERS, then state "
        "explicitly where this corpus's findings sit: consistent with the literature, "
        "extending it, novel, or in tension with it, referring to corpus claims in prose.",
        "Cite every literature claim as [PMID <id>](https://pubmed.ncbi.nlm.nih.gov/<id>/) "
        "using only ids from the CANDIDATE PAPERS; cite only papers that are relevant; never "
        "cite anything else.",
        "Use only figures that appear in the CANDIDATE PAPERS or the HUB PAGE, copied exactly, "
        "and keep each paper's own caveats (sample size, single patient, in vitro) beside the "
        "claim; a null result stays null.",
        "Never use [src:] tags in this section; [[wikilinks]] may name pages the hub names.",
        "If no candidate is relevant, reply with exactly NONE.",
        NO_PREAMBLE.format(first="'## Literature Context'"),
        PLATFORM,
    ),
    words=(300, 500),
    first="## Literature Context",
    cite=False,
    empty="NONE",
)
TASK = "Write the '## Literature Context' section for the HUB PAGE."


def topic_core(text: str) -> str:
    """Canonical hub input, excluding this stage's section and splice whitespace."""
    return re.sub(r"\s+", " ", SECTION.sub("", text)).strip()


QUERY_USER = """\
Below is a topic-hub page from a microbial-biology research wiki. Propose two
PubMed search queries (plain keyword queries, no field tags) that would find
the published literature this topic's findings should be placed against —
one broad for the field's established knowledge, one narrow for the specific
phenomena the hub discusses.

{hub_text}

Return ONLY valid JSON: {{"queries": ["...", "..."]}}
"""


def eutils(endpoint: str, **params) -> dict:
    params |= {"db": "pubmed", "retmode": "json", "tool": "beril-wiki"}
    url = f"{EUTILS}/{endpoint}.fcgi?{urllib.parse.urlencode(params)}"
    with NCBI:
        time.sleep(0.4)  # NCBI courtesy limit without an API key
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.loads(r.read())


def fetch_candidates(queries: list[str]) -> dict[str, str]:
    """PMID -> one-line citation for up to MAX_PAPERS deduped results."""
    if configured():
        return fetch_abstracts(queries)
    ids: list[str] = []
    for q in queries[:2]:
        try:
            found = eutils("esearch", term=q, retmax=MAX_PAPERS // 2, sort="relevance")
            ids += [i for i in found["esearchresult"].get("idlist", []) if i not in ids]
        except Exception as e:  # network/NCBI hiccup: skip the query, not the run
            print(f"    [WARN] esearch failed for {q!r}: {e}")
    if not ids:
        return {}
    try:
        summ = eutils("esummary", id=",".join(ids[:MAX_PAPERS]))["result"]
    except Exception as e:
        print(f"    [WARN] esummary failed: {e}")
        return {}
    out = {}
    for pid in ids[:MAX_PAPERS]:
        doc = summ.get(pid)
        if not doc:
            continue
        first = (doc.get("sortfirstauthor") or "?").split()[0]
        out[pid] = (
            f"{first} et al., {doc.get('pubdate', '?')[:4]}, {doc.get('source', '?')} — "
            f"{doc.get('title', '?')}"
        )
    return out


def fetch_abstracts(queries: list[str]) -> dict[str, str]:
    """Cache PubMed abstract evidence, propagating network failures for retry."""
    cache = runtime().store / "papers"
    cache.mkdir(exist_ok=True)
    path = cache / f"{digest(queries[:2])}.json"
    if path.exists():
        return json.loads(path.read_text())
    ids = []
    for query_text in queries[:2]:
        result = eutils("esearch", term=query_text, retmax=MAX_PAPERS // 2, sort="relevance")
        ids.extend(i for i in result["esearchresult"].get("idlist", []) if i not in ids)
    if not ids:
        path.write_text("{}")
        return {}
    if any(not re.fullmatch(r"\d+", pid) for pid in ids):
        raise WorkflowError("PubMed returned an invalid identifier")
    url = f"{EUTILS}/efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(ids[:MAX_PAPERS]), "retmode": "xml", "tool": "beril-wiki"}
    )
    with NCBI:
        time.sleep(0.4)
        with urllib.request.urlopen(url, timeout=30) as response:
            raw = response.read(2_000_001)
    if len(raw) > 2_000_000:
        raise WorkflowError("PubMed response exceeds 2MB")
    result = abstracts_from_xml(raw, set(ids))
    path.write_text(json.dumps(result, indent=2))
    return result


def abstracts_from_xml(raw: bytes, allowed: set[str]) -> dict[str, str]:
    result = {}
    for article in ET.fromstring(raw).findall(".//PubmedArticle"):
        pid = article.findtext(".//MedlineCitation/PMID", "")
        title_node = article.find(".//ArticleTitle")
        title = "".join(title_node.itertext()) if title_node is not None else ""
        abstract = "\n".join(
            "".join(node.itertext()) for node in article.findall(".//AbstractText")
        )
        if pid in allowed and abstract.strip():
            result[pid] = f"{title}\nABSTRACT (not full text):\n{abstract}"
    return result


def review_hub(page: pathlib.Path, system: str) -> str | None:
    """The accepted section for a hub, or None when nothing should be spliced."""
    body = page.read_text(encoding="utf-8", errors="replace")
    stripped = SECTION.sub("", body)
    hub_text = stripped[: None if configured() else 12000]

    q_raw = C.llm(
        [
            {"role": "system", "content": system},
            {"role": "user", "content": QUERY_USER.format(hub_text=hub_text)},
        ],
        f"lit/{page.stem}/queries",
    )
    queries = [q for q in (C.parse_json_reply(q_raw).get("queries") or []) if isinstance(q, str)]
    papers = fetch_candidates(queries)
    if not papers:
        # Model queries can be too narrow for PubMed; fall back to the title.
        h1 = re.search(r"^# (.+)$", stripped, re.M)
        title = re.sub(r"[^\w\s-]", " ", h1.group(1)) if h1 else page.stem.replace("-", " ")
        papers = fetch_candidates([f"{title} bacteria", title])
    if not papers:
        print(f"    {page.stem}: no candidate papers — skipping")
        return None

    paper_block = "\n".join(f"- PMID {pid}: {cite}" for pid, cite in papers.items())
    pack = (
        f"HUB PAGE:\n\n{hub_text}\n\nCANDIDATE PAPERS (the only citable literature):\n{paper_block}"
    )

    def cited_candidates(parts: list[str]) -> list[Issue]:
        return [
            Issue(paragraph=i, category="citation", quote=f"PMID {pid}", note="not a candidate")
            for i, part in enumerate(parts)
            for pid in PMID_LINK.findall(part)
            if pid not in papers
        ]

    section = derived_page(
        f"lit/{page.stem}/section",
        CONTRACT,
        TASK,
        pack,
        allowed=pack,
        sources={},
        valid_ids=set(),
        extra=cited_candidates,
    )
    if section == "NONE":
        print(f"    {page.stem}: model found no relevant candidates")
        return None
    return section


def splice(page: pathlib.Path, section: str) -> None:
    """Under the lead: after H1 + first paragraph, before the first H2."""
    stripped = SECTION.sub("", page.read_text(encoding="utf-8", errors="replace"))
    m = re.search(r"\n## ", stripped)
    at = m.start() if m else len(stripped)
    page.write_text(
        stripped[:at].rstrip() + "\n\n" + section.strip() + "\n" + stripped[at:], encoding="utf-8"
    )


def main(root: pathlib.Path) -> int:
    topics = root / "wiki" / "topics"
    if not topics.is_dir():
        print("stages.literature: no topic hubs yet — run stages.topics first")
        return 0
    system = C.SYSTEM.format(contract=(ROOT / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    state_path = root / "state" / "litcontext.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    if "--force" in sys.argv:
        state = {}
        print("  --force: ignoring cached digests")

    todo = []
    for page in sorted(topics.glob("*.md")):
        page_digest = hashlib.sha256(
            topic_core(page.read_text(encoding="utf-8", errors="replace")).encode()
        ).hexdigest()[:16]
        if state.get(page.name) == page_digest:
            continue
        todo.append((page, page_digest))
    skipped = len(list(topics.glob("*.md"))) - len(todo)

    done = failed = 0
    for (page, page_digest), result in parallel(
        todo, lambda item: review_hub(item[0], system), workers()
    ):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"lit/{page.name}", result)
            print(f"  [FAILED] lit/{page.stem}: {result}")
            continue  # a failed section stays dirty for the next run
        if result is not None:
            splice(page, result)
        record_failure(f"lit/{page.name}", None)
        state[page.name] = page_digest
        atomic_json(state_path, state)
        done += 1
    prune_failures("lit/", {f"lit/{p.name}" for p in topics.glob("*.md")})

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    usage = (
        "usage recorded in the shared agentic ledger"
        if configured()
        else f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)"
    )
    print(
        f"stages.literature: {done} hub(s) reviewed, {skipped} unchanged, "
        f"{failed} failure(s); " + usage
    )
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=ROOT)
    sys.exit(main(ap.parse_args().root))
