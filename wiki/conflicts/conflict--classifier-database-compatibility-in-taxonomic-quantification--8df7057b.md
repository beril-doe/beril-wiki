<!-- tension-hash: 8df7057b9e74ab7c -->
# Phylogeny-dominant gene content versus classifier-derived environmental association

Two projects in this corpus report apparently opposite verdicts on how much environment explains microbial variation, but they measure different things. The ecotype analysis concludes that phylogeny — shared evolutionary ancestry — generally outweighs environmental similarity when predicting how similar two genomes' gene contents are. The classifier-compatibility analysis, working on taxonomic profiles produced by read classifiers (software that assigns sequencing reads to taxa against a reference database), instead detects strong environmental associations within a single classifier's output matrix. The disagreement matters because a reader skimming either result alone would draw a general conclusion about "environment versus phylogeny" that neither analysis actually licenses, and because the two results are flagged as not directly reconcilable rather than as a contradiction one side should win. This page records the disagreement as a standing, unresolved comparison. See [[concepts/classifier-database-compatibility-in-taxonomic-quantification]].

## Evidence Sides

**Phylogeny dominates gene-content similarity (ecotype side).** The ecotype analysis found that phylogeny generally dominated environmental similarity as a predictor of genome-wide gene-content similarity [src: ecotype_analysis, euk_in_prok_correlates]. The direction of this claim is comparative and general ("generally dominated"), not absolute: it does not assert that environment has no effect, only that it is the weaker of the two predictors on that response.

**Environmental association is strong within a classifier matrix (contamination-correlates side).** The present analysis detected strong within-matrix classifier-derived environmental associations [src: ecotype_analysis, euk_in_prok_correlates]. The scope qualifier "within-matrix" is load-bearing: the association is observed inside one classifier's output, not across classifiers with differing reference databases and taxonomic scopes.

The two results cannot be directly reconciled because they use different responses, different data structures, and different environmental representations [src: ecotype_analysis, euk_in_prok_correlates]. That is a statement about methodological incommensurability, not a claim that either result is wrong.

## Possible Reconciliations

- *Hypothesis (different response variables):* gene-content similarity and classifier-derived taxonomic composition may respond to environment on different scales, so both statements could hold simultaneously without either being an error.
- *Hypothesis (environmental representation):* the two analyses encode "environment" differently, so their environmental predictors may not be estimating the same quantity, and the apparent conflict may be an artifact of encoding rather than biology.
- *Hypothesis (data-structure confounding):* within-matrix environmental association may partly reflect classifier reference-database scope covarying with sample environment, which would inflate the environmental signal relative to a genome-level comparison.

## Resolving Work

- Re-run the ecotype-style phylogeny-versus-environment partitioning on classifier-derived taxonomic profiles, using the same environmental representation as the classifier analysis: does the dominance ordering flip when only the response changes?
- Re-run the classifier association test on gene-content distance matrices from the same samples: is the environmental association still strong when the data structure is held to genome-level features?
- Harmonize environmental metadata into one shared encoding across both projects and refit both models: how much of the apparent disagreement survives a common environmental representation?
- Stratify the within-matrix associations by classifier reference-database scope: does environmental signal attenuate when database-scope covariance is controlled?
- Specify, before refitting, which single response and threshold would count as adjudicating the comparison, so neither result is averaged into the other.
