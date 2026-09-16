<!-- tension-hash: ec20299a21e53e9a -->
# Universal Phylum-Wide COG Partitioning or Sample-Limited Extrapolation?

The [[concepts/two-speed-bacterial-genome]] page reports a disagreement over how far its COG (Clusters of Orthologous Groups, a scheme that assigns genes to broad functional categories) pattern extends. The cog_analysis report and the discoveries digest describe this COG pattern as holding universally across bacterial phyla, which suggests deep evolutionary constraint, yet the same report cautions that its 32-species sample might be too small to reveal phylum-specific patterns [src: cog_analysis, discoveries]. This matters because a universal partition would support reading the two-speed structure as a fundamental constraint on bacterial genomes. If phylum-specific departures exist and the sample cannot detect them, the universality claim is an extrapolation and should not be treated as an established finding.

## Evidence Sides

**Side A: the pattern is universal across phyla**

The cog_analysis report and the discoveries digest present the COG partitioning pattern as holding universally across bacterial phyla. They interpret this consistency as suggesting deep evolutionary constraint on how functions are divided between core and accessory genes [src: cog_analysis, discoveries].

**Side B: the sample cannot establish universality**

The same report states that its 32-species sample might be too small to reveal phylum-specific patterns [src: cog_analysis, discoveries]. On this reading, a pattern that looks consistent within the sample does not show that no phylum departs from it. The universality claim is therefore an extrapolation from the sample, not a demonstrated result [src: cog_analysis, discoveries]. This side does not report any phylum that departs from the pattern. Its point is that the available sample cannot rule such departures out.

## Possible Reconciliations

- **Hypothesis 1:** The core-versus-accessory partition is broadly conserved in direction, while its magnitude varies by phylum in ways a small sample cannot resolve. Under this hypothesis, both the universality statement (about direction) and the caveat (about phylum-level detail) could hold.
- **Hypothesis 2:** The sampled species over-represent some lineages, so the apparent universality reflects sampling composition. Under this hypothesis, the "deep constraint" interpretation would need to be withdrawn or narrowed.
- **Hypothesis 3:** Universality holds for the strongest categories but not for weaker ones. Under this hypothesis, any universal claim would have to be stated category by category.

## Resolving Work

- **Expanded sample:** Rerun the COG enrichment analysis (comparing how often each COG category occurs among core genes versus novel or accessory genes) on a sample of pangenomes (each pangenome being the full gene set across all genomes of one species, core plus accessory) expanded to many species per phylum, drawn from GTDB (Genome Taxonomy Database) species clusters. Question: does each category's core-versus-accessory direction hold within every phylum taken separately?
- **Phylogenetic control:** Apply a phylogenetically controlled model, such as PGLS (phylogenetic generalized least squares, a regression that accounts for shared ancestry), to per-species COG enrichment values. Question: does the consistency survive once relatedness among species is accounted for?
- **Phylum heterogeneity test:** Fit a random-effects model (a regression that estimates how much an effect varies among groups, here treating phylum as the grouping factor) to per-species enrichment values. Question: is between-phylum variance in any COG category distinguishable from zero?
- **Sample-size sensitivity:** Run a rarefaction analysis that subsamples species within the expanded set. Question: at what sample size do phylum-specific departures become detectable, and does the original 32-species sample fall below it [src: cog_analysis, discoveries]?
