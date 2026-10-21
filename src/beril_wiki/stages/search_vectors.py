#!/usr/bin/env python3
"""Section vectors for the site's meaning search, cached by content hash.

The publish step (``scripts/build_quartz.sh``) splits every rendered page into
sections and writes the exact text each one is embedded with, keyed by its
hash, to ``quartz/search-embed-input.json``. This stage embeds the sections
whose hash has no stored vector, with CBORG's LBL-hosted nomic-embed-text
($0 per token), and keeps one int8 vector per current hash in
``search/section-vectors.jsonl``. The next publish copies them into the site.

The store is committed because the site is built in CI, which has no CBORG
key: readers' browsers embed only their queries, with their own keys.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \\
        uv run python -m beril_wiki.stages.search_vectors [--force]
"""

from __future__ import annotations

import argparse
import base64
import json
import pathlib
import time
from collections.abc import Callable

from beril_wiki.paths import ROOT
from beril_wiki.stages.consolidate import EMBED_BATCH, embed

INPUT = ROOT / "quartz" / "search-embed-input.json"
# Outside state/: the curator fingerprints and promotes state/ wholesale, so a store
# refreshed by a keyed publish would break its no-op check and its promotion.
STORE = ROOT / "search" / "section-vectors.jsonl"
# The key allows 20 requests a minute; one batch is one request, so this stays near 15.
PACE_SECONDS = 4.0
DIM = 768
# The browser embeds queries with this model (theme/src/search/config.ts), so documents
# must use it too, whatever EMBED_MODEL the consolidate stage is pointed at.
MODEL = "openai/lbl/nomic-embed-text"

Embedder = Callable[[list[str]], list[list[float]]]


def nomic(texts: list[str]) -> list[list[float]]:
    return embed(texts, model=MODEL)


def duplicated(texts: list[str], vectors: list[list[float]]) -> set[int]:
    """Rows whose vector another row with different text also got.

    consolidate.embed repairs most of CBORG's duplicated rows but lets a few
    through. Stored here they would never be re-embedded, so they are skipped
    and the next run tries them again.
    """
    first: dict[tuple[float, ...], int] = {}
    bad: set[int] = set()
    for i, v in enumerate(vectors):
        j = first.setdefault(tuple(v), i)
        if j != i and texts[j] != texts[i]:
            bad |= {i, j}
    return bad


def quantize(vector: list[float]) -> tuple[str, float]:
    """Store a unit vector as int8 plus one scale: value = int8 * scale.

    At 768 dimensions this loses nothing measurable: on a 258-query test set
    (October 2026), keyword + meaning search put the source section in the top
    five for 82.6% of queries from int8 vectors and 82.2% from float32.
    """
    peak = max(abs(x) for x in vector) or 1.0
    q = bytes((round(x / peak * 127) & 0xFF) for x in vector)
    return base64.b64encode(q).decode(), peak / 127


def load_store(path: pathlib.Path = STORE) -> dict[str, dict]:
    if not path.exists():
        return {}
    rows = (json.loads(line) for line in path.read_text().splitlines() if line.strip())
    return {r["h"]: {"v": r["v"], "s": r["s"]} for r in rows}


def write_store(rows: dict[str, dict], path: pathlib.Path = STORE) -> None:
    # Sorted by hash, one line per vector, so a recompile changes only the lines it touched.
    lines = [
        json.dumps({"h": h, "v": r["v"], "s": round(r["s"], 9)}) for h, r in sorted(rows.items())
    ]
    tmp = path.with_suffix(".tmp")
    tmp.write_text("\n".join(lines) + ("\n" if lines else ""))
    tmp.replace(path)


def update(
    inputs: list[dict],
    store: dict[str, dict],
    embedder: Embedder = nomic,
    force: bool = False,
    pace: float = PACE_SECONDS,
    batch: int = EMBED_BATCH,
    save: Callable[[dict[str, dict]], None] | None = None,
) -> tuple[dict[str, dict], int]:
    """Embed the inputs whose hash is not stored; drop vectors no section uses.

    Returns the new store and the number of sections embedded, not counting
    duplicated rows left for the next run. ``save`` is called
    after every 50 batches so an interrupted run keeps its progress.
    """
    current = {r["h"]: r["text"] for r in inputs}
    kept = {} if force else {h: v for h, v in store.items() if h in current}
    todo = [h for h in current if h not in kept]
    embedded = 0
    for start in range(0, len(todo), batch):
        hashes = todo[start : start + batch]
        texts = [current[h] for h in hashes]
        vectors = embedder(texts)
        if any(len(v) != DIM for v in vectors):
            raise SystemExit(
                f"[ERROR] expected {DIM}-dimension vectors, got {sorted({len(v) for v in vectors})}"
            )
        bad = duplicated(texts, vectors)
        if bad:
            print(f"  [WARN] search_vectors: {len(bad)} duplicated vector(s) left for the next run")
        for i, (h, v) in enumerate(zip(hashes, vectors, strict=True)):
            if i not in bad:
                b64, scale = quantize(v)
                kept[h] = {"v": b64, "s": scale}
                embedded += 1
        done = start + len(hashes)
        if save and (start // batch) % 50 == 49:
            save(kept)
            print(f"  search_vectors: {done}/{len(todo)} embedded")
        if pace and done < len(todo):
            time.sleep(pace)
    return kept, embedded


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--force", action="store_true", help="re-embed every section")
    args = ap.parse_args()
    if not INPUT.exists():
        raise SystemExit(f"[ERROR] {INPUT} not found: run scripts/build_quartz.sh first")
    inputs = json.loads(INPUT.read_text())
    store, n = update(inputs, load_store(), force=args.force, save=write_store)
    write_store(store)
    print(f"search_vectors: {len(inputs)} sections, {n} embedded, {len(store)} stored")


if __name__ == "__main__":
    main()
