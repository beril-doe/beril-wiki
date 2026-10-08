---
type: "Summary"
description: "Summary of the counter_ion_effects project, which tested whether chloride from metal salts confounds genome-wide metal-fitness measurements and found substantial metal\u2013NaCl shared-stress overlap but no chloride dose effect, with Metal Fitness Atlas core enrichment robust to correction."
doc_type: "short"
full_text: "sources/counter_ion_effects__REPORT.md"
---
# Counter Ion Effects on Metal Fitness Measurements

## Overview

This analysis tested whether counter ions, especially chloride delivered by metal salts, confound genome-wide metal-fitness measurements. Across 71 NaCl experiments, 10,821 metal-important gene records, 86 organism × metal pairs, 14 metals, and 19 organisms, it found substantial metal–NaCl overlap but no evidence that chloride dose is the primary driver. The overlap reflects shared cellular stress biology, while Metal Fitness Atlas core-genome enrichment remains robust after removing shared-stress genes. [src: counter_ion_effects]

## Key Findings

### Shared NaCl and Metal Fitness Signals

Figure — heatmap of metal–NaCl gene overlap by organism and metal: ![Heatmap of metal-NaCl gene overlap by organism and metal](figures/nacl_metal_overlap_heatmap.png) [src: counter_ion_effects]

Across 19 organisms and 14 metals (86 organism × metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) were also NaCl-important. This pooled gene-record percentage is different from the per-metal organism-level mean overlaps reported below. Overlap occurred for every metal, ranging from 9.2% for molybdenum to 57.6% for manganese. The report takes this to mean that a large fraction of the metal-fitness signal reflects general cellular vulnerability shared between metal stress and osmotic/ionic stress. *Synechococcus elongatus* (SynE) was an outlier: 88.6% of its genes were shared-stress (565/638), from 12 NaCl dose-response experiments spanning 0.5–250 mM. Other organisms had 1–6 NaCl experiments. Excluding SynE lowered the overlap from 39.8% to 36.7% (3,739/10,183), so the result was not driven by that outlier. The `n_sick >= 1` threshold is much easier to meet with 12 experiments. The next-highest organisms (Korea 58.6%, Phaeo 56.4%, Pedo557 53.0%) have typical NaCl experiment counts. [src: counter_ion_effects]

The analysis identified 71 NaCl experiments across 25 organisms and 4,648 NaCl-important genes (mean 186 per organism). The overlap analysis covered 19 of the 25 organisms with NaCl data, 86 organism × metal pairs, and 14 metals. Of the 10,821 tested metal-important gene records, 6,517 (60.2%) were classified as metal-specific (important for metals but not NaCl) and 4,304 (39.8%) as shared-stress. The report's novel-contribution summary describes the 39.8% overlap as across 25 organisms, but the main overlap result specifies 19 organisms. Both denominators are recorded here without reconciliation. [src: counter_ion_effects]

Figure — shared-stress versus metal-specific gene classification by metal: ![Per-metal gene classification: shared-stress vs metal-specific](figures/gene_classification_by_metal.png) [src: counter_ion_effects]

Across all organisms, 6,517 of 10,821 metal-important gene records (60.2%) were classified as metal-specific. Shared-stress genes were important for a mean of 4.1 metals per gene, compared with 2.5 metals per metal-specific gene. In *Desulfovibrio vulgaris* Hildenborough (DvH), 495 unique metal-important genes comprised 73 shared-stress genes (14.7%) and 422 metal-specific genes (85.3%); 90.5% of metal-specific genes had SEED annotations compared with 78.1% of shared-stress genes. The report reads this as suggesting that the metal-specific set includes well-characterized metal homeostasis functions (Ni/Fe-hydrogenase, nitrogenase regulators, metal transporters), while shared-stress genes include more uncharacterized general stress proteins. This functional interpretation is descriptive and was not formally tested. [src: counter_ion_effects]

### Counter Ions Are Not the Primary Driver

Figure — per-metal NaCl overlap colored by counter-ion type: ![Per-metal overlap colored by counter ion type](figures/metal_nacl_overlap_by_counter_ion.png) [src: counter_ion_effects]

