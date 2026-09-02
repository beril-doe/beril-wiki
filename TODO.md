# BERIL Wiki — v1 TODO

Prioritized for one goal: a human scientist opens a URL and finds the corpus
readable, credible, and actionable. Price tags are LLM-spend estimates (CBORG
Sonnet rates unless noted); $0 = deterministic code. Items from Paramvir's
wishlist are tagged [P]; platform-dependent items are deferred at the bottom.

## P0 — the wiki must be openable and navigable

- [ ] **Concept-enrichment pass** (~$12–15): Sonnet planning sweep over the 75
      summaries to create the missing synthesis-layer concepts (Luna bootstrap
      produced 19 vs ~80 expected); adds a `PLAN_MODEL`/enrich mode to
      compile.py. Everything below (hubs, lit context) builds on concepts.
- [ ] **Run downstream stages** (~$5–8): conflicts → topic hubs → figures →
      extras → check. Produces the home page, topics, conflict pages,
      author/data pages — the entire navigation layer. [P: adoption]
- [ ] **Host the site** ($0): Quartz build → GitHub Pages on beril-doe/beril-wiki
      (baseUrl change + CI or manual push). A shareable URL is the adoption
      prerequisite. [P: adoption, multi-user readership]

## P1 — reader value on top of the compiled corpus

- [ ] **Open Directions browse page** ($0): deterministically aggregate every
      concept's `## Open Directions` into one "Research Opportunities" page,
      grouped by topic hub. The wiki becomes a what-to-do-next surface.
      [P: surface hypotheses, recommend next steps]
- [ ] **Literature-context stage** (~$5–10): `lit_context.py` adds a cited
      `## Literature Context` section to concept pages + discoveries digest;
      PubMed via NCBI eutils, PMIDs verified deterministically in the
      write-time validator (no fabricated references). Answers the reader's
      first question: known or novel? [P: literature investigation, scoped
      from agent to compile-time stage]
- [ ] **Negative-results digest** ($0 + prompt line): aggregate the summaries'
      "Caveats and Open Work" sections (present in 73/75) into a browsable
      negative/null-results page; add an explicit null-results instruction to
      the summary prompt for future compiles. [P: make negative results
      discoverable so collaborators don't repeat analyses]
- [ ] **Entity hygiene** ($0): deterministically retire single-source
      passing-mention entity pages (197 of 336), downgrading their wikilinks —
      same mechanism quartz_ingest already uses for dead links.

## P2 — cheap visibility wins, after P0/P1

- [ ] **Uptake section on summaries** ($0): deterministic reverse-index — each
      summary page gets "This project feeds: [concepts...]" — a first, honest
      version of impact tracking. [P: track how outputs influence later work]
- [ ] **Publish CI** ($0): GitHub Action to rebuild + deploy on push, so the
      site stays current with the incremental pipeline. [P: living synthesis]

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
