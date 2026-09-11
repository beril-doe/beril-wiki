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
#   entities  merge entity pages identified as the same entity (no-op when clean)
#   conflicts promote multi-project Tensions to conflict pages (hash-skipped)
#   hubs     re-cluster + regenerate only topic hubs whose members changed
#   figures  manifest + LLM figure placements (hash-skipped)
#   extras   deterministic author/data pages
#   names    rename the data platform to its current name (deterministic)
#   repair   re-run any page failing write-time validation (no-op when clean)
#   check    citation, numeric, uptake, and duplicate-concept audits (fails on errors)
#   publish  Quartz static site (dead links stripped, evidence labels added)
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

# Entity identity resolution. Deterministic detection (name / declared alias /
# external id in the Identity section), never similarity: embeddings rank two
# different genes at 0.971 over these pages. A corpus with no duplicates makes
# no model call, so this is a no-op in the steady state.
echo "== entities" | tee -a "$LOG"
"${PY[@]}" "$HERE/entity_dedup.py" --apply | tee -a "$LOG" | tail -3

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

# The platform is the KBase Data Lakehouse. Reports written while it was
# called BERDL, or the BER Data Lakehouse, seed those names into every page
# compiled from them, so the rename runs after everything that writes a page
# and before the checks. Deterministic and idempotent; no LLM call.
echo "== names" | tee -a "$LOG"
"${PY[@]}" "$HERE/normalize_names.py" "$REPO" | tee -a "$LOG"

# Compile's resume-skip is per document, so a page that mis-attributes one
# number stays broken while the document that fixes it counts as integrated.
# This runs before check so those pages are repaired rather than merely
# reported; a corpus that already validates makes no LLM calls.
echo "== repair" | tee -a "$LOG"
"${PY[@]}" "$HERE/repair_page.py" | tee -a "$LOG" | tail -3

echo "== check" | tee -a "$LOG"
"${PY[@]}" "$HERE/wiki_check.py" "$REPO" | tee -a "$LOG"

if [ "${1:-}" != "--no-publish" ]; then
  echo "== publish" | tee -a "$LOG"
  "$HERE/build_quartz.sh" 2>&1 | tail -2 | tee -a "$LOG"
fi
echo "== pipeline done"
