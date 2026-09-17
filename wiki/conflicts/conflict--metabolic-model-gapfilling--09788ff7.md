<!-- tension-hash: 09788ff7935b3c40 -->
# Does Pangenome Dynamics Explain Latent Metabolic Capability When Conservation Does Not?

Two analyses of the same phenomenon — genomically complete pathways that show no fitness importance under tested conditions ("latent capabilities") — point in different directions about what predicts them. A gene-conservation test failed to detect any difference between active and latent pathways, while species-level pangenome openness (the fraction of a species' gene clusters that are accessory rather than core) tracked latency strongly. Compounding this, different analyses report three different latent fractions that must not be averaged. The disagreement matters for [[concepts/metabolic-model-gapfilling]]: if latency is an evolutionary property visible in pangenome structure but invisible in conservation, then gapfilled models — models completed by adding inferred reactions so growth can be simulated — and completeness-based models cannot be validated by conservation arguments alone, and the fraction of model content that is fitness-inert depends on which classification one adopts.

## Evidence Sides

**Conservation does not separate active from latent pathways (null result).** The comparison of active-versus-latent conservation was non-significant, p = 0.94. [src: metabolic_capability_dependency, pathway_capability_dependency] This is a null result, not a small effect: it states that conservation of a pathway's genes failed to distinguish pathways whose genes carry fitness signal from those whose genes do not.

**Pangenome openness does track latency (positive correlations).** Latent rate correlated with openness at Spearman ρ = 0.69, p = 0.0004, n = 22, where Spearman ρ is a rank correlation and n counts species clades, not organisms. [src: metabolic_capability_dependency, pathway_capability_dependency] Separately, variable pathway count correlated with openness at partial rho = 0.530, p = 2.83e-203 — a partial correlation, i.e. one computed after controlling for a covariate. [src: metabolic_capability_dependency, pathway_capability_dependency]

**The latent fractions are not interchangeable.** Latent fractions of 41.0%, 35.4%, and 15.8% come from different analyses and must not be averaged. [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]

## Possible Reconciliations

- *Hypothesis:* conservation and pangenome openness measure latency at different levels — per-gene sequence retention versus species-level gene turnover — so a per-gene null (p = 0.94) and a clade-level correlation (ρ = 0.69, p = 0.0004, n = 22) can both hold without contradiction. [src: metabolic_capability_dependency, pathway_capability_dependency]
- *Hypothesis:* the openness signal is driven by pathway presence/absence variation across genomes (partial rho = 0.530, p = 2.83e-203) rather than by the fitness-neutrality of complete pathways, making the two correlations partly non-overlapping constructs. [src: metabolic_capability_dependency, pathway_capability_dependency]
- *Hypothesis:* the spread between 41.0%, 35.4%, and 15.8% reflects denominator and threshold choices, so any apparent agreement or disagreement about "how latent" bacterial metabolism is is an artifact of classification scheme until denominators are matched. [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]

## Resolving Work

- Re-run the active-versus-latent conservation test on the same clade-aggregated unit used for the openness correlation (n = 22): does the null at p = 0.94 persist when the unit of analysis matches? [src: metabolic_capability_dependency, pathway_capability_dependency]
- Recompute each latent fraction on a single shared denominator and threshold grid, reporting all three side by side rather than a pooled value: how much of the 41.0%/35.4%/15.8% spread is denominator, how much is threshold? [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]
- Partial the conservation metric into the openness–latency correlation: does ρ = 0.69 survive conditioning on conservation, and does conservation gain signal conditioned on openness? [src: metabolic_capability_dependency, pathway_capability_dependency]
- Separate variable-pathway count from latent-capability rate as predictors of openness, since only the former carries the partial rho = 0.530, p = 2.83e-203 result: are these one signal or two? [src: metabolic_capability_dependency, pathway_capability_dependency]
