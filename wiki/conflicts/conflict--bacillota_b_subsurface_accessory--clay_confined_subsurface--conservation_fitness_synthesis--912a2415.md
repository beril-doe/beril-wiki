<!-- tension-hash: be368ded23b287d1 -->
# Genome expansion versus pathway completeness: do cultured subsurface genomes measure biosynthetic self-sufficiency?

Projects in this corpus disagree about whether the cultured deep-subsurface genomes available on the KBase Data Lakehouse can be used to judge biosynthetic self-sufficiency — the capacity of an organism to make its own metabolic building blocks rather than acquiring them from partners. The disagreement recorded on [[concepts/biosynthetic-self-sufficiency-and-cultivation]] has five distinct strands: (1) whether a negative result in the cultured cohort speaks to the community it was drawn from; (2) whether genome and gene-family expansion in deep-clay lineages counts as evidence of self-sufficiency when the direct pathway-completeness metric goes the other way; (3) whether gene conservation or laboratory cost can stand in for natural selective value; (4) whether condition-dependent reclassification of "latent" pathways is biology or a threshold artifact; and (5) whether the signal for retained-but-unused capability lives in pathway conservation or in clade-level genome dynamics. None of these is a case of two projects reporting different values for the same quantity; each is a case of two projects measuring different things and drawing opposed conclusions about the same biological question. That makes averaging or picking a winner the wrong move, and makes the scope of each measurement the thing to settle.

## Evidence Sides

### Disagreement 1 — A negative result in the cultured cohort versus an open hypothesis about the uncultured community

**Side 1a — The observed cultured genomes show no elevated self-sufficiency.** The deep cultured cohort does not support elevated self-sufficiency. [src: clay_confined_subsurface]

**Side 1b — Extreme self-sufficient lineages may sit outside the cultured collection.** The report's broader interpretation of deep subsurface biology leaves open the possibility that extreme self-sufficient lineages occur outside the cultured collection. [src: clay_confined_subsurface] The project itself characterizes this as a representation tension rather than a direct contradiction between measurements: the observed cultured genomes and the hypothesized full community refer to different biological subsets. [src: clay_confined_subsurface]

### Disagreement 2 — Genome expansion versus amino-acid pathway completeness

**Side 2a — Expansion supports a self-sufficiency model.** The Bacillota_B evidence **supports** a self-sufficiency model for cultivable subsurface genomes through larger genome size and OG content — OG meaning orthologous group, a cluster of genes inferred to share common ancestry and function. [src: bacillota_b_subsurface_accessory]

**Side 2b — Direct pathway completeness does not.** The GapMind comparison — GapMind being an annotation tool that scores how completely a genome encodes defined amino-acid biosynthesis pathways — finds no elevated amino-acid pathway completeness and, after quality filtering, finds lower completeness in the deep cohort. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] The two sides should not be reconciled by treating genome expansion as proof of biosynthetic self-sufficiency: they measure different aspects of genomic and metabolic capacity. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

### Disagreement 3 — Laboratory cost and conservation versus natural selective value

**Side 3a — Laboratory burden is not absence of value.** Conserved genes can be costly under laboratory conditions, so laboratory burden does not by itself show that a cultured or uncultured lineage lacks natural selective value. [src: conservation_fitness_synthesis]

**Side 3b — Neither proxy reaches the question.** This **refines** rather than overturns the representation argument, because neither conservation nor laboratory fitness directly establishes biosynthetic self-sufficiency in the deep subsurface. [src: conservation_fitness_synthesis]

### Disagreement 4 — Condition-dependence versus threshold construction

**Side 4a — Latent capabilities are real but condition-bounded.** All 66 aggregate Latent Capability pairs — genome-complete pathways without detectable fitness importance under the standard tested conditions — became important under at least one condition type. [src: pathway_capability_dependency]

**Side 4b — The reversal may be built into the method.** The report cautions that median-based condition-specific thresholds can cause reclassification by construction. [src: pathway_capability_dependency] Taken together, this **supports** treating cultured laboratory observations as condition-bounded evidence rather than as definitive evidence for or against environmental self-sufficiency. [src: pathway_capability_dependency]

### Disagreement 5 — Pathway conservation versus clade-level pangenome dynamics

**Side 5a — Conservation of individual pathways carries no signal.** Pathway-level conservation did not distinguish latent capabilities from active dependencies. [src: metabolic_capability_dependency]

**Side 5b — Genome fluidity at clade level does.** Latent-capability rate correlated positively with pangenome openness — the tendency of a clade's gene repertoire to keep gaining new genes as more genomes are sampled — at the clade level (Spearman ρ = 0.69, p = 0.0004, n = 22 clades), where Spearman ρ is a rank correlation coefficient. [src: metabolic_capability_dependency] This **refines** the representation argument by placing the signal at the level of genome dynamics and clade context rather than simple conservation of individual complete pathways; it does not resolve whether cultured subsurface genomes are representative of extreme self-sufficient lineages. [src: metabolic_capability_dependency]

## Possible Reconciliations

These are hypotheses, not findings; each would let both sides of a strand be simultaneously correct.

