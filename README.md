# BERIL Knowledge Wiki

The compiled knowledge wiki of the BERIL Research Observatory. Roughly 75
AI-conducted microbial-biology research reports go in; a hub-structured
scientific wiki comes out, with topic hubs, cross-project concept syntheses,
per-claim citations, recorded conflicts, and negative results, all produced by
a reproducible pipeline.

**Read it at [beril-doe.org/beril-wiki](https://beril-doe.org/beril-wiki)**
· [About & how to cite](https://beril-doe.org/beril-wiki/about)

> These pages are compiled by software from AI-conducted research reports and
> are **not peer-reviewed**. Some of the underlying work has been reviewed by
> the researchers behind it; the compiled pages have not been checked as a
> whole, so do not assume any particular claim was. Citations and numeric
> fidelity are machine-verified, and
> narrowly: a figure is checked to appear in a source the paragraph cites, as a
> token, so a flipped sign or a changed unit passes. Scientific correctness is
> not checked at all. Read
> [About This Wiki](https://beril-doe.org/beril-wiki/about) before citing
> anything, and prefer the underlying research report over the synthesis page
> that aggregates it.

## Build it locally

```sh
git clone git@github.com:beril-doe/beril-wiki.git && cd beril-wiki
./setup.sh                              # installs deps, builds the site
cd quartz && npx quartz build --serve   # http://localhost:8080
```

Needs [uv](https://docs.astral.sh/uv/) and [node](https://nodejs.org)
(`brew install uv node`). No API keys required, because the compiled wiki, its
source reports, and every referenced figure are committed. You are only
rendering them.

## Run the pipeline (maintainers)

```sh
CBORG_API_KEY=... ./pipeline/run_pipeline.sh    # incremental: same command every time
```

Requires a BERIL observatory checkout (`BERIL_CHECKOUT`, for source reports
and figures) and CBORG access. Every stage is hash-cached and idempotent, so an
unchanged corpus re-runs for $0.

## Learn more

- [`docs/pipeline.md`](docs/pipeline.md), workflow architecture: stages,
  models, write-time validation, caching and cost control
- [`docs/wiki.md`](docs/wiki.md), how the wiki itself is structured and how
  to read it
- [`TODO.md`](TODO.md), status and open items, and
  [`PARITY_REPORT.md`](PARITY_REPORT.md), how the compiler was validated
- `contract/AGENTS.md`, the editorial contract injected into every compile

## Publishing

Pushing to `main` rebuilds and deploys the site to
[beril-doe.org/beril-wiki](https://beril-doe.org/beril-wiki)
([`.github/workflows/pages.yml`](.github/workflows/pages.yml)). Pull requests
build without deploying, so the Linux-only parts of the render are checked
before they reach the live site.

The job is render-only. It needs no API key, because `wiki/`, `wiki-extra/`
and every figure are committed. Refreshing the *content* is still a maintainer
running `run_pipeline.sh` and committing the result.

Before it deploys, the workflow runs `wiki_check --strict` over the corpus and
asserts that every content page carries its provenance callout; either failing
blocks publication.

## License

AGPL-3.0, matching the BERIL Research Observatory corpus this wiki is
compiled from. Covers the pipeline and the compiled wiki alike. See
[`LICENSE`](LICENSE) and [`CITATION.cff`](CITATION.cff).
