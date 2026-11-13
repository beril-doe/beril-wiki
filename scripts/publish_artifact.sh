#!/usr/bin/env bash
# Publish the built site (quartz/public, from build_quartz.sh) as a versioned
# artifact and make it current, so the running wiki container can swap to it
# with POST /wiki/_admin/reload. No commit, image build or rollout.
#
#   scripts/publish_artifact.sh [--id ID] [--no-check]
#
# A successful push also commits wiki/, state/, corpus/index.json and the
# vectors to the `history` branch and tags artifact/<id>; `artifact rollback
# --to <id>` moves current back and restores the checkout from that tag.
#
# Needs the store in the environment (beril_wiki.publish.artifact):
#   WIKI_ARTIFACT_ENDPOINT   https://s3.example or file:///a/directory
#   WIKI_ARTIFACT_BUCKET WIKI_ARTIFACT_PREFIX WIKI_ARTIFACT_ACCESS_KEY WIKI_ARTIFACT_SECRET_KEY
# and, to tell the server, WIKI_RELOAD_URL (e.g. http://localhost:8080/wiki/_admin/reload)
# with WIKI_RELOAD_TOKEN; without them the artifact is published and the reload
# is left to the caller.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
SITE="$REPO/quartz/public"
CHECK=1
ARGS=()
for arg in "$@"; do
  case "$arg" in
    --no-check) CHECK=0 ;;
    *) ARGS+=("$arg") ;;
  esac
done

# The same gates that block a Pages deploy or an image push block an artifact:
# check --strict, the theme typecheck and check_site.sh. `push` refuses without
# a record of all three passing on exactly this build (quartz/gate-results.json,
# written here or by build_quartz.sh); --no-check reuses the build's record.
if [ "$CHECK" = 1 ]; then
  uv run --project "$REPO" python -m beril_wiki.publish.artifact gate --root "$REPO" --site "$SITE"
fi

uv run --project "$REPO" python -m beril_wiki.publish.artifact push \
  --root "$REPO" --site "$SITE" --base-url "${WIKI_BASE_URL:-}" "${ARGS[@]}"

if [ -n "${WIKI_RELOAD_URL:-}" ] && [ -n "${WIKI_RELOAD_TOKEN:-}" ]; then
  curl -fsS -X POST -H "Authorization: Bearer $WIKI_RELOAD_TOKEN" "$WIKI_RELOAD_URL"
  echo
fi
