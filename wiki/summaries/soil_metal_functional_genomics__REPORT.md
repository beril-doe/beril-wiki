---
type: "Summary"
description: "Summary of the project Soil Metal Concentrations Drive Functional Gene Shifts."
doc_type: "short"
full_text: "sources/soil_metal_functional_genomics__REPORT.md"
---
# Soil Metal Concentrations Drive Functional Gene Shifts

This page summarises a preliminary project that asked whether soil metal concentrations relate to the functional gene content of co-located microbial communities. The main answer is yes: many associations are significant and a conditional db-RDA R² is high. The evidence is observational and incomplete. [src: soil_metal_functional_genomics]

## Key Findings

### Soil-wide associations

The soil analysis found 2,355 significant COG-metal associations at FDR < 0.05 across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 soil samples. [src: soil_metal_functional_genomics]

Chromium and lead drive the strongest soil COG-metal association signals. [src: soil_metal_functional_genomics]

Transporters (ABC, RND) and biosynthesis genes dominate the top soil COG-metal association hits. [src: soil_metal_functional_genomics]

The soil db-RDA yielded R² = 0.799, p = 0.005 with a permutation test using 999 permutations, reported as metal concentrations explaining 80% of variance in community COG profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics]

The report interprets the association between soil metals and co-located microbial community functional gene content as not a statistical artefact of batch effects because project accession was conditioned out. [src: soil_metal_functional_genomics]

### Copper-specific analysis

The copper-specific analysis identified 116 COGs at FDR < 0.05 using 7,566 samples with nearby KBase genomes at 10 km. [src: soil_metal_functional_genomics]

Its top positive associations include cell division and nucleotide transport (BQ, FQ, FK, CF). [src: soil_metal_functional_genomics]

Its top negative associations include energy production (DI, CE), suggesting energetic trade-offs under copper stress. [src: soil_metal_functional_genomics]

The report interprets copper-associated energetic trade-offs and membrane transport enrichment as consistent with known copper toxicity mechanisms in bacteria. [src: soil_metal_functional_genomics]

### Biome comparison

Biome-stratified PGLS shows distinct metal-COG relationships in soil, marine, and wastewater environments, indicating environment-specific functional responses rather than a universal resistance programme. [src: soil_metal_functional_genomics]

## Caveats and Open Work

### Status

The report is preliminary: Spearman correlation, db-RDA, and PGLS analyses are complete in NB01–NB04, while NB05 effect size and spatial validation and NB06 figures are pending. [src: soil_metal_functional_genomics]

All reported metal-COG associations are observational. [src: soil_metal_functional_genomics]

### db-RDA interpretation

The report cautions that conditional db-RDA R² = 0.799 may describe metals' explanation of residual rather than total community COG variance if project effects account for the majority of variance. [src: soil_metal_functional_genomics]

The unconditional db-RDA R² for metals alone without removing project effects is unreported and may be substantially lower than the conditional figure. [src: soil_metal_functional_genomics]

Reporting unconditional db-RDA R² (metals only, without project accession conditioning) remains pending. [src: soil_metal_functional_genomics]

### Multiple testing and confounding

The report describes 2,355 significant associations at FDR < 0.05 in 51,748 samples from 9 metals × 435 COGs = 3,915 tests as a high 60% discovery rate. [src: soil_metal_functional_genomics]

The report asserts that co-contaminating metals make tests non-independent, that Benjamini-Hochberg FDR correction assumes independent tests and is anti-conservative under positive correlation, and that true FDR is likely higher than reported. [src: soil_metal_functional_genomics]

Co-contamination is a significant confound because Cr, Cu, Pb, and Zn co-vary in many industrial soils. [src: soil_metal_functional_genomics]

Whether individual COG-metal associations are metal-specific or reflect a generic stress response to multi-metal contamination remains unresolved, with NB05 partial correlation models pending. [src: soil_metal_functional_genomics]

The report identifies the NB05 item 3 partial correlation model as the remedy for this confounding. [src: soil_metal_functional_genomics]

The pending partial correlation model is COG ~ Cr | Cu + Zn + Pb, intended to distinguish metal-specific from general responses. [src: soil_metal_functional_genomics]

Spearman ρ effect sizes have not been systematically reported across all 2,355 associations, and many associations may be statistically significant but biologically small. [src: soil_metal_functional_genomics]

The pending effect size audit will examine the ρ distribution across 2,355 associations and flag ρ < 0.05. [src: soil_metal_functional_genomics]

### Copper proximity

The copper-specific analysis matches soil samples to KBase genomes using a 10 km proximity criterion, at which many nearby genomes may not be co-located with copper measurements. [src: soil_metal_functional_genomics]

The report states that sensitivity analyses at 5 km and 20 km thresholds are needed before attributing COG-copper associations to measured sites. [src: soil_metal_functional_genomics]

Rerunning copper proximity analyses at 5 km and 20 km thresholds remains pending. [src: soil_metal_functional_genomics]

### Other pending work

The pending spatial autocorrelation validation will test Moran's I on residuals and use SEVM if significant. [src: soil_metal_functional_genomics]

Pending mechanistic classification will assign significant COGs to resistance, stress, membrane, energy, and unknown categories. [src: soil_metal_functional_genomics]

NB05 items 1–4 require re-running analyses from the `kescience_mgnify`/`kbase_ke_pangenome` Spark tables. [src: soil_metal_functional_genomics]

No local CSV output of Spearman ρ values or model residuals is available, so the pending validations cannot be completed without Spark access. [src: soil_metal_functional_genomics]

## Slots Into

- [[concepts/co-contamination-and-multiple-testing-confounding-in-metal-function-associations]]: Co-varying metals and anti-conservative FDR limit the 2,355 associations. [src: soil_metal_functional_genomics]
- [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]]: The db-RDA with conditional R² = 0.799 links soil metals to community COG profiles. [src: soil_metal_functional_genomics]
- [[concepts/spatial-matching-of-environmental-samples-to-genomes]]: The 10 km copper matching needs 5 km and 20 km sensitivity checks. [src: soil_metal_functional_genomics]
- [[concepts/geographic-and-biome-distribution-of-environmental-metal-resistance]]: Soil, marine and wastewater show distinct metal-COG relationships. [src: soil_metal_functional_genomics]
