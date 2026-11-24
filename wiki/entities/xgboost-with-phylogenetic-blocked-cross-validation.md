---
type: "Method"
description: "Gradient-boosted regression with SHAP importance and phylogenetically blocked CV used to compare model configurations."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md"]
aliases: ["SHAP", "Shapley additive explanations", "XGBoost"]
---
# XGBoost with phylogenetic-blocked cross-validation

XGBoost with phylogenetic-blocked cross-validation combines gradient-boosted regression, SHAP importance and blocked CV to compare model configurations. [src: bacdive_phenotype_metal_tolerance]

Both add blocked cross-validation (CV): one blocked by phylogeny, one by geography. [src: bacdive_phenotype_metal_tolerance, comprehensive_metal_ecology] A third project, on ENIGMA growth prediction, used SHAP TreeExplainer. The cited claims do not say which model it explained. [src: genotype_to_phenotype_enigma] The evidence is per-project and not pooled.

## Key facts

- The BacDive metal-tolerance project ran XGBoost prediction with phylogenetic-blocked CV, SHAP importance and a 5-model comparison in `04_multivariate_model.ipynb`. [src: bacdive_phenotype_metal_tolerance]
- The comparison is saved as `data/model_comparison.csv`, with cross-validated R² for 5 model configurations. [src: bacdive_phenotype_metal_tolerance]
- The comprehensive metal ecology project used XGBoost with spatial 5-fold block CV in an exploratory analysis called NB29. [src: comprehensive_metal_ecology]
- The ENIGMA genotype-to-phenotype project used the SHAP TreeExplainer. It decomposes each growth prediction into contributions from individual KOs (KEGG orthologs) and condition features. Global importance is the mean |SHAP| across predictions. [src: genotype_to_phenotype_enigma]

## Phylogenetic-blocked CV on BacDive

Two configurations in the 5-fold phylogenetic-blocked CV differ widely. The gene-count-only model has R² = 0.063, RMSE (root mean square error) = 0.045, n = 3,994 and 1 feature. [src: bacdive_phenotype_metal_tolerance] The full combined model has R² = 0.633, RMSE = 0.028, n = 3,994 and 17 features. [src: bacdive_phenotype_metal_tolerance]

SHAP importance in the full model ranks taxonomic class/order codes and `n_metal_clusters` as the top predictors. [src: bacdive_phenotype_metal_tolerance] Phenotype features contribute minimally to individual predictions once taxonomy is included. The report reads this as classical microbiology phenotypes acting as phylogenetic proxies, not independent predictors of metal tolerance. [src: bacdive_phenotype_metal_tolerance] See [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]] and [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]].

## Spatial-block CV on community metal-gene density (NB29)

NB29 predicts community-weighted mean (CWM) metal-gene density from environmental variables. The target is mean_n_metal_clusters, weighted by relative abundance (trait mean=12.7, SD=8.2). The predictors are pH, temperature, precipitation, elevation, NDVI, clay, lat/lon and log_Cu/Zn/Pb/Ni. [src: comprehensive_metal_ecology]

Prediction in held-out geographic blocks is poor. Mean CV RMSE is 11.89, ranging from 19.37 in Block 0 to 6.20 in Block 3. This is comparable to the within-sample SD (standard deviation). [src: comprehensive_metal_ecology]

SHAP shows that Cu+Zn+Pb+Ni contribute 45.9% of mean |SHAP|. The top predictor is log_Ni_ppm, with mean |SHAP|=2.23. [src: comprehensive_metal_ecology]

The report calls its hypothesis only partially supported. Metals contribute beyond pH and climate in SHAP, but overall predictive power is low (RMSE ≈ SD). [src: comprehensive_metal_ecology]

The report reads the metal-dominated SHAP and the poor spatial-block RMSE as consistent with NB28. On this reading, metals structure community composition, but spatial heterogeneity makes environment-to-CWM transfer generalise poorly across regions. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].

## SHAP with correlated features (ENIGMA)

Naive SHAP on 4,305 KOs splits credit across correlated gene blocks. [src: genotype_to_phenotype_enigma] Grouping features at |r|>0.8 reveals a 63-feature genome-scale axis that dominates with small training sets. [src: genotype_to_phenotype_enigma] The report sums SHAP within groups to avoid credit-splitting. It reads individual SHAP values inside a group as "this group matters", not "this specific KO matters". [src: genotype_to_phenotype_enigma] See [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features]].
