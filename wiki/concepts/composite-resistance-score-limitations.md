---
type: "Concept"
description: "Why composite resistance scores are insufficient for mechanistic inference"
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md"]
---
# Limits of Composite Resistance Scores for Mechanistic Inference

Composite resistance scores summarize tolerance across multiple metals or conditions, but they do not by themselves identify the metal-specific mechanisms producing that tolerance. The BacDive analysis illustrates this limitation by comparing classical phenotypes with genome-based predictions from the [[entities/metal-fitness-atlas]], rather than with direct metal-tolerance measurements. [src: bacdive_phenotype_metal_tolerance]

The study used 97,334 [[entities/bacdive]] strains, of which 37,368 (38.4%) matched a pangenome species and metal score, covering 5,647 unique GTDB species. [src: bacdive_phenotype_metal_tolerance] Among these, 3,994 species had at least 5 phenotype features and were used for the principal predictive comparisons. [src: bacdive_phenotype_metal_tolerance]

## Evidence that the composite score is not mechanistically specific

The strongest univariate association was between Gram stain and the composite metal-tolerance score: Gram-negative species scored higher than Gram-positive species with Cohen's d = -0.61, p < 1e-60, and n = 3,272 species. [src: bacdive_phenotype_metal_tolerance] This **supports** [[concepts/environmental-resistome]] at the level of broad genome-associated resistance patterns, but it does not establish that the Gram-negative envelope causes tolerance to any particular metal. [src: bacdive_phenotype_metal_tolerance]

The Gram-stain association was almost entirely between lineages, especially between Gram-positive Actinomycetes and Gram-negative Proteobacteria, and could not be tested within taxonomic classes because of this structure. [src: bacdive_phenotype_metal_tolerance] Thus, a strong association with a composite score can reflect lineage composition rather than a transferable mechanism. [src: bacdive_phenotype_metal_tolerance]

Urease-positive species had lower composite metal-tolerance scores, with d = -0.18 and p < 1e-5, reversing the prediction that urease-associated nickel handling would confer nickel tolerance. [src: bacdive_phenotype_metal_tolerance] The effect was driven by Actinomycetes, where d = -0.59 and p < 1e-16, but disappeared within Gammaproteobacteria, where d = +0.08 and was not significant, and Bacilli, where d = +0.06 and was not significant. [src: bacdive_phenotype_metal_tolerance] This **refines** the interpretation of the composite score: an apparent phenotype–resistance relationship may fail when tested within the lineage in which the proposed mechanism should operate. [src: bacdive_phenotype_metal_tolerance]

Catalase provides a second example of non-mechanistic aggregation. [src: bacdive_phenotype_metal_tolerance] Its overall association with the composite score was positive, d = +0.10, but catalase-negative species scored higher within Actinomycetes, with d = -0.62 and p < 1e-5, Gammaproteobacteria, with d = -0.49 and p = 0.004, and Betaproteobacteria, with d = -0.51 and p = 0.006. [src: bacdive_phenotype_metal_tolerance] The overall result therefore reflected between-class composition rather than a consistent within-class relationship. [src: bacdive_phenotype_metal_tolerance]

Other phenotype associations also demonstrate why composite scores should not be read as metal-specific evidence. [src: bacdive_phenotype_metal_tolerance] Seven of 10 tested features passed FDR (false discovery rate) correction at q < 0.05, including Gram stain, oxidase, motility, urease, enzyme breadth, nitrate reduction, and catalase, while metabolite breadth and acetate utilization were not significant. [src: bacdive_phenotype_metal_tolerance] H₂S production did not pass correction, with d = -0.867 and q = 7.3e-02, and only 8 H₂S-negative species were present, making that estimate unreliable and likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance]

## Predictive models and circularity risk

Taxonomy alone explained 35.4% of composite metal-tolerance variance, phenotype features alone explained 16.3%, and taxonomy plus phenotype yielded R² = 0.345, slightly below taxonomy alone at R² = 0.354. [src: bacdive_phenotype_metal_tolerance] The phenotype-plus-taxonomy change was delta R² = -0.009, indicating that the measured phenotypes added little independent predictive information after taxonomy was included. [src: bacdive_phenotype_metal_tolerance]

Adding the number of metal resistance gene clusters, `n_metal_clusters`, increased the full model to R² = 0.633. [src: bacdive_phenotype_metal_tolerance] In 5-fold phylogenetic-blocked cross-validation, the gene-count-only model had R² = 0.063 and RMSE = 0.045; phenotype only had R² = 0.163 and RMSE = 0.043; taxonomy only had R² = 0.354 and RMSE = 0.038; taxonomy plus phenotype had R² = 0.345 and RMSE = 0.038; and the full model had R² = 0.633 and RMSE = 0.028. [src: bacdive_phenotype_metal_tolerance]

