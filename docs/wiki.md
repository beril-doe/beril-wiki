# Wiki architecture

The wiki is a layered synthesis over the BERIL Research Observatory's project
reports. Each layer answers a different reader question, and every factual
claim in the reader-facing layers carries a per-claim citation back to its
source project.

```mermaid
flowchart TD
    subgraph ENTRY["Entry layer — wiki-extra/ (start here)"]
        HOME[home.md — home] --> TOPICS["topics/ — narrative hubs,<br/>each opening with a<br/>PMID-cited Literature Context"]
        HOME --> OPP[opportunities.md —<br/>every Open Direction, one page]
        HOME --> NEG[negative-results.md —<br/>what did not work, per project]
    end

    subgraph SYNTH["Synthesis layer — wiki/"]
        TOPICS --> CONCEPTS["concepts/ — cross-project<br/>ideas, mechanisms, caveats"]
        TOPICS --> CONFLICTS["conflicts/ — recorded disagreements:<br/>Evidence Sides · Resolving Work"]
        CONCEPTS --> ENTITIES["entities/ — organisms, methods,<br/>datasets, compounds…"]
    end

    subgraph EVIDENCE["Evidence layer"]
        CONCEPTS -->|"keyed source footnotes"| SUMMARIES["summaries/ — one dense,<br/>faithful page per report"]
        SUMMARIES --> RAW[sources/ — the raw reports]
    end

    subgraph SIDE["Deterministic reference — wiki-extra/"]
        AUTH[authors/]
        DATA[data/ — collections used]
    end
```

## Page types and their contracts

| Layer | Page type | Contract |
|---|---|---|
| `wiki/summaries/` | one per report | dense and faithful, exact numbers, source footnotes on claims; ends with `## Slots Into` naming the concepts it feeds; includes null/negative results |
| `wiki/concepts/` | cross-project synthesis | argues *across* projects; typed relations in prose (**supports / contradicts / refines**); disagreements under `## Tensions`; ends with `## Open Directions` (data + method + question) |
| `wiki/entities/` | one per named thing | organisms, genes/pathways, compounds, methods, datasets, places, people; canonical name + aliases; single-source entities are hidden at publish until a second project cites them |
| `wiki-extra/topics/` | narrative hubs | the corpus argued as one story per topic; opens with `## Literature Context` (external, PMID-verified) |
| `wiki-extra/conflicts/` | promoted disagreements | `## Evidence Sides` (each side cited) and `## Resolving Work` (what would settle it) — never averaged away |
| `wiki-extra/` digests | opportunities, negative-results, authors, data | generated deterministically by code, no LLM |

## The citation grammar

- `[^project_id]` cites factual claims in summaries, concepts,
  entities, and hubs; ids are report filename stems (plus `discoveries` /
  `pitfalls` for the cross-project digests). `wiki_check.py` verifies every
  id resolves and every flagged number appears in a cited source.
- Standard relative Markdown links connect pages, including across `wiki/`
  and `wiki-extra/`. Footnote definitions link to the corresponding source
  record's resource. Model-response shorthand (`[src:]` and wikilinks) is
  normalized by the writer, not saved as the corpus format.
- `## Literature Context` sections are the one exception to corpus-only
  citation: they cite external papers as `[PMID nnnn](pubmed url)`, verified
  against the actual PubMed query results at build time.

## Frontmatter (managed by code, never hand-edited)

Every non-reserved page in both collections carries `type`; generated pages
also retain their descriptive metadata. `sources` contains records with
`resource` and, for corpus citations, stable `id` values. Concepts cite summaries;
summaries cite raw reports. Optional source metadata is preserved. `index.md`
and `log.md` follow OKF reserved-page rules, while `wiki-extra/home.md` holds
the narrative overview. No trust or verification claims are invented.

## Publish-time transforms

`quartz_ingest.py` derives the reader site from the corpus without touching
it:

- Native links are remapped into Quartz's shared content directory; summaries link their raw
  reports ("Raw report:") and gain a deterministic **"Feeds into:"** line
  listing every concept that cites the project — a first, honest impact view.
- Entity pages citing only one source are omitted (they return automatically
  once a second project cites them); their links downgrade to plain text.
- Flagship figures chosen by the figures stage are spliced in from the
  committed figure cache. Source footnotes remain intact.
- The home page links to the upstream OKF graph, rendered directly from both
  native collections, including entities filtered from the reader site.

## Reading model

Start at the **home page → a topic hub**: the Literature Context says where
the field stands, "What the Corpus Shows" argues the corpus's answer, and
"Where to Go Deeper" hands you concepts → summaries → raw reports, so every
claim is at most three hops from its evidence. `opportunities.md` is the
what-to-do-next surface; `negative-results.md` is what to check before
repeating an analysis.

## Ground rules

`wiki/` and `wiki-extra/` are **generated output — never hand-edit content**.
Editorial behavior is changed in `contract/AGENTS.md` (injected into every
compile call) or in the stage prompts; content changes flow from source
reports through the pipeline.
