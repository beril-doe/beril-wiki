---
type: "Finding"
description: "The FBA model captures 1.76\u00d7 higher Complex I flux on aromatic substrates (0.55 vs 0.31), but predicts 0% essentiality \u2014 it sees the increased demand but not the bottleneck."
finding_id: "aromatic_catabolism_network--7d6bd2aa"
result: "null result"
source: "aromatic_catabolism_network"
quantities: [{"value": "1.76\u00d7", "what": "higher predicted Complex I flux on aromatic substrates", "unit": "", "denominator": "", "scope": ""}, {"value": "0%", "what": "predicted Complex I essentiality", "unit": "", "denominator": "", "scope": ""}]
caveat: "30/51 quinate-specific genes have no FBA reaction mappings at all, so cofactor supply chains (PQQ, iron) and regulatory genes are invisible to the metabolic model."
first_added: "2026-11-24"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# FBA predicts no Complex I essentiality despite higher flux

The FBA model captures 1.76× higher Complex I flux on aromatic substrates (0.55 vs 0.31), but predicts 0% essentiality — it sees the increased demand but not the bottleneck. [src: aromatic_catabolism_network]

## Key figures

- **1.76×**: higher predicted Complex I flux on aromatic substrates [src: aromatic_catabolism_network]
- **0%**: predicted Complex I essentiality [src: aromatic_catabolism_network]

## Evidence

> The FBA model captures 1.76× higher Complex I flux on aromatic substrates (0.55 vs 0.31), but predicts 0% essentiality — it sees the increased demand but not the bottleneck. [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

30/51 quinate-specific genes have no FBA reaction mappings at all, so cofactor supply chains (PQQ, iron) and regulatory genes are invisible to the metabolic model. [src: aromatic_catabolism_network]

> Furthermore, 30/51 quinate-specific genes have no FBA reaction mappings at all — cofactor supply chains (PQQ, iron) and regulatory genes are invisible to the metabolic model. [src: aromatic_catabolism_network]

## Other caveats in this report

- The report attributes the ADP1 FBA model's failure to identify the Complex I bottleneck to growth-rate optimization and redistribution of flux through alternative pathways. [src: aromatic_catabolism_network]
- The report states that loss of any Complex I subunit creates a complete-loss threshold effect that FBA's linear programming framework does not capture. [src: aromatic_catabolism_network]
- PQQ biosynthesis, iron acquisition, transcriptional regulation, and newly identified Complex I accessory factors lie outside the scope of the ADP1 FBA model. [src: aromatic_catabolism_network]
- The report identifies cofactor supply chains, iron homeostasis, and respiratory-chain capacity constraints as a specific class of metabolic-model incompleteness. [src: aromatic_catabolism_network]
- The ADP1 co-fitness analysis uses only 8 conditions and 8-dimensional growth vectors, limiting gene-gene correlation resolution. [src: aromatic_catabolism_network]
