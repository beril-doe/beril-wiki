"""The image's own site build has every tree the build script reads."""

from __future__ import annotations

import re
from pathlib import Path

DOCKERFILE = Path(__file__).resolve().parents[1] / "Dockerfile"


def stage(name: str) -> str:
    text = DOCKERFILE.read_text()
    found = re.search(rf"^FROM .* AS {name}\n(.*?)(?=^FROM |\Z)", text, re.M | re.S)
    assert found, name
    return found.group(1)


def test_the_site_stage_copies_the_corpus_the_ingest_serves():
    # publish.ingest copies corpus/manifest.json into the site as corpus-manifest.json;
    # a SITE_FROM=site build without corpus/ baked a site that lacked it.
    copied = re.findall(r"^COPY (\S+) ", stage("site"), re.M)
    for tree in ("src", "theme", "scripts", "contract", "state", "wiki", "corpus"):
        assert tree in copied, tree