- **Sampling-scope hypothesis (Disagreement 1).** Both sides may hold if the cultured cohort is an unbiased sample of the cultivable fraction and a biased sample of the whole community: the measurement then correctly describes what was measured while saying nothing about lineages that never entered culture. The project's own framing that the two claims "refer to different biological subsets" is consistent with this reading. [src: clay_confined_subsurface]

- **Different-axis hypothesis (Disagreement 2).** Genome and OG expansion may index anaerobic persistence, electron transfer, or niche-specific accessory functions rather than amino-acid biosynthesis, so a larger genome could coexist with equal or lower completeness across the specific amino-acid pathways GapMind scores. This would make both measurements accurate and non-substitutable, which is precisely the caution the concept page records. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

- **Metric-ceiling hypothesis (Disagreement 2).** If cultured genomes cluster near the top of the completeness scale, small filtered differences may reflect where the metric saturates rather than a biological deficit in biosynthetic capacity; the expansion signal would then be the more informative of the two, without the completeness result being wrong. Stated as a hypothesis only.

- **Environment-mismatch hypothesis (Disagreement 3).** Costly-in-the-laboratory and conserved-in-the-pangenome may both be true of the same genes if laboratory conditions are a poor proxy for subsurface selection; conservation would then track natural value while laboratory cost tracks assay conditions. Neither would license a claim about self-sufficiency. [src: conservation_fitness_synthesis]

- **Condition-coverage hypothesis (Disagreement 4).** If "latent" status is defined relative to a restricted condition panel, then complete condition coverage should convert latency into importance for essentially every pair — which is what the 66-pair result shows — and a median-relative threshold would produce the same appearance even without biology. The two explanations are separable by calibration, not by inspection. [src: pathway_capability_dependency]

- **Level-of-analysis hypothesis (Disagreement 5).** A null at the individual-pathway level and a positive correlation at the clade level are compatible if retention of fitness-neutral pathways is governed by genome-wide gene flux rather than by per-pathway conservation pressure; the clade-level result would then be the correct scale and the pathway-level null an under-powered or wrong-unit test. [src: metabolic_capability_dependency]

## Resolving Work

**Disagreement 1 — representation of the cultured cohort**
- Assemble deep-subsurface metagenome-assembled genomes (MAGs — genomes reconstructed from environmental sequence without isolation) from the same formations as the cultured isolates and score them with the identical GapMind pipeline: does the uncultured fraction contain completeness values above the cultured range? [src: clay_confined_subsurface]
- Compare cultured and uncultured cohorts under matched quality filtering, reporting cohort sizes before and after, to test whether the negative result survives when representation is equalized. [src: clay_confined_subsurface]
- Stratify the comparison by isolation source and phylum so that "cultured versus uncultured" is not confounded with cohort composition. [src: clay_confined_subsurface]

**Disagreement 2 — expansion versus completeness**
- Decompose the enriched orthologous groups of the deep-clay cohort into amino-acid biosynthesis versus other functional classes and test whether the expansion overlaps the pathways GapMind scores at all. [src: bacillota_b_subsurface_accessory]
- Recompute self-sufficiency from a finer-grained enzyme-level annotation of amino-acid biosynthesis and compare it against the pathway-count score on the same genomes, to separate a metric ceiling from a biological deficit. [src: clay_confined_subsurface]
- Regress completeness on genome size and OG count within the deep cohort: if expansion and completeness are uncorrelated, the two sides are measuring independent axes and neither should be read as the other. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

**Disagreement 3 — conservation and laboratory cost**
- Join subsurface pathway profiles to conservation and laboratory-fitness annotations and ask whether candidate self-sufficient lineages carry costly-and-conserved biosynthetic genes or the costly-and-dispensable pattern. [src: conservation_fitness_synthesis]
- Test whether conservation and laboratory cost predict each other for biosynthetic genes specifically, rather than genome-wide, to establish whether either proxy has traction on self-sufficiency. [src: conservation_fitness_synthesis]
- Identify conditions under which conserved-and-costly biosynthetic genes become fitness-beneficial, giving the proxy an interpretable environmental referent. [src: conservation_fitness_synthesis]

**Disagreement 4 — condition-dependence versus threshold artifact**
- Calibrate condition-specific pathway-importance thresholds against independently defined essential genes, then re-derive how many of the 66 pairs still reclassify. [src: pathway_capability_dependency]
- Run the same classification with permuted or randomized condition labels: if a comparable fraction reclassifies, the median-relative threshold is doing the work. [src: pathway_capability_dependency]
- Report the reclassification result as a function of threshold choice rather than at a single cut, so the conclusion's dependence on the cut is visible. [src: pathway_capability_dependency]

**Disagreement 5 — pathway conservation versus clade dynamics**
- Replace proxy-based pathway membership with direct per-step gene assignments and re-test whether the latent-capability association with pangenome openness persists (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [src: metabolic_capability_dependency]
- Re-run the pathway-level conservation test with power analysis and per-category stratification to determine whether its null is a true absence of signal or insufficient resolution. [src: metabolic_capability_dependency]
- Extend the clade-level analysis to subsurface clades with enough sampled genomes to estimate pangenome openness, testing whether the openness–latency relationship holds where the representation question is actually posed. [src: metabolic_capability_dependency]
