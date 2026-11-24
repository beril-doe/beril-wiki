---
type: "Finding"
description: "Per-condition analysis reveals that the largest Complex I defects relative to background are on acetate (-1.55) and succinate (-1.39) \u2014 non-aromatic substrates that also generate high NADH flux through the TCA cycle."
finding_id: "aromatic_catabolism_network--3a51f6c6"
result: "correction"
source: "aromatic_catabolism_network"
quantities: [{"value": "-1.55", "what": "Complex I defect on acetate relative to background", "unit": "", "denominator": "", "scope": ""}, {"value": "-1.39", "what": "Complex I defect on succinate relative to background", "unit": "", "denominator": "", "scope": ""}]
caveat: "Ortholog-transferred fitness mixes signals from multiple Fitness Browser organisms with different respiratory chain architectures, so direct single-organism measurements would be more definitive."
first_added: "2026-11-24"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Complex I defects are largest on non-aromatic high-NADH substrates

Per-condition analysis reveals that the largest Complex I defects relative to background are on acetate (-1.55) and succinate (-1.39) — non-aromatic substrates that also generate high NADH flux through the TCA cycle. [src: aromatic_catabolism_network]

## Key figures

- **-1.55**: Complex I defect on acetate relative to background [src: aromatic_catabolism_network]
- **-1.39**: Complex I defect on succinate relative to background [src: aromatic_catabolism_network]

## Evidence

> However, per-condition analysis reveals that the largest Complex I defects relative to background are on acetate (-1.55) and succinate (-1.39) — non-aromatic substrates that also generate high NADH flux through the TCA cycle. [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

Ortholog-transferred fitness mixes signals from multiple Fitness Browser organisms with different respiratory chain architectures, so direct single-organism measurements would be more definitive. [src: aromatic_catabolism_network]

> Ortholog-transferred fitness data mixes signals from multiple FB organisms with different respiratory chain architectures. Direct Complex I fitness measurements on aromatic substrates in a single organism would be more definitive. [src: aromatic_catabolism_network]

## Other caveats in this report

- In ADP1, 30/51 quinate-specific genes have no FBA reaction mappings, leaving cofactor supply chains and regulatory genes invisible to the metabolic model. [src: aromatic_catabolism_network]
- The report attributes the ADP1 FBA model's failure to identify the Complex I bottleneck to growth-rate optimization and redistribution of flux through alternative pathways. [src: aromatic_catabolism_network]
- The report states that loss of any Complex I subunit creates a complete-loss threshold effect that FBA's linear programming framework does not capture. [src: aromatic_catabolism_network]
- PQQ biosynthesis, iron acquisition, transcriptional regulation, and newly identified Complex I accessory factors lie outside the scope of the ADP1 FBA model. [src: aromatic_catabolism_network]
- The report identifies cofactor supply chains, iron homeostasis, and respiratory-chain capacity constraints as a specific class of metabolic-model incompleteness. [src: aromatic_catabolism_network]
