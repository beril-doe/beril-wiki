---
type: "Finding"
description: "NB12 originally reported no significant within-species plant-associated subclade segregation in 5 species tested (0/5 significant), but this null result was caused by a genome-ID format mismatch."
finding_id: "plant_microbiome_ecotypes--a3526004"
result: "null result"
source: "plant_microbiome_ecotypes"
quantities: [{"value": "0/5", "what": "significant species originally reported", "unit": "", "denominator": "5 species", "scope": "NB12"}]
caveat: "Only 18 of 65 candidate plant-associated species had any pairwise phylogenetic-distance data in the KBase Data Lakehouse table kbase_ke_pangenome.phylogenetic_tree_distance_pairs."
first_added: "2026-11-24"
source_hash: "ab4bafa20bb607a1edf87a293d67885cd96017817bfabdbff2c19bac9dc95272"
---
# Earlier null for subclade segregation came from ID mismatch

NB12 originally reported no significant within-species plant-associated subclade segregation in 5 species tested (0/5 significant), but this null result was caused by a genome-ID format mismatch. [src: plant_microbiome_ecotypes]

## Key figures

- **0/5**: significant species originally reported (denominator 5 species; scope NB12) [src: plant_microbiome_ecotypes]

## Evidence

> NB12's null result for H7 (5 species tested, 0/5 significant) was caused by a **genome-ID format mismatch** [src: plant_microbiome_ecotypes]

From the report [[summaries/plant_microbiome_ecotypes__REPORT]].

## Caveat

Only 18 of 65 candidate plant-associated species had any pairwise phylogenetic-distance data in the KBase Data Lakehouse table kbase_ke_pangenome.phylogenetic_tree_distance_pairs. [src: plant_microbiome_ecotypes]

> **Phylogenetic-tree coverage**: only **18 of 65 candidate species** had any pairwise phylogenetic-distance data in `kbase_ke_pangenome.phylogenetic_tree_distance_pairs`. [src: plant_microbiome_ecotypes]

## Other caveats in this report

- The original NB04 PERMANOVA on the Phase 1 25-marker panel reported R² = 0.527 (pseudo-F = 235.1, p = 0.001), but NB14's exclude-top-3-species sensitivity left residual R² of only 0.072 after removal of dominant rhizobial / Pseudomonas clades. [src: plant_microbiome_ecotypes]
- Most of the original compartment R² of 0.527 was a taxonomic-sampling artifact of a few genome-rich species rather than a community-wide signal. [src: plant_microbiome_ecotypes]
- The report states that the revised compartment decomposition does not contradict per-function enrichments, but corrects the inflated headline magnitude of multivariate R². [src: plant_microbiome_ecotypes]
- The Phase 1 NB06 complementarity result of Cohen's d = −7.54 was largely a formula error because the mean difference was divided by the SD of permutation means rather than the raw pair-level SD. [src: plant_microbiome_ecotypes]
- Of the apparent 20× reduction in the early Phase 2b complementarity effect estimate, ~90% was attributed to formula correction and ~10% to aggregation correction. [src: plant_microbiome_ecotypes]
