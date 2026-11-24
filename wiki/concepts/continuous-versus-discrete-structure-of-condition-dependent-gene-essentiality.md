---
type: "Concept"
description: "Whether gene growth requirements across conditions form discrete phenotypic modules or a continuum, and how many independent dimensions a condition panel provides; stops at gene-level clustering of deletion or fitness profiles."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md"]
---
# Continuous versus discrete structure of condition-dependent gene essentiality

In the Acinetobacter baylyi ADP1 deletion collection, gene growth requirements across 8 carbon sources look like a continuum, not a set of discrete modules, with one small quinate exception. [src: adp1_deletion_phenotypes] The 8 conditions give about 5 independent dimensions of information. [src: adp1_deletion_phenotypes] See [[entities/acinetobacter-baylyi-adp1]] and [[summaries/adp1_deletion_phenotypes__REPORT]].

## Conditions form tiers but not two groups

The 8 carbon sources fall into demanding, moderate and robust tiers, and the tiers hold across multiple defect thresholds. [src: adp1_deletion_phenotypes] Urea is the most demanding, with 97.9% of genes showing severe defects at ratio < 0.5. [src: adp1_deletion_phenotypes] Quinate is the most robust, with only 1.6% of genes defective. [src: adp1_deletion_phenotypes] Mean growth ratios span 3.3-fold, from 0.41 for urea to 1.36 for quinate. [src: adp1_deletion_phenotypes]

- Demanding (urea, acetate, butanediol): mean growth ratio 0.41–0.65, with defects at ratio < 0.8 in 95–100% of genes. [src: adp1_deletion_phenotypes]
- Moderate (asparagine, lactate): mean growth ratio 0.80–0.82, with defects at ratio < 0.8 in 37–45% of genes. [src: adp1_deletion_phenotypes]
- Robust (glucarate, glucose, quinate): mean growth ratio 1.25–1.36, with defects at ratio < 0.8 in 0.5–2.4% of genes. [src: adp1_deletion_phenotypes]

## How many independent dimensions

The report reads the 8 conditions as providing about 5 independent dimensions, far more than a two-group demanding-versus-robust model implies. [src: adp1_deletion_phenotypes] Another report in the corpus also gives about 5 dimensions. [src: aromatic_catabolism_network] Pairwise correlations are moderate at best. The highest is acetate–butanediol at r = 0.58, and the median across all 28 pairs is r = 0.25. [src: adp1_deletion_phenotypes] The original ADP1 study gives a mean inter-condition correlation of 0.38. [src: adp1_triple_essentiality] A separate analysis reports a mean pairwise defect correlation of 0.38, with a range of -0.03 to 1.0. [src: adp1_triple_essentiality]

PCA (principal component analysis) of the 2,034×8 growth matrix needs 5 components to capture 82% of variance. [src: adp1_deletion_phenotypes] No single component captures more than 37%. [src: adp1_deletion_phenotypes] PC1 (principal component 1) explains 36.7% and reflects general growth sensitivity, with all conditions loading positively. [src: adp1_deletion_phenotypes] PC2 explains 12.7% and isolates urea with loading = +0.75, separating nitrogen from carbon metabolism. [src: adp1_deletion_phenotypes] The remaining components distinguish specific carbon-source pairs. [src: adp1_deletion_phenotypes]

The report suggests that the diverse metabolic entry points of the carbon sources explain the independence. [src: adp1_deletion_phenotypes] It also suggests that more carbon sources, nitrogen sources or stress conditions would substantially increase phenotypic resolution. [src: adp1_deletion_phenotypes] The number is limited by the panel: only 8 carbon sources were tested, and the dimensions may increase with more conditions. [src: adp1_deletion_phenotypes]

## No discrete modules at gene level

Hierarchical clustering of genes by their 8-condition profiles gives an optimal K = 3 with a low silhouette score of 0.24. [src: adp1_deletion_phenotypes, discoveries] The score stays low across all tested k from 2 to 25, which the report takes as showing that the landscape lacks natural cluster boundaries. [src: adp1_deletion_phenotypes] The two large modules (1,160 and 850 genes) are broad generally sensitive and generally tolerant groups. [src: adp1_deletion_phenotypes] Neither has functional enrichment surviving FDR (false discovery rate) correction. [src: adp1_deletion_phenotypes] The report treats this clustering failure as informative, because it indicates a continuous phenotype landscape. [src: adp1_deletion_phenotypes] It concludes that essentiality varies continuously across conditions, not in discrete functional categories. [src: adp1_deletion_phenotypes] Most genes vary gradually in condition sensitivity. [src: adp1_deletion_phenotypes] A second report likewise concludes that growth importance is condition-dependent and continuous, and that neither FBA (flux balance analysis) nor TnSeq (transposon sequencing) captures this variation. [src: adp1_triple_essentiality]

The report proposes independent component analysis (ICA) in place of hierarchical clustering, to extract condition-specific signals from the gradient landscape. It suggests ICA may reveal latent factors that clustering misses. [src: adp1_deletion_phenotypes]

### The quinate exception

One small module of 24 genes has extreme quinate-specific defects, with mean z-score = -7.28 on quinate and near-zero on other conditions. [src: adp1_deletion_phenotypes] These are aromatic-degradation genes, and the module is the only discrete one in the dataset. [src: adp1_deletion_phenotypes] The report finds no other discrete modules in ADP1. [src: adp1_deletion_phenotypes] The discoveries digest repeats this: the landscape is a gradient apart from the tight 24-gene quinate-specific module. [src: discoveries] See also [[entities/ketoadipate-pathway]].

## Relation to the literature

The report says its continuity supports the adaptive-flexibility framework of Guzman et al. (2018), which argues that binary essential/non-essential labels miss condition-dependent effects. [src: adp1_deletion_phenotypes, discoveries] It describes the continuity as a gradient across conditions, not as discrete modules. [src: adp1_deletion_phenotypes]

## Tensions

- Nichols et al. (2011) found that chemical-genetic profiles in *E. coli* define phenotypic modules extending beyond operon boundaries. [src: adp1_deletion_phenotypes] The report finds no discrete modules in ADP1, only a gradient. [src: adp1_deletion_phenotypes]
- Many *E. coli* chemical-genomics conditions give correlated fitness profiles, while the ADP1 carbon-source requirements are largely independent. [src: adp1_deletion_phenotypes] The report suggests the difference may reflect single-gene deletions versus chemical perturbations, or a more interconnected ADP1 metabolism. [src: adp1_deletion_phenotypes]

## Open Directions

- Add nitrogen-source and stress conditions to the ADP1 deletion panel, then re-run PCA to test whether the ~5 dimensions grow with the panel.
- Run ICA on the 2,034×8 matrix to test whether it finds latent factors that hierarchical clustering misses.
- Compare deletion and chemical-perturbation profiles in one organism, to separate method effects from metabolic architecture as the cause of the ADP1–*E. coli* difference.
- Test whether other single-entry-point pathways form discrete modules when a matching condition is present, as quinate does.
