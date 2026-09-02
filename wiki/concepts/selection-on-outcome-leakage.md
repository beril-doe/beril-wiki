---
type: "Concept"
description: "How reusing selected features can inflate ecological and genomic associations"
sources: ["summaries/pitfalls.md", "summaries/ecotype_env_reanalysis__REPORT.md"]
---
# Selection-on-outcome leakage in microbiome and genomic inference

Selection-on-outcome leakage occurs when observations are grouped or selected using the same biological features that are later tested for differences, so the analysis can amplify apparent associations and overstate their reproducibility. [src: pitfalls] The documented microbiome example shows that clustering taxa and then testing those taxa within the resulting clusters can produce unstable candidate lists. [src: pitfalls] This concept connects [[summaries/pitfalls]] with [[concepts/ecotype-environment-gene-content]], [[concepts/confirmatory-exploratory-ecological-association-discordance]], and [[concepts/sample-size-aware-phenotype-consensus]].

## Mechanism

In the cited workflow, samples were clustered on a taxon-abundance matrix, and the same taxa were subsequently tested within the clusters. [src: pitfalls] Because the taxa influence both cluster membership and the test outcome, the apparent within-cluster differences are not independent evidence for the clusters or for the selected taxa. [src: pitfalls] This is a form of outcome-dependent feature selection: the analysis uses a feature to define the comparison and then treats the feature's contrast as if it had been selected independently. [src: pitfalls]

The problem is not limited to microbiome taxa; the same design risk applies whenever genomic or functional features are used to construct groups and are then reused as outcomes. [src: pitfalls] Independent validation, held-out features, or a genuinely different data representation is therefore needed before treating selected associations as confirmatory findings. [src: pitfalls]

## Evidence from the IBD ecotype analysis

In `ibd_phage_targeting`, K=4 latent Dirichlet allocation (LDA) ecotypes produced a 33-species Tier-A list with CLR-Δ effect sizes from +0.5 to +3.0. [src: pitfalls] Held-out-species sensitivity produced Jaccard values of 0.230 for E1 and 0.064 for E3. [src: pitfalls] The reported analysis treated a Jaccard value above 0.5 as bounded leakage and below 0.3 as leakage dominating for that sensitivity procedure; these are project-specific decision thresholds rather than universal statistical guarantees. [src: pitfalls]

Leave-one-species-out refitting changed *C. scindens* from a non-significant result to CD increases in both E1, with CI +0.68 to +0.87, and E3, with CI +1.13 to +1.71. [src: pitfalls] This result **supports** the interpretation that reusing clustering-related taxa can alter both significance and estimated direction, rather than merely reducing statistical power. [src: pitfalls]

Independent within-substudy evidence reduced the Tier-A list from 33 candidates to 3. [src: pitfalls] This sharp reduction **supports** the use of independent validation when exploratory cluster-derived associations are being considered for confirmation. [src: pitfalls]

## Safeguards and interpretation

Leakage should be assessed with held-out-feature clustering, leave-one-feature-out refitting, or clustering on a genuinely different functional matrix such as pathways or EC numbers. [src: pitfalls] These designs separate the features used to define the ecological comparison from the features used to evaluate it, reducing direct reuse of the selected outcome. [src: pitfalls]

The findings should be interpreted as evidence about analysis design, not as evidence that all ecotype-associated taxa are false discoveries. [src: pitfalls] The document instead shows that the original 33-species list was sensitive to feature reuse and that independent within-substudy analysis provided a more restrictive set of 3 candidates. [src: pitfalls] This **refines** [[concepts/confirmatory-exploratory-ecological-association-discordance]] by identifying feature reuse as a concrete source of discordance between exploratory and confirmatory ecological associations. [src: pitfalls]

Leakage safeguards also matter for [[concepts/ecotype-environment-gene-content]], because ecotype-linked environmental or genomic interpretations can inherit instability when the grouping variables are tested again as explanatory features. [src: pitfalls] The [[summaries/ecotype_env_reanalysis__REPORT]] **refines** this caution: using genome-level environmental classifications and a consistent within-method comparison, environmental species had no stronger environment–gene-content correlations than human-associated species (one-sided Mann-Whitney U: U=1536, p=0.83), and the clinical sampling bias did not explain the weak signal. [src: ecotype_env_reanalysis] This distinguishes selection or composition effects from outcome leakage rather than establishing that either is absent. [src: ecotype_env_reanalysis] The reanalysis also used a different genome-extraction and downsampling strategy, so its absolute correlations are not comparable with the original analysis; only the within-method group comparison was treated as valid. [src: ecotype_env_reanalysis]

They complement, rather than replace, design-consistent within-substudy contrasts, because the documented healthy and disease buckets contained disjoint sub-studies and pooled mixed-model contrasts were structurally unidentifiable in that setting. [src: pitfalls]

## Tensions

The evidence does not establish a universal Jaccard cutoff for detecting leakage. [src: pitfalls] The values 0.5 and 0.3 were explicitly project-specific decision thresholds for the cited sensitivity procedure, so applying them unchanged to another dataset or clustering method would be an unsupported extrapolation. [src: pitfalls]

The observed instability also does not by itself identify whether clustering, differential-abundance modeling, subgroup sample size, or study structure contributed most to the changes. [src: pitfalls] Resolving those components requires analyses that vary the feature partition and validation design while preserving the underlying samples and labels. [src: pitfalls]

The ecotype reanalysis further shows that absolute partial-correlation values can differ substantially when genome inclusion and downsampling change: its median across 183 species was 0.081 versus 0.003 in the original analysis, described as a 27x difference. [src: ecotype_env_reanalysis] This **supports** retaining the existing warning against interpreting instability or magnitude across incompatible methodologies as evidence of leakage alone, while the within-method environmental-versus-human-associated null comparison remains informative. [src: ecotype_env_reanalysis]

## Open Directions

- Re-run the IBD ecotype analysis with held-out-species clustering and compare Tier-A membership, CLR-Δ estimates, and confidence intervals with the original 33-species list; determine which associations persist without direct feature reuse. [src: pitfalls]
- Apply leave-one-species-out refitting to every candidate rather than only *C. scindens*; quantify how often significance, effect direction, and ecotype-specific estimates change. [src: pitfalls]
- Cluster the same samples using pathways or EC numbers instead of taxa, then test taxon-level associations; determine whether a feature representation that is independent of the tested taxa reduces the leakage signal. [src: pitfalls]
- Combine the four IBD sub-studies with at least 10 CD and 10 nonIBD samples using within-substudy contrasts and inverse-variance meta-analysis; compare the resulting candidates with the ecotype-derived list. [src: pitfalls]
- Recalculate stability across the reported Jaccard values of 0.230 for E1 and 0.064 for E3 under alternative feature-holdout partitions; determine whether the observed instability is specific to the cited partitioning procedure. [src: pitfalls]
- Reconcile the 27x partial-correlation discrepancy by extracting downsampled and full-genome sets under the same pipeline, then test whether genome count and feature reuse jointly alter environmental-versus-human-associated comparisons. [src: ecotype_env_reanalysis]
