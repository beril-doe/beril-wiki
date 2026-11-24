---
type: "Method"
description: "Centered log-ratio transformation with Wilcoxon-type tests, ALDEx2-style, for OTU differential abundance between groups."
sources: ["summaries/ibd_phage_targeting__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md"]
aliases: ["ALDEx2-style CLR differential abundance"]
---
# CLR-based differential abundance analysis

This page covers CLR-based differential abundance analysis, also called ALDEx2-style CLR differential abundance. CLR is the centered log-ratio transform, and the Wilcoxon-type tests are run on the transformed values. In ibd_phage_targeting it corrected a compositional bias in a pooled-cohort battery. [src: ibd_phage_targeting] In lignin_community_enrichment it was planned across 5 contrasts, and n=3 per group left no individual OTU (operational taxonomic unit) significant after FDR (false discovery rate) correction. [src: lignin_community_enrichment]

## Key facts

- Raw Mann-Whitney tests on relative abundance are systematically biased by the sum-to-constant constraint. The ibd_phage_targeting report cites Gloor et al. (2017), Lin & Peddada (2020) and Tsilimigras & Fodor (2016) for this. [src: ibd_phage_targeting]
- The same report adds LinDA (linear CLR regression with bias correction) as a second-method concordance check. [src: ibd_phage_targeting]
- The lignin community enrichment report plans ALDEx2-style CLR + Wilcoxon differential abundance in a notebook, NB05, with 5 planned contrasts. [src: lignin_community_enrichment]
- That report expresses effect sizes as CLR differences. [src: lignin_community_enrichment]

## Use in ibd_phage_targeting

NB00 tested the compositional-artifact explanation. It ran a curated battery of 8 protective and 6 reported-pathobiont species under both raw Mann-Whitney on relative abundance and CLR-based Mann-Whitney. [src: ibd_phage_targeting] In the pooled-cohort protective-species battery, raw Mann-Whitney mis-directed 4+ of 8 protective species, and CLR correction recovered them. [src: ibd_phage_targeting] NB00 reproduces the compositional-bias result directly on this battery. [src: ibd_phage_targeting] See [[summaries/ibd_phage_targeting__REPORT]] and [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

## Use in lignin_community_enrichment

With n=3 per group, pairwise Mann-Whitney U tests have a minimum achievable p-value of 0.10. Only 10 permutations are possible for 3 vs 3, so FDR-corrected significance is impossible for individual OTUs. [src: lignin_community_enrichment] Accordingly, no individual OTUs reached FDR significance. [src: lignin_community_enrichment] See [[summaries/lignin_community_enrichment__REPORT]] and [[concepts/small-sample-limits-in-community-amplicon-statistics]].

## Open Directions

- Run the LinDA concordance check alongside CLR-Wilcoxon on the lignin contrasts to see whether a model-based test gives more power than rank tests at n=3.
- Repeat the ibd_phage_targeting battery with cohort stratification to test whether CLR recovery holds within each substudy.
