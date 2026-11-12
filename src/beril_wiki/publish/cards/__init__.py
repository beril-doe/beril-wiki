"""Publish-time joins for finding and research-direction records.

The curator stages write each record alone; this step places them. It adds the
literature label from state/novelty.json, the topics a finding belongs to, the
conflicts and research directions related to it, and two texts a reader copies from
each direction: a prompt for BERIL and a handoff brief. It also writes a JSON export
for agents. Everything here is a deterministic join over pages the pipeline wrote,
so placement never costs a model call and never edits pages under wiki/.

Reanalysis proposals, which repeat or correct existing work, are listed per report
under data-issues/ for the reports' maintainers rather than as research.

ingest.py calls record() on each record page before its generic transforms (title,
[src:] links, dead-link repair) run, about_text() on the About page, then
write_extras() once. The modules, in import order: text (reader words for pipeline
terms), corpus (what the joins read), data (the lakehouse tables a question names,
generated data pages and the coverage note), links (links and shared results), picks
(home and topic picks), pages (the record pages) and export (index pages, data pages
and cards.json).
"""

from beril_wiki.publish.cards.corpus import DIRS, ISSUES, Corpus
from beril_wiki.publish.cards.data import about_text, generated_routes
from beril_wiki.publish.cards.export import write_extras
from beril_wiki.publish.cards.pages import record

__all__ = [
    "DIRS",
    "ISSUES",
    "Corpus",
    "about_text",
    "generated_routes",
    "record",
    "write_extras",
]
