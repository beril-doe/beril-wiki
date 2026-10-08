<!-- tension-hash: 52cc7c498f332f18 -->
# Do Cofitness Co-inheritance Signals Generalize Better at the Module Level Than for Gene Pairs?

This disagreement concerns the unit at which laboratory cofitness predicts whether genes are inherited together across genomes. Cofitness means genes with correlated fitness profiles in transposon-mutant experiments. Co-inheritance means the genes co-occur across genomes. Pairwise tests show a small signal, and a cross-organism consistency test was not significant, so consistency across organisms is not established [src: cofitness_coinheritance]. Module-level tests show a larger signal, strongest for accessory modules [src: cofitness_coinheritance]. The limits on that module result come from more than one project. It is unclear whether modules are the more general unit of co-inheritance or whether the module advantage holds only for a small, uneven subset. The answer affects how [[concepts/cofitness-network-architecture]] treats fitness modules as evolutionary units.

## Evidence Sides

**Side A: pairwise cofitness gives a small signal whose cross-organism consistency is not established.** Co-occurrence is measured as delta phi: the phi coefficient (a correlation for binary presence/absence) of cofit gene pairs minus that of prevalence-matched random pairs. Cofit pairs had a mean delta phi of +0.011 across organisms, but the aggregate delta was +0.003. The Wilcoxon signed-rank test, a nonparametric test of whether per-organism effects are consistently non-zero, gave p=0.13. That is a null result: it does not show cross-organism consistency, and it does not show the signal is absent [src: cofitness_coinheritance].

**Side B: module-level signals are larger, suggesting the hypothesis that modules are stronger co-inheritance units.** Modules come from independent component analysis (ICA), a decomposition that groups genes into co-varying fitness modules. ICA modules had delta phi=+0.053 overall, and accessory modules reached +0.108 [src: cofitness_coinheritance]. These figures suggest the hypothesis that modules, not pairs, may be the stronger units of co-inheritance [src: cofitness_coinheritance].

**Side C: limits on generalizing the module advantage.**
- In the organism Korea, no modules were significant, because all were >90% core (present in nearly all genomes of the species) with prevalence near 1.0 [src: cofitness_coinheritance].
- The accessory-versus-core difference was only near significant (p=0.051) [src: cofitness_coinheritance].
- Across the mapped module set, only 5% of modules were accessory, so accessory-module advantages cannot be generalized [src: module_conservation].

## Possible Reconciliations

- **Hypothesis 1, aggregation effect:** Modules may pool many weak pairwise associations into a detectable signal. If so, the module and pairwise results describe the same biology at different resolutions rather than contradicting each other.
- **Hypothesis 2, prevalence ceiling:** Where genes are almost universally present, as in Korea, phi has little variance to work with. Weak pairwise signals and absent module signals could then reflect limited measurability rather than an absence of co-inheritance.
- **Hypothesis 3, rare-class inflation:** The accessory-module advantage may come from a small, unrepresentative subset of modules. It may not reflect a property of fitness modules in general.

## Resolving Work

- Use the module set from the module-conservation analysis and resample core modules down to the accessory class size. Compare delta phi across classes to test whether the accessory advantage persists in a size-balanced comparison; this cannot by itself show that accessory modules are representative.
- Within each organism, compare delta phi for pairs drawn from the same ICA module against cofit pairs outside any module. This tests whether module membership, rather than aggregation alone, carries the signal.
- Stratify pairwise and module delta phi by gene prevalence bins. This tests whether near-universal prevalence, as seen in Korea, suppresses detectable co-inheritance.
- Repeat module-level tests with alternative core/accessory classification cutoffs. This checks whether the near-significant accessory-versus-core difference depends on the thresholds chosen.
