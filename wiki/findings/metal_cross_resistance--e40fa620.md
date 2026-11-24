---
type: "Finding"
description: "The fully core gradient across general-stress, metal-shared and metal-specific tiers of metal-important genes was 57.2% \u2192 50.4% \u2192 45.7%, an 11.5 percentage point spread."
finding_id: "metal_cross_resistance--e40fa620"
result: "observation"
source: "metal_cross_resistance"
quantities: [{"value": "57.2% \u2192 50.4% \u2192 45.7%", "what": "fully core fraction by tier: general stress, metal-shared, metal-specific", "unit": "percent", "denominator": "", "scope": ""}, {"value": "11.5 percentage point", "what": "spread between general-stress and metal-specific tiers", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 28 organisms are not phylogenetically independent, and formal methods such as PGLS or independent contrasts would strengthen the conservation claim."
first_added: "2026-11-24"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Metal-specific genes are less pangenome-core than general-stress genes

The fully core gradient across general-stress, metal-shared and metal-specific tiers of metal-important genes was 57.2% → 50.4% → 45.7%, an 11.5 percentage point spread. [src: metal_cross_resistance]

## Key figures

- **57.2% → 50.4% → 45.7%**: fully core fraction by tier: general stress, metal-shared, metal-specific [src: metal_cross_resistance]
- **11.5 percentage point**: spread between general-stress and metal-specific tiers [src: metal_cross_resistance]

## Evidence

> The "fully core" gradient (57.2% → 50.4% → 45.7%) is particularly clear — an 11.5 percentage point spread. [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

The 28 organisms are not phylogenetically independent, and formal methods such as PGLS or independent contrasts would strengthen the conservation claim. [src: metal_cross_resistance]

> - **Phylogenetic non-independence**: The 28 organisms are not phylogenetically independent. Formal phylogenetic comparative methods (PGLS, independent contrasts) would strengthen the conservation claim. [src: metal_cross_resistance]

## Other caveats in this report

- The report attributes the non-significant metal-label permutation test to uniformly positive metal-pair correlations, for which shuffling labels does not change the mean. [src: metal_cross_resistance]
- Only 2/28 organisms reached individual significance in leave-one-out consensus prediction, indicating that individual organisms meaningfully deviate from the average trend. [src: metal_cross_resistance]
- After matching and collapsing, the BacDive validation had an effective sample size of 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive matching used genus+species substring search, which is imprecise for genus-only identifications such as Acidovorax sp.; the report cautions against treating these fuzzy matches as precise. [src: metal_cross_resistance]
- The report states that a proper H3 test would require applying the Metal Fitness Atlas KEGG/PFAM mapping approach to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]
