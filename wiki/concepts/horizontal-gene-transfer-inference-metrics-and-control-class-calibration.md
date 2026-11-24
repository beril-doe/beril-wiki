---
type: "Concept"
description: "Which metric detects acquisition and gene flow on a species tree at genomic scale (Sankoff parsimony, dispersion nulls, DTL reconciliation), and how positive and negative control classes were built and failed."
sources: ["summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md"]
---
# Horizontal gene transfer inference metrics and control-class calibration

This page covers which metric detects acquisition and gene flow on a species tree at genomic scale (Sankoff parsimony, dispersion nulls, DTL reconciliation), and how positive and negative control classes were built and failed. Tree-aware [[entities/sankoff-parsimony|Sankoff parsimony]] recovers the expected control-class direction, but its effect size at UniRef50 is small. [src: gene_function_ecological_agora] At KO (KEGG ortholog) resolution, with clean housekeeping controls only, the effect sizes pass the pre-registered gate. [src: gene_function_ecological_agora] The method has not been benchmarked against modern DTL (duplication transfer loss) reconciliation. [src: gene_function_ecological_agora] The evidence comes from one project, gene_function_ecological_agora, on the GTDB-r214 tree. [src: discoveries] See also [[summaries/gene_function_ecological_agora__REPORT]] and [[summaries/discoveries]].

## Sankoff parsimony with acquisition-depth bins

M22 Sankoff parsimony attributed 17M gain events on the GTDB-r214 species tree to 5 acquisition-depth bins: recent, older_recent, mid, older and ancient. [src: discoveries] The report describes this as a tree-aware acquisition-depth signal at full GTDB scale, on an 18,989-leaf tree. [src: gene_function_ecological_agora] M15 made Sankoff parsimony, a lightweight tree-aware metric, mandatory. [src: gene_function_ecological_agora] M16 made it the primary Phase 2 atlas metric and relegated parent-rank dispersion to diagnostics. [src: gene_function_ecological_agora]

The report argues that Sankoff parsimony is tractable at this scale, whereas exact DTL methods are not. [src: gene_function_ecological_agora] It cites Mirkin et al. 2003 and Csurös 2010 as precedent for parsimony as an HGT proxy where full DTL reconciliation (AleRax, ALE, Notung) is computationally infeasible. [src: gene_function_ecological_agora] Williams et al. qualify that framing: principled DTL methods are scaling, but not yet to the full 18,989-leaf tree. [src: gene_function_ecological_agora]

M22 extracts gain locations from the parsimony reconstruction and assigns each to the rank-LCA of its descendant leaves. The report calls this the same level of phylogenetic-origin claim as Alm 2006 made via lineage-specific-expansion analysis. [src: gene_function_ecological_agora]

### Recent-to-ancient ratio as a function-class signature

The recent-to-ancient gain ratio separates the control classes. [[entities/crispr-cas|CRISPR-Cas]] had a ratio of 24.5×, read as an HGT-active signature. [src: discoveries, gene_function_ecological_agora] Strict housekeeping functions (RNA polymerase core, tRNA synthetase, ribosomal) had a ratio of ~1×, read as vertical inheritance. [src: discoveries, gene_function_ecological_agora] The report treats the ratio per function class as a substantive measure of vertical versus horizontal dominance, separate from any pre-registered hypothesis test. [src: discoveries, gene_function_ecological_agora]

### Full GTDB KO atlas

At full atlas scale the M18 amplification gate from the NB09c panel subset (2.69M rows) reproduces: 6/6 strict pairs pass Cohen's d ≥ 0.3 with a 95% bootstrap CI lower bound > 0. [src: gene_function_ecological_agora] The effect sizes match NB09c almost exactly. The report attributes the small drift from NB09c's best d = 3.558 (n_pos = 6, n_neg = 20) to sample composition, and says the substrate-hierarchy claim is reconfirmed. [src: gene_function_ecological_agora]

Gain-depth distributions per class, as percent of gains in recent (genus), older_recent, mid, older and ancient bins, then total gains and recent/ancient ratio:

