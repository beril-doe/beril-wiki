---
type: "Finding"
description: "Complex I (NADH:ubiquinone oxidoreductase) accounts for 21 of 51 quinate-specific genes (41%), making it the dominant support requirement for aromatic catabolism."
finding_id: "aromatic_catabolism_network--09feb273"
result: "observation"
source: "aromatic_catabolism_network"
quantities: [{"value": "21 of 51", "what": "quinate-specific genes assigned to Complex I", "unit": "genes", "denominator": "51 quinate-specific genes", "scope": "Acinetobacter baylyi ADP1"}, {"value": "41%", "what": "share of quinate-specific genes in Complex I", "unit": "percent", "denominator": "51 quinate-specific genes", "scope": "ADP1"}]
caveat: "The categorization of Complex I-associated genes beyond the core nuo operon (the 11 co-fitness assignments) is based on phenotypic correlation only, and some may be indirect connections."
first_added: "2026-11-24"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Complex I dominates the support requirement for aromatic catabolism in ADP1

Complex I (NADH:ubiquinone oxidoreductase) accounts for 21 of 51 quinate-specific genes (41%), making it the dominant support requirement for aromatic catabolism. [src: aromatic_catabolism_network]

## Key figures

- **21 of 51 genes**: quinate-specific genes assigned to Complex I (denominator 51 quinate-specific genes; scope Acinetobacter baylyi ADP1) [src: aromatic_catabolism_network]
- **41%**: share of quinate-specific genes in Complex I (denominator 51 quinate-specific genes; scope ADP1) [src: aromatic_catabolism_network]

## Evidence

> Complex I (NADH:ubiquinone oxidoreductase) accounts for 21 of 51 quinate-specific genes (41%), making it the dominant support requirement for aromatic catabolism. [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

The categorization of Complex I-associated genes beyond the core nuo operon (the 11 co-fitness assignments) is based on phenotypic correlation only, and some may be indirect connections. [src: aromatic_catabolism_network]

> The categorization of "Complex I-associated" genes beyond the core nuo operon (the 11 co-fitness assignments) is based on phenotypic correlation only. Some may have indirect connections rather than physical association with Complex I. [src: aromatic_catabolism_network]

## Other caveats in this report

- In ADP1, 30/51 quinate-specific genes have no FBA reaction mappings, leaving cofactor supply chains and regulatory genes invisible to the metabolic model. [src: aromatic_catabolism_network]
- The report attributes the ADP1 FBA model's failure to identify the Complex I bottleneck to growth-rate optimization and redistribution of flux through alternative pathways. [src: aromatic_catabolism_network]
- The report states that loss of any Complex I subunit creates a complete-loss threshold effect that FBA's linear programming framework does not capture. [src: aromatic_catabolism_network]
- PQQ biosynthesis, iron acquisition, transcriptional regulation, and newly identified Complex I accessory factors lie outside the scope of the ADP1 FBA model. [src: aromatic_catabolism_network]
- The report identifies cofactor supply chains, iron homeostasis, and respiratory-chain capacity constraints as a specific class of metabolic-model incompleteness. [src: aromatic_catabolism_network]
