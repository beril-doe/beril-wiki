---
type: Concept
description: How reuse of grouping features can inflate microbiome and genomic associations
sources:
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
- id: ecotype_env_reanalysis
  resource: ../summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: ecotype_functional_differentiation
  resource: ../summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
title: Selection-on-outcome leakage in microbiome and genomic inference
---
# Selection-on-outcome leakage in microbiome and genomic inference

Selection-on-outcome leakage occurs when observations are grouped or selected using the same biological features that are later tested for differences, so the analysis can amplify apparent associations and overstate their reproducibility. [^pitfalls] The documented microbiome example shows that clustering taxa and then testing those taxa within the resulting clusters can produce unstable candidate lists. [^pitfalls] This concept connects [pitfalls](../summaries/pitfalls.md) with [ecotype-environment-gene-content](ecotype-environment-gene-content.md), [confirmatory-exploratory-ecological-association-discordance](confirmatory-exploratory-ecological-association-discordance.md), and [sample-size-aware-phenotype-consensus](sample-size-aware-phenotype-consensus.md).

## Mechanism

In the cited workflow, samples were clustered on a taxon-abundance matrix, and the same taxa were subsequently tested within the clusters. [^pitfalls] Because the taxa influence both cluster membership and the test outcome, the apparent within-cluster differences are not independent evidence for the clusters or for the selected taxa. [^pitfalls] This is a form of outcome-dependent feature selection: the analysis uses a feature to define the comparison and then treats the feature's contrast as if it had been selected independently. [^pitfalls]

The problem is not limited to microbiome taxa; the same design risk applies whenever genomic or functional features are used to construct groups and are then reused as outcomes. [^pitfalls] The [ecotype_functional_differentiation__REPORT](../summaries/ecotype_functional_differentiation__REPORT.md) **supports** this genomic extension: PCA and KMeans clustering of within-species gene content was followed by testing COG (Clusters of Orthologous Groups) functional profiles, which summarize overlapping gene-content variation. Across 12 species, 170 of 257 COG tests (66.1%) were significant after BH-FDR correction, but this demonstrates functional differentiation rather than independent confirmation of it because the tested representation is biologically related to the grouping representation. [^ecotype_functional_differentiation] Independent validation, held-out features, or a genuinely different data representation is therefore needed before treating selected associations as confirmatory findings. [^pitfalls]

## Evidence from the IBD ecotype analysis

In `ibd_phage_targeting`, K=4 latent Dirichlet allocation (LDA) ecotypes produced a 33-species Tier-A list with CLR-Δ effect sizes from +0.5 to +3.0. [^pitfalls] Held-out-species sensitivity produced Jaccard values of 0.230 for E1 and 0.064 for E3. [^pitfalls] The reported analysis treated a Jaccard value above 0.5 as bounded leakage and below 0.3 as leakage dominating for that sensitivity procedure; these are project-specific decision thresholds rather than universal statistical guarantees. [^pitfalls]

Leave-one-species-out refitting changed *C. scindens* from a non-significant result to CD increases in both E1, with CI +0.68 to +0.87, and E3, with CI +1.13 to +1.71. [^pitfalls] This result **supports** the interpretation that reusing clustering-related taxa can alter both significance and estimated direction, rather than merely reducing statistical power. [^pitfalls]

Independent within-substudy evidence reduced the Tier-A list from 33 candidates to 3. [^pitfalls] This sharp reduction **supports** the use of independent validation when exploratory cluster-derived associations are being considered for confirmation. [^pitfalls]

## Safeguards and interpretation

Leakage should be assessed with held-out-feature clustering, leave-one-feature-out refitting, or clustering on a genuinely different functional matrix such as pathways or EC numbers. [^pitfalls] These designs separate the features used to define the ecological comparison from the features used to evaluate it, reducing direct reuse of the selected outcome. [^pitfalls]

The findings should be interpreted as evidence about analysis design, not as evidence that all ecotype-associated taxa are false discoveries. [^pitfalls] The document instead shows that the original 33-species list was sensitive to feature reuse and that independent within-substudy analysis provided a more restrictive set of 3 candidates. [^pitfalls] This **refines** [confirmatory-exploratory-ecological-association-discordance](confirmatory-exploratory-ecological-association-discordance.md) by identifying feature reuse as a concrete source of discordance between exploratory and confirmatory ecological associations. [^pitfalls]

Leakage safeguards also matter for [ecotype-environment-gene-content](ecotype-environment-gene-content.md), because ecotype-linked environmental or genomic interpretations can inherit instability when the grouping variables are tested again as explanatory features. [^pitfalls] The [ecotype_env_reanalysis__REPORT](../summaries/ecotype_env_reanalysis__REPORT.md) **refines** this caution: using genome-level environmental classifications and a consistent within-method comparison, environmental species had no stronger environment–gene-content correlations than human-associated species (one-sided Mann-Whitney U: U=1536, p=0.83), and the clinical sampling bias did not explain the weak signal. [^ecotype_env_reanalysis] This distinguishes selection or composition effects from outcome leakage rather than establishing that either is absent. [^ecotype_env_reanalysis] The reanalysis also used a different genome-extraction and downsampling strategy, so its absolute correlations are not comparable with the original analysis; only the within-method group comparison was treated as valid. [^ecotype_env_reanalysis]

