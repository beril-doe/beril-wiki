---
type: "Finding"
description: "In psRCH2, the only organism with copper as both CuCl\u2082 (anaerobic, 3 replicates) and CuSO\u2084 (aerobic, 3 replicates), the cross-salt fitness correlation was r=0.439, lower than within-replicate correlations of r=0.720 (CuCl\u2082) and r=0.859 (CuSO\u2084)."
finding_id: "counter_ion_effects--5a523214"
result: "observation"
source: "counter_ion_effects"
quantities: [{"value": "r=0.439", "what": "cross-salt fitness correlation, CuCl\u2082 vs CuSO\u2084", "unit": "", "denominator": "", "scope": "psRCH2"}, {"value": "r=0.720", "what": "within-replicate correlation, CuCl\u2082", "unit": "", "denominator": "", "scope": "psRCH2"}, {"value": "r=0.859", "what": "within-replicate correlation, CuSO\u2084", "unit": "", "denominator": "", "scope": "psRCH2"}]
caveat: "The comparison is severely confounded by aerobic/anaerobic growth, since hundreds of genes differ between these conditions independent of copper, so it cannot isolate counter-ion effects."
first_added: "2026-10-27"
source_hash: "c43b2ab4f0d5dd44e987cc5bb413ebd72891a74a14ce45245be883ec2ca48807"
---
# Same-metal copper salts in psRCH2 correlate weakly across counter ions

In psRCH2, the only organism with copper as both CuCl₂ (anaerobic, 3 replicates) and CuSO₄ (aerobic, 3 replicates), the cross-salt fitness correlation was r=0.439, lower than within-replicate correlations of r=0.720 (CuCl₂) and r=0.859 (CuSO₄). [src: counter_ion_effects]

## Key figures

- **r=0.439**: cross-salt fitness correlation, CuCl₂ vs CuSO₄ (scope psRCH2) [src: counter_ion_effects]
- **r=0.720**: within-replicate correlation, CuCl₂ (scope psRCH2) [src: counter_ion_effects]
- **r=0.859**: within-replicate correlation, CuSO₄ (scope psRCH2) [src: counter_ion_effects]

## Evidence

> psRCH2 is the only organism tested with the same metal (copper) as both CuCl₂ (anaerobic, 3 replicates) and CuSO₄ (aerobic, 3 replicates). The cross-salt correlation is r=0.439, substantially lower than within-replicate correlations (CuCl₂: r=0.720; CuSO₄: r=0.859). [src: counter_ion_effects]

From the report [[summaries/counter_ion_effects__REPORT]].

## Caveat

The comparison is severely confounded by aerobic/anaerobic growth, since hundreds of genes differ between these conditions independent of copper, so it cannot isolate counter-ion effects. [src: counter_ion_effects]

> However, this comparison is severely confounded by aerobic/anaerobic growth — hundreds of genes differ between these conditions independent of copper. [src: counter_ion_effects]

## Other caveats in this report

- Synechococcus elongatus (SynE) had 88.6% shared-stress genes (565/638) and 12 NaCl experiments spanning 0.5–250 mM, versus 1–6 experiments elsewhere. Excluding it reduced pooled overlap from 39.8% to 36.7% (3,739/10,183); the n_sick >= 1 rule is easier to meet with more experiments. [src: counter_ion_effects]
- The narrative says core enrichment was preserved for 12 of 14 metals and that only cadmium reversed. It reports increased deltas for molybdenum (+0.132 → +0.145), tungsten (+0.129 → +0.134), mercury (+0.116 → +0.133), and selenium (+0.115 → +0.131), but decreased deltas for aluminum (+0.099 → +0.068) and zinc (+0.145 → +0.115). Its reversal wording conflicts with the corrected-conservation table: cadmium remains negative, while iron changes sign. [src: counter_ion_effects]
- The corrected-conservation table gives cadmium an original-to-corrected core fraction of 0.522 → 0.422 against baseline 0.530, with delta -0.008 → -0.108 (n=92, 1 organism): its delta does not reverse sign despite the table label. Iron changes core fraction 0.778 → 1.000 against baseline 0.818 and delta -0.040 → +0.182 (n=9, 1 organism): its delta does reverse sign. This conflicts with the prose claim that only cadmium reverses. [src: counter_ion_effects]
- As literature context, the report cites Danilova et al. (2020) for a 2.5-fold CuSO₄-versus-CuCl₂ toxicity difference at 0.5 M; it contrasts this with typical random barcode transposon sequencing (RB-TnSeq) concentrations of 0.05–2 mM and infers smaller counter-ion effects there. [src: counter_ion_effects]
- NaCl is not a chloride-only control because it introduces Na⁺ and osmotic stress; KCl or choline chloride would isolate chloride more specifically, although available choline chloride experiments differ in concentration. [src: counter_ion_effects]
