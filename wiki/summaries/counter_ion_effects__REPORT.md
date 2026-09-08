---
type: Summary
description: Metal–NaCl overlap is real stress biology, not counter-ion confounding.
doc_type: short
full_text: ../sources/counter_ion_effects__REPORT.md
title: Counter Ion Effects on Metal Fitness Measurements
sources:
- id: counter_ion_effects
  resource: ../sources/counter_ion_effects__REPORT.md
  title: counter ion effects
---
# Counter Ion Effects on Metal Fitness Measurements

## Overview

This analysis tested whether counter ions, especially chloride delivered by metal salts, confound genome-wide metal-fitness measurements. Across 71 NaCl experiments, 10,821 metal-important gene records, 86 organism × metal pairs, 14 metals, and 19 organisms, it found substantial metal–NaCl overlap but no evidence that chloride dose is the primary driver. The overlap reflects shared cellular stress biology, while Metal Fitness Atlas core-genome enrichment remains robust after removing shared-stress genes. [^counter_ion_effects]

## Key Findings

### Shared NaCl and Metal Fitness Signals

Across 19 organisms and 14 metals, 4,304 of 10,821 metal-important gene records (39.8%) were also NaCl-important. Overlap occurred for every metal, ranging from 9.2% for molybdenum to 57.6% for manganese. Excluding the *Synechococcus elongatus* outlier, which contributed 565/638 shared genes (88.6%) from 12 NaCl dose-response experiments, overlap declined from 39.8% to 36.7% (3,739/10,183), so the result was not driven by that outlier. [^counter_ion_effects]

NaCl experiments identified 4,648 NaCl-important genes across 25 organisms, while the overlap analysis included 19 organisms and 86 organism × metal pairs. The 10,821 tested metal-important records therefore include 6,517 metal-specific records (60.2%) and 4,304 shared-stress records (39.8%). [^counter_ion_effects]

Shared-stress genes were important for a mean of 4.1 metals per gene, compared with 2.5 metals per metal-specific gene. In DvH, 495 unique metal-important genes comprised 73 shared-stress genes (14.7%) and 422 metal-specific genes (85.3%); 90.5% of metal-specific genes had SEED annotations compared with 78.1% of shared-stress genes. [^counter_ion_effects]

### Counter Ions Are Not the Primary Driver

Chloride concentration did not explain the overlap. Zinc sulfate, which delivers 0 mM chloride, had 44.6% NaCl overlap, exceeding cobalt at 41.3% despite cobalt delivering up to 500 mM chloride, copper at 41.0%, and nickel at 39.3%. Chloride-delivered metals had a mean overlap of 41.6%, compared with 37.8% for non-chloride metals. [^counter_ion_effects]

The per-metal overlap values were manganese 57.6% (1 organism), cadmium 50.5% (1), aluminum 46.1% (12), zinc 44.6% (12), cobalt 41.3% (18), copper 41.0% (16), nickel 39.3% (17), uranium 37.2% (2), iron 33.3% (1), chromium 29.2% (2), selenium 26.8% (1), mercury 23.4% (1), tungsten 10.8% (1), and molybdenum 9.2% (1). [^counter_ion_effects]

The report interprets the shared signal as biology involving cell-envelope integrity, DNA repair, and ion homeostasis, rather than counter-ion contamination. NaCl is not a pure chloride control because it also supplies sodium and osmotic stress. [^counter_ion_effects]

### DvH Metal–NaCl Correlation Hierarchy

In DvH, which had 13 metals and 6 NaCl experiments, whole-genome Pearson correlations with NaCl were zinc r=0.715, manganese r=0.545, copper r=0.532, cobalt r=0.498, mercury r=0.478, nickel r=0.446, aluminum r=0.420, molybdenum r=0.396, uranium r=0.350, selenium r=0.342, chromium r=0.318, tungsten r=0.298, and iron r=0.086. The hierarchy did not follow chloride concentration: zinc sulfate had zero chloride but ranked first. [^counter_ion_effects]

The report interprets high NaCl correlation as consistent with broad toxicity through essential-cofactor displacement or disruption of multiple cellular systems, especially for zinc, manganese, copper, cobalt, mercury, and nickel. Lower correlation for molybdenum, uranium, selenium, chromium, tungsten, and iron is interpreted as consistent with more pathway-specific effects; iron was described as affecting specific iron-dependent enzymes rather than causing general cellular damage. These mechanistic interpretations are extrapolations from the fitness-profile hierarchy rather than direct biochemical tests. [^counter_ion_effects]

### Metal Fitness Atlas Robustness

After removing shared-stress genes and restricting analysis to metal-specific genes, core-genome enrichment was preserved for 12 of 14 metals. Seven metals showed stronger corrected enrichment: molybdenum, with delta changing from +0.132 to +0.145; tungsten, +0.129 to +0.134; mercury, +0.116 to +0.133; selenium, +0.115 to +0.131; nickel, +0.088 to +0.098; chromium, +0.056 to +0.069; and uranium, +0.031 to +0.040. [^counter_ion_effects]

