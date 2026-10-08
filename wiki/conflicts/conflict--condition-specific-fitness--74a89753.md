<!-- tension-hash: 74a89753d503ddf1 -->
# Do Active Metabolic Dependencies Sit Higher in the Pangenome Core Than Latent Capabilities?

Two pathway-level analyses disagree on whether metabolic pathways that organisms actively depend on are more conserved across their pangenomes than pathways they carry but do not depend on (latent capabilities). Gene-level work associates essentiality and strong fitness effects with higher core fractions. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome] The disagreement decides whether that gradient carries over to whole pathways, or whether pathway carriage follows a different logic, such as pathway variability tracking pangenome openness, the degree to which a species' pangenome keeps acquiring new genes. It bears on [[concepts/condition-specific-fitness]], [[concepts/gene-essentiality]], [[concepts/ecotype-environment-gene-content]] and [[concepts/pangenome-conservation-fitness-decoupling]].

## Evidence Sides

**Latent capabilities are no less conserved than active dependencies.** Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies. The test of active greater than latent was not significant (p = 0.94; a p-value is the probability, assuming no true difference, of a result at least this extreme in the tested direction). [src: metabolic_capability_dependency] This null result runs against gene-level analyses, which associate essentiality and strong fitness effects with higher core fractions. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome] In the same study, the latent rate tracked openness. [src: metabolic_capability_dependency; pathway_capability_dependency; pgp_pangenome_ecology] The metric here is complete-pathway carriage across species genomes. [src: metabolic_capability_dependency, pathway_capability_dependency]

**Active dependencies are slightly more core.** A newer analysis found mean core gene completeness of 0.986 for Active Dependencies versus 0.975 for Latent Capabilities. [src: pathway_capability_dependency] This comparison covered only 7 matched model organisms with near-complete core genomes, which compresses the comparison. [src: pathway_capability_dependency] The larger analysis in that work links pathway variability, not pathway dependency, to openness. [src: pathway_capability_dependency] Separately, plant growth-promoting (PGP) genes were mostly more core than the 46.8% baseline. [src: metabolic_capability_dependency; pathway_capability_dependency; pgp_pangenome_ecology]

**Evidence that does not settle it.** National Microbiome Data Collaborative (NMDC) community data showed negative leucine and arginine associations. These do not resolve the tension, because GapMind, a pathway-completeness predictor, measures genomic potential rather than expression or essentiality, and abiotic controls were unavailable. [src: nmdc_community_metabolic_ecology]

The two sides use different metrics, and both differences are small. Neither side is preferred here. [src: metabolic_capability_dependency, pathway_capability_dependency]

## Possible Reconciliations

- *Hypothesis:* the sides disagree because they measure different things. Complete-pathway carriage across genomes and the core completeness of a pathway's genes may diverge even when the underlying biology is the same.
- *Hypothesis:* the near-complete core genomes of the 7 model organisms leave little room for any difference, so the newer direction may not generalize. [src: pathway_capability_dependency]
- *Hypothesis:* the gene-level gradient holds for individual genes but is diluted at the pathway level, where pangenome openness drives pathway variability more than dependency does.

## Resolving Work

- Apply both metrics, complete-pathway carriage and core gene completeness, to the same organism set. This would test whether the opposite directions are an artifact of metric choice.
- Extend the dependency classification beyond model organisms to species with open, incompletely annotated pangenomes. This would test whether near-complete genomes compress the active-versus-latent gap.
- Within each organism, compare core fraction for genes in active-dependency pathways against genes in latent pathways, matched by fitness category. This would test whether the gene-level gradient survives aggregation into pathways.
- Model latent rate jointly on pangenome openness and dependency class. This would test whether openness, not dependency, explains conservation differences.
- Pair NMDC GapMind completeness with metatranscriptomic data (community-wide RNA sequencing that measures which genes are expressed) and abiotic covariates. This would test whether the leucine and arginine associations reflect dependency or only genomic potential.
