---
type: Compound
description: Lysine, an amino acid linked to pathway completeness and utilization
  evidence
sources:
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
title: Lysine
---
# Lysine

## Identity

**Canonical name:** Lysine. [^fw300_metabolic_consistency]

**Known aliases:** No aliases were reported in this document. [^fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in this document. [^fw300_metabolic_consistency]

## Evidence from FW300-N2E3

Lysine emerged in the Web of Microbes exometabolome of [pseudomonas-fw300-n2e3](pseudomonas-fw300-n2e3.md) and was among the 13 metabolites with complete [gapmind](gapmind.md) pathway predictions. [^fw300_metabolic_consistency]

Lysine also showed growth in the Fitness Browser experiment used for the cross-database comparison, making it part of the 13/13 set in which complete GapMind predictions agreed with Fitness Browser growth measurements. [^fw300_metabolic_consistency]

In [bacdive](bacdive.md), lysine utilization was observed in 0 of 3 strains, reported as 0+/3-, with moderate confidence. [^fw300_metabolic_consistency]

The report treats the lysine production-versus-utilization result as a consistent negative BacDive observation but emphasizes that the sample size of 3 strains is too small for a strong species-level conclusion. [^fw300_metabolic_consistency]

The lysine result therefore distinguishes production from utilization: FW300-N2E3 released or accumulated lysine in WoM and showed growth in a matched Fitness Browser condition, whereas the available species-level BacDive records did not show lysine utilization. [^fw300_metabolic_consistency]

## Pathway Capability and Accessory Contribution

The newer pathway-capability analysis **refines** the earlier complete GapMind interpretation by showing that lysine biosynthesis had all-gene completeness of 0.804, core-only completeness of 0.664, and an exact accessory-dependent gap of 0.140 across the analyzed genomes. [^pathway_capability_dependency] This supports the interpretation that lysine biosynthetic capacity can depend partly on genes outside the universally conserved core, while not itself demonstrating lysine exchange between organisms. [^pathway_capability_dependency]

## Related Pages

- [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) — source report for the cross-database lysine evidence. [^fw300_metabolic_consistency]
- [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) — source report for lysine pathway completeness and accessory-gene evidence. [^pathway_capability_dependency]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — lysine is part of the report's integration of exometabolomics, fitness, phenotype, and pathway data. [^fw300_metabolic_consistency]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the lysine result contributes to condition-specific Fitness Browser interpretation. [^fw300_metabolic_consistency]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — complete GapMind prediction for lysine was concordant with Fitness Browser growth. [^fw300_metabolic_consistency]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — lysine biosynthetic completeness differed between all-gene and core-only analyses by 0.140. [^pathway_capability_dependency]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — the result required matching lysine across multiple BERDL databases. [^fw300_metabolic_consistency]

[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
