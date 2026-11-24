---
type: "Concept"
description: "How cases and controls from different substudies make diagnosis collinear with study, how clustering on features later tested within clusters causes selection-on-outcome leakage, and which within-study designs repair them."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
---
# Substudy nesting and feature leakage in pooled-cohort microbiome comparisons

This page covers substudy nesting and feature leakage in pooled-cohort microbiome comparisons. In cMD, diagnosis is collinear with study, because no sub-study contains both CD and HC samples. [src: pitfalls] Clustering samples on taxon abundance and then testing the same taxa within clusters mechanically inflates effects for cluster-defining taxa. [src: ibd_phage_targeting, pitfalls] The evidence comes from the ibd_phage_targeting project plus the central pitfalls digest. [src: ibd_phage_targeting, pitfalls] See [[entities/curatedmetagenomicdata]], [[entities/crohnsphage-data-mart]], [[summaries/pitfalls]] and [[summaries/ibd_phage_targeting__REPORT]].

## Substudy nesting makes diagnosis collinear with study

cMD bundles samples from ~50+ published studies into CMD_HEALTHY and CMD_IBD buckets. [src: pitfalls] Every CMD_HEALTHY sample comes from a healthy-cohort study, such as LifeLinesDeep_2016, AsnicarF_2021, YachidaS_2019 and HansenLBS_2018. [src: pitfalls] Every CMD_IBD CD sample comes from an IBD-cohort study, such as HallAB_2017, VilaAV_2018, LiJ_2014, IjazUZ_2017 and NielsenHB_2014. [src: pitfalls] No sub-study contains both CD and HC samples. [src: pitfalls]

In the ecotype-assigned slice of 8,489 samples, 45 sub-studies have ≥ 10 HC and 5 have ≥ 10 CD. Zero sub-studies contain both. [src: ibd_phage_targeting, pitfalls]

A pooled CD-vs-HC linear mixed-effects model with a substudy random effect is therefore structurally unidentifiable. The random effect perfectly predicts diagnosis. [src: ibd_phage_targeting, pitfalls] The project verified empirically that statsmodels.mixedlm silently failed to converge on every battery species. [src: ibd_phage_targeting] With lbfgs it returns without error but gives no usable fixed-effect estimate. [src: pitfalls] The pitfalls report cites Vujkovic-Cvijin 2020 on this kind of structural confounding. It says a standard random-effects model cannot adjust it in the cMD pooled-cohort contrast. [src: pitfalls]

If a pooled CD-vs-HC effect must be reported, the report says not to rely on substudy random effects. It says to quote the effect as-is, with a caveat that study, cohort, sequencing center and sample prep are all collinear with diagnosis. [src: pitfalls] The report says the problem also generalizes to any pooled public-dataset analysis (such as SRA study inventories or Qiita studies) where the case and control cohorts were collected by different groups. [src: pitfalls]

The report names this nesting problem as a generalizable methodology contribution. [src: ibd_phage_targeting]

### Recovering the substudy label

For cMD IBD samples, participant_id such as CMD:HallAB_2017:SKST006 encodes the substudy in the middle colon-separated token. [src: pitfalls] For HC samples, the substudy is stored under the key "study" in the dim_samples.external_ids JSON blob, for example AsnicarF_2021. [src: pitfalls] Together these cover ≈ 80 % of cMD samples. [src: pitfalls] A short-prefix regex on sample IDs covers < 20 % and produces mostly noise categories. [src: pitfalls]

### Consequences of the confound

Pooled relative-abundance Mann–Whitney was systematically under-sensitive for protective-species depletion. The report attributes this to compositional bias plus pooled-cohort heterogeneity. [src: ibd_phage_targeting] In the protective-species battery, raw Mann-Whitney mis-directed 4+ of 8 species, and centered log-ratio (CLR) correction recovered them. [src: ibd_phage_targeting]

The preliminary pooled analysis called [[entities/clostridium-scindens]] CD-enriched at log₂FC +2.67. This contradicts its described protective bile-acid role and ~79 % prevalence in healthy individuals. [src: ibd_phage_targeting] Under both raw and CLR methods it stayed CD-enriched (raw log₂FC +5.66; CLR Δ +1.25). The report concludes that compositional correction alone is insufficient. [src: ibd_phage_targeting]

