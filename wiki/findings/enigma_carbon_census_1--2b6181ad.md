---
type: "Finding"
description: "The pre-registered null of uniform coverage across classes is not rejected by a \u03c7\u00b2 test on the 8 enigma_isolate_call callables by class: \u03c7\u00b2=5.07, p=0.53 (df=6)."
finding_id: "enigma_carbon_census_1--2b6181ad"
result: "null result"
source: "enigma_carbon_census_1"
quantities: [{"value": "\u03c7\u00b2=5.07", "what": "chi-square statistic", "unit": "", "denominator": "", "scope": "8 enigma_isolate_call callables by class"}, {"value": "p=0.53", "what": "p-value", "unit": "", "denominator": "", "scope": "df=6"}]
caveat: "With only ~9 callables across 83 compounds the design is underpowered to detect a class gradient, and the pattern is confounded with annotation coverage."
first_added: "2026-11-24"
source_hash: "62204d5c4271f61cef9bd5c3aee8b1410bebd0a60d508276d2875691a7194f49"
---
# Uniform class coverage null is not rejected for callable compounds

The pre-registered null of uniform coverage across classes is not rejected by a χ² test on the 8 enigma_isolate_call callables by class: χ²=5.07, p=0.53 (df=6). [src: enigma_carbon_census_1]

## Key figures

- **χ²=5.07**: chi-square statistic (scope 8 enigma_isolate_call callables by class) [src: enigma_carbon_census_1]
- **p=0.53**: p-value (scope df=6) [src: enigma_carbon_census_1]

## Evidence

> But the **pre-registered null (uniform coverage across classes) is not rejected**: a χ² test on the 8 `enigma_isolate_call` callables by class (Shikimates 5/25, Alkaloids 2/26, Terpenoids 1/17, Fatty acids 0/10, Polyketides 0/2, AA/Peptides 0/2, mixed 0/1) gives **χ²=5.07, p=0.53 (df=6)**; [src: enigma_carbon_census_1]

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
