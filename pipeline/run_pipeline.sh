#!/usr/bin/env bash
# BERIL wiki — the whole pipeline, bootstrap and incremental alike.
#
#   CBORG_API_KEY=... ./run_pipeline.sh            # full run
#   ./run_pipeline.sh --no-publish                 # skip the Quartz build
#
# Every stage is incremental/idempotent, so the SAME command handles the first
# pass and every subsequent addition:
#   fetch    sync projects/*/REPORT.md + docs digests into staging/
#   compile  first-party compiler — content-hash skips unchanged docs
#   consolidate embedding-ranked concept merges + evidence back-merge (free embeds)
#   conflicts promote multi-project Tensions to conflict pages (hash-skipped)
#   hubs     re-cluster + regenerate only topic hubs whose members changed
#   figures  manifest + LLM figure placements (hash-skipped)
#   extras   deterministic author/data pages
#   check    citation, numeric, uptake, and duplicate-concept audits (fails on errors)
#   publish  Quartz static site (dead links stripped at publish)
#
# ./run_pipeline.sh --force        rebuild every derived stage, ignoring caches
# ./run_pipeline.sh --no-publish   skip the Quartz build
set -euo pipefail
# --force rebuilds every derived stage instead of trusting its cache. Use it
# after a change to a stage's prompt or grouping rule, which the content hashes
# cannot see. Without it the pipeline is incremental and an unchanged corpus is
# a no-op. Anything reproducible belongs here, not in ad-hoc rm of state files.
FORCE=""
for a in "$@"; do [ "$a" = "--force" ] && FORCE="--force"; done
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
LOG="$REPO/pipeline.log"
: "${CBORG_API_KEY:?set CBORG_API_KEY}"
export OPENAI_API_KEY="$CBORG_API_KEY"
export OPENAI_BASE_URL="${OPENAI_BASE_URL:-https://api.cborg.lbl.gov}"
PY=(uv run --project "$REPO" python)

echo "== fetch" | tee "$LOG"
"${PY[@]}" "$HERE/fetch_reports.py" | tee -a "$LOG"

echo "== compile" | tee -a "$LOG"
"${PY[@]}" "$HERE/compile.py" | tee -a "$LOG" | tail -3
if grep -qE "\[ERROR\]" "$LOG"; then echo "compile had errors — see $LOG"; exit 1; fi

echo "== enrich" | tee -a "$LOG"
"${PY[@]}" "$HERE/enrich_concepts.py" | tee -a "$LOG" | tail -3

echo "== consolidate" | tee -a "$LOG"
"${PY[@]}" "$HERE/consolidate_concepts.py" | tee -a "$LOG" | tail -3

echo "== conflicts" | tee -a "$LOG"
"${PY[@]}" "$HERE/conflicts_build.py" ${FORCE} | tee -a "$LOG"

echo "== hubs" | tee -a "$LOG"
"${PY[@]}" "$HERE/topics_build.py" ${FORCE} | tee -a "$LOG"

echo "== literature" | tee -a "$LOG"
"${PY[@]}" "$HERE/lit_context.py" ${FORCE} | tee -a "$LOG" | tail -3

echo "== figures" | tee -a "$LOG"
"${PY[@]}" "$HERE/figures_build.py" ${FORCE} | tee -a "$LOG" | tail -3

echo "== extras" | tee -a "$LOG"
"${PY[@]}" "$HERE/extra_pages.py" | tee -a "$LOG"

echo "== authors" | tee -a "$LOG"
"${PY[@]}" "$HERE/authors_build.py" | tee -a "$LOG" | tail -3

echo "== check" | tee -a "$LOG"
"${PY[@]}" "$HERE/wiki_check.py" "$REPO" | tee -a "$LOG"

if [ "${1:-}" != "--no-publish" ]; then
  echo "== publish" | tee -a "$LOG"
  "$HERE/build_quartz.sh" 2>&1 | tail -2 | tee -a "$LOG"
fi
echo "== pipeline done"
