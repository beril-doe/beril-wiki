---
type: "Finding"
description: "Co-fitness analysis assigns 44/51 genes (86%) to four functional subsystems: the core aromatic degradation pathway (8 genes), Complex I / NADH dehydrogenase (21 genes), iron acquisition (7 genes), and PQQ biosynthesis (2 genes), plus 6 transcriptional regulators."
finding_id: "aromatic_catabolism_network--8650ba38"
result: "observation"
source: "aromatic_catabolism_network"
quantities: [{"value": "44/51", "what": "quinate-specific genes assigned to functional subsystems by co-fitness", "unit": "genes", "denominator": "51 quinate-specific genes", "scope": "ADP1"}, {"value": "21", "what": "genes assigned to Complex I / NADH dehydrogenase", "unit": "genes", "denominator": "", "scope": "ADP1"}, {"value": "8", "what": "genes in the core aromatic degradation pathway", "unit": "genes", "denominator": "", "scope": "ADP1"}, {"value": "86%", "what": "fraction of quinate-specific genes assigned", "unit": "", "denominator": "51 quinate-specific genes", "scope": "ADP1"}]
caveat: "Co-fitness correlations use only 8 conditions (8-dimensional growth vectors), limiting the resolution of gene-gene correlations."
first_added: "2026-10-27"
source_hash: "68071594c6f00c685e2305ec838c11f3c31f6ef34c03cf0c699a64d106b027d6"
---
# Co-fitness assigns most quinate-specific genes to four support subsystems

Co-fitness analysis assigns 44/51 genes (86%) to four functional subsystems: the core aromatic degradation pathway (8 genes), Complex I / NADH dehydrogenase (21 genes), iron acquisition (7 genes), and PQQ biosynthesis (2 genes), plus 6 transcriptional regulators. [src: aromatic_catabolism_network]

## Key figures

- **44/51 genes**: quinate-specific genes assigned to functional subsystems by co-fitness (denominator 51 quinate-specific genes; scope ADP1) [src: aromatic_catabolism_network]
- **21 genes**: genes assigned to Complex I / NADH dehydrogenase (scope ADP1) [src: aromatic_catabolism_network]
- **8 genes**: genes in the core aromatic degradation pathway (scope ADP1) [src: aromatic_catabolism_network]
- **86%**: fraction of quinate-specific genes assigned (denominator 51 quinate-specific genes; scope ADP1) [src: aromatic_catabolism_network]

## Evidence

> Co-fitness analysis assigns 44/51 genes (86%) to four functional subsystems: the core aromatic degradation pathway (8 genes), Complex I / NADH dehydrogenase (21 genes), iron acquisition (7 genes), and PQQ biosynthesis (2 genes), plus 6 transcriptional regulators. [src: aromatic_catabolism_network]

From the report [[summaries/aromatic_catabolism_network__REPORT]].

## Caveat

Co-fitness correlations use only 8 conditions (8-dimensional growth vectors), limiting the resolution of gene-gene correlations. [src: aromatic_catabolism_network]

> - The co-fitness analysis uses only 8 conditions (8-dimensional growth vectors), limiting the resolution of gene-gene correlations. [src: aromatic_catabolism_network]

## Other caveats in this report

- NDH-2 compensation is proposed as a likely explanation for ADP1's apparent quinate specificity, not directly established here. [src: aromatic_catabolism_network]
- The report identifies growth-rate optimization and alternative flux routes as reasons the flux balance analysis model may miss a bottleneck. [src: aromatic_catabolism_network]
- The report argues that the model's linear framework misses the threshold effect of disabling a multisubunit Complex I. [src: aromatic_catabolism_network]
- The report interprets cross-species fitness as a high-TCA-flux rather than strictly aromatic Complex I dependency; its NDH-2 explanation remains inferential. [src: aromatic_catabolism_network]
- Cross-species ortholog-transferred fitness mixes organisms with different respiratory chains; the report lacks a definitive single-organism aromatic-substrate Complex I test. [src: aromatic_catabolism_network]
