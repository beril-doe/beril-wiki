---
type: Summary
description: Ecotype-specific IBD phage targeting and patient cocktail framework
doc_type: short
full_text: ../sources/ibd_phage_targeting__REPORT.md
title: Metagenome-Prioritized Phage Cocktails for Crohn's Disease and IBD
sources:
- id: ibd_phage_targeting
  resource: ../sources/ibd_phage_targeting__REPORT.md
  title: ibd phage targeting
---
# Metagenome-Prioritized Phage Cocktails for Crohn's Disease and IBD

## Overview

This report closes five project pillars by combining four microbiome ecotypes, rigor-controlled pathobiont prioritization, pathway/BGC/metabolite/strain/serology analyses, three phage-evidence layers, and UC Davis per-patient cocktail design. Its central thesis is that Crohn's disease in joint species–metabolite space is dominated by one canonical correlation axis (r = 0.96), within which six actionable Tier-A pathobionts and two cross-corroborated mechanism narratives support state-dependent hybrid-cocktail design. [^ibd_phage_targeting]

## Key Findings

### Ecotypes and patient stratification

Four ecotypes were selected from 8,489 curatedMetagenomicData MetaPhlAn3 samples (5,333 healthy and 3,156 IBD/other) using consensus K = 4 from cross-method adjusted Rand index between LDA and GMM. The ecotypes were E0 diverse-commensal (3,604 samples; 66.8 % of healthy controls), E1 Bacteroides2-transitional (2,601), E2 Prevotella copri enterotype (920), and E3 severe Bacteroides-expanded (1,364). The consensus framework had 48.9 % per-sample LDA/GMM agreement; K = 4 had cross-method ARI = 0.131, while K = 7 had ARI = 0.140, and the smallest-K-within-0.02-of-maximum parsimony rule selected K = 4. [^ibd_phage_targeting]

All 23 UC Davis patients were projected onto the ecotype embedding: E0 contained 7 samples (27 %), E1 11 (42 %), E2 0, and E3 8 (31 %). The distribution differed from uniformity, χ²(3) = 10.0, p = 0.019. A clinical-covariate classifier achieved macro OvR AUC = 0.799 with {is_ibd, sex, age} and 0.810 with extended severity covariates, but agreement with metagenomic calls was only 41 % (9/22) and 36 % (8/22), respectively; metagenomics therefore remained necessary for patient-level ecotype assignment in this all-CD cohort. [^ibd_phage_targeting]

The ecotype framework showed real cross-study variance: leave-one-substudy-out ARI had mean 0.113 and range 0.000–0.282, while pathway-feature refitting gave ARI = 0.113 and 50.6 % overall agreement. Nevertheless, external HMP_2019_ibdmdb replication included 1,627 samples from 130 subjects, 80.4 % of samples with projection confidence > 0.70, subject-level ecotype × diagnosis χ² = 15.61, p = 0.016, and 88.2 % sign concordance for the E1 Tier-A list (45/51 candidates). [^ibd_phage_targeting]

### Rigor-controlled target prioritization

The report retracts the original NB04 within-ecotype interpretation of the C. scindens result, the original Jaccard framing, and the original 33-species Tier-A list. Under a confound-free within-IBD-substudy CD-versus-nonIBD meta-analysis, C. scindens was CD-up with pooled CLR-Δ = +1.18, FDR = 1e-8, and 4/4 sign concordance; the earlier within-ecotype null result was attributed to feature leakage and study–diagnosis nesting. The corrected E1-versus-E3 top-30 Jaccard was 0.104 against a permutation-null mean of 0.785 ± 0.054 over 200 permutations, empirical p = 0.000. [^ibd_phage_targeting]

The rigor-controlled candidate set contained 51 E1 candidates, 40 provisional E3 candidates, and 5 cross-ecotype engraftment-confirmed pathobionts. Six actionable Tier-A targets reached total score ≥ 2.5: Hungatella hathewayi (4.0), Mediterraneibacter gnavus (3.8), Escherichia coli (3.6), Eggerthella lenta (3.3), Flavonifractor plautii (3.3), and Enterocloster bolteae (2.8). Five of six donor-2708-engraftment pathobionts passed the confound-free CD-up test: M. gnavus (+5.13), E. lenta (+2.30), E. coli (+1.43), E. bolteae (+1.09), and H. hathewayi (+0.92); K. oxytoca was below the prevalence filter. [^ibd_phage_targeting]

