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
| `wiki/findings/` | At most 6 headline findings per report in `contract/cards.yaml`, each with Key figures, the verbatim Evidence quote, its Caveat and the report's other caveats. The literature label lives in `state/novelty.json` and joins the page at publish. The `outcomes` stage, which runs after `gists`, reads every finding publish would list and writes its result type to `state/outcomes.json`. Claude names one type, GPT reviews it, and the answer is cached per finding on its inputs. The stage reads every finding because the extraction tag misfiles in both directions. |
| `wiki/directions/` | Research directions for each topic in `contract/cards.yaml`, written from the topic's findings, literature labels and conflicts: the question, Hypothesis, Why it matters, How to test it, What would support or refute it, Data, Builds on and Closest published work. Proposals that would repeat or correct existing work are not directions; they are listed per report for maintainers at publish. The `followups` stage, which runs after `directions`, reads every direction and writes what following it up needs to `state/followups.json`. Claude names one answer, GPT reviews it, and the answer is cached per direction on its inputs. The stage reads every direction because its `approach` and `readiness` fields misfile in both directions. The two stages share one loop in `stages/classify.py`. A failed item keeps its old answer in state for recovery, and publish falls back as described below. |

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
    (each project, its topic and its results) and `cross_topics`.
  - `findings/index.md` carries the Results map's data in its frontmatter:
    the comparison columns (`compare_order`), the note for each column
    (`compare_notes`), `something_new` (the "Something new" head and the two
    columns it spans), the links, the shared results (most topics first),
    project titles and the topics with no results. Links come in three
    families: `r`, related results from `state/links.json`; `p`, one
    project's report uses or cites another's, also from `state/links.json`;
    and `q`, results the same open question builds on, computed from the
    direction records. The map draws only `r` links whose two results are
    both listed. A link or shared result with a missing end is dropped.
    `cards.json` gains the same `links` and `shared`.
  - A finding page's frontmatter gains `related`: the listed results in other
    projects that a current related-result link joins to it. The page lists
    them under "Related results in other projects", each with its report
    title and the relation in reader words, sorted by report title, then by
    result title. A result with no listed related result has no such section.
  - Publish ranks three results (`home_rank`) and three questions that
    build on several projects (`home_question_rank`) for the home page.
    The home results come only from projects that feed two or more topics,
    and each comes from its own project and topic. Results rank by their
    PubMed comparison (new direction, then differs, then adds to, then the
    rest), then by how many other projects they link to, then a positive
    result before the other types, then by the project's topic count. The home
    questions rank by how many projects they build on, then by how many
    topics. No project appears in two home questions.
  - Each shared result in `state/shared.json` with two or more members gives
    each member's card a Compare button on the Results page. A shared result
    retires when any member is unlisted, because its statement speaks for
    every member.
  - A finding's `rtype` is its result type from `state/outcomes.json`:
    `positive`, `negative`, `inconclusive` or `data`. Its `kind_text` gives
    the type in reader words: Positive result, Negative result, Inconclusive
    or About the data. Publish ignores a failed label. Before the `outcomes`
    stage has read a finding, or when its label failed, publish takes the type
    from the extraction tag. An observation, inference or correction becomes
    positive, a measured absence becomes negative, and an inconclusive test or
    any other null result becomes inconclusive.
  - A listed correction gains `updates_claim`, and its card shows "Revises an
    earlier claim" beside its type.
  - A question page's frontmatter gains `follow`, what following it up needs
    from `state/followups.json`: `existing`, `outside` or `experiment`. Its
    `follow_text` gives that in reader words: Analyze existing data, Add
    outside data or Run an experiment. An experiment question whose first
    step analyzes existing data gains `first_step` ("Starts with existing
    data"). A question that may not find or join its data gains
    `data_unclear` ("Data availability unclear"). Before the `followups`
    stage has read a question, or when its label failed, publish takes these
    from the direction's own fields. A lakehouse analysis becomes existing
    data and any other approach an experiment. "Analysis then experiment"
    sets `first_step`, and an unknown readiness sets `data_unclear`. The
    question page's Data line reads "Following up: …" in the same words.
  - `directions/index.md` carries the grid's columns, least effort first, in
    `follow_order`, their words in `follow_text` and each column's
    definition in `follow_notes`.
  - Free text a stage wrote, such as a readiness explanation or a question's
    body, passes through one map of reader terms, so "needs compute" reads
    "needs a new analysis" and a label name reads as its chip text.
  - A finding page's frontmatter gains `listed`. A finding is listed (on the
    Results page, in counts, the map and the home and topic hub picks) only
    with an accepted plain summary that does not repeat an earlier finding of
    its report, and a null result only when it measured something; missing
    data and an analysis that never ran are not results. A finding the
    `outcomes` stage types as `bookkeeping` (a fix to the project's own list
    or rule) or `untested` (an explanation the project never tested) is not
    listed either. An unlisted finding keeps its page, so links to it still
    resolve.
  - A listed correction carries its PubMed chip like any other result. A label whose searches found no abstracts says so instead of the
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
avoid repeating unsuccessful analyses.

