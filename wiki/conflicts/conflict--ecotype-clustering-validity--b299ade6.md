<!-- tension-hash: b299ade675cdeb34 -->
# Does within-dataset separation or cross-dataset reproducibility certify a microbial ecotype?

Reports in this corpus describe their microbial ecotype clusters with different statistics, and the reported values appear to disagree about whether such ecotypes are well defined. One family reports a *silhouette* score — a per-member measure of how much closer a point sits to its own cluster than to the nearest other cluster. Another reports resampling agreement as *ARI* (adjusted Rand index, a chance-corrected measure of agreement between two partitions), computed under bootstrap refits (re-clustering a dataset resampled with replacement) and under LOSO (leave-one-study-out) refits that hold out a whole study or cohort. In the comparisons cited here, these statistics answer different questions — separation within one dataset versus reproducibility across datasets — and are reported for different feature spaces, so the apparent disagreement about whether microbial ecotypes are well defined cannot be settled by comparing the reported values. [src: amr_strain_variation, ecotype_functional_differentiation, ibd_phage_targeting] This page records the disagreement for [[concepts/ecotype-clustering-validity]] rather than closing it.

## Evidence Sides

**Separation within a single dataset (silhouette).** Density-based clustering of AMR (antimicrobial resistance) profiles reported a median silhouette of 0.620 in the species where clusters were found, while auxiliary gene-content clustering reported a mean silhouette of 0.215. [src: amr_strain_variation, ecotype_functional_differentiation] Pathway-presence clustering adds a further feature space to the same comparison, with all 10 target species above silhouette 0.2 and scores reaching 0.89, values obtained on a species set that was never matched to the gene-content analysis. [src: metabolic_capability_dependency, ecotype_functional_differentiation]

**Resampling agreement, within a pooled dataset and across cohorts (bootstrap and LOSO ARI).** Gut community-composition clustering instead reported resampling statistics: on taxonomic features, bootstrap ARI 0.13–0.17 and mean LOSO ARI 0.113 across 8 sub-studies, both low; on metabolite features, a within-pooled bootstrap ARI of 0.937 that the report attributes to reproducible cohort-batch structure rather than biology, alongside cross-cohort LOSO ARI 0.000 for either held-out cohort. [src: ibd_phage_targeting]

## Possible Reconciliations

- *Hypothesis:* the two certificates are orthogonal rather than contradictory — a partition can be geometrically separated and still fail to transfer, which is the pattern the metabolite result would exhibit if cohort-batch structure is separable within a pooled dataset but absent across cohorts. [src: ibd_phage_targeting]
- *Hypothesis:* the spread among silhouettes is driven by feature space rather than by how well-defined ecotypes are — pathway presence may be more discretely distributed than auxiliary gene content, and the two analyses were run on species sets that were never matched. [src: metabolic_capability_dependency, ecotype_functional_differentiation]
- *Hypothesis:* the denominators differ in kind — the median silhouette is reported conditional on the species where clusters were found [src: amr_strain_variation, ecotype_functional_differentiation], whereas the gut ARI values are reported both within one pooled dataset and across held-out cohorts or sub-studies [src: ibd_phage_targeting] — so neither value estimates the other's quantity.

## Resolving Work

- Recompute silhouette **and** bootstrap/LOSO ARI on one matched species set, across AMR, auxiliary gene-content and pathway-presence features: do the two certificates rank the same species the same way?
- Apply the gut study's leave-one-study-out refit to genome-based clusters, using genomes partitioned by source study rather than by cohort: does geometric separation survive study hold-out?
- For each feature space, test the recovered partitions against study and isolation-source labels with an explicit association test, and re-cluster after dropping study-correlated features: how much of the reported separation tracks batch rather than biology?
- Fix an explicit certification threshold per statistic in advance and report both for every clustered species, so null and passing results are distinguishable without re-analysis.
