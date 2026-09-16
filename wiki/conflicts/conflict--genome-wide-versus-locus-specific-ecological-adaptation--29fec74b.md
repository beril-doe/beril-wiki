<!-- tension-hash: 29fec74b06bb98c4 -->
# Does Pangenome Openness Bear on Genome-Wide Versus Locus-Specific Ecological Adaptation?

This tension sits within [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]]. It asks whether broad pangenome structure can show if ecology shapes bacterial gene content across the whole genome or only at particular loci. Pangenome openness describes how much new gene content keeps appearing as more genomes of a species are sampled. Here phylogeny means evolutionary relatedness among genomes. The evidence gives a null result: openness did not predict environment or phylogeny effects, and that test did not look at individual loci or functional categories. [src: pangenome_openness] So it is unresolved whether openness metrics hide category-specific ecological associations. [src: pangenome_openness, ecotype_functional_differentiation]

## Evidence Sides

**Side 1: Openness does not predict environment or phylogeny effects**

The null relationship between pangenome openness and environment or phylogeny effects **qualifies** the reading that broad pangenome structure can explain genome-wide versus locus-specific ecological dynamics. Openness did not predict either effect. [src: pangenome_openness] This is a null result at the level of whole-pangenome openness. The test did not directly compare individual loci or functional categories. [src: pangenome_openness] It is therefore evidence against openness as a predictor. It is not evidence that ecology acts only genome-wide, or only at specific loci.

**Side 2: Evidence for functional differentiation stands, and category-level associations remain open**

The openness null result does not contradict the evidence for functional differentiation. It leaves unresolved whether openness metrics conceal category-specific ecological associations. [src: pangenome_openness, ecotype_functional_differentiation] On this side, ecological signal could be concentrated in particular functional categories. A coarse whole-pangenome measure such as openness could then miss it, even though the null result itself stands. [src: pangenome_openness, ecotype_functional_differentiation]

## Possible Reconciliations

- **Hypothesis: resolution mismatch.** Openness is a measure of broad pangenome structure, and the openness test did not directly compare individual loci or functional categories. [src: pangenome_openness] Ecological effects may act within particular functional categories and average out at the whole-pangenome scale, so both sides could hold at once.
- **Hypothesis: accessory genes acquired without regard to niche.** Accessory genes are those whose presence varies among genomes within a species. The genes that make a pangenome open may be gained opportunistically rather than in a niche-specific way, so openness would be uninformative about ecology even where specific loci respond to environment. [src: pangenome_openness]

## Resolving Work

- **Category-stratified openness:** Using the pangenomes already analysed, compute openness separately for each functional category (for example COG, Clusters of Orthologous Groups, categories). Then test whether category-specific openness predicts environment or phylogeny effects where whole-pangenome openness did not.
- **Locus-level association:** For species with ecotype assignments (ecotypes being within-species groups of genomes that share distinct gene content), test individual accessory gene families for association with environment versus phylogeny. Then ask whether species with more ecologically associated loci differ in openness.
- **Joint species set:** Run both the openness analysis and the ecotype functional-differentiation analysis on the same species. This tests directly whether functional differentiation is present in species where openness shows no signal.
- **Openness-matched comparison:** Pair species of similar openness that differ in ecotype functional differentiation. Compare which functional categories carry the differentiation, to see whether openness conceals category-specific structure.