The top bar holds Results and Open questions (when the corpus has findings),
Topics, a Browse menu, About, Search, Ask and the theme toggle. Browse lists
Concepts, Entities, Conflicts, Reports and Authors. Without JavaScript the
Browse list opens while focus is inside the menu. About is the last site
link. On a wide screen it sits at the right end of the links, just before
Search. At 960 px and below the links take a row of their own, and About
follows Browse on that row.

The home page opens with the wiki's title, the introduction from
`wiki/index.md`, the search box and an "Ask the wiki" button. Beside the
introduction, "The corpus" gives the number of project reports,
cross-project digests, concepts, entities, recorded conflicts and topics.
Each figure links to its collection. The sections that follow are
"Highlights", "Find your way in", "The map" and "Topics". "Highlights"
appears only when the corpus has findings. It holds the "Topic strips" key,
then "What the projects found" and "Questions still open".

"Find your way in" holds one card per kind of page: Topics, Concepts,
Entities, Conflicts and Reports, then Results and Open questions when the
corpus has findings. Each card states which question that kind of page
answers, and gives its page count. A row of links follows, taken from the
Browse list in `wiki/index.md`.

"What the projects found" shows the three result cards that publish ranks
for the home page, as the rendering section above describes. "Questions
still open" shows the three questions that publish ranks for the home page.
Each question is a card that names the projects it builds on. The question
cards use the same three-column grid as the result cards, so their topic
strips line up. Below 900 px both take one column. Each part
ends with a link to all results or all questions.

Each home result and question carries a topic strip: one slot per topic, in
the same order on every strip, filled for each topic the entry touches. The
taller slot is the entry's main topic. Opening a strip lists its topic names.
A "Topic strips" key above both parts is one row: its label, the same slots
and a readout. "What do the colours mean?" opens the explanation of what a
topic is and how a strip reads. Pointing at a slot shows that topic's name,
linked to its page, and its sentence from the topic list in `wiki/index.md`.
Picking a
topic in the row or in a strip's list outlines every home result and
question that has it. The other entries lose their card background and
their strips fade. The readout keeps the picked topic and says how many
results and questions on the page share it. The pick also lights that
topic's cluster on the home map and fades the others. "See it on the map"
scrolls down to the map, whose legend says its colours are the same topics
as the strips. Escape or "Show all" clears the pick. Without JavaScript the
key keeps its label and its explanation, the row of slots stays hidden, and
the strips still open.

"The map" draws the topics and the concepts they gather. A click on a point
opens its page. "Topics" is a table with one row per topic: its name, its
sentence from the topic list in `wiki/index.md`, and its counts of concepts,
reports, conflicts and entities.

The Topics index (`/topics/`) lists the topic cards, each with its concept
and report counts.

Topic hubs, project reports and concept pages list the results and open
questions that belong to them, in the card style of the Results page. A part
shows its first three entries as cards. A "N more" fold lists the rest by
title. An open-question card shows its title, why, "Builds on a
new-direction result" when that applies, and what following it up needs. It
adds "Starts with existing data" and "Data availability unclear" when they
apply. A part with no entries
does not appear. The heads in these parts add no space above them beyond the
gap between parts.

