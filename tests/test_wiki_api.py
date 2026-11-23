"""The internal API answers from the served artifact, names it, and never lists authors."""

from __future__ import annotations

import json

import pytest
from starlette.testclient import TestClient

from beril_wiki import wiki_api as W
from beril_wiki.serve import create_app


def page(i, slug, title, group, out=(), desc=""):
    return {
        "i": i,
        "slug": slug,
        "title": title,
        "cls": group,
        "label": group.title(),
        "group": group,
        "desc": desc,
        "topic": "",
        "topicSlug": "",
        "topicSlugs": ["topics/fitness"] if group == "concept" else [],
        "hue": "",
        "aliases": ["essential genes"] if group == "concept" else [],
        "headings": [],
        "out": list(out),
        "first": "",
    }


PAGES = [
    page(
        0, "concepts/gene-essentiality", "Gene essentiality", "concept", ["summaries/demo__REPORT"]
    ),
    page(1, "summaries/demo__REPORT", "Demo report", "report"),
    page(2, "authors/ada-lovelace", "Ada Lovelace", "other"),
    page(3, "sources/demo", "demo source", "source"),
]
SECTIONS = [
    {
        "i": 0,
        "s": "concepts/gene-essentiality",
        "p": "",
        "a": "",
        "t": "Essential genes are those a cell cannot lose under the tested condition.",
    },
    {
        "i": 1,
        "s": "concepts/gene-essentiality",
        "p": "Core evidence",
        "a": "core-evidence",
        "t": "RB-TnSeq in Pseudomonas putida KT2440 found 596 essential genes.",
    },
    {
        "i": 2,
        "s": "concepts/gene-essentiality",
        "p": "Core evidence › Caveats",
        "a": "caveats",
        "t": "Essentiality calls depend on insertion density and growth medium.",
    },
    {
        "i": 3,
        "s": "summaries/demo__REPORT",
        "p": "Key Findings",
        "a": "key-findings",
        "t": "The demo report compared FBA and TnSeq essentiality for 866 genes.",
    },
    {
        "i": 4,
        "s": "authors/ada-lovelace",
        "p": "",
        "a": "",
        "t": "Ada Lovelace wrote about essential genes and KT2440 at length here.",
    },
]


@pytest.fixture
def site(tmp_path):
    root = tmp_path / "public"
    (root / "static/search").mkdir(parents=True)
    (root / "index.html").write_text("home")
    (root / "static/search/pages.json").write_text(json.dumps({"build": "b123", "pages": PAGES}))
    (root / "static/search/sections.json").write_text(
        json.dumps({"build": "b123", "sections": SECTIONS})
    )
    corpus = tmp_path / "corpus"
    (corpus / "sources").mkdir(parents=True)
    (corpus / "sources/demo__REPORT.md").write_text(
        "# Report: demo\n\nOf 866 genes, 639 (73.8%) are concordant.\n"
    )
    return root, corpus


def corpus_of(site) -> W.Corpus:
    root, corpus = site
    return W.Corpus("v1", root, corpus)


def test_tokenizer_keeps_identifiers_whole_and_in_parts():
    assert W.tokenize("RB-TnSeq in P. putida KT2440 (596 genes).") == [
        "rb-tnseq",
        "rb",
        "tnseq",
        "putida",
        "kt2440",
        "596",
        "genes",
    ]
    assert W.tokenize("the and of") == []


def test_search_ranks_scopes_and_excludes_authors(site):
    c = corpus_of(site)
    result = W.search(c, "essential genes KT2440", None, 10)
    assert result["artifact"] == "v1" and result["build"] == "b123"
    addresses = [r["address"] for r in result["results"]]
    assert addresses[0] == "wiki/concepts/gene-essentiality#core-evidence"
    assert not any(a.startswith("wiki/authors/") for a in addresses)
    assert {"address", "title", "heading", "text", "score"} <= set(result["results"][0])
    scoped = W.search(c, "essentiality TnSeq", "report", 5)
    assert [r["address"] for r in scoped["results"]] == ["wiki/summaries/demo__REPORT#key-findings"]
    prefixed = W.search(c, "essentiality", "concepts/", 5)
    assert all(r["address"].startswith("wiki/concepts/") for r in prefixed["results"])


def test_read_page_section_and_source(site):
    c = corpus_of(site)
    whole = W.read(c, "wiki/concepts/gene-essentiality")
    assert whole is not None
    assert whole["title"] == "Gene essentiality" and whole["sources"] == ["demo"]
    assert "## Core evidence" in whole["content"] and len(whole["sections"]) == 3
    section = W.read(c, "wiki/concepts/gene-essentiality#caveats")
    assert section is not None
    assert [s["anchor"] for s in section["sections"]] == ["caveats"]
    assert section["address"] == "wiki/concepts/gene-essentiality#caveats"
    # The site publishes sources/<id> (ingest drops the __REPORT staging suffix); the
    # corpus keeps the suffix, and the read must still find the exact Markdown.
    for address in ("wiki/sources/demo", "wiki/sources/demo__REPORT"):
        source = W.read(c, address)
        assert source is not None, address
        assert source["exact"] and source["content"].startswith("# Report: demo")
        assert source["sources"] == ["demo"]
    assert W.read(c, "wiki/concepts/none") is None
    for bad in ("wiki/authors/ada-lovelace", "concepts/x", "wiki/../etc", "wiki/nope/x"):
        with pytest.raises(ValueError):
            W.read(c, bad)


