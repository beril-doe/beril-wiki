<!-- tension-hash: 797bce433eb2ce1e -->
# Tension: Pangenome openness predicts metabolic variability but not environment- or phylogeny-driven gene content

Pangenome openness — the fraction of a species' gene clusters that are accessory (strain-variable) rather than core (present in nearly all genomes) — is used across this corpus as an index of how dynamic a lineage's gene content is. Two capability studies find that openness tracks metabolic variability strongly, while the openness study itself finds that openness did not predict how much of gene content is structured by environment versus phylogeny. Whether openness is a general dynamism index or a metabolism-specific one determines whether it can be reused as a proxy in ecotype work, so the disagreement is recorded rather than averaged [src: metabolic_capability_dependency; pathway_capability_dependency; pangenome_openness]. This tension arises within [[concepts/ecotype-environment-gene-content]].

## Evidence Sides

**Openness co-varies with metabolic capability variation (positive, significant).** Latent capability rate — the per-clade fraction of complete pathways that are fitness-neutral — correlated with pangenome openness at Spearman ρ = 0.69, p = 0.0004, n = 22, where Spearman ρ is a rank correlation insensitive to nonlinear scaling [src: metabolic_capability_dependency]. Independently, variable pathway count correlated with openness at partial rho = 0.530, p = 2.83e-203, a partial correlation meaning the association survives statistical control of a covariate [src: pathway_capability_dependency].

**Openness does not predict environment or phylogeny effect sizes (null).** Openness did not predict environment or phylogeny effect sizes, with rho = -0.05 and 0.03 and p-values 0.54 and 0.73 respectively [src: pangenome_openness]. This is a null result — a failure to detect, not a weak positive — and it is reported as such; it does not cancel or dilute the positive correlations above.

## Possible Reconciliations

- **Response-variable hypothesis:** the two sides may measure different quantities — counts and rates of variable or latent metabolic traits on one side, variance-partition effect sizes on the other — so openness could index metabolic gene turnover while being uninformative about how that turnover is apportioned between environment and phylogeny. Hypothesis only; untested here.
- **Denominator/scale hypothesis:** the positive results are anchored at n = 22 clades and at pan-bacterial scale; the null may reflect a non-overlapping or differently powered sample rather than an absent relationship. Hypothesis only.
- **Confounding hypothesis:** one positive result is a partial correlation (rho = 0.530) explicitly controlling a covariate, while the reported null correlations are unadjusted; residual sampling-depth structure could mask a real association in either direction. Hypothesis only.

## Resolving Work

- Recompute environment and phylogeny effect sizes on exactly the 22 clades used for the latent-capability correlation, by the same rank-correlation method, and ask whether the null survives on the matched denominator.
- Re-run the openness-versus-effect-size correlations as partial correlations controlling genome count, and ask whether the adjustment that strengthened rho to 0.530 elsewhere changes the -0.05 and 0.03 estimates.
- Restrict both analyses to metabolic gene families only, and ask whether openness predicts environment effect size for metabolism even when it fails genome-wide.
- Report a confidence interval and a power analysis for each null estimate, and ask whether the data could have detected an effect of the size seen on the positive side.