- A topic hub opens with "Results from this topic" and "Open questions in
  this topic" (every question filed under the topic, by title). The results
  part shows up to three cards from the results filed under the topic, ordered
  by their rank for that topic, then by comparison label. When a topic's top
  three ranked results hold no negative result, publish swaps the third for
  the topic's first negative result from another project, if it has one.
  Each part links to
  the Results or Open questions page with its Topic chip set to that topic,
  so the results link shows every card again. A topic with no results of its
  own shows its top-ranked results from other topics, with no results link.
  A "Background" head
  then introduces the synthesis. Topic hubs do not show the open-questions
  grid.
- A project report opens with "Results from this project" (New direction first) and
  "Open questions that build on this project". A "The report" head then
  introduces the summary.
- A concept page opens with "Results from the projects this page cites" and
  "Open questions on these projects". A "Background" head then introduces
  the synthesis. The results take one project at a time, so the first cards
  come from different projects. Within each project, results filed under the
  concept's own topic come first, then New direction first. Questions that build on
  more of the cited projects come first.
- Every topic, report and concept page shows both parts, so pages of one
  kind share one layout. An empty part keeps its head and shows one sentence
  in a dashed box, such as "No open question builds on this project yet."
  The two cross-project digests have no project, so they show neither part.

A result card shows its type in plain words (Positive result, Negative
result, Inconclusive, About the data), a title, a one or two sentence
summary from `state/gists.json`, and a footer naming the source report and
the topic whose concepts cite that report most. A result that revises the
project's own earlier claim also shows "Revises an earlier claim", on its card,
its page bar and its map preview and box list. An unlisted bookkeeping fix's page
shows no type, no revision note and no PubMed chip. A card has no test statistics
and no caveat; the page holds the numbers and the Limits section. A finding
without an accepted summary shows only title and footer.

The Results index (`/findings/`) opens with a map headed "How new is each
result?". A mark's position shows the topic (rows) and how the result
compares with PubMed (columns: New direction, Adds to published work,
Differs from published work, Similar to published work, No clear comparison,
then Not compared yet when any result lacks a comparison). A "Something new"
head with its result count spans the first two columns, the two kinds of
new. A "Compared with published work" head spans the rest. Every
column heading carries the note `compare_notes` gives it, shown on hover or
on a click or tap. The New direction note says that an AI search of PubMed
abstracts found nothing close, so the results could open a new direction,
and that the search does not establish novelty or correctness.

A mark's fill and shape show the type of result: a solid circle for a
positive result, a hollow circle for a negative result, a dashed circle for
an inconclusive result and a grey square for a result about the data. A ring marks a
result that has a related result in another project, where that result also
has a mark. Marks are ink and 10 px across, and no mark takes a column's
colour. Each column header has a coloured bar: orange for New direction,
blue for Adds to published work, green for Differs from published work and
Similar to published work, and grey for No clear comparison and Not compared
yet. A square
box holds one project's results in one cell. The square beside each row's
topic label is the topic's colour, the same colour its cards and chips use;
no mark takes it. The legend draws the kinds, the ring and the box with the
same classes as the map.

Hovering over or focusing a box draws a line from each of its ringed results
to its related result, outlines the box and dashes the outline of each box
the lines reach. Other boxes fade. Hovering a result's mark opens its card
beside the mark: its kind, title, gist, a line when it has a related result,
project and an "Open the result" link. The card stays while the pointer is on
the mark or the card. While the pointer moves from the mark toward the card,
the card stays inside the triangle from where the pointer left the mark to
the card's near edge. Marks the pointer crosses inside that triangle do not
take over; outside it, the mark under the pointer takes over. A click or tap
on a mark pins that result's card only. Escape, a press outside, or a second
click or tap closes it. A pinned card stays while other marks are hovered and
follows its mark on scroll and resize. Clicking a box's edge, or pressing
Enter on the focused box, pins the box and lists below the map the project
(linked to its report), each result in the box with its kind, and each
related result in another project with the link's label from
`state/links.json` and a button that pins that result's box. Escape clears it. At 700 px and below the map becomes a
list by topic: each cell shows its column label with the note button and its
count, and no lines are drawn. Each cell label has a bar on its left in its
column's colour. On a phone, a tap on a mark opens its card,
and a tap on the box's edge opens the list under the cell. Touch screens show
larger marks. A note under the map names topics with no results.

