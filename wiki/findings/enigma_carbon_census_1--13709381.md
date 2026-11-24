---
type: "Finding"
description: "The dark fraction is nearly identical across sources (groundwater 53/59 = 90%, necromass 21/24 = 88%), so the report interprets darkness as a chemical-class property, not a sampling-source artifact."
finding_id: "enigma_carbon_census_1--13709381"
result: "inference"
source: "enigma_carbon_census_1"
quantities: [{"value": "53/59 = 90%", "what": "dark fraction of groundwater compounds", "unit": "compounds", "denominator": "59 groundwater compounds", "scope": "ENIGMA Carbon Census"}, {"value": "21/24 = 88%", "what": "dark fraction of necromass compounds", "unit": "compounds", "denominator": "24 necromass compounds", "scope": "ENIGMA Carbon Census"}]
caveat: "With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the pattern is confounded with annotation coverage."
first_added: "2026-11-24"
source_hash: "62204d5c4271f61cef9bd5c3aee8b1410bebd0a60d508276d2875691a7194f49"
---
# Darkness tracks chemical class, not sampling source

The dark fraction is nearly identical across sources (groundwater 53/59 = 90%, necromass 21/24 = 88%), so the report interprets darkness as a chemical-class property, not a sampling-source artifact. [src: enigma_carbon_census_1]

## Key figures

- **53/59 = 90% compounds**: dark fraction of groundwater compounds (denominator 59 groundwater compounds; scope ENIGMA Carbon Census) [src: enigma_carbon_census_1]
- **21/24 = 88% compounds**: dark fraction of necromass compounds (denominator 24 necromass compounds; scope ENIGMA Carbon Census) [src: enigma_carbon_census_1]

## Evidence

> The dark fraction is nearly identical across sources (groundwater 53/59 = 90%, necromass 21/24 = 88%), so darkness is a chemical-class property, not a sampling-source artifact. [src: enigma_carbon_census_1]

From the report [[summaries/enigma_carbon_census_1__REPORT]].

## Caveat

With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the pattern is confounded with annotation coverage. [src: enigma_carbon_census_1]

> With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the directional pattern is further **confounded with annotation coverage** (which classes KEGG/ModelSEED/genome_depot annotate) rather than a clean biological degradability gradient. [src: enigma_carbon_census_1]

## Other caveats in this report

- Lauric acid's Fitness Browser organism is a reference bacterium rather than an ENIGMA isolate, so it does not change the ENIGMA-isolate deliverable. [src: enigma_carbon_census_1]
- Organism-dark status in the ENIGMA Carbon Census means resource-darkness, not absence from science; class-level catabolic literature exists for compounds including monoterpenes and nicotine. [src: enigma_carbon_census_1]
- The ENIGMA Carbon Census literature-rescue channel NB02b returned zero because it used a shallow PubMed-title screen, which the report calls a method floor rather than evidence of absence. [src: enigma_carbon_census_1]
- The ENIGMA Carbon Census mis-scores xanthine as carbon-catabolic because its allowlisted R02107 xanthine-to-urate xanthine oxidase reaction belongs to nitrogen acquisition in the purine pathway, making the effective carbon-callable set 8 rather than 9. [src: enigma_carbon_census_1]
- The ENIGMA Carbon Census initially used the φ coefficient for co-occurrence, but rarity of most capacities in tens-to-hundreds of 3109 genomes compresses φ toward zero and can hide multiplicative enrichment. [src: enigma_carbon_census_1]
