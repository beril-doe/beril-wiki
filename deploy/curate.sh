#!/usr/bin/env bash
# The scheduled curator's entry point (Dockerfile.curator, deploy/k8s/).
#
#   curate.sh plan      refresh code, `corpus pull-hub` (BERIL's feed -> corpus/),
#                       `stages.fetch` (corpus/ -> staging/), `agentic plan`; exit 3
#                       when a run would do something, 0 otherwise
#   curate.sh run       plan (reported), `agentic run` under the env budgets, and
#                       when it promoted: render, publish, push `history`
#   curate.sh publish   render and publish the accepted wiki without curating
#   curate.sh render    render only (quartz/public), for checking an image
#   curate.sh status    `agentic status`
#
# The PVC at WIKI_WORKDIR holds a git clone of beril-wiki: code and the trees the
# curator owns (wiki/ state/ corpus/ search/ .agentic/) together. Only the code
# paths are refreshed from WIKI_GIT_REF at start; the data trees are never
# checked out, so `main` stops being authoritative for them once this has run
# and the `history` branch is. A missing clone is created only when
# BERIL_WIKI_ALLOW_COLD_START=1 (deploy/README.md, "First-time population").
#
# Environment (deploy/README.md has the full table): WIKI_WORKDIR, WIKI_GIT_URL,
# WIKI_GIT_REF, WIKI_GIT_TOKEN (push access to history; read by a credential
# helper at call time, never written anywhere), WIKI_CURATE_MAX_TOKENS,
# WIKI_CURATE_MAX_JOBS, WIKI_CURATE_WORKERS, WIKI_CURATE_STAGE_MAX_USD
# ("STAGE=USD STAGE=USD"), WIKI_CURATE_EXTRA_ARGS, WIKI_BASE_URL, and what
# build_quartz.sh / publish_artifact.sh / the agentic runner read themselves.
set -euo pipefail

MODE="${1:-plan}"
WIKI_WORKDIR="${WIKI_WORKDIR:-/work/beril-wiki}"
WIKI_GIT_URL="${WIKI_GIT_URL:-https://github.com/beril-doe/beril-wiki.git}"
WIKI_GIT_REF="${WIKI_GIT_REF:-main}"
# Refreshed from WIKI_GIT_REF every start. Never wiki/ state/ corpus/ search/.
CODE_PATHS=(src scripts theme contract deploy pyproject.toml uv.lock agentic.yaml
  Dockerfile Dockerfile.curator)
# Pre-warmed in the image; seeded into the clone when it has none of its own.
WIKI_QUARTZ_CACHE="${WIKI_QUARTZ_CACHE:-/opt/quartz}"
WIKI_THEME_CACHE="${WIKI_THEME_CACHE:-/opt/theme}"

log() { printf '%s curate[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$MODE" "$*" >&2; }
die() { log "ERROR $*"; exit "${2:-1}"; }

case "$MODE" in plan | run | publish | render | status) ;; *) die "unknown mode '$MODE'" 64 ;; esac

# --- git: identity for history commits, token through a helper, no prompts ---
export GIT_TERMINAL_PROMPT=0
export GIT_AUTHOR_NAME="${WIKI_GIT_NAME:-BERIL wiki curator}" \
  GIT_COMMITTER_NAME="${WIKI_GIT_NAME:-BERIL wiki curator}" \
  GIT_AUTHOR_EMAIL="${WIKI_GIT_EMAIL:-wiki-curator@beril.invalid}" \
  GIT_COMMITTER_EMAIL="${WIKI_GIT_EMAIL:-wiki-curator@beril.invalid}"
