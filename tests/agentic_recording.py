"""Synthetic recorded replies used only by offline end-to-end tests."""

import json

from beril_wiki.agentic.runtime import digest

FACTS = "Yield was 42%. [src: a]\n\nYield was 56%. [src: b]"


def reply(self, messages, step):
    if step.endswith("/science-review"):
        return '{"accepted": true, "issues": []}'
    if step.startswith("curator/decision/"):
        data = json.loads(messages[0]["content"].split("\n")[-1])
        action = next((a for a in data["available"] if a in data["pending"]), "finish")
        return json.dumps({"action": action, "reason": "Refresh required knowledge"})
    if step == "curator/topics":
        data = json.loads(messages[0]["content"].split("\n")[-1])
        return json.dumps(
            {
                "reason": "Group related yield evidence",
                "groups": [
                    {"title": "Yield studies", "concepts": [p["stem"] for p in data["concepts"]]}
                ],
            }
        )
    if step.startswith("extract/"):
        data = json.loads(messages[0]["content"].split("\n")[-1])
        quote = data["text"].split("\n")[0]
        return json.dumps(
            {
                "findings": [
                    {
                        "quote": quote,
                        "start": data["start"],
                        "end": data["start"] + len(quote),
                        "claim": quote,
                        "kind": "finding",
                    }
                ],
                "empty_reason": "",
            }
        )
    if step.startswith("batch/plan"):
        return json.dumps(
            {
                "pages": [
                    {
                        "path": f"concepts/{name}.md",
                        "title": name.title(),
                        "type": "Concept",
                        "sources": ["a", "b"],
                        "reason": "Integrate distinct yield context",
                    }
                    for name in ("yield", "cost", "temperature")
                ],
                "coverage": [
                    {
                        "evidence": f"{sid}:0:0",
                        "concepts": ["concepts/yield.md"],
                        "summary_only": "",
                    }
                    for sid in ("a", "b")
                ],
            }
        )
    if step.startswith("write/"):
        data = json.loads(messages[0]["content"].split("\n")[-1])
        body = "# " + data["job"]["title"] + "\n\n" + FACTS
        if "/summaries/" in step:
            body += "\n\n## Caveats\n\nConditions differ. [src: a, b]"
            body += "\n\n## Slots Into\n\n- [[concepts/yield]] — yield comparisons."
        else:
            body += "\n\n## Tensions\n\n" + FACTS.replace("\n\n", " ")
            body += "\n\n## Open Directions\n\nMeasure conditions."
        return json.dumps(
            {"base_hash": digest(""), "content": body, "description": "Yield measurements"}
        )
    if step.startswith("conflicts/"):
        return (
            "# Yield tension\n\n## Evidence Sides\n\n"
            + FACTS
            + "\n\n## Resolving Work\n\nMeasure conditions."
        )
    if step == "topics/names":
        return '{"0": "Yield studies"}'
    if step.startswith("topics/"):
        return "# Yield studies\n\n" + FACTS + "\n\nSee [[concepts/yield]]."
    if step == "home":
        return (
            "# BERIL Knowledge Wiki\n\n## Topics\n\n- [[topics/yield-studies]]"
            "\n\n## Corpus\n\nReports."
        )
    if step.endswith("/queries"):
        return '{"queries": ["yield measurement"]}'
    if step.startswith("lit/"):
        return (
            "## Literature Context\n\nConditions affect yield. "
            "[PMID 1](https://pubmed.ncbi.nlm.nih.gov/1/)"
        )
    if step.startswith("authors/"):
        return "## Contributions\n\n" + FACTS
    if step.startswith("figures/"):
        return (
            '{"placements": [{"after_paragraph": 1, "figure": 0, '
            '"caption": "invented caption"}], "csv_flags": []}'
        )
    raise AssertionError(f"Unexpected recorded job: {step}")


def forbid_api(*args, **kwargs):
    raise AssertionError("An API generation/embedding call escaped the SDK boundary")


def install():
    import io
    import urllib.request
    from unittest.mock import patch

    import litellm

    from beril_wiki.agentic.runtime import Runtime

    Runtime.ask = reply
    patch.object(litellm, "completion", side_effect=forbid_api).start()
    patch.object(litellm, "embedding", side_effect=forbid_api).start()

    def recorded_url(url, **kwargs):
        if "/esearch.fcgi?" in url:
            return io.BytesIO(b'{"esearchresult": {"idlist": ["1"]}}')
        if "/efetch.fcgi?" in url:
            return io.BytesIO(
                b"<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>1</PMID>"
                b"<Article><ArticleTitle>Yield</ArticleTitle><Abstract><AbstractText>"
                b"Conditions affect yield.</AbstractText></Abstract></Article></MedlineCitation>"
                b"</PubmedArticle></PubmedArticleSet>"
            )
        raise AssertionError(f"Unexpected network call: {url}")

    patch.object(urllib.request, "urlopen", side_effect=recorded_url).start()
