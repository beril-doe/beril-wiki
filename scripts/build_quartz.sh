#!/usr/bin/env bash
# Build the Quartz site for the BERIL wiki. Idempotent; first run clones Quartz (~2 min).
#   scripts/build_quartz.sh      then: cd quartz && npx quartz build --serve
# Serves at http://localhost:8080. The quartz/ clone is gitignored; content is derived.
#
#   WIKI_BASE_URL=beril-doe.org/beril-wiki scripts/build_quartz.sh   # for publish
#
# baseUrl sets absolute links, the sitemap and RSS. A CNAME file is emitted only
# when WIKI_CNAME is set, since that file belongs to a custom domain and not to
# a github.io project page.
#
# The look of the site lives in theme/ (a local Quartz plugin providing the page
# frame, plus the stylesheet). Nothing under quartz/ is edited by hand: this
# script regenerates the config and copies the stylesheet in on every run.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
QP="$REPO/quartz"
THEME="$REPO/theme"
BASE_URL="${WIKI_BASE_URL:-localhost:8080}"
# Pinned: quartz/ is a gitignored clone, so an unpinned upstream main means
# every CI build renders against whatever Quartz shipped that day. This is the
# commit the current site was built and reviewed against; a tag also works.
QUARTZ_REF="${QUARTZ_REF:-075afd3f712da0088a07f5284a7b3aba37dd61b6}"

if [ ! -d "$QP" ]; then
  git init --quiet "$QP"
  git -C "$QP" remote add origin https://github.com/jackyzha0/quartz.git
  git -C "$QP" fetch --quiet --depth 1 origin "$QUARTZ_REF"
  git -C "$QP" checkout --quiet FETCH_HEAD
  npm --prefix "$QP" install --silent
fi

# Theme plugin. Quartz symlinks a local plugin into .quartz/plugins at build
# time but does not compile it, so build it here. preact is linked from the
# Quartz install rather than installed again: the frame's elements must come
# from the same copy of preact that renders them.
npm --prefix "$THEME" install --silent --no-audit --no-fund
rm -rf "$THEME/node_modules/preact"
ln -s "$QP/node_modules/preact" "$THEME/node_modules/preact"
npm --prefix "$THEME" run --silent build

# Quartz 5 reads quartz.config.yaml; derive ours from the shipped default every
# build (idempotent) so theme/config changes here always take effect.
uv run --project "$REPO" python -m beril_wiki.publish.quartz_config "$QP" "$BASE_URL"

# Stylesheet: Quartz compiles quartz/styles/custom.scss unlayered, after its
# own base layer, so this is where the theme's CSS goes. Copied every build
# because quartz/ is a gitignored clone.
cp "$THEME/styles/beril.scss" "$QP/quartz/styles/custom.scss"

# Publish is render-only: wiki/ is committed, so no stage
# regeneration here (run_pipeline.sh owns that). Figures come from the
# observatory checkout when present; a checkout-less clone renders without them.
uv run --project "$REPO" python -m beril_wiki.publish.ingest "$REPO" "$QP/content"
(cd "$QP" && npx quartz build)
echo
echo "built. serve with:  cd $QP && npx quartz build --serve"
