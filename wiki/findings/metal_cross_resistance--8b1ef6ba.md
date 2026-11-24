---
type: "Finding"
description: "Fe-Zn cross-resistance was unexpectedly strong (r = 0.61, n = 6), which the report suggests likely reflects shared disruption of iron-sulfur cluster proteins."
finding_id: "metal_cross_resistance--8b1ef6ba"
result: "inference"
source: "metal_cross_resistance"
quantities: [{"value": "r = 0.61", "what": "Fe-Zn cross-resistance correlation", "unit": "", "denominator": "", "scope": "6 organisms"}, {"value": "n = 6", "what": "number of organisms with the Fe-Zn pair", "unit": "", "denominator": "", "scope": ""}]
caveat: "Organisms range from 3 to 112 metal experiments, affecting the reliability of per-organism matrices."
first_added: "2026-11-24"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Iron-zinc cross-resistance is unexpectedly strong, possibly via iron-sulfur cluster disruption

Fe-Zn cross-resistance was unexpectedly strong (r = 0.61, n = 6), which the report suggests likely reflects shared disruption of iron-sulfur cluster proteins. [src: metal_cross_resistance]

## Key figures

- **r = 0.61**: Fe-Zn cross-resistance correlation (scope 6 organisms) [src: metal_cross_resistance]
- **n = 6**: number of organisms with the Fe-Zn pair [src: metal_cross_resistance]

## Evidence

> - **Fe-Zn** (r = 0.61, n = 6): Unexpectedly strong; likely reflects shared disruption of iron-sulfur cluster proteins [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

Organisms range from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [src: metal_cross_resistance]

> - **Unequal experiment counts**: Organisms range from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [src: metal_cross_resistance]

## Other caveats in this report

- The report attributes the non-significant metal-label permutation test to uniformly positive metal-pair correlations, for which shuffling labels does not change the mean. [src: metal_cross_resistance]
- Only 2/28 organisms reached individual significance in leave-one-out consensus prediction, indicating that individual organisms meaningfully deviate from the average trend. [src: metal_cross_resistance]
- After matching and collapsing, the BacDive validation had an effective sample size of 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive matching used genus+species substring search, which is imprecise for genus-only identifications such as Acidovorax sp.; the report cautions against treating these fuzzy matches as precise. [src: metal_cross_resistance]
- The report states that a proper H3 test would require applying the Metal Fitness Atlas KEGG/PFAM mapping approach to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]
