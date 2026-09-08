---
type: Method
description: XGBoost method for predicting genome-based metal tolerance
sources:
- id: bacdive_phenotype_metal_tolerance
  resource: ../summaries/bacdive_phenotype_metal_tolerance__REPORT.md
  title: bacdive phenotype metal tolerance
- id: metal_fitness_atlas
  resource: ../summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
title: XGBoost
---
# XGBoost

## Identity

XGBoost (Extreme Gradient Boosting) is the machine-learning method used in this study to model genome-based metal tolerance from taxonomy, BacDive phenotype features, and metal-resistance gene-cluster counts. [^bacdive_phenotype_metal_tolerance]

Known alias: Extreme Gradient Boosting. [^bacdive_phenotype_metal_tolerance]

No stable external identifier is reported for this method in the source document. [^bacdive_phenotype_metal_tolerance]

## Use in the BacDive metal-tolerance study

The full XGBoost model used 17 features across 3,994 species and included taxonomy, phenotype variables, and `n_metal_clusters`, the number of metal-resistance gene clusters. [^bacdive_phenotype_metal_tolerance]

In 5-fold phylogenetic-blocked cross-validation, the full model achieved R² = 0.633 and RMSE = 0.028, outperforming the gene-count-only model (R² = 0.063, RMSE = 0.045), phenotype-only model (R² = 0.163, RMSE = 0.043), taxonomy-only model (R² = 0.354, RMSE = 0.038), and taxonomy-plus-phenotype model (R² = 0.345, RMSE = 0.038). [^bacdive_phenotype_metal_tolerance]

In the non-cross-validated model comparison, taxonomy explained 35.4% of metal-tolerance variance, phenotype features explained 16.3%, and taxonomy plus phenotype yielded R² = 0.345, a delta R² = -0.009 relative to taxonomy alone. [^bacdive_phenotype_metal_tolerance]

Adding `n_metal_clusters` increased the full model to R² = 0.633, supporting [environmental-resistome](../concepts/environmental-resistome.md)'s interpretation that genome-encoded metal-resistance repertoire was the strongest predictor in this analysis. [^bacdive_phenotype_metal_tolerance]

## Feature interpretation

SHAP (Shapley additive explanations) feature importance from the full [shap](shap.md)-interpreted XGBoost model placed taxonomic class and order codes together with `n_metal_clusters` among the top predictors. [^bacdive_phenotype_metal_tolerance]

Phenotype features contributed minimally after taxonomy was included, supporting the interpretation that the measured phenotypes were primarily phylogenetic proxies rather than independent predictors of the composite metal-tolerance score. [^bacdive_phenotype_metal_tolerance]

The model comparison does not establish metal-specific mechanisms because the target was a composite genome-based score rather than direct metal-tolerance measurements. [^bacdive_phenotype_metal_tolerance]

## Relation to the metal fitness atlas

The [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) provides a methodological contrast rather than a new XGBoost application: its pangenome-scale prediction used a simple gene-presence repertoire score, which failed to predict metal fitness. [^metal_fitness_atlas] This **refines** the interpretation of XGBoost's BacDive result: predictive performance depends on the modeled target and feature design, so the atlas failure does not contradict the full BacDive XGBoost model. [^metal_fitness_atlas]

## Related source

The method is described in the study summary [bacdive_phenotype_metal_tolerance__REPORT](../summaries/bacdive_phenotype_metal_tolerance__REPORT.md), alongside the [metal-fitness-atlas](metal-fitness-atlas.md) scores and [bacdive](bacdive.md) phenotype data. [^bacdive_phenotype_metal_tolerance]

[^bacdive_phenotype_metal_tolerance]: [bacdive phenotype metal tolerance](../summaries/bacdive_phenotype_metal_tolerance__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
