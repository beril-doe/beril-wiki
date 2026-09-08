---
type: Summary
description: BacDive phenotypes add no predictive power beyond taxonomy for metal
  tolerance
doc_type: short
full_text: ../sources/bacdive_phenotype_metal_tolerance__REPORT.md
title: BacDive Phenotype Signatures of Metal Tolerance
sources:
- id: bacdive_phenotype_metal_tolerance
  resource: ../sources/bacdive_phenotype_metal_tolerance__REPORT.md
  title: bacdive phenotype metal tolerance
---
# BacDive Phenotype Signatures of Metal Tolerance

## Overview

This study bridges [bacdive](../entities/bacdive.md) phenotypes to genome-based metal tolerance scores from the [metal-fitness-atlas](../entities/metal-fitness-atlas.md), testing whether classical microbiology features independently predict metal tolerance or primarily reflect phylogenetic structure. The bridge contains 97,334 BacDive strains; 37,368 (38.4%) match a pangenome species and metal score, representing 5,647 unique GTDB species, including 3,994 species with at least 5 phenotype features. Ten phenotype features were tested, with 7 of 10 significant after FDR (false discovery rate) correction. [^bacdive_phenotype_metal_tolerance]

## Key Findings

### Phenotype associations

Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species), the largest effect among tested phenotype features. Class-stratified analysis could not test the association within taxonomic classes because the signal is almost entirely between-lineage, especially between Gram-positive Actinomycetes and Gram-negative Proteobacteria; the association is mechanistically plausible because the Gram-negative outer membrane can restrict metal-cation uptake, but it is statistically confounded with phylogeny. [^bacdive_phenotype_metal_tolerance]

Seven features passed FDR correction at q < 0.05: Gram stain (d = -0.610, q = 4.0e-60), oxidase (d = +0.530, q = 1.3e-24), motility (d = +0.345, q = 7.2e-23), urease (d = -0.175, q = 9.1e-06), enzyme breadth (rho = -0.058, q = 8.2e-04), nitrate reduction (d = +0.100, q = 7.4e-03), and catalase (d = +0.104, q = 4.1e-02). H₂S production did not pass correction (d = -0.867, q = 7.3e-02), while metabolite breadth (rho = -0.013, q = 4.7e-01) and acetate utilization (d = +0.005, q = 7.9e-01) were not significant. [^bacdive_phenotype_metal_tolerance]

Urease-positive species had lower metal tolerance scores (d = -0.18, p < 1e-5), reversing the prediction that urease-associated nickel handling would confer nickel tolerance. The effect was driven by Actinomycetes (d = -0.59, p < 1e-16); it disappeared within Gammaproteobacteria (d = +0.08, ns) and Bacilli (d = +0.06, ns), supporting phylogenetic confounding rather than a general urease effect. [^bacdive_phenotype_metal_tolerance]

The anaerobe-aerobe difference was negligible (d = -0.016, p = 0.55) among 3,751 species with oxygen-tolerance data. Facultative anaerobes had the highest mean score (0.221), compared with aerobes (0.216) and anaerobes (0.215); the three-group Kruskal-Wallis test was marginally significant (H = 8.53, p = 0.014), but the effect was biologically trivial. [^bacdive_phenotype_metal_tolerance]

Catalase showed a Simpson's-paradox pattern: the overall association was positive (d = +0.10), but catalase-negative species scored higher within Actinomycetes (d = -0.62, p < 1e-5), Gammaproteobacteria (d = -0.49, p = 0.004), and Betaproteobacteria (d = -0.51, p = 0.006). The overall positive association therefore reflected between-class composition rather than a consistent within-class relationship. [^bacdive_phenotype_metal_tolerance]

### Predictive models and phylogenetic confounding

Taxonomy alone explained 35.4% of metal tolerance variance, phenotype features alone explained 16.3%, and taxonomy plus phenotype yielded R² = 0.345, slightly below taxonomy alone; the phenotype-plus-taxonomy change was delta R² = -0.009. Adding the number of metal resistance gene clusters (`n_metal_clusters`) increased the full model to R² = 0.633, indicating that genome-encoded resistance repertoire was the strongest predictor in this analysis. [^bacdive_phenotype_metal_tolerance]

In 5-fold phylogenetic-blocked cross-validation, the gene-count-only model had R² = 0.063 and RMSE = 0.045; phenotype only had R² = 0.163 and RMSE = 0.043; taxonomy only had R² = 0.354 and RMSE = 0.038; taxonomy plus phenotype had R² = 0.345 and RMSE = 0.038; and the full model had R² = 0.633 and RMSE = 0.028. Every model used n = 3,994 species; the models used 1, 13, 3, 16, and 17 features, respectively. [^bacdive_phenotype_metal_tolerance]

