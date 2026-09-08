---
type: Compound
description: Xylose is a proposed selective prebiotic substrate for commensals over
  Pseudomonas aeruginosa.
sources:
- id: cf_formulation_design
  resource: ../summaries/cf_formulation_design__REPORT.md
  title: cf formulation design
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
title: Xylose
---
# Xylose

## Identity

**Canonical name:** Xylose [^cf_formulation_design]

**Known aliases:** No aliases are reported in the source document. [^cf_formulation_design]

**Stable external identifier:** No stable external identifier is reported in the source document. [^cf_formulation_design]

Xylose is a compound proposed as a selective prebiotic substrate in a protective microbiome formulation for competitive exclusion of [pseudomonas-aeruginosa](pseudomonas-aeruginosa.md). [^cf_formulation_design]

## Evidence from cf_formulation_design

The report identified xylose as a pathway-level metabolic opportunity because xylose utilization was complete in at least one core commensal species but absent in [pseudomonas-aeruginosa](pseudomonas-aeruginosa.md) PA14. [^cf_formulation_design]

PA pathway completeness for xylose was 0%, and the corresponding selectivity value was 1.00. [^cf_formulation_design]

The proposed prebiotic strategy predicts that xylose will support [neisseria-mucosa](neisseria-mucosa.md) and [gemella-sanguinis](gemella-sanguinis.md) more selectively than PA14. [^cf_formulation_design]

This prediction was based on genomic pathway comparison rather than direct xylose growth experiments, because the 22-substrate carbon panel omitted the sugar alcohols and pentoses identified genomically. [^cf_formulation_design]

The report found that PA14 outgrew the average commensal on every one of the 22 tested substrates, so xylose is a proposed alternative to amino-acid competition rather than a demonstrated commensal growth advantage. [^cf_formulation_design]

## Evidence from pseudomonas_carbon_ecology

The newer comparative analysis **supports** the genomic basis of the selectivity claim: xylose completeness was 0.0% in 7 *Pseudomonas* s.s. species and 74.4% in 189 *Pseudomonas_E* species, a difference of +74.4 percentage points. [^pseudomonas_carbon_ecology] This result **refines** the PA14-specific observation by placing xylose loss in the broader context of host-associated *Pseudomonas* s.s. versus the generally more environmentally associated *Pseudomonas_E* group; it does not directly test growth of PA14 or the proposed commensals. [^pseudomonas_carbon_ecology]

## Interpretation and limitations

Xylose therefore links [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) with [condition-specific-fitness](../concepts/condition-specific-fitness.md): its proposed value comes from a metabolic gap between PA14 and candidate commensals that may shape condition-dependent competitive fitness. [^cf_formulation_design]

The xylose prediction requires experimental validation before use in a formulation, including direct growth and competition assays with [neisseria-mucosa](neisseria-mucosa.md), [gemella-sanguinis](gemella-sanguinis.md), PA14, PAO1, and clinical PA isolates. [^cf_formulation_design]

The new analysis **supports** retaining this validation requirement: carbon-pathway profiles showed ecological structure, but xylose alone was not established as a fine-grained environment discriminator, and the analysis did not provide direct competition evidence. [^pseudomonas_carbon_ecology]

The result also contributes to [multi-omics-integration](../concepts/multi-omics-integration.md) and [pangenome-integration](../concepts/pangenome-integration.md), because the proposed substrate was identified by combining pathway comparisons with patient metatranscriptomics and pangenome data. [^cf_formulation_design]

## Source

- [cf_formulation_design__REPORT](../summaries/cf_formulation_design__REPORT.md) — formulation-design report integrating metabolic assays, patient omics, interaction data, and pangenome analysis. [^cf_formulation_design]
- [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md) — comparative *Pseudomonas* carbon-pathway analysis contextualizing xylose pathway loss. [^pseudomonas_carbon_ecology]

[^cf_formulation_design]: [cf formulation design](../summaries/cf_formulation_design__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
