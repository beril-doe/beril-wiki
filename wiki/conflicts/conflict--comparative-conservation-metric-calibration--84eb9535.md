<!-- tension-hash: 84eb95358a064d69 -->
# Does "Conserved" Mean Clade-Core Membership or Broad Taxonomic Breadth?

The corpus uses "conserved" for at least two measurements, and they do not tell the same story about gene importance. One comparison used essentiality data from the Fitness Browser (a collection of genome-wide mutant fitness data). It tested these calls against core membership, meaning whether a gene belongs to the core of its species pangenome (the full set of genes found across a species' genomes). Essential genes showed only modest core enrichment, with a median odds ratio of 1.56. An odds ratio here compares the odds of being core for essential versus non-essential genes. An expanded analysis using GTDB (the Genome Taxonomy Database) instead sorted genes into conservation categories running from kingdom to species and mobile levels. This reflects ortholog breadth: how widely across taxonomy a gene's orthologs occur. Orthologs are equivalent genes in different organisms that descend from a common ancestor. [src: conservation_vs_fitness, functional_dark_matter] The source concept page, [[concepts/comparative-conservation-metric-calibration]], records this as a metric-resolution tension rather than a contradiction. It matters because ranking unknown genes by "conservation" depends on which measurement is used. A third result also questions whether core status means uniformly greater importance at all. [src: fitness_effects_conservation]

## Evidence Sides

**Side 1: Core membership within a species clade is a modest discriminator of essentiality**

In the Fitness Browser comparison, essential genes showed only modest core enrichment, with a median odds ratio of 1.56. [src: conservation_vs_fitness, functional_dark_matter]

**Side 2: Broad taxonomic ortholog breadth resolves conservation into graded levels**

The expanded GTDB analysis produced conservation categories that span kingdom, species and mobile levels. [src: conservation_vs_fitness, functional_dark_matter] The difference between the two sides **refines** the interpretation of "conserved". Core membership within a species clade and broad taxonomic ortholog breadth are related measurements, but they are not interchangeable. [src: conservation_vs_fitness, functional_dark_matter]

**Qualifying evidence: core genes have heavier fitness-effect tails in both directions**

Core genes showed heavier fitness-effect tails in both directions. Tails are the extreme ends of the fitness-effect distribution, covering strongly deleterious and strongly beneficial effects. Heavier tails mean more genes fall at those extremes. Core status may therefore identify genes with stronger conditional costs and benefits rather than genes with uniformly greater importance. [src: fitness_effects_conservation] The source phrases this as a possibility, not an established mechanism.

## Possible Reconciliations

- *Hypothesis:* The modest enrichment under clade-core membership may partly reflect the coarseness of a binary core/non-core measure. A graded breadth measure might separate essential from non-essential genes differently. The excerpted evidence does not test this.
- *Hypothesis:* If core genes carry stronger conditional costs and benefits, then "importance" is condition-dependent. Any single conservation metric would then track only part of that importance. [src: fitness_effects_conservation]

## Resolving Work

- **Graded breadth versus essentiality.** Join Fitness Browser essentiality calls to the GTDB kingdom-to-species/mobile conservation categories, and estimate enrichment per category with odds ratios. The question is whether graded breadth discriminates essential genes better than clade-core membership does.
- **Within-gene agreement between metrics.** For genes scored by both metrics, cross-tabulate clade-core status against GTDB breadth category. The question is how often the two metrics disagree about the same gene, and in which functional classes.
- **Fitness tails by breadth category.** Repeat the analysis of fitness-effect distribution tails, stratified by GTDB breadth category instead of core status. The question is whether heavier two-directional tails persist under the broader metric.
- **Ranking sensitivity for unknown genes.** Re-rank functionally unannotated genes under each conservation metric. Compare the resulting priority lists with rank correlation, a statistic that measures how similarly two lists order the same items. The question is how much prioritization depends on the metric chosen.
