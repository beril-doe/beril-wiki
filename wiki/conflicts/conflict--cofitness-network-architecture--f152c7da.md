<!-- tension-hash: f152c7da164dd392 -->
# Functional Coupling or Shared Ancestry: What Cross-Genome Fitness Similarity Measures

Two projects in this corpus report cross-genome signal that could reflect genuine functional coupling between genes or organisms, or could reflect nothing more than phylogenetic relatedness — and neither project has, on its own evidence, separated the two. What is at stake is whether the architecture claims collected on [[concepts/cofitness-network-architecture]] describe function or ancestry: both projects flag ancestry as an unresolved confound in their own comparisons, but they reach that position through different sampling gaps, so no single control settles both.

## Evidence Sides

**Stratified co-occurrence still tracks phylogeny (cofitness_coinheritance).** This project stratified gene-pair co-occurrence by phylogenetic distance and found that near genomes had mean phi — the gene-pair co-occurrence association statistic — of 0.102 versus 0.067 for medium-distance genomes. [src: cofitness_coinheritance] The stratification is explicitly incomplete: most organisms lacked a far stratum. [src: cofitness_coinheritance] So the design that could have shown functional coupling persisting at long distance was not available for most species, and the residual difference between the two strata that were measured is in the direction expected from shared ancestry rather than from function.

**Comparative metal fitness needs an explicit phylogenetic model (metal_cross_resistance).** The metal study likewise requires PGLS — phylogenetic generalized least squares, a regression that models the expected covariance among species induced by their shared tree — or independent contrasts, the difference-based alternative that removes that covariance before testing. [src: metal_cross_resistance] Its organisms were not phylogenetically independent, its matrices ranged from 3 to 112 metal experiments, and metal concentrations differed. [src: metal_cross_resistance] Here the confound is compounded by unequal per-organism sampling depth and non-uniform exposure, so a phylogenetic correction alone may not be sufficient without also modelling the experiment-count and concentration heterogeneity.

## Possible Reconciliations

- *Hypothesis:* the two projects face different sampling gaps — an incomplete distance stratification in one, non-independent organisms in the other — so each requires its own null rather than a shared correction.
- *Hypothesis:* functional coupling and ancestry are not separable in this corpus at all, because the strata and organism sets that would separate them (a populated far stratum; phylogenetically independent organisms) are absent by sampling rather than by biology.
- *Hypothesis:* the unequal matrix sizes (3 to 112 metal experiments) and differing metal concentrations, not phylogeny, drive most of the apparent organism-level structure. [src: metal_cross_resistance]

## Resolving Work

- Recruit genomes into the far stratum for the species that lack one, recompute stratified mean phi, and ask whether any excess over the medium-stratum value of 0.067 survives at long branch distance. [src: cofitness_coinheritance]
- Refit the metal cross-resistance comparisons under PGLS and under independent contrasts, and ask whether the same metal relationships hold under both. [src: metal_cross_resistance]
- Subsample all organisms to a common number of metal experiments and ask how much organism-level structure depends on matrices ranging from 3 to 112 experiments. [src: metal_cross_resistance]
- Model metal concentration as a covariate rather than pooling across differing concentrations, and ask whether concentration or phylogeny explains more residual variance. [src: metal_cross_resistance]
- Apply a matched permutation null that preserves phylogenetic distance while breaking functional pairing, and ask whether either project's signal exceeds it.
