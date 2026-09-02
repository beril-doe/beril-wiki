---
type: "Concept"
description: "Five phenotypic dimensions separate general sensitivity from substrate-specific requirements."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md"]
---
# Condition-space dimensionality separates general sensitivity from substrate-specific requirements

Condition-space dimensionality describes how many independent axes are needed to represent gene-dependent growth effects across tested substrates. In the *Acinetobacter baylyi* ADP1 deletion collection, the evidence supports a multidimensional phenotype space in which general growth sensitivity is distinct from substrate-specific metabolic requirements. [src: adp1_deletion_phenotypes]

## Key evidence

The analysis used a complete growth matrix of 2,034 genes measured across 8 carbon sources, with growth ratios defined as mutant/wild-type values. [src: adp1_deletion_phenotypes] Growth ratios below 1.0 indicated growth defects, whereas values above 1.0 indicated no defect or a slight growth advantage from experimental normalization. [src: adp1_deletion_phenotypes]

Principal component analysis (PCA), a method that summarizes correlated variation into orthogonal components, found that 5 components captured 82% of the variance in the 2,034×8 matrix. [src: adp1_deletion_phenotypes] PC1 explained 36.7% of the variance and represented general growth sensitivity because all conditions loaded positively on it. [src: adp1_deletion_phenotypes] PC2 explained 12.7% of the variance and isolated urea, which had a loading of +0.75, separating nitrogen metabolism from carbon metabolism. [src: adp1_deletion_phenotypes] No single component captured more than 37% of the variance, which supports a multidimensional interpretation rather than a single dominant sensitivity axis. [src: adp1_deletion_phenotypes]

Pairwise Pearson correlations were moderate at best: acetate–butanediol had the highest correlation at r = 0.58, while the median across all 28 condition pairs was r = 0.25. [src: adp1_deletion_phenotypes] These correlations support approximately 5 independent dimensions of phenotypic information rather than a simple two-group model contrasting demanding and robust conditions. [src: adp1_deletion_phenotypes]

## General sensitivity and substrate-specific requirements

The condition space contains a broad sensitivity axis, but the substrate profiles are not interchangeable. [src: adp1_deletion_phenotypes] The 8 carbon sources formed demanding, moderate, and robust tiers, with urea, acetate, and butanediol in the demanding tier; asparagine and lactate in the moderate tier; and glucarate, glucose, and quinate in the robust tier. [src: adp1_deletion_phenotypes] Mean growth ratios ranged from 0.41 on urea to 1.36 on quinate, and the fraction of genes with severe defects at growth ratio < 0.5 ranged from 97.9% on urea to 1.6% on quinate. [src: adp1_deletion_phenotypes]

The tier structure alone does not explain the matrix because condition-specific requirements occupy additional axes. [src: adp1_deletion_phenotypes] A total of 625 genes, or 31% of the complete matrix, had a condition-specificity score ≥ 1.0, indicating that their growth importance was concentrated on one carbon source. [src: adp1_deletion_phenotypes] Quinate selected pcaC, pcaG, pcaH, pcaB, quiA, quiB, pqqC, and pqqD for protocatechuate/quinate degradation and PQQ biosynthesis, while urea selected ureA, ureB, ureC, ureD, ureE, ureF, and ureG for the urease complex. [src: adp1_deletion_phenotypes] The other substrates likewise selected pathway-linked genes, including fatty acid β-oxidation and the glyoxylate shunt on acetate, the Entner-Doudoroff pathway and PQQ-glucose dehydrogenase on glucose, and respiratory and lactate-associated genes on lactate. [src: adp1_deletion_phenotypes]

The quinate-specific gene set contained 51 genes at specificity > 0.5 and z < -1. [src: adp1_deletion_phenotypes] It included core aromatic degradation genes and NADH-ubiquinone oxidoreductase subunits from respiratory Complex I, suggesting the hypothesis that aromatic catabolism creates distinctive electron-transport-chain demands. [src: adp1_deletion_phenotypes] PQQ biosynthesis genes were condition-specific for both quinate and glucose, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [src: adp1_deletion_phenotypes]

## Relation to phenotype architecture

Hierarchical clustering produced an optimal K = 3 but a low silhouette score of 0.24. [src: adp1_deletion_phenotypes] The two large modules contained 1,160 and 850 genes and represented broadly sensitive versus broadly tolerant profiles, while no specific functional enrichment survived false discovery rate (FDR) correction. [src: adp1_deletion_phenotypes] A small module of 24 genes was the exception, showing extreme quinate-specific defects with a mean quinate z-score of -7.28 and near-zero scores on other conditions. [src: adp1_deletion_phenotypes] This supports a continuous condition-dependent essentiality gradient with one discrete aromatic-degradation module, rather than a phenotype space composed primarily of discrete functional categories. [src: adp1_deletion_phenotypes]

This finding **supports** [[concepts/condition-specific-fitness]] by showing that fitness effects are distributed across multiple substrate-linked dimensions rather than captured by a single global essentiality score. [src: adp1_deletion_phenotypes] It **refines** [[concepts/gene-essentiality]] because broad sensitivity and substrate-specific importance represent different components of gene importance. [src: adp1_deletion_phenotypes] The result also **supports** the use of [[entities/principal-component-analysis]] for separating shared sensitivity from condition-specific variation in deletion-phenotype matrices. [src: adp1_deletion_phenotypes]

## Tensions

The approximately 5 independent dimensions are inferred from only 8 tested carbon sources, so the dimensionality may increase when additional conditions are measured. [src: adp1_deletion_phenotypes] The low clustering silhouette score and absence of FDR-significant functional enrichments favor a gradient interpretation, but they do not exclude additional discrete modules that would emerge under a broader condition panel or with improved measurement precision. [src: adp1_deletion_phenotypes]

## Open Directions

- Measure the same deletion collection across an expanded condition panel and use PCA or independent component analysis to test whether the approximately 5-dimensional structure remains stable or increases with substrate diversity. [src: adp1_deletion_phenotypes]
- Replicate the single-timepoint growth measurements with technical replicates and quantify measurement error to test whether condition-specificity scores ≥ 1.0 distinguish biological substrate requirements from noise. [src: adp1_deletion_phenotypes]
- Map the 625 condition-specific genes onto pathway annotations and compare their loadings across conditions to determine which metabolic modules define the additional axes beyond general sensitivity. [src: adp1_deletion_phenotypes]
- Test the hypothesis that quinate and protocatechuate catabolism impose distinctive respiratory-chain demands by measuring respiratory Complex I mutants under quinate, glucose, and related aromatic substrates. [src: adp1_deletion_phenotypes]
- Reanalyze the 24-gene quinate module with additional aromatic substrates to test whether it is specific to quinate or represents a broader aromatic-catabolism axis. [src: adp1_deletion_phenotypes]
