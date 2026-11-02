#!/usr/bin/env bash
# Gates on a built site (quartz/public) that block publishing it, wherever it
# is published: GitHub Pages (pages.yml) and the SPIN image (image.yml).
#   scripts/check_site.sh [site-dir]
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
SITE="${1:-$REPO/quartz/public}"

# A build that silently dropped the corpus would still deploy green.
pages=$(find "$SITE" -name '*.html' | wc -l)
echo "$pages HTML pages built"
[ "$pages" -ge 400 ] || { echo "::error::only $pages pages built, expected >=400"; exit 1; }
test -f "$SITE/about.html" || { echo "::error::about page missing"; exit 1; }

# The disclaimer is injected into Markdown inputs, so any route Quartz
# generates on its own publishes without it. Exempt: 404 (an error page),
# about.html (which IS the explanation), and Quartz's redirect stubs, which are
# meta-refreshes rather than pages. The corpus names pages `X__REPORT` while
# Quartz's canonical slug is lowercase, so it emits a noindex meta-refresh at
# the original casing; those stubs only exist as separate files on a
# case-sensitive filesystem, which is why this check is only right on Linux.
#
# The marker is DERIVED from the constant the pipeline injects, not typed here.
# Hand-copying it meant every reword silently disarmed the gate: rewording the
# sentence once left the check hunting for a phrase no page contained any more,
# which fails every page rather than passing them, but the reverse is just as
# possible.
uv run --project "$REPO" python - "$SITE" <<'PY'
import pathlib, sys
from beril_wiki.publish.ingest import PROVENANCE
marker = PROVENANCE.split(".")[0].strip()   # first sentence, rendered verbatim
assert len(marker) > 20, marker
missing, checked = [], 0
for f in sorted(pathlib.Path(sys.argv[1]).rglob("*.html")):
    text = f.read_text(errors="replace")
    if 'http-equiv="refresh"' in text or f.name in ("404.html", "about.html"):
        continue
    checked += 1
    if marker not in text:
        missing.append(str(f))
if missing:
    print(f"::error::{len(missing)} page(s) published without the provenance callout")
    print("\n".join(missing[:20]))
    sys.exit(1)
print(f"all {checked} content pages carry: {marker!r}")
PY
