---
type: "Finding"
description: "The predicted dose-dependent relationship between Cl\u207b concentration and NaCl overlap was rejected, because ZnSO\u2084 with 0 Cl\u207b exceeded most chloride metals."
finding_id: "counter_ion_effects--619981e8"
result: "null result"
source: "counter_ion_effects"
quantities: []
caveat: "NaCl is not a chloride-only control because it also delivers Na\u207a and osmotic stress, so the test does not isolate chloride cleanly."
first_added: "2026-10-27"
source_hash: "c43b2ab4f0d5dd44e987cc5bb413ebd72891a74a14ce45245be883ec2ca48807"
---
# Dose-dependent chloride effect on NaCl overlap rejected

The predicted dose-dependent relationship between Cl⁻ concentration and NaCl overlap was rejected, because ZnSO₄ with 0 Cl⁻ exceeded most chloride metals. [src: counter_ion_effects]

## Evidence

> | **H1b** (dose-dependent Cl⁻) | Overlap scales with Cl⁻ concentration | **Rejected**: ZnSO₄ (0 Cl⁻) > most Cl⁻ metals | [src: counter_ion_effects]

From the report [[summaries/counter_ion_effects__REPORT]].

## Caveat

NaCl is not a chloride-only control because it also delivers Na⁺ and osmotic stress, so the test does not isolate chloride cleanly. [src: counter_ion_effects]

> - **NaCl ≠ pure Cl⁻ control**: NaCl delivers both Na⁺ and Cl⁻. The NaCl fitness profile includes sodium toxicity and osmotic stress effects beyond just chloride. A pure KCl or choline chloride control would more specifically isolate chloride effects (some FB organisms have choline chloride experiments but at different concentrations). [src: counter_ion_effects]

## Other caveats in this report

- Synechococcus elongatus (SynE) had 88.6% shared-stress genes (565/638) and 12 NaCl experiments spanning 0.5–250 mM, versus 1–6 experiments elsewhere. Excluding it reduced pooled overlap from 39.8% to 36.7% (3,739/10,183); the n_sick >= 1 rule is easier to meet with more experiments. [src: counter_ion_effects]
- The narrative says core enrichment was preserved for 12 of 14 metals and that only cadmium reversed. It reports increased deltas for molybdenum (+0.132 → +0.145), tungsten (+0.129 → +0.134), mercury (+0.116 → +0.133), and selenium (+0.115 → +0.131), but decreased deltas for aluminum (+0.099 → +0.068) and zinc (+0.145 → +0.115). Its reversal wording conflicts with the corrected-conservation table: cadmium remains negative, while iron changes sign. [src: counter_ion_effects]
- The psRCH2 copper-salt comparison cannot isolate counter-ion effects because the salts were tested under different oxygen conditions. [src: counter_ion_effects]
- The corrected-conservation table gives cadmium an original-to-corrected core fraction of 0.522 → 0.422 against baseline 0.530, with delta -0.008 → -0.108 (n=92, 1 organism): its delta does not reverse sign despite the table label. Iron changes core fraction 0.778 → 1.000 against baseline 0.818 and delta -0.040 → +0.182 (n=9, 1 organism): its delta does reverse sign. This conflicts with the prose claim that only cadmium reverses. [src: counter_ion_effects]
- As literature context, the report cites Danilova et al. (2020) for a 2.5-fold CuSO₄-versus-CuCl₂ toxicity difference at 0.5 M; it contrasts this with typical random barcode transposon sequencing (RB-TnSeq) concentrations of 0.05–2 mM and infers smaller counter-ion effects there. [src: counter_ion_effects]
