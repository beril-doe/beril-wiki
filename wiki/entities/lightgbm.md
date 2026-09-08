---
type: Method
description: Gradient-boosted tree method for genome-by-condition growth prediction
sources:
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
title: LightGBM
---
# LightGBM

## What this entity is

**Canonical name:** LightGBM gradient-boosted decision-tree method. [^genotype_to_phenotype_enigma]

**Known aliases:** LightGBM; gradient-boosted decision-tree modeling; GBDT (gradient-boosted decision tree). [^genotype_to_phenotype_enigma]

**Stable external identifier:** No stable external identifier was reported for the method in this document. [^genotype_to_phenotype_enigma]

LightGBM was used to predict binary bacterial growth from genome content and growth condition in the integrated ENIGMA corpus. [^genotype_to_phenotype_enigma]

## Use in genotype-by-condition prediction

The full-corpus model used 46,389 genome × condition pairs from 727 genomes, 106 genus-blocked holdouts, and 4,293 shared [kegg](kegg.md) orthologs. [^genotype_to_phenotype_enigma]

The overall binary-growth AUC (area under the receiver-operating-characteristic curve) was 0.620. [^genotype_to_phenotype_enigma]

Performance varied by condition class: amino acids achieved AUC 0.775 across 7,765 pairs, nucleosides achieved AUC 0.780 across 829 pairs, carbon sources achieved AUC 0.695 across 8,965 pairs, other conditions achieved AUC 0.654 across 24,590 pairs, antibiotics achieved AUC 0.619 across 238 pairs, metals achieved AUC 0.605 across 232 pairs, and nitrogen achieved AUC 0.435 across 152 pairs. [^genotype_to_phenotype_enigma]

Adding KO × condition interaction features increased mean AUC from 0.620 to 0.653, an improvement of 0.032, with improvement in 80 of 106 held-out genera. [^genotype_to_phenotype_enigma]

Across 343 individually testable conditions, 95 achieved AUC > 0.75. [^genotype_to_phenotype_enigma]

The best individual conditions were tryptophan with AUC 0.933, phenylalanine with AUC 0.932, valine with AUC 0.927, mannose with AUC 0.904, and galactose with AUC 0.895. [^genotype_to_phenotype_enigma]

The worst individual conditions were turanose with AUC 0.059 and adonitol with AUC 0.010. [^genotype_to_phenotype_enigma]

## Interpretation and limitations

The model predicted binary growth capability more effectively for some substrate classes than for metals, antibiotics, and nitrogen. [^genotype_to_phenotype_enigma]

Continuous growth traits—µmax, lag, and yield-related max_A—were not predictable under genus-blocked holdout from KO presence/absence or bulk genomic features, producing negative R² in both the 46K-pair model and dedicated bulk-feature regression. [^genotype_to_phenotype_enigma]

The report interprets this contrast as evidence that gene content more directly encodes whether an organism can use a substrate, whereas growth rate depends on enzyme kinetics, expression, regulatory context, and ribosome efficiency. [^genotype_to_phenotype_enigma]

Auditing 42,771 genus-blocked holdout predictions gave 65.1% overall accuracy, 7,844 false positives, and 7,101 false negatives. [^genotype_to_phenotype_enigma]

Filtering to confident predictions with |p − 0.5| > 0.25 identified 1,276 high-confidence errors concentrated in genus × condition-class cells including Methylobacterium on amino acids, Sphingomonas on other carbon sources, and Microbacterium on nucleosides. [^genotype_to_phenotype_enigma]

The model was used to rank 343 conditions for active learning by error rate × model uncertainty × field-relevance weight, producing a proposal for 50 next experiments. [^genotype_to_phenotype_enigma]

## Related pages

- [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md) — source report describing the LightGBM genome-by-condition growth models. [^genotype_to_phenotype_enigma]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — cross-condition differences in predictability of growth capability. [^genotype_to_phenotype_enigma]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — shift from genome-scale proxies to substrate-specific predictors as the training corpus expands. [^genotype_to_phenotype_enigma]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — integration of growth curves, KO annotations, fitness data, exometabolomics, pangenomes, and environmental metadata. [^genotype_to_phenotype_enigma]
- [shap](shap.md) — interpretation of model feature importance using SHAP (SHapley Additive exPlanations). [^genotype_to_phenotype_enigma]
- [xgboost](xgboost.md) — related gradient-boosting method listed in the corpus. [^genotype_to_phenotype_enigma]

[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
