---
type: "Concept"
description: "How to distinguish shared stress responses from stressor-specific fitness requirements"
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/metal_specificity__REPORT.md"]
---
# Separating Shared Stress Responses from Stressor-Specific Fitness Requirements

Fitness profiles measured under different stressors can contain both a shared cellular-stress component and requirements specific to the tested stressor. This distinction is important for interpreting condition-specific fitness, because overlap between stressor responses does not by itself show that the delivery vehicle or counter ion caused the signal. [src: counter_ion_effects]

The [[summaries/counter_ion_effects__REPORT]] provides a direct test using metal and NaCl fitness data. Across 71 NaCl experiments, 10,821 metal-important gene records, 86 organism × metal pairs, 14 metals, and 19 organisms, 4,304 records—39.8%—were also NaCl-important. [src: counter_ion_effects] The analysis therefore supports a substantial shared-stress component, while retaining a larger metal-specific component of 6,517 records—60.2%. [src: counter_ion_effects]

## Evidence for a Shared-Stress Component

NaCl-important genes overlapped with metal-important genes for every metal, with overlap ranging from 9.2% for molybdenum to 57.6% for manganese. [src: counter_ion_effects] Removing the *Synechococcus elongatus* outlier reduced overlap from 39.8% to 36.7%, or from 4,304/10,821 to 3,739/10,183 records, so the overall signal was not driven by that organism. [src: counter_ion_effects]

Shared-stress genes were important for a mean of 4.1 metals per gene, compared with 2.5 metals per metal-specific gene. [src: counter_ion_effects] In *Desulfovibrio vulgaris* Hildenborough (DvH), 495 unique metal-important genes comprised 73 shared-stress genes, or 14.7%, and 422 metal-specific genes, or 85.3%. [src: counter_ion_effects] This pattern supports the interpretation that shared-stress genes tend to recur across more metal conditions, whereas metal-specific genes contribute more narrowly distributed fitness requirements. [src: counter_ion_effects]

The functional interpretation is consistent with shared cellular pressures involving cell-envelope integrity, DNA repair, and ion homeostasis, but these categories were not tested with formal functional-enrichment analyses. [src: counter_ion_effects] The proposed mechanisms should therefore be treated as hypotheses rather than established pathway assignments. [src: counter_ion_effects]

The [[summaries/metal_specificity__REPORT]] **supports** this decomposition with an independent classification of 7,609 metal-important gene records: 4,177 (54.9%) were metal-specific, 2,888 (38.0%) were general sick across non-metal experiments, and 544 (7.2%) were metal+stress. [src: metal_specificity] Its metal-specific category used a stricter non-metal sick-rate criterion, so it should not be interpreted as a replacement estimate for the 39.8% NaCl-overlap fraction. [src: metal_specificity] In particular, the counter-ion analysis found 39.8% overlap, whereas the stricter analysis found 14.7% sick under osmotic stress; this **refines** the shared-stress estimate by showing that the fraction depends materially on thresholds and condition scope. [src: metal_specificity]

## Evidence for Stressor-Specific Requirements

The overlap did not account for most metal-important records: 6,517 records, or 60.2%, were classified as metal-specific. [src: counter_ion_effects] In DvH, 90.5% of metal-specific genes had SEED annotations, compared with 78.1% of shared-stress genes, although this comparison was descriptive rather than a formal enrichment test. [src: counter_ion_effects]

The DvH whole-genome Pearson correlations with NaCl formed a heterogeneous hierarchy rather than a uniform shared-stress response: zinc r=0.715, manganese r=0.545, copper r=0.532, cobalt r=0.498, mercury r=0.478, nickel r=0.446, aluminum r=0.420, molybdenum r=0.396, uranium r=0.350, selenium r=0.342, chromium r=0.318, tungsten r=0.298, and iron r=0.086. [src: counter_ion_effects] The report interprets higher correlations for zinc, manganese, copper, cobalt, mercury, and nickel as consistent with broad toxicity, while lower correlations for molybdenum, uranium, selenium, chromium, tungsten, and iron are consistent with more pathway-specific effects; these mechanistic interpretations are extrapolations from fitness profiles rather than direct biochemical tests. [src: counter_ion_effects]

This separation refines [[concepts/condition-specific-fitness]]: a condition-specific fitness profile should be decomposed into shared-stress and stressor-specific components before being assigned a mechanistic interpretation. [src: counter_ion_effects] The metal-specificity analysis **supports** this interpretation because metal-specific genes were enriched for metal-resistance keywords relative to general-sick genes (12.2% versus 7.8%; Fisher exact OR=1.64, p=2.4e-8). [src: metal_specificity]

## Counter-Ion Test

The shared signal was not explained by chloride dose. Zinc sulfate delivered 0 mM chloride yet had 44.6% NaCl overlap, exceeding cobalt at 41.3% despite cobalt delivering up to 500 mM chloride, copper at 41.0%, and nickel at 39.3%. [src: counter_ion_effects] Chloride-delivered metals had a mean overlap of 41.6%, compared with 37.8% for non-chloride metals. [src: counter_ion_effects]

In DvH, zinc sulfate also had the highest NaCl correlation, r=0.715, despite delivering zero chloride. [src: counter_ion_effects] This supports the conclusion that shared fitness signals primarily reflect common cellular stress biology rather than chloride contamination, while NaCl remains an imperfect chloride control because it supplies sodium and creates osmotic stress. [src: counter_ion_effects]

