---
type: "Finding"
description: "The direction of cross-resistance (all positive) is universal, while its quantitative magnitude is moderately conserved across organisms (leave-one-out consensus prediction r = 0.41, Mantel mean r = 0.23)."
finding_id: "metal_cross_resistance--fe1c0679"
result: "observation"
source: "metal_cross_resistance"
quantities: [{"value": "r = 0.41", "what": "leave-one-out consensus prediction correlation", "unit": "", "denominator": "", "scope": ""}, {"value": "r = 0.23", "what": "Mantel mean correlation between organisms", "unit": "", "denominator": "", "scope": ""}]
caveat: "Only 2/28 organisms reach individual significance in leave-one-out prediction, so individual organisms meaningfully deviate from the average trend."
first_added: "2026-11-24"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Cross-resistance direction is universal but magnitude only moderately conserved

The direction of cross-resistance (all positive) is universal, while its quantitative magnitude is moderately conserved across organisms (leave-one-out consensus prediction r = 0.41, Mantel mean r = 0.23). [src: metal_cross_resistance]

## Key figures

- **r = 0.41**: leave-one-out consensus prediction correlation [src: metal_cross_resistance]
- **r = 0.23**: Mantel mean correlation between organisms [src: metal_cross_resistance]

## Evidence

> The direction of cross-resistance (all positive) is universal; the quantitative magnitude is moderately conserved across organisms (leave-one-out consensus prediction r = 0.41, Mantel mean r = 0.23). [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

Only 2/28 organisms reach individual significance in leave-one-out prediction, so individual organisms meaningfully deviate from the average trend. [src: metal_cross_resistance]

> The leave-one-out consensus prediction (mean r = 0.41) shows that a universal cross-resistance map is a useful predictor of individual organism patterns, though only 2/28 organisms reach individual significance — indicating that the consensus captures the average trend but individual organisms have meaningful deviations. [src: metal_cross_resistance]

## Other caveats in this report

- The report attributes the non-significant metal-label permutation test to uniformly positive metal-pair correlations, for which shuffling labels does not change the mean. [src: metal_cross_resistance]
- After matching and collapsing, the BacDive validation had an effective sample size of 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive matching used genus+species substring search, which is imprecise for genus-only identifications such as Acidovorax sp.; the report cautions against treating these fuzzy matches as precise. [src: metal_cross_resistance]
- The report states that a proper H3 test would require applying the Metal Fitness Atlas KEGG/PFAM mapping approach to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]
- Different metal concentrations across experiments could affect the report's cross-resistance estimates through dose-response effects. [src: metal_cross_resistance]
