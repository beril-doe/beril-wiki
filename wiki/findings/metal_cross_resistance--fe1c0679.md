---
type: "Finding"
description: "The report concludes that the direction of cross-resistance (all positive) is universal, while the quantitative magnitude is moderately conserved across organisms (leave-one-out consensus prediction r = 0.41, Mantel mean r = 0.23)."
finding_id: "metal_cross_resistance--fe1c0679"
result: "inference"
source: "metal_cross_resistance"
quantities: [{"value": "0.41", "what": "leave-one-out consensus prediction r", "unit": "r", "denominator": "", "scope": "across organisms"}, {"value": "0.23", "what": "Mantel mean r", "unit": "r", "denominator": "", "scope": "across organisms"}]
caveat: "Leave-one-out consensus prediction had mean r = 0.41, but only 2/28 organisms reach individual significance, so individual organisms deviate meaningfully from the consensus."
first_added: "2026-10-27"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Cross-resistance direction is universal but its magnitude is only moderately conserved

The report concludes that the direction of cross-resistance (all positive) is universal, while the quantitative magnitude is moderately conserved across organisms (leave-one-out consensus prediction r = 0.41, Mantel mean r = 0.23). [src: metal_cross_resistance]

## Key figures

- **0.41 r**: leave-one-out consensus prediction r (scope across organisms) [src: metal_cross_resistance]
- **0.23 r**: Mantel mean r (scope across organisms) [src: metal_cross_resistance]

## Evidence

> The direction of cross-resistance (all positive) is universal; the quantitative magnitude is moderately conserved across organisms (leave-one-out consensus prediction r = 0.41, Mantel mean r = 0.23). [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

Leave-one-out consensus prediction had mean r = 0.41, but only 2/28 organisms reach individual significance, so individual organisms deviate meaningfully from the consensus. [src: metal_cross_resistance]

> The leave-one-out consensus prediction (mean r = 0.41) shows that a universal cross-resistance map is a useful predictor of individual organism patterns, though only 2/28 organisms reach individual significance — indicating that the consensus captures the average trend but individual organisms have meaningful deviations. [src: metal_cross_resistance]

## Other caveats in this report

- The report proposes an evolutionary model from ancestral general-stress defense through shared metal defense to specialized metal-specific resistance. Ancestry and evolutionary rates are interpretations, not directly demonstrated here. [src: metal_cross_resistance]
- Validation excluded 2 organisms lacking tier data (azobra and BFirm, with <3 metals) and collapsed multiple Fitness Browser strains per species, including 5 P. fluorescens strains sharing one BacDive pool. [src: metal_cross_resistance]
- After matching and strain collapsing, validation had 20 independent species; the report considers this too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive genus-plus-species substring matching can be imprecise for genus-only labels such as Acidovorax sp. [src: metal_cross_resistance]
- The report contrasts its underpowered validation with a prior pangenome-scale analysis of 42K strains (Cohen's d = +1.0) and proposes testing signatures across 27K species using KEGG/PFAM mapping. [src: metal_cross_resistance]
