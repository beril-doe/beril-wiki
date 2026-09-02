---
type: "Method"
description: "Dimensionality-reduction method for detecting ecosystem-associated pathway structure"
sources: ["summaries/ecotype_functional_differentiation__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Principal component analysis

## What this entity is

Principal component analysis (PCA) is a dimensional-reduction method used in this report before [[entities/kmeans-clustering]] to identify gene-content ecotypes from bacterial genome profiles. [src: ecotype_functional_differentiation]

**Canonical name:** Principal component analysis. [src: ecotype_functional_differentiation]

**Known alias:** PCA. [src: ecotype_functional_differentiation]

**Stable external identifier:** No stable external identifier was reported for this method in the document. [src: ecotype_functional_differentiation]

## Use in ecotype functional differentiation

The analysis applied PCA with up to 50 components before KMeans clustering of bacterial genomes from the BERDL pangenome database. [src: ecotype_functional_differentiation]

The PCA–KMeans workflow searched cluster counts from k = 2 to k = 6 and selected the configuration with the best silhouette score. [src: ecotype_functional_differentiation]

Valid gene-content ecotypes were identified in 12 of 15 sampled species, assigning 1,820 genomes across 12 species spanning 6 phyla. [src: ecotype_functional_differentiation]

The species averaged 3.7 ecotypes, with a range of 2–6, and the mean silhouette score was 0.215 with a median of 0.174. [src: ecotype_functional_differentiation]

The clearest clustering occurred in *Erwinia amylovora*, with a silhouette score of 0.468 and 2 ecotypes, and in *Bacteroides xylanisolvens*, with a silhouette score of 0.366 and 6 ecotypes. [src: ecotype_functional_differentiation]

The weakest reported clustering signals occurred in *Staphylococcus simulans*, with a silhouette score of 0.118, and *Streptococcus pseudopneumoniae*, with a silhouette score of 0.131. [src: ecotype_functional_differentiation]

## Community and ecosystem metabolic-ecology applications

The NMDC community analysis **extends** PCA from genome-profile ecotype discovery to ecosystem-scale pathway-completeness structure: it applied PCA to a 220-sample × 80-pathway matrix. [src: nmdc_community_metabolic_ecology]

PC1 explained 49.4% of variance, PC2 explained 16.6%, and PC1–5 explained 83.0% in total. [src: nmdc_community_metabolic_ecology] PCA separated Soil and Freshwater communities strongly: the pairwise comparison had Mann-Whitney U = 3,674 and p < 0.0001, with median PC1 values of +3.86 for Soil and −6.28 for Freshwater. [src: nmdc_community_metabolic_ecology]

The Pseudomonas carbon-ecology analysis **supports and broadens** this use of PCA by applying it to 62 GapMind carbon-pathway profiles across species. The first 5 components captured 74.9% of variance, with PC1 explaining 31.2% and PC2 17.9%. [src: pseudomonas_carbon_ecology]

In that analysis, the primary PCA axis was dominated by the split between *Pseudomonas* s.s. and *Pseudomonas_E*, driven by sugar-pathway loss; lifestyle categories substantially overlapped within *Pseudomonas_E*. This **refines** the community result: PCA can reveal strong ecosystem-associated structure, but the dominant axis may reflect deep phylogenetic or subgenus differences rather than fine-grained lifestyle. [src: pseudomonas_carbon_ecology]

Together, these applications **support** the existing use of PCA for identifying structured gene-content variation while **refining** the interpretation from within-species ecotypes to community metabolic-potential and species-level carbon-capability gradients. [src: nmdc_community_metabolic_ecology, pseudomonas_carbon_ecology]

## Interpretation and limitations

The PCA-based clustering supports the finding that within-species gene-content ecotypes can show systematic COG functional differentiation, because all 12 species with valid clusters had at least one significantly differentiated COG category. [src: ecotype_functional_differentiation]

The report cautions that PCA followed by KMeans may be affected by clustering assumptions, sampling limitations, annotation coverage, and phylogenetic confounding. [src: ecotype_functional_differentiation]

KMeans was used because [[entities/hdbscan]] was unavailable on the cluster; unlike HDBSCAN, KMeans assumes spherical clusters and requires a selected value of k. [src: ecotype_functional_differentiation]

Without within-species phylogenetic controls such as core-genome trees, the PCA-derived ecotype assignments cannot distinguish ecological adaptation from phylogenetic or demographic substructure. [src: ecotype_functional_differentiation]

In the NMDC application, PCA separation is likewise consistent with distinct metabolic configurations across habitats but does not establish whether the differences arise from habitat physicochemistry, taxonomic composition, or both. [src: nmdc_community_metabolic_ecology]

The Pseudomonas analysis **strengthens** this limitation: its PCA signal was primarily a subgenus division, and the study did not explicitly control for phylogenetic non-independence among species. [src: pseudomonas_carbon_ecology] The report therefore proposes phylogenetic generalized least squares (PGLS), a regression method that accounts for phylogenetic relatedness, or phylogenetic logistic regression using the GTDB species tree. [src: pseudomonas_carbon_ecology]

## Related pages

- [[summaries/ecotype_functional_differentiation__REPORT]] — source summary describing the PCA-based ecotype analysis. [src: ecotype_functional_differentiation]
- [[summaries/nmdc_community_metabolic_ecology__REPORT]] — source summary describing the community pathway-completeness PCA. [src: nmdc_community_metabolic_ecology]
- [[summaries/pseudomonas_carbon_ecology__REPORT]] — source summary describing PCA of Pseudomonas carbon-pathway profiles. [src: pseudomonas_carbon_ecology]
- [[concepts/ecotype-environment-gene-content]] — cross-document concept concerning within-species gene-content ecotypes and environmental differentiation. [src: ecotype_functional_differentiation]
- [[concepts/pangenome-integration]] — cross-document concept concerning pangenome-based gene-content analysis. [src: ecotype_functional_differentiation]
- [[entities/kmeans-clustering]] — clustering method paired with PCA in the reported workflow. [src: ecotype_functional_differentiation]
- [[entities/hdbscan]] — alternative clustering method identified as unavailable for this analysis. [src: ecotype_functional_differentiation]
