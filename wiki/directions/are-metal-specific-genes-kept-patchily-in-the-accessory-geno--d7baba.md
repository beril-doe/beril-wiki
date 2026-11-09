---
type: "Research direction"
description: "In two separate analyses, genes needed only under metals were less often core than genes needed under many stresses. The analyses used different gene sets and definitions, so their core fractions are not directly comparable, but both point the same way. Is the patchy presence of metal-specific genes maintained by isolation from metal-rich habitats within species?"
hypothesis: "Within a species, genomes isolated from metal-rich or contaminated habitats carry metal-specific genes more often than genomes from clean habitats, and more strongly than they carry general-stress genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene classes and pangenome presence exist, but most Fitness Browser species have few genomes, habitat labels must be harmonised, and the earlier core fractions rest on differing gene sets, so only well-sampled species can be tested."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["metal_specificity--fed6dcbd", "metal_cross_resistance--fdba2abe", "metal_specificity--1f6b00a4"]
conflicts: ["conflict--composite-resistance-score-limitations--ba02b0ad"]
papers: ["42262111", "38948139", "29769716", "40302248"]
builds_on: ["findings/metal_specificity--fed6dcbd", "findings/metal_cross_resistance--fdba2abe", "findings/metal_specificity--1f6b00a4", "conflicts/conflict--composite-resistance-score-limitations--ba02b0ad"]
projects: ["metal_cross_resistance", "metal_fitness_atlas", "metal_specificity"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Are metal-specific genes kept patchily in the accessory genome by local metal exposure?

In two separate analyses, genes needed only under metals were less often core than genes needed under many stresses. The analyses used different gene sets and definitions, so their core fractions are not directly comparable, but both point the same way. Is the patchy presence of metal-specific genes maintained by isolation from metal-rich habitats within species?

## Hypothesis

Within a species, genomes isolated from metal-rich or contaminated habitats carry metal-specific genes more often than genomes from clean habitats, and more strongly than they carry general-stress genes.

## Why it matters

Lab fitness shows which genes matter under metals but not why they are absent from many genomes. A habitat link would show that metal-specific resistance is maintained by local selection. No habitat link would point to drift or neutral loss and would weaken an ecological reading of the lower core share.

## How to test it

For Fitness Browser organisms with deep pangenomes, classify genes as metal-specific, shared across metals, or generally important from knockout fitness, using one fixed definition of core for all classes. For each gene, record presence across genomes of the same species in the Pangenome Collection. Label each genome's habitat from NMDC BioSamples isolation-source metadata. Test, within species, whether presence of metal-specific genes is associated with contaminated or metal-rich isolation sources, relative to general-stress genes. Restrict to species with enough genomes, since most Fitness Browser species have few (median 9).

## What would support or refute it

Support: metal-specific genes are more often present in genomes from metal-rich habitats, and more so than general-stress genes. Refutation: presence is unrelated to isolation habitat, or equally related for both gene classes.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene classes and pangenome presence exist, but most Fitness Browser species have few genomes, habitat labels must be harmonised, and the earlier core fractions rest on differing gene sets, so only well-sampled species can be tested.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/metal_specificity--fed6dcbd|Metal-specific genes are less core-enriched than general-sick genes]] (Insufficient literature evidence)
- Finding: [[findings/metal_cross_resistance--fdba2abe|Pangenome conservation falls from general-stress to metal-shared to metal-specific genes]] (Insufficient literature evidence)
- Finding: [[findings/metal_specificity--1f6b00a4|Novel candidate families are less often metal-specific than annotated ones]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--composite-resistance-score-limitations--ba02b0ad|Is the core-genome enrichment of metal-fitness genes one estimate or several incomparable ones?]]

## Closest published work

- [PMID 42262111](https://pubmed.ncbi.nlm.nih.gov/42262111/) Systemic trade-offs between core and accessory genomes govern stress adaptation in Rhodococcus erythropolis.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 40302248](https://pubmed.ncbi.nlm.nih.gov/40302248/) High-Throughput Tn-Seq Screens Identify Both Known and Novel Pseudomonas putida KT2440 Genes Involved in Metal Tolerance.

PMID 42262111 reports trade-offs between core and accessory genomes under stress in one species, and PMID 38948139 links fitness genes to core status in another; neither asks whether metal-specific genes follow isolation habitat within species.
