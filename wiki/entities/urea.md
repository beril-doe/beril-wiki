---
type: "Compound"
description: "Nitrogenous compound used as a demanding ADP1 growth condition"
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Urea

## Identity

**Canonical name:** Urea. [src: acinetobacter_adp1_explorer]

**Known aliases:** No aliases were reported in the source document. [src: acinetobacter_adp1_explorer]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: acinetobacter_adp1_explorer]

## Key Facts

Urea was one of 8 carbon sources used to measure mutant growth fitness in the *Acinetobacter baylyi* ADP1 database. [src: acinetobacter_adp1_explorer]

The deletion-phenotype analysis **refines** urea’s characterization as a demanding condition: it had the lowest mean growth ratio, **0.41**, with **97.9%** of genes showing severe defects at growth ratio < 0.5 and **95–100%** defective at ratio < 0.8. [src: adp1_deletion_phenotypes] The respiratory-chain analysis **supports and refines** this characterization, reporting that urea was generally demanding and required everything in the reported respiratory-chain profile. [src: respiratory_chain_wiring]

Urea fitness had a pairwise correlation of **r = 0.11** with quinate fitness. [src: acinetobacter_adp1_explorer]

Urea fitness was weakly correlated with all other tested conditions, with correlations ranging from **r = 0.12-0.28**. [src: acinetobacter_adp1_explorer]

The report interprets the weak correlations as suggesting that urea catabolism involves a largely independent set of genes; this remains a dataset-specific hypothesis rather than an established cross-species finding. [src: acinetobacter_adp1_explorer] The new analysis **supports and refines** this interpretation: principal component analysis (PCA), which summarizes correlated variation into orthogonal components, isolated urea from carbon metabolism, with a loading of **+0.75** on PC2. [src: adp1_deletion_phenotypes]

Urea-specific genes included ureA, ureB, ureC, ureD, ureE, ureF, and ureG, representing the urease complex. [src: adp1_deletion_phenotypes]

These measurements are part of the ADP1-centered resource described in [[summaries/acinetobacter_adp1_explorer__REPORT]], which contributes mutant growth fitness data unavailable for ADP1 in the Fitness Browser. [src: acinetobacter_adp1_explorer]

The deletion analysis is described in [[summaries/adp1_deletion_phenotypes__REPORT]]. [src: adp1_deletion_phenotypes] The respiratory-chain interpretation is described in [[summaries/respiratory_chain_wiring__REPORT]]. [src: respiratory_chain_wiring]

## Related Pages

- [[concepts/condition-specific-fitness]] — condition-specific mutant-growth fitness patterns involving urea. [src: acinetobacter_adp1_explorer]
- [[concepts/gene-essentiality]] — urea’s demanding-condition phenotype and urea-specific gene requirements refine condition-dependent essentiality. [src: adp1_deletion_phenotypes]
- [[entities/urease-complex]] — urea-specific genes include the urease-complex components. [src: adp1_deletion_phenotypes]
- [[entities/acinetobacter-baylyi-adp1]] — organism used for the urea fitness measurements. [src: acinetobacter_adp1_explorer]