A comparison chip appears on a card only when the PubMed comparison gave one
of four labels: New direction, Adds to published work, Differs from
published work or Similar to published work. Tap or focus it to read its
note: an AI comparison with PubMed abstracts, dated, that does not establish
novelty or correctness. The New direction chip's note says the search found
nothing close to the result, so it could open a new direction. "No clear
comparison" and "Not assessed" show no chip.

`/directions/` is the open-questions grid: topics down the side, what
following up a question needs across the top, one dot per question. The
columns run least effort first: Analyze existing data, Add outside data, Run
an experiment. A line above them reads "Less effort to follow up → more
effort". Each column header shows its definition from `follow_notes` under
its name. Every dot is an
ink circle, 10 px across like the Results map's marks. Both maps use one type
size for row labels and one for column headers. A dot is orange when the
question cites a listed result in the Results map's New direction column, and
ringed when it builds on results from two or more projects. A half-filled dot
starts with existing data. A dashed dot marks a question whose data
availability is unclear. The legend shows each of these two marks only when a
question in the grid has it. The square beside each row's topic label is the topic's
colour. Hover, focus or tap a dot for a pop-up with the question, "Builds on
a new-direction result" when that applies, what following it up needs, "Starts
with existing data" and "Data availability unclear" when they apply, why, and
an "Open the question" link. A ringed dot's pop-up also names
the projects it builds on, their topics and the results it builds on. The
pop-up stays, pins and closes as a result's card does on the Results map.
The dot's accessible name carries the question, what following it up needs,
the two markers and the new-direction words when they apply, and how many
projects and topics it joins. The dot is a link, so the
grid works without JavaScript. Under 640 px each topic becomes one block.

Under each map, every listed result or question is a card in the concepts
card style, and a filter bar sits above the cards. The bar holds a text
filter, a sort, a Cards or List switch, an "N of M" count, rows of chips and
toggles. The URL keeps the state (`q`, `sort`, `view`, one parameter per chip
row and per toggle), so a link or a reload restores the filter. Filtering
fades the map marks that the filter hides, and each box whose marks are all
hidden. Cards render without JavaScript; the bar needs it.

- On Results, the chip rows are Topic, How new and Type of result, and the
  sorts are Most new first, Topic and Project. The "Related across projects" toggle keeps
  the results that have a related result in another project, and those cards
  say so. A result that belongs to a shared result names the relation and has
  a Compare button. Compare opens a panel
  under the last card of its row, holding the question the projects asked,
  each project's own result with its summary, and a paragraph on how they
  relate. Without JavaScript every panel shows below the cards.
- On Open questions, the chip rows are Topic and What following up needs, and
  the sorts are Topic and Least effort first. Each What following up needs
  chip carries its column's note. The toggles are "Starts with existing
  data", "Builds on results from two or more projects" and "Builds on a
  new-direction result". Each toggle appears only when a question has it. A
  question card shows what following it up needs, "Starts with existing data"
  and "Data availability unclear" when they apply, why, "Builds on a
  new-direction result" when that applies, how many projects and topics it
  joins, and its topic.

A result page lists "Related results in other projects" when a listed result
in another project relates to it. A result page lists "Concepts that cite this
project", and a question page lists "Concepts that cite these projects": the
concept pages that cite the project reports behind it. The concepts that cite
those reports most come first. The list shows six, and a "N more" fold holds
the rest. On a direction, "Copy BERIL prompt" copies a
prompt to paste into BERIL and "Copy handoff brief" copies Markdown for a
collaborator or a lab.
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
reader's own CBORG key. The reader adds, changes or forgets it under the
question box on the Ask page and in "Ask about this page", or in the search
palette's meaning-search control. Asking or turning on meaning search without
a key opens the key dialog. Ask
ranks by keywords and meaning together and answers with Claude Sonnet 5.5
unless the reader picks another CBORG model; when CBORG cannot embed the
question, the answer says it used keyword ranking only. The
[README](../README.md#search-and-ask) covers how the index and its vectors are
built.

`wiki/` is generated output. Change source reports, the
[editorial contract](../contract/AGENTS.md), recorded human concept decisions
or generation prompts, then run the curator. Preserve `.agentic/` when
resuming so accepted model results and prior token charges remain available.
