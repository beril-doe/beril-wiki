---
type: Compound
description: Nitrogenous compound used as a demanding ADP1 growth condition
sources:
- id: acinetobacter_adp1_explorer
  resource: ../summaries/acinetobacter_adp1_explorer__REPORT.md
  title: acinetobacter adp1 explorer
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: Urea
---
# Urea

## Identity

**Canonical name:** Urea. [^acinetobacter_adp1_explorer]

**Known aliases:** No aliases were reported in the source document. [^acinetobacter_adp1_explorer]

**Stable external identifier:** No stable external identifier was reported in the source document. [^acinetobacter_adp1_explorer]

## Key Facts

Urea was one of 8 carbon sources used to measure mutant growth fitness in the *Acinetobacter baylyi* ADP1 database. [^acinetobacter_adp1_explorer]

The deletion-phenotype analysis **refines** urea’s characterization as a demanding condition: it had the lowest mean growth ratio, **0.41**, with **97.9%** of genes showing severe defects at growth ratio < 0.5 and **95–100%** defective at ratio < 0.8. [^adp1_deletion_phenotypes] The respiratory-chain analysis **supports and refines** this characterization, reporting that urea was generally demanding and required everything in the reported respiratory-chain profile. [^respiratory_chain_wiring]

Urea fitness had a pairwise correlation of **r = 0.11** with quinate fitness. [^acinetobacter_adp1_explorer]

Urea fitness was weakly correlated with all other tested conditions, with correlations ranging from **r = 0.12-0.28**. [^acinetobacter_adp1_explorer]

The report interprets the weak correlations as suggesting that urea catabolism involves a largely independent set of genes; this remains a dataset-specific hypothesis rather than an established cross-species finding. [^acinetobacter_adp1_explorer] The new analysis **supports and refines** this interpretation: principal component analysis (PCA), which summarizes correlated variation into orthogonal components, isolated urea from carbon metabolism, with a loading of **+0.75** on PC2. [^adp1_deletion_phenotypes]

Urea-specific genes included ureA, ureB, ureC, ureD, ureE, ureF, and ureG, representing the urease complex. [^adp1_deletion_phenotypes]

These measurements are part of the ADP1-centered resource described in [acinetobacter_adp1_explorer__REPORT](../summaries/acinetobacter_adp1_explorer__REPORT.md), which contributes mutant growth fitness data unavailable for ADP1 in the Fitness Browser. [^acinetobacter_adp1_explorer]

The deletion analysis is described in [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md). [^adp1_deletion_phenotypes] The respiratory-chain interpretation is described in [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md). [^respiratory_chain_wiring]

## Related Pages

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — condition-specific mutant-growth fitness patterns involving urea. [^acinetobacter_adp1_explorer]
- [gene-essentiality](../concepts/gene-essentiality.md) — urea’s demanding-condition phenotype and urea-specific gene requirements refine condition-dependent essentiality. [^adp1_deletion_phenotypes]
- [urease-complex](urease-complex.md) — urea-specific genes include the urease-complex components. [^adp1_deletion_phenotypes]
- [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) — organism used for the urea fitness measurements. [^acinetobacter_adp1_explorer]

[^acinetobacter_adp1_explorer]: [acinetobacter adp1 explorer](../summaries/acinetobacter_adp1_explorer__REPORT.md)
[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
