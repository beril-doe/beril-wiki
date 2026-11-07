---
type: "Research direction"
description: "Binary growth on amino acids, nucleosides and tryptophan was predicted from gene content across genera, yet metals, antibiotics and nitrogen sources were not, and growth rate, lag and yield could not be predicted across genera. Does the prediction also hold among strains within one genus, or does it mostly sort genera?"
hypothesis: "Prediction quality for amino acids and nucleosides falls sharply when only strains of the same genus are compared, because the model relies on gene sets that act as genus proxies. Metals, antibiotics and nitrogen sources depend on single accessory or regulatory differences that gene-content features miss."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "The 46K strain-condition pairs are in hand, but continuous traits could not be predicted across genera and GC content was available for only 32 of 727 genomes."
collections: ["enigma-coral", "kbase-phenotype", "kbase-ke-pangenome"]
findings: ["genotype_to_phenotype_enigma--602fd76d", "genotype_to_phenotype_enigma--ccab2bff", "genotype_to_phenotype_enigma--ad8903f3"]
conflicts: ["conflict--cross-tenant-data-bridging--d89b8efa"]
papers: ["42271456", "29769716", "14688090"]
builds_on: ["findings/genotype_to_phenotype_enigma--602fd76d", "findings/genotype_to_phenotype_enigma--ccab2bff", "findings/genotype_to_phenotype_enigma--ad8903f3", "conflicts/conflict--cross-tenant-data-bridging--d89b8efa"]
projects: ["fw300_metabolic_consistency", "genotype_to_phenotype_enigma"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does gene-content growth prediction work mainly by recognizing which genus a strain belongs to?

Binary growth on amino acids, nucleosides and tryptophan was predicted from gene content across genera, yet metals, antibiotics and nitrogen sources were not, and growth rate, lag and yield could not be predicted across genera. Does the prediction also hold among strains within one genus, or does it mostly sort genera?

## Hypothesis

Prediction quality for amino acids and nucleosides falls sharply when only strains of the same genus are compared, because the model relies on gene sets that act as genus proxies. Metals, antibiotics and nitrogen sources depend on single accessory or regulatory differences that gene-content features miss.

## Why it matters

It would show whether gene content truly predicts phenotype or mostly reflects phylogeny, setting the limit on predicting growth for new isolates within a well-sampled genus.

## How to test it

In the ENIGMA CORAL growth data joined to the Phenotype Collection and Pangenome Collection, compare leave-one-genus-out evaluation with within-genus splits for each condition class, restricted to genera with enough strains that both growers and non-growers occur. Measure what share of the predictive gene groups differ between genera versus vary among strains within a genus. For metal, antibiotic and nitrogen conditions, test whether accessory genes that vary within a genus separate growers from non-growers. Then choose strain pairs of one genus that the model calls differently and test their growth in the lab.

## What would support or refute it

Support: accuracy collapses within genus for amino acids and nucleosides, and the leading features are those that differ between genera. Refutation: within-genus accuracy stays comparable to the across-genus result and leading features vary within genera.

## Data

Approach: analysis then experiment. Readiness: needs compute. The 46K strain-condition pairs are in hand, but continuous traits could not be predicted across genera and GC content was available for only 32 of 727 genomes.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Finding: [[findings/genotype_to_phenotype_enigma--ccab2bff|Continuous growth parameters are not predictable across genera from gene content]] (Insufficient literature evidence)
- Finding: [[findings/genotype_to_phenotype_enigma--ad8903f3|Condition-specific catabolic genes emerge only with large training sets]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cross-tenant-data-bridging--d89b8efa|Does Genomic and Metabolic Evidence for Tryptophan Imply Measured Growth on It?]]

## Closest published work

- [PMID 42271456](https://pubmed.ncbi.nlm.nih.gov/42271456/) Machine learning-based linking of bacterial genomes to optimal growth pH: a foundation for rational microbial engineering.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 14688090](https://pubmed.ncbi.nlm.nih.gov/14688090/) Cross-sectional analysis of clinical and environmental isolates of Pseudomonas aeruginosa: biofilm formation, virulence, and genome diversity.

PMID 42271456 links genomes to optimal growth pH with machine learning and PMID 29769716 maps mutant phenotypes of unknown genes. Neither tests whether prediction survives restriction to strains within one genus.
