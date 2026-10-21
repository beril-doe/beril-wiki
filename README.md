# BERIL Knowledge Wiki

The compiled knowledge wiki of the BERIL Research Observatory. Roughly 75
AI-conducted microbial-biology research reports go in; a hub-structured
scientific wiki comes out, with topic hubs, cross-project concept syntheses,
per-claim citations, recorded conflicts, and negative results, all produced by
a reproducible pipeline.

**Read it at [beril-doe.org/beril-wiki](https://beril-doe.org/beril-wiki)**
· [About & how to cite](https://beril-doe.org/beril-wiki/about)

> **An AI-generated wiki, partially reviewed.** A pipeline built these pages
> from AI-conducted research reports. Scientists have checked some of that
> underlying research; no one reviewed the pages themselves, and nothing marks
> which claims fall on which side. Citations and numbers are machine-verified,
> and narrowly: a figure is checked to appear in a source the paragraph cites,
> as text, so a flipped sign or a changed unit passes. Nothing checks whether a
> finding is correct. Read
> [About This Wiki](https://beril-doe.org/beril-wiki/about) before citing
> anything, and cite the underlying research report rather than the synthesis
> page that aggregates it.

## Build it locally

```sh
git clone git@github.com:beril-doe/beril-wiki.git && cd beril-wiki
scripts/setup.sh                              # installs deps, builds the site
cd quartz && npx quartz build --serve   # http://localhost:8080
```

Needs [uv](https://docs.astral.sh/uv/) and [node](https://nodejs.org)
(`brew install uv node`). No API keys required, because the compiled wiki, its
source reports, and every referenced figure are committed. You are only
rendering them.

## Update the wiki (maintainers)

A fixed Python schedule drives Claude Agent SDK writer and reviewer jobs; the
only structural model call chooses topic groups. Python enforces coverage,
scientific review, token budgets, and recoverable promotion. Start by inspecting
staged changes without inference:

```sh
uv run python -m beril_wiki.agentic plan
```

Runs load the committed [model policy](agentic.yaml): Opus 5.5 for scientific
work and Sonnet 5 for queries and figure selection.
Derived pages (conflicts, hubs, home, literature, authors) are written from
evidence packed into one prompt, checked by code, reviewed in one turn and
corrected by paragraph patches; a page that does not converge is recorded, not
a run stop. See the [operating guide](docs/agentic-workflow.md) for
subscription login, the observatory checkout, run budgets, workers, failed-page
retry, search, and recovery, or open the
[HTML walkthrough](docs/agentic-workflow.html) for the control flow. A capped
real-source update remains the acceptance step before a large compilation.
The API-backed `scripts/run_pipeline.sh` remains available for compatibility.

## Repository layout

| Path | What it holds |
| --- | --- |
| `wiki/` | the compiled wiki: every collection, the home page, figures and assets. Generated; never hand-edit |
| `src/beril_wiki/` | the curator and runtime under `agentic/`, shared compiler and checks, domain operations under `stages/`, and Quartz rendering under `publish/` |
| `scripts/` | `setup.sh`, `run_pipeline.sh` and `build_quartz.sh` |
| `tests/` | deterministic checks and recorded-response workflow tests |
| `theme/` | the Quartz page frame (one component per page region), the stylesheet (one partial per region), and the browser script and index builder for search and Ask |
| `contract/` | the editorial contract injected into every compile, the concept decisions manifest, and the errata a person has recorded against the source reports |
| `state/` | per-stage caches that make the pipeline incremental |
| `search/` | ignored local copy of the section vectors for meaning search; the shared copy lives on the `search-data` branch |
| `.agentic/` | ignored runtime ledger, raw results, receipts, and candidate workspace; preserve when resuming |
| `docs/` | curator operating guide, HTML walkthrough, and wiki-format reference |

## Development

```sh
uv sync                      # installs the package (editable) and the dev tools
uv run pytest                # tests
uv run ruff check            # lint
uv run ruff format           # format
uv run ty check              # type check
```

The same four commands run in CI on every pull request and on `main`
([`.github/workflows/tests.yml`](.github/workflows/tests.yml)); the publish
workflow separately validates the committed wiki, renders it, and type-checks
the theme. Use `uv run python -m beril_wiki.agentic` for curator operations.
Direct stage invocations are maintenance tools and do not establish the
curator's shared budget or isolated promotion context. The theme type-checks
with `npm --prefix theme run typecheck` once `scripts/build_quartz.sh` has installed it.

## Learn more

- [`docs/agentic-workflow.md`](docs/agentic-workflow.md), commands, editorial
  actions, caching, budgets, validation, and recovery
- [`docs/agentic-workflow.html`](docs/agentic-workflow.html), visual walkthrough
- [`docs/wiki.md`](docs/wiki.md), how the wiki itself is structured and how
  to read it
- [`contract/AGENTS.md`](contract/AGENTS.md), the editorial contract

## Publishing

Pushing to `main` rebuilds and deploys the site to
[beril-doe.org/beril-wiki](https://beril-doe.org/beril-wiki)
([`.github/workflows/pages.yml`](.github/workflows/pages.yml)). Pull requests
build without deploying, so the Linux-only parts of the render are checked
before they reach the live site.

The job is render-only. It needs no API key, because `wiki/` and every
figure are committed. Refreshing the *content* is still a maintainer
running the curator and committing the accepted result. The curator does not
commit, push, build Quartz, or deploy automatically.

Before it deploys, the workflow runs `beril_wiki.check --strict` over the corpus and
asserts that every content page carries its provenance callout; either failing
blocks publication.

### Search and Ask

Search and Ask the wiki run in the reader's browser, so the Pages site needs
no server. Keyword search needs nothing from the reader. Meaning search and Ask
call CBORG with the reader's own CBORG key, which the reader enters through the
key button in the top bar. The browser stores the key in localStorage (or in
sessionStorage if the reader unticks "Remember on this device") and sends it
only to `api.cborg.lbl.gov`. The site ships no maintainer key. Browser storage
belongs to the origin, not the path, so every page under `beril-doe.org`,
including the organisation's home page, can read a remembered key; the key
dialog says so. A dedicated subdomain for the wiki would remove that exposure.
An `/ask?q=` link fills in the question but asks it only when the reader came
from the site's own search or page drawer, so a shared link never spends the
reader's credit.

`scripts/build_quartz.sh` builds the search index after `npx quartz build`.
Meaning search compares the reader's query with one int8 vector per section,
keyed by a hash of the section's text. The vectors (about 8 MB) live on the
orphan branch `search-data`, which holds one commit with one file, so they never
enter `main`'s history. The script first pulls them into the ignored local store
`search/section-vectors.jsonl`. When `CBORG_API_KEY` is set, it then runs
`python -m beril_wiki.stages.search_vectors`, which embeds only the sections
with no vector using CBORG's free `lbl/nomic-embed-text`, and indexes again.

Whenever page text changes, share the new vectors before the change merges:

```sh
CBORG_API_KEY=... scripts/build_quartz.sh
uv run python -m beril_wiki.publish.search_data push
```

`push` merges the local store into `search-data`, replaces the branch's single
commit, and dispatches the Pages workflow on `main` (it needs `gh`; otherwise
run `gh workflow run pages.yml --ref main`). CI has no key: it pulls the
vectors, fails a pull request whose sections lack one, and only warns on a
deploy from `main`. Vectors for sections that no longer exist are kept, so a
feature branch's push never drops ones the live site uses; from an up-to-date
`main`, `push --prune` removes them. `scripts/run_pipeline.sh` pushes after
publishing.

## License

AGPL-3.0, matching the BERIL Research Observatory corpus this wiki is
compiled from. Covers the pipeline and the compiled wiki alike. See
[`LICENSE`](LICENSE) for the terms, [`NOTICE`](NOTICE) for scope and
third-party attribution, and [`CITATION.cff`](CITATION.cff).
