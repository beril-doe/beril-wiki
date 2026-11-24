<!-- tension-hash: 54262c042718b124 -->
# Gut Ecotype Stability Versus Cross-Study Reproducibility: Is the Framework Replicated?

The ibd_phage_targeting project groups gut metagenomes into discrete ecotypes (community types). [src: ibd_phage_targeting] Sources disagree on whether this framework and its Tier-A list (the candidate disease-associated taxa that passed the project's rigor-controlled checks) are reproducible. An adversarial review flagged 48.9 % cross-method agreement and no external replication of the framework, while the project reports 88.2 % sign-concordance on HMP2 (the HMP_2019_ibdmdb cohort) for operational Tier-A. [src: discoveries] [src: ibd_phage_targeting] The tension matters because it determines how far the framework and its candidate lists can be trusted. It is drawn from [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

## Evidence Sides

**Side 1: The framework is unstable or unreplicated**
- The adversarial review flagged 48.9 % cross-method agreement and no external replication of the framework. [src: discoveries]
- Bootstrap ARI (adjusted Rand index, a measure of clustering agreement) of 0.13–0.17 suggested modest stability. Leave-one-study-out (LOSO) ARI, with a mean of 0.113 and a range of 0.000–0.282, showed that the bootstrap masked sub-study variation. [src: ibd_phage_targeting]
- Leakage checks, which refit ecotypes on held-out species splits, found low Jaccard overlap (E1 0.230, E3 0.064). Jaccard is the overlap between two sets divided by their union. E1 and E3 are two of the ecotypes. [src: pitfalls]
- Requiring an independent evidence stream shrank the within-ecotype Tier-A from 33 to 3. [src: pitfalls]
- The Kuehl species-detection figures (54 % detected; 70 % with no detection) disagree on their face. [src: discoveries]

**Side 2: The operational Tier-A is externally validated**
- The report calls the operational Tier-A validated by 88 % HMP2 replication. [src: ibd_phage_targeting]
- The project reports 88.2 % HMP2 sign-concordance for operational Tier-A. [src: ibd_phage_targeting]
- The report reconciles the two sides only by separating framework stability from claim replication. [src: ibd_phage_targeting]

## Possible Reconciliations

- **Hypothesis: stability and replication are different properties.** Disease claims could replicate across cohorts even when cluster boundaries shift, as the report's own separation implies. [src: ibd_phage_targeting] This is not established, because the low Jaccard values and the shrinkage from 33 to 3 bear on the Tier-A list itself. [src: pitfalls]
- **Hypothesis: the 88.2 % figure and the leakage results measure different candidate sets.** The figure may describe the operational Tier-A, while the leakage checks describe the within-ecotype list. This remains untested.
- **Hypothesis: the Kuehl discrepancy comes from different denominators or definitions of detection.** The source figures do not say.

## Resolving Work

- Data: HMP2 and other independent cohorts. Method: recompute sign concordance separately for the 3 surviving candidates and for the original 33. Question: does the 88.2 % figure depend on which list is tested?
- Data: the sub-study cluster assignments. Method: compare LOSO ARI against the bootstrap ARI, sub-study by sub-study. Question: which sub-studies drive the range of 0.000–0.282?
- Data: the cross-method cluster labels. Method: decompose the 48.9 % cross-method agreement by method pair. Question: do the disagreements involve the same samples that move between ecotypes under LOSO?
- Data: the raw Kuehl detection tables. Method: recount with a single stated denominator. Question: is the 54 % versus 70 % mismatch a definitional artifact?
- Data: a truly external cohort never used in ecotype definition. Method: pre-registered projection of ecotypes and replication of Tier-A. Question: does the framework itself replicate, not just the claims?
