<!-- tension-hash: 84eb95358a064d69 -->
# “Conserved” Measured as Core Membership Versus “Conserved” Measured as Taxonomic Breadth

Two conservation metrics circulating in this corpus do not resolve the same thing, and the corpus records the mismatch as a metric-resolution tension rather than a contradiction. One line of evidence scores a gene by whether it belongs to the core genome of a species clade — the set of gene clusters present in essentially all strains of that species — and finds that essential genes are only modestly enriched there (median odds ratio 1.56, where an odds ratio is the multiplicative change in odds of core membership) [src: conservation_vs_fitness, functional_dark_matter]. Another scores a gene by how broadly its orthologs span the taxonomy, producing graded categories rather than a binary. A third result adds a qualification: core status may mark conditional costs and benefits rather than uniformly greater importance [src: fitness_effects_conservation]. Which metric is used determines which unknown genes look like priorities.

## Evidence Sides

**Core membership within a species clade is a weak discriminator.** In the Fitness Browser comparison — the Fitness Browser being the collection of genome-wide transposon-mutant fitness measurements — essential genes showed only modest core enrichment, with a median odds ratio of 1.56 [src: conservation_vs_fitness, functional_dark_matter]. On this measurement, core status separates essential from non-essential genes, but weakly.

**Taxonomic ortholog breadth resolves a graded scale.** The expanded GTDB analysis — GTDB being the Genome Taxonomy Database, a standardized genome-based bacterial taxonomy — produced conservation categories spanning kingdom to species and mobile levels [src: conservation_vs_fitness, functional_dark_matter]. This is a multi-level scale, not a within-species binary, and the corpus reads the difference as **refining** rather than overturning: core membership within a species clade and broad taxonomic ortholog breadth are related but not interchangeable measurements [src: conservation_vs_fitness, functional_dark_matter].

**Core status may mark conditionality, not uniform importance.** The broader fitness-effects result adds a related qualification: core genes showed heavier fitness-effect tails in both directions, so core status may identify genes with stronger conditional costs and benefits rather than genes with uniformly greater importance [src: fitness_effects_conservation].

## Possible Reconciliations

- *Hypothesis:* the two metrics measure different timescales — within-species retention versus deep ancestral retention — so a modest within-species odds ratio and a kingdom-to-species-to-mobile gradient can both be correct simultaneously [src: conservation_vs_fitness, functional_dark_matter].
- *Hypothesis:* core membership saturates within well-sampled species clades, compressing the enrichment signal, while taxonomic breadth retains dynamic range across levels [src: conservation_vs_fitness, functional_dark_matter].
- *Hypothesis:* the bidirectional tail effect means core status is a conditionality marker, so any single-axis conservation score will under-predict importance for genes whose costs and benefits are context-dependent [src: fitness_effects_conservation].

## Resolving Work

- Score the same gene set on both axes (species-clade core membership and GTDB level assignment) and cross-tabulate: how far do the two rankings actually diverge, and for which functional categories?
- Regress essentiality against each metric separately and jointly: does taxonomic breadth add discriminative power beyond core membership?
- Stratify the fitness-effect tails by GTDB conservation level: are the heavier bidirectional tails concentrated at one level, or present at all of them?
- Test whether species-clade sampling depth predicts the odds ratio across organisms: is the modest enrichment a biological ceiling or a sampling artifact?

Source: [[concepts/comparative-conservation-metric-calibration]]
