<!-- tension-hash: 8325c1f480a748fe -->
# Does Aggregating Genes into Modules Rescue a Weak Gene-Level Fitness-to-Genome-Content Bridge?

Two projects in [[concepts/cross-tenant-data-bridging]] join laboratory fitness measurements to comparative-genomics signals, and both report that the join is weak at the finest grain. They disagree about what happens when genes are aggregated into multi-gene modules: one project treats module-level aggregation as the level where the bridge finally carries signal, the other tests at the module level and finds nothing. Because bridge designs in this corpus choose their unit of analysis up front, the disagreement decides whether "go to modules" is a genuine remedy or a reframing of the same weak signal.

## Evidence Sides

**Modules strengthen a bridge that is weak (and inverted) pairwise.** The co-fitness bridge — co-fitness being the similarity of two genes' fitness profiles across conditions, compared against co-occurrence, their co-presence across genomes — reports weak pairwise but stronger module-level effects. Pairwise, the direction is negative: stronger co-fitness weakly predicts *lower* co-occurrence, Spearman rho (a rank correlation) = -0.109, p<1e-300 across 1.04M pairs, and the comparison has to be restricted to auxiliary genes below the 95% prevalence threshold to be interpretable at all [src: cofitness_coinheritance]. On this side, the module level is where a usable effect appears.

**Modules do not rescue the null.** The field-versus-lab study likewise finds weak condition-only prediction — AUC (area under the ROC curve, a ranking-accuracy measure where higher values mean better discrimination) 0.548, with field-only 0.517 and lab-only 0.531 — and at the module level reports **no significant correlation** between module conservation and field activity, rho=0.071, p=0.62 [src: field_vs_lab_fitness]. This is a null result, not a small positive one, and it is measured at exactly the grain the other side nominates as the remedy.

## Possible Reconciliations

- **Different-response-variable hypothesis:** the two bridges aggregate to modules but score different genomic quantities (co-occurrence between gene pairs versus conservation of a module), so a module-level gain in one need not appear in the other.
- **Prevalence-filter hypothesis:** the co-fitness result is conditioned on auxiliary-only comparisons below 95% prevalence [src: cofitness_coinheritance]; if the module-conservation test is run without an equivalent restriction, a ceiling could mask any effect.
- **Power hypothesis:** rho=0.071, p=0.62 [src: field_vs_lab_fitness] may reflect too few modules to detect an effect of the size the other side observes, rather than its absence.
- **Distinct-phenomena hypothesis:** the pairwise anti-correlation (rho=-0.109) and the claimed module-level gain may not be the same signal scaled up, so neither side's module claim generalizes.

## Resolving Work

- Re-run the module-conservation test on modules restricted to genes below the 95% prevalence threshold; does the null (rho=0.071, p=0.62) persist once the ceiling is removed?
- Apply both bridges' module definitions to the same organism set and score both response variables; is the module-level gain specific to co-occurrence?
- Run a power analysis on the module-level correlation: what effect size could rho=0.071, p=0.62 have excluded?
- Compute pairwise and module-level statistics from identical gene pairs, so the "weak pairwise, stronger module" contrast is measured within one denominator rather than across two studies.
