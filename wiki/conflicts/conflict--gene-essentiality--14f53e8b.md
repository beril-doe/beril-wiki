<!-- tension-hash: 14f53e8b313cdc13 -->
# Is Core-Genome Membership a Predictor of Gene Importance, or a Predictor of How Well a Gene Has Been Studied?

Projects in this corpus agree that essential genes tend to be core (present in every genome of a species' pangenome) but disagree about what that association licenses. One line of work treats core status and annotation richness as usable proxies for importance; another finds that a large slice of core gene space is functionally dark; a third finds that core enrichment persists among genes with no fitness effect at all, and that the core-versus-accessory burden pattern is function-specific rather than uniform. The disagreement matters because core status is cheap to compute and is routinely used to prioritize genes for experiment, while essentiality measured by transposon sequencing (TnSeq, which infers importance from the depletion of insertion mutants) is expensive. If conservation tracks study effort more than phenotype, prioritizing by core status would recycle what is already known. This tension is recorded on [[concepts/gene-essentiality]].

## Evidence Sides

**Conservation and annotation as predictors of essentiality.** Analyses of *Acinetobacter baylyi* ADP1 associate essentiality with core pangenome status and with richer functional annotation, supporting the use of conservation and annotation coverage as predictors when direct perturbation data are absent [src: acinetobacter_adp1_explorer].

**Core genome contains a large annotation-dark fraction.** A census of core gene clusters found 415,603 core clusters with multiple-sequence-alignment (MSA) depth below 10 — that is, fewer than ten alignable homologs available for structure or function transfer — of which 68.9% were hypothetical (carrying no functional annotation) [src: alphafold_msa_annotation]. Core membership therefore does not entail annotation richness for this subset.

**Core enrichment persists where there is no phenotype, and reverses by function.** Core status is not confined to important genes: always-neutral genes — those with no detectable fitness effect in any experiment — are 66% core [src: conservation_fitness_synthesis, fitness_effects_conservation]. Directionally against the burden expectation, 24.4% of core genes show positive fitness when deleted versus 19.9% of accessory genes [src: conservation_fitness_synthesis, fitness_effects_conservation]. The burden pattern is function-specific, with reversals in some functional categories rather than a uniform core effect [src: core_gene_tradeoffs].

## Possible Reconciliations

- **Hypothesis: the association is real but low-specificity.** Core status may raise the prior on importance without being able to separate important from neutral genes, since always-neutral genes are still 66% core [src: conservation_fitness_synthesis, fitness_effects_conservation].
- **Hypothesis: annotation richness and conservation are separable axes.** MSA depth, not core membership, may drive annotation quality, so a core-and-shallow subset can be simultaneously conserved and dark [src: alphafold_msa_annotation].
- **Hypothesis: conservation selects for pathway participation, not indispensability.** If core genes sit in more pathways with condition-dependent costs and benefits [src: core_gene_tradeoffs], they would show both more importance and more burden, which would explain the higher positive-fitness rate among core genes [src: conservation_fitness_synthesis, fitness_effects_conservation] without contradicting the essentiality association.

## Resolving Work

- Join the ADP1 TnSeq essentiality calls to per-cluster MSA depth and hypothetical status, and ask whether the essentiality–core association survives stratification by MSA depth.
- Recompute core enrichment separately within the 415,603 shallow-MSA core clusters versus deep-MSA core clusters, asking which stratum carries the essentiality signal.
- Within each functional category, test whether the 24.4%-versus-19.9% burden direction holds or reverses, to quantify how much of the core effect is function-specific.
- Fit a model predicting measured fitness from core status, MSA depth and annotation status jointly, asking whether core status retains predictive value once study depth is controlled.
- Assay a sample of always-neutral core genes under conditions absent from current experiment sets, asking whether their neutrality is biological or a coverage artifact.
