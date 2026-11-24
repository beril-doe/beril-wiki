---
type: "Summary"
description: "Summary of the project Counter Ion Effects on Metal Fitness Measurements."
doc_type: "short"
full_text: "sources/counter_ion_effects__REPORT.md"
---
# Counter Ion Effects on Metal Fitness Measurements

This page summarises the project Counter Ion Effects on Metal Fitness Measurements. About 40% of metal-important gene records were also important under sodium chloride (NaCl) stress. [src: counter_ion_effects] The overlap did not scale with chloride delivered by metal salts. [src: counter_ion_effects] Metal Fitness Atlas core-genome enrichment survived removal of shared-stress genes for 12 of 14 metals. [src: counter_ion_effects] The report reads the overlap as genuine shared biology rather than counter-ion contamination, and concludes that Atlas users need not filter NaCl-responsive genes. [src: counter_ion_effects] The overlap analysis included 19 of the 25 organisms with NaCl data. [src: counter_ion_effects] Several per-metal values rest on one organism, as noted below. [src: counter_ion_effects] The report also proposes follow-up work, chiefly matched chloride/sulfate metal-salt experiments, listed under Caveats and Open Work. [src: counter_ion_effects]

## Key Findings

### Hypothesis outcomes

The report tested four hypotheses plus a null. H1a (>20% of metal genes also NaCl-important) was supported by 39.8% overlap. [src: counter_ion_effects] H1b (overlap scales with Cl⁻ concentration) was rejected, because ZnSO₄ with 0 Cl⁻ exceeded most chloride metals. [src: counter_ion_effects] H1c (core enrichment weakens after correction) was rejected, since enrichment was robust and strengthened for essential metals. [src: counter_ion_effects] H1d (chloride versus oxyanion functional profiles differ) was dropped and not tested. [src: counter_ion_effects] H0 (counter ions negligible) was partially supported: counter ions specifically are negligible, and shared stress biology is real but does not undermine the Atlas conclusions. [src: counter_ion_effects]

### Metal–NaCl overlap is large and general

Across 19 organisms and 14 metals (86 organism × metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) were also important under NaCl stress. [src: counter_ion_effects] The analysis identified 71 NaCl experiments across 25 organisms and 4,648 NaCl-important genes (mean 186 per organism). [src: counter_ion_effects] Only 19 of the 25 organisms with NaCl data entered the overlap analysis. [src: counter_ion_effects] The report reads the overlap as general cellular vulnerability shared between metal and osmotic/ionic stress. [src: counter_ion_effects] It describes this as the first systematic quantification of metal-salt overlap in genome-wide fitness data. [src: counter_ion_effects] Across all organisms, 6,517 of 10,821 records (60.2%) were metal-specific, meaning important for metals but not NaCl. [src: counter_ion_effects]

*Synechococcus elongatus* (SynE) was an outlier at 88.6% (565/638 genes). It had 12 NaCl dose-response experiments spanning 0.5–250 mM, against 1–6 for other organisms. [src: counter_ion_effects] The n_sick >= 1 threshold is easier to meet with 12 experiments. [src: counter_ion_effects] Excluding SynE lowered the overall overlap from 39.8% to 36.7% (3,739/10,183), so the report concludes SynE does not drive the finding. [src: counter_ion_effects] The next-highest organisms were Korea 58.6%, Phaeo 56.4% and Pedo557 53.0%, with typical NaCl experiment counts. [src: counter_ion_effects]

### Chloride counter ions do not explain the overlap

