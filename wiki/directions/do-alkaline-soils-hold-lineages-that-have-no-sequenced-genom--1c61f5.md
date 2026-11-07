---
type: "Research direction"
description: "Poorly mapped soils are about 0.8 pH units more alkaline than well-mapped ones, and models of soil gene content fail on new data. Do alkaline soils harbour whole lineages absent from genome collections, rather than just fewer sequenced samples?"
hypothesis: "Taxa abundant in alkaline soils are disproportionately from clades lacking close genomes, and this holds after accounting for how many samples were sequenced per pH range."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Soil pH and taxon profiles are present, but taxon-to-genome matching and sampling-effort matching must be built."
collections: ["nmdc-arkin", "nmdc-ncbi-biosamples", "kbase-ke-pangenome"]
findings: ["soil_frontier_genomics--25df967c", "soil_frontier_genomics--0fa73728"]
conflicts: []
papers: ["38722174", "36443458"]
builds_on: ["findings/soil_frontier_genomics--25df967c", "findings/soil_frontier_genomics--0fa73728"]
projects: ["soil_frontier_genomics"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Do alkaline soils hold lineages that have no sequenced genome yet?

Poorly mapped soils are about 0.8 pH units more alkaline than well-mapped ones, and models of soil gene content fail on new data. Do alkaline soils harbour whole lineages absent from genome collections, rather than just fewer sequenced samples?

## Hypothesis

Taxa abundant in alkaline soils are disproportionately from clades lacking close genomes, and this holds after accounting for how many samples were sequenced per pH range.

## Why it matters

It would separate a true biological blind spot from a sampling gap, and direct isolation and sequencing effort toward alkaline soils.

## How to test it

Assign taxa from soil samples in NMDC Multi-omics and NMDC BioSamples to the Pangenome Collection, noting taxa with no close genome match. Compare the share of unmatched taxa across pH bins, matching by number of samples per bin and sampling region.

## What would support or refute it

Support: the unmatched share rises with pH even with sampling effort matched. Refutation: the share is flat across pH once sampling is matched, so the gap is only a sampling effect.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Soil pH and taxon profiles are present, but taxon-to-genome matching and sampling-effort matching must be built.

- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/soil_frontier_genomics--25df967c|Genomic-frontier soils are more alkaline than well-mapped soils]] (Insufficient literature evidence)
- Finding: [[findings/soil_frontier_genomics--0fa73728|All soil functional-gene prediction models fail out-of-sample]] (Insufficient literature evidence)

## Closest published work

- [PMID 38722174](https://pubmed.ncbi.nlm.nih.gov/38722174/) Genomic fingerprints of the world's soil ecosystems.
- [PMID 36443458](https://pubmed.ncbi.nlm.nih.gov/36443458/) Standardized multi-omics of Earth's microbiomes reveals microbial and metabolite diversity.

PMID 38722174 describes genomic fingerprints of soil ecosystems; this asks whether pH marks lineages with no genomic coverage.
