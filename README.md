# BERIL Knowledge Wiki

The compiled knowledge wiki of the BERIL Research Observatory: ~75 AI-conducted
microbial-biology research reports in, a hub-structured scientific wiki out —
topic hubs with literature context, cross-project concept syntheses, per-claim
citations, conflicts, and negative results, all produced by a reproducible
pipeline.

**Read it at [beril-doe.github.io/beril-wiki](https://beril-doe.github.io/beril-wiki)**
· [About & how to cite](https://beril-doe.github.io/beril-wiki/about)

> These pages are compiled by software from AI-conducted research reports and
> are **not peer-reviewed**. Nothing here has been checked by a human scientist
> before publication. Citations and numeric fidelity are machine-verified;
> scientific correctness is not. Read
> [About This Wiki](https://beril-doe.github.io/beril-wiki/about) before citing
> anything, and prefer the underlying research report over the synthesis page
> that aggregates it.

The observatory's reviewed knowledge surface — claims, tensions and data
products with human-assigned confidence and review dates — is the
[BERIL Atlas](https://beril.kbase.us/atlas). Where the two disagree, the Atlas
is the reviewed artifact.

## Build it locally

```sh
git clone git@github.com:beril-doe/beril-wiki.git && cd beril-wiki
./setup.sh                              # installs deps, builds the site
cd quartz && npx quartz build --serve   # http://localhost:8080
```

Needs [uv](https://docs.astral.sh/uv/) and [node](https://nodejs.org)
(`brew install uv node`). No API keys required — the compiled wiki, its
source reports, and all referenced figures are committed; you are only
rendering them.

## Run the pipeline (maintainers)

```sh
CBORG_API_KEY=... ./pipeline/run_pipeline.sh    # incremental: same command every time
```

Requires a BERIL observatory checkout (`BERIL_CHECKOUT`, for source reports
and figures) and CBORG access. Every stage is hash-cached and idempotent — an
unchanged corpus re-runs for $0.

## Learn more

- [`docs/pipeline.md`](docs/pipeline.md) — workflow architecture: stages,
  models, write-time validation, caching and cost control
- [`docs/wiki.md`](docs/wiki.md) — how the wiki itself is structured and how
  to read it
- [`TODO.md`](TODO.md) — v1 status and open items ·
  [`PARITY_REPORT.md`](PARITY_REPORT.md) — how the compiler was validated
- `contract/AGENTS.md` — the editorial contract injected into every compile
- [`reference/README.md`](reference/README.md) — why `reference/` is not the
  wiki and must not be cited

## Publishing

Pushing to `main` rebuilds and deploys the site
([`.github/workflows/pages.yml`](.github/workflows/pages.yml)). The job is
render-only — it needs no API key, because `wiki/`, `wiki-extra/` and every
figure are committed. Refreshing the *content* is still a maintainer running
`run_pipeline.sh` and committing the result.

## License

AGPL-3.0, matching the BERIL Research Observatory corpus this wiki is
compiled from. Covers the pipeline and the compiled wiki alike. See
[`LICENSE`](LICENSE) and [`CITATION.cff`](CITATION.cff).
