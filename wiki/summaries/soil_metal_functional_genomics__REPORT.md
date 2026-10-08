---
type: "Summary"
description: "Preliminary analysis of associations between nine soil metal concentrations and microbial COG functional gene content across 51,748 samples, with its confounding, effect-size and spatial-validation caveats."
doc_type: "short"
full_text: "sources/soil_metal_functional_genomics__REPORT.md"
---
# Soil Metal Concentrations Drive Functional Gene Shifts

## Overview

This preliminary report analyzes associations between soil metal concentrations and microbial functional gene content using Spearman correlation, distance-based redundancy analysis (db-RDA, a constrained ordination of a distance matrix against explanatory variables), and phylogenetic generalized least squares (PGLS); these Spearman correlation, db-RDA and PGLS analyses (NB01–NB04) are complete, while NB05 effect-size and spatial validation remain pending. The NB06 figures are also pending, so the report provides no completed figures. The analysis covers 51,748 soil samples and nine metals: copper (Cu), cobalt (Co), chromium (Cr), nickel (Ni), zinc (Zn), lead (Pb), arsenic (As), cadmium (Cd), and mercury (Hg). [src: soil_metal_functional_genomics]

## Key Findings

- The study identified 2,355 significant COG–metal associations at FDR < 0.05 across the nine metals and 51,748 soil samples. Here, COG refers to a Cluster of Orthologous Groups functional category, and FDR refers to false discovery rate. Chromium and lead produced the strongest signals, while transporters, including ABC and RND systems, and biosynthesis genes dominated the top hits. [src: soil_metal_functional_genomics]
- In a copper-specific analysis of 116 COGs at FDR < 0.05, using 7,566 samples with nearby KBase genomes within 10 km, the strongest positive associations included cell division and nucleotide transport categories (BQ, FQ, FK, and CF), whereas the strongest negative associations included energy-production categories (DI and CE). These results suggest energetic trade-offs under copper stress, but the associations are observational. The report interprets the copper-associated energetic trade-offs and membrane-transport enrichment as consistent with known bacterial copper-toxicity mechanisms; this is an interpretation, not a tested mechanism. [src: soil_metal_functional_genomics]
- The db-RDA model yielded R² = 0.799 and p = 0.005 using 999 permutations. After conditioning on batch and project effects, metal concentrations explained 80% of the variance in community COG profiles. [src: soil_metal_functional_genomics]
- Biome-stratified PGLS, a comparative regression method that accounts for phylogenetic relationships, found distinct metal–COG relationships in soil, marine, and wastewater environments. This supports environment-specific functional responses rather than a universal resistance programme. [src: soil_metal_functional_genomics]

## Caveats and Pending Validation

All reported associations are observational. Co-contamination is a major confound because chromium, copper, lead, and zinc co-vary in many industrial soils; it is therefore unresolved whether individual COG–metal associations are metal-specific or reflect a generic response to multi-metal contamination. Partial-correlation models are planned to address this distinction. [src: soil_metal_functional_genomics]

The reported db-RDA R² = 0.799 is conditional: project accession was removed before fitting metal predictors. If project effects explain most community COG variance, this value describes metals’ explanation of residual variance rather than total variance. The unconditional R² for metals alone was not reported and may be substantially lower; both values should be reported. [src: soil_metal_functional_genomics]

The 2,355 discoveries among 3,915 implied tests (nine metals × 435 COGs) represent a 60% discovery rate, but the report cautions that metal co-contamination makes tests non-independent. Benjamini–Hochberg FDR correction may therefore be anti-conservative under positive correlation, and the true FDR may be higher than reported. The report names the partial-correlation model (NB05 item 3) as the correct remedy; this is the report's methodological assessment, not a validated recalculation of FDR. [src: soil_metal_functional_genomics]

Effect sizes have not been systematically reported across all 2,355 associations. The planned effect-size audit will examine the Spearman rho distribution and flag associations with rho < 0.05, because statistical significance may not imply substantial biological effect. [src: soil_metal_functional_genomics]

The copper-specific analysis used a 10 km proximity criterion to match soil samples with KBase genomes. Some genomes designated as nearby may not be co-located with the copper measurements, so copper–COG attribution requires sensitivity analyses at 5 km and 20 km. [src: soil_metal_functional_genomics]

The planned validation includes Moran’s I spatial-autocorrelation testing on residuals, with SEVM if spatial autocorrelation is significant; partial correlation of COG ~ Cr | Cu + Zn + Pb; mechanistic classification of significant COGs into resistance, stress, membrane, energy, and unknown categories; reporting unconditional db-RDA R²; and copper proximity sensitivity at 5 km and 20 km. [src: soil_metal_functional_genomics]

NB05 items 1–4 require rerunning analyses from the `kescience_mgnify` and `kbase_ke_pangenome` Spark tables. No local CSV containing the Spearman rho values or model residuals is available, so these validations cannot be completed without Spark access. [src: soil_metal_functional_genomics]

## Slots Into

- [[concepts/environmental-resistome]] — Metal-associated transporter and biosynthesis shifts provide environmental evidence relevant to the distribution of resistance-related functions, while the report’s confounding warnings constrain interpretation. [src: soil_metal_functional_genomics]
- [[concepts/ecotype-environment-gene-content]] — Biome-specific metal–COG relationships support environment-dependent links between environmental chemistry and microbial gene content. [src: soil_metal_functional_genomics]
- [[concepts/metal-cross-resistance]] — Co-varying chromium, copper, lead, and zinc create a direct test of whether apparent metal associations are metal-specific or reflect multi-metal stress. [src: soil_metal_functional_genomics]
- [[concepts/environment-embedding-geography]] — The 10 km genome–soil matching rule and planned 5 km and 20 km sensitivity analyses make spatial co-location central to interpreting copper-associated functions. [src: soil_metal_functional_genomics]
- [[concepts/confirmatory-exploratory-ecological-association-discordance]] — The 60% discovery rate, possibly anti-conservative FDR under dependent tests, and unreported effect sizes mark the 2,355 associations as exploratory pending the effect-size audit. [src: soil_metal_functional_genomics]
- [[concepts/study-batch-confounding-of-environmental-associations]] — The db-RDA R² = 0.799 is conditional on project accession, and the unconditional metals-only R² was not reported. [src: soil_metal_functional_genomics]
- [[concepts/shared-stress-versus-stressor-specific-fitness]] — The planned partial-correlation model COG ~ Cr | Cu + Zn + Pb is meant to separate metal-specific from generic multi-metal stress responses. [src: soil_metal_functional_genomics]
- [[concepts/composite-resistance-score-limitations]] — Co-varying Cr, Cu, Pb and Zn prevent attributing COG associations to individual metals. [src: soil_metal_functional_genomics]
- [[concepts/spatial-sampling-effort-confounding]] — Spatial autocorrelation of residuals remained untested (planned Moran's I, with SEVM if significant). [src: soil_metal_functional_genomics]
