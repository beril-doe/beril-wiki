---
type: Gene_Or_Pathway
description: Acetate-associated pathway supporting growth through central metabolism
sources:
- id: adp1_deletion_phenotypes
  resource: ../summaries/adp1_deletion_phenotypes__REPORT.md
  title: adp1 deletion phenotypes
- id: harvard_forest_warming
  resource: ../summaries/harvard_forest_warming__REPORT.md
  title: harvard forest warming
title: Glyoxylate Shunt
---
# Glyoxylate Shunt

## What this entity is

**Canonical name:** Glyoxylate shunt. [^adp1_deletion_phenotypes]

**Known aliases:** No aliases are reported in this document. [^adp1_deletion_phenotypes]

**Stable external identifier:** No stable external identifier is reported in this document. [^adp1_deletion_phenotypes]

The glyoxylate shunt is a metabolic pathway identified here through acetate-associated deletion phenotypes. [^adp1_deletion_phenotypes]

## Evidence across studies

Acetate condition-specific genes included fadB, malate synthase G, and citB, which the report associates with fatty acid β-oxidation and the glyoxylate shunt. [^adp1_deletion_phenotypes]

These findings place the glyoxylate shunt within the acetate-specific metabolic architecture detected in the *Acinetobacter baylyi* ADP1 deletion collection. [^adp1_deletion_phenotypes]

The acetate result contributes to the broader finding that 625 genes, or 31% of the complete 2,034-gene matrix, had a condition-specificity score of at least 1.0. [^adp1_deletion_phenotypes]

The Harvard Forest warming study **refines** this acetate-associated evidence by detecting increased RNA signals for the glyoxylate-cycle genes aceA/icl (K01637) and aceB/glcB (K01638) in heated mineral soil: log2 fold changes were +0.460 and +0.268, respectively, with p=0.037 for each. [^harvard_forest_warming] These gene-level signals extend the pathway’s observed environmental context beyond ADP1 deletion phenotypes, but they were not established as FDR-significant across 14K KOs. [^harvard_forest_warming]

## Related pages

The acetate-associated pathway requirement feeds into [condition-specific-fitness](../concepts/condition-specific-fitness.md), which synthesizes how gene importance depends on the tested carbon source. [^adp1_deletion_phenotypes]

It also relates to [gene-essentiality](../concepts/gene-essentiality.md), because the deletion results identify pathway genes whose growth importance is condition-dependent rather than universally essential. [^adp1_deletion_phenotypes]

The warming evidence connects the pathway to [multi-omics-integration](../concepts/multi-omics-integration.md) through a transcript-pool response, while the complete analysis is summarized in [harvard_forest_warming__REPORT](../summaries/harvard_forest_warming__REPORT.md). [^harvard_forest_warming]

The source analysis is summarized in [adp1_deletion_phenotypes__REPORT](../summaries/adp1_deletion_phenotypes__REPORT.md). [^adp1_deletion_phenotypes]

[^adp1_deletion_phenotypes]: [adp1 deletion phenotypes](../summaries/adp1_deletion_phenotypes__REPORT.md)
[^harvard_forest_warming]: [harvard forest warming](../summaries/harvard_forest_warming__REPORT.md)
