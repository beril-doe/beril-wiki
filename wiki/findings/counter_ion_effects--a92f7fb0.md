---
type: "Finding"
description: "Across 19 organisms and 14 metals (86 organism \u00d7 metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) are also important under NaCl stress."
finding_id: "counter_ion_effects--a92f7fb0"
result: "observation"
source: "counter_ion_effects"
quantities: [{"value": "39.8%", "what": "metal-important gene records also NaCl-important", "unit": "percent", "denominator": "10,821 metal-important gene records", "scope": "19 organisms, 14 metals"}, {"value": "4,304", "what": "records shared with NaCl stress", "unit": "records", "denominator": "10,821", "scope": "86 organism \u00d7 metal pairs"}]
caveat: "The 39.8% overlap depends on the NaCl-importance threshold (fit < -1 or n_sick \u2265 1); a stricter threshold would reduce overlap and a more permissive one would increase it."
first_added: "2026-11-24"
source_hash: "c43b2ab4f0d5dd44e987cc5bb413ebd72891a74a14ce45245be883ec2ca48807"
---
# Large share of metal fitness genes also matter under NaCl stress

Across 19 organisms and 14 metals (86 organism × metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) are also important under NaCl stress. [src: counter_ion_effects]

## Key figures

- **39.8%**: metal-important gene records also NaCl-important (denominator 10,821 metal-important gene records; scope 19 organisms, 14 metals) [src: counter_ion_effects]
- **4,304 records**: records shared with NaCl stress (denominator 10,821; scope 86 organism × metal pairs) [src: counter_ion_effects]

## Evidence

> Across 19 organisms and 14 metals (86 organism × metal pairs), 4,304 of 10,821 metal-important gene records (39.8%) are also important under NaCl stress. [src: counter_ion_effects]

From the report [[summaries/counter_ion_effects__REPORT]].

## Caveat

The 39.8% overlap depends on the NaCl-importance threshold (fit < -1 or n_sick ≥ 1); a stricter threshold would reduce overlap and a more permissive one would increase it. [src: counter_ion_effects]

> - **Threshold sensitivity**: The 39.8% overlap depends on the NaCl-importance threshold (fit < -1 or n_sick ≥ 1). A stricter threshold would reduce overlap; a more permissive one would increase it. [src: counter_ion_effects]

## Other caveats in this report

- Synechococcus elongatus (SynE) was a shared-stress outlier at 88.6% (565/638 genes), driven by 12 NaCl dose-response experiments spanning 0.5–250 mM, compared with 1–6 NaCl experiments for other organisms. [src: counter_ion_effects]
- The n_sick >= 1 threshold was easier to satisfy for SynE because it had 12 experiments. [src: counter_ion_effects]
- The cadmium enrichment analysis had very low statistical power because it included only 92 original genes from 1 organism. [src: counter_ion_effects]
- The psRCH2 copper salt comparison was severely confounded by aerobic versus anaerobic growth, with hundreds of genes differing independently of copper. [src: counter_ion_effects]
- The report warns that corrected enrichment deltas for cadmium (n=92) and iron (n=9), each from a single organism, are statistically unreliable because of very low gene counts. [src: counter_ion_effects]
