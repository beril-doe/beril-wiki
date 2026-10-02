<!-- tension-hash: 519f408972c2370b -->
# Do Latent Metabolic Capabilities Differ in Conservation from Active Dependencies?

Two projects that sort metabolic pathways into *active dependencies* (the organism measurably needs them) and *latent capabilities* (encoded but with no measured growth requirement) disagree about whether dependency predicts pangenome conservation — the fraction of strains in a species that carry a gene, with "core" meaning near-universal. One reports a null, with latent pathways if anything slightly more conserved; the other reports a small gap in the opposite direction. At stake is whether the gene-level rule that fitness importance tracks conservation survives aggregation to pathways, as drawn in [[concepts/condition-specific-fitness]], [[concepts/gene-essentiality]] and [[concepts/ecotype-environment-gene-content]]. A community-scale amino-acid analysis over NMDC — the community metagenome and metabolite data collection that project draws on — cannot arbitrate: the NMDC negative leucine and arginine associations do not resolve this tension because GapMind (which infers pathway completeness from genome sequence) measures genomic potential, not expression or essentiality, and abiotic controls were unavailable. [src: nmdc_community_metabolic_ecology]

## Evidence Sides

**Pathway-level null — latent no less conserved.** Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, and the active-greater-than-latent comparison was not significant (p = 0.94, the probability of a result this extreme if the classes did not differ). [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome] In the same study latent rate tracked openness — how readily a species' pangenome keeps admitting new genes. [src: metabolic_capability_dependency; pathway_capability_dependency; pgp_pangenome_ecology] This side holds the null as a null, not as a weak positive.

**Gene-level gradient — importance tracks core membership.** Gene-level analyses associate essentiality and strong fitness effects with higher core fractions, which is the expectation the pathway-level result fails to reproduce. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome]

**Matched 7-organism comparison — a small active-over-latent gap.** The new 7-organism analysis instead found mean core gene completeness of 0.986 for Active Dependencies versus 0.975 for Latent Capabilities, but its model-organism coverage and near-complete genomes compress the comparison; the same project's larger analysis links pathway *variability* — not pathway dependency — to openness. [src: pathway_capability_dependency] Adjacent support: PGP (plant-growth-promoting) genes were mostly more core than the 46.8% baseline. [src: metabolic_capability_dependency; pathway_capability_dependency; pgp_pangenome_ecology]

## Possible Reconciliations

- **Aggregation hypothesis:** pathway-level means may wash out a gene-level gradient, so both the 0.869-versus-0.829 null and the gene-level association could hold at their own scales. Untested.
- **Compression hypothesis:** the 0.986-versus-0.975 gap may be a direction-preserving remnant of a larger effect flattened by near-complete model genomes, as that project itself cautions. Hypothesis, not a demonstrated correction.
- **Wrong-axis hypothesis:** conservation may be governed by pathway variability rather than dependency class, making both comparisons under-powered tests of the wrong predictor.

## Resolving Work

- Re-run the dependency-versus-conservation comparison on the metabolic study's full pathway set *and* the 7-organism set under one classifier and one conservation metric: does the sign flip survive harmonization?
- Recompute the pathway comparison from constituent gene conservations rather than pathway means, testing whether aggregation alone converts a gene-level gradient into p = 0.94.
- Extend the 7-organism validation to non-model taxa with draft-quality genomes, asking whether the 0.986/0.975 gap widens when genome completeness stops being near-uniform.
- Model conservation jointly on dependency class and pathway variability to test which predictor carries the openness relationship.
- Pair GapMind completeness with expression or transposon-fitness data on shared samples, so latency can be distinguished from unexpressed potential.
