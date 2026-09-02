---
type: "Concept"
description: "How uneven sampling and phylogenetic structure distort microbial phenotype inference"
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md"]
---
# Coverage and Study Bias in Microbial Phenotype Databases

Coverage and study bias in microbial phenotype databases can make apparently broad phenotype–genotype associations reflect uneven sampling, sparse feature measurements, and phylogenetic composition rather than independent biological relationships. [src: bacdive_phenotype_metal_tolerance]

The [[summaries/bacdive_phenotype_metal_tolerance__REPORT]] provides a case study by linking [[entities/bacdive]] phenotypes to genome-based metal-tolerance scores from the [[entities/metal-fitness-atlas]]. [src: bacdive_phenotype_metal_tolerance]

## Coverage of the BacDive–Pangenome Bridge

The bridge contained 97,334 BacDive strains, of which 37,368 (38.4%) matched a pangenome species and metal score. [src: bacdive_phenotype_metal_tolerance] These matches represented 5,647 unique GTDB species, including 3,994 species with at least 5 phenotype features. [src: bacdive_phenotype_metal_tolerance] Species-name matching recovered 5,647 of 27,702 GTDB species (38.4%), and GCA accession matching was not implemented. [src: bacdive_phenotype_metal_tolerance]

Coverage varied substantially among the ten tested phenotype features. [src: bacdive_phenotype_metal_tolerance] Feature-level coverage ranged from 43,378 strains with isolation-source data and 29,784 with metabolite-breadth data to 5,254 strains with H₂S-production data and 1,980 with acetate-utilization data. [src: bacdive_phenotype_metal_tolerance] Across these features, matched strains ranged from 22,581 to 475, while species with metal scores ranged from 4,531 to 422. [src: bacdive_phenotype_metal_tolerance]

These differences mean that apparently comparable phenotype tests can have very different effective sample sizes and species composition. [src: bacdive_phenotype_metal_tolerance] The H₂S comparison illustrates the problem: only 8 H₂S-negative species were present in the matched set, making its observed effect size of d = -0.87 unreliable and likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance]

## Taxonomic and Cultivation Bias

BacDive testing is biased toward well-studied organisms, including Pseudomonas and Escherichia coli, while poorly studied species have sparser phenotype data. [src: bacdive_phenotype_metal_tolerance] This study bias can couple phenotype availability to taxonomy, ecology, and research history, so database-wide associations may not represent uniform sampling across microbial diversity. [src: bacdive_phenotype_metal_tolerance]

The strongest univariate association was between Gram stain and metal tolerance: Gram-negative species had higher scores than Gram-positive species, with Cohen’s d = -0.61, p < 1e-60, and n = 3,272 species. [src: bacdive_phenotype_metal_tolerance] However, class-stratified analysis could not test this association within taxonomic classes because the signal was almost entirely between lineages, especially between Gram-positive Actinomycetes and Gram-negative Proteobacteria. [src: bacdive_phenotype_metal_tolerance] Thus, the result supports the need to distinguish phenotype coverage and lineage composition from within-lineage biological effects, connecting this case to [[concepts/phylogenetic-confounding-of-phenotype-associations]]. [src: bacdive_phenotype_metal_tolerance]

Urease provides a second example of coverage interacting with phylogeny. [src: bacdive_phenotype_metal_tolerance] Urease-positive species had lower metal-tolerance scores, with d = -0.18 and p < 1e-5, but the effect was driven by Actinomycetes, where d = -0.59 and p < 1e-16; it disappeared within Gammaproteobacteria, where d = +0.08 and was not significant, and Bacilli, where d = +0.06 and was not significant. [src: bacdive_phenotype_metal_tolerance]

Catalase showed a Simpson’s-paradox pattern in which the overall association was positive, with d = +0.10, while catalase-negative species scored higher within Actinomycetes, with d = -0.62 and p < 1e-5, Gammaproteobacteria, with d = -0.49 and p = 0.004, and Betaproteobacteria, with d = -0.51 and p = 0.006. [src: bacdive_phenotype_metal_tolerance] The overall catalase association therefore reflected between-class composition rather than a consistent within-class relationship. [src: bacdive_phenotype_metal_tolerance]

## Model Evidence for Coverage-Driven Interpretation

Taxonomy alone explained 35.4% of metal-tolerance variance, phenotype features alone explained 16.3%, and taxonomy plus phenotype yielded R² = 0.345, slightly below taxonomy alone, with delta R² = -0.009. [src: bacdive_phenotype_metal_tolerance] Adding the number of metal-resistance gene clusters, `n_metal_clusters`, increased the full model to R² = 0.633. [src: bacdive_phenotype_metal_tolerance]

