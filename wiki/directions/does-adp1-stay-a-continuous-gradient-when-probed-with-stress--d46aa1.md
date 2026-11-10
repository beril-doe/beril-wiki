---
type: "Research direction"
description: "ADP1 deletion phenotypes on 8 carbon sources form a continuous gradient with one discrete module, yet transposon data from many other bacteria resolve numerous stable modules. Is the gradient caused by testing only carbon sources, by deleting single genes, or by ADP1's own interconnected metabolism?"
hypothesis: "Measuring the ADP1 deletion collection under a broad panel of stress and nitrogen-source conditions will reveal several new discrete modules beyond the quinate aromatic-degradation module. Chemical perturbation across the same carbon sources will not produce more discrete modules than gene deletion does."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The decisive step is new growth measurements on the ADP1 deletion collection and wild-type chemical exposures; only the reference comparison uses existing data."
collections: ["kescience-fitnessbrowser"]
findings: ["adp1_deletion_phenotypes--86a03233", "adp1_deletion_phenotypes--e7f5d7d3", "fitness_modules--c9df945b"]
conflicts: ["conflict--fitness-module-detection-sensitivity--ab525b1a"]
papers: ["18319726", "25374488", "38323821", "25968644", "29545622"]
builds_on: ["findings/adp1_deletion_phenotypes--86a03233", "findings/adp1_deletion_phenotypes--e7f5d7d3", "findings/fitness_modules--c9df945b", "conflicts/conflict--fitness-module-detection-sensitivity--ab525b1a"]
projects: ["adp1_deletion_phenotypes", "fitness_modules"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Does ADP1 stay a continuous gradient when probed with stress, nitrogen and chemical perturbations?

ADP1 deletion phenotypes on 8 carbon sources form a continuous gradient with one discrete module, yet transposon data from many other bacteria resolve numerous stable modules. Is the gradient caused by testing only carbon sources, by deleting single genes, or by ADP1's own interconnected metabolism?

## Hypothesis

Measuring the ADP1 deletion collection under a broad panel of stress and nitrogen-source conditions will reveal several new discrete modules beyond the quinate aromatic-degradation module. Chemical perturbation across the same carbon sources will not produce more discrete modules than gene deletion does.

## Why it matters

If new condition classes expose hidden modules, a continuous landscape reflects a narrow assay panel and not intrinsic biology. If modules stay absent, perturbation type or ADP1 metabolism sets the architecture, which changes how module calls from any one screen should be read.

## How to test it

Grow the ADP1 deletion collection under a new panel of oxidative, osmotic, metal and iron-limited stresses plus several nitrogen sources, alongside the original carbon sources. Cluster the new profiles with the same hierarchical method used before and with independent component analysis, and count discrete modules and their pathway content. In parallel, expose wild-type ADP1 to chemical inhibitors across the same carbon sources and compare how discrete the resulting structure is with that from deletions. Compare against module structure in Fitness Browser organisms as a reference.

## What would support or refute it

Support: new conditions yield several discrete, pathway-coherent modules, and chemical perturbation is no more modular than deletion. Refute: ADP1 stays continuous across many added conditions (pointing to organism biology), or chemical perturbation gives clearly sharper modules (pointing to perturbation type).

## Data

Approach: experiment. Readiness: needs new measurements. The decisive step is new growth measurements on the ADP1 deletion collection and wild-type chemical exposures; only the reference comparison uses existing data.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/adp1_deletion_phenotypes--86a03233|Gene clustering yields no functional enrichment surviving multiple-testing correction]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--e7f5d7d3|Eight conditions provide about five independent phenotypic dimensions]] (Insufficient literature evidence)
- Finding: [[findings/fitness_modules--c9df945b|Module families recur across organisms, reaching a pan-bacterial span]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--fitness-module-detection-sensitivity--ab525b1a|Continuous Phenotype Gradient or Discrete Fitness Modules?]]

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in Pseudomonas putida KT2440.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 29545622](https://pubmed.ncbi.nlm.nih.gov/29545622/) A comprehensive evaluation of module detection methods for gene expression data.

PMID 18319726 built the ADP1 deletion collection and PMID 38323821 found modules in Pseudomonas putida fitness data. Neither measures ADP1 deletions beyond carbon sources or compares deletion with chemical perturbation in the same organism.
