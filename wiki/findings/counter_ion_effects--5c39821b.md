---
type: "Finding"
description: "In DvH (13 metals, 6 NaCl experiments), whole-genome fitness correlations with NaCl ranged from zinc (r=0.715) to iron (r=0.086); zinc ranked first despite sulfate delivery with zero Cl\u207b, and the report infers that the hierarchy follows toxicity mechanism rather than chloride concentration."
finding_id: "counter_ion_effects--5c39821b"
result: "inference"
source: "counter_ion_effects"
quantities: [{"value": "r=0.715", "what": "zinc whole-genome fitness correlation with NaCl", "unit": "", "denominator": "", "scope": "DvH"}, {"value": "0.086", "what": "iron correlation with NaCl (lowest)", "unit": "", "denominator": "", "scope": "DvH"}, {"value": "0.545", "what": "manganese correlation with NaCl", "unit": "", "denominator": "", "scope": "DvH"}]
caveat: "Manganese, cadmium, selenium, mercury, iron, molybdenum and tungsten were each tested in only one organism, DvH, so their statistics lack cross-organism replication."
first_added: "2026-10-27"
source_hash: "c43b2ab4f0d5dd44e987cc5bb413ebd72891a74a14ce45245be883ec2ca48807"
---
# DvH metal–NaCl fitness correlations vary widely; report attributes this to toxicity mechanism

In DvH (13 metals, 6 NaCl experiments), whole-genome fitness correlations with NaCl ranged from zinc (r=0.715) to iron (r=0.086); zinc ranked first despite sulfate delivery with zero Cl⁻, and the report infers that the hierarchy follows toxicity mechanism rather than chloride concentration. [src: counter_ion_effects]

## Key figures

- **r=0.715**: zinc whole-genome fitness correlation with NaCl (scope DvH) [src: counter_ion_effects]
- **0.086**: iron correlation with NaCl (lowest) (scope DvH) [src: counter_ion_effects]
- **0.545**: manganese correlation with NaCl (scope DvH) [src: counter_ion_effects]

## Evidence

> In DvH (the most extensively profiled organism: 13 metals, 6 NaCl experiments), whole-genome fitness correlations between each metal and NaCl reveal a hierarchy: Zinc (r=0.715) > Manganese (0.545) > Copper (0.532) > Cobalt (0.498) > Mercury (0.478) > Nickel (0.446) > Aluminum (0.420) > Molybdenum (0.396) > Uranium (0.350) > Selenium (0.342) > Chromium (0.318) > Tungsten (0.298) > Iron (0.086). This hierarchy does not follow Cl⁻ concentration (zinc is delivered as sulfate with zero Cl⁻ but ranks first). Instead, it follows toxicity mechanism: metals that broadly displace essential cofactors (Zn, Mn, Cu, Co) share more genes with NaCl stress than metals that target specific pathways (Mo, W — molybdopterin enzymes; Fe — iron-sulfur clusters). [src: counter_ion_effects]

From the report [[summaries/counter_ion_effects__REPORT]].

## Caveat

Manganese, cadmium, selenium, mercury, iron, molybdenum and tungsten were each tested in only one organism, DvH, so their statistics lack cross-organism replication. [src: counter_ion_effects]

> - **Single-organism metals**: Manganese, cadmium, selenium, mercury, iron, molybdenum, and tungsten are tested in only 1 organism (DvH). Their overlap statistics have no cross-organism replication. [src: counter_ion_effects]

## Other caveats in this report

- Synechococcus elongatus (SynE) had 88.6% shared-stress genes (565/638) and 12 NaCl experiments spanning 0.5–250 mM, versus 1–6 experiments elsewhere. Excluding it reduced pooled overlap from 39.8% to 36.7% (3,739/10,183); the n_sick >= 1 rule is easier to meet with more experiments. [src: counter_ion_effects]
- The narrative says core enrichment was preserved for 12 of 14 metals and that only cadmium reversed. It reports increased deltas for molybdenum (+0.132 → +0.145), tungsten (+0.129 → +0.134), mercury (+0.116 → +0.133), and selenium (+0.115 → +0.131), but decreased deltas for aluminum (+0.099 → +0.068) and zinc (+0.145 → +0.115). Its reversal wording conflicts with the corrected-conservation table: cadmium remains negative, while iron changes sign. [src: counter_ion_effects]
- The psRCH2 copper-salt comparison cannot isolate counter-ion effects because the salts were tested under different oxygen conditions. [src: counter_ion_effects]
- The corrected-conservation table gives cadmium an original-to-corrected core fraction of 0.522 → 0.422 against baseline 0.530, with delta -0.008 → -0.108 (n=92, 1 organism): its delta does not reverse sign despite the table label. Iron changes core fraction 0.778 → 1.000 against baseline 0.818 and delta -0.040 → +0.182 (n=9, 1 organism): its delta does reverse sign. This conflicts with the prose claim that only cadmium reverses. [src: counter_ion_effects]
- As literature context, the report cites Danilova et al. (2020) for a 2.5-fold CuSO₄-versus-CuCl₂ toxicity difference at 0.5 M; it contrasts this with typical random barcode transposon sequencing (RB-TnSeq) concentrations of 0.05–2 mM and infers smaller counter-ion effects there. [src: counter_ion_effects]