The report attributes the NB04 within-ecotype direction reversals to feature leakage compounded with the pooled-cohort substudy × diagnosis confound. Both CLR-MW and LinDA share this bias, so agreement between methods within an ecotype does not resolve it. [src: ibd_phage_targeting] For the engraftment pathobionts specifically, it says the sign was reversed because the HC samples in each ecotype came from entirely different source studies than the CD samples in the same ecotype. [src: ibd_phage_targeting]

## Feature leakage in cluster-stratified differential abundance

Clustering samples on taxon abundance and then running differential abundance on the same taxa within cluster is selection-on-outcome confounding. Cluster membership is a function of the same abundances that the test then uses. Within-cluster effect sizes are mechanically inflated for cluster-defining taxa, and the within-cluster top-N list is largely the cluster definition itself. [src: ibd_phage_targeting, pitfalls] The report names this as a second generalizable methodology contribution. [src: ibd_phage_targeting]

The report extends the warning to microbiome ecotypes and enterotypes. It also extends it to single-cell type-stratified differential expression, and to any analysis where cluster labels are a function of the features being tested. [src: pitfalls]

The adversarial review found this leakage in NB04. [src: discoveries] In NB04, K=4 LDA ecotypes were trained on MetaPhlAn3 species abundances. Within-ecotype CD-vs-HC CLR-Mann-Whitney tests then ran on the same species matrix. [src: pitfalls] NB04 reported a 33-species within-ecotype Tier-A list with effect sizes +0.5 to +3.0 CLR-Δ. [src: pitfalls] The leakage recurred in the v1.6 plan, where pathway differential abundance was stratified by pathway-feature ecotype. [src: discoveries]

### Detection

The report proposes held-out-species sensitivity and leave-one-species-out refitting. [src: ibd_phage_targeting] The held-out-species check used 5 random 50/50 species splits. It refit LDA on half A and tested half B. It compared the refit top-30 with the original top-30 ∩ half-B by Jaccard. [src: pitfalls] The heuristic treats Jaccard > 0.5 as leakage bounded and < 0.3 as leakage dominating. [src: pitfalls] The NB04b held-out-species sensitivity check observed E1 Jaccard 0.230 and E3 Jaccard 0.064. [src: pitfalls] This confirmed substantial leakage. [src: ibd_phage_targeting] The criterion failed in both ecotypes, so the original within-ecotype Tier-A cannot be trusted directly. [src: ibd_phage_targeting]

The leave-one-species-out analysis refit ecotypes without each battery species, re-derived labels, and retested the held-out species. [src: pitfalls] Under it, C. scindens was CD↑ in both E1 (CI +0.68, +0.87) and E3 (CI +1.13, +1.71). [src: pitfalls] NB04 had called it nonsignificant within both ecotypes, and that call was the basis for its "paradox resolved" claim. [src: pitfalls] The report attributes the nonsignificant call to self-selection, and it identified the call as a leakage artifact. [src: pitfalls, discoveries, ibd_phage_targeting]

Two automated reviews of the pre-repair NB04 found no critical issues. An adversarial reviewer found 5 critical and 6 important issues, which NB04b and NB04c empirically confirmed. [src: ibd_phage_targeting] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### What was retracted

The report supersedes the original NB04 analysis and retracts two of its three headline claims. [src: ibd_phage_targeting]

- **H2c, the paradox-resolution claim.** It is retracted. [src: ibd_phage_targeting]
- **The NB04 Tier-A list of 33 species** (18 E1, 15 E3). It is retracted. [src: ibd_phage_targeting]
- **H2b's Jaccard = 0.14 framing.** The value was near the random-overlap baseline of ~0.10 for top-30 of ~300 filtered species. It had no null distribution. The report keeps the conclusion and replaces the statistic. [src: ibd_phage_targeting]
- **H2b support.** A permutation null under randomized ecotype labels gave a mean Jaccard of 0.785 ± 0.054. The observed Jaccard was 0.104, with empirical p = 0.000 over 200 permutations. [src: ibd_phage_targeting]
- **The ecotype-marker reading of E1 candidates.** All 14 E1 candidates passing filters (1) + (2) had negative effects under the confound-free contrast. [src: discoveries] Another statement gives 14 of 18 E1 candidates with negative within-substudy effects, read as ecotype markers. [src: ibd_phage_targeting] The pitfalls report likewise says most NB04 Tier-A E1 candidates had negative within-study effects, so they are ecotype markers rather than CD drivers. [src: pitfalls] The report attributes their apparent CD↑ calls to leakage plus compositional bias. [src: discoveries]
- **The ecotype-marker narrative for engraftment pathobionts.** It is retracted. The report calls them CD drivers under any analysis that controls for study confounding. [src: ibd_phage_targeting]
- **F. prausnitzii, R. hominis and L. eligens.** Their within-ecotype CD↑ calls are retracted. The confound-free analysis shows CD depletion. [src: ibd_phage_targeting]
- **C. scindens "n.s." calls.** They are contradicted. [src: ibd_phage_targeting]

