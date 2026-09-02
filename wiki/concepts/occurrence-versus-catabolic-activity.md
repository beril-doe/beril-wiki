---
type: "Concept"
description: "Environmental presence is not evidence of compound degradation."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Environmental occurrence does not establish compound catabolism

Detection of an organism, genus, or community in an environment demonstrates occurrence or abundance, but does not establish that the organism degrades a target compound there. The [[summaries/enigma_carbon_census_1__REPORT]] provides a direct example: its environmental atlas measured organismal abundance and occurrence, whereas compound catabolic activity was not measured. [src: enigma_carbon_census_1]

## Evidence from the ENIGMA Carbon Census

The global environmental atlas covered 86 implicated genera using 3825 taxonomy-bearing NMDC metagenomes and 302 Planet Microbe marine runs. [src: enigma_carbon_census_1] In NMDC, 83/86 genera were detected in 1719 metagenomes, and 99% of samples were labeled through two independent ontology systems. [src: enigma_carbon_census_1] The macro-environment counts were soil 2260, freshwater 723, periphyton 472, plant 119, and sediment 42. [src: enigma_carbon_census_1]

Periphyton revealed a strong Burkholderiales/Comamonadaceae occurrence reservoir: listed genera reached approximately 96–97% prevalence with mean relative abundance approximately 0.005–0.009. [src: enigma_carbon_census_1] Label-free abundance outliers included Nocardioides at 0.43 in epipsammon, Hydrogenophaga at 0.28 in epiphyton, and Mycobacterium at 0.22 in soil; outliers occurred for 34 genera in periphyton and 32 in soil. [src: enigma_carbon_census_1] These measurements identify environments where candidate organisms occur, but they do not show that those organisms consumed any of the 83 enrichment compounds. [src: enigma_carbon_census_1]

The marine arm similarly provided an occurrence contrast rather than a catabolism assay: all 68/68 listed genera showed positive abundance across 302 Planet Microbe runs, while terrestrial/freshwater genera generally occurred at approximately 1e-3 to 1e-4 abundance in open ocean. [src: enigma_carbon_census_1] Alteromonas was a genuine marine member, occurring at 0.048 in 240/302 runs with prevalence 0.79; Pseudomonas and Sphingomonas had abundances 0.011 and 0.0063, respectively. [src: enigma_carbon_census_1] These values support biome occupancy comparisons, not claims of compound transformation. [src: enigma_carbon_census_1]

## Why the evidence types must remain separate

The census connected environmental occurrence with higher-tier evidence, including ENIGMA-isolate utilizer predictions and GTDB strain placement, but those evidence streams did not convert genus-level environmental detection into an activity measurement. [src: enigma_carbon_census_1] Deliverable (a) contained 569 ENIGMA-isolate utilizer prediction rows across 8 ENIGMA-isolate-callable compounds, while deliverable (b) placed 494 strain records representing 359 distinct strains on GTDB taxonomy. [src: enigma_carbon_census_1] These predictions and placements identify genetic or isolate-level utilization potential; the environmental atlas identifies where implicated genera were detected. [src: enigma_carbon_census_1]

The distinction is especially important because only 9 of 83 compounds were callable under the project's definition, and the effective carbon-callable set was 8 after xanthine was removed as a carbon-catabolic call. [src: enigma_carbon_census_1] The remaining 74/83 compounds were organism-dark within the queried BERDL and curated resources, meaning that environmental detection of possible hosts cannot by itself resolve their missing catabolic determinants. [src: enigma_carbon_census_1] This supports [[concepts/potential-versus-realized-data-integration]]: potential inferred from genomes or isolate predictions should not be presented as realized activity in environmental samples. [src: enigma_carbon_census_1]

## Interpretation and scope

The environmental atlas supports prioritizing locations and taxa for enrichment, particularly periphyton sites associated with the observed Burkholderiales/Comamonadaceae reservoir. [src: enigma_carbon_census_1] It does not establish substrate uptake, pathway expression, growth on the compound, transformation-product formation, or flux through a catabolic pathway because no environmental dataset measured the census compounds. [src: enigma_carbon_census_1]

The project therefore reported an SSO field-occurrence atlas rather than a statistical groundwater-versus-necromass source contrast. [src: enigma_carbon_census_1] H3 was untestable and confounded because only 2 of the 8 ENIGMA-isolate-callable compounds were necromass-sourced, and both were phthalate-class aromatics with Actinomycetota-heavy utilizers. [src: enigma_carbon_census_1] This limitation connects to [[concepts/ecotype-environment-gene-content]] and [[concepts/environmental-embedding-ecological-validity]]: environmental labels can structure where organisms are found, but they do not substitute for compound-resolved activity measurements. [src: enigma_carbon_census_1]

The environmental abundance analysis also requires caution in statistical interpretation. [src: enigma_carbon_census_1] Soil-versus-freshwater enrichment statistics treated each metagenome as independent despite compositional, zero-inflated relative abundances, and all 83 genera reached q<0.05 with many q values near 1e-70. [src: enigma_carbon_census_1] The project judged direction and rank more trustworthy than the p-values and considered label-free outlier discovery the more defensible signal. [src: enigma_carbon_census_1] This reinforces [[concepts/sampling-depth-and-downsampling-effects]] by showing that occurrence-based associations require study-aware designs before being interpreted as ecological or metabolic causality. [src: enigma_carbon_census_1]

## Tensions

A high environmental prevalence can support the practical hypothesis that a taxon is accessible for enrichment, but it cannot establish that the taxon catabolizes a particular compound in situ. [src: enigma_carbon_census_1] The census found 3-hydroxybenzoic-acid utilizers at 0.90 field prevalence at genus resolution while also explicitly classifying the environmental atlas as an abundance or occurrence proxy rather than evidence of compound degradation or activity. [src: enigma_carbon_census_1] The apparent tension is resolved by treating occurrence as site-selection evidence and catabolism as a separate claim requiring compound-resolved experiments or activity measurements. [src: enigma_carbon_census_1]

## Open Directions

- Pair the 86 implicated genera and 83 census compounds with compound-resolved enrichment cultures, substrate depletion measurements, and transformation-product assays to test whether environmental occurrence predicts realized catabolism. [src: enigma_carbon_census_1]
- Use metatranscriptomics or metaproteomics on periphyton and soil samples enriched for the observed genera to test whether candidate catabolic pathways are expressed in the presence of specific census compounds; the current atlas measured occurrence but no compound activity. [src: enigma_carbon_census_1]
- Apply study-aware mixed models or sample-level permutations to the NMDC data to test whether environmental occurrence differences remain after accounting for sampling structure and compositional, zero-inflated abundances. [src: enigma_carbon_census_1]
- Experimentally test the 29 fully orphan compounds in periphyton-sited enrichments to determine whether the observed Burkholderiales/Comamonadaceae reservoir contains unrecognized utilizers. [src: enigma_carbon_census_1]
- Combine GTDB strain placement, pathway-completeness checks, and isotope tracing for selected callable compounds to distinguish genetic utilization potential from measured carbon incorporation. [src: enigma_carbon_census_1]
