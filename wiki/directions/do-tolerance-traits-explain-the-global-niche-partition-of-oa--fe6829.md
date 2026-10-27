---
type: "Research direction"
description: "Is the global separation (1.35 pH units more acidic, 6.9 \u00b0C warmer) of the Rhodanobacter-Ralstonia-Dyella cluster from the Brevundimonas-Caulobacter-Sphingomonas cluster explained by differences in physiological pH and temperature tolerance?"
hypothesis: "The partition is physiological: representative isolates differ in pH and temperature growth ranges in line with global occupancy. After conditioning on pH and temperature, compositionally aware co-occurrence analysis will show little residual exclusion between clusters."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The co-occurrence reanalysis is new compute on existing data, but the decisive isolate growth tests need new measurements."
collections: ["enigma-coral"]
findings: ["genotype_to_phenotype_enigma--a6ede42b"]
conflicts: []
papers: ["38366921", "40118314", "30481288", "39501158"]
builds_on: ["findings/genotype_to_phenotype_enigma--a6ede42b"]
projects: ["genotype_to_phenotype_enigma"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Do tolerance traits explain the global niche partition of Oak Ridge genera?

Is the global separation (1.35 pH units more acidic, 6.9 °C warmer) of the Rhodanobacter-Ralstonia-Dyella cluster from the Brevundimonas-Caulobacter-Sphingomonas cluster explained by differences in physiological pH and temperature tolerance?

## Hypothesis

The partition is physiological: representative isolates differ in pH and temperature growth ranges in line with global occupancy. After conditioning on pH and temperature, compositionally aware co-occurrence analysis will show little residual exclusion between clusters.

## Why it matters

A physiological explanation would let community turnover at contaminated sites be predicted from tolerance traits. Residual exclusion would instead point to biotic interactions.

## How to test it

Rerun co-occurrence with a compositionally aware method (SparCC-style) on the full 100-Well-Survey ASV matrix in enigma-coral, with pH and temperature as covariates, and quantify residual cluster-to-cluster association. The 464K-sample global occupancy comes from the Microbial Atlas 16S resource, which is not among the listed collections. In parallel, measure growth of representative isolates from each cluster across a pH gradient at two temperatures.

## What would support or refute it

Support: isolate growth ranges differ in the direction of global occupancy and residual exclusion is small after covariate control. Refute: growth ranges do not differ, or substantial negative residual association persists after conditioning on pH and temperature.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The co-occurrence reanalysis is new compute on existing data, but the decisive isolate growth tests need new measurements.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--a6ede42b|Global pH niche partition separates two Oak Ridge genus clusters]] (Candidate novel)

## Closest published work

- [PMID 38366921](https://pubmed.ncbi.nlm.nih.gov/38366921/) Influence of host phylogeny and water physicochemistry on microbial assemblages of the fish skin microbiome.
- [PMID 40118314](https://pubmed.ncbi.nlm.nih.gov/40118314/) The response and ecological implications between various sulfur forms and environmental factors in acid mine drainage.
- [PMID 30481288](https://pubmed.ncbi.nlm.nih.gov/30481288/) Deforestation impacts network co-occurrence patterns of microbial communities in Amazon soils.
- [PMID 39501158](https://pubmed.ncbi.nlm.nih.gov/39501158/) Rhizosphere bacterial community is mainly determined by soil environmental factors, but the active bacterial diversity is mainly shaped by plant selection.

PMID 38366921 and PMID 40118314 link temperature and pH to Ralstonia and Sphingomonas abundance in fish skin and acid mine drainage. None contrasts these two clusters across global samples or tests physiological tolerance.
