---
type: "Finding"
description: "The report found no chloride-dose pattern: zinc sulfate (0 mM Cl\u207b) had 44.6% NaCl overlap, versus cobalt 41.3% (up to 500 mM Cl\u207b), copper 41.0% and nickel 39.3%, with group means of 41.6% for chloride metals and 37.8% for non-chloride metals; it concludes the overlap reflects shared stress biology rather than chloride counter ions."
finding_id: "counter_ion_effects--482d2003"
result: "inference"
source: "counter_ion_effects"
quantities: [{"value": "44.6%", "what": "zinc sulfate NaCl overlap at 0 mM Cl\u207b", "unit": "%", "denominator": "", "scope": "per-metal mean"}, {"value": "41.3%", "what": "cobalt NaCl overlap (up to 500 mM Cl\u207b)", "unit": "%", "denominator": "", "scope": "per-metal mean"}, {"value": "41.6%", "what": "mean overlap for chloride metals", "unit": "%", "denominator": "", "scope": "group mean"}, {"value": "37.8%", "what": "mean overlap for non-chloride metals", "unit": "%", "denominator": "", "scope": "group mean"}]
caveat: "NaCl is not a chloride-only control because it also delivers Na\u207a and osmotic stress; KCl or choline chloride would isolate chloride more specifically, though available choline chloride experiments differ in concentration."
first_added: "2026-10-27"
source_hash: "c43b2ab4f0d5dd44e987cc5bb413ebd72891a74a14ce45245be883ec2ca48807"
---
# NaCl overlap does not track chloride delivered by the metal salt

The report found no chloride-dose pattern: zinc sulfate (0 mM Cl⁻) had 44.6% NaCl overlap, versus cobalt 41.3% (up to 500 mM Cl⁻), copper 41.0% and nickel 39.3%, with group means of 41.6% for chloride metals and 37.8% for non-chloride metals; it concludes the overlap reflects shared stress biology rather than chloride counter ions. [src: counter_ion_effects]

## Key figures

- **44.6%**: zinc sulfate NaCl overlap at 0 mM Cl⁻ (scope per-metal mean) [src: counter_ion_effects]
- **41.3%**: cobalt NaCl overlap (up to 500 mM Cl⁻) (scope per-metal mean) [src: counter_ion_effects]
- **41.6%**: mean overlap for chloride metals (scope group mean) [src: counter_ion_effects]
- **37.8%**: mean overlap for non-chloride metals (scope group mean) [src: counter_ion_effects]

## Evidence

> The critical test: does the overlap scale with chloride delivered by the metal salt? **No.** Zinc sulfate (0 mM Cl⁻) shows 44.6% NaCl overlap — higher than most chloride-delivered metals including cobalt (41.3%, up to 500 mM Cl⁻), copper (41.0%), and nickel (39.3%). Chloride metals as a group (mean 41.6%) are barely different from non-chloride metals (37.8%). The overlap is driven by shared stress biology — cell envelope damage, ion homeostasis disruption, and general stress response — not by chloride counter ions. [src: counter_ion_effects]

From the report [[summaries/counter_ion_effects__REPORT]].

## Caveat

NaCl is not a chloride-only control because it also delivers Na⁺ and osmotic stress; KCl or choline chloride would isolate chloride more specifically, though available choline chloride experiments differ in concentration. [src: counter_ion_effects]

> - **NaCl ≠ pure Cl⁻ control**: NaCl delivers both Na⁺ and Cl⁻. The NaCl fitness profile includes sodium toxicity and osmotic stress effects beyond just chloride. A pure KCl or choline chloride control would more specifically isolate chloride effects (some FB organisms have choline chloride experiments but at different concentrations). [src: counter_ion_effects]

## Other caveats in this report

- Synechococcus elongatus (SynE) had 88.6% shared-stress genes (565/638) and 12 NaCl experiments spanning 0.5–250 mM, versus 1–6 experiments elsewhere. Excluding it reduced pooled overlap from 39.8% to 36.7% (3,739/10,183); the n_sick >= 1 rule is easier to meet with more experiments. [src: counter_ion_effects]
- The narrative says core enrichment was preserved for 12 of 14 metals and that only cadmium reversed. It reports increased deltas for molybdenum (+0.132 → +0.145), tungsten (+0.129 → +0.134), mercury (+0.116 → +0.133), and selenium (+0.115 → +0.131), but decreased deltas for aluminum (+0.099 → +0.068) and zinc (+0.145 → +0.115). Its reversal wording conflicts with the corrected-conservation table: cadmium remains negative, while iron changes sign. [src: counter_ion_effects]
- The psRCH2 copper-salt comparison cannot isolate counter-ion effects because the salts were tested under different oxygen conditions. [src: counter_ion_effects]
- The corrected-conservation table gives cadmium an original-to-corrected core fraction of 0.522 → 0.422 against baseline 0.530, with delta -0.008 → -0.108 (n=92, 1 organism): its delta does not reverse sign despite the table label. Iron changes core fraction 0.778 → 1.000 against baseline 0.818 and delta -0.040 → +0.182 (n=9, 1 organism): its delta does reverse sign. This conflicts with the prose claim that only cadmium reverses. [src: counter_ion_effects]
- As literature context, the report cites Danilova et al. (2020) for a 2.5-fold CuSO₄-versus-CuCl₂ toxicity difference at 0.5 M; it contrasts this with typical random barcode transposon sequencing (RB-TnSeq) concentrations of 0.05–2 mM and infers smaller counter-ion effects there. [src: counter_ion_effects]
