---
type: "Finding"
description: "This analysis reveals that aromatic catabolism requires 51 genes \u2014 over 8\u00d7 the core pathway \u2014 organized into 4 biochemically rational subsystems."
finding_id: "aromatic_catabolism_network--117d1659"
result: "observation"
source: "aromatic_catabolism_network"
quantities: [{"value": "51", "what": "genes required for aromatic catabolism", "unit": "genes", "denominator": "", "scope": "ADP1 quinate-specific genes"}, {"value": "over 8\u00d7", "what": "size relative to the core pathway", "unit": "", "denominator": "", "scope": ""}, {"value": "4", "what": "biochemically rational subsystems", "unit": "subsystems", "denominator": "", "scope": ""}]
caveat: "The co-fitness analysis uses only 8 conditions (8-dimensional growth vectors), limiting the resolution of gene-gene correlations."
first_added: "2026-11-24"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Aromatic catabolism needs far more genes than the core pathway

This analysis reveals that aromatic catabolism requires 51 genes — over 8× the core pathway — organized into 4 biochemically rational subsystems. [src: aromatic_catabolism_network]

## Key figures

- **51 genes**: genes required for aromatic catabolism (scope ADP1 quinate-specific genes) [src: aromatic_catabolism_network]
- **over 8×**: size relative to the core pathway [src: aromatic_catabolism_network]
- **4 subsystems**: biochemically rational subsystems [src: aromatic_catabolism_network]

## Evidence

> This analysis reveals that aromatic catabolism requires 51 genes — over 8× the core pathway — organized into 4 biochemically rational subsystems. [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

The co-fitness analysis uses only 8 conditions (8-dimensional growth vectors), limiting the resolution of gene-gene correlations. [src: aromatic_catabolism_network]

> The co-fitness analysis uses only 8 conditions (8-dimensional growth vectors), limiting the resolution of gene-gene correlations. [src: aromatic_catabolism_network]

## Other caveats in this report

- In ADP1, 30/51 quinate-specific genes have no FBA reaction mappings, leaving cofactor supply chains and regulatory genes invisible to the metabolic model. [src: aromatic_catabolism_network]
- The report attributes the ADP1 FBA model's failure to identify the Complex I bottleneck to growth-rate optimization and redistribution of flux through alternative pathways. [src: aromatic_catabolism_network]
- The report states that loss of any Complex I subunit creates a complete-loss threshold effect that FBA's linear programming framework does not capture. [src: aromatic_catabolism_network]
- PQQ biosynthesis, iron acquisition, transcriptional regulation, and newly identified Complex I accessory factors lie outside the scope of the ADP1 FBA model. [src: aromatic_catabolism_network]
- The report identifies cofactor supply chains, iron homeostasis, and respiratory-chain capacity constraints as a specific class of metabolic-model incompleteness. [src: aromatic_catabolism_network]