def test_ls_lists_collections_then_pages_without_authors(site):
    c = corpus_of(site)
    top = W.ls(c, "")
    assert [e["title"] for e in top["entries"]] == list(W.COLLECTIONS)
    assert "authors" not in [e["title"] for e in top["entries"]]
    concepts = W.ls(c, "wiki/concepts")
    assert concepts["entries"] == [
        {"address": "wiki/concepts/gene-essentiality", "title": "Gene essentiality"}
    ]
    with pytest.raises(ValueError):
        W.ls(c, "authors")


def test_source_slices_exact_characters(site):
    c = corpus_of(site)
    piece = W.source(c, "demo", 16, 12)
    assert piece["text"] == "Of 866 genes" and piece["total"] == 58 and piece["end"] == 28
    assert "beyond" in W.source(c, "demo", 999, 10)["error"]
    assert W.source(c, "other", 0, 10)["error"] == "source not available"
    with pytest.raises(ValueError):
        W.source(c, "../x", 0, 10)


def test_source_finds_a_report_under_either_name_and_keeps_its_bytes(site):
    root, corpus = site
    # discoveries and pitfalls are stored under the published name, as read hands
    # them out as citations; a CRLF report is served with its CRs, so offsets
    # agree with the hashed bytes.
    (corpus / "sources/discoveries.md").write_bytes(b"# Discoveries\r\n\r\nOne \xc3\xa9 two.\r\n")
    c = corpus_of(site)
    whole = W.read(c, "wiki/sources/discoveries")
    assert whole is not None and whole["exact"]
    assert whole["content"] == "# Discoveries\r\n\r\nOne \u00e9 two.\r\n"
    piece = W.source(c, "discoveries", 17, 9)
    assert piece["text"] == "One \u00e9 two" and piece["total"] == len(whole["content"])
    assert whole["content"][piece["offset"] : piece["end"]] == piece["text"]
    assert W.source(c, "demo", 0, 8)["text"] == "# Report"  # the __REPORT copy still wins
    app = create_app(root, "/wiki", corpus_dir=corpus, internal_token="internal")
    with TestClient(app) as client:
        r = client.get(
            "/wiki/_api/source",
            params={"project": "discoveries", "offset": 17, "length": 9},
            headers={"Authorization": "Bearer internal"},
        )
        assert r.status_code == 200 and r.json()["text"] == "One \u00e9 two"


def test_routes_are_token_guarded_and_name_the_artifact(site):
    root, corpus = site
    app = create_app(root, "/wiki", corpus_dir=corpus, internal_token="internal")
    auth = {"Authorization": "Bearer internal"}
    with TestClient(app) as c:
        assert c.get("/wiki/_api/search", params={"q": "KT2440"}).status_code == 401
        bad = c.get(
            "/wiki/_api/search", params={"q": "KT2440"}, headers={"Authorization": "Bearer x"}
        )
        assert bad.status_code == 401
        r = c.get("/wiki/_api/search", params={"q": "KT2440", "k": 2}, headers=auth)
        assert r.status_code == 200
        body = r.json()
        assert body["artifact"] == "baked"
        assert body["results"][0]["address"] == "wiki/concepts/gene-essentiality#core-evidence"
        r = c.get(
            "/wiki/_api/read", params={"address": "wiki/concepts/gene-essentiality"}, headers=auth
        )
        assert r.json()["sources"] == ["demo"] and r.json()["artifact"] == "baked"
        r = c.get("/wiki/_api/read", params={"address": "wiki/authors/ada-lovelace"}, headers=auth)
        assert r.status_code == 400
        r = c.get("/wiki/_api/read", params={"address": "wiki/concepts/none"}, headers=auth)
        assert r.status_code == 404
        r = c.get("/wiki/_api/ls", params={"path": "wiki/summaries"}, headers=auth)
        assert r.json()["entries"][0]["address"] == "wiki/summaries/demo__REPORT"
        r = c.get(
            "/wiki/_api/source",
            params={"project": "demo", "offset": 16, "length": 12},
            headers=auth,
        )
        assert r.json()["text"] == "Of 866 genes"
        assert (
            c.get("/wiki/_api/source", params={"project": "nope"}, headers=auth).status_code == 404
        )
        # The site itself is still served around the API.
        assert c.get("/wiki/").text == "home"
        assert c.get("/wiki/_api/nope", headers=auth).status_code == 404
    with TestClient(create_app(root, "/wiki", corpus_dir=corpus)) as c:
        assert c.get("/wiki/_api/ls", headers=auth).status_code == 503
