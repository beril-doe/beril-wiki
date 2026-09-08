---
type: Method
description: Multivariate method for relating distance-based functional profiles to
  explanatory variables
sources:
- id: plant_microbiome_ecotypes
  resource: ../summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: Distance-based redundancy analysis
---
# Distance-based redundancy analysis

## What this entity is

**Canonical name:** Distance-based redundancy analysis. **Known alias:** db-RDA. No stable external identifier was reported in the source document. [^plant_microbiome_ecotypes]

Distance-based redundancy analysis is a multivariate method used in this study to isolate compartment centroid, or location, effects from dispersion effects in functional-distance data. [^plant_microbiome_ecotypes]

## Key facts from the documents

Using a refined 17-marker panel and Jaccard distances across 607 root, rhizosphere, and phyllosphere species, db-RDA estimated a location-only R² of 0.060 with p = 0.001. [^plant_microbiome_ecotypes]

The location-only R² of 0.060 represented 84% of the total PERMANOVA R² of 0.071, while 16% was attributable to dispersion. [^plant_microbiome_ecotypes]

The db-RDA result therefore supports the conclusion that plant compartments have statistically significant but weak functional separation, with approximately 6% of variance associated with compartment location effects. [^plant_microbiome_ecotypes]

PERMDISP detected dispersion heterogeneity with F = 15.6 and p = 0.001; root species had a mean distance of 0.452 from their centroid, phyllosphere species had 0.503, and rhizosphere species had 0.528. [^plant_microbiome_ecotypes]

The db-RDA analysis refines the interpretation of the PERMANOVA result by showing that most of the explained variation reflected centroid shifts rather than dispersion differences. [^plant_microbiome_ecotypes]

The soil-metal analysis **extends** this method’s use from compartment functional distances to community COG profiles: its conditional model reported R² = 0.799 and p = 0.005 using 999 permutations after conditioning on batch and project effects, with metals explaining 80% of residual COG-profile variance. [^soil_metal_functional_genomics] This result is conditional rather than directly comparable to the plant location-only R², because the soil analysis removed project effects before fitting metal predictors; unconditional metal-only R² was not reported. [^soil_metal_functional_genomics]

## Related pages

This method is relevant to [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) because it quantifies the compartment component of environmental differences in functional gene profiles. [^plant_microbiome_ecotypes] The soil-metal result **supports** this broader environmental-gene-content connection by identifying biome-specific metal–COG relationships, while remaining observational. [^soil_metal_functional_genomics]

It also contributes to [environment-embedding-geography](../concepts/environment-embedding-geography.md) through the comparison of root, rhizosphere, and phyllosphere functional profiles. [^plant_microbiome_ecotypes] The soil analysis **refines** that connection by showing that spatial and project conditioning affect interpretation of metal-associated profiles. [^soil_metal_functional_genomics]

The source reports are summarized in [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md) and [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md). [^plant_microbiome_ecotypes] [^soil_metal_functional_genomics]

[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../summaries/plant_microbiome_ecotypes__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