- pos_crispr_cas: 58.7, 27.6, 7.0, 4.3, 2.4; 20,898 gains [src: gene_function_ecological_agora]; ratio 58.7 / 2.4 = 24.5, highly recent-skewed and consistent with documented HGT activity. [src: gene_function_ecological_agora]
- pos_tcs_hk: 45.1, 32.9, 10.6, 7.0, 4.4; 518,106 gains [src: gene_function_ecological_agora]; ratio 10.3. [src: gene_function_ecological_agora]
- pos_betalac: 44.2, 32.7, 10.7, 7.5, 4.9; 139,000 gains [src: gene_function_ecological_agora]; ratio 9.0. [src: gene_function_ecological_agora]
- neg_ribosomal_strict: 38.9, 33.3, 12.4, 9.1, 6.3; 79,168 gains [src: gene_function_ecological_agora]; ratio 6.2, mixed, as expected for the contaminated strict-K range. [src: gene_function_ecological_agora]
- neg_rnap_core_strict: 38.5, 34.2, 12.2, 9.0, 6.0; 4,086 gains [src: gene_function_ecological_agora]; ratio 6.4. [src: gene_function_ecological_agora]
- neg_trna_synth_strict: 24.7, 31.8, 17.5, 15.2, 10.7; 15,060 gains [src: gene_function_ecological_agora]; ratio 2.3, most ancient-skewed and consistent with universal vertical inheritance. [src: gene_function_ecological_agora]

The report states that HGT-active classes have a recent/ancient ratio 4–10× higher than clean housekeeping. [src: gene_function_ecological_agora] It interprets this as extending low paralogy under dosage constraint to low recent acquisition under dosage constraint, both manifestations of the same selective regime. [src: gene_function_ecological_agora]

The ratios of CRISPR-Cas 24.5× and tRNA-synth 2.3× align qualitatively with the HGT literature (Smillie 2011, Forsberg 2012, Metcalf 2014, Phillips 2012). They are not yet quantitatively cross-validated against an independent dataset. [src: gene_function_ecological_agora] The report also notes that P4-D4 returns an informative atlas-scale null, read as M22 and pangenome openness measuring distinct evolutionary phenomena. [src: gene_function_ecological_agora]

### What M22 does not attribute

M22 gives recipients and depth, not donor-recipient flow. It reports the rank-LCA of leaves under each gain event, which is where the gain landed, not who donated it. [src: gene_function_ecological_agora] Deep-rank donor inference is constrained by composition-signal degradation for events older than ~10–100 Myr and by the infeasibility of per-family DTL reconciliation at GTDB scale. [src: gene_function_ecological_agora]

### Leaf consistency as an independent check

[[entities/leaf-consistency|Leaf consistency]] (LC) is the fraction of species in a recipient clade that carry the KO. It was measured for 17.07M M22 gain events at 97.8% coverage. [src: gene_function_ecological_agora] Mean LC is 0.34 for recent gains and 0.20 for ancient gains. [src: gene_function_ecological_agora] The per-bin values fall monotonically: recent 0.34, older_recent 0.30, mid 0.26, older 0.23, ancient 0.20. [src: gene_function_ecological_agora] The report reads this as validating M22. Its explanation is that recent gains land in clades where the KO is propagated, while ancient gains have diversified with subsequent losses. [src: gene_function_ecological_agora]

Because LC was not used in any pre-registered hypothesis test, the report calls it its cleanest independent validation of the housekeeping versus HGT-active framework. [src: gene_function_ecological_agora] In the signature plane:

- Strict housekeeping sits in the low-recent, high-LC vertical quadrant: RNAP core 0.97, tRNA-synth 0.94, ribosomal 0.92. [src: gene_function_ecological_agora]
- CRISPR-Cas (LC 0.29), AMR (0.11) and TCS HK (0.13) sit in the high-recent, low-LC patchy quadrant. [src: gene_function_ecological_agora] TCS HK is two-component system histidine kinase.
- Loose housekeeping classes fall in the middle, because their definitions include paralogs and weakly housekeeping members. [src: gene_function_ecological_agora]
- The ancient-patchy quadrant is sparse and holds only paralog-inflated loose-housekeeping classes. [src: gene_function_ecological_agora]

## The order-rank anomaly and the metric diagnostic

