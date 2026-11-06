---
type: "Finding"
description: "The fully-core proportion declines from general-stress genes (57.2%) to metal-shared genes important for \u22652 metals (50.4%) to metal-specific genes important for exactly 1 metal (45.7%), an 11.5 percentage point spread."
finding_id: "metal_cross_resistance--fdba2abe"
result: "observation"
source: "metal_cross_resistance"
quantities: [{"value": "57.2%", "what": "general-stress genes that are fully core", "unit": "%", "denominator": "general-stress genes", "scope": ""}, {"value": "50.4%", "what": "metal-shared genes that are fully core", "unit": "%", "denominator": "metal-shared genes", "scope": ""}, {"value": "45.7%", "what": "metal-specific genes that are fully core", "unit": "%", "denominator": "metal-specific genes", "scope": ""}, {"value": "11.5", "what": "spread in fully-core proportion", "unit": "percentage points", "denominator": "", "scope": "across the three tiers"}]
caveat: "The 28 organisms are not phylogenetically independent, and formal phylogenetic comparative methods (PGLS, independent contrasts) were not applied to strengthen the conservation claim."
first_added: "2026-10-27"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Pangenome conservation falls from general-stress to metal-shared to metal-specific genes

The fully-core proportion declines from general-stress genes (57.2%) to metal-shared genes important for ≥2 metals (50.4%) to metal-specific genes important for exactly 1 metal (45.7%), an 11.5 percentage point spread. [src: metal_cross_resistance]

## Key figures

- **57.2%**: general-stress genes that are fully core (denominator general-stress genes) [src: metal_cross_resistance]
- **50.4%**: metal-shared genes that are fully core (denominator metal-shared genes) [src: metal_cross_resistance]
- **45.7%**: metal-specific genes that are fully core (denominator metal-specific genes) [src: metal_cross_resistance]
- **11.5 percentage points**: spread in fully-core proportion (scope across the three tiers) [src: metal_cross_resistance]

## Evidence

> The predicted gradient holds: general stress genes (pleiotropic, important across many conditions) are the most conserved in the pangenome, metal-shared genes (cross-resistance drivers, important for ≥2 metals) are intermediate, and metal-specific genes (important for exactly 1 metal) are least conserved. The "fully core" gradient (57.2% → 50.4% → 45.7%) is particularly clear — an 11.5 percentage point spread. [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

The 28 organisms are not phylogenetically independent, and formal phylogenetic comparative methods (PGLS, independent contrasts) were not applied to strengthen the conservation claim. [src: metal_cross_resistance]

> - **Phylogenetic non-independence**: The 28 organisms are not phylogenetically independent. Formal phylogenetic comparative methods (PGLS, independent contrasts) would strengthen the conservation claim. [src: metal_cross_resistance]

## Other caveats in this report

- Leave-one-out consensus prediction had mean r = 0.41, but only 2/28 organisms reached individual significance. [src: metal_cross_resistance]
- The report proposes an evolutionary model from ancestral general-stress defense through shared metal defense to specialized metal-specific resistance. Ancestry and evolutionary rates are interpretations, not directly demonstrated here. [src: metal_cross_resistance]
- Validation excluded 2 organisms lacking tier data (azobra and BFirm, with <3 metals) and collapsed multiple Fitness Browser strains per species, including 5 P. fluorescens strains sharing one BacDive pool. [src: metal_cross_resistance]
- After matching and strain collapsing, validation had 20 independent species; the report considers this too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive genus-plus-species substring matching can be imprecise for genus-only labels such as Acidovorax sp. [src: metal_cross_resistance]
