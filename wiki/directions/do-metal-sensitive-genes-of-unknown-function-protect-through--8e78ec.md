---
type: "Research direction"
description: "Among novel metal-candidate gene families, 45.6% are metal-specific versus 58.2% of annotated ones, and a module-level search found no metal-specific modules. Do these candidates act by binding metals, or by maintaining general envelope or stress tolerance that metals happen to test?"
hypothesis: "Candidates that lose fitness under many metals and under non-metal membrane or oxidative stresses act through general envelope integrity, while the smaller metal-specific set carries metal-binding features."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Profiles exist in the lakehouse, but testing mechanism needs structure prediction and new growth assays on mutants."
collections: ["kescience-fitnessbrowser", "kbase-uniprot"]
findings: ["metal_specificity--1f6b00a4", "metal_specificity--83d867cf", "metal_specificity--0f40573a"]
conflicts: ["conflict--metal-cross-resistance--59068bf5"]
papers: ["29769716", "30729256", "22125499", "25906431"]
builds_on: ["findings/metal_specificity--1f6b00a4", "findings/metal_specificity--83d867cf", "findings/metal_specificity--0f40573a", "conflicts/conflict--metal-cross-resistance--59068bf5"]
projects: ["metal_cross_resistance", "metal_specificity"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do metal-sensitive genes of unknown function protect through metal binding or envelope integrity?

Among novel metal-candidate gene families, 45.6% are metal-specific versus 58.2% of annotated ones, and a module-level search found no metal-specific modules. Do these candidates act by binding metals, or by maintaining general envelope or stress tolerance that metals happen to test?

## Hypothesis

Candidates that lose fitness under many metals and under non-metal membrane or oxidative stresses act through general envelope integrity, while the smaller metal-specific set carries metal-binding features.

## Why it matters

It would show what the unannotated metal-fitness genes do and whether a metal-specific category is real. The module result alone cannot decide this, because the module scoring used a normalization that limited detection when metal experiments were few.

## How to test it

Step 1, lakehouse: in the Fitness Browser, classify candidate families by fitness profile across metal and non-metal experiments, favouring organisms with many experiments to reduce the extra apparent pleiotropy in deeply profiled organisms. Repeat the module search with scoring that does not depend on metal experiments being a large share of each organism's data, and predict structure and metal-binding sites for each class. Step 2, experiment: knock down representatives in Desulfovibrio vulgaris Hildenborough or Bacteroides thetaiotaomicron and assay growth with metals, detergents and oxidants.

## What would support or refute it

Support: general-profile candidates are sensitive to envelope stressors, and specific candidates show binding sites and metal-selective growth defects. Refute: general-profile candidates show no envelope sensitivity, or specific ones lack binding features.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Profiles exist in the lakehouse, but testing mechanism needs structure prediction and new growth assays on mutants.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]

## Builds on

- Finding: [[findings/metal_specificity--1f6b00a4|Novel candidate families are less often metal-specific than annotated ones]] (Insufficient literature evidence)
- Finding: [[findings/metal_specificity--83d867cf|Module-level analysis found no metal-specific modules]] (Insufficient literature evidence)
- Finding: [[findings/metal_specificity--0f40573a|Just over half of metal-important genes are metal-specific]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--metal-cross-resistance--59068bf5|Universal Positive Metal Cross-Resistance: Metal-Specific Mechanism or General-Stress Response?]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 30729256](https://pubmed.ncbi.nlm.nih.gov/30729256/) Gene function and expression regulation of RuvRCAB in bacterial Cr(VI), As(III), Sb(III), and Cd(II) resistance.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.
- [PMID 25906431](https://pubmed.ncbi.nlm.nih.gov/25906431/) Interplay between copper and zinc homeostasis through the transcriptional regulator Zur in Enterococcus faecalis.

PMID 29769716 assigns phenotypes to unknown genes without separating metal-specific from general sensitivity; PMID 25906431 explores one metal-regulator interplay in a single organism.
