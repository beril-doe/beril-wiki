---
type: "Summary"
description: "Summary of the project The regulatory and proteomic architecture of Δ*fur*-permitted lipid A loss in *Caulobacter crescentus*."
doc_type: "short"
full_text: "sources/caulobacter_fur_lipida_loss__REPORT.md"
---
# The regulatory and proteomic architecture of Δ*fur*-permitted lipid A loss in *Caulobacter crescentus*

The regulatory and proteomic architecture of Δ*fur*-permitted lipid A loss in *Caulobacter crescentus*.

Fur derepression is supported as a major driver of the Δ*fur* signal. [src: caulobacter_fur_lipida_loss] The ChvI phase-structure half of H1 is supported. [src: caulobacter_fur_lipida_loss] The respiratory-ATP idea was demoted to a working hypothesis. [src: caulobacter_fur_lipida_loss] The outer-membrane proteome is single-replicate, so Lpt conclusions stay open. [src: caulobacter_fur_lipida_loss] Organism page: [[entities/caulobacter-crescentus]].

## Key Findings

### Fur derepression and buffering

The Δ*fur* Δ*sspB* Δ*rsaA* vs Δ*rsaA* contrast (4584-vs-4580) correlates with Leaden 2018's Δ*fur* signal at Spearman ρ = 0.315, p = 2.08e-03 over 93 Leaden Δ*fur* DEGs, with 71% sign concordance. The report reads this as Fur derepression being a major driver. [src: caulobacter_fur_lipida_loss] Yet 53 of the 93 DEGs are buffered at logFC ~0 despite -5 to -9 in Leaden. [src: caulobacter_fur_lipida_loss] The buffered set is dominated by the cbb3 / cyd / *fix*-NOPQ micro-aerobic respiratory operon (CCNA_01466-01476, *ccoNOPQ*, *cydCDA*, *fixG/H/I*). [src: caulobacter_fur_lipida_loss] See [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].

### Fitness ranking of Fur-released gene sets

RB-TnSeq (random barcode transposon sequencing) fitness data for Caulobacter (`kescience_fitnessbrowser`, orgId=`Caulo`, 198 experiments) ranked Fur-released gene sets under envelope stress. [src: caulobacter_fur_lipida_loss] The pre-registered ≥10% threshold lies below the genome background rate, so passing it says little about specific importance. [src: caulobacter_fur_lipida_loss] Path A has 17 phenotype-bearing genes of 32 (53.1%), fold = 1.60×, p = 0.016, judged marginally enriched. [src: caulobacter_fur_lipida_loss] Path A comprises Fur-released TonB-dependent transporters (TBDTs) and iron-uptake systems. [src: caulobacter_fur_lipida_loss] ChvT (CCNA_03108) has |t| = 43.7 under envelope stress. [src: caulobacter_fur_lipida_loss] The ΔsspB buffering of respiratory genes is real at transcript level, but fitness data do not independently show that set is critical for Δ*lpxc* rescue. [src: caulobacter_fur_lipida_loss] The "respiratory ATP required" framing was demoted to a working hypothesis. [src: caulobacter_fur_lipida_loss]

### ChvI regulon phase structure

The union of the Stein 2021 and Quintero-Yanes 2022 ChvI regulons has 488 ChvI-induced genes in the tested universe. [src: caulobacter_fur_lipida_loss] The engaged genes split into disjoint cohorts: 20 + 10 + 49 = 79. [src: caulobacter_fur_lipida_loss] The pre-registered phase-structure threshold (≥10 genes per cohort) passes strongly. [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].

- Unique-to-early (20 genes) includes lasso peptide cyclase CCNA_02794 (+8.6) and ApbE iron-sulfur cluster repair protein (+3.8). [src: caulobacter_fur_lipida_loss]
- Both-phase (10 genes) includes ChvI itself (CCNA_00237, +1.45 in 4584-vs-4580), read as autoregulation. [src: caulobacter_fur_lipida_loss] It also includes amelogenin/CpxP-related CCNA_03997. [src: caulobacter_fur_lipida_loss]
- Late-consequence (49 genes, induced only after lipid A loss) includes LolA-family CCNA_03820 (+2.89) and Pal-like CCNA_00784 (+2.08). [src: caulobacter_fur_lipida_loss] The report reads LolA induction as a generic outer-membrane stress response. [src: caulobacter_fur_lipida_loss]

The phase-structure half of H1 is supported. SigU as driver is only partial, pending SigU-induction RNA-seq. [src: caulobacter_fur_lipida_loss] The reframed SigU coherence check on the late cohort gave 24.5% envelope/transport/regulator enrichment, below the 50% relaxed criterion. [src: caulobacter_fur_lipida_loss]

### CtpA

CtpA (CCNA_03113) upregulation in 4599-vs-4584 was rejected at the pre-registered bar (logFC +0.58, pvalue=0.048, FDR=0.109; not detected in the outer-membrane proteome). [src: caulobacter_fur_lipida_loss] The cumulative 4599-vs-4580 contrast is significant (logFC +0.76, FDR 0.035) but conflates Δ*fur* + Δ*sspB* and Δ*lpxc* effects. [src: caulobacter_fur_lipida_loss] The report treats it as consistent with Fur regulation, not as evidence for lipid-A-loss-driven induction. [src: caulobacter_fur_lipida_loss] See [[concepts/contrast-design-and-confounding-in-testing-a-putative-lipid-a-processing-enzyme]].

### Sphingolipid and Lpt transport

Sphingolipid biosynthesis looks constitutive: *spt* is DOWN -0.64 (FDR 0.002) and *sphk* DOWN -0.40 (FDR 0.02). [src: caulobacter_fur_lipida_loss] At transcript level, MsbA-like CCNA_00307 rises +0.89 (FDR 0.01) and LptC-related CCNA_03716 +0.56 (FDR 0.005). [src: caulobacter_fur_lipida_loss] At protein level the directly measured Lpt proteins go the opposite way, for example LptE (CCNA_03866) log2(4672/4659) −0.78 and log2(4672/4580) −0.68. [src: caulobacter_fur_lipida_loss] MsbA-like protein was detected only in rescued strain 4672 (abundance 300), so its direction is uncomputable. [src: caulobacter_fur_lipida_loss] For lptC2 (CCNA_01226), transcript is -0.60 (FDR 0.034) but protein log2(4672/4659) is +1.08. [src: caulobacter_fur_lipida_loss] Because lptC2 protein was already −0.42 log2 in 4659/4580, the net change versus wild type is +0.66 log2 (≈1.58×). [src: caulobacter_fur_lipida_loss] CCNA_01217, sphingolipid machinery needed for CHIR-090 tolerance in Zik 2022, shows protein log2 = +0.77 (4672 vs 4659) or +0.74 vs wild type. [src: caulobacter_fur_lipida_loss] See [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]] and [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

### Peptidoglycan remodeling

The locked gene set has 53 loci. [src: caulobacter_fur_lipida_loss] 28 genes meet the H4 threshold (≥3 required): 25 transcript-significant in 4599-vs-4584 (FDR<0.05) plus 6 proteome hits, deduplicated. [src: caulobacter_fur_lipida_loss] Direction is mostly down (20 DOWN) with specific inductions (5 UP transcript, 3 UP protein). [src: caulobacter_fur_lipida_loss]

- Up: SdpA CCNA_01252 (+4.8 log2 protein), Pal (+2.08 transcript, +2.84 protein), PleA, PbpX and CCNA_01754. [src: caulobacter_fur_lipida_loss]
- Down: FtsI, PbpC (-1.15 protein), D,D-transpeptidase (-1.27 protein), *murD*, *mviN/murJ*, *amiC*, *ripA*, and membrane-bound transglycosylase A (-2.47 log2 protein). [src: caulobacter_fur_lipida_loss]

The report proposes, as a hypothesis, that without LPS-mediated Mg²⁺-bridged stacking the cell upregulates Pal to anchor directly. [src: caulobacter_fur_lipida_loss] See [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]].

### Comparative species analysis

PaperBLAST presence/absence compared *C. crescentus*, *A. baumannii*, *N. meningitidis* and *M. catarrhalis*. [src: caulobacter_fur_lipida_loss] ChvG-ChvI is Caulobacter-restricted, consistent with its published alphaproteobacterial restriction. [src: caulobacter_fur_lipida_loss] The report argues the other species cannot use the Δ*fur* plus anionic-sphingolipid rescue, since they lack the lipid machinery. [src: caulobacter_fur_lipida_loss] *N. meningitidis* has a capsule locus (9 hits) for the Steeghs 2001 route. [src: caulobacter_fur_lipida_loss] *A. baumannii* and *N. meningitidis* have lpxX/lpxL (8 and 3 hits) for the Gao 2008 route. [src: caulobacter_fur_lipida_loss] See [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives]].

