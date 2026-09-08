---
type: Gene_Or_Pathway
description: Glucose-associated pathway supporting condition-specific metabolism in
  ADP1
sources:
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: Entner-Doudorff Pathway
---
# Entner-Doudorff Pathway

## What this entity is

**Canonical name:** Entner-Doudorff pathway. [^adp1_deletion_phenotypes]

**Known aliases:** None reported in this document. [^adp1_deletion_phenotypes]

**Stable external identifier:** None reported in this document. [^adp1_deletion_phenotypes]

The Entner-Doudorff pathway is a glucose-associated metabolic pathway identified in the ADP1 deletion-phenotype analysis. [^adp1_deletion_phenotypes]

## Evidence from ADP1 deletion phenotypes

The complete growth matrix measured 2,034 genes across 8 carbon sources, and glucose-specific phenotypes selected eda, gntT, gluconokinase, and glucose dehydrogenase (PQQ) as genes associated with the Entner-Doudorff pathway and PQQ-dependent glucose utilization. [^adp1_deletion_phenotypes]

The report identifies glucose as one of three robust conditions, alongside glucarate and quinate, with mean growth ratios of 1.25–1.36 and 0.5–2.4% of genes defective at the growth-ratio threshold of less than 0.8%. [^adp1_deletion_phenotypes]

PQQ biosynthesis genes were condition-specific for both glucose and quinate, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [^adp1_deletion_phenotypes]

Across all eight carbon sources, 625 genes, representing 31% of the complete matrix, had a condition-specificity score of at least 1.0. [^adp1_deletion_phenotypes]

## Respiratory-chain interpretation

The respiratory-chain analysis **refines** the pathway’s glucose association by proposing that glucose distributes NADH production across Entner-Doudoroff pathway steps and the TCA cycle, generating 9 total NADH, or 1.50 NADH per carbon. [^respiratory_chain_wiring]

This distributed production is proposed to remain within the capacity of NDH-2, helping explain why no specifically required respiratory component was detected on glucose and why Complex I had a growth ratio of 1.44 there. This is a theoretical flux interpretation rather than a measured flux distribution. [^respiratory_chain_wiring]

The same analysis **contrasts** glucose with quinate: quinate-associated aromatic-ring cleavage is proposed to create a concentrated TCA-cycle NADH burst, despite producing 4 total NADH, or 0.57 NADH per carbon, making Complex I more important on quinate. [^respiratory_chain_wiring]

## Related pages

- [glucose](glucose.md) — glucose was the condition associated with Entner-Doudoroff pathway genes in the deletion analysis. [^adp1_deletion_phenotypes]
- [pqq-biosynthesis](pqq-biosynthesis.md) — PQQ biosynthesis genes were condition-specific for glucose and quinate. [^adp1_deletion_phenotypes]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the pathway is evidence that gene importance depends on the tested carbon source. [^adp1_deletion_phenotypes]
- [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md) — source summary for the ADP1 deletion collection phenotype analysis. [^adp1_deletion_phenotypes]
- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md) — source summary for the condition-specific respiratory-chain interpretation. [^respiratory_chain_wiring]

[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
