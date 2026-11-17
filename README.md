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
> and narrowly: a number is compared with the sources the paragraph cites, allowing
> equivalent scientific notation and simple differences or ratios at the stated
> precision. A flipped sign or a changed unit still passes. Nothing checks whether a
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

A fixed Python schedule drives Claude page sessions and GPT reviewer jobs; the
only structural model call chooses topic groups. Python enforces coverage,
scientific review, token budgets, and recoverable promotion. Start by listing
changed staged sources and stale editorial stages without inference:

```sh
uv run python -m beril_wiki.agentic plan
```

Runs load the committed [model policy](agentic.yaml): GPT-6.1 Sol extracts
evidence, writes queries and selects figures, Sonnet 5.5 plans and writes
derived pages, Haiku 5.5 writes integrated pages, and GPT-6 Luna reviews them.
Sonnet 5.5 writes the finding and research-direction records, Haiku 5.5 labels
result types and follow-up needs, and GPT-6 Luna and GPT-6.1 Sol review those
records. Every page is written in one Claude session: the writer edits the page
file, runs the host's checks and asks the GPT reviewer through tools, and the
host accepts only the exact text both approved. A page that does not converge
is recorded, not a run stop. Model changes apply to pages written from then on;
`pilot` measures a model on named pages first. See the [operating guide](docs/agentic-workflow.md) for
subscription login, the vendored `corpus/`, run budgets, workers, failed-page
retry, search, and recovery, or open the
[HTML walkthrough](docs/agentic-workflow.html) for the control flow. A capped
real-source update remains the acceptance step before a large compilation.
`uv run python -m beril_wiki.agentic cards --max-tokens N --max-jobs M` runs
only the finding, literature-label, research-direction, plain-summary,
links, shared-result, result-type (`outcomes`) and follow-up (`followups`)
stages (or those named with `--stage`) for the reports
and topics in `contract/cards.yaml`, then `check --strict`.
`--stage-max-usd STAGE=USD` caps a stage's recorded Claude spend across runs,
on `cards` and `run` alike.
`uv run python -m beril_wiki.stages.lakehouse --check` checks the committed
lakehouse catalog in `state/lakehouse/`; the
[operating guide](docs/agentic-workflow.md#lakehouse-catalog) gives the snapshots
it is built from and what a refresh costs.
The API-backed `scripts/run_pipeline.sh` remains available for compatibility.

## Repository layout

| Path | What it holds |
| --- | --- |
| `wiki/` | the compiled wiki: every collection, the home page, figures and assets. Generated; never hand-edit |
| `src/beril_wiki/` | the curator and runtime under `agentic/`, shared compiler and checks, domain operations under `stages/`, and Quartz rendering under `publish/` |
| `scripts/` | `setup.sh`, `run_pipeline.sh` and `build_quartz.sh` |
| `tests/` | deterministic checks and recorded-response workflow tests |
| `theme/` | the Quartz page frame (one component per page region), the stylesheet (one partial per region), and the browser script and index builder for search and Ask |
| `contract/` | the editorial contract injected into every compile, the concept decisions manifest, the errata a person has recorded against the source reports, the scope of finding and research-direction records (`cards.yaml`), and human decisions on literature labels (`novelty-decisions.yaml`) |
| `corpus/` | every source a run reads, laid out like an observatory checkout, with `manifest.json` recording each file's hash and origin (`beril_wiki.corpus`; `pull-hub` fills it from BERIL's context API, see the operating guide, "Pulling the corpus from BERIL"); the site serves the manifest as `corpus-manifest.json` |
| `state/` | per-stage caches that make the pipeline incremental, and the lakehouse catalog under `lakehouse/` |
| `search/` | ignored local copy of the section vectors for meaning search; the shared copy lives on the `history` branch and inside every site artifact |
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
the theme. A `scope` job also runs `scripts/check_update.py`, which keeps a
`wiki/<id>` publisher branch inside its own project
([details](docs/agentic-workflow.md)). Use `uv run python -m beril_wiki.agentic` for curator operations.
Direct stage invocations are maintenance tools and do not establish the
curator's shared budget or isolated promotion context. The theme type-checks
with `npm --prefix theme run typecheck` once `scripts/build_quartz.sh` has installed it.

