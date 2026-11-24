---
type: "Research direction"
description: "Can laboratory fitness under metal stress predict genus abundance across Oak Ridge sites with differing uranium?"
hypothesis: "Per-metal lab tolerance, not an aggregate score, predicts the abundance ratio between high and low uranium sites once genus-level matching and geochemical covariates are included."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Abundance, chemistry and fitness tables appear in the catalog; matching and covariate modelling remain undone, and the catalog did not show metadata linking every sample."
databases: ["enigma.coral", "kescience.fitnessbrowser"]
tables: ["enigma.coral.ddt_brick0000459", "enigma.coral.sdt_sample", "enigma.coral.ddt_brick0000010", "kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.organism"]
findings: ["lab_field_ecology--7268dc9b", "lab_field_ecology--c4028be7", "lab_field_ecology--0a8de054", "lab_field_ecology--94b20be5"]
conflicts: []
papers: ["30523276", "17948804", "20729318", "38552495"]
builds_on: ["findings/lab_field_ecology--7268dc9b", "findings/lab_field_ecology--c4028be7", "findings/lab_field_ecology--0a8de054", "findings/lab_field_ecology--94b20be5"]
projects: ["lab_field_ecology"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Does lab-measured metal tolerance predict which genera thrive at uranium-contaminated field sites?

Can laboratory fitness under metal stress predict genus abundance across Oak Ridge sites with differing uranium?

## Hypothesis

Per-metal lab tolerance, not an aggregate score, predicts the abundance ratio between high and low uranium sites once genus-level matching and geochemical covariates are included.

## Why it matters

A working link would let lab fitness screens forecast field persistence. A failure would show lab fitness misses the selective pressures that structure natural communities.

## How to test it

Match Fitness Browser genera to Oak Ridge amplicon data, replace the aggregate score with per-metal fitness scores, and correlate with each site's uranium and metal concentrations, adding pH and oxygen as covariates. Compare Caulobacter (less abundant at high uranium) and Herbaspirillum (more abundant), and Desulfovibrio, which is too rare to test. Extend beyond 12 genera.

## What would support or refute it

Support: per-metal scores track field abundance in the right direction after covariates. Refute: no relationship, or Caulobacter and Herbaspirillum directions contradict their lab scores.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Abundance, chemistry and fitness tables appear in the catalog; matching and covariate modelling remain undone, and the catalog did not show metadata linking every sample.

## Builds on

- Finding: [[findings/lab_field_ecology--7268dc9b|Caulobacter abundance falls strongly at high-uranium sites]] (Candidate novel)
- Finding: [[findings/lab_field_ecology--c4028be7|Herbaspirillum is enriched at high-uranium sites]] (Candidate novel)
- Finding: [[findings/lab_field_ecology--0a8de054|Lab metal tolerance does not significantly predict field abundance at contaminated sites]] (Extends retrieved work)
- Finding: [[findings/lab_field_ecology--94b20be5|Desulfovibrio shows no uranium correlation despite ENIGMA model status]] (Candidate novel)

## Closest published work

- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.
- [PMID 17948804](https://pubmed.ncbi.nlm.nih.gov/17948804/) Inhibition of a U(VI)- and sulfate-reducing consortia by U(VI).
- [PMID 20729318](https://pubmed.ncbi.nlm.nih.gov/20729318/) Significant association between sulfate-reducing bacteria and uranium-reducing microbial communities as revealed by a combined massively parallel sequencing-indicator species approach.
- [PMID 38552495](https://pubmed.ncbi.nlm.nih.gov/38552495/) Reproducible responses of geochemical and microbial successional patterns in the subsurface to carbon source amendment.

30523276 shows Rhodanobacter rising with uranium in this aquifer, but no work tests lab fitness as a predictor across genera.
