<!-- tension-hash: 7b9c5a6c4be7d241 -->
# Prophage Density and AMR Breadth: Robust Signal or Residual Ancestry Effect?

Two projects in this corpus bear on whether pangenome-level associations survive control for shared ancestry, and they do so from different angles rather than meeting head-on. One reports an association between prophage marker density — the abundance of integrated-bacteriophage signatures (terminase, phage structural proteins, holin/lysin) in a genome — and antimicrobial resistance (AMR) repertoire breadth that persists across taxa; the other reports a null result for pangenome openness, the degree to which a species keeps acquiring new genes as genomes are added, as a predictor of whether environment or phylogeny dominates gene content. The question matters because it is unsettled whether mobile-element density is a genuine, lineage-independent driver of resistance repertoires or a correlate of lineages that happen to be both open-pangenomed and mobile-element-rich. This page records the tension at the heart of [[concepts/phylogenetic-confounding-of-pangenome-associations]].

## Evidence Sides

**Side A — the prophage association persists across phyla and under a genome-count control.** Prophage marker density remained associated with AMR repertoire breadth across all five reported major phyla and after controlling for genome count [src: prophage_amr_comobilization; pangenome_openness]. The sign of the association is not stated in the evidence, and no control beyond phylum-level reporting and genome count is reported.

**Side B — openness did not predict the magnitude of environment or phylogeny effects.** The openness analysis found that openness did not predict the magnitude of environment or phylogeny effects — that is, how strongly ecology versus shared ancestry shapes a species' gene content [src: prophage_amr_comobilization; pangenome_openness]. This is a null result and stays a null result: no effect was detected, which is not the same as a demonstrated absence of effect.

**Shared caveat — the two results are not commensurable.** These results concern different predictors and response variables, so they do not establish whether prophage density is independent of shared ancestry or whether the association reflects open-pangenome lineages acquiring multiple mobile elements [src: prophage_amr_comobilization].

## Possible Reconciliations

- *Hypothesis 1 (non-overlap):* the two analyses simply address different quantities — mobile-element density versus pangenome openness, AMR breadth versus eco-phylo effect magnitude — and no conflict exists once the predictors are aligned.
- *Hypothesis 2 (residual confounding):* phylum-level stratification plus a genome-count control is a coarser correction than a phylogenetic model, so Side A's association could still be carried by finer-grained lineage structure, which would reconcile it with Side B's null.
- *Hypothesis 3 (common cause):* open-pangenome lineages acquire multiple mobile elements together, making prophage density and AMR breadth joint symptoms of one acquisition regime rather than one causing the other [src: prophage_amr_comobilization].

## Resolving Work

- Refit the prophage-density-to-AMR-breadth relationship with phylogenetic generalized least squares (PGLS, regression that weights residuals by a phylogenetic covariance matrix) on a reference tree: does the association survive continuous ancestry control, not just phylum stratification?
- Regress AMR repertoire breadth on pangenome openness directly, within the same species set used for the prophage analysis: is the null for openness a property of the predictor or of the response variable it was tested against?
- Repeat the phylum-stratified test at genus and species level: does the association attenuate monotonically as the taxonomic grain tightens, as Hypothesis 2 predicts?
- Partition variance between prophage density and openness in a joint model: do they explain overlapping or independent shares of AMR breadth, discriminating Hypothesis 1 from Hypothesis 3?
