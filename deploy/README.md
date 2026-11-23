# Running the curator on SPIN

The curator is a scheduled job, never the web process: it holds a long lock,
runs for hours, and keeps its incremental state on disk. It ships as its own
image (`Dockerfile.curator`, pushed by `.github/workflows/curator-image.yml` as
`ghcr.io/beril-doe/beril-wiki-curator:develop` on pull requests and `:latest`
from main), runs `deploy/curate.sh` as its entry point, and is dispatched by the
manifests under `deploy/k8s/`. The dev namespace is `knowledge-engine`; the
manifests pull `ghcr.io/beril-doe/beril-wiki-curator:develop`, the tag the
workflow pushes, and name dev hosts, so production changes hosts, budgets and
the tag. GHCR is where SPIN already pulls the wiki's serve image from
(`image.yml`, `spin_deploy.yml`); no workflow holds a NERSC registry
credential. Should a namespace need `registry.nersc.gov` instead, copy the
tag by hand and change the three `image:` lines:

```sh
docker login registry.nersc.gov
docker buildx imagetools create \
  --tag registry.nersc.gov/kbase/beril-wiki-curator:develop \
  ghcr.io/beril-doe/beril-wiki-curator:develop
```

## Layout: one volume, one git clone

The jobs mount a single RWO volume (`deploy/k8s/pvc.yaml`) at `/work`, and
`/work/beril-wiki` (`WIKI_WORKDIR`) is a full git clone of this repository.
Code and data live together, which is what every script here assumes
(`scripts/build_quartz.sh` renders `$REPO/wiki`, `publish_artifact.sh` commits
`history` from the same checkout, `artifact rollback` restores into it).

