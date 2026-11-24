---
type: "Concept"
description: "Whether discrete community ecotypes inferred from pooled metagenomes are stable across studies, methods, feature bases and external cohorts, and whether clinical covariates can stand in for metagenomic assignment; stops at what the ecotypes imply for targets."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
---
# Gut microbiome ecotype stability and cross-study reproducibility

Discrete gut ecotypes (community types) inferred from pooled metagenomes in the ibd_phage_targeting project are only partly stable. Cluster boundaries vary across methods, sub-studies and feature bases, and an adversarial review found no external replication of the framework. [src: discoveries, ibd_phage_targeting] Cluster-specific disease findings did replicate externally, and clinical covariates did not substitute for metagenomic assignment. [src: ibd_phage_targeting] The report concludes the framework is cross-study variable but externally usable, because projected ecotypes stratify disease and Tier-A replicates. [src: ibd_phage_targeting] A later leakage check (see below) shows that the within-ecotype candidate lists themselves were partly self-selected and shrank sharply once an independent evidence stream was required. [src: pitfalls]

## Choosing K and cross-method agreement

LDA (latent Dirichlet allocation) held-out perplexity and GMM BIC fall monotonically with K, so they always prefer the largest K. [src: discoveries, ibd_phage_targeting] Five-fold held-out perplexity at ~8.5K samples gave the same monotone signal and did not separate overfitting from real structure. [src: discoveries] The project instead used cross-method adjusted Rand index (ARI) between LDA and GMM, which has peaks and valleys. The reasoning is that the methods agree only on K values that reflect real partitions. [src: discoveries, ibd_phage_targeting]

ARI peaked at K=7 (0.140) and K=4 (0.131). A parsimony rule (smallest K within 0.02 ARI of the maximum) selected K=4. [src: discoveries, ibd_phage_targeting] The report recommends this agreement-based choice for any two-model-family ecotype analysis. [src: discoveries] The four ecotypes were E0 healthy, E1 Bacteroides2 disease, E2 Prevotella and E3 severe Bacteroides. [src: discoveries] E0 is diverse-commensal and contains 66.8 % of HC. [src: ibd_phage_targeting] They were trained on 8,489 curatedMetagenomicData MetaPhlAn3 samples (5,333 HC + 3,156 IBD/other). [src: discoveries, ibd_phage_targeting] The report treats LDA on pseudo-counts as equivalent to Dirichlet multinomial mixtures at this scale. [src: ibd_phage_targeting]

Per-sample agreement between methods at K=4 is only 48.9 %. [src: ibd_phage_targeting] The report reads this as a microbiome continuum discretized for operational use. [src: ibd_phage_targeting] Hard calls should be operational labels, not biology, and soft probabilities are kept. [src: ibd_phage_targeting]

## Stability across studies and feature bases

Internal and cross-study tests show marginal stability. The bootstrap criterion failed: ARI 0.16 against a > 0.30 threshold. [src: ibd_phage_targeting] Bootstrap ARI across 5 × 80 % subsamples was 0.13–0.17. [src: ibd_phage_targeting]

Leave-one-substudy-out (LOSO) testing gave a mean ARI of 0.113 (range 0.000–0.282) and mean per-sample agreement of 55.0 % (range 16.9 %–85.5 %). This fails the > 0.30 threshold, and the report calls it more honest than the bootstrap. [src: ibd_phage_targeting] Sub-studies differed: LifeLinesDeep aligned well (ARI 0.21, agreement 85.5 %), while VilaAV agreed only 17 %. [src: ibd_phage_targeting]

Part of the LOSO gap reflects the 48.9 % cross-method agreement of the consensus baseline. The report still says sub-study variance is real and the "four reproducible ecotypes" framing must be qualified. [src: ibd_phage_targeting]

A refit on pathway features agreed with the taxon consensus at ARI = 0.113 and 50.6 % per-sample agreement. [src: ibd_phage_targeting] The report reads E1 as substantially recoverable from this disjoint feature basis. [src: ibd_phage_targeting] E3 was less recoverable (30.7 %), which with single-study E3 evidence supports only a provisional E3 Tier-A framing. [src: ibd_phage_targeting] It describes the structure as mixed ecological and taxonomic. [src: ibd_phage_targeting]

