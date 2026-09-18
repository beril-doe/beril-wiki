<!-- tension-hash: fdbf2939c398016e -->
# Whole-pangenome openness shows no eco-phylogenetic signal while individual PGP genes show strong environmental enrichment

Two projects in this corpus measure how much a bacterial pangenome's gene content reflects its environment, and they reach opposite-seeming conclusions depending on the unit of analysis. One asks whether pangenome *openness* — a whole-genome summary of how readily a species acquires new genes — tracks environment or phylogeny, and finds nothing. The other asks whether *particular* plant-growth-promoting (PGP) genes are enriched in particular environments, and finds strong associations. This matters because the two results attach to different units of analysis: a null at the genome-summary level and an enrichment at the named-gene level cannot both be generalized until it is established which scale a given question belongs to. The tension feeds [[concepts/gene-cooccurrence-ecological-guilds]].

## Evidence Sides

**Openness carries no environment or phylogeny signal.** The pangenome-openness analysis reports a null result: no significant relationship between openness and either the environment effect (Spearman rho, a rank-correlation statistic, = -0.05, p-value = 0.54) or the phylogeny effect (Spearman rho = 0.03, p-value = 0.73). [src: pangenome_openness] Both correlations are near zero and neither p-value approaches conventional significance; this is a null, not a weak positive, and should not be restated as a small effect.

**Selected genes carry strong environmental enrichment.** The PGP analysis finds strong environment-associated enrichment for particular genes, including acdS and pqqC. [src: pgp_pangenome_ecology] The signal here is attached to named gene subsets, not to any whole-pangenome metric.

## Possible Reconciliations

*Hypothesis (scale mismatch).* A whole-pangenome openness metric may fail to predict broad eco-phylogenetic structure while selected gene subsets retain environmental associations — that is, a metric averaged over every gene in a pangenome may dilute a signal concentrated in a small, functionally coherent subset. [src: pangenome_openness, pgp_pangenome_ecology]

*Hypothesis (representation mismatch).* The two analyses may not measure the same quantity at all: openness describes the *rate* of gene gain, while gene enrichment describes *which* genes are present. A lineage could be closed yet still carry environment-specific genes in its core, leaving openness uninformative about environmental fit by construction.

*Hypothesis (denominator mismatch).* The species sets, environment labels and statistical thresholds used by the two projects may differ enough that neither result constrains the other. This is a scale and representation tension rather than a direct contradiction.

## Resolving Work

- Run both analyses on one shared species set with one shared environment labelling, so that the null and the enrichment result share a denominator and become directly comparable.
- Test whether the environment-enriched genes sit in each species' core fraction (genes present in nearly every strain) or its accessory fraction (genes present in only some strains): if they are largely core, openness — a measure of how readily new genes are acquired — cannot be expected to track them, and the tension dissolves by construction.
- Recompute openness using only genes whose presence varies across strains of a species, then re-run the same Spearman correlation against the environment effect: does a variable-gene openness metric recover a signal the whole-pangenome metric misses?
- Simulate pangenomes in which a fixed small gene subset is environment-structured and the remainder is not, then measure what effect size openness retains: this quantifies how much dilution is needed to produce rho = -0.05.
- Stratify the openness correlation by clade to test whether a signal exists within lineages but cancels across them.
