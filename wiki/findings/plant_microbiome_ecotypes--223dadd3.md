---
type: "Finding"
description: "In a within-genus label permutation, only 3 of 15 testable markers survive: nitrogen fixation (perm p < 0.001), ACC deaminase (perm p < 0.001), and T3SS (perm p = 0.005)."
finding_id: "plant_microbiome_ecotypes--223dadd3"
result: "observation"
source: "plant_microbiome_ecotypes"
quantities: [{"value": "3 of 15", "what": "testable markers surviving within-genus label permutation", "unit": "markers", "denominator": "15 testable markers", "scope": "within-genus permutation"}, {"value": "p = 0.005", "what": "permutation p-value for T3SS", "unit": "", "denominator": "", "scope": "T3SS"}]
caveat: "The test used only n = 200 permutations, which is under-resolved for p \u2264 0.005, and applied no multiple-testing correction across 15 markers; Bonferroni \u03b1 = 0.0033 would demote T3SS while N-fix and ACC deaminase remain significant."
first_added: "2026-10-27"
source_hash: "ab4bafa20bb607a1edf87a293d67885cd96017817bfabdbff2c19bac9dc95272"
---
# Only three plant markers survive strict within-genus permutation

In a within-genus label permutation, only 3 of 15 testable markers survive: nitrogen fixation (perm p < 0.001), ACC deaminase (perm p < 0.001), and T3SS (perm p = 0.005). [src: plant_microbiome_ecotypes]

## Key figures

- **3 of 15 markers**: testable markers surviving within-genus label permutation (denominator 15 testable markers; scope within-genus permutation) [src: plant_microbiome_ecotypes]
- **p = 0.005**: permutation p-value for T3SS (scope T3SS) [src: plant_microbiome_ecotypes]

## Evidence

> **Only 3 of 15 testable markers survive**: nitrogen fixation (perm p < 0.001), ACC deaminase (perm p < 0.001), and T3SS (perm p = 0.005). [src: plant_microbiome_ecotypes]

From the report [[summaries/plant_microbiome_ecotypes__REPORT]].

## Caveat

The test used only n = 200 permutations, which is under-resolved for p ≤ 0.005, and applied no multiple-testing correction across 15 markers; Bonferroni α = 0.0033 would demote T3SS while N-fix and ACC deaminase remain significant. [src: plant_microbiome_ecotypes]

> **Caveats**: n = 200 permutations is under-resolved for p ≤ 0.005 (T3SS is therefore marginal); no multiple-testing correction was applied across 15 markers (Bonferroni α = 0.0033 would demote T3SS; N-fix and ACC deaminase remain sig). [src: plant_microbiome_ecotypes]

## Other caveats in this report

- The original compartment PERMANOVA R² = 0.527 was largely a taxonomic-sampling artifact: excluding three dominant species reduced it to 0.072, although the reported per-marker enrichments persisted. The stated compartment counts do not sum to 1,136 and should not be silently reconciled. [src: plant_microbiome_ecotypes]
- The proposed purifying-selection explanation is an interpretation of mixed proxy evidence, not a direct demonstration of selection. [src: plant_microbiome_ecotypes]
- Co-occurring plant-associated genera show a small redundancy signal. The earlier extreme Cohen’s d = −7.54 largely resulted from using the SD of permutation means instead of the raw pair-level SD; corrected analyses yield about −0.4. [src: plant_microbiome_ecotypes]
- The reduction in COG3569 odds ratio from 8.92 to 6.01 indicates partial phylogenetic confounding. [src: plant_microbiome_ecotypes]
- NB02 classified 15,474/25,660 species (60.3%) as dual-nature by binary marker presence; NB07's weighted composite scheme classified 25.2% as dual-nature. The passage establishes different classification definitions but does not give an NB07 denominator. [src: plant_microbiome_ecotypes]
