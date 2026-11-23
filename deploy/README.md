# Running the curator on SPIN

The curator is a scheduled job, never the web process: it holds a long lock,
runs for hours, and keeps its incremental state on disk. It ships as its own
image (`Dockerfile.curator`, pushed by `.github/workflows/curator-image.yml` as
`ghcr.io/beril-doe/beril-wiki-curator:develop` on pull requests and `:latest`
from main), runs `deploy/curate.sh` as its entry point, and is dispatched by the
manifests under `deploy/k8s/`. The dev namespace is `knowledge-engine`; the
manifests name the dev image `registry.nersc.gov/kbase/beril-wiki-curator:develop`
and dev hosts, so production changes hosts, budgets and the tag.

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
`stages/search_vectors.py`), so rather than an override the job links
`$WIKI_WORKDIR/quartz -> /opt/quartz` when the clone has no `quartz/` and
copies `/opt/theme/node_modules` into `theme/` when that is absent. The render
writes into the container, not the volume; the artifact is what persists.

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
| `WIKI_ARTIFACT_ENDPOINT`, `WIKI_ARTIFACT_PREFIX` | ConfigMap | `http://wiki:8080/wiki/_admin/store` and `wiki`: the wiki pod's store routes (below) |
| `WIKI_RELOAD_URL`, `WIKI_RELOAD_TOKEN` | ConfigMap, Secret | `http://wiki:8080/wiki/_admin/reload` and the pod's admin bearer, shared by the store routes |
| `WIKI_CURATE_MAX_TOKENS`, `WIKI_CURATE_MAX_JOBS`, `WIKI_CURATE_WORKERS` | ConfigMap | `agentic run --max-tokens / --max-jobs / --workers` |
| `WIKI_CURATE_STAGE_MAX_USD` | ConfigMap | space-separated `STAGE=USD` list, each one a `--stage-max-usd`; `STAGE` is a job-step prefix (`extract plan write lit figures curator merge merge-judge backmerge repair`) or an editorial stage, never a model role, and `curate.sh` refuses the list at every start otherwise |
| `WIKI_CURATE_EXTRA_ARGS` | ConfigMap | appended to `agentic run` verbatim (for example `--strict-pages`) |
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
| `plan` | `cronjob-plan.yaml`, hourly | refresh code; `corpus pull-hub`; `stages.fetch`; `agentic plan`; log `plan: changed_sources=N pending_editorial=N` | 0 nothing to do, 3 a run would do something (the CronJob maps 3 to success), 2 no clone |
| `run` | `cronjob-curate.yaml`, nightly; `job-run-now.yaml` | `plan`; stop at 0 when empty; else `agentic run` under the budgets; `build_quartz.sh`; `publish_artifact.sh --id <UTC stamp> --no-check`; `git push origin history refs/tags/artifact/*` | 0 published or nothing to do; non-zero on any failed step, including a held `.agentic/lock` and a refused cold start |
| `publish` | by hand | refresh code; render and publish the accepted wiki as above, without curating | as `run` |
| `status` | by hand | `agentic status`, or a note when no run has been recorded | 0 |

Every step logs one timestamped line (`2026-11-17T07:30:00Z curate[run] ...`).
Staging is empty between scheduled runs, so `plan` first runs `corpus pull-hub`
(BERIL's feed into `corpus/`, every file sha256-checked, the cursor kept in
`corpus/manifest.json`) and `stages.fetch` (`corpus/` into `staging/`), and
`changed_sources` then names the projects a run would integrate. Budgets
are fixed per run, so a bad night is capped; `agentic run` refuses a second
runner on the same checkout, and a run killed by the Job's deadline is charged
from its transcripts and resumes from cached work the next night.

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
curator's `WIKI_ARTIFACT_ENDPOINT=http://wiki:8080/wiki/_admin/store` selects
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
