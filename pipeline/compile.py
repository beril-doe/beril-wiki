#!/usr/bin/env python3
"""First-party wiki compiler — replaces OpenKB's `openkb add`.

Per new/changed staged doc (content hash vs state/hashes.json, sequential,
oldest-first by project id):
  1 summarize   -> wiki/summaries/  (dense, exact numbers, [src:] tags,
                   ends with ## Slots Into)
  2 plan        -> one call against the live concept/entity index + the
                   duplicate-concept audit; new concepts need justification
  3 merge-rewrite each touched concept/entity page (typed relations in prose)
  4 validate at write time: [src:] ids known, flagged numbers present in a
    cited source, wikilink targets exist or are created this run. One retry
    with violations quoted; second failure keeps the old page, logs [ERROR],
    and the run exits nonzero.
  5 index.md + log.md maintained deterministically in code.

Prompts start from OpenKB's compiler (Apache-2.0 — attribution in /LICENSE),
merged with contract/AGENTS.md, which is injected into every call and remains
the runtime-editable rulebook.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python pipeline/compile.py [--root DIR] [doc.md ...]

# ponytail: full-page rewrite per touched page; sectioned append if >500 docs
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import shutil
import sys

import yaml
from litellm import completion

from wiki_check import NUMBER, SRC_TAG, cited_ids, duplicate_concepts, is_table_or_links, norm_num, paragraphs

HERE = pathlib.Path(__file__).parent
REPO = HERE.parent
MODEL = os.environ.get("COMPILE_MODEL", "openai/claude-sonnet-5")
# Merge-rewrites re-emit the FULL page: the corpus's hot hub pages are 27-44KB
# (9-15k tokens of content), so 8k and even 16k caps truncated their merges
# (parity runs 2026-09-01). 32k covers the largest page plus growth headroom;
# the ~25% length rule in the update prompts polices bloat separately.
MAX_TOKENS = 32768
# Budget guard: estimated at Anthropic Sonnet list price ($3/$15 per Mtok);
# CBORG bills LBL, so this is a tripwire, not an invoice.
BUDGET_USD = float(os.environ.get("COMPILE_BUDGET_USD", "5"))
PRICE_IN, PRICE_OUT = 3e-6, 15e-6

ENTITY_TYPES = ("organism", "gene_or_pathway", "compound", "method", "dataset", "place", "person", "other")
WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:[#|][^\]]*)?\]\]")
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

_usage = {"in": 0, "out": 0}
_failures: list[str] = []

# ---------------------------------------------------------------------------
# Prompts (lifted from OpenKB's compiler, merged with contract/AGENTS.md)
# ---------------------------------------------------------------------------

SYSTEM = """\
You are the BERIL wiki compilation agent. You compile AI-conducted research-project
reports into a hub-structured scientific wiki: per-document summary pages plus
cross-document concept and entity pages, following the editorial contract below.

{contract}

Write all content in English. Use [[wikilinks]] to connect related pages
(e.g. [[concepts/gene-essentiality]]). Never emit YAML frontmatter (---) in
generated content; it is managed by code.
"""

KNOWN_TARGETS_USER = """\
The wiki currently contains these pages, and they (plus any pages explicitly
planned for creation in this run) are the COMPLETE list of valid [[wikilink]]
targets in the responses that follow:

{targets}

Do NOT invent new wikilink targets. To mention a concept or entity that is not
in the whitelist, write it as plain text without brackets.
"""

SUMMARY_USER = """\
New document: {fname} (source id: {sid})

Full text:
{content}

Write the summary page for this document in Markdown: dense and faithful,
preserving exact numbers (never round, estimate, or reconcile), every factual
paragraph ending with its [src: {sid}] citation tag. Start with an H1 title,
then ## Overview, then the key findings with their exact numbers, then the
caveats the document itself states. End the page with a ## Slots Into section
listing the concept pages these findings feed, one bullet each:
"- [[concepts/<slug>]] — which finding and why". Use existing concept slugs
from the whitelist where they fit; a finding that fits no existing concept may
name a new slug (the planning step will decide whether to create it).