The overlap did not scale with chloride delivered by the metal salt. [src: counter_ion_effects] Metal–NaCl gene overlap was uncorrelated with effective chloride concentration across 86 organism × metal pairs. [src: counter_ion_effects] Effective chloride was computed for 559 metal experiments. [src: counter_ion_effects] Zinc sulfate (0 mM Cl⁻) showed 44.6% overlap. This was higher than cobalt (41.3%, up to 500 mM Cl⁻), copper (41.0%) and nickel (39.3%). [src: counter_ion_effects] Zinc supplied as sulfate with zero chloride ranked 4th in NaCl overlap, above 10 of 14 metals. [src: counter_ion_effects] Uranium as acetate with zero chloride ranked 8th. [src: counter_ion_effects] Cobalt chloride delivers up to 500 mM Cl⁻ yet has lower overlap (41.3%) than zinc sulfate. [src: counter_ion_effects] Chloride metals averaged 41.6% and non-chloride metals 37.8%, a small difference. [src: counter_ion_effects] The report attributes the overlap to shared cell-envelope damage, ion-homeostasis disruption and general stress response. [src: counter_ion_effects] It claims a definitive rejection of counter-ion confounding using zinc sulfate as a natural control. [src: counter_ion_effects] Zinc sulfate also had the highest DvH NaCl correlation (r=0.715) alongside the 4th-highest overlap (44.6%), which the report says would be unexpected if chloride were the confound. [src: counter_ion_effects]

The report hypothesizes that the shared genes are core functions vulnerable to both metal and osmotic stress: cell envelope integrity (divalent cation imbalance and osmolarity changes) [src: counter_ion_effects], DNA (deoxyribonucleic acid) repair (metal-induced oxidative damage overlapping NaCl-induced stress) [src: counter_ion_effects], and ion homeostasis (metal influx competing with Na⁺/K⁺/Cl⁻ transporters). [src: counter_ion_effects] It also calls the ~40% overlap consistent with the general stress response paradigm, in which RpoS-dependent genes respond to heavy metals, osmolarity and oxidative damage (Battesti et al. 2011). [src: counter_ion_effects] It cites Danilova et al. (2020) for 2.5-fold CuSO₄–CuCl₂ toxicity differences at 0.5 M, where osmotic effects dominate. [src: counter_ion_effects] It infers that counter-ion effects would be proportionally smaller at typical RB-TnSeq (random barcode transposon sequencing) concentrations of 0.05–2 mM. [src: counter_ion_effects]

Per-metal mean overlap, with salt type, number of organisms and the reported mean maximum Cl⁻ (mM). The report states the cobalt "up to 500 mM" figure above and the 28 mM mean maximum below separately, and does not relate them. [src: counter_ion_effects]

| Metal | Salt | Overlap | Organisms | Mean max Cl⁻ |
|---|---|---|---|---|
| Manganese | chloride | 57.6% | 1 | 200 [src: counter_ion_effects] |
| Cadmium | chloride | 50.5% | 1 | not reported [src: counter_ion_effects] |
| Aluminum | chloride | 46.1% | 12 | 8 [src: counter_ion_effects] |
| Zinc | sulfate | 44.6% | 12 | 0 [src: counter_ion_effects] |
| Cobalt | chloride | 41.3% | 18 | 28 [src: counter_ion_effects] |
| Copper | chloride | 41.0% | 16 | 2 [src: counter_ion_effects] |
| Nickel | chloride | 39.3% | 17 | 2 [src: counter_ion_effects] |
| Uranium | acetate | 37.2% | 2 | 0 [src: counter_ion_effects] |
| Iron | media comp. | 33.3% | 1 | 0 [src: counter_ion_effects] |
| Chromium | media comp. | 29.2% | 2 | 0 [src: counter_ion_effects] |
| Selenium | media comp. | 26.8% | 1 | 0 [src: counter_ion_effects] |
| Mercury | chloride | 23.4% | 1 | 20 [src: counter_ion_effects] |
| Tungsten | media comp. | 10.8% | 1 | 0 [src: counter_ion_effects] |
| Molybdenum | media comp. | 9.2% | 1 | 0 [src: counter_ion_effects] |

Manganese, cadmium, iron, selenium, mercury, molybdenum and tungsten each have a mean from a single organism (DvH). [src: counter_ion_effects]

## Correlation hierarchy in DvH

