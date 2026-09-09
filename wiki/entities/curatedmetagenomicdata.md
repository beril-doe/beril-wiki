---
type: "Dataset"
description: "Cross-cohort microbiome dataset used for ecotype and IBD analyses"
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
---
# curatedMetagenomicData

## What it is

**Canonical name:** curatedMetagenomicData. [src: discoveries]

**Known aliases:** `curatedMetagenomicData`. [src: discoveries]

**Stable external identifier:** No stable external identifier was reported in [[summaries/discoveries]]. [src: discoveries]

curatedMetagenomicData is a microbiome dataset used in cross-cohort analysis summarized in [[summaries/discoveries]] and in the metagenome-prioritized phage-targeting analysis summarized in [[summaries/ibd_phage_targeting__REPORT]]. [src: discoveries] [src: ibd_phage_targeting]

## Key facts

A K=4 LDA-GMM consensus analysis of 8,489 curatedMetagenomicData samples produced four ecotypes: E0 diverse commensal (n=3,604), E1 Bacteroides2 transitional (n=2,601), E2 Prevotella copri enterotype (n=920), and E3 severe Bacteroides-expanded (n=1,364). [src: discoveries]

Healthy samples concentrated in E0 and E2, which together accounted for 84% of healthy samples, whereas Crohn’s disease and ulcerative colitis samples were distributed across E1 and E3. [src: discoveries]

The newer analysis **supports** these ecotype definitions and refines the E0 result: E0 contained 66.8% of healthy controls, while the full dataset contained 5,333 healthy and 3,156 IBD/other samples. [src: ibd_phage_targeting]

Cross-method adjusted Rand index (ARI), a clustering-agreement measure, selected K=4 because ARI was 0.131, within 0.02 of the peak at K=7 with ARI=0.140. [src: discoveries]

A pooled classifier achieved a macro one-versus-rest area under the receiver operating characteristic curve (OvR AUC) of 0.80 but achieved only 41% agreement on UC Davis patients. [src: discoveries]

The newer analysis **refines** this portability result: among 23 UC Davis patients, the metagenomic ecotype distribution was E0=7 (27%), E1=11 (42%), E2=0, and E3=8 (31%), with χ²(3)=10.0 and p=0.019. A clinical-covariate classifier achieved macro OvR AUC=0.799, or 0.810 with extended severity covariates, but agreement with metagenomic calls was 41% (9/22) and 36% (8/22), respectively. [src: ibd_phage_targeting]

On the UC Davis patients, `is_ibd=1` was constant and 19 of 22 patients were predicted as E1, exposing a portability failure in the pooled classifier. [src: discoveries]

Projection using LDA across MetaPhlAn3 namespaces produced plausible Kuehl ecotype proportions of 27%, 42%, and 31%, while CLR-plus-PCA GMM projected all 26 Kuehl samples to E3 at confidence greater than 0.97 because Kuehl detected only 54% of the training species. [src: ibd_phage_targeting]

The newer report **supports** retaining metagenomics for patient-level assignment: leave-one-substudy-out ARI had mean 0.113 and range 0.000–0.282, while pathway-feature refitting gave ARI=0.113 and 50.6% overall agreement. External HMP_2019_ibdmdb replication included 1,627 samples from 130 subjects; 80.4% of samples had projection confidence >0.70, and subject-level ecotype × diagnosis yielded χ²=15.61 and p=0.016. [src: ibd_phage_targeting]

The pitfalls analysis **qualifies** disease-comparison inference: healthy and disease buckets contain disjoint sub-studies, and among 8,489 ecotype-assigned samples, 45 sub-studies had at least 10 HC samples, 5 had at least 10 CD samples, and 0 had at least 10 of both; four IBD sub-studies with at least 10 CD and 10 nonIBD samples comprised 242 CD and 369 nonIBD samples. Within-substudy contrasts combined by inverse-variance meta-analysis are therefore design-consistent, whereas a pooled `log_abundance ~ diagnosis + (1 | substudy)` model is structurally unidentifiable for the CD-versus-HC contrast. [src: pitfalls]

The phage-targeting analysis is also **qualified** by selection leakage: clustering taxa and testing those same taxa produced a 33-species Tier-A list, but held-out-species sensitivity gave Jaccard values of 0.230 for E1 and 0.064 for E3; independent within-substudy evidence reduced the list from 33 candidates to 3. [src: pitfalls]

MetaPhlAn3 cross-cohort use requires a synonymy layer rather than simple string normalization, because GTDB renamings and lineage differences can create false contrasts; one CrohnsPhage comparison reached log₂FC approximately 28, equivalent to approximately 2.68 × 10⁸ fold, when one cohort’s abundance collapsed to a pseudocount. [src: pitfalls]

The dataset therefore supports cross-cohort microbiome ecotype analysis, but its use for transferring classifiers requires explicit validation against cohort effects, feature-namespace differences, study design, and selection leakage. [src: discoveries] [src: pitfalls]

These portability limitations connect curatedMetagenomicData to [[concepts/multi-omics-integration]] and to [[entities/metaphlan3]]. [src: discoveries]

## Related source

- [[summaries/ibd_phage_targeting__REPORT]] — applies the ecotype framework to patient stratification and state-dependent phage-cocktail design. [src: ibd_phage_targeting]
- [[summaries/pitfalls]] — documents cohort-design, namespace-reconciliation, and leakage safeguards for analyses using the dataset. [src: pitfalls]
