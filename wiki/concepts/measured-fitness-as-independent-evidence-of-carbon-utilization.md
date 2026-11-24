---
type: "Concept"
description: "Covers using measured carbon-source fitness experiments in reference organisms to call compound utilization independently of genome-annotation filters, and its limits for target isolates."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Measured fitness as independent evidence of carbon utilization

The evidence is a single case from one report. The measurement comes from a reference bacterium, so it adds no information about the ENIGMA target isolates. [src: enigma_carbon_census_1]

## How the census defines "callable"

The census calls a compound callable if it has an ENIGMA-isolate utilizer call or a Tier-1 measured RB-TnSeq (random barcode transposon sequencing) carbon-source fitness experiment. [src: enigma_carbon_census_1] The Tier-1 channel comes from carbon-source experiments in the kescience_fitnessbrowser data, i.e. the [[entities/fitness-browser]]. [src: enigma_carbon_census_1] See [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls]] for that filter.

## The lauric acid case

Lauric acid is the ninth callable compound. It has a Tier-1 measured carbon-source growth experiment in the Fitness Browser, and an InChIKey re-match in notebook NB02c confirmed the match structurally. [src: enigma_carbon_census_1] The match file holds one such structural match, for lauric acid. [src: enigma_carbon_census_1] The re-match goes from compound name to PubChem to InChIKey, and the report labels it review I1. [src: enigma_carbon_census_1] The census classes lauric acid as a fatty acid callable on a measured_fitness basis only. [src: enigma_carbon_census_1]

## Limits for target isolates

The Fitness Browser organism for lauric acid is a reference bacterium, not an ENIGMA isolate. The ENIGMA-isolate deliverable is therefore unchanged. [src: enigma_carbon_census_1]

- The compound has 0 strains, 0 high-certainty strains, 0 genera and 0 field genera, and no top field prevalence. [src: enigma_carbon_census_1]
- It has no ENIGMA-isolate prediction rows and is absent from deliverable (a). [src: enigma_carbon_census_1]
- It is necromass-sourced but has no isolate utilizers and no field data, so it adds nothing to the source contrast. [src: enigma_carbon_census_1] See [[concepts/confounding-of-compound-source-with-chemical-class]].
- It contributes no ENIGMA-isolate phylogenetic prediction, so it sits outside both arms. [src: enigma_carbon_census_1]
- Adding it brings Fatty acids coverage to 1/10. The census verdict on a class gradient stays unchanged. [src: enigma_carbon_census_1]

For related coverage effects, see [[concepts/annotation-coverage-bias-in-chemical-class-callability]] and the [[summaries/enigma_carbon_census_1__REPORT|report summary]].

## Open Directions

- Test whether ENIGMA isolates grow on lauric acid. This would turn the reference-organism call into an isolate-level call.
- Run the InChIKey re-match across all Tier-1 Fitness Browser carbon-source experiments for other compound classes. The census found only one match, so this would show whether lauric acid is unusual.
- Compare measured-fitness calls with annotation-filtered calls for the same compounds in shared reference organisms. This would check how independent the two routes are.