NB08c used Sankoff parsimony on the GTDB-r214 tree to ask whether the order-rank anomaly was a metric artifact or a methodology failure. [src: gene_function_ecological_agora] The report concludes it was a parent-rank-dispersion artifact: the framework was not broken, the metric was wrong. [src: gene_function_ecological_agora] Parent-rank dispersion permutation null was replaced by Sankoff parsimony with recipient-rank gain attribution. [src: gene_function_ecological_agora]

- Median order-rank K is 1 for both positive HGT and negative housekeeping UniRefs, so UniRefs are clade-restricted regardless of class. The distributions differ at p < 10⁻¹⁹ but share a median, so K bias does not explain the anomaly. [src: gene_function_ecological_agora]
- Within Pseudomonadota, dispersion is lower for positive controls (median 0.25) than for negative housekeeping (median 0.33). [src: gene_function_ecological_agora] The report says this metric is biased by class coverage: housekeeping occurs in every family, while HGT-active classes are clade-specific within the phylum. [src: gene_function_ecological_agora] It names per-phylum Sankoff parsimony as the right within-phylum analog. [src: gene_function_ecological_agora]
- Sankoff score per present leaf puts TCS HK, β-lactamase and CAZymes (carbohydrate-active enzymes) above ribosomal, tRNA-synth and RNAP housekeeping. [src: gene_function_ecological_agora] The direction is recovered at p = 2.1×10⁻⁵. [src: gene_function_ecological_agora]

Effect size limits this result. Diagnostic panel C reports Cohen's d = 0.15 [src: gene_function_ecological_agora], and the report gives the UniRef50 Sankoff effect as d = 0.146. [src: gene_function_ecological_agora] The report states that the UniRef50 d = 0.15 is well below the pre-registered d ≥ 0.3 threshold for atlas-grade discrimination. [src: gene_function_ecological_agora] The earlier "+0.6 to +1.2 σ less clumped than housekeeping" framing used parent-rank z-units rather than Cohen's d and overstated the effect. [src: gene_function_ecological_agora] M18 therefore set a hard gate. The Phase 2 KO atlas must show d ≥ 0.3 on Sankoff parsimony for at least one positive HGT control against negative housekeeping, relative to the UniRef50 baseline of d = 0.15. [src: gene_function_ecological_agora]

## KO-level M18 test (NB09c)

M18 passed on the cleanest housekeeping (tRNA-synth and RNAP core). Cohen's d rose from 0.146 (UniRef50, NB08c, positives against all housekeeping) to 0.665–3.558 for the best KO pairs, a 4–25× amplification depending on positive class. [src: gene_function_ecological_agora] The report concludes that the substrate-hierarchy claim survives at KO resolution and the full Phase 2 atlas can proceed. [src: gene_function_ecological_agora] NB09c found 6/9 strict pairs passing d ≥ 0.3 with 95% CI lower bound > 0. [src: gene_function_ecological_agora] The three failures were all against ribosomal controls. Per pair (n_pos, n_neg, Cohen's d, 95% CI, one-sided MW p as labelled in the report):

- pos_crispr_cas vs neg_trna_synth_strict: 6, 20, +3.558, [+2.93, +21.53], 4×10⁻⁶; pass. [src: gene_function_ecological_agora]
- pos_crispr_cas vs neg_rnap_core_strict: 6, 3, +1.905, [+1.47, +11.88], 0.012; pass. [src: gene_function_ecological_agora]
- pos_betalac vs neg_trna_synth_strict: 110, 20, +0.812, [+0.72, +0.95], <10⁻¹⁵; pass. [src: gene_function_ecological_agora]
- pos_betalac vs neg_rnap_core_strict: 110, 3, +0.753, [+0.67, +0.86], 0.0017; pass. [src: gene_function_ecological_agora]
- pos_tcs_hk vs neg_trna_synth_strict: 310, 20, +0.690, [+0.60, +0.88], <10⁻¹⁵; pass. [src: gene_function_ecological_agora]
- pos_tcs_hk vs neg_rnap_core_strict: 310, 3, +0.665, [+0.58, +0.85], 0.0015; pass. [src: gene_function_ecological_agora]
- pos_betalac vs neg_ribosomal_strict: 110, 83, −0.836, [−1.17, −0.52], 0.87; fail. [src: gene_function_ecological_agora]
- pos_crispr_cas vs neg_ribosomal_strict: 6, 83, −0.919, [−1.15, −0.66], 0.71; fail. [src: gene_function_ecological_agora]
- pos_tcs_hk vs neg_ribosomal_strict: 310, 83, −1.705, [−2.15, −1.33], 0.96; fail. [src: gene_function_ecological_agora]

