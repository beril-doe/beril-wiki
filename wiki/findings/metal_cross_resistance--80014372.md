---
type: "Finding"
description: "The metal-label permutation test was non-significant (p = 0.42) because all metal pairs are positive, so shuffling labels does not change the mean."
finding_id: "metal_cross_resistance--80014372"
result: "null result"
source: "metal_cross_resistance"
quantities: [{"value": "p = 0.42", "what": "metal-label permutation test p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The non-significance arises because all metal pairs are positive, so shuffling labels does not change the mean when correlations are uniformly positive."
first_added: "2026-11-24"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Metal-label permutation test does not detect pair-specific cross-resistance structure

The metal-label permutation test was non-significant (p = 0.42) because all metal pairs are positive, so shuffling labels does not change the mean. [src: metal_cross_resistance]

## Key figures

- **p = 0.42**: metal-label permutation test p-value [src: metal_cross_resistance]

## Evidence

> The metal-label permutation test (p = 0.42) is non-significant because ALL metal pairs are positive; shuffling labels doesn't change the mean when correlations are uniformly positive. [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

The non-significance arises because all metal pairs are positive, so shuffling labels does not change the mean when correlations are uniformly positive. [src: metal_cross_resistance]

> The metal-label permutation test (p = 0.42) is non-significant because ALL metal pairs are positive; shuffling labels doesn't change the mean when correlations are uniformly positive. [src: metal_cross_resistance]

## Other caveats in this report

- Only 2/28 organisms reached individual significance in leave-one-out consensus prediction, indicating that individual organisms meaningfully deviate from the average trend. [src: metal_cross_resistance]
- After matching and collapsing, the BacDive validation had an effective sample size of 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive matching used genus+species substring search, which is imprecise for genus-only identifications such as Acidovorax sp.; the report cautions against treating these fuzzy matches as precise. [src: metal_cross_resistance]
- The report states that a proper H3 test would require applying the Metal Fitness Atlas KEGG/PFAM mapping approach to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]
- Different metal concentrations across experiments could affect the report's cross-resistance estimates through dose-response effects. [src: metal_cross_resistance]