In 5-fold phylogenetic-blocked cross-validation, the gene-count-only model had R² = 0.063 and RMSE = 0.045; the phenotype-only model had R² = 0.163 and RMSE = 0.043; the taxonomy-only model had R² = 0.354 and RMSE = 0.038; the taxonomy-plus-phenotype model had R² = 0.345 and RMSE = 0.038; and the full model had R² = 0.633 and RMSE = 0.028. [src: bacdive_phenotype_metal_tolerance] Every model used n = 3,994 species, with 1, 13, 3, 16, and 17 features, respectively. [src: bacdive_phenotype_metal_tolerance]

SHAP (Shapley additive explanation) feature importance from the full XGBoost model placed taxonomic class/order codes and `n_metal_clusters` among the top predictors, while phenotype features contributed minimally after taxonomy was included. [src: bacdive_phenotype_metal_tolerance] This supports the interpretation that the measured phenotypes were primarily phylogenetic proxies rather than independent predictors of the composite metal-tolerance score. [src: bacdive_phenotype_metal_tolerance]

## Direct-Validation Coverage Limits

The direct Fitness Browser–BacDive validation contained 12 organisms representing 6 unique species: Cupriavidus basilensis, Methanococcus maripaludis, Ralstonia solanacearum, Pseudomonas simiae, Azospirillum brasilense, and Pseudomonas fluorescens. [src: bacdive_phenotype_metal_tolerance] All Gram-typed organisms were Gram-negative, preventing within-set testing of the strongest Gram-stain association. [src: bacdive_phenotype_metal_tolerance] All urease-typed organisms were urease-negative despite being routinely tested against nickel. [src: bacdive_phenotype_metal_tolerance] The single anaerobe, Methanococcus maripaludis, had only 1 metal tested versus 4–5 for aerobes, so n = 1 was not interpretable. [src: bacdive_phenotype_metal_tolerance]

The direct validation therefore did not provide balanced coverage for the key phenotype contrasts. [src: bacdive_phenotype_metal_tolerance] This limitation complements the broader [[concepts/phenotype-database-coverage-bias]] concern that database observations can be constrained by which organisms were tested, which phenotypes were recorded, and which comparisons were possible. [src: bacdive_phenotype_metal_tolerance]

## Tensions

The study found seven of ten phenotype features significant after FDR correction: Gram stain, oxidase, motility, urease, enzyme breadth, nitrate reduction, and catalase. [src: bacdive_phenotype_metal_tolerance] However, phenotype features alone explained 16.3% of variance, taxonomy alone explained 35.4%, and adding phenotype features to taxonomy reduced the model to R² = 0.345. [src: bacdive_phenotype_metal_tolerance] The tension is therefore between widespread univariate significance and limited evidence that these phenotypes add independent predictive information after accounting for taxonomic structure. [src: bacdive_phenotype_metal_tolerance]

The Metal Fitness Atlas scores were genome-based predictions rather than direct metal-tolerance measurements. [src: bacdive_phenotype_metal_tolerance] Consequently, the observed associations were phenotype-to-genome correlations rather than phenotype-to-phenotype measurements, and controlling for `n_metal_clusters` mitigated circular reasoning in partial correlations without converting the analysis into direct experimental validation. [src: bacdive_phenotype_metal_tolerance]

## Open Directions

- Apply GCA accession matching to the BacDive and GTDB records, then quantify whether recovered species alter feature-level coverage and the estimated phenotype–metal-score associations. [src: bacdive_phenotype_metal_tolerance]
- Use PGLS (phylogenetic generalized least squares) or phylogenetic PCA on the matched 3,994-species set to test whether Gram stain, urease, catalase, and other phenotype associations persist after explicit removal of phylogenetic signal. [src: bacdive_phenotype_metal_tolerance]
- Reweight or stratify analyses by phenotype-test coverage and taxonomic representation, then test whether the model rankings and exact effect estimates change when well-studied lineages are prevented from dominating the comparison. [src: bacdive_phenotype_metal_tolerance]
- Add BacDive machine-learning-predicted phenotypes and compare their associations with experimentally recorded phenotypes to determine whether expanded coverage introduces model-dependent bias. [src: bacdive_phenotype_metal_tolerance]
- Assemble urease-positive and urease-negative organisms from the same taxonomic class and test them with RB-TnSeq (random barcode transposon sequencing) under nickel and other metals to distinguish nickel-specific effects from general tolerance. [src: bacdive_phenotype_metal_tolerance]
- Expand direct validation across Gram-positive and Gram-negative organisms, multiple oxygen-tolerance states, and balanced metal panels to determine whether the database associations reproduce in measured metal-tolerance phenotypes. [src: bacdive_phenotype_metal_tolerance]