## Within-study designs that repair both problems

Four cMD IBD sub-studies have both CD and nonIBD samples with ≥ 10 each: HallAB_2017, LiJ_2014, IjazUZ_2017 and NielsenHB_2014. In aggregate they hold 242 CD and 369 nonIBD samples. [src: pitfalls]

The report recommends a within-study CLR-Δ or regression within each sub-study, combined by inverse-variance weighted meta-analysis, as the clean CD-effect estimate. [src: pitfalls] This meta-analysis is also the benchmark against which a pooled effect should be sanity-checked. [src: pitfalls]

The replacement computes CLR-Δ within each sub-study, on samples processed the same way by the same group. It then combines sub-studies by inverse-variance weighted meta-analysis. Stratifying by ecotype before meta-analysis gives ecotype-specific effects. [src: ibd_phage_targeting] The report asserts there is no feature-leakage self-reference, because ecotype and CD effect are computed on disjoint axes. [src: ibd_phage_targeting] This was the only evidence stream independent of the ecotype definition that generated NB04. [src: discoveries, ibd_phage_targeting]

Bootstrap stability does not remove the bias. CLR-MW and LinDA use the same ecotype-defined subsamples and share the selection-on-outcome bias. [src: ibd_phage_targeting]

Under the within-IBD-substudy CD-vs-nonIBD contrast, C. scindens is CD↑ with pooled CLR-Δ = +1.18, FDR 1e-8 and 4/4 sign concordance. [src: ibd_phage_targeting] The report uses this meta-analysis rather than within-ecotype stratification to handle HC-study versus IBD-study nesting. [src: ibd_phage_targeting]

In NB04c, the within-ecotype Tier-A was gated with this confound-free within-substudy CD-vs-nonIBD stream. [src: pitfalls] Species had to pass both within-ecotype differential abundance and the independent contrast. This shrank Tier-A from 33 to 3 candidates. [src: pitfalls]

The stricter test also removes some earlier calls. Blautia wexlerae does not replicate in E3 × HallAB_2017 (+0.25, FDR 0.80). It leaves the rock-solid E3 set, which had relied on cohort-level rather than E3-restricted evidence. [src: ibd_phage_targeting]

The v1.6 plan inherited a "4-substudy meta-viable" claim from NB04e without re-verifying the pathway data, which actually had 3+1. [src: discoveries]

## Proposed repairs still open

The report recommends leave-one-feature-out refitting for any feature whose within-cluster differential-abundance call would drive a decision. [src: pitfalls] It proposes defining clusters on a functional matrix (KEGG pathways, MetaCyc or EC numbers, where EC = Enzyme Commission) and then testing taxonomic differential abundance. This would make same-feature leakage structurally impossible. [src: pitfalls] The report proposes rebuilding ecotypes on a functional (pathway or KEGG) feature matrix to break taxonomic-feature leakage. [src: discoveries] That rebuild of Pillar 1 was flagged as future work and not performed. [src: pitfalls] The report also proposes within-IBD-substudy CD-vs-nonIBD analysis stratified by ecotype as the primary analysis. This requires substudy × ecotype × diagnosis cells with ≥ 10 samples each, and their availability needs checking. [src: discoveries]

## Open Directions

- Rebuild ecotypes on a functional (pathway or KEGG) feature matrix, then repeat the held-out-species Jaccard test. This tests whether taxonomic-feature leakage is broken.
- Count substudy × ecotype × diagnosis cells with ≥ 10 samples. This shows whether the stratified within-substudy analysis can be primary.
- Re-verify the substudy count for pathway data before any meta-analysis. This closes the 4-versus-3+1 discrepancy.
- Apply leave-one-species-out refits to other cluster-then-test analyses. See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]] and [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].
