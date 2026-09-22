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

Runs load the committed [model policy](agentic.yaml): Opus 5 for scientific
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
| `theme/` | the Quartz page frame (one component per page region) and the stylesheet (one partial per region) |
| `contract/` | the editorial contract injected into every compile, the concept decisions manifest, and the errata a person has recorded against the source reports |
| `state/` | per-stage caches that make the pipeline incremental |
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

Use `uv run python -m beril_wiki.agentic` for curator operations. Direct stage
invocations are maintenance tools and do not establish the curator's shared
budget or isolated promotion context. The theme type-checks
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

## License

AGPL-3.0, matching the BERIL Research Observatory corpus this wiki is
compiled from. Covers the pipeline and the compiled wiki alike. See
[`LICENSE`](LICENSE) for the terms, [`NOTICE`](NOTICE) for scope and
third-party attribution, and [`CITATION.cff`](CITATION.cff).
