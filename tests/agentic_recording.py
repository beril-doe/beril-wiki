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
    if step.startswith("plan/route/"):
        data = json.loads(messages[0]["content"].split("\n")[-1])
        return json.dumps(
            {
                "routes": [
                    {"evidence": r["id"], "concepts": [], "summary_only": "", "new_topic": "yield"}
                    for r in data["records"]
                ],
                "entities": [],
            }
        )
    if step.startswith("plan/propose/"):
        data = json.loads(messages[0]["content"].split("\n")[-1])
        return json.dumps(
            {
                "concepts": [
                    {
                        "path": "concepts/yield.md",
                        "title": "Yield",
                        "reason": "Integrate distinct yield context",
                        "evidence": [r["id"] for r in data["records"]],
                    }
                ],
                "unplaced": [],
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

    from beril_wiki.agentic import page_agent
    from beril_wiki.agentic.runtime import Runtime

    Runtime.ask = reply
    page_agent.run = page_session
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


def page_session(agent, page, workdir, *, max_reviews=4):
    """A page session replayed from recorded replies, for offline tests.

    The writer's draft is the reply to the page's step; each correction is the reply to
    the step plus /repair, asked with the open issues, as a session would revise after
    a failed check or review. For an integrated page a reply is the candidate JSON the
    recorded writers return (content or anchored edits); for a derived page it is the
    Markdown. Check and review are the stage's own, so gates, review, verification and
    the stage's stop rules run unchanged."""
    from beril_wiki.agentic import page_agent as PA
    from beril_wiki.agentic.batch import reconstruct
    from beril_wiki.agentic.runtime import CandidateError

    def parse(raw):
        if page.meta is None:
            return raw, None
        candidate = json.loads(raw)
        meta = {
            "description": candidate.get("description"),
            "accounted_evidence": candidate.get("accounted_evidence") or {},
        }
        return reconstruct(page.text, candidate), meta

    raw = agent.ask(page.messages, page.step)
    reviewed, issues = False, []
    for attempt in range(max_reviews + 1):
        try:
            text, meta = parse(raw)
            issues = page.check(text, meta)
        except (CandidateError, ValueError) as exc:
            issues = [str(exc)]
        if not issues:
            try:
                issues = page.review(text, meta)
            except CandidateError as exc:
                raise PA.Exhausted(str(exc), exc.objections, True) from exc
            reviewed = True
            if not issues:
                return text, meta
        if attempt == max_reviews:
            break
        raw = agent.ask(
            page.messages + [{"role": "user", "content": "ISSUES " + json.dumps(issues)}],
            page.step + "/repair",
        )
    raise PA.Exhausted(
        f"{page.step}: rounds spent; still open: {'; '.join(issues)}", issues, reviewed
    )