## Feature leakage in within-ecotype testing

The NB04 ecotypes were trained on MetaPhlAn3 species abundances, and within-ecotype CD-vs-HC CLR-Mann-Whitney tests were then run on the same species matrix. [src: pitfalls] NB04 reported a 33-species within-ecotype Tier-A list with effect sizes +0.5 to +3.0 CLR-Δ. [src: pitfalls]

The NB04b held-out-species check used 5 random 50/50 species splits. It refit LDA on half A, tested half B, and compared the refit top-30 with the original top-30 ∩ half-B by Jaccard index. [src: pitfalls] The heuristic treats Jaccard > 0.5 as leakage bounded and < 0.3 as leakage dominating. [src: pitfalls] Observed values were E1 = 0.230 [src: pitfalls] and E3 = 0.064 [src: pitfalls], both below 0.3.

A leave-one-species-out refit re-derived ecotype labels without each battery species and retested that species. [src: pitfalls] C. scindens (see [[entities/clostridium-scindens]]) was called nonsignificant within both ecotypes in NB04, the basis for a "paradox resolved" claim. [src: pitfalls] Under leave-one-species-out it was CD-increased in E1 (CI +0.68, +0.87) [src: pitfalls] and in E3 (CI +1.13, +1.71). [src: pitfalls] The report attributes the earlier nonsignificant call to self-selection. [src: pitfalls]

An independent within-IBD-substudy CD-vs-nonIBD analysis found that most NB04 Tier-A E1 candidates had negative within-study effects. The report interprets them as ecotype markers rather than CD drivers. [src: pitfalls] NB04c therefore gated the within-ecotype Tier-A with that independent, confound-free evidence stream. [src: pitfalls] Requiring both contrasts shrank Tier-A from 33 to 3 candidates. [src: pitfalls]

## External cohorts and operational replication

Framework stability and operational-claim replication are distinct properties needing separate tests. A project can have shaky cluster boundaries but robust cluster-specific findings. [src: ibd_phage_targeting] In external HMP2 (HMP_2019_ibdmdb) replication, 1,627 samples from 130 subjects were projected onto the K=4 LDA, with 80.4 % of samples at confidence > 0.70. [src: ibd_phage_targeting] E1 Tier-A replicated at 88.2 % sign-concordance (45 / 51 candidates CD↑ in both cohorts), including every top-10 candidate. [src: ibd_phage_targeting] The per-species comparison used CD-vs-nonIBD CLR-Δ within HMP2-projected E1 samples (593 CD / 337 nonIBD). [src: ibd_phage_targeting] Two of the top 20 candidates failed: S. thermophilus on effect sign, and B. stercoris as sign-discordant and non-significant. [src: ibd_phage_targeting] The S. thermophilus effect was slightly negative in HMP2, potentially reflecting differential dairy exposure between HMP2 and HallAB/NielsenHB cohorts. [src: ibd_phage_targeting]

HMP2 subject-level ecotype also stratified CD, UC and nonIBD diagnosis (χ² = 15.61, p = 0.016). [src: ibd_phage_targeting] HMP2 skews more toward E1 than curatedMetagenomicData, which is more balanced between E1 and E3. The report suggests this likely reflects recruitment of newly diagnosed or milder IBD rather than flare-dominated severe disease. [src: ibd_phage_targeting] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]] for the target side.

## Projection across classifiers

The held-out cohort used Kaiju NCBI-NR read classification, and the reference embedding used MetaPhlAn3 marker-gene abundance. [src: discoveries] LDA on pseudo-counts was robust because non-detection does not force a projection coordinate. [src: discoveries] All 23 UC Davis patients were projected onto the four-ecotype embedding through the report's synonymy layer. [src: ibd_phage_targeting] UC Davis Kuehl samples projected to E0, E1 and E3 at 27 / 42 / 31 %, described as plausible. [src: discoveries] No patient fell in E2. The distribution is non-random (χ²(3) = 10.0, p = 0.019) and consistent with an active-disease Western cohort. [src: ibd_phage_targeting] See [[entities/uc-davis-kuehl-wgs-crohn-s-disease-cohort]].