These results **support** the interpretation that genome-encoded resistance repertoire is more predictive of the composite score than the tested classical phenotypes, but they do not prove that the resistance-gene count captures the causal mechanism for each metal. [src: bacdive_phenotype_metal_tolerance] The score itself is a genome-based prediction rather than a direct measurement of metal tolerance, so correlations between phenotype and score remain phenotype-to-genome correlations rather than phenotype-to-phenotype measurements. [src: bacdive_phenotype_metal_tolerance] Controlling for `n_metal_clusters` reduces one form of circular reasoning in partial correlations, but it does not convert the composite score into a mechanistic assay. [src: bacdive_phenotype_metal_tolerance]

SHAP (Shapley additive explanation) importance from the full XGBoost model placed taxonomic class/order codes and `n_metal_clusters` among the top predictors, while phenotype features contributed minimally after taxonomy was included. [src: bacdive_phenotype_metal_tolerance] This **supports** [[concepts/phylogenetic-confounding-of-phenotype-associations]] and **refines** [[concepts/composite-resistance-score-limitations]] by showing that predictive importance does not establish biological specificity. [src: bacdive_phenotype_metal_tolerance]

## Limits of direct validation

The direct Fitness Browser–BacDive validation contained 12 organisms representing 6 unique species: Cupriavidus basilensis, Methanococcus maripaludis, Ralstonia solanacearum, Pseudomonas simiae, Azospirillum brasilense, and Pseudomonas fluorescens. [src: bacdive_phenotype_metal_tolerance] All Gram-typed organisms were Gram-negative, preventing within-set testing of the strongest Gram-stain association. [src: bacdive_phenotype_metal_tolerance] All urease-typed organisms were urease-negative despite being routinely tested against nickel, and the single anaerobe, Methanococcus maripaludis, had only 1 metal tested versus 4–5 for aerobes, so the anaerobe comparison was not interpretable. [src: bacdive_phenotype_metal_tolerance]

The study therefore did not establish that catalase predicts copper tolerance, urease predicts nickel tolerance, or H₂S production predicts zinc, copper, or cadmium tolerance. [src: bacdive_phenotype_metal_tolerance] The composite-score result is consequently best treated as an association and prioritization signal, not as evidence for a metal-specific mechanism. [src: bacdive_phenotype_metal_tolerance]

## Relation to the wider wiki

This page **supports** [[concepts/condition-specific-fitness]] because the proposed remedy is to replace aggregate scores with measurements resolved by metal and experimental condition. [src: bacdive_phenotype_metal_tolerance] It also **refines** [[concepts/circularity-in-metabolic-model-validation]] by showing that a genome-derived target can be useful for prediction while remaining unsuitable as independent mechanistic validation. [src: bacdive_phenotype_metal_tolerance] The complete source analysis is available at [[summaries/bacdive_phenotype_metal_tolerance__REPORT]]. [src: bacdive_phenotype_metal_tolerance]

## Open Directions

- Match BacDive strains to GTDB genomes using GCA accessions and repeat the phenotype-to-score analysis to test whether the 38.4% species-name matching rate limited mechanistic resolution. [src: bacdive_phenotype_metal_tolerance]
- Replace the composite score with per-metal scores and use PGLS (phylogenetic generalized least squares) or phylogenetic PCA to test whether catalase predicts copper, urease predicts nickel, and H₂S production predicts zinc, copper, or cadmium tolerance after removing phylogenetic signal. [src: bacdive_phenotype_metal_tolerance]
- Assemble urease-positive and urease-negative organisms within the same taxonomic classes and apply [[entities/tnseq]] or [[entities/crispri]] under nickel and other metals to test nickel-specific mechanisms rather than general composite tolerance. [src: bacdive_phenotype_metal_tolerance]
- Experimentally test the H₂S hypothesis with balanced positive and negative controls under zinc, copper, and cadmium exposure to determine whether the observed d = -0.867 was a small-sample artifact. [src: bacdive_phenotype_metal_tolerance]
- Compare composite-score predictions with direct Fitness Browser growth or fitness measurements across matched organisms and metals to determine which resistance-gene features predict measured tolerance rather than a derived genome-based score. [src: bacdive_phenotype_metal_tolerance]
