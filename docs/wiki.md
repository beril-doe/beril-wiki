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
one. Separate model review assesses scientific
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
