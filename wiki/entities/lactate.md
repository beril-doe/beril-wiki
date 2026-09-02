---
type: "Compound"
description: "Lactate links condition-specific respiration with microbial metabolite production."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Lactate

## Identity

Lactate is the canonical compound name used for a carbon source in the *Acinetobacter baylyi* ADP1 deletion-phenotype analysis. [src: adp1_deletion_phenotypes]

- **Canonical name:** Lactate. [src: adp1_deletion_phenotypes]
- **Known aliases:** No aliases were reported in the source document. [src: adp1_deletion_phenotypes]
- **Stable external identifier:** No stable external identifier was reported in the source document. [src: adp1_deletion_phenotypes]

## Evidence from ADP1 and cross-collection integration

Lactate was one of 8 carbon sources tested across a complete growth matrix containing 2,034 genes. [src: adp1_deletion_phenotypes]

Lactate belonged to the moderate condition tier, together with asparagine; these conditions had mean growth ratios of 0.80–0.82 and 37–45% of genes showing defects. [src: adp1_deletion_phenotypes]

The lactate-specific gene pattern included **lldR** and **cyoC/cyoD**, linking lactate-dependent growth phenotypes to lactate utilization and respiratory functions. [src: adp1_deletion_phenotypes]

The respiratory-chain analysis **refines** this claim by identifying cytochrome bo3 as specifically required for lactate growth, while cytochrome bd is dispensable and Complex I is only mildly important; the reported Complex I growth ratio is 0.77. [src: respiratory_chain_wiring]

The respiratory analysis further reports 5 NADH produced from lactate, or 1.67 NADH per carbon, with production through pyruvate plus the TCA cycle; this theoretical stoichiometry suggests that lactate selects a distinct respiratory configuration rather than simply a quantitative level of respiratory demand. [src: respiratory_chain_wiring]

A separate Web of Microbes (WoM) analysis **supports** the value of lactate as a cross-collection phenotype: lactate was an `E` (“emerged”) metabolite for *Pseudomonas* sp. FW300-N2E3, meaning it was absent from the starting medium and newly detected, and Sodium D-Lactate was tested as a carbon source in the Fitness Browser. [src: webofmicrobes_explorer] This bridge does not establish the ADP1 respiratory mechanism, but it provides a direct metabolite-production-to-fitness comparison that is adjacent to the ADP1 condition-specific result. [src: webofmicrobes_explorer]

These findings **support** [[concepts/condition-specific-fitness]] by showing that lactate exposes an intermediate level of condition-dependent deletion sensitivity rather than the extreme sensitivity observed under demanding conditions or the low defect rate observed under robust conditions. [src: adp1_deletion_phenotypes]

They also **refine** [[concepts/gene-essentiality]] because lactate-associated growth effects illustrate that gene importance can vary by growth condition rather than fitting a strictly binary essential/non-essential classification. [src: adp1_deletion_phenotypes]

The source analyses integrate deletion growth measurements with TnSeq classifications, functional annotations, pangenome status, respiratory-chain fitness, FBA, theoretical stoichiometry, cross-species comparisons, and proteomics, connecting lactate phenotypes to [[concepts/multi-omics-integration]]. [src: adp1_deletion_phenotypes] [src: respiratory_chain_wiring]

## Source

- [[summaries/adp1_deletion_phenotypes__REPORT]] — Summary of the ADP1 deletion collection phenotype analysis, including lactate condition classification and associated genes. [src: adp1_deletion_phenotypes]
- [[summaries/respiratory_chain_wiring__REPORT]] — Condition-specific respiratory-chain wiring analysis for ADP1, including lactate-associated cytochrome bo3 dependence. [src: respiratory_chain_wiring]
- [[summaries/webofmicrobes_explorer__REPORT]] — WoM metabolite-action semantics and links between lactate production and Fitness Browser carbon-source experiments. [src: webofmicrobes_explorer]
