---
type: Summary
description: Multi-layer analysis of Fur, ChvI, Lpt, and peptidoglycan responses enabling
  lipid A loss
doc_type: short
full_text: ../sources/caulobacter_fur_lipida_loss__REPORT.md
title: Regulatory and proteomic architecture of Δfur-permitted lipid A loss in *Caulobacter
  crescentus*
sources:
- id: caulobacter_fur_lipida_loss
  resource: ../sources/caulobacter_fur_lipida_loss__REPORT.md
  title: caulobacter fur lipida loss
---
# Regulatory and proteomic architecture of Δfur-permitted lipid A loss in *Caulobacter crescentus*

## Overview

This report analyzes how Δ*fur* Δ*sspB* permits Δ*lpxc* viability in *Caulobacter crescentus* by integrating transcriptomics, single-replicate outer-membrane proteomics, Caulobacter RB-TnSeq fitness data, published ChvI regulons, and comparative species annotation. The evidence supports Fur derepression of transport and iron-uptake systems, a two-phase ChvI response, constitutive rather than induced sphingolipid biosynthesis, transcript–protein discordance in the Lpt apparatus, and peptidoglycan remodeling; the mechanistic importance of the SspB-buffered respiratory program and the CtpA hypothesis remains unresolved or unsupported at the preregistered thresholds. [^caulobacter_fur_lipida_loss]

## Key findings

### Fur derepression and the ΔsspB-buffered respiratory program

The 4584-vs-4580 contrast (Δ*fur* Δ*sspB* Δ*rsaA* vs Δ*rsaA*) correlated with Leaden 2018's Δ*fur* signal across 93 DEGs with Spearman ρ = 0.315, p = 2.08e-03, and 71% sign concordance. Of those 93 DEGs, 53 were buffered in the present data, with logFC approximately 0 despite Leaden values of -5 to -9; the buffered set was dominated by the cbb3 / cyd / *fix*-NOPQ micro-aerobic respiratory operon, including CCNA_01466-01476, *ccoNOPQ*, *cydCDA*, and *fixG/H/I*. Fur derepression is therefore statistically supported, whereas the mechanistic importance of the Δ*sspB*-buffered respiratory program for Δ*lpxc* rescue is only a hypothesis. [^caulobacter_fur_lipida_loss]

Caulobacter RB-TnSeq data from `kescience_fitnessbrowser` covered 198 experiments, including 22 envelope-stress experiments but zero iron-limitation experiments. The genome-wide envelope-stress background contained 1311 phenotype-bearing genes among 3943 genes, or 33.25%. Path A, the 32-gene concordant-strong Fur signature, contained 17 phenotype-bearing genes, or 53.1%, corresponding to 1.60× enrichment with hypergeometric p = 0.016. Path B, the 26-gene SspB-buffered set used for the enrichment test, contained 9 phenotype-bearing genes, or 34.6%, corresponding to 1.04× enrichment with p = 0.515; it was indistinguishable from background. [^caulobacter_fur_lipida_loss]

ChvT (CCNA_03108) had envelope-stress |*t*| = 43.7, while other Fur-derepressed TBDTs included CCNA_02910, CCNA_00210, CCNA_02048, and CCNA_00028 with |*t*| values of 9-28. The pre-registered ≥10% phenotype-bearing threshold was below the 33.25% genome background and was therefore not informative without background correction. [^caulobacter_fur_lipida_loss]

### ChvI phase structure

Published ChvI-induced regulons from Stein 2021 and Quintero-Yanes 2022 contained 488 genes in the tested universe. They partitioned into 20 unique-to-early genes, 10 genes induced in both phases, and 49 late-consequence genes, for a disjoint total of 79 ChvI-induced genes. The unique-to-early group included the lasso peptide cyclase CCNA_02794 at +8.6, the ApbE iron-sulfur cluster repair protein at +3.8, and *imuB* at +1.5. [^caulobacter_fur_lipida_loss]

The both-phases group included ChvI itself, CCNA_00237, with logFC +1.45 in 4584-vs-4580, supporting autoregulation, as well as SIMPL-family CCNA_02378, which changed from +1.9 to +3.9, and amelogenin/CpxP-related CCNA_03997. The late-consequence group included LolA-family CCNA_03820 at +2.89, Pal-like CCNA_00784 at +2.08, a *zot*-like membrane perturber, *osrP*, and multiple TBDTs. [^caulobacter_fur_lipida_loss]

