# Wiki format and reading guide

The wiki synthesizes BERIL Research Observatory reports into linked scientific
pages. The [curator operating guide](agentic-workflow.md) describes how those
pages are generated; the [HTML walkthrough](agentic-workflow.html) shows how
the schedule runs and what validates each page.

## Collections

| Path | Purpose and required content |
| --- | --- |
| `wiki/index.md` and `wiki/topics/` | Home and narrative topic hubs. A model proposal chooses titles and assigns every concept to exactly one group; each hub is written from its member pages, reviewed and patched by paragraph. Literature Context adds external context with verified PubMed citations. |
| `wiki/concepts/` | Cross-project synthesis with cited evidence, supports/contradicts/refines relations, Tensions, and Open Directions. |
| `wiki/conflicts/` | One page per disagreement: every Tensions paragraph that cites two or more projects, with cited Evidence Sides, Possible Reconciliations and Resolving Work. Paragraphs restating the same figures share a page. Slugs are `conflict--<concept>--<digest of the paragraph>`, so an unchanged disagreement keeps its page and a changed one is retired. |
| `wiki/entities/` | Named organisms, genes, methods, datasets and other entities, with canonical names and aliases. Publishing hides pages with only one source. |
| `wiki/summaries/` | Faithful report summaries with exact quantities, caveats, negative results and Slots Into links. |
| `wiki/sources/` | Copied source reports, preserving the original report bytes. |
| `wiki/authors/` | Attribution and project lists from observatory metadata, plus model-written, reviewed Contributions sections. |
| `wiki/data/` | Data-collection metadata joined to the projects that mention each collection. |
| `wiki/opportunities.md` and `wiki/negative-results.md` | Deterministic digests of Open Directions and report caveats or null results. |
| `wiki/findings/` | At most 6 headline findings per report in `contract/cards.yaml`, each with Key figures, the verbatim Evidence quote, its Caveat and the report's other caveats. The literature label lives in `state/novelty.json` and joins the page at publish. |
| `wiki/directions/` | Research directions for each topic in `contract/cards.yaml`, written from the topic's findings, literature labels and conflicts: the question, Hypothesis, Why it matters, How to test it, What would support or refute it, Data, Builds on and Closest published work. Proposals that would repeat or correct existing work are not directions; they are listed per report for maintainers at publish. |

Topic membership is saved in `state/curator-topics.json`. The host rejects
unknown or duplicated concepts, missing memberships, unsafe titles and stale
concept fingerprints. The number of hubs follows the accepted grouping.

## Citations and provenance

`[src: project_id]` identifies evidence supporting a paragraph. IDs resolve to
source report stems, with `discoveries` and `pitfalls` identifying the
cross-project digests. `[[wikilinks]]` connect concepts, entities, summaries
and other pages. Literature Context sections cite external papers with
`[PMID nnnn](PubMed URL)` links checked against retrieved PubMed results.

Compiled scientific pages carry `type`, `description` and `sources`
frontmatter. A `sources` entry must correspond to a citation in the body;
metadata alone does not establish that a report's evidence was integrated.
The curator uses content hashes, accepted coverage and cached job results for
resume decisions. Metadata pages and raw reports have their own formats.

Deterministic checks verify citation IDs, selected quantities, links and
retention of unchanged evidence. Every generated page needs an H1, which
publishing turns into its title; `beril_wiki.check` fails on a page without
one. For finding and research-direction records the check also requires that a
finding's Evidence quote appear verbatim in its report and its key figures in
that report. A literature label must be one of the six, carry a retrieval date
unless it is "Not assessed", and name only PMIDs it retrieved. A research
direction must build on findings or conflicts that exist, name collections
that are pages under `wiki/data/`, cite only papers a finding's literature
check retrieved, and not have a title that asks to redo existing work.
Separate model review assesses scientific
support and lost meaning. Neither establishes that the underlying research is
correct; a number appearing in a cited report does not establish its units,
denominator or interpretation.

## Rendering the accepted corpus

[`publish/ingest.py`](../src/beril_wiki/publish/ingest.py) derives Quartz content
from the accepted wiki without editing it:

- Source tags become links to summary pages, which link to raw reports and
  gain a computed Feeds into list of concepts that cite the project.
- Single-source entities are omitted from the site. Links to omitted pages
  become plain text; those entities remain in the source corpus.
- Saved figure placements use committed files under `wiki/figures/`.
- Pages receive provenance callouts and evidence counts. These counts do not
  represent human review or confidence ratings.