## Control classes and how they failed

### Positive controls: AMR

The pos_amr class (AMR is antimicrobial resistance) had an anomalously low median Sankoff/n_present of 12.0, attributed to Pseudomonadota detection bias. [src: gene_function_ecological_agora] The report traces this to [[entities/bakta-amr|bakta_amr]] being sourced from AMRFinderPlus's Pseudomonadota-heavy reference set. [src: gene_function_ecological_agora] The set is also dominated by clade-specific resistance variants. The report calls the AMR negative result consistent with that narrowness, not a methodology failure. [src: gene_function_ecological_agora] M17 excluded bakta_amr from the Phase 2 positive controls. It kept β-lactamase, CRISPR-Cas and TCS HK, and used natural_expansion as a paralog-signal sanity check. [src: gene_function_ecological_agora] The stated reason is that 49% of AMR UniRefs are >50% Pseudomonadota in NB08c Diagnostic D. [src: gene_function_ecological_agora] AMR still appears as info_amr (54.8% recent, 4.1% ancient) for transparency, not as load-bearing evidence. [src: gene_function_ecological_agora]

### Negative controls: housekeeping

The pre-registered v2 criterion required the producer mean to be within ±1σ of zero for ribosomal, tRNA-synthetase and RNAP core classes. [src: gene_function_ecological_agora] The Phase 1A pilot found all three at producer z ≈ −0.15 with CIs (confidence intervals) entirely below zero. The criterion was then revised post-hoc to "CI upper bound ≤ 0.5". [src: gene_function_ecological_agora] Across ranks the producer z was −0.15 to −0.24 σ, with 95% CIs entirely below zero. [src: gene_function_ecological_agora] At full GTDB scale these classes sit ~12 % below cohort with z ≈ −0.15. [src: gene_function_ecological_agora]

The report calls this biologically correct. Dosage-constrained genes carry fewer paralogs than typical genes at matched prevalence. [src: gene_function_ecological_agora] That prior was anticipated in plan v2 design but not encoded in the criterion. [src: gene_function_ecological_agora] The report states that the "near zero" criterion was wrong and the correct one is "≤ 0 with CI not strongly positive". [src: gene_function_ecological_agora] Its lesson is to encode known biological priors explicitly in pre-registered criteria, not the absolute-null value. [src: gene_function_ecological_agora]

### Ribosomal controls

The NB09b description-matched neg_ribosomal class was dominated by clade-restricted accessory proteins and false matches (RimM, RbfA, processing and silencing factors, mitochondrial ribosomal protein false matches), caught by the rule `LOWER(ipr_desc) LIKE '%ribosomal protein%'`. [src: gene_function_ecological_agora] NB09c then defined strict ribosomal housekeeping as K02860..K02899 ∪ K02950..K02998, with 89 KOs total and 83 in the panel. [src: gene_function_ecological_agora] This strict class also failed all three M18 pairs against the positive controls. [src: gene_function_ecological_agora] Its median Sankoff/n_present was 18.83 (q25=0.11, q75=23.13, bimodal), with median n_present_leaves 13. [src: gene_function_ecological_agora] About half of the 83 KOs are universal and half clade-restricted, while tRNA synthetase and RNAP core are clean universal housekeeping. [src: gene_function_ecological_agora] The report attributes the failure to the range being a pre-2000 KEGG-numbering approximation that mixes universal ribosomal proteins with accessory variants. [src: gene_function_ecological_agora]

The general lesson is that description-based class detection, mostly clean at UniRef50, does not survive KO aggregation, because the 50% majority-vote threshold admits accessory class members. [src: gene_function_ecological_agora]

### Resulting commitments (M21, M23)

