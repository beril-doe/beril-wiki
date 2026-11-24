---
type: "Other"
description: "Soil habitat samples dominating the NMDC cohort."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
aliases: ["Soil ecosystem"]
---
# Soil

Soil, also called the soil ecosystem, is the habitat that supplies most samples in the NMDC cohort: 126 of 220. [src: nmdc_community_metabolic_ecology] The evidence comes from two reports: one on eukaryotic signal in prokaryote-targeted metagenomes, and one on community metabolic ecology. See [[entities/nmdc-integrated-collections]] for the collections.

## Key facts

- The full NMDC 220-sample cohort contained 126 Soil samples, 33 Freshwater samples and 61 samples with unrecorded ecosystem type. [src: nmdc_community_metabolic_ecology]
- Terrestrial (soil) NMDC samples show 55.7% eukaryotic detection and a plastid share of eukaryotes of 0.43. The eukaryotic sources are mixed: plant plastid plus soil fungi and protists. [src: euk_in_prok_correlates] See [[concepts/sources-and-prevalence-of-eukaryotic-contamination-in-prokaryote-targeted-metagenomes]].

## Metabolic potential versus Freshwater

Soil and Freshwater communities occupied nearly non-overlapping regions of the principal component analysis (PCA) space. Kruskal-Wallis across three ecosystem types was highly significant on PC1 (H = 52.98, p < 0.0001) and PC2 (H = 123.74, p < 0.0001). [src: nmdc_community_metabolic_ecology] PC1 means principal component 1. The pairwise Soil versus Freshwater PC1 separation had Mann-Whitney U = 3,674, p < 0.0001. Median PC1 was +3.86 for Soil and −6.28 for Freshwater. [src: nmdc_community_metabolic_ecology] See [[entities/mann-whitney-u-test]].

PC1 loaded almost entirely on carbon utilization pathways (glucuronate, fumarate, succinate, cellobiose, galactose), with near-uniform positive loadings. The report reads this as broadly higher carbon substrate completeness in Soil than in Freshwater communities. [src: nmdc_community_metabolic_ecology] It also interprets the uniformly high positive loadings as substantially higher predicted carbon metabolic diversity in Soil. [src: nmdc_community_metabolic_ecology] This is an interpretation of predicted pathway loadings. See [[concepts/ecosystem-differentiation-of-community-metabolic-potential]].

## Use as a control

To control for the strong ecosystem-type effect, the report re-ran its H1 analysis on 125 Soil-ecosystem samples only. It excluded the 6 Unknown-ecosystem samples in the H1 dataset. [src: nmdc_community_metabolic_ecology] See [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]] and [[summaries/nmdc_community_metabolic_ecology__REPORT]].