DvH was the most extensively profiled organism, with 13 metals and 6 NaCl experiments. [src: counter_ion_effects] Whole-genome fitness correlations with NaCl ran from zinc (r=0.715) [src: counter_ion_effects], manganese (0.545) [src: counter_ion_effects], copper (0.532) [src: counter_ion_effects], cobalt (0.498) [src: counter_ion_effects], mercury (0.478) [src: counter_ion_effects], nickel (0.446) [src: counter_ion_effects], aluminum (0.420) [src: counter_ion_effects], molybdenum (0.396) [src: counter_ion_effects], uranium (0.350) [src: counter_ion_effects], selenium (0.342) [src: counter_ion_effects], chromium (0.318) [src: counter_ion_effects] and tungsten (0.298) [src: counter_ion_effects], down to iron (0.086). [src: counter_ion_effects] The report interprets this order as following toxicity mechanism. Metals that broadly displace cofactors (Zn, Mn, Cu, Co) share more genes with NaCl than metals targeting specific pathways (Mo and W, molybdopterin enzymes; Fe, iron-sulfur clusters). [src: counter_ion_effects] It frames the order as a gradient from general to pathway-specific toxicity [src: counter_ion_effects], with high overlap (r > 0.4) for Zn, Mn, Cu, Co, Hg and Ni read as broad cofactor displacement resembling general ionic stress [src: counter_ion_effects], and low overlap (r < 0.4) for Mo, U, Se, Cr, W and Fe read as targeting specific pathways such as molybdopterin, iron-sulfur clusters and selenoprotein biosynthesis. [src: counter_ion_effects] Iron (r=0.086) is attributed to iron limitation affecting specific Fe-dependent enzymes. [src: counter_ion_effects] The report summarizes this as general Zn (r=0.72) to specific Fe (r=0.09) [src: counter_ion_effects] and says it aligns with Nies (2003). [src: counter_ion_effects]

In DvH, 495 unique metal-important genes split into 73 shared-stress (14.7%) and 422 metal-specific (85.3%). [src: counter_ion_effects] Shared-stress genes were important across a mean 4.1 metals per gene versus 2.5 for metal-specific genes, consistent with broad vulnerability. [src: counter_ion_effects] Of the metal-specific genes, 90.5% had SEED annotations, against 78.1% of shared-stress genes. [src: counter_ion_effects] The report suggests the metal-specific set includes Ni/Fe-hydrogenase, nitrogenase regulators and metal transporters, while shared-stress genes include more uncharacterized general stress proteins. [src: counter_ion_effects] The report offers a gene classification framework splitting metal fitness genes into shared-stress (40%) and metal-specific (60%) classes. [src: counter_ion_effects]

## A within-organism copper salt test

psRCH2 was the only organism tested with copper as both CuCl₂ (anaerobic, 3 replicates) and CuSO₄ (aerobic, 3 replicates). [src: counter_ion_effects] The cross-salt correlation was r=0.439, lower than the within-replicate correlations (CuCl₂ r=0.720; CuSO₄ r=0.859). [src: counter_ion_effects] This comparison is severely confounded by aerobic versus anaerobic growth, since hundreds of genes differ between those conditions independent of copper. [src: counter_ion_effects] Aerobic CuSO₄ without Cl⁻ correlated more strongly with NaCl (r=0.450) than anaerobic CuCl₂ (r=0.212). The report reads this as further evidence against a chloride confound and as a sign of shared aerobic stress mechanisms. [src: counter_ion_effects]

## Metal Fitness Atlas core enrichment survives correction

The original Atlas found metal-important genes 87.4% core (OR, odds ratio, 2.08). [src: counter_ion_effects] The report notes this could in principle be inflated by shared osmotic-stress core machinery. [src: counter_ion_effects] After removing the ~40% shared-stress genes and keeping metal-specific genes, core-genome enrichment was fully preserved for 12 of 14 metals. [src: counter_ion_effects] Core enrichment increased for 7 of 14 metals: Mo, W, Hg, Se, Ni, Cr and U. [src: counter_ion_effects] The report explains that shared-stress genes are ~90% core, and removing them concentrates the analysis on metal-specific genes that are still highly core. [src: counter_ion_effects]

Four metals showed clearly stronger enrichment: molybdenum (delta +0.132 to +0.145) [src: counter_ion_effects], tungsten (+0.129 to +0.134) [src: counter_ion_effects], mercury (+0.116 to +0.133) [src: counter_ion_effects] and selenium (+0.115 to +0.131). [src: counter_ion_effects]

