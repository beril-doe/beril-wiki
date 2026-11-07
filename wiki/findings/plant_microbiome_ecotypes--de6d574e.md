---
type: "Finding"
description: "A sensitivity analysis excluding the top-3 species per compartment reduced the PERMANOVA R\u00b2 from 0.527 to 0.072 (still significant, p = 0.001), correcting the original compartment effect size."
finding_id: "plant_microbiome_ecotypes--de6d574e"
result: "correction"
source: "plant_microbiome_ecotypes"
quantities: [{"value": "0.527", "what": "original PERMANOVA R\u00b2 for compartment", "unit": "R\u00b2", "denominator": "", "scope": ""}, {"value": "0.072", "what": "PERMANOVA R\u00b2 after excluding top-3 species per compartment", "unit": "R\u00b2", "denominator": "", "scope": "p = 0.001"}]
caveat: "PERMDISP detected significant dispersion heterogeneity between cohorts (H=33.12, p=3.0e-7), so the PERMANOVA effect size should be interpreted as an upper bound."
first_added: "2026-10-27"
source_hash: "ab4bafa20bb607a1edf87a293d67885cd96017817bfabdbff2c19bac9dc95272"
---
# Compartment PERMANOVA effect was largely driven by a few dominant species

A sensitivity analysis excluding the top-3 species per compartment reduced the PERMANOVA R² from 0.527 to 0.072 (still significant, p = 0.001), correcting the original compartment effect size. [src: plant_microbiome_ecotypes]

## Key figures

- **0.527 R²**: original PERMANOVA R² for compartment [src: plant_microbiome_ecotypes]
- **0.072 R²**: PERMANOVA R² after excluding top-3 species per compartment (scope p = 0.001) [src: plant_microbiome_ecotypes]

## Evidence

> Two of the three RESEARCH_PLAN.md safeguards were executed in NB14: (a) sensitivity excluding top-3 species per compartment reduced PERMANOVA R² from 0.527 to 0.072 (still significant, p = 0.001); (b) within-genus label shuffling found only 3/15 markers (nitrogen fixation, ACC deaminase, T3SS) survive the strict permutation null. [src: plant_microbiome_ecotypes]

From the report [[summaries/plant_microbiome_ecotypes__REPORT]].

## Caveat

PERMDISP detected significant dispersion heterogeneity between cohorts (H=33.12, p=3.0e-7), so the PERMANOVA effect size should be interpreted as an upper bound. [src: plant_microbiome_ecotypes]

> 9. **Multivariate dispersion**: PERMDISP testing (NB08) revealed significant dispersion heterogeneity between cohorts (H=33.12, p=3.0e-7), meaning the PERMANOVA R²=0.53 may partly reflect variance differences rather than pure location shifts. The compartment effect is still supported by the Fisher enrichment tests (69/96 significant), but the PERMANOVA effect size should be interpreted as an upper bound. [src: plant_microbiome_ecotypes]

## Other caveats in this report

- The original compartment PERMANOVA R² = 0.527 was largely a taxonomic-sampling artifact: excluding three dominant species reduced it to 0.072, although the reported per-marker enrichments persisted. The stated compartment counts do not sum to 1,136 and should not be silently reconciled. [src: plant_microbiome_ecotypes]
- The proposed purifying-selection explanation is an interpretation of mixed proxy evidence, not a direct demonstration of selection. [src: plant_microbiome_ecotypes]
- Co-occurring plant-associated genera show a small redundancy signal. The earlier extreme Cohen’s d = −7.54 largely resulted from using the SD of permutation means instead of the raw pair-level SD; corrected analyses yield about −0.4. [src: plant_microbiome_ecotypes]
- The reduction in COG3569 odds ratio from 8.92 to 6.01 indicates partial phylogenetic confounding. [src: plant_microbiome_ecotypes]
- NB02 classified 15,474/25,660 species (60.3%) as dual-nature by binary marker presence; NB07's weighted composite scheme classified 25.2% as dual-nature. The passage establishes different classification definitions but does not give an NB07 denominator. [src: plant_microbiome_ecotypes]
