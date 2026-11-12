---
type: "Research direction"
description: "Pairs of genes with similar fitness profiles are only weakly linked to co-occurrence across genomes, and module-level field activity was unrelated to conservation in Desulfovibrio vulgaris Hildenborough. Is shared inheritance of functionally coupled genes confined to physically adjacent genes, such as operons and islands?"
hypothesis: "Within fitness modules, members that are adjacent on the chromosome are co-inherited across genomes far more than non-adjacent members, and non-adjacent members show no more co-inheritance than matched random gene sets. This explains why pairwise and module signals look weak when pooled."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Module membership, gene order and genome presence tables are in the lakehouse, but the matched-random comparison across species must be built."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["field_vs_lab_fitness--73215ec1"]
conflicts: ["conflict--cross-tenant-data-bridging--8325c1f4"]
papers: ["38948139", "38323821", "37065130", "36097170"]
builds_on: ["findings/field_vs_lab_fitness--73215ec1", "conflicts/conflict--cross-tenant-data-bridging--8325c1f4"]
projects: ["cofitness_coinheritance", "field_vs_lab_fitness"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Are cofitness modules co-inherited across genomes only when their genes sit next to each other?

Pairs of genes with similar fitness profiles are only weakly linked to co-occurrence across genomes, and module-level field activity was unrelated to conservation in Desulfovibrio vulgaris Hildenborough. Is shared inheritance of functionally coupled genes confined to physically adjacent genes, such as operons and islands?

## Hypothesis

Within fitness modules, members that are adjacent on the chromosome are co-inherited across genomes far more than non-adjacent members, and non-adjacent members show no more co-inheritance than matched random gene sets. This explains why pairwise and module signals look weak when pooled.

## Why it matters

It would explain the disagreement between projects on whether modules rescue weak fitness-to-genome links. It would also tell analysts to define units by genomic adjacency rather than by fitness similarity alone when inferring selection from co-occurrence.

## How to test it

For organisms in the Fitness Browser that have fitness modules, take auxiliary genes only, at below 95% prevalence. Use the Pangenome Collection to compute co-occurrence of module members across genomes of the same species. Split member pairs into adjacent (within a few genes) and non-adjacent. Compare each class with random auxiliary gene sets matched on prevalence and on mean fitness, including the Desulfovibrio vulgaris Hildenborough modules from the field-versus-lab analysis.

## What would support or refute it

Support: adjacent pairs are co-inherited well above matched random sets, while non-adjacent pairs are not. Refute: non-adjacent module members are also co-inherited above matched random sets, which would mean the weak pooled signal is not explained by adjacency, or neither class exceeds the random sets.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Module membership, gene order and genome presence tables are in the lakehouse, but the matched-random comparison across species must be built.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/field_vs_lab_fitness--73215ec1|No significant correlation between module field activity and conservation]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cross-tenant-data-bridging--8325c1f4|Does Module-Level Aggregation Rescue Weak Cross-Tenant Fitness Bridges?]]

## Closest published work

- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.
- [PMID 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in Pseudomonas putida KT2440.
- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 38948139 links cofitness network connectivity to essentiality in open pangenomes and PMID 38323821 derives functional modules from fitness data in Pseudomonas putida. Neither asks whether co-inheritance of module members depends on chromosomal adjacency.