SHAP (Shapley additive explanation) feature importance from the full XGBoost model placed taxonomic class/order codes and `n_metal_clusters` among the top predictors, while phenotype features contributed minimally after taxonomy was included. This supports the interpretation that the measured phenotypes are phylogenetic proxies rather than independent predictors of the composite metal tolerance score. [^bacdive_phenotype_metal_tolerance]

### Data coverage and direct validation

The analysis included 97,334 BacDive strains, 37,368 matched strains (38.4%), 5,647 unique GTDB species, 3,994 species with at least 5 phenotype features, 10 tested phenotype features, and 9 taxonomic classes with at least 50 species. Feature-level coverage ranged from 43,378 strains with isolation-source data and 29,784 with metabolite-breadth data to 5,254 with H₂S-production data and 1,980 with acetate-utilization data; matched strains ranged from 22,581 to 475, and species with metal scores ranged from 4,531 to 422 across these features. [^bacdive_phenotype_metal_tolerance]

The direct Fitness Browser–BacDive validation contained 12 organisms representing 6 unique species: Cupriavidus basilensis, Methanococcus maripaludis, Ralstonia solanacearum, Pseudomonas simiae, Azospirillum brasilense, and Pseudomonas fluorescens. All Gram-typed organisms were Gram-negative, preventing within-set testing of the strongest association; all urease-typed organisms were urease-negative yet were routinely tested against nickel. The single anaerobe, Methanococcus maripaludis, had only 1 metal tested versus 4–5 for aerobes, so n = 1 was not interpretable. [^bacdive_phenotype_metal_tolerance]

The study's hypothesis outcomes were: H1a, Gram-negative higher metal scores, supported univariately but phylogenetically confounded; H1b, anaerobes better tolerate redox metals, not supported (d = -0.02, ns); H1c, broader metabolism predicts higher scores, not supported (rho = -0.01, ns); H1d, catalase-positive organisms better tolerate selected redox metals, marginally supported (d = +0.10, q = 0.04); H1e, urease-positive organisms better tolerate nickel, reversed (d = -0.18) and driven by Actinomycetes; and H1f, H₂S producers better tolerate Zn, Cu, and Cd, unreliable because only 8 negative controls produced an effect estimate likely inflated by small-sample bias. [^bacdive_phenotype_metal_tolerance]

## Caveats

The Metal Fitness Atlas scores are genome-based predictions rather than direct metal-tolerance measurements. Controlling for `n_metal_clusters` mitigates circular reasoning in partial correlations, but the associations remain phenotype-to-genome correlations rather than phenotype-to-phenotype measurements. [^bacdive_phenotype_metal_tolerance]

Species-name matching recovered 5,647 of 27,702 GTDB species (38.4%); GCA accession matching was not implemented and could recover additional links. [^bacdive_phenotype_metal_tolerance]

The 12-organism direct validation was underpowered: all Gram-typed organisms were Gram-negative, preventing within-set testing of H1a. [^bacdive_phenotype_metal_tolerance]

BacDive testing is biased toward well-studied organisms, including Pseudomonas and Escherichia coli, which have many phenotype tests, whereas poorly studied species have sparse data. [^bacdive_phenotype_metal_tolerance]

The H₂S result is underpowered because only 8 H₂S-negative species were present in the matched set; consequently, d = -0.87 is unreliable and likely inflated by small-sample bias. [^bacdive_phenotype_metal_tolerance]

The composite-score analysis does not establish metal-specific mechanisms. Per-metal scores would be needed to test whether catalase predicts copper, urease predicts nickel, or H₂S predicts zinc, copper, and cadmium tolerance. [^bacdive_phenotype_metal_tolerance]

Suggested follow-up includes GCA accession matching; PGLS (phylogenetic generalized least squares) or phylogenetic PCA to remove phylogenetic signal; inclusion of BacDive machine-learning-predicted phenotypes with attention to model-dependent bias; and experimental testing of the underpowered H₂S hypothesis. Urease-positive and urease-negative organisms from the same taxonomic class should be profiled with RB-TnSeq (random barcode transposon sequencing) under nickel and other metals to test nickel-specific rather than general tolerance. [^bacdive_phenotype_metal_tolerance]

## Slots Into

- [environmental-resistome](../concepts/environmental-resistome.md) — The full model's R² = 0.633 and the dominance of `n_metal_clusters` support genome-encoded metal-resistance repertoire as the strongest predictor of metal tolerance. [^bacdive_phenotype_metal_tolerance]
- [pangenome-integration](../concepts/pangenome-integration.md) — The BacDive-to-pangenome bridge matched 37,368 strains (38.4%) and enabled species-level phenotype–metal-score integration across 5,647 GTDB species. [^bacdive_phenotype_metal_tolerance]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — The proposed per-metal analyses and matched-strain nickel experiments address whether phenotypes predict metal-specific rather than composite tolerance. [^bacdive_phenotype_metal_tolerance]

[^bacdive_phenotype_metal_tolerance]: [bacdive phenotype metal tolerance](../sources/bacdive_phenotype_metal_tolerance__REPORT.md)
