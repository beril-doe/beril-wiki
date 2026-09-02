---
type: "Compound"
description: "A branched-chain amino acid with cross-database pathway evidence."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Valine

## Identity

**Canonical name:** Valine. [src: fw300_metabolic_consistency]

**Known aliases:** No aliases were reported in the source document. [src: fw300_metabolic_consistency]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: fw300_metabolic_consistency]

## Evidence from fw300_metabolic_consistency

Valine emerged in the [[entities/web-of-microbes]] exometabolome of *Pseudomonas* FW300-N2E3. [src: fw300_metabolic_consistency]

Valine had a complete pathway prediction from [[entities/gapmind]] and supported growth involving 160 significant gene effects in [[entities/kescience-fitnessbrowser]]. [src: fw300_metabolic_consistency]

Valine was utilized by 1/1 matched [[entities/bacdive]] strain, corresponding to 100% utilization in the available species-level data. [src: fw300_metabolic_consistency]

Valine was one of three metabolites—along with malate and arginine—with four-way concordance across WoM production or emergence, Fitness Browser growth data, BacDive utilization, and GapMind pathway prediction. [src: fw300_metabolic_consistency]

The valine result therefore supports the cross-database integration described in [[concepts/multi-omics-integration]] and the pathway-completeness evidence discussed in [[concepts/metabolic-model-gapfilling]]. [src: fw300_metabolic_consistency]

The 160 significant gene effects associated with valine contribute to the report's broader interpretation of condition-specific fitness landscapes, while the source cautions that broadly pleiotropic amino-acid-biosynthesis genes can reflect housekeeping requirements rather than substrate-specific catabolism. [src: fw300_metabolic_consistency]

## Pathway capability and dependency

The new pathway-level analysis **refines** the prior complete-pathway result: across its species set, valine biosynthesis had all-gene completeness of 0.614, core-only completeness of 0.468, and an accessory-dependent gap of 0.146. [src: pathway_capability_dependency] This supports the interpretation that valine biosynthetic capacity can partly depend on genes outside the universally conserved core, while the analysis does not demonstrate valine exchange between organisms. [src: pathway_capability_dependency]

The analysis also distinguished genomic pathway capability from experimentally observed dependency, so a complete valine pathway need not imply fitness importance under standard conditions. [src: pathway_capability_dependency]

## Source

- [[summaries/fw300_metabolic_consistency__REPORT]] — cross-database analysis of FW300-N2E3 metabolite production, growth capability, species-level utilization, and pathway completeness.
- [[summaries/pathway_capability_dependency__REPORT]] — comparison of GapMind pathway completeness, accessory-gene contribution, and fitness-based dependency.
