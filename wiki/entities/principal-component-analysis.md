---
type: "Method"
description: "Dimensionality reduction by principal components used to assess independent dimensions in multivariate data matrices; stops at clustering applied afterwards."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
aliases: ["PCA"]
---
# Principal component analysis

This page is about principal component analysis (PCA), a dimensionality reduction used to assess independent dimensions in multivariate data matrices. Three projects applied it: ADP1 growth phenotypes [src: adp1_deletion_phenotypes], NMDC community pathway completeness [src: nmdc_community_metabolic_ecology], and Pseudomonas carbon pathway profiles. [src: pseudomonas_carbon_ecology] Each result comes from a single dataset or organism group.

## Key facts

- Each project reports variance in the first five components: 82% for ADP1 [src: adp1_deletion_phenotypes], 83.0% for the NMDC ecosystem matrix [src: nmdc_community_metabolic_ecology], and 74.9% for Pseudomonas. [src: pseudomonas_carbon_ecology]

## ADP1 growth phenotypes

PCA of the 2,034×8 growth matrix of *Acinetobacter baylyi* ADP1 needs 5 components to capture 82% of variance. [src: adp1_deletion_phenotypes] No single component captures more than 37%. [src: adp1_deletion_phenotypes] The report reads this as about 5 independent dimensions of phenotypic information. That is more than a binary demanding/robust classification suggests. [src: adp1_deletion_phenotypes] See [[concepts/continuous-versus-discrete-structure-of-condition-dependent-gene-essentiality]].

PC1 explains 36.7% of variance and represents general growth sensitivity, with all conditions loading positively. [src: adp1_deletion_phenotypes] PC2 explains 12.7% and isolates urea (loading = +0.75). It separates nitrogen metabolism from carbon metabolism. [src: adp1_deletion_phenotypes] The remaining components distinguish specific carbon-source pairs. [src: adp1_deletion_phenotypes]

Only 8 carbon sources were tested, so the ~5 dimensions may increase with more conditions. [src: adp1_deletion_phenotypes]

## NMDC ecosystem pathway completeness

The matrix was 220 samples × 80 pathways of completeness. [src: nmdc_community_metabolic_ecology] PC1 explained 49.4% of variance and PC2 explained 16.6%. [src: nmdc_community_metabolic_ecology] Both differed across ecosystem types, with Kruskal-Wallis H = 52.98 for PC1 and H = 123.74 for PC2, both p < 0.0001. [src: nmdc_community_metabolic_ecology] See [[entities/kruskal-wallis-test-with-eta-squared-effect-size]] and [[concepts/ecosystem-differentiation-of-community-metabolic-potential]].

PC3, PC4 and PC5 explained 7.9%, 5.2% and 3.9%. [src: nmdc_community_metabolic_ecology] The top positive PC1 loadings point in the Soil direction. They are glucuronate (0.146), fumarate (0.144), succinate (0.143), lysine (0.140) and cellobiose (0.139). [src: nmdc_community_metabolic_ecology]

## Pseudomonas carbon pathways

PCA of the 62-pathway profiles captured 74.9% of variance in the first 5 components, with PC1 at 31.2%. [src: pseudomonas_carbon_ecology] Among 54 free-living and plant-associated species, PC2 explained 17.9%. [src: pseudomonas_carbon_ecology] The primary axis separates *Pseudomonas* s.s. from *Pseudomonas_E*, driven by sugar pathway loss. [src: pseudomonas_carbon_ecology] See [[concepts/host-adaptation-pathway-loss-in-pseudomonas-carbon-catabolism]].

This limits any lifestyle reading. The report cautions that the dominant PCA signal separates subgenera rather than lifestyles. [src: pseudomonas_carbon_ecology] See [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]] and [[concepts/carbon-pathway-profiles-as-predictors-of-environment-and-lifestyle]].
