---
type: "Finding"
description: "The ENIGMA Carbon Census labels 74/83 (89%) compounds organism-dark because the genetic determinants of their utilization are not linkable via the queried KBase Data Lakehouse and curated resources."
finding_id: "enigma_carbon_census_1--602ae5ad"
result: "observation"
source: "enigma_carbon_census_1"
quantities: [{"value": "74/83 (89%)", "what": "compounds that are organism-dark", "unit": "compounds", "denominator": "83 census compounds", "scope": "ENIGMA Carbon Census"}]
caveat: "Organism-dark status means resource-darkness, not absence from science; class-level catabolic literature exists for compounds including monoterpenes and nicotine."
first_added: "2026-11-24"
source_hash: "62204d5c4271f61cef9bd5c3aee8b1410bebd0a60d508276d2875691a7194f49"
---
# Most census compounds are organism-dark, with no linkable genetic determinants

The ENIGMA Carbon Census labels 74/83 (89%) compounds organism-dark because the genetic determinants of their utilization are not linkable via the queried KBase Data Lakehouse and curated resources. [src: enigma_carbon_census_1]

## Key figures

- **74/83 (89%) compounds**: compounds that are organism-dark (denominator 83 census compounds; scope ENIGMA Carbon Census) [src: enigma_carbon_census_1]

## Evidence

> The remaining **74/83 (89%) are organism-dark**: the genetic determinants of their utilization are **not linkable via the queried BERDL and curated resources**. [src: enigma_carbon_census_1]

From the report [[summaries/enigma_carbon_census_1__REPORT]].

## Caveat

Organism-dark status means resource-darkness, not absence from science; class-level catabolic literature exists for compounds including monoterpenes and nicotine. [src: enigma_carbon_census_1]

> This is *resource-darkness*, not proof of absence from science — class-level catabolic literature exists for several of these compounds (e.g. monoterpenes, nicotine), [src: enigma_carbon_census_1]

## Other caveats in this report

- Lauric acid's Fitness Browser organism is a reference bacterium rather than an ENIGMA isolate, so it does not change the ENIGMA-isolate deliverable. [src: enigma_carbon_census_1]
- The ENIGMA Carbon Census literature-rescue channel NB02b returned zero because it used a shallow PubMed-title screen, which the report calls a method floor rather than evidence of absence. [src: enigma_carbon_census_1]
- The ENIGMA Carbon Census mis-scores xanthine as carbon-catabolic because its allowlisted R02107 xanthine-to-urate xanthine oxidase reaction belongs to nitrogen acquisition in the purine pathway, making the effective carbon-callable set 8 rather than 9. [src: enigma_carbon_census_1]
- With only ~9 callables across 83 compounds, the ENIGMA Carbon Census class-gradient design is underpowered and its directional pattern is confounded by KEGG/ModelSEED/genome_depot annotation coverage rather than clean biological degradability. [src: enigma_carbon_census_1]
- The ENIGMA Carbon Census initially used the φ coefficient for co-occurrence, but rarity of most capacities in tens-to-hundreds of 3109 genomes compresses φ toward zero and can hide multiplicative enrichment. [src: enigma_carbon_census_1]