Core fraction (original → corrected) against baseline, and enrichment delta (original → corrected):

| Metal | Core fraction | Baseline | Delta | Verdict |
|---|---|---|---|---|
| Manganese | 1.000 → 1.000 | 0.818 | +0.182 → +0.182 | unchanged [src: counter_ion_effects] |
| Molybdenum | 0.950 → 0.964 | 0.818 | +0.132 → +0.145 | stronger [src: counter_ion_effects] |
| Tungsten | 0.947 → 0.952 | 0.818 | +0.129 → +0.134 | stronger [src: counter_ion_effects] |
| Mercury | 0.934 → 0.951 | 0.818 | +0.116 → +0.133 | stronger [src: counter_ion_effects] |
| Selenium | 0.933 → 0.949 | 0.818 | +0.115 → +0.131 | stronger [src: counter_ion_effects] |
| Zinc | 0.895 → 0.865 | 0.750 | +0.145 → +0.115 | weaker [src: counter_ion_effects] |
| Nickel | 0.882 → 0.892 | 0.794 | +0.088 → +0.098 | stronger [src: counter_ion_effects] |
| Copper | 0.882 → 0.876 | 0.792 | +0.090 → +0.084 | slightly weaker [src: counter_ion_effects] |
| Cobalt | 0.866 → 0.866 | 0.790 | +0.076 → +0.076 | unchanged [src: counter_ion_effects] |
| Aluminum | 0.897 → 0.866 | 0.799 | +0.099 → +0.068 | weaker [src: counter_ion_effects] |
| Chromium | 0.710 → 0.723 | 0.654 | +0.056 → +0.069 | stronger [src: counter_ion_effects] |
| Uranium | 0.685 → 0.694 | 0.654 | +0.031 → +0.040 | slightly stronger [src: counter_ion_effects] |
| Cadmium | 0.522 → 0.422 | 0.530 | -0.008 → -0.108 | reversed (n=92, 1 org) [src: counter_ion_effects] |
| Iron | 0.778 → 1.000 | 0.818 | -0.040 → +0.182 | reversed but n=9, 1 org [src: counter_ion_effects] |

Aluminum fell modestly from +0.099 to +0.068 [src: counter_ion_effects], and zinc from +0.145 to +0.115. [src: counter_ion_effects] Only cadmium reversed in the weakening direction, from -0.008 to -0.108. [src: counter_ion_effects] That result has very low statistical power, with only 92 original genes from 1 organism. [src: counter_ion_effects] The report concludes the atlas finding, that metal-fitness genes are core-enriched, is not an artifact of shared-stress overlap. [src: counter_ion_effects] It reads this as strengthening the core genome robustness model of the Metal Fitness Atlas (Dehal 2026), and claims validation of the Atlas. [src: counter_ion_effects] It notes that the Atlas reported condition-specific genes (important only for metals, not other stresses) as less core, and suggests this project's classification could refine that analysis. [src: counter_ion_effects]

## Data and Methods

The analysis compared metal-important and NaCl-important genes in fitness screens. It covered 19 organisms for overlap. [src: counter_ion_effects] DvH supplied the whole-genome correlations with NaCl. [src: counter_ion_effects] psRCH2 supplied the within-organism comparison of the two copper salts. [src: counter_ion_effects] Fitness scores and experiment metadata came from the kescience_fitnessbrowser tables genefitness and experiment, via cached matrices. [src: counter_ion_effects] Core/accessory classification came from the kbase_ke_pangenome table gene_cluster, via the FB (Fitness Browser)-pangenome link. [src: counter_ion_effects]

The project's five notebooks covered, in order: identifying 71 NaCl experiments and computing effective Cl⁻ [src: counter_ion_effects]; gene-set overlap, the Cl⁻ dose-response test and DvH profile correlations [src: counter_ion_effects]; shared-stress versus metal-specific classification with functional annotations [src: counter_ion_effects]; reanalysis of the Metal Fitness Atlas after removing shared-stress genes [src: counter_ion_effects]; and the direct psRCH2 CuCl₂ versus CuSO₄ comparison. [src: counter_ion_effects]

