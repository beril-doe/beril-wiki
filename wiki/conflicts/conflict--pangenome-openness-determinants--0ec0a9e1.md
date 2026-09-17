<!-- tension-hash: 0ec0a9e134ab38f7 -->
# Pangenome Openness: A Reproducible Metabolic Correlate, or Correlations Limited by Coverage, Thresholds and Null Results?

Pangenome openness — the propensity of a species' gene repertoire to keep expanding as more genomes are sampled — is assigned different determinants by different projects in this corpus, and the projects do not agree on how much any of them explains. One line of work treats variable metabolic capability as a reproducible candidate determinant or proxy; another reports null correlations between openness and the environment-versus-phylogeny axis, leaving the explanations offered for them as untested hypotheses; a third holds that the environmental associations are coverage-limited and should not be read as population-wide causal estimates. Whether openness has an established determinant, a reproducible correlate, or neither is therefore unsettled, and each side's answer rests on a different specification, threshold or coverage cut. This page records the disagreement carried on [[concepts/pangenome-openness-determinants]].

## Evidence Sides

**Metabolic variability as a candidate determinant.** The strongest current interpretation is that metabolic pathway variability is a reproducible candidate determinant or proxy of openness, while direct environmental and phylogenetic effects remain specification-dependent. [src: discoveries] The ecotype–openness association — ecotypes being within-species clusters of metabolic capability — **supports** metabolic diversification as an additional correlate, but its dependence on clustering thresholds and genome-count eligibility prevents it from establishing causality. [src: pathway_capability_dependency] The positive latent-capability association (latent capability = a genomically complete pathway with no detectable fitness importance under tested conditions) **further supports** this correlate while leaving unresolved whether openness promotes fitness-neutral capabilities, whether shared ecological context produces both, or whether both are affected by sampling and community interactions. [src: metabolic_capability_dependency]

**The null result on environment and phylogeny.** On this side the reported correlations between openness and environment or phylogeny effects were null, and the HGT (horizontal gene transfer) and core/accessory explanations offered for them remain hypotheses requiring functional and transfer-specific tests, not established consequences of the null correlations. [src: pangenome_openness]

**Coverage limitation on environmental associations.** The AlphaEarth (environmental-embedding) associations should be treated as coverage-limited and not as population-wide causal estimates because only 6.8% of species had sufficient coverage. [src: discoveries]

**Conservation as a weak, condition-dependent distinction.** The fitness study **supports** a functional distinction between core and accessory genes but **refines** any interpretation that conservation alone explains pangenome openness: its conservation gradient was statistically robust yet weak, and core genes also showed condition-specific and opposing fitness effects. [src: fitness_effects_conservation]

## Possible Reconciliations

- *Hypothesis:* the sides measure different layers — metabolic variability may correlate with openness while environment and phylogeny, as specified, do not, so a null on one axis need not contradict a correlate on another.
- *Hypothesis:* the metabolic correlates and the openness estimate share a sampling dependency (genome counts, clustering thresholds, coverage eligibility), and part of the association is an artifact of how each was constructed.
- *Hypothesis:* shared ecological context generates both variable metabolism and expandable repertoires, making the correlate real but non-causal in either direction.

## Resolving Work

- Re-estimate the environmental association on species that pass coverage eligibility versus those that do not, holding the openness estimator fixed: does the null survive when coverage is the only thing varied? [src: discoveries, pangenome_openness]
- Recompute the ecotype–openness relation across a sweep of clustering thresholds and genome-count cutoffs: is the correlate threshold-stable or threshold-created? [src: pathway_capability_dependency]
- Test latent capabilities against transfer-specific evidence (HGT-flagged loci) rather than against gene-content correlations: are neutral pathways preferentially recently acquired? [src: metabolic_capability_dependency, pangenome_openness]
- Stratify the conservation gradient by condition to ask whether core genes with opposing fitness effects are the ones driving apparent openness. [src: fitness_effects_conservation]