GMM on CLR (centered log-ratio) + PCA (principal component analysis) was fragile. The report states that Kuehl detects only 54 % of training species [src: discoveries] and, separately, that 70 % of training species have no Kuehl detection. [src: discoveries] These two figures are not consistent with each other as stated, since 54 % detected would leave 46 % undetected. The report does not reconcile them, so each is given as written. Zero imputation with a small pseudocount puts sparse vectors in one dominant Gaussian cluster regardless of biology. [src: discoveries] All 26 Kuehl samples projected to E3 at GMM confidence > 0.97, which the report calls an artifact. [src: discoveries] The report recommends LDA or MMvec as primary and CLR-based methods as advisory at best. [src: discoveries]

## Can clinical covariates replace metagenomics?

No. A classifier using is_ibd, sex and age to predict K=4 ecotypes reached macro one-versus-rest (OvR) AUC 0.80 in 5-fold CV, above the 0.70 threshold (0.799, n = 8,489). [src: discoveries, ibd_phage_targeting] On UC Davis patients, where is_ibd is constant, it agreed with the metagenomic call for only 41 % (9/22). [src: discoveries, ibd_phage_targeting] It predicted E1 for 19/22 patients, following the marginal mode among IBD training samples. [src: discoveries, ibd_phage_targeting] The AUC counted healthy-versus-IBD separability, whereas UC Davis needed the harder separation of E1 from E3 within IBD. [src: discoveries] Metagenomics therefore remains required for ecotype assignment in UC Davis-type cohorts. [src: ibd_phage_targeting]

Training-cohort OvR-AUC is a weak proxy for patient-level usefulness when a strong cohort-axis variable is constant in held-out patients. [src: discoveries, ibd_phage_targeting] The report recommends testing on an independent cohort with that variable held fixed and using agreement there as the honest metric. [src: discoveries] See also [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]] and [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

## Tensions

- The adversarial review flagged 48.9 % cross-method agreement and no external replication of the framework. [src: discoveries] The project reports 88.2 % HMP2 sign-concordance for operational Tier-A. [src: ibd_phage_targeting] The report reconciles these only by separating framework stability from claim replication. [src: ibd_phage_targeting]
- Bootstrap ARI (0.13–0.17) suggested modest stability. LOSO ARI (mean 0.113, range 0.000–0.282) showed bootstrap masked sub-study variation. [src: ibd_phage_targeting]
- The Kuehl species-detection figures (54 % detected; 70 % with no detection) disagree on their face. [src: discoveries]
- The report calls the operational Tier-A validated by 88 % HMP2 replication. [src: ibd_phage_targeting] Yet the leakage checks found low Jaccard (E1 0.230, E3 0.064) and shrank the within-ecotype Tier-A from 33 to 3 once an independent stream was required. [src: pitfalls]

## Open Directions

- Fit LDA and GMM on a second, independent pooled cohort and test whether ARI again peaks at K=4. This would give the external replication of the framework that is currently missing.
- Re-run the LOSO test with a consensus baseline that avoids the 48.9 % LDA↔GMM disagreement, to separate baseline error from true sub-study variance.
- Recompute the Kuehl species-detection fraction against the training species list, to resolve the 54 % versus 70 % discrepancy.
- Project Kuehl onto the reference with a Kaiju-matched reference or restricted to commonly detected species, to check whether the E0/E1/E3 split holds.
- Evaluate the clinical classifier within IBD only (is_ibd fixed) on a second IBD cohort, to measure real patient-level agreement.
- Examine why E3 is less recoverable (30.7 %) from pathway features, using additional multi-study E3 samples.
- Check how many of the 45 HMP2-concordant E1 candidates are among the 3 that survive the independent-stream gate, to separate replication of ecotype markers from replication of CD drivers.