- A `> **Erratum.**` callout under a paragraph means the cited report states
  that figure wrongly. The reports are archived unedited, so the correction is
  recorded in `contract/errata.yaml` and placed beside every claim that repeats
  the figure; the paragraph above it copies the report faithfully.
- Two reader pages are written at publish time and never into `wiki/`:
  `guide.md` ("How to read this wiki", a table of page kinds with their page
  counts) and `ask.md`, which the theme's browser script fills with the Ask
  interface. A record page shows its one-line brief, when the page has one,
  and a line naming its kind that links to the guide.
- Finding and research-direction records publish with every build.
  [`publish/cards.py`](../src/beril_wiki/publish/cards.py) joins each finding's
  literature label, topics, related conflicts and the research directions that
  build on it, and gives each direction a BERIL prompt and a handoff brief. It
  also writes `findings/index.md`, `directions/index.md`, a `cards.json`
  export, and one `data-issues/<report>.md` page per report listing the
  in-scope proposals that would repeat, correct or reconcile its work; each
  report summary links to its list.
- `publish/cards.py` also places and joins results across
  projects:
  - Each result sits under the main topic whose concepts cite its project
    most; ties go alphabetically.
  - A finding page's frontmatter gains `compare_text`, its PubMed comparison in
    reader words or "Not compared yet".
  - A question that builds on results from two or more projects gains `cross`
    (each project, its topic and its results) and `cross_topics`. The home
    takes three such questions, most projects first, with no project in two.
  - `findings/index.md` carries the Results picture's data in its frontmatter:
    the comparison columns, the links, the shared results (most topics first), project
    titles and the topics with no results. Links come in three families: `r`,
    related results from `state/links.json`; `p`, one project's report uses or
    cites another's, also from `state/links.json`; and `q`, results the same
    open question builds on, computed from the direction records so the ringed
    questions and the lines always agree. A link or shared result with a
    missing end is dropped. `cards.json` gains the same `links` and `shared`.
  - The home shows the three most interesting results, each from its own
    project and topic, drawn only from projects that feed two or more topics.
    Results rank by their PubMed comparison (no close match, then differs, then
    builds on, then the rest), then by how many other projects they link to,
    then a result before a null or correction, then by the project's topic
    count.
  - The Results page shows every shared result from `state/shared.json` under
    the picture, those spanning the most topics, then the most projects, first.
  - Free text a stage wrote, such as a readiness explanation or a question's
    body, passes through one map of reader terms, so "needs compute" reads
    "needs a new analysis" and a label name reads as its chip text.
  - A finding page's frontmatter gains `listed`. A finding is listed (on the
    Results page, in counts, the picture and the home and topic picks) only
    with an accepted plain summary that does not repeat an earlier finding of
    its report, and a null result only when it measured something; missing
    data and an analysis that never ran are not results. An unlisted finding
    keeps its page, so links to it still resolve.
  - A correction carries no PubMed chip: it revises the project's own work.
    A label whose searches found no abstracts says so instead of the
    comparison note. A result page's report-wide caveats fold under "Other
    caveats in this report, not specific to this result".
  - A project link whose only relation is "lists it as a reference only" is
    not shown.