CLR-Spearman-Louvain networks contained 3–7 modules per subnet, and every E1_all, E1_CD, E3_all, and E3_CD subnet placed 4–5 of the 6 actionable targets in one pathobiont module. The modules contained 28,730, 15,354, 30,453, and 19,909 edges, respectively, across 6, 4, 3, and 7 modules. The result supports multi-target ecological intervention, but the originally proposed A. caccae cross-feeding interpretation was later reframed as shared-environment co-occurrence after paired metabolomics testing. [^ibd_phage_targeting]

### Mechanism and multi-omics findings

The H3 framework produced 5 SUPPORTED, 1 PARTIALLY SUPPORTED, 2 PARTIAL, and 1 NOT SUPPORTED verdicts. Class-hierarchy pathway analysis found iron/heme acquisition enriched among CD-up pathways with OR = 8.11 and FDR = 7.4e-6, including 15 of 52 CD-up pathways; H. hathewayi had species-level enrichment for purine/pyrimidine recycling (OR = 4.86, FDR = 0.048) and TMA/choline (OR = 9.33, FDR = 0.048). [^ibd_phage_targeting]

The iron-acquisition narrative was concentrated on E. coli. Heme biosynthesis was correlated with E. coli at ρ = 0.640, E. coli had mean ρ = +0.45 with 15 iron pathways, and the Tier-A BGC analysis found iron-siderophore enrichment of OR = 44.4, FDR = 6.5e-56, and genotoxin/microcin enrichment of OR = 234.0, FDR = 3.3e-35. E. coli alone among the six actionable core species carried the iron-plus-genotoxin MIBiG signature: 54 iron BGCs and 25 genotoxin BGCs, including 19 Yersiniabactin, 16 Enterobactin, 8 Colibactin, and 15 Microcin B17 BGCs. [^ibd_phage_targeting]

The bile-acid 7α-dehydroxylation narrative identified F. plautii, E. lenta, and E. bolteae as active network members in 468 paired HMP2 samples. F. plautii correlated with cholate at ρ = −0.26 and lithocholate at ρ = +0.15; E. bolteae correlated with deoxycholate at ρ = +0.17 and lithocholate at ρ = +0.18; and E. lenta correlated with ketodeoxycholate at ρ = −0.14. The pattern supports a bile-acid coupling cost for targeting these species, with F. plautii assigned the highest cost. [^ibd_phage_targeting]

HMP2 metabolomics identified 52 differentially abundant metabolites from 579 testable named metabolites, including 50 CD-up and 2 CD-down metabolites. Polyamines were enriched with OR = 14.6 and FDR = 0.008, and long-chain PUFAs with OR = 7.9 and FDR = 0.009. Urobilin was CD-down with cliff δ = −0.38 and FDR = 0.09, while tauro-α/β-muricholate and free taurine were CD-up. Cross-cohort HMP2-to-FRANZOSA bridging produced 9 strict replications and theme-level sign concordance of 100 % for urobilin/porphyrin, 80 % for acyl-carnitines, and 75 % for long-chain PUFAs; polyamines had no m/z bridge. [^ibd_phage_targeting]

The paired metabolomics analysis found only 7 strict cross-feeding triangles and opposite lactate associations for A. caccae (+0.18) versus F. plautii (−0.23) and E. bolteae (−0.20), so cross-feeding was not supported. In contrast, the same analysis found E. coli-associated cadaverine at ρ = +0.45, with E. coli also associated with choline at +0.25 and tryptophan at +0.25. [^ibd_phage_targeting]

Kumbhari strain-adaptation analysis identified 23,579 FDR < 0.10 genes across 59 species. IBD-biased genes were enriched for adaptation with OR = 1.38 and p = 2.4e-6 and depleted for housekeeping with OR = 0.62 and p = 6.4e-20. F. plautii had 0 FDR-passing strain-adaptation genes among 3,245 tested genes, supporting species-abundance-mediated rather than strain-content-mediated association for that species. Serology did not meet the strict target-correlation threshold: the largest site-adjusted association was ANCA × M. gnavus at r = +0.31, FDR = 0.40. [^ibd_phage_targeting]

