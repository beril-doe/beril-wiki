"""Synthetic recorded replies used only by offline end-to-end tests."""

import json

from beril_wiki.agentic.runtime import digest
from beril_wiki.check import all_paragraphs

FACTS = "Yield was 42%. [src: a]\n\nYield was 56%. [src: b]"
PAD = "Growth conditions were compared across the two projects without new figures. "


def pad(text: str, words: int) -> str:
    """Bring a recorded page to the word range its stage contract requires."""
    while len(text.split()) < words:
        text += "\n\n" + PAD * 12
    return text


def reply(self, messages, step, *, model=None):
    if step.endswith(("/science-review", "/review")):
        return '{"accepted": true, "issues": []}'
    if "/patch/" in step:
        raise AssertionError(f"recorded pages must pass their gates: {step}")
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
            {
                "base_hash": digest(""),
                "content": body,
                "description": "Yield measurements",
                "accounted_evidence": {
                    c["evidence"]: next(
                        i
                        for i, par in enumerate(all_paragraphs(body))
                        if f"[src: {c['evidence'].split(':')[0]}]" in par
                    )
                    for c in data["coverage"]
                },
            }
        )
    if step.startswith("conflicts/"):
        sides = FACTS.split("\n\n")
        return pad(
            "# Yield tension\n\nTwo projects disagree on yield; see [[concepts/yield]].\n\n"
            f"## Evidence Sides\n\n**Project a.** {sides[0]}\n\n**Project b.** {sides[1]}\n\n"
            "## Possible Reconciliations\n\nHypothesis: conditions differed.\n\n"
            "## Resolving Work\n\n- Repeat both measurements under one protocol.",
            300,
        )
    if step == "topics/names":
        return '{"0": "Yield studies"}'
    if step.startswith("topics/"):
        return pad(
            "# Yield studies\n\nWhat the corpus says about yield.\n\n## What the Corpus Shows\n\n"
            "**Yield.** " + FACTS + " See [[concepts/yield]].\n\n## Tensions and Caveats\n\n"
            "The projects disagree. [src: a, b]\n\n## Where to Go Deeper\n\n"
            "- [[concepts/yield]] — the comparison.",
            900,
        )
    if step == "home":
        return (
            "# BERIL Knowledge Wiki\n\nAn AI-conducted corpus.\n\nTopics are the entry points.\n\n"
            "## Topics\n\n- [[topics/yield-studies|Yield studies]] (1 concepts): yield.\n\n"
            "## Corpus\n\nReports.\n\n## Browse\n\n- [[catalog|Full page catalog]]"
        )
    if step.endswith("/queries"):
        return '{"queries": ["yield measurement"]}'
    if step.startswith("lit/"):
        return pad(
            "## Literature Context\n\nConditions affect yield. "
            "[PMID 1](https://pubmed.ncbi.nlm.nih.gov/1/)",
            300,
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