The phase-structure threshold of at least 10 genes per cohort passed. The late cohort's envelope/transport/regulator enrichment was 24.5%, below the relaxed 50% criterion, and the late-versus-early Fisher test was p = 0.243. Caulobacter SigU, CCNA_02977, is uncharacterized in the published literature; a PaperBLAST scout returned zero substantive snippets. Thus the phase structure is supported, while SigU as the driver of the late cohort remains only partially supported. [^caulobacter_fur_lipida_loss]

### Sphingolipid biosynthesis, CtpA, and Lpt components

The sphingolipid biosynthesis pathway was constitutive rather than induced: 0/6 biosynthesis genes were UP, *spt* was DOWN by -0.64 with FDR 0.002, and *sphk* was DOWN by -0.40 with FDR 0.02. CtpA/CCNA_03113 showed logFC +0.58 with pvalue = 0.048 and FDR = 0.109 in 4599-vs-4584, was not detected in the outer-membrane proteome, and therefore failed both the PASS and BORDERLINE preregistered criteria. Its verdict was REJECTED at the preregistered bar. [^caulobacter_fur_lipida_loss]

At the transcript level, no canonical Lpt component was DOWN; the MsbA-like CCNA_00307 was UP by +0.89 with FDR 0.01, and LptC-related CCNA_03716 was UP by +0.56 with FDR 0.005. At the protein level, the detected canonical components moved in the opposite direction: LptD changed by log2(4672/4659) = -0.47 and by log2(4672/4580) = -0.62, while LptE changed by -0.78 and -0.68, respectively. CCNA_00307 was detected only in the rescued strain, at abundance 300 in 4672 and NaN in the other strains, so its direction relative to wild-type baseline was uncomputable. [^caulobacter_fur_lipida_loss]

The sphingolipid transporter CCNA_01226 (*lptC2*) showed transcript -0.60 with FDR 0.034 but protein log2(4672/4659) = +1.08. Because its protein level was already DOWN by -0.42 log2 in 4659/4580, its net protein change versus wild-type baseline was +0.66 log2, reported as approximately 1.58×. CCNA_01217 protein changed by +0.77 in 4672 versus 4659, or +0.74 versus wild type. These single-replicate observations are consistent with post-transcriptional stabilization of sphingolipid-transport machinery but do not establish it statistically. [^caulobacter_fur_lipida_loss]

### Peptidoglycan remodeling

The preregistered peptidoglycan-remodeling set contained 53 loci, of which 28 unique loci met the H4 threshold: 25 were transcript-significant in 4599-vs-4584 at FDR<0.05 and 6 had OM-proteome |log2|>1. The response was predominantly downregulatory, with 20 DOWN loci and specific inductions comprising 5 UP transcript hits plus 3 UP protein hits. [^caulobacter_fur_lipida_loss]

Specific induced activities included SdpA/CCNA_01252 at +4.8 log2 protein, Pal/CCNA_00784 at +2.08 transcript and +2.84 protein, PleA, PbpX, and CCNA_01754. Basal division and elongation machinery was broadly reduced, including FtsI, PbpZ at -1.08 transcript, PbpC at -1.15 protein, a D,D-transpeptidase at -1.27 protein, *murD*, *mviN/murJ*, multiple LdpD/E/F M23-family endopeptidases, *amiC*, *ripA*, and membrane-bound transglycosylase A at -2.47 log2 protein. [^caulobacter_fur_lipida_loss]

Pal was induced at both transcript and protein levels and was also among the late-cohort ChvI genes. The report reframes its interpretation using the primary role of Tol-Pal in retrograde phospholipid transport and outer-membrane lipid homeostasis: Pal-Tol upregulation is consistent with increased lipid-remodeling demand after loss of outer-leaflet lipid A, while direct Pal–peptidoglycan contacts and the Caulobacter division-associated role remain additional context rather than direct measurements in this project. [^caulobacter_fur_lipida_loss]

### Comparative species analysis

NCBI annotation confirmed that *spt* and *cerR* were Caulobacter-unique across *C. crescentus*, *A. baumannii*, *N. meningitidis*, and *M. catarrhalis*, with patterns 1000. ChvG and ChvI also showed pattern 1000, supporting Caulobacter restriction of the ChvG-ChvI circuit among the tested species. The comparator species therefore lack the Caulobacter sphingolipid substitute pathway and ChvG-ChvI regulatory circuit. [^caulobacter_fur_lipida_loss]

The original PaperBLAST screen produced false negatives for known Caulobacter lipid A genes: LpxA returned 0 PaperBLAST hits versus 11 NCBI hits, LpxC 0 versus 15, LpxD 0 versus 15, LpxB 1 versus 18, and LpxK 0 versus 18. The report characterizes this as an approximately 80% false-negative rate for the tested Caulobacter lipid A genes, while retaining the cross-species absence claims because those were independently supported by NCBI annotation and literature. [^caulobacter_fur_lipida_loss]