## Caveats and Open Work

The SynE outlier is addressed by the exclusion analysis above. [src: counter_ion_effects] The psRCH2 salt comparison is confounded by oxygen status, and it is the only within-metal counter-ion comparison. [src: counter_ion_effects] The cadmium (n=92) and iron (n=9) corrected deltas, each from one organism, are statistically unreliable. [src: counter_ion_effects] Manganese (n=30, 1 org) is low-powered, though its 100% core result is robust by ceiling effect. [src: counter_ion_effects] Several per-metal overlaps rest on one organism, with no cross-organism replication. [src: counter_ion_effects]

- NaCl delivers Na⁺ as well as Cl⁻, so its profile includes sodium toxicity and osmotic effects. The report proposes KCl or choline chloride as more specific chloride controls. [src: counter_ion_effects]
- The 39.8% overlap depends on the NaCl-importance threshold (fit < -1 or n_sick ≥ 1). Stricter thresholds would reduce it and more permissive ones would increase it. [src: counter_ion_effects]
- Putative essential genes (~14.3% of protein-coding genes) lack insertions and are absent from both datasets. They are 82% core, and excluding them affects original and corrected analyses equally. [src: counter_ion_effects]
- The shared-stress versus metal-specific classification was not formally tested for functional enrichment by hypergeometric tests, and the SEED annotation comparison is descriptive. [src: counter_ion_effects]
- H1d, on chloride versus oxyanion functional profiles, was dropped and not tested. [src: counter_ion_effects]

### Follow-up proposed by the report

- Use COG (clusters of orthologous groups), KEGG and PFAM annotations to test whether shared-stress genes are enriched for envelope/transport functions and metal-specific genes for metal-binding/efflux. [src: counter_ion_effects]
- Compare metal–choline chloride overlap with metal–NaCl overlap to separate chloride from osmotic confounding; several Fitness Browser organisms have choline chloride experiments. [src: counter_ion_effects]
- Apply the metal–NaCl overlap analysis to ICA (independent component analysis) modules from the fitness_modules project, asking whether metal-responsive modules overlap NaCl-responsive ones. [src: counter_ion_effects]
- Use the classification to refine the Atlas result on condition-specific metal genes. [src: counter_ion_effects]
- Run RB-TnSeq with matched metal chloride and sulfate concentrations in a single organism under identical growth conditions, which the report calls the most impactful follow-up because it removes the aerobic/anaerobic confound of the psRCH2 comparison. [src: counter_ion_effects]
- Specific proposed pairs: CuCl₂ 0.5 mM versus CuSO₄ 0.5 mM in MR-1 or DvH, since copper is the most-tested metal and both salts are available [src: counter_ion_effects]; ZnCl₂ 0.2 mM versus ZnSO₄ 0.2 mM in MR-1, adding chloride to the already-tested sulfate form to test the null directly [src: counter_ion_effects]; and CoCl₂ 0.1 mM versus CoSO₄ 0.1 mM in DvH, since cobalt has the highest Cl⁻ load in current data. [src: counter_ion_effects]
- Run NaCl dose-response experiments at 0.1, 1, 10, 100 and 500 mM in DvH to allow dose-matching between NaCl stress and effective Cl⁻ from metal salts. [src: counter_ion_effects]

## Slots Into

- [[concepts/counter-ion-confounding-in-metal-fitness-assays]]: overlap did not scale with chloride delivery, and zinc sulfate overlapped 44.6%. [src: counter_ion_effects]
- [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]]: 39.8% of metal-important records were also NaCl-important. [src: counter_ion_effects]
- [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]]: enrichment was preserved for 12 of 14 metals after correction. [src: counter_ion_effects]
- [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]]: 60.2% of records were metal-specific, and shared-stress genes spanned more metals. [src: counter_ion_effects]
- [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]]: the report proposes matched chloride/sulfate RB-TnSeq experiments for copper, zinc and cobalt. [src: counter_ion_effects]