Aluminum weakened from +0.099 to +0.068, zinc from +0.145 to +0.115, and copper from +0.090 to +0.084; manganese remained +0.182 and cobalt remained +0.076. Cadmium changed from -0.008 to -0.108, while iron changed from -0.040 to +0.182. Cadmium had n=92 genes and iron had n=9 genes, each from one organism, so those corrected values have low statistical power; manganese also had only n=30 genes from one organism, although its 100% core fraction is a ceiling result. [^counter_ion_effects]

The original Metal Fitness Atlas conclusion that metal-important genes are 87.4% core, with OR=2.08, was therefore not attributable to shared NaCl-stress genes. The report states that researchers using the atlas do not need to filter out NaCl-responsive genes for the atlas’s core-enrichment conclusion. [^counter_ion_effects]

### Within-Metal Salt Comparison

psRCH2 was the only organism with copper tested as both CuCl₂ and CuSO₄. The cross-salt correlation was r=0.439, compared with within-replicate correlations of r=0.720 for CuCl₂ and r=0.859 for CuSO₄. This comparison is severely confounded by aerobic versus anaerobic growth: CuCl₂ was tested anaerobically and CuSO₄ aerobically, so hundreds of genes may differ independently of copper. [^counter_ion_effects]

CuSO₄ had a higher correlation with NaCl than CuCl₂, r=0.450 versus r=0.212, despite supplying no chloride. This result argues against chloride as the primary confound, but the aerobic/anaerobic confounding prevents the comparison from isolating counter-ion effects. [^counter_ion_effects]

### Hypothesis Outcomes

H1a, predicting more than 20% overlap, was supported by the 39.8% overlap. H1b, predicting a dose-dependent chloride relationship, was rejected because zinc sulfate with 0 mM chloride exceeded most chloride-delivered metals. H1c, predicting weakened atlas core enrichment after correction, was rejected because enrichment was robust and strengthened for several metals. H1d, predicting chloride-versus-oxyanion functional-profile differences, was not tested. The null hypothesis that counter ions are negligible was partially supported: counter ions appeared negligible specifically, while shared-stress biology was substantial but did not undermine atlas conclusions. [^counter_ion_effects]

## Caveats

The 39.8% overlap depends on the NaCl-importance threshold, defined using fit < -1 or n_sick ≥ 1; stricter or more permissive thresholds could reduce or increase the overlap. The *S. elongatus* estimate is especially sensitive because it had 12 NaCl experiments spanning 0.5–250 mM, whereas other organisms had 1–6 NaCl experiments. [^counter_ion_effects]

NaCl cannot isolate chloride because it delivers both Na⁺ and Cl⁻ and produces osmotic effects. A KCl or choline chloride control would more specifically test chloride effects, although some Fitness Browser organisms have choline chloride experiments at different concentrations. [^counter_ion_effects]

Approximately 14.3% of protein-coding genes, classified as putative essential genes, lacked transposon insertions and were absent from both NaCl and metal-fitness data. These genes are 82% core, and their exclusion affects the original and corrected conservation analyses equally. [^counter_ion_effects]

Manganese, cadmium, selenium, mercury, iron, molybdenum, and tungsten were each tested in only 1 organism, so their overlap statistics lack cross-organism replication. The psRCH2 CuCl₂–CuSO₄ comparison is additionally limited by aerobic/anaerobic confounding. [^counter_ion_effects]

The shared-stress versus metal-specific classification did not include formal functional-enrichment tests; the SEED annotation comparison was descriptive. The proposed mechanistic categories therefore remain hypotheses requiring direct functional testing. [^counter_ion_effects]

The report proposes formal COG, KEGG, and PFAM enrichment tests; comparison with choline chloride; module-level analysis using independent component analysis (ICA); refinement of condition-specific metal-gene analysis; and matched CuCl₂/CuSO₄, ZnCl₂/ZnSO₄, and CoCl₂/CoSO₄ RB-TnSeq experiments under identical conditions. It also proposes DvH NaCl dose-response experiments at 0.1, 1, 10, 100, and 500 mM to match effective chloride doses. [^counter_ion_effects]

## Slots Into

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the 39.8% overlap and DvH correlation hierarchy show that metal fitness profiles combine shared-stress and metal-specific condition responses. [^counter_ion_effects]
- [gene-essentiality](../concepts/gene-essentiality.md) — corrected core-enrichment analysis shows that the Metal Fitness Atlas signal persists after removing shared-stress genes, while putative essential genes remain excluded from both datasets. [^counter_ion_effects]
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — the DvH whole-genome metal–NaCl correlations and proposed module-level decomposition provide cross-condition fitness-profile evidence for shared versus specific stress architecture. [^counter_ion_effects]

[^counter_ion_effects]: [counter ion effects](../sources/counter_ion_effects__REPORT.md)
