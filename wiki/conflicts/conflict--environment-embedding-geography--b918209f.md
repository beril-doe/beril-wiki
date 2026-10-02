<!-- tension-hash: b918209fd8913444 -->
# Significant environment associations versus effects that vanish under control: when does trait content encode ecology?

Two projects in this corpus test whether a genomic trait profile tracks the environment a lineage comes from, and both return a statistically significant association — yet in each case the association fails a second test applied to it, and the two projects fail differently. One finds significance without predictive power; the other finds significance that reverses sign once a covariate is controlled. The disagreement is not over either number but over what a significant trait–environment association licenses: a real ecological signal that is merely hard to exploit, or an artifact of structure (taxonomy, genome size) that the significance test never removed. This matters for every claim on [[concepts/environment-embedding-geography]] that reads environmental meaning out of gene or pathway content.

## Evidence Sides

**Significant but weakly predictive — carbon pathway profiles in *Pseudomonas*.** *Pseudomonas* carbon profiles were environmentally associated at p=0.006, i.e. the environment grouping is unlikely under the permuted null. [src: pseudomonas_carbon_ecology] Against that, balanced accuracy — classification accuracy averaged over classes, so that unequal class sizes cannot inflate it — was 0.408 +/- 0.169, and PCA (principal component analysis, an unsupervised projection onto axes of maximal variance) primarily separated *Pseudomonas* s.s. (sensu stricto) from *Pseudomonas*_E, i.e. the dominant structure in the profiles was taxonomic rather than environmental. [src: pseudomonas_carbon_ecology] The association stands; the ecological reading of it does not follow automatically.

**Significant but confounded — PHB and niche breadth.** PHB showed a raw breadth association of rho=0.106 (Spearman rank correlation, a rank-based measure of monotonic association) at p=1.77×10^-06. [src: phb_granule_ecology] The genome-size-controlled partial rho — the same correlation with genome size held constant — was -0.047 at p=0.037: a sign reversal, with the controlled estimate near-null and pointing the opposite way. [src: phb_granule_ecology] Here the raw significance is directly attributable to a covariate, and the controlled estimate is inverted in direction rather than simply attenuated.

## Possible Reconciliations

- *Hypothesis:* both results are the same phenomenon at different stages of control — the *Pseudomonas* p=0.006 is a raw association whose taxonomic structure has not yet been partialled out, and would behave like the PHB raw-to-partial transition if it were. Untested in this corpus.
- *Hypothesis:* significance and predictive accuracy measure different things, so a genuinely weak-but-real environmental effect can produce p=0.006 while leaving balanced accuracy near 0.408 +/- 0.169; low accuracy would then be a power and class-resolution symptom, not evidence of confounding.
- *Hypothesis:* the two traits differ in kind — a multi-pathway profile and a single presence/absence trait need not share a confounding structure, so neither result generalizes to the other.

## Resolving Work

- Re-run the *Pseudomonas* environmental association as a phylogeny- or clade-partialled test (s.s. vs _E as a covariate): does p=0.006 survive removal of the axis PCA identified?
- Apply the partial-correlation protocol used for PHB to genome size in the *Pseudomonas* pathway profiles: is pathway count, like PHB, a genome-size proxy?
- Fit within-clade classifiers separately in *Pseudomonas* s.s. and *Pseudomonas*_E: does balanced accuracy rise when the taxonomic split is removed as a shortcut?
- Report effect sizes with confidence intervals alongside p-values for both traits: how much of the gap between the two projects is estimation precision rather than biology?
- Test whether the PHB partial rho=-0.047 sign reversal replicates in an independent environment-annotation set, to separate covariate control from annotation artifact.
