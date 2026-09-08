---
type: Method
description: Random Forest method for predicting Pseudomonas isolation environments
sources:
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
title: Random Forest classifier
---
# Random Forest classifier

## What this entity is

**Canonical name:** Random Forest classifier. [^pseudomonas_carbon_ecology]

**Known aliases:** Random Forest; RF classifier. [^pseudomonas_carbon_ecology]

**Stable external identifier:** None was reported in the source document. [^pseudomonas_carbon_ecology]

A Random Forest is an ensemble machine-learning method that combines predictions from multiple decision trees; here it was used to classify *Pseudomonas* isolation environments from carbon-pathway profiles. [^pseudomonas_carbon_ecology]

## Use in the Pseudomonas carbon-ecology analysis

The classifier used 62-pathway carbon profiles predicted with GapMind to distinguish four environment classes: soil, freshwater, plant_surface, and rhizosphere. [^pseudomonas_carbon_ecology]

The filtered dataset contained 51 species: 13 soil species, 13 freshwater species, 19 plant_surface species, and 6 rhizosphere species. [^pseudomonas_carbon_ecology]

In 5-fold stratified cross-validation, the classifier achieved a balanced accuracy of 0.408 +/- 0.169, compared with a 0.250 chance baseline. [^pseudomonas_carbon_ecology]

The most discriminating pathways were D-serine, with importance 0.132; arabinose, 0.094; rhamnose, 0.086; fucose, 0.085; and xylose, 0.070. [^pseudomonas_carbon_ecology]

These results support a non-random association between carbon-pathway profiles and isolation environment, but the balanced accuracy of 0.408 indicates that carbon profiles alone were insufficient for fine-grained environment discrimination among free-living *Pseudomonas* species. [^pseudomonas_carbon_ecology]

## Interpretation and limitations

The classifier was applied after species-level filtering requiring at least 5 genomes and at least 60% majority-environment agreement for the broader free-living and plant-associated analysis. [^pseudomonas_carbon_ecology]

The report identifies small sample sizes per environment class, overlap between related environments such as soil and rhizosphere, coarse resolution of the 62 GapMind pathways, and phylogenetic structure as limitations that may affect classification performance. [^pseudomonas_carbon_ecology]

The dominant variation in the carbon profiles separated *Pseudomonas* s.s. from *Pseudomonas_E*, rather than cleanly separating lifestyles within *Pseudomonas_E*, indicating that phylogenetic structure may confound environment prediction. [^pseudomonas_carbon_ecology]

The report proposes extending the feature set with aromatic-degradation modules and testing genome-level prediction using the full 789,012-row genome-pathway matrix. [^pseudomonas_carbon_ecology]

## Related pages

- [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md) — source summary describing the classifier and its evaluation. [^pseudomonas_carbon_ecology]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — interpretation of how carbon profiles embed isolation environments. [^pseudomonas_carbon_ecology]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — relationship between pathway content and ecological niche. [^pseudomonas_carbon_ecology]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — GapMind pathway predictions used as classifier features. [^pseudomonas_carbon_ecology]
- [carbon-source-phenotypes](carbon-source-phenotypes.md) — carbon-utilization phenotype profiles related to the classifier inputs. [^pseudomonas_carbon_ecology]
- [pseudomonas](pseudomonas.md) — genus represented in the analyzed genome collection. [^pseudomonas_carbon_ecology]
- [gapmind](gapmind.md) — pathway-completeness method supplying the carbon-profile features. [^pseudomonas_carbon_ecology]

[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
