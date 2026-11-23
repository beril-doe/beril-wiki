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


def test_the_build_context_admits_every_source_the_site_stage_copies():
    """.dockerignore starts with `*`; every COPY source of the site stage must be
    re-included or the in-image build (SITE_FROM=site) fails before rendering."""
    ignore = (DOCKERFILE.parent / ".dockerignore").read_text().splitlines()
    admitted = {line[1:].rstrip("/") for line in ignore if line.startswith("!")}
    for src in re.findall(r"^COPY (?!--from)(\S+) ", stage("site"), re.M):
        name = src.rstrip("/").replace("searc[h]", "search")
        top = name.split("/")[0]
        assert any(a == name or a.split("/")[0] == top for a in admitted), (
            f"{src} is copied by the site stage but not admitted by .dockerignore"
        )
