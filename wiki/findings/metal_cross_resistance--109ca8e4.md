---
type: "Finding"
description: "At the Fitness Browser species scale, multi-metal tolerance scores did not correlate with BacDive isolation from metal environments (Spearman rho ~ -0.02, p > 0.8)."
finding_id: "metal_cross_resistance--109ca8e4"
result: "null result"
source: "metal_cross_resistance"
quantities: [{"value": "~ -0.02", "what": "Spearman rho between multi-metal tolerance and BacDive metal-environment isolation", "unit": "rho", "denominator": "", "scope": "Fitness Browser species scale"}, {"value": "> 0.8", "what": "p-value of the correlation", "unit": "", "denominator": "", "scope": "Fitness Browser species scale"}]
caveat: "After matching and collapsing strains, the effective sample size is 20 independent species, which the report considers far too small for a meaningful correlation test."
first_added: "2026-10-27"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Multi-metal tolerance scores do not track BacDive metal-environment isolation

At the Fitness Browser species scale, multi-metal tolerance scores did not correlate with BacDive isolation from metal environments (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance]

## Key figures

- **~ -0.02 rho**: Spearman rho between multi-metal tolerance and BacDive metal-environment isolation (scope Fitness Browser species scale) [src: metal_cross_resistance]
- **> 0.8**: p-value of the correlation (scope Fitness Browser species scale) [src: metal_cross_resistance]

## Evidence

> The multi-metal tolerance scores do not correlate with BacDive isolation from metal environments at the FB species scale (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

After matching and collapsing strains, the effective sample size is 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance]

> After matching and collapsing, the effective sample size is **20 independent species** — far too small for a meaningful correlation test. [src: metal_cross_resistance]

## Other caveats in this report

- Leave-one-out consensus prediction had mean r = 0.41, but only 2/28 organisms reached individual significance. [src: metal_cross_resistance]
- The report proposes an evolutionary model from ancestral general-stress defense through shared metal defense to specialized metal-specific resistance. Ancestry and evolutionary rates are interpretations, not directly demonstrated here. [src: metal_cross_resistance]
- Validation excluded 2 organisms lacking tier data (azobra and BFirm, with <3 metals) and collapsed multiple Fitness Browser strains per species, including 5 P. fluorescens strains sharing one BacDive pool. [src: metal_cross_resistance]
- BacDive genus-plus-species substring matching can be imprecise for genus-only labels such as Acidovorax sp. [src: metal_cross_resistance]
- The report contrasts its underpowered validation with a prior pangenome-scale analysis of 42K strains (Cohen's d = +1.0) and proposes testing signatures across 27K species using KEGG/PFAM mapping. [src: metal_cross_resistance]
