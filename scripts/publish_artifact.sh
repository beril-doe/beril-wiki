#!/usr/bin/env bash
# Publish the built site (quartz/public, from build_quartz.sh) as a versioned
# artifact and make it current, so the running wiki container can swap to it
# with POST /wiki/_admin/reload. No commit, image build or rollout.
#
#   scripts/publish_artifact.sh [--id ID] [--no-check]
#   scripts/publish_artifact.sh --point ID
#
# A successful push also commits wiki/, state/, corpus/ and the
# vectors to the `history` branch and tags artifact/<id>; `artifact rollback
# --to <id>` moves current back and restores the checkout from that tag.
# --point ID skips the build and the push: it moves current to an artifact
# already in the store (deploy/curate.sh finishing a publish whose history is
# on origin but whose current never moved) and reloads.
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
POINT=""
ARGS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --no-check) CHECK=0 ;;
    --point) POINT="${2:?--point needs an artifact id}"; shift ;;
    *) ARGS+=("$1") ;;
  esac
  shift
done

if [ -n "$POINT" ]; then
  uv run --project "$REPO" python -c '
import json, sys
from beril_wiki.publish import artifact as A
store, keys = A.store_from_env(), A.Keys(A.prefix_from_env())
print(json.dumps(A.point_current(store, keys, sys.argv[1]), indent=1))' "$POINT"
else
  # The same gates that block a Pages deploy or an image push block an artifact:
  # check --strict, the theme typecheck and check_site.sh. `push` refuses without
  # a record of all three passing on exactly this build (quartz/gate-results.json,
  # written here or by build_quartz.sh); --no-check reuses the build's record.
  if [ "$CHECK" = 1 ]; then
    uv run --project "$REPO" python -m beril_wiki.publish.artifact gate --root "$REPO" --site "$SITE"
  fi
  uv run --project "$REPO" python -m beril_wiki.publish.artifact push \
    --root "$REPO" --site "$SITE" --base-url "${WIKI_BASE_URL:-}" "${ARGS[@]}"
fi

if [ -n "${WIKI_RELOAD_URL:-}" ] && [ -n "${WIKI_RELOAD_TOKEN:-}" ]; then
  curl -fsS -X POST -H "Authorization: Bearer $WIKI_RELOAD_TOKEN" "$WIKI_RELOAD_URL"
  echo
fi