| Path | What it holds | Why it must persist |
| --- | --- | --- |
| `wiki/` | the accepted, compiled wiki | `changed_sources` compares every staged report with `wiki/sources/`; without it every source is new |
| `state/` | per-stage caches, `state/agentic.json` (the accepted fingerprint), `state/hub.json` (the hub feed cursor) | the run's own idea of what is already done, and the cursor says what `pull-hub` already has |
| `corpus/` | every source a run reads, and `corpus/manifest.json` (file hashes, each project's owner and revision) | a source id assigned once must never be assigned again |
| `search/section-vectors.jsonl` | the meaning-search vectors | embedding again costs time; the file is gitignored |
| `.agentic/` | the ledger (`jobs.sqlite`), evidence, plans, failures, the lock | spend accounting and cached paid work |

At every start `curate.sh` refreshes **code paths only** from `WIKI_GIT_REF`
(default `main`): `src scripts theme contract deploy pyproject.toml uv.lock
agentic.yaml Dockerfile Dockerfile.curator`, with a path-limited `git fetch` +
`git checkout FETCH_HEAD -- <paths>` (files the ref dropped are removed too).
`wiki/`, `state/`, `corpus/`, `search/` and `.agentic/` are never checked out,
so a code change on `main` reaches the next job without an image rebuild, while
the data the curator owns is only ever written by the curator. **Once the job
has run, `wiki/`, `state/` and `corpus/` on `main` stop being authoritative;
the `history` branch is** (every publish commits them there and tags
`artifact/<id>`). A pull request that edits those trees on `main` changes
nothing on the volume. `WIKI_SKIP_CODE_REFRESH=1` leaves the clone as it is.

What runs is the clone's code, not a copy baked into the image. The image
holds the dependencies in a venv at `/opt/venv` (from `uv.lock`,
`--no-install-project`) and sets `UV_PROJECT_ENVIRONMENT=/opt/venv`,
`UV_NO_SYNC=1` and `PYTHONPATH=/work/beril-wiki/src`, so the repository
scripts' `uv run --project $REPO python ...` calls run `/opt/venv`'s Python
against the clone's `src/` without syncing anything onto the volume, and
`beril_wiki.paths.ROOT` resolves to the clone (`BERIL_WIKI_ROOT` names the
same path). A dependency change (`uv.lock`) therefore needs a new image, which
the workflow builds when the lock changes. The Claude CLI is the native binary
bundled in the Agent SDK wheel, linked to `/usr/local/bin/claude`; the Codex
CLI is the one `openai-codex` ships. Neither needs Node; Node 22 is in the
image for Quartz and the theme build.

The Quartz clone (at the commit `build_quartz.sh` pins) with its
`node_modules`, and the theme's `node_modules`, are pre-warmed in the image at
`/opt/quartz` and `/opt/theme`. The build chain hard-codes `$REPO/quartz` in
four places (the script, `check_site.sh`, `theme/src/build/search.ts`,
`stages/search_vectors.py`), and `quartz/` must be a real directory in the
clone: Quartz loads the theme plugin as `../theme` relative to its own
physical path, so a `quartz -> /opt/quartz` symlink made it load `/opt/theme`
(dependencies, no `dist/`) and fall back to its default frame with only a log
line to say so. The job therefore copies `/opt/quartz` into
`$WIKI_WORKDIR/quartz` on the first run, replaces the copy when the pinned
Quartz commit changes, and copies `/opt/theme/node_modules` into `theme/` when
that is absent. The render writes into `quartz/` on the volume (about 1 GB
with `node_modules` and `public/`); `curate.sh render` checks that
`quartz/public/index.html` carries the theme's frame (`class="page-grid"`)
and fails otherwise. `curate.sh render` on its own, with the volume mounted,
is how to check an image before trusting it with a publish.

## First-time population

A pod that starts without the clone looks exactly like a first-ever run and
would re-integrate the whole corpus at full cost. `curate.sh` therefore exits 2
when `$WIKI_WORKDIR/.git` is missing, and `agentic run` refuses when
`state/agentic.json` is absent, unless `BERIL_WIKI_ALLOW_COLD_START=1` says the
cold start is meant. Populate the volume once, from a pod with it mounted (for
example the run-now Job with `command: ["sleep", "infinity"]`, then
`kubectl exec`), or let the job do it with the override:

```sh
git clone --branch main https://github.com/beril-doe/beril-wiki.git /work/beril-wiki
cd /work/beril-wiki
git fetch origin history:history            # the audit trail and the vectors
uv run --project . python -m beril_wiki.publish.search_data pull
```

`main` carries `wiki/`, `state/` and `corpus/`; `search_data pull` fills
`search/section-vectors.jsonl` from `history`. With the clone in place,
`curate.sh plan` reports what the first run would do (`changed_sources=0` when
`corpus/` already holds everything BERIL's feed lists past the cursor in
`corpus/manifest.json`).

## Job environment

Set through `deploy/k8s/configmap.yaml` and the Secret `beril-wiki-curator`
(create it from your own terminal with `kubectl create secret generic
beril-wiki-curator -n knowledge-engine --from-literal=NAME=VALUE ...`; the
keys are the Secret rows below, and no filled copy belongs in git).

| Variable | Where | Value |
| --- | --- | --- |
| `BERIL_URL` | ConfigMap | BERIL's base URL; `corpus pull-hub` reads `/api/context/*` with `BERIL_TOKEN` and nothing else (never `/ov`), and the run itself reads `corpus/` (`FETCH_BACKEND` stays `local`) |
| `BERIL_TOKEN` | Secret | the wiki service account's BERIL PAT |
| `BERIL_WIKI_AUTH` | ConfigMap | `api`: jobs run on the keys below; OAuth and provider routing are stripped |
| `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL` | Secret | Claude-role jobs; the base URL may be a CBORG-compatible gateway |
| `OPENAI_API_KEY`, `OPENAI_BASE_URL` | Secret | Codex-role jobs through CBORG's OpenAI-compatible endpoint |
| `CBORG_API_KEY` | Secret | section embeddings in `build_quartz.sh` |
| `WIKI_WORKDIR`, `WIKI_GIT_URL`, `WIKI_GIT_REF` | ConfigMap | the clone, where it is fetched from, which ref's code paths are refreshed |
| `WIKI_GIT_TOKEN` | Secret | GitHub token with `contents:write`, for `git push origin history` and the `artifact/*` tags |
| `WIKI_GIT_NAME`, `WIKI_GIT_EMAIL` | ConfigMap | author of the `history` commits |
| `WIKI_BASE_URL` | ConfigMap | `beril.kbase.us/wiki` or the dev host; baked into sitemap, RSS and canonical URLs |
| `WIKI_ARTIFACT_ENDPOINT`, `WIKI_ARTIFACT_PREFIX` | ConfigMap | `http://beril-wiki:8080/wiki/_admin/store` and `wiki`: the wiki pod's store routes (below), through the Service the SPIN guide names `beril-wiki` (Compose: `wiki`) |
| `WIKI_RELOAD_URL`, `WIKI_RELOAD_TOKEN` | ConfigMap, Secret | `http://beril-wiki:8080/wiki/_admin/reload` and the pod's admin bearer, shared by the store routes |
| `WIKI_CURATE_MAX_TOKENS`, `WIKI_CURATE_MAX_JOBS`, `WIKI_CURATE_WORKERS` | ConfigMap | `agentic run --max-tokens / --max-jobs / --workers` |
| `WIKI_CURATE_STAGE_MAX_USD` | ConfigMap | space-separated `STAGE=USD` list, each one a `--stage-max-usd`; `STAGE` is a job-step prefix (`extract plan write lit figures curator merge merge-judge backmerge repair`) or an editorial stage, never a model role, and `curate.sh` refuses the list at every start otherwise |
| `WIKI_CURATE_EXTRA_ARGS` | ConfigMap | appended to `agentic run` verbatim (for example `--strict-pages`) |
| `WIKI_LOCK_FILE`, `WIKI_LOCK_WAIT` | optional | the curator's job lock, `/work/.curate.lock` beside the clone, and how long `run`/`publish`/`render` wait for it (1800 s; `plan` never waits) |
| `BERIL_WIKI_ALLOW_COLD_START` | set by hand | `1` lets `curate.sh` clone a missing checkout and `agentic run` start without `state/agentic.json` |
| `WIKI_SKIP_CODE_REFRESH` | set by hand | `1` skips the fetch and path checkout |

`WIKI_GIT_TOKEN` reaches git through a credential helper that `curate.sh`
installs in git's environment-held config (`GIT_CONFIG_*`): the helper prints
the token from the environment when git asks, so it appears in no file on the
volume, no config and no command line. The same mechanism rewrites a
`git@github.com:` origin to https and marks the clone a `safe.directory`, since
the volume may have been populated by another uid.

## What `curate.sh` does

| Mode | Dispatched by | Steps | Exit |
| --- | --- | --- | --- |
| `plan` | `cronjob-plan.yaml`, hourly | refresh code; `corpus pull-hub`; `stages.fetch`; `agentic plan`; log `plan: changed_sources=N pending_editorial=N retry_pages=N accepted_current=true|false|unknown` | 0 nothing to do, 3 a run would do something (the CronJob maps 3 to success), 2 no clone |
| `run` | `cronjob-curate.yaml`, nightly; `job-run-now.yaml` | `plan` (reported, never a gate); `agentic run` under the budgets, which makes the same test itself and promotes or prints `unchanged; zero model calls`; when it promoted: `build_quartz.sh`; `publish_artifact.sh --id <UTC stamp> --no-check`; `git push origin history refs/tags/artifact/*` | 0 published or nothing to publish; non-zero on any failed step, including a held `.agentic/lock` and a refused cold start |
| `publish` | by hand | refresh code; render and publish the accepted wiki as above, without curating | as `run` |
| `render` | by hand | refresh code; `build_quartz.sh` into `quartz/public`; check the frame; no store, no push | 0 rendered with the theme's frame, else non-zero |
| `status` | by hand | `agentic status`, or a note when no run has been recorded | 0 |

Every step logs one timestamped line (`2026-11-17T07:30:00Z curate[run] ...`).
Staging is empty between scheduled runs, so `plan` first runs `corpus pull-hub`
(BERIL's feed into `corpus/`, every file sha256-checked, the cursor kept in
`corpus/manifest.json`) and `stages.fetch` (`corpus/` into `staging/`), and
`changed_sources` then names the projects a run would integrate. The other
counts are what `agentic run` would act on without any source changing:
`retry_pages` (integrated pages left in `.agentic/failures.json` with retries
left, re-drafted unasked) and `accepted_current`, `run`'s own fingerprint
test, which a README, figure or errata change alone fails, as does a code or
model change (`unknown` when the Claude CLI, whose version is part of the
fingerprint, is not on the PATH). Budgets
are fixed per run, so a bad night is capped; `agentic run` refuses a second
runner on the same checkout, and a run killed by the Job's deadline is charged
from its transcripts and resumes from cached work the next night.

`concurrencyPolicy: Forbid` is per CronJob, so the hourly plan would start
while the nightly run is curating, and its code refresh, `pull-hub` and
`stages.fetch` would change the run's inputs, which then refuses promotion
("inputs changed during compilation"). Every mode but `status` therefore
holds `flock` on `/work/.curate.lock` (beside the clone, so a cold start can
take it first; `.agentic/lock` is `agentic run`'s own, held inside it): `plan`
exits 0 with "skipping this plan" when another job holds it, and `run`,
`publish` and `render` wait up to `WIKI_LOCK_WAIT` seconds for the plan to
finish before giving up with exit 75.

Run now: `kubectl -n knowledge-engine create job
--from=cronjob/beril-wiki-curator-curate curator-run-now-$(date +%Y%m%d%H%M)`,
or apply `deploy/k8s/job-run-now.yaml` with a fresh name; both run `run`, which
still does nothing when the plan is empty (switch the args to `publish` to
re-render regardless). Roll back with `uv run python -m
beril_wiki.publish.artifact rollback --to <id>` from a pod with the volume and
the Secret mounted, then `POST /wiki/_admin/reload`.

## The artifact transport

No bucket is reachable from both the job and the wiki pod, and `kubectl cp`
is no transport for a CronJob, so the wiki server carries the store itself.
With `WIKI_RELOAD_TOKEN` set and a `file://` store (the pod runs with
`WIKI_ARTIFACT_ENDPOINT=file:///srv/artifacts/store`, on the same volume as
its unpacked sites), it answers `PUT`, `GET` and `HEAD
/wiki/_admin/store/{key}` and `GET /wiki/_admin/store?prefix=`, guarded by
the same bearer as the reload, bodies streamed to disk under
`WIKI_STORE_MAX_BYTES` (default 1 GiB) with the sha256 echoed back. The
curator's `WIKI_ARTIFACT_ENDPOINT=http://beril-wiki:8080/wiki/_admin/store` selects
`publish.artifact.HttpStore`, which speaks those routes; `push`, `rollback`,
`current` and the reload are unchanged, and `publish_artifact.sh` still calls
`WIKI_RELOAD_URL` afterwards. The ingress must keep `/wiki/_admin` (and
`/wiki/_api`) unreachable from outside the cluster, as before.

## The wiki container

The wiki `Deployment` is separate: it serves the current artifact, mounts its
own volume at `/srv/artifacts` for the unpacked sites and the store, and reads
`WIKI_ARTIFACT_ENDPOINT=file:///srv/artifacts/store` plus `WIKI_RELOAD_TOKEN`
and `WIKI_INTERNAL_TOKEN`. The ingress routes `/wiki` to it but must not
expose `/wiki/_admin` or `/wiki/_api`; the webapp reaches the internal API
over the cluster network as `http://wiki:8080/wiki/_api/`. See the README,
"Run the image locally".
