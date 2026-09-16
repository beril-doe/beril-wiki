<!-- tension-hash: 8df7057b9e74ab7c -->
# Phylogeny-dominated gene content versus strong classifier-derived environmental associations

The corpus holds two results that point in different directions on how strongly environment structures microbial data. One finds phylogeny, meaning relatedness by evolutionary descent, generally outweighing environment. The other finds strong environmental associations in classifier-derived data. A classifier is software that assigns sequencing reads to taxa against a reference database. The disagreement matters for [[concepts/classifier-database-compatibility-in-taxonomic-quantification]]. That page argues that taxonomic quantities produced by classifiers are not freely comparable across studies or analyses. These two results show the same caution applying to environmental inference: an environmental effect detected in one data structure does not automatically carry over to another [src: ecotype_analysis, euk_in_prok_correlates].

## Evidence Sides

**Phylogeny generally dominates environment**

The ecotype analysis tested what predicts genome-wide gene-content similarity, meaning how alike genomes are in the genes they carry. It found that phylogeny generally dominated environmental similarity as a predictor [src: ecotype_analysis, euk_in_prok_correlates]. On this side, environment is the weaker predictor of the response studied, not an absent one.

**Strong classifier-derived environmental associations**

The present analysis detected strong within-matrix classifier-derived environmental associations [src: ecotype_analysis, euk_in_prok_correlates]. These associations are bounded by being within-matrix; they are not shown to hold beyond that data structure.

The TENSION text states that these results cannot be directly reconciled because they use different responses, data structures, and environmental representations [src: ecotype_analysis, euk_in_prok_correlates]. Neither side refutes the other, and this page does not prefer either one.

## Possible Reconciliations

- **Hypothesis: different responses.** Gene content within genomes may be more constrained by descent than the composition of classifier-detected signal within samples. If so, both findings could hold at once.
- **Hypothesis: different environmental representations.** How environment is encoded may set how much environmental signal is recoverable. One representation could be coarser or more host-confounded than the other.
- **Hypothesis: classifier artifact.** Some of the within-matrix association strength may reflect classifier reference-database scope rather than biology, the database-compatibility concern behind this tension [src: ecotype_analysis, euk_in_prok_correlates].

## Resolving Work

- Encode environment the same way in both analyses, then rerun each one. This tests whether environmental representation alone shifts the relative strength of environment versus phylogeny.
- Re-profile the samples behind the classifier-derived associations using classifiers with different database scopes. This asks whether the strong environmental associations persist across classifiers or depend on one reference database.
- Add a phylogenetic covariate, such as relatedness of the detected taxa, to the within-matrix association models. This asks whether environmental associations remain strong once descent is controlled for.
- Run the ecotype-style environment-versus-phylogeny comparison on a sample-level composition response, rather than genome gene content. This isolates whether the type of response drives the divergence.