## Learn more

- [`docs/agentic-workflow.md`](docs/agentic-workflow.md), commands, model
  policy, page sessions, pilots, caching, budgets, validation, and recovery
- [`docs/agentic-workflow.html`](docs/agentic-workflow.html), visual walkthrough
- [`docs/wiki.md`](docs/wiki.md), how the wiki itself is structured and how
  to read it
- [`deploy/README.md`](deploy/README.md), running the curator as a scheduled
  job: the persistent volume it needs, its environment, and the cold-start guard
- [`contract/AGENTS.md`](contract/AGENTS.md), the editorial contract

## Publishing

Pushing to `main` rebuilds and deploys the site to
[beril-doe.org/beril-wiki](https://beril-doe.org/beril-wiki)
([`.github/workflows/pages.yml`](.github/workflows/pages.yml)). Pull requests
build without deploying, so the Linux-only parts of the render are checked
before they reach the live site.

The site publishes the finding and research-direction records under
`wiki/findings/` and `wiki/directions/` as its Results and Open questions pages.

The job is render-only. It needs no API key, because `wiki/` and every
figure are committed. Refreshing the *content* is still a maintainer
running the curator and committing the accepted result. The curator does not
commit, push, build Quartz, or deploy automatically.

Before it deploys, the workflow runs `beril_wiki.check --strict` over the corpus and
asserts that every content page carries its provenance callout
([`scripts/check_site.sh`](scripts/check_site.sh)); either failing blocks publication.

### The SPIN image

The same site is also served from the BERIL webapp's host, at
[beril.kbase.us/wiki](https://beril.kbase.us/wiki), by a container on SPIN. The
ingress routes `/wiki` to it without rewriting the path. The container runs a
small server ([`src/beril_wiki/serve.py`](src/beril_wiki/serve.py)) that resolves
extensionless page URLs as Pages does.
[`.github/workflows/image.yml`](.github/workflows/image.yml) runs the same render
and checks, then pushes one image: every pull request pushes
`ghcr.io/beril-doe/beril-wiki:develop` (built for `beril-dev.kbase.us/wiki`),
and a merge to main pushes `:latest` (built for `beril.kbase.us/wiki`). A
manual run takes the tag as an input. The host is baked into absolute links,
so each environment has its own tag. Once the image is pushed, the same run
calls [`spin_deploy.yml`](.github/workflows/spin_deploy.yml) with that tag,
which restarts the matching SPIN deployment so it pulls the new image. The
deploy workflow can also be run by hand to restart one environment.

#### Run the image locally

    WIKI_BASE_URL=localhost:8080/wiki scripts/build_quartz.sh
    docker build -t beril-wiki .
    docker run --rm -p 8080:8080 beril-wiki     # http://localhost:8080/wiki/

The site is built before the image rather than inside it, because the search
vectors come from the `history` branch and need the checkout's `.git`.
`build_quartz.sh` also writes `quartz/corpus/` (the source reports, finding and
direction records and `cards.json`), which the image bakes in at `/srv/corpus`
for the internal API below.

The server ([`serve.py`](src/beril_wiki/serve.py), FastAPI) reads:

| Variable | Default | Meaning |
| --- | --- | --- |
| `WIKI_SITE_DIR` | `/srv/site` | the site baked into the image, served when no artifact is |
| `WIKI_CORPUS_DIR` | `/srv/corpus` | the baked corpus the internal API reads beside it |
| `WIKI_PREFIX` | `/wiki` | the URL prefix the ingress routes here |
| `WIKI_SITE_ROOT` | `/srv/artifacts` | where downloaded artifacts are unpacked (`site-<id>/`); mount a volume |
| `WIKI_ARTIFACT_ENDPOINT` | unset | S3 endpoint (`http://minio:9000`) or `file:///dir`; unset means serve the baked site only. A `file://` store also enables the store routes below |
| `WIKI_STORE_MAX_BYTES` | 1 GiB | the largest body `PUT /wiki/_admin/store/{key}` accepts |
| `WIKI_ARTIFACT_BUCKET`, `WIKI_ARTIFACT_PREFIX` (`wiki`), `WIKI_ARTIFACT_ACCESS_KEY`, `WIKI_ARTIFACT_SECRET_KEY`, `WIKI_ARTIFACT_REGION` | | the store |
| `WIKI_RELOAD_TOKEN` | unset | bearer token for `POST /wiki/_admin/reload` and `GET /wiki/_admin/status`; unset disables both (503) |
| `WIKI_INTERNAL_TOKEN` | unset | bearer token for the internal API under `/wiki/_api/`; unset disables it (503) |

`GET /wiki/_admin/status` (with the reload token) names the artifact being
served (`baked` for the image's own tree). `GET /healthz` is the liveness probe.

**The store routes.** With a `file://` store and `WIKI_RELOAD_TOKEN` set, the
same token guards `PUT`, `GET` and `HEAD /wiki/_admin/store/{key}` and `GET
/wiki/_admin/store?prefix=`: the server's own directory store, reachable over
HTTP for a publisher that shares neither a bucket nor a volume with it. Bodies
stream to disk under `WIKI_STORE_MAX_BYTES`, keys are checked against
traversal, and the sha256 is echoed back. On the curator side
`WIKI_ARTIFACT_ENDPOINT=http://<wiki host>/wiki/_admin/store` plus
`WIKI_RELOAD_TOKEN` selects `publish.artifact.HttpStore`, so `push`, `rollback`
and `current` work unchanged against a wiki container started with
`WIKI_ARTIFACT_ENDPOINT=file:///srv/artifacts/store`. This is what the
scheduled curator uses (`deploy/README.md`), and it is the simplest local loop
too: no MinIO, one container, the publish commands above with the http
endpoint. Like `/wiki/_api`, the ingress must not expose `/wiki/_admin`.

**Publish a site without a new image.** The curator host (or anyone with the
store's keys) packs the built site and makes it current; the container swaps
to it on request:

    export WIKI_ARTIFACT_ENDPOINT=http://localhost:9000 WIKI_ARTIFACT_BUCKET=beril-wiki \
           WIKI_ARTIFACT_ACCESS_KEY=minioadmin WIKI_ARTIFACT_SECRET_KEY=minioadmin
    WIKI_BASE_URL=localhost:8080/wiki scripts/build_quartz.sh
    scripts/publish_artifact.sh                         # gates, push, record history, point current
    curl -X POST -H "Authorization: Bearer $WIKI_RELOAD_TOKEN" localhost:8080/wiki/_admin/reload
    uv run python -m beril_wiki.publish.artifact rollback --to <id>   # then reload again

**The gate.** `push` refuses unless a gate record for exactly this build shows
`beril_wiki.check --strict`, `npm --prefix theme run typecheck` and
`scripts/check_site.sh` all passed: `build_quartz.sh` writes one to
`quartz/gate-results.json` (`WIKI_SKIP_GATES=1` leaves them to CI's steps),
`publish_artifact.sh` reruns them, and `push --run-gates` runs them in the same
invocation. The three results go into the manifest, and the server refuses a
manifest without them, so `current` never moves to a site CI would reject.

Each push is immutable (`site-<id>.tar.gz` plus `site-<id>.manifest.json`
under the prefix); `current.json` is the only thing that moves. A successful
push also commits `wiki/`, `state/`, `corpus/` and
`search/section-vectors.jsonl` from the working checkout to the `history`
branch (created orphan when absent, through a temporary index so your own
branch is untouched), tags `artifact/<id>` and, when the checkout has an
`origin` with a `history` branch, pushes both there before `current` moves:
the record must chain onto the fetched `origin/history`, and a rejected push
(another host published first) leaves `current` alone and undoes the local
record (`--no-history-push` keeps it local, for offline use). `push` and
`rollback` hold `<prefix>/publish.lease` in the store meanwhile, so two hosts
cannot move `current` at once; a lease a dead host left expires after
`WIKI_PUBLISH_LEASE_SECONDS` (default 3600). `rollback --to <id>` restores `wiki/`, `state/`,
`corpus/` and `search/` from the tag into the checkout and moves `current`
back, so the next curate run starts from the restored promotion instead of
building on the bad one; the previous trees are kept aside until `current` has
moved, and put back if it could not, so the served artifact and the checkout
always stand at the same promotion. It refuses while a run holds
`.agentic/lock` or when the tag is missing. The server reads the store's
manifest first and refuses it before any download when its id, page count,
gates or tarball sha256 disagree with `current.json`; it then streams the
tarball to a file, verifies its sha256, and extracts it one member at a time
(regular files and directories only) under `WIKI_ARTIFACT_MAX_MEMBERS`
(50000), `WIKI_ARTIFACT_MAX_UNPACKED_BYTES` (4 GiB) and
`WIKI_ARTIFACT_MAX_MEMBER_BYTES` (1 GiB), removing the partial tree when a cap
trips, so a compressed archive cannot fill the volume. It checks the manifest's
id, page count and gates against the unpacked tree before it swaps, keeps the previous artifact unpacked, and on a restart
serves the last one it unpacked when the store is unreachable, or the baked
site when nothing was. The manifest also records the git commit, the accepted
run's fingerprint from `state/agentic.json` and the sha256 of every source
report. `WIKI_ARTIFACT_ENDPOINT=file:///some/dir` is a store without S3, for
tests or a single host.

To try the whole loop against MinIO on one machine:

    docker run -d --name minio -p 9000:9000 -e MINIO_ROOT_USER=minioadmin \
      -e MINIO_ROOT_PASSWORD=minioadmin quay.io/minio/minio server /data
    docker run --rm -it --entrypoint sh --network host quay.io/minio/mc -c \
      "mc alias set local http://localhost:9000 minioadmin minioadmin && mc mb -p local/beril-wiki"
    docker run --rm -p 8080:8080 -e WIKI_ARTIFACT_ENDPOINT=http://host.docker.internal:9000 \
      -e WIKI_ARTIFACT_BUCKET=beril-wiki -e WIKI_ARTIFACT_ACCESS_KEY=minioadmin \
      -e WIKI_ARTIFACT_SECRET_KEY=minioadmin -e WIKI_RELOAD_TOKEN=dev beril-wiki
    # then, from the checkout, the publish commands above with WIKI_RELOAD_TOKEN=dev

The observatory's `docker-compose.yml` has a `wiki` profile service that pulls
`ghcr.io/beril-doe/beril-wiki:develop`. It reads the image from
`BERIL_WIKI_IMAGE`, so a local build runs there without editing that repo:

    docker build -t beril-wiki:local .                 # in this checkout
    BERIL_WIKI_IMAGE=beril-wiki:local docker compose --profile wiki up -d   # in the observatory

Put the `WIKI_ARTIFACT_*` and `WIKI_RELOAD_TOKEN` values in the observatory's
`.env` (its `wiki` service has no `env_file`, so pass them with `docker compose
run -e` or a compose override file) to point that container at a store.

Quartz bakes the full `WIKI_BASE_URL` into the sitemap, RSS, canonical and
`og:url` tags, and used to bake it into the footer's About link too. The footer
link is now root-relative (the path of the base URL), so one artifact serves
`beril.kbase.us/wiki` and `beril-dev.kbase.us/wiki` with only those metadata
URLs naming the build host; a host that needs them exact still gets its own
artifact, built with its own `WIKI_BASE_URL`.

#### Curator image

The curator runs on SPIN as its own image, `Dockerfile.curator`, pushed by
[`curator-image.yml`](.github/workflows/curator-image.yml) as
`ghcr.io/beril-doe/beril-wiki-curator:develop` (pull requests) and `:latest`
(main), with no deploy step: the CronJobs pull the tag when they next start.
The image carries the dependencies, Node 22, the bundled Claude and Codex CLIs
and a pre-warmed Quartz clone; the wiki's code and data live in a git clone on
a persistent volume whose code paths the job refreshes from `main` at every
start, so the data trees the curator owns are written by the curator alone and
`history`, not `main`, is authoritative for them once it runs. The entry point
[`deploy/curate.sh`](deploy/curate.sh) has four modes (`plan` hourly, `run`
nightly, `publish`, `status`) and publishes through the store routes above.
Manifests and the full environment table are in
[`deploy/README.md`](deploy/README.md). Locally:

    docker build -f Dockerfile.curator -t beril-wiki-curator .
    docker run --rm -v "$PWD/../work:/work" -e FETCH_BACKEND=hub -e BERIL_URL=... \
      -e BERIL_TOKEN=... beril-wiki-curator plan      # /work/beril-wiki must be a clone

#### Internal API

The container also answers an internal, token-guarded HTTP API under
`/wiki/_api/` ([`wiki_api.py`](src/beril_wiki/wiki_api.py)), the backend the
BERIL webapp's `WikiManager` reads the wiki through (`beril context find|read
--source wiki`). It is for in-cluster callers only (`http://wiki:8080`): **the
ingress must not expose `/wiki/_api` or `/wiki/_admin`**; add `location ~
^/wiki/_(api|admin) { return 404; }` (or an equivalent deny) ahead of the
`/wiki` proxy rule in the SPIN NGINX config and in the observatory's
`nginx.conf`. Every request carries `Authorization: Bearer
$WIKI_INTERNAL_TOKEN`; with the variable unset the routes answer 503.

| Route | Answer |
| --- | --- |
| `GET /wiki/_api/search?q=&scope=&k=` | `{artifact, results: [{address, title, heading, text, score}]}`; `scope` is a page group (`concept`, `topic`, `finding`, ...) or a path prefix such as `concepts/` |
| `GET /wiki/_api/read?address=` | `{artifact, address, title, content, sources}` for `wiki/<collection>/<slug>[#section]`; a `sources/` address returns the exact report Markdown |
| `GET /wiki/_api/ls?path=` | the collections, or the pages of one |
| `GET /wiki/_api/source?project=&offset=&length=` | exact characters of a source report, for quote checks |

Collections served: concepts, topics, conflicts, entities, summaries, sources,
findings, directions, data. The authors collection is excluded server-side.
Every answer names the artifact it was served from. Search is keyword only
(BM25 over the site's own section index); vector search is a TODO until the
server holds an embedding key.

### Search and Ask

Search and Ask the wiki run in the reader's browser, so the Pages site needs
no server. Keyword search needs nothing from the reader. Meaning search and Ask
call CBORG with the reader's own CBORG key. The reader enters it on the Ask page
or in the search box's meaning-search control, and asking without a key opens
the same key dialog. The browser stores the key in localStorage (or in
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
`history` branch, which every `scripts/publish_artifact.sh` run commits to
(with `wiki/`, `state/` and `corpus/`, tagged `artifact/<id>`), and
inside every site artifact under `corpus/`. The script first pulls them into
the ignored local store `search/section-vectors.jsonl`
(`beril_wiki.publish.search_data pull`). When `CBORG_API_KEY` is set, it then
runs `python -m beril_wiki.stages.search_vectors`, which embeds only the
sections with no vector using CBORG's free `lbl/nomic-embed-text`, and indexes
again. CI has no key: it pulls the vectors, fails a pull request whose sections
lack one (`SEARCH_REQUIRE_VECTORS=1`), and only warns on a deploy from `main`.
Vectors for sections that no longer exist are kept, so a feature branch's build
never drops ones the live site uses. Until the first artifact push puts
`history` on the remote, `pull` falls back to the legacy single-commit
`search-data` branch and `search_data push [--prune]` still updates it; that
branch goes away once `history` carries the vectors.

## License

AGPL-3.0, matching the BERIL Research Observatory corpus this wiki is
compiled from. Covers the pipeline and the compiled wiki alike. See
[`LICENSE`](LICENSE) for the terms, [`NOTICE`](NOTICE) for scope and
third-party attribution, and [`CITATION.cff`](CITATION.cff).
