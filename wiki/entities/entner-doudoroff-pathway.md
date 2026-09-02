---
type: "Gene_Or_Pathway"
description: "Glucose-associated pathway supporting condition-specific metabolism in ADP1"
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Entner-Doudorff Pathway

## What this entity is

**Canonical name:** Entner-Doudorff pathway. [src: adp1_deletion_phenotypes]

**Known aliases:** None reported in this document. [src: adp1_deletion_phenotypes]

**Stable external identifier:** None reported in this document. [src: adp1_deletion_phenotypes]

The Entner-Doudorff pathway is a glucose-associated metabolic pathway identified in the ADP1 deletion-phenotype analysis. [src: adp1_deletion_phenotypes]

## Evidence from ADP1 deletion phenotypes

The complete growth matrix measured 2,034 genes across 8 carbon sources, and glucose-specific phenotypes selected eda, gntT, gluconokinase, and glucose dehydrogenase (PQQ) as genes associated with the Entner-Doudorff pathway and PQQ-dependent glucose utilization. [src: adp1_deletion_phenotypes]

The report identifies glucose as one of three robust conditions, alongside glucarate and quinate, with mean growth ratios of 1.25–1.36 and 0.5–2.4% of genes defective at the growth-ratio threshold of less than 0.8%. [src: adp1_deletion_phenotypes]

PQQ biosynthesis genes were condition-specific for both glucose and quinate, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [src: adp1_deletion_phenotypes]

Across all eight carbon sources, 625 genes, representing 31% of the complete matrix, had a condition-specificity score of at least 1.0. [src: adp1_deletion_phenotypes]

## Respiratory-chain interpretation

The respiratory-chain analysis **refines** the pathway’s glucose association by proposing that glucose distributes NADH production across Entner-Doudoroff pathway steps and the TCA cycle, generating 9 total NADH, or 1.50 NADH per carbon. [src: respiratory_chain_wiring]

This distributed production is proposed to remain within the capacity of NDH-2, helping explain why no specifically required respiratory component was detected on glucose and why Complex I had a growth ratio of 1.44 there. This is a theoretical flux interpretation rather than a measured flux distribution. [src: respiratory_chain_wiring]

The same analysis **contrasts** glucose with quinate: quinate-associated aromatic-ring cleavage is proposed to create a concentrated TCA-cycle NADH burst, despite producing 4 total NADH, or 0.57 NADH per carbon, making Complex I more important on quinate. [src: respiratory_chain_wiring]

## Related pages

- [[entities/glucose]] — glucose was the condition associated with Entner-Doudoroff pathway genes in the deletion analysis. [src: adp1_deletion_phenotypes]
- [[entities/pqq-biosynthesis]] — PQQ biosynthesis genes were condition-specific for glucose and quinate. [src: adp1_deletion_phenotypes]
- [[concepts/condition-specific-fitness]] — the pathway is evidence that gene importance depends on the tested carbon source. [src: adp1_deletion_phenotypes]
- [[summaries/adp1_deletion_phenotypes__REPORT]] — source summary for the ADP1 deletion collection phenotype analysis. [src: adp1_deletion_phenotypes]
- [[summaries/respiratory_chain_wiring__REPORT]] — source summary for the condition-specific respiratory-chain interpretation. [src: respiratory_chain_wiring]
