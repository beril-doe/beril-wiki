---
type: "Research direction"
description: "Bioleaching genera were not enriched as a group for a broad metal gene signature once genome size was accounted for, though Leptospirillum ranked high on its own. Do these specialists tolerate metals through a few distinct gene families rather than a bigger general repertoire?"
hypothesis: "Families found in some bioleaching genera and rare in matched non-bioleaching relatives will also separate bioleaching genera that were not used to find them, and will do so better than the broad signature score."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pangenome and Fitness Browser data are in the lakehouse. Matched comparison sets need building, and only a few bioleaching genera have pangenomes, which limits held-out rotation."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["metal_fitness_atlas--33814a75", "metal_fitness_atlas--e9d8e5b4", "metal_specificity--1f6b00a4"]
conflicts: []
papers: ["30389769", "12829273", "29150517", "27712915"]
builds_on: ["findings/metal_fitness_atlas--33814a75", "findings/metal_fitness_atlas--e9d8e5b4", "findings/metal_specificity--1f6b00a4"]
projects: ["metal_fitness_atlas", "metal_specificity"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Do extreme metal-tolerant bacteria rely on a few specialist gene families rather than breadth?

Bioleaching genera were not enriched as a group for a broad metal gene signature once genome size was accounted for, though Leptospirillum ranked high on its own. Do these specialists tolerate metals through a few distinct gene families rather than a bigger general repertoire?

## Hypothesis

Families found in some bioleaching genera and rare in matched non-bioleaching relatives will also separate bioleaching genera that were not used to find them, and will do so better than the broad signature score.

## Why it matters

It would show that species-level metal scores built from long gene lists miss real specialists. Searches for metal-tolerant organisms could then target specific families.

## How to test it

In the Pangenome Collection, find gene families enriched in one bioleaching genus (for example Acidithiobacillus) against matched non-bioleaching relatives. Test them only on held-out bioleaching genera (for example Leptospirillum) and their matched relatives, rotating which genus is held out. Use the literature-based bioleaching status of each genus as the label, not any property of the discovery set. Compare with the broad signature score. Check overlap with the 149 conserved but unannotated metal-phenotype families from the Fitness Browser and whether the families carry metal-related annotations.

## What would support or refute it

Support: a small family set found in one genus separates held-out specialists from their relatives better than the broad signature. Refute: families found in one genus fail on held-out genera, so specialists look like other species. That would suggest tolerance relies on regulation or sequence variants invisible to gene content.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pangenome and Fitness Browser data are in the lakehouse. Matched comparison sets need building, and only a few bioleaching genera have pangenomes, which limits held-out rotation.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/metal_fitness_atlas--33814a75|Bioleaching genera not enriched for metal signature after normalization]] (Candidate novel)
- Finding: [[findings/metal_fitness_atlas--e9d8e5b4|Uncharacterized gene families show conserved metal phenotypes across organisms]] (Insufficient literature evidence)
- Finding: [[findings/metal_specificity--1f6b00a4|Novel candidate families are less often metal-specific than annotated ones]] (Insufficient literature evidence)

## Closest published work

- [PMID 30389769](https://pubmed.ncbi.nlm.nih.gov/30389769/) Comparative Genomic Analysis Reveals the Distribution, Organization, and Evolution of Metal Resistance Genes in the Genus Acidithiobacillus.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 29150517](https://pubmed.ncbi.nlm.nih.gov/29150517/) Multi-omics Reveals the Lifestyle of the Acidophilic, Mineral-Oxidizing Model Species Leptospirillum ferriphilumT.
- [PMID 27712915](https://pubmed.ncbi.nlm.nih.gov/27712915/) Comparative genomics unravels metabolic differences at the species and/or strain level and extremely acidic environmental adaptation of ten bacteria belonging to the genus Acidithiobacillus.

PMID 30389769 and PMID 12829273 describe metal-resistance genes in Acidithiobacillus. PMID 29150517 and PMID 27712915 describe acidophile genomes. None tests whether specialist-specific families, rather than repertoire size, separate specialists in held-out genera.
