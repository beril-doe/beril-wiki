---
type: "Research direction"
description: "Tryptophan is produced, has a complete catabolic pathway call and many fitness-relevant genes, and growth on it is predictable in a large model, yet none of 50 P. fluorescens strains used it as a carbon source. Does it serve these strains as a nitrogen source or biosynthetic input instead?"
hypothesis: "Tryptophan-fitness genes in these strains act in nitrogen assimilation or biosynthesis, so strains with the complete pathway grow on tryptophan as sole nitrogen source but not as sole carbon source."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The fitness-by-condition split can run on existing data, but nitrogen-source growth has not been measured for these strains."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["genotype_to_phenotype_enigma--602fd76d"]
conflicts: ["conflict--cross-tenant-data-bridging--d89b8efa"]
papers: []
builds_on: ["findings/genotype_to_phenotype_enigma--602fd76d", "conflicts/conflict--cross-tenant-data-bridging--d89b8efa"]
projects: ["fw300_metabolic_consistency", "genotype_to_phenotype_enigma"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is tryptophan in Pseudomonas fluorescens a nitrogen source rather than a carbon source?

Tryptophan is produced, has a complete catabolic pathway call and many fitness-relevant genes, and growth on it is predictable in a large model, yet none of 50 P. fluorescens strains used it as a carbon source. Does it serve these strains as a nitrogen source or biosynthetic input instead?

## Hypothesis

Tryptophan-fitness genes in these strains act in nitrogen assimilation or biosynthesis, so strains with the complete pathway grow on tryptophan as sole nitrogen source but not as sole carbon source.

## Why it matters

It would explain why pathway completeness and fitness evidence can agree while carbon growth is absent. That would show what a binary growth prediction really captures and guide how pathway calls are read.

## How to test it

Grow FW300-N2E3 and several of the 50 strains on tryptophan as sole carbon source and as sole nitrogen source. Split the Fitness Browser tryptophan experiments by whether tryptophan was carbon, nitrogen or part of rich medium, and map the genes that clearly affect fitness on tryptophan to catabolic versus biosynthetic pathway steps in Pangenome Collection pathway calls. Compare with the large model's calls for the same strains.

## What would support or refute it

Support: nitrogen-source growth in strains with a complete pathway and tryptophan fitness genes concentrated in nitrogen or biosynthetic steps. Refute: no growth as nitrogen source either, and fitness genes that belong to catabolic steps, which would point to missing transport or regulation.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The fitness-by-condition split can run on existing data, but nitrogen-source growth has not been measured for these strains.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cross-tenant-data-bridging--d89b8efa|Does Genomic and Metabolic Evidence for Tryptophan Imply Measured Growth on It?]]
