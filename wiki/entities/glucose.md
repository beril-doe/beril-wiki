---
type: Compound
description: Carbon source associated with ADP1's Entner–Doudoroff metabolism and
  respiratory redundancy.
sources:
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: Glucose
---
# Glucose

## Identity

Glucose is the canonical name used for this carbon-source condition in the ADP1 deletion phenotype analysis. [^adp1_deletion_phenotypes]

- **Known aliases:** None specified in the source. [^adp1_deletion_phenotypes]
- **Stable external identifier:** Not reported in the source. [^adp1_deletion_phenotypes]

## Evidence from ADP1 deletion phenotypes

Glucose belongs to the robust condition tier, together with glucarate and quinate, in the eight-carbon-source deletion matrix. [^adp1_deletion_phenotypes]

Across the robust tier, mean growth ratios range from 1.25 to 1.36 and 0.5–2.4% of genes show growth defects. [^adp1_deletion_phenotypes]

Growth ratios are mutant/wild-type values, with values below 1.0 indicating growth defects and values above 1.0 indicating no defect or a slight growth advantage from experimental normalization. [^adp1_deletion_phenotypes]

Glucose selects condition-specific genes associated with the [entner-doudoroff-pathway](entner-doudoroff-pathway.md), including eda, gntT, gluconokinase, and glucose dehydrogenase (PQQ). [^adp1_deletion_phenotypes]

PQQ biosynthesis genes are condition-specific for both glucose and quinate, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [^adp1_deletion_phenotypes]

## Respiratory-chain wiring

The respiratory-chain analysis **refines** glucose's condition-specific profile: no specifically required respiratory component was identified, and all listed components showed full redundancy. [^respiratory_chain_wiring] Complex I had a growth ratio of 1.44 on glucose, compared with 0.37 on quinate and 0.49 on acetate, supporting a condition-specific rather than uniformly essential respiratory requirement. [^respiratory_chain_wiring]

The report proposes that glucose distributes NADH production across Entner–Doudoroff pathway steps and the TCA cycle, rather than producing the concentrated TCA-cycle NADH burst proposed for quinate; this is a theoretical stoichiometric interpretation, not a measured flux distribution. [^respiratory_chain_wiring] Glucose produces 9 total NADH, or 1.50 NADH per carbon. [^respiratory_chain_wiring] These findings **support** [condition-specific-fitness](../concepts/condition-specific-fitness.md) by linking glucose pathway use with a distinct respiratory configuration. [^respiratory_chain_wiring]

The glucose findings contribute to [condition-specific-fitness](../concepts/condition-specific-fitness.md) by showing that carbon-source choice identifies pathway-specific fitness requirements. [^adp1_deletion_phenotypes]

## Related pages

- [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md) — source report for the ADP1 deletion phenotype analysis.
- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md) — source report on carbon-dependent respiratory-chain configuration in ADP1.
- [entner-doudoroff-pathway](entner-doudoroff-pathway.md) — pathway associated with glucose-specific genes.
- [pqq-biosynthesis](pqq-biosynthesis.md) — biosynthetic process linked to glucose-dependent dehydrogenase activity.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — cross-project synthesis of condition-dependent growth effects.

[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
