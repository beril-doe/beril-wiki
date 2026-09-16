<!-- tension-hash: 8325c1f480a748fe -->
# Does Module-Level Aggregation Rescue Weak Cross-Tenant Fitness Bridges?

Two projects that join gene-fitness data to other data collections in the KBase Data Lakehouse find weak signal for gene pairs or condition-based predictors. They disagree on whether grouping genes into multi-gene modules recovers that signal. The co-fitness project reports stronger effects for modules than for gene pairs [src: cofitness_coinheritance]. The field-versus-lab project finds no significant link between module conservation and field activity [src: field_vs_lab_fitness]. This matters for [[concepts/cross-tenant-data-bridging]]. If modules carry the signal, bridging analyses should be built around them. If they do not, the weak bridges may reflect limits of the data rather than of the unit of analysis.

## Evidence Sides

**Side A: pairwise signal is weak, and modules show stronger effects**

The co-fitness project linked co-fitness (correlated fitness profiles of two genes across conditions) to gene co-occurrence across genomes. It reports weak pairwise effects but stronger module-level effects [src: cofitness_coinheritance]. Co-fitness strength was anti-correlated with co-occurrence (Spearman rank correlation rho=-0.109, p<1e-300 across 1.04M pairs, where p is the p-value, the probability of a result at least this extreme if no association existed) [src: cofitness_coinheritance]. This required auxiliary-only comparisons below 95% prevalence [src: cofitness_coinheritance]. The negative direction is a measured result; one possible interpretation, not established here, is that it reflects confounding rather than absent functional coupling.

**Side B: the bridge is weak whether the unit is conditions or modules**

The field-versus-lab study found that condition-only prediction is weak. Its AUC values (area under the receiver-operating-characteristic curve, where higher values mean better discrimination than chance) were 0.548 for field plus lab combined, 0.517 for field-only and 0.531 for lab-only [src: field_vs_lab_fitness]. It found no significant correlation between module conservation and field activity (rho=0.071, p=0.62) [src: field_vs_lab_fitness]. This is a null result at the module level. The study does not report the module-level gain described in Side A.

## Possible Reconciliations

- *Hypothesis:* The two projects ask different module-level questions. One relates co-fitness to co-occurrence [src: cofitness_coinheritance]. The other tests whether module conservation tracks field activity [src: field_vs_lab_fitness]. A module effect for the first question need not appear for the second.
- *Hypothesis:* A prevalence ceiling affects both projects. Most genes in fitness-profiled organisms may fall in near-universal clusters, leaving too little variance to detect a conservation signal. The co-fitness analysis required auxiliary-only comparisons below 95% prevalence [src: cofitness_coinheritance]; the evidence does not say whether the field-versus-lab module test used such a restriction.
- *Hypothesis:* The weak condition-level AUCs reflect the fitness data itself rather than the bridge. If so, aggregating into modules cannot recover signal that is missing from the inputs.

## Resolving Work

- Rerun the field-versus-lab module-conservation correlation using only auxiliary genes below 95% prevalence. This tests whether the null result in Side B is driven by a prevalence ceiling.
- Use one shared module definition for both analyses. Test whether module-level co-occurrence enrichment and module field-activity correlation agree on the same modules.
- Regress co-occurrence on co-fitness while controlling for gene prevalence and phylogenetic distance. This tests whether the negative rho in Side A persists after these controls or is fully explained by confounding.
- Add module membership as a predictor in the field-versus-lab classifier. This tests whether it raises AUC above the condition-only models, which would show whether modules carry information that conditions do not.

## Open Directions

- Compare the auxiliary-only, below-95% restriction across both projects to settle whether the module-level disagreement is a methodological artifact or a real difference between the two bridges.
