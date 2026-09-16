<!-- tension-hash: 14f53e8b313cdc13 -->
# Is Gene Essentiality Tied to Core Status and Rich Annotation, or Do Conserved Genes Break That Link?

This tension sits on [[concepts/gene-essentiality]]. One reading treats pangenome core status (as opposed to accessory status) and rich functional annotation as markers of essential genes. Other projects find large classes of core genes that are poorly annotated, fitness-neutral, or even costly to keep. This matters because conservation and annotation are used as predictors of essentiality. If the link is weak or depends on function, those predictors could misrank candidate genes.

## Evidence Sides

**Side A: essentiality goes with core status and richer annotation.** Analyses of *Acinetobacter baylyi* ADP1 associate gene essentiality with core status and with richer functional annotation [src: acinetobacter_adp1_explorer]. These analyses combine transposon sequencing (TnSeq, which infers gene importance from mutant abundance) with pangenome classification and annotation. This is a single-organism result. It is not a cross-species measurement.

**Side B: core status does not imply rich annotation or essentiality.**
- 415,603 core gene clusters had a multiple-sequence-alignment (MSA) depth below 10, meaning fewer than 10 homologous sequences were available to align. Of these clusters, 68.9% were hypothetical, with no functional annotation [src: alphafold_msa_annotation].
- Genes that were always neutral had no detectable fitness effect in any experiment. Even so, 66% of them were core [src: conservation_fitness_synthesis, fitness_effects_conservation].
- Some deletions produced positive fitness, meaning the mutant grew better without the gene. This happened for 24.4% of core genes versus 19.9% of accessory genes [src: conservation_fitness_synthesis, fitness_effects_conservation].
- The burden pattern reverses in some functional categories. In those categories, non-core genes are the more burdensome group [src: core_gene_tradeoffs].

Side B does not deny that core genes are enriched for essentiality. It shows that this enrichment coexists with large neutral and burdensome core fractions [src: conservation_fitness_synthesis, core_gene_tradeoffs] and with a large unannotated core fraction [src: alphafold_msa_annotation].

## Possible Reconciliations

- **Hypothesis 1: annotation depends on alignment depth, not core status.** Rich annotation may track MSA depth. The low-depth core subset could then be a distinct "dark" class that sits beside a well-annotated core majority.
- **Hypothesis 2: an enrichment is not a rule.** Side A may describe a modest shift in proportions. Side B may describe the large remainder that this shift leaves behind. Under this reading, both sides could hold at once.
- **Hypothesis 3: function and condition decide the direction.** Function-specific reversals suggest that the core–essentiality relationship varies by functional category and growth condition. A single pooled association may hide this.
- **Hypothesis 4: ADP1 may not generalize.** The ADP1 association may hold for that organism or its data coverage and not transfer to other species.

## Resolving Work

- **Essentiality in the low-depth core subset.** Intersect the 415,603 core clusters with MSA depth <10 [src: alphafold_msa_annotation] with essentiality calls from fitness data. The question is whether these unannotated core genes are essential at rates similar to annotated core genes.
- **Stratified test in ADP1.** Repeat the ADP1 essentiality–core–annotation association stratified by MSA depth bin [src: acinetobacter_adp1_explorer]. The question is whether annotation still predicts essentiality once alignment depth is controlled.
- **Per-organism, per-category models.** Fit essentiality-versus-conservation models separately for each organism and each functional category, using the fitness data behind [src: fitness_effects_conservation, core_gene_tradeoffs]. The question is whether the pooled core enrichment survives in categories that show reversals.
- **Condition-resolved burden.** Use condition-resolved fitness profiles to test whether core genes with positive fitness are trade-off genes that become essential under other conditions [src: conservation_fitness_synthesis]. The question is whether conditional essentiality explains the extra burden seen in core genes.