The alternative lipid A-loss routes identified in the comparison were species-specific: *A. baumannii* has PBP1A and Ld-transpeptidases, *N. meningitidis* has 9 capsule-biosynthesis PaperBLAST hits, and *A. baumannii* and *N. meningitidis* have late acyltransferase *lpxX/lpxL* hits numbering 8 and 3, respectively. The report states that Caulobacter lacks these alternatives and instead uses its sphingolipid substitution route. [^caulobacter_fur_lipida_loss]

## Caveats and unresolved questions

The Δ*sspB*-buffered cbb3/*fix* respiratory program is a clean transcript-level observation, but its fitness phenotype-bearing rate was 34.6%, versus 33.25% for the genome background, with hypergeometric p = 0.515 and fold = 1.04×. Consequently, the claim that respiratory ATP is required for envelope remodeling remains a working hypothesis, not an established mechanism. [^caulobacter_fur_lipida_loss]

The fitness compendium contained zero iron-limitation experiments among 198 Caulobacter experiments, so the iron-limitation arm of H2 was descoped to envelope-only analysis. Testing that arm requires additional RB-TnSeq experiments under bipyridyl chelation, ferric supplementation, and hemin, or a cross-walk to published Δ*fur* phenotypes. [^caulobacter_fur_lipida_loss]

CtpA was rejected at the preregistered bar because pvalue = 0.048 failed the BORDERLINE lower bound of 0.05, FDR = 0.109 failed the PASS criterion, and protein was not detected. The cumulative 4599-vs-4580 FDR = 0.035 result cannot isolate the Δ*lpxc*-specific response because it conflates Δ*fur*, Δ*sspB*, and Δ*lpxc* effects. [^caulobacter_fur_lipida_loss]

The OM proteome had a single replicate per strain, so no per-protein statistics were available. The *lptC2* protein induction, Pal-Tol upregulation, LptD/LptE decline, and CCNA_01217 increase require replicated proteomics before publication-level claims can be made. [^caulobacter_fur_lipida_loss]

The transcriptome used a single PYE rich-medium growth condition, and the observed Fur signal represents constitutive Δ*fur* derepression rather than a direct iron-limitation response. Caulobacter SigU lacks a characterized published regulon, and the late ChvI cohort did not pass the relaxed coherence criterion. [^caulobacter_fur_lipida_loss]

The comparative PaperBLAST analysis was vulnerable to naming-convention false negatives, and *M. catarrhalis* was under-annotated in PaperBLAST with 162 genes total. NCBI annotation strengthened the headline absence claims, but a deeper Pfam HMM search against named RefSeq proteomes is still needed to detect unannotated paralogs. [^caulobacter_fur_lipida_loss]

The peptidoglycan gene set included two likely regex false positives: CCNA_00565, a γ-glutamyltranspeptidase matched through “transpeptidase,” and CCNA_01833, a glucosylceramidase matched because “ceramidase” contains “amidase.” Their inclusion did not change the H4 verdict, which remained well above the ≥3 threshold. [^caulobacter_fur_lipida_loss]

The report identifies replicated OM proteomics, targeted *lptC2* and Pal assays, SigU-induction RNA-seq, genetic tests of the dual-release model, lipidomics, iron-axis fitness experiments, Tol-Pal phospholipid-transport assays, cross-species engineering, and sequence-based homology searches as specific resolving work. [^caulobacter_fur_lipida_loss]

## Slots Into

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the background-calibrated RB-TnSeq analysis distinguishes marginal Path A enrichment from the unsupported Path B respiratory hypothesis. [^caulobacter_fur_lipida_loss]
- [gene-essentiality](../concepts/gene-essentiality.md) — the report tests which Fur-released and peptidoglycan-remodeling gene sets show condition-specific fitness phenotypes and relates them to Δ*lpxc* viability. [^caulobacter_fur_lipida_loss]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — transcript, single-replicate OM-proteome, fitness, regulon, and comparative-annotation evidence reveal Lpt transcript–protein discordance and convergent Pal-Tol remodeling. [^caulobacter_fur_lipida_loss]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — the analysis bridges `kescience_fitnessbrowser`, `kescience_paperblast`, published datasets, and project-generated transcript/proteome measurements to test the rescue mechanism. [^caulobacter_fur_lipida_loss]

[^caulobacter_fur_lipida_loss]: [caulobacter fur lipida loss](../sources/caulobacter_fur_lipida_loss__REPORT.md)
