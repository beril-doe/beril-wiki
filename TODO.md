# BERIL Wiki — v1 TODO

Prioritized for one goal: a human scientist opens a URL and finds the corpus
readable, credible, and actionable. Price tags are LLM-spend estimates (CBORG
Sonnet rates unless noted); $0 = deterministic code. Items from Paramvir's
wishlist are tagged [P]; platform-dependent items are deferred at the bottom.

## P0 — the wiki must be openable and navigable

- [x] **Concept-enrichment pass** (DONE, all-Luna ~$1.5): now a permanent
      pipeline stage (`enrich_concepts.py`, hash-cached per summary) rather
      than a one-off; grew the synthesis layer 19 → 153 concepts. Calibrated
      prompt requires cross-project recurrence per create.
- [x] **Run downstream stages** (DONE, all-Luna ~$1): conflicts (13), topic
      hubs (15), figures (179 placements), extras, check (0 errors). Full
      pipeline re-run is a $0 no-op. [P: adoption]
- [ ] **Host the site** — ON HOLD pending Paramvir's approval for a public
      GitHub Pages deploy; local Quartz build works meanwhile
      (`pipeline/build_quartz.sh`, serves at localhost:8080).
      [P: adoption, multi-user readership]

## P1 — reader value on top of the compiled corpus

- [x] **Open Directions browse page** (DONE): `wiki-extra/opportunities.md`,
      deterministic aggregation of all 153 concepts' Open Directions.
      [P: surface hypotheses, recommend next steps]
- [x] **Literature-context stage** (DONE, ~$0.2): `lit_context.py` — detailed
      literature review spliced at the TOP of every topic hub (per Paramvir's
      intent): model-proposed PubMed queries, NCBI eutils candidates, every
      cited PMID verified in code. All 15 hubs reviewed. Extending the same
      stage to major concept pages is a config change when wanted.
      [P: place BERIL work in the context of existing literature]
- [x] **Negative-results digest** (DONE): `wiki-extra/negative-results.md`
      aggregates all 75 projects' caveat/null sections; summary prompt now
      demands null results explicitly. [P: don't repeat what didn't work]
- [x] **Entity hygiene** (DONE): single-source entity pages (197/336) are
      filtered at publish time (reversible — they surface at 2+ sources);
      their links downgrade to plain text.

## P2 — cheap visibility wins, after P0/P1

- [x] **Uptake section on summaries** (DONE): publish-time "Feeds into:
      [concepts]" reverse-index line on every summary page.
      [P: track how outputs influence later work]
- [ ] **Publish CI** ($0): GitHub Action to rebuild + deploy on push — blocked
      with hosting on Paramvir's approval. [P: living synthesis]

## Known draft-stage debts

- Concept consolidation (`consolidate_concepts.py`) closed the two debts that
  used to live here: 153 -> 99 concepts, single-source 136 -> 15.
- Embeddings are a WEAK detector for this defect and should not be trusted alone.
  Measured against pairs whose bodies restate near-identical numbers, whole-page
  cosine put them at median rank 189 of 7381 and recall@45 was 29%; the
  deterministic evidence-overlap generator (shared cited project + >=3 identical
  figures) finds them exactly, for free. Numbers-in-common is the direct
  signature of a restated shard; semantic similarity is only a proxy for it.
  If this ever regresses, suspect the REPRESENTATION before the model: embedding
  only the lead paragraph scored median rank 2214 and recall@45 of 0%.
- CLOSED: hub/conflict/author pages now get the same numeric and wikilink
  validation compile pages get, and `wiki_check` scans all five publishable
  collections. Dead concept links went 34 -> 0.
- The numeric check verifies that a figure APPEARS in a cited source. It cannot
  verify units, denominators, direction, that a figure attaches to the right
  claim, or any non-numeric claim. Do not read "0 errors" as "the corpus is
  true". Small integers (<4 digits, no decimal) are deliberately out of scope.
- One known mis-citation: `entities/mycobacterium-tuberculosis.md` credits a
  91% accessory-AMR fraction to `metabolic_capability_dependency`, which does
  not report it (`amr_environmental_resistome` does). Compile's resume-skip
  will not rewrite the page because it legitimately cites that document
  elsewhere, and `wiki/` is generated so it must not be hand-edited. It needs a
  targeted page-repair path, which does not exist yet.
- 4 duplicate-concept warnings are pairs where BOTH sides are mature (>= 4 cited
  projects), which `consolidate_concepts.py` declines by design. They need a
  human call, not a threshold change.
- Entity deduplication is the one collection still unaddressed. 336 pages, no
  detector, and the concept detectors must NOT be reused: embeddings rank
  `aciad2176`/`aciad3137` (different genes) at 0.971 and numeric overlap scores
  `cyanobacteriia`/`photosystem-ii` at 1.00. It needs identity resolution on
  canonical names, aliases and external ids -- which `contract/AGENTS.md`
  requires but only ~40 of 336 pages record, so an id-extraction pass comes
  first. Low priority: 1 exact name collision (`egg-nog`/`eggnog`) plus a
  handful of plausible ones, and 197 of 336 pages are hidden at publish.
- The budget tripwire UNDERCOUNTS. A consolidation pass self-reported `~$0.80`
  while the gateway billed $1.29 (~2x), so `COMPILE_BUDGET_USD` is not a hard
  ceiling; reasoning tokens appear to be billed but absent from
  `usage.completion_tokens`. `topics_build`, `conflicts_build` and
  `figures_build` have no tripwire at all. Real spend is readable from
  `GET https://api.cborg.lbl.gov/user/info` (`user_info.spend`).
- `conflicts_build.py` never deletes stale conflict pages (`topics_build` does
  reap stale hubs), so a concept merge can strand a conflict page. `wiki_check`
  does not scan `wiki-extra/conflicts`, so it will not flag one.
- One second-run lit/hub churn cycle observed (a few hubs regenerate once
  after their reviews land); converges, costs cents.

## Deferred — platform features, not compiler features

- Multi-user/agent knowledge aggregation, session & transcript preservation,
  LangFuse tagging/access control, transcript search: belong to the BERIL
  hub/observatory; the wiki consumes them via fetch_reports' hub backend
  when they exist.
- Autonomous dataset-analysis agents + per-dataset decision wikis: observatory
  side; the wiki already ingests their reports incrementally.
- Dileep/Chris/Prachi integration & transporter-evidence revisit: research
  content tasks — they become wiki content the moment their reports land in
  projects/.
