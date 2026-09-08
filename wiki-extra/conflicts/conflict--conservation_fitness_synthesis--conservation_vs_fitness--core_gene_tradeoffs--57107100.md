---
title: Conservation Metrics Disagree on Breadth, Rank Stability, and Biological Meaning
type: Conflict
sources:
- id: functional_dark_matter
  resource: ../../wiki/summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: conservation_vs_fitness
  resource: ../../wiki/summaries/conservation_vs_fitness__REPORT.md
  title: conservation vs fitness
- id: fitness_effects_conservation
  resource: ../../wiki/summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: conservation_fitness_synthesis
  resource: ../../wiki/summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
- id: core_gene_tradeoffs
  resource: ../../wiki/summaries/core_gene_tradeoffs__REPORT.md
  title: core gene tradeoffs
---
<!-- tension-hash: def056acb9caa63f -->
# Conservation Metrics Disagree on Breadth, Rank Stability, and Biological Meaning

The disagreement documented on [comparative-conservation-metric-calibration](../../wiki/concepts/comparative-conservation-metric-calibration.md) concerns what a conservation score actually measures. One analysis suggested nearly universal conservation, whereas a broader taxonomic analysis resolved substantial variation across taxonomic and mobile categories; even when rankings were globally similar, the selected top genes differed substantially. Comparisons with fitness and gene-module data further suggest that “conserved,” “core,” and “important” are related but non-interchangeable concepts.

## Evidence Sides

**Side 1 — Broad conservation depends on database and taxonomic resolution**

The initial eggNOG metric suggested near-universal breadth for 99.9% of clusters, whereas the GTDB r214 analysis resolved root ortholog groups across kingdom, phylum, class, order, family, genus, species, and mobile categories. [^functional_dark_matter] This indicates that apparent conservation can depend strongly on reference-database composition, ortholog-group propagation, and the taxonomic level used for scoring. [^functional_dark_matter]

**Side 2 — Global rank agreement does not guarantee stable experimental choices**

The species-count variant was highly correlated with the original ranking at the global level, with Spearman ρ = 0.982, yet its top-50 and top-100 overlaps were only 62% and 58%, respectively. [^functional_dark_matter] Thus, rank correlation and decision stability answer different questions when conservation metrics guide experimental selection. [^functional_dark_matter]

**Side 3 — Core membership and fitness effects are not equivalent to broad conservation**

The Fitness Browser comparison found only modest core enrichment for essential genes, with a median odds ratio 1.56, while the expanded GTDB analysis produced conservation categories spanning kingdom to species and mobile levels. [^conservation_vs_fitness][^functional_dark_matter] Core genes also showed heavier fitness-effect tails in both directions, suggesting that core status may identify genes with stronger conditional costs and benefits rather than genes with uniformly greater importance. [^fitness_effects_conservation] Module-family breadth did not predict conservation (rho=-0.01, p=0.91), and condition-specific fitness did not establish niche-specific fitness. [^conservation_fitness_synthesis]

## Possible Reconciliations

- **Hypothesis — Measurement resolution:** eggNOG breadth, GTDB taxonomic ortholog breadth, core membership, and Fitness Browser essentiality may measure different biological properties rather than directly conflicting properties. [^functional_dark_matter][^conservation_vs_fitness]
- **Hypothesis — Ranking versus selection:** a high global Spearman ρ can coexist with low top-list overlap because small score changes or ties may reorder the genes most likely to be selected experimentally. [^functional_dark_matter]
- **Hypothesis — Laboratory scope:** conserved genes with strong laboratory fitness effects may reflect conditional costs and benefits, while laboratory conditions capture only a fraction of natural environments. [^core_gene_tradeoffs]
- **Hypothesis — Detection limits:** defining burden as fitness above 1 may capture trade-offs rather than true dispensability, and a 90% identity threshold for DIAMOND matching may miss rapidly evolving genes. [^core_gene_tradeoffs]

## Resolving Work

- Recompute conservation using matched eggNOG and GTDB r214 references, holding ortholog propagation and taxonomic scoring levels constant; test whether the 99.9% breadth estimate persists.
- Compare complete ranked lists with Spearman ρ, top-50 and top-100 overlaps, tie handling, and bootstrap confidence intervals; determine which metric best predicts reproducible experimental selections.
- Cross-tabulate kingdom-to-species/mobile conservation categories with core status, essentiality, and Fitness Browser effect sizes; test whether median odds ratio 1.56 and heavier fitness-effect tails vary by conservation level.
- Reanalyze module-family breadth and condition-specific fitness across additional environments; test whether rho=-0.01, p=0.91 remains null outside the measured conditions.
- Repeat homology and burden analyses with identity thresholds below and above 90% and with rapidly evolving genes explicitly assessed; determine whether missed matches change the conservation–fitness trade-off.

[^functional_dark_matter]: [functional dark matter](../../wiki/summaries/functional_dark_matter__REPORT.md)
[^conservation_vs_fitness]: [conservation vs fitness](../../wiki/summaries/conservation_vs_fitness__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../../wiki/summaries/fitness_effects_conservation__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../../wiki/summaries/conservation_fitness_synthesis__REPORT.md)
[^core_gene_tradeoffs]: [core gene tradeoffs](../../wiki/summaries/core_gene_tradeoffs__REPORT.md)
