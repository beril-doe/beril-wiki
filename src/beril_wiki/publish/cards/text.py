"""Reader-facing words for the pipeline terms the card records store.

Record files keep the pipeline's own labels (a literature label, a result type, a
follow-up need); pages, cards and the export show these words instead.
"""

from __future__ import annotations

NOT_ASSESSED = "Not assessed"
PUBMED = "https://pubmed.ncbi.nlm.nih.gov/{}/"
# The guarded labels name the agreement that let them stand.
GUARDED = ("Candidate novel", "In tension with retrieved work")
# What kind of result a listed finding is (stages/outcomes.py), in the reader's words.
TYPE_TEXT = {
    "positive": "Positive result",
    "negative": "Negative result",
    "inconclusive": "Inconclusive",
    "data": "About the data",
}
# Types that are not results a reader browses: their pages stay, off the lists.
OFF_TYPES = ("bookkeeping", "untested")
# Before the outcomes stage has read a finding, its extraction tag stands in.
TYPE_FALLBACK = {
    "observation": "positive",
    "inference": "positive",
    "correction": "positive",
    "measured absence": "negative",
    "inconclusive test": "inconclusive",
}
# What following up an open question needs (stages/followups.py), least effort first.
FOLLOW_TEXT = {
    "existing": "Analyze existing data",
    "outside": "Add outside data",
    "experiment": "Run an experiment",
    "unchecked": "Not checked yet",
}
FIRST_STEP_TEXT = "Starts with existing data"
UNCLEAR_TEXT = "Data availability unclear"
# Questions on the directions index frontmatter: the columns, least effort first, then
# the questions no check has placed.
FOLLOW_ORDER = ["existing", "outside", "experiment", "unchecked"]


def follow_notes(tenants: int, date: str) -> dict[str, str]:
    """What each follow-up column means, with the catalog's tenant count and date.

    Parameters
    ----------
    tenants : int
        How many lakehouse tenants the catalog covers.
    date : str
        The catalog snapshot date in reader form.

    Returns
    -------
    dict[str, str]
        Follow-up key to the note the Open questions page shows for its column.
    """
    return {
        "existing": f"An AI model matched the test to tables in the lakehouse catalog of {date}. "
        "No one has run the analysis.",
        "outside": f"Not found in the {tenants} tenants the catalog covers. Public genomes, "
        "metagenomes or another study's measurements can supply it, with no new lab work.",
        "experiment": f"Not found in the {tenants} tenants the catalog covers. Only a new lab or "
        "field measurement can test the hypothesis.",
        "unchecked": "The check that names the data a question needs has not run on it, or did "
        "not finish. This page makes no data claim.",
    }


# The first two are the two kinds of new: a new direction, and new on published ground.
CHIP = {
    "Candidate novel": "New direction",
    "Extends retrieved work": "Adds to published work",
    "In tension with retrieved work": "Differs from published work",
    "Established in retrieved literature": "Similar to published work",
}
LABEL_TEXT = CHIP | {"Insufficient literature evidence": "No clear comparison"}
SOMETHING_NEW = "Something new"
# Home order: results PubMed abstracts hold least like them first.
INTEREST = [CHIP[k] for k in ("Candidate novel", "In tension with retrieved work")] + [
    CHIP["Extends retrieved work"]
]
CHIP_NOTE = (
    "An AI comparison with PubMed abstracts retrieved on {date}. "
    "It does not establish novelty or correctness."
)
# "New direction" alone would read as a verdict, so its note says what the search did and
# did not show.
NOVEL_NOTE = (
    "An AI search of PubMed abstracts, retrieved on {date}, found nothing close to this "
    "result, so it could open a new direction. It does not establish novelty or correctness."
)
NOT_COMPARED = "Not compared yet"
# The Results picture's columns, most novel first; the last shows only when non-empty.
COMPARE_ORDER = [*CHIP.values(), LABEL_TEXT["Insufficient literature evidence"], NOT_COMPARED]
# What each Results picture column means, shown when a reader hovers or taps its heading.
COMPARE_NOTES = {
    CHIP["Candidate novel"]: (
        "An AI search of PubMed abstracts found nothing close to these results, so they "
        "could open a new direction. It does not establish novelty or correctness."
    ),
    CHIP["Extends retrieved work"]: (
        "PubMed abstracts report related work, and these results add to it."
    ),
    CHIP["In tension with retrieved work"]: (
        "PubMed abstracts report something different from these results."
    ),
    CHIP["Established in retrieved literature"]: "PubMed abstracts report a similar result.",
    LABEL_TEXT["Insufficient literature evidence"]: (
        "PubMed abstracts held too little on these results to compare, or the comparison "
        "did not settle."
    ),
    NOT_COMPARED: "These results are waiting for their PubMed search.",
}
RELATION_TEXT = {
    "same result": "Same result in each project",
    "one extends the other": "One project extends the other's analysis",
    "same direction, different definitions": "Different definitions, same direction",
    "similar comparison, different scope": "A similar comparison on different data",
    "one measures what the other cannot": "One measures what the other cannot",
}
# Pipeline phrases that can sit inside free text a stage wrote, such as a readiness
# explanation or a check note, with the words a reader sees instead.
READER_TERMS = {
    "needs compute": "needs a new analysis",
    "lakehouse analysis": "analysis of existing data",
    "Research direction": "Open question",
    "research direction": "open question",
} | {label: text for label, text in LABEL_TEXT.items()}


def reader_terms(text: str) -> str:
    """Free text with pipeline phrases replaced by the reader-facing words."""
    for term, plain_words in READER_TERMS.items():
        text = text.replace(term, plain_words)
    return text


def compare_text(entry: dict | None) -> str:
    """The Results picture's column for a finding: how it compares with PubMed, or that
    it has not been compared (no label yet, a failed first search, or withdrawn)."""
    return LABEL_TEXT.get((entry or {}).get("label", NOT_ASSESSED), NOT_COMPARED)


def chip_note(entry: dict | None, result: str = "") -> str:
    """What a PubMed chip means and when it was checked; empty when there is no chip."""
    if not entry or not chip_of(entry, result):
        return ""
    return label_note(entry)


def label_note(entry: dict) -> str:
    """The note for a pipeline label, dated by its PubMed retrieval."""
    note = NOVEL_NOTE if entry.get("label") == "Candidate novel" else CHIP_NOTE
    return note.format(date=entry.get("retrieved_on", ""))


def chip_of(entry: dict | None, result: str = "") -> str:
    """The comparison chip a card shows; empty unless a pipeline label says something.

    A correction that is only bookkeeping is unlisted, so a listed correction reports a
    result and carries its chip like any other. `result` stays for callers' symmetry."""
    del result
    if not entry or entry.get("override"):
        return ""
    return CHIP.get(entry.get("label", NOT_ASSESSED), "")
