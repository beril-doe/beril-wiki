#!/usr/bin/env bash
# Build the Quartz site for the BERIL wiki. Idempotent; first run clones Quartz (~2 min).
#   ./build_quartz.sh            then: cd quartz && npx quartz build --serve
# Serves at http://localhost:8080. The quartz/ clone is gitignored; content is derived.
#
#   WIKI_BASE_URL=beril-doe.github.io/beril-wiki ./build_quartz.sh   # for publish
#
# baseUrl sets absolute links, the sitemap and RSS. A CNAME file is emitted only
# when WIKI_CNAME is set, since that file belongs to a custom domain and not to
# a github.io project page.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
QP="$REPO/quartz"
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

# Quartz 5 reads quartz.config.yaml; derive ours from the shipped default every
# build (idempotent) so theme/config changes here always take effect.
# Palette + type mirror the BERIL workbench themes (apps/web/src/themes.css):
# "paper" light and "observatory" violet-ink dark; Fraunces / IBM Plex.
uv run --project "$REPO" python - "$QP" "$BASE_URL" <<'PY'
import os, pathlib, sys, yaml
qp, base_url = pathlib.Path(sys.argv[1]), sys.argv[2]
cfg = yaml.safe_load((qp / "quartz.config.default.yaml").read_text())
c = cfg["configuration"]
c["pageTitle"] = "BERIL Knowledge Wiki"
c["baseUrl"] = base_url
c["analytics"] = None
c["theme"]["typography"] = {
    "header": "Fraunces", "body": "IBM Plex Sans", "code": "IBM Plex Mono",
}
c["theme"]["colors"]["lightMode"] = {          # workbench "paper"
    "light": "#faf9f7",        # --background
    "lightgray": "#e5e2db",    # --border
    "gray": "#6f6c7a",         # --muted-foreground
    "darkgray": "#1d1b24",     # --foreground (body text)
    "dark": "#1d1b24",         # headers
    "secondary": "#6d28d9",    # --primary (links, site title)
    "tertiary": "#8b5cf6",     # hover/visited
    "highlight": "rgba(109, 40, 217, 0.08)",
    "textHighlight": "rgba(109, 40, 217, 0.25)",
}
c["theme"]["colors"]["darkMode"] = {           # workbench "observatory"
    "light": "#0b0a10",
    "lightgray": "#272430",
    "gray": "#918e9f",
    "darkgray": "#e7e5ee",
    "dark": "#e7e5ee",
    "secondary": "#a78bfa",
    "tertiary": "#c4b5fd",
    "highlight": "rgba(167, 139, 250, 0.1)",
    "textHighlight": "rgba(167, 139, 250, 0.3)",
}
# Footer is on every page by construction, so it carries the things a reader
# needs from anywhere: what this is, how to cite it, its licence, and the
# observatory's reviewed knowledge surface next door.
for p in cfg["plugins"]:
    # CNAME is only for a custom domain. Quartz derives it from baseUrl's host,
    # which for a project page yields "beril-doe.github.io" — a file that would
    # tell Pages to serve this repo at the org's user-site domain. Emit one only
    # when a real custom domain is asked for.
    if p["source"] == "@quartz-community/cname":
        p["enabled"] = bool(os.environ.get("WIKI_CNAME"))
    if p["source"] == "@quartz-community/footer":
        p["options"]["links"] = {
            "About & how to cite": "https://" + base_url.rstrip("/") + "/about",
            "BERIL Atlas": "https://beril.kbase.us/atlas",
            "BERIL Observatory": "https://beril.kbase.us/",
            "Source": "https://github.com/beril-doe/beril-wiki",
            "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/",
        }
(qp / "quartz.config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True))
PY

# Thin, quiet scrollbars everywhere — mirrors the workbench's .beril-scroll
# (apps/web/src/index.css) against Quartz's palette, where --lightgray is the
# workbench --border and --gray is --muted-foreground. Rewritten every build
# because quartz/ is a gitignored clone.
cat > "$QP/quartz/styles/custom.scss" <<'SCSS'
@use "./variables.scss" as *;

// Scrollbars that do not shout. Mirrors the BERIL workbench .beril-scroll.
*::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
*::-webkit-scrollbar-track {
  background: transparent;
}
*::-webkit-scrollbar-thumb {
  border-radius: 999px;
  background: color-mix(in oklab, var(--gray) 40%, transparent);
}
*::-webkit-scrollbar-thumb:hover {
  background: color-mix(in oklab, var(--gray) 60%, transparent);
}
@supports (scrollbar-width: thin) {
  * {
    scrollbar-width: thin;
    scrollbar-color: var(--lightgray) transparent;
  }
}
SCSS

# Publish is render-only: wiki/ and wiki-extra/ are committed, so no stage
# regeneration here (run_pipeline.sh owns that). Figures come from the
# observatory checkout when present; a checkout-less clone renders without them.
uv run --project "$REPO" python "$HERE/quartz_ingest.py" "$REPO" "$QP/content"
(cd "$QP" && npx quartz build)
echo
echo "built. serve with:  cd $QP && npx quartz build --serve"