The independent `ecotype_analysis` **supports** separating leakage from a genuinely weak environmental signal: across 172 bacterial species, the median partial correlation for environment was 0.0025 versus 0.0143 for phylogeny, with no significant environmental effect in 156 species (90.7%). [^ecotype_analysis] It therefore suggests that weak whole-genome environmental associations cannot, by themselves, demonstrate outcome leakage; the study instead hypothesized that environmental adaptation may affect specific gene subsets and that AlphaEarth embeddings may miss relevant variation. [^ecotype_analysis] AlphaEarth embeddings covered only 28.4% of genomes, making limited environmental coverage an alternative explanation that should be distinguished from feature reuse. [^ecotype_analysis]

They complement, rather than replace, design-consistent within-substudy contrasts, because the documented healthy and disease buckets contained disjoint sub-studies and pooled mixed-model contrasts were structurally unidentifiable in that setting. [^pitfalls]

## Tensions

The evidence does not establish a universal Jaccard cutoff for detecting leakage. [^pitfalls] The values 0.5 and 0.3 were explicitly project-specific decision thresholds for the cited sensitivity procedure, so applying them unchanged to another dataset or clustering method would be an unsupported extrapolation. [^pitfalls]

The observed instability also does not by itself identify whether clustering, differential-abundance modeling, subgroup sample size, or study structure contributed most to the changes. [^pitfalls] Resolving those components requires analyses that vary the feature partition and validation design while preserving the underlying samples and labels. [^pitfalls]

The ecotype functional-differentiation result **refines** this tension rather than resolving it: all 12 analyzed species had at least one differentiated COG category, but approximately 38% of gene clusters had COG annotations, and the report notes that effect significance may partly reflect large sample sizes. [^ecotype_functional_differentiation] Thus, widespread COG differences are compatible with real functional structure, annotation and sampling effects, or reuse of related gene-content information; they do not alone quantify leakage.

The ecotype reanalysis further shows that absolute partial-correlation values can differ substantially when genome inclusion and downsampling change: its median across 183 species was 0.081 versus 0.003 in the original analysis, described as a 27x difference. [^ecotype_env_reanalysis] This **supports** retaining the existing warning against interpreting instability or magnitude across incompatible methodologies as evidence of leakage alone, while the within-method environmental-versus-human-associated null comparison remains informative. [^ecotype_env_reanalysis]

The original ecotype analysis reports a weak environmental signal overall, whereas the reanalysis reports a median partial correlation of 0.081 under a different pipeline. [^ecotype_analysis][^ecotype_env_reanalysis] This **supports** treating cross-pipeline magnitude comparisons as a tension in measurement and sampling rather than as evidence that leakage caused either result. [^ecotype_analysis][^ecotype_env_reanalysis]

## Open Directions

- Re-run the IBD ecotype analysis with held-out-species clustering and compare Tier-A membership, CLR-Δ estimates, and confidence intervals with the original 33-species list; determine which associations persist without direct feature reuse. [^pitfalls]
- Apply leave-one-species-out refitting to every candidate rather than only *C. scindens*; quantify how often significance, effect direction, and ecotype-specific estimates change. [^pitfalls]
- Cluster the same samples using pathways or EC numbers instead of taxa, then test taxon-level associations; determine whether a feature representation that is independent of the tested taxa reduces the leakage signal. [^pitfalls]
- Combine the four IBD sub-studies with at least 10 CD and 10 nonIBD samples using within-substudy contrasts and inverse-variance meta-analysis; compare the resulting candidates with the ecotype-derived list. [^pitfalls]
- Recalculate stability across the reported Jaccard values of 0.230 for E1 and 0.064 for E3 under alternative feature-holdout partitions; determine whether the observed instability is specific to the cited partitioning procedure. [^pitfalls]
- Reconcile the 27x partial-correlation discrepancy by extracting downsampled and full-genome sets under the same pipeline, then test whether genome count and feature reuse jointly alter environmental-versus-human-associated comparisons. [^ecotype_env_reanalysis]
- Test whether COG functional categories and alternative environmental metadata reveal associations masked at whole-genome resolution without reusing features to define groups. [^ecotype_analysis]
- Reanalyze ecotype clusters with held-out COG categories and within-species phylogenetic controls; test whether the 170/257 significant COG contrasts persist independently of gene-content clustering and phylogenetic structure. [^ecotype_functional_differentiation]

[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
[^ecotype_functional_differentiation]: [ecotype functional differentiation](../summaries/ecotype_functional_differentiation__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../summaries/ecotype_env_reanalysis__REPORT.md)
[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
