<!-- tension-hash: 8a1793daa1cb84a7 -->
# Pangenome Openness: Predictive of Gene-Content Dynamics, or Not?

Two projects in this corpus disagree about whether **pangenome openness** — the fraction of a species' gene repertoire that sits in the accessory (variable) portion rather than the core — carries any signal about the ecological and evolutionary forces shaping gene content. One analysis finds openness strongly and positively associated with the number of variable metabolic pathways once genome count is controlled; the other reports null relationships between openness and the effect sizes of environment or phylogeny on gene content. The disagreement matters because openness is widely used as a one-number summary of genome fluidity, and the two results imply opposite verdicts on whether that summary is informative. This tension arises from [[concepts/condition-specific-fitness]].

## Evidence Sides

**Side A — openness tracks pathway variability.** Variable pathway count was positively associated with pangenome openness after genome-count control, with a partial Spearman rank correlation (a rank-based association measure with a confounder held constant) of rho=0.530 at p=2.83e-203. [src: pathway_capability_dependency; pangenome_openness] The association is reported as a directional, positive effect surviving control for genome count.

**Side B — openness predicts nothing about environment or phylogeny.** Broader pangenome analyses reported null relationships between openness and environment or phylogeny effect sizes. [src: pathway_capability_dependency; pangenome_openness] This is a null result and stays a null result: no direction is claimed, and it is not evidence of a small positive effect.

## Possible Reconciliations

- *Hypothesis (predictor breadth):* the two analyses may not be testing the same quantity — openness could track a narrow, metabolism-specific axis of gene-content variability while remaining uninformative about the broader environment-versus-phylogeny partition; the corpus itself treats the pathway-variability result as one that **refines rather than resolves** the conflict for exactly this reason, pathway variability being the narrower predictor. [src: pathway_capability_dependency; pangenome_openness]
- *Hypothesis (phylogenetic non-independence):* the positive partial correlation may be inflated by shared ancestry among species, since the new analysis did not compute full phylogenetic independent contrasts — a correction that removes the shared-ancestry component of cross-species correlations; under this hypothesis the two results could converge toward the null. [src: pathway_capability_dependency; pangenome_openness]
- *Hypothesis (magnitude, not direction):* openness may index how much of a gene repertoire turns over without indicating which force drives that turnover, in which case a positive association with pathway variability and a null against environment- and phylogeny-effect sizes are both expected rather than contradictory. [src: pathway_capability_dependency; pangenome_openness]

## Resolving Work

- Recompute the openness-versus-variable-pathway association using phylogenetic independent contrasts or phylogenetic generalized least squares (PGLS, regression with residual covariance set by the tree) on the same species set: does rho=0.530 survive shared-ancestry correction? [src: pathway_capability_dependency; pangenome_openness]
- Apply the same genome-count control used on the pathway side to the environment- and phylogeny-effect analyses: does the null persist under matched confounder handling?
- Test both predictors in one model on one species set, so breadth of predictor rather than dataset differences explains the gap.
- Report per-genus or per-clade estimates for both analyses to see whether the positive and null signals separate by lineage rather than by method.