git_env() {
  # Append key=value to git's environment-held config: it applies to every git
  # call this job makes (fetch, search_data pull, push) and lands in no file.
  local n="${GIT_CONFIG_COUNT:-0}"
  export "GIT_CONFIG_KEY_$n=$1" "GIT_CONFIG_VALUE_$n=$2" GIT_CONFIG_COUNT=$((n + 1))
}
# The volume may have been populated by another uid than the job's.
git_env safe.directory "$WIKI_WORKDIR"
if [ -n "${WIKI_GIT_TOKEN:-}" ]; then
  # The helper prints the token from the environment when git asks for it; the
  # token itself is in no config value, file or command line.
  git_env credential.helper \
    '!f() { printf "username=x-access-token\npassword=%s\n" "$WIKI_GIT_TOKEN"; }; f'
  git_env url.https://github.com/.insteadOf git@github.com:
fi

# --- python: the image's venv (UV_PROJECT_ENVIRONMENT, UV_NO_SYNC) running the
# clone's code; on a laptop `uv run` syncs the clone's own .venv instead. -------
export BERIL_WIKI_ROOT="$WIKI_WORKDIR" PYTHONPATH="$WIKI_WORKDIR/src${PYTHONPATH:+:$PYTHONPATH}"
py() { uv run --project "$WIKI_WORKDIR" python "$@"; }
agentic() { py -m beril_wiki.agentic --root "$WIKI_WORKDIR" "$@"; }

refresh_code() {
  if [ ! -d "$WIKI_WORKDIR/.git" ]; then
    [ "${BERIL_WIKI_ALLOW_COLD_START:-}" = 1 ] || die "no git clone at $WIKI_WORKDIR. \
Mount the persistent volume that holds the clone (wiki/, state/, corpus/, search/, \
.agentic/), or set BERIL_WIKI_ALLOW_COLD_START=1 to clone $WIKI_GIT_URL and start from \
the committed trees on purpose." 2
    log "no clone at $WIKI_WORKDIR; cold start allowed, cloning $WIKI_GIT_URL ($WIKI_GIT_REF)"
    git clone --quiet --branch "$WIKI_GIT_REF" "$WIKI_GIT_URL" "$WIKI_WORKDIR"
  fi
  if [ "${WIKI_SKIP_CODE_REFRESH:-}" = 1 ]; then
    log "code refresh skipped (WIKI_SKIP_CODE_REFRESH=1)"
    return
  fi
  git -C "$WIKI_WORKDIR" fetch --quiet origin "$WIKI_GIT_REF"
  # Only paths the ref has, so a file not yet on it does not fail the checkout;
  # then drop files the ref removed, which checkout -- <path> leaves behind.
  local present
  present=$(git -C "$WIKI_WORKDIR" ls-tree --name-only FETCH_HEAD -- "${CODE_PATHS[@]}")
  [ -n "$present" ] || die "none of ${CODE_PATHS[*]} exist on $WIKI_GIT_REF"
  # shellcheck disable=SC2086
  git -C "$WIKI_WORKDIR" checkout --quiet FETCH_HEAD -- $present
  comm -23 <(git -C "$WIKI_WORKDIR" ls-files -- "${CODE_PATHS[@]}" | sort) \
    <(git -C "$WIKI_WORKDIR" ls-tree -r --name-only FETCH_HEAD -- "${CODE_PATHS[@]}" | sort) |
    while IFS= read -r stale; do
      git -C "$WIKI_WORKDIR" rm --quiet --cached -- "$stale" && rm -f "$WIKI_WORKDIR/$stale"
    done
  log "code: $(git -C "$WIKI_WORKDIR" rev-parse --short FETCH_HEAD) of $WIKI_GIT_REF -> ${CODE_PATHS[*]}"
}

