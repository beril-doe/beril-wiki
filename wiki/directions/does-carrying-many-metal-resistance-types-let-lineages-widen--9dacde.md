---
type: "Research direction"
description: "Genera resisting more metal types occupy broader niches, but the link weakened under a stricter prevalence filter, and habitat range itself is strongly inherited. Does metal-type diversity arise before habitat expansion or after it?"
hypothesis: "Most gains of new metal-resistance types happen after a lineage has already broadened its habitat range. Metal diversity is then a consequence of exposure, not a cause of niche expansion."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome-level metal-resistance calls and isolation-source metadata exist, but habitat classes are noisy and the tree-based gain-ordering analysis has to be built."
collections: ["kbase-ke-pangenome"]
findings: ["microbeatlas_metal_ecology--012a4b6c", "microbeatlas_metal_ecology--1e5f530e", "microbeatlas_metal_ecology--b38d81d3", "metal_resistance_global_biogeography--9181c949"]
conflicts: []
papers: ["35643011", "27717408", "37406521", "32681784"]
builds_on: ["findings/microbeatlas_metal_ecology--012a4b6c", "findings/microbeatlas_metal_ecology--1e5f530e", "findings/microbeatlas_metal_ecology--b38d81d3", "findings/metal_resistance_global_biogeography--9181c949"]
projects: ["metal_resistance_global_biogeography", "microbeatlas_metal_ecology"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does carrying many metal-resistance types let lineages widen their habitat, or follow it?

Genera resisting more metal types occupy broader niches, but the link weakened under a stricter prevalence filter, and habitat range itself is strongly inherited. Does metal-type diversity arise before habitat expansion or after it?

## Hypothesis

Most gains of new metal-resistance types happen after a lineage has already broadened its habitat range. Metal diversity is then a consequence of exposure, not a cause of niche expansion.

## Why it matters

If true, metal-resistance repertoires cannot be used to predict which lineages will spread, and co-selection ideas that treat metals as drivers of expansion would need revising.

## How to test it

On the genome tree in the Pangenome Collection, reconstruct gains of metal-resistance types and of habitat categories in the same genera, taking habitat categories from genome isolation-source metadata since the occurrence-based habitat counts behind the original finding are not in the listed collections. Test whether gains of habitat categories precede or follow gains of metal types along branches. Use soil enrichment and marine depletion of resistance in geolocated environmental genomes as an independent check of habitat dependence.

## What would support or refute it

Support: metal-type gains cluster on branches after habitat gains. Refutation: gains of metal types come first, or the two are unrelated once the tree is considered.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome-level metal-resistance calls and isolation-source metadata exist, but habitat classes are noisy and the tree-based gain-ordering analysis has to be built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/microbeatlas_metal_ecology--012a4b6c|Metal-type diversity, not AMR gene count, predicts bacterial niche breadth after phylogeny]] (Candidate novel)
- Finding: [[findings/microbeatlas_metal_ecology--1e5f530e|Metal-type association loses significance under strict prevalence filtering]] (Insufficient literature evidence)
- Finding: [[findings/microbeatlas_metal_ecology--b38d81d3|Niche breadth and habitat range are strongly phylogenetically conserved in bacteria]] (Insufficient literature evidence)
- Finding: [[findings/metal_resistance_global_biogeography--9181c949|Soil is enriched and marine depleted for metal resistance]] (Candidate novel)

## Closest published work

- [PMID 35643011](https://pubmed.ncbi.nlm.nih.gov/35643011/) Multiple metal(loid) contamination reshaped the structure and function of soil archaeal community.
- [PMID 27717408](https://pubmed.ncbi.nlm.nih.gov/27717408/) The structure and diversity of human, animal and environmental resistomes.
- [PMID 37406521](https://pubmed.ncbi.nlm.nih.gov/37406521/) The vertically-stratified resistomes in mangrove sediments was driven by the bacterial diversity.
- [PMID 32681784](https://pubmed.ncbi.nlm.nih.gov/32681784/) Development, spread and persistence of antibiotic resistance genes (ARGs) in the soil microbiomes through co-selection.

PMIDs 35643011 and 27717408 relate metal contamination and resistance diversity to communities; this asks about the order of events within lineages.
