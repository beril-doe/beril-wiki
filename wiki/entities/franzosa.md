---
type: Dataset
description: Franzosa cohort used for cross-cohort metabolomics validation
sources:
- id: ibd_phage_targeting
  resource: ../summaries/ibd_phage_targeting__REPORT.md
  title: ibd phage targeting
title: Franzosa
---
# Franzosa

## What this entity is

**Canonical name:** Franzosa. [^ibd_phage_targeting]

**Known aliases:** No aliases are reported in the source document. [^ibd_phage_targeting]

**Stable external identifier:** No stable external identifier is reported in the source document. [^ibd_phage_targeting]

Franzosa is a microbiome/metabolomics dataset used alongside [hmp2](hmp2.md) for cross-cohort validation in the [ibd_phage_targeting__REPORT](../summaries/ibd_phage_targeting__REPORT.md). [^ibd_phage_targeting]

## Key facts from ibd_phage_targeting

- Cross-cohort HMP2-to-Franzosa metabolomics bridging produced 9 strict replications. [^ibd_phage_targeting]
- Theme-level sign concordance between HMP2 and Franzosa was 100 % for urobilin/porphyrin, 80 % for acyl-carnitines, and 75 % for long-chain polyunsaturated fatty acids. [^ibd_phage_targeting]
- Polyamines had no mass-to-charge-ratio bridge between HMP2 and Franzosa. [^ibd_phage_targeting]
- Pooled HMP2 and Franzosa metabolomics clustering separated the cohorts, indicating an uncorrected batch-effect limitation. [^ibd_phage_targeting]
- The first principal component explained 79 % of variance in the pooled metabolomics data. [^ibd_phage_targeting]
- Cross-cohort leave-one-substudy-out adjusted Rand index was 0.000, compared with a taxonomic baseline of 0.113. [^ibd_phage_targeting]

## Relations

Franzosa contributes cross-dataset evidence to [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) because the report links its metabolomics results with HMP2 while explicitly documenting batch limitations. [^ibd_phage_targeting]

Franzosa also contributes to [multi-omics-integration](../concepts/multi-omics-integration.md) through cross-cohort metabolite replication and the assessment of cohort separation in pooled metabolomics data. [^ibd_phage_targeting]

[^ibd_phage_targeting]: [ibd phage targeting](../summaries/ibd_phage_targeting__REPORT.md)
