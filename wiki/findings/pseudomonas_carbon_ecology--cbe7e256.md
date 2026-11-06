---
type: "Finding"
description: "A Random Forest classifier trained on 4 environment classes (soil, freshwater, plant_surface, rhizosphere; 51 species total) achieved balanced accuracy of 0.408 +/- 0.169, above the 0.250 chance level."
finding_id: "pseudomonas_carbon_ecology--cbe7e256"
result: "observation"
source: "pseudomonas_carbon_ecology"
quantities: [{"value": "0.408 +/- 0.169", "what": "Balanced accuracy of Random Forest", "unit": "", "denominator": "", "scope": "4 environment classes, 51 species"}, {"value": "0.250", "what": "Chance level balanced accuracy", "unit": "", "denominator": "", "scope": ""}]
caveat: "The moderate accuracy likely reflects small sample sizes per class, overlap between related environment types such as soil vs. rhizosphere, and the coarse resolution of 62 GapMind pathways."
first_added: "2026-10-27"
source_hash: "9a0d1678e23b48d6e7732b56ad5ca0452fed1ff9fcf5c9c5e8e9b23315c58260"
---
# Random Forest predicts environment class from carbon pathways above chance

A Random Forest classifier trained on 4 environment classes (soil, freshwater, plant_surface, rhizosphere; 51 species total) achieved balanced accuracy of 0.408 +/- 0.169, above the 0.250 chance level. [src: pseudomonas_carbon_ecology]

## Key figures

- **0.408 +/- 0.169**: Balanced accuracy of Random Forest (scope 4 environment classes, 51 species) [src: pseudomonas_carbon_ecology]
- **0.250**: Chance level balanced accuracy [src: pseudomonas_carbon_ecology]

## Evidence

> A Random Forest classifier trained on 4 environment classes (soil, freshwater, plant_surface, rhizosphere; 51 species total) achieved **balanced accuracy of 0.408 +/- 0.169**, substantially above the 0.250 chance level. [src: pseudomonas_carbon_ecology]

From the report [[summaries/pseudomonas_carbon_ecology__REPORT]].

## Caveat

The moderate accuracy likely reflects small sample sizes per class, overlap between related environment types such as soil vs. rhizosphere, and the coarse resolution of 62 GapMind pathways. [src: pseudomonas_carbon_ecology]

> The moderate accuracy likely reflects: (1) small sample sizes per class, (2) overlap between related environment types (e.g., soil vs. rhizosphere), and (3) the relatively coarse resolution of 62 GapMind pathways. [src: pseudomonas_carbon_ecology]

## Other caveats in this report

- The principal pathway-profile axis separates subgenera, while lifestyle categories overlap within Pseudomonas_E; ecological interpretation is therefore limited by phylogenetic separation. [src: pseudomonas_carbon_ecology]
- Only 64.2% of genomes (8,171/12,732) had classifiable isolation sources; categories were assigned by keywords. [src: pseudomonas_carbon_ecology]
- The report contrasts within-infection metabolic loss with a hypothesis of ancestral lineage-level streamlining; the timing remains an interpretation. [src: pseudomonas_carbon_ecology]
- The report notes strain-level hydrocarbon-gene variation and hypothesizes that 62 GapMind pathways may be too coarse for fine-grained environment prediction. [src: pseudomonas_carbon_ecology]
- Release from selection for plant-associated metabolism during an animal-host transition is an interpretation of the pathway-loss pattern, not a directly tested transition. [src: pseudomonas_carbon_ecology]
