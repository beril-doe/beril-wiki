---
type: "Finding"
description: "The prediction that core-genome enrichment would weaken after shared-stress correction was rejected: enrichment is robust and strengthens for essential metals."
finding_id: "counter_ion_effects--e835d451"
result: "null result"
source: "counter_ion_effects"
quantities: []
caveat: "Cadmium (n=92, 1 organism) has delta -0.008 \u2192 -0.108 and iron (n=9, 1 organism) has delta -0.040 \u2192 +0.182, so the prose claim that only cadmium reverses conflicts with the table."
first_added: "2026-10-27"
source_hash: "c43b2ab4f0d5dd44e987cc5bb413ebd72891a74a14ce45245be883ec2ca48807"
---
# Core-genome enrichment not weakened by removing shared-stress genes

The prediction that core-genome enrichment would weaken after shared-stress correction was rejected: enrichment is robust and strengthens for essential metals. [src: counter_ion_effects]

## Evidence

> | **H1c** (atlas robustness) | Core enrichment weakens after correction | **Rejected**: enrichment is robust, strengthens for essential metals | [src: counter_ion_effects]

From the report [[summaries/counter_ion_effects__REPORT]].

## Caveat

Cadmium (n=92, 1 organism) has delta -0.008 → -0.108 and iron (n=9, 1 organism) has delta -0.040 → +0.182, so the prose claim that only cadmium reverses conflicts with the table. [src: counter_ion_effects]

> | Cadmium | 0.522 | 0.422 | 0.530 | -0.008 | -0.108 | reversed (n=92, 1 org) | | Iron | 0.778 | 1.000 | 0.818 | -0.040 | +0.182 | reversed but n=9, 1 org | [src: counter_ion_effects]

## Other caveats in this report

- Synechococcus elongatus (SynE) had 88.6% shared-stress genes (565/638) and 12 NaCl experiments spanning 0.5–250 mM, versus 1–6 experiments elsewhere. Excluding it reduced pooled overlap from 39.8% to 36.7% (3,739/10,183); the n_sick >= 1 rule is easier to meet with more experiments. [src: counter_ion_effects]
- The narrative says core enrichment was preserved for 12 of 14 metals and that only cadmium reversed. It reports increased deltas for molybdenum (+0.132 → +0.145), tungsten (+0.129 → +0.134), mercury (+0.116 → +0.133), and selenium (+0.115 → +0.131), but decreased deltas for aluminum (+0.099 → +0.068) and zinc (+0.145 → +0.115). Its reversal wording conflicts with the corrected-conservation table: cadmium remains negative, while iron changes sign. [src: counter_ion_effects]
- The psRCH2 copper-salt comparison cannot isolate counter-ion effects because the salts were tested under different oxygen conditions. [src: counter_ion_effects]
- As literature context, the report cites Danilova et al. (2020) for a 2.5-fold CuSO₄-versus-CuCl₂ toxicity difference at 0.5 M; it contrasts this with typical random barcode transposon sequencing (RB-TnSeq) concentrations of 0.05–2 mM and infers smaller counter-ion effects there. [src: counter_ion_effects]
- NaCl is not a chloride-only control because it introduces Na⁺ and osmotic stress; KCl or choline chloride would isolate chloride more specifically, although available choline chloride experiments differ in concentration. [src: counter_ion_effects]