## Key Findings: Finding 3 — ChvI engages in two phases: early cooperator + late consequence …

This part of the report tests the "dual-release switch" idea for Δ*fur* Δ*sspB* in *Caulobacter crescentus*. The Δ*fur* arm is supported by the transcript correlation with Leaden 2018 [src: caulobacter_fur_lipida_loss] and by marginal fitness enrichment of the Fur-released Path A genes. [src: caulobacter_fur_lipida_loss] The Δ*sspB* respiratory-protection arm stays a plausible hypothesis, not statistically distinguished from genome background. [src: caulobacter_fur_lipida_loss]

### Fur arm versus SspB buffering

The 4584-vs-4580 contrast (Δ*fur* Δ*sspB* Δ*rsaA* vs Δ*rsaA*) correlates with Leaden 2018's Δ*fur* signal at Spearman ρ = 0.315, p = 2.08e-03 over 93 Leaden Δ*fur* DEGs, with 71% sign concordance. The report takes this as support for Fur derepression as a major driver. [src: caulobacter_fur_lipida_loss] See [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].

However, 53 of the 93 DEGs are buffered, at logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden. [src: caulobacter_fur_lipida_loss] The buffered set is dominated by the cbb3 / cyd / *fix*-NOPQ micro-aerobic respiratory operon (CCNA_01466-01476, *ccoNOPQ*, *cydCDA*, *fixG/H/I*). [src: caulobacter_fur_lipida_loss]

### Fitness ranking of the two paths

The report used Caulobacter RB-TnSeq (random barcode transposon sequencing) fitness data (`kescience_fitnessbrowser`, orgId=`Caulo`, 198 experiments) to rank the Fur-released gene sets under envelope stress. [src: caulobacter_fur_lipida_loss] The iron-limitation arm of H2 could not be tested because the compendium has zero iron-limitation experiments, so H2 was restricted to the envelope axis. [src: caulobacter_fur_lipida_loss]

The genome-background phenotype-bearing rate (|fitness *t*| > 4 in ≥ 2 envelope-stress experiments) is 33.25% (n=3943 genes; K=1311 phenotype-bearing). [src: caulobacter_fur_lipida_loss] The pre-registered ≥10% threshold lies below this rate, so passing it says little about specific mechanistic importance. [src: caulobacter_fur_lipida_loss] See [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]].

