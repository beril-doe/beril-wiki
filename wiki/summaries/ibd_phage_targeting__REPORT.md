---
type: "Summary"
description: "Summary of the project Metagenome-Prioritized Phage Cocktails for Crohn's Disease and IBD."
doc_type: "short"
full_text: "sources/ibd_phage_targeting__REPORT.md"
---
# Metagenome-Prioritized Phage Cocktails for Crohn's Disease and IBD

Some verdicts are strong and others are partial. The report scores its H3 hypotheses as 5 SUPPORTED + 1 PARTIALLY SUPPORTED + 2 PARTIAL + 1 NOT SUPPORTED. [src: ibd_phage_targeting]

## Key Findings

### Ecotypes and rigor-controlled target discovery

The ecotype structure is reported as mixed ecological and taxonomic, not purely either. [src: ibd_phage_targeting] For example, the Bacteroides2 transitional ecotype E1 has n = 2,601, with defining abundances of P. vulgatus 9.8 %, B. uniformis 7.2 % and Phocaeicola dorei 3.5 %. [src: ibd_phage_targeting] LDA is the primary Kuehl ecotype projection call, and GMM (Gaussian mixture model) is advisory. [src: ibd_phage_targeting]

A rigor-repair pipeline (NB04b to NB04e) replaced the earlier pooled analysis. NB04b adds bootstrap CIs, leakage-bound sensitivity, LOO refit, a Jaccard permutation null and ecotype stability. [src: ibd_phage_targeting] NB04e then defines ecotype-specific Tier-A targets by within-ecotype × within-substudy meta-analysis of 4 IBD sub-studies with both CD and nonIBD. [src: ibd_phage_targeting] Examples:
- C. scindens had pooled CLR-Δ +1.18, FDR 1e-8 and sign concordance 4/4 in NB04c. [src: ibd_phage_targeting]
- S. thermophilus ranked 3 in E1 with CLR-Δ +2.69 and FDR 4e-6. [src: ibd_phage_targeting]
- The E3 Tier-A result is provisional and rests on the single study HallAB_2017. C. spiroforme is a top candidate there with CLR-Δ +4.11. [src: ibd_phage_targeting]

Compositional correction matters. In NB00, L. eligens and other protective species flip from nonsignificant in raw Mann-Whitney analysis to CD-depleted in CLR analysis. [src: ibd_phage_targeting] NB05 was authorized to proceed for E1 with a 51-candidate meta-viable Tier-A. [src: ibd_phage_targeting]

### Target prioritization

NB05 scores CD association from 0–5 using five independent signals. [src: ibd_phage_targeting] It yields six actionable Tier-A targets: H. hathewayi (4.0), M. gnavus (3.8), E. coli (3.6), E. lenta (3.3), F. plautii (3.3) and E. bolteae (2.8). [src: ibd_phage_targeting] M. gnavus is the top candidate across all three NB05 input categories. [src: ibd_phage_targeting] E. coli ranks 3, supported by engraftment and MIBiG matches to Colibactin, Yersiniabactin and Enterobactin. [src: ibd_phage_targeting] The report treats E. coli as a Tier-1 phage target that needs strain resolution, aimed at the AIEC (adherent-invasive E. coli) subset. [src: ibd_phage_targeting]

### Mechanism layers (pathways, BGCs, metabolomics, multi-omics)

- NB07a: E. coli has 105 Tier-A pathway pairs > 0.4, while F. plautii has 7. [src: ibd_phage_targeting] Pathway meta-viability is 3 robust substudies plus 1 boundary (LiJ_2014, nonIBD = 10), not the "4 meta-viable" framing inherited from the taxonomic counts. [src: ibd_phage_targeting]
- NB07b: within carriers, E. coli shows less metabolic versatility per cell in CD samples. [src: ibd_phage_targeting] For E. bolteae, H3a (b) was untestable. [src: ibd_phage_targeting]
- NB07c: the module coupling was later reframed as shared-environment co-occurrence in healthy/normobiotic samples. [src: ibd_phage_targeting]
- NB08a: NRPS_PKS_hybrid BGCs were enriched in the Tier-A core (32 / 286 versus 739 / 9,774 background; Fisher OR 1.54, FDR 0.042). [src: ibd_phage_targeting]
- NB09a: metabolomics found several long-chain PUFAs CD-up, such as docosapentaenoate (cliff +0.45, FDR 0.06). [src: ibd_phage_targeting] For the E. coli iron/heme axis, metabolomics is neutral because LC-MS undersamples siderophores, while BGC evidence corroborates the axis. [src: ibd_phage_targeting]
- NB09c: bile-acid coupling cost differs by species. F. plautii has the highest cost and is an active 7α-dehydroxylator. [src: ibd_phage_targeting] E. bolteae has moderate cost. [src: ibd_phage_targeting]
- NB07d: all 6 actionable Tier-A core species load CD-positive on CC1 in HMP2. [src: ibd_phage_targeting]

### Phage targetability and per-patient design

Pure phage cocktails are not feasible for any E1 patient. Only a hybrid with non-phage alternatives is. [src: ibd_phage_targeting] H. hathewayi and F. plautii, the 2 highest-NB05-scored species, are both Pillar-4 phage gaps. [src: ibd_phage_targeting] For H. hathewayi, the report prioritizes INPHARED and IMG/VR searches and proposes GAG-degrading enzyme inhibitors if no phages are found. [src: ibd_phage_targeting]

For E. coli, NB13 greedy minimum-set-cover gives a 5-phage cocktail covering 94.7 % of 188 strains. [src: ibd_phage_targeting] At the initial visit, the workflow recommends a focused E3 cocktail. [src: ibd_phage_targeting]

In UC Davis CD patient 6967, M. gnavus expanded 14× in an E1→E3 transition, and E. coli stayed absent. [src: ibd_phage_targeting] This motivates the hypothesis that M. gnavus qPCR could serve as a cheap proxy for ecotype shift. [src: ibd_phage_targeting]

## Thesis (Pillars 1–5 closed)

This part of the report closes all five project pillars. It argues that Crohn's disease (CD) variation is one dominant axis, that phage evidence supports only part of the target list, and that per-patient cocktails need a hybrid strategy. [src: ibd_phage_targeting]

### A single cross-modality axis

The report treats CD at the gut-microbiome level as a single principal-direction phenomenon in joint species–metabolite space, not a many-axis manifold. [src: ibd_phage_targeting] The dominant cross-modality structure in HMP2 metagenomics plus metabolomics is a canonical correlation pair with r = 0.96. [src: ibd_phage_targeting] A single composite axis separates CD from non-IBD subjects at cliff δ = +0.50 (p = 4×10⁻⁴). [src: ibd_phage_targeting]

On this axis, the six actionable Tier-A pathobionts load CD-positive: *H. hathewayi*, *M. gnavus*, *E. coli*, *E. lenta*, *F. plautii* and *E. bolteae*. [src: ibd_phage_targeting] The commensals *R. bromii*, *A. putredinis* and *L. eligens* load CD-negative, as do urobilin and secondary bile acids. [src: ibd_phage_targeting] Polyamines, long-chain polyunsaturated fatty acids (PUFAs), fatty-acid amides described as ebf/ecf substrates, and *E. coli*-specific cadaverine load CD-positive. [src: ibd_phage_targeting]

The report reads its separate analyses as projections of this same axis. These are pathway differential abundance, biosynthetic gene cluster (BGC), metabolomics, paired species–metabolite and co-occurrence modules. [src: ibd_phage_targeting] Within the axis, the iron-acquisition narrative centred on adherent-invasive *E. coli* (AIEC) and the bile-acid 7α-dehydroxylation narrative are orthogonal sub-mechanisms. The second centres on *F. plautii*, *E. lenta* and *E. bolteae*. [src: ibd_phage_targeting]

### Phage targetability

The phage evidence stack has three layers: literature curation (NB12), experimental susceptibility (NB13) and in-vivo phageome (NB14). [src: ibd_phage_targeting] Targets fall into different evidence classes:

| Species | Phage evidence |
|---|---|
| *E. coli* | Clinical-trial-stage, with EcoActive as precedent [src: ibd_phage_targeting] |
| *E. lenta*, *E. bolteae* | Lytic literature phages PMBT5 and PMBT24 [src: ibd_phage_targeting] |
| *M. gnavus* | Temperate-only, 6 phages [src: ibd_phage_targeting] |
| *H. hathewayi*, *F. plautii* | Coverage gap [src: ibd_phage_targeting] |

A concrete 5-phage *E. coli* AIEC cocktail covers 95 % of 188 PhageFoundry-tested strains. Its phages are DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2 and LF110_P2. [src: ibd_phage_targeting] The two gap species also have the highest NB05 scores, 4.0 and 3.3. [src: ibd_phage_targeting] INPHARED and IMG/VR external database queries remain the highest-priority follow-up. [src: ibd_phage_targeting]

### Per-patient cocktails in the UC Davis cohort

The framework profiles 23 UC Davis CD patients by ecotype, Montreal classification, calprotectin, medication and Kuehl_WGS Tier-A presence. [src: ibd_phage_targeting] Concrete cocktail drafts were produced for 14 of 23 patients (61 %). [src: ibd_phage_targeting] All 9 E1 patients carry the full Tier-A pathobiont module. [src: ibd_phage_targeting] A pure phage cocktail is not feasible for any E1 patient. [src: ibd_phage_targeting]

The report therefore proposes a 3-strategy hybrid. [src: ibd_phage_targeting]
- Direct phage targeting covers *E. coli* AIEC, *E. bolteae* with PMBT24 and *E. lenta* with PMBT5. [src: ibd_phage_targeting]
- Alternative therapies are *H. hathewayi* GAG-degrading enzyme inhibitors and *F. plautii* bile-acid-binding co-therapy. [src: ibd_phage_targeting]
- Limited or engineered approaches for *M. gnavus* are lytic-locked phage engineering or a biochemical glucorhamnan-synthesis target. [src: ibd_phage_targeting]

*F. plautii* is present in 78 % of patients, including all 9 E1. [src: ibd_phage_targeting] The report calls its bile-acid-coupling cost the dominant E1 design constraint. That cost is the highest, and it combines with the phage gap into a double penalty, so the report deprioritizes the species from the cocktail. [src: ibd_phage_targeting]

*E. coli* is present in only 35 % of patients, much lower than expected for an AIEC-canonical species. [src: ibd_phage_targeting] The NB13 5-phage cocktail is therefore directly applicable to only ~8/23 patients. [src: ibd_phage_targeting]

### Longitudinal check and dosing rules

Patient 6967 is the only UC Davis patient with biological-replicate samples at multiple timepoints. [src: ibd_phage_targeting] This patient shows E1→E3 ecotype drift across 2 visits. [src: ibd_phage_targeting] The dominant signature is a 14× *M. gnavus* expansion, from 0.53 to 7.45 reads. [src: ibd_phage_targeting] Cocktail Jaccard between visits is 0.60. [src: ibd_phage_targeting] Three targets are shared: *H. hathewayi*, *M. gnavus* and *E. lenta*, the "universal Tier-1 trio". [src: ibd_phage_targeting] Two targets, *E. bolteae* and *F. plautii*, appear only at visit 1 and are described as E1-specific. [src: ibd_phage_targeting] Patient 1112 technical replicates have Tier-A Spearman ρ = 1.000. The report reads this as Kaiju reliability across resequencing replicates, which validates the technical-noise floor. [src: ibd_phage_targeting]

The report's five state-dependent dosing rules include these:
- Re-test ecotype every 3–6 months. [src: ibd_phage_targeting]
- Make *F. plautii* inclusion E1-specific, dropping it on E1→E3. [src: ibd_phage_targeting]
- Make *E. coli* inclusion E3-specific, subject to AIEC strain detection. [src: ibd_phage_targeting]
- Use the universal Tier-1 trio as the backbone for any active-disease CD patient. [src: ibd_phage_targeting]

*M. gnavus* qPCR is proposed as a cheap clinical proxy for ecotype state. A 5-fold change triggers a full ecotype re-test and avoids routine metagenomics. [src: ibd_phage_targeting] The clinical-translation workflow runs from initial ecotype assignment to an ecotype-specific cocktail. It then moves to 3–6 month follow-up with calprotectin, qPCR and an ecotype-shift decision tree. [src: ibd_phage_targeting]

### Closure, rigor and limits

NB17 gives a cross-cutting synthesis, a per-patient master table, a target decision matrix and a 4-phase clinical-translation roadmap. [src: ibd_phage_targeting] The project has 31 notebooks and 24 numbered Novel Contributions. [src: ibd_phage_targeting] INPHARED and IMG/VR queries and multi-cohort prospective validation remain out-of-scope clinical-translation prerequisites. [src: ibd_phage_targeting]

The original NB04 analysis was superseded by a seven-notebook pipeline. An adversarial review found 5 critical and 6 important methodological issues that two standard reviews missed. [src: ibd_phage_targeting] NB04b–e repaired the rigor. NB04f–h tested leave-one-substudy-out (LOSO) cross-study stability, feature-leakage structure and HMP_2019_ibdmdb external replication. [src: ibd_phage_targeting] The rigor-controlled Tier-A set replicates at 88.2 % sign concordance on HMP2. [src: ibd_phage_targeting] The ecotype framework itself still has real cross-study variance. [src: ibd_phage_targeting]

## Thesis (Pillars 1–5 closed); Executive Summary

This part of the report sets out the thesis. Crohn's disease (CD) and ulcerative colitis (UC) microbiomes partition into reproducible ecotypes with distinct pathobiont signatures, so cohort-level phage cocktails will mismatch individual patients unless ecotype is known first. [src: ibd_phage_targeting] The project asks whether ecotypes can be defined, UC Davis Crohn's patients placed on them, and ecotype-specific and per-patient target lists derived. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]] and [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

### Ecotype framework

The report trained four ecotypes on 8,489 curatedMetagenomicData MetaPhlAn3 samples (5,333 healthy controls (HC) + 3,156 IBD/other). [src: ibd_phage_targeting] Consensus K = 4 came from the cross-method adjusted Rand index between LDA and a Gaussian mixture model (GMM). Perplexity and BIC kept preferring larger K. [src: ibd_phage_targeting]

- E0: diverse-commensal, holding 66.8 % of HC. [src: ibd_phage_targeting]
- E1: Bacteroides2-transitional, dominant in CD/UC/T1D/T2D. [src: ibd_phage_targeting]
- E2: *Prevotella copri* enterotype, non-Western healthy. [src: ibd_phage_targeting]
- E3: severe Bacteroides-expanded, linked to IBD flare, CDI and donor 2708. [src: ibd_phage_targeting]

External replication used HMP_2019_ibdmdb, pulled live with curatedMetagenomicData v3.18 and not in the training set. [src: ibd_phage_targeting] It projected 1,627 samples from 130 subjects onto the K=4 LDA, with 80.4 % of samples at confidence > 0.70. [src: ibd_phage_targeting] Subject-level ecotype × {CD, UC, nonIBD} gave χ² = 15.61, p = 0.016, so ecotype stratifies disease in HMP2. [src: ibd_phage_targeting]

### UC Davis placement

All 23 UC Davis patients were projected onto the embedding through a taxonomy synonymy layer. [src: ibd_phage_targeting] The layer maps 2,417 aliases to 1,848 canonical species, using NCBI taxid and GTDB r214+ genus renames. [src: ibd_phage_targeting] The report calls data/species_synonymy.tsv the reconciliation backbone for cMD pooling and Kaiju → MetaPhlAn3 projection. [src: ibd_phage_targeting] See [[entities/uc-davis-kuehl-wgs-crohn-s-disease-cohort]].

Patients fell in E0 (27 %), E1 (42 %) and E3 (31 %), and none fell in E2. This is non-random (χ²(3) = 10.0, p = 0.019) and fits an active-disease Western cohort. [src: ibd_phage_targeting] Patient 6967 drifted from E1 to E3 across re-sampling. The report calls this its first direct signal of intra-patient ecosystem instability. [src: ibd_phage_targeting]

A classifier using HC/IBD status, sex and age reached macro AUC 0.80 in pooled cross-validation. It agreed with the metagenomic projection for only 41 % of UC Davis patients. [src: ibd_phage_targeting] It collapses to "IBD → E1" because is_ibd dominates and is constant in the test cohort. The report concludes that metagenomics is still required for patient-level assignment in an all-CD cohort. [src: ibd_phage_targeting]

### Rigor-controlled targets

Raw Mann-Whitney tests on relative abundance mis-directed 4+ of 8 protective species. CLR (centered log-ratio) correction recovered them. [src: ibd_phage_targeting]

Two original claims were retracted. The first was that within-ecotype stratification resolves the pooled-CLR CD↑ *C. scindens* result. [src: ibd_phage_targeting] The second was H2c, the paradox resolution. The NB04 within-ecotype "n.s." call came from feature leakage, where samples are clustered on taxon abundances and the same taxa are then tested within cluster. [src: ibd_phage_targeting] Leave-one-species-out refitting finds *C. scindens* CD↑ in both E1 and E3. [src: ibd_phage_targeting] A within-IBD-substudy CD-vs-nonIBD meta-analysis (NB04c §3) gave pooled CLR-Δ = +1.18, FDR = 1e-8 and 4/4 sign concordance. [src: ibd_phage_targeting] The report lists both pitfalls, cMD substudy-nesting and feature leakage, as generalizable. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]] and [[entities/clostridium-scindens]].

H2b (ecotype-specific targeting) is supported at high confidence. Under 200 permutations of randomized ecotype labels, Jaccard(top-30 E1, top-30 E3) had a null mean of 0.785 ± 0.054. The observed value was 0.104, with empirical p = 0.000. [src: ibd_phage_targeting] NB04's earlier "Jaccard = 0.14" framing is retracted because it was near the random-overlap baseline and had no null distribution. The conclusion survives and the statistic does not. [src: ibd_phage_targeting]

NB04e defines ecotype-specific Tier-A lists by within-ecotype × within-substudy meta-analysis. It uses the 4 IBD sub-studies with both CD and nonIBD: HallAB_2017, LiJ_2014, IjazUZ_2017 and NielsenHB_2014. [src: ibd_phage_targeting]

- **E1 Tier-A:** 51 candidates, from 2 sub-studies (HallAB_2017 + NielsenHB_2014, 82 CD / 280 nonIBD), all 100 % sign-concordant. [src: ibd_phage_targeting] Top candidates are *M. gnavus* (+4.85) [src: ibd_phage_targeting], *S. salivarius* (+3.26) [src: ibd_phage_targeting], *S. thermophilus* (+2.69) [src: ibd_phage_targeting], *Erysipelatoclostridium innocuum* (+2.65) [src: ibd_phage_targeting], *S. parasanguinis* (+2.44) [src: ibd_phage_targeting] and *Enterocloster asparagiformis* (+2.41). [src: ibd_phage_targeting] The report calls this list classical CD pathobionts, not the ecotype-marker commensals that NB04's within-ecotype analysis spuriously produced. [src: ibd_phage_targeting]
- **E3 Tier-A:** 40 candidates from the single study HallAB_2017 (22 CD / 31 nonIBD). [src: ibd_phage_targeting] The list is provisional. Replication needs a second cMD-IBD study with both CD and nonIBD in E3, which is blocked until HMP2 raw data (`PENDING_HMP2_RAW`) is ingested. [src: ibd_phage_targeting] Top candidates are *H. symbiosa* (+4.64) [src: ibd_phage_targeting], *M. gnavus* (+4.46) [src: ibd_phage_targeting], *B. coccoides* (+4.22) [src: ibd_phage_targeting], *R. faecis* (+4.14) [src: ibd_phage_targeting] and *C. spiroforme* (+4.11). [src: ibd_phage_targeting]
- **Engraftment-confirmed pathobionts:** In the non-ecotype-stratified within-IBD-substudy contrast, five of six donor-2708-engraftment pathobionts pass as CD↑ with FDR < 0.10 and ≥ 66 % sign concordance. They are *M. gnavus* (+5.13) [src: ibd_phage_targeting], *E. lenta* (+2.30) [src: ibd_phage_targeting], *E. coli* (+1.43) [src: ibd_phage_targeting], *E. bolteae* (+1.09) [src: ibd_phage_targeting] and *H. hathewayi* (+0.92). [src: ibd_phage_targeting] *K. oxytoca* fell below the prevalence filter and was not tested. [src: ibd_phage_targeting]

The rigor-controlled NB05 input is the deduplicated union of the E1 Tier-A (51), the E3 provisional Tier-A (40) and the 5 engraftment-confirmed pathobionts. That comes to approximately 70–90 unique species. [src: ibd_phage_targeting] *M. gnavus* is the top candidate in all three categories. [src: ibd_phage_targeting] See [[entities/mediterraneibacter-gnavus]].

## Executive Summary: Pillar 3 deliverables (this report)

This part of the report gives the rigor-controlled results on Tier-A replication in HMP2, actionable target scoring (NB05), co-occurrence networks (NB06), and verdicts on the H3 falsifiability framework (Pillar 3 notebooks). [src: ibd_phage_targeting]

### Replication of Tier-A in HMP2

The report states that E1 Tier-A replicates at 88.2 % sign-concordance. In HMP2, 45 / 51 candidates were CD↑ in both cohorts, including every top-10 candidate (M. gnavus, S. salivarius, S. thermophilus, E. innocuum, S. parasanguinis, E. asparagiformis, I. bartlettii, H. symbiosa, G. pamelaeae, E. ramosum). [src: ibd_phage_targeting] Two top-20 candidates failed to replicate. S. thermophilus failed on effect sign, possibly because of cohort-specific dairy exposure. B. stercoris was non-significant. [src: ibd_phage_targeting] The ecotype framework itself has real cross-study variance (NB04f LOSO ARI 0.113, where LOSO is leave one substudy out and ARI is adjusted Rand index). The report nonetheless holds that the operational Tier-A is externally validated. [src: ibd_phage_targeting]

### Actionable targets (NB05)

NB05 applied the A3–A6 criteria to 71 unique rigor-controlled candidates. It produced 6 actionable targets with total_score ≥ 2.5. [src: ibd_phage_targeting] The scores were:

| Target | Score |
|---|---|
| Hungatella hathewayi (top-scoring) | 4.0 [src: ibd_phage_targeting] |
| Mediterraneibacter gnavus | 3.8 [src: ibd_phage_targeting] |
| Escherichia coli | 3.6 [src: ibd_phage_targeting] |
| Eggerthella lenta | 3.3 [src: ibd_phage_targeting] |
| Flavonifractor plautii | 3.3 [src: ibd_phage_targeting] |
| Enterocloster bolteae | 2.8 [src: ibd_phage_targeting] |

The report associates E. coli with MIBiG Colibactin, Yersiniabactin and Enterobactin. [src: ibd_phage_targeting] Nine Tier-B candidates scored 2.2–2.4. They include S. salivarius with Salivaricin MIBiG matches, E. asparagiformis, V. parvula and S. parasanguinis. They remain candidates, subject to promotion in Pillar 4 on phage availability. [src: ibd_phage_targeting]

### Co-occurrence modules (NB06)

CLR (centered log-ratio) + Spearman + Louvain networks on E1_all, E1_CD, E3_all and E3_CD gave 3–7 modules per subnet. [src: ibd_phage_targeting] In every subnet, 4–5 of the 6 actionable Tier-A candidates co-clustered into a single "pathobiont module" of 57–84 nodes. [src: ibd_phage_targeting] The report concludes that multi-target phage cocktails are ecologically appropriate for the members of this module. [src: ibd_phage_targeting] F. plautii and E. coli show ecotype-specific module membership. The report flags this as relevant to per-patient cocktail specificity in Pillar 5. [src: ibd_phage_targeting] It suggests that module-anchor commensals (Butyricicoccus pullicaecorum, Anaerostipes caccae, and Lactococcus lactis in E3) may give functional-driver context for Pillar 3. [src: ibd_phage_targeting]

### H3 falsifiability framework

Twelve Pillar 3 notebooks test the H3 framework across pathway, BGC (biosynthetic gene cluster), metabolite, strain and serology granularities. They also include a multi-omics joint-factor pilot. [src: ibd_phage_targeting] The report states that all 8 H3 sub-hypotheses were tested with formal verdicts. [src: ibd_phage_targeting] It scores them as 5 SUPPORTED + 1 PARTIALLY SUPPORTED + 2 PARTIAL + 1 NOT SUPPORTED. [src: ibd_phage_targeting] That tally sums to nine, and the table below has nine rows. The report's own list for the "8" names H3a a/c, H3a b v1.8, H3a-new, H3b, H3c, H3d-DA, H3d-clust and H3e, which is nine verdict entries. [src: ibd_phage_targeting] The cited claims do not explain the difference. It most likely comes from H3a being counted as one sub-hypothesis with three parts, but this is an inference, not something the report states.

| Sub-hypothesis | Notebook | Verdict and key figures |
|---|---|---|
| H3a (a): CD-vs-nonIBD pathway differential abundance against a permutation null | NB07a | Supported. 52 CD-up MetaCyc pathways, perm-null mean 0.077 [src: ibd_phage_targeting] |
| H3a (b): CD-up pathways concentrate in IBD-mechanism class themes | NB07_v1.8 | Supported. Iron/heme is the dominant theme, OR=8.1 (FDR 7e-6) [src: ibd_phage_targeting] |
| H3a (c): pathway-pathobiont attribution recapitulates known biology | NB07a | Supported. 137 pairs at \|ρ_meta\|>0.4 [src: ibd_phage_targeting]; heme↔E. coli ρ=0.640 [src: ibd_phage_targeting] |
| H3a-new: module-anchor commensal × pathobiont metabolic coupling | NB07c + NB09c | PARTIAL, reframed as shared-environment coupling [src: ibd_phage_targeting] |
| H3b: Kumbhari strain-adaptation gene content separates disease- from health-adapted strains | NB10a | Supported. IBD-biased adaptation enrichment OR=1.38 (p=2.4e-6) [src: ibd_phage_targeting]; housekeeping depletion OR=0.62 (p=6.4e-20) [src: ibd_phage_targeting] |
| H3c: BGC-encoded inflammatory mediators sit in a minority of Tier-A pathobionts | NB08a | Partially supported. Iron-siderophore OR=44 [src: ibd_phage_targeting]; genotoxin OR=234 [src: ibd_phage_targeting]; both E. coli-only within the Tier-A core |
| H3d-DA: CD-up metabolite signatures concentrate in IBD-relevant chemical classes | NB09a | Supported (50 CD vs 26 nonIBD). Polyamines OR=14.6 [src: ibd_phage_targeting]; long-chain PUFAs (polyunsaturated fatty acids) OR=7.9 [src: ibd_phage_targeting] |
| H3d-clust: metabolite-derived clustering is more stable across cohorts than taxonomy | NB09d | Not supported. Cross-cohort LOSO ARI=0.000, with cohort-batch dominance [src: ibd_phage_targeting] |
| H3e: anti-microbial antibody titers correlate with Tier-A pathobiont abundance | NB11 | PARTIAL. Top \|r\|=0.31 (FDR 0.40) [src: ibd_phage_targeting] |

NB09b provides a cross-cohort metabolomics bridge to FRANZOSA_2019. [src: ibd_phage_targeting] NB09d tests metabolite-feature ecotype stability. [src: ibd_phage_targeting]

### Nulls and what they mean

NB09c rejects cross-feeding. It found only 7 strict triangles, and A. caccae had opposite-sign lactate associations to the pathobionts. [src: ibd_phage_targeting] After the NB09d result, taxonomy remains the primary ecotype framework. [src: ibd_phage_targeting] The report concludes that m/z-bridge metabolite-feature clustering requires batch correction. [src: ibd_phage_targeting] It also concludes that paired sample-level metabolite-metagenomics can disambiguate cross-feeding from shared-environment effects. [src: ibd_phage_targeting]

The two PARTIAL verdicts (H3e, H3a-new) reflect single-cohort data-scope structural caveats, not biological refutation. [src: ibd_phage_targeting] For H3e the single-cohort caveat is structural per plan v1.7. [src: ibd_phage_targeting]

### Multi-omics pilot (NB07d)

NB07d is a multi-omics joint-factor pilot per plan v1.7 N13. It is not formally an H3 hypothesis test. [src: ibd_phage_targeting] Its CCA (canonical correlation analysis) recapitulates the entire CD-vs-nonIBD signal in a single joint factor. [src: ibd_phage_targeting] On HMP2 paired taxonomy and metabolomics, CC1 (r=0.96) jointly captures the species and metabolite signatures from all 8 H3 sub-hypotheses. The report calls this the integrative validation of the H3 framework. [src: ibd_phage_targeting] It describes this as independent rediscovery, since CCA on jointly PCA-transformed modalities differs from the per-modality differential-abundance and correlation tests. [src: ibd_phage_targeting] The report defines CC1 as the operational species- and metabolite-level definition of CD biology in HMP2 for Pillar 4–5 cocktail design. [src: ibd_phage_targeting]

See also [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]] and [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

## Executive Summary: Pillar 3 deliverables (this report) (2)

This part of the report covers the Pillar 3 hypothesis tests (H3a–H3e). Most were supported or partly supported. Several results are limited by ontology choice, single-cohort data or strict thresholds. [src: ibd_phage_targeting]

### H3a: pathways and ontology choice

H3a (a + c) is supported. Within-IBD-substudy Crohn's disease (CD) versus nonIBD pathway differential abundance gives 52 CD-up MetaCyc pathways (false discovery rate FDR<0.10, |effect|>0.5), with permutation null mean 0.077. [src: ibd_phage_targeting] There are 137 pathway–pathobiont attribution pairs at |ρ_meta|>0.4. The top hit is heme biosynthesis (PWY-5920) with *Escherichia coli* at ρ=0.640. The report says this recapitulates adherent-invasive *E. coli* (AIEC) biology. [src: ibd_phage_targeting]

The H3a (b) verdict depends on the ontology. The v1.7 regex-on-pathway-names test gave FAIL-degenerate. [src: ibd_phage_targeting] The v1.8 test used the ModelSEEDDatabase MetaCyc class hierarchy, which covers 90 % of 575 HUMAnN3 pathways. [src: ibd_phage_targeting] It supported H3a (b). Iron/heme acquisition was the dominant CD-up theme (OR=8.1, FDR 7e-6; 15 of 52 CD-up pathways). [src: ibd_phage_targeting] Two further enrichments appeared: *Hungatella hathewayi* purine/pyrimidine recycling (OR=4.9) and trimethylamine (TMA)/choline (OR=9.3). [src: ibd_phage_targeting] The report states: "Same data, opposite verdict — driven by ontology choice", and encodes the lesson as plan norm N17. [src: ibd_phage_targeting] See [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]].

### Anaerostipes caccae coupling: cross-feeding rejected

NB07c first found species-level Spearman correlations of *A. caccae* with pathobionts in E1_CD. These were ρ=+0.39 with *Enterocloster bolteae*, +0.33 with *H. hathewayi*, +0.31 with *Mediterraneibacter gnavus* and +0.29 with *Flavonifractor plautii*. They were initially consistent with butyrogenic cross-feeding. [src: ibd_phage_targeting] NB09c paired-sample disambiguation rejected that reading. It found only 7 strict triangles, and lactate associated with the opposite sign for *A. caccae* versus the pathobionts. [src: ibd_phage_targeting] The report reframes the coupling as shared-environment co-occurrence in healthy/normobiotic samples. [src: ibd_phage_targeting] See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

### H3b: strain adaptation (NB10a)

H3b is supported. NB10a analyzed 23,579 FDR<0.10 Kumbhari strain-adaptation genes across 59 species. [src: ibd_phage_targeting] IBD-biased genes are 1.38× enriched for adaptation functions (mucin/glycan, two-component signaling, antibiotic resistance, virulence; OR=1.38, p=2.4e-6). [src: ibd_phage_targeting] They are 0.62× depleted for housekeeping (OR=0.62, p=6.4e-20), so the strict housekeeping-domination falsifiability bound is rejected. [src: ibd_phage_targeting] *F. plautii* has 0 FDR-passing genes. The report reads this informative null as confirming species-abundance-mediated CD association, which corroborates the NB07b within-carrier analysis. [src: ibd_phage_targeting]

### H3c: biosynthetic gene clusters (NB08a)

H3c is partially supported. BGC-theme Fisher enrichments are iron_siderophore OR=44.4 (FDR 6e-56), genotoxin_microcin OR=234 (FDR 3e-35) and NRPS-PKS-hybrid OR=1.5 (FDR 0.04). [src: ibd_phage_targeting] Among Tier-A core species, *E. coli* alone carries the iron-plus-genotoxin signature. [src: ibd_phage_targeting] It has 54 iron MIBiG hits (19 Yersiniabactin, 16 Enterobactin, 19 siderophore-class) and 25 genotoxin hits (8 Colibactin, 15 Microcin B17). [src: ibd_phage_targeting] Five of the 6 Tier-A core species have CD-up CB-ORF rates above background. [src: ibd_phage_targeting] ebf/ecf RPKM is CD-up across 4 cohorts at p<1e-31, which replicates Elmassry 2025. [src: ibd_phage_targeting] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

### H3d: metabolites (NB09a, NB09b, NB09c)

H3d-DA is supported. In HMP2, 52 of 579 named metabolites pass subject-level differential abundance (50 CD vs 26 nonIBD subjects). [src: ibd_phage_targeting] Two themes are Fisher-significant: polyamines (OR=14.6; putrescine, N1-acetylspermine, N-acetylputrescine, anserine and diacetylspermine all CD-up) and long-chain polyunsaturated fatty acids (PUFAs; OR=7.9; arachidonate, adrenate, DHA, DPA and EPA all CD-up). [src: ibd_phage_targeting] Tauro-α/β-muricholate and free taurine are CD-up. The report says this corroborates the *F. plautii* 7α-dehydroxylation deficit at metabolite level. [src: ibd_phage_targeting]

At sample level, NB09c computed Spearman ρ over 468 paired CSM* HMP2 samples × 8 species × 583 metabolites. [src: ibd_phage_targeting] *F. plautii*, *Eggerthella lenta* and *E. bolteae* show the predicted substrate-product signature. It is negative with primary tauro-bile acids and positive with secondary bile acids. [src: ibd_phage_targeting] *M. gnavus* and *E. coli* show the opposite pattern. [src: ibd_phage_targeting] *E. coli* dominates cohort-level correlations (cadaverine +0.45, choline +0.25, tryptophan +0.25). [src: ibd_phage_targeting] See [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]].

NB09b bridged HMP2 to FRANZOSA_2019 by m/z (±0.005 Da). This mapped 122 of 592 named HMP2 metabolites to Franzosa peaks, and 118 were testable. [src: ibd_phage_targeting] Three themes replicate at ≥75 % sign-concordance. [src: ibd_phage_targeting]

- Urobilin/porphyrin: 100 % sign-concordance, n=3, median Franzosa cliff −0.747, the strongest replicated effect. [src: ibd_phage_targeting]
- Acyl-carnitines: 80 %, n=5, median Franzosa cliff +0.531. [src: ibd_phage_targeting]
- Long-chain PUFAs: 75 %, n=12, median Franzosa cliff +0.273. [src: ibd_phage_targeting]

Bile-acid sign-concordance is lower: primary 57 % and secondary 40 %. Cohort-aggregate bile-acid differential abundance is weaker than the NB09c paired sample-level evidence. [src: ibd_phage_targeting] Polyamines cannot be bridged by m/z because of the low-mass HILIC-pos gap. The HMP2 polyamine OR=14.6 therefore stands as a single-cohort finding. [src: ibd_phage_targeting] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

### H3e: serology (NB11)

H3e is only partial at the strict threshold. NB11 ran 48 assay–species tests across 67 HMP2 subjects, using site-adjusted partial Pearson r. [src: ibd_phage_targeting] No pair clears |r|>0.40 with FDR<0.10. [src: ibd_phage_targeting] The top pair is ANCA (anti-neutrophil cytoplasmic antibody) with *M. gnavus* at +0.31 (FDR 0.40). [src: ibd_phage_targeting] The cohort sanity check passes, because ANCA-UC, ASCA-CD and CBir1-CD all match the canonical direction. [src: ibd_phage_targeting] Single-site r reaches +0.46 at Harvard, but cohort aggregation pulls the association toward null. [src: ibd_phage_targeting] The report treats the single-cohort caveat as structural. [src: ibd_phage_targeting] It concludes that serology is usable as a CD-versus-UC stratifier but not as a per-target abundance predictor. [src: ibd_phage_targeting]

## Executive Summary: Pillar 3 closure synthesis — two cross-corroborated mechanism …

The joint factor pilot succeeded, and the report says its first factor recapitulates all Pillar 3 mechanism narratives. [src: ibd_phage_targeting] The report counts two independent six-line cross-corroboration narratives. [src: ibd_phage_targeting]

### Metabolomics clustering across cohorts

NB09b reports 9 strict cross-cohort metabolomics replications. [src: ibd_phage_targeting] The hypothesis H3d-clust was not supported in NB09d. Pooled HMP2 and Franzosa K=4 K-means on 326 subjects × 111 m/z-bridge features gave cohort-driven clusters, not diagnosis-driven ones. [src: ibd_phage_targeting] PC1 (principal component 1) explained 79 % of variance and separated HMP2 from Franzosa cleanly. [src: ibd_phage_targeting] Cross-cohort LOSO (leave one substudy out) ARI (adjusted Rand index) was 0.000, far below the 0.113 taxonomic baseline from NB04f. [src: ibd_phage_targeting] The within-pooled bootstrap ARI of 0.937 is misleading, because it measures cohort-batch reproducibility and not biology. [src: ibd_phage_targeting]

The report's methodological lesson is that m/z-bridge metabolomics needs explicit batch correction (ComBat/SVA/RUV) for cross-cohort clustering. [src: ibd_phage_targeting] The taxonomic NB01b consensus K=4 ecotype framework therefore stays the primary ecotype basis for cocktail design. [src: ibd_phage_targeting] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

### Joint factor pilot (NB07d)

The NB07d pilot succeeded. A 2-modality CCA (canonical correlation analysis) on paired HMP2 CSM* subjects, using taxonomy and metabolomics, gave 4 canonical pairs at r=0.89-0.96. [src: ibd_phage_targeting] Pathways were left out because they are not in the mart. [src: ibd_phage_targeting]

CC1 has canon r=0.96 and a CD-vs-nonIBD cliff of +0.50 (p=4e-4). The report says it is a single joint factor that recapitulates all Pillar 3 mechanism narratives. [src: ibd_phage_targeting] All 6 actionable Tier-A core species load CD-positive on it. [src: ibd_phage_targeting] Its metabolite loadings include urobilin CD-down, polyamines, PUFAs, cadaverine associated with Escherichia coli, linoleoyl/palmitoyl ethanolamides and secondary bile-acid depletion. [src: ibd_phage_targeting] The report says NB07d independently rediscovers the NB06 H2d pathobiont module structure as one principal direction in joint species-metabolite space. [src: ibd_phage_targeting]

### Two six-line cross-corroboration narratives

After eight Pillar 3 notebooks, the report counts two independent six-line narratives (Novel Contribution #17). Each shows one biological claim at several analytical granularities. [src: ibd_phage_targeting]

**Iron / AIEC (adherent-invasive E. coli) narrative.** The report's six lines are:
- NB05 matches E. coli to Yersiniabactin, Enterobactin and Colibactin in MIBiG. [src: ibd_phage_targeting]
- NB07a links heme biosynthesis to E. coli at ρ=0.640 at sample level. [src: ibd_phage_targeting]
- NB07 v1.8 finds the iron/heme MetaCyc-class theme dominant among CD-up pathways (OR=8.1, FDR 7e-6). [src: ibd_phage_targeting]
- NB07c finds iron-pathway covariation concentrated on E. coli, with mean ρ=0.45 vs 0.13 for Anaerostipes caccae. [src: ibd_phage_targeting]
- NB08a finds iron-siderophore BGCs 44× enriched in Tier-A core, driven entirely by E. coli's 54 iron MIBiG BGCs. [src: ibd_phage_targeting]
- The literature line cites Dalmasso 2021, Prudent 2021, Dogan 2014, Veziant 2016 and Dubinsky 2022. [src: ibd_phage_targeting]

See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

**Bile-acid 7α-dehydroxylation narrative.** The report names F. plautii, E. lenta and E. bolteae as active 7α-dehydroxylating species in the CD pathobiont module. [src: ibd_phage_targeting] Its six lines are below. The NB09c line is given as three species-level associations.
- NB05 places all three in actionable Tier-A. [src: ibd_phage_targeting]
- NB07b finds F420-bile-acid metabolism among within-carrier CD-up biosynthesis pathways in F. plautii. [src: ibd_phage_targeting]
- NB09a finds tauro-α/β-muricholate and free taurine CD-up at subject level, read as substrate-pool elevation. [src: ibd_phage_targeting]
- NB09c paired samples give F. plautii × cholate ρ=−0.26 and × lithocholate ρ=+0.15. [src: ibd_phage_targeting] They give E. bolteae × deoxycholate ρ=+0.17 and × lithocholate ρ=+0.18. [src: ibd_phage_targeting] They give E. lenta × ketodeoxycholate ρ=−0.14. [src: ibd_phage_targeting]
- NB10a finds 0 FDR-passing strain-adaptation genes for F. plautii. The report reads this informative null as a species-abundance-mediated mechanism with no within-species escape route through gene-content selection. [src: ibd_phage_targeting]
- The literature line cites Franzosa 2019 and Devlin & Fischbach 2015 (bai operon). [src: ibd_phage_targeting]

See [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]].

### Per-species target prioritization

| Species | Tier-A score | Report's priority and notes |
|---|---|---|
| Hungatella hathewayi | 4.0 | Tier-1; no iron specialization, not in bile-acid network, species-abundance plus within-carrier biosynthesis-up/sugar-down; low BA cost, broad targeting OK [src: ibd_phage_targeting] |
| Mediterraneibacter gnavus | 3.8 | Tier-1; no iron specialization, not in network; low BA cost; mucin-degradation mechanism well characterized [src: ibd_phage_targeting] |
| Escherichia coli | 3.6 | Tier-1 with strain-resolution requirement; dominant iron specialization; low BA cost [src: ibd_phage_targeting] |
| Flavonifractor plautii | 3.3 | Tier-2; weak iron specialization; highest BA-coupling cost [src: ibd_phage_targeting] |
| Eggerthella lenta | 3.3 | Tier-2; moderate BA-coupling cost [src: ibd_phage_targeting] |
| Enterocloster bolteae | 2.8 | Tier-2; moderate BA-coupling cost; mixed mediation [src: ibd_phage_targeting] |

- For M. gnavus, NB10a found no Kumbhari signal, so the report labels its mechanism species-abundance-mediated. It is described as a mucin-glucorhamnan producer per Henke 2019. [src: ibd_phage_targeting]
- E. coli's action is strain-content-mediated and specific to the AIEC subset. The report says to target the pks/Yersiniabactin/Enterobactin-positive AIEC subset specifically. [src: ibd_phage_targeting]
- For F. plautii, the report states that depletion shifts the bile-acid pool toward inflammatory primary tauro-conjugated forms. It suggests considering UDCA (ursodeoxycholic acid) or a bile-acid-binding agent. [src: ibd_phage_targeting]
- For E. lenta, the action is drug-metabolism-mediated (Koppel 2018 Cgr2), with NB08a CB-ORF CD-DOWN 54%. Its primary CD association is non-BGC, so strain resolution may not be required. [src: ibd_phage_targeting]

See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

### Phage-design framework for Pillars 4–5

The report lays out a four-step framework.
1. Assign each patient an ecotype from stool MetaPhlAn3 projection (E0, E1 or E3). E2 is absent in active CD. [src: ibd_phage_targeting]
2. Build per-ecotype Tier-A target lists. E1_CD module 0 has H. hathewayi, F. plautii, E. bolteae, E. lenta and M. gnavus. [src: ibd_phage_targeting] E3_CD module 1 has E. lenta, H. hathewayi, E. coli and M. gnavus. [src: ibd_phage_targeting] F. plautii is E1-specific and E. coli is E3-specific. [src: ibd_phage_targeting]
3. Match Tier-1 and Tier-2 candidates to available phages in PhageFoundry and external phage databases. E. coli AIEC has direct phage-therapy precedent (Galtier 2017). [src: ibd_phage_targeting]
4. Draft per-patient cocktails for the UC Davis 23 patients. Each draft combines ecotype, Tier-A profile, bile-acid coupling cost and medication harmonization. [src: ibd_phage_targeting]

Patient 6967's longitudinal E1 ↔ E3 shift is the central per-patient stability test. [src: ibd_phage_targeting] The report concludes that the H3 framework plus the CC1 pilot give Pillar 5 a mechanistically grounded multi-attribute decision framework, not a single-axis Tier-A score. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

## Executive Summary: Pillar 4 deliverables (this report)

This part of the report delivers Pillar 4. Three notebooks (NB12, NB13, NB14) build a 3-layer phage-evidence stack of curated literature, experimental susceptibility and in-vivo phageome data for the 6 actionable Tier-A core pathobionts. The stack feeds a cocktail-design framework. [src: ibd_phage_targeting] Pillar 5 notebooks NB15 and NB16 then apply it per patient. [src: ibd_phage_targeting] The evidence is a mix of literature curation, one experimental dataset (E. coli only) and modest correlations.

### Layer 1: curated literature (NB12)

NB12 scores phage availability from 0 to 3 for 12 organisms, using ref_phage_biology, a literature-curated synthesis from indicator_taxa_literature_review. [src: ibd_phage_targeting] It sorts the actionable Tier-A species into four classes:
- Clinical-trial-stage: 1 species, Escherichia coli EcoActive. [src: ibd_phage_targeting]
- Lytic-literature: 2 species, Eggerthella lenta PMBT5 and Enterocloster bolteae PMBT24. [src: ibd_phage_targeting]
- Temperate-only: 1 species, Mediterraneibacter gnavus, with 6 temperate phages. [src: ibd_phage_targeting]
- Gap: 2 species, Hungatella hathewayi and Flavonifractor plautii. [src: ibd_phage_targeting]

### Layer 2: experimental susceptibility (NB13)

NB13 uses the KBase Data Lakehouse phagefoundry_strain_modelling dataset. It holds 96 phages × 188 E. coli strains × 17,672 experimentally tested susceptibility pairs (Gaborieau 2025-10-02). [src: ibd_phage_targeting] The susceptibility rate is 22 %. [src: ibd_phage_targeting] Greedy minimum-set-cover gives a 5-phage cocktail covering 94.7 % of the 188 strains: DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2 and LF110_P2. The report calls it comparable in size to the 7-phage EcoActive clinical-trial cocktail. [src: ibd_phage_targeting]

Of 94 phages, 65 (69 %) were isolated against B2/D phylogroup hosts, described as predominantly AIEC (adherent-invasive E. coli). [src: ibd_phage_targeting] Top phages include isolates against the canonical AIEC reference strains LF82, LF73 and 536. [src: ibd_phage_targeting] 26 strains (14 %) are resistant at ≤5 % susceptibility and are escape candidates. [src: ibd_phage_targeting] This layer covers E. coli only. The other five targets are absent from the PhageFoundry collection. [src: ibd_phage_targeting]

### Layer 3: in-vivo phageome (NB14)

NB14 joins 3,039 HMP2 viromics rows across 630 samples that have NB04h ecotype calls, a 97 % overlap. [src: ibd_phage_targeting] Gokushovirus WZ-2015a is lower in Crohn's disease (CD) across ecotypes. In E1 the cliff value is -0.358 with FDR (false discovery rate) 5e-7, n_CD=231 versus n_HC=125. This is consistent with Norman 2015 and Clooney 2019 on Microviridae depletion. [src: ibd_phage_targeting] E. coli correlates with Podoviridae (Spearman +0.18) and Myoviridae (+0.13). The report reads these as endogenous E. coli phage carriage by T7-like and T4-like Caudovirales. [src: ibd_phage_targeting] All in-vivo correlations have |ρ|≤0.18, a modest signal relative to the species-level CD axis. [src: ibd_phage_targeting] H. hathewayi and M. gnavus correlate negatively with the dominant "Unknown" phage family. [src: ibd_phage_targeting] The VirMAP family-classification gap is 80 % of observations, which limits family-level reading. [src: ibd_phage_targeting]

### Per-target tiers and convergence

The report treats agreement of the three independent evidence types on the same per-target classification as the Pillar-4 rigor signal. [src: ibd_phage_targeting]

| Target | Evidence | Tier |
|---|---|---|
| E. coli AIEC | EcoActive; 5-phage cocktail at 95 % strain coverage; 65/94 AIEC-relevant phylogroup; +0.18 Podoviridae, +0.13 Myoviridae | Tier-1, high confidence, all 3 layers aligned [src: ibd_phage_targeting] |
| E. lenta | PMBT5 siphovirus literature; not in PhageFoundry; no detectable in-vivo correlation | Tier-2, feasible with monitoring [src: ibd_phage_targeting] |
| E. bolteae | PMBT24 (Kielviridae, virulent); not in PhageFoundry; +0.12 Myoviridae | Tier-2, feasible with monitoring [src: ibd_phage_targeting] |
| M. gnavus | 6 temperate siphoviruses; not in PhageFoundry; weak in-vivo signal | Limited: temperate-only, alternatives needed [src: ibd_phage_targeting] |
| H. hathewayi | No known phages; not in PhageFoundry; no in-vivo correlation | Gap: external-database query priority [src: ibd_phage_targeting] |
| F. plautii | Not in literature curation or PhageFoundry; no in-vivo correlation | Gap, plus highest bile-acid-coupling cost: alternatives preferred [src: ibd_phage_targeting] |

### Three Pillar-5 design strategies

The 6 actionable targets stratify into 3 design strategies. [src: ibd_phage_targeting]

1. **Direct phage targeting (Tier-1).** E. coli AIEC would use EcoActive precedent or the 5-phage NB13 cocktail. [src: ibd_phage_targeting] This requires a strain-resolution AIEC diagnostic based on pks-island, Yersiniabactin and Enterobactin gene presence. [src: ibd_phage_targeting]
2. **Targeting with monitoring (Tier-2).** E. lenta (PMBT5) and E. bolteae (PMBT24) are targeted with bile-acid pool monitoring. [src: ibd_phage_targeting] M. gnavus is possible only if lytic-locked phage engineering succeeds. [src: ibd_phage_targeting]
3. **Alternatives.**
   - H. hathewayi is the top priority for INPHARED and IMG/VR searches. If no phages are found, the fallback is GAG-degrading enzyme inhibitors. [src: ibd_phage_targeting]
   - F. plautii has the lowest priority because of its bile-acid-coupling cost. The report suggests co-administering UDCA (ursodeoxycholic acid) or a bile-acid-binding agent instead. [src: ibd_phage_targeting]
   - M. gnavus would use biochemical glucorhamnan-synthesis inhibitors (Henke 2019) if lytic-locked engineering fails. [src: ibd_phage_targeting]

### Ecotype implications in UC Davis

- E0 is 27 % of the cohort. It has minimal pathobiont burden and possibly needs no cocktail. [src: ibd_phage_targeting]
- E1 is 42 %. It is the dominant CD ecotype, and the full cocktail (E. coli AIEC, Tier-2 E. bolteae and E. lenta, bile-acid monitoring) is appropriate. [src: ibd_phage_targeting]
- E3 is 31 %. It is severely Bacteroides-expanded, with prominent E. coli and M. gnavus. Ecological-cost annotation is more critical because of the higher pathobiont burden. [src: ibd_phage_targeting]
- Patient 6967 drifts longitudinally between E1 and E3. This is the first central per-patient stability test and suggests ecotype-state-aware dosing. [src: ibd_phage_targeting]

### NB15 per-patient drafts

NB15 profiles 23 UC Davis CD patients using NB02 ecotype, Montreal classification, calprotectin, medication and Kuehl_WGS Tier-A presence. [src: ibd_phage_targeting] NB16 tests longitudinal stability and sets a state-dependent dosing rule. [src: ibd_phage_targeting] Per-target prescribing rates are listed below. E. coli is the lowest, even though it is the only Tier-1 target.

| Target | Prescribing rate |
|---|---|
| M. gnavus | 91 % [src: ibd_phage_targeting] |
| H. hathewayi | 83 % [src: ibd_phage_targeting] |
| E. bolteae | 83 % [src: ibd_phage_targeting] |
| F. plautii | 78 % [src: ibd_phage_targeting] |
| E. lenta | 70 % [src: ibd_phage_targeting] |
| E. coli | 35 % [src: ibd_phage_targeting] |

Per ecotype, E0 (n=7) has a mean of 1.71 targets and 0 patients with concrete phage. [src: ibd_phage_targeting] E1 (n=9) has a mean of 4.89 targets and 9 patients with concrete cocktails. [src: ibd_phage_targeting] E3 (n=6) has a mean of 2.33 targets and 4 patients with concrete phages. [src: ibd_phage_targeting] Mixed-ecotype patient 6967 has 3 targets. [src: ibd_phage_targeting] Overall, 14 of 23 patients (61 %) have concrete phage cocktail drafts. [src: ibd_phage_targeting]

## Executive Summary: Pillar 5 closure synthesis — hybrid cocktail framework + …

This part of the report gives Pillar 5's clinical-translation deliverables: four per-patient design principles [src: ibd_phage_targeting], a stratification of UC Davis Crohn's disease (CD) patients into cocktail-design categories [src: ibd_phage_targeting], a longitudinal case (patient 6967), state-dependent dosing rules, and a per-ecotype workflow. The longitudinal result comes from one patient with two visits. [src: ibd_phage_targeting]

### Why E1 needs a hybrid cocktail

All 9 E1 patients carry the full 5-species Tier-A pathobiont module, but only 3 of the 5 species have direct lytic phage options. Those three are Escherichia coli, Enterocloster bolteae and Eggerthella lenta, "when present". [src: ibd_phage_targeting] The other two, Hungatella hathewayi and Flavonifractor plautii, are Pillar-4 phage-gap species. A pure phage cocktail is therefore structurally infeasible, and the report calls for phages plus non-phage alternatives. [src: ibd_phage_targeting] NB15 proposes direct phages for E. coli, E. bolteae and E. lenta. It proposes alternatives for H. hathewayi and F. plautii, and engineering or biochemical approaches for Mediterraneibacter gnavus. [src: ibd_phage_targeting]

### Flavonifractor plautii: leave alone

The report treats F. plautii as a "leave alone" target despite its NB05 score of 3.3. [src: ibd_phage_targeting] It is present in 78 % of UC Davis patients and in all 9 E1 patients. [src: ibd_phage_targeting] The report gives it the highest bile-acid coupling cost and identifies it as an active 7α-dehydroxylator. [src: ibd_phage_targeting] It is also a phage-gap species absent from ref_phage_biology. [src: ibd_phage_targeting] The report calls this a triple penalty. It advises avoiding F. plautii and using bile-acid-binding co-therapy (ursodeoxycholic acid (UDCA) or cholestyramine) to maintain the secondary bile-acid pool that its depletion would erode. [src: ibd_phage_targeting]

### Escherichia coli and the unmet need

Only 8 of 23 UC Davis patients carry detectable E. coli (35 %). The report contrasts this with the literature framing of adherent-invasive E. coli (AIEC) as the prototypical CD pathobiont. [src: ibd_phage_targeting] The NB13 5-phage AIEC cocktail (DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2, LF110_P2) is directly applicable to about 35 % of patients. [src: ibd_phage_targeting] H. hathewayi (universal 83 %) and M. gnavus (universal 91 %) are both phage gaps and represent the unmet need. [src: ibd_phage_targeting] The report therefore ranks INPHARED and IMG/VR queries for lytic phages of these two species above further refinement of the E. coli cocktail. [src: ibd_phage_targeting]

### Longitudinal case: patient 6967

Patient 6967 is the only multi-timepoint UC Davis CD patient with biological-replicate samples. Patient 1112 instead has 2 resequencing replicates of one biological sample. [src: ibd_phage_targeting] Patient 6967 shows E1→E3 ecotype drift across 2 visits. [src: ibd_phage_targeting] M. gnavus expands 14× (0.53 → 7.45 reads) and dominates the signature. [src: ibd_phage_targeting] E. lenta (3.1×), F. plautii (1.9×), E. bolteae (2.1×) and H. hathewayi (1.3×) also expand. The report reads this as general dysbiosis worsening. [src: ibd_phage_targeting]

Visit 1 (E1) has 5 priority targets, all present. [src: ibd_phage_targeting] Visit 2 (E3) has 3 present. [src: ibd_phage_targeting] E. coli is absent, so 6967 is not an AIEC carrier. [src: ibd_phage_targeting] The cocktail Jaccard between visits is 0.60. The report reads this as moderate overlap that needs non-trivial redesign but not a complete rewrite. [src: ibd_phage_targeting] Patient 1112's replicates give Spearman ρ = 1.000 (p < 0.001) on 6 Tier-A targets. The report treats this as validation of Kaiju reliability for the longitudinal contrast. [src: ibd_phage_targeting]

### State-dependent dosing rules (NB16)

NB16 proposes five rules. [src: ibd_phage_targeting]
- Re-test ecotype every 3-6 months for active CD patients on phage cocktail therapy. [src: ibd_phage_targeting]
- Include F. plautii only in E1, and drop it on an E1→E3 transition. [src: ibd_phage_targeting]
- Include E. coli only in E3, subject to AIEC strain detection, and drop it on an E3→E1 transition. [src: ibd_phage_targeting]
- Use M. gnavus, H. hathewayi and E. lenta as a universal Tier-1 trio. Both ecotypes carry them, so they need no re-evaluation on an ecotype shift. They form the backbone for any active-disease CD patient. [src: ibd_phage_targeting]
- Use M. gnavus qPCR as a candidate cheap proxy for ecotype state. A 5-fold change triggers a full ecotype re-test and avoids metagenomics at every visit. [src: ibd_phage_targeting]

### Per-patient categories and workflow

The report assigns cocktails by ecotype, calprotectin status and E. coli presence, as in the table below. Counts are approximate where the report gives "~". [src: ibd_phage_targeting]

| Group | Patients | Recommendation |
|---|---|---|
| E1, active calprotectin, E. coli present | ~3 | Full Tier-1: NB13 5-phage E. coli cocktail, PMBT24, PMBT5, alternatives for F. plautii, H. hathewayi and M. gnavus [src: ibd_phage_targeting] |
| E1, active calprotectin, no E. coli | ~5 | Tier-2 hybrid: PMBT24, PMBT5, alternatives, and UDCA/BA-binding co-administration for F. plautii [src: ibd_phage_targeting] |
| E1, quiescent | 1-2 | Reserve cocktail for flares; monitor calprotectin and ecotype state [src: ibd_phage_targeting] |
| E0 | 7 | Limited cocktail, because priority targets are phage-gap or temperate; consider non-cocktail strategies [src: ibd_phage_targeting] |
| E3, E. coli present | ~3 | NB13 5-phage E. coli cocktail, PMBT5, alternatives [src: ibd_phage_targeting] |
| E3, no E. coli | ~3 | Limited: E. lenta and H. hathewayi only [src: ibd_phage_targeting] |
| Mixed (6967) | 1 | State-dependent dosing, rebalancing the cocktail at each visit [src: ibd_phage_targeting] |

The workflow starts with stool metagenomics for ecotype assignment. [src: ibd_phage_targeting] E0 patients then get a limited cocktail and flare reserve. [src: ibd_phage_targeting] E1 patients get the full hybrid 3-strategy cocktail. This includes the NB13 E. coli cocktail if AIEC-positive, PMBT24, PMBT5, and alternatives for H. hathewayi and F. plautii. [src: ibd_phage_targeting] E3 patients get a focused cocktail with E. coli if present, PMBT5 and alternatives. [src: ibd_phage_targeting]

### Caveats

The only multi-timepoint patient with biological replicates is 6967, so the drift result comes from one patient with two visits. [src: ibd_phage_targeting] The M. gnavus qPCR trigger is explicitly only a candidate proxy. [src: ibd_phage_targeting]

### Slots Into

- [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]]: the five dosing rules, the per-ecotype workflow and the patient 6967 drift. [src: ibd_phage_targeting]
- [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]]: F. plautii is deprioritized and H. hathewayi and M. gnavus are the unmet targets. [src: ibd_phage_targeting]
- [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]]: only 3 of the 5 E1 module species have direct lytic phage options. [src: ibd_phage_targeting]
- [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]]: the F. plautii bile-acid coupling cost motivates UDCA/cholestyramine co-therapy. [src: ibd_phage_targeting]

## Executive Summary: Pillar 5 closure capstone (NB17) — cross-cutting synthesis

This part of the report closes Pillar 5. It consolidates Pillars 1-5 into three clinical-translation artifacts: a per-patient master table, a target decision matrix and a roadmap with a final verdict. [src: ibd_phage_targeting] It yields concrete phage cocktail drafts for 14 of 23 UC Davis CD patients (CD = Crohn's disease). [src: ibd_phage_targeting] The evidence is a computational integration within plan v1.9, which has no raw reads. [src: ibd_phage_targeting]

### Per-patient master table and cocktail categories

The master table covers all 23 UC Davis CD patients. It combines ecotype, Montreal classification, calprotectin, medication, Tier-A presence, design category, cocktail strategy and longitudinal status. [src: ibd_phage_targeting] Twelve patients fall in reserve-for-flare category C. These patients have calprotectin below 250 or unmeasured. They get no active cocktail, only calprotectin monitoring plus M. gnavus qPCR. They carry the same Tier-A panel as the active patients, held in reserve. [src: ibd_phage_targeting] The other 11 patients fall into five design groups: [src: ibd_phage_targeting]

| Category | Patients | Strategy |
|---|---|---|
| E1 hybrid 3-strategy (no E. coli) | 4 | PMBT24, PMBT5, alternatives for H. hathewayi, F. plautii and M. gnavus, and UDCA/BA-binding [src: ibd_phage_targeting] |
| E0 limited (priority targets are GAP) | 4 | Limited cocktail; consider non-phage strategies [src: ibd_phage_targeting] |
| E1 hybrid 3-strategy (full, with E. coli AIEC) | 1 | NB13 5-phage E. coli cocktail, PMBT24, PMBT5, alternatives, UDCA [src: ibd_phage_targeting] |
| E3 focused (with E. coli) | 1 | NB13 5-phage E. coli cocktail, PMBT5, alternatives [src: ibd_phage_targeting] |
| State-dependent dosing | 1 | Patient 6967: cocktail rebalances on E1↔E3 ecotype shifts [src: ibd_phage_targeting] |

### Target decision matrix

The matrix maps 6 actionable Tier-A targets across 5 attributes to a final priority class. The attributes are NB05 score, ecotype membership, BA-coupling cost, mediation mode and phage tier. [src: ibd_phage_targeting]

| Target | NB05 score | Ecotype | BA cost | Phage tier | UC Davis prevalence | Priority |
|---|---|---|---|---|---|---|
| H. hathewayi | 4.0 | E1+E3 | none | GAP | 83 % | Tier-1 phage GAP; INPHARED/IMG-VR query priority [src: ibd_phage_targeting] |
| M. gnavus | 3.8 | E1+E3 | none | temperate-only | 91 % | Tier-1 limited; lytic-locked engineering or biochemical glucorhamnan target [src: ibd_phage_targeting] |
| E. coli | 3.6 | E3-specific | none | clinical-trial | 35 % | Tier-1 phage with strain resolution; NB13 5-phage cocktail; AIEC diagnostic required [src: ibd_phage_targeting] |
| E. lenta | 3.3 | universal Tier-1 | moderate | lytic (PMBT5) | 70 % | Tier-2 phage; PMBT5 with BA monitoring [src: ibd_phage_targeting] |
| F. plautii | 3.3 | E1-specific | HIGHEST | GAP | 78 % | Tier-2 deprioritize; triple penalty; UDCA/BA-binding co-therapy [src: ibd_phage_targeting] |
| E. bolteae | 2.8 | E1+E3 | moderate | lytic (PMBT24) | 83 % | Tier-2 phage; PMBT24 with BA monitoring [src: ibd_phage_targeting] |

AIEC means adherent-invasive Escherichia coli.

The report says the matrix exposes the structural shape of the translation problem. The 2 highest-NB05-scored species, H. hathewayi and F. plautii, are both Pillar-4 GAP. [src: ibd_phage_targeting] E. coli has the most complete phage precedent but is the rarest target in UC Davis, at 35 % carriage. [src: ibd_phage_targeting] M. gnavus is near-universal but has only temperate phage options. [src: ibd_phage_targeting] The report recommends deprioritizing F. plautii despite its NB05-actionable status, because of the triple penalty. [src: ibd_phage_targeting]

### Follow-up workflow

Follow-up visits are proposed every 3-6 months. Calprotectin assesses disease activity. M. gnavus qPCR serves as an inexpensive ecotype-state indicator. [src: ibd_phage_targeting] The workflow then branches on the ecotype result:
- E1 → E3: drop F. plautii and consider adding an E. coli cocktail. [src: ibd_phage_targeting]
- E3 → E1: add an F. plautii alternative and reassess E. coli targeting. [src: ibd_phage_targeting]
- Stable ecotype: continue the current cocktail. [src: ibd_phage_targeting]

### Roadmap and thesis

The roadmap has four tiers:
- **Immediate (current cohort):** the roadmap lists as already delivered 23 patient cocktail drafts, the F. plautii BA-cost annotation, a 4-category stratification, and 5 state-dependent dosing rules plus a clinical workflow. [src: ibd_phage_targeting] The report's claims do not state how these 23 drafts relate to the 14 of 23 patients with concrete phage cocktail drafts. [src: ibd_phage_targeting]
- **Near-term (6–12 months):** INPHARED and IMG/VR queries for 3 GAP species, an AIEC strain-resolution diagnostic, and M. gnavus qPCR validation. [src: ibd_phage_targeting]
- **Mid-term (12–24 months):** a targeted qPCR ecotype panel, a per-patient bile-acid panel, a multi-cohort serology meta-analysis, and longitudinal sampling beyond patient 6967. [src: ibd_phage_targeting]
- **Long-term (24+ months):** a hybrid 3-strategy cocktail clinical pilot, lytic-locked phage engineering for M. gnavus, and GAG-degrading enzyme inhibitor screening for H. hathewayi. [src: ibd_phage_targeting]

The final thesis calls Crohn's disease at the gut-microbiome level a single principal-direction phenomenon (NB07d CC1 r=0.96). [src: ibd_phage_targeting] Within it, 6 actionable Tier-A pathobionts and 2 cross-corroborated mechanism narratives define a state-dependent, hybrid-cocktail design framework. The two narratives are iron acquisition and bile-acid 7α-dehydroxylation. [src: ibd_phage_targeting] The report declares all 5 pillars closed and the central science question answered within plan v1.9 scope. [src: ibd_phage_targeting] The verdict file also holds per-pillar verdicts, a 24 NC index and the roadmap. [src: ibd_phage_targeting]

### Caveats

- External INPHARED (~25K phages) and IMG/VR (~3M UViGs) queries for the 3 gut-anaerobe coverage gaps remain out-of-scope follow-ups. The gaps are H. hathewayi, M. gnavus lytic alternatives and F. plautii. [src: ibd_phage_targeting]
- The state-dependent dosing rule rests on a single patient trajectory (n=1, patient 6967). [src: ibd_phage_targeting]
- Multi-cohort prospective validation of that rule and per-patient AIEC strain-resolution diagnostics are flagged as required clinical-translation prerequisites in the Near-term tier. [src: ibd_phage_targeting]

## Key Findings: UC Davis CD patients span three ecotypes, none in E2

This part of the report trains two ecotype models on a large pooled metagenome set, picks K = 4 and projects the UC Davis Crohn's disease (CD) cohort onto the result. It then tests whether clinical covariates can replace metagenomics. The ecotypes are reproducible only modestly across methods. The clinical classifier looks good on paper but fails per patient. [src: ibd_phage_targeting]

### Training and choice of K = 4

The report trained on 8,489 MetaPhlAn3 samples from fact_taxon_abundance (CMD_HEALTHY + CMD_IBD cohorts). It used two independent methods, LDA on pseudo-counts and GMM (Gaussian mixture model) on CLR (centered log-ratio) + PCA-20, across K ∈ {2..8}. [src: ibd_phage_targeting] LDA held-out perplexity and GMM BIC fall monotonically with K, so they cannot choose K. [src: ibd_phage_targeting] The discriminating signal is cross-method ARI (adjusted Rand index) between LDA and GMM. It peaks locally at K = 4 (ARI = 0.131) and again at K = 7 (0.140). [src: ibd_phage_targeting] A parsimony rule, the smallest K within 0.02 ARI of the maximum, selects K = 4. [src: ibd_phage_targeting] Per-sample agreement between the methods at K = 4 is only 48.9 %. [src: ibd_phage_targeting]

### The four ecotypes

| Ecotype | n | Defining abundances | Diagnosis pattern |
|---|---|---|---|
| E0 diverse commensal | 3,604 | F. prausnitzii 6.8 %, R. bromii 4.5 %, B. uniformis 4.6 %, P. vulgatus 4.4 % | 66.8 % of HC (healthy controls) [src: ibd_phage_targeting] |
| E1 Bacteroides2 transitional | 2,601 | P. vulgatus 9.8 %, B. uniformis 7.2 %, Phocaeicola dorei 3.5 % | 48 % CD, 58 % UC, 100 % T1D, 97 % T2D, 67 % nonIBD [src: ibd_phage_targeting] |
| E2 Prevotella copri enterotype | 920 | P. copri 28 %, F. prausnitzii 6 % | 16.9 % HC, ~0 % disease (non-Western healthy) [src: ibd_phage_targeting] |
| E3 severe Bacteroides-expanded | 1,364 | P. vulgatus 14.2 %, B. fragilis 3.6 % | 50 % CD, 40 % UC, 67 % IBD acute, 38 % CDI, donor 2708 [src: ibd_phage_targeting] |

The report regards H1a (at least 3 reproducible ecotypes) as directionally supported. [src: ibd_phage_targeting] It maps E0, E1, E2 and E3 recognizably onto the Bacteroides / Prevotella / Ruminococcus enterotype framework. It reads E1 and E3 as the Bacteroides2 low-cell-count dysbiosis signature documented in CD by Vandeputte et al. 2017. [src: ibd_phage_targeting]

### Projection of the UC Davis cohort

All 26 Kuehl_WGS samples (23 unique patients) projected onto the K = 4 reference through the synonymy layer. [src: ibd_phage_targeting] For this, 262 unique Kaiju-classified species were normalized to 97 canonical species in the training feature space. [src: ibd_phage_targeting] See [[entities/uc-davis-kuehl-wgs-crohn-s-disease-cohort]] for the cohort.

The samples fell as follows: E0, 7 (27 %); E1, 11 (42 %); E2, 0; E3, 8 (31 %). [src: ibd_phage_targeting] The distribution differs from uniform (χ²(3) = 10.0, p = 0.019). [src: ibd_phage_targeting] The report describes the cohort as Western-looking, with no E2 patients and 73 % in E1 or E3. [src: ibd_phage_targeting] It regards H1b as directionally supported, because patients spread across several ecotypes. This supports the premise of stratified targeting. [src: ibd_phage_targeting]

Longitudinal patients were mostly stable. Patient 1112 was E3 at both timepoints, p1/p1reseq was E3 in both, and p2 was E1 in both. [src: ibd_phage_targeting] Patient 1460 (calprotectin 7,280 μg/g) was assigned E1. [src: ibd_phage_targeting] Patient 6967 flipped between E1 and E3 across two samples. The report calls this its first direct observation of intra-patient ecosystem instability, relevant to dosing schedules (H5d). [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

### Method robustness

LDA on pseudo-counts is robust to the projection mismatch. 54 % of Kuehl feature rows fall outside the training feature space, and LDA treats them as not detected. [src: ibd_phage_targeting] GMM on CLR + PCA is fragile. The same sparsity forces all 26 Kuehl samples into a single Gaussian (E3) at confidence > 0.97, which the report calls an artifact, not biology. [src: ibd_phage_targeting] LDA is therefore the primary Kuehl projection call and GMM is advisory. [src: ibd_phage_targeting]

### Clinical-covariate classifiers (H1c)

The report trained two LightGBM classifiers on the pooled CMD cohort to predict the K = 4 consensus ecotype from clinical covariates. [src: ibd_phage_targeting] The minimal classifier uses is_ibd, sex and age (n = 8,489) and reaches macro OvR AUC (area under curve) = 0.799. [src: ibd_phage_targeting] The extended classifier adds hbi_max, sccai_max and calp_max (n = 1,675 subset) and reaches macro AUC = 0.810. [src: ibd_phage_targeting] Both exceed the H1c threshold of 0.70, so H1c nominally passes. [src: ibd_phage_targeting]

Per patient, the classifiers fail on UC Davis. The minimal classifier agrees with the metagenomic call for 41 % of patients (9/22). The extended classifier agrees for 36 % (8/22). [src: ibd_phage_targeting] Twelve of 22 patients disagree under both classifiers. [src: ibd_phage_targeting] The minimal classifier predicts E1 for 19/22 patients. [src: ibd_phage_targeting]

The report gives these reasons:
- In the training cohort, IBD samples split ~58 % E1 / ~40 % E3 / ~2 % E0 / ~0 % E2. The dominant learned rule is therefore is_ibd = 1 → E1. [src: ibd_phage_targeting]
- In UC Davis, which is all CD, is_ibd is constant. The rule collapses to the marginal mode. [src: ibd_phage_targeting]
- The extended training subset is 702 E1 / 959 E3 / 3 E0 / 11 E2. That is effectively an E1-versus-E3 binary problem, and severity markers do not separate the two reliably. [src: ibd_phage_targeting]

The revised H1c interpretation is that clinical covariates separate HC from IBD trivially, through is_ibd. They do not separate transitional E1 from severe E3 within IBD. [src: ibd_phage_targeting] The report concludes that metagenomics remains required for ecotype assignment in UC Davis-type cohorts. [src: ibd_phage_targeting] It also warns that OvR-AUC on a pooled cohort with a strong cohort-axis feature overstates per-patient usefulness. [src: ibd_phage_targeting] Related issues are in [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

## Key Findings: Within-ecotype × within-substudy meta-analysis defines ecotype-specific …

This part of the report asks why a pooled analysis called *Clostridium scindens* CD (Crohn's disease)-enriched, and what happened to the original within-ecotype analysis when the report repaired it. Compositional correction (CLR, centered log-ratio) fixed the signal for several protective species but did not remove the *C. scindens* enrichment. [src: ibd_phage_targeting] The report then retracted two of three headline NB04 claims. [src: ibd_phage_targeting] It replaced the original analysis with a within-substudy CD-vs-nonIBD design computed within each sub-study and combined by meta-analysis. [src: ibd_phage_targeting]

### The paradox and compositional correction (NB00)

The preliminary pooled Mann–Whitney analysis called *Clostridium scindens* CD-enriched at log₂FC +2.67. This contradicted its described protective bile-acid-producing role and ~79 % prevalence in healthy individuals. [src: ibd_phage_targeting] The report considered three explanations: compositional artifact, strain heterogeneity, and ecotype mixing in the pooled analysis. [src: ibd_phage_targeting]

NB00 tested the first by running 8 protective and 6 reported-pathobiont species under raw Mann–Whitney on relative abundance and under CLR-based Mann–Whitney. [src: ibd_phage_targeting] CLR correction recovered depletion for protective species that raw testing missed. *F. prausnitzii*, *A. muciniphila*, *R. hominis*, *L. eligens* and *A. rectalis* flipped from nonsignificant to CD-depleted. [src: ibd_phage_targeting] *Roseburia intestinalis* flipped from raw CD-enriched to CLR CD-depleted, which reproduced the proposed artifact pattern on a second species. [src: ibd_phage_targeting] The report concludes that pooled relative-abundance Mann–Whitney is systematically under-sensitive for protective-species depletion, because of compositional bias and pooled-cohort heterogeneity. [src: ibd_phage_targeting]

Reported pathobionts agreed across methods. *M. gnavus* (*R. gnavus*), *E. bolteae*, *E. lenta* and *H. hathewayi* were all CD-enriched under both raw and CLR tests. [src: ibd_phage_targeting]

*C. scindens* stayed CD-enriched under both methods (raw log₂FC +5.66; CLR Δ +1.25). NB00 therefore concluded that compositional correction alone is insufficient and that strain heterogeneity and ecotype mixing remain possible explanations. [src: ibd_phage_targeting]

### Retraction of the original NB04 claims

The original NB04 analysis was a within-ecotype CD-vs-HC (healthy control) CLR Mann–Whitney, committed 2026-04-24 early. The report supersedes it and retracts two of its three headline claims. [src: ibd_phage_targeting]

- **H2c (retracted).** The claim that within-ecotype stratification resolved the *C. scindens* paradox was retracted. [src: ibd_phage_targeting] The NB04 within-ecotype nonsignificant call was a feature-leakage artifact. Samples were clustered on taxon abundance, and the same taxon was then tested within cluster. [src: ibd_phage_targeting]
- **H2b (interpretation retained, statistic replaced).** The Jaccard of 0.14 was near the random-overlap baseline of ~0.10 for top-30 of ~300 filtered species. [src: ibd_phage_targeting] Against a permutation null (200 random-label permutations, null mean 0.785 ± 0.054), the observed Jaccard of 0.104 has empirical p = 0.000. H2b therefore survives strongly. [src: ibd_phage_targeting] The original argument still rested on an effect size without a reference distribution, which the report calls the wrong argument structure. [src: ibd_phage_targeting]
- **Tier-A list (retracted).** The list of 33 species (18 E1, 15 E3) was retracted. [src: ibd_phage_targeting] Held-out-species sensitivity Jaccard was E1 = 0.230 and E3 = 0.064, against a > 0.5 leakage-bounded threshold. [src: ibd_phage_targeting] In an independent confound-free CD-vs-control contrast, 14 of 18 E1 candidates had negative within-substudy effects. The report reads them as ecotype markers, not CD drivers. [src: ibd_phage_targeting]

### Why the pooled design is unidentifiable

curatedMetagenomicData pools samples across ≈ 51 source studies. [src: ibd_phage_targeting] In the ecotype-assigned slice of 8,489 samples, 45 sub-studies have ≥ 10 HC and 5 have ≥ 10 CD, but zero contain both. [src: ibd_phage_targeting] Healthy samples come from HC-only studies such as LifeLinesDeep_2016, AsnicarF_2021 and YachidaS_2019. [src: ibd_phage_targeting] CD samples come from IBD-cohort studies: HallAB_2017, VilaAV_2018, LiJ_2014, IjazUZ_2017 and NielsenHB_2014. [src: ibd_phage_targeting]

A pooled CD-vs-HC mixed-effects model with a substudy random effect is therefore structurally unidentifiable, because the random effect perfectly predicts diagnosis. [src: ibd_phage_targeting] `statsmodels.mixedlm` silently failed to converge on every battery species under this design. [src: ibd_phage_targeting] The report attributes *C. scindens* enrichment in the confound-free design to higher prevalence in the IBD-cohort source studies than in the healthy-cohort source studies. [src: ibd_phage_targeting]

### The replacement design

The identifiable contrast is CD-vs-nonIBD within IBD sub-studies. Four studies have ≥ 10 of each group (CD/nonIBD counts):

| Study | CD / nonIBD |
|---|---|
| HallAB_2017 | 89/73 [src: ibd_phage_targeting] |
| LiJ_2014 | 76/10 [src: ibd_phage_targeting] |
| IjazUZ_2017 | 56/38 [src: ibd_phage_targeting] |
| NielsenHB_2014 | 21/248 [src: ibd_phage_targeting] |

CLR-Δ is computed within each sub-study. Inverse-variance weighted meta-analysis then combines sub-studies. [src: ibd_phage_targeting] Stratifying by ecotype before meta-analysis gives ecotype-specific effects. [src: ibd_phage_targeting] The report asserts that this design avoids feature-leakage self-reference, because ecotype partitions samples and CLR-Δ is computed within partitions. [src: ibd_phage_targeting]

Under this contrast *C. scindens* is CD-enriched at +1.18 CLR-Δ (FDR, false discovery rate, 1e-8), with 4/4 sign-concordance across sub-studies. [src: ibd_phage_targeting] Under leave-one-species-out refit, it is CD-enriched within both E1 and E3 once excluded from the clustering input. [src: ibd_phage_targeting]

In NB04c, the 14-species battery across 242 CD / 369 nonIBD pooled samples recovers the canonical signature of pathobionts up and protective commensals down. [src: ibd_phage_targeting] *Mediterraneibacter gnavus* has pooled CLR-Δ +5.13, FDR ~0, concordance 4/4. [src: ibd_phage_targeting] *Eggerthella lenta* has +2.30, FDR 4e-9, concordance 4/4. [src: ibd_phage_targeting]

### Pipeline and pitfalls

The rigor-repair pipeline runs NB04b (bootstrap CIs, leakage-bound sensitivity, leave-one-out refit, Jaccard permutation null, ecotype stability). [src: ibd_phage_targeting] NB04c adds the within-substudy meta-analysis and LinDA in pure Python. [src: ibd_phage_targeting] NB04d is a rigor-controlled stopping rule. [src: ibd_phage_targeting] NB04e is the within-ecotype × within-substudy meta-analysis. [src: ibd_phage_targeting] The report records substudy-nesting unidentifiability and feature leakage in cluster-stratified differential abundance as generalizable pitfalls in `docs/pitfalls.md`. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

## Key Findings: Within-ecotype × within-substudy meta-analysis defines ecotype-specific … (2)

This part of the report gives the within-substudy Crohn's disease (CD) versus nonIBD meta-analysis (NB04c). It reports that NB04's within-ecotype calls for several species were reversed or contradicted by the confound-free analysis. It then gives the ecotype-stratified meta-analysis (NB04e), which yields Tier-A lists for ecotype E1 and, provisionally, E3. The E1 result pools two sub-studies. The E3 result rests on one study. [src: ibd_phage_targeting]

### Confound-free CD-versus-nonIBD meta-analysis (NB04c)

The NB04c within-substudy meta-analysis gives CD-enriched and CD-depleted species. Bilophila wadsworthia is the one null result. [src: ibd_phage_targeting]

| Species | Pooled CLR-Δ | FDR | Sign concordance |
|---|---|---|---|
| Escherichia coli | +1.43 | 2e-4 | 3/4 [src: ibd_phage_targeting] |
| Clostridium scindens | +1.18 | 1e-8 | 4/4 [src: ibd_phage_targeting] |
| Enterocloster bolteae | +1.09 | 3e-6 | 4/4 [src: ibd_phage_targeting] |
| Hungatella hathewayi | +0.92 | 5e-4 | 3/4 [src: ibd_phage_targeting] |
| Bilophila wadsworthia | +0.07 | n.s. | 3/4 [src: ibd_phage_targeting] |
| Lachnospira eligens | −1.01 | 4e-3 | 3/4 [src: ibd_phage_targeting] |
| Roseburia intestinalis | −1.14 | 2e-3 | 4/4 [src: ibd_phage_targeting] |
| Akkermansia muciniphila | −1.30 | 3e-3 | 3/4 [src: ibd_phage_targeting] |
| Faecalibacterium prausnitzii | −1.67 | 9e-8 | 4/4 [src: ibd_phage_targeting] |
| Roseburia hominis | −1.77 | 4e-7 | 4/4 [src: ibd_phage_targeting] |
| Coprococcus eutactus | −3.09 | 4e-15 | 4/4 [src: ibd_phage_targeting] |

The report retracts NB04's within-ecotype calls that F. prausnitzii, R. hominis and L. eligens were CD-enriched in E1 and E3. The confound-free analysis finds them CD-depleted. [src: ibd_phage_targeting] It also says NB04's nonsignificant result for C. scindens in both ecotypes is contradicted. [src: ibd_phage_targeting] The report blames feature leakage combined with the pooled-cohort substudy-by-diagnosis confound for NB04's direction reversals. Both CLR-MW and LinDA share this bias, so agreement between the two within-ecotype methods cannot resolve it. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

### Ecotype-stratified meta-analysis (NB04e)

NB04e stratifies the within-substudy contrasts by ecotype. This tests whether the canonical CD signature differs by ecotype, and it yields ecotype-specific Tier-A lists structurally free of leakage. [src: ibd_phage_targeting] Only three substudy-by-ecotype cells meet the bar of at least 10 CD and at least 10 nonIBD samples. [src: ibd_phage_targeting]

- E1, HallAB_2017: 67 CD and 41 nonIBD samples. [src: ibd_phage_targeting]
- E1, NielsenHB_2014: 15 CD and 239 nonIBD samples. [src: ibd_phage_targeting]
- E3, HallAB_2017: 22 CD and 31 nonIBD samples. [src: ibd_phage_targeting]

E0 and E2 cannot be analysed this way. They are healthy-cohort ecotypes with no nonIBD samples from IBD studies. [src: ibd_phage_targeting] E1 is meta-viable across two sub-studies, while E3 depends on HallAB_2017 alone. [src: ibd_phage_targeting]

### E1 Tier-A

E1 Tier-A has 51 candidates. All are 100 % sign-concordant across sub-studies, with FDR < 0.10 and pooled CLR-Δ > 0.5. [src: ibd_phage_targeting] The full list is in data/nb04e_within_ecotype_meta.tsv. [src: ibd_phage_targeting] The top ten are:

| Rank | Species | CLR-Δ | FDR |
|---|---|---|---|
| 1 | Mediterraneibacter gnavus | +4.85 | 2e-12 [src: ibd_phage_targeting] |
| 2 | Streptococcus salivarius | +3.26 | 2e-9 [src: ibd_phage_targeting] |
| 3 | Streptococcus thermophilus | +2.69 | 4e-6 [src: ibd_phage_targeting] |
| 4 | Erysipelatoclostridium innocuum | +2.65 | 4e-7 [src: ibd_phage_targeting] |
| 5 | Streptococcus parasanguinis | +2.44 | 2e-6 [src: ibd_phage_targeting] |
| 6 | Enterocloster asparagiformis | +2.41 | 2e-9 [src: ibd_phage_targeting] |
| 7 | Intestinibacter bartlettii | +2.36 | 3e-5 [src: ibd_phage_targeting] |
| 8 | Hungatella symbiosa | +2.23 | 1e-5 [src: ibd_phage_targeting] |
| 9 | Gordonibacter pamelaeae | +2.18 | 2e-5 [src: ibd_phage_targeting] |
| 10 | Erysipelatoclostridium ramosum | +2.16 | 4e-6 [src: ibd_phage_targeting] |

### Interpretation of E1 candidates

These readings are the report's interpretation and were not measured here.

- **Oral streptococci.** The report reads the enrichment of S. salivarius, S. thermophilus and S. parasanguinis as consistent with the oral-gut ectopic-colonization literature. [src: ibd_phage_targeting] It cites S. salivarius as a salivary biomarker for orofacial granulomatosis co-occurring with CD (Goel 2019, PMID 30796823). [src: ibd_phage_targeting] See [[entities/streptococcus-salivarius]].
- **S. thermophilus caveat.** S. thermophilus occurs in anti-inflammatory multi-strain probiotics. Its species-level CD enrichment therefore does not automatically mean pathobiont status. NB05 uses strain-level literature and engraftment evidence to disambiguate it. [src: ibd_phage_targeting]
- **E. innocuum.** The report describes it as a vancomycin-resistant IBD pathobiome. It is linked to creeping fat and intestinal strictures in CD and to reduced UC remission rates, and FMT is under evaluation as an intervention. [src: ibd_phage_targeting] Among E1 Tier-A candidates, it has the strongest stand-alone clinical-association evidence independent of this project's data. [src: ibd_phage_targeting]
- **Clostridial candidates.** The report assigns E. asparagiformis, I. bartlettii, H. symbiosa, E. ramosum, E. bolteae, E. clostridioformis and E. citroniae to the Lachnospiraceae / Erysipelotrichaceae expansion of the Bacteroides-2 dysbiosis subtype that defines E1. [src: ibd_phage_targeting] It treats their presence as underlying ecology, not an ecotype-marker artifact, because within-substudy meta-analysis controls the selection-on-outcome pattern behind the original NB04 list. [src: ibd_phage_targeting]
- **G. pamelaeae.** It produces urolithins from dietary ellagitannins and increases during microbiome recovery from dysbiosis-inducing insult. [src: ibd_phage_targeting] The report therefore finds its E1 CD enrichment hard to read as pathobiont activity. It flags the species for protective-analog exclusion (Tier-A-A4) in NB05. [src: ibd_phage_targeting]

### E3 Tier-A (provisional)

E3 Tier-A is provisional. It has 40 candidates from the single study HallAB_2017. [src: ibd_phage_targeting] The top candidates and their CLR-Δ values are:

- H. symbiosa, +4.64. [src: ibd_phage_targeting]
- M. gnavus, +4.46. [src: ibd_phage_targeting]
- B. coccoides, +4.22. [src: ibd_phage_targeting]
- R. faecis, +4.14. [src: ibd_phage_targeting]
- C. spiroforme, +4.11. [src: ibd_phage_targeting]
- S. salivarius, +4.04. [src: ibd_phage_targeting]
- E. innocuum, +3.68. [src: ibd_phage_targeting]

## Key Findings: Within-ecotype × within-substudy meta-analysis defines ecotype-specific … (3)

This part of the report tightens the E3 and engraftment-pathobiont results, applies four stopping criteria, and tests the ecotype framework for cross-study stability, pathway-feature recoverability and external projection in HMP2. At the NB04d stage the framework was judged usable for stratification but only marginally stable and not externally replicated. Later tests found it cross-study variable, and in the held-out HMP2 cohort ecotype stratified diagnosis. [src: ibd_phage_targeting]

### E3 replication and the retracted NB04 within-ecotype reading

*Flavonifractor plautii* replicates in the E3 Tier-A at CLR-Δ +2.26 (FDR 0.02). [src: ibd_phage_targeting] [[entities/flavonifractor-plautii]] *Blautia wexlerae* does not replicate in the stricter E3 × HallAB_2017 test (+0.25, FDR 0.80). It is removed from the NB04d rock-solid E3 set, which had relied on cohort-level rather than E3-restricted evidence. [src: ibd_phage_targeting] The E3 list stays provisional until a second cMD-IBD sub-study supplies at least 10 CD and at least 10 nonIBD E3 samples. HMP2 is the candidate once PENDING_HMP2_RAW is resolved. [src: ibd_phage_targeting]

Under the confound-free design, the report states that the classical engraftment pathobionts from donor 2708 → P1 → P2 are unambiguously CD-enriched. This is the opposite of NB04's within-ecotype interpretation. [src: ibd_phage_targeting] Five of 6 engraftment pathobionts pass the confound-free CD↑ test. [src: ibd_phage_targeting] *K. oxytoca* falls below the prevalence filter. [src: ibd_phage_targeting] The report retracts the NB04 narrative that these species are ecotype markers rather than CD drivers. It attributes the sign reversals to healthy-control and CD samples coming from entirely different source studies within each ecotype. [src: ibd_phage_targeting]

The retracted NB04 within-ecotype results were:

| Species | NB04 within-ecotype result |
|---|---|
| *M. gnavus* | E1 CD↓ −2.7, E3 CD↑ +1.6 [src: ibd_phage_targeting] |
| *E. lenta* | E1 CD↓ −2.4, E3 CD↓ −0.8 [src: ibd_phage_targeting] |
| *E. coli* | E1 CD↓ −1.8, E3 CD↓ −0.9 [src: ibd_phage_targeting] |
| *E. bolteae* | E1 CD↓ −1.6, E3 n.s. +0.6 [src: ibd_phage_targeting] |
| *H. hathewayi* | E1 CD↓ −1.4, E3 n.s. −0.1 [src: ibd_phage_targeting] |

NB04_within_ecotype_DA was superseded by the rigor-controlled pipeline of NB04b, NB04c, NB04d and NB04e. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

### NB04d stopping rule

Two of four criteria failed, and the report treats the failures as limits on what can be trusted. [src: ibd_phage_targeting]

- Feature leakage (held-out-species Jaccard, threshold > 0.5) failed in E1 (0.230) and E3 (0.064). [src: ibd_phage_targeting]
- The ecotype-specific Tier-A criterion (≥ 3 candidates) was met by E1 with 51 and E3 with 40, although E3 had single-study support. [src: ibd_phage_targeting]
- The confound-free engraftment-pathobiont criterion (≥ 3 of 6) was met at cohort level, with 5/5 tested. [src: ibd_phage_targeting]
- Internal stability (bootstrap ARI, threshold > 0.30) failed at 0.16. [src: ibd_phage_targeting]

The report concludes that NB04's original within-ecotype Tier-A cannot be trusted directly. [src: ibd_phage_targeting] NB04e's within-ecotype × within-substudy meta-analysis is structurally immune to leakage because its clustering and differential-abundance axes are disjoint. [src: ibd_phage_targeting] The framework had marginal internal stability (ARI 0.13–0.17 across 5 × 80 % subsamples). At this stage the report still judged it usable for downstream stratification, because NB02 projection is deterministic once fit, but flagged it as not externally replicated. [src: ibd_phage_targeting]

NB05 was authorized for E1 with the 51-candidate meta-viable Tier-A, which has confound-free multi-study support. [src: ibd_phage_targeting] For E3 it proceeds with caveat on the 40-candidate single-study Tier-A, with replication the first follow-up and HMP2 ingestion the unblock. [src: ibd_phage_targeting] The 5 engraftment-confirmed pathobionts are cross-ecotype candidates. [src: ibd_phage_targeting] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

### Further tests of the ecotype framework

NB04f, NB04g and NB04h tested cross-study generalization, residual feature leakage and external-cohort replication. [src: ibd_phage_targeting]

**NB04f (leave-one-substudy-out).** NB04f held out each of the top 8 cMD sub-studies by sample count. These were LifeLinesDeep_2016, AsnicarF_2021, NielsenHB_2014, VilaAV_2018, LiJ_2014, HallAB_2017, YachidaS_2019 and HansenLBS_2018. [src: ibd_phage_targeting] It refit K=4 latent Dirichlet allocation (LDA) on the remaining samples, projected the held-out samples back, Hungarian-aligned the labels and computed ARI against the NB01b consensus ecotype. [src: ibd_phage_targeting] Mean LOSO ARI was 0.113 (range 0.000–0.282), which fails the > 0.30 stability threshold. The report calls this more honest than the bootstrap ARI of 0.13–0.17 from NB04b. [src: ibd_phage_targeting] Mean per-sample agreement was 55.0 % (range 16.9 %–85.5 %). [src: ibd_phage_targeting] Agreement was high for LifeLinesDeep (ARI 0.21, 85.5 %) [src: ibd_phage_targeting] and HansenLBS (65 %). [src: ibd_phage_targeting] It was low for AsnicarF (38 %) [src: ibd_phage_targeting] and VilaAV (17 %). [src: ibd_phage_targeting] Part of the gap reflects the NB01b LDA+GMM (Gaussian mixture model) consensus, which had only 48.9 % cross-method agreement. [src: ibd_phage_targeting] The report concludes that the ecotype framework is cross-study variable, so the "four reproducible ecotypes" framing must be qualified. [src: ibd_phage_targeting] See [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

**NB04g (pathway features).** NB04g refit K=4 LDA on fact_pathway_abundance, using 3,145 CMD_IBD samples and 2,000 top-variance HUMAnN3 pathways. It compared the result with the taxon-based consensus. [src: ibd_phage_targeting] Overall ARI was 0.113 and per-sample agreement 50.6 %. [src: ibd_phage_targeting] Agreement differed by ecotype:

| Ecotype | Agreement | n |
|---|---|---|
| E1 | 65.3 % [src: ibd_phage_targeting] | 1,839 |
| E2 | 47.4 % [src: ibd_phage_targeting] | 19 |
| E3 | 30.7 % [src: ibd_phage_targeting] | 1,244 |
| E0 | 0 % [src: ibd_phage_targeting] | 43 |

E0 is the healthy-dominant ecotype and is rare in this pathway cohort. [src: ibd_phage_targeting] The report reads this as showing that the E1 taxon-ecotype is substantially recoverable from a disjoint pathway feature basis. [src: ibd_phage_targeting] Lower E3 recoverability, together with NB04e's single-study E3 evidence, supports the provisional E3 Tier-A framing. [src: ibd_phage_targeting] The report interprets the ecotype structure as mixed ecological and taxonomic. [src: ibd_phage_targeting] The refit is within-disease only, because fact_pathway_abundance has no healthy-control pathway coverage. [src: ibd_phage_targeting]

**NB04h (HMP2 external cohort).** NB04h pulled HMP2 MetaPhlAn3 profiles from curatedMetagenomicData v3.18. These comprise 1,627 samples, 130 subjects and 582 species, with 255/335 training-feature overlap after synonymy. [src: ibd_phage_targeting] HMP2 was absent from the CMD_IBD training substudy list, so it is a genuinely held-out cohort. It uses the same MetaPhlAn3 classifier namespace as the training data. [src: ibd_phage_targeting] Subject-level projection placed 106 of 130 subjects (82 %) in E1, with 11 in E2, 10 in E3 and 3 in E0. [src: ibd_phage_targeting] Ecotype stratified CD, UC and nonIBD diagnosis in HMP2 (χ² = 15.61, p = 0.016). [src: ibd_phage_targeting] HMP2 skews more toward E1 than the more balanced E1+E3 distribution in cMD. The report suggests this likely reflects recruitment of newly diagnosed or milder IBD rather than flare-dominated severe disease. [src: ibd_phage_targeting]

## Key Findings: Within-ecotype × within-substudy meta-analysis defines ecotype-specific … (4)

This part of the report covers external replication of the E1 Tier-A list in HMP2 data, the NB05 scoring that turns 71 candidates into 6 actionable targets, and the start of the NB06 co-occurrence networks. HMP2 replication is strong: 45 of 51 E1 Tier-A candidates replicate in sign. [src: ibd_phage_targeting] The scoring results are computed rankings from curated criteria, not experimental validation. [src: ibd_phage_targeting]

### HMP2 external replication

HMP2 projection was confident. Median maximum LDA posterior was 0.861, and 80.4 % of samples had a maximum posterior > 0.70. [src: ibd_phage_targeting] The report says this projection avoids the Kaiju–MetaPhlAn3 fragility that affects the [[entities/uc-davis-kuehl-wgs-crohn-s-disease-cohort|UC Davis]] Gaussian mixture model (GMM) projection, because HMP2 and the training data use the same MetaPhlAn3 pipeline. [src: ibd_phage_targeting] HMP2 was pulled with pull_hmp2_metaphlan3.R against [[entities/curatedmetagenomicdata]] v3.18. [src: ibd_phage_targeting]

Within HMP2-projected E1 samples (593 Crohn's disease (CD) / 337 nonIBD), 45 / 51 (88.2 %) NB04e E1 Tier-A candidates had sign-concordant CD-positive centered log-ratio (CLR) effects. [src: ibd_phage_targeting] Top replicators were:

| Species | HMP2 effect | FDR |
|---|---|---|
| M. gnavus | +1.08 | 3e-13 [src: ibd_phage_targeting] |
| E. asparagiformis | +0.89 | 1e-21 [src: ibd_phage_targeting] |
| H. symbiosa | +1.18 | 6e-22 [src: ibd_phage_targeting] |
| E. innocuum | +0.28 | 4e-16 [src: ibd_phage_targeting] |
| E. bolteae | +1.27 | 2e-18 [src: ibd_phage_targeting] |
| E. clostridioformis | +1.04 | 2e-21 [src: ibd_phage_targeting] |

Only 2 of the top 20 failed replication. [src: ibd_phage_targeting] S. thermophilus was sign-discordant, with a slightly negative HMP2 E1 effect. The report suggests this may reflect differential dairy exposure in HMP2 versus the HallAB/NielsenHB cohorts. [src: ibd_phage_targeting] Bacteroides stercoris was sign-discordant and not significant. [src: ibd_phage_targeting]

The report concludes that the operational Tier-A for NB05 is validated. It calls the ecotype framework cross-study variable but externally usable, because projected ecotypes stratify disease and Tier-A replicates at 88 %. [src: ibd_phage_targeting] See [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

### NB05 scoring design

NB05 applies four criteria (A3–A6) to 71 unique rigor-controlled candidates: 51 E1, 40 E3 provisional and 5 cross-ecotype engraftment candidates, after deduplication. [src: ibd_phage_targeting] The total Tier-A score is A3/5 + A4 + A5 + A6, with range 0–4 and an actionable threshold of 2.5. [src: ibd_phage_targeting]

- **A3 (CD association, 0–5)** counts five independent signals: confound-free meta-analysis, HMP2 replication, the Kumbhari differential reference, UHGG-indexed IBD associations and curated phage-biology targets. [src: ibd_phage_targeting] The Kumbhari signal uses log₂FC > 0.5 and FDR < 0.10. [src: ibd_phage_targeting] Scores are 0 for 13 candidates, 1 for 22, 2 for 25, 3 for 5, 4 for 5 and 5 for 1. [src: ibd_phage_targeting]
- **A4 (protective-analog exclusion)** fails a candidate with a negative within-IBD-substudy CD-versus-nonIBD effect, or one on the curated protective list. [src: ibd_phage_targeting] That list includes F. prausnitzii, A. muciniphila, R. intestinalis, R. hominis, L. eligens, A. rectalis, C. scindens, C. eutactus, B. adolescentis and B. longum. [src: ibd_phage_targeting] Three candidates fail: Anaerostipes hadrus (−0.32 effect) [src: ibd_phage_targeting], [[entities/clostridium-scindens|Clostridium scindens]] (curated protective list) [src: ibd_phage_targeting], and Roseburia faecis (−2.74 effect). [src: ibd_phage_targeting]
- **A5 (engraftment / strain adaptation)** gives 1.0 to the 5 donor-2708-engraftment pathobionts: M. gnavus, E. lenta, E. coli, E. bolteae and H. hathewayi. [src: ibd_phage_targeting] It gives 0.5 for Kumbhari strain-competition disease dominance or an IBD-adapted-strain gene signal. [src: ibd_phage_targeting] Three candidates reach 0.5: A. hadrus, B. cellulosilyticus and F. plautii. [src: ibd_phage_targeting]
- **A6 (biosynthetic gene clusters, BGCs)** counts BGCs from ref_bgc_catalog. Matching is synonymy-inverted, so pre-GTDB "Ruminococcus gnavus" maps to Mediterraneibacter gnavus. [src: ibd_phage_targeting] A candidate scores 1.0 if at least one BGC contains CD-enriched CB-ORFs (effect > 0.5 and FDR < 0.05). [src: ibd_phage_targeting] Fourteen candidates score 1.0. [src: ibd_phage_targeting]

Examples of A6 scorers:
- M. gnavus: 39 BGCs and 26 CD-enriched CB-ORFs, the largest count. [src: ibd_phage_targeting]
- E. coli: 93 BGCs with MIBiG matches to Colibactin, Yersiniabactin and Enterobactin. [src: ibd_phage_targeting]
- S. salivarius: 98 BGCs with Salivaricin 9, Salivaricin A and Cochonodin I. [src: ibd_phage_targeting]
- S. parasanguinis: 51 BGCs, 11 CD-enriched. [src: ibd_phage_targeting]
- H. hathewayi: 6 BGCs, 4 CD-enriched. [src: ibd_phage_targeting]

### NB05 results: six actionable candidates

Six of the 71 scored candidates pass the 2.5 threshold. [src: ibd_phage_targeting]

| Rank | Species | Total | Basis |
|---|---|---|---|
| 1 | Hungatella hathewayi | 4.0 | E1 and engraftment; all 5 A3 signals pass; 6 BGCs, 4 CD-enriched CB-ORFs [src: ibd_phage_targeting] |
| 2 | Mediterraneibacter gnavus | 3.8 | E1, E3_prov, engraftment; 4/5 A3; 39 BGCs, 26 CD-enriched CB-ORFs (inflammatory glucorhamnan mechanism) [src: ibd_phage_targeting] |
| 3 | Escherichia coli | 3.6 | E1 and engraftment; MIBiG matches to Colibactin, Yersiniabactin, Enterobactin [src: ibd_phage_targeting] |
| 4 | Eggerthella lenta | 3.3 | E1 and engraftment; 4/5 A3; Kumbhari IBD-adapted-strain gene signal [src: ibd_phage_targeting] |
| 5 | Flavonifractor plautii | 3.3 | E1 and E3_prov; Kumbhari strain competition; BGC with CD-enriched CB-ORFs [src: ibd_phage_targeting] |
| 6 | Enterocloster bolteae | 2.8 | E1 and engraftment [src: ibd_phage_targeting] |

For E. bolteae, NB05 found no BGC catalog hit and flags this as a potential blind spot. [src: ibd_phage_targeting]

Tier-B candidates score 2.2–2.4 and fall below the threshold. They are Enterocloster asparagiformis, Streptococcus salivarius, E. citroniae, E. clostridioformis, Blautia coccoides, Veillonella atypica, S. parasanguinis, Actinomyces oris and V. parvula. [src: ibd_phage_targeting] They have BGC evidence, pass A4 and have A3 = 1–2 signals. They lack direct engraftment or strain-adaptation evidence. [src: ibd_phage_targeting] Pillar 4 phage-targetability scoring may promote any of them based on B-tier phage-availability evidence. [src: ibd_phage_targeting] The scored TSV data/nb05_tier_a_scored.tsv is the authoritative hand-off to NB06 co-occurrence networks and Pillar 4 scoring. [src: ibd_phage_targeting]

NB05 was run with run_nb05.py rather than nbconvert because of an environment-specific numpy.bool serialization issue when saving the notebook. The report treats the outputs pre-populated in the committed notebook as authoritative. [src: ibd_phage_targeting]

### NB06 network construction

NB06 built four per-subnet correlation networks. It used a CLR transform and rank-based Pearson correlation (= Spearman rho), with per-edge Benjamini-Hochberg false discovery rate (BH-FDR). Edges needed |rho| > 0.3 and FDR < 0.05. Louvain communities were weighted by |rho|. [src: ibd_phage_targeting] Networkx 3.5's built-in Louvain was enough. The report held back FastSpar / SpiecEasi installation as unnecessary for the H2d question, given clear module structure at CLR-Spearman. [src: ibd_phage_targeting]

## Key Findings: Within-ecotype × within-substudy meta-analysis defines ecotype-specific … (5)

This part of the report maps co-occurrence networks (NB06) for the ecotypes E1 and E3 and starts the Pillar 3 pathway analysis (NB07a). In every network, the Tier-A pathobionts fall mostly in one module. NB07a's pathway analysis passes two of its three clauses. [src: ibd_phage_targeting]

### NB06 co-occurrence networks

The report builds four networks, each with a different number of samples, nodes, edges and modules. [src: ibd_phage_targeting]

- E1_all: 2,601 samples, 318 nodes, 28,730 edges, 6 modules. [src: ibd_phage_targeting]
- E1_CD: 581 samples, 255 nodes, 15,354 edges, 4 modules. [src: ibd_phage_targeting]
- E3_all: 1,364 samples, 296 nodes, 30,453 edges, 3 modules. [src: ibd_phage_targeting]
- E3_CD: 605 samples, 252 nodes, 19,909 edges, 7 modules. [src: ibd_phage_targeting]

The report calls the H2d verdict nominally PARTIAL but biologically SUPPORTED for the pathobiont module. [src: ibd_phage_targeting] The raw mean actionable targets per module on E1_all + E3_all was 1.38. That is below the plan's ≥ 2 bar. [src: ibd_phage_targeting] The report attributes the low mean to dilution. The other modules are commensal, Prevotella or diverse-healthy communities, which have 0 Tier-A hits by construction. [src: ibd_phage_targeting]

In every subnet, one module held 4-5 of the 6 actionable Tier-A candidates. [src: ibd_phage_targeting] The pathobiont modules were:
- E1_all module 1 (size 84): E. lenta, E. bolteae, F. plautii, H. hathewayi, M. gnavus. [src: ibd_phage_targeting]
- E1_CD module 0 (size 75): the same actionable set. [src: ibd_phage_targeting]
- E3_all module 1 (size 76): E. lenta, E. bolteae, E. coli, H. hathewayi, M. gnavus. [src: ibd_phage_targeting]
- E3_CD module 1 (size 57): E. lenta, E. coli, H. hathewayi, M. gnavus. [src: ibd_phage_targeting]

The report interprets this as a single ecologically linked co-occurrence module within Crohn's disease (CD) ecotypes. [src: ibd_phage_targeting] It suggests that shared conditions, likely bile-acid dysregulation and low-oxygen inflammation, make multi-target cocktails appropriate. [src: ibd_phage_targeting] It hypothesizes that a cocktail hitting 3+ of M. gnavus, E. lenta, E. bolteae, H. hathewayi and E. coli will have compounding effects. [src: ibd_phage_targeting] See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

### Ecotype differences

Flavonifractor plautii was in the main pathobiont module in E1 but in the generalist module in E3. [src: ibd_phage_targeting] The report therefore sees co-targeting as coherent for E1 patients. It suggests E3 patients may need a separate phage for F. plautii. [src: ibd_phage_targeting] Escherichia coli was in the pathobiont module only in E3. The report calls this consistent with adherent-invasive E. coli (AIEC) being more characteristic of severe-Bacteroides-expanded E3 than transitional E1. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

### Commensal hubs and butyrate producers

The top-degree non-Tier-A hubs in E1_all module 1 were Firmicutes bacterium CAG 110, Collinsella massiliensis and Phascolarctobacterium sp CAG 266. [src: ibd_phage_targeting] In E3_all module 1 they were Butyricicoccus pullicaecorum, Anaerostipes caccae and Lactococcus lactis. [src: ibd_phage_targeting] The report describes B. pullicaecorum as an extensively studied butyrate-producing IBD-probiotic candidate with published safety data. [src: ibd_phage_targeting] It describes A. caccae as a canonical butyrate producer. [src: ibd_phage_targeting]

Both species sit in the E3 pathobiont module, not in a separate healthy-commensal module. The report notes they are CD-depleted in most pooled analyses. It calls this co-variation biologically interesting. [src: ibd_phage_targeting] It proposes a metabolic-partner or cross-feeding interpretation. This is an interpretation, not a tested result. [src: ibd_phage_targeting] It cautions against "preserve butyrate producers" as a naive phage-targeting goal, because these species may track with the pathobionts. [src: ibd_phage_targeting]

The report declares Pillar 2 fully closed. It cites 6 actionable targets of 71 and a single pathobiont module. [src: ibd_phage_targeting] It treats the scored, module-assigned, hub-ranked Tier-A set as the full input for phage-availability analysis and UC Davis per-patient cocktail drafts. [src: ibd_phage_targeting] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]]. NB06 was run through run_nb06.py with pre-populated notebook outputs, as a workaround for an nbconvert numpy.bool issue. [src: ibd_phage_targeting]

### Species synonymy layer

The project's species synonymy table maps 2,417 aliases to 1,848 canonical species. It uses NCBI taxid matching from ref_taxonomy_crosswalk, supplemented with GTDB r214+ genus renames. [src: ibd_phage_targeting] NB00 found that fact_taxon_abundance uses three divergent cohort name formats: CMD_IBD short names, CMD_HEALTHY full MetaPhlAn3 lineage and KUEHL_WGS Kaiju. A naive pivot splits species into zero-overlap rows and produces log₂FC ≈ 28 artifacts. [src: ibd_phage_targeting] The layer was built in NB01b and joined by NB00, NB01, NB02, NB03 and every downstream notebook. [src: ibd_phage_targeting] The report documents this as a project-level pitfall and proposes the pattern as a general BERIL convention for multi-cohort microbiome integration. [src: ibd_phage_targeting] See [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]].

### NB07a pathway meta-analysis

NB07a is the first Pillar 3 notebook. It ran under RESEARCH_PLAN.md v1.7 norms, after adversarial review. [src: ibd_phage_targeting] Its primary contrast is a within-IBD-substudy CD-vs-nonIBD meta-analysis on CMD_IBD-only HUMAnN3 MetaCyc pathway abundance. [src: ibd_phage_targeting] For this modality there are 3 robust substudies (HallAB_2017, IjazUZ_2017, NielsenHB_2014) and 1 boundary substudy (LiJ_2014, nonIBD = 10). [src: ibd_phage_targeting] The report rejects the "4 meta-viable" framing inherited from NB04e's taxonomic counts. [src: ibd_phage_targeting] VilaAV_2018 was excluded (CD = 216, nonIBD = 0). [src: ibd_phage_targeting] A 10%-prevalence filter kept 409 of 575 unstratified MetaCyc pathways. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

H3a v1.7 was judged partially supported. Two of three clauses passed. Clause (b) was structurally degenerate, not a fundamental refutation. [src: ibd_phage_targeting]

- **Clause (a), pass:** 52 CD-up and 22 CD-down pathways passed false discovery rate (FDR) < 0.10 with |effect| > 0.5, 74 in either direction. [src: ibd_phage_targeting] The CD-up permutation-null mean was 0.077 ± 0.87, with empirical p < 0.001. [src: ibd_phage_targeting]
- **Clause (b), fail (degenerate):** only 44 / 409 background pathways matched the 7 a-priori MetaCyc categories under the v1.7 regex patterns. [src: ibd_phage_targeting] Only 3 of 52 CD-up pathways fell in those categories. The test had ~zero power, and the null also sat at 100% top-3 concentration. [src: ibd_phage_targeting] See [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]].
- **Clause (c), pass:** max |ρ_meta| = 0.797, against a null of 0.177 ± 0.019 and empirical p < 0.001. [src: ibd_phage_targeting]

NB07a found 137 pathway-pathobiont pairs with |ρ_meta| > 0.4. All were 100% sign-concordant across the 3 robust substudies. [src: ibd_phage_targeting] The top 25 pairs were all Escherichia coli pathways, and the report says they recapitulate known AIEC biology. [src: ibd_phage_targeting] Examples:
- Rank 1, GLYOXYLATE-BYPASS (ρ_meta = 0.797): fat utilization in fasting/inflamed gut and AIEC adaptation to the bile-acid environment. [src: ibd_phage_targeting]
- Rank 5, PWY-6803 phosphatidylcholine acyl editing (0.725): a trimethylamine (TMA) precursor pathway, linked to NB05 H. hathewayi A6. [src: ibd_phage_targeting]
- Rank 6, PWY-7385 1,3-propanediol biosynthesis (0.707): the eut/pdu pathway, a classical AIEC virulence factor. [src: ibd_phage_targeting]
- Rank 12, allantoin degradation to glyoxylate (0.685): purine recycling under inflammation. [src: ibd_phage_targeting]

## Key Findings: NB07b — Stratified-pathway DA per Tier-A-core species (H3a (b) …

NB07a tested the pathway-level clauses of hypothesis H3a (v1.7) and NB07b repeated the category test at species resolution. Pathway attribution to the Tier-A core species was strong and dominated by [[entities/escherichia-coli|Escherichia coli]]. The category-coherence clause (b) failed at both resolutions, but the report treats that failure as structural, not biological. [src: ibd_phage_targeting]

### Attribution to Tier-A species

Tier-A pathway pairs above 0.4 were concentrated in *E. coli*. The counts were: *E. coli* 105 pairs (76% of total signal) [src: ibd_phage_targeting], *H. hathewayi* 16 [src: ibd_phage_targeting], *M. gnavus* 8 [src: ibd_phage_targeting], *F. plautii* 7 [src: ibd_phage_targeting], *E. lenta* 1 [src: ibd_phage_targeting] and *E. bolteae* 0. [src: ibd_phage_targeting]

Top *E. coli* pathways included these:
- Rank 13, 2-methylcitrate cycle I (ρ_meta = 0.683), linked to propionate detoxification. [src: ibd_phage_targeting]
- Rank 19, heme biosynthesis from glycine (ρ_meta = 0.640), linked to iron metabolism and the NB05 *E. coli* Yersiniabactin MIBiG match. [src: ibd_phage_targeting]
- Rank 25, L-arginine degradation II (AST pathway) (ρ_meta = 0.617), assigned to AA-decarboxylation, one of the 7 a-priori categories. [src: ibd_phage_targeting]

The report attributes *E. coli* dominance to three factors. These are an AIEC (adherent-invasive *E. coli*) repertoire well matched to MetaCyc, higher relative-abundance variance, and better HUMAnN3 genome-content representation than obligate anaerobes such as *E. lenta* and *E. bolteae*. [src: ibd_phage_targeting] The zero attribution for *E. bolteae* leads the report to hypothesize that its CD-up signal lies at the BGC (biosynthetic gene cluster) level or the Kumbhari strain-frequency level, not the pathway level. [src: ibd_phage_targeting]

### Clause (b): category coherence fails

Only 3 of 52 CD-up unstratified MetaCyc pathways fell in the 7 a-priori IBD categories, so the test was structurally underpowered. [src: ibd_phage_targeting] The signal did not preferentially load on bile-acid 7α-dehydroxylation, mucin degradation, sulfidogenesis, TMA/TMAO, eut/pdu, polyamine or AA-decarb. [src: ibd_phage_targeting] It instead captured broader bacterial-fitness themes: heme/iron, glyoxylate, fat metabolism and allantoin/purines. [src: ibd_phage_targeting] The report says CD-associated pathways are dominated by biosynthesis and niche-shift signals. [src: ibd_phage_targeting]

The report offers these readings of the failure:
- Adding categories for alternative-electron-acceptor metabolism, iron acquisition and fat utilization in inflammation might recover the clause (b) signal. [src: ibd_phage_targeting]
- Shared housekeeping pathways may dominate the unstratified level. [src: ibd_phage_targeting]
- Given the strong attribution signal, clause (b) is a follow-up question, not a current refutation. [src: ibd_phage_targeting]

### NB07b: species-resolved test

NB07b asks whether per-species CD-up pathways in HUMAnN3 stratified data concentrate in the a-priori categories. [src: ibd_phage_targeting] It has about 42K pathway-species combinations to query. [src: ibd_phage_targeting] H3a (b) was NOT SUPPORTED for all 6 Tier-A core species. The report calls this verdict structural, because the categories are sparse in per-species repertoires. [src: ibd_phage_targeting]

| Species | CD-up | CD-down | Status and reason |
|---|---|---|---|
| *H. hathewayi* | 16 | 17 | underpowered; 1 of 16 CD-up in the 7-category set [src: ibd_phage_targeting] |
| *M. gnavus* | 0 | 0 | untestable; only 4 background pathways in the 7 categories [src: ibd_phage_targeting] |
| *E. coli* | 2 | 18 | underpowered; 0 of 2 CD-up in the 7 categories [src: ibd_phage_targeting] |
| *E. lenta* | 0 | 0 | untestable; 3 background pathways in the 7 categories [src: ibd_phage_targeting] |
| *F. plautii* | 0 | 2 | underpowered; 0 of 0 CD-up in the 7 categories [src: ibd_phage_targeting] |
| *E. bolteae* | 1 | 3 | untestable; 3 background pathways in the 7 categories [src: ibd_phage_targeting] |

Together, NB07a and NB07b show that the 7 categories are too narrow to capture HUMAnN3 MetaCyc CD signal at either resolution. [src: ibd_phage_targeting] The refutation applies only to the v1.7 category set. It does not mean that no compositional themes exist. A broader schema derived programmatically from MetaCyc taxonomy is needed. [src: ibd_phage_targeting]

### Within-carrier shifts

In *H. hathewayi* (33 passing pathways), CD versus nonIBD shows a coherent shift between biosynthesis and degradation. [src: ibd_phage_targeting]

| Direction | Pathway | Effect | FDR |
|---|---|---|---|
| CD-up | Pentose phosphate pathway | +1.18 | 1.6e-5 [src: ibd_phage_targeting] |
| CD-up | Glycolysis IV (plant cytosol) | +0.94 | 1.0e-3 [src: ibd_phage_targeting] |
| CD-up | Chorismate biosynthesis I | +0.86 | 1.6e-6 [src: ibd_phage_targeting] |
| CD-up | Purine nucleobases degradation | +0.89 | 2.6e-4 [src: ibd_phage_targeting] |
| CD-down | Pyrimidine deoxyribonucleosides salvage | −1.51 | 2.4e-7 [src: ibd_phage_targeting] |
| CD-down | 1,3-Propanediol biosynthesis | −1.27 | 4.3e-6 [src: ibd_phage_targeting] |
| CD-down | Lactose / galactose degradation | −1.18 | 7.0e-5 [src: ibd_phage_targeting] |
| CD-down | O-antigen biosynthesis (GDP-mannose) | −1.07 | 3.4e-4 [src: ibd_phage_targeting] |

The report interprets this as a shift toward a biosynthetic/catabolic-stress state and away from sugar utilization. [src: ibd_phage_targeting] It reads the CD-down propanediol-degradation signal as consistent with niche partitioning, in which *E. coli* may dominate this niche under CD. [src: ibd_phage_targeting] This is an interpretation, not a direct measurement.

*E. coli* (20 passing pathways) shows within-carrier CD-down per-pathway abundance. This is opposite to its cohort-level CD-up direction. [src: ibd_phage_targeting]

| Pathway | Effect | FDR |
|---|---|---|
| CMP-legionaminate biosynthesis | −0.95 | 3.0e-5 [src: ibd_phage_targeting] |
| L-1,2-propanediol degradation | −0.81 | 2.9e-4 [src: ibd_phage_targeting] |
| Allantoin degradation to glyoxylate | −0.81 | 1.8e-6 [src: ibd_phage_targeting] |
| Phospholipid remodeling (PE) | −0.84 | 7.3e-6 [src: ibd_phage_targeting] |
| Octane oxidation | −0.72 | 2.4e-5 [src: ibd_phage_targeting] |

### Outputs

NB07a produced a table of 409 pathways with meta statistics [src: ibd_phage_targeting] and a table of 2,454 pathway × Tier-A-core species pairs with per-substudy and meta ρ. [src: ibd_phage_targeting] It also produced the formal H3a v1.7 verdict with all permutation-null statistics. [src: ibd_phage_targeting]

Next test: the report names species-stratified NB07b analysis as the appropriate next test of clause (b). One question is whether *M. gnavus* gains bile-acid-deconjugation pathways in CD versus nonIBD. [src: ibd_phage_targeting]

## Key Findings: NB07 v1.8 H3a (b) retest — MetaCyc class hierarchy + Fisher per-theme …

This part of the report covers two linked analyses. NB07b asks whether the Tier-A core species shift their metabolism within carriers. NB07 v1.8 re-tests the cohort-level H3a (b) hypothesis with a structured MetaCyc class hierarchy in place of regex categories. The v1.8 re-test supports H3a (b) at cohort level through iron/heme acquisition. The report treats the change from the v1.7 FAIL verdict as a result of the categorization method alone. [src: ibd_phage_targeting]

### NB07b: within-carrier shifts per Tier-A core species

In *Escherichia coli* carriers, L-histidine degradation I was CD-down (CD = Crohn's disease) with effect −0.62 and FDR 2.8e-3 (FDR = false discovery rate). [src: ibd_phage_targeting] The report reads this as follows: cohort-level *E. coli* abundance is CD-up, so total pathway flux scales up. Within carriers, per-cell pathway repertoire is CD-down, which it interprets as less metabolic versatility per cell in CD samples. [src: ibd_phage_targeting]

The report offers two interpretations that are not mutually exclusive, and both align with the AIEC (adherent-invasive *E. coli*) narrative. [src: ibd_phage_targeting]
- CD *E. coli* may be an AIEC-specialized subset that has shed peripheral metabolic capabilities, consistent with earlier Yersiniabactin, Colibactin and IBD-specific lineage findings. [src: ibd_phage_targeting]
- CD *E. coli* may face metabolic competition from co-abundant *Klebsiella* or other Enterobacteriaceae, which lowers per-cell read-mapping share. [src: ibd_phage_targeting]

Deeper strain-level analysis of raw reads was dropped under plan v1.9's no-raw-reads scope. A genome-content survey using `kbase_genomes` and Kumbhari `fact_strain_competition` is listed as Future Direction #9. [src: ibd_phage_targeting]

The other four core species (*M. gnavus*, *E. lenta*, *F. plautii*, *E. bolteae*) each had ≤ 4 passing pathways. Their CD signal is dominated by carriage prevalence, not within-carrier metabolic shift. [src: ibd_phage_targeting] The report concludes that pathway-level mechanism is the wrong resolution for these species. It names BGC-level analysis (NB08, executed) and Kumbhari strain-frequency analysis (NB10a) as no-raw-reads alternatives. [src: ibd_phage_targeting]

### NB07 v1.8: replacing regex with MetaCyc classes

The v1.7 H3a (b) FAIL verdict came from regex limits. Only 44/409 background pathways matched the 7 a-priori category patterns. PWY-5920 (superpathway of heme biosynthesis from glycine) was silently labelled "0_other". [src: ibd_phage_targeting] v1.8 uses structured MetaCyc class assignments from ModelSEEDDatabase and expands to 12 IBD-relevant themes. [src: ibd_phage_targeting] The ModelSEED hierarchy assigns PWY-5920 to HEME-SYN, Heme-b-Biosynthesis, Cofactor-Biosynthesis and Tetrapyrrole-Biosynthesis. [src: ibd_phage_targeting] Plan norm N17 prefers ontology or class hierarchy over name-pattern regex and keeps regex as a sensitivity check. [src: ibd_phage_targeting] See [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]] and [[entities/metacyc-pathway-class-hierarchy]].

### Cohort-level result

Per-theme Fisher's exact tests asked whether CD-up pathways are enriched in each theme. They used BH-FDR (Benjamini-Hochberg false discovery rate) across themes, and a theme counted as supported at FDR < 0.10 and odds ratio (OR) > 1.5. The cohort-level verdict is SUPPORTED. [src: ibd_phage_targeting] Iron/heme acquisition met the criteria. Seven other themes listed below did not. [src: ibd_phage_targeting]

| Theme | Background | CD-up | Expected | OR | p | FDR | Tag |
|---|---|---|---|---|---|---|---|
| 08 iron/heme acquisition | 32 / 409 | 15 / 52 (29 %) | 4.07 | 8.11 | 5.8e-7 | 7.4e-6 | [src: ibd_phage_targeting] |
| 09 anaerobic respiration | 50 | 8 | 6.36 | 1.36 | 0.29 | 1.0 | [src: ibd_phage_targeting] |
| 02 mucin/glycan/host | 83 | 11 | 10.55 | 1.06 | 0.50 | 1.0 | [src: ibd_phage_targeting] |
| 12 aromatic AA/chorismate/indole | 22 | 3 | 2.80 | 1.09 | 0.55 | 1.0 | [src: ibd_phage_targeting] |
| 10 fat metabolism/glyoxylate | 111 | 13 | 14.11 | 0.88 | 0.70 | 1.0 | [src: ibd_phage_targeting] |
| 07 AA decarboxylation | 62 | 7 | 7.88 | 0.85 | 0.71 | 1.0 | [src: ibd_phage_targeting] |
| 11 purine/pyrimidine recycling | 78 | 7 | 9.92 | 0.63 | 0.91 | 1.0 | [src: ibd_phage_targeting] |
| 06 polyamine/urea | 90 | 6 | 11.44 | 0.42 | 0.99 | 1.0 | [src: ibd_phage_targeting] |

The report calls iron/heme acquisition the dominant CD-up biochemical theme, at 8.1× over background and 29 % of CD-up pathways versus 8 % expected. [src: ibd_phage_targeting] The 15 CD-up pathways include heme biosynthesis (PWY-5920, ρ = 0.64 with *E. coli* in NB07a), heme degradation and siderophore-related pathways. [src: ibd_phage_targeting] The report says the reversal of v1.7 is entirely due to category-schema choice, not to any change in the data. [src: ibd_phage_targeting]

### Species-level result: *Hungatella hathewayi*

*H. hathewayi* had two themes supported across its 16 CD-up pathways. [src: ibd_phage_targeting] Purine/pyrimidine recycling gave OR=4.86, FDR=0.048 (7/16 CD-up pathways). [src: ibd_phage_targeting] TMA (trimethylamine)/choline gave OR=9.33, FDR=0.048 (4/16). [src: ibd_phage_targeting] Its NB07b CD-up pathways included pentose phosphate, purine nucleobase degradation and PWY-6803 phosphatidylcholine acyl editing, the building-block pathways of these two themes. [src: ibd_phage_targeting] The report describes *H. hathewayi* as a known TMA producer (CutC/D activity), so it finds the choline enrichment mechanistically coherent. [src: ibd_phage_targeting]

Limit: the other Tier-A core species lack the CD-up counts needed for per-theme power. *M. gnavus*, *E. lenta* and *F. plautii* have 0, and *E. coli* and *E. bolteae* have 1-2. [src: ibd_phage_targeting]

### Convergence on iron biology

The report interprets four lines of evidence as converging on iron biology as the dominant CD pathobiont specialization in this dataset. This is the report's interpretation, not a direct test. [src: ibd_phage_targeting]
- NB05 *E. coli* MIBiG matches include the siderophores Yersiniabactin and Enterobactin, plus Colibactin from the same pks island. [src: ibd_phage_targeting]
- NB07a's top pathway-pathobiont attribution is heme biosynthesis ↔ *E. coli* (ρ = 0.640). [src: ibd_phage_targeting]
- AIEC literature (Dalmasso 2021, Prudent 2021, Dogan 2014) flags iron acquisition as a central AIEC fitness mechanism. [src: ibd_phage_targeting]

See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

### Lesson and outputs

The report's lesson is that regex on pathway names is a poor substitute for a curated class hierarchy. ModelSEEDDatabase ships a usable MetaCyc hierarchy with 90 % coverage of HUMAnN3 outputs, and the report recommends it as the default for pathway category-enrichment tests. [src: ibd_phage_targeting] The NB07b output holds 621 species-pathway × meta rows. [src: ibd_phage_targeting]

## Key Findings: NB07c — Module-anchor commensal × pathobiont metabolic coupling (H3a-new)

This part of the report tests whether the commensal "anchors" of Crohn's disease (CD)-specific co-occurrence modules show metabolic coupling with the pathobionts beside them. The answer is partial: the coupling is clear for Anaerostipes caccae in E1_CD and absent in E3_CD. The iron signal traces mostly to Escherichia coli. The evidence is correlational, and the report defers separating cross-feeding from shared environment. [src: ibd_phage_targeting]

### Question and design

NB06 found that 4–5 of 6 actionable Tier-A pathobionts co-cluster in a single CD-specific module per ecotype. [src: ibd_phage_targeting] NB07c asks whether the non-pathobiont anchors of those modules show metabolic coupling with the pathobionts (the H3a-new test). [src: ibd_phage_targeting] For each anchor–pathobiont pair it computes within-substudy Spearman ρ across CMD_IBD samples. It then Fisher z-meta-analyzes the 3 robust substudies (ZellerG_2014, NielsenHB_2014, IjazUZ_2017) and checks sign concordance. [src: ibd_phage_targeting] An iron-context layer adds triple correlations (anchor × pathobiont × iron pathway) over 15 iron/heme pathways. These triples test whether the iron theme is community-wide or pathobiont-specific. [src: ibd_phage_targeting] The 15 pathways include ENTBACSYN-PWY (enterobactin biosynthesis), HEMESYN2-PWY (heme biosynthesis II) and 8 menaquinol-biosynthesis pathways. [src: ibd_phage_targeting]

E1_CD module 0 has 75 nodes. Its anchors are Clostridiales bacterium 1_7_47FAA, Anaerostipes caccae and Bacteroides nordii, alongside 5 actionable Tier-A pathobionts. [src: ibd_phage_targeting] A. caccae is the only genuine butyrate-producer among the module-anchor commensals. [src: ibd_phage_targeting] E3_CD module 1 has 57 nodes. Its anchors are two oral ectopic-colonizer Actinomyces and the lactate utilizer Lactonifactor longoviformis, alongside 4 pathobionts. [src: ibd_phage_targeting]

### E1_CD: Anaerostipes caccae couples positively with pathobionts

A. caccae couples positively with all 5 E1_CD module pathobionts, with sign concordance 1.0 across all 3 substudies. [src: ibd_phage_targeting] Four pairs are strong and the fifth is weak. [src: ibd_phage_targeting]

| Pair | ρ_meta |
|---|---|
| A. caccae × E. bolteae (strongest) | +0.39 [src: ibd_phage_targeting] |
| A. caccae × H. hathewayi | +0.33 [src: ibd_phage_targeting] |
| A. caccae × M. gnavus | +0.31 [src: ibd_phage_targeting] |
| A. caccae × F. plautii | +0.29 [src: ibd_phage_targeting] |
| A. caccae × E. lenta (weakest) | +0.08 [src: ibd_phage_targeting] |

Bacteroides nordii couples negatively with [[entities/mediterraneibacter-gnavus]] (−0.21) and with [[entities/flavonifractor-plautii]] (−0.20). [src: ibd_phage_targeting] The report reads these as niche competition for similar polysaccharide substrates, with CD selecting one side over the other. [src: ibd_phage_targeting]

The report reads the A. caccae pattern as consistent with butyrate-producer cross-feeding inside the CD module. The proposed substrates are M. gnavus glucorhamnan and mucin sugars, F. plautii bile-acid metabolites and H. hathewayi lactate. [src: ibd_phage_targeting] This is an interpretation, not a direct measurement. NB07c defers separating cross-feeding from shared-environment co-occurrence to metabolite corroboration in NB09c. [src: ibd_phage_targeting]

### Iron context: the signal is carried by E. coli

A. caccae's mean correlation with the 15 iron pathways is +0.13, much weaker than E. coli's +0.45. The report therefore rules against iron cross-feeding and calls the coupling most likely substrate-, sugar- or lactate-mediated. [src: ibd_phage_targeting]

Mean iron-pathway correlations for the pathobionts:

| Species | Mean ρ with iron pathways |
|---|---|
| E. coli | +0.45 [src: ibd_phage_targeting] |
| H. hathewayi | +0.20 [src: ibd_phage_targeting] |
| F. plautii | +0.17 [src: ibd_phage_targeting] |
| M. gnavus | +0.16 [src: ibd_phage_targeting] |
| E. bolteae | +0.09 [src: ibd_phage_targeting] |
| E. lenta | +0.03 [src: ibd_phage_targeting] |

The report reads E. coli's ρ = +0.45 across 2,674 CMD_IBD samples as showing that iron-pathway abundance scales with E. coli abundance, so E. coli dominantly carries the signal. [src: ibd_phage_targeting] It reads the weak coupling of the other species as consistent with non-iron CD specializations: TMA (trimethylamine)/choline in H. hathewayi, bile-acid 7α-dehydroxylation in F. plautii, and glucorhamnan/mucin in M. gnavus. [src: ibd_phage_targeting] Among actionable Tier-A species, only E. coli had NB05 iron-siderophore MIBiG matches, for yersiniabactin and enterobactin. [src: ibd_phage_targeting]

This narrows the earlier iron-theme interpretation. The report's framing is now that CD's E. coli, particularly its adherent-invasive (AIEC) subset, drives iron acquisition, while other Tier-A pathobionts have non-iron specializations. [src: ibd_phage_targeting] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

### E3_CD: no metabolic-coupling structure

In E3_CD only Lactonifactor × [[entities/eggerthella-lenta]] is strong (ρ_meta = +0.27). [src: ibd_phage_targeting] The two oral Actinomyces anchors couple weakly with M. gnavus and E. lenta, at about ρ=0.17–0.19. [src: ibd_phage_targeting] The report interprets their module membership as shared inflammation-driven ectopic colonization, not metabolic partnership. [src: ibd_phage_targeting]

### Verdict and design implication

H3a-new is judged partially supported. E1_CD has 4 strong-positive, sign-concordant A. caccae pairs, while E3_CD anchors lack metabolic-coupling structure. [src: ibd_phage_targeting]

The report warns that a cocktail depleting M. gnavus, F. plautii, H. hathewayi or E. bolteae may incidentally reduce A. caccae through loss of substrate. [src: ibd_phage_targeting] Because butyrate is anti-inflammatory, losing A. caccae could partially offset the cocktail's benefit. [src: ibd_phage_targeting] It proposes a "metabolic-coupling cost" annotation for each actionable Tier-A target before cocktail finalization. The annotation would list the beneficial commensals that depend on the target and the predicted net inflammatory balance. [src: ibd_phage_targeting] See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

### Outputs

The analysis was run with run_nb07c.py, building on NB06 module hubs and the NB07_v1.8 iron-pathway list. [src: ibd_phage_targeting] Its outputs hold 27 anchor–pathobiont pairs with meta-correlations, per-substudy values and sign concordance, and 405 anchor–pathobiont–iron-pathway triples. [src: ibd_phage_targeting] The formal verdict is in data/nb07c_h3a_new_verdict.json. [src: ibd_phage_targeting]

## Key Findings: NB08a — BGC × pathobiont enrichment (H3c) — genomic mechanism layer

This part of the report tests, at the genome level, whether Tier-A pathobionts carry an iron-siderophore and genotoxin biosynthetic gene cluster (BGC) signature. It finds that the signature sits in *Escherichia coli* alone. The report also finds a strong sample-level CD signal for ebf/ecf, and it judges hypothesis H3c only partially supported. [src: ibd_phage_targeting]

### Background and design

Earlier notebooks pointed to iron. NB05 flagged Yersiniabactin, Enterobactin and Colibactin matches in *E. coli*. [src: ibd_phage_targeting] NB07 found iron/heme acquisition to be the dominant CD-up MetaCyc pathway-class theme (OR=8.1, FDR 7e-6). [src: ibd_phage_targeting] NB07c found sample-level iron-pathway co-variation concentrated on *E. coli*. [src: ibd_phage_targeting] NB08a tests genomic content using the Elmassry 2025 ref_bgc_catalog (10,060 BGCs across 6,221 species-annotated entries). [src: ibd_phage_targeting] It uses Fisher's exact test with BH-FDR (Benjamini-Hochberg false discovery rate) across 4 IBD-relevant themes. [src: ibd_phage_targeting]

### BGC theme enrichment

Iron-siderophore and genotoxin/microcin clusters are strongly over-represented in the Tier-A core. The NRPS-PKS hybrid class is only weakly enriched, and bacteriocin/RiPP clusters sit at background. [src: ibd_phage_targeting] The report counts 3 of the 4 themes as supported. [src: ibd_phage_targeting]

- iron_siderophore: Tier-A core 54 / 286, background 51 / 9,774, Fisher OR 44.4, FDR 6.5e-56. [src: ibd_phage_targeting]
- genotoxin_microcin: 25 / 286 versus 4 / 9,774, OR 234.0, FDR 3.3e-35. [src: ibd_phage_targeting]
- NRPS_PKS_hybrid: 32 / 286 versus 739 / 9,774, OR 1.54, FDR 0.042. [src: ibd_phage_targeting]
- bacteriocin_RiPP: 154 / 286 versus 5,217 / 9,774, OR 1.02, FDR 0.90 (background rate). [src: ibd_phage_targeting]

The report reads this as converging with the pathway-level OR of 8.1. It treats the two as different evidence streams and concludes that iron acquisition is a CD pathobiont-defining genomic capability, not just a pathway-level cohort signal. [src: ibd_phage_targeting]

### The signature is specific to E. coli

Within actionable Tier-A core, *E. coli* alone carries the iron+genotoxin signature. [src: ibd_phage_targeting] It has 146 BGCs, including 54 iron and 25 genotoxin MIBiG matches. [src: ibd_phage_targeting] The other five species have no iron or genotoxin matches: *M. gnavus* has 58 BGCs [src: ibd_phage_targeting], *E. lenta* 41 [src: ibd_phage_targeting], *E. bolteae* 18 [src: ibd_phage_targeting], *H. hathewayi* 13 [src: ibd_phage_targeting] and *F. plautii* 10. [src: ibd_phage_targeting]

The 54 *E. coli* iron BGCs comprise 19 Yersiniabactin, 16 Enterobactin and 19 siderophore-class BGCs, with some redundant per-strain assemblies. [src: ibd_phage_targeting] The 25 genotoxin BGCs comprise 8 Colibactin, 15 Microcin B17 and 2 Microcin J25. [src: ibd_phage_targeting] The report concludes that iron biology in CD pathobionts is essentially an *E. coli* (AIEC, adherent-invasive *E. coli*) phenomenon. It says the other Tier-A pathobionts have non-iron CD-association mechanisms. [src: ibd_phage_targeting]

The report describes five evidence streams converging on AIEC iron acquisition as a central CD-pathobiont specialization mechanism. They include heme–*E. coli* ρ=0.640 and sample-level *E. coli*–iron-pathway ρ=0.45. [src: ibd_phage_targeting]

### Read-level CB-ORF enrichment

Test 3 uses ref_cborf_enrichment (5,157 CB-ORFs). [src: ibd_phage_targeting] The background catalog has 5,052 matched CB-ORFs, a 2.5 % CD-up rate and mean effect -0.18. [src: ibd_phage_targeting] Five of 6 Tier-A core species exceed that background (range 14–82 %). *E. lenta* is the exception, with CB-ORFs CD-down at 54 %. [src: ibd_phage_targeting]

- *E. bolteae*: 11 CB-ORFs matched, 9 (82 %) CD-up at FDR<0.10, 0 CD-down, mean effect +2.81. [src: ibd_phage_targeting]
- *F. plautii*: 5 matched, 2 (40 %) CD-up, 0 CD-down, mean effect +0.77. [src: ibd_phage_targeting]
- *E. coli*: 51 matched, 14 (27 %) CD-up, 0 CD-down, mean effect +1.56. [src: ibd_phage_targeting]
- *M. gnavus*: 19 matched, 5 (26 %) CD-up, 0 CD-down, mean effect +1.43. [src: ibd_phage_targeting]
- *H. hathewayi*: 7 matched, 1 (14 %) CD-up, 0 CD-down, mean effect +0.52. [src: ibd_phage_targeting]
- *E. lenta*: 13 matched, 0 CD-up, 7 (54 %) CD-down, mean effect -0.28. [src: ibd_phage_targeting]

The report ties the *E. lenta* pattern to NB07b's finding that its per-pathway abundance is mostly carriage-prevalence-driven. It also notes that the canonical *Eggerthella* mechanism is drug metabolism (cardiac glycoside inactivation), not BGC-encoded inflammatory mediators. [src: ibd_phage_targeting] This is the report's interpretation, not a direct measurement here.

### ebf/ecf cohort meta-analysis

Test 4 uses ref_ebf_ecf_prevalence (1,349 samples × 4 cohorts), with Mann-Whitney tests per cohort and Stouffer's z-meta. [src: ibd_phage_targeting] The RPKM meta-analysis gives z 11.71 (p 1.1e-31) for ebf and z 11.97 (p 5.1e-33) for ecf. [src: ibd_phage_targeting] All 4 cohorts (HMP2-IBDMDB, MetaHIT, LLDEEP-NLIBD, PRISM) show CD > HC for both, with cliff-deltas 0.17–0.73. [src: ibd_phage_targeting] The report says this replicates the Elmassry 2025 immunoactive fatty acid amide BGC family CD-up finding at p < 1e-31, and calls that finding the largest single effect in the project so far. [src: ibd_phage_targeting]

### H3c verdict and design implications

The report judges H3c partially supported. [src: ibd_phage_targeting] The strict species × BGC interaction-term test is untested. It needs species-stratified per-sample BGC abundance, which the current pre-computed mart slice lacks. [src: ibd_phage_targeting]

- For the *E. coli* phage component, the report recommends targeting Yersiniabactin/Enterobactin/Colibactin-positive AIEC strains. [src: ibd_phage_targeting] It drops AIEC strain resolution from cMD raw reads. As the no-raw-reads alternative, it proposes a kbase_genomes *pks* plus iron-BGC genome-content query. [src: ibd_phage_targeting]
- For *M. gnavus*, *E. lenta*, *E. bolteae*, *H. hathewayi* and *F. plautii*, cocktail design relies on Tier-A scoring, module membership and within-carrier metabolic signature, not on BGC presence. [src: ibd_phage_targeting]
- ebf/ecf RPKM is proposed as a sample-level CD biomarker for treatment-response monitoring, not for cocktail target selection, because no per-species attribution is available. [src: ibd_phage_targeting]

The analysis is implemented in run_nb08a.py and builds on actionable Tier-A targets and three reference datasets. [src: ibd_phage_targeting] Its outputs include a per-species BGC repertoire summary, a theme-enrichment table of 4 themes with Fisher OR and FDR, a per-species iron and genotoxin breakdown, per-species CB-ORF CD-up rates, ebf/ecf cohort meta z-statistics, and a formal H3c verdict file. [src: ibd_phage_targeting]

Related pages: [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]], [[entities/escherichia-coli]].

## Key Findings: NB09a — HMP2 metabolomics CD-vs-nonIBD (H3d-DA)

NB09a is the report's first metabolomics analysis. It asks whether the HMP2 metabolite axes separating Crohn's disease (CD) from nonIBD agree with the iron, trimethylamine (TMA), fat, bile-acid and fatty-acid-amide themes from the earlier pathway and biosynthetic gene cluster (BGC) analyses. [src: ibd_phage_targeting] Two of 11 themes are supported: polyamines and long-chain polyunsaturated fatty acids (PUFAs). [src: ibd_phage_targeting] The bile-acid theme is not supported at theme level (FDR 1.0), although its three CD-up members are all tauro/taurine forms. [src: ibd_phage_targeting] The short-chain fatty acid (SCFA) result is a null. [src: ibd_phage_targeting]

### Data and design

The analysis uses precomputed HMP2 metabolomics from the KBase Data Lakehouse mart. It takes diagnosis labels from cMD R-package sample metadata and does no raw-FASTQ reprocessing. [src: ibd_phage_targeting] Of 546 metabolomics samples, 468 (86 %) match cMD metagenomics samples by sample-ID code. The matched set covers 106 diagnosed subjects (50 CD + 30 UC + 26 nonIBD). [src: ibd_phage_targeting] The subject-level analysis uses one first-occurrence visit sample per subject, and UC is excluded from the primary contrast. [src: ibd_phage_targeting]

Per-metabolite Mann-Whitney tests, cliff_delta and Benjamini-Hochberg false discovery rate (BH-FDR) were applied to 592 named, HMDB-annotated metabolites out of 81,867 total, mostly unnamed, peaks. Of these, 579 were testable with at least 5 samples per group. [src: ibd_phage_targeting] In total, 52 metabolites pass FDR < 0.10 with |cliff_delta| > 0.20: 50 CD-up and 2 CD-down. [src: ibd_phage_targeting] Eleven chemical-class themes were tested by Fisher's exact test with BH-FDR across themes. "Supported" means FDR < 0.10 and OR > 1.5. [src: ibd_phage_targeting]

### Theme results

| Theme | Members | CD-up | OR | FDR | Supported |
|---|---|---|---|---|---|
| polyamines | 9 | 5 | 14.6 | 0.008 | yes [src: ibd_phage_targeting] |
| long_chain_PUFA | 15 | 6 | 7.9 | 0.009 | yes [src: ibd_phage_targeting] |
| acyl_carnitines | 22 | 2 | 1.06 | 1.0 | no [src: ibd_phage_targeting] |
| bile_acids | 21 | 3 | 0.56 | 1.0 | no [src: ibd_phage_targeting] |
| lipid_classes | 163 | 19 | 1.64 | 0.76 | no [src: ibd_phage_targeting] |
| short_chain_fatty_acids | 14 | 0 | not given | 1.0 | no [src: ibd_phage_targeting] |
| tma_choline | 29 | 2 | 0.78 | 1.0 | no [src: ibd_phage_targeting] |
| urobilin_porphyrin | 5 | 1 (CD-down) | 143 | 0.13 | no; the report says n=1 is too small [src: ibd_phage_targeting] |

The small tryptophan_indole, fatty_acid_amides, aromatic_AA and oxidative themes each have 0 CD-up metabolites and FDR 1.0. [src: ibd_phage_targeting]

### Polyamines

Five polyamine-theme metabolites are CD-up (cliff delta, FDR): putrescine (+0.45, 0.08), N1-acetylspermine (+0.56, 0.06), N-acetylputrescine (+0.46, 0.06), anserine (+0.43, 0.08) and diacetylspermine (+0.43, 0.08). [src: ibd_phage_targeting] The report notes that polyamines are an established IBD biomarker class, citing Pegg 2014, Wang 2018 and Franzosa 2019. [src: ibd_phage_targeting]

This result contrasts with the earlier pathway-level result. The v1.8 §9 `06_polyamine_urea` theme was CD-down at pathway level (OR=0.42) but is CD-up at metabolite level here (OR=14.6). [src: ibd_phage_targeting] The report proposes an explanation. Pool accumulation could come from more catabolism of dietary protein or mucin plus less microbial polyamine clearance, without higher biosynthesis flux. On this view the pool readout is the clinically actionable observation, and the pathway signal reflects production capacity. [src: ibd_phage_targeting]

### Long-chain PUFAs and lipids

Six of 15 long-chain PUFAs are CD-up. Five are listed with cliff delta and FDR: adrenate C22:4 (+0.55, 0.027), arachidonate C20:4 (+0.48, 0.05), docosapentaenoate C22:5 (+0.45, 0.06), docosahexaenoate C22:6 (+0.41, 0.08) and eicosapentaenoate C20:5 (+0.40, 0.09). [src: ibd_phage_targeting] The pattern covers n-6 adrenate and arachidonate, which are eicosanoid precursors, and n-3 DHA, DPA and EPA. [src: ibd_phage_targeting]

The report links this pool to the fat-metabolism/glyoxylate theme. That theme was not Fisher-significant at pathway level (OR=0.88), but the metabolite pool is theme-significant here. [src: ibd_phage_targeting] The report offers three possible explanations: impaired host fatty-acid uptake or β-oxidation, increased dietary fat mobilization, or reduced Lactobacillus/Roseburia PUFA biohydrogenation. [src: ibd_phage_targeting]

The lipid_classes theme is not supported. The report attributes this to a dilute 163-metabolite background in which most lipid classes do not shift. [src: ibd_phage_targeting] The 19 CD-up lipids are dominated by long-chain-PUFA cholesteryl esters (CEs). They include 12 CEs, 4 sphingomyelins (SMs), 1 ceramide and 2 TAGs. [src: ibd_phage_targeting] The report says CE-PUFA elevation mirrors free-PUFA elevation, because CEs are the storage form of esterified PUFAs. [src: ibd_phage_targeting]

### Acyl-carnitines

Only two long-chain acyl-carnitines are CD-up: C16 carnitine (+0.41, FDR=0.08) and C18:1 carnitine (+0.39, FDR=0.09). [src: ibd_phage_targeting] The report describes them as long-chain fatty-acid β-oxidation intermediates. It links them to fat metabolism and to Hungatella hathewayi TMA/choline metabolism. [src: ibd_phage_targeting] The theme-level OR of 1.06 is not significant. The report attributes this to a 22-carnitine background dominated by short- and medium-chain forms that do not shift in CD. [src: ibd_phage_targeting]

### Bile acids

The bile-acid theme is not supported at theme level. Only three members are CD-up, and they are free taurine, tauro-α-muricholate and tauro-β-muricholate. [src: ibd_phage_targeting] Free taurine is CD-up at cliff +0.47, and tauro-α/β-muricholate at +0.40. [src: ibd_phage_targeting] The report reads this qualitative pattern as consistent with reduced microbial 7α-dehydroxylation in CD. It also says the pattern corroborates the mechanistic role of the actionable [[entities/flavonifractor-plautii|Flavonifractor plautii]]. [src: ibd_phage_targeting] See [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]].

### SCFAs and the cross-feeding hypothesis

None of the 14 SCFAs is differentially abundant in the subject-level CD-vs-nonIBD analysis. Acetate, propionate, butyrate, valerate and hexanoate all miss FDR<0.10. [src: ibd_phage_targeting] The report offers three explanations: LC-MS (liquid chromatography-mass spectrometry) undersampling of volatile, polar SCFAs, masking of within-subject variation by the subject-averaged contrast, or small gross pool differences relative to within-subject variability. [src: ibd_phage_targeting]

The report calls this an important null for the NB07c cross-feeding hypothesis. Cohort-level butyrate differential abundance cannot confirm the *A. caccae* × pathobiont cross-feeding hypothesis. [src: ibd_phage_targeting] The report names a paired sample-level test (NB09c) as the right follow-up. It asks whether butyrate co-varies with *A. caccae* × pathobiont co-occurrence in paired metabolomics and metagenomics samples. [src: ibd_phage_targeting] See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

### Urobilin and the iron axis

Urobilin is CD-down (cliff=-0.38, FDR=0.09). [src: ibd_phage_targeting] The report describes it as a gut-bacterial bilirubin catabolite made by Clostridium/Bacteroides species expressing bilirubin reductase. [src: ibd_phage_targeting] It reads the CD-down signal as reduced bacterial bilirubin reduction, consistent with dysbiosis or loss of urobilinoid-producing commensals. [src: ibd_phage_targeting]

For the [[entities/escherichia-coli|Escherichia coli]] iron/heme axis (pathway OR=8.1), metabolomics is neutral, because LC-MS undersamples siderophores. BGC evidence from NB08a §11 corroborates the axis. [src: ibd_phage_targeting] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

## Key Findings: NB09c — Sample-level paired metabolomics × metagenomics: NB07c …

### H3d-DA verdict and convergence with earlier pathway findings

The report declares H3d-DA SUPPORTED because 52 metabolites pass differential abundance and 2 themes pass Fisher enrichment, which meets both falsifiability gates. [src: ibd_phage_targeting] NB09a adds polyamines and long-chain PUFAs (polyunsaturated fatty acids) as new mechanism axes that complement the iron, bile-acid and TMA findings. [src: ibd_phage_targeting] The convergence table compares each earlier pathway result with the metabolite result:

| Axis | Pathway-level result | Metabolite-level result | Call |
|---|---|---|---|
| Bile-acid 7α-dehydroxylation (F. plautii) | NB07b F420-BA pathways CD-up | tauro-α/β-muricholate and taurine CD-up | confirmed [src: ibd_phage_targeting] |
| TMA/choline (H. hathewayi) | OR=9.3 | C16/C18:1 carnitines CD-up; TMAO not theme-significant | partially corroborated [src: ibd_phage_targeting] |
| Fat metabolism/glyoxylate | OR=0.88 (NS) | long-chain PUFAs OR=7.9 (theme-significant) | new [src: ibd_phage_targeting] |
| Polyamine pool | OR=0.42 (CD-DOWN) | polyamines OR=14.6 (CD-UP) | new; pool is not flux [src: ibd_phage_targeting] |
| SCFA cross-feeding (NB07c) | A. caccae × pathobiont +0.39 | butyrate, acetate and propionate not differentially abundant | null at cohort level; paired analysis pending [src: ibd_phage_targeting] |

(CD = Crohn's disease; OR = odds ratio; NS = not significant.)

The report says tauro-muricholate elevation confirms the mechanistic premise for F. plautii targeting. It reads the 7α-dehydroxylation deficit as real at the metabolite-pool level, not only predicted from pathway results. [src: ibd_phage_targeting] Polyamine and PUFA elevations are proposed as sample-level CD biomarkers for treatment-response monitoring. They are not species-specific cocktail targets, because no per-species attribution is available. [src: ibd_phage_targeting] The SCFA null may mean that depleting A. caccae produces no measurable cohort-level butyrate change. The report still treats the within-sample paired test as the right test of the causal cross-feeding claim. [src: ibd_phage_targeting]

The analysis used subject-level HMP2 data (cMD-fetched sample-to-subject metadata plus mart metabolomics) under the plan's no-raw-reads constraint. [src: ibd_phage_targeting] Outputs cover 579 named metabolites with Mann-Whitney, cliff, FDR (false discovery rate) and theme assignments [src: ibd_phage_targeting], 11 themes with Fisher OR and FDR [src: ibd_phage_targeting], and the formal verdict. [src: ibd_phage_targeting]

### NB09c: paired test of SCFA cross-feeding

NB07c had left open whether A. caccae's species-level coupling with pathobionts reflected butyrogenic cross-feeding or a shared response to the CD niche. The couplings were +0.39 (E. bolteae), +0.33 (H. hathewayi), +0.31 (M. gnavus) and +0.29 (F. plautii). [src: ibd_phage_targeting] NB09c ran the paired test on 468 paired HMP2 samples that have both metabolomics and cMD MetaPhlAn3 metagenomics. [src: ibd_phage_targeting] Under strict criteria (same-sign anchor and pathobiont correlations, both |ρ|>0.20 and both FDR<0.10), it found only 7 triangles across 8 species × 583 named metabolites. [src: ibd_phage_targeting] The top candidates were caffeine, linoleoylethanolamide, urobilin and cholate, shared by various species pairs. [src: ibd_phage_targeting] None of the 7 was a butyrogenic cross-feeding intermediate. [src: ibd_phage_targeting]

The report reads the pattern as shared-niche health-direction co-occurrence. A. caccae, B. nordii, F. plautii and E. lenta are mostly commensals. Together they correlate negatively with cholate and positively with urobilin (CD-DOWN in NB09a), which the report takes to mean they co-occur in healthy or normobiotic samples. [src: ibd_phage_targeting]

Correlations by species, in the order A. caccae, B. nordii, H. hathewayi, F. plautii, E. bolteae, E. lenta, M. gnavus, E. coli:

| Metabolite | Values |
|---|---|
| butyrate | +0.10, +0.13, -0.08, -0.02, -0.04, -0.05, -0.02, +0.04 [src: ibd_phage_targeting] |
| lactate | +0.18, +0.10, +0.03, -0.23, -0.20, -0.07, +0.10, +0.24 [src: ibd_phage_targeting] |
| choline | +0.04, +0.01, -0.07, -0.16, -0.15, -0.13, +0.11, +0.25 [src: ibd_phage_targeting] |
| carnitine | -0.04, -0.02, -0.01, -0.18, -0.06, -0.04, +0.04, +0.19 [src: ibd_phage_targeting] |
| putrescine | -0.04, -0.09, -0.07, -0.02, -0.15, -0.11, +0.13, +0.19 [src: ibd_phage_targeting] |
| tryptophan | -0.09, -0.10, -0.10, -0.13, -0.10, -0.22, +0.14, +0.25 [src: ibd_phage_targeting] |

The butyrate association with A. caccae (+0.10) is significant but very weak. It is consistent with A. caccae producing butyrate at the population level. [src: ibd_phage_targeting] The report attributes the weak signal partly to LC-MS (liquid chromatography-mass spectrometry) undersampling of SCFAs, with only butyrate and propionate detected. It attributes the rest to gut butyrate pools dominated by Faecalibacterium and Roseburia. [src: ibd_phage_targeting] The report regards the opposite-sign lactate associations as its strongest evidence against cross-feeding. A. caccae is positive, while F. plautii and E. bolteae are negative, so the species occupy different cohort-level metabolic niches. [src: ibd_phage_targeting]

### E. coli dominance and the TMA/choline finding

E. coli dominates the cohort-level correlation signal. Its cadaverine correlation of +0.45 is the strongest in the curated panel. [src: ibd_phage_targeting] The report links these correlations to canonical Enterobacteriaceae metabolism: lysine decarboxylase makes cadaverine, arginine decarboxylase makes putrescine, and choline and carnitine serve as substrates. [src: ibd_phage_targeting]

The earlier cMD pathway-level H. hathewayi TMA/choline finding does not strongly replicate in HMP2 samples. The H. hathewayi–choline ρ is −0.07 (NS). [src: ibd_phage_targeting] The report therefore narrows that finding to a combined Enterobacteriaceae and Lachnospiraceae signal, not one specific to H. hathewayi. [src: ibd_phage_targeting] It proposes two possible reasons: H. hathewayi prevalence is lower in HMP2 paired samples (25 %) than in the cMD studies behind the earlier finding, and E. coli's high prevalence (50 %) and abundance variance dominate the sample-level signal. [src: ibd_phage_targeting]

### Bile-acid correlations and the 7α-dehydroxylation network

Species–bile-acid correlations, in the same species order:

| Bile acid | Values |
|---|---|
| tauro-α/β-muricholate (primary tauro) | -0.03, -0.15, 0.00, -0.04, -0.04, -0.11, +0.20, +0.06 [src: ibd_phage_targeting] |
| cholate (primary unconjugated) | -0.13, -0.18, -0.10, -0.26, -0.10, -0.13, +0.11, -0.02 [src: ibd_phage_targeting] |
| deoxycholate (secondary) | -0.07, +0.05, -0.12, +0.06, +0.17, +0.03, -0.10, -0.05 [src: ibd_phage_targeting] |
| lithocholate (secondary) | -0.05, +0.06, -0.12, +0.15, +0.18, +0.07, -0.20, -0.13 [src: ibd_phage_targeting] |
| ketodeoxycholate (secondary, oxidized) | -0.12, -0.15, -0.01, -0.19, -0.05, -0.14, +0.14, +0.24 [src: ibd_phage_targeting] |

The report reads F. plautii, E. lenta and E. bolteae as showing the predicted substrate–product signature. They correlate negatively with primary tauro-conjugated bile acids and positively with secondary unconjugated ones (deoxycholate, lithocholate). The report calls this direct sample-level confirmation of the 7α-dehydroxylation network in HMP2. [src: ibd_phage_targeting]

## Key Findings: NB10a — Kumbhari strain-adaptation gene predictor (H3b)

This part of the report reframes the earlier NB07c verdict. Paired sample-level evidence does not support the A. caccae–pathobiont cross-feeding hypothesis, and shared-environment co-occurrence is the more parsimonious explanation. [src: ibd_phage_targeting] The report then moves the ecological-cost annotation to bile-acid coupling and tests strain-level adaptation genes in the Kumbhari cohort. See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]] and [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]].

### Cross-feeding not supported

The report calls the cross-feeding hypothesis "not supported" by sample-level paired evidence and favors the shared-environment hypothesis for A. caccae × pathobiont species-level coupling. [src: ibd_phage_targeting] NB09c therefore downgrades the NB07c §10 implication that depleting pathobionts may incidentally reduce A. caccae. A substrate–product relationship is not detectable at sample level, so phage targeting of pathobionts is unlikely to deplete A. caccae substantially through metabolic coupling. [src: ibd_phage_targeting] The NB09c outputs are a species–metabolite correlation table (8 species × 583 metabolites, paired Spearman ρ and FDR), 7 strict cross-feeding-triangle candidates, a curated 7-theme panel and a formal verdict file. [src: ibd_phage_targeting] The analysis builds on NB07c module-anchor × pathobiont coupling and NB09a metabolite annotations, without raw reads. [src: ibd_phage_targeting]

### Bile-acid coupling cost replaces metabolic-coupling cost

The report replaces "metabolic-coupling cost" with bile-acid coupling cost as the primary per-target ecological-cost annotation for the NB05 actionable Tier-A set. [src: ibd_phage_targeting] The assignments rest on correlations with bile acids:

| Target | Cost | Basis |
|---|---|---|
| F. plautii | highest | cholate −0.26, lithocholate +0.15, a 7α-dehydroxylation pattern; depletion is predicted to shift bile acids toward primary inflammatory forms [src: ibd_phage_targeting] |
| E. bolteae | moderate | deoxycholate +0.17, lithocholate +0.18, a secondary 7α-dehydroxylation contributor [src: ibd_phage_targeting] |
| E. lenta | moderate | cholate −0.13, ketodeoxycholate −0.14, a partial pattern consistent with Eggerthellaceae bile-acid metabolism [src: ibd_phage_targeting] |
| H. hathewayi, M. gnavus, E. coli | low | outside the 7α-dehydroxylation network in this dataset [src: ibd_phage_targeting] |

Several lines converge on this axis:
- NB07b found F420-dependent bile-acid metabolism pathways among F. plautii within-carrier CD-up pathways. [src: ibd_phage_targeting]
- NB09a found subject-level CD-up tauro-α/β-muricholate and free taurine, consistent with reduced 7α-dehydroxylation in CD. [src: ibd_phage_targeting]
- NB09c paired data showed F. plautii, E. lenta and E. bolteae negatively associated with primary tauro-bile acids and positively with secondary unconjugated bile acids. [src: ibd_phage_targeting]
- NB05 identifies F. plautii and E. lenta as actionable Tier-A pathobionts. [src: ibd_phage_targeting]
- The literature (Franzosa 2019, Devlin & Fischbach 2015) treats a 7α-dehydroxylation deficit as a canonical IBD finding. [src: ibd_phage_targeting]

The report calls this a second six-line cross-corroboration narrative, alongside iron acquisition, and a second mechanism axis with multi-line convergence. [src: ibd_phage_targeting]

### H3b: strain-adaptation genes in Kumbhari

H3b hypothesizes that strain-adaptation gene content discriminates disease-dominant from health-dominant strains, through biologically interpretable rather than housekeeping genes. [src: ibd_phage_targeting] The test is restricted to Kumbhari/LSS-PRISM, the only project data with strain-level resolution. [src: ibd_phage_targeting] NB10a uses precomputed `ref_kumbhari_s7_gene_strain_inference` (219,121 gene × species rows; 59 species). It cross-references this with `fact_strain_competition` (15,520 strain × sample rows; 100 UHGG genome IDs in 94 LSS-PRISM participants). [src: ibd_phage_targeting]

**Coverage limit.** Only F. plautii of the actionable Tier-A core is in the 59-species panel. [src: ibd_phage_targeting] The other 5 species (H. hathewayi, M. gnavus, E. lenta, E. bolteae, E. coli) are absent, because Kumbhari focused on commensal strain heterogeneity rather than pathobiont mechanism. [src: ibd_phage_targeting] H3b therefore evaluates the methodology on 59 commensals and directly tests only one actionable Tier-A species. [src: ibd_phage_targeting]

**Result: supported.** The analysis found 23,579 FDR<0.10 strain-adaptation genes: 12,159 IBD-biased and 11,420 health-biased across 59 species. [src: ibd_phage_targeting]

| Category | IBD-biased set | Background | Fisher OR | p |
|---|---|---|---|---|
| Adaptation (7 subcategories) | 2.13 % | 1.59 % | 1.38 | 2.4e-6 [src: ibd_phage_targeting] |
| Housekeeping (6 subcategories) | 2.81 % | 4.36 % | 0.62 | 6.4e-20 [src: ibd_phage_targeting] |
| Unclassified | 95.06 % | 94.05 % | — | — [src: ibd_phage_targeting] |

The report treats 1.38× adaptation enrichment and 0.62× housekeeping depletion as the supported pattern. It rejects the strict housekeeping-domination bound at p=6.4e-20. [src: ibd_phage_targeting] Most genes are unclassified, so the categorized signal is small in absolute terms. [src: ibd_phage_targeting]

**Adaptation themes.** Mucin/glycan utilization dominated, with 94 IBD-biased genes. [src: ibd_phage_targeting] The other counts were two-component signaling 52 [src: ibd_phage_targeting], antibiotic resistance 35 [src: ibd_phage_targeting], membrane transport specialty 33 [src: ibd_phage_targeting], virulence/secretion 15 [src: ibd_phage_targeting], bile acid 15 [src: ibd_phage_targeting] and oxidative stress response 15. [src: ibd_phage_targeting]

**Recurrent orthologs.** The list gives the number of Kumbhari species in which each KEGG ortholog was IBD-biased.
- K03088, 21 species: sigma factor (RpoE/RpoS, environmental stress response) [src: ibd_phage_targeting]
- K01990, 20 species: ABC (ATP-binding cassette) transporter ATP-binding protein [src: ibd_phage_targeting]
- K06147, 19 species: ABC-2 type transport system [src: ibd_phage_targeting]
- K02529, 18 species: LacI/GalR family transcriptional regulator [src: ibd_phage_targeting]
- K07240, 17 species: TIM44-like protein [src: ibd_phage_targeting]
- K03424, 17 species: TatD-related deoxyribonuclease [src: ibd_phage_targeting]
- K08303, 16 species: SmpB (tmRNA-binding, translation rescue) [src: ibd_phage_targeting]
- K03466, 15 species: DNA topoisomerase [src: ibd_phage_targeting]

The report reads the cross-species pattern as dominated by transport, regulation, stress response and DNA repair, which it calls classic niche-adaptation signatures. [src: ibd_phage_targeting] Top gene symbols were corC (Mg²⁺/Co²⁺ efflux), luxQ (autoinducer-2 quorum sensing), pglA/rfbC (capsule polysaccharide/LPS), bepC (efflux pump) and abgB (aminobenzoyl-glutamate utilization). Each was consistent across 9-10 species. [src: ibd_phage_targeting]

### F. plautii informative null

F. plautii had zero FDR<0.10 strain-adaptation genes among 3,245 genes tested. [src: ibd_phage_targeting] The report contrasts this with its confirmed species-level CD association (NB04e, NB05) and the NB09c bile-acid associations (ρ × cholate -0.26; ρ × lithocholate +0.15). [src: ibd_phage_targeting] It interprets the CD association as operating through species-level abundance, not strain-level genomic adaptation. [src: ibd_phage_targeting] The reasoning is that 7α-dehydroxylation is presumably encoded by core bai-operon genes present in essentially all F. plautii strains. The CD signal then reflects how much F. plautii is present, not which strain dominates. [src: ibd_phage_targeting]

## Key Findings: NB11 — HMP2 serology × Tier-A pathobiont (H3e)

This part of the report covers two analyses. NB10a tests whether strain-adaptation gene content from the Kumbhari dataset carries real signal (H3b), and the report calls it SUPPORTED. NB11 tests whether anti-microbial antibody titers track Tier-A pathobiont abundance (H3e), and strict H3e is NOT SUPPORTED. Both rest on a single cohort each. [src: ibd_phage_targeting]

### NB10a: Kumbhari strain-adaptation gene predictor (H3b)

The report assigns H3b a SUPPORTED verdict. It states that the gene-content analysis carries biologically interpretable signal that is statistically distinct from housekeeping artifact. [src: ibd_phage_targeting] The shared IBD-adaptation gene set covers sigma factor, ABC (ATP-binding cassette) transport, quorum sensing, capsule LPS (lipopolysaccharide) and efflux genes. The report reads it as consistent with a biologically real "IBD-niche" signature across multiple commensal species. [src: ibd_phage_targeting] The outputs include per-species IBD-biased and health-biased gene counts for 59 species, and functional classifications for 23,579 FDR-passing genes. They also include shared KEGG ortholog (KO) and gene-symbol signals across species. [src: ibd_phage_targeting]

For *Flavonifractor plautii*, no genes passed the false discovery rate (FDR) filter, so its deep-dive file is empty. [src: ibd_phage_targeting] The report treats this null as independent corroboration of NB07b: small within-carrier pathway shifts, with the Crohn's disease (CD) signal dominated by carriage prevalence. [src: ibd_phage_targeting] It infers that phage depletion of *F. plautii* would reduce bile-acid 7α-dehydroxylation activity in proportion to the abundance reduction. It sees no strain-level escape route through within-species gene-content selection. [src: ibd_phage_targeting]

Caveats:
- The result comes from one cohort, Kumbhari/LSS-PRISM, and its cross-cohort sensitivity test was acknowledged to be weak. [src: ibd_phage_targeting]
- The proposed cross-cohort check, NB10b, was sensitivity-only. It was not run because raw reads were unavailable. [src: ibd_phage_targeting]
- 95 % of FDR-passing genes are unclassified by the gene-symbol regex. The 13-category classifier captures only annotated roles, so the functional enrichment applies to the classified subset and not to the full gene set. [src: ibd_phage_targeting]
- Actionable Tier-A coverage is limited to *F. plautii*. The report therefore sees H3b as validating the method on commensals but not as extending directly to pathobiont mechanisms. [src: ibd_phage_targeting]

### NB11: serology versus Tier-A pathobionts (H3e)

H3e proposes that anti-microbial antibody titers correlate with Tier-A pathobiont abundance within inflammatory bowel disease (IBD) patients. It uses n=67 subjects across 3 sites (Cincinnati Children's Hospital Medical Center (CCHMC), Harvard and Emory), with site as a covariate. The effect threshold is |r|>0.40, calibrated to power 0.80 at α=0.05 for n=67. [src: ibd_phage_targeting] The analysis uses cMD-fetched HMP2 MetaPhlAn3 abundance, plus 2,520 serology measurements across 12 assays. All 67 serology subjects match metagenomics. [src: ibd_phage_targeting] It crosses six serology axes (ANCA, ASCA, CBir1, IgA-ASCA, IgG-ASCA, OmpC) with 8 species for 48 tests. These are site-residualized partial Pearson correlations with Benjamini-Hochberg FDR. [src: ibd_phage_targeting] ANCA is anti-neutrophil cytoplasmic antibody.

#### Cohort sanity check

The cohort is n=32 CD, 14 UC and 21 nonIBD subjects. [src: ibd_phage_targeting] All six axes show the canonical IBD direction, which the report takes as validating standard immunology. [src: ibd_phage_targeting] OmpC matches only partially. [src: ibd_phage_targeting]

- ANCA: mean 17.8 in CD and 42.6 in UC. [src: ibd_phage_targeting]
- ASCA: mean 0.28 in CD and 0.0 in UC. [src: ibd_phage_targeting]
- CBir1: mean 29.0 in CD and 13.7 in UC. [src: ibd_phage_targeting]
- IgA ASCA: mean 14.2 in CD and 1.2 in UC. [src: ibd_phage_targeting]
- IgG ASCA: mean 15.0 in CD and 3.6 in UC. [src: ibd_phage_targeting]
- OmpC: mean 9.3 in CD and 7.6 in UC. [src: ibd_phage_targeting]

#### Species associations

No pair reaches the threshold. The top observed |r| is 0.31 at FDR=0.40, so strict H3e is NOT SUPPORTED. The report labels the verdict PARTIAL. [src: ibd_phage_targeting]

- ANCA × *M. gnavus*: partial r=+0.31, raw ρ=+0.24, FDR=0.40. Harvard r=+0.456 (p=0.008); CCHMC r=−0.03 NS. [src: ibd_phage_targeting]
- OmpC × *E. lenta*: partial r=+0.29, raw ρ=+0.10, FDR=0.40. CCHMC r=−0.02 NS; Harvard r=+0.14 NS. [src: ibd_phage_targeting]
- ANCA × *H. hathewayi*: partial r=+0.23, raw ρ=+0.16, FDR=0.59. Harvard r=+0.345 (p=0.050); CCHMC r=+0.02 NS. [src: ibd_phage_targeting]
- IgA-ASCA × *E. coli*: partial r=+0.23, raw ρ=+0.22, FDR=0.59. Harvard r=+0.30 (p=0.09); CCHMC r=+0.06 NS. [src: ibd_phage_targeting]
- CBir1 × *E. bolteae*: partial r=+0.22, raw ρ=+0.22, FDR=0.59. CCHMC r=+0.381 (p=0.035); Harvard r=+0.04 NS. [src: ibd_phage_targeting]
- ANCA × *F. plautii*: partial r=+0.22, raw ρ=+0.32, FDR=0.59. CCHMC r=+0.443 (p=0.013); Harvard r=+0.25 NS. [src: ibd_phage_targeting]

Most associations concentrate in one of the two productive sites and dilute when the cohort is aggregated. [src: ibd_phage_targeting] With Harvard 33, CCHMC 31 and Emory 3 subjects, single-site partial r reaches |r|≈0.40–0.46. The pooled cohort is pulled toward the null, so the strict threshold is not met. [src: ibd_phage_targeting]

The report offers interpretations, not tests of mechanism:
- Positive ANCA links to *M. gnavus*, *H. hathewayi* and *F. plautii* are consistent with high-pathobiont-burden states triggering a broader humoral response. [src: ibd_phage_targeting]
- CBir1 × *E. bolteae* is called mechanistically coherent, since CBir1 is anti-flagellin and *E. bolteae* is flagellated. [src: ibd_phage_targeting]
- IgA-ASCA × *E. coli* is called the most mucosal-immunity-relevant axis, and its +0.23 is read as consistent with *E. coli* outer-antigen recognition. [src: ibd_phage_targeting]

#### Implications and caveats

Serology is not yet a quantitative per-target prioritization signal for cocktail design in this cohort. [src: ibd_phage_targeting] It can serve as a CD-vs-UC stratifier, because the ANCA-UC, ASCA-CD and CBir1-CD axes are intact. It cannot serve as a per-target abundance predictor. [src: ibd_phage_targeting] The |r|≈0.31 ceiling means a subject's anti-*M. gnavus* ANCA titer cannot confidently predict that subject's *M. gnavus* abundance. [src: ibd_phage_targeting]

Limits stated by the report:
- n=67 across 3 uneven sites is structurally low-power for |r|>0.40 at α=0.05 with 48-test correction. [src: ibd_phage_targeting]
- Subject-level aggregation discards longitudinal information from multiple visits. Mixed-effects regression could add power, but unbalanced visit counts complicate interpretation. [src: ibd_phage_targeting]
- OmpC and ANCA cross-react with related antigens, so per-species attributions are correlative rather than exclusive. [src: ibd_phage_targeting]
- The single-cohort limit is structural, with no project-internal replication path. [src: ibd_phage_targeting]
- Multi-cohort meta-analysis is the next step, but it is outside project scope. [src: ibd_phage_targeting]

Site-stratified results for the top 10 pairs are provided separately. [src: ibd_phage_targeting]

### Provenance

NB10a was run with `run_nb10a.py` under plan v1.7 H3b and v1.9 (no raw reads). [src: ibd_phage_targeting]

## Key Findings: NB09b — Cross-cohort metabolomics bridge (HMP2 NB09a → FRANZOSA_2019)

This part of the report asks whether the Crohn's disease (CD) metabolite signatures found in HMP2 replicate in FRANZOSA_2019, an independent cohort. Replication is strong for three of eight testable themes (urobilin, acyl-carnitines, long-chain polyunsaturated fatty acids, PUFA). Polyamines could not be tested, and bile-acid evidence rests on a different stream. [src: ibd_phage_targeting]

### Setup and matching

The earlier analysis NB09a found polyamines (odds ratio, OR=14.6) and long-chain PUFAs (OR=7.9) as CD-up theme signatures in HMP2. Urobilin was CD-down. [src: ibd_phage_targeting] CD-up tauro-α/β-muricholate and free taurine corroborate the reported *Flavonifractor plautii* 7α-dehydroxylation deficit. [src: ibd_phage_targeting] See [[entities/flavonifractor-plautii]].

NB09b tests these signatures in FRANZOSA_2019 (220 participants: 88 CD, 76 ulcerative colitis, 56 Control). [src: ibd_phage_targeting] It uses precomputed `fact_metabolomics` only and no raw reads. [src: ibd_phage_targeting] A mouse ileal tissue dataset (DAVE_SAMP_METABOLOMICS) was dropped because it is not human IBD data. [src: ibd_phage_targeting] Franzosa metabolite IDs use an `[m/z]_[RT]` format with no compound names in the mart. [src: ibd_phage_targeting] HMP2 named metabolites were therefore bridged to Franzosa peaks by m/z (±0.005 Da) within method. [src: ibd_phage_targeting] Retention time (RT) was not used, because the two cohorts' runs used different gradients and columns. [src: ibd_phage_targeting]

In all, 122 of 592 named HMP2 metabolites matched a Franzosa peak, and 118 of those 122 passed Franzosa CD-vs-Control differential-abundance filters. [src: ibd_phage_targeting]

### Per-theme concordance

Sign concordance varied widely by theme. Urobilin, acyl-carnitines and long-chain PUFAs reached 75% or more. [src: ibd_phage_targeting] Counts are matched metabolites, CD-up in HMP2, CD-up in Franzosa, and sign-concordant.

| Theme | Matched | CD-up HMP2 | CD-up Franzosa | Concordant | Median Franzosa cliff | Claim |
|---|---|---|---|---|---|---|
| urobilin_porphyrin | 3 | 0 | 0 | 3 (100 %) | −0.747 | [src: ibd_phage_targeting] |
| acyl_carnitines | 5 | 4 | 5 | 4 (80 %) | +0.531 | [src: ibd_phage_targeting] |
| long_chain_PUFA | 12 | 12 | 9 | 9 (75 %) | +0.273 | [src: ibd_phage_targeting] |
| aromatic_AA_metabolites | 3 | 3 | 2 | 2 (67 %) | +0.181 | [src: ibd_phage_targeting] |
| bile_acids_primary | 7 | 5 | 4 | 4 (57 %) | +0.252 | [src: ibd_phage_targeting] |
| lipid_classes | 21 | 14 | 4 | 11 (52 %) | −0.069 | [src: ibd_phage_targeting] |
| tryptophan_indole | 2 | 1 | 0 | 1 (50 %) | −0.199 | [src: ibd_phage_targeting] |
| bile_acids_secondary | 5 | 3 | 2 | 2 (40 %) | −0.159 | [src: ibd_phage_targeting] |

Overall concordance was 64% (76 of 118). There were 9 strict replications (both FDR<0.10, |cliff|>0.20 and sign match). The report calls these the project's strongest cross-cohort metabolomics signal. [src: ibd_phage_targeting] It calls 64% moderately above the 50% chance baseline and the 9 strict replications firmly above chance. [src: ibd_phage_targeting]

### Replicated findings

- **Urobilin:** The report names urobilin CD-down its strongest replicated metabolite-level finding. It reads it as consistent loss of bilirubin-reducing commensals in CD across HMP2 and Franzosa. This is an interpretation. [src: ibd_phage_targeting]
- **Acyl-carnitines:** The C16 and C18:1 long-chain acyl-carnitines flagged CD-up in HMP2 are independently elevated in Franzosa CD samples. [src: ibd_phage_targeting] The report links this to the fat-metabolism/glyoxylate theme and impaired β-oxidation in inflamed mucosa. This is a proposed mechanism. [src: ibd_phage_targeting]
- **PUFAs:** Adrenate, arachidonate, DHA and DPA replicate cleanly. This supports the report's view that elevation of the inflammatory eicosanoid-precursor pool is robust across cohorts. [src: ibd_phage_targeting] Eicosapentaenoate (EPA) has the opposite sign in 1 of 3 non-concordant cases. The report suggests cohort differences in dietary fish-oil supplementation as a possible cause. [src: ibd_phage_targeting]

### Null result: polyamines

The polyamine bridge failed, with 0 m/z matches. [src: ibd_phage_targeting] None of the 9 polyamines behind the HMP2 OR=14.6 enrichment was recovered. [src: ibd_phage_targeting] The report notes that polyamines are low-mass HILIC-pos compounds (putrescine 89.11, spermidine 146.17, spermine 203.22). The m/z tolerance and the Franzosa method-library overlap yield no matches. [src: ibd_phage_targeting] The HMP2 polyamine OR=14.6 therefore remains a single-cohort finding. Replication needs external Franzosa supplementary tables with compound names, which are outside the project's no-raw-reads scope. [src: ibd_phage_targeting]

### Bile acids: a different evidence stream

Cross-cohort bile-acid concordance was weak: 57% for primary and 40% for secondary bile acids. [src: ibd_phage_targeting] The report does not treat this as refuting its bile-acid story. It holds that bile-acid pool sizes are more susceptible to dietary and antibiotic confounding than within-cohort species × metabolite correlation. [src: ibd_phage_targeting] It judges the HMP2 paired-sample substrate-product signature for *F. plautii*, *Eggerthella lenta* and *Enterocloster bolteae* the more robust evidence. [src: ibd_phage_targeting] See [[entities/eggerthella-lenta]] and [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]].

In paired HMP2 samples, *F. plautii* correlates with cholate at ρ = −0.26 and with lithocholate at +0.15. [src: ibd_phage_targeting] This is a species × metabolite correlation, not CD-vs-Control aggregate differential abundance. [src: ibd_phage_targeting] The report reads the mechanistic signature for active 7α-dehydroxylation as preserved within paired samples despite the cross-cohort confounding. [src: ibd_phage_targeting] Its six-line bile-acid narrative is anchored on paired sample-level evidence and literature mechanism, not on cohort-aggregate replication. [src: ibd_phage_targeting] The two streams differ, so weakness in one need not invalidate the other. [src: ibd_phage_targeting]

### Caveats

- Only 122 of 592 named HMP2 metabolites could be matched, using m/z alone. [src: ibd_phage_targeting]
- Several themes rest on very few matched metabolites (2 to 7). [src: ibd_phage_targeting]
- Polyamines remain untested. [src: ibd_phage_targeting]

### Outputs

Outputs are `data/nb09b_cross_cohort_concordance.tsv` (122 matched pairs with cliff_delta and sign-match flags), `data/nb09b_theme_replication.tsv` and `data/nb09b_cross_cohort_verdict.json`. The scripts are `run_nb09b.py` and `run_nb11.py`. The formal NB11 H3e verdict is in `data/nb11_h3e_verdict.json`. [src: ibd_phage_targeting]

## Key Findings: NB09d — H3d-clust metabolite-feature ecotype LOSO stability

This part of the report tests whether clustering on metabolite features gives more cross-cohort-stable ecotypes than the taxonomic framework. It does not: the hypothesis is not supported, and the cluster structure reflects cohort batch rather than diagnosis. [src: ibd_phage_targeting] A companion NB07d analysis of paired HMP2 subjects found strong shared taxonomy–metabolomics structure. [src: ibd_phage_targeting]

### H3d-clust design and result

NB09d tests H3d-clust, the hypothesis that metabolite-derived clustering has higher cross-cohort stability than taxonomic-derived ecotypes. It uses the NB09b m/z-bridge panel and pooled HMP2 and Franzosa metabolomics, with no raw reads. [src: ibd_phage_targeting] The method pools 326 subjects (106 HMP2 × 220 Franzosa) on 111 unique m/z-bridge metabolite features. It standardizes each metabolite, applies PCA to 15 components, and runs K-means with K=4. [src: ibd_phage_targeting] Baselines are the NB04f taxonomic LOSO ARI (0.113) and the NB04b bootstrap ARI (0.16). [src: ibd_phage_targeting] LOSO is leave one substudy out and ARI is the adjusted Rand index.

The verdict is NOT SUPPORTED. Cross-cohort LOSO ARI was 0.000, against the 0.113 taxonomic baseline. [src: ibd_phage_targeting] Held-out HMP2 gave 0.000, held-out Franzosa gave 0.000, and the mean was 0.000. [src: ibd_phage_targeting] The within-pooled bootstrap (80 % × 30) gave ARI 0.937 against 0.16 for NB04b taxonomic. [src: ibd_phage_targeting] The report calls this figure misleading as biological stability evidence. It measures how reproducibly K-means recovers the cohort-batch structure under subsampling, not whether the clusters are biologically informative. [src: ibd_phage_targeting]

### Clusters follow cohort, not diagnosis

Each of the four clusters is 100 % from a single cohort. [src: ibd_phage_targeting]

| Cluster | Subjects | Cohort | Diagnoses |
|---|---|---|---|
| 0 | 86 | Franzosa 100 % | 46 Control + 30 UC + 10 CD [src: ibd_phage_targeting] |
| 1 | 58 | HMP2 100 % | 29 CD + 23 UC + 6 nonIBD [src: ibd_phage_targeting] |
| 2 | 134 | Franzosa 100 % | 78 CD + 46 UC + 10 Control [src: ibd_phage_targeting] |
| 3 | 48 | HMP2 100 % | 21 CD + 7 UC + 20 nonIBD [src: ibd_phage_targeting] |

PC1 explains 79 % of total variance and cleanly separates HMP2 (PC1 ≈ +12) from Franzosa (PC1 ≈ −5). [src: ibd_phage_targeting] PCs 2–15 together explain ~10 % of variance and carry the diagnosis information. [src: ibd_phage_targeting] Within each cohort the clusters do carry diagnosis information (cluster × diagnosis χ²(6)=88.3, p=7e-17). Cluster boundaries are still mostly aligned with cohort boundaries. [src: ibd_phage_targeting]

### Interpretation and consequences

The report concludes that unaddressed batch effects dominate m/z-bridge metabolomics cluster structure. [src: ibd_phage_targeting] It attributes the portability of taxonomic ecotypes to MetaPhlAn3 relative abundances, which are unitless and compositionally constrained. That constraint acts as a natural normalization of cohort differences. [src: ibd_phage_targeting] This is the report's explanation, not a separate test. Metabolite clustering inherits absolute-intensity differences between LC-MS (liquid chromatography-mass spectrometry) runs. These come from instruments, ionization tuning and solvent batches. The report says clustering needs explicit batch correction (ComBat, SVA, RUV or quantile normalization) first. [src: ibd_phage_targeting]

For the project, the NB01b consensus K=4 taxonomic ecotypes remain the primary basis for Pillar 4–5 cocktail design. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]]. Refitting ecotypes on metabolite features is not a drop-in replacement, because it would need external batch-correction infrastructure. [src: ibd_phage_targeting] The report treats the NB09c §13 within-HMP2 paired sample-level species–metabolite correlations as the more robust mechanism evidence. Cohort-aggregate cross-cohort metabolite differential abundance is dominated by batch effects (NB09b primary BAs 57 % concord; secondary BAs 40 %). [src: ibd_phage_targeting] The report declares the H3 falsifiability framework fully closed. H3a (a/c), H3a (b) v1.8, H3a-new, H3b, H3c, H3d-DA, H3d-clust and H3e all have formal verdicts. [src: ibd_phage_targeting] See also [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

### Limits of the NB09d verdict

- No batch correction was applied. The report expects ComBat, SVA or RUV would likely improve cross-cohort LOSO ARI substantially. The verdict covers only raw m/z-bridge clustering without batch correction. [src: ibd_phage_targeting]
- Within-cohort metabolite ecotypes might still serve single-laboratory clinical translation. The failure concerns cross-cohort portability. [src: ibd_phage_targeting]
- The feature space is small, at 111 unique features. A space of 500-1000 name-annotated metabolites might give different results. It would need external Franzosa supplementary annotations, which are out of scope under plan v1.9. [src: ibd_phage_targeting]
- K=4 was imposed by the plan to match the taxonomic framework. The natural cluster count might be K=2, separating HMP2 from Franzosa. [src: ibd_phage_targeting]

### NB07d: paired HMP2 taxonomy–metabolomics structure

NB07d could not use HMP2 pathways. The KBase Data Lakehouse pathway-abundance table contains only CMD_IBD_PATHWAYS, and the project disallowed raw-read processing. [src: ibd_phage_targeting] Because mofapy2 was unavailable, it used sklearn canonical correlation analysis (CCA) on per-modality principal-component scores. [src: ibd_phage_targeting] The data were 106 paired HMP2 CSM* subjects. They had 130 ≥10%-prevalence CLR-transformed species and 582 named log10-intensity metabolites with ≥30% non-NaN coverage. [src: ibd_phage_targeting] Each modality was reduced to 30 components, and CCA gave 4 canonical pairs. [src: ibd_phage_targeting] All four canonical correlations were very strong: r = 0.964, 0.928, 0.911, 0.889. [src: ibd_phage_targeting]

Only CC1 clearly discriminated diagnosis. It had mean CD +0.235, UC +0.123 and nonIBD −0.593, a CD-vs-nonIBD Cliff effect of +0.498 and Mann–Whitney p = 4e-4. [src: ibd_phage_targeting] CC1 separated CD from nonIBD by ~0.83 SD, with UC in between. The report reads this as consistent with UC being a milder dysbiosis state on the same axis. [src: ibd_phage_targeting] The other three axes were not strongly diagnosis-discriminative:

- CC2 had Cliff effect +0.092 and p = 0.51. [src: ibd_phage_targeting]
- CC3 had Cliff effect −0.146 and p = 0.30. [src: ibd_phage_targeting]
- CC4 had Cliff effect −0.274 and p = 0.05. [src: ibd_phage_targeting]

All 6 actionable Tier-A core species loaded CD-positive on CC1. [src: ibd_phage_targeting] The loadings were M. gnavus +0.195 [src: ibd_phage_targeting], E. coli +0.173 [src: ibd_phage_targeting], F. plautii +0.153 [src: ibd_phage_targeting], H. hathewayi +0.144 [src: ibd_phage_targeting], E. lenta +0.109 [src: ibd_phage_targeting] and E. bolteae +0.103. [src: ibd_phage_targeting] Oral-gut Tier-B candidates also loaded positively: V. parvula +0.194 [src: ibd_phage_targeting] and A. intestini +0.161. [src: ibd_phage_targeting] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

## Key Findings: NB07d — MOFA+-style HMP2 multi-omics joint factor pilot (taxonomy + …

The NB07d pilot ran a canonical correlation analysis (CCA) on HMP2 species and metabolite data as a stand-in for MOFA+. The report judges it successful: the first canonical component (CC1) is described as the unified Crohn's disease (CD)-versus-nonIBD axis in joint species–metabolite space. [src: ibd_phage_targeting] The evidence is a single pilot on n=106 subjects, which the report calls modest for a 4-factor decomposition. [src: ibd_phage_targeting]

### Main result

The report reads the dominant HMP2 cross-modality structure as pathobiont-module dominance plus its metabolic consequences. It says this structure is detectable as one canonical correlation pair at r=0.96. [src: ibd_phage_targeting] The report says CC1 independently rediscovers the NB06 pathobiont-module biology. CCA joint factors and CLR (centered log-ratio)–Spearman–Louvain modules converge on the same biology. [src: ibd_phage_targeting]

### Species loadings

Oral-gut Tier-B candidate V. atypica loaded positively on CC1 at +0.151. [src: ibd_phage_targeting] Ecotype-defining commensals from NB01b loaded negatively, in the commensal direction. These were R. bromii (−0.173) [src: ibd_phage_targeting], R. bicirculans (−0.170) [src: ibd_phage_targeting] and A. putredinis (−0.169). [src: ibd_phage_targeting] L. eligens [src: ibd_phage_targeting] and B. intestinihominis [src: ibd_phage_targeting] also loaded negatively.

Ecotype structure was implicit in these loadings. E1-Bact2-transitional and E3-Bacteroides-expanded species loaded positively, and E0-commensal species loaded negatively. [src: ibd_phage_targeting] See [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

### Metabolite loadings

Metabolites that the report treats as depleted in CD loaded negatively on CC1:
- Urobilin, across 3 instances, with max −0.143. The report ties this to its cross-cohort CD-depletion narrative. [src: ibd_phage_targeting]
- Glycodeoxycholate, −0.113. [src: ibd_phage_targeting]
- Lithocholate, −0.080. [src: ibd_phage_targeting]
- Caproate, −0.113. [src: ibd_phage_targeting]

The fatty-acid amides and polyamines loaded positively, in the CD-elevated direction. The sphingosine isomers, 7-methylguanine and ADMA/SDMA also loaded positively. The report links each group to earlier findings:

| Group | CC1 loadings | Report's linked finding |
|---|---|---|
| Fatty-acid amides | linoleoyl ethanolamide ×2 (+0.110, +0.106) [src: ibd_phage_targeting]; palmitoylethanolamide +0.108 [src: ibd_phage_targeting] | NB08a ebf/ecf biosynthetic gene cluster (BGC) family CD-up, p<1e-31 (Elmassry 2025) [src: ibd_phage_targeting] |
| Sphingosine isomers | sphingosine-isomer1/2 (+0.109, +0.105) | CD-up lipid classes [src: ibd_phage_targeting] |
| 7-Methylguanine | +0.121 | H. hathewayi purine recycling [src: ibd_phage_targeting] |
| Polyamines | N-acetylputrescine +0.105 [src: ibd_phage_targeting]; diacetylspermine +0.091 [src: ibd_phage_targeting]; cadaverine +0.086 [src: ibd_phage_targeting]; putrescine +0.084 [src: ibd_phage_targeting] | NB09a polyamine odds ratio (OR)=14.6 and NB09c cadaverine × E. coli ρ=+0.45 [src: ibd_phage_targeting] |
| Long-chain polyunsaturated fatty acids (PUFAs) | docosapentaenoate ×2 (+0.092, +0.091) [src: ibd_phage_targeting]; adrenate +0.081 [src: ibd_phage_targeting]; arachidonate +0.048 [src: ibd_phage_targeting] | NB09a OR=7.9 and NB09b 75 % cross-cohort concordance [src: ibd_phage_targeting] |
| ADMA/SDMA | +0.099 | Uremic-toxin marker; arginine catabolism connected to TMA/choline [src: ibd_phage_targeting] |

### Caveats and open work

- **Method.** The report states that CCA on principal-component scores captures the same canonical-correlation signal as MOFA+ in the two-modality case. [src: ibd_phage_targeting] CCA does not model modality-specific factors, which stay in the per-modality PCA components. [src: ibd_phage_targeting] MOFA+ could add ~5–10 unique factors per modality beyond the joint factors. [src: ibd_phage_targeting]
- **Scope.** NB07d is a pilot. It does not replace a full three-modality MOFA+ with factor-relevance gating. [src: ibd_phage_targeting]
- **Over-alignment.** All 4 canonical correlations exceeded 0.88. The report says this suggests over-aligned per-modality PCAs, and that a proper MOFA+ would impose sparsity to gate factor count. [src: ibd_phage_targeting]
- **Sample size.** n=106 subjects is modest for a 4-factor decomposition. CC2, CC3 and CC4 are suggestive but not strongly disease-discriminative. [src: ibd_phage_targeting]
- **Third modality.** Adding pathways would need cMD_IBD reprocessing on cohort-aligned subjects (NB07a) and sample-level pairing. The existing cMD_IBD pathway slice is not paired with HMP2 metabolomics. [src: ibd_phage_targeting]
- **Ecotype.** The report proposes regressing factor scores on ecotype and diagnosis. This would test whether residual factor variance encodes ecotype-specific biology. [src: ibd_phage_targeting]

### Outputs and run

NB07d wrote the top 15 species and 15 metabolite loadings for each of 4 canonical components. [src: ibd_phage_targeting] It also wrote the 106 subjects' CC1-4 species, metabolite and joint scores plus diagnosis [src: ibd_phage_targeting], and a formal pilot verdict file. [src: ibd_phage_targeting] The run used run_nb07d.py. The report says its multi-modal QC prerequisites NB04e, NB07a and NB09a all passed. [src: ibd_phage_targeting]

## Key Findings: NB12 — Pathobiont × phage targetability matrix (Pillar 4 opener)

NB12 builds a literature-curated matrix of phage availability for each actionable pathobiont, and NB13 starts the quantitative follow-up for *E. coli*. The main result is that phage availability is weakest for the species with the highest NB05 scores. The matrix rests on a 12-organism literature synthesis, so it is qualitative. The PhageFoundry cocktail analysis is a direct measurement on one *E. coli* dataset. [src: ibd_phage_targeting]

### Design of the matrix

The Pillar 4 framework layers a per-pathobiont phage-availability profile (Tier-B in the project's 4-tier rubric) on the NB05 actionable Tier-A scoring and the Pillar-3 mechanism profile. [src: ibd_phage_targeting] NB12 builds the matrix from `ref_phage_biology`, a 12-organism literature-curated synthesis from indicator_taxa_literature_review. [src: ibd_phage_targeting] The Tier-B score is a 0-3 ordinal scale: 0 means no known phages, 1 temperate or limited, 2 lytic literature, and 3 clinical trial or commercial cocktail. [src: ibd_phage_targeting] The matrix is saved as a TSV with NB05, phage and Pillar-5 class, and the verdict JSON holds the formal verdict, the Pillar-4/5 hand-off and the limitations. [src: ibd_phage_targeting]

### Per-pathobiont results

The 6 actionable Tier-A pathobionts fall into 4 phage-availability classes. Class 3 (clinical) holds *E. coli*. Class 2 (lytic literature) holds *E. lenta* and *E. bolteae*. Class 1 (temperate-limited) holds *M. gnavus*. Class 0 (gap) holds *H. hathewayi* and *F. plautii*. [src: ibd_phage_targeting]

| Species | NB05 | Phage score | Lifestyle | Bile-acid cost | Note |
|---|---|---|---|---|---|
| *H. hathewayi* | 4.0 | 0 | none | low | Gap. It has the highest NB05 score but no known phages, so it is the priority for external INPHARED + IMG/VR queries. [src: ibd_phage_targeting] |
| *M. gnavus* | 3.8 | 1 | temperate | low | Limited. All 6 known phages are temperate, which motivates lytic-locked engineering or a biochemical glucorhamnan-synthesis target. [src: ibd_phage_targeting] |
| *E. coli* (AIEC) | 3.6 | 3 | lytic + clinical | low | Tier-1 clinical and the most advanced target. It has the EcoActive cocktail (7 lytic phages, clinical trials) and the FimH-targeting HER259. [src: ibd_phage_targeting] |
| *E. lenta* | 3.3 | 2 | lytic literature | moderate | Tier-2. The siphovirus PMBT5 is characterized, and the non-BGC drug-metabolism mechanism is attributed to Koppel 2018. [src: ibd_phage_targeting] |
| *F. plautii* | 3.3 | 0 | unknown (not in ref) | highest | Gap plus high cost. Phage targeting is deprioritized in favor of bile-acid monitoring or biochemical alternatives. [src: ibd_phage_targeting] |
| *E. bolteae* | 2.8 | 2 | lytic literature | moderate | Tier-2. PMBT24 is a virulent, 99,962 bp Kielviridae phage and the best-characterized lytic phage among gut-anaerobe Tier-A targets. [src: ibd_phage_targeting] |

The two highest-NB05-scored species, *H. hathewayi* (4.0) and *M. gnavus* (3.8), have the weakest phage availability. [src: ibd_phage_targeting] *F. plautii* also has the highest bile-acid coupling cost, so phage targeting may give way to bile-acid-binding co-therapy. [src: ibd_phage_targeting]

### Hand-off to Pillar 5

The Pillar 4 to Pillar 5 hand-off defines 3 design strategies for the 6 actionable Tier-A targets. [src: ibd_phage_targeting]

- **Direct phage targeting (Tier-1):** the *E. coli* AIEC subset with the EcoActive clinical-trial cocktail. This requires a strain-resolution diagnostic per NB07b/NB08a. [src: ibd_phage_targeting]
- **Phage targeting with monitoring (Tier-2):** *E. lenta* (PMBT5) and *E. bolteae* (PMBT24), and *M. gnavus* if lytic-locked engineering succeeds. [src: ibd_phage_targeting]
- **Phage gap, alternatives needed:**
  - *H. hathewayi* is the top priority for external database queries. If no phages turn up, the fallback is GAG-degrading enzyme inhibitors. [src: ibd_phage_targeting]
  - *M. gnavus* would use biochemical glucorhamnan-synthesis targets (Henke 2019) if lytic-locked engineering fails. [src: ibd_phage_targeting]
  - *F. plautii* gets the lowest Pillar-5 priority because of its bile-acid cost. The report suggests deprioritizing it or co-administering UDCA (ursodeoxycholic acid) or a bile-acid-binding agent. [src: ibd_phage_targeting]

### Quantitative data found during NB12

The report deferred the quantitative data found during NB12 execution to NB13. [src: ibd_phage_targeting]

- HMP2 fact_viromics has 3,039 sample-rows of direct phage observations in patient stool. [src: ibd_phage_targeting]
- It contains 16 unique *E. coli* phages and 13 unique *Klebsiella* phages. [src: ibd_phage_targeting]
- It has no observations of phages targeting *H. hathewayi*, *M. gnavus*, *F. plautii*, *E. lenta* or *E. bolteae*. The report says this confirms the gut-anaerobe phage coverage gap seen in the literature curation. [src: ibd_phage_targeting]
- ref_viromics_cd_vs_nonibd holds pre-computed CD (Crohn's disease) versus non-IBD differential abundance for 22 viruses. [src: ibd_phage_targeting] The top hit is the microvirus Gokushovirus WZ-2015a, depleted in CD with log2FC=-2.7 and FDR (false discovery rate)=1e-11. [src: ibd_phage_targeting]
- The KBase Data Lakehouse Spark authentication was restored mid-execution, so the PhageFoundry quantitative analysis was promoted to NB13. [src: ibd_phage_targeting]

### NB13: PhageFoundry cocktail design for *E. coli*

NB12 gave the qualitative foundation. NB13 adds a strain-resolution cocktail-design layer from the KBase Data Lakehouse `phagefoundry_strain_modelling` dataset. The dataset has 96 phages × 188 strains × 17,672 experimentally tested susceptibility pairs, from the Gaborieau 2025-10-02 phage-prediction experiment (AUC=0.88). [src: ibd_phage_targeting] The report calls it the definitive *E. coli* AIEC phage-cocktail design dataset for this project. [src: ibd_phage_targeting] Of the pairs, 3,929 were susceptible and 13,743 resistant, a 22 % susceptibility rate. [src: ibd_phage_targeting] See also [[entities/phagefoundry]].

Greedy minimum-set-cover design seeks the smallest cocktail covering at least a given percentage of the 188 strains. [src: ibd_phage_targeting]

| Target | Phages | Coverage achieved | Phages added |
|---|---|---|---|
| ≥50 % | 1 | 63.8 % | DIJ07_P2 (*Phapecoctavirus*) [src: ibd_phage_targeting] |
| ≥75 % | 2 | 81.4 % | + LF73_P1 (*Tequatrovirus*) [src: ibd_phage_targeting] |
| ≥90 % | 4 | 92.6 % | + AL505_Ev3 + 55989_P2 [src: ibd_phage_targeting] |
| ≥95 % | 5 | 94.7 % | + LF110_P2 [src: ibd_phage_targeting] |
| ≥99 % | 8 | 98.4 % | + NIC06_P2 + LF73_P4 + BCH953_P4 [src: ibd_phage_targeting] |

For the ≥95 % target, the 5-phage cocktail covered 94.7 % of strains, just under the stated threshold. The report states that a 5-phage cocktail covers 94.7 % of 188 *E. coli* strains in PhageFoundry. [src: ibd_phage_targeting] This cocktail is comparable in size to the EcoActive 7-phage clinical-trial cocktail, and the report calls both 5-7 phages. [src: ibd_phage_targeting] The top-ranked phage DIJ07_P2 alone lyses 63.8 % of strains, which the report calls remarkable single-phage breadth. [src: ibd_phage_targeting]

### AIEC relevance by phylogroup

The report cites Dogan 2014/Dubinsky 2022 for AIEC strains being predominantly phylogroup B2 (~80 %) and D (~20 %). [src: ibd_phage_targeting] The PhageFoundry phages by host phylogroup are:

| Phylogroup | Phages | Median host range | Maximum | Label |
|---|---|---|---|---|
| B2 | 50 | 21.3 % | 63.3 % | Primary AIEC phylogroup [src: ibd_phage_targeting] |
| D | 15 | 13.8 % | 63.8 % | Secondary AIEC phylogroup [src: ibd_phage_targeting] |
| A | 10 | 16.5 % | 39.4 % | Predominantly commensal [src: ibd_phage_targeting] |
| B1 | 9 | 20.2 % | 50.5 % | Predominantly commensal [src: ibd_phage_targeting] |
| Other (C/0/G) | 10 | varied | varied | Rare [src: ibd_phage_targeting] |

The report states that 65 of 94 phages (69 %) were isolated against B2/D hosts and calls this strongly AIEC-relevant. [src: ibd_phage_targeting] Several of the broadest-host-range B2/D phages were isolated against canonical AIEC reference strains:

- LF82_P8 (*Mosigvirus*) has a 60.1 % host range. LF82 is the AIEC reference strain (Darfeuille-Michaud 2004). [src: ibd_phage_targeting]
- LF73_P1 has a 62.8 % host range, and its host LF73 is also a CD-associated AIEC strain. [src: ibd_phage_targeting]
- 536_P7 / 536_P9 come from *E. coli* 536, which the report identifies as a UPEC/B2 archetype. [src: ibd_phage_targeting]

## Key Findings: NB14 — HMP2 endogenous phageome × ecotype × diagnosis

This part of the report designs an Escherichia coli phage cocktail from the [[entities/phagefoundry]] susceptibility data (NB13). It then adds in-vivo phage data from the Human Microbiome Project 2 (HMP2) cohort (NB14). The cocktail result comes from experimental susceptibility data. The report's data do not validate in-vivo gut delivery, and the listed HMP2 E. coli phages do not match PhageFoundry phages by name. [src: ibd_phage_targeting]

### Cocktail design from PhageFoundry (NB13)

NB13 uses 96 phages × 188 strains × 17,672 pairs of experimental susceptibility data. It reports that a 5-phage cocktail covers 95 % of E. coli strains, and that 69 % of phages are of AIEC-relevant (adherent-invasive E. coli) phylogroup. [src: ibd_phage_targeting] The report treats PhageFoundry as the primary cocktail-design source. It describes PhageFoundry as research and clinical isolates with experimental susceptibility, and describes HMP2 viromics as natural phages from patient stool. [src: ibd_phage_targeting]

- Tier-1 cocktail: 5 phages with stated 95 % strain coverage: DIJ07_P2 + LF73_P1 + AL505_Ev3 + 55989_P2 + LF110_P2. [src: ibd_phage_targeting]
- Extended Tier-1+ cocktail: 8 phages with stated 99 % strain coverage, made by adding NIC06_P2 + LF73_P4 + BCH953_P4. The report calls its size comparable to EcoActive. [src: ibd_phage_targeting]
- NB13 outputs: a 96-phage host-range table with host-range percentage, Family, Genus and Phage_host_phylo. [src: ibd_phage_targeting] It also gives a 188-strain susceptibility table. [src: ibd_phage_targeting] A verdict file gives cocktail compositions at 50/75/90/95/99 % coverage. [src: ibd_phage_targeting]

### Caveats on the cocktail

- The 7 unique E. coli phages in HMP2 fact_viromics (D108, EC6, ECML-117, Murica, slur16, vB_EcoM-VpaE1, vB_EcoM_AYO145A) do not overlap by name with PhageFoundry phages. [src: ibd_phage_targeting] The project's data therefore do not validate in-vivo gut delivery of the cocktail phages. That would need in-vivo testing. [src: ibd_phage_targeting]
- PhageFoundry has no explicit AIEC-versus-commensal annotation. The 188 strains include LF82, LF73, 536, NIC06 and BCH953 as named phage isolation hosts. Accurate AIEC coverage still needs cross-reference to literature isolate annotations. [src: ibd_phage_targeting]
- The cocktail covers broad E. coli diversity but does not separate AIEC from commensal strains. The report therefore requires per-patient detection of the pks-island, Yersiniabactin and Enterobactin genes before cocktail selection. [src: ibd_phage_targeting]
- The susceptibility matrix is binary, with no titer or burst size. Real dosing also depends on burst size, receptor binding kinetics and gastric passage survival, which the report puts out of scope. [src: ibd_phage_targeting]
- 26 strains (14 %) are phage-resistant at ≤5 % susceptibility. Their clinical significance needs cross-reference to AIEC pks-island annotation. [src: ibd_phage_targeting]

### In-vivo phage community in HMP2 (NB14)

NB14 adds an in-vivo phage-community layer to the NB12 literature layer and the NB13 susceptibility layer. [src: ibd_phage_targeting] HMP2 fact_viromics holds 3,039 sample-rows × 273 viruses profiled with VirMAP. [src: ibd_phage_targeting] Cross-referencing with NB04h ecotype projections gives ecotype calls for 630 of 648 viromics samples (97 %). [src: ibd_phage_targeting] These are 27 (E0), 484 (E1), 55 (E2) and 50 (E3) samples, spanning CD (Crohn's disease), UC and healthy. [src: ibd_phage_targeting]

#### Gokushovirus is depleted in CD

Per-ecotype, per-virus CD-versus-nonIBD Mann-Whitney tests ran 85 differential-abundance tests across 4 ecotypes. Three passed strict FDR<0.10 (false discovery rate). [src: ibd_phage_targeting]

| Ecotype | Virus | Cliff δ | n CD vs n HC | FDR |
|---|---|---|---|---|
| E1 | Gokushovirus WZ-2015a | −0.358 | 231 vs 125 | 5e-7 [src: ibd_phage_targeting] |
| E2 | Gokushovirus WZ-2015a | −0.471 | 21 vs 20 | 0.056 [src: ibd_phage_targeting] |
| E2 | Human feces pecovirus | −0.300 | 21 vs 20 | 0.056 [src: ibd_phage_targeting] |

The report calls Gokushovirus WZ-2015a robustly CD-down across multiple ecotypes, strongest in E1. [src: ibd_phage_targeting] It says this independently rediscovers the precomputed ref_viromics_cd_vs_nonibd top hit (log2fc=-2.7, FDR=1e-11). [src: ibd_phage_targeting] It describes Gokushovirus as a Microviridae member with single-stranded DNA and a ~5 kb genome. It says Gokushovirinae includes a canonical crassphage-like lineage infecting Bacteroides and Prevotella gut commensals. [src: ibd_phage_targeting] It reads the depletion as consistent with Norman 2015 and Clooney 2019 IBD-Microviridae depletion. [src: ibd_phage_targeting]

Two limits apply. In E0, Gokushovirus has cliff=-0.55 but does not pass strict FDR<0.10, which the report attributes to power. [src: ibd_phage_targeting] Power is asymmetric: E1 has 231 CD samples, while E0, E2 and E3 have 12-30. [src: ibd_phage_targeting]

#### Pathobiont–phage-family correlations

NB14 tested Tier-A pathobiont species against phage-family Spearman correlations in 630 paired viromics and metaphlan3 samples. [src: ibd_phage_targeting]

| Species | Phage family | Spearman ρ | p |
|---|---|---|---|
| E. coli | Podoviridae | +0.183 | 4e-6 [src: ibd_phage_targeting] |
| H. hathewayi | Unknown | -0.150 | 2e-4 [src: ibd_phage_targeting] |
| M. gnavus | Unknown | -0.134 | 7e-4 [src: ibd_phage_targeting] |
| E. coli | Myoviridae | +0.125 | 0.002 [src: ibd_phage_targeting] |
| E. bolteae | Myoviridae | +0.119 | 0.003 [src: ibd_phage_targeting] |

Podoviridae and Myoviridae are Caudovirales families that include T7-like and T4-like E. coli phages. [src: ibd_phage_targeting] The report reads the positive E. coli correlations as plausible endogenous phage-host correlation, reflecting commensal phage carriage or lysogenic-state co-occurrence. [src: ibd_phage_targeting] All correlations have |ρ|≤0.18, so there are no strong (|ρ|>0.30) endogenous phage candidates targeting Tier-A pathobionts. [src: ibd_phage_targeting]

The report reads the negative H. hathewayi and M. gnavus correlations as pathobiont blooms displacing unclassified phages, consistent with reduced phage diversity in CD dysbiosis. [src: ibd_phage_targeting] Panel A shows modest ecotype-specific variation: Anelloviridae E1-specific, Parvoviridae E2-elevated, and Unknown family E2-dominant. [src: ibd_phage_targeting]

VirMAP classifies 80 % of observations as Unknown family. The report treats this classification gap as the methodological limit, not biology. [src: ibd_phage_targeting] It also limits per-family differential-abundance and correlation power. [src: ibd_phage_targeting]

### Combined phage-evidence verdict

The report scores three evidence layers. NB12 (curated literature) classifies E. coli AIEC as clinical-trial-stage via EcoActive, M. gnavus phages as temperate-only, and H. hathewayi and F. plautii as phage gaps. [src: ibd_phage_targeting] NB13 is the susceptibility layer above. [src: ibd_phage_targeting] The NB14 in-vivo layer covers 630 samples × 21 families. [src: ibd_phage_targeting]

The combined verdict is high phage-therapy feasibility for E. coli, because the clinical cocktail, experimental susceptibility and in-vivo phage correlation align. [src: ibd_phage_targeting] For M. gnavus, H. hathewayi and F. plautii the gap is confirmed across all three layers. They have no clinical phages, no PhageFoundry coverage and no HMP2 in-vivo Podoviridae/Myoviridae signal. [src: ibd_phage_targeting] The report ranks INPHARED and IMG/VR queries for these three gaps as the highest-priority follow-up before cocktail drafts. [src: ibd_phage_targeting]

### Run details

NB13 ran as run_nb13.py through the KBase Data Lakehouse Spark Connect, under plan v1.7 NB13 and v1.9 no-raw-reads. [src: ibd_phage_targeting]

## Key Findings: NB15 — UC Davis per-patient profile + cocktail draft (Pillar 5 opener)

This part of the report covers NB14, the HMP2 endogenous phageome analysis, and NB15, which turns the earlier evidence into per-patient cocktail drafts for the UC Davis Crohn's disease (CD) cohort. NB14's claims here are mostly its outputs and limits. NB15 gives the substantive results, and they come from a small cohort, so they serve as templates and not as validation. [src: ibd_phage_targeting]

### NB14: HMP2 endogenous phageome

NB14 ran as run_nb14.py under plan v1.7 (endogenous phageome stratification) and v1.9 (no raw reads). [src: ibd_phage_targeting] It recorded 85 ecotype × virus differential-abundance tests [src: ibd_phage_targeting] and 126 Tier-A species × phage family Spearman correlations. [src: ibd_phage_targeting] It also wrote a formal verdict file. [src: ibd_phage_targeting] Two limits apply. HMP2 viromics has no CRISPR-spacer-derived phage-host predictions, so finding phages for Tier-A hosts would need an IMG/VR cross-reference. [src: ibd_phage_targeting] Lumping viruses into an "Unknown" family hides species-level signal, so per-virus differential abundance is more informative than per-family analysis for IBD-relevant phages. [src: ibd_phage_targeting]

### NB15: per-patient cocktail drafts

NB15 builds per-patient cocktail drafts for 23 UC Davis CD patients from Pillar 1-4 evidence. [src: ibd_phage_targeting] Its inputs per patient are ecotype, demographics, Kuehl_WGS Kaiju Tier-A presence (≥0.001 relative abundance), Tier-A score, mechanism profile and phage availability. [src: ibd_phage_targeting] See also [[entities/uc-davis-kuehl-wgs-crohn-s-disease-cohort]] and [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

#### Pathobiont carriage

Most Tier-A species are carried by most patients. E. coli is the exception.

| Species | Patients | Share |
|---|---|---|
| M. gnavus | 21 | 91 % [src: ibd_phage_targeting] |
| H. hathewayi | 19 | 83 % [src: ibd_phage_targeting] |
| E. bolteae | 19 | 83 % [src: ibd_phage_targeting] |
| F. plautii | 18 | 78 % [src: ibd_phage_targeting] |
| E. lenta | 16 | 70 % [src: ibd_phage_targeting] |
| E. coli | 8 | 35 % [src: ibd_phage_targeting] |

The report therefore sees NB13's 5-phage AIEC (adherent-invasive E. coli) cocktail as directly applicable to ~35 % of the cohort. [src: ibd_phage_targeting] It calls the phage gap for near-universally carried H. hathewayi and M. gnavus the dominant unmet need. [src: ibd_phage_targeting]

#### Ecotype summary

E1 patients get concrete cocktails far more often than E0 patients. E0 patients get none, because their priority targets are phage gaps or temperate-only. [src: ibd_phage_targeting]

| Ecotype | Patients | Mean targets / patient | With cocktails | With concrete phage |
|---|---|---|---|---|
| E0 | 7 | 1.71 | 7 | 0 [src: ibd_phage_targeting] |
| E1 | 9 | 4.89 | 9 | 9 [src: ibd_phage_targeting] |
| E3 | 6 | 2.33 | 5 | 4 [src: ibd_phage_targeting] |
| Mixed (6967) | 1 | 3.0 | 1 | 1 [src: ibd_phage_targeting] |
| Total | 23 | 4.39 | 22 | 14 [src: ibd_phage_targeting] |

All 9 E1 patients receive concrete cocktails of PMBT24 and PMBT5, plus the AIEC 5-phage cocktail if E. coli is present. [src: ibd_phage_targeting]

#### Clinical triage groups

- Group A, active disease with multiple targets: patients 3701 (calprotectin 8000), 1835 (3340), 5843 (2150) and 6434 (251, with 6 targets). These get the highest-priority full hybrid cocktail of phages plus alternatives for gap species. [src: ibd_phage_targeting]
- Group B, active disease with few targets: E0 patients with limited pathobiont burden. These get a limited cocktail, and deprioritizing is considered. [src: ibd_phage_targeting]
- Group C, quiescent: patients 1112 (41), 2708 (3), 1492 (9) and 1460 (7). The cocktail is reserved for flares, and calprotectin is monitored. [src: ibd_phage_targeting]
- Group D, mixed ecotype: patient 6967, who drifts between E1 and E3. This patient gets state-dependent dosing, which serves as the central per-patient stability test for Pillar 5. [src: ibd_phage_targeting]

#### Recommendations by subgroup

| Subgroup | Patients | Recommendation |
|---|---|---|
| E1, active calprotectin, E. coli present | ~3 | Full Tier-1: NB13 5-phage E. coli cocktail, PMBT24, PMBT5, and alternatives for F. plautii, H. hathewayi and M. gnavus [src: ibd_phage_targeting] |
| E1, active calprotectin, no E. coli | ~5 | Tier-2: PMBT24, PMBT5 and alternatives [src: ibd_phage_targeting] |
| E1, quiescent | 1-2 | Reserve for flares and monitor calprotectin [src: ibd_phage_targeting] |
| E0, any | 7 | Limited cocktail, possible deprioritization, because priority targets are gaps or temperate-only [src: ibd_phage_targeting] |
| E3 with E. coli | ~3 | NB13 5-phage E. coli cocktail, PMBT5 and alternatives [src: ibd_phage_targeting] |
| E3 without E. coli | ~3 | Limited cocktail targeting E. lenta and H. hathewayi only [src: ibd_phage_targeting] |

#### E1 hybrid design and the F. plautii constraint

The E1 hybrid draft uses direct phages for E. coli (if present), E. bolteae (PMBT24) and E. lenta (PMBT5). [src: ibd_phage_targeting] It proposes alternatives for H. hathewayi (GAG-degrading enzyme inhibitors) and F. plautii (bile-acid-binding co-therapy, or deprioritization). [src: ibd_phage_targeting] M. gnavus is limited because its phages are temperate-only. The draft suggests lytic-locked engineering or a biochemical glucorhamnan-synthesis target. [src: ibd_phage_targeting] The report concludes that a pure phage cocktail is not feasible for any E1 patient, and only a hybrid with non-phage alternatives works. [src: ibd_phage_targeting] Because three species are phage gaps, it ranks INPHARED and IMG/VR queries for new gut-anaerobe phages as the top Pillar-4 follow-up before clinical translation. [src: ibd_phage_targeting] See [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]].

The report calls F. plautii the dominant E1 design constraint. It is present in 78 % of patients (18/23), including all 9 E1 patients, and it has the highest bile-acid coupling cost as an active 7α-dehydroxylator. [src: ibd_phage_targeting] The report states that phage targeting would shift the bile-acid pool toward inflammatory primary tauro-conjugated forms. Its alternative is to deprioritize F. plautii and co-administer UDCA (ursodeoxycholic acid) or a bile-acid-binding agent. [src: ibd_phage_targeting] F. plautii is also a Pillar-4 gap, absent from ref_phage_biology, so it is a "leave alone" target for Pillar 5. [src: ibd_phage_targeting] See [[entities/flavonifractor-plautii]].

### Caveats

- The 23-patient cohort is small, so results are exemplars or templates and not statistically robust per-patient validation. [src: ibd_phage_targeting]
- Kuehl_WGS used Kaiju, not MetaPhlAn3, so Tier-A presence calls are less confident than in the curatedMetagenomicData (CMD) analyses. [src: ibd_phage_targeting]
- No per-patient bile-acid measurements exist, so bile-acid cost is set at ecotype level. [src: ibd_phage_targeting]
- The deprioritization of F. plautii is precautionary and rests on mechanism. Clinical validation needs per-patient bile-acid panels. [src: ibd_phage_targeting]
- The 8 E. coli-positive patients have no patient-specific AIEC strain-resolution diagnostic. The recommendations assume AIEC subset prevalence from Dogan 2014. [src: ibd_phage_targeting]

### Outputs

NB15 supplies full profiles for 23 patients [src: ibd_phage_targeting], a long-format per-patient by per-target cocktail breakdown [src: ibd_phage_targeting], and a formal verdict with per-ecotype summary. [src: ibd_phage_targeting]

## Key Findings: NB16 — Patient 6967 longitudinal stability + state-dependent dosing strategy

This part of the report builds per-patient cocktail recommendations for the UC Davis Crohn's disease (CD) cohort. It tests longitudinal stability in patient 6967 and checks Kaiju reliability with patient 1112's replicates. The longitudinal result is a single-patient observation (n=1). The Kaiju replicate check is strong for the six Tier-A pathobionts. [src: ibd_phage_targeting]

### Patient 6967 longitudinal trajectory

Patient 6967 is the only multi-timepoint UC Davis CD patient with documented E1↔E3 ecotype drift across 2 visits. [src: ibd_phage_targeting] Visit 1 was called E1 (confidence 0.64) and visit 2 E3 (confidence 0.41). [src: ibd_phage_targeting] Most Tier-A pathobionts expanded between the visits, and *M. gnavus* expanded most. The report calls the 14× *M. gnavus* expansion the dominant signature of the E1→E3 transition. It reads the 1.3–3.1× expansions of the other Tier-A species as general dysbiosis worsening. [src: ibd_phage_targeting]

| Tier-A species | Visit 1 | Visit 2 | Fold change | Claim |
|---|---:|---:|---:|---|
| H. hathewayi | 0.27 | 0.36 | 1.3× | [src: ibd_phage_targeting] |
| M. gnavus | 0.53 | 7.45 | 14.0× | [src: ibd_phage_targeting] |
| E. lenta | 0.40 | 1.24 | 3.1× | [src: ibd_phage_targeting] |
| F. plautii | 0.84 | 1.62 | 1.9× | [src: ibd_phage_targeting] |
| E. bolteae | 0.25 | 0.54 | 2.1× | [src: ibd_phage_targeting] |
| E. coli | 0.00 | 0.00 | — | [src: ibd_phage_targeting] |

*E. coli* was absent at both visits, so the report concludes patient 6967 is not an adherent-invasive *E. coli* (AIEC) carrier. [src: ibd_phage_targeting] The report says this matches its earlier ecotype biology. E3 is severe-Bacteroides-expanded, with *M. gnavus* as a dominant expansion axis. E1 is Bact2-transitional, with milder pathobiont burden. [src: ibd_phage_targeting]

### Would the cocktail change?

The cocktail changes only partly between visits. Visit 1 (E1) had all 5 E1_CD module 0 priority targets present, giving {H. hathewayi, M. gnavus, E. bolteae, E. lenta, F. plautii}. [src: ibd_phage_targeting] Visit 2 (E3) had 4 E3_CD module 1 priority targets, of which 3 were present because *E. coli* was absent. Its cocktail was {E. lenta, H. hathewayi, M. gnavus}. [src: ibd_phage_targeting] The shared trio *H. hathewayi*, *M. gnavus* and *E. lenta* is called the universal Tier-1 trio. [src: ibd_phage_targeting] *E. bolteae* and *F. plautii* are visit-1-only, E1-specific targets that would be deprioritized on transition to E3. [src: ibd_phage_targeting]

### Kaiju reliability in patient 1112

Two resequencing replicates of the same biological sample from patient 1112 agreed closely, so the report judges Kaiju calls for actionable Tier-A pathobionts in UC Davis samples highly reliable. [src: ibd_phage_targeting] Rank concordance across the 6 Tier-A species was perfect, with Spearman ρ = 1.000 (p < 0.001). [src: ibd_phage_targeting] *E. lenta* showed the largest difference, at 10 %. [src: ibd_phage_targeting]

| Tier-A species | Reads_1112-1 | Reads_1112_reseq-1 | Difference | Claim |
|---|---:|---:|---:|---|
| H. hathewayi | 0.445 | 0.436 | 2 % | [src: ibd_phage_targeting] |
| M. gnavus | 7.916 | 7.792 | 1.6 % | [src: ibd_phage_targeting] |
| E. lenta | 0.712 | 0.642 | 10 % | [src: ibd_phage_targeting] |
| F. plautii | 2.019 | 1.994 | 1.2 % | [src: ibd_phage_targeting] |
| E. bolteae | 0.864 | 0.862 | 0.2 % | [src: ibd_phage_targeting] |
| E. coli | 0.000 | 0.000 | — | [src: ibd_phage_targeting] |

### Proposed dosing rules and workflow

The items below are the report's recommendations and proposals. Only the state-dependent dosing rule is stated to be theoretical and not yet validated in clinical practice. [src: ibd_phage_targeting]

- Re-test ecotype every 3-6 months for active CD patients on phage cocktail therapy, because patient 6967 shows that ecotype is dynamic. [src: ibd_phage_targeting]
- Keep *M. gnavus*, *H. hathewayi* and *E. lenta* as the backbone for any active-disease CD patient, with no re-evaluation on ecotype shift. [src: ibd_phage_targeting]
- On an E1→E3 transition, deprioritize *F. plautii*. NB07c assigns it to E1_CD module 0, and dropping it also reduces the bile-acid coupling-cost concern. [src: ibd_phage_targeting]
- On an E3→E1 transition, deprioritize *E. coli*, subject to AIEC strain detection, because it is an E3_CD module 1 priority. [src: ibd_phage_targeting]
- The report hypothesizes that *M. gnavus* qPCR could be a cheap proxy for ecotype shift, avoiding full metagenomics at every visit. This is motivated by patient 6967's 14× expansion. [src: ibd_phage_targeting] It suggests a 5-fold change in *M. gnavus* might trigger full ecotype re-evaluation. [src: ibd_phage_targeting]

The proposed workflow starts with stool metagenomics for ecotype assignment. E0 gets a limited cocktail held as flare reserve. [src: ibd_phage_targeting] E1 gets a full hybrid 3-strategy cocktail: the NB13 5-phage *E. coli* set if AIEC-positive, PMBT24, PMBT5, and alternatives for *H. hathewayi* and *F. plautii*. [src: ibd_phage_targeting] E3 gets a focused cocktail of *E. coli* targeting if present, PMBT5, and alternatives. [src: ibd_phage_targeting] Follow-up visits at 3-6 months use calprotectin to assess disease activity and *M. gnavus* qPCR as the ecotype-state indicator. [src: ibd_phage_targeting] After a confirmed E1→E3 shift, the workflow drops *F. plautii* and considers adding an *E. coli* cocktail. After an E3→E1 shift, it adds a *F. plautii* alternative and reassesses *E. coli* targeting. A stable ecotype continues the current cocktail. [src: ibd_phage_targeting]

### Caveats

- The ecotype-drift conclusions rest on a single longitudinal trajectory (n=1). Patient 6967 is the only multi-timepoint patient with biological replicate samples in the cohort. [src: ibd_phage_targeting]
- Visit confidences of 0.64 and 0.41 are moderate, so the ecotype call shift could partly reflect classifier uncertainty. The report argues the 14× *M. gnavus* and 3× *E. lenta* expansions are quantitative observations independent of the ecotype label. [src: ibd_phage_targeting]
- No timing information exists between the two visits, so the duration of drift is unknown. This limits timing recommendations for the clinical workflow. [src: ibd_phage_targeting]
- Whether the 0.60 Jaccard (3-of-5 component overlap) means clinically meaningful redesign depends on patient response heterogeneity, which is outside the project's scope. [src: ibd_phage_targeting]
- The state-dependent dosing rule is theoretical and not yet validated in clinical practice. [src: ibd_phage_targeting]

See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]] for the wider design concept.

## Interpretation: Project narrative summary (Pillars 1–5 closed)

This part of the report is its narrative summary of the project. It states that the project's central question, whether ecotype-specific and per-patient pathobiont target lists can be derived for rational phage-cocktail design, now has a project-internal answer that is robust across pathway, BGC (biosynthetic gene cluster), metabolite, strain, serology, phage-evidence and per-patient longitudinal evidence streams. [src: ibd_phage_targeting] The work spans 23 notebooks and two adversarial reviews that caught 9 critical and 16 important methodological issues. [src: ibd_phage_targeting] The phage-targetability work for Pillars 4–5 remains to be done. [src: ibd_phage_targeting]

### Ecotype framework

The NB01b consensus K=4 framework stratifies 8,489 cMD samples, 1,627 HMP2 samples and 23 UC Davis patients into E0 healthy-commensal, E1 Bact2-transitional, E2 Prevotella and E3 severe-Bacteroides clusters. [src: ibd_phage_targeting] It replicated externally on HMP2 at 80% projection confidence, with disease-stratification χ²(2)=15.6 and p=0.016. [src: ibd_phage_targeting] The report maps E0 to the diverse Ruminococcus enterotype and E2 to the Prevotella enterotype. It maps E1 and E3 to transitional and severe Bacteroides states. [src: ibd_phage_targeting] Between-method agreement for the K=4 assignments is only 48.9 %, which the report reads as a real microbiome continuum discretized for operational purposes. [src: ibd_phage_targeting] The report names Dirichlet multinomial mixtures as the canonical discovery method. It says LDA on pseudo-counts gives equivalent assignments at this sample scale, confirmed by cross-method ARI (adjusted Rand index) against an independent CLR (centered log-ratio)-based GMM (Gaussian mixture model). [src: ibd_phage_targeting]

### Target priorities and mechanisms

NB05 yields six actionable Tier-A targets. Their scores are H. hathewayi 4.0 [src: ibd_phage_targeting], M. gnavus 3.8 [src: ibd_phage_targeting], E. coli 3.6 [src: ibd_phage_targeting], E. lenta 3.3 [src: ibd_phage_targeting], F. plautii 3.3 [src: ibd_phage_targeting] and E. bolteae 2.8. [src: ibd_phage_targeting] The report builds two cross-corroborated six-line mechanism narratives. The first is iron acquisition in the E. coli AIEC (adherent-invasive E. coli) subset, with OR (odds ratio)=8.1 for pathway evidence and OR=44 for BGC evidence. [src: ibd_phage_targeting] The second is bile-acid 7α-dehydroxylation, seen as a paired-sample substrate-product signature for F. plautii, E. lenta and E. bolteae. [src: ibd_phage_targeting] All Pillar 3 narratives collapse into one multi-omics joint factor, NB07d CC1, with canonical r=0.96 and CD-vs-nonIBD cliff=+0.50. The report reads this CCA (canonical correlation analysis) result as per-modality analyses converging on the same biology. [src: ibd_phage_targeting]

The NB05 E. coli MIBiG hits map onto known AIEC virulence determinants. Yersiniabactin is the iron-capture siderophore AIEC LF82 uses to survive in macrophage phagolysosomes. [src: ibd_phage_targeting] Colibactin is a pks+ genotoxin implicated in AIEC-associated colorectal carcinogenesis. [src: ibd_phage_targeting] Enterobactin is another AIEC siderophore active in mucosal-associated IBD settings. [src: ibd_phage_targeting] The report cites IBD-specific E. coli genomic adaptations as independent confirmation of over-abundance with disease-specific lineages. [src: ibd_phage_targeting] It notes that AIEC drives ileal CD mucosal invasion [src: ibd_phage_targeting] and that R. gnavus produces an inflammatory glucorhamnan polysaccharide. [src: ibd_phage_targeting]

A per-target design profile separates iron/AIEC-mediated from other CD specialization, bile-acid coupling cost, and species-abundance-mediated from strain-content-mediated mechanisms. [src: ibd_phage_targeting] This turns Tier-A score as target priority into a multi-attribute decision framework. [src: ibd_phage_targeting] The H3a-new shared-environment reframing sharpens the "metabolic-coupling cost" annotation into a more rigorous "bile-acid coupling cost". [src: ibd_phage_targeting]

### Metabolites

Three metabolite signatures replicated from HMP2 to Franzosa at ≥75% sign-concordance (NB09b). Urobilin is CD-down, interpreted as loss of bilirubin-reducer commensals. [src: ibd_phage_targeting] Acyl-carnitines are CD-up. [src: ibd_phage_targeting] Long-chain PUFAs (polyunsaturated fatty acids) are CD-up and are described as inflammatory eicosanoid precursors. [src: ibd_phage_targeting]

### Hypothesis verdicts

The H3 falsifiability framework is closed with 5 SUPPORTED, 1 PARTIALLY SUPPORTED, 2 PARTIAL (single-cohort caveat) and 1 NOT SUPPORTED verdicts. [src: ibd_phage_targeting] The H3d-clust failure means taxonomic-feature ecotypes stay the primary basis for clinical translation. Metabolite-feature ecotypes would need external batch correction. [src: ibd_phage_targeting]

### Methodology contributions

The NB04e within-IBD-substudy CD-vs-nonIBD meta-analysis design resolves the feature-leakage and substudy-confounding pitfalls of pooled-cohort differential abundance. [src: ibd_phage_targeting] The report lists generalizable contributions:
- cMD substudy-nesting unidentifiability [src: ibd_phage_targeting];
- feature leakage in cluster-stratified DA [src: ibd_phage_targeting];
- LOSO (leave one substudy out) ARI as an honest stability metric [src: ibd_phage_targeting];
- pool ≠ flux for pathway versus metabolite DA [src: ibd_phage_targeting];
- multi-line cross-corroboration as a portable rigor pattern [src: ibd_phage_targeting];
- cohort batch dominating clustering for absolute-intensity multi-cohort modalities. [src: ibd_phage_targeting]

Pooled multi-cohort DA is heavily confounded by age, diet and geography. [src: ibd_phage_targeting] The H1c finding that is_ibd dominates classifier AUC but collapses on a single-cohort test is a concrete instance. [src: ibd_phage_targeting] Raw Mann-Whitney tests on relative abundance are biased by the sum-to-constant constraint, and NB00 reproduces this on a curated battery. [src: ibd_phage_targeting] LinDA, linear CLR regression with bias correction, serves as the second-method concordance check in NB04c. [src: ibd_phage_targeting]

### Clinical translation and caveats

Per-ecotype cocktail design is the project's deliverable. [src: ibd_phage_targeting] If active CD patients separate into E0, E1 and E3, the pathobiont targets differ by ecotype. [src: ibd_phage_targeting] The preliminary report's donor 2708 engraftment analysis gave a pooled list of R. gnavus, E. bolteae, E. coli, E. lenta, C. difficile and K. oxytoca. [src: ibd_phage_targeting] A cocktail built on that list would mismatch the ~27 % of UC Davis patients in E0, who may not need it. [src: ibd_phage_targeting] It may also be over-aggressive for the 42 % in E1, whose pathobiont burden differs from E3. [src: ibd_phage_targeting]

H1c's nominal AUC (area under curve) meets the routine-data screening goal. The UC Davis translation shows, however, that the classifier cannot separate E1 from E3 without metagenomics. [src: ibd_phage_targeting] Trial screening therefore needs stool metagenomics. The alternatives are a rapid qPCR panel on ecotype-defining species, or better training data. The latter awaits HMP2 MetaPhlAn3 ingestion and HMP2 plus Franzosa medication metadata. [src: ibd_phage_targeting]

Patient 6967's longitudinal E1 ↔ E3 shift in NB02 is the central per-patient-stability test for whether dosing should be state-dependent. [src: ibd_phage_targeting] What remains for Pillars 4–5 is a phage targetability matrix per Tier-A core, from PhageFoundry and external phage databases. The report will combine it with the per-target design profile to draft per-ecotype and per-patient cocktails for the 23 UC Davis patients. [src: ibd_phage_targeting]

## Interpretation: Literature context

This part of the report sets its findings beside published work on oral-gut biology, AIEC phage therapy, iron, choline, butyrate producers, biosynthetic gene clusters (BGCs) and bile acids. The literature is used mainly as a consistency check on the report's own results. [src: ibd_phage_targeting]

### Oral-gut axis and oral streptococci

The report cites literature in which oral-cavity species colonize the inflammatory bowel disease (IBD) gut ectopically and may contribute to pathogenesis, an "oral-gut axis". [src: ibd_phage_targeting] Its top E1 Tier-A candidates, Streptococcus salivarius, Streptococcus thermophilus and Streptococcus parasanguinis, are oral streptococci whose within-substudy Crohn's disease (CD) enrichment fits this framework. [src: ibd_phage_targeting] S. salivarius is reported as a salivary biomarker for orofacial granulomatosis co-occurring with CD. [src: ibd_phage_targeting] The NB05 Salivaricin hits are lantibiotic bacteriocins whose proimmune activity regulates the oral microbiome. [src: ibd_phage_targeting] The report also identifies Erysipelatoclostridium innocuum as a vancomycin-resistant CD-associated pathobiome correlated with creeping-fat and intestinal strictures. [src: ibd_phage_targeting] The report says its earlier leakage-contaminated NB04 analysis had presented this expected biology as "commensal Simpson's paradox" noise. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

### Phage precedent and causal sufficiency

The report cites Galtier 2017, in which AIEC-specific (adherent-invasive Escherichia coli) bacteriophages targeting CEACAM6-bound E. coli reduced AIEC-associated intestinal mucosal signal in CD models. [src: ibd_phage_targeting] It treats this as precedent that makes E. coli (NB05 Tier-A #3, with 3 MIBiG virulence matches) a feasible phage target. [src: ibd_phage_targeting] In NB06, 5 of 6 actionable Tier-A candidates co-occur in a single module. The report therefore argues for multi-target cocktails over AIEC-only ones, because the module would likely re-equilibrate around a remaining hub. [src: ibd_phage_targeting] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

The report also cites Sheikh 2024, in which CD-patient microbiome transplanted into germ-free mice produced colitis with discontinued-pattern, proximal colonic localization. [src: ibd_phage_targeting] It reads this as evidence that composition is causally sufficient for the phenotype, which supports the premise of composition-modifying cocktails. [src: ibd_phage_targeting]

### Iron acquisition

The report's NB07 v1.8 finding that iron/heme acquisition is the dominant CD-up MetaCyc class-enriched theme (OR=8.1, FDR 7e-6) is described as causally consistent with the IBD-iron literature. [src: ibd_phage_targeting] Cited work includes:
- Ellermann 2020, showing that dietary iron variably modulates microbiota assembly in colitis-resistant and colitis-susceptible mice. [src: ibd_phage_targeting]
- A statement that oral iron supplementation can exacerbate disease activity in a subset of IBD patients. [src: ibd_phage_targeting]
- Buret 2019, linking iron acquisition to virulence-factor expression in commensals that become pathobionts in IBD and colorectal cancer. [src: ibd_phage_targeting]

The report interprets this as iron being a pathobiont-selective resource that CD pathobionts have systematically over-invested in, through siderophores, heme uptake and heme biosynthesis. [src: ibd_phage_targeting] This is an interpretation, not a direct test. It proposes that iron-supplementation decisions account for ecotype-specific pathobiont iron-system expression. It also proposes that phages could deplete iron-system-enriched AIEC while sparing iron-pathway-deficient commensals. [src: ibd_phage_targeting] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

NB07b found E. coli per-pathway abundance lower in CD within carriers, despite cohort-level elevation. The affected pathways were allantoin degradation, propanediol degradation, octane oxidation, histidine degradation and phospholipid remodeling. [src: ibd_phage_targeting] The report reads this as consistent with an AIEC-specialized subset that invested in iron and adherent-invasion machinery at the cost of generalist metabolism. [src: ibd_phage_targeting] The cMD raw-reads strain-resolution test was dropped as infeasible. The report proposes instead a kbase_genomes survey of pks, Yersiniabactin and Enterobactin co-occurrence, cross-referenced with fact_strain_competition Kumbhari strain-frequency data. [src: ibd_phage_targeting]

### Hungatella hathewayi and choline

H. hathewayi's TMA/choline theme enrichment (OR=9.33, FDR=0.048) is consistent with bacterial choline degradation. [src: ibd_phage_targeting] CutC is a glycyl radical enzyme that degrades choline to trimethylamine (TMA) in human gut microbes, and the host converts TMA to TMAO, which has cardiovascular and renal disease implications. [src: ibd_phage_targeting] Together with its CD-up phosphatidylcholine acyl editing, this leads the report to suggest H. hathewayi is functionally a TMA-producing pathobiont in CD samples. [src: ibd_phage_targeting]

### Anaerostipes caccae and cross-feeding

A. caccae is a butyrate producer using lactate/acetate co-substrates and host-mucin-derived sugars, and a primary colonic lactate utilizer. [src: ibd_phage_targeting] Its strong positive coupling with M. gnavus, F. plautii, H. hathewayi and E. bolteae is read as consistent with known cross-feeding circuits. [src: ibd_phage_targeting] The proposed cross-feeding is not iron-mediated: the A. caccae iron-pathway correlation is much smaller than that of E. coli. [src: ibd_phage_targeting] The report warns that depleting the pathobiont cluster may incidentally reduce a potentially anti-inflammatory butyrate producer. This motivates its ecological-durability criterion (Tier C). [src: ibd_phage_targeting] See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

### Biosynthetic gene clusters

The report uses the Elmassry BGC catalog (10,060 BGCs across 6,221 species-annotated entries) as genomic-content evidence. [src: ibd_phage_targeting] E. coli alone among the 6 actionable Tier-A core species carries the canonical AIEC virulence BGC repertoire [src: ibd_phage_targeting]:

| BGC class in E. coli | Count |
|---|---|
| Yersiniabactin | 19 [src: ibd_phage_targeting] |
| Enterobactin | 16 [src: ibd_phage_targeting] |
| Siderophore-class | 19 [src: ibd_phage_targeting] |
| Colibactin | 8 [src: ibd_phage_targeting] |
| Microcin B17 | 15 [src: ibd_phage_targeting] |

The other 5 Tier-A core species sit in "MIBiG dark matter". They carry substantial non-MIBiG-annotated BGC content, including 41 BGCs in E. lenta [src: ibd_phage_targeting] and 58 in M. gnavus, 31 of them lanthipeptides. [src: ibd_phage_targeting] Their CB-ORFs are CD-enriched at the read level, but their CD-association mechanisms are not captured by MIBiG-themed BGC analysis. [src: ibd_phage_targeting]

E. lenta CB-ORFs are 54 % CD-down versus 0 % CD-up. The report calls this consistent with Koppel et al. 2018, in which Eggerthella CD-association is driven by drug metabolism (Cgr2 / arginine-2,3-aminomutase) and not by secondary-metabolite biosynthesis. [src: ibd_phage_targeting]

The ebf/ecf BGC families are CD-up across 4 cohorts at p<1e-31. This replicates the Elmassry headline finding. [src: ibd_phage_targeting] The families produce immunoactive fatty acid amide signaling lipids similar in structure to host endocannabinoids. [src: ibd_phage_targeting] The independent cMD-style reanalysis (1,349 samples across HMP2-IBDMDB, MetaHIT, LLDEEP and PRISM) gave meta z = 11.71 for ebf [src: ibd_phage_targeting] and z = 11.97 for ecf. [src: ibd_phage_targeting] There is no per-species attribution. The report therefore treats ebf/ecf as a sample-level CD biomarker for treatment-response monitoring, not for cocktail target selection. [src: ibd_phage_targeting]

### Bile-acid 7α-dehydroxylation

In 468 paired CSM* HMP2 samples, F. plautii, E. lenta and E. bolteae showed the predicted bile-acid substrate-product signature. [src: ibd_phage_targeting] F. plautii correlated negatively with cholate (ρ=−0.26). [src: ibd_phage_targeting] Correlations with secondary bile acids were positive:
- E. bolteae with lithocholate, ρ=+0.18. [src: ibd_phage_targeting]
- F. plautii with lithocholate, +0.15. [src: ibd_phage_targeting]
- E. bolteae with deoxycholate, +0.17. [src: ibd_phage_targeting]

M. gnavus and E. coli showed the opposite pattern, so the report concludes they are not in the 7α-dehydroxylation network. [src: ibd_phage_targeting] The report calls this direct sample-level confirmation of the canonical CD 7α-dehydroxylation deficit. It identifies F. plautii, E. lenta and E. bolteae as the active 7α-dehydroxylating species in the actionable Tier-A set. [src: ibd_phage_targeting] See [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]].

## Interpretation: Novel contributions

This part of the report places its metabolomic, ecological-cost and methodological results in the literature and in its own earlier analyses. It describes bile-acid 7α-dehydroxylation and iron acquisition as two independent six-line convergence narratives. [src: ibd_phage_targeting] It also records how the pre-repair NB04 analysis was challenged and then confirmed as flawed by NB04b and NB04c. [src: ibd_phage_targeting]

### Bile-acid 7α-dehydroxylation

The report treats the CD bile-acid deficit as canonical. It cites the *bai* operon mechanism in *Clostridium scindens*-like bacteria (Devlin & Fischbach 2015, PMID 26412091) and Franzosa 2019, and it identifies *F. plautii*, *E. lenta* and *E. bolteae* as active 7α-dehydroxylating species in the actionable Tier-A set. [src: ibd_phage_targeting] NB09c identifies the bile-acid 7α-dehydroxylation network as the dominant per-target ecological-cost axis, with these three species carrying active activity in HMP2 paired samples. [src: ibd_phage_targeting] The report regards the NB09c paired correlations as independent of, and stronger than, the NB07b within-carrier *F. plautii* F420-bile-acid pathway differential abundance. In its words, pathway differential abundance confirms genomic capability and the paired correlation confirms active in vivo activity. [src: ibd_phage_targeting]

Tauro-α/β-muricholate and free taurine are CD-up. The report reads this as metabolite-level confirmation of reduced 7α-dehydroxylation and as a pre-treatment biomarker supporting *F. plautii* as a phage target. [src: ibd_phage_targeting] It predicts that phage targeting of these species would shift the bile-acid pool toward inflammatory primary tauro-conjugated forms. [src: ibd_phage_targeting] Bile-acid coupling cost therefore replaces metabolic-coupling cost as the primary Pillar 4 ecological annotation. [src: ibd_phage_targeting]

The report counts six lines of convergence for this narrative: NB07b F420-pathway, NB09a tauro-muricholate, NB09c paired correlation, NB05 actionable status, Franzosa 2019 and the Devlin/Fischbach mechanism literature. [src: ibd_phage_targeting] It counts six lines for iron acquisition as well: NB05, NB07a, NB07 v1.8, NB07c, NB08a and AIEC (adherent-invasive *Escherichia coli*) literature. [src: ibd_phage_targeting] It also states that AIEC iron acquisition is supported by five independent streams at three analytical granularities. These are literature-MIBiG lookup, pathway–species correlation, pathway-class enrichment, pathway–species covariation and genomic biosynthetic gene cluster (BGC) content. [src: ibd_phage_targeting]

### Cross-feeding versus bile-acid cost

NB06 H2d found that pathobionts co-cluster in single CD-specific modules. [src: ibd_phage_targeting] NB07c found strong positive species-level coupling between pathobionts and non-pathobiont module anchors, especially *Anaerostipes caccae*, described as the only genuine butyrate producer. The report called this consistent with cross-feeding. [src: ibd_phage_targeting] It therefore proposed a per-target ecological-cost annotation, because depleting pathobionts might incidentally remove anti-inflammatory commensals. [src: ibd_phage_targeting]

NB09c's paired sample-level test did not support this. It found no metabolic intermediate backing cross-feeding: lactate had opposite signs for *A. caccae* and the pathobionts, and there were only 7 strict triangles. [src: ibd_phage_targeting]

### Metabolite themes in HMP2

At subject level in HMP2 (50 CD vs 26 nonIBD), polyamines (Fisher OR=14.6, FDR 0.008) and long-chain PUFAs (polyunsaturated fatty acids; OR=7.9, FDR 0.009) are the two CD-up metabolite themes. [src: ibd_phage_targeting] The report describes polyamines as products of gut bacterial fermentation of arginine/ornithine and as well-characterized IBD biomarkers. [src: ibd_phage_targeting] It describes the PUFAs as an inflammatory eicosanoid precursor pool, with arachidonate used for prostaglandin/leukotriene biosynthesis. [src: ibd_phage_targeting] Nineteen cholesteryl esters are CD-up, and the report reads them as corroborating a storage pool of esterified PUFAs. [src: ibd_phage_targeting] It links the PUFA signal to the fat-metabolism/glyoxylate theme, which was sub-threshold at pathway level (OR=0.88) but significant at metabolite-theme level. [src: ibd_phage_targeting]

The polyamine/urea theme is CD-DOWN at pathway level (OR=0.42), yet polyamines are CD-UP as a metabolite class (OR=14.6), the largest metabolomics theme-level effect. [src: ibd_phage_targeting] The report says both are correct. A pool reflects production minus consumption plus dietary and host inputs, so pool and flux measurements are not interchangeable. [src: ibd_phage_targeting] Elevated pools may come from more substrate (dietary protein or mucin) and less microbial clearance, without higher biosynthesis. [src: ibd_phage_targeting]

### Strain adaptation null

NB10a found zero FDR<0.10 strain-adaptation genes among 3,245 *F. plautii* genes tested in Kumbhari. This held despite species-level CD association and active 7α-dehydroxylation evidence. [src: ibd_phage_targeting] The report reads the null as showing that the CD association depends on how much *F. plautii* is present, not on which strain dominates. [src: ibd_phage_targeting] It hypothesizes that the activity is encoded by core *bai*-operon genes present in essentially all strains. [src: ibd_phage_targeting] It predicts that phage depletion of species with this profile would reduce the encoded activity predictably, with no gene-content-selection escape route. [src: ibd_phage_targeting]

### Ecotype framework, leakage and replication

The four-ecotype IBD framework on 8.5 K samples reproduces published enterotype structure. It adds better disease resolution between E1 (transitional) and E3 (severe) within the Bacteroides-dominant state. [src: ibd_phage_targeting]

Clustering on taxon abundance and then testing the same taxa within clusters is selection-on-outcome confounding. It mechanically inflates effects for cluster-defining taxa. [src: ibd_phage_targeting] The report proposes held-out-species sensitivity (Jaccard > 0.5 means leakage is bounded) or leave-one-species-out refitting to detect it. [src: ibd_phage_targeting] NB04b measured E1 Jaccard 0.230 and E3 Jaccard 0.064, which confirmed that the original NB04 within-ecotype Tier-A was substantially leakage-driven. [src: ibd_phage_targeting]

In the ecotype-assigned curatedMetagenomicData slice, 45 sub-studies have ≥ 10 healthy controls (HC) and 5 have ≥ 10 CD samples, but none have both. [src: ibd_phage_targeting] A pooled CD-vs-HC mixed-effects model with a substudy random effect is therefore structurally unidentifiable. `statsmodels.mixedlm` silently failed to converge on every battery species. [src: ibd_phage_targeting] The confound-free alternative is within-IBD-substudy CD-vs-nonIBD, where 4 cMD studies carry both groups. [src: ibd_phage_targeting]

NB04e's within-ecotype × within-substudy meta-analysis removes feature leakage, because the clustering and differential-abundance axes are disjoint. It removes study confounding, because within-substudy contrasts carry no study-level variation. [src: ibd_phage_targeting] It fails gracefully when substudy × ecotype × diagnosis cells are too small, and it reports which ecotypes are meta-viable, single-study-only or not viable. [src: ibd_phage_targeting]

Bootstrap 80 %-subsample ARI (adjusted Rand index) in NB04b was 0.13–0.17. Leave-one-substudy-out (LOSO) ARI across 8 sub-studies in NB04f was 0.00–0.28, with mean 0.113, so the bootstrap masked per-substudy variation. [src: ibd_phage_targeting] Even so, NB04h replicated the NB04e operational Tier-A at 88.2 % sign concordance on HMP2 with high projection confidence. [src: ibd_phage_targeting] The report concludes that framework stability and operational-claim replication are distinct properties needing separate tests. A project can have shaky cluster boundaries but robust cluster-specific findings. [src: ibd_phage_targeting]

Two independent automated review runs on pre-repair NB04 found no critical issues. An adversarial reviewer found 5 critical and 6 important issues, all confirmed empirically by NB04b and NB04c. [src: ibd_phage_targeting]

### Pathway categorization

On identical data and differential-abundance pipeline, a regex scheme categorized 44/409 pathways in 7 themes and gave H3a (b) "FAIL — degenerate". A curator-validated MetaCyc class hierarchy from ModelSEEDDatabase categorized 514/575 pathways in 12 themes and gave "SUPPORTED", with iron/heme acquisition 8.1× enriched. [src: ibd_phage_targeting]

### Cross-cohort metabolomics

Pooling HMP2 and Franzosa metabolomics on a 111-feature m/z-bridge panel and clustering with PCA (principal component analysis) plus K-means K=4 gave clusters that separated completely by cohort, not diagnosis. [src: ibd_phage_targeting] PC1 explained 79 % of variance and was essentially a cohort batch effect. [src: ibd_phage_targeting] Cross-cohort LOSO ARI was 0.000, well below the 0.113 taxonomic-ecotype baseline. [src: ibd_phage_targeting]

The report attributes the portability of taxonomic ecotypes to MetaPhlAn3 relative abundances being unitless and sum-to-1 per sample, which gives natural cohort normalization. [src: ibd_phage_targeting] Metabolite clustering inherits absolute-intensity differences between LC-MS (liquid chromatography-mass spectrometry) runs and needs explicit ComBat/SVA/RUV batch correction. [src: ibd_phage_targeting] Within-pooled bootstrap stability measures batch reproducibility rather than biological reproducibility. [src: ibd_phage_targeting]

### Reusable methods proposed

The report proposes four methodological contributions:
- Cross-method ARI as a K-selection criterion when per-method fit decreases monotonically with K. [src: ibd_phage_targeting]
- The OvR-AUC versus per-patient agreement gap as a diagnostic of classifier-utility overstatement when a cohort-axis variable dominates features. [src: ibd_phage_targeting]
- The observation that, in Kaiju-to-MetaPhlAn3 projection, LDA is robust while CLR+GMM is fragile. [src: ibd_phage_targeting]
- A project-wide synonymy layer as a reusable artifact for multi-cohort microbiome work. [src: ibd_phage_targeting]

## Interpretation: Novel contributions (2)

This part of the report covers its novel contributions: cross-cohort metabolomics replication, a single joint CD axis in HMP2, converging phage evidence, per-patient cocktail design with a state-dependent dosing rule, and the limits of the ecotype framework. The dosing rule rests on one patient, and the report calls it a hypothesis for prospective validation. [src: ibd_phage_targeting] The cross-cohort replication count comes from the HMP2-to-FRANZOSA_2019 comparison. [src: ibd_phage_targeting]

### Cross-cohort metabolomics replication

The HMP2-to-FRANZOSA_2019 comparison, bridged by m/z at ±0.005 Da, established 9 strict and 3 theme-level replications. [src: ibd_phage_targeting] Three chemical-class themes passed the ≥75 % sign-concordance threshold:
- Urobilin/porphyrin: 100 %, CD-DOWN. [src: ibd_phage_targeting]
- Acyl-carnitines: 80 %, CD-up. [src: ibd_phage_targeting]
- Long-chain PUFAs: 75 %, CD-up. [src: ibd_phage_targeting]

The urobilin signal had a median Franzosa cliff of −0.747, the strongest replicated effect in the project. The report reads it as loss of bilirubin-reducing commensals across cohorts. [src: ibd_phage_targeting]

Cohort-aggregate bile-acid differential abundance was weaker, with 57 % primary and 40 % secondary concordance. The report treats this as a different evidence stream from the within-cohort paired substrate–product signature, and says one can be weaker without invalidating the other. [src: ibd_phage_targeting]

### A single joint axis in HMP2

A canonical correlation analysis (CCA) of HMP2 paired taxonomy and metabolomics gave a first canonical pair (CC1) with r=0.96 and a CD-versus-nonIBD cliff of +0.50 (p=4e-4). It recovered, in one axis, signatures the report had developed in separate analyses. [src: ibd_phage_targeting]
- All 6 actionable Tier-A core species load CD-positive. [src: ibd_phage_targeting]
- Urobilin and secondary bile acids load CD-negative. [src: ibd_phage_targeting]
- Polyamines, PUFAs, fatty-acid amides, sphingolipids, cadaverine and N-acetylputrescine load CD-positive. [src: ibd_phage_targeting]

The report concludes that the CD-versus-nonIBD state in HMP2 species–metabolite space is a single principal direction, not a many-axis manifold. [src: ibd_phage_targeting] It adopts CC1 as the operational definition of CD biology in HMP2 for cocktail design and clinical translation. [src: ibd_phage_targeting]

### Converging phage evidence and the anaerobe gap

The phage evidence has three layers: curated literature, PhageFoundry susceptibility data (96 phages × 188 E. coli strains × 17,672 pairs), and in-vivo HMP2 phageome data (630 samples). [src: ibd_phage_targeting] The layers agree. E. coli phage availability shows in all three, and Hungatella hathewayi and Flavonifractor plautii are coverage gaps in all three. [src: ibd_phage_targeting] The report treats all three layers as necessary but none as sufficient for cocktail design. [src: ibd_phage_targeting] See [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]].

Among 23 UC Davis CD patients, all 9 E1 patients carried the full 5-species Tier-A module: H. hathewayi, F. plautii, Enterocloster bolteae, Eggerthella lenta and Mediterraneibacter gnavus. [src: ibd_phage_targeting] Only 3 of the 5 have direct lytic phage options: E. lenta PMBT5, E. bolteae PMBT24, and E. coli AIEC if present. [src: ibd_phage_targeting] The report therefore calls a pure phage cocktail for the full E1 module structurally infeasible. [src: ibd_phage_targeting] It proposes a 3-strategy hybrid:
- Direct phage targeting.
- GAG-degrading enzyme inhibitors for H. hathewayi, and bile-acid-binding co-therapy for F. plautii.
- Lytic-locked engineering, or a glucorhamnan-synthesis target, for M. gnavus. [src: ibd_phage_targeting]

More generally, the report names gut-anaerobe phage availability as the structural ceiling on cocktail completeness. Pure phage cocktails work for Enterobacteriaceae-dominated dysbiosis only in the E. coli AIEC subset where phage diversity is high (EcoActive precedent). The dominant anaerobe pathobionts (H. hathewayi, M. gnavus, F. plautii) need alternative or hybrid strategies. [src: ibd_phage_targeting]

### Longitudinal case and state-dependent dosing

Patient 6967 is the only multi-timepoint UC Davis CD patient with biological replicates. This patient shifted from E1 to E3 across 2 visits, with M. gnavus expanding 14× (0.53 → 7.45). [src: ibd_phage_targeting] Cocktail Jaccard between visits was 0.60, with 3 shared and 2 visit-1-only targets. [src: ibd_phage_targeting] Patient 1112's two resequencing replicates gave Tier-A Spearman ρ = 1.000. The report takes this as evidence that Kaiju calls are reliable. [src: ibd_phage_targeting]

The report derives these rules:
- Retest ecotype every 3-6 months, because ecotype is dynamic. [src: ibd_phage_targeting]
- M. gnavus, H. hathewayi and E. lenta form a universal Tier-1 backbone spanning E1 and E3. It does not need re-evaluation on ecotype shift. [src: ibd_phage_targeting]
- F. plautii inclusion is E1-specific, so drop it on E1→E3. E. coli inclusion is E3-specific, subject to AIEC strain detection on E3→E1. [src: ibd_phage_targeting]
- M. gnavus qPCR is a candidate cheap proxy for ecotype state. A 5-fold change triggers a full retest. [src: ibd_phage_targeting]

The rule comes from a single trajectory. n=1 limits generalization, and the report calls it a hypothesis for prospective validation, not established clinical practice. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

### Limits of the ecotype framework

Cross-study stability is weak. Bootstrap ARI (adjusted Rand index) of 0.13–0.17 understated the instability. Leave-one-substudy-out (LOSO) ARI across the top 8 sub-studies had mean 0.113 and range [0.000, 0.282]. [src: ibd_phage_targeting] Alignment varies by sub-study. LifeLinesDeep (0.21 / 85 % agreement) and HansenLBS (65 %) align well. AsnicarF (38 %) and VilaAV (17 %) do not. [src: ibd_phage_targeting] Part of the variance reflects the comparison baseline, since the NB01b consensus has only 48.9 % cross-method agreement. The report still says the "four reproducible ecotypes" framing must be qualified. [src: ibd_phage_targeting]

The framework is still usable. HMP2 external projection recovers non-random disease stratification (χ² p=0.016), and 80 % of samples have max posterior > 0.70. [src: ibd_phage_targeting] The operational E1 Tier-A replicates at 88.2 % sign concordance. [src: ibd_phage_targeting]

Refitting on pathway features only partly recovers the ecotypes: ARI 0.113 on 3,145 CMD_IBD samples. [src: ibd_phage_targeting] E1 is the most recoverable (65.3 % agreement) and E3 the weakest (30.7 %), which reinforces E3's provisional status. [src: ibd_phage_targeting] The report reads the structure as mixed ecological and taxonomic. [src: ibd_phage_targeting] See [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

### Gaps by ecotype

- **E3:** The 40-candidate Tier-A list derives from HallAB_2017 only. [src: ibd_phage_targeting] HMP2 projection places only 10 of 130 subjects in E3 versus 106 in E1, so it cannot supply a second-substudy meta-analysis. [src: ibd_phage_targeting] E3 Tier-A stays provisional until a sub-study with enough E3 samples and both diagnosis groups is available. [src: ibd_phage_targeting]
- **E0 and E2:** These are healthy-cohort ecotypes. E0 is 66.8 % of HC, and E2 is the P. copri enterotype, almost entirely non-Western healthy. [src: ibd_phage_targeting] No IBD sub-study in cMD supplies nonIBD controls for them, so a confound-free CD-vs-nonIBD contrast cannot be computed. [src: ibd_phage_targeting]
- **UC Davis E0 patients (27 % of the cohort):** Their Tier-A must come from cross-ecotype cohort-level evidence (the 5 engraftment-confirmed pathobionts) or from ecotype-agnostic within-substudy CD-vs-nonIBD evidence. [src: ibd_phage_targeting]
- **HMP2 reingestion:** HMP2 MetaPhlAn3 is not yet ingested (PENDING_HMP2_RAW in lineage.yaml). [src: ibd_phage_targeting] Reingestion would add a second IBD sub-study for E3 replication, expand CMD + HMP2 to ≈ 11.5 K samples for ecotype refitting, and enable serology-by-ecotype integration. [src: ibd_phage_targeting]

### Other caveats

- UC Davis has n = 23 patients, so the Pillar 5 per-patient cocktail drafts need validation in external CD cohorts. [src: ibd_phage_targeting]
- The Kaiju versus MetaPhlAn3 classifier mismatch limits confidence in UC Davis ecotype calls. LDA is more trustworthy than GMM here. [src: ibd_phage_targeting]
- The extended classifier is effectively E1-vs-E3 binary, because its within-ecotype subset has only 3 E2 and 11 E0 samples. [src: ibd_phage_targeting]
- Ecotype calls are hard assignments of an underlying continuum and are operational labels, not biology. Soft probabilities are kept in data/ecotype_assignments.tsv. [src: ibd_phage_targeting]
- The planned differential-abundance consensus required ≥ 2 / 3 agreement among ANCOM-BC, MaAsLin2 and LinDA, but the implemented consensus is partial. [src: ibd_phage_targeting] LinDA was implemented in pure Python to avoid the R/rpy2 dependency. [src: ibd_phage_targeting] The NB04c bootstrap-CI and NB04e within-substudy-meta outputs are additional evidence streams, not drop-in substitutes for ANCOM-BC or MaAsLin2. A full R-native three-method consensus remains a publication-grade follow-up. [src: ibd_phage_targeting]

## Interpretation: Limitations

The report states limits on statistical independence. [src: ibd_phage_targeting] It also states limits on the cross-feeding hypothesis. [src: ibd_phage_targeting] Further limits cover the iron-siderophore comparator [src: ibd_phage_targeting], phage availability [src: ibd_phage_targeting], the small UC Davis cohort [src: ibd_phage_targeting] and the calprotectin threshold. [src: ibd_phage_targeting]

### Statistical independence and weak replication

CLR-MW and LinDA both use the same ecotype-defined subsamples. They share a selection-on-outcome bias, so bootstrap stability does not remove feature leakage. [src: ibd_phage_targeting] Only the within-substudy CD-vs-nonIBD contrast is an independent evidence source. This is why the NB04d Tier-A gating requires within-substudy concordance. [src: ibd_phage_targeting] See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

Pillar 2 cross-cohort replication is weak. The Tier-A list, especially E3, should be treated as hypotheses for experimental validation, not established targets. The UC Davis cocktail drafts inherit this limitation. [src: ibd_phage_targeting]

### Cross-feeding hypothesis not supported

Paired sample-level metabolite-metagenomic data (NB09c) do not support the NB07c cross-feeding hypothesis. [src: ibd_phage_targeting] Only 7 strict cross-feeding triangles emerge. Lactate × Anaerostipes caccae (+0.18) has the opposite sign to lactate × Flavonifractor plautii (-0.23) and lactate × Enterocloster bolteae (-0.20). That is inconsistent with a lactate-mediated loop. [src: ibd_phage_targeting] The report reads the NB07c coupling as shared-environment co-occurrence in healthy or normobiotic samples. [src: ibd_phage_targeting] It infers that phage targeting of pathobionts is unlikely to substantially deplete A. caccae through metabolic coupling. [src: ibd_phage_targeting] See [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]].

The E3_CD module couples more weakly than E1_CD. Its two oral Actinomyces anchors couple only weakly (~ρ=0.17–0.19) to module pathobionts. [src: ibd_phage_targeting] The NB07c cocktail-design implication is therefore E1-specific. UC Davis E3 patients (31 % of the cohort) may need a different module-anchor framework. [src: ibd_phage_targeting]

### Iron-siderophore signature

The narrowing of the iron theme to Escherichia coli is correlation-based. It uses species-by-pathway Spearman ρ across CMD_IBD samples. [src: ibd_phage_targeting] The v1.8 analysis found that 8 of 15 iron pathways were menaquinol biosynthesis, which is not strictly E. coli-specific. [src: ibd_phage_targeting] The strongest signature pathways, ENTBACSYN-PWY and HEMESYN2-PWY, are E. coli-canonical. [src: ibd_phage_targeting] NB08a adds direct genomic evidence. E. coli alone among actionable Tier-A core species carries iron-siderophore MIBiG matches, with 54 BGCs (biosynthetic gene clusters) versus 0 in the other 5 actionable species. [src: ibd_phage_targeting] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

Several limits apply:
- HUMAnN3 species-stratified attribution needs raw reads and was dropped per plan v1.9. NB08a genomic BGC content is the substitute within the no-raw-reads scope. [src: ibd_phage_targeting]
- The strict H3c species-by-BGC interaction test remains untested and was dropped per plan v1.9. [src: ibd_phage_targeting]
- NB08a Test 3 uses the ref_cborf_enrichment CD-vs-HC main-effect table. Its CB-ORF CD-up enrichment cannot separate an interaction from species and BGC main effects. [src: ibd_phage_targeting]
- The interaction test needs raw-read-dependent species-stratified per-sample BGC abundance. The report calls the drop a structural scope limitation, not a deferred follow-up. The operational NB08a test is main-effect-only. [src: ibd_phage_targeting]
- The Tier-A background comparator is the full catalog of 10,060 BGCs across all species, not a matched comparator. [src: ibd_phage_targeting]
- The Fisher odds ratio (OR) of 44× for iron_siderophore is partly inflated by the catalog-wide rarity of iron MIBiG matches (51 / 9,774 = 0.5 %). It should not be read as a precise effect size. [src: ibd_phage_targeting]
- The report proposes a more conservative matched-niche comparator. It would combine gut Proteobacteria and CD-associated Firmicutes at similar genome-assembly depth. [src: ibd_phage_targeting]
- The report states that the qualitative E. coli-only signature is robust across comparator choices. [src: ibd_phage_targeting]

### Phage availability

The report names INPHARED and IMG/VR queries as the highest-priority external extension before clinical translation. Its internal-only scope excludes them. [src: ibd_phage_targeting] See [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]].

The E1 patient cocktail draft is a hybrid 3-strategy framework, not a pure phage cocktail. The report calls this a structural property of gut-anaerobe phage availability. [src: ibd_phage_targeting]

PhageFoundry holds 96 phages × 188 E. coli strains × 17,672 susceptibility pairs. The report calls this sufficient for a 5-phage AIEC (adherent-invasive E. coli) cocktail at 95 % strain coverage. [src: ibd_phage_targeting] The other 5 actionable Tier-A species are not in phagefoundry_strain_modelling. Their phage availability rests on ref_phage_biology literature curation alone. [src: ibd_phage_targeting] The 95 % figure applies to the 188 PhageFoundry-tested strains, not UC Davis patient isolates. Patient applicability needs AIEC strain-resolution diagnostics on stool isolates, queued in the NB17 near-term roadmap. [src: ibd_phage_targeting]

### HMP2 viromics

HMP2 viromics has 80 % Unknown family classification, so most phage observations cannot be linked to a target host. [src: ibd_phage_targeting] The E. coli correlations with Podoviridae (+0.18) and Myoviridae (+0.13) are restricted to the classifiable 20 %. [src: ibd_phage_targeting] Better resolution needs VirMAP/MARVEL reruns with newer phage reference databases, which is out of scope. [src: ibd_phage_targeting]

NB14 phageome effect sizes with ecotype and diagnosis are modest (max |ρ|≤0.18). The phageome is a noisier channel than species taxonomy, where NB04e effect sizes routinely have |CLR-Δ|>1.0. [src: ibd_phage_targeting] The 3-layer phage-evidence convergence rests on directional concordance, not matched effect sizes. [src: ibd_phage_targeting]

### UC Davis cohort and clinical translation

The 23-patient UC Davis cohort is small. Per-patient cocktail recommendations are exemplars or templates, not statistically robust validation. Generalization needs multi-center validation. [src: ibd_phage_targeting] The operational strategy distribution is 12 reserve / 4 E1 hybrid / 4 E0 limited / 1 E1 full / 1 E3 / 1 state-dependent. It should be revisited in a larger CD cohort. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

- **Bile acids:** The cohort has no per-patient bile-acid measurements. The F. plautii bile-acid-coupling-cost annotation is ecotype-level evidence from paired HMP2 samples. [src: ibd_phage_targeting] Clinical translation requires per-patient bile-acid panels for monitoring and dosing. [src: ibd_phage_targeting]
- **AIEC diagnostics:** The cohort has no per-patient AIEC strain-resolution diagnostic. Eight of 23 patients carry detectable E. coli by Kaiju. The 5-phage AIEC recommendation assumes AIEC-subset prevalence from Dogan 2014 / Dubinsky 2022. [src: ibd_phage_targeting] Per-patient genotyping for pks-island, Yersiniabactin and Enterobactin is a near-term prerequisite. [src: ibd_phage_targeting]
- **Dosing rules:** The state-dependent dosing rule is n=1. Patient 6967 is the only multi-timepoint patient with biological-replicate samples. [src: ibd_phage_targeting] The 5 dosing rules and the clinical workflow are mechanistically interpretable through ecotype biology and per-ecotype module structure. Prospective validation needs expanded longitudinal sampling. [src: ibd_phage_targeting]
- **Patient 1112:** Its technical-replicate Spearman ρ=1.000 validates the technical-noise floor. It is not a biological-replicate trajectory. [src: ibd_phage_targeting]
- **Timing:** Visit timing and the duration of patient 6967's E1→E3 drift are unknown. The 3-6 month re-test interval is a clinical-convention default, not derived from data. [src: ibd_phage_targeting]
- **M. gnavus qPCR proxy:** It is a hypothesis. The 14× expansion in patient 6967's E3 transition suggests a 5-fold trigger for full ecotype re-testing, but it comes from a single trajectory. [src: ibd_phage_targeting] Validation needs a prospective cohort with paired qPCR and metagenomics across timepoints. [src: ibd_phage_targeting]
- **Cocktail Jaccard 0.60:** Its generalizability is unknown. Whether 3-of-5 component overlap warrants redesign depends on patient-response heterogeneity, which is outside project scope. [src: ibd_phage_targeting]
- **Calprotectin threshold:** NB17 splits active from quiescent patients at 250 μg/g. This clinical convention is not validated against per-patient response. [src: ibd_phage_targeting] Some patients at 41–248 μg/g, currently C_quiescent, may benefit from an active cocktail. The threshold should be re-evaluated in a pilot. [src: ibd_phage_targeting]

## Data: Generated data

This part of the report lists the data sources behind the analysis. They are the local CrohnsPhage mart, other Lakehouse collections queued for later notebooks, and the project's own derived data files. Several derived files are marked superseded or retracted but kept for audit. [src: ibd_phage_targeting]

### Local and queued sources

The local CrohnsPhage star-schema mart (v10, schema v2.4) supplies sample and participant metadata, MetaPhlAn3 and Kaiju taxonomy, severity markers, and UC Davis demographics. [src: ibd_phage_targeting] The tables used are dim_samples, dim_participants, fact_taxon_abundance, fact_clinical_longitudinal, ref_taxonomy_crosswalk, and crohns_patient_demographics.xlsx. [src: ibd_phage_targeting] See also [[entities/crohnsphage-data-mart]].

The report queues the following collections for later notebooks:

| Source | Queued for | Purpose |
|---|---|---|
| kbase_ke_pangenome | NB04+ | Pangenome, AMR (antimicrobial resistance) and GapMind functional analysis, Pillar 2/3 [src: ibd_phage_targeting] |
| kescience_mgnify | external validation | Independent IBD-cohort cross-check [src: ibd_phage_targeting] |
| phagefoundry_strain_modelling, phagefoundry_ecoliphages_genomedepot, phagefoundry_klebsiella_* | NB12+ | Phage-host interaction and coverage matrix, Pillar 4 [src: ibd_phage_targeting] |
| kescience_fitnessbrowser | NB13 | Phage-resistance fitness-cost inference, Tier-C C3 [src: ibd_phage_targeting] |
| kescience_paperblast, kescience_pubmed | NB05 | Literature-linked mechanism, Tier-A A3 [src: ibd_phage_targeting] |
| kescience_bacdive | Pillar 2/3 | Strain phenotype context [src: ibd_phage_targeting] |

### Derived files: ecotype definition and UC Davis projection

The project built a species synonymy layer and the ecotype assignments. `data/species_synonymy.tsv` (2,417 rows) is an alias-to-canonical species map. [src: ibd_phage_targeting] `data/ecotype_assignments.tsv` (8,489 rows) holds the K = 4 consensus ecotype per CMD sample, with LDA and GMM (Gaussian mixture model) calls and a `methods_agree` flag. [src: ibd_phage_targeting]

The UC Davis files are:
- `ucdavis_kuehl_ecotype_projection.tsv` (26 rows), a per-sample Kuehl projection onto the K = 4 embedding. [src: ibd_phage_targeting]
- `ucdavis_patient_ecotype_summary.tsv` (23 rows), a per-patient ecotype call merged with clinical covariates. [src: ibd_phage_targeting]
- `ucdavis_clinical_ecotype_prediction.tsv` (23 rows), classifier-only predictions for agreement testing. [src: ibd_phage_targeting]

### Derived files: DA and Tier-A refinement

NB04 and its sub-notebooks went through several rounds of revision. The earliest outputs are marked superseded or retracted but kept for audit. [src: ibd_phage_targeting] In the file descriptions below, "DA" is the report's own abbreviation.

- `nb00_protective_species_da_comparison.tsv` (14 rows) compares raw-MW and CLR-MW calls for the protective-species battery. [src: ibd_phage_targeting]
- `nb04_h2c_protective_battery.tsv` (15 rows) is superseded. It gives per-species verdicts across pooled raw, pooled CLR, E1 CLR and E3 CLR. [src: ibd_phage_targeting]
- `nb04_tier_a_candidates.tsv` (33 rows) is the retracted original within-ecotype Tier-A. [src: ibd_phage_targeting]
- `nb04_da_ecotype_1.tsv` (248 rows) and `nb04_da_ecotype_3.tsv` (201 rows) are superseded within-E1 and within-E3 CD-vs-HC CLR-MW DA at FDR < 0.1. [src: ibd_phage_targeting]
- `nb04_da_pooled_clr.tsv` (321 rows) is pooled CLR MW, kept for reference. [src: ibd_phage_targeting]
- `nb04b_battery_bootstrap_ci.tsv` (45 rows) gives bootstrap CIs with a TOST-equivalence verdict for the 14-species battery across pooled, E1 and E3. [src: ibd_phage_targeting]
- `nb04b_battery_LOO.tsv` (26 rows) gives leave-one-species-out refit verdicts. [src: ibd_phage_targeting]
- `nb04b_held_out_sensitivity.tsv` (10 rows) gives held-out-species sensitivity Jaccards as a leakage bound. [src: ibd_phage_targeting]
- `nb04b_tier_a_refined.tsv` (33 rows) is an intermediate bootstrap-CI refinement of NB04 Tier-A. [src: ibd_phage_targeting]
- `nb04c_within_substudy_cd_nonibd.tsv` (152 rows) gives per species × substudy CD-vs-nonIBD bootstrap CIs. [src: ibd_phage_targeting]
- `nb04c_within_substudy_meta.tsv` (38 rows) is a cohort-level IVW meta-analysis across 4 IBD substudies. [src: ibd_phage_targeting]
- `nb04c_linda.tsv` (1,005 rows) gives LinDA bias-corrected results per species across pooled, E1 and E3. [src: ibd_phage_targeting]
- `nb04c_lme.tsv` has 0 rows. It is empty on purpose, to document that pooled CD-vs-HC linear mixed-effects modelling is structurally unidentifiable. [src: ibd_phage_targeting]
- `nb04c_tier_a_refined.tsv` (33 rows) is a 3-way-evidence refinement using bootstrap, LinDA and within-substudy results. [src: ibd_phage_targeting]
- `nb04d_stopping_rule_verdict.json` holds the per-ecotype stopping-rule verdict and the NB05 input set. [src: ibd_phage_targeting]
- `nb04e_per_cell_DA.tsv` (1,005 rows) gives DA per ecotype × substudy cell. [src: ibd_phage_targeting]
- `nb04e_within_ecotype_meta.tsv` (670 rows) is the rigor-controlled Tier-A, a per-ecotype meta-analysis across eligible substudies. [src: ibd_phage_targeting]
- `nb04e_option_A_viability.json` holds the viability verdict for Option A (within-ecotype × within-substudy). [src: ibd_phage_targeting]

### Derived files: ecotype stability and replication

The leave-one-substudy-out (LOSO) check, `nb04f_loso_stability.tsv` (8 rows), gives per-substudy ARI (adjusted Rand index) and agreement. [src: ibd_phage_targeting] Its formal verdict is a mean ARI of 0.113, labelled "study-dependent". [src: ibd_phage_targeting] See [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

`nb04g_pathway_ecotype_assignments.tsv` (3,145 rows) gives a pathway-ecotype label alongside the taxon-ecotype label per sample. [src: ibd_phage_targeting] The comparison of the two gives ARI 0.113 and a PARTIAL verdict. [src: ibd_phage_targeting]

The HMP2 replication files are:
- `nb04h_hmp2_ecotype_projection.tsv` (1,627 rows), HMP2 per-sample ecotype and max posterior. [src: ibd_phage_targeting]
- `nb04h_hmp2_subject_ecotype.tsv` (130 rows), per-subject ecotype mode and disease_subtype. [src: ibd_phage_targeting]
- `nb04h_hmp2_e1_cd_vs_nonibd.tsv` (335 rows), within-E1 CD-vs-nonIBD CLR-Δ per species. [src: ibd_phage_targeting]
- `nb04h_e1_tier_a_hmp2_replication.tsv` (51 rows), the NB04e E1 Tier-A cross-referenced with HMP2 E1 CD-vs-nonIBD. [src: ibd_phage_targeting]
- `nb04h_hmp2_replication_verdict.json`, the formal external replication verdict, PASS. [src: ibd_phage_targeting]

### Derived files: scoring, networks and pathways

`nb05_tier_a_scored.tsv` (71 rows) is the authoritative NB05 output. It has A3–A6 score breakdowns, a total score and an actionable flag. [src: ibd_phage_targeting] The NB05 summary reports 6 actionable targets of 71 scored. [src: ibd_phage_targeting] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

The NB06 files are:
- `nb06_edges_{subnet}.tsv` (variable row count), per-subnet edge lists with |rho| > 0.3 and FDR < 0.05. [src: ibd_phage_targeting]
- `nb06_modules.tsv` (~20 rows), a per-subnet module summary with actionable and tier-B content. [src: ibd_phage_targeting]
- `nb06_module_hubs.tsv` (~15 rows), the top-3 hub species per module by degree. [src: ibd_phage_targeting]
- `nb06_verdict.json`, the NB06 summary and H2d verdict. [src: ibd_phage_targeting]

For pathways, `nb07_h3a_v18_pathway_classes.tsv` (575 rows) maps HUMAnN3 pathways to MetaCyc classes and IBD themes, as an audit trail for the v1.8 schema. [src: ibd_phage_targeting] `nb07_h3a_v18_cohort_enrichment.tsv` (12 rows) holds per-theme cohort-level Fisher enrichment. [src: ibd_phage_targeting] Its iron/heme theme has OR=8.1 and FDR 7e-6. [src: ibd_phage_targeting]

## Data: Generated data (2)

This part of the report lists the data files it provides for the IBD phage-targeting analysis. The listing records each file's contents and, for several, a formal hypothesis verdict. The entries are the report's own descriptions of its outputs. [src: ibd_phage_targeting]

### Pathobiont and pathway-theme tests

The per-species pathway-theme Fisher enrichment supports 2 themes for *H. hathewayi*, and the formal v1.8 H3a (b) verdict is SUPPORTED. [src: ibd_phage_targeting] The anchor × pathobiont file has 27 pairs with within-IBD-substudy ρ_meta and sign concordance. A second file crosses these 27 pairs with 15 v1.8 iron pathways, giving 405 triples. [src: ibd_phage_targeting] The H3a-new verdict is PARTIAL: the *A. caccae* coupling is clean in E1_CD. [src: ibd_phage_targeting]

### Biosynthetic gene clusters and Crohn's disease signal (NB08a)

The Tier-A core species' biosynthetic gene cluster (BGC) repertoire file has 6 rows. [src: ibd_phage_targeting] The BGC-theme Fisher enrichment of Tier-A core against background gives iron OR=44 and genotoxin OR=234. [src: ibd_phage_targeting] The per-species counts are concentrated in one species. *E. coli* has 54 iron and 25 genotoxin MIBiG counts, and the other Tier-A core species have 0+0. [src: ibd_phage_targeting]

A per-species table gives the CB-ORF CD-up rate at false discovery rate (FDR) <0.10, against a catalog background of 2.5 %. [src: ibd_phage_targeting] The ebf/ecf cohort meta-analysis uses Stouffer's z over 4 cohorts, and both p are <1e-31. [src: ibd_phage_targeting] The formal H3c verdict is PARTIALLY SUPPORTED. [src: ibd_phage_targeting]

### Metabolomics (NB09a–d)

The differential-abundance table covers 579 named metabolites, with Mann-Whitney, cliff_delta, FDR, theme assignments and a passes flag. [src: ibd_phage_targeting] Theme enrichment covers 11 themes × {CD-up, CD-down}, with Fisher OR and Benjamini-Hochberg FDR (BH-FDR). It supports polyamines and polyunsaturated fatty acids (PUFAs). [src: ibd_phage_targeting] The formal H3d-DA verdict is SUPPORTED. [src: ibd_phage_targeting]

The report's per-theme cross-cohort sign concordance is urobilin 100 %, acyl-carnitines 80 % and PUFAs 75 %. [src: ibd_phage_targeting] A separate file holds 122 matched HMP2-name × Franzosa-peak pairs, and the per-theme summary file has 8 rows. [src: ibd_phage_targeting] The formal replication verdict is STRONG on 3 themes, with 9 strict replications. [src: ibd_phage_targeting]

The species–metabolite correlation file covers 8 species × 583 metabolites, with paired Spearman ρ and per-species FDR. [src: ibd_phage_targeting] Seven strict cross-feeding triangles meet same sign, |ρ|>0.20 and FDR<0.10. [src: ibd_phage_targeting] A curated panel covers 7 themes × 8 species. [src: ibd_phage_targeting] The NB09c verdict does not support cross-feeding, but it identifies a bile-acid 7α-dehydroxylation network. [src: ibd_phage_targeting]

The metabolite-ecotype assignments cover 326 pooled subjects at K=4. [src: ibd_phage_targeting] The H3d-clust hypothesis is NOT SUPPORTED, because cohort batch effect dominates m/z-bridge clustering. [src: ibd_phage_targeting]

### Strain adaptation (NB10a)

The H3b verdict is SUPPORTED, with adaptation enrichment and housekeeping depletion. [src: ibd_phage_targeting] The per-species bias counts cover 59 Kumbhari species. [src: ibd_phage_targeting] The classified significant genes number 23,579 at FDR<0.10 across 13 functional categories. [src: ibd_phage_targeting] Two further files rank cross-species IBD-biased KEGG orthologs (KOs) and gene symbols by n_species. [src: ibd_phage_targeting] The *F. plautii* FDR<0.10 strain-adaptation deep dive has 0 rows, which the report calls an informative null. [src: ibd_phage_targeting]

### Serology (NB11)

The serology correlations have 48 rows, with site-adjusted partial Pearson r, raw Spearman ρ and BH-FDR. [src: ibd_phage_targeting] The site-stratified file gives Spearman ρ for the top 10 pairs across 3 sites, 30 rows. [src: ibd_phage_targeting] H3e receives a PARTIAL verdict, because the strict |r|>0.40 threshold was not met. [src: ibd_phage_targeting]

### Joint omics and phage availability

The joint-omics files hold canonical loadings (120 rows) and subject scores for 106 paired-CSM subjects. CC1 captures the CD-vs-nonIBD axis. [src: ibd_phage_targeting] The pilot is called SUCCESSFUL, with CC1 canonical r=0.96 and a CD-vs-nonIBD cliff of +0.50 (p=4e-4). [src: ibd_phage_targeting] The final matrix scores each of the 6 Tier-A core pathobionts for phage availability (0-3). It also lists therapeutic targets and a Pillar-5 priority class. [src: ibd_phage_targeting]

## Data: Generated data (3)

This part of the report lists the output and input data files for its later analysis stages (notebooks NB12–NB17). The stages cover phage availability, E. coli strain modelling, in-vivo phageome associations, per-patient cocktail design, longitudinal dosing, and the final verdicts. [src: ibd_phage_targeting]

### Phage availability and cocktail design (NB12–NB13)

The NB12 verdict file holds the Pillar 4 opener verdict and a 4-class phage-availability stratification. [src: ibd_phage_targeting] The NB13 strain-modelling table has 17,672 rows. It holds susceptibility pairs for 96 phages × 188 E. coli strains from PhageFoundry (Gaborieau 2025). [src: ibd_phage_targeting] A greedy minimum-set-cover 5-phage cocktail of DIJ07_P2 + LF73_P1 + AL505_Ev3 + 55989_P2 + LF110_P2 covers 94.7% of the 188 strains. [src: ibd_phage_targeting] The NB13 verdict file holds the formal cocktail design verdict and AIEC (adherent-invasive Escherichia coli) phylogroup B2/D coverage. [src: ibd_phage_targeting] See [[entities/phagefoundry]] and [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]].

### In-vivo phageome (NB14)

The NB14 table gives HMP2 viromics × ecotype × diagnosis Spearman ρ, Cliff's δ and FDR (false discovery rate) for each phage family. Its row count varies. [src: ibd_phage_targeting] The verdict file labels Gokushovirus as CD-DOWN (CD is Crohn's disease). [src: ibd_phage_targeting] It lists the E. coli × Podo/Myo associations as +0.18/+0.13. [src: ibd_phage_targeting]

### Per-patient cocktails and longitudinal dosing (NB15–NB16)

A long-format table breaks down the cocktail by patient and target (component, evidence, caveat). Its row count varies. [src: ibd_phage_targeting] The Pillar 5 opener verdict file holds a per-ecotype prescribing summary and 4 patient-design categories. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

The NB16 longitudinal table has 6 rows for patient 6967. It records per-visit Tier-A abundance and fold change, with a move from visit 1 E1 to visit 2 E3. [src: ibd_phage_targeting] It reports a 14× expansion of M. gnavus. [src: ibd_phage_targeting] The longitudinal verdict file reports cocktail Jaccard 0.60 and Spearman ρ=1.000. It also lists 5 state-dependent dosing rules. [src: ibd_phage_targeting]

### Closure files (NB17)

The NB17 patient master table has 23 rows. It is the Pillar 5 closure capstone. It combines the full master attributes with design category, cocktail strategy and longitudinal status. [src: ibd_phage_targeting] The target decision matrix has 6 rows. It maps 6 actionable Tier-A targets, each with 5 attributes (NB05 score, ecotype, BA cost, mediation, phage tier), to a final priority class. [src: ibd_phage_targeting] The final verdict file holds per-pillar final verdicts, a 24 NC index, a 4-phase clinical-translation roadmap, a thesis statement, and design and strategy distributions. [src: ibd_phage_targeting] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy|pathobiont target prioritization]].

### External inputs and schema

Three HMP2 input files are listed: MetaPhlAn3 relative abundance (582 rows), sample metadata from cMD (1,627 rows) and per-taxon lineage metadata (585 rows). [src: ibd_phage_targeting] The report marks the abundance file as an out-of-project artifact. [src: ibd_phage_targeting] See [[entities/crohnsphage-data-mart]].

## Supporting Evidence: Notebooks

This part of the report lists the notebooks behind the analysis. They run from data audit and ecotype fitting, through rigor repair and external replication, to target scoring, pathway, genomic and metabolomic mechanism layers, and serology. [src: ibd_phage_targeting]

### Data audit and ecotype fitting

NB00 profiles the data mart, reconciles dictionaries and runs a compositional differential-abundance proof of concept on the protective-species battery. [src: ibd_phage_targeting] NB01 scans K = 2..8 on CMD MetaPhlAn3 and commits the synonymy layer. [src: ibd_phage_targeting] NB01b refits K = 4 by consensus, using cross-method adjusted Rand index (ARI) and parsimony. [src: ibd_phage_targeting] NB02 projects UC Davis Kuehl samples onto K = 4, with linear discriminant analysis (LDA) as primary and Gaussian mixture model (GMM) as advisory. [src: ibd_phage_targeting] NB03 builds minimal and extended H1c classifiers and tests them on UC Davis. [src: ibd_phage_targeting]

### Rigor repair and stability

NB04 is superseded and kept for audit. Its claims 1 and 2, from the original within-ecotype Crohn's disease (CD) vs healthy control centered log-ratio (CLR) differential abundance, are retracted. [src: ibd_phage_targeting]

- NB04b adds bootstrap confidence intervals, TOST equivalence verdicts, held-out-species leakage sensitivity, a leave-one-out refit, a Jaccard permutation null for H2b and ecotype bootstrap stability. [src: ibd_phage_targeting]
- NB04c resolves substudies. It runs a confound-free within-IBD-substudy CD-vs-nonIBD meta-analysis and a pure-Python LinDA. It documents that the linear mixed-effects model is unidentifiable and refines Tier-A using 3-way evidence. [src: ibd_phage_targeting]
- NB04d formalizes the NB05 stopping rule, with 4 criteria, per-ecotype verdicts and an input candidate set. [src: ibd_phage_targeting]
- NB04e gives within-ecotype × within-substudy cell counts and differential abundance. It adds a rigor-controlled E1 + E3 Tier-A meta-analysis across eligible substudies. [src: ibd_phage_targeting]

Ecotype replication across studies is weak. NB04f's leave-one-substudy-out (LOSO) test across the top 8 cMD substudies shows cross-study instability, with mean LOSO ARI 0.113. [src: ibd_phage_targeting] NB04g refits K=4 LDA on HUMAnN3 pathway features in 3,145 CMD_IBD samples. It recovers the ecotypes only partially, with ARI 0.113 and E1 65 % agreement. [src: ibd_phage_targeting]

Separately, NB04h projects 1,627 HMP_2019_ibdmdb samples onto K=4 LDA and finds 88.2 % E1 Tier-A sign-concordance. [src: ibd_phage_targeting] It pulls the data with pull_hmp2_metaphlan3.R against curatedMetagenomicData v3.18. [src: ibd_phage_targeting]

### Target scoring and co-occurrence

NB05 scores 71 rigor-controlled candidates on Tier-A A3–A6. It yields 6 actionable targets for Pillar 4/5: H. hathewayi, M. gnavus, E. coli, E. lenta, F. plautii and E. bolteae. [src: ibd_phage_targeting] It runs through run_nb05.py, which bypasses nbconvert because of an environment numpy.bool issue. [src: ibd_phage_targeting]

NB06 tests H2d with CLR, Spearman correlations and Louvain community detection, per ecotype × CD/all subnet. [src: ibd_phage_targeting] It finds that 5/6 actionable Tier-A species form a single pathobiont module per subnet, so multi-target cocktails are appropriate. [src: ibd_phage_targeting]

### Pathway mechanisms

NB07a is the Pillar 3 opener. Within-IBD-substudy CD-vs-nonIBD pathway differential abundance passes clauses a and c of the H3a v1.7 three-clause falsifiability test. Clause b gives a FAIL-degenerate verdict. [src: ibd_phage_targeting]

NB07b runs stratified pathway differential abundance per Tier-A core species. It uses a within-carrier CD-vs-nonIBD meta-analysis, with a single-substudy fallback. [src: ibd_phage_targeting] H. hathewayi shows biosynthesis up and sugar degradation down. [src: ibd_phage_targeting] E. coli pathways are CD-DOWN within carriers, which the report describes as AIEC (adherent-invasive E. coli) strain-level specialization. [src: ibd_phage_targeting]

NB07 v1.8 retests H3a (b) with the ModelSEED MetaCyc class hierarchy, a 12-theme IBD overlay, Fisher per-theme enrichment and Benjamini-Hochberg false discovery rate (BH-FDR). [src: ibd_phage_targeting] Iron/heme is the dominant CD-up theme (OR=8.1, FDR 7e-6), which reverses the v1.7 verdict. [src: ibd_phage_targeting]

NB07c tests H3a-new. It uses CD-specific module-anchor commensal × pathobiont species-level Spearman coupling and an iron-pathway triple correlation. [src: ibd_phage_targeting] A. caccae × pathobiont coupling is clean in E1_CD. [src: ibd_phage_targeting] E. coli dominates iron-pathway co-variation. [src: ibd_phage_targeting]

### Genomic and metabolomic layers

NB08a supplies the H3c genomic mechanism layer. It combines biosynthetic gene cluster (BGC) theme enrichment per Tier-A core, CB-ORF CD-up enrichment and an ebf/ecf cohort meta-analysis. [src: ibd_phage_targeting] Iron-siderophore enrichment is OR=44 for E. coli only. [src: ibd_phage_targeting] Genotoxin enrichment is OR=234. [src: ibd_phage_targeting] ebf/ecf gives p<1e-31 across 4 cohorts. [src: ibd_phage_targeting]

NB09a tests H3d-DA on HMP2 subject-level CD-vs-nonIBD metabolomics (50 vs 26 subjects), with 11-theme Fisher enrichment. [src: ibd_phage_targeting] It supports H3d-DA, with 52 metabolites and 2 themes: polyamines OR=14.6 and PUFAs OR=7.9. [src: ibd_phage_targeting] Tauro-muricholate confirms an F. plautii 7α-dehydroxylation deficit. [src: ibd_phage_targeting]

NB09c uses 468 paired CSM* samples × 8 species × 583 metabolites. It disambiguates the NB07c cross-feeding and examines the bile-acid 7α-dehydroxylation network. [src: ibd_phage_targeting] Cross-feeding is not supported. Only 7 strict triangles appear, and lactate associations have opposite signs between A. caccae and pathobionts. [src: ibd_phage_targeting] The bile-acid network is identified. F. plautii, E. lenta and E. bolteae show the predicted primary-tauro-BA-down and secondary-BA-up substrate-product signature. [src: ibd_phage_targeting] NB09c therefore reframes NB07c as shared-environment co-occurrence. It introduces "bile-acid coupling cost" as the primary Pillar 4 annotation. [src: ibd_phage_targeting]

NB09b bridges HMP2 to FRANZOSA_2019, which has 220 participants (88 CD, 76 UC, 56 Control). [src: ibd_phage_targeting] It matches named HMP2 metabolites to Franzosa peaks by m/z within ±0.005 Da, using the same method. This gives 118 testable matched pairs. [src: ibd_phage_targeting] Three themes replicate strongly at ≥75 %. Urobilin replicates at 100 % (CD-DOWN, cliff −0.75), acyl-carnitines at 80 % (CD-up, cliff +0.53) and long-chain PUFAs at 75 % (CD-up, cliff +0.27). [src: ibd_phage_targeting]

### Strain adaptation and serology

NB10a tests the H3b Kumbhari strain-adaptation gene predictor, using 23,579 FDR<0.10 genes across 59 species. It adds a housekeeping-vs-adaptation falsifiability test. [src: ibd_phage_targeting] The result supports IBD-biased adaptation (OR=1.38, p=2.4e-6). [src: ibd_phage_targeting] The same test reports housekeeping OR=0.62 (p=6.4e-20). [src: ibd_phage_targeting] F. plautii has 0 FDR-passing genes. The report calls this an informative null that confirms a species-abundance-mediated CD association and corroborates the NB07b within-carrier analysis. [src: ibd_phage_targeting]

NB11 tests H3e with HMP2 serology × Tier-A pathobiont site-adjusted partial Pearson correlations. It runs 48 assay × species tests across 67 subjects × 3 sites. [src: ibd_phage_targeting] The verdict is PARTIAL. The top pair, ANCA (anti-neutrophil cytoplasmic antibody) × M. gnavus, is +0.31 (FDR 0.40). No pair clears the strict |r|>0.40 + FDR<0.10 threshold. [src: ibd_phage_targeting] The cohort sanity check passes on canonical IBD-serology patterns. [src: ibd_phage_targeting] Site-stratified single-site r reaches +0.46 at Harvard, but cohort aggregation pulls toward null. The report states that the single-cohort caveat is structural. [src: ibd_phage_targeting]

## Supporting Evidence: Notebooks (2)

Replication of several metabolite themes, a failed metabolite-ecotype stability test, a successful joint taxonomy–metabolomics axis, and cocktail drafts for 14 of 23 patients are the main results of these notebooks. [src: ibd_phage_targeting] For E1 patients, a pure phage cocktail is not feasible. [src: ibd_phage_targeting]

### Metabolite replication across cohorts (NB09b)

NB09b finds strong cross-cohort replication on three themes at 75 % or higher: urobilin (100 %, CD-down, cliff −0.75), acyl-carnitines (80 %, CD-up, cliff +0.53) and long-chain PUFAs (75 %, CD-up, cliff +0.27). [src: ibd_phage_targeting] Two limits apply. The polyamine theme cannot be bridged by m/z because of a low-mass HILIC-pos gap. [src: ibd_phage_targeting] Secondary bile acids replicate at only 40 %, and the report states that cohort-aggregate differential abundance is weaker than the paired sample-level evidence in NB09c. [src: ibd_phage_targeting]

### Metabolite ecotypes do not hold across cohorts (NB09d)

The metabolite-feature ecotype hypothesis H3d-clust was not supported. [src: ibd_phage_targeting] NB09d pooled HMP2 and Franzosa data (326 subjects × 111 m/z-bridge features) and ran PCA plus K-means with K=4. [src: ibd_phage_targeting] Cross-cohort leave-one-substudy-out (LOSO) adjusted Rand index (ARI) was 0.000, far below the 0.113 taxonomic baseline from NB04f. [src: ibd_phage_targeting] The clusters were driven by cohort, not diagnosis: PC1 carried 79 % of variance and separated the cohorts cleanly. [src: ibd_phage_targeting] The report concludes that m/z-bridge metabolomics needs explicit batch correction (ComBat/SVA/RUV) before cross-cohort clustering. It keeps taxonomic features as the primary ecotype basis. [src: ibd_phage_targeting] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

### Joint taxonomy–metabolomics pilot (NB07d)

The MOFA+-style pilot succeeded and recovered the pathobiont structure as one joint axis. It used 106 paired CSM* subjects, 130 species and 582 metabolites. Per-modality PCA was followed by CCA to give 4 canonical pairs. [src: ibd_phage_targeting] Pathways were left out because they were not in the mart under the v1.9 no-raw-reads constraint. [src: ibd_phage_targeting] The first canonical component had canonical r=0.96, and the CD-vs-nonIBD cliff was +0.50 (p=4e-4). [src: ibd_phage_targeting] All 6 actionable Tier-A core species load positively on CC1. [src: ibd_phage_targeting] Metabolite loadings recapitulate urobilin CD-down, polyamines, PUFAs, ebf/ecf fatty-acid amides, cadaverine × E. coli and bile-acid depletion on that single axis. [src: ibd_phage_targeting] The report describes this as independent rediscovery of the NB06 H2d pathobiont module structure as a principal direction in joint species-metabolite space. [src: ibd_phage_targeting]

### Phage targetability and cocktail design (NB12–NB14)

NB12 crosses the 6 actionable Tier-A core targets with literature curation in `ref_phage_biology`. It sorts phage availability into clinical-trial, lytic-literature, temperate-only and GAP classes, and cross-references therapeutic targets for alternative strategies. [src: ibd_phage_targeting] NB13 designs an E. coli cocktail from PhageFoundry data (96 phages × 188 strains × 17,672 susceptibility pairs, Gaborieau 2025). [src: ibd_phage_targeting] Greedy minimum-set-cover gives a 5-phage cocktail (DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2, LF110_P2) at 94.7 % strain coverage. [src: ibd_phage_targeting] AIEC (adherent-invasive Escherichia coli) phylogroup B2/D coverage is 65/94 phages. [src: ibd_phage_targeting]

NB14 examined HMP2 viromics (3,039 rows × 630 samples, 97 % NB04h ecotype-call coverage). [src: ibd_phage_targeting] Gokushovirus WZ-2015a was lower in CD across ecotypes, with E1 cliff=-0.358, FDR=5e-7, n_CD=231 vs n_HC=125. The report calls this Microviridae depletion consistent with Norman 2015 and Clooney 2019. [src: ibd_phage_targeting] Endogenous correlations of E. coli with Podoviridae (+0.18) and Myoviridae (+0.13) are reported as confirming in-vivo carriage. [src: ibd_phage_targeting]

### Per-patient drafts and longitudinal rules (NB15–NB16)

NB15 builds cocktail drafts for 23 UC Davis CD patients from ecotype, Montreal classification, calprotectin, medication and Tier-A presence. [src: ibd_phage_targeting] It gives per-target prescribing rates, per-ecotype summaries (E0/E1/E3/mixed) and 4 patient-design categories: active+many, active+few, quiescent and mixed-ecotype. [src: ibd_phage_targeting] Concrete phage cocktails were possible for 14 of 23 patients (61 %). [src: ibd_phage_targeting] A pure phage cocktail is not feasible for E1, which needs a 3-strategy hybrid. F. plautii bile-acid cost is the dominant E1 design constraint. [src: ibd_phage_targeting]

NB16 follows patient 6967, the only multi-timepoint UC Davis CD patient with biological replicates. This patient drifted from E1 to E3 across 2 visits, with a 14× M. gnavus expansion (0.53 → 7.45). [src: ibd_phage_targeting] Cocktail Jaccard between visits was 0.60. Three targets were shared (H. hathewayi, M. gnavus, E. lenta, the universal Tier-1 trio). Two were visit-1-only (E. bolteae, F. plautii). [src: ibd_phage_targeting] Patient 1112's technical replicates gave Tier-A Spearman ρ = 1.000, presented as Kaiju reliability validation. [src: ibd_phage_targeting]

The five state-dependent dosing rules say to re-test ecotype at 3-6 mo. [src: ibd_phage_targeting] They make F. plautii targeting E1-specific [src: ibd_phage_targeting] and E. coli targeting E3-specific. [src: ibd_phage_targeting] They make the universal Tier-1 trio the cocktail backbone. [src: ibd_phage_targeting] They propose M. gnavus qPCR as a cheap clinical proxy, where a 5-fold change triggers a full ecotype re-test. [src: ibd_phage_targeting] NB16 also supplies a clinical workflow of initial visit, follow-up calprotectin/qPCR and an ecotype-shift decision tree. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

### Synthesis (NB17)

NB17 provides a master table for the 23 patients (per-pillar attributes, design category, cocktail strategy, longitudinal status). [src: ibd_phage_targeting] It adds a target decision matrix (6 Tier-A targets × 5 attributes → priority class) [src: ibd_phage_targeting] and a 4-phase roadmap (Immediate / Near / Mid / Long term). [src: ibd_phage_targeting] The final verdict closes all 5 pillars, with 31 notebooks and 24 Novel Contributions. [src: ibd_phage_targeting] The final thesis calls CD a single principal-direction phenomenon (NB07d CC1 r=0.96). Within it, 6 actionable Tier-A pathobionts and 2 cross-corroborated mechanisms (iron and bile-acid 7α-dehydroxylation) define a state-dependent hybrid-cocktail framework, with drafts for 14 of 23 patients. [src: ibd_phage_targeting]

### Other supporting files

The report keeps legacy K = 8 fit figures for methodology audit. [src: ibd_phage_targeting]

## Project Outline (final); Future Directions (out-of-scope clinical-translation …

This part of the report gives the final project outline and the follow-up work it leaves outside scope. The report states that all 5 pillars are closed and that only out-of-scope Pillar-4-followup external-database queries remain. [src: ibd_phage_targeting] It also says the central science question is fully answered within plan v1.9 scope (no raw reads), and it classes the clinical-pilot prerequisites as out-of-scope follow-ups. [src: ibd_phage_targeting]

### Pillar results as closed

Pillar 1 produced four reproducible IBD ecotypes from 8,489 cMD MetaPhlAn3 samples. The report calls H1a directionally supported, and the UC Davis test for H1b gave χ² p=0.019. [src: ibd_phage_targeting] The H1c clinical-covariate classifier passed AUC (area under curve) 0.80 in cross-validation. It agreed with metagenomics on only 41 % of UC Davis patients, so the report revised its position: metagenomics remains required. [src: ibd_phage_targeting] H1c showed that assigning ecotype from clinical covariates alone is not viable. [src: ibd_phage_targeting]

Pillar 2 replaced NB04 with the rigor-repair notebooks NB04b+c+d+e. It added LOSO (leave one substudy out) stability, pathway-feature refitting, HMP2 external replication, Tier-A scoring and per-ecotype co-occurrence networks. [src: ibd_phage_targeting] It identified six actionable Tier-A species: H. hathewayi, M. gnavus, E. coli, E. lenta, F. plautii and E. bolteae. [src: ibd_phage_targeting] HMP2 gave 88.2 % E1 Tier-A external replication. [src: ibd_phage_targeting]

Pillar 3 tested all 8 H3 sub-hypotheses with 12 notebooks. [src: ibd_phage_targeting] The report gives a verdict score of 5 SUPPORTED + 1 PARTIALLY SUPPORTED + 2 PARTIAL + 1 NOT SUPPORTED. [src: ibd_phage_targeting] These verdicts add up to 9, not 8. The claims do not say how the two figures relate, so the report's own counts are left as stated. Pillar 3 also produced two cross-corroborated 6-line mechanism narratives and cross-cohort replication on 3 themes. [src: ibd_phage_targeting] A multi-omics joint factor pilot (NB07d) gave CC1 r=0.96. [src: ibd_phage_targeting]

Pillar 4 used NB12, NB13 and NB14 to build a 3-layer phage-evidence stack. [src: ibd_phage_targeting] It yielded a concrete 5-phage E. coli AIEC (adherent-invasive E. coli) cocktail at 95 % strain coverage. [src: ibd_phage_targeting] The gut-anaerobe Tier-A coverage gap was confirmed across all 3 layers. [src: ibd_phage_targeting]

### Cocktail feasibility and dosing

Concrete cocktails exist for 14 of 23 patients (61 %). [src: ibd_phage_targeting] A pure phage cocktail is not feasible for E1, which needs a 3-strategy hybrid. [src: ibd_phage_targeting] F. plautii bile-acid cost is the dominant E1 design constraint. [src: ibd_phage_targeting] E. coli occurs in only 35 % of the cohort. [src: ibd_phage_targeting] The two highest NB05-scored species, H. hathewayi (4.0) and F. plautii (3.3), are Pillar-4 gaps, and M. gnavus phage evidence is temperate-only. [src: ibd_phage_targeting]

Patient 6967's longitudinal E1→E3 drift was validated, with a 14× M. gnavus expansion. Five state-dependent dosing rules were established. [src: ibd_phage_targeting] The synthesis was delivered as a per-patient master table, a target decision matrix and a 4-phase clinical-translation roadmap. [src: ibd_phage_targeting] The dosing rule comes from an n=1 trajectory. [src: ibd_phage_targeting]

### Out-of-scope follow-ups

**Phage gaps.** The highest-priority extension is querying INPHARED and IMG/VR for the 3 gut-anaerobe phage-coverage gaps. [src: ibd_phage_targeting] INPHARED holds ~25K phages. [src: ibd_phage_targeting] IMG/VR holds ~3M UViGs. [src: ibd_phage_targeting] The report proposes that closing these gaps would turn the hybrid framework into a pure-phage one for at least some E1 patients. [src: ibd_phage_targeting]

**Strain and state diagnostics.**
- The report attributes the E. coli CD association to strain content in an AIEC subset. Its evidence is the NB07b within-carrier signal and the NB08a iron+genotoxin BGCs (biosynthetic gene clusters). [src: ibd_phage_targeting]
- It proposes an AIEC strain-resolution diagnostic for the 8/23 E. coli-positive UC Davis patients. [src: ibd_phage_targeting]
- The NB13 cocktail needs per-patient genotyping for pks-island, Yersiniabactin and Enterobactin genes, by PCR or an amplicon panel. [src: ibd_phage_targeting]
- The 14× M. gnavus expansion suggests the hypothesis that qPCR could replace full metagenomics in follow-up. [src: ibd_phage_targeting] Validating this needs a prospective cohort with paired qPCR and metagenomics across timepoints. [src: ibd_phage_targeting]
- The report proposes a 4–6 species qPCR ecotype panel (F. prausnitzii, P. copri, P. vulgatus, B. fragilis, M. gnavus). [src: ibd_phage_targeting]
- F. plautii bile-acid coupling cost is currently ecotype-level, not per-patient. Clinical translation therefore needs per-patient bile-acid measurements. [src: ibd_phage_targeting]

**Cohort expansion.**
- H3e remains PARTIAL in NB11. IBD anti-microbial antibody datasets outside HMP2 are not in the Lakehouse. [src: ibd_phage_targeting] A multi-cohort serology meta-analysis would address the cohort-aggregate versus site-stratified r=0.46 vs +0.31 gap. [src: ibd_phage_targeting]
- Multi-patient longitudinal cohorts would test whether ecotype drift is common. [src: ibd_phage_targeting] They would also test whether M. gnavus 5× expansion is the right qPCR threshold. [src: ibd_phage_targeting] A third question is whether cocktail Jaccard 0.60 generalizes. [src: ibd_phage_targeting]
- For external validation beyond HMP2, only HallAB_2017 currently qualifies among cMD sub-studies with CD and nonIBD that populate E3. [src: ibd_phage_targeting] The report also proposes non-Western IBD cohorts to test E2 Tier-A. [src: ibd_phage_targeting]

See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]] and [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]] for the wider context.

## Future Directions (out-of-scope clinical-translation prerequisites); Authors

This part of the report proposes clinical, alternative-therapy, methods and data follow-ups, and it names an author. [src: ibd_phage_targeting]

### Clinical-translation prerequisites

The report proposes a clinical pilot of hybrid 3-strategy cocktails in the UC Davis Crohn's disease (CD) cohort. The pilot would be organized by ecotype, patient, and state-dependent dosing. [src: ibd_phage_targeting] See [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]].

The report also proposes two non-standard routes for specific targets. One is lytic-locked phage engineering for *M. gnavus*, if natural lytic phages remain unavailable after INPHARED/IMG-VR querying. [src: ibd_phage_targeting] The other is screening for inhibitors of GAG-degrading enzymes in *H. hathewayi*, as an alternative to phage. [src: ibd_phage_targeting]

### Methods follow-ups

The report names the NB04e within-substudy × within-ecotype confound-free meta design as its most portable methodological contribution. It proposes writing this up as a standalone methods paper for the broader cMD-style multi-cohort microbiome community. [src: ibd_phage_targeting]

It also proposes a 3-modality MOFA+ on cMD_IBD pathway-aligned subjects as an NB07d follow-up. [src: ibd_phage_targeting] NB07d ran only a 2-modality canonical correlation analysis (CCA) on HMP2, because pathway data are not paired with HMP2 metabolomics. [src: ibd_phage_targeting] The cMD_IBD pathway slice in the mart is paired with cMD_IBD species at sample level. [src: ibd_phage_targeting]

### Batch effects and the polyamine gap

NB09d found that cohort batch dominates m/z-bridge clustering. [src: ibd_phage_targeting] The report suggests that ComBat/SVA/RUV harmonization before principal component analysis (PCA) and K-means could show whether metabolite-feature ecotypes become more portable across cohorts after batch correction. [src: ibd_phage_targeting] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

The NB09b m/z bridge fails on polyamines because of a low-mass HILIC-pos gap. [src: ibd_phage_targeting] The HMP2 polyamine odds ratio (OR) of 14.6 therefore stands as a single-cohort finding. [src: ibd_phage_targeting] The report proposes that external Franzosa supplementary tables with compound-name annotations would close this gap. [src: ibd_phage_targeting]

### Authors

Adam Arkin (ORCID: 0000-0002-4999-2931), of U.C. Berkeley / Lawrence Berkeley National Laboratory, is an author of the report. [src: ibd_phage_targeting]

## Caveats and Open Work

- NB09d's metabolite-ecotype failure concerns cross-cohort portability specifically. Within-cohort metabolite ecotypes might still serve single-laboratory translation. [src: ibd_phage_targeting]
- NB11 aggregates by subject, which loses longitudinal information. Mixed-effects regression might add power, but unbalanced visit counts complicate interpretation. [src: ibd_phage_targeting]
- The F. plautii bai-operon presumption is not directly tested: the CD signal is read as abundance, not strain dominance. [src: ibd_phage_targeting]
- Patient 6967 is the only multi-timepoint UC Davis CD patient with biological replicates. [src: ibd_phage_targeting] The M. gnavus qPCR proxy rests on that single patient and stays a hypothesis. [src: ibd_phage_targeting]
- The mean-per-module statistic is diluted by modules that contain 0 Tier-A hits by construction. [src: ibd_phage_targeting]
- The E3 Tier-A list is provisional and single-study. [src: ibd_phage_targeting]

## Slots Into

- [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]]: NB05 yields six actionable Tier-A targets, led by H. hathewayi (4.0). [src: ibd_phage_targeting]
- [[concepts/phage-availability-for-gut-pathobionts-and-the-gut-anaerobe-phage-gap]]: H. hathewayi and F. plautii are phage gaps. [src: ibd_phage_targeting]
- [[concepts/pathobiont-co-occurrence-modules-versus-cross-feeding-with-commensals]]: NB07c coupling was reframed as shared-environment co-occurrence. [src: ibd_phage_targeting]
- [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]]: F. plautii has the highest bile-acid coupling cost. [src: ibd_phage_targeting]
- [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]]: the E. coli iron axis is corroborated by BGC evidence. [src: ibd_phage_targeting]
