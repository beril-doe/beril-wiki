# Wiki format and reading guide

The wiki synthesizes BERIL Research Observatory reports into linked scientific
pages. The [curator operating guide](agentic-workflow.md) describes how those
pages are generated; the [HTML walkthrough](agentic-workflow.html) shows who
chooses the work and who validates it.

## Collections

| Path | Purpose and required content |
| --- | --- |
| `wiki/index.md` and `wiki/topics/` | Home and narrative topic hubs. The curator chooses titles and assigns every concept to exactly one group. Literature Context adds external context with verified PubMed citations. |
| `wiki/concepts/` | Cross-project synthesis with cited evidence, supports/contradicts/refines relations, Tensions, and Open Directions. |
| `wiki/conflicts/` | Disagreements with cited Evidence Sides and Resolving Work; conflicting findings remain explicit. |
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
retention of unchanged evidence. Separate model review assesses scientific
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

Run [`scripts/build_quartz.sh`](../scripts/build_quartz.sh) after local
acceptance to render the site. Publishing committed content is separate from
curation; the curator does not build or deploy the site. See the
[README publishing instructions](../README.md#publishing).

## Reading and editing

Start at home, open a topic hub, then follow concepts to summaries and raw
reports. Literature Context connects the synthesis to external papers;
opportunities and negative results help readers find follow-up questions and
avoid repeating unsuccessful analyses.

`wiki/` is generated output. Change source reports, the
[editorial contract](../contract/AGENTS.md), recorded human concept decisions
or generation prompts, then run the curator. Preserve `.agentic/` when
resuming so accepted model results and prior token charges remain available.
