---
type: "Research direction"
description: "When soil inocula are enriched on lignin, do fungal communities diverge between identical replicates because of chance early colonisation, while bacterial communities converge through consistent selection?"
hypothesis: "Fungal replicates diverge because early random colonisers dominate and are not displaced, so variability persists at high sequencing depth and with a standard mock community. Bacterial replicates converge regardless of inoculum size."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "New replicated enrichments with deep fungal and bacterial sequencing and mock communities are required; the earlier run had too few replicates and poor fungal read depth."
databases: []
tables: []
findings: ["lignin_community_enrichment--0c3cdb00", "lignin_community_enrichment--8b7c9a44"]
conflicts: []
papers: ["42592007", "26487437", "38035526"]
builds_on: ["findings/lignin_community_enrichment--0c3cdb00", "findings/lignin_community_enrichment--8b7c9a44"]
projects: ["lignin_community_enrichment"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Are fungal lignin-enrichment communities variable because of chance founder effects rather than noisy sequencing?

When soil inocula are enriched on lignin, do fungal communities diverge between identical replicates because of chance early colonisation, while bacterial communities converge through consistent selection?

## Hypothesis

Fungal replicates diverge because early random colonisers dominate and are not displaced, so variability persists at high sequencing depth and with a standard mock community. Bacterial replicates converge regardless of inoculum size.

## Why it matters

It would separate a true difference in how bacterial and fungal communities assemble from a measurement problem, and decide whether fungal enrichment can be engineered by selection or needs control of founders.

## How to test it

Split one soil inoculum into many replicate lignin enrichments at two inoculum sizes. Sequence fungal markers at high depth with a known mock community and spike-in, and bacterial markers in parallel. Compare spread among replicates for each group across successive transfer rounds and test whether early dominant fungal taxa predict later composition.

## What would support or refute it

Support: fungal spread stays high at matched depth and mock communities are recovered faithfully, early colonisers predict later composition, while bacterial replicates converge. Refutation: fungal spread falls sharply at high depth or tracks sequencing failures in the mock, which would make the earlier difference a technical artefact.

## Data

Approach: experiment. Readiness: needs new measurements. New replicated enrichments with deep fungal and bacterial sequencing and mock communities are required; the earlier run had too few replicates and poor fungal read depth.

## Builds on

- Finding: [[findings/lignin_community_enrichment--0c3cdb00|Bacteria respond reproducibly while fungi are highly stochastic]] (Candidate novel)
- Finding: [[findings/lignin_community_enrichment--8b7c9a44|Ecological memory not detectable in fungal ITS data]] (Insufficient literature evidence)

## Closest published work

- [PMID 42592007](https://pubmed.ncbi.nlm.nih.gov/42592007/) Lignin enrichment selects specialized fungal communities from contrasting soils.
- [PMID 26487437](https://pubmed.ncbi.nlm.nih.gov/26487437/) Soil-Derived Microbial Consortia Enriched with Different Plant Biomass Reveal Distinct Players Acting in Lignocellulose Degradation.
- [PMID 38035526](https://pubmed.ncbi.nlm.nih.gov/38035526/) Bacterial community regulation of soil organic matter molecular structure in heavy metal-rich mangrove sediments.

PMID 42592007 shows fungal lignin enrichment shaped by temperature and inoculum source and PMID 26487437 reports differing bacterial and fungal consortia across substrates, but neither compares replicate reproducibility between kingdoms at equal depth.
