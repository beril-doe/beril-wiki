---
type: "Compound"
description: "Lysine, an amino acid linked to pathway completeness and utilization evidence"
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Lysine

## Identity

**Canonical name:** Lysine. [src: fw300_metabolic_consistency]

**Known aliases:** No aliases were reported in this document. [src: fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in this document. [src: fw300_metabolic_consistency]

## Evidence from FW300-N2E3

Lysine emerged in the Web of Microbes exometabolome of [[entities/pseudomonas-fw300-n2e3]] and was among the 13 metabolites with complete [[entities/gapmind]] pathway predictions. [src: fw300_metabolic_consistency]

Lysine also showed growth in the Fitness Browser experiment used for the cross-database comparison, making it part of the 13/13 set in which complete GapMind predictions agreed with Fitness Browser growth measurements. [src: fw300_metabolic_consistency]

In [[entities/bacdive]], lysine utilization was observed in 0 of 3 strains, reported as 0+/3-, with moderate confidence. [src: fw300_metabolic_consistency]

The report treats the lysine production-versus-utilization result as a consistent negative BacDive observation but emphasizes that the sample size of 3 strains is too small for a strong species-level conclusion. [src: fw300_metabolic_consistency]

The lysine result therefore distinguishes production from utilization: FW300-N2E3 released or accumulated lysine in WoM and showed growth in a matched Fitness Browser condition, whereas the available species-level BacDive records did not show lysine utilization. [src: fw300_metabolic_consistency]

## Pathway Capability and Accessory Contribution

The newer pathway-capability analysis **refines** the earlier complete GapMind interpretation by showing that lysine biosynthesis had all-gene completeness of 0.804, core-only completeness of 0.664, and an exact accessory-dependent gap of 0.140 across the analyzed genomes. [src: pathway_capability_dependency] This supports the interpretation that lysine biosynthetic capacity can depend partly on genes outside the universally conserved core, while not itself demonstrating lysine exchange between organisms. [src: pathway_capability_dependency]

## Related Pages

- [[summaries/fw300_metabolic_consistency__REPORT]] — source report for the cross-database lysine evidence. [src: fw300_metabolic_consistency]
- [[summaries/pathway_capability_dependency__REPORT]] — source report for lysine pathway completeness and accessory-gene evidence. [src: pathway_capability_dependency]
- [[concepts/multi-omics-integration]] — lysine is part of the report's integration of exometabolomics, fitness, phenotype, and pathway data. [src: fw300_metabolic_consistency]
- [[concepts/condition-specific-fitness]] — the lysine result contributes to condition-specific Fitness Browser interpretation. [src: fw300_metabolic_consistency]
- [[concepts/metabolic-model-gapfilling]] — complete GapMind prediction for lysine was concordant with Fitness Browser growth. [src: fw300_metabolic_consistency]
- [[concepts/gene-function-acquisition-depth]] — lysine biosynthetic completeness differed between all-gene and core-only analyses by 0.140. [src: pathway_capability_dependency]
- [[concepts/cross-tenant-data-bridging]] — the result required matching lysine across multiple KBase Data Lakehouse databases. [src: fw300_metabolic_consistency]