The only within-organism comparison of copper salts was severely confounded: CuCl₂ was tested anaerobically and CuSO₄ aerobically in psRCH2. [src: counter_ion_effects] The cross-salt correlation was r=0.439, compared with within-replicate correlations of r=0.720 for CuCl₂ and r=0.859 for CuSO₄. [src: counter_ion_effects] CuSO₄ had a higher NaCl correlation than CuCl₂, r=0.450 versus r=0.212, despite supplying no chloride, which argues against chloride as the primary confound but does not isolate counter-ion effects because oxygen regime differed. [src: counter_ion_effects]

## Consequences for Atlas-Level Inference

Removing shared-stress genes preserved Metal Fitness Atlas core-genome enrichment for 12 of 14 metals. [src: counter_ion_effects] Corrected enrichment strengthened for molybdenum, changing from +0.132 to +0.145; tungsten, from +0.129 to +0.134; mercury, from +0.116 to +0.133; selenium, from +0.115 to +0.131; nickel, from +0.088 to +0.098; chromium, from +0.056 to +0.069; and uranium, from +0.031 to +0.040. [src: counter_ion_effects]

Aluminum weakened from +0.099 to +0.068, zinc from +0.145 to +0.115, and copper from +0.090 to +0.084, while manganese remained +0.182 and cobalt remained +0.076. [src: counter_ion_effects] Cadmium changed from -0.008 to -0.108, and iron changed from -0.040 to +0.182. [src: counter_ion_effects] Cadmium had n=92 genes and iron had n=9 genes, each from one organism, while manganese had n=30 genes from one organism; these results therefore have low statistical power or, for manganese, a 100% core fraction that is a ceiling result. [src: counter_ion_effects]

The original conclusion that metal-important genes were 87.4% core, with OR=2.08, was not attributable to shared NaCl-stress genes. [src: counter_ion_effects] This supports [[concepts/gene-essentiality]] by showing that removing a broad shared-stress component does not eliminate the atlas-level conservation signal.

## Interpretation and Boundaries

The 39.8% overlap depends on the NaCl-importance threshold of fit < -1 or n_sick ≥ 1, so changing that threshold could change the estimated shared-stress fraction. [src: counter_ion_effects] The *S. elongatus* estimate is especially sensitive because it had 12 NaCl experiments spanning 0.5–250 mM, whereas other organisms had 1–6 NaCl experiments. [src: counter_ion_effects]

The overlap analysis cannot by itself distinguish chloride, sodium, osmotic stress, or other shared physiological effects because NaCl contains both Na⁺ and Cl⁻. [src: counter_ion_effects] The result therefore motivates [[concepts/salt-chemistry-confounding-of-fitness-assays]] rather than replacing it with a claim that counter ions are universally negligible.

Approximately 14.3% of protein-coding genes were classified as putative essential genes because they lacked transposon insertions and were absent from both NaCl and metal-fitness data. [src: counter_ion_effects] These genes were 82% core, and their exclusion affected the original and corrected conservation analyses equally. [src: counter_ion_effects] This limitation connects the decomposition problem to [[concepts/essentiality-assay-discordance]] and [[concepts/gene-essentiality]], because unmeasured essential genes cannot be assigned confidently to either shared-stress or stressor-specific fitness requirements.

The stricter metal-specificity analysis also had substantial representation limits: 7,609 of 12,838 metal-important gene records were retained, while 5,229 were excluded because of locusId-format mismatches, and seven metal-tested organisms could not be processed. [src: metal_specificity] This **refines** the interpretation of cross-condition fractions by showing that both classification thresholds and analyzable organism sets can shape the apparent balance between shared and stressor-specific requirements. [src: metal_specificity]

## Open Directions

- Compare matched choline chloride and NaCl datasets to ask whether the shared component follows chloride specifically or instead reflects sodium and osmotic stress; choline chloride would provide a more specific chloride control than NaCl. [src: counter_ion_effects]
- Perform formal COG, KEGG, and PFAM enrichment tests on shared-stress versus metal-specific genes to test whether cell-envelope, DNA-repair, and ion-homeostasis categories are genuinely overrepresented. [src: counter_ion_effects]
- Apply independent component analysis (ICA), a method that decomposes correlated measurements into latent components, to metal and NaCl fitness profiles to ask whether shared and stressor-specific axes can be separated at the module level. [src: counter_ion_effects] The metal-specificity analysis identified 0 metal-specific modules using per-module z-normalization, but notes that its raw module-condition scale differed from the precomputed z-scored profiles that identified 600 metal-responsive module records; rerunning the comparison on the latter profiles would test whether the negative result is scale-dependent. [src: metal_specificity]
- Run matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ RB-TnSeq experiments—random barcode transposon sequencing—under identical oxygen and culture conditions to test counter-ion effects without aerobic/anaerobic confounding. [src: counter_ion_effects]
- Generate DvH NaCl dose-response data at 0.1, 1, 10, 100, and 500 mM to match effective chloride doses and test whether the metal–NaCl correlation hierarchy changes with dose. [src: counter_ion_effects]
- Reanalyze the 10,821 metal-important records with stricter and more permissive NaCl-importance thresholds to quantify how much the estimated 39.8% shared-stress fraction depends on classification rules. [src: counter_ion_effects] Resolve the metal-specificity locusId mismatches and repeat its classification across the excluded organisms to test whether attrition changes the shared-versus-specific balance. [src: metal_specificity]
