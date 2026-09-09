# BERIL Wiki — Design & Build Brief

This repo is the standalone home of the BERIL knowledge wiki: a compiled,
hub-structured scientific wiki over the BERIL Research Observatory's project
corpus (~73 AI-conducted microbial-biology research reports, growing). It is
the **only** wiki in this repo — do not call it "v4" or version anything; it is
simply the BERIL wiki. Its predecessors live elsewhere and are superseded.

## Mission for the initial build

Build the **first-party wiki compiler** that replaces the OpenKB dependency,
then prove parity. Everything else in `pipeline/` already works and carries
over with path adaptations. Scope of this build:

1. `pipeline/compile.py` — the compiler (spec below).
2. `pipeline/fetch_reports.py` — input sync (spec below).
3. Adapt the existing `pipeline/*` stages' paths to this repo's layout.
4. Run the **parity test** (protocol below) within the **$5 LLM budget cap**.
5. Report results and STOP for human review. Do not run a full 73-doc
   rebuild without an explicit, price-tagged go-ahead from the user
   (~$5-10 estimated; the user is cost-sensitive — never launch multi-dollar
   LLM runs without a stated price and their yes).

## What we learned (v1 → v2 → v3, condensed)

**v1 ("atlas"; agent + prompts, no pipeline)**: great editorial page types
(conflicts with evidence-sides + resolving-work, claims, open directions,
claim-delta integration rule) but no mechanism — coverage silently stalled at
55/73 projects. Lesson: *freshness must be produced by a pipeline, not
permitted by instructions.* Its editorial ideas survive in `contract/AGENTS.md`.

**v2 ("compendium"; custom deterministic harness + statement cards)**: the
tightest formal design — citation whitelists enforced at write time, typed
statement links (supports/contradicts/refines), zero duplication by
construction, byte-reproducible page planning. But its "knowledge graph" was
12 pre-seeded topics (no discovery), incrementality ran on prose instructions
(it froze 8 projects behind), and prose quality needed endless prompt work.
Lesson: *write-time enforcement and typed relations are worth keeping;
hand-planned topics and prose-driven orchestration are not.*

**v3 (OpenKB compiler + our pipeline)**: the winning architecture —
**accumulate-by-rewrite**: per document, summarize → plan against the current
concept/entity index → merge-rewrite each touched page, with hash bookkeeping.
Two independent adversarial reviews ranked its output first (8.7/10 mean;
verified: all 73 projects integrated, median 7 synthesis pages citing each).
Its weaknesses: enforcement was post-hoc (checker warns instead of the writer
being blocked), concept duplication/verbosity (~313k reader-layer words),
OpenKB dependency risk (dormant upstream), O(N²) rewrite cost on hot pages at
~1000-doc scale. Lesson: *keep the loop, replace the engine, move enforcement
into the write path.*

## Compiler spec (`pipeline/compile.py`)

Per new/changed document (content-hash vs `state/hashes.json`, skip
unchanged; process docs sequentially, oldest-first by project id):

1. **Summarize** → `wiki/summaries/<project>__REPORT.md` (or `<name>.md` for
   the digests). Dense, faithful, exact numbers, per-claim `[src: <project>]`
   tags, ends with `## Slots Into` listing target concept pages.
