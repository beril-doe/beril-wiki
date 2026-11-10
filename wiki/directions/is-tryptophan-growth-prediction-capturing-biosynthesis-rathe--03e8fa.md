---
type: "Research direction"
description: "Why is growth on tryptophan well predicted from gene content when 50 P. fluorescens strains did not use it as a carbon source?"
hypothesis: "The tryptophan model leans on biosynthesis and uptake genes, so it predicts growth in tryptophan-limited media, not catabolism. Models fitted only on carbon-source labels would lose this accuracy."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The trained models and growth labels exist but feature attribution must be rerun by condition label."
collections: ["enigma-coral", "kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["genotype_to_phenotype_enigma--602fd76d"]
conflicts: ["conflict--cross-tenant-data-bridging--d89b8efa"]
papers: []
builds_on: ["findings/genotype_to_phenotype_enigma--602fd76d", "conflicts/conflict--cross-tenant-data-bridging--d89b8efa"]
projects: ["fw300_metabolic_consistency", "genotype_to_phenotype_enigma"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is tryptophan growth prediction capturing biosynthesis rather than use as a carbon source?

Why is growth on tryptophan well predicted from gene content when 50 P. fluorescens strains did not use it as a carbon source?

## Hypothesis

The tryptophan model leans on biosynthesis and uptake genes, so it predicts growth in tryptophan-limited media, not catabolism. Models fitted only on carbon-source labels would lose this accuracy.

## Why it matters

It would show that high prediction accuracy can reflect the wrong biology and tell users which conditions gene-content models can be trusted for.

## How to test it

List the gene families that drive the tryptophan model and classify them as biosynthesis, transport or degradation. Retrain using only carbon-source tryptophan labels and compare with the nitrogen-source and rich-medium labels. Score the 50 P. fluorescens strains with each model. Split the Fitness Browser tryptophan genes by whether tryptophan was the carbon or nitrogen source.

## What would support or refute it

Supported if biosynthesis genes dominate and the carbon-only model fails. Refuted if degradation genes dominate and predictions still disagree with the 0 of 50 strains.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The trained models and growth labels exist but feature attribution must be rerun by condition label.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cross-tenant-data-bridging--d89b8efa|Does Genomic and Metabolic Evidence for Tryptophan Imply Measured Growth on It?]]
