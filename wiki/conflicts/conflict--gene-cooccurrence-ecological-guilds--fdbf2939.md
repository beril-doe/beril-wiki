<!-- tension-hash: fdbf2939c398016e -->
# Whole-pangenome openness shows no eco-phylogenetic signal while individual PGP genes show strong environmental enrichment

Two projects in this corpus measure how much a bacterial pangenome's gene content reflects its environment, and they reach opposite-seeming conclusions depending on the unit of analysis. One asks whether pangenome *openness* — how readily a species' gene repertoire takes on new genes — tracks environment or phylogeny, and finds nothing. The other asks whether *particular* plant-growth-promoting (PGP) genes are enriched in particular environments, and finds strong associations. This matters because a whole-genome summary metric and a named gene subset are easily read as answering the same question about environmental adaptation, and here they do not answer it the same way; which unit of analysis a claim rests on has to be stated, not assumed. The tension feeds [[concepts/gene-cooccurrence-ecological-guilds]].

## Evidence Sides

**Openness carries no environment or phylogeny signal.** The pangenome-openness analysis reports a null result: no significant relationship between openness and either the environment effect (Spearman rho, a rank-correlation statistic, = -0.05, p-value = 0.54) or the phylogeny effect (Spearman rho = 0.03, p-value = 0.73). [src: pangenome_openness] Both correlations are near zero and neither p-value approaches conventional significance; this is a null, not a weak positive, and should not be restated as a small effect.

**Selected genes carry strong environmental enrichment.** The PGP analysis finds strong environment-associated enrichment for particular genes, including acdS and pqqC. [src: pgp_pangenome_ecology] The signal here is attached to named gene subsets, not to any whole-pangenome metric.

## Possible Reconciliations

*Hypothesis (scale mismatch).* A whole-pangenome openness metric may fail to predict broad eco-phylogenetic structure while selected gene subsets retain environmental associations. One mechanism that would produce this pattern — proposed here, not measured by either project — is that averaging over the whole gene repertoire, both core genes (present in nearly all strains of a species) and accessory genes (present in only some), dilutes a signal concentrated in a small, functionally coherent subset.

*Hypothesis (representation mismatch).* The two analyses may not measure the same quantity at all: openness describes the *rate* of gene gain, while gene enrichment describes *which* genes are present. A lineage could be closed yet still carry environment-specific genes in its core, leaving openness uninformative about environmental fit by construction.

*Hypothesis (denominator mismatch).* The species sets, environment labels and statistical thresholds used by the two projects may differ enough that neither result constrains the other. This is a scale and representation tension rather than a direct contradiction.

## Resolving Work

- Recompute openness restricted to the environment-enriched genes (acdS, pqqC) and the genes that co-occur with them, then re-run the same Spearman correlation against the environment effect: does a subset-restricted metric recover a signal the whole-pangenome metric misses?
- Run both analyses on one shared species set with one shared environment labelling, so that the null and the enrichment result share a denominator and become directly comparable.
- Test whether the environment-enriched genes sit in the core or the accessory fraction of each species; if they are largely core, an openness metric built on gene gain cannot be expected to track them, and the tension dissolves by construction.
- Simulate pangenomes in which a fixed small gene subset is environment-structured and the remainder is not, then measure what effect size openness retains: quantifies how much dilution is needed to produce rho = -0.05.
- Stratify the openness correlation by clade to test whether a signal exists within lineages but cancels across them.
