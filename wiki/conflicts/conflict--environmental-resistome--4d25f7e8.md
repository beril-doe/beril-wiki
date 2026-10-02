<!-- tension-hash: 4d25f7e8ededc524 -->
# Does phylogenetic signal in AMR gene content reflect lineage-associated acquisition or uneven sampling?

Across the corpus, antimicrobial-resistance (AMR) gene profiles — the presence/absence patterns of resistance genes in a genome — track phylogenetic distance, the genome-to-genome divergence within a species, in 701 of 1,261 species examined. [src: amr_strain_variation, ecotype_analysis] The disagreement is not about whether that pattern exists but about what it measures: a biological process in which resistance genes are gained and retained along lineages, or a sampling artifact in which lineages are unevenly drawn from different environments so that phylogeny stands in for environment. The same ambiguity runs the other way for the weak environmental signal, which cannot be distinguished from inadequate environmental representation. This matters for [[concepts/environmental-resistome]], because every claim that ecology structures the resistome depends on environment and phylogeny being separable in the available data.

## Evidence Sides

**Side A — the positive relationship is lineage-associated acquisition.** The positive relationship between AMR and phylogenetic distance in 701/1,261 species is read as resistance gene content being inherited and accumulated along lineages, so that relatedness predicts shared resistance repertoire. [src: amr_strain_variation, ecotype_analysis]

**Side B — the positive relationship reflects uneven sampling of lineages across environments.** The same 701/1,261 result is equally consistent with lineages being sampled non-randomly from environments, so that phylogenetic distance carries an unmeasured environmental contrast. Available analyses do not separate these explanations. [src: amr_strain_variation, ecotype_analysis] On the environmental side the measurement is weak for known reasons: geographic coordinates were often missing or imprecise, and partial correlations — correlations between two distance matrices holding a third constant — assume linear relationships between those matrices, so weak environmental signal cannot distinguish absent adaptation from inadequate environmental representation. [src: amr_strain_variation, ecotype_analysis]

## Possible Reconciliations

- *Hypothesis:* both processes contribute, and the 701/1,261 count is a mixture of species where inheritance dominates and species where sampling structure dominates; nothing in the current analyses assigns species to either group.
- *Hypothesis:* the environmental signal is genuinely present but attenuated by missing or imprecise coordinates, so the apparent dominance of phylogeny is a measurement asymmetry rather than a biological ranking.
- *Hypothesis:* the relationship between the AMR and environmental distance matrices is non-linear, in which case the linearity assumption of partial correlation would suppress a real environmental effect without suppressing the phylogenetic one.

## Resolving Work

- Stratify the 701/1,261 species by how evenly their genomes are distributed across environment categories, and test whether phylogenetic signal weakens as sampling becomes balanced — does the signal survive in evenly sampled species?
- Re-run the phylogeny/environment comparison on the subset of genomes with complete, precise geographic coordinates, asking whether environmental signal strengthens when coordinate quality is controlled rather than assumed.
- Replace the linear partial-correlation step with a rank-based or non-parametric matrix comparison on the same distance matrices: does a non-linear environment–AMR relationship appear?
- Use curated isolation-source metadata as an environment proxy independent of coordinates, to ask whether weak environmental signal persists when the environment variable no longer depends on geography.
