<!-- tension-hash: 813fc4abf9e80e87 -->
# Conflict: Whether Environment and Metabolism Are Determinants of Pangenome Openness

Two openness analyses in this corpus disagree about whether a species' pangenome openness — the propensity of its gene repertoire to keep expanding as more genomes are sampled — has environmental or metabolic determinants at all. One analysis reports a null: no significant environment or phylogenetic relationship. The other reports strong associations, both between variable metabolic pathways and openness and between ecological breadth and pathway completeness. The disagreement matters because the two answers imply different research programs: if no such relationship is detectable, openness is treated as a description of gene-content sampling rather than as an ecological readout; if the associations hold, openness is a readout of metabolic flexibility and niche range and belongs in models of habitat adaptation. This page records the disagreement for [[concepts/pangenome-openness-determinants]] without resolving it.

## Evidence Sides

**Side A — no environmental or phylogenetic determinant.** One openness analysis reported no significant environment or phylogenetic relationship with openness. [src: discoveries] The new analysis **supports** this null side for its harmonized openness-versus-effect test — a test of openness against environment and phylogeny effects — but explicitly does not test the pathway or AlphaEarth associations directly, so its support is confined to the openness-versus-effect comparison. [src: pangenome_openness] This side is a null result and stays a null result: it reports absence of a detected relationship, not a demonstrated absence of one.

**Side B — variable metabolism and ecological breadth do associate.** The other openness analysis found strong associations between variable metabolic pathways — pathways present in some genomes of a species and absent in others — and openness, and separately between ecological breadth, the range of habitats a species is recorded from, and pathway completeness, the fraction of a pathway's steps a genome encodes. [src: discoveries] These are two distinct associations with two different response variables (openness, pathway completeness), only the first of which is the same response variable Side A tested.

## Possible Reconciliations

- **Hypothesis: predictor definition.** The tension may reflect differences in predictor definition, so that the two analyses regressed openness on predictors that are not the same quantity and both results could hold. [src: discoveries]
- **Hypothesis: genome-count control.** Openness estimates depend on how many genomes are sampled per species; differing genome-count control could generate the discrepancy. [src: discoveries]
- **Hypothesis: species inclusion.** The two analyses may cover non-overlapping species sets. [src: discoveries]
- **Hypothesis: environmental coverage.** Differing environmental coverage, rather than a simple contradiction about whether environment matters, may drive the split. [src: discoveries]

## Resolving Work

- Run the variable-pathway and ecological-breadth regressions on the same harmonized species set used for the openness-versus-effect test: do Side B's associations survive Side A's inclusion criteria? [src: pangenome_openness]
- Recompute openness under a fixed genome-count subsampling scheme across both analyses' species, then re-test both predictor families: is the split an artifact of genome-count control? [src: discoveries]
- Test openness directly against the AlphaEarth predictors, which the supporting null analysis did not test, to determine whether the null extends to that predictor set. [src: pangenome_openness]
- Compare the environmental coverage of each analysis' species set, and re-test Side B's ecological-breadth-versus-pathway-completeness association restricted to the habitats both cover. [src: discoveries]