A two-modality CCA pilot on 106 paired HMP2 subjects produced four canonical correlations of 0.964, 0.928, 0.911, and 0.889. CC1 had r = 0.964, cliff CD-versus-nonIBD = +0.498, and MW p = 4e-4; all six actionable Tier-A species loaded positively, while urobilin and secondary bile acids loaded negatively and polyamines, PUFAs, fatty-acid amides, and cadaverine loaded positively. The report interprets CC1 as a single dominant CD axis, while noting that the analysis was a pilot and did not include the unavailable pathway modality. [^ibd_phage_targeting]

### Phage evidence and cocktail design

The three-layer phage evidence stack classified the six actionable targets into clinical-trial-stage E. coli, lytic-literature E. lenta and E. bolteae, temperate-only M. gnavus, and coverage gaps for H. hathewayi and F. plautii. PhageFoundry contained 96 phages, 188 E. coli strains, and 17,672 experimentally tested susceptibility pairs, with 3,929 susceptible pairs and a 22 % susceptibility rate. Greedy minimum-set-cover design produced a five-phage cocktail—DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2, and LF110_P2—covering 94.7 % of the 188 strains; the report also describes this as approximately 95 % coverage. [^ibd_phage_targeting]

The extended eight-phage design reached 98.4 % coverage. Of 94 phages with host-phylogroup information, 65 (69 %) were isolated against B2/D hosts, the phylogroups emphasized as AIEC-relevant. Twenty-six strains (14 %) were phage-resistant at ≤5 % susceptibility. HMP2 endogenous phageome analysis covered 630 samples and found Gokushovirus WZ-2015a CD-down in E1 with cliff δ = −0.358, FDR = 5e-7, n_CD = 231, and n_HC = 125; E. coli correlated with Podoviridae at ρ = +0.183 and Myoviridae at ρ = +0.125. [^ibd_phage_targeting]

The phage evidence supports direct targeting for E. coli, monitored lytic-phage targeting for E. lenta and E. bolteae, limited or engineered targeting for M. gnavus, and non-phage alternatives or external database searches for H. hathewayi and F. plautii. The report recommends INPHARED and IMG/VR queries for the three gut-anaerobe gaps, while emphasizing that the current phage evidence does not establish in-vivo efficacy of the PhageFoundry cocktail. [^ibd_phage_targeting]

### Per-patient framework and longitudinal validation

Among 23 UC Davis CD patients, M. gnavus was present in 21 (91 %), H. hathewayi in 19 (83 %), E. bolteae in 19 (83 %), F. plautii in 18 (78 %), E. lenta in 16 (70 %), and E. coli in 8 (35 %). The cohort contained 7 E0, 9 E1, 6 E3, and 1 mixed-ecotype patient. Fourteen of 23 patients (61 %) received concrete phage cocktail drafts, although the report also records 22 patients with a target-level cocktail profile before distinguishing concrete phage availability. [^ibd_phage_targeting]

All 9 E1 patients carried the full five-species E1 pathobiont module, but H. hathewayi and F. plautii were phage gaps and M. gnavus was temperate-only. The report therefore concludes that a pure phage cocktail is structurally infeasible for E1 and requires a three-strategy hybrid: direct phage targeting where lytic options exist, alternatives such as GAG-degrading enzyme inhibitors or bile-acid co-therapy, and limited or engineered approaches for M. gnavus. F. plautii is deprioritized despite its Tier-A score because it combines the highest bile-acid coupling cost with a phage gap. [^ibd_phage_targeting]

Patient 6967 shifted from E1 to E3 across two visits. M. gnavus increased from 0.53 to 7.45 reads, a 14.0× expansion; E. lenta increased 3.1×, F. plautii 1.9×, E. bolteae 2.1×, and H. hathewayi 1.3×, while E. coli remained absent. The visit-level cocktail Jaccard was 0.60, with H. hathewayi, M. gnavus, and E. lenta shared between visits and E. bolteae plus F. plautii present only at visit 1. A patient 1112 resequencing replicate had Tier-A Spearman ρ = 1.000 with p < 0.001. [^ibd_phage_targeting]

