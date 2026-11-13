"""The MCP tools answer from the served artifact and name it."""

from __future__ import annotations

import json

import pytest
from starlette.testclient import TestClient

from beril_wiki import mcp_server as M
from beril_wiki.serve import create_app

PAGES = [
    {
        "i": 0,
        "slug": "concepts/gene-essentiality",
        "title": "Gene essentiality",
        "cls": "concept",
        "label": "Concept",
        "group": "concept",
        "desc": "Which genes a cell cannot lose.",
        "topic": "Fitness",
        "topicSlug": "topics/fitness",
        "topicSlugs": ["topics/fitness"],
        "hue": "",
        "aliases": ["essential genes"],
        "headings": ["Core evidence", "Open Directions"],
        "out": ["summaries/demo__REPORT"],
        "first": "",
    },
    {
        "i": 1,
        "slug": "summaries/demo__REPORT",
        "title": "Demo report",
        "cls": "report",
        "label": "Project report",
        "group": "report",
        "desc": "",
        "topic": "",
        "topicSlug": "",
        "topicSlugs": [],
        "hue": "",
        "aliases": [],
        "headings": [],
        "out": [],
        "first": "",
    },
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
]
CARDS = {
    "findings": [
        {
            "id": "demo--1cfedc83",
            "url": "findings/demo--1cfedc83",
            "title": "FBA and TnSeq agree for most genes",
            "claim": "639 of 866 genes are concordant.",
            "result": "observation",
            "source": "demo",
            "quantities": [{"value": "639", "what": "concordant genes"}],
            "caveat": "Sparse FBA coverage.",
            "topics": ["fitness"],
            "label": "Not assessed",
            "type": "observation",
        }
    ],
    "research_directions": [
        {
            "id": "are-conserved-genes--9f8d23",
            "title": "Are conserved genes needed?",
            "projects": ["demo"],
        }
    ],
}


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
    (corpus / "findings").mkdir()
    (corpus / "sources/demo__REPORT.md").write_text(
        "# Report: demo\n\nOf 866 genes, 639 (73.8%) are concordant.\n"
    )
    (corpus / "findings/demo--1cfedc83.md").write_text("# FBA and TnSeq agree\n\nBody.\n")
    (corpus / "cards.json").write_text(json.dumps(CARDS))
    return root, corpus


def corpus_of(site) -> M.Corpus:
    root, corpus = site
    return M.Corpus("v1", root, corpus)


def test_tokenizer_keeps_identifiers_whole_and_in_parts():
    assert M.tokenize("RB-TnSeq in P. putida KT2440 (596 genes).") == [
        "rb-tnseq",
        "rb",
        "tnseq",
        "putida",
        "kt2440",
        "596",
        "genes",
    ]
    assert M.tokenize("the and of") == []


def test_search_ranks_sections_and_scopes_by_group_or_prefix(site):
    c = corpus_of(site)
    hits = c.index.search("essential genes KT2440", 5, lambda i: True)
    assert hits[0][0] == 1  # the section naming KT2440 and essential genes
    mcp = M.create_mcp(lambda: c)
    result = call(mcp, "search", {"query": "essentiality TnSeq", "k": 3})
    assert result["artifact"] == "v1" and result["build"] == "b123"
    paths = [h["path"] for h in result["hits"]]
    assert "concepts/gene-essentiality" in paths and "summaries/demo__REPORT" in paths
    scoped = call(mcp, "search", {"query": "essentiality TnSeq", "scope": "report"})
    assert [h["path"] for h in scoped["hits"]] == ["summaries/demo__REPORT"]
    prefixed = call(mcp, "search", {"query": "essentiality", "scope": "concepts/"})
    assert {h["path"] for h in prefixed["hits"]} == {"concepts/gene-essentiality"}
    assert prefixed["hits"][0]["anchor"] in ("", "core-evidence", "caveats")


def call(mcp, name, args) -> dict:
    """The tool's structured result, however FastMCP hands it back in-process."""
    import asyncio

    out = asyncio.run(mcp.call_tool(name, args))
    if isinstance(out, dict):
        return out
    if isinstance(out, tuple):
        return out[1]
    return json.loads(out[0].text)


