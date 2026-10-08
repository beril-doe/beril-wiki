<!-- tension-hash: f152c7da164dd392 -->
# Functional Coupling or Shared Ancestry? Cross-Organism Signals in Fitness Networks

Two projects that read biological coupling from patterns across many bacteria both report that shared ancestry has not been ruled out, so it is unresolved whether those patterns show functional coupling or inherited relatedness. In the gene co-inheritance study, the open question is whether genes that are cofit in the lab (their mutant fitness profiles correlate across conditions) are co-inherited because they work together or because related genomes share gene content. In the metal study, the open question is whether patterns that recur across organisms are independent observations. This matters for [[concepts/cofitness-network-architecture]], which treats cofitness and cross-organism consistency as evidence of functional architecture while ancestry confounding in these comparisons remains unresolved.

## Evidence Sides

**Co-inheritance signal tracks phylogenetic distance**

The study scored co-occurrence of gene pairs across genomes with phi, a correlation coefficient for presence/absence data. Cofit gene pairs had higher phi among near genomes (mean phi=0.102) than among medium-distance genomes (mean phi=0.067). [src: cofitness_coinheritance] Most organisms lacked a far stratum of genomes, which limits the ability to disentangle functional coupling from ancestry. [src: cofitness_coinheritance] On this evidence, functional coupling remains confounded by ancestry. This is an unresolved confound, not a finding that coupling is absent. [src: cofitness_coinheritance]

**Cross-organism metal patterns lack phylogenetic correction**

The metal cross-resistance study likewise needs PGLS (phylogenetic generalized least squares, a regression that models trait covariance expected from a phylogeny) or independent contrasts (differences between sister lineages that remove shared phylogenetic history). Its organisms were not phylogenetically independent. [src: metal_cross_resistance] The comparison is also uneven in other ways. Per-organism matrices ranged from 3 to 112 metal experiments, and metal concentrations differed between experiments. [src: metal_cross_resistance] Cross-organism agreement therefore cannot yet be attributed to conserved mechanism rather than shared lineage or unequal sampling. [src: metal_cross_resistance]

## Possible Reconciliations

- *Hypothesis:* Both signals mix a real functional component with a phylogenetic one, and neither study has yet separated the two.
- *Hypothesis:* The confound may weigh differently in the two settings. Co-inheritance across conspecific genomes may be more sensitive to ancestry than fitness correlations measured within each organism and only then compared across organisms. This is untested.
- *Hypothesis:* In the metal study, uneven experiment counts and concentrations may introduce non-phylogenetic heterogeneity that either masks or mimics phylogenetic structure.

## Resolving Work

- **Co-inheritance:** Add genomes that fill the missing far stratum for the cofitness organisms. Recompute cofit versus random phi by distance stratum to test whether excess phi persists at large phylogenetic distance.
- **Metal cross-resistance:** Build a species tree for the metal-study organisms. Refit cross-organism metal-pair correlations with PGLS or independent contrasts to test whether directional consistency survives phylogenetic correction.
- **Sampling heterogeneity:** Subsample each organism's metal fitness matrix to a common experiment count, stratified by concentration. Test whether cross-organism patterns depend on matrix size or dose rather than lineage.
- **Within-lineage negative control:** Compare cofitness-predicted co-occurrence and metal-pair correlations within single clades against comparisons across clades. This would show whether signal concentrates among close relatives.
