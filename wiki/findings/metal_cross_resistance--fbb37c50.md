---
type: "Finding"
description: "Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), 98.1% of gene-level fitness correlations are positive (311/317) and 99.1% are statistically significant (p < 0.05); all 15 metal pairs tested in \u22655 organisms show >90% sign consistency, with no metal pair systematically negative in any organism."
finding_id: "metal_cross_resistance--fbb37c50"
result: "observation"
source: "metal_cross_resistance"
quantities: [{"value": "98.1%", "what": "gene-level fitness correlations that are positive", "unit": "%", "denominator": "317 organism-metal pair observations", "scope": "28 organisms, 85 unique metal pairs"}, {"value": "311/317", "what": "positive correlations", "unit": "", "denominator": "317 organism-metal pair observations", "scope": "28 organisms"}, {"value": "99.1%", "what": "correlations statistically significant", "unit": "%", "denominator": "317 organism-metal pair observations", "scope": "28 organisms, 85 unique metal pairs; p < 0.05"}, {"value": ">90%", "what": "sign consistency for all 15 metal pairs tested in \u22655 organisms", "unit": "", "denominator": "", "scope": "pairs tested in \u22655 organisms"}]
caveat: "All tested metal pairs are positive, and without non-metal stress controls the analysis cannot distinguish universal metal cross-resistance from general stress shared by all metals."
first_added: "2026-10-27"
source_hash: "500dd3cfb440724464d76e3acbbeb03b0f8408de0fccbf2e8a4f53a05e43721b"
---
# Gene-level metal cross-resistance is almost uniformly positive across diverse bacteria

Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), 98.1% of gene-level fitness correlations are positive (311/317) and 99.1% are statistically significant (p < 0.05); all 15 metal pairs tested in ≥5 organisms show >90% sign consistency, with no metal pair systematically negative in any organism. [src: metal_cross_resistance]

## Key figures

- **98.1%**: gene-level fitness correlations that are positive (denominator 317 organism-metal pair observations; scope 28 organisms, 85 unique metal pairs) [src: metal_cross_resistance]
- **311/317**: positive correlations (denominator 317 organism-metal pair observations; scope 28 organisms) [src: metal_cross_resistance]
- **99.1%**: correlations statistically significant (denominator 317 organism-metal pair observations; scope 28 organisms, 85 unique metal pairs; p < 0.05) [src: metal_cross_resistance]
- **>90%**: sign consistency for all 15 metal pairs tested in ≥5 organisms (scope pairs tested in ≥5 organisms) [src: metal_cross_resistance]

## Evidence

> Across 317 organism-metal pair observations (28 organisms, 85 unique metal pairs), **98.1% of gene-level fitness correlations are positive** (311/317) and **99.1% are statistically significant** (p < 0.05). All 15 metal pairs tested in ≥5 organisms show >90% sign consistency — no metal pair has systematically negative cross-resistance in any organism. [src: metal_cross_resistance]

From the report [[summaries/metal_cross_resistance__REPORT]].

## Caveat

All tested metal pairs are positive, and without non-metal stress controls the analysis cannot distinguish universal metal cross-resistance from general stress shared by all metals. [src: metal_cross_resistance]

> - **No negative controls**: All tested metal pairs are positive. We cannot distinguish "universal cross-resistance" from "all metals cause general stress" without non-metal stress controls (partially addressed by the counter_ion_effects project). [src: metal_cross_resistance]

## Other caveats in this report

- Leave-one-out consensus prediction had mean r = 0.41, but only 2/28 organisms reached individual significance. [src: metal_cross_resistance]
- The report proposes an evolutionary model from ancestral general-stress defense through shared metal defense to specialized metal-specific resistance. Ancestry and evolutionary rates are interpretations, not directly demonstrated here. [src: metal_cross_resistance]
- Validation excluded 2 organisms lacking tier data (azobra and BFirm, with <3 metals) and collapsed multiple Fitness Browser strains per species, including 5 P. fluorescens strains sharing one BacDive pool. [src: metal_cross_resistance]
- After matching and strain collapsing, validation had 20 independent species; the report considers this too small for a meaningful correlation test. [src: metal_cross_resistance]
- BacDive genus-plus-species substring matching can be imprecise for genus-only labels such as Acidovorax sp. [src: metal_cross_resistance]