Chloride concentration did not explain the overlap, and the predicted dose-dependent relationship between Cl⁻ concentration and NaCl overlap was rejected. Zinc sulfate, which delivers 0 mM chloride, had 44.6% NaCl overlap, exceeding cobalt at 41.3% despite cobalt delivering up to 500 mM chloride, copper at 41.0%, and nickel at 39.3%. Chloride-delivered metals had a mean overlap of 41.6%, compared with 37.8% for non-chloride metals. The per-metal table lists mean maximum Cl⁻ concentrations of 0 mM for zinc (12 organisms), 28 mM for cobalt (18 organisms), 2 mM for copper (16 organisms), and 2 mM for nickel (17 organisms). The report attributes the overlap to shared stress biology (cell envelope damage, ion homeostasis disruption, and general stress response) rather than to chloride counter ions. That explanation is the report's interpretation and was not directly tested. [src: counter_ion_effects]

Figure — effective Cl⁻ concentration versus NaCl overlap scatter, the H1b test: ![Cl⁻ concentration vs NaCl overlap scatter](figures/cl_concentration_vs_overlap.png) [src: counter_ion_effects]

The per-metal table reports organism-level mean overlap values, which must not be conflated with the pooled 4,304/10,821 gene-record overlap: manganese 57.6% (1 organism), cadmium 50.5% (1), aluminum 46.1% (12), zinc 44.6% (12), cobalt 41.3% (18), copper 41.0% (16), nickel 39.3% (17), uranium 37.2% (2), iron 33.3% (1), chromium 29.2% (2), selenium 26.8% (1), mercury 23.4% (1), tungsten 10.8% (1), and molybdenum 9.2% (1). Zinc, delivered as sulfate with zero chloride, ranked 4th in NaCl overlap, above 10 of 14 metals. Uranium, delivered as acetate with zero chloride, ranked 8th. The report's statement that the ranking follows toxicity mechanism rather than counter-ion identity is an interpretation, not a direct test. [src: counter_ion_effects]

The report interprets the shared signal as biology involving cell-envelope integrity, DNA repair, and ion homeostasis, rather than counter-ion contamination. NaCl is not a pure chloride control because it also supplies sodium and osmotic stress. [src: counter_ion_effects]

As literature context, the report cites Danilova et al. (2020), who reported 2.5-fold differences between CuSO₄ and CuCl₂ toxicity at 0.5 M, a range where osmotic effects dominate. Random barcode transposon sequencing (RB-TnSeq; pooled mutant fitness assays) typically uses lower concentrations of 0.05–2 mM, and the report infers that counter-ion effects would be proportionally smaller there. This is an extrapolation, not a measurement made in this project. [src: counter_ion_effects]

### DvH Metal–NaCl Correlation Hierarchy

Figure — DvH Pearson correlations between the NaCl fitness profile and each metal profile: ![DvH fitness profile correlations with NaCl](figures/dvh_nacl_metal_correlation.png) [src: counter_ion_effects]

In DvH, which had 13 metals and 6 NaCl experiments, whole-genome Pearson correlations with NaCl were zinc r=0.715, manganese r=0.545, copper r=0.532, cobalt r=0.498, mercury r=0.478, nickel r=0.446, aluminum r=0.420, molybdenum r=0.396, uranium r=0.350, selenium r=0.342, chromium r=0.318, tungsten r=0.298, and iron r=0.086. The hierarchy did not follow chloride concentration: zinc sulfate had zero chloride but ranked first. The report proposes instead that the hierarchy follows toxicity mechanism. In its account, metals that broadly displace essential cofactors (Zn, Mn, Cu, Co) share more genes with NaCl stress than metals that target specific pathways (Mo and W, through molybdopterin enzymes; Fe, through iron–sulfur clusters). This mechanistic reading is an interpretation of the correlation ranking, not a direct test. [src: counter_ion_effects]