Run [`scripts/build_quartz.sh`](../scripts/build_quartz.sh) after local
acceptance to render the site. Publishing committed content is separate from
curation; the curator does not build or deploy the site. See the
[README publishing instructions](../README.md#publishing).

## Reading and editing

Start at home, open a topic hub, then follow concepts to summaries and raw
reports. Literature Context connects the synthesis to external papers;
opportunities and negative results help readers find follow-up questions and
avoid repeating unsuccessful analyses. The home page's "Find your way in"
cards state which question each kind of page answers.

When the corpus has findings, the top bar adds Results and Open questions
before the existing collections, which all keep their entries. The home page
opens with what the wiki is, how it was made, the corpus
counts and Ask, then "Find your way in", "What the projects found",
"Questions still open", The map and Topics.

Each home result and question carries a topic strip: one slot per topic, in
the same order on every strip, filled for each topic the entry touches. The
taller slot is the entry's main topic. Opening a strip lists its topic names.
A "Topic strips" panel above both sections says what a topic is and holds a
row of the same slots. Pointing at a slot shows that topic's name, linked to
its page, and its sentence from the home topic list. Picking a topic in the row
or in a strip's list outlines every home result and question that has it,
drops the card from the rest, and keeps the topic and how many of each share it
in the panel. The pick also lights that topic's cluster on the home map and
fades the others; "See it on the map" scrolls down to it, and the map's legend
says its colours are the same topics as the strips. Escape or "Show all" clears
the pick. Without JavaScript the
panel keeps its explanation, the row stays hidden, and the strips still open.

"What the projects found" shows three result cards, each from its own project
and topic. They are the results PubMed abstracts hold the least like and that
link to the most other projects, as the rendering section above ranks them.

"Questions still open" lists three questions that join projects, each naming
the projects it builds on. In the
open-questions grid a ringed dot marks a question that builds on
results from two or more projects; its pop-up names those projects, their
topics and the results it builds on.

A topic hub shows "Results from this topic" (up to three cards) and "Open
questions in this topic" (that topic's row of the grid) above its synthesis.

A result card shows its kind in plain words (Result, Interpretation, Null or
missing result, Correction), a title, a one or two sentence summary from
`state/gists.json`, and a footer naming the source report and the topic whose
concepts cite that report most. A card has no test statistics and no caveat; the page holds the
numbers and the Limits section. A finding without an accepted summary shows
only title and footer. The Results index (`/findings/`) filters cards by kind
and topic.

Under the Results picture, "Results several projects reached" shows every
shared result: a result that two or more projects reached, spanning two or more
topics. A shared card names its projects, its topics and how the results
relate. Its "Compare the results" button opens a panel under the card's row,
or under the card on a phone. The panel holds the question the projects asked,
each project's own result with its summary, and a paragraph on how they
relate. Without JavaScript every panel shows.

At the top of the Results index, the Results picture places each result by how it compares
with PubMed (columns, from "No close match in PubMed abstracts" to "Too little
published evidence to compare", then "Not compared yet" when any result lacks a
comparison) and by topic (rows). A project's results in one cell form a group.
Hovering over or focusing a group draws its links to other projects: a solid line for
related results, a dashed line for results the same open question builds on,
and a dotted line for one project using or citing another. Clicking a group
pins it and lists every link below the picture, including links to projects
with no results; Escape clears it. Phones draw no lines and open the list under
the tapped cell. A note under the picture names topics with no results.

A comparison chip appears on a card only when the PubMed comparison found a
close match, a build on earlier work, a difference or a similar result. Tap or
focus it to read that it is an AI comparison with PubMed abstracts, dated, and
that it does not establish novelty or correctness. "Too little published
evidence" and "Not assessed" show no chip.

`/directions/` is the open-questions grid: topics down the side, what answering
a question needs across the top (data already in the lakehouse, analysis to
build, new measurements, not yet clear), one dot per question. Dot shape is the
approach, colour is the topic. Hover, focus or tap a dot for the question and
what it needs; the dot is a link, so the grid works without JavaScript. Under
640 px each topic becomes one block. Every question is also in a collapsed list.
"Plan my next project" is gone from the home page; the Ask box stays. On a
direction, "Copy BERIL prompt" copies a prompt to paste into BERIL and "Copy
handoff brief" copies Markdown for a collaborator or a lab.
`scripts/check_reader.py` checks these pages (see
[the agentic workflow](agentic-workflow.md#checking-the-reader-pages)). A
comparison chip is an AI comparison with PubMed abstracts, not a reviewed
verdict.

Search (the top bar, or `/`) returns sections rather than whole pages, so a
result opens the page at the matching paragraph. It ranks by keywords unless
the reader turns on "Meaning search" in the search palette, which also ranks
sections by meaning. Ask the wiki (`/ask`) answers a question from the 8
best-matching sections, at most 3 from one page, and cites each claim to its
section. Ask never draws on author pages, so an answer cannot turn into a claim
about a person. Every knowledge page except author pages has an "Ask about this
page" button that answers from that page only. Meaning search and Ask use the
reader's own CBORG key, entered through the key button in the top bar. Ask
ranks by keywords and meaning together and answers with Claude Sonnet 5.5
unless the reader picks another CBORG model; when CBORG cannot embed the
question, the answer says it used keyword ranking only. The
[README](../README.md#search-and-ask) covers how the index and its vectors are
built.

`wiki/` is generated output. Change source reports, the
[editorial contract](../contract/AGENTS.md), recorded human concept decisions
or generation prompts, then run the curator. Preserve `.agentic/` when
resuming so accepted model results and prior token charges remain available.
