---
type: Dataset
description: IBD-associated human microbiome and metabolomics dataset
sources:
- id: ibd_phage_targeting
  resource: ../summaries/ibd_phage_targeting__REPORT.md
  title: ibd phage targeting
title: HMP2
---
# HMP2

## What this entity is

**Canonical name:** HMP2. [^ibd_phage_targeting]

**Known alias:** HMP2. [^ibd_phage_targeting]

**Stable external identifier:** None was supplied in the report. [^ibd_phage_targeting]

HMP2 is a human microbiome dataset used in the report for paired taxonomic, metabolomic, and endogenous-phage analyses of Crohn's disease and non-IBD samples. [^ibd_phage_targeting]

## Key facts in this document

- Paired HMP2 metabolomics included 468 samples for analysis of relationships among [flavonifractor-plautii](flavonifractor-plautii.md), [eggerthella-lenta](eggerthella-lenta.md), [enterocloster-bolteae](enterocloster-bolteae.md), and bile-acid metabolites. [^ibd_phage_targeting]
- HMP2 metabolomics tested 579 named metabolites and identified 52 differentially abundant metabolites, consisting of 50 CD-up and 2 CD-down metabolites. [^ibd_phage_targeting]
- Polyamines were enriched among the differential metabolites with OR = 14.6 and FDR = 0.008, while long-chain PUFAs were enriched with OR = 7.9 and FDR = 0.009. [^ibd_phage_targeting]
- [urobilin](urobilin.md) was CD-down with Cliff's δ = −0.38 and FDR = 0.09, whereas tauro-α/β-muricholate and free taurine were CD-up. [^ibd_phage_targeting]
- Cross-cohort bridging from HMP2 to [franzosa](franzosa.md) produced 9 strict replications, with theme-level sign concordance of 100 % for urobilin/porphyrin, 80 % for acyl-carnitines, and 75 % for long-chain PUFAs; polyamines had no m/z bridge. [^ibd_phage_targeting]
- A two-modality canonical correlation analysis (CCA, a method for finding correlated axes between two data modalities) used 106 paired HMP2 subjects and produced canonical correlations of 0.964, 0.928, 0.911, and 0.889. [^ibd_phage_targeting]
- The first canonical axis had r = 0.964, Cliff's CD-versus-nonIBD = +0.498, and Mann–Whitney p = 4e-4; all six actionable Tier-A species loaded positively, while urobilin and secondary bile acids loaded negatively. [^ibd_phage_targeting]
- The first canonical axis also had positive loadings for polyamines, PUFAs, fatty-acid amides, and [cadaverine](cadaverine.md), and the report interpreted it as a dominant CD-associated joint species–metabolite axis. [^ibd_phage_targeting]
- Endogenous-phage analysis covered 630 HMP2 samples. [^ibd_phage_targeting]
- Gokushovirus WZ-2015a was CD-down in E1 with Cliff's δ = −0.358, FDR = 5e-7, n_CD = 231, and n_HC = 125. [^ibd_phage_targeting]
- [escherichia-coli](escherichia-coli.md) correlated with Podoviridae at ρ = +0.183 and Myoviridae at ρ = +0.125 in the HMP2 endogenous-phage analysis. [^ibd_phage_targeting]
- HMP2 viromics had an 80 % family-classification Unknown fraction, and endogenous-phage correlations had maximum absolute ρ ≤ 0.18. [^ibd_phage_targeting]
- When HMP2 and FRANZOSA m/z data were pooled, batch effects separated the cohorts, with PC1 explaining 79 % of variance and cross-cohort leave-one-substudy-out ARI = 0.000. [^ibd_phage_targeting]
- The report reduced a planned three-modality MOFA+ integration to a two-modality CCA pilot because HMP2 pathway abundance was unavailable in the mart. [^ibd_phage_targeting]

## Related pages

HMP2 is central to the report's [multi-omics-integration](../concepts/multi-omics-integration.md) analysis and its cross-dataset limitations are relevant to [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md). [^ibd_phage_targeting]

See the source-specific synthesis in [ibd_phage_targeting__REPORT](../summaries/ibd_phage_targeting__REPORT.md). [^ibd_phage_targeting]

[^ibd_phage_targeting]: [ibd phage targeting](../summaries/ibd_phage_targeting__REPORT.md)
