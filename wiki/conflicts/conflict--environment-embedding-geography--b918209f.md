<!-- tension-hash: b918209fd8913444 -->
# Environmental association versus lineage and genome-size structure in microbial trait patterns

Two projects report statistically detectable links between genomic traits and environment. Each also reports evidence that the link may reflect lineage or genome size rather than ecological selection. For *Pseudomonas* carbon pathway profiles, the environmental association is significant (p=0.006, where p is the probability of a result this extreme if there were no association), but predictive power is modest. Principal component analysis (PCA, a projection onto the axes of greatest variance) primarily separated *Pseudomonas* s.s. from Pseudomonas_E [src: pseudomonas_carbon_ecology]. For polyhydroxybutyrate (PHB, a bacterial carbon-storage polymer), there is a raw association with niche breadth (rho=0.106, p=1.77×10^-06, where rho is a Spearman rank correlation). Once genome size is controlled, this becomes a negative partial correlation, meaning a correlation adjusted for a covariate (rho=-0.047, p=0.037) [src: phb_granule_ecology]. This matters for [[concepts/environment-embedding-geography]] because it decides how trait–environment associations in the corpus should be read: as ecological signal, or as something that must first be corrected for structure in the genomes.

## Evidence Sides

**Side A: trait profiles carry a detectable environmental signal**

*Pseudomonas* carbon profiles were environmentally associated (p=0.006) [src: pseudomonas_carbon_ecology]. PHB showed a raw association with niche breadth, rho=0.106, p=1.77×10^-06 [src: phb_granule_ecology]. Read alone, both results point toward environment-linked trait variation.

**Side B: the signal is weak, or it is carried by lineage or genome size**

In *Pseudomonas*, balanced accuracy was 0.408 +/- 0.169 [src: pseudomonas_carbon_ecology]. Balanced accuracy is classification accuracy averaged across classes so that unequal class sizes do not inflate it. Principal component analysis (PCA, a projection onto the axes of greatest variance) primarily separated *Pseudomonas* s.s. (sensu stricto, the core genus) from Pseudomonas_E, a separately labelled lineage [src: pseudomonas_carbon_ecology]. This suggests that the dominant structure is taxonomic.

For PHB, the genome-size-controlled partial rho was -0.047, p=0.037 [src: phb_granule_ecology]. Partial rho is a Spearman rank correlation computed after removing the effect of a covariate. Controlling for genome size therefore reverses the sign of the raw breadth association [src: phb_granule_ecology].

## Possible Reconciliations

- **Hypothesis 1: real but small signal.** Environmental association may be genuine but weak relative to lineage structure. A test can then be significant while classification stays modest. This would make the two sides compatible rather than contradictory, but it is untested here.
- **Hypothesis 2: confounding by structure.** Apparent environmental associations may arise mainly because lineages or larger genomes are unevenly distributed across environments. In that case, the Side A results would be largely indirect.
- **Hypothesis 3: endpoint dependence.** Association with environment *category* and association with niche *breadth* are different questions. One trait could follow environment type while its breadth relationship is driven by genome size. The two findings may therefore not test the same claim.

## Resolving Work

- **Lineage-stratified test.** Re-run the *Pseudomonas* environment-association test on carbon pathway profiles within *Pseudomonas* s.s. and within Pseudomonas_E separately. Question: does the environmental association persist inside each lineage?
- **Phylogenetic correction.** Use phylogenetic generalized least squares (PGLS, regression that accounts for shared ancestry) on PHB presence versus niche breadth, with genome size as a covariate. Question: does the partial correlation survive once phylogeny is also controlled?
- **Matched classification.** Train a classifier on *Pseudomonas* pathway profiles with lineage-blocked cross-validation, and compare it against a lineage-label-only baseline. Question: do pathways add predictive information beyond taxonomy?
- **Genome-size-stratified environment-type test.** Apply the same genome-size control used for PHB breadth to *Pseudomonas* environment association. Question: is genome size a shared confounder across both projects?
