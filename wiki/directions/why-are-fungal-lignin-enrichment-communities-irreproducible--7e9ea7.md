---
type: "Research direction"
description: "On lignin, bacterial communities repeated closely across replicates while fungal ones were nearly unrelated between replicates, and any memory of earlier rounds was undetectable in fungi. Is fungal assembly intrinsically chance-driven, or does low fungal inoculum density cause it?"
hypothesis: "Fungal replicate variation falls sharply when each replicate receives a large, well-mixed share of the same inoculum. If assembly is intrinsically chance-driven, variation stays high."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Needs new enrichment cultures with more replicates and deeper fungal sequencing; the original data had very few replicates and poor ITS replicate agreement."
collections: []
findings: ["lignin_community_enrichment--0c3cdb00", "lignin_community_enrichment--8b7c9a44", "lignin_community_enrichment--fa5eb6ce"]
conflicts: []
papers: ["42592007", "26487437", "39526802"]
builds_on: ["findings/lignin_community_enrichment--0c3cdb00", "findings/lignin_community_enrichment--8b7c9a44", "findings/lignin_community_enrichment--fa5eb6ce"]
projects: ["lignin_community_enrichment"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Why are fungal lignin-enrichment communities irreproducible while bacterial ones repeat?

On lignin, bacterial communities repeated closely across replicates while fungal ones were nearly unrelated between replicates, and any memory of earlier rounds was undetectable in fungi. Is fungal assembly intrinsically chance-driven, or does low fungal inoculum density cause it?

## Hypothesis

Fungal replicate variation falls sharply when each replicate receives a large, well-mixed share of the same inoculum. If assembly is intrinsically chance-driven, variation stays high.

## Why it matters

It would separate a sampling artefact from priority-effect assembly in fungi. That tells designers of lignin-degrading consortia whether fungal members can be reproducibly selected.

## How to test it

Run lignin enrichments from one soil using a dilution series of a pooled inoculum with many replicates per dilution. Sequence fungal ITS at higher depth against a curated fungal reference and bacterial 16S. Measure between-replicate variation by dilution for both groups. Re-run a second round to test memory of first-round history.

## What would support or refute it

Support: fungal replicate variation drops at high inoculum while bacteria stay reproducible at all dilutions. Refute: fungal variation stays high at all dilutions, supporting chance-driven assembly.

## Data

Approach: experiment. Readiness: needs new measurements. Needs new enrichment cultures with more replicates and deeper fungal sequencing; the original data had very few replicates and poor ITS replicate agreement.

## Builds on

- Finding: [[findings/lignin_community_enrichment--0c3cdb00|Bacteria respond reproducibly while fungi are highly stochastic]] (Candidate novel)
- Finding: [[findings/lignin_community_enrichment--8b7c9a44|Ecological memory not detectable in fungal ITS data]] (Insufficient literature evidence)
- Finding: [[findings/lignin_community_enrichment--fa5eb6ce|Planned bacterial–fungal Procrustes concordance test was not completed]] (Insufficient literature evidence)

## Closest published work

- [PMID 42592007](https://pubmed.ncbi.nlm.nih.gov/42592007/) Lignin enrichment selects specialized fungal communities from contrasting soils.
- [PMID 26487437](https://pubmed.ncbi.nlm.nih.gov/26487437/) Soil-Derived Microbial Consortia Enriched with Different Plant Biomass Reveal Distinct Players Acting in Lignocellulose Degradation.
- [PMID 39526802](https://pubmed.ncbi.nlm.nih.gov/39526802/) Microbial consortia driving (ligno)cellulose transformation in agricultural woodchip bioreactors.

PMID 42592007 shows fungal lignin enrichments shaped by temperature and inoculum source, and PMID 26487437 reports bacterial and fungal consortia differing by substrate; neither compares replicate reproducibility of the two groups across inoculum density.
