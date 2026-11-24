---
type: "Dataset"
description: "Curated MetaPhlAn3 metagenome collection used to derive four gut ecotypes spanning health and disease."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
aliases: ["CMD", "CMD_HEALTHY", "CMD_IBD", "cMD"]
---
# curatedMetagenomicData

curatedMetagenomicData (cMD; also CMD, with CMD_HEALTHY and CMD_IBD buckets) is a curated collection of MetaPhlAn3 metagenomes. In the ibd_phage_targeting analysis it was used to derive four gut ecotypes that separate disease from healthy samples. [src: discoveries] Its main hazard is that disease status is nested inside source studies, so healthy and Crohn's disease (CD) samples never share a study. [src: ibd_phage_targeting, pitfalls]

## Key facts

- cMD pools samples across ≈ 51 source studies. [src: ibd_phage_targeting] Another report describes it as bundling ~50+ published studies into CMD_HEALTHY and CMD_IBD buckets. [src: pitfalls]
- K=4 LDA-GMM consensus on 8,489 cMD MetaPhlAn3 samples (5,333 healthy controls (HC) + 3,156 inflammatory bowel disease (IBD)/other) gave four ecotypes. They align with published gut enterotype structure and separate disease from healthy samples. [src: discoveries]
- External replication used HMP_2019_ibdmdb, pulled live via curatedMetagenomicData v3.18. It was not in the cMD_IBD training set. [src: ibd_phage_targeting]

## The four ecotypes

| Ecotype | Samples | Defining taxa | Composition |
|---|---|---|---|
| E0 Diverse commensal | 3,604 | F. prausnitzii, R. bromii, B. uniformis, Bifidobacterium, balanced | 66.8 % of HC [src: discoveries] |
| E1 Bacteroides2 transitional | 2,601 | P. vulgatus, B. uniformis, B. dorei | 48 % CD, 58 % UC, 100 % T1D, 97 % T2D, 67 % nonIBD [src: discoveries] |
| E2 Prevotella copri enterotype | 920 | P. copri 28 % | 16.9 % of HC, ~0 % disease (non-Western healthy) [src: discoveries] |
| E3 Severe Bacteroides-expanded | 1,364 | P. vulgatus 14 % + B. fragilis 3.6 % | 50 % CD, 40 % UC, 67 % IBD acute flare, 38 % CDI [src: discoveries] |

Healthy samples concentrate in E0 + E2 (84 % combined). [src: discoveries] CD and UC patients spread across E1 and E3 rather than sitting in one ecotype. The report treats this as a patient-stratification signal for downstream within-ecotype analyses. [src: discoveries] The report reads the link of the Bacteroides2 ecotype to both metabolic disease (T1D, T2D) and IBD as echoing the "low-diversity disease state" hypothesis. This is an interpretation, not a measured result. [src: discoveries]

## Study nesting confound

Disease status is confounded with source study. In the 8,489-sample ecotype-assigned slice, 45 sub-studies have ≥ 10 HC and 5 have ≥ 10 CD, but zero sub-studies contain both. [src: ibd_phage_targeting] The pitfalls digest states the same: no sub-study contains both CD and HC samples. [src: pitfalls] HC samples come from healthy-cohort studies such as LifeLinesDeep_2016, AsnicarF_2021, YachidaS_2019 and HansenLBS_2018. [src: pitfalls] CD samples come from IBD-cohort studies HallAB_2017, VilaAV_2018, LiJ_2014, IjazUZ_2017 and NielsenHB_2014. [src: pitfalls, ibd_phage_targeting] Healthy-versus-CD contrasts therefore cannot separate disease from study effects. See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

The identifiable confound-free contrast is CD versus nonIBD within IBD sub-studies. Four studies have ≥ 10 of each, with CD/nonIBD counts as follows. [src: ibd_phage_targeting]

- HallAB_2017: 89/73 [src: ibd_phage_targeting]
- LiJ_2014: 76/10 [src: ibd_phage_targeting]
- IjazUZ_2017: 56/38 [src: ibd_phage_targeting]
- NielsenHB_2014: 21/248 [src: ibd_phage_targeting]

The aggregate is 242 CD / 369 nonIBD. [src: pitfalls]

## Resolving the sub-study

For IBD samples, participant_id such as CMD:HallAB_2017:SKST006 encodes the sub-study in its middle colon-separated token. [src: pitfalls] For HC samples, the sub-study is in the dim_samples.external_ids JSON blob under the key "study", for example AsnicarF_2021. [src: pitfalls] Together these cover ≈ 80 % of cMD samples. A short-prefix regex on sample IDs covers < 20 % and yields mostly noise categories. [src: pitfalls]

## Related pages

- [[summaries/ibd_phage_targeting__REPORT]]
- [[summaries/discoveries]]
- [[summaries/pitfalls]]
- [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]]
- [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]]
