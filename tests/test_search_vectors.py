"""The search-vector cache: embed only new section texts, keep one vector per
current section, and store vectors compactly without losing their direction."""

import base64
import hashlib
import json
import math

from beril_wiki.stages import search_vectors as sv


def fake_embedder(calls):
    def embed(texts):
        calls.append(list(texts))
        # A distinct vector per text, the same in every run, so stored rows can be told apart.
        seed = [int(hashlib.md5(t.encode()).hexdigest(), 16) % 10007 for t in texts]
        return [[(s + d) / 1000 for d in range(sv.DIM)] for s in seed]

    return embed


def inputs(*names):
    return [{"h": f"h-{n}", "text": f"search_document: {n}"} for n in names]


def test_only_new_hashes_are_embedded():
    calls = []
    store, n = sv.update(inputs("a", "b"), {}, embedder=fake_embedder(calls), pace=0)
    assert n == 2 and set(store) == {"h-a", "h-b"}

    calls.clear()
    store, n = sv.update(inputs("a", "b", "c"), store, embedder=fake_embedder(calls), pace=0)
    assert n == 1
    assert calls == [["search_document: c"]]


def test_vectors_for_removed_sections_are_dropped():
    store, _ = sv.update(inputs("a", "b"), {}, embedder=fake_embedder([]), pace=0)
    store, n = sv.update(inputs("b"), store, embedder=fake_embedder([]), pace=0)
    assert n == 0 and set(store) == {"h-b"}


def test_force_re_embeds_everything():
    calls = []
    store, _ = sv.update(inputs("a"), {}, embedder=fake_embedder(calls), pace=0)
    calls.clear()
    _, n = sv.update(inputs("a"), store, embedder=fake_embedder(calls), force=True, pace=0)
    assert n == 1 and calls == [["search_document: a"]]


def test_batches_never_exceed_the_batch_size():
    calls = []
    sv.update(inputs(*"abcdefghij"), {}, embedder=fake_embedder(calls), pace=0, batch=4)
    assert [len(c) for c in calls] == [4, 4, 2]


def test_wrong_dimension_is_refused():
    def short(texts):
        return [[0.1] * 10 for _ in texts]

    try:
        sv.update(inputs("a"), {}, embedder=short, pace=0)
    except SystemExit as e:
        assert "768" in str(e)
    else:
        raise AssertionError("a 10-dimension vector was accepted")


def test_quantize_keeps_direction():
    v = [math.sin(d) for d in range(sv.DIM)]
    norm = math.sqrt(sum(x * x for x in v))
    v = [x / norm for x in v]
    b64, scale = sv.quantize(v)
    raw = base64.b64decode(b64)
    assert len(raw) == sv.DIM
    back = [(b - 256 if b > 127 else b) * scale for b in raw]
    cos = sum(x * y for x, y in zip(v, back, strict=True)) / math.sqrt(sum(y * y for y in back))
    assert cos > 0.999


def test_store_round_trips_sorted(tmp_path):
    path = tmp_path / "vectors.jsonl"
    store, _ = sv.update(inputs("b", "a"), {}, embedder=fake_embedder([]), pace=0)
    sv.write_store(store, path)
    lines = path.read_text().splitlines()
    assert [json.loads(line)["h"] for line in lines] == ["h-a", "h-b"]
    assert sv.load_store(path) == {
        h: {"v": r["v"], "s": round(r["s"], 9)} for h, r in store.items()
    }


def test_duplicated_rows_are_left_for_the_next_run():
    def collide(texts):
        # CBORG's failure mode: two different texts come back with one vector.
        return [
            [0.5] * sv.DIM if t.endswith(("a", "b")) else [0.1 + i] * sv.DIM
            for i, t in enumerate(texts)
        ]

    store, n = sv.update(inputs("a", "b", "c"), {}, embedder=collide, pace=0)
    assert n == 1 and set(store) == {"h-c"}
    calls = []
    store, n = sv.update(inputs("a", "b", "c"), store, embedder=fake_embedder(calls), pace=0)
    assert n == 2 and calls == [["search_document: a", "search_document: b"]]


def test_default_embedder_pins_the_query_model(monkeypatch):
    seen = []
    monkeypatch.setattr(sv, "embed", lambda texts, model: seen.append(model) or [[0.1] * sv.DIM])
    sv.update(inputs("a"), {}, pace=0)
    assert seen == ["openai/lbl/nomic-embed-text"]
