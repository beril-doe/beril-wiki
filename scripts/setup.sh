#!/usr/bin/env bash
# One-shot setup: everything needed to build and view the wiki locally.
#   scripts/setup.sh    then:  cd quartz && npx quartz build --serve
# Needs: uv (python env) and node/npm (Quartz). Viewing requires no API keys
# and no observatory checkout — the compiled wiki is committed in this repo.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"

command -v uv >/dev/null   || { echo "missing uv — install with:  brew install uv  (or https://docs.astral.sh/uv/)"; exit 1; }
command -v node >/dev/null || { echo "missing node — install with:  brew install node  (or https://nodejs.org)"; exit 1; }

uv sync --project "$REPO"
"$HERE/build_quartz.sh"
echo
echo "setup done. view the wiki with:"
echo "  cd $REPO/quartz && npx quartz build --serve     # http://localhost:8080"
