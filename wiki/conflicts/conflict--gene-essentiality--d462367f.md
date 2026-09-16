<!-- tension-hash: d462367f5db0cebf -->
# Essential-gene core fraction: 82% across 43 bacteria or 86.1% across 33 organisms?

Two projects integrate gene essentiality with pangenome conservation and report different shares of essential genes classified as core. One project reports 82% (82.2% under strongest-effect grouping) across approximately 194,000 genes from 43 bacteria [src: fitness_effects_conservation]. The other reports 86.1% among 148,826 genes from 33 organisms [src: conservation_vs_fitness]. The disagreement matters because the core fraction anchors claims in [[concepts/gene-essentiality]] that link conservation to essentiality. That page treats conservation as a predictor or hypothesis, not as a definition of essentiality. The tension is methodological: it involves datasets, organism filters, pangenome mappings and denominators, although whether each of these actually differs between the analyses remains to be established. The two estimates must not be averaged.

## Evidence Sides

**Side A: essential genes are 82% core**
- Essential genes are 82% core across approximately 194,000 genes from 43 bacteria [src: fitness_effects_conservation].
- Grouping genes by their strongest fitness effect gives 82.2% core for the essential class [src: fitness_effects_conservation].
- This estimate comes from the larger organism set and the larger gene denominator [src: fitness_effects_conservation].

**Side B: essential genes are 86.1% core**
- Essential genes are 86.1% core among 148,826 genes from 33 organisms [src: conservation_vs_fitness].
- This estimate comes from a smaller organism set and a smaller gene denominator, with its own organism filter and pangenome mapping [src: conservation_vs_fitness].

## Possible Reconciliations

- *Hypothesis 1: organism composition.* The 33-organism set may contain organisms whose essential genes are more often core. If so, the higher fraction would reflect which organisms were included, not a different relationship between essentiality and conservation.
- *Hypothesis 2: denominator definition.* The two counts (approximately 194,000 versus 148,826) may define the gene universe differently. For example, one may count all genes and the other only protein-coding genes, or they may handle unmapped genes differently. Either choice could shift the core share.
- *Hypothesis 3: pangenome mapping.* Different rules for linking genes to pangenome gene clusters could classify borderline clusters as core in one analysis and as non-core in the other.
- *Hypothesis 4: grouping scheme.* The 82% and 82.2% figures come from two category schemes within one project. Category boundaries may also differ between the two projects in ways that move genes into or out of the essential class.

Neither estimate is preferred here.

## Resolving Work

- **Organism intersection:** Restrict both projects' gene-level tables to the organisms they share and recompute the essential-gene core fraction with each pipeline. Question: does the gap persist on identical organisms?
- **Denominator audit:** Compare the gene-inclusion filters behind the approximately 194,000 and 148,826 gene counts, record which genes each analysis excludes, and recompute each fraction under the other's filter. Question: how much of the difference does the denominator alone explain?
- **Mapping concordance:** For genes present in both analyses, cross-tabulate the core/accessory call made by each pangenome mapping. Question: are discordant calls concentrated among essential genes?
- **Essential-class definition:** Apply one shared definition of "essential" to both gene sets and rerun the core-fraction calculation. Question: does a common definition bring the two fractions together?
- **Per-organism comparison:** Compute per-organism essential-gene core fractions in both projects and compare their distributions. Question: is the pooled difference driven by a few organisms or spread across many?
