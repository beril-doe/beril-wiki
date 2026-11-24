---
type: "Finding"
description: "Multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at the Fitness Browser species scale (Spearman rho ~ -0.02, p > 0.8)."
finding_id: "metal_cross_resistance--109ca8e4"
result: "null result"
source: "metal_cross_resistance"
quantities: [{"value": "rho ~ -0.02", "what": "Spearman correlation of tolerance score with metal-environment isolation", "unit": "", "denominator": "", "scope": ""}, {"value": "p > 0.8", "what": "significance of the correlation", "unit": "", "denominator": "", "scope": ""}]
caveat: "After matching and collapsing, the effective sample size is 20 independent species, far too small for a meaningful correlation test."
first_added: "2026-11-24"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Multi-metal tolerance scores do not track BacDive metal-environment isolation

Multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at the Fitness Browser species scale (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance]

## Key figures

- **rho ~ -0.02**: Spearman correlation of tolerance score with metal-environment isolation [src: metal_cross_resistance]
- **p > 0.8**: significance of the correlation [src: metal_cross_resistance]

## Evidence

> The multi-metal tolerance scores do not correlate with BacDive isolation from metal environments at the FB species scale (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

After matching and collapsing, the effective sample size is 20 independent species, far too small for a meaningful correlation test. [src: metal_cross_resistance]

> After matching and collapsing, the effective sample size is **20 independent species** — far too small for a meaningful correlation test. [src: metal_cross_resistance]

## Other caveats in this report

- The report attributes the non-significant metal-label permutation test to uniformly positive metal-pair correlations, for which shuffling labels does not change the mean. [src: metal_cross_resistance]
- Only 2/28 organisms reached individual significance in leave-one-out consensus prediction, indicating that individual organisms meaningfully deviate from the average trend. [src: metal_cross_resistance]
- BacDive matching used genus+species substring search, which is imprecise for genus-only identifications such as Acidovorax sp.; the report cautions against treating these fuzzy matches as precise. [src: metal_cross_resistance]
- The report states that a proper H3 test would require applying the Metal Fitness Atlas KEGG/PFAM mapping approach to cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]
- Different metal concentrations across experiments could affect the report's cross-resistance estimates through dose-response effects. [src: metal_cross_resistance]