seed_build_caches() {
  # quartz/ is gitignored and derived, and it must be a real directory in the
  # clone: Quartz loads the theme plugin as ../theme relative to its own physical
  # path, so a `quartz -> /opt/quartz` symlink resolved the theme to /opt/theme
  # (node_modules, no dist/) and Quartz silently rendered its default frame. The
  # image's clone is copied in on the first run and replaced when the pinned
  # Quartz commit changes; the build then writes into the volume.
  local q="$WIKI_WORKDIR/quartz" want have=""
  if [ -L "$q" ]; then
    rm "$q"
    log "quartz: removed the symlink an earlier job left"
  fi
  if [ -d "$WIKI_QUARTZ_CACHE/node_modules" ]; then
    want=$(git -C "$WIKI_QUARTZ_CACHE" rev-parse HEAD)
    [ ! -d "$q/.git" ] || have=$(git -C "$q" rev-parse HEAD 2>/dev/null || true)
    if [ "$have" != "$want" ]; then
      rm -rf "$q"
      cp -a "$WIKI_QUARTZ_CACHE" "$q"
      log "quartz: copied $WIKI_QUARTZ_CACHE (${want:0:12}) into the clone"
    fi
  fi
  if [ ! -d "$WIKI_WORKDIR/theme/node_modules" ] && [ -d "$WIKI_THEME_CACHE/node_modules" ]; then
    cp -R "$WIKI_THEME_CACHE/node_modules" "$WIKI_WORKDIR/theme/node_modules"
    log "theme: seeded node_modules from $WIKI_THEME_CACHE"
  fi
}

