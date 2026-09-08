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
  4. code verifies every cited PMID is in the candidate set (one retry, then
     skip — a fabricated reference never ships),
  5. the section is spliced directly under the hub's lead paragraph.

wiki_check skips this section: its numbers come from external papers, not
corpus sources. State: state/litcontext.json. Uses compile.py's llm() so the
COMPILE_BUDGET_USD tripwire covers this stage too.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python pipeline/lit_context.py [--root DIR]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

import compile as C
import okf

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SECTION = re.compile(r"^## Literature Context\s*\n.*?(?=\n## |\Z)", re.M | re.S)
PMID_LINK = re.compile(r"\[PMID (\d+)\]")
MAX_PAPERS = 20

QUERY_USER = """\
Below is a topic-hub page from a microbial-biology research wiki. Propose two
PubMed search queries (plain keyword queries, no field tags) that would find
the published literature this topic's findings should be placed against —
one broad for the field's established knowledge, one narrow for the specific
phenomena the hub discusses.

{hub_text}

Return ONLY valid JSON: {{"queries": ["...", "..."]}}
"""

REVIEW_USER = """\
Write a "## Literature Context" section for the topic-hub page above: a
literature review (300-500 words, 2-4 paragraphs) that places this corpus's
findings in the context of published work.

Candidate papers (the ONLY citable literature — do not cite anything else):
{papers}

Requirements:
- First establish what is known in the field from the candidates, then state
  explicitly where this corpus's findings sit: which are consistent with the
  literature, which extend it, and which are novel or in tension with it —
  referring to corpus claims in prose (you may use [[wikilinks]] to pages
  named in the hub, but do NOT use [src:] tags in this section).
- Cite every literature claim as [PMID <id>](https://pubmed.ncbi.nlm.nih.gov/<id>/)
  using ONLY ids from the candidate list. Do not invent citations. Only cite
  papers actually relevant; ignore irrelevant candidates.
- If no candidate is relevant, return exactly: NONE

Return ONLY the section Markdown starting with "## Literature Context"
(no fences, no JSON).
"""


def eutils(endpoint: str, **params) -> dict:
    params |= {"db": "pubmed", "retmode": "json", "tool": "beril-wiki"}
    url = f"{EUTILS}/{endpoint}.fcgi?{urllib.parse.urlencode(params)}"
    time.sleep(0.4)  # NCBI courtesy limit without an API key
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read())


def fetch_candidates(queries: list[str]) -> dict[str, str]:
    """PMID -> one-line citation for up to MAX_PAPERS deduped results."""
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
        out[pid] = f"{first} et al., {doc.get('pubdate', '?')[:4]}, {doc.get('source', '?')} — {doc.get('title', '?')}"
    return out


def review_hub(page: pathlib.Path, system: str) -> bool:
    body = page.read_text(encoding="utf-8", errors="replace")
    stripped = SECTION.sub("", body)
    hub_text = stripped[:12000]

    q_raw = C.llm([{"role": "system", "content": system},
                   {"role": "user", "content": QUERY_USER.format(hub_text=hub_text)}],
                  f"lit/{page.stem}/queries")
    queries = [q for q in (C.parse_json_reply(q_raw).get("queries") or []) if isinstance(q, str)]
    papers = fetch_candidates(queries)
    if not papers:
        # Model queries can be too narrow for PubMed; fall back to the title.
        h1 = re.search(r"^# (.+)$", stripped, re.M)
        title = re.sub(r"[^\w\s-]", " ", h1.group(1)) if h1 else page.stem.replace("-", " ")
        papers = fetch_candidates([f"{title} bacteria", title])
    if not papers:
        print(f"    {page.stem}: no candidate papers — skipping")
        return False

    paper_block = "\n".join(f"- PMID {pid}: {cite}" for pid, cite in papers.items())
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": f"TOPIC-HUB PAGE:\n\n{hub_text}"},
                {"role": "user", "content": REVIEW_USER.format(papers=paper_block)}]
    section = C.llm(messages, f"lit/{page.stem}/review").strip()
    bad = [p for p in PMID_LINK.findall(section) if p not in papers]
    if bad or (not section.startswith("## Literature Context") and section != "NONE"):
        why = f"cited PMIDs not in candidate list: {bad}" if bad else "reply must start with '## Literature Context' or be NONE"
        section = C.llm(messages + [{"role": "assistant", "content": section},
                                    {"role": "user", "content": f"Invalid: {why}. Rewrite the section fixing this."}],
                        f"lit/{page.stem}/retry").strip()
        bad = [p for p in PMID_LINK.findall(section) if p not in papers]
        if bad or (not section.startswith("## Literature Context") and section != "NONE"):
            print(f"    [ERROR] lit/{page.stem}: invalid after retry — section not added")
            C._failures.append(f"lit:{page.stem}")
            return False
    if section == "NONE":
        print(f"    {page.stem}: model found no relevant candidates")
        return False

    # Splice under the lead: after H1 + first paragraph, before the first H2.
    m = re.search(r"\n## ", stripped)
    at = m.start() if m else len(stripped)
    okf.write(page, stripped[:at].rstrip() + "\n\n" + section.strip() + "\n" + stripped[at:], encoding="utf-8")
    return True


def main(root: pathlib.Path) -> int:
    topics = root / "wiki-extra" / "topics"
    if not topics.is_dir():
        print("lit_context: no topic hubs yet — run topics_build first")
        return 0
    system = C.SYSTEM.format(contract=(C.REPO / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    state_path = root / "state" / "litcontext.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    if "--force" in sys.argv:
        state = {}
        print("  --force: ignoring cached digests")

    done = skipped = 0
    for page in sorted(topics.glob("*.md")):
        digest = hashlib.sha256(SECTION.sub("", page.read_text(encoding="utf-8", errors="replace")).encode()).hexdigest()[:16]
        if state.get(page.name) == digest:
            skipped += 1
            continue
        print(f"  reviewing {page.name}")
        n_fail = len(C._failures)
        try:
            review_hub(page, system)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"    [ERROR] lit/{page.stem}: {e}")
            C._failures.append(f"lit:{page.stem}")
            continue
        if len(C._failures) > n_fail:
            continue  # failed review stays dirty for the next run
        state[page.name] = digest
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))
        done += 1

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(f"lit_context: {done} hub(s) reviewed, {skipped} unchanged, {len(C._failures)} failure(s); "
          f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)")
    return 1 if C._failures else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=C.REPO)
    sys.exit(main(ap.parse_args().root))
