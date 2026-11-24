---
type: "Finding"
description: "Ortholog-transferred fitness data from the Fitness Browser (12,241 entries, 2,005 genes, 13 conditions) shows Complex I orthologs have significantly worse fitness on aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001)."
finding_id: "aromatic_catabolism_network--3128e9e3"
result: "observation"
source: "aromatic_catabolism_network"
quantities: [{"value": "-1.35", "what": "mean Complex I ortholog fitness on aromatic conditions", "unit": "", "denominator": "", "scope": ""}, {"value": "-0.77", "what": "mean Complex I ortholog fitness on non-aromatic conditions", "unit": "", "denominator": "", "scope": ""}, {"value": "p < 0.0001", "what": "Mann-Whitney test", "unit": "", "denominator": "", "scope": ""}]
caveat: "Ortholog-transferred fitness mixes signals from multiple Fitness Browser organisms with different respiratory chain architectures, so direct single-organism measurements on aromatics would be more definitive."
first_added: "2026-11-24"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Complex I orthologs are more defective on aromatics across Fitness Browser organisms

Ortholog-transferred fitness data from the Fitness Browser (12,241 entries, 2,005 genes, 13 conditions) shows Complex I orthologs have significantly worse fitness on aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001). [src: aromatic_catabolism_network]

## Key figures

- **-1.35**: mean Complex I ortholog fitness on aromatic conditions [src: aromatic_catabolism_network]
- **-0.77**: mean Complex I ortholog fitness on non-aromatic conditions [src: aromatic_catabolism_network]
- **p < 0.0001**: Mann-Whitney test [src: aromatic_catabolism_network]

## Evidence

> Ortholog-transferred fitness data from the Fitness Browser (12,241 entries, 2,005 genes, 13 conditions) shows Complex I orthologs have significantly worse fitness on aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001). [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

Ortholog-transferred fitness mixes signals from multiple Fitness Browser organisms with different respiratory chain architectures, so direct single-organism measurements on aromatics would be more definitive. [src: aromatic_catabolism_network]

> Ortholog-transferred fitness data mixes signals from multiple FB organisms with different respiratory chain architectures. Direct Complex I fitness measurements on aromatic substrates in a single organism would be more definitive. [src: aromatic_catabolism_network]

## Other caveats in this report

- In ADP1, 30/51 quinate-specific genes have no FBA reaction mappings, leaving cofactor supply chains and regulatory genes invisible to the metabolic model. [src: aromatic_catabolism_network]
- The report attributes the ADP1 FBA model's failure to identify the Complex I bottleneck to growth-rate optimization and redistribution of flux through alternative pathways. [src: aromatic_catabolism_network]
- The report states that loss of any Complex I subunit creates a complete-loss threshold effect that FBA's linear programming framework does not capture. [src: aromatic_catabolism_network]
- PQQ biosynthesis, iron acquisition, transcriptional regulation, and newly identified Complex I accessory factors lie outside the scope of the ADP1 FBA model. [src: aromatic_catabolism_network]
- The report identifies cofactor supply chains, iron homeostasis, and respiratory-chain capacity constraints as a specific class of metabolic-model incompleteness. [src: aromatic_catabolism_network]
