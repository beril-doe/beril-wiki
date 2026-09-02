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

- Concept consolidation (`consolidate_concepts.py`) now merges near-duplicate
  shards and back-merges cross-document evidence, so the two debts that used to
  live here are closed. What it cannot fix: ~51 thin concepts have no summary
  above 0.75 cosine — they are genuinely single-project ideas, and no threshold
  reaches them. Do not read a remaining single-source page as a stage failure.
- Hub/conflict/author pages get `bad_src_ids` stripping but NOT the numeric
  check compile pages get; the hub-number warnings in `wiki_check` are that gap.
  `topics_build.py` has its own untracked `llm()` rather than `generate_page`,
  so routing it through the shared validator is its own change, not a one-liner.
- Nor do those stages validate WIKILINK targets the way `generate_page` does, so
  newly generated hub/conflict pages carry a few `[[concepts/<project_id>]]`
  links to pages that never existed. Harmless today — `wiki_check` does not scan
  links in `wiki-extra/`, and `quartz_ingest.strip_dead_wikilinks` removes them
  at publish — but it is the same untracked-`llm()` gap as the numeric check.
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
