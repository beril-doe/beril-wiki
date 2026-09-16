<!-- tension-hash: 7b9c5a6c4be7d241 -->
# Does the Prophage–AMR Association Survive Shared Ancestry, Given That Pangenome Openness Does Not Predict the Magnitude of Environment or Phylogeny Effects?

This page records a tension raised in [[concepts/phylogenetic-confounding-of-pangenome-associations]]. Phylogenetic confounding means that differences among taxonomic groups can create or hide an association between two traits that share the same taxonomic distribution. One analysis reports that the density of prophage markers (genes from bacteriophage genomes integrated into a bacterial chromosome) remained associated with antimicrobial resistance (AMR) repertoire breadth across all five reported major phyla. [src: prophage_amr_comobilization; pangenome_openness] Another reports that pangenome openness did not predict the magnitude of environment or phylogeny effects. [src: prophage_amr_comobilization; pangenome_openness] Pangenome openness is the degree to which a species keeps gaining new genes as more genomes are sampled. The two results concern different predictors and response variables, so neither settles the other. [src: prophage_amr_comobilization] The question matters because a prophage–AMR link driven by shared ancestry, or by open-pangenome lineages collecting many mobile elements, would mean something different from a co-mobilization signal, in which AMR genes and prophages move together as jointly transferred genetic material.

## Evidence Sides

**Prophage density tracks AMR breadth across phyla**

Prophage marker density remained associated with AMR repertoire breadth across all five reported major phyla and after controlling for genome count. [src: prophage_amr_comobilization; pangenome_openness]

**Openness does not predict environment or phylogeny effects**

The openness analysis found that openness did not predict the magnitude of environment or phylogeny effects. [src: prophage_amr_comobilization; pangenome_openness] This is a null result about openness. It is not evidence about prophage density or AMR breadth.

**Why the two do not combine into a verdict**

These results concern different predictors and response variables. They therefore do not establish whether prophage density is independent of shared ancestry, or whether the association reflects open-pangenome lineages acquiring multiple mobile elements. [src: prophage_amr_comobilization]

## Possible Reconciliations

- **Hypothesis A (ancestry-independent link):** Prophage density and AMR breadth are linked through co-mobilization, independent of shared ancestry.
- **Hypothesis B (lineage-level confounding):** Shared ancestry at finer ranks, such as genus or species, drives both traits. The reported results do not establish whether this occurs.
- **Hypothesis C (open-pangenome mediation):** Lineages with open pangenomes acquire many mobile elements, including both prophages and AMR genes. The openness null result concerns environment and phylogeny effect sizes, not mobile-element load, so it does not rule this out.

## Resolving Work

- Use the species-level pangenome data with phylogenetic generalized least squares (PGLS, a regression that accounts for shared ancestry through a phylogeny). Ask whether prophage marker density still predicts AMR repertoire breadth once phylogenetic covariance is modelled.
- Add each species' pangenome openness estimate as a covariate or mediator in the prophage–AMR model. Ask whether openness accounts for the association, which would test Hypothesis C.
- Fit within-genus or within-family stratified models on the same prophage and AMR inventories. Ask whether the association persists below the phylum rank, which would test Hypothesis B.
- Run a permutation test that shuffles prophage density within clades while preserving clade structure. Ask whether the observed association exceeds what clade membership alone produces.
