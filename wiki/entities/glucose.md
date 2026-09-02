---
type: "Compound"
description: "Carbon source associated with ADP1's Entner\u2013Doudoroff metabolism and respiratory redundancy."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Glucose

## Identity

Glucose is the canonical name used for this carbon-source condition in the ADP1 deletion phenotype analysis. [src: adp1_deletion_phenotypes]

- **Known aliases:** None specified in the source. [src: adp1_deletion_phenotypes]
- **Stable external identifier:** Not reported in the source. [src: adp1_deletion_phenotypes]

## Evidence from ADP1 deletion phenotypes

Glucose belongs to the robust condition tier, together with glucarate and quinate, in the eight-carbon-source deletion matrix. [src: adp1_deletion_phenotypes]

Across the robust tier, mean growth ratios range from 1.25 to 1.36 and 0.5–2.4% of genes show growth defects. [src: adp1_deletion_phenotypes]

Growth ratios are mutant/wild-type values, with values below 1.0 indicating growth defects and values above 1.0 indicating no defect or a slight growth advantage from experimental normalization. [src: adp1_deletion_phenotypes]

Glucose selects condition-specific genes associated with the [[entities/entner-doudoroff-pathway]], including eda, gntT, gluconokinase, and glucose dehydrogenase (PQQ). [src: adp1_deletion_phenotypes]

PQQ biosynthesis genes are condition-specific for both glucose and quinate, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [src: adp1_deletion_phenotypes]

## Respiratory-chain wiring

The respiratory-chain analysis **refines** glucose's condition-specific profile: no specifically required respiratory component was identified, and all listed components showed full redundancy. [src: respiratory_chain_wiring] Complex I had a growth ratio of 1.44 on glucose, compared with 0.37 on quinate and 0.49 on acetate, supporting a condition-specific rather than uniformly essential respiratory requirement. [src: respiratory_chain_wiring]

The report proposes that glucose distributes NADH production across Entner–Doudoroff pathway steps and the TCA cycle, rather than producing the concentrated TCA-cycle NADH burst proposed for quinate; this is a theoretical stoichiometric interpretation, not a measured flux distribution. [src: respiratory_chain_wiring] Glucose produces 9 total NADH, or 1.50 NADH per carbon. [src: respiratory_chain_wiring] These findings **support** [[concepts/condition-specific-fitness]] by linking glucose pathway use with a distinct respiratory configuration. [src: respiratory_chain_wiring]

The glucose findings contribute to [[concepts/condition-specific-fitness]] by showing that carbon-source choice identifies pathway-specific fitness requirements. [src: adp1_deletion_phenotypes]

## Related pages

- [[summaries/adp1_deletion_phenotypes__REPORT]] — source report for the ADP1 deletion phenotype analysis.
- [[summaries/respiratory_chain_wiring__REPORT]] — source report on carbon-dependent respiratory-chain configuration in ADP1.
- [[entities/entner-doudoroff-pathway]] — pathway associated with glucose-specific genes.
- [[entities/pqq-biosynthesis]] — biosynthetic process linked to glucose-dependent dehydrogenase activity.
- [[concepts/condition-specific-fitness]] — cross-project synthesis of condition-dependent growth effects.