def test_read_page_and_section(site):
    mcp = M.create_mcp(lambda: corpus_of(site))
    page = call(mcp, "read_page", {"path": "concepts/gene-essentiality"})
    assert page["title"] == "Gene essentiality" and len(page["sections"]) == 3
    assert page["links_out"] == ["summaries/demo__REPORT"]
    assert call(mcp, "read_page", {"path": "/concepts/gene-essentiality.html"})["title"]
    section = call(
        mcp, "read_section", {"path": "concepts/gene-essentiality", "heading": "caveats"}
    )
    assert [s["anchor"] for s in section["sections"]] == ["caveats"]
    assert call(mcp, "read_page", {"path": "concepts/none"})["error"] == "no such page"
    with pytest.raises(Exception, match="not a page path"):
        call(mcp, "read_page", {"path": "../etc/passwd"})


def test_findings_directions_and_sources_come_from_the_corpus(site):
    mcp = M.create_mcp(lambda: corpus_of(site))
    listed = call(mcp, "list_findings", {"project": "demo"})
    assert listed["count"] == 1 and listed["findings"][0]["id"] == "demo--1cfedc83"
    assert call(mcp, "list_findings", {"topic": "fitness"})["count"] == 1
    assert call(mcp, "list_findings", {"topic": "soil"})["count"] == 0
    finding = call(mcp, "get_finding", {"id": "demo--1cfedc83"})
    assert finding["record"]["claim"] == "639 of 866 genes are concordant."
    assert finding["markdown"].startswith("# FBA and TnSeq agree")
    assert call(mcp, "get_finding", {"id": "nope"})["error"] == "no such finding"
    direction = call(mcp, "get_direction", {"id": "are-conserved-genes--9f8d23"})
    assert direction["record"]["projects"] == ["demo"] and direction["markdown"] is None
    source = call(mcp, "get_source", {"project": "demo", "offset": 16, "length": 12})
    assert source["text"] == "Of 866 genes" and source["total"] == 58
    assert "beyond" in call(mcp, "get_source", {"project": "demo", "offset": 999})["error"]
    assert call(mcp, "get_source", {"project": "../x"})["error"] == "bad project id"
    assert "not available" in call(mcp, "get_source", {"project": "other"})["error"]


def test_without_a_corpus_the_record_tools_say_so(site):
    root, _ = site
    mcp = M.create_mcp(lambda: M.Corpus("baked", root, None))
    assert call(mcp, "list_findings", {}) == {
        "artifact": "baked",
        "build": "b123",
        "topic": None,
        "project": None,
        "count": 0,
        "findings": [],
        "available": False,
    }
    assert call(mcp, "get_source", {"project": "demo"})["error"].startswith("source not available")


def test_mounted_at_wiki_mcp_over_streamable_http(site):
    root, corpus = site
    app = create_app(root, "/wiki", corpus_dir=corpus)
    headers = {"Accept": "application/json, text/event-stream", "Content-Type": "application/json"}
    with TestClient(app) as c:
        # The slashless form redirects with 308, which keeps the POST and its body.
        r = c.post("/wiki/mcp", headers=headers, json={}, follow_redirects=False)
        assert r.status_code == 308 and r.headers["location"] == "/wiki/mcp/"
        init = c.post(
            "/wiki/mcp/",
            headers=headers,
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-03-26",
                    "capabilities": {},
                    "clientInfo": {"name": "t", "version": "0"},
                },
            },
        )
        assert init.status_code == 200, init.text
        assert init.json()["result"]["serverInfo"]["name"] == "beril-wiki"
        tools = c.post(
            "/wiki/mcp/", headers=headers, json={"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
        )
        names = {t["name"] for t in tools.json()["result"]["tools"]}
        assert names == {
            "search",
            "read_page",
            "read_section",
            "list_findings",
            "get_finding",
            "get_direction",
            "get_source",
        }
        called = c.post(
            "/wiki/mcp/",
            headers=headers,
            json={
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {"name": "search", "arguments": {"query": "KT2440"}},
            },
        )
        result = called.json()["result"]
        assert result["structuredContent"]["artifact"] == "baked"
        assert result["structuredContent"]["hits"][0]["path"] == "concepts/gene-essentiality"
        # The site itself is still served around the mount.
        assert c.get("/wiki/").text == "home"
