<!-- tension-hash: 5a54a7b7d5f3aa16 -->
# Does Pangenome Openness Track Lineage-Dependent Patterns or Not?

This page records a scope tension, not a direct contradiction. The antimicrobial resistance (AMR) pangenome analysis reports lineage-dependent associations with pangenome openness, meaning how much a species' total gene repertoire keeps growing as genomes are added. The openness-effects analysis found that openness did not predict either environment or phylogeny effect sizes in its matched species set. Here phylogeny means evolutionary relationships among species, and an effect size is the magnitude of an assessed effect [src: pangenome_openness; amr_pangenome_atlas]. This matters because the two results concern different response variables, so together they do not establish whether the within-phylum AMR patterns persist after explicit phylogenetic correction [src: pangenome_openness; amr_pangenome_atlas]. The framing comes from [[concepts/phylogenetic-confounding-of-pangenome-associations]].

## Evidence Sides

**Side A: openness associations depend on lineage (AMR analysis)**

The AMR analysis shows lineage-dependent openness associations, with patterns read within phyla rather than only in aggregate [src: pangenome_openness; amr_pangenome_atlas]. Because the two analyses concern different response variables, they do not establish whether these within-phylum AMR patterns persist after explicit phylogenetic correction [src: pangenome_openness; amr_pangenome_atlas].

**Side B: openness predicts neither environment nor phylogeny effects (openness-effects analysis)**

In the matched species set, openness did not predict either environment or phylogeny effect sizes [src: pangenome_openness; amr_pangenome_atlas]. This is a null result for openness as a predictor of those effect sizes.

## Possible Reconciliations

- **Hypothesis 1: different response variables.** Openness may relate to AMR gene content within lineages while remaining unrelated to environment or phylogeny effect sizes. This is possible because the analyses measure different outcomes [src: pangenome_openness; amr_pangenome_atlas].
- **Hypothesis 2: confounding in the AMR associations.** The lineage-dependent AMR associations may partly reflect shared taxonomic distribution rather than a within-lineage relationship. If so, they would weaken under explicit phylogenetic correction.
- **Hypothesis 3: sample scope.** The matched species set used for the openness-effects analysis may cover a different subset of lineages from the AMR analysis, so the null may not apply to the phyla where AMR patterns appear.

## Resolving Work

- **Phylogenetic correction of AMR associations.** Refit the within-phylum AMR-versus-openness associations using a phylogenetically informed regression, such as phylogenetic generalized least squares (PGLS, a regression that models trait covariance expected from shared ancestry). The question is whether the lineage-dependent patterns survive explicit correction.
- **Shared species set.** Restrict both analyses to species present in both datasets and test openness against both AMR content and environment and phylogeny effect sizes. The question is whether the divergence comes from response variable or from sample scope.
- **Within-lineage null test.** Repeat the openness-versus-effect-size test separately within each phylum that carries AMR patterns. The question is whether the aggregate null hides lineage-specific relationships.
- **Taxonomic distribution check.** Compare the taxonomic distributions of openness and AMR content across lineages. The question is whether the shared distribution alone can produce the reported associations.
