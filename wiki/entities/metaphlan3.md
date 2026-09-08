---
type: Method
description: MetaPhlAn3 taxonomic profiling method and cross-cohort microbiome namespace
sources:
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: ibd_phage_targeting
  resource: ../summaries/ibd_phage_targeting__REPORT.md
  title: ibd phage targeting
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
title: MetaPhlAn3
---
# MetaPhlAn3

## What it is

MetaPhlAn3 is a microbial taxonomic profiling method and namespace used in the discoveries analysis of cross-cohort microbiome ecotype projection. [^discoveries]

**Canonical name:** MetaPhlAn3. [^discoveries]  
**Known aliases:** MetaPhlAn 3. [^discoveries]  
**Stable external identifier:** Not specified in [discoveries](../summaries/discoveries.md). [^discoveries]

## Key facts

A linear discriminant analysis plus Gaussian mixture model (LDA-GMM) projection used MetaPhlAn3 and Kaiju namespaces and produced plausible Kuehl cohort proportions of 27%, 42%, and 31% across the inferred ecotypes. [^discoveries]

By contrast, a centered log-ratio transformation plus principal component analysis and Gaussian mixture model (CLR-PCA GMM) projected all 26 Kuehl samples to the E3 ecotype at confidence greater than 0.97 because Kuehl detected only 54% of the training species. [^discoveries]

These results identify namespace compatibility and species-detection coverage as important limitations when transferring microbiome ecotype models across cohorts. [^discoveries]

The ibd_phage_targeting analysis **supports** the use of MetaPhlAn3 for ecotype construction: 8,489 curatedMetagenomicData samples were analyzed, and a consensus K = 4 framework defined four ecotypes before projection to 23 UC Davis patients. [^ibd_phage_targeting] The same analysis **refines** the earlier transferability limitation by reporting 48.9 % per-sample LDA/GMM agreement, leave-one-substudy-out ARI with mean 0.113 and range 0.000–0.282, and 50.6 % agreement after pathway-feature refitting. [^ibd_phage_targeting]

It also **supports** the prior warning about method asymmetry: LDA was judged more robust, whereas GMM assigned all 26 UC Davis samples to E3 with confidence >0.97 under sparse feature overlap, an interpretation considered artifactual. [^ibd_phage_targeting]

The pitfalls analysis **refines** these transferability warnings: cross-cohort MetaPhlAn3 analyses require a synonymy layer rather than simple string normalization because taxonomic names may differ across short names, full lineage strings, and GTDB reclassifications, including *Bacteroides vulgatus*/*Phocaeicola vulgatus*, *Eubacterium rectale*/*Agathobacter rectalis*, and *Ruminococcus gnavus*/*Mediterraneibacter gnavus*. [^pitfalls] In the CrohnsPhage mart, failure to reconcile names produced log₂FC approximately 28, equivalent to approximately 2.68 × 10⁸ fold, because one cohort’s abundance collapsed to a pseudocount; a targeted battery used a hand-curated 23-entry synonym map, while full-taxonomy aggregation requires an NCBI-taxid-backed, GTDB-version-aware reconciliation layer. [^pitfalls]

## Related pages

- [discoveries](../summaries/discoveries.md) — source summary containing the MetaPhlAn3 projection findings.
- [ibd_phage_targeting__REPORT](../summaries/ibd_phage_targeting__REPORT.md) — source summary of the ecotype, multi-omics, and phage-targeting analysis. [^ibd_phage_targeting]
- [pitfalls](../summaries/pitfalls.md) — source summary documenting MetaPhlAn3 name-reconciliation and cross-cohort analysis pitfalls. [^pitfalls]
- [curatedmetagenomicdata](curatedmetagenomicdata.md) — dataset used in the cross-cohort ecotype analysis. [^discoveries]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — cross-cohort and multi-modal integration context for microbiome analyses. [^discoveries]

[^discoveries]: [discoveries](../summaries/discoveries.md)
[^ibd_phage_targeting]: [ibd phage targeting](../summaries/ibd_phage_targeting__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
