---
type: "Research direction"
description: "Two groups of genera found at Oak Ridge (Rhodanobacter, Ralstonia and Dyella versus Brevundimonas, Caulobacter and Sphingomonas) occupy different habitats worldwide. The first group lives in environments 1.35 pH units more acidic and 6.9\u00b0C warmer. Which of the two variables actually drives the split?"
hypothesis: "Acidity is the primary driver. In samples matched for pH, the abundance contrast between the two clusters largely disappears, whereas in samples matched for temperature it persists. In culture, strains of the first cluster outgrow strains of the second at low pH at both temperatures."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The survey analysis can use global OTU counts with matched soil pH and temperature columns shown in the catalog, but the decisive growth experiment across pH and temperature needs new measurements."
databases: ["arkinlab.microbeatlas", "kescience.fitnessbrowser"]
tables: ["arkinlab.microbeatlas.otu_counts_long", "arkinlab.microbeatlas.enriched_metadata_gee", "arkinlab.microbeatlas.otu_metadata", "kescience.fitnessbrowser.organism"]
findings: ["genotype_to_phenotype_enigma--a6ede42b"]
conflicts: []
papers: ["38366921", "40118314", "30481288", "39501158"]
builds_on: ["findings/genotype_to_phenotype_enigma--a6ede42b"]
projects: ["genotype_to_phenotype_enigma"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Is acidity, rather than temperature, what separates two Oak Ridge genus clusters worldwide?

Two groups of genera found at Oak Ridge (Rhodanobacter, Ralstonia and Dyella versus Brevundimonas, Caulobacter and Sphingomonas) occupy different habitats worldwide. The first group lives in environments 1.35 pH units more acidic and 6.9°C warmer. Which of the two variables actually drives the split?

## Hypothesis

Acidity is the primary driver. In samples matched for pH, the abundance contrast between the two clusters largely disappears, whereas in samples matched for temperature it persists. In culture, strains of the first cluster outgrow strains of the second at low pH at both temperatures.

## Why it matters

A global niche partition only helps predict which lab strains stand in for field organisms if its driver is known. Naming pH rather than temperature would also show which Oak Ridge contamination variable to prioritise. The original observation reports shared or exclusive niches, not direct interaction, so this separates habitat filtering from correlation.

## How to test it

Step 1 (lakehouse): join global amplicon survey counts for the six genera to the soil pH and air temperature layers attached to each sample. Compare the abundance contrast between the two clusters in pH-matched samples that differ in temperature, and in temperature-matched samples that differ in pH. Only samples with these layers can be used. Step 2 (experiment): grow strains of Dyella, Ralstonia, Sphingomonas and Caulobacter from the mutant fitness collection across a pH gradient at two temperatures, each alone and in mixed culture.

## What would support or refute it

Support: the contrast between clusters shrinks to little in pH-matched samples but persists in temperature-matched ones, and acid-cluster strains win at low pH at both temperatures. Refutation: the contrast persists after pH matching, or temperature alone changes which strain wins in culture.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The survey analysis can use global OTU counts with matched soil pH and temperature columns shown in the catalog, but the decisive growth experiment across pH and temperature needs new measurements.

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--a6ede42b|Global pH niche partition separates two Oak Ridge genus clusters]] (Candidate novel)

## Closest published work

- [PMID 38366921](https://pubmed.ncbi.nlm.nih.gov/38366921/) Influence of host phylogeny and water physicochemistry on microbial assemblages of the fish skin microbiome.
- [PMID 40118314](https://pubmed.ncbi.nlm.nih.gov/40118314/) The response and ecological implications between various sulfur forms and environmental factors in acid mine drainage.
- [PMID 30481288](https://pubmed.ncbi.nlm.nih.gov/30481288/) Deforestation impacts network co-occurrence patterns of microbial communities in Amazon soils.
- [PMID 39501158](https://pubmed.ncbi.nlm.nih.gov/39501158/) Rhizosphere bacterial community is mainly determined by soil environmental factors, but the active bacterial diversity is mainly shaped by plant selection.

PMID 38366921 and PMID 40118314 tie pH and temperature to Ralstonia and Sphingomonas only in fish skin and acid mine drainage; none separates the two drivers for these two clusters worldwide.