Return a JSON object with two keys:
- "description": a single sentence (under 100 chars) describing the document's main contribution
- "content": the full summary page in Markdown

Return ONLY valid JSON, no fences.
"""

PLAN_USER = """\
Based on the summary above, decide how to update the wiki's CONCEPT pages and
ENTITY pages.

A CONCEPT is an abstract recurring idea/pattern/mechanism. An ENTITY is a
specific named thing (see the entity-type rules in the system message). Each
name goes in exactly ONE group.

Existing concept pages:
{concept_briefs}

Existing entity pages (source counts = how many docs already cite them):
{entity_briefs}

Current duplicate-concept audit (near-duplicate pairs already in the wiki —
do not deepen these, and do not add a third page overlapping either member):
{dup_report}

Return a JSON object with two top-level keys, "concepts" and "entities".

"concepts" is an object with:
1. "create" — new concepts: array of {{"name": "concept-slug", "title": "Title",
   "justification": "REQUIRED — why no existing page covers this phenomenon;
   name the closest existing page and why extending it would be wrong"}}
2. "update" — existing concepts with significant new evidence: array of
   {{"name": "slug", "title": "Title"}}
3. "related" — existing concept slugs to cross-link only: array of strings.

"entities" has the same three keys, but create/update objects add a "type"
field, one of: {entity_types}.

Rules:
- Prefer "update" over "create": extend, don't duplicate. A create without a
  convincing justification is rejected by the pipeline.
- Claim-delta integration: update the smallest set of pages that captures what
  this document strengthens, weakens, redirects, or makes newly testable.
  Typically 2-6 concept creates+updates per document.
- Create an entity page only when the entity is central to this document or
  recurs across sources; 5-15 per rich document, fewer for sparse ones.
- Do NOT create a concept that is just the document's topic itself.

Return ONLY valid JSON, no fences, no explanation.
"""

CONCEPT_CREATE_USER = """\
Write the concept page for: {title} (file: concepts/{name}.md)

This concept was planned from document "{sid}", whose summary is above.

Requirements (per the editorial contract):
- H1 title, clear explanation, the key evidence with exact numbers copied from
  the summary — never invent or round numbers.
- EVERY factual claim ends with a [src: <project_id>] tag ({sid} for this
  document's findings).
- Link [[summaries/{summary_stem}]] and related pages, subject to the
  whitelist rules above.
- End with ## Open Directions (each entry: data + method + question).

Return a JSON object with two keys:
- "description": a single sentence (under 100 chars) defining this concept
- "content": the full concept page in Markdown

Return ONLY valid JSON, no fences.
"""

CONCEPT_UPDATE_USER = """\
Update the concept page: {title} (file: concepts/{name}.md)

Current content of this page:
{existing}

Merge-rewrite this page to integrate the new evidence from document "{sid}"
(summary above) — do not just append. Rules:
- Preserve ALL existing claims, numbers, and citations; never delete, weaken,
  or alter existing evidence.
- Where new evidence sits adjacent to an existing claim, state the relation
  explicitly in prose: "this **supports** ...", "this **contradicts** ...",
  or "this **refines** ..." — never just add a parallel fact.
- If the new evidence disagrees with an existing claim, record it under a
  ## Tensions section citing each side; never resolve by averaging or by
  silently preferring one side.
- Every NEW factual claim ends with [src: {sid}]; numbers copied exactly.
- Follow the wikilink whitelist rules above; add [[summaries/{summary_stem}]].
- Keep (and extend if warranted) the ## Open Directions ending.
- Keep the merged page TIGHT: at most ~25% longer than the current page.
  Weave the new evidence into existing sections; do not restate the summary's
  result tables (fine detail lives on the summary page, cite and link it).
  This is a claim-delta merge, not a second report.

Return a JSON object with two keys:
- "description": a single sentence (under 100 chars) defining this concept (may change)
- "content": the full rewritten page in Markdown

Return ONLY valid JSON, no fences.
"""

ENTITY_CREATE_USER = """\
Write the entity page for: {title} (type: {etype}, file: entities/{name}.md)

This entity relates to document "{sid}", summarized above.

Requirements: H1 title first, then what this entity is (canonical name; list
known aliases and any stable external identifier), the key facts about it from
this document with
exact numbers, every factual claim ending with [src: {sid}], and [[wikilinks]]
to related pages including [[summaries/{summary_stem}]] — subject to the
whitelist rules above.

Return a JSON object with three keys:
- "description": a single sentence (under 100 chars) identifying this entity
- "type": one of {entity_types}
- "content": the full entity page in Markdown

Return ONLY valid JSON, no fences.
"""

ENTITY_UPDATE_USER = """\
Update the entity page: {title} (type: {etype}, file: entities/{name}.md)

Current content of this page:
{existing}

Merge-rewrite to integrate the new facts about this entity from document
"{sid}" (summary above) — do not just append. Preserve all existing claims,
numbers, and citations; state relations to adjacent existing claims explicitly
(**supports** / **contradicts** / **refines**); every new claim ends with
[src: {sid}]; numbers copied exactly; follow the whitelist rules above and add
[[summaries/{summary_stem}]]. Keep the merged page TIGHT: at most ~25% longer
than the current page — weave the new facts in, do not restate the summary
(fine detail lives on the summary page, cite and link it).

Return a JSON object with three keys:
- "description": a single sentence (under 100 chars) identifying this entity
- "type": one of {entity_types}
- "content": the full rewritten page in Markdown

Return ONLY valid JSON, no fences.
"""

RETRY_USER = """\
Your page failed write-time validation:

{violations}

Rewrite the FULL page fixing every violation:
- an unknown [src:] id: correct it to a real source id or remove the claim
- a number not found in its cited source: use the source's exact number or drop it
- a paragraph with figures but no citation: add the correct [src:] tag
- a wikilink to a nonexistent page: convert it to plain text
Do not otherwise change the page. Return the same JSON shape as before.
Return ONLY valid JSON, no fences.
"""


# ---------------------------------------------------------------------------
# LLM + parsing helpers
# ---------------------------------------------------------------------------


class PageError(Exception):
    """A generated page was rejected (truncated or failed validation twice)."""


def llm(messages: list[dict], step: str) -> str:
    est = _usage["in"] * PRICE_IN + _usage["out"] * PRICE_OUT
    if est > BUDGET_USD:
        raise SystemExit(f"[ERROR] budget cap ${BUDGET_USD:.2f} exceeded (est ${est:.2f}) — stopping before {step}")
    resp = completion(
        model=MODEL,
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
        messages=messages,
        temperature=0.2, timeout=600, max_tokens=MAX_TOKENS,
    )
    u = resp.usage
    _usage["in"] += u.prompt_tokens
    _usage["out"] += u.completion_tokens
    print(f"    {step}: in={u.prompt_tokens} out={u.completion_tokens}")
    if resp.choices[0].finish_reason == "length":
        raise PageError(f"{step}: hit the {MAX_TOKENS}-token cap — refusing a truncated page")
    return (resp.choices[0].message.content or "").strip()


def parse_json_reply(text: str) -> dict:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-z]*\n|\n```$", "", t)
    m = re.search(r"\{.*\}", t, re.S)
    if not m:
        raise ValueError(f"no JSON object in reply: {t[:120]!r}")
    # strict=False: models sometimes emit raw control chars inside strings.
    obj = json.loads(m.group(0), strict=False)
    if not isinstance(obj, dict):
        raise ValueError(f"expected JSON object, got {type(obj).__name__}")
    return obj


def parse_fm(text: str) -> tuple[dict, str]:
    m = FM.match(text)
    if not m:
        return {}, text
    return (yaml.safe_load(m.group(1)) or {}), text[m.end():]


def fm_block(fields: dict) -> str:
    return "---\n" + "".join(f"{k}: {json.dumps(v)}\n" for k, v in fields.items()) + "---\n"


def fm_entity_type(etype: str) -> str:
    return "_".join(p.capitalize() for p in etype.split("_"))


# ---------------------------------------------------------------------------
# Write-time validation (the core upgrade over OpenKB)
# ---------------------------------------------------------------------------


def wikilink_targets(root: pathlib.Path) -> set[str]:
    return {
        str(f.relative_to(base)).removesuffix(".md")
        for base in (root / "wiki", root / "wiki-extra") if base.is_dir()
        for f in base.rglob("*.md")
    }


def validate_page(content: str, sources: dict[str, str], targets: set[str],
                  require_slots: bool = False, check_links: bool = True) -> list[str]:
    v: list[str] = []
    if not content.strip():
        return ["empty page content"]
    for i, par in enumerate(paragraphs(content), 1):
        ids = cited_ids(par)
        for s in ids:
            if s not in sources:
                v.append(f"paragraph {i}: unknown source id [src: {s}]")
        nums = NUMBER.findall(SRC_TAG.sub("", par))
        known = [s for s in ids if s in sources]
        if nums and not ids and not is_table_or_links(par):
            v.append(f"paragraph {i}: contains figure(s) {nums[:4]} but no [src:] citation: {par[:80]!r}")
        elif nums and known:
            pool = "".join(sources[s] for s in known).replace(",", "")
            for tok in nums:
                if norm_num(tok) not in pool:
                    v.append(f"paragraph {i}: number {tok!r} not found in cited source(s) {known}")
    if check_links:
        for m in WIKILINK.finditer(content):
            t = m.group(1).strip().lstrip("/")
            if t not in targets:
                v.append(f"wikilink [[{t}]] targets a page that does not exist")
    if require_slots and "## Slots Into" not in content:
        v.append("summary must end with a '## Slots Into' section")
    return v


def downgrade_dead_links(text: str, targets: set[str]) -> str:
    """Deterministic fallback for links validation can't save (e.g. a Slots
    Into slug the plan declined to create): keep the label, drop the brackets."""
    def repl(m: re.Match) -> str:
        t = m.group(1).strip().lstrip("/")
        if t in targets:
            return m.group(0)
        label = m.group(2) or t.rsplit("/", 1)[-1].replace("-", " ")
        return label
    return re.sub(r"\[\[([^\]|#]+?)(?:\|([^\]]*))?\]\]", repl, text)


def generate_page(messages: list[dict], step: str, sources: dict[str, str],
                  targets: set[str], require_slots: bool = False, check_links: bool = True) -> dict:
    """One LLM page call + write-time validation with a single violation-quoting
    retry. Raises PageError on second failure (caller keeps the old page)."""
    def attempt(msgs: list[dict], name: str) -> tuple[str, dict | None, list[str]]:
        raw = llm(msgs, name)
        try:
            obj = parse_json_reply(raw)
        except (json.JSONDecodeError, ValueError) as e:
            # A malformed reply costs the page a retry, never the whole doc.
            return raw, None, [f"your reply was not parseable JSON ({e}) — resend the SAME page as one valid JSON object"]
        return raw, obj, validate_page(obj.get("content") or "", sources, targets, require_slots, check_links)

    raw, obj, violations = attempt(messages, step)
    if violations:
        print(f"    {step}: {len(violations)} violation(s), retrying")
        retry = messages + [
            {"role": "assistant", "content": raw},
            {"role": "user", "content": RETRY_USER.format(violations="\n".join(f"- {x}" for x in violations))},
        ]
        raw, obj, violations = attempt(retry, f"{step}/retry")
        if violations:
            raise PageError(f"{step}: still invalid after retry: " + "; ".join(violations[:5]))
    return obj


# ---------------------------------------------------------------------------
# Corpus bookkeeping (deterministic, code-owned)
# ---------------------------------------------------------------------------


def page_briefs(d: pathlib.Path, with_sources: bool = False) -> str:
    lines = []
    for p in sorted(d.glob("*.md")):
        fm, _ = parse_fm(p.read_text(encoding="utf-8", errors="replace"))
        desc = str(fm.get("description") or "").strip()
        if with_sources:
            n = len(fm.get("sources") or [])
            etype = str(fm.get("type") or "other").lower()
            lines.append(f"- {p.stem} ({etype}, {n} sources) — {desc}")
        else:
            lines.append(f"- {p.stem}: {desc}")
    return "\n".join(lines) or "(none yet)"


def merge_sources(fm: dict, summary_path: str) -> list[str]:
    srcs = [s for s in (fm.get("sources") or []) if isinstance(s, str)]
    if summary_path not in srcs:
        srcs.append(summary_path)
    return srcs


def rebuild_index(root: pathlib.Path) -> None:
    wiki = root / "wiki"
    lines = ["# Knowledge Base Index", "", "## Documents"]
    for p in sorted((wiki / "summaries").glob("*.md"), reverse=True):
        fm, _ = parse_fm(p.read_text(encoding="utf-8", errors="replace"))
        lines.append(f"- [[summaries/{p.stem}]] (short) — {fm.get('description', '')}")
    lines += ["", "## Concepts"]
    for p in sorted((wiki / "concepts").glob("*.md")):
        fm, _ = parse_fm(p.read_text(encoding="utf-8", errors="replace"))
        lines.append(f"- [[concepts/{p.stem}]] — {fm.get('description', '')}")
    lines += ["", "## Entities"]
    for p in sorted((wiki / "entities").glob("*.md")):
        fm, _ = parse_fm(p.read_text(encoding="utf-8", errors="replace"))
        etype = str(fm.get("type") or "other").lower()
        lines.append(f"- [[entities/{p.stem}]] ({etype}) — {fm.get('description', '')}")
    (wiki / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_log(root: pathlib.Path, fname: str) -> None:
    log = root / "wiki" / "log.md"
    if not log.exists():
        log.write_text("# Operations Log\n", encoding="utf-8")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log.open("a", encoding="utf-8") as f:
        f.write(f"\n## [{ts}] ingest | {fname}\n")


# ---------------------------------------------------------------------------
# Per-document compile
# ---------------------------------------------------------------------------


def normalize_plan(plan: dict, root: pathlib.Path) -> dict:
    """Enforce extend-don't-duplicate: an existing name is always an update; a
    create without justification is rejected loudly."""
    out = {"concepts": {"create": [], "update": []}, "entities": {"create": [], "update": []}}
    for group, subdir in (("concepts", "concepts"), ("entities", "entities")):
        g = plan.get(group) or {}
        seen: set[str] = set()
        for kind in ("create", "update"):
            for it in (g.get(kind) or []):
                if not isinstance(it, dict) or not isinstance(it.get("name"), str) or not it["name"].strip():
                    continue
                name = re.sub(r"[^\w.-]+", "-", it["name"].strip()).strip("-")
                if name in seen:
                    continue
                seen.add(name)
                item = {"name": name, "title": it.get("title") or name}
                if group == "entities":
                    etype = it.get("type")
                    item["type"] = etype if etype in ENTITY_TYPES else "other"
                exists = (root / "wiki" / subdir / f"{name}.md").exists()
                if exists:
                    out[group]["update"].append(item)
                elif kind == "create":
                    if group == "concepts" and not str(it.get("justification") or "").strip():
                        print(f"    [WARN] rejecting unjustified new concept {name!r}")
                        continue
                    out[group]["create"].append(item)
                else:
                    print(f"    [WARN] plan updated nonexistent {group[:-1]} {name!r} — treating as create")
                    out[group]["create"].append(item)
    return out


def compile_doc(root: pathlib.Path, fname: str, sources: dict[str, str], system: str) -> None:
    wiki = root / "wiki"
    sid = re.sub(r"__REPORT$", "", pathlib.Path(fname).stem)
    stem = pathlib.Path(fname).stem
    summary_rel = f"summaries/{stem}.md"
    targets = wikilink_targets(root) | {f"summaries/{stem}"}

    def whitelist_msg(tg: set[str]) -> dict:
        return {"role": "user", "content": KNOWN_TARGETS_USER.format(targets="\n".join(f"- {t}" for t in sorted(tg)))}

    # 1 — summarize. Wikilinks are NOT validated here: Slots Into may name new
    # slugs the plan hasn't ruled on yet; dead ones are downgraded in code below.
    summary_obj = generate_page(
        [{"role": "system", "content": system}, whitelist_msg(targets),
         {"role": "user", "content": SUMMARY_USER.format(fname=fname, sid=sid, content=sources[sid])}],
        f"{sid}/summary", sources, targets, require_slots=True, check_links=False,
    )
    summary_md = summary_obj["content"]

    # 2 — plan
    plan_raw = llm(
        [{"role": "system", "content": system},
         {"role": "user", "content": f"New document summary for {fname}:\n\n{summary_md}"},
         {"role": "user", "content": PLAN_USER.format(
             concept_briefs=page_briefs(wiki / "concepts"),
             entity_briefs=page_briefs(wiki / "entities", with_sources=True),
             dup_report="\n".join(duplicate_concepts(root)) or "(no duplicates flagged)",
             entity_types=", ".join(ENTITY_TYPES))}],
        f"{sid}/plan")
    plan = normalize_plan(parse_json_reply(plan_raw), root)

    # Planned creations become valid wikilink targets for every page this run.
    for group, sub in (("concepts", "concepts"), ("entities", "entities")):
        for it in plan[group]["create"]:
            targets.add(f"{sub}/{it['name']}")

    # Summary links that the plan declined to create get downgraded in code.
    (wiki / "summaries").mkdir(parents=True, exist_ok=True)
    (wiki / "sources").mkdir(parents=True, exist_ok=True)
    (wiki / "summaries" / f"{stem}.md").write_text(
        fm_block({"type": "Summary", "description": summary_obj.get("description", ""),
                  "doc_type": "short", "full_text": f"sources/{fname}"})
        + downgrade_dead_links(summary_md, targets).strip() + "\n", encoding="utf-8")
    shutil.copy2(root / "staging" / fname, wiki / "sources" / fname)

    # 3 — merge-rewrite each touched page
    summary_ctx = {"role": "user", "content": f"Summary of the new document {fname} (source id {sid}):\n\n{summary_md}"}
    jobs = (
        [("concepts", it) for it in plan["concepts"]["update"] + plan["concepts"]["create"]]
        + [("entities", it) for it in plan["entities"]["update"] + plan["entities"]["create"]]
    )
    for group, it in jobs:
        name, title = it["name"], it["title"]
        path = wiki / group / f"{name}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        old_fm, old_body = parse_fm(path.read_text(encoding="utf-8", errors="replace")) if path.exists() else ({}, "")
        if old_body and summary_rel in (old_fm.get("sources") or []):
            # ponytail: resume-skip assumes a report is stable once integrated;
            # drop this guard if source reports start mutating after ingest.
            print(f"    {sid}/{group}/{name}: already integrated — skipping (resume)")
            continue
        if group == "concepts":
            task = (CONCEPT_UPDATE_USER.format(title=title, name=name, sid=sid, existing=old_body, summary_stem=stem)
                    if old_body else
                    CONCEPT_CREATE_USER.format(title=title, name=name, sid=sid, summary_stem=stem))
        else:
            etype = it.get("type") or str(old_fm.get("type") or "other").lower()
            task = (ENTITY_UPDATE_USER.format(title=title, name=name, sid=sid, etype=etype,
                                              existing=old_body, summary_stem=stem, entity_types=", ".join(ENTITY_TYPES))
                    if old_body else
                    ENTITY_CREATE_USER.format(title=title, name=name, sid=sid, etype=etype,
                                              summary_stem=stem, entity_types=", ".join(ENTITY_TYPES)))
        try:
            obj = generate_page(
                [{"role": "system", "content": system}, whitelist_msg(targets), summary_ctx,
                 {"role": "user", "content": task}],
                f"{sid}/{group}/{name}", sources, targets)
        except PageError as e:
            print(f"    [ERROR] {e} — keeping old version" if old_body else f"    [ERROR] {e} — page not created")
            _failures.append(f"{sid}: {group}/{name}")
            targets.discard(f"{group}/{name}")
            continue
        fm = {"type": "Concept", "description": obj.get("description", ""),
              "sources": merge_sources(old_fm, summary_rel)}
        if group == "entities":
            etype = obj.get("type") if obj.get("type") in ENTITY_TYPES else (it.get("type") or "other")
            fm["type"] = fm_entity_type(etype)
        path.write_text(fm_block(fm) + obj["content"].strip() + "\n", encoding="utf-8")

    # 5 — deterministic bookkeeping
    rebuild_index(root)
    append_log(root, fname)


# ---------------------------------------------------------------------------


def load_sources(root: pathlib.Path) -> dict[str, str]:
    return {
        re.sub(r"__REPORT$", "", f.stem): f.read_text(encoding="utf-8", errors="replace")
        for f in (root / "staging").glob("*.md")
    }


def main(root: pathlib.Path, only: list[str] | None = None) -> int:
    sources = load_sources(root)
    if not sources:
        print(f"compile: no staged docs under {root}/staging", file=sys.stderr)
        return 1
    system = SYSTEM.format(contract=(REPO / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    state_path = root / "state" / "hashes.json"
    state_path.parent.mkdir(exist_ok=True)
    hashes = json.loads(state_path.read_text()) if state_path.exists() else {}

    docs = sorted(f.name for f in (root / "staging").glob("*.md"))
    if only:
        docs = [d for d in docs if d in only]
    done = skipped = 0
    for fname in docs:
        digest = hashlib.sha256((root / "staging" / fname).read_bytes()).hexdigest()
        if hashes.get(fname) == digest:
            skipped += 1
            continue
        print(f"  compiling {fname}")
        n_fail_before = len(_failures)
        try:
            compile_doc(root, fname, sources, system)
        except (PageError, ValueError, json.JSONDecodeError) as e:
            print(f"    [ERROR] {fname}: {e} — doc not integrated")
            _failures.append(fname)
            continue
        if len(_failures) > n_fail_before:
            # Rejected pages leave the doc dirty so the next run retries them.
            print(f"    [ERROR] {fname}: {len(_failures) - n_fail_before} page(s) rejected — doc left dirty for re-run")
            continue
        hashes[fname] = digest
        state_path.write_text(json.dumps(hashes, indent=1, sort_keys=True))
        done += 1

    est = _usage["in"] * PRICE_IN + _usage["out"] * PRICE_OUT
    print(f"compile: {done} doc(s) compiled, {skipped} unchanged, {len(_failures)} failure(s); "
          f"tokens in={_usage['in']} out={_usage['out']} (~${est:.2f} est)")
    for f in _failures:
        print(f"  [ERROR] rejected: {f}")
    return 1 if _failures else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=REPO)
    ap.add_argument("docs", nargs="*", help="restrict to these staged filenames")
    args = ap.parse_args()
    sys.exit(main(args.root, args.docs or None))
