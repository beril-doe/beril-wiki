#!/usr/bin/env bash
# Build the Quartz site for the BERIL wiki. Idempotent; first run clones Quartz (~2 min).
#   ./build_quartz.sh            then: cd quartz && npx quartz build --serve
# Serves at http://localhost:8080. The quartz/ clone is gitignored; content is derived.
#
#   WIKI_BASE_URL=beril-doe.org/beril-wiki ./build_quartz.sh   # for publish
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
# Palette and type follow theme/styles/beril.scss, which aliases Quartz's
# variables onto its own tokens; keep the two in step.
uv run --project "$REPO" python - "$QP" "$BASE_URL" <<'PY'
import os, pathlib, sys, yaml
qp, base_url = pathlib.Path(sys.argv[1]), sys.argv[2]
cfg = yaml.safe_load((qp / "quartz.config.default.yaml").read_text())
c = cfg["configuration"]
c["pageTitle"] = "BERIL Knowledge Wiki"
c["baseUrl"] = base_url
c["analytics"] = None
# Instrument Serif ships one weight; asking Google Fonts for 700 as well makes
# the whole stylesheet request fail, so spell the weights out.
TYPOGRAPHY = {
    "header": {"name": "Instrument Serif", "weights": [400], "includeItalic": False},
    "body": {"name": "Instrument Sans", "weights": [400, 500, 600], "includeItalic": True},
    "code": {"name": "IBM Plex Mono", "weights": [400, 500], "includeItalic": False},
}
c["theme"]["typography"] = TYPOGRAPHY
c["theme"]["colors"]["lightMode"] = {
    "light": "#fafaf7",        # page background
    "lightgray": "#dde1e4",    # rules
    "gray": "#737b83",         # muted text
    "darkgray": "#4a5158",     # secondary text
    "dark": "#1e2226",         # ink
    "secondary": "#2c63c7",    # links
    "tertiary": "#1f4fa8",     # link hover
    "highlight": "rgba(44, 99, 199, 0.08)",
    "textHighlight": "rgba(176, 122, 18, 0.3)",
}
c["theme"]["colors"]["darkMode"] = {
    "light": "#15181b",
    "lightgray": "#2c3237",
    "gray": "#8a929a",
    "darkgray": "#b5bcc3",
    "dark": "#e8eaec",
    "secondary": "#7fa6f0",
    "tertiary": "#a9c3f5",
    "highlight": "rgba(127, 166, 240, 0.12)",
    "textHighlight": "rgba(224, 169, 58, 0.3)",
}
# The frame renders its own title, navigation, neighbours and backlinks, so
# the stock components for those are switched off rather than hidden.
FRAME_REPLACES = {
    "explorer", "graph", "backlinks", "article-title", "content-meta",
    "tag-list", "page-title", "reader-mode", "breadcrumbs", "spacer",
}
# Footer is on every page by construction, so it carries the things a reader
# needs from anywhere: what this is, how to cite it, its licence, and where the
# reports come from. No link to the BERIL Atlas: this wiki is intended to take
# its place, so sending readers there is the wrong direction of travel.
for p in cfg["plugins"]:
    name = p["source"].removeprefix("@quartz-community/")
    if name in FRAME_REPLACES:
        p["enabled"] = False
    # Search and the theme toggle sit in the frame's top bar (the header slot),
    # not in the default toolbar group of the left sidebar.
    if name in ("search", "darkmode"):
        p["layout"] = {"position": "header", "priority": 10 if name == "search" else 20}
    # CNAME is only for a per-repo custom domain. The org already serves Pages
    # from the verified domain beril-doe.org, so this project site is routed to
    # beril-doe.org/beril-wiki without a CNAME file; writing one derived from
    # baseUrl's host would instead claim the bare domain for this repo. Emit one
    # only when a per-repo domain is explicitly asked for.
    # The fonts plugin emits its own --headerFont/--bodyFont after the theme
    # block and falls back to Quartz's stock faces unless told otherwise.
    if name == "quartz-fonts":
        p["options"] = {"useThemeFonts": False, **TYPOGRAPHY}
    if name == "cname":
        p["enabled"] = bool(os.environ.get("WIKI_CNAME"))
    # Frontmatter here is machinery — type, description, the sources list that
    # keeps citations honest. Rendered as a properties table above every page
    # it reads as debug output, and the description just restates the opening
    # paragraph. Hide the table, do NOT disable the plugin: it is also Quartz's
    # frontmatter parser, so switching it off leaves every page "Untitled".
    if name == "note-properties":
        p["options"]["hidePropertiesView"] = True
    # No page in this corpus declares tags. Every "tag" Quartz finds is Obsidian
    # syntax matching ordinary prose in the raw reports -- "the #1-ranked gene
    # AO356_11255" produced a published /tags/1-ranked page. Turning the tag
    # routes off removes a taxonomy the corpus never claimed.
    if name == "tag-page":
        p["enabled"] = False
    if name == "footer":
        p["options"]["links"] = {
            "About & how to cite": "https://" + base_url.rstrip("/") + "/about",
            "BERIL Observatory": "https://beril.kbase.us/",
            "Source": "https://github.com/beril-doe/beril-wiki",
            "AGPL-3.0": "https://www.gnu.org/licenses/agpl-3.0.html",
        }
# The theme plugin: a path relative to the quartz/ directory, where the build
# runs. It contributes the "beril" page frame used for content and folder pages.
cfg["plugins"].append({"source": "../theme", "enabled": True})
for page_type in ("content", "folder"):
    cfg["layout"]["byPageType"].setdefault(page_type, {})["template"] = "beril"
(qp / "quartz.config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True))
PY

# Stylesheet: Quartz compiles quartz/styles/custom.scss unlayered, after its
# own base layer, so this is where the theme's CSS goes. Copied every build
# because quartz/ is a gitignored clone.
cp "$THEME/styles/beril.scss" "$QP/quartz/styles/custom.scss"

# Publish is render-only: wiki/ and wiki-extra/ are committed, so no stage
# regeneration here (run_pipeline.sh owns that). Figures come from the
# observatory checkout when present; a checkout-less clone renders without them.
uv run --project "$REPO" python "$HERE/quartz_ingest.py" "$REPO" "$QP/content"
(cd "$QP" && npx quartz build)
echo
echo "built. serve with:  cd $QP && npx quartz build --serve"
