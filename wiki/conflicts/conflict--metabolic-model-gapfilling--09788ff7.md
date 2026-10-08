<!-- tension-hash: 09788ff7935b3c40 -->
# Is latent metabolic capability tied to gene conservation or to pangenome openness?

On [[concepts/metabolic-model-gapfilling]], latent capabilities are genomically complete pathways that show no detectable fitness importance under the conditions tested. [src: metabolic_capability_dependency, pathway_capability_dependency] Pangenome openness is the share of a species' gene clusters that are accessory rather than core. [src: metabolic_capability_dependency, pathway_capability_dependency] The two lines of evidence point in different directions. Conservation did not differ significantly between active and latent pathways (p-value, the probability of a result this extreme under no effect, p = 0.94). Openness did track latent and variable pathways. The supporting statistics are a Spearman rank correlation (ρ or rho, a measure of how consistently two quantities rise together in rank order) and a partial correlation, which adjusts for a covariate (ρ = 0.69, p = 0.0004, n = 22, where n is sample size; partial rho=0.530, p=2.83e-203). [src: metabolic_capability_dependency, pathway_capability_dependency] The tension matters for whether a complete pathway can be read as one an organism depends on. The corpus also reports three latent fractions, 41.0%, 35.4%, and 15.8%, which come from different analyses and must not be averaged. [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]

## Evidence Sides

**Conservation side: no statistically significant active-versus-latent difference.** Comparing the conservation of active and latent pathways gave a non-significant result (p = 0.94). [src: metabolic_capability_dependency, pathway_capability_dependency] This is a null result. It neither shows that conservation is equal nor that latent pathways are less conserved than pathways the organism depends on.

**Openness side: latency and pathway variability track openness.** The latent rate correlated with pangenome openness (ρ = 0.69, p = 0.0004, n = 22 species clades). [src: metabolic_capability_dependency, pathway_capability_dependency] Variable pathway count also correlated with openness in a partial correlation (partial rho=0.530, p=2.83e-203). [src: metabolic_capability_dependency, pathway_capability_dependency]

**Non-comparable latent fractions.** The figures 41.0%, 35.4%, and 15.8% are reported as latent fractions from different analyses and must not be averaged. [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency] The source excerpts do not label 35.4% as a latent share. This page records that discrepancy and does not resolve it.

## Possible Reconciliations

- *Hypothesis:* the analyses work at different scales. Conservation was compared across pathway-organism pairs, while openness was correlated across species clades or species. [src: metabolic_capability_dependency, pathway_capability_dependency] A clade-level pattern need not appear as a pathway-level conservation difference.
- *Hypothesis:* "latent" depends on context. A pathway that is neutral under the tested conditions may matter under stress or nutrient limitation. That could blur a conservation contrast without removing the openness correlations.
- *Hypothesis:* the latent fractions differ because the projects used different organism sets, pathway sets, and classification thresholds, not because they disagree about biology.

## Resolving Work

- **Data:** the per-pair classifications from both pathway projects. **Method:** re-run the active-versus-latent conservation test within each clade, with the same unit of analysis as the openness correlation. **Question:** does a conservation difference appear once the scale matches?
- **Data:** Fitness Browser stress, nitrogen-limitation, and carbon-limitation experiments. **Method:** reclassify latent pathways by condition type. **Question:** does the conservation null persist when the label is specific to a condition?
- **Data:** the classification rules of all three analyses. **Method:** audit which category each of 41.0%, 35.4%, and 15.8% denotes, with its denominator and thresholds. **Question:** are these three figures actually comparable latent fractions? [src: discoveries, pathway_capability_dependency, metabolic_capability_dependency]
- **Data:** pangenome openness together with per-gene core or accessory status. **Method:** model the latent rate against openness and gene-level conservation jointly. **Question:** does openness predict latency independently of conservation?
