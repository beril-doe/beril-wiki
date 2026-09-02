---
type: "Method"
description: "SHAP explains feature contributions in predictive models."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# SHAP

## What this is

SHAP is the canonical name for Shapley additive explanations, a model-interpretation method that attributes a prediction to feature contributions. [src: bacdive_phenotype_metal_tolerance]

Known alias: Shapley additive explanation. [src: bacdive_phenotype_metal_tolerance]

No stable external identifier was reported for this method in the source document. [src: bacdive_phenotype_metal_tolerance]

## Use in the BacDive metal-tolerance study

SHAP feature importance was applied to the full XGBoost model to assess which predictors contributed to genome-based metal-tolerance scores. [src: bacdive_phenotype_metal_tolerance]

Taxonomic class and order codes, together with `n_metal_clusters`, were among the top predictors in the SHAP ranking. [src: bacdive_phenotype_metal_tolerance]

Phenotype features contributed minimally after taxonomy was included, supporting the interpretation that the measured phenotypes were primarily phylogenetic proxies rather than independent predictors of the composite metal-tolerance score. [src: bacdive_phenotype_metal_tolerance]

The model was trained across 3,994 species and included 17 features in the full model. [src: bacdive_phenotype_metal_tolerance]

This result supports [[concepts/environmental-resistome]], where the full model reached R² = 0.633 after adding the number of metal-resistance gene clusters. [src: bacdive_phenotype_metal_tolerance]

## Use in ENIGMA genotype-to-phenotype prediction

In the ENIGMA study, correlation-grouped SHAP attributed 25.3% of total importance to a 63-feature genome-scale axis and 45.9% to condition class; membrane adaptation, tRNA modification, aromatic catabolism, and flagellar-motility KO blocks each contributed approximately 2%. [src: genotype_to_phenotype_enigma]

This **refines** the BacDive result: SHAP can expose broad taxonomic or genome-scale proxies, but the larger ENIGMA corpus also identified condition-specific predictors, including K03762 (`proP`), K10440 (`rbsC`), K01857 (`pcaB`), K13633 (`ftrA`), and K01214 (`treX`). [src: genotype_to_phenotype_enigma]

The ENIGMA analysis further used SHAP to compare predicted growth with Fitness Browser fitness effects; 18.7% of top SHAP KOs expanded into correlation-grouped gene blocks had significant matched-condition fitness effects versus a 16.3% random baseline, a 1.19× enrichment. This **supports** interpreting feature-attribution results as potentially mechanistic while **refining** the distinction between gene presence across genera and gene essentiality within one strain. [src: genotype_to_phenotype_enigma]

The detailed ENIGMA application is described in [[summaries/genotype_to_phenotype_enigma__REPORT]]. [src: genotype_to_phenotype_enigma]

## Related material

The method is described in the study summary [[summaries/bacdive_phenotype_metal_tolerance__REPORT]]. [src: bacdive_phenotype_metal_tolerance]

Its interpretation also relates to [[concepts/pangenome-integration]], because the analysis integrated BacDive phenotypes with species-level pangenome and metal-score data. [src: bacdive_phenotype_metal_tolerance]