plan_step() {
  # Brings corpus/ up to BERIL's feed (every file sha256-checked; nothing installed
  # on a failure), stages it, then prints the plan and logs its counts. Returns 3
  # when a run would do something, by run's own test: the accepted fingerprint
  # (sources, README and figure bytes, errata, code, models) no longer matches, or
  # a page is queued for a retry. A run never talks to the hub itself: it reads
  # corpus/ as its checkout. The nightly does not gate on this return: `agentic
  # run` makes the same test and is the authority.
  local out summary
  # Checked explicitly: errexit is off inside a function called in a && or || list.
  py -m beril_wiki.corpus pull-hub || die "corpus pull-hub failed (exit $?)"
  py -m beril_wiki.stages.fetch >/dev/null || die "stages.fetch failed (exit $?)"
  out=$(agentic plan) || die "agentic plan failed (exit $?)"
  printf '%s\n' "$out"
  summary=$(printf '%s' "$out" | py -c '
import json, sys
d = json.load(sys.stdin)
keys = ("changed_sources", "pending_editorial", "retry_pages")
counts = {k: len(d.get(k) or []) for k in keys}
current = d.get("accepted_current")
work = any(counts.values()) or current is False
shown = "unknown" if current is None else str(current).lower()
print(int(work), " ".join(f"{k}={v}" for k, v in counts.items()), f"accepted_current={shown}")') ||
    die "could not read the plan"
  log "plan: ${summary#* }"
  [ "${summary%% *}" = 0 ] && return 0 || return 3
}

accepted_hash() {
  # Promotion rewrites state/agentic.json with a fresh fingerprint; a run that found
  # the state current leaves it alone.
  git -C "$WIKI_WORKDIR" hash-object state/agentic.json 2>/dev/null || echo none
}

render_step() {
  : "${WIKI_BASE_URL:?WIKI_BASE_URL is required to render (e.g. beril.kbase.us/wiki)}"
  log "render: build_quartz.sh (WIKI_BASE_URL=$WIKI_BASE_URL)"
  "$WIKI_WORKDIR/scripts/build_quartz.sh"
  # The theme's frame, not Quartz's default: a plugin Quartz could not load is
  # only a log line ("Unknown page frame beril, falling back to default"), so
  # check the output rather than the exit code. The wordmark is the theme's top
  # bar (theme/src/components/Bar.tsx), on every page including the home page.
  grep -q 'class="wordmark"' "$WIKI_WORKDIR/quartz/public/index.html" ||
    die "render: quartz/public/index.html carries no BERIL frame (theme plugin not loaded)"
}

publish_step() {
  local stamp
  stamp=$(date -u +%Y%m%dT%H%M%SZ)
  render_step
  # The gates ran inside build_quartz.sh and are recorded for this exact build;
  # push refuses without that record, so --no-check repeats nothing.
  log "publish: artifact $stamp -> ${WIKI_ARTIFACT_ENDPOINT:-<no store>}"
  "$WIKI_WORKDIR/scripts/publish_artifact.sh" --id "$stamp" --no-check
  if git -C "$WIKI_WORKDIR" rev-parse --verify --quiet refs/heads/history >/dev/null; then
    log "push: history and artifact/* tags to origin"
    git -C "$WIKI_WORKDIR" push --quiet origin history 'refs/tags/artifact/*'
  else
    log "push: no history branch recorded yet; nothing to push"
  fi
}

check_caps() {
  # The caps name job-step prefixes (extract plan write ...) or editorial stages,
  # never model roles; `agentic run` refuses anything else, so check here, in the
  # hourly plan too, rather than at the nightly run hours later.
  # shellcheck disable=SC2086
  py -c '
import sys
from beril_wiki.agentic.__main__ import check_usd_caps
from beril_wiki.agentic.runtime import WorkflowError
try:
    check_usd_caps(sys.argv[1:])
except WorkflowError as exc:
    sys.exit(f"WIKI_CURATE_STAGE_MAX_USD: {exc}")' ${WIKI_CURATE_STAGE_MAX_USD:-} ||
    die "stage caps rejected (exit $?)"
}

run_step() {
  local args=(run)
  args+=(--max-tokens "${WIKI_CURATE_MAX_TOKENS:?WIKI_CURATE_MAX_TOKENS is required}")
  args+=(--max-jobs "${WIKI_CURATE_MAX_JOBS:?WIKI_CURATE_MAX_JOBS is required}")
  args+=(--workers "${WIKI_CURATE_WORKERS:-4}")
  local cap
  for cap in ${WIKI_CURATE_STAGE_MAX_USD:-}; do args+=(--stage-max-usd "$cap"); done
  # shellcheck disable=SC2206
  [ -z "${WIKI_CURATE_EXTRA_ARGS:-}" ] || args+=(${WIKI_CURATE_EXTRA_ARGS})
  log "curate: agentic ${args[*]} (auth ${BERIL_WIKI_AUTH:-subscription})"
  # A held .agentic/lock or a missing accepted state stops here with a non-zero
  # exit. Returns 0 when the run promoted a new accepted state, 1 when it found
  # the state current ("unchanged; zero model calls") and there is nothing to publish.
  local before
  before=$(accepted_hash)
  agentic "${args[@]}" || die "agentic run failed (exit $?)"
  [ "$(accepted_hash)" != "$before" ]
}

main() {
  local started rc
  started=$(date +%s)
  log "start in $WIKI_WORKDIR"
  case "$MODE" in
    plan)
      refresh_code
      check_caps
      plan_step && rc=0 || rc=$?
      ;;
    run)
      refresh_code
      check_caps
      seed_build_caches
      plan_step || true # reported; agentic run makes the same test itself
      if run_step; then
        publish_step
      else
        log "accepted state unchanged by the run; nothing to publish"
      fi
      rc=0
      ;;
    publish)
      refresh_code
      seed_build_caches
      publish_step
      rc=0
      ;;
    render)
      refresh_code
      seed_build_caches
      render_step
      rc=0
      ;;
    status)
      [ -d "$WIKI_WORKDIR/.git" ] || die "no clone at $WIKI_WORKDIR" 2
      if [ -f "$WIKI_WORKDIR/.agentic/config.json" ]; then
        agentic status
      else
        log "no run has been recorded in $WIKI_WORKDIR/.agentic yet"
      fi
      rc=0
      ;;
  esac
  log "done in $(( $(date +%s) - started ))s (exit $rc)"
  exit "$rc"
}

# Sourced (tests), the functions are defined and nothing runs.
[[ "${BASH_SOURCE[0]}" != "$0" ]] || main
