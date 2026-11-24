---
type: "Finding"
description: "Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), 98.1% of gene-level fitness correlations are positive (311/317)."
finding_id: "metal_cross_resistance--1dc0eaa0"
result: "observation"
source: "metal_cross_resistance"
quantities: [{"value": "98.1%", "what": "share of gene-level fitness correlations that are positive", "unit": "percent", "denominator": "317 organism-metal pair observations", "scope": "28 organisms, 85 unique metal pairs"}, {"value": "311/317", "what": "positive correlations out of all observations", "unit": "", "denominator": "", "scope": ""}]
caveat: "All tested metal pairs are positive, so without non-metal stress controls the report cannot distinguish universal cross-resistance from all metals causing general stress."
first_added: "2026-11-24"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Gene-level metal fitness correlations are almost universally positive across diverse bacteria

Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), 98.1% of gene-level fitness correlations are positive (311/317). [src: metal_cross_resistance]

## Key figures

- **98.1%**: share of gene-level fitness correlations that are positive (denominator 317 organism-metal pair observations; scope 28 organisms, 85 unique metal pairs) [src: metal_cross_resistance]
- **311/317**: positive correlations out of all observations [src: metal_cross_resistance]

## Evidence

> Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), **98.1% of gene-level fitness correlations are positive** (311/317) and **99.1% are statistically significant** (p < 0.05). [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

All tested metal pairs are positive, so without non-metal stress controls the report cannot distinguish universal cross-resistance from all metals causing general stress. [src: metal_cross_resistance]

> - **No negative controls**: All tested metal pairs are positive. We cannot distinguish "universal cross-resistance" from "all metals cause general stress" without non-metal stress controls (partially addressed by the counter_ion_effects project). [src: metal_cross_resistance]

## Other caveats in this report

- The report attributes the non-significant metal-label permutation test to uniformly positive metal-pair correlations, for which shuffling labels does not change the mean. [src: metal_cross_resistance]
- Only 2/28 organisms reached individual significance in leave-one-out consensus prediction, indicating that individual organisms meaningfully deviate from the average trend. [src: metal_cross_resistance]
- After matching and collapsing, the BacDive validation had an effective sample size of 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive matching used genus+species substring search, which is imprecise for genus-only identifications such as Acidovorax sp.; the report cautions against treating these fuzzy matches as precise. [src: metal_cross_resistance]
- The report states that a proper H3 test would require applying the Metal Fitness Atlas KEGG/PFAM mapping approach to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]
