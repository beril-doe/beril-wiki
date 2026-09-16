---
type: "Concept"
description: "How to tell FDR-corrected null results caused by incomplete metadata or sample-size p-value floors apart from real evidence that an effect is absent, using AMR temporal trends and per-OTU lignin enrichment as examples."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md"]
---
A null result after multiple-testing correction can mean one of two things. Either the effect is absent, or the design could not have detected it. Two projects in this corpus report nulls after false-discovery-rate (FDR; the expected share of false positives among calls declared significant) correction. In each case the authors attribute the null to a limitation of the design or data rather than to an absent effect: incomplete metadata in one case and small group sizes in the other. How well each explanation is supported differs. For the lignin project the explanation is a demonstrated p-value floor, so its per-OTU null is uninformative. For the AMR project the explanation is the authors' interpretation and remains a hypothesis. Neither null should be read as established evidence of absence, but only the first is known to be uninformative [src: amr_strain_variation, lignin_community_enrichment].

## Metadata-limited null: AMR gene-count temporal trends

The temporal analysis covered 513 species with >=20 genomes spanning >=3 years (post-1990). None showed a significant temporal trend in antimicrobial-resistance (AMR) gene count after [[entities/benjamini-hochberg-fdr]] correction. The regression slopes were roughly symmetric around zero, with 251 positive and 262 negative [src: amr_strain_variation].

The report does not treat this as evidence that temporal trends are absent. It argues that the null likely reflects sparse and noisy collection-date metadata in [[entities/ncbi-biosample]] records. It cites well-documented AMR expansions in species such as [[entities/staphylococcus-aureus]] and [[entities/klebsiella-pneumoniae]] as reasons to expect real trends [src: amr_strain_variation].

The report also states as a limitation that only 70% of genomes had parseable collection dates. It names incomplete date metadata as the likely driver of the temporal null [src: amr_strain_variation].

As a future direction, the report proposes partnering with NCBI metadata curation to obtain higher-quality collection dates for temporal trend analysis. This is a proposal to improve the existing analysis. It does not mean the temporal analysis was never done [src: amr_strain_variation].

## Design-limited null: per-OTU lignin enrichment

With n=3 per group, pairwise [[entities/mann-whitney-u-test]] comparisons have a minimum achievable p-value of 0.10, because 3 vs 3 allows only 10 possible permutations. Pairwise [[entities/permanova]] (permutational multivariate analysis of variance) with 3 vs 3 samples has a permutation floor of p~0.10. These pairwise tests therefore cannot reach significance, and FDR-corrected significance is impossible for individual OTUs (operational taxonomic units). Tests that pool more samples do gain power. Global tests reach significance: the [[entities/kruskal-wallis-test]] across all 7 groups, and global PERMANOVA. The factorial PERMANOVA design (M2, n=12 for Round 2) is the most powerful test available. It gives significant results for both R1 history (p=0.002) and R2 carbon source (p=0.018) [src: lignin_community_enrichment].

With n=3 per group, no individual OTU reached FDR significance (minimum p=0.10 for Mann-Whitney with 3 vs 3). The report gives its differential-abundance results as CLR (centred log-ratio) differences, which are effect sizes. It notes that effect sizes such as CLR differences and R² values stay interpretable even when p-values are constrained [src: lignin_community_enrichment].

## Comparing the two nulls

The two nulls arise for different reasons, and their causes are shown with different strength. In the lignin study, the cause is a mathematical floor on achievable p-values. The source states this directly, and significant results from pooled and factorial tests on the same data corroborate it. The pairwise null is therefore known to be uninformative [src: lignin_community_enrichment]. In the AMR study, metadata incompleteness is the authors' interpretation, not a demonstrated mechanism. The suggestion that the null hides real trends should be treated as a hypothesis that the 513-species analysis did not test directly [src: amr_strain_variation].

## Tensions

The AMR report records a corrected null for temporal trends. It also states that the null likely does not reflect a true absence of trends, citing documented expansions in *S. aureus* and *K. pneumoniae*. The two claims do not contradict each other, but the second rests on outside knowledge rather than on an analysis within the report. The null itself stands, and its explanation remains unresolved [src: amr_strain_variation].

## Open Directions

- Re-run the AMR temporal regressions using only genomes with parseable dates, and stratify species by date completeness to test whether date sparsity explains the null. The report says only 70% of genomes had parseable dates [src: amr_strain_variation].
- Use a positive control. Check whether the date-filtered pipeline recovers the expected AMR expansion in *S. aureus* and *K. pneumoniae* before treating the corrected null across 513 species as uninformative [src: amr_strain_variation].
- For the lignin enrichment, rank OTUs by CLR effect size and validate the top candidates with designs that have more replicates. Re-analysing the existing data cannot get past the n=3 pairwise floor of 0.10 [src: lignin_community_enrichment].
