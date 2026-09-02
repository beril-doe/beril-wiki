---
type: "Method"
description: "Method linking two data modalities through maximally correlated canonical variates"
sources: ["summaries/ibd_phage_targeting__REPORT.md"]
---
# Canonical correlation analysis

## What it is

**Canonical name:** canonical correlation analysis. **Known alias:** CCA. **Stable external identifier:** not specified in the report. [src: ibd_phage_targeting]

Canonical correlation analysis (CCA) is a statistical method that identifies paired linear combinations of two data modalities with maximal correlation. [src: ibd_phage_targeting] In this project, CCA was used as a two-modality pilot connecting microbial taxonomy with metabolomics within the [[concepts/multi-omics-integration]] framework. [src: ibd_phage_targeting]

## Key facts from ibd_phage_targeting

The pilot used 106 paired HMP2 subjects and produced four canonical correlations: 0.964, 0.928, 0.911, and 0.889. [src: ibd_phage_targeting]

The first canonical correlation, CC1, had r = 0.964, a Crohn's disease versus non-IBD Cliff's delta of +0.498, and Mann–Whitney p = 4e-4. [src: ibd_phage_targeting]

All six actionable Tier-A species loaded positively on CC1, while urobilin and secondary bile acids loaded negatively. [src: ibd_phage_targeting]

Polyamines, polyunsaturated fatty acids, fatty-acid amides, and cadaverine loaded positively on CC1. [src: ibd_phage_targeting]

The report interprets CC1 as a single dominant Crohn's disease axis in joint species–metabolite space. [src: ibd_phage_targeting]

The CCA result supports the report's integration of taxonomic and metabolomic evidence, but it was explicitly a pilot and did not include the unavailable pathway modality. [src: ibd_phage_targeting]

## Limitations

The planned three-modality MOFA+ analysis was reduced to a two-modality CCA pilot because HMP2 pathway abundance was unavailable in the data mart. [src: ibd_phage_targeting]

The CCA result should therefore be treated as a pilot association rather than a complete multi-omics mechanism, because the pathway modality was absent. [src: ibd_phage_targeting]

## Related pages

- [[concepts/multi-omics-integration]] — Cross-document synthesis of multi-omics integration, including this taxonomy–metabolomics CCA result. [src: ibd_phage_targeting]
- [[summaries/ibd_phage_targeting__REPORT]] — Summary of the source report containing the CCA analysis. [src: ibd_phage_targeting]
