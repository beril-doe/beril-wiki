#!/usr/bin/env bash
# Build the Quartz site for the BERIL wiki. Idempotent; first run clones Quartz (~2 min).
#   ./build_quartz.sh            then: node pipeline/serve_quartz.cjs
# Serves at http://localhost:8080. The quartz/ clone is gitignored; content is derived.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
QP="$REPO/quartz"

# Upgrade cached legacy pages through the same deterministic code as generation.
# These checks complete before touching the last successful rendered site.
uv run --project "$REPO" python "$HERE/okf.py" "$REPO"
uv run --project "$REPO" python "$HERE/wiki_check.py" "$REPO"
uv run --project "$REPO" python "$HERE/okf_tools.py" "$REPO" --graph "$REPO/build/okf-graph.html"

if [ ! -d "$QP" ]; then
  git clone --depth 1 --quiet https://github.com/jackyzha0/quartz.git "$QP"
fi
if [ ! -d "$QP/node_modules" ]; then
  bun install --cwd "$QP" --ignore-scripts
fi

# Quartz 5 reads quartz.config.yaml; derive ours from the shipped default every
# build (idempotent) so theme/config changes here always take effect.
# Palette + type mirror the BERIL workbench themes (apps/web/src/themes.css):
# "paper" light and "observatory" violet-ink dark; Fraunces / IBM Plex.
uv run --project "$REPO" python - "$QP" <<'PY'
import pathlib, sys, yaml
qp = pathlib.Path(sys.argv[1])
cfg = yaml.safe_load((qp / "quartz.config.default.yaml").read_text())
c = cfg["configuration"]
c["pageTitle"] = "BERIL Knowledge Wiki"
c["baseUrl"] = "localhost:8080"
c["analytics"] = None
for plugin in cfg["plugins"]:
    if plugin["source"] == "@quartz-community/crawl-links":
        plugin.setdefault("options", {})["markdownLinkResolution"] = "relative"
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

# Generation belongs to run_pipeline.sh; this build needs no model calls.
uv run --project "$REPO" python "$HERE/quartz_ingest.py" "$REPO" "$QP/content"
(cd "$QP" && node quartz/bootstrap-cli.mjs build --output "$REPO/build/site")
uv run --project "$REPO" python - "$REPO" "$QP" <<'PY'
import pathlib, shutil, sys
repo, qp = map(pathlib.Path, sys.argv[1:])
site = repo / "build/site"
shutil.copy2(repo / "build/okf-graph.html", site / "okf-graph.html")
assets = repo / "build/okf-assets"
if assets.is_dir():
    shutil.copytree(assets, site / "okf-assets", dirs_exist_ok=True)
previous = qp / "public.previous"
if previous.exists():
    shutil.rmtree(previous)
public = qp / "public"
if public.exists():
    public.rename(previous)
try:
    site.rename(public)
except OSError:
    if previous.exists():
        previous.rename(public)
    raise
PY
echo
echo "built. serve with: node $HERE/serve_quartz.cjs"
