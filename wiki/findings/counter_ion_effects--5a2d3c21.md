---
type: "Finding"
description: "Across 19 organisms and 14 metals (86 organism \u00d7 metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) are also important under NaCl stress, for every metal tested, from 9.2% for molybdenum to 57.6% for manganese."
finding_id: "counter_ion_effects--5a2d3c21"
result: "observation"
source: "counter_ion_effects"
quantities: [{"value": "39.8%", "what": "pooled share of metal-important gene records also important under NaCl stress", "unit": "%", "denominator": "10,821 metal-important gene records", "scope": "19 organisms, 14 metals, 86 organism \u00d7 metal pairs"}, {"value": "4,304", "what": "metal-important gene records also important under NaCl", "unit": "gene records", "denominator": "10,821", "scope": "pooled"}, {"value": "9.2%", "what": "lowest per-metal overlap (molybdenum)", "unit": "%", "denominator": "", "scope": "per metal"}, {"value": "57.6%", "what": "highest per-metal overlap (manganese)", "unit": "%", "denominator": "", "scope": "per metal"}]
caveat: "Synechococcus elongatus is an outlier (88.6% shared-stress, 565/638 genes, 12 NaCl experiments); excluding it lowers pooled overlap from 39.8% to 36.7% (3,739/10,183), and the n_sick >= 1 rule is easier to meet with more experiments."
first_added: "2026-10-27"
source_hash: "c43b2ab4f0d5dd44e987cc5bb413ebd72891a74a14ce45245be883ec2ca48807"
---
# Large share of metal-important genes also matter under NaCl stress

Across 19 organisms and 14 metals (86 organism × metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) are also important under NaCl stress, for every metal tested, from 9.2% for molybdenum to 57.6% for manganese. [src: counter_ion_effects]

## Key figures

- **39.8%**: pooled share of metal-important gene records also important under NaCl stress (denominator 10,821 metal-important gene records; scope 19 organisms, 14 metals, 86 organism × metal pairs) [src: counter_ion_effects]
- **4,304 gene records**: metal-important gene records also important under NaCl (denominator 10,821; scope pooled) [src: counter_ion_effects]
- **9.2%**: lowest per-metal overlap (molybdenum) (scope per metal) [src: counter_ion_effects]
- **57.6%**: highest per-metal overlap (manganese) (scope per metal) [src: counter_ion_effects]

## Evidence

> Across 19 organisms and 14 metals (86 organism × metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) are also important under NaCl stress. This substantial overlap exists for every metal tested — from 9.2% for molybdenum to 57.6% for manganese — indicating that a large fraction of the "metal fitness" signal reflects general cellular vulnerability shared between metal and osmotic/ionic stress. [src: counter_ion_effects]

From the report [[summaries/counter_ion_effects__REPORT]].

## Caveat

Synechococcus elongatus is an outlier (88.6% shared-stress, 565/638 genes, 12 NaCl experiments); excluding it lowers pooled overlap from 39.8% to 36.7% (3,739/10,183), and the n_sick >= 1 rule is easier to meet with more experiments. [src: counter_ion_effects]

> **Sensitivity to outliers**: *Synechococcus elongatus* (SynE) is a dramatic outlier at 88.6% shared-stress (565/638 genes), driven by its 12 NaCl dose-response experiments spanning 0.5–250 mM — far more than any other organism (1–6 NaCl experiments). The `n_sick >= 1` threshold is much easier to satisfy with 12 experiments. Excluding SynE, the overall overlap drops modestly from 39.8% to 36.7% (3,739/10,183), confirming that the finding is not driven by this outlier. The next-highest organisms (Korea 58.6%, Phaeo 56.4%, Pedo557 53.0%) have typical NaCl experiment counts. [src: counter_ion_effects]

## Other caveats in this report

- The narrative says core enrichment was preserved for 12 of 14 metals and that only cadmium reversed. It reports increased deltas for molybdenum (+0.132 → +0.145), tungsten (+0.129 → +0.134), mercury (+0.116 → +0.133), and selenium (+0.115 → +0.131), but decreased deltas for aluminum (+0.099 → +0.068) and zinc (+0.145 → +0.115). Its reversal wording conflicts with the corrected-conservation table: cadmium remains negative, while iron changes sign. [src: counter_ion_effects]
- The psRCH2 copper-salt comparison cannot isolate counter-ion effects because the salts were tested under different oxygen conditions. [src: counter_ion_effects]
- The corrected-conservation table gives cadmium an original-to-corrected core fraction of 0.522 → 0.422 against baseline 0.530, with delta -0.008 → -0.108 (n=92, 1 organism): its delta does not reverse sign despite the table label. Iron changes core fraction 0.778 → 1.000 against baseline 0.818 and delta -0.040 → +0.182 (n=9, 1 organism): its delta does reverse sign. This conflicts with the prose claim that only cadmium reverses. [src: counter_ion_effects]
- As literature context, the report cites Danilova et al. (2020) for a 2.5-fold CuSO₄-versus-CuCl₂ toxicity difference at 0.5 M; it contrasts this with typical random barcode transposon sequencing (RB-TnSeq) concentrations of 0.05–2 mM and infers smaller counter-ion effects there. [src: counter_ion_effects]
- NaCl is not a chloride-only control because it introduces Na⁺ and osmotic stress; KCl or choline chloride would isolate chloride more specifically, although available choline chloride experiments differ in concentration. [src: counter_ion_effects]