| Path | Genes | Phenotype-bearing | Rate | Background-corrected result |
|---|---|---|---|---|
| A (concordant_strong, clean Fur signature) | 32 | 17 | 53.1% | fold = 1.60×, p = 0.016, marginally enriched [src: caulobacter_fur_lipida_loss] |
| B (SspB-buffered, cbb3/*fix*-rich) | 26 | 9 | 34.6% | fold = 1.04×, p = 0.515, indistinguishable from background [src: caulobacter_fur_lipida_loss] |

Path A comprises Fur-released TonB-dependent transporters (TBDTs) and iron-uptake systems. [src: caulobacter_fur_lipida_loss] ChvT (CCNA_03108) has |*t*| = 43.7 under envelope stress. [src: caulobacter_fur_lipida_loss] Other Fur-derepressed TBDTs (CCNA_02910, 00210, 02048, 00028) have |*t*| 9-28. [src: caulobacter_fur_lipida_loss]

The ΔsspB buffering of respiratory genes is real at the transcript level. The fitness data do not independently support this set as mechanistically critical for the Δ*lpxc* rescue. [src: caulobacter_fur_lipida_loss] The report demotes "respiratory ATP (adenosine triphosphate) required" from an established finding to a working hypothesis. [src: caulobacter_fur_lipida_loss]

### ChvI phase structure

The union of the published Stein 2021 and Quintero-Yanes 2022 ChvI regulons gives 488 ChvI-induced genes in the tested universe. [src: caulobacter_fur_lipida_loss] The report splits the engaged genes into three disjoint cohorts. [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].

- **Unique-to-early:** 20 genes induced in 4584-vs-4580 but not 4599-vs-4584. [src: caulobacter_fur_lipida_loss] They include lasso peptide cyclase CCNA_02794 (+8.6), the ApbE iron-sulfur cluster repair protein (+3.8) [src: caulobacter_fur_lipida_loss], and *imuB* SOS DNA polymerase (+1.5), which corroborates Leaden 2018's SOS activation under Δ*fur*. [src: caulobacter_fur_lipida_loss]
- **Both phases:** 10 genes induced in both contrasts, read as cooperative continuation. [src: caulobacter_fur_lipida_loss] They include ChvI itself (CCNA_00237, logFC +1.45 in 4584-vs-4580), read as autoregulation [src: caulobacter_fur_lipida_loss], SIMPL-family CCNA_02378 (+1.9 → +3.9) [src: caulobacter_fur_lipida_loss], and amelogenin/CpxP-related CCNA_03997. CpxP is the *E. coli* envelope-stress chaperone partner of CpxA. [src: caulobacter_fur_lipida_loss]
- **Late-consequence:** 49 genes induced only after lipid A loss in 4599-vs-4584. [src: caulobacter_fur_lipida_loss] They include LolA-family outer-membrane (OM) lipoprotein carrier CCNA_03820 (+2.89) [src: caulobacter_fur_lipida_loss] and Pal-like CCNA_00784 (+2.08) of the Tol-Pal envelope-integrity complex. [src: caulobacter_fur_lipida_loss] They also include a *zot*-like membrane perturber, *osrP* stress protein and multiple TBDTs. [src: caulobacter_fur_lipida_loss]

The report reads LolA induction under both Δ*spt* sphingolipid loss and Δ*lpxc* lipid A loss as a generic OM-stress response in Caulobacter. [src: caulobacter_fur_lipida_loss] Earlier drafts conflated the 20 unique-to-early and 10 both-phase genes as 30 early genes. The corrected disjoint partition is 20 + 10 + 49 = 79 engaged genes. [src: caulobacter_fur_lipida_loss] The pre-registered threshold of ≥10 genes per cohort passes strongly. [src: caulobacter_fur_lipida_loss]

A reframed SigU coherence check on the late cohort returned 24.5% envelope/transport/regulator enrichment, below the 50% relaxed criterion. [src: caulobacter_fur_lipida_loss] Caulobacter SigU is uncharacterized in the literature: a PaperBLAST scout returned zero substantive snippets for CCNA_02977. The late cohort's coherence therefore cannot be validated against a gold standard. [src: caulobacter_fur_lipida_loss] The phase-structure half of H1 is supported. SigU as a driver is only partial, pending SigU-induction RNA-seq. [src: caulobacter_fur_lipida_loss]

### CtpA, sphingolipid and Lpt checks

CtpA (CCNA_03113) upregulation in 4599-vs-4584 was rejected at the pre-registered bar. The transcript showed logFC +0.58, pvalue=0.048 and FDR (false discovery rate)=0.109, and the protein was not detected in the OM proteome. [src: caulobacter_fur_lipida_loss] The BORDERLINE criterion required both 0.05 < pvalue < 0.15 and protein detection. [src: caulobacter_fur_lipida_loss]

The cumulative 4599-vs-4580 contrast is significant (logFC +0.76, FDR 0.035). It conflates Δ*fur* + Δ*sspB* and Δ*lpxc* effects, whereas 4599-vs-4584 was designed to isolate the Δ*lpxc*-specific response. [src: caulobacter_fur_lipida_loss] The report treats it as a supplemental observation consistent with Fur regulation of CtpA. It is not evidence for lipid-A-loss-driven induction. [src: caulobacter_fur_lipida_loss] See [[concepts/contrast-design-and-confounding-in-testing-a-putative-lipid-a-processing-enzyme]].

Sphingolipid biosynthesis was constitutive rather than induced: 0/6 biosynthesis genes were UP. [src: caulobacter_fur_lipida_loss] *spt* was DOWN -0.64 (FDR 0.002) [src: caulobacter_fur_lipida_loss] and *sphk* was DOWN -0.40 (FDR 0.02). [src: caulobacter_fur_lipida_loss] At the transcript level, 0 canonical Lpt components were DOWN. [src: caulobacter_fur_lipida_loss] MsbA-like CCNA_00307 rose +0.89 (FDR 0.01) [src: caulobacter_fur_lipida_loss] and LptC-related CCNA_03716 rose +0.56 (FDR 0.005). [src: caulobacter_fur_lipida_loss] See [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]].

The OM proteome points the other way. LptD (CCNA_01760) fell with log2(4672/4659) −0.47 and log2(4672/4580) −0.62. [src: caulobacter_fur_lipida_loss] LptE (CCNA_03866) fell with log2(4672/4659) −0.78 and log2(4672/4580) −0.68. [src: caulobacter_fur_lipida_loss] MsbA-like CCNA_00307 was detected only in rescued strain 4672 (abundance 300, NaN (not a number) in the others), so its direction relative to wild type is uncomputable. [src: caulobacter_fur_lipida_loss]

The report finds the transcript upregulation of MsbA-like and LptC-related consistent with the Uchendu 2026 shared-component model. The two Lpt proteins measured directly go in the opposite direction. [src: caulobacter_fur_lipida_loss] See [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

## Key Findings: Finding 5 — Peptidoglycan remodeling: specific lytic engagement + broad …

This part of the report covers sphingolipid transport and biosynthesis proteins, peptidoglycan remodeling, and a cross-species comparison in *Caulobacter crescentus*. The protein data are single-replicate pilot observations, so they are suggestive rather than statistically established. [src: caulobacter_fur_lipida_loss]

### Sphingolipid transport and biosynthesis proteins

The sphingolipid-machinery protein increases are smaller than first stated, and they come from single-replicate data. [src: caulobacter_fur_lipida_loss] See [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]] and [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

- The report identifies CCNA_01226 (lptC2) as the Uchendu 2026 Caulobacter-specific sphingolipid inner-membrane transporter. [src: caulobacter_fur_lipida_loss] Its transcript changed -0.60 (FDR 0.034, false discovery rate), while its protein log2(4672/4659) was +1.08. [src: caulobacter_fur_lipida_loss]
- That +1.08 overstates the net change. lptC2 protein was already down -0.42 log2 in the intermediate strain (4659/4580), so the net change in the rescued strain versus wild type is +0.66 log2 (≈1.58×). [src: caulobacter_fur_lipida_loss] The 4672/4659 step is therefore partly a recovery from an earlier decrease. [src: caulobacter_fur_lipida_loss]
- CCNA_01217 is sphingolipid biosynthesis machinery required for CHIR-090 tolerance in Zik 2022. [src: caulobacter_fur_lipida_loss] Its protein log2 was +0.77 in 4672 vs 4659, or +0.74 vs wild type. [src: caulobacter_fur_lipida_loss]
- These are single-replicate observations. They are consistent with post-transcriptional stabilization of sphingolipid-transport machinery when LpxC competition for the shared LptB ATPase disappears, but they do not statistically establish it. [src: caulobacter_fur_lipida_loss]
- The single-replicate outer-membrane proteome also cannot show whether the canonical Lpt apparatus is maintained, replaced or downregulated in the Δlpxc state. Replicated proteomics are required. [src: caulobacter_fur_lipida_loss]

### Peptidoglycan remodeling

Peptidoglycan remodeling meets the pre-registered H4 threshold. It is mainly a downregulation of division and elongation machinery, with a few specific inductions. [src: caulobacter_fur_lipida_loss] See [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]].

The gene set had 53 loci and was locked before differential-expression analysis. [src: caulobacter_fur_lipida_loss] Twenty-eight genes met the H4 threshold, which required at least 3. They comprise 25 transcript-significant genes in 4599-vs-4584 (FDR<0.05) plus 6 outer-membrane-proteome |log2|>1 hits, deduplicated to 28 unique loci. [src: caulobacter_fur_lipida_loss]

The direction is predominantly downregulation (20 DOWN genes), with specific inductions (5 UP transcript and 3 UP protein). The report states that its earlier "coordinated bidirectional reorganization" framing overstated the bidirectionality. [src: caulobacter_fur_lipida_loss]

Two set members are likely regex false-positives. CCNA_00565 γ-glutamyltranspeptidase is a glutathione enzyme matched on "transpeptidase". CCNA_01833 glucosylceramidase is a ceramide enzyme matched because "ceramidase" contains "amidase". [src: caulobacter_fur_lipida_loss] They do not change the H4 verdict, which stays well above the threshold, but downstream interpretation should not rest on them. [src: caulobacter_fur_lipida_loss]

**Induced in rescued cells:**
- SdpA CCNA_01252, a soluble lytic murein transglycosylase, rose +4.8 log2 protein. [src: caulobacter_fur_lipida_loss]
- Pal CCNA_00784 rose +2.08 transcript and +2.84 protein. [src: caulobacter_fur_lipida_loss] Pal is a peptidoglycan-associated outer-membrane lipoprotein of the Tol-Pal envelope-integrity complex. It is also a top late-cohort ChvI gene, which the report calls strong cross-notebook convergence. [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].
- PleA, PbpX and CCNA_01754 were also among the specifically induced activities. [src: caulobacter_fur_lipida_loss]

**Downregulated:**
- FtsI, a cell-division penicillin-binding protein. [src: caulobacter_fur_lipida_loss]
- PbpZ (-1.08 transcript), PbpC (-1.15 protein) and a D,D-transpeptidase (-1.27 protein). [src: caulobacter_fur_lipida_loss]
- murD and mviN/murJ, the biosynthesis and flippase machinery. [src: caulobacter_fur_lipida_loss]
- The LdpD/E/F M23-family endopeptidases. [src: caulobacter_fur_lipida_loss]
- amiC amidase and ripA hydrolase. [src: caulobacter_fur_lipida_loss]
- Membrane-bound transglycosylase A, at -2.47 log2 protein. [src: caulobacter_fur_lipida_loss]

The report interprets this as the cell shutting down normal division and elongation turnover while engaging specific lytic transglycosylases and Pal-Tol anchoring factors. [src: caulobacter_fur_lipida_loss] It proposes that Pal induction compensates through direct protein anchoring for the loss of LPS-mediated (lipopolysaccharide) Mg²⁺-bridged outer-membrane–LPS–Pal stacking. This is a proposed mechanism, not a measured one. [src: caulobacter_fur_lipida_loss]

### Cross-species comparison

The report argues that *C. crescentus* depends on sphingolipid substitution because it lacks the alternative routes available to other species. [src: caulobacter_fur_lipida_loss] See [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives]].

A comparative [[entities/paperblast]] presence/absence analysis covered *C. crescentus*, *Acinetobacter baumannii*, *Neisseria meningitidis* and *Moraxella catarrhalis*. [src: caulobacter_fur_lipida_loss] The sphingolipid pathway genes spt (serine palmitoyltransferase), bcerS (bacterial ceramide synthase) and sphingosine kinase are absent from the other three species. [src: caulobacter_fur_lipida_loss] ChvG-ChvI is also Caulobacter-restricted in this comparison. This is consistent with the published alphaproteobacterial restriction of the circuit. [src: caulobacter_fur_lipida_loss] The report argues that the other three species cannot use the Caulobacter Δfur plus anionic-sphingolipid rescue because they lack the substitute lipid machinery. [src: caulobacter_fur_lipida_loss]

The published alternative routes match what each genome encodes:
- *A. baumannii* has PBP1A and Ld-transpeptidases for the Kang 2021 peptidoglycan-remodeling route. [src: caulobacter_fur_lipida_loss]
- *N. meningitidis* has a large capsule biosynthesis locus (9 PaperBLAST hits) for the Steeghs 2001 capsule-substitution route. [src: caulobacter_fur_lipida_loss]
- *A. baumannii* and *N. meningitidis* have late acyltransferases lpxX/lpxL (8 and 3 hits) for the Gao 2008 acylation-truncation route. [src: caulobacter_fur_lipida_loss]

The report asserts that Caulobacter has none of these alternatives, so sphingolipid substitution is its only viable path. [src: caulobacter_fur_lipida_loss]

## Results: Hypothesis scorecard

This part of the report scores each pre-registered hypothesis (H1–H4) plus comparative and method checks for *Caulobacter crescentus*. Most hypotheses passed or partly passed their thresholds. Several arms were rejected, demoted or marked as needing replication. [src: caulobacter_fur_lipida_loss]

### H1: ChvI phase structure
The phase-structure hypothesis passed its pre-registered bar of ≥10 genes per cohort, with unique-early=20, both=10 and late=49. [src: caulobacter_fur_lipida_loss] The sub-hypothesis that SigU drives the late cohort got only partial support. The observed 24.5% missed the ≥50% envelope/transport/regulator and Fisher p<1e-3 criterion, and the report reframed it as a literature gap. [src: caulobacter_fur_lipida_loss]

The early cohort is regulator-rich, with 6.7% regulator/TCS (two-component system) in the unique-to-early 20. [src: caulobacter_fur_lipida_loss] The late 49 have 10.2% envelope/OM and 12.2% TBDT. [src: caulobacter_fur_lipida_loss] Lipid/membrane and PG/cell wall categories are at 0% in the early cohort. [src: caulobacter_fur_lipida_loss] A Fisher exact test of this shift was not significant (p=0.243), so the regulator-to-structural shift is suggestive but not statistically discriminated. [src: caulobacter_fur_lipida_loss]

ChvI (CCNA_00237) sits in the both-phases set, with logFC +1.45 in 4584-vs-4580 and continued induction in 4599-vs-4584. The report calls this direct evidence of ChvG-ChvI autoregulation during Fur+SspB release. [src: caulobacter_fur_lipida_loss] It corrects an earlier draft that labeled ChvI as early-cohort. [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].

### H2: critical Fur regulon
Path A (concordant_strong) had 17/32 = 53% phenotype-bearing genes, fold 1.60×, p=0.016 against background. The report calls this marginal enrichment. [src: caulobacter_fur_lipida_loss] Path B (SspB-buffered) had 9/26 = 35%, fold 1.04×, p=0.515. It passed the threshold but was not enriched, so the report demoted this arm to a hypothesis. [src: caulobacter_fur_lipida_loss]

The ≥10% threshold sits below background, so it is essentially a presence test and not an enrichment test. The revised formal verdict uses hypergeometric enrichment against background. [src: caulobacter_fur_lipida_loss] Under the recalibrated test (p<0.05 and fold≥1.5×), Path A is supported, with fold=1.60× and p=0.016. [src: caulobacter_fur_lipida_loss] Path B is not supported, with fold=1.04× and p=0.515. [src: caulobacter_fur_lipida_loss] See [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]] and [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].

The Fur signature scatter shows an amplified derepression cohort that exceeds Leaden's logFC, and a buffered cohort near y=0 spanning Leaden's full -9 to -5 range. [src: caulobacter_fur_lipida_loss] HutA is the iron-derepressed TonB-dependent transporter highlighted in this analysis. [src: caulobacter_fur_lipida_loss] It is the extreme top-right point, at +10.5 vs Leaden's +2.2. [src: caulobacter_fur_lipida_loss]

### H3: sphingolipid and Lpt repurposing
CtpA upregulation in 4599-vs-4584 was rejected at the pre-registered bar. It showed logFC +0.58, pvalue=0.048 and FDR=0.109, and the protein was not detected. [src: caulobacter_fur_lipida_loss]

The constitutive sphingolipid pathway hypothesis passed strongly. 0 biosynthesis genes were up at FDR<0.05, and spt/sphk were slightly down. [src: caulobacter_fur_lipida_loss] NB00 had already rejected the initial idea that Δfur derepresses sphingolipid biosynthesis, because the pathway is not induced. [src: caulobacter_fur_lipida_loss] Canonical Lpt maintenance passed at the transcript level, with 0 components down at FDR<0.05 and MsbA-like and LptC-related transcripts up. [src: caulobacter_fur_lipida_loss] NB00 likewise found Lpt maintained or up, consistent with Uchendu 2026's shared-component model. [src: caulobacter_fur_lipida_loss]

Two post-hoc protein observations limit this. The canonical Lpt protein check was discordant with transcripts (LptD log2(4672/4659) = −0.47; LptE = −0.78) in a single replicate. [src: caulobacter_fur_lipida_loss] A pilot *lptC2* observation showed transcript -0.60 (FDR 0.034) but protein log2 +1.08 vs intermediate and +0.66 vs WT, again in a single replicate, and needs replication. [src: caulobacter_fur_lipida_loss] See [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]] and [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

### Method check on PaperBLAST
See [[entities/paperblast]] and [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]].

## Results; Interpretation

### Annotation cross-checks and false negatives

NCBI annotation independently supports the absence of the sphingolipid pathway and of ChvG-ChvI in *Acinetobacter baumannii*, *Neisseria meningitidis* and *Moraxella catarrhalis*. This adds to PaperBLAST text matching and published literature. [src: caulobacter_fur_lipida_loss] NB06b returned spt counts of 7,0,0,0 and cerR counts of 6,0,0,0 for *C. crescentus* and the three comparators. [src: caulobacter_fur_lipida_loss] ChvI is confirmed as Caulobacter-only in the species panel. [src: caulobacter_fur_lipida_loss]

NCBI annotation also produces false negatives in *C. crescentus*. MsbA has NCBI Cc=0 but is present as CCNA_00307, annotated as a phospholipid/LPS (lipopolysaccharide) ABC (ATP-binding cassette) transporter. LptA also has Cc=0 but is present without the lptA symbol in NA1000. [src: caulobacter_fur_lipida_loss] The report calls these naming-convention false negatives, because Caulobacter is annotated mainly with CCNA_* locus tags. [src: caulobacter_fur_lipida_loss] The sphingolipid and ChvI findings are unaffected, because the matching genes carry canonical symbols: Cc=7 for spt, 5 for ChvG and 6 for cerR/ChvI. [src: caulobacter_fur_lipida_loss] See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]].

### Iron uptake and respiratory buffering

The report marks "Δ*fur* derepresses TBDT and iron-uptake systems" as supported. [src: caulobacter_fur_lipida_loss] Top hits ChvT, HutA and the FrpB cluster encode outer-membrane transport machinery normally used for iron acquisition. [src: caulobacter_fur_lipida_loss] The Path A concordant_strong subset (32 genes) is marginally enriched for envelope-stress phenotype-bearing genes: 53% observed vs 33% background, fold 1.60×, hypergeometric p=0.016. [src: caulobacter_fur_lipida_loss] The report proposes that this machinery may take part in sphingolipid (CPG) trafficking through the shared Lpt apparatus. It does not demonstrate this. [src: caulobacter_fur_lipida_loss]

In the NB01 concordance analysis, transcript-level buffering is real: 53/93 Leaden Δ*fur* differentially expressed genes are blunted in the report's data, dominated by the cbb3/*fix* operon. [src: caulobacter_fur_lipida_loss] The fitness data do not back the cbb3/*fix* genes as special, however. The Path B phenotype-bearing rate (34.6%) is indistinguishable from genome background (33.25%, hypergeometric p=0.515). [src: caulobacter_fur_lipida_loss] The model that respiratory ATP (adenosine triphosphate) powers envelope remodeling is plausible but not established. [src: caulobacter_fur_lipida_loss] See [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]] and [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]].

### ChvI phase structure

The ChvI response has 20 unique-to-early, 10 both-phase and 49 late genes. [src: caulobacter_fur_lipida_loss] ChvI itself is in the both-phase set with early-contrast logFC +1.45, which the report reads as direct autoregulation. [src: caulobacter_fur_lipida_loss] The shift from a regulator-rich early response to an envelope-structural late response is suggestive but not statistically discriminated (Fisher p=0.243). [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].

### Sphingolipid biosynthesis and Lpt transport

The report concludes that sphingolipid biosynthesis is constitutive, and that rescue does not require its upregulation (marked strongly supported). [src: caulobacter_fur_lipida_loss] Zero biosynthesis genes are significantly up, and spt and sphk are mildly down. [src: caulobacter_fur_lipida_loss] The report asserts that the existing CPG pool suffices. [src: caulobacter_fur_lipida_loss]

Lpt repurposing in the Δ*lpxc* state shows transcript-protein discordance (marked MIXED). [src: caulobacter_fur_lipida_loss] At the transcript level, MsbA-like CCNA_00307 is up +0.89 (FDR 0.01) and LptC-related CCNA_03716 is up +0.56 (FDR 0.005). FDR is false discovery rate. [src: caulobacter_fur_lipida_loss] At the protein level, the two canonical Lpt proteins detected decline in the rescued strain: LptD log2(4672/4659)=−0.47 and LptE=−0.78. [src: caulobacter_fur_lipida_loss] Single-replicate proteomics cannot tell whether this reflects reduced demand for LPS-specific transport or contradicts the shared-component model. [src: caulobacter_fur_lipida_loss]

The sphingolipid-specific lptC2 (CCNA_01226) shows protein log2(4672/4659) = +1.08 despite transcript −0.60 (FDR 0.034). [src: caulobacter_fur_lipida_loss] Net change against the wild-type baseline is +0.66 log2, ≈1.58×, because lptC2 was already down −0.42 in the intermediate strain. [src: caulobacter_fur_lipida_loss] This hints at post-transcriptional stabilization. It is not statistically established and needs the replicated proteomics scheduled for summer 2026. [src: caulobacter_fur_lipida_loss] See [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]] and [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

### CtpA

CtpA's proposed role as the LpxF-equivalent processing step is not supported at the preregistered bar. Its transcript pvalue is 0.048 in 4599-vs-4584, FDR=0.109, and protein was not detected. [src: caulobacter_fur_lipida_loss] The cumulative 4599-vs-4580 contrast is significant (FDR=0.035) but confounds Δ*fur* and Δ*lpxc* effects. [src: caulobacter_fur_lipida_loss] The LpxF-substitute hypothesis remains untested. [src: caulobacter_fur_lipida_loss] See [[concepts/contrast-design-and-confounding-in-testing-a-putative-lipid-a-processing-enzyme]].

### Peptidoglycan remodeling and Tol-Pal

Shutdown dominates peptidoglycan remodeling: 20 of the 28 H4 hits are down, including FtsI, PbpZ, MurD, multiple endopeptidases and amidases. [src: caulobacter_fur_lipida_loss] Against that backdrop, SdpA (+4.8 log2 OM protein), PleA, PbpX and the Pal-Tol envelope-integrity factor Pal stand out as specific inductions. [src: caulobacter_fur_lipida_loss]

The report retracts an earlier attribution of Pal upregulation to compensation for LPS-mediated Mg²⁺-bridged OM-LPS-Pal stacking, because it had no cited support. [src: caulobacter_fur_lipida_loss] It cites Tan & Chng 2025 (Nat Commun 16:2293, PMID 40055349, where PMID is PubMed identifier). That work established retrograde phospholipid transport for outer-membrane lipid homeostasis as the primary Tol-Pal function, rather than LPS-Pal structural anchoring. [src: caulobacter_fur_lipida_loss] The report's supported interpretation is that Tol-Pal upregulation in Δ*lpxc* is consistent with increased retrograde phospholipid transport after loss of outer-leaflet LPS. [src: caulobacter_fur_lipida_loss] Direct Pal-peptidoglycan contacts may add to this, because Caulobacter Tol-Pal is essential for OM constriction at cell division. [src: caulobacter_fur_lipida_loss] See [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]].

## Interpretation: Literature Context

This part of the report separates what the data support from what stays hypothesis. The comparative claims are confirmed by NCBI annotation. The transport, respiratory-buffering and proteomic results are limited by single-replicate proteomics or by fitness data that cannot discriminate the genes from background. [src: caulobacter_fur_lipida_loss]

### Comparative arm and annotation checks

The NB06b NCBI annotation re-tests the comparative arm and confirms the headline cross-species claims. [src: caulobacter_fur_lipida_loss] ChvG-ChvI is alphaproteobacterial-restricted, confirmed by PaperBLAST and NCBI annotation (ChvG counts 5,0,0,0; ChvI counts 6,0,0,0). [src: caulobacter_fur_lipida_loss] The report notes that none of the comparators (Acinetobacter baumannii, Neisseria meningitidis, Moraxella catarrhalis) are alphaproteobacteria or Bacteroidetes. [src: caulobacter_fur_lipida_loss] Greenwich et al. 2023, a review of the conserved alphaproteobacterial ChvG-ChvI circuit, is consistent with this absence in the three comparators. [src: caulobacter_fur_lipida_loss] Olea-Ozuna et al. 2020/2024 independently confirm that Caulobacter encodes a sphingolipid biosynthesis pathway absent in the other three Gram-negatives. [src: caulobacter_fur_lipida_loss] The NB06b bcerS query failed in Caulobacter crescentus, but other markers confirm the sphingolipid-pathway finding. [src: caulobacter_fur_lipida_loss]

PaperBLAST text matching had a ~80% false-negative rate for Caulobacter's own lipid A biosynthesis genes. LpxA/C/D/B/K all returned 0 from PaperBLAST but 11-18 each from NCBI. [src: caulobacter_fur_lipida_loss] The report argues this does not threaten the cross-species finding, because the headline concerns absence in the comparators, where NCBI confirms. [src: caulobacter_fur_lipida_loss]

The report places other lipid A-loss routes beside the Caulobacter result:
- Kang et al. 2021 describes A. baumannii Δlpxc via PBP1A loss plus LdtJ/LdtK. [src: caulobacter_fur_lipida_loss] The report calls Caulobacter's engagement of SdpA/PleA and Pal-Tol peptidoglycan remodeling biologically analogous but mechanistically distinct. Both organisms reorganize peptidoglycan when LPS/LOS is removed, but with different enzyme families. [src: caulobacter_fur_lipida_loss]
- Steeghs et al. 2001 describes N. meningitidis ΔlpxA via capsule substitution. [src: caulobacter_fur_lipida_loss] This is consistent with the NB06 finding of 9 capsule-biosynthesis PaperBLAST hits in N. meningitidis versus 2-3 in the others. [src: caulobacter_fur_lipida_loss]
- Gao et al. 2008 describes M. catarrhalis late-acyltransferase truncation. [src: caulobacter_fur_lipida_loss] The NB06 analysis found the lpxX/lpxL family present in A. baumannii (8) and N. meningitidis (3) but absent in C. crescentus (0). [src: caulobacter_fur_lipida_loss]

### Fur and ΔsspB transcript buffering

Leaden et al. 2018 is a published Caulobacter Δfur RNA-seq study. The report re-analyzed its supplementary Table 2 to obtain a Fur-only differentially expressed gene (DEG) signature. [src: caulobacter_fur_lipida_loss] A Spearman ρ = 0.315 concordance with the report's 4584-vs-4580 contrast is read as confirming Fur derepression as a major signal component. [src: caulobacter_fur_lipida_loss] da Silva Neto et al. 2009 cross-validates HutA, the FrpB-like cluster and bacterioferritin in the concordant_strong set as canonical Fur targets. [src: caulobacter_fur_lipida_loss]

The ΔsspB co-deletion buffers a transcript-level program that Δfur alone would otherwise repress. 53 of 93 Leaden Δfur DEGs were blunted, dominated by the cbb3/fix-NOPQ micro-aerobic respiratory operon CCNA_01466–01476. [src: caulobacter_fur_lipida_loss] The report calls this buffering a new observation, possible only by comparing Δfur ΔsspB with Leaden's Δfur-alone data. [src: caulobacter_fur_lipida_loss] Its importance for Δlpxc rescue remains hypothesis. The Path B fitness data do not statistically discriminate these genes from the genome background under envelope stress. [src: caulobacter_fur_lipida_loss]

### Sphingolipid and Lpt transport

Zik et al. 2022, the foundational paper, was authored by the project's data provider K.R. Ryan. [src: caulobacter_fur_lipida_loss] It established that Δlpxc viability in C. crescentus requires both Δfur and the anionic sphingolipid CPG. It also found that Fur-regulated processes, not iron status per se, underlie viability. [src: caulobacter_fur_lipida_loss] Uchendu, Isom, Klein 2026 identifies the sphingolipid inner-membrane transporters CCNA_01213/01214/01226 (lptG2/F2/C2), which share the canonical LptB ATPase with LPS transport. [src: caulobacter_fur_lipida_loss]

The report claims the first regulatory and proteomic evidence that this shared-component model operates in a Δlpxc strain. [src: caulobacter_fur_lipida_loss] The canonical Lpt apparatus shows transcript upregulation with protein-level discordance. [src: caulobacter_fur_lipida_loss] At transcript level, MsbA-like CCNA_00307 is +0.89 (false discovery rate, FDR=0.01) and LptC-related CCNA_03716 is +0.56 (FDR=0.005). The report says both support Uchendu's shared-component prediction. [src: caulobacter_fur_lipida_loss] The two canonical Lpt proteins actually detected decline at protein level in the rescued strain: LptD by -0.47 log2 and LptE by -0.78 log2. [src: caulobacter_fur_lipida_loss] Replicated proteomics are needed to resolve whether the apparatus is functionally maintained, substrate-limited or downregulated at protein level. [src: caulobacter_fur_lipida_loss]

Uchendu's lptC2 protein accumulates >2-fold despite transcript downregulation. [src: caulobacter_fur_lipida_loss] For lptC2 (CCNA_01226), the transcript is -0.60 (FDR 0.034). The protein log2 is +1.08 versus intermediate (+0.66 versus WT). [src: caulobacter_fur_lipida_loss] This suggested post-transcriptional induction rests on a single replicate. It requires the proteome replication scheduled for summer 2026. [src: caulobacter_fur_lipida_loss]

The sphingolipid biosynthesis pathway is constitutive rather than induced in the Δlpxc rescue. spt and sphk are mildly down, not up, at transcript level. [src: caulobacter_fur_lipida_loss] The report infers that rescue must be flux-driven or post-transcriptional. This rules out the "Δfur derepresses sphingolipid biosynthesis" framing. [src: caulobacter_fur_lipida_loss]

### ChvI regulon and Tol-Pal

Stein et al. 2021 and Quintero-Yanes et al. 2022 supplied the published Caulobacter ChvI regulons used as reference sets for the H1 partition test. [src: caulobacter_fur_lipida_loss] The ChvI envelope-stress regulon engages in two phases with cooperative continuation. The partition is 20 unique-to-early, 10 both-phase and 49 late genes. [src: caulobacter_fur_lipida_loss] ChvI itself sits in the both-phase set with logFC +1.45 in the early contrast, which the report reads as autoregulation evidence. [src: caulobacter_fur_lipida_loss] The report says this full disjoint partition was not previously characterized. [src: caulobacter_fur_lipida_loss]

Pal CCNA_00784 is upregulated in the Δlpxc state by +2.08 at transcript level and +2.84 at protein level (NB05 and NB03 late cohort). [src: caulobacter_fur_lipida_loss] Tan & Chng 2025 establish Tol-Pal's primary function as retrograde phospholipid transport for outer-membrane lipid homeostasis, not LPS-Pal structural anchoring as an earlier draft supposed. [src: caulobacter_fur_lipida_loss] Following that paper, the report's parsimonious reading is that Pal upregulation supports increased retrograde phospholipid transport. [src: caulobacter_fur_lipida_loss] Yeh et al. 2010 establish that Caulobacter Tol-Pal is essential for outer-membrane constriction at cell division, unlike E. coli Tol-Pal. [src: caulobacter_fur_lipida_loss]

### Fitness-threshold calibration

Pre-registered fitness-phenotype thresholds in BERIL Fitness Browser projects must be calibrated against the genome-wide background rate rather than a fixed percentage. [src: caulobacter_fur_lipida_loss] A ≥10% threshold against a 33% background passes any random gene set. The report recommends revising the plan's H2 threshold to use fold-enrichment over background. [src: caulobacter_fur_lipida_loss]

## Interpretation: Limitations

This part of the report lists what limits its conclusions. CtpA fails its pre-registered bar, the outer-membrane proteome has no replicates, the fitness threshold was miscalibrated, and several comparative and mechanistic claims depend on screens, inference or outside literature. [src: caulobacter_fur_lipida_loss]

### CtpA and contrast design

CtpA was rejected at the pre-registered bar in *Caulobacter crescentus*. The 4599-vs-4584 transcript test gave pvalue=0.048 and FDR (false discovery rate)=0.109. That fails the BORDERLINE lower bound of 0.05 and the PASS bar of 0.05. [src: caulobacter_fur_lipida_loss] CtpA was also not detected in the single-replicate outer-membrane (OM) proteome. [src: caulobacter_fur_lipida_loss] Earlier drafts mislabeled this result as BORDERLINE, and the report corrects that. [src: caulobacter_fur_lipida_loss] The cumulative 4599-vs-4580 contrast (FDR=0.035) is significant. It conflates Δfur + ΔsspB and Δlpxc effects. The pre-registered 4599-vs-4584 contrast was designed to isolate the Δlpxc-specific response. [src: caulobacter_fur_lipida_loss] CtpA's hypothesized LpxF-substitute role (Zik 2022) remains untested. [src: caulobacter_fur_lipida_loss] See [[concepts/contrast-design-and-confounding-in-testing-a-putative-lipid-a-processing-enzyme]].

### Proteomics

The OM proteome has a single replicate per strain and no per-protein statistics, so only direction is interpretable. [src: caulobacter_fur_lipida_loss] The lptC2 protein induction, the Pal-Tol upregulation, the LptD/LptE protein decline and the CCNA_01217 protein increase need the replicated proteomics scheduled for summer 2026 before they can be claimed at publication rigor. [src: caulobacter_fur_lipida_loss] See [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

The Pal upregulation data show Pal up. The mechanistic reading is retrograde phospholipid transport for OM lipid homeostasis. That reading depends on Tan & Chng 2025 and remains an inference, not a direct measurement. [src: caulobacter_fur_lipida_loss] The report replaced an earlier "LPS-Mg²⁺-bridged stacking" mechanism. That mechanism was uncited and inconsistent with current Tol-Pal biology. [src: caulobacter_fur_lipida_loss] See [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]].

### Fitness thresholds and the iron arm

The Path B (SspB-buffered) fitness phenotype-bearing rate is indistinguishable from genome background. [src: caulobacter_fur_lipida_loss] The pre-registered ≥10% threshold sat below the 33.25% background rate. Adversarial review surfaced this miscalibration, and it is recorded as a learned pattern. [src: caulobacter_fur_lipida_loss] See [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]]. The "respiratory ATP (adenosine triphosphate) required" arm of the dual-release switch model is a working hypothesis, not an established finding. [src: caulobacter_fur_lipida_loss]

KBase Data Lakehouse fitness data supplied multi-condition resolution for the envelope arm of H2. [src: caulobacter_fur_lipida_loss] The Caulobacter Fitness Browser (FB) compendium has zero iron-limitation experiments out of 198. [src: caulobacter_fur_lipida_loss] H2's iron-limitation arm was therefore descoped to exploratory under the preflight rule. Testing the iron axis needs either more RB-TnSeq (random barcode transposon sequencing) under bipyridyl chelation or a cross-walk to Leaden 2018's published Δfur phenotype. [src: caulobacter_fur_lipida_loss]

The transcriptome used a single growth condition, PYE rich medium. Its Fur signal is therefore constitutive Δfur derepression, not a real iron-limitation response. [src: caulobacter_fur_lipida_loss] See [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].

### SigU attribution

*Caulobacter* SigU (CCNA_02977) is uncharacterized in PaperBLAST. [src: caulobacter_fur_lipida_loss] The H1 SigU-as-driver test was reframed from literature overlap to a functional coherence check on the late cohort. Even this relaxed criterion failed (Fisher p=0.243). [src: caulobacter_fur_lipida_loss] Targeted SigU-induction RNA-seq would resolve the cohort attribution. [src: caulobacter_fur_lipida_loss]

### Comparative annotation screens

NB06 PaperBLAST has a ~80% false-negative rate for known *Caulobacter* essential lipid A biosynthesis genes. LpxA, LpxC, LpxD and LpxK each had 0 hits in PaperBLAST, while NCBI confirms 11-18 each. [src: caulobacter_fur_lipida_loss] The post-review NB06b NCBI annotation re-test reconfirmed the headline biology. Sphingolipid-pathway genes are absent in *A. baumannii*, *N. meningitidis* and *M. catarrhalis*, and ChvG-ChvI is restricted to alphaproteobacteria. [src: caulobacter_fur_lipida_loss] NB06 should now be read as a screen, and NB06b is the authoritative comparative measurement for the headline claim. [src: caulobacter_fur_lipida_loss] *M. catarrhalis* is under-annotated in PaperBLAST (162 genes total), so its presence/absence rows are advisory only. [src: caulobacter_fur_lipida_loss] See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]] and [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]].

### Corrections to cohort counts and gene sets

Earlier drafts described an "early cohort of 30 genes" that included the 10 both-phase genes. The corrected NB03 disjoint ChvI partition is 20 unique-to-early + 10 both-phase + 49 late. The phase-structure verdict is unchanged. [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].

NB05 description-text matching falsely put CCNA_00565 (γ-glutamyltranspeptidase, a glutathione enzyme) and CCNA_01833 (glucosylceramidase, a ceramide enzyme) into the pre-curated PG-remodeling set. [src: caulobacter_fur_lipida_loss] They remain in the union of significant hits. They do not change the H4 verdict, which is well above the ≥3 threshold. [src: caulobacter_fur_lipida_loss]

## Data: Generated Data

This part of the report lists the Lakehouse tables and the data files the analysis notebooks (NB00 to NB07) used or produced. The Lakehouse tables are covered by. [src: caulobacter_fur_lipida_loss] The orientation outputs are covered by. [src: caulobacter_fur_lipida_loss] Each file group below carries its own tags.

### Lakehouse tables used

The report drew on two Lakehouse databases. From `kescience_fitnessbrowser` it used the `organism`, `experiment`, `fitbyexp_caulo` and `gene` tables for a 198-experiment Caulobacter RB-TnSeq (random barcode transposon sequencing) fitness ranking of the Fur-released gene set (NB02). [src: caulobacter_fur_lipida_loss] From `kescience_paperblast` it used the `gene`, `genepaper`, `snippet` and `curatedgene` tables for the Caulobacter SigU literature scout (NB03) and for cross-species presence/absence (NB06). [src: caulobacter_fur_lipida_loss] See [[entities/fitness-browser]] and [[entities/paperblast]].

### Source expression data (NB00, NB01)

NB00 is a Phase A orientation panel. It covers sphingolipid/Lpt CPM, ChvI enrichment, Zik suppressors, top DEGs and outer-membrane proteome strain shifts. [src: caulobacter_fur_lipida_loss]

| File | Rows | Content |
|---|---|---|
| `data/NB01_leaden_fur_de.csv` | 93 | Leaden 2018 Δfur DEGs, parsed from Frontiers Table 2.XLSX [src: caulobacter_fur_lipida_loss] |
| `data/NB01_leaden_iron_de.csv` | 491 | Leaden 2018 iron-limitation (2h DP) DEGs [src: caulobacter_fur_lipida_loss] |
| `data/NB01_fur_only_signature.csv` | 93 | Join of Leaden Δfur DEGs with the report's 4584-vs-4580 logFCs [src: caulobacter_fur_lipida_loss] |

`data/NB01_source_provenance.md` records that the PMC supplementary preflight succeeded, so no CTS re-analysis was needed. [src: caulobacter_fur_lipida_loss]

### Fitness scoring (NB02)

`data/NB02_caulo_experiments.csv` has 198 rows. It classifies the Caulobacter FB (Fitness Browser) experiments by condition: envelope=22, oxidative=4, carbon=48, iron=0. [src: caulobacter_fur_lipida_loss] Two scoring files follow. `data/NB02_pathA_concordant_strong_scoring.csv` has 32 rows of Path A fitness phenotype scoring. [src: caulobacter_fur_lipida_loss] `data/NB02_pathB_buffered_scoring.csv` has 53 rows of Path B SspB-buffered fitness phenotype scoring. [src: caulobacter_fur_lipida_loss]

The post-review recalibrated H2 verdict is in `data/NB02b_h2_hypergeometric_verdict.csv` (2 rows). It supports Path A (fold 1.60×, p=0.016). [src: caulobacter_fur_lipida_loss] It does not support Path B (1.04×, p=0.515). [src: caulobacter_fur_lipida_loss] See [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]].

### ChvI, SigU, transcript and proteome panels (NB03, NB04)

- `data/NB03_chvi_phase_cohorts.csv` (89 rows) gives the ChvI gene-by-gene phase assignment (early/both/late). [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].
- `data/NB03_phase_cohort_themes.csv` (9 rows) gives the functional theme breakdown by cohort. [src: caulobacter_fur_lipida_loss]
- `data/NB03_sigU_literature_gap.md` is the provenance for the SigU literature scout, which returned no Caulobacter snippets. [src: caulobacter_fur_lipida_loss]
- `data/NB04_sphingolipid_transcript.csv` (15 rows) is the sphingolipid biosynthesis and Uchendu transporters expression panel. [src: caulobacter_fur_lipida_loss]
- `data/NB04_lpt_transcript.csv` (6 rows) is the canonical Lpt apparatus expression panel. [src: caulobacter_fur_lipida_loss]
- `data/NB04_ctpA_transcript.csv` (1 row) is the CtpA / CCNA_03113 expression panel. [src: caulobacter_fur_lipida_loss]
- `data/NB04_protein_panel.csv` (22 rows) cross-references the outer-membrane proteome for the sphingolipid, Lpt and CtpA sets. [src: caulobacter_fur_lipida_loss]

See [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]].

### Peptidoglycan gene set (NB05)

`data/NB05_pg_gene_set.csv` (53 rows) is the pre-curated peptidoglycan-remodeling gene set, locked before DE analysis. [src: caulobacter_fur_lipida_loss] `data/NB05_pg_significant_hits.csv` (31 rows) lists the PG enzymes meeting the H4 threshold. [src: caulobacter_fur_lipida_loss] See [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]].

### Cross-species presence and the scorecard (NB06, NB07)

PaperBLAST-based presence files (NB06) are `data/NB06_comparative_presence_counts.csv` (25 rows, focal-gene PaperBLAST hit counts per species) and `data/NB06_comparative_presence_bool.csv` (25 rows, boolean presence/absence matrix). [src: caulobacter_fur_lipida_loss]

The NCBI annotation files (NB06b) are `data/NB06b_ncbi_presence_counts.csv` (28 rows, hit counts per focal family per species) and `data/NB06b_ncbi_presence_bool.csv` (28 rows, boolean presence matrix). [src: caulobacter_fur_lipida_loss] `data/NB06b_paperblast_vs_ncbi_comparison.csv` has a variable row count. It gives per-species PaperBLAST vs NCBI agreement and documents the ~80% false-negative rate of PaperBLAST text matching for C. crescentus lipid A biosynthesis genes. [src: caulobacter_fur_lipida_loss] See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]].

`data/NB07_scorecard.csv` (12 rows) is the hypothesis scorecard. It cross-references the pre-registered thresholds to outcomes. [src: caulobacter_fur_lipida_loss]

## Supporting Evidence; Future Directions; References

This part of the report gives the caveats on its post-hoc findings and the follow-up experiments it proposes. It also lists the notebooks, references and contributors. The follow-up experiments are proposals, not results. [src: caulobacter_fur_lipida_loss]

### Caveats on the proteomic findings

The report says two novel post-hoc findings need replication before publication. The first is *lptC2* protein induction with transcript-protein decoupling. [src: caulobacter_fur_lipida_loss] The second is Pal-Tol upregulation. [src: caulobacter_fur_lipida_loss] See [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]]. The data provider had already planned replication of the outer-membrane proteome for summer 2026. [src: caulobacter_fur_lipida_loss] The report proposes targeted Western blots in lptC2-tagged and Pal-tagged strains to strengthen these claims. [src: caulobacter_fur_lipida_loss]

### Genetic and lipidomic predictions

- The dual-release-switch model predicts that Δ*lpxc* should not be viable on a Δ*fur* background with *sspB* intact, because the cbb3/*fix* respiratory chain would shut down. [src: caulobacter_fur_lipida_loss]
- The same model predicts that Δ*lpxc* should not be viable on a Δ*sspB* background with *fur* intact, because Fur would repress the transport machinery needed for sphingolipid trafficking. [src: caulobacter_fur_lipida_loss] See [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].
- The report states that both predictions are testable in the existing Ryan-lab strain background. [src: caulobacter_fur_lipida_loss]
- The post-transcriptional flux model predicts that in strain 4599 (Δ*lpxc* Δ*fur* Δ*sspB*) the sphingolipid pool is maintained or increased despite no biosynthesis induction, because LpxC competition for shared substrates is gone. [src: caulobacter_fur_lipida_loss]
- The report also predicts that CtpA-mediated processing should produce a specific CPG headgroup, the LpxF substitute step. [src: caulobacter_fur_lipida_loss] Targeted lipidomics with intact lipid A precursor quantification would test both predictions. [src: caulobacter_fur_lipida_loss] See [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]].

### Tol-Pal and Pal

The revised Pal interpretation (Tan & Chng 2025) predicts increased retrograde phospholipid-transport activity by Tol-Pal in the Δ*lpxc* state, to maintain outer-membrane lipid homeostasis. [src: caulobacter_fur_lipida_loss] Pulse-chase lipidomics after exogenous fluorescent phospholipid loading would test this directly. [src: caulobacter_fur_lipida_loss] The report says Tol-Pal essentiality in *Caulobacter* (Yeh 2010) complicates depletion experiments. Conditional-depletion strains permit the test. [src: caulobacter_fur_lipida_loss] See [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]].

### SigU regulon

The report states that the published literature contains no *Caulobacter* SigU regulon, which it calls a clear gap. [src: caulobacter_fur_lipida_loss] It proposes characterizing the regulon by SigU-induction RNA-seq, using ectopic vanillate-inducible SigU expression followed by genome-wide differential expression. [src: caulobacter_fur_lipida_loss] The late ChvI cohort from NB03 would give a candidate target list to validate. [src: caulobacter_fur_lipida_loss] See [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]].

### Iron axis of H2

The *Caulobacter* RB-TnSeq (random barcode transposon sequencing) compendium has zero iron-limitation experiments. The iron-flux arm of H2 was therefore untestable here. [src: caulobacter_fur_lipida_loss] The report proposes RB-TnSeq fitness experiments under bipyridyl chelation, ferric salt supplementation and hemin. These would test whether the Fur-released subset with envelope-stress phenotypes also scores under iron limitation. [src: caulobacter_fur_lipida_loss] See [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]].

### Acinetobacter baumannii predictions

The "structural unavailability" model predicts that introducing the *Caulobacter* sphingolipid pathway into *A. baumannii*, which lacks it, should be neutral or modestly protective under colistin selection. [src: caulobacter_fur_lipida_loss] The report states that the PBP1A/Ldt route in *A. baumannii* works independently of sphingolipids. [src: caulobacter_fur_lipida_loss] A sphingolipid-engineered strain should therefore have two alternative routes to colistin resistance. The report predicts increased rates of colistin-resistant escapers. [src: caulobacter_fur_lipida_loss] See [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives]].

### Comparative-search limits

The NB06b retest using NCBI annotation confirmed the headline biological claims. Annotation-based search misses unannotated paralogs. [src: caulobacter_fur_lipida_loss] See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]]. The report retains the concern that an unannotated *spt* paralog was missed in a comparator. [src: caulobacter_fur_lipida_loss] For full rigor it proposes Pfam HMM searches for PF00155 serine palmitoyltransferase, PF03331 LpxC and PF01475 Fur, using hmmsearch or pyhmmer. [src: caulobacter_fur_lipida_loss] The proposed target proteomes are:

- GCF_000196795.1, *A. baumannii* ATCC 17978 [src: caulobacter_fur_lipida_loss]
- GCF_000008805.1, *N. meningitidis* MC58 [src: caulobacter_fur_lipida_loss]
- GCF_000092265.1, *M. catarrhalis* BBH18 [src: caulobacter_fur_lipida_loss]

The report estimates 2-4 hours via CTS. [src: caulobacter_fur_lipida_loss]

### Notebooks

The report's analysis ran through a series of notebooks:

- 00 orientation scoped the data shape, sphingolipid panel, ChvI overlap, Zik suppressors and top differentially expressed genes. [src: caulobacter_fur_lipida_loss]
- 01 assessed concordance with the Leaden 2018 Δ*fur* differentially expressed genes and identified the SspB-buffered cbb3/*fix* cohort. [src: caulobacter_fur_lipida_loss]
- 02 ranked Path A and Path B Fur-released sets by RB-TnSeq fitness and checked the H2 threshold. [src: caulobacter_fur_lipida_loss] 02b recalibrated the H2 verdict after review, using hypergeometric enrichment against background. [src: caulobacter_fur_lipida_loss]
- 03 partitioned the early and late ChvI phases and examined the SigU literature gap. [src: caulobacter_fur_lipida_loss]
- 04 examined the H3 subclaims (CtpA, constitutive sphingolipids, maintained Lpt) and the lptC2 protein finding. [src: caulobacter_fur_lipida_loss]
- 05 tested H4 peptidoglycan remodeling against a pre-curated gene set. [src: caulobacter_fur_lipida_loss]
- 06 screened cross-species presence and absence using [[entities/paperblast]]. [src: caulobacter_fur_lipida_loss] 06b retested with NCBI annotation, confirmed the biological claims and diagnosed a PaperBLAST false-negative pattern. [src: caulobacter_fur_lipida_loss]
- 07 gave a 4-panel master figure and hypothesis scorecard. [src: caulobacter_fur_lipida_loss]

### References

- Price et al. (2018), "Mutant phenotypes for thousands of bacterial genes of unknown function," *Nature* 557(7706):503, PMID (PubMed identifier) 29769718. It is the primary citation for the KBase Data Lakehouse `kescience_fitnessbrowser` source. [src: caulobacter_fur_lipida_loss]
- Price, Deutschbauer and Arkin (2021), "PaperBLAST: Text Mining Papers for Information about Homologs," *mSystems* 6(1):e00185-19, PMID 33531404. It is the primary citation for the `kescience_paperblast` source. [src: caulobacter_fur_lipida_loss]
- Arkin et al. (2018), "KBase: The United States Department of Energy Systems Biology Knowledgebase," *Nature Biotechnology* 36(7):566-569, PMID 29979655. It is the primary citation for the KBase infrastructure. [src: caulobacter_fur_lipida_loss]
- Tan and Chng (2025), "Primary role of the Tol-Pal complex in bacterial outer membrane lipid homeostasis," *Nature Communications* 16(1):2293, PMID 40055349. It is the basis for the revised Pal-upregulation interpretation, and the adversarial review identified it as a missing citation. [src: caulobacter_fur_lipida_loss]
- Yeh et al. (2010), *Journal of Bacteriology* 192(19):4847-4858, PMID 20693330. It gives *Caulobacter*-specific Tol-Pal context on essentiality and a division-associated role. [src: caulobacter_fur_lipida_loss]

### Contributors

Adam Arkin (University of California, Berkeley; ORCID 0000-0002-4999-2931) is the lead analyst. [src: caulobacter_fur_lipida_loss] Kathleen R. Ryan (University of California, Berkeley) is the data provider and scientific collaborator. Co-authorship is pending publication discussion. [src: caulobacter_fur_lipida_loss]

## Caveats and Open Work

- The iron-limitation arm of H2 could not be tested because the compendium has zero iron-limitation experiments. H2 was restricted to the envelope axis. [src: caulobacter_fur_lipida_loss]
- Path A enrichment is only marginal, and the threshold is uninformative on its own. [src: caulobacter_fur_lipida_loss]
- The single-replicate outer-membrane proteome cannot show whether the canonical Lpt apparatus is maintained, replaced or downregulated. Replicated proteomics are required. [src: caulobacter_fur_lipida_loss]
- Two peptidoglycan-set members are likely regex false positives: CCNA_00565 γ-glutamyltranspeptidase and CCNA_01833 glucosylceramidase. [src: caulobacter_fur_lipida_loss]
- SigU-induction RNA-seq is needed to test SigU as driver. [src: caulobacter_fur_lipida_loss]
- Earlier drafts overstated bidirectional peptidoglycan reorganisation. [src: caulobacter_fur_lipida_loss]

## Slots Into

- [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]]: 53 of 93 Leaden Δ*fur* DEGs are buffered, mostly respiratory operon genes. [src: caulobacter_fur_lipida_loss]
- [[concepts/chvg-chvi-envelope-stress-regulon-phase-structure]]: the 20 + 10 + 49 cohort partition passes the pre-registered threshold. [src: caulobacter_fur_lipida_loss]
- [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]]: Lpt transcripts rise while LptE protein falls. [src: caulobacter_fur_lipida_loss]
- [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]]: the lptC2 transcript is down while its protein is up. [src: caulobacter_fur_lipida_loss]
- [[concepts/peptidoglycan-remodeling-and-tol-pal-engagement-after-outer-membrane-lps-loss]]: Pal is up at transcript and protein. [src: caulobacter_fur_lipida_loss]
- [[concepts/calibration-of-fitness-phenotype-thresholds-against-genome-background]]: the ≥10% threshold sits below background. [src: caulobacter_fur_lipida_loss]
- [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives]]: other species have capsule or acyltransferase routes. [src: caulobacter_fur_lipida_loss]
- [[concepts/contrast-design-and-confounding-in-testing-a-putative-lipid-a-processing-enzyme]]: the cumulative CtpA contrast conflates Fur and lipid A effects. [src: caulobacter_fur_lipida_loss]