2. **Plan** — one call given: the new summary, the full concept/entity index
   (titles + one-line descriptions), and the duplicate-concept detector's
   current output (reuse logic from `pipeline/wiki_check.py`). Returns JSON:
   pages to create/update, with justification required for any *new* concept
   (extend-don't-duplicate is enforced here, not requested).
3. **Merge-rewrite** each touched concept/entity page: current page + new
   evidence in, merged page out. When adding evidence adjacent to existing
   claims the prose must state the relation: **supports / contradicts /
   refines** (v2's typed vocabulary, in prose).
4. **Write-time validation with retry (the core upgrade over OpenKB)** —
   before accepting any generated page: every `[src:]` id must be a known
   source; every flagged number (reuse `wiki_check.py`'s NUMBER regex) must
   appear in a cited source; wikilink targets must exist or be created this
   run. On failure: one retry with the specific violations quoted; on second
   failure: reject the page, keep the old version, log loudly, nonzero exit.
5. Maintain `wiki/index.md` (catalog) and `wiki/log.md` deterministically in
   code, not by LLM.

Prompts: START from OpenKB's, lifted from `reference/openkb-src/agent/compiler.py`
(Apache-2.0 — attribution already in /LICENSE), merged with the editorial
contract in `contract/AGENTS.md`, which is injected into every compile call
and remains the runtime-editable rulebook. LLM calls via litellm.
Known ceiling to mark, not solve: hot-page full-rewrite cost grows with
corpus size (`# ponytail: full-page rewrite; sectioned append if >500 docs`).

## Input (`pipeline/fetch_reports.py`)

Two backends behind one function, selected by config:
- `local` (now): sync `REPORT.md` per project + `docs/discoveries.md` +
  `docs/pitfalls.md` from a BERIL repo checkout
  (default `/Volumes/WorkSSD/Work/BERIL/BERIL-research-observatory`) into
  `staging/`; figures read from `<checkout>/projects/<id>/figures/` (used by
  `figures_build.py` and `quartz_ingest.py` — adapt their `REPO/projects`
  paths to this).
- `hub` (later): BERIL hub client — leave a stub; projects/ is moving there.

## Corpus format contract (do not change — the reference corpus follows it)

- Layout: `wiki/{summaries,concepts,entities}/*.md`, `wiki-extra/{topics,conflicts,authors,data}/*.md` + `wiki-extra/index.md` (home).
- Citations: `[src: <project_id>]`, comma-separated ids, ids = report filename
  stem minus `__REPORT` (digests: `discoveries`, `pitfalls`).
- Cross-links: `[[wikilinks]]`, paths relative to corpus root
  (`[[concepts/x]]`, `[[summaries/x__REPORT]]`).
- Frontmatter on wiki/ pages: `type`, `description`, `sources` (list of
  `summaries/...` paths). `sources` must never list a project the body does not
  cite: the v3 corpus padded it with bare "See also" links on 60 of 81 concept
  pages, which reads as synthesis without being it. Distinct `[src:]` ids in the
  body is the real measure; `consolidate_concepts.py` enforces the two in step.
- Downstream stages (`conflicts_build`, `topics_build`, `figures_build`,
  `extra_pages`, `wiki_check`, `quartz_ingest`) all parse these conventions —
  they are the compatibility test for compiler output.

## Pipeline (already built — adapt paths only)

`run_pipeline.sh` orchestrates: fetch → compile → enrich → consolidate →
conflicts → hubs → literature → figures → extras → authors →
check (errors block publish) → publish (Quartz v5, BERIL-workbench
theme baked into `build_quartz.sh`; dead-wikilink stripping, summary→raw-report
provenance links, figure splicing at publish). Topic hubs: Louvain over the
concept graph, resolution 2.0, names cached in state to prevent churn; only
changed hubs regenerate. All stages are hash-cached and idempotent — preserve
that property in everything you touch.

## Relationship to the v1 Atlas

This wiki is intended to take the place of the BERIL Atlas at
beril.kbase.us/atlas, so nothing published here links to it: sending readers to
the surface being replaced is the wrong direction of travel. That intent is
recorded here rather than on the site. It is a plan, with no date and no
announcement behind it, and the public pages state only what is true today.

The Atlas is NOT a reviewed artifact, and an earlier version of this file said
it was. All 141 of its pages carry `generated_by: Codex GPT-5` and
`status: draft`, none records a reviewer, and its `last_reviewed:` dates fall
on five clusters matching generation batches. Its `confidence:` field is a
model rating its own output. Do not describe it as the reviewed counterpart to
this wiki, on the site or anywhere else.

The Observatory link (beril.kbase.us) stays in the footer. That is where the
reports come from, so it is provenance rather than a pointer to a competing
surface.

## Models & environment

- Gateway: CBORG (LBL). `OPENAI_API_KEY=$CBORG_API_KEY`,
  `OPENAI_BASE_URL=https://api.cborg.lbl.gov`. IP-gated to LBLnet/authorized IPs.
- Compile + synthesis stages: `openai/claude-sonnet-5` (validated). A/B
  evidence: gpt-5.6-luna is ~10x cheaper and citation-compliant but shards
  concepts finely and writes thinner hubs; acceptable for bulk backfills,
  Sonnet for anything hub/merge-heavy.
- Never use PageIndex Cloud or any paid OpenKB service.

## Parity protocol (the acceptance test)

`reference/wiki-v3/` is the benchmark output (compiled by OpenKB+Sonnet/Luna,
kept OUT of version control — see .gitignore — so a clone will not have it;
restore it from the previous generation's checkout to re-run parity)
review-scored 8.7/10). Hold out 2-3 projects (suggest: `metal_specificity`,
`bacdive_phenotype_metal_tolerance`, `prophage_amr_comobilization`):
1. Seed a scratch corpus with the reference wiki MINUS pages/mentions of the
   held-out projects is impractical — instead compile the held-out projects
   INTO a copy of the reference corpus and compare the resulting merges
   against how the reference handled the same projects.
2. Judge: `wiki_check.py` (0 errors required; warnings ≤ reference), merge
   quality by side-by-side read (did existing pages get extended without
   losing content?), citation/number fidelity, extend-vs-duplicate behavior.
3. Report a comparison table + verdict; STOP for human review.

## House rules

- Ask before any spend beyond the $5 cap, with a price tag.
- Plain Python, stdlib + litellm + networkx + pyyaml only; uv for env.
- Every stage leaves a runnable check; match the existing code style in
  `pipeline/` (it is the house style).
- `wiki/` and `wiki-extra/` are generated output — never hand-edit content.
- reference/ is deletable after cutover; never treat it as live state.
