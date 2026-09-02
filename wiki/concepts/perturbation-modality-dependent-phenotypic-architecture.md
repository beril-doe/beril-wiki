---
type: "Concept"
description: "How perturbation modality can shape observed phenotype architecture"
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md"]
---
# Genetic deletions and chemical perturbations may expose different phenotype architectures

## Core idea

Perturbation modality may influence whether experiments reveal continuous condition-dependent effects or discrete phenotypic modules. [src: adp1_deletion_phenotypes] The [[summaries/adp1_deletion_phenotypes__REPORT]] provides evidence from a single-gene deletion collection in *Acinetobacter baylyi* ADP1, while comparison with chemical-genetic profiles in *Escherichia coli* motivates the hypothesis that genetic deletions and chemical perturbations can expose different phenotype architectures. [src: adp1_deletion_phenotypes]

## Evidence from the ADP1 deletion collection

The ADP1 analysis measured 2,034 genes across 8 carbon sources and found a 3.3-fold range in mean growth ratios, from 0.41 on urea to 1.36 on quinate. [src: adp1_deletion_phenotypes] The growth ratio was defined as mutant growth divided by wild-type growth, with values below 1.0 indicating growth defects and values above 1.0 indicating no defect or a slight growth advantage from experimental normalization. [src: adp1_deletion_phenotypes]

The condition structure was predominantly continuous rather than sharply modular: hierarchical clustering produced an optimal K = 3 but a low silhouette score of 0.24, with two large modules containing 1,160 and 850 genes and representing broadly sensitive versus broadly tolerant profiles. [src: adp1_deletion_phenotypes] No specific functional enrichment survived false discovery rate (FDR) correction, where FDR controls the expected proportion of false discoveries among statistically significant results. [src: adp1_deletion_phenotypes]

The deletion data nevertheless contained one discrete exception: a 24-gene module showed extreme quinate-specific defects, with a mean quinate z-score of -7.28 and near-zero scores on other conditions. [src: adp1_deletion_phenotypes] These genes were aromatic degradation pathway genes, making the quinate module a discrete metabolic signature embedded within an otherwise graded phenotype landscape. [src: adp1_deletion_phenotypes]

Condition-specific effects were widespread: 625 genes, or 31% of the complete matrix, had a condition-specificity score ≥ 1.0. [src: adp1_deletion_phenotypes] The strongest condition-specific signals mapped to expected metabolic architectures, including aromatic degradation and PQQ biosynthesis on quinate, the urease complex on urea, fatty acid β-oxidation and the glyoxylate shunt on acetate, and the Entner-Doudoroff pathway and PQQ-dependent glucose dehydrogenase on glucose. [src: adp1_deletion_phenotypes]

The broader condition landscape also resisted a simple binary partition: principal component analysis (PCA), a method that summarizes correlated variation into orthogonal components, required 5 components to capture 82% of the variance, while the largest component explained 36.7%. [src: adp1_deletion_phenotypes] Pairwise Pearson correlations were moderate at best, with a maximum of r = 0.58 for acetate–butanediol and a median of r = 0.25 across all 28 condition pairs. [src: adp1_deletion_phenotypes]

## Modality-dependent interpretation

The ADP1 result supports the interpretation that single-gene deletions can expose a continuous gradient of condition-dependent fitness, with a small pathway-specific module superimposed on that gradient. [src: adp1_deletion_phenotypes] The report contrasts this pattern with discrete phenotypic modules reported for chemical-genetic profiles in *E. coli*, but does not establish whether the difference is caused by perturbation modality, organismal metabolism, experimental design, or some combination of these factors. [src: adp1_deletion_phenotypes]

Accordingly, the appropriate claim is a hypothesis rather than an established general rule: genetic deletions and chemical perturbations may expose different phenotype architectures because they alter biological systems through different perturbational routes. [src: adp1_deletion_phenotypes] An alternative hypothesis is that ADP1 metabolism is more interconnected than the system represented by the compared *E. coli* chemical-genetic profiles, causing single-gene deletions to produce a smoother landscape. [src: adp1_deletion_phenotypes]

This interpretation refines [[concepts/condition-specific-fitness]] by showing that condition-specific fitness can appear as a continuous distribution rather than only as discrete condition modules. [src: adp1_deletion_phenotypes] It also connects to [[concepts/gene-essentiality]], because the 625 condition-specific genes demonstrate why binary essential/non-essential labels do not capture the full phenotype architecture. [src: adp1_deletion_phenotypes] The result should be interpreted alongside [[concepts/perturbation-modality-dependent-phenotypic-architecture]] itself as a modality-comparison hypothesis, not as a cross-organism conclusion established by the ADP1 dataset alone. [src: adp1_deletion_phenotypes]

## Limits of the evidence

The growth ratios were single-timepoint measurements with unknown technical noise, so some condition-specificity scores may reflect measurement error as well as biology. [src: adp1_deletion_phenotypes] The complete matrix excluded 499 essential genes and 316 genes with incomplete data, biasing the analysis toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes] Only 8 carbon sources were tested, so the approximately 5 independent dimensions could increase when additional conditions are measured. [src: adp1_deletion_phenotypes] The low clustering silhouette score and absent FDR-significant enrichments support a gradient interpretation, but proposed independent component analysis and an expanded condition panel remained future work rather than completed analyses. [src: adp1_deletion_phenotypes]

## Open Directions

- Compare matched ADP1 single-gene deletions and chemical perturbations across the same 8 carbon sources, using identical growth measurements and hierarchical clustering, to test whether chemical perturbations produce more discrete modules than the deletion collection. [src: adp1_deletion_phenotypes]
- Repeat the comparison across an expanded condition panel and apply independent component analysis, asking whether the approximately 5 dimensions inferred from the current matrix remain stable or increase with broader environmental coverage. [src: adp1_deletion_phenotypes]
- Integrate deletion phenotypes with RB-TnSeq, or random barcode transposon sequencing, measurements under matched conditions and compare condition-specificity scores, to test whether perturbation modality changes the apparent continuity of fitness effects. [src: adp1_deletion_phenotypes]
- Reanalyze the ADP1 deletion matrix with replicate-aware error models and FDR-controlled module detection, asking whether the 24-gene quinate module remains discrete after technical noise is modeled. [src: adp1_deletion_phenotypes]
- Compare ADP1 and *E. coli* using matched perturbation types, condition panels, and clustering metrics, asking whether organismal metabolic interconnectedness or perturbation modality better explains the difference between continuous and discrete architectures. [src: adp1_deletion_phenotypes]
