---
type: "Finding"
description: "NB14 found that excluding the top-3 genome-rich species per compartment reduced the original NB04 Phase 1 25-marker PERMANOVA R\u00b2 from 0.527 to 0.072, an 86% loss."
finding_id: "plant_microbiome_ecotypes--8fc0d70a"
result: "correction"
source: "plant_microbiome_ecotypes"
quantities: [{"value": "0.527", "what": "original PERMANOVA R\u00b2 on Phase 1 25-marker panel", "unit": "R\u00b2", "denominator": "", "scope": "NB04 plant compartments"}, {"value": "0.072", "what": "R\u00b2 after excluding top-3 genome-rich species per compartment", "unit": "R\u00b2", "denominator": "", "scope": "NB14 sensitivity analysis"}, {"value": "86%", "what": "loss in R\u00b2", "unit": "", "denominator": "", "scope": ""}]
caveat: "Most of the original 0.527 was a taxonomic-sampling artifact of a few genome-rich species rather than a community-wide signal."
first_added: "2026-11-24"
source_hash: "ab4bafa20bb607a1edf87a293d67885cd96017817bfabdbff2c19bac9dc95272"
---
# Compartment effect on functional profiles was largely a sampling artifact

NB14 found that excluding the top-3 genome-rich species per compartment reduced the original NB04 Phase 1 25-marker PERMANOVA R² from 0.527 to 0.072, an 86% loss. [src: plant_microbiome_ecotypes]

## Key figures

- **0.527 R²**: original PERMANOVA R² on Phase 1 25-marker panel (scope NB04 plant compartments) [src: plant_microbiome_ecotypes]
- **0.072 R²**: R² after excluding top-3 genome-rich species per compartment (scope NB14 sensitivity analysis) [src: plant_microbiome_ecotypes]
- **86%**: loss in R² [src: plant_microbiome_ecotypes]

## Evidence

> The original NB04 PERMANOVA reported R² = 0.527 for compartment on the Phase 1 25-marker panel; NB14's sensitivity analysis showed R² drops to 0.072 when the top-3 genome-rich species per compartment are excluded (an 86% loss). [src: plant_microbiome_ecotypes]

From the report [[summaries/plant_microbiome_ecotypes__REPORT]].

## Caveat

Most of the original 0.527 was a taxonomic-sampling artifact of a few genome-rich species rather than a community-wide signal. [src: plant_microbiome_ecotypes]

> **most of the original 0.527 was a taxonomic-sampling artifact** of a few genome-rich species rather than a community-wide signal. [src: plant_microbiome_ecotypes]

## Other caveats in this report

- The original NB04 PERMANOVA on the Phase 1 25-marker panel reported R² = 0.527 (pseudo-F = 235.1, p = 0.001), but NB14's exclude-top-3-species sensitivity left residual R² of only 0.072 after removal of dominant rhizobial / Pseudomonas clades. [src: plant_microbiome_ecotypes]
- The report states that the revised compartment decomposition does not contradict per-function enrichments, but corrects the inflated headline magnitude of multivariate R². [src: plant_microbiome_ecotypes]
- The Phase 1 NB06 complementarity result of Cohen's d = −7.54 was largely a formula error because the mean difference was divided by the SD of permutation means rather than the raw pair-level SD. [src: plant_microbiome_ecotypes]
- Of the apparent 20× reduction in the early Phase 2b complementarity effect estimate, ~90% was attributed to formula correction and ~10% to aggregation correction. [src: plant_microbiome_ecotypes]
- Attenuation from Fisher OR to phylogenetically controlled OR indicates partial phylogenetic confounding because plant-associated species cluster taxonomically, although the report states that substantial ecological signal persists after correction. [src: plant_microbiome_ecotypes]
