---
type: "Finding"
description: "The report interprets that most marker-level plant-association signals are genus-scale rather than species-scale, because marker presence does not reliably distinguish plant-associated from non-plant species within genera."
finding_id: "plant_microbiome_ecotypes--9a9aeb0d"
result: "inference"
source: "plant_microbiome_ecotypes"
quantities: []
caveat: "The within-genus shuffle used n = 200 permutations, which is under-resolved for p \u2264 0.005 and makes the T3SS result marginal."
first_added: "2026-11-24"
source_hash: "ab4bafa20bb607a1edf87a293d67885cd96017817bfabdbff2c19bac9dc95272"
---
# Most marker plant-association signals are genus-scale, not species-scale

The report interprets that most marker-level plant-association signals are genus-scale rather than species-scale, because marker presence does not reliably distinguish plant-associated from non-plant species within genera. [src: plant_microbiome_ecotypes]

## Evidence

> The honest reading is that **most of the marker-level plant-association signals in this project are genus-scale, not species-scale** — plant adaptation is largely a property of which genera happen to be plant-associated, and within those genera, marker presence does not reliably distinguish plant-associated from non-plant species. [src: plant_microbiome_ecotypes]

From the report [[summaries/plant_microbiome_ecotypes__REPORT]].

## Caveat

The within-genus shuffle used n = 200 permutations, which is under-resolved for p ≤ 0.005 and makes the T3SS result marginal. [src: plant_microbiome_ecotypes]

> **Caveats**: n = 200 permutations is under-resolved for p ≤ 0.005 (T3SS is therefore marginal); [src: plant_microbiome_ecotypes]

## Other caveats in this report

- The original NB04 PERMANOVA on the Phase 1 25-marker panel reported R² = 0.527 (pseudo-F = 235.1, p = 0.001), but NB14's exclude-top-3-species sensitivity left residual R² of only 0.072 after removal of dominant rhizobial / Pseudomonas clades. [src: plant_microbiome_ecotypes]
- Most of the original compartment R² of 0.527 was a taxonomic-sampling artifact of a few genome-rich species rather than a community-wide signal. [src: plant_microbiome_ecotypes]
- The report states that the revised compartment decomposition does not contradict per-function enrichments, but corrects the inflated headline magnitude of multivariate R². [src: plant_microbiome_ecotypes]
- The Phase 1 NB06 complementarity result of Cohen's d = −7.54 was largely a formula error because the mean difference was divided by the SD of permutation means rather than the raw pair-level SD. [src: plant_microbiome_ecotypes]
- Of the apparent 20× reduction in the early Phase 2b complementarity effect estimate, ~90% was attributed to formula correction and ~10% to aggregation correction. [src: plant_microbiome_ecotypes]
