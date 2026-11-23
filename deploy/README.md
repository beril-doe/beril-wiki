# Running the curator on SPIN

The curator is a scheduled job, never the web process: it holds a long lock,
runs for hours, and keeps its incremental state on disk. Two things follow.

## One persistent volume, mounted at the wiki checkout

The CronJob mounts a single PVC at the checkout (say `/work/beril-wiki`), and
that checkout holds everything a run reads and promotes:

| Path | What it holds | Why it must persist |
| --- | --- | --- |
| `wiki/` | the accepted, compiled wiki | `changed_sources` compares every staged report with `wiki/sources/`; without it every source is new |
| `state/` | per-stage caches, `state/agentic.json` (the accepted fingerprint), `state/hub.json` (the hub feed cursor) | the run's own idea of what is already done, and the cursor says what `pull-hub` already has |
| `corpus/` | every source a run reads, and `corpus/manifest.json` (file hashes, each project's owner and revision) | a source id assigned once must never be assigned again |
| `search/section-vectors.jsonl` | the meaning-search vectors | embedding again costs time; the file is gitignored |
| `.agentic/` | the ledger (`jobs.sqlite`), evidence, plans, failures, the lock | spend accounting and cached paid work |

The checkout is also where `publish_artifact.sh` commits the `history` branch
from (and where `artifact rollback` restores into), so `git` with push access
to `history` must be configured in the pod.

A pod that starts without the PVC looks exactly like a first-ever run and would
re-integrate the whole corpus at full cost. `agentic run` therefore refuses to
start when `state/agentic.json` is absent unless `BERIL_WIKI_ALLOW_COLD_START=1`
is set; `agentic plan` on the mounted volume reports `unchanged` when nothing
has moved. The initial population of the volume is a one-time `git clone` of
this repository (which carries `wiki/`, `state/`, `corpus/`) plus
`search_data pull`; after that only the job writes to it.

## Job environment

| Variable | Value |
| --- | --- |
| `BERIL_URL`, `BERIL_TOKEN` | BERIL's base URL and the wiki service PAT (a Secret), read only by `corpus pull-hub`; the run itself reads `corpus/` (`FETCH_BACKEND` stays `local`) |
| `BERIL_WIKI_AUTH` | `api`, with `ANTHROPIC_API_KEY`/`ANTHROPIC_BASE_URL` and `OPENAI_API_KEY`/`OPENAI_BASE_URL` from Secrets (CBORG-compatible) |
| `CBORG_API_KEY` | for the section embeddings in `build_quartz.sh` |
| `WIKI_ARTIFACT_ENDPOINT`, `WIKI_ARTIFACT_BUCKET`, `WIKI_ARTIFACT_PREFIX`, `WIKI_ARTIFACT_ACCESS_KEY`, `WIKI_ARTIFACT_SECRET_KEY` | the artifact store the wiki container also reads |
| `WIKI_RELOAD_URL`, `WIKI_RELOAD_TOKEN` | `http://wiki:8080/wiki/_admin/reload` and its bearer token, so a push swaps the live site |
| `WIKI_BASE_URL` | `beril.kbase.us/wiki` (or the dev host) |

## What one scheduled run does

```sh
cd /work/beril-wiki
uv run python -m beril_wiki.corpus pull-hub              # BERIL's feed -> corpus/; verifies every file
uv run python -m beril_wiki.agentic plan                 # free; exit if changed_sources is empty
uv run python -m beril_wiki.agentic run --max-tokens N --max-jobs M --stage-max-usd ...
scripts/build_quartz.sh                                  # render, embed, index, gates
scripts/publish_artifact.sh --no-check                   # push artifact, record + push history, point current, reload
```

`artifact push` holds `<prefix>/publish.lease` in the store while it works (so
two hosts cannot move `current` at once), fetches `origin/history`, refuses
when another host has published since the local `history`, and pushes
`history` and `artifact/<id>` to `origin` before it moves `current`: a
rejected push leaves `current` alone and undoes the local record. A separate
`git push origin history --tags` after the script is therefore no longer
needed. A lease a dead host left behind expires after
`WIKI_PUBLISH_LEASE_SECONDS` (default 3600) and is then taken over.

Budgets are fixed per run, so a bad night is capped. The hourly poll runs only
`pull-hub` and `plan`; the curate step runs at most once per window (nightly by default), and
an admin "run now" is the same command dispatched by hand.

## The wiki container

The wiki `Deployment` is separate: it serves the current artifact, mounts its
own volume at `/srv/artifacts` for the unpacked sites, and reads the same
`WIKI_ARTIFACT_*` values plus `WIKI_RELOAD_TOKEN` and `WIKI_INTERNAL_TOKEN`.
The ingress routes `/wiki` to it but must not expose `/wiki/_admin` or
`/wiki/_api`; the webapp reaches the internal API over the cluster network as
`http://wiki:8080/wiki/_api/`. See the README, "Run the image locally".
