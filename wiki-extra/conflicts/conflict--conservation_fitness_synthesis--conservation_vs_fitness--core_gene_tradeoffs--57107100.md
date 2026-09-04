<!-- tension-hash: 942dda8e6fd33d47 -->
# Conservation Metrics Disagree on Breadth, Rank Stability, and Biological Meaning

The disagreement documented on [[concepts/comparative-conservation-metric-calibration]] concerns what a conservation score actually measures. One analysis suggested nearly universal conservation, whereas a broader taxonomic analysis resolved substantial variation across taxonomic and mobile categories; even when rankings were globally similar, the selected top genes differed substantially. Comparisons with fitness and gene-module data further suggest that “conserved,” “core,” and “important” are related but non-interchangeable concepts.

## Evidence Sides

**Side 1 — Broad conservation depends on database and taxonomic resolution**

The initial eggNOG metric suggested near-universal breadth for 99.9% of clusters, whereas the GTDB r214 analysis resolved root ortholog groups across kingdom, phylum, class, order, family, genus, species, and mobile categories. [src: functional_dark_matter] This indicates that apparent conservation can depend strongly on reference-database composition, ortholog-group propagation, and the taxonomic level used for scoring. [src: functional_dark_matter]

**Side 2 — Global rank agreement does not guarantee stable experimental choices**

The species-count variant was highly correlated with the original ranking at the global level, with Spearman ρ = 0.982, yet its top-50 and top-100 overlaps were only 62% and 58%, respectively. [src: functional_dark_matter] Thus, rank correlation and decision stability answer different questions when conservation metrics guide experimental selection. [src: functional_dark_matter]

**Side 3 — Core membership and fitness effects are not equivalent to broad conservation**

The Fitness Browser comparison found only modest core enrichment for essential genes, with a median odds ratio 1.56, while the expanded GTDB analysis produced conservation categories spanning kingdom to species and mobile levels. [src: conservation_vs_fitness, functional_dark_matter] Core genes also showed heavier fitness-effect tails in both directions, suggesting that core status may identify genes with stronger conditional costs and benefits rather than genes with uniformly greater importance. [src: fitness_effects_conservation] Module-family breadth did not predict conservation (rho=-0.01, p=0.91), and condition-specific fitness did not establish niche-specific fitness. [src: conservation_fitness_synthesis]

## Possible Reconciliations

- **Hypothesis — Measurement resolution:** eggNOG breadth, GTDB taxonomic ortholog breadth, core membership, and Fitness Browser essentiality may measure different biological properties rather than directly conflicting properties. [src: functional_dark_matter, conservation_vs_fitness]
- **Hypothesis — Ranking versus selection:** a high global Spearman ρ can coexist with low top-list overlap because small score changes or ties may reorder the genes most likely to be selected experimentally. [src: functional_dark_matter]
- **Hypothesis — Laboratory scope:** conserved genes with strong laboratory fitness effects may reflect conditional costs and benefits, while laboratory conditions capture only a fraction of natural environments. [src: core_gene_tradeoffs]
- **Hypothesis — Detection limits:** defining burden as fitness above 1 may capture trade-offs rather than true dispensability, and a 90% identity threshold for DIAMOND matching may miss rapidly evolving genes. [src: core_gene_tradeoffs]

## Resolving Work

- Recompute conservation using matched eggNOG and GTDB r214 references, holding ortholog propagation and taxonomic scoring levels constant; test whether the 99.9% breadth estimate persists.
- Compare complete ranked lists with Spearman ρ, top-50 and top-100 overlaps, tie handling, and bootstrap confidence intervals; determine which metric best predicts reproducible experimental selections.
- Cross-tabulate kingdom-to-species/mobile conservation categories with core status, essentiality, and Fitness Browser effect sizes; test whether median odds ratio 1.56 and heavier fitness-effect tails vary by conservation level.
- Reanalyze module-family breadth and condition-specific fitness across additional environments; test whether rho=-0.01, p=0.91 remains null outside the measured conditions.
- Repeat homology and burden analyses with identity thresholds below and above 90% and with rapidly evolving genes explicitly assessed; determine whether missed matches change the conservation–fitness trade-off.