M21 (plan v2.8) commits all d-based metrics and M18-style validation in Phase 2/3 to tRNA-synth (K01866..K01890) plus RNAP core (K03040, K03043, K03046) as canonical clean housekeeping. Ribosomal controls are reported as informational only. [src: gene_function_ecological_agora]

RNAP core has only n_neg = 3. The pos_crispr_cas versus neg_rnap_core_strict pair (n_pos=6, n_neg=3) had a bootstrap 95% CI of [1.55, 11.58], wide on the upper bound. The CI lower bound is stably > 0 across all 6 passing pairs, so the criterion is robust, but the small-n imbalance is a defensibility concern. [src: gene_function_ecological_agora] M23 (plan v2.10) therefore pre-registers n_neg ≥ 20 per group for primary hypothesis tests. [src: gene_function_ecological_agora] Under it, RNAP-core and ribosomal comparisons become informational only, and tRNA-synth-strict (n=20) is the load-bearing housekeeping control. [src: gene_function_ecological_agora]

### Circular validation

The natural_expansion producer-null validation is circular. The class is selected for paralog count ≥ 3 and tested against a null designed to detect paralog expansion. [src: gene_function_ecological_agora] The report keeps it only as a metric-direction sanity check. The holdout becomes the load-bearing producer-null validation. [src: gene_function_ecological_agora]

## Limits relative to DTL reconciliation

The report positions its parsimony approximation against the DTL literature: Williams 2024, López Sánchez 2026, Liu 2021, Kundu 2018 and Bansal 2012. [src: gene_function_ecological_agora] It admits its Sankoff approach has no principled benchmarking against modern DTL reconciliation. [src: gene_function_ecological_agora] It also lacks gene-tree rooting-uncertainty quantification. [src: gene_function_ecological_agora] The report calls the methodology a generation behind the state of the art. [src: gene_function_ecological_agora] Cross-validation against Liu 2021 DTLOR or Bansal 2012/2013 SPR-based DTL on a representative GTDB subset is out of scope. It would need external tools and per-family gene-tree estimation. [src: gene_function_ecological_agora]

López Sánchez et al. 2026 (DOI 10.1177/15578666261426009, PMID 41955011) present a directly parallel Sankoff-Rousseau algorithm for HGT inference using KEGG functions on bacterial species. [src: gene_function_ecological_agora] The report calls M22 conceptually similar and proposes benchmarking the two on a shared substrate. [src: gene_function_ecological_agora]

## Tensions

- The recent-to-ancient ratio contrasts CRISPR-Cas at 24.5× with strict housekeeping at ~1×. [src: discoveries] Yet the UniRef50 Sankoff effect size is small, with d = 0.15 against the pre-registered d ≥ 0.3 threshold. [src: gene_function_ecological_agora] At KO level with clean controls, d reaches 0.665–3.558. [src: gene_function_ecological_agora]
- The report gives strict housekeeping at ~1× [src: gene_function_ecological_agora], while its atlas table gives ratios of 2.3 to 6.4 for the strict housekeeping classes. [src: gene_function_ecological_agora]
- The report argues DTL does not scale to GTDB. [src: gene_function_ecological_agora] Williams et al. say principled DTL methods are scaling, though not yet to 18,989 leaves. [src: gene_function_ecological_agora]

## Open Directions

- Benchmark M22 gain attribution against a DTL reconciliation (Liu 2021 DTLOR or Bansal SPR-based) on a representative GTDB subset. This would close the missing-benchmark gap.
- Run M22 and López Sánchez 2026's Sankoff-Rousseau algorithm on a shared substrate and compare gain-depth calls.
- Quantify gene-tree rooting uncertainty on a sample of families and propagate it to depth-bin assignments.
- Test the M18 gate (d ≥ 0.3) at KO level with per-phylum Sankoff, using the holdout as the producer-null validation.
- Rebuild the AMR positive control from a set that is not Pseudomonadota-biased, and rerun the Sankoff comparison.
- Rebuild a ribosomal control from universal r-proteins only, using current KEGG assignments rather than the K-number range, and test whether it meets n_neg ≥ 20.
- Cross-validate the CRISPR-Cas and tRNA-synth recent-to-ancient ratios against an independent HGT dataset.
