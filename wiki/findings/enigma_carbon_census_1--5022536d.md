---
type: "Finding"
description: "The report states that the ENIGMA Carbon Census is ~89% organism-dark (74/83 compounds with no isolate utilizer call), and infers that this map of ignorance is biased by chemical class (alkaloids/terpenoids dark, aromatics callable) rather than by sampling source (groundwater 90% vs necromass 88% dark)."
finding_id: "enigma_carbon_census_1--5022536d"
result: "inference"
source: "enigma_carbon_census_1"
quantities: [{"value": "74/83", "what": "compounds with no isolate utilizer call (organism-dark)", "unit": "compounds", "denominator": "83 census compounds", "scope": "ENIGMA Carbon Census"}, {"value": "~89%", "what": "organism-dark fraction", "unit": "", "denominator": "83 compounds", "scope": ""}, {"value": "90%", "what": "dark fraction, groundwater compounds", "unit": "", "denominator": "", "scope": "groundwater source"}, {"value": "88%", "what": "dark fraction, necromass compounds", "unit": "", "denominator": "", "scope": "necromass source"}]
caveat: "With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the directional pattern is confounded with annotation coverage rather than a clean biological degradability gradient."
first_added: "2026-10-27"
source_hash: "62204d5c4271f61cef9bd5c3aee8b1410bebd0a60d508276d2875691a7194f49"
---
# Most census compounds lack utilizer calls, biased by chemical class

The report states that the ENIGMA Carbon Census is ~89% organism-dark (74/83 compounds with no isolate utilizer call), and infers that this map of ignorance is biased by chemical class (alkaloids/terpenoids dark, aromatics callable) rather than by sampling source (groundwater 90% vs necromass 88% dark). [src: enigma_carbon_census_1]

## Key figures

- **74/83 compounds**: compounds with no isolate utilizer call (organism-dark) (denominator 83 census compounds; scope ENIGMA Carbon Census) [src: enigma_carbon_census_1]
- **~89%**: organism-dark fraction (denominator 83 compounds) [src: enigma_carbon_census_1]
- **90%**: dark fraction, groundwater compounds (scope groundwater source) [src: enigma_carbon_census_1]
- **88%**: dark fraction, necromass compounds (scope necromass source) [src: enigma_carbon_census_1]

## Evidence

> The ENIGMA Carbon Census is **~89% organism-dark** (74/83 compounds with no isolate utilizer call) — the actionable product of a knowledge census can be the map of ignorance, and that map is biased exactly by chemical class (alkaloids/terpenoids dark, aromatics callable), not by sampling source (groundwater 90% vs necromass 88% dark). [src: enigma_carbon_census_1]

From the report [[summaries/enigma_carbon_census_1__REPORT]].

## Caveat

With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the directional pattern is confounded with annotation coverage rather than a clean biological degradability gradient. [src: enigma_carbon_census_1]

> With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the directional pattern is further **confounded with annotation coverage** (which classes KEGG/ModelSEED/genome_depot annotate) rather than a clean biological degradability gradient. [src: enigma_carbon_census_1]

## Other caveats in this report

- Lauric acid's measured-fitness organism is a reference bacterium, not an ENIGMA isolate. [src: enigma_carbon_census_1]
- Resource darkness is not evidence of biological absence; a shallow PubMed title screen yielded zero literature rescues. [src: enigma_carbon_census_1]
- Xanthine's R02107 reaction reflects purine nitrogen acquisition, not carbon catabolism; the effective carbon-callable count is 8 rather than 9. [src: enigma_carbon_census_1]
- Because rare capacities compress the φ coefficient, the reanalysis used Haldane-corrected odds ratios with 95% confidence intervals and Jaccard indices from saved 2×2 counts. [src: enigma_carbon_census_1]
- The 34 all-high-certainty terephthalic-acid calls reflect a single-reaction-signature artifact, not stronger evidence. [src: enigma_carbon_census_1]
