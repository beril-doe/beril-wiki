---
type: "Research direction"
description: "With no lanmodulin or xoxF in most acid-drainage genomes from the rare-earth site, do those organisms handle lanthanides with proteins that annotation cannot recognise?"
hypothesis: "Acid-drainage genomes from rare-earth sites carry lanthanide-binding proteins with calcium-binding-like motifs but no match to known families, and these bind lanthanides more strongly than calcium."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Motif scanning needs new computation and the binding test needs protein expression and spectroscopy."
collections: ["kbase-ke-pangenome", "kbase-uniref"]
findings: ["lanthanide_methylotrophy_atlas--4c03dc0b"]
conflicts: []
papers: ["34432449", "30351021", "37259003", "35999730"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--4c03dc0b"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Do rare-earth-rich acid sites use lanthanide-binding proteins unrelated to known ones?

With no lanmodulin or xoxF in most acid-drainage genomes from the rare-earth site, do those organisms handle lanthanides with proteins that annotation cannot recognise?

## Hypothesis

Acid-drainage genomes from rare-earth sites carry lanthanide-binding proteins with calcium-binding-like motifs but no match to known families, and these bind lanthanides more strongly than calcium.

## Why it matters

It would reveal lanthanide-handling systems outside the known protein families and show that gene annotation missed them. It could also give new proteins for rare-earth recovery.

## How to test it

Scan the acid-drainage genomes for proteins with lanmodulin-like or calcium-binding motif patterns and predicted secreted or periplasmic location, excluding those with annotated homologs. Compare their frequency with matched genomes from acid drainage without rare earths. Express the top candidates and test lanthanide and calcium binding by sensitised terbium luminescence.

## What would support or refute it

Support: candidates enriched at the rare-earth site over the control that bind lanthanides preferentially. Refutation: candidates are equally common in the control or bind calcium as well as lanthanides.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Motif scanning needs new computation and the binding test needs protein expression and spectroscopy.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--4c03dc0b|REE-acid-mine-drainage MAGs show little xoxF and no lanmodulin]] (Insufficient literature evidence)

## Closest published work

- [PMID 34432449](https://pubmed.ncbi.nlm.nih.gov/34432449/) Probing Lanmodulin's Lanthanide Recognition via Sensitized Luminescence Yields a Platform for Quantification of Terbium in Acid Mine Drainage.
- [PMID 30351021](https://pubmed.ncbi.nlm.nih.gov/30351021/) Lanmodulin: A Highly Selective Lanthanide-Binding Protein from a Lanthanide-Utilizing Bacterium.
- [PMID 37259003](https://pubmed.ncbi.nlm.nih.gov/37259003/) Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer.
- [PMID 35999730](https://pubmed.ncbi.nlm.nih.gov/35999730/) Broad-spectrum and effective rare earth enriching via Lanmodulin-displayed Yarrowia lipolytica.

PMID 34432449 and 37259003 characterise lanmodulin binding; this searches for binders that annotation-based detection could not find.
