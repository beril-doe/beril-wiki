"""Wording rules for the text a reader meets on result and question pages.

The card stages reject a model reply that breaks one of these rules, publish and
scripts/check_reader.py check accepted text against the same rules, and a change here
reschedules every card stage (curator.stage_revision hashes this file).
"""

from __future__ import annotations

import re

# Test statistics and named tests.
STATS = re.compile(
    r"\bp\s*[=<>≤]|\b[rq]\s*=|ρ|\brho\b|\bAUC\b|χ²|\bFDR\b|×\s*10"
    r"|\b(Cohen|Mann-Whitney|Kruskal|Spearman|Pearson|Mantel)\b",
    re.I,
)
# Statistical and power wording a reader should not meet in a link label or shared text.
STAT_WORDS = re.compile(
    r"\b(?:(?:non-?)?significan\w*|(?:under|low|statistical )power\w*|effect sizes?"
    r"|statistic\w*|p-?values?)\b",
    re.I,
)
MULTIPLE_TESTING = re.compile(r"\bmultiple[- ]testing\b", re.I)


def statistical(text: str) -> bool:
    """A statistic or statistical wording, such as 'significant' or 'multiple-testing'."""
    return any(p.search(text) for p in (STATS, STAT_WORDS, MULTIPLE_TESTING))


# Names a reader outside the project cannot decode: an annotation system or database, a
# statistical procedure or a notebook code. Lineage names such as Pseudomonas_E are left
# to the prompt: the reviewer requires the name the finding gives, so code rejecting it
# made those gists unresolvable. Hypothesis codes (H2) too: hydrogen is also H2.
JARGON = re.compile(
    r"\b(?:SEED|COGs?|KEGG|GapMind|ICA|PERMANOVA|Procrustes|Mantel|D'Agostino|"
    r"Black Queen|preregistered|pre-registered|Tier[- ]?[A-C]|NB\d+)\b"
)
# Claims a plain summary must not make: novelty, firsts and caveats, which the page
# shows separately.
GIST_BANNED = re.compile(
    r"\b(novel|first|breakthrough|confirms|caveats?|limitations?|however)\b", re.I
)
_CONFIRMS = r"confirm\w*|corroborat\w*|validat\w*|reproduc\w*|replicat\w*|independen\w*|agree\w*"
_EACH_OTHER = r"support(?:s|ed)? each other"
# Wording that would read as one project confirming another.
CONFIRMING = re.compile(rf"\b(?:{_CONFIRMS})\b|{_EACH_OTHER}", re.I)
# What a link label or shared result must not say: the confirming wording plus the
# claims GIST_BANNED names.
LINK_BANNED = re.compile(
    rf"\b(?:{_CONFIRMS}"
    r"|novel|first|breakthrough|caveats?|limitations?|however)\b"
    rf"|{_EACH_OTHER}",
    re.I,
)
# Plumbing a reader cannot use on a link: files, tables and their snake_case names.
PLUMBING = re.compile(
    r"\b(?:files?|tables?|columns?|parquet|tsv|csv|schema|notebooks?)\b|\b[a-z0-9]+(?:_[a-z0-9]+)+\b",
    re.I,
)
# Identifiers a reader cannot decode: snake_case table or collection names, NMDC study
# ids and tree node names.
IDENTIFIER = re.compile(r"\b[a-z0-9]+(?:_[a-z0-9]+)+\b|\bnmdc:[\w-]+|\bNode_\d+\b")
REPORT_TALK = re.compile(
    r"\bthe (?:reports?|supplied evidence|evidence supplied|source reports?)\b", re.I
)
# Work that repeats, corrects or tidies an existing analysis. It belongs to the people
# who maintain the reports, not on the pages a scientist reads to choose a project.
REANALYSIS = re.compile(
    r"\b(?:re-?(?:comput|run|analy[sz]|count|deriv|estimat|scor|test|fit|build|process"
    r"|annotat|classif|examin|evaluat|quantif|check|tabulat)\w*|recount\w*|reconcil\w*"
    r"|audit\w*|harmoni[sz]\w*|standardi[sz]\w*|repeat\w*|trace\s+the|correct\s+the"
    r"|align\s+(?:the\s+)?(?:denominator|threshold|definition|count)s?)\b",
    re.I,
)


def is_reanalysis(text: str) -> bool:
    """Whether a proposal's opening clause asks to redo or tidy existing work."""
    lead = " ".join(re.sub(r"\*\*", "", text).split()[:14])
    return REANALYSIS.search(lead) is not None


def asks_to_redo(text: str) -> bool:
    """Whether a research question opens by asking to redo or tidy existing work.

    Only the first words count: a question may name redone work as its context ("Do
    genes that stay dark after reannotation ...") without asking to redo it."""
    lead = " ".join(re.sub(r"\*\*", "", text).split()[:4])
    return REANALYSIS.search(lead) is not None


def words(text: str) -> int:
    """The word count the length limits on card text use."""
    return len(text.split())