The report interprets high NaCl correlation as consistent with broad toxicity through essential-cofactor displacement or disruption of multiple cellular systems, especially for zinc, manganese, copper, cobalt, mercury, and nickel. Lower correlation for molybdenum, uranium, selenium, chromium, tungsten, and iron is interpreted as consistent with more pathway-specific effects; iron was described as affecting specific iron-dependent enzymes rather than causing general cellular damage. These mechanistic interpretations are extrapolations from the fitness-profile hierarchy rather than direct biochemical tests. [src: counter_ion_effects]

### Metal Fitness Atlas Robustness

Figure — two-panel comparison of original versus corrected core fraction and delta per metal: ![Original vs corrected core enrichment per metal](figures/atlas_original_vs_corrected.png) [src: counter_ion_effects]

After removing shared-stress genes and restricting analysis to metal-specific genes, core-genome enrichment was preserved for 12 of 14 metals. Seven metals showed stronger corrected enrichment: molybdenum, with delta changing from +0.132 to +0.145; tungsten, +0.129 to +0.134; mercury, +0.116 to +0.133; selenium, +0.115 to +0.131; nickel, +0.088 to +0.098; chromium, +0.056 to +0.069; and uranium, +0.031 to +0.040. The report's narrative counts these 7 of 14 metals (Mo, W, Hg, Se, Ni, Cr, U) as strengthened. Its corrected-conservation table, however, also shows an increased delta for iron, although that rests on n=9 genes from one organism. The narrative also reports modest decreases for aluminum (+0.099 → +0.068) and zinc (+0.145 → +0.115). It says only cadmium reverses (delta -0.008 → -0.108) and notes that, with only 92 original genes from 1 organism, this has very low statistical power. That reversal wording conflicts with the corrected-conservation table, in which cadmium's delta stays negative while iron's changes sign (detailed below). [src: counter_ion_effects]

Aluminum weakened from +0.099 to +0.068, zinc from +0.145 to +0.115, and copper from +0.090 to +0.084; manganese remained +0.182 and cobalt remained +0.076. Cadmium's core fraction changed from 0.522 to 0.422 against a baseline of 0.530, with delta changing from -0.008 to -0.108. The table labels cadmium "reversed", but its delta does not change sign. Iron's core fraction changed from 0.778 to 1.000 against a baseline of 0.818, with delta changing from -0.040 to +0.182, which is a sign reversal. This conflicts with the report's prose, which states that only cadmium reverses (delta -0.008 → -0.108) and attributes the low statistical power to its 92 original genes from 1 organism. The narrative also counts only 7 of 14 metals as showing stronger corrected enrichment, even though the table shows an increased delta for iron. Cadmium had n=92 genes and iron had n=9 genes, each from one organism, and the report calls their corrected deltas statistically unreliable; manganese also had only n=30 genes from one organism, although its 100% core fraction is a ceiling result. [src: counter_ion_effects]

The original Metal Fitness Atlas found that metal-important genes are 87.4% core, with OR=2.08 (odds ratio). In principle, the shared-stress component could have inflated this result, because osmotic-stress genes are core cellular machinery. The prediction that core enrichment would weaken after correction was rejected, so the conclusion was not attributable to shared NaCl-stress genes. The report states that researchers using the atlas do not need to filter out NaCl-responsive genes for the atlas’s core-enrichment conclusion. [src: counter_ion_effects]

### Within-Metal Salt Comparison

Figure — psRCH2 CuCl₂ versus CuSO₄ fitness profiles: ![psRCH2 CuCl₂ vs CuSO₄ fitness profiles](figures/psrch2_copper_comparison.png) [src: counter_ion_effects]

psRCH2 was the only organism with copper tested as both CuCl₂ (anaerobic, 3 replicates) and CuSO₄ (aerobic, 3 replicates). The cross-salt correlation was r=0.439, compared with within-replicate correlations of r=0.720 for CuCl₂ and r=0.859 for CuSO₄. This comparison is severely confounded by aerobic versus anaerobic growth: CuCl₂ was tested anaerobically and CuSO₄ aerobically, so hundreds of genes may differ independently of copper. [src: counter_ion_effects]

CuSO₄ had a higher correlation with NaCl than CuCl₂, r=0.450 versus r=0.212, despite supplying no chloride. This result argues against chloride as the primary confound, but the aerobic/anaerobic confounding prevents the comparison from isolating counter-ion effects. [src: counter_ion_effects]

