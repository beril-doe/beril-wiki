---
type: "Method"
description: "MetaPhlAn3 taxonomic profiling method and cross-cohort microbiome namespace"
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
---
# MetaPhlAn3

## What it is

MetaPhlAn3 is a microbial taxonomic profiling method and namespace used in the discoveries analysis of cross-cohort microbiome ecotype projection. [src: discoveries]

**Canonical name:** MetaPhlAn3. [src: discoveries]  
**Known aliases:** MetaPhlAn 3. [src: discoveries]  
**Stable external identifier:** Not specified in [[summaries/discoveries]]. [src: discoveries]

## Key facts

A linear discriminant analysis plus Gaussian mixture model (LDA-GMM) projection used MetaPhlAn3 and Kaiju namespaces and produced plausible Kuehl cohort proportions of 27%, 42%, and 31% across the inferred ecotypes. [src: discoveries]

By contrast, a centered log-ratio transformation plus principal component analysis and Gaussian mixture model (CLR-PCA GMM) projected all 26 Kuehl samples to the E3 ecotype at confidence greater than 0.97 because Kuehl detected only 54% of the training species. [src: discoveries]

These results identify namespace compatibility and species-detection coverage as important limitations when transferring microbiome ecotype models across cohorts. [src: discoveries]

The ibd_phage_targeting analysis **supports** the use of MetaPhlAn3 for ecotype construction: 8,489 curatedMetagenomicData samples were analyzed, and a consensus K = 4 framework defined four ecotypes before projection to 23 UC Davis patients. [src: ibd_phage_targeting] The same analysis **refines** the earlier transferability limitation by reporting 48.9 % per-sample LDA/GMM agreement, leave-one-substudy-out ARI with mean 0.113 and range 0.000–0.282, and 50.6 % agreement after pathway-feature refitting. [src: ibd_phage_targeting]

It also **supports** the prior warning about method asymmetry: LDA was judged more robust, whereas GMM assigned all 26 UC Davis samples to E3 with confidence >0.97 under sparse feature overlap, an interpretation considered artifactual. [src: ibd_phage_targeting]

The pitfalls analysis **refines** these transferability warnings: cross-cohort MetaPhlAn3 analyses require a synonymy layer rather than simple string normalization because taxonomic names may differ across short names, full lineage strings, and GTDB reclassifications, including *Bacteroides vulgatus*/*Phocaeicola vulgatus*, *Eubacterium rectale*/*Agathobacter rectalis*, and *Ruminococcus gnavus*/*Mediterraneibacter gnavus*. [src: pitfalls] In the CrohnsPhage mart, failure to reconcile names produced log₂FC approximately 28, equivalent to approximately 2.68 × 10⁸ fold, because one cohort’s abundance collapsed to a pseudocount; a targeted battery used a hand-curated 23-entry synonym map, while full-taxonomy aggregation requires an NCBI-taxid-backed, GTDB-version-aware reconciliation layer. [src: pitfalls]

## Related pages

- [[summaries/discoveries]] — source summary containing the MetaPhlAn3 projection findings.
- [[summaries/ibd_phage_targeting__REPORT]] — source summary of the ecotype, multi-omics, and phage-targeting analysis. [src: ibd_phage_targeting]
- [[summaries/pitfalls]] — source summary documenting MetaPhlAn3 name-reconciliation and cross-cohort analysis pitfalls. [src: pitfalls]
- [[entities/curatedmetagenomicdata]] — dataset used in the cross-cohort ecotype analysis. [src: discoveries]
- [[concepts/multi-omics-integration]] — cross-cohort and multi-modal integration context for microbiome analyses. [src: discoveries]
