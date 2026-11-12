---
type: "Research direction"
description: "A deletion screen of Acinetobacter baylyi ADP1 on 8 carbon sources found a continuous gradient with one discrete 24-gene quinate module. Cross-organism analyses of transposon data recover many coherent modules. Is the difference due to the number of conditions, or to the kind of perturbation?"
hypothesis: "If organisms in the Fitness Browser are limited to 8 carbon-source experiments, their module structure will collapse into a continuous gradient like ADP1's. The way ADP1 was perturbed, by single deletion rather than pooled transposon mutants, then matters little."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "The subsampling uses existing Fitness Browser data. The ADP1 pooled library is a new experiment, since ADP1 is absent from that dataset."
collections: ["kescience-fitnessbrowser"]
findings: ["adp1_deletion_phenotypes--86a03233", "adp1_deletion_phenotypes--e7f5d7d3", "adp1_deletion_phenotypes--ec39f324", "fitness_modules--e33de0ee"]
conflicts: ["conflict--fitness-module-detection-sensitivity--ab525b1a"]
papers: ["18319726", "25374488", "29545622", "38323821", "42584158"]
builds_on: ["findings/adp1_deletion_phenotypes--86a03233", "findings/adp1_deletion_phenotypes--e7f5d7d3", "findings/adp1_deletion_phenotypes--ec39f324", "findings/fitness_modules--e33de0ee", "conflicts/conflict--fitness-module-detection-sensitivity--ab525b1a"]
projects: ["adp1_deletion_phenotypes", "fitness_modules"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Is ADP1's smooth phenotype landscape caused by having only eight conditions?

A deletion screen of Acinetobacter baylyi ADP1 on 8 carbon sources found a continuous gradient with one discrete 24-gene quinate module. Cross-organism analyses of transposon data recover many coherent modules. Is the difference due to the number of conditions, or to the kind of perturbation?

## Hypothesis

If organisms in the Fitness Browser are limited to 8 carbon-source experiments, their module structure will collapse into a continuous gradient like ADP1's. The way ADP1 was perturbed, by single deletion rather than pooled transposon mutants, then matters little.

## Why it matters

It would show whether module calls from one dataset reflect biology or experimental design. That tells researchers how many conditions are needed before gene groups can be read as organized units.

## How to test it

For each Fitness Browser organism with many carbon-source experiments, repeatedly draw 8 carbon-source experiments. Group genes with the clustering method the ADP1 study used, and also with independent component analysis (a method that splits a gene-by-condition table into sets of genes whose fitness rises and falls together, called modules). Record how much discrete module structure remains and compare it with ADP1's weak clustering and single small aromatic module. Then build a pooled transposon library of ADP1, grow it on the same 8 carbon sources, and analyze it the same way.

## What would support or refute it

Support: 8-condition subsamples lose most modules and look like ADP1 in both the lakehouse and the pooled ADP1 library. Refute: 8-condition subsamples keep distinct modules, or pooled ADP1 data show modules the deletion screen missed. That would point to perturbation type or ADP1 biology.

## Data

Approach: analysis then experiment. Readiness: needs compute. The subsampling uses existing Fitness Browser data. The ADP1 pooled library is a new experiment, since ADP1 is absent from that dataset.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/adp1_deletion_phenotypes--86a03233|Gene clustering yields no functional enrichment surviving multiple-testing correction]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--e7f5d7d3|Eight conditions provide about five independent phenotypic dimensions]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--ec39f324|Aromatic degradation genes form the only discrete phenotypic module]] (Extends retrieved work)
- Finding: [[findings/fitness_modules--e33de0ee|Nearly all modules show elevated within-module cofitness]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--fitness-module-detection-sensitivity--ab525b1a|Continuous Phenotype Gradient or Discrete Fitness Modules?]]

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 29545622](https://pubmed.ncbi.nlm.nih.gov/29545622/) A comprehensive evaluation of module detection methods for gene expression data.
- [PMID 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in Pseudomonas putida KT2440.
- [PMID 42584158](https://pubmed.ncbi.nlm.nih.gov/42584158/) The iModulon framework: how x-AI reveals microbial regulatory logic.

PMID 18319726 built the ADP1 deletion collection and PMID 38323821 decomposed transposon fitness data for Pseudomonas putida. PMID 29545622 benchmarked module detection methods. None separates condition number from perturbation type.