The proposed state-dependent workflow recommends ecotype reassessment every 3–6 months, retaining the universal Tier-1 trio of M. gnavus, H. hathewayi, and E. lenta, dropping F. plautii after E1→E3 transition, and considering E. coli targeting in E3 when an AIEC strain diagnostic is positive. A five-fold change in M. gnavus abundance is proposed as a trigger for full ecotype retesting, but the report explicitly labels this qPCR proxy and dosing rule as hypotheses requiring prospective validation. [^ibd_phage_targeting]

## Caveats

The ecotype framework is operationally useful but not uniformly reproducible: LOSO ARI averaged 0.113, the E3 Tier-A list came from a single eligible cMD study, E0 and E2 lacked viable within-ecotype CD-versus-nonIBD contrasts, and hard ecotype assignments discretize an underlying continuum. The Kaiju-to-MetaPhlAn3 projection also showed method asymmetry: LDA was more robust, whereas GMM assigned all 26 UC Davis samples to E3 with confidence >0.97 under sparse feature overlap, an interpretation judged artifactual. [^ibd_phage_targeting]

The project used a partial multi-method differential-abundance consensus because LinDA was implemented in pure Python and ANCOM-BC/MaAsLin2 were not completed. The NB08a species × BGC interaction test was not performed, its full-catalog comparator may inflate the OR = 44.4 estimate, and raw-read strain-resolution analyses were dropped under the no-raw-reads scope. [^ibd_phage_targeting]

The metabolomics ecotype clustering result is specifically limited by uncorrected batch effects: pooled HMP2 and FRANZOSA m/z-bridge clustering separated cohorts, with PC1 explaining 79 % of variance and cross-cohort LOSO ARI = 0.000, below the taxonomic baseline of 0.113. The 3-modality MOFA+ plan was reduced to a 2-modality CCA pilot because HMP2 pathway abundance was unavailable in the mart, and the polyamine signature remains single-cohort because no m/z bridge was found. [^ibd_phage_targeting]

PhageFoundry coverage applies to its 188 tested E. coli strains, not UC Davis patient isolates, and the dataset lacks explicit AIEC-versus-commensal labels, burst-size measurements, titer data, and in-vivo delivery validation. HMP2 viromics had an 80 % family-classification Unknown fraction, and endogenous phage correlations were modest with maximum absolute ρ ≤ 0.18. The three gut-anaerobe coverage gaps remain unresolved pending INPHARED and IMG/VR searches. [^ibd_phage_targeting]

The UC Davis per-patient framework is based on only 23 patients, has no patient-specific bile-acid measurements or AIEC strain-resolution diagnostics, and uses Kaiju-derived target presence. Patient 6967 is the only biological-replicate longitudinal trajectory, so the E1→E3 drift, cocktail Jaccard = 0.60, 3–6-month reassessment interval, five-fold qPCR trigger, and state-dependent dosing rules are hypotheses rather than clinically validated rules. [^ibd_phage_targeting]

## Slots Into

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — Ecotype-specific Tier-A targets, condition-dependent pathobiont modules, and state-dependent cocktail dosing connect microbial fitness to CD ecological states. [^ibd_phage_targeting]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — The CCA pilot integrates taxonomy and metabolomics into CC1, with r = 0.964 and cliff CD-versus-nonIBD = +0.498, while exposing pathway–metabolite pool-versus-flux differences. [^ibd_phage_targeting]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — Iron/heme pathway enrichment, E. coli BGC content, strain-adaptation genes, and bile-acid metabolic signatures distinguish species-abundance-mediated from strain-content-mediated mechanisms. [^ibd_phage_targeting]
- [pangenome-integration](../concepts/pangenome-integration.md) — PhageFoundry strain susceptibility, AIEC phylogroup coverage, and the proposed pks/Yersiniabactin/Enterobactin diagnostic connect strain-level genome content to cocktail selection. [^ibd_phage_targeting]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — The report demonstrates cross-cohort and cross-dataset integration across curatedMetagenomicData, HMP2, FRANZOSA, PhageFoundry, viromics, and UC Davis profiles, while documenting taxonomy synonymy and batch limitations. [^ibd_phage_targeting]

[^ibd_phage_targeting]: [ibd phage targeting](../sources/ibd_phage_targeting__REPORT.md)