### Hypothesis Outcomes

H1a, predicting more than 20% overlap, was supported by the 39.8% overlap. H1b, predicting a dose-dependent chloride relationship, was rejected because zinc sulfate with 0 mM chloride exceeded most chloride-delivered metals. H1c, predicting weakened atlas core enrichment after correction, was rejected because enrichment was robust and strengthened for several metals. H1d, predicting chloride-versus-oxyanion functional-profile differences, was dropped and not tested. The null hypothesis that counter ions are negligible was partially supported: counter ions appeared negligible specifically, while shared-stress biology was substantial but did not undermine atlas conclusions. [src: counter_ion_effects]

## Data Sources

Fitness scores and experiment metadata came from the `genefitness` and `experiment` tables of the `kescience_fitnessbrowser` collection, via cached matrices ([[entities/kescience-fitnessbrowser]]). Core/accessory classification came from `kbase_ke_pangenome` `gene_cluster` data via the Fitness Browser–pangenome link ([[entities/kbase-ke-pangenome]]). The generated `data/nacl_experiments.csv` contains 71 NaCl/RbCl experiments across 25 organisms. [src: counter_ion_effects]

The report lists these other generated outputs: `data/nacl_fitness_summary.csv`, with 94,908 per-gene NaCl fitness summaries (mean, min, n_sick); `data/nacl_important_genes.csv`, with 4,648 genes with significant NaCl fitness defects; `data/effective_chloride_concentrations.csv`, with 559 rows of counter ion and effective Cl⁻ per metal experiment; `data/metal_nacl_overlap.csv`, with 86 per-organism × metal overlap statistics (Fisher, Jaccard); `data/dvh_nacl_metal_correlations.csv`, with 13 DvH whole-genome Pearson r values between NaCl and each metal; `data/gene_classification_shared_vs_metal.csv`, with 10,821 cross-organism shared-stress versus metal-specific classifications; `data/dvh_gene_classification.csv`, with 495 DvH gene classifications that include SEED annotation information (this does not mean all 495 are annotated); and `data/corrected_metal_conservation.csv`, with 14 per-metal original-versus-corrected core-fraction comparisons. The notebook `01_nacl_identification.ipynb` identifies the 71 NaCl experiments, extracts fitness profiles, and computes effective Cl⁻. [src: counter_ion_effects]

## Caveats

The 39.8% overlap depends on the NaCl-importance threshold, defined using fit < -1 or n_sick ≥ 1; stricter or more permissive thresholds could reduce or increase the overlap. The *S. elongatus* estimate is especially sensitive because it had 12 NaCl experiments spanning 0.5–250 mM, whereas other organisms had 1–6 NaCl experiments. [src: counter_ion_effects]

NaCl cannot isolate chloride because it delivers both Na⁺ and Cl⁻ and produces osmotic effects. A KCl or choline chloride control would more specifically test chloride effects, although some Fitness Browser organisms have choline chloride experiments at different concentrations. The report proposes comparing metal–choline chloride (ChCl) overlap with metal–NaCl overlap to separate chloride from osmotic confounding. This proposal rests on the report's premise that ChCl provides Cl⁻ without Na⁺ or osmotic effects. That premise is not tested here, and the comparison is not reported as completed. [src: counter_ion_effects]

Approximately 14.3% of protein-coding genes, classified as putative essential genes, lacked transposon insertions and were absent from both NaCl and metal-fitness data. These genes are 82% core, and their exclusion affects the original and corrected conservation analyses equally. [src: counter_ion_effects]

Manganese, cadmium, selenium, mercury, iron, molybdenum, and tungsten were each tested in only 1 organism, DvH, so their overlap statistics lack cross-organism replication. The psRCH2 CuCl₂–CuSO₄ comparison is additionally limited by aerobic/anaerobic confounding. [src: counter_ion_effects]

The shared-stress versus metal-specific classification did not include formal functional-enrichment tests; the SEED annotation comparison was descriptive. The proposed mechanistic categories therefore remain hypotheses requiring direct functional testing. [src: counter_ion_effects]

