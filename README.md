# BERIL Knowledge Wiki

The compiled knowledge wiki of the BERIL Research Observatory: ~75 AI-conducted
microbial-biology research reports in, a hub-structured scientific wiki out —
topic hubs with literature context, cross-project concept syntheses, per-claim
citations, conflicts, and negative results, all produced by a reproducible
pipeline.

## View the wiki

```sh
git clone git@github.com:beril-doe/beril-wiki.git && cd beril-wiki
./setup.sh                              # installs deps, builds the site
node pipeline/serve_quartz.cjs
```

Needs [uv](https://docs.astral.sh/uv/), [Bun](https://bun.sh), and [Node](https://nodejs.org)
(`brew install uv bun node`). No API keys required — the compiled wiki, its
source reports, and all referenced figures are committed; you are only
rendering them.

`wiki/` and `wiki-extra/` contain native Open Knowledge Format v0.2 pages.
The normal scripts maintain metadata, relative links, and source footnotes;
setup upgrades legacy formatting automatically. The site includes an OKF
graph generated with Google's reference viewer from those same files.

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
