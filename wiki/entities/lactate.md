---
type: Compound
description: Lactate links condition-specific respiration with microbial metabolite
  production.
sources:
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
- id: webofmicrobes_explorer
  resource: ../summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
title: Lactate
---
# Lactate

## Identity

Lactate is the canonical compound name used for a carbon source in the *Acinetobacter baylyi* ADP1 deletion-phenotype analysis. [^adp1_deletion_phenotypes]

- **Canonical name:** Lactate. [^adp1_deletion_phenotypes]
- **Known aliases:** No aliases were reported in the source document. [^adp1_deletion_phenotypes]
- **Stable external identifier:** No stable external identifier was reported in the source document. [^adp1_deletion_phenotypes]

## Evidence from ADP1 and cross-collection integration

Lactate was one of 8 carbon sources tested across a complete growth matrix containing 2,034 genes. [^adp1_deletion_phenotypes]

Lactate belonged to the moderate condition tier, together with asparagine; these conditions had mean growth ratios of 0.80–0.82 and 37–45% of genes showing defects. [^adp1_deletion_phenotypes]

The lactate-specific gene pattern included **lldR** and **cyoC/cyoD**, linking lactate-dependent growth phenotypes to lactate utilization and respiratory functions. [^adp1_deletion_phenotypes]

The respiratory-chain analysis **refines** this claim by identifying cytochrome bo3 as specifically required for lactate growth, while cytochrome bd is dispensable and Complex I is only mildly important; the reported Complex I growth ratio is 0.77. [^respiratory_chain_wiring]

The respiratory analysis further reports 5 NADH produced from lactate, or 1.67 NADH per carbon, with production through pyruvate plus the TCA cycle; this theoretical stoichiometry suggests that lactate selects a distinct respiratory configuration rather than simply a quantitative level of respiratory demand. [^respiratory_chain_wiring]

A separate Web of Microbes (WoM) analysis **supports** the value of lactate as a cross-collection phenotype: lactate was an `E` (“emerged”) metabolite for *Pseudomonas* sp. FW300-N2E3, meaning it was absent from the starting medium and newly detected, and Sodium D-Lactate was tested as a carbon source in the Fitness Browser. [^webofmicrobes_explorer] This bridge does not establish the ADP1 respiratory mechanism, but it provides a direct metabolite-production-to-fitness comparison that is adjacent to the ADP1 condition-specific result. [^webofmicrobes_explorer]

These findings **support** [condition-specific-fitness](../concepts/condition-specific-fitness.md) by showing that lactate exposes an intermediate level of condition-dependent deletion sensitivity rather than the extreme sensitivity observed under demanding conditions or the low defect rate observed under robust conditions. [^adp1_deletion_phenotypes]

They also **refine** [gene-essentiality](../concepts/gene-essentiality.md) because lactate-associated growth effects illustrate that gene importance can vary by growth condition rather than fitting a strictly binary essential/non-essential classification. [^adp1_deletion_phenotypes]

The source analyses integrate deletion growth measurements with TnSeq classifications, functional annotations, pangenome status, respiratory-chain fitness, FBA, theoretical stoichiometry, cross-species comparisons, and proteomics, connecting lactate phenotypes to [multi-omics-integration](../concepts/multi-omics-integration.md). [^adp1_deletion_phenotypes] [^respiratory_chain_wiring]

## Source

- [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md) — Summary of the ADP1 deletion collection phenotype analysis, including lactate condition classification and associated genes. [^adp1_deletion_phenotypes]
- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md) — Condition-specific respiratory-chain wiring analysis for ADP1, including lactate-associated cytochrome bo3 dependence. [^respiratory_chain_wiring]
- [webofmicrobes_explorer__REPORT](../summaries/webofmicrobes_explorer__REPORT.md) — WoM metabolite-action semantics and links between lactate production and Fitness Browser carbon-source experiments. [^webofmicrobes_explorer]

[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../summaries/webofmicrobes_explorer__REPORT.md)