The report proposes formal COG (Clusters of Orthologous Groups functional categories), KEGG, and PFAM enrichment tests; comparison with choline chloride; module-level analysis using independent component analysis (ICA); refinement of condition-specific metal-gene analysis; and matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ RB-TnSeq experiments under identical conditions. It also proposes DvH NaCl dose-response experiments at 0.1, 1, 10, 100, and 500 mM to match effective chloride doses. [src: counter_ion_effects]

The proposed COG, KEGG, and PFAM tests would formally check whether shared-stress genes are enriched for envelope/transport functions and metal-specific genes for metal-binding/efflux; that pattern is not established here. The proposed module-level analysis would apply the metal–NaCl overlap to modules from the fitness_modules project rather than to individual genes. Whether metal-responsive modules overlap NaCl-responsive modules therefore remains open. [src: counter_ion_effects]

The report attributes to metal_fitness_atlas the finding that condition-specific genes, important only for metals and not other stresses, are less core. It proposes that this project's shared-stress versus metal-specific classification could refine that analysis. [src: counter_ion_effects]

The report names RB-TnSeq with matched metal chloride and metal sulfate concentrations in a single organism under identical growth conditions as the most impactful follow-up, because it would eliminate the aerobic/anaerobic confound that limits the psRCH2 comparison. It proposes three pairs. The first is CuCl₂ 0.5 mM versus CuSO₄ 0.5 mM in MR-1 or DvH, because copper is the most-tested metal. The second is ZnCl₂ 0.2 mM versus ZnSO₄ 0.2 mM in MR-1: zinc was already tested as sulfate, and adding the chloride form would directly test the null. The third is CoCl₂ 0.1 mM versus CoSO₄ 0.1 mM in DvH: cobalt has the highest Cl⁻ load in current data, and the sulfate form would confirm mechanism. These are proposed conditions, not reported results. [src: counter_ion_effects]

## Slots Into

- [[concepts/condition-specific-fitness]] — the 39.8% overlap and DvH correlation hierarchy show that metal fitness profiles combine shared-stress and metal-specific condition responses. [src: counter_ion_effects]
- [[concepts/gene-essentiality]] — corrected core-enrichment analysis shows that the Metal Fitness Atlas signal persists after removing shared-stress genes, while putative essential genes remain excluded from both datasets. [src: counter_ion_effects]
- [[concepts/cofitness-network-architecture]] — the DvH whole-genome metal–NaCl correlations and proposed module-level decomposition provide cross-condition fitness-profile evidence for shared versus specific stress architecture. [src: counter_ion_effects]
- [[concepts/shared-stress-versus-stressor-specific-fitness]] — the pooled 39.8% overlap, the 60.2% metal-specific share, the rejected chloride dose-dependence, and the NaCl-is-not-pure-chloride caveat split metal fitness into shared and stressor-specific components. [src: counter_ion_effects]
- [[concepts/metal-cross-resistance]] — shared-stress genes were important for a mean of 4.1 metals versus 2.5 for metal-specific genes, while manganese, cadmium, selenium, mercury, iron, molybdenum, and tungsten were each tested only in DvH. [src: counter_ion_effects]
- [[concepts/pangenome-conservation-fitness-decoupling]] — atlas core enrichment survived shared-stress correction, with an unresolved cadmium/iron sign discrepancy between the report's table and prose. [src: counter_ion_effects]
- [[concepts/laboratory-fitness-versus-natural-selection]] — the Metal Fitness Atlas 87.4% core (OR=2.08) result is shown not to be an artifact of shared NaCl-stress genes. [src: counter_ion_effects]
- [[concepts/fitness-condition-coverage-prioritization-bias]] — SynE's 12 NaCl experiments made the `n_sick >= 1` rule easier to satisfy, inflating its shared-stress fraction. [src: counter_ion_effects]
- [[concepts/transposon-callability-bias]] — approximately 14.3% of protein-coding genes, putative essentials that are 82% core, were absent from both fitness datasets. [src: counter_ion_effects]
- [[concepts/pangenome-integration]] — core/accessory labels came from the Fitness Browser–pangenome link. [src: counter_ion_effects]
