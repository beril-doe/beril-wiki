"""Reader-facing words for the pipeline terms the card records store.

Record files keep the pipeline's own labels (a literature label, a result kind, a
readiness); pages, cards and the export show these words instead.
"""

from __future__ import annotations

NOT_ASSESSED = "Not assessed"
PUBMED = "https://pubmed.ncbi.nlm.nih.gov/{}/"
# The guarded labels name the agreement that let them stand.
GUARDED = ("Candidate novel", "In tension with retrieved work")
# Reader-facing words for pipeline terms; record files keep the pipeline's own.
KIND_TEXT = {
    "observation": "Result",
    "inference": "Interpretation",
    "null result": "Null or missing result",
    "correction": "Correction",
}
CHIP = {
    "Candidate novel": "No close match in PubMed abstracts",
    "Extends retrieved work": "Builds on PubMed work",
    "In tension with retrieved work": "Differs from PubMed abstracts",
    "Established in retrieved literature": "Similar result in PubMed",
}
LABEL_TEXT = CHIP | {"Insufficient literature evidence": "Too little published evidence to compare"}
# Home order: results PubMed abstracts hold least like them first.
INTEREST = [CHIP[k] for k in ("Candidate novel", "In tension with retrieved work")] + [
    CHIP["Extends retrieved work"]
]
CHIP_NOTE = (
    "An AI comparison with PubMed abstracts retrieved on {date}. "
    "It does not establish novelty or correctness."
)
NEED = {
    "data in the lakehouse": ("data", "Data already in the lakehouse"),
    "needs compute": ("build", "Analysis to build"),
    "needs new measurements": ("measure", "New measurements"),
    "unknown": ("unclear", "Not yet clear"),
}
APPROACH_TEXT = {
    "lakehouse analysis": "Analysis of existing data",
    "experiment": "Experiment",
    "analysis then experiment": "Analysis, then experiment",
}
NOT_COMPARED = "Not compared yet"
# The Results picture's columns, most novel first; the last shows only when non-empty.
COMPARE_ORDER = [*CHIP.values(), LABEL_TEXT["Insufficient literature evidence"], NOT_COMPARED]
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
    return CHIP_NOTE.format(date=entry.get("retrieved_on", ""))


def chip_of(entry: dict | None, result: str = "") -> str:
    """The comparison chip a card shows; empty unless a pipeline label says something.

    A correction revises the project's own earlier analysis, so how PubMed relates to it
    says nothing a reader can use, and a chip there reads as a verdict on the error."""
    if not entry or entry.get("override") or result == "correction":
        return ""
    return CHIP.get(entry.get("label", NOT_ASSESSED), "")
