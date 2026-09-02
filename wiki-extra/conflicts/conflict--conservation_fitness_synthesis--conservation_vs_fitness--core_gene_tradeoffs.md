<!-- tension-hash: 942dda8e6fd33d47 -->
# Conservation breadth versus metric resolution

The disagreement concerns what conservation metrics actually measure: an initial eggNOG-based score suggested nearly universal breadth, whereas GTDB-based ortholog analysis resolved conservation across multiple taxonomic and mobile categories. The conflict matters because conservation rankings may appear robust in aggregate while changing substantially at the decision thresholds used to select experimental targets. It is documented on [[concepts/comparative-conservation-metric-calibration]].

## Evidence Sides

**Initial eggNOG metric and global ranking stability**

The initial eggNOG metric suggested near-universal breadth for 99.9% of clusters. [src: functional_dark_matter] The species-count variant was highly correlated with the original ranking at the global level, with Spearman ρ = 0.982, yet its top-50 and top-100 overlaps were only 62% and 58%, respectively. [src: functional_dark_matter] This supports reporting rank correlation and decision stability together when conservation metrics guide experimental selection. [src: functional_dark_matter]

**GTDB taxonomic resolution and narrower interpretation of conservation**

The GTDB r214 analysis resolved root ortholog groups across kingdom, phylum, class, order, family, genus, species, and mobile categories. [src: functional_dark_matter] Apparent conservation can therefore depend strongly on reference-database composition, ortholog-group propagation, and the taxonomic level used for scoring. [src: functional_dark_matter] Core membership within a species clade and broad taxonomic ortholog breadth are related but not interchangeable measurements. [src: conservation_vs_fitness, functional_dark_matter]

**Fitness and ecological qualifications**

Essential genes showed only modest core enrichment, with median odds ratio 1.56, while the expanded GTDB analysis produced conservation categories spanning kingdom to species and mobile levels. [src: conservation_vs_fitness, functional_dark_matter] Core genes showed heavier fitness-effect tails in both directions, so core status may identify genes with stronger conditional costs and benefits rather than genes with uniformly greater importance. [src: fitness_effects_conservation] Module-family breadth did not predict conservation (rho=-0.01, p=0.91), and condition-specific fitness did not establish niche-specific fitness. [src: conservation_fitness_synthesis] Laboratory fitness measurements and conservation patterns do not by themselves establish that costly conserved genes are maintained by natural selection. [src: core_gene_tradeoffs]

## Possible Reconciliations

- **Hypothesis — database and propagation effects:** eggNOG’s near-universal breadth and GTDB’s category structure may reflect different reference compositions and ortholog-group propagation rules rather than incompatible biological observations.
- **Hypothesis — rank versus selection stability:** ρ = 0.982 may describe global ordering, while 62% and 58% overlaps reveal instability among the highest-ranked candidates.
- **Hypothesis — scope and definition:** “conserved” may refer either to broad taxonomic ortholog breadth or to core membership within a species clade; these definitions need not produce the same enrichment or fitness associations.
- **Hypothesis — laboratory versus natural relevance:** condition-specific fitness, module-family breadth, and core status may capture laboratory or structural properties without directly measuring niche-specific fitness or natural ecological importance.

## Resolving Work

- Recompute both eggNOG and GTDB scores from the same gene set, with matched ortholog-propagation rules, to test whether database composition explains the breadth difference.
- Compare rank correlation and top-50/top-100 overlap across taxonomic scoring levels to determine where decision instability emerges.
- Stratify essentiality and Fitness Browser effects by conservation definition and taxonomic level, asking whether median odds ratio 1.56 changes when “conserved” is redefined.
- Test module-family breadth and condition-specific fitness against independently sampled ecological or field-associated fitness data to assess natural niche relevance.
- Reanalyze rapidly evolving genes using matching methods that do not rely solely on the 90% identity threshold for DIAMOND matching, and test whether the conclusions change.
