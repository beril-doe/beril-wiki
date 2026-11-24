---
type: "Finding"
description: "Across 22 organisms and 14 metals, genes with significant fitness defects under metal stress are 87.4% core vs 76.9% baseline (OR=2.08, p=4.3e-162)."
finding_id: "metal_fitness_atlas--7bedd365"
result: "observation"
source: "metal_fitness_atlas"
quantities: [{"value": "87.4%", "what": "core fraction of genes with significant metal-stress fitness defects", "unit": "percent", "denominator": "", "scope": "22 organisms, 14 metals"}, {"value": "76.9%", "what": "baseline core fraction", "unit": "percent", "denominator": "", "scope": ""}, {"value": "OR=2.08", "what": "odds ratio of core enrichment", "unit": "", "denominator": "", "scope": ""}]
caveat: "Metal-important genes are defined broadly (fit < -1 OR n_sick \u2265 1, capturing ~3.3% of genes), and most are general stress genes rather than metal-specific."
first_added: "2026-11-24"
source_hash: "9ea58c19144575c5e8a783b777863269a18b37241d89bb6c0a9c2a044de1353d"
---
# Metal-stress fitness genes are enriched in the core genome

Across 22 organisms and 14 metals, genes with significant fitness defects under metal stress are 87.4% core vs 76.9% baseline (OR=2.08, p=4.3e-162). [src: metal_fitness_atlas]

## Key figures

- **87.4%**: core fraction of genes with significant metal-stress fitness defects (scope 22 organisms, 14 metals) [src: metal_fitness_atlas]
- **76.9%**: baseline core fraction [src: metal_fitness_atlas]
- **OR=2.08**: odds ratio of core enrichment [src: metal_fitness_atlas]

## Evidence

> Across 22 organisms and 14 metals, genes with significant fitness defects under metal stress are **87.4% core** vs 76.9% baseline (OR=2.08, p=4.3e-162). [src: metal_fitness_atlas]

From the report [[summaries/metal_fitness_atlas__REPORT]].

## Caveat

Metal-important genes are defined broadly (fit < -1 OR n_sick ≥ 1, capturing ~3.3% of genes), and most are general stress genes rather than metal-specific. [src: metal_fitness_atlas]

> - **Metal-important definition is broad**: fit < -1 OR n_sick ≥ 1 captures ~3.3% of genes, most of which are general stress genes rather than metal-specific. [src: metal_fitness_atlas]

## Other caveats in this report

- The atlas conservation analysis covers 22 of 31 metal-tested organisms (71%). [src: metal_fitness_atlas]
- The 9 organisms excluded from atlas conservation analysis—Putida, Keio, SynE, Miya, Kang, BFirm, Cola, Ponti, and Dino—lack Fitness Browser–pangenome links. [src: metal_fitness_atlas]
- The report considers systematic bias from excluded organisms unlikely because they are taxonomically diverse. [src: metal_fitness_atlas]
- The atlas's functional predictions for unknown genes are based solely on cross-species fitness data. [src: metal_fitness_atlas]
- Without normalization, species with large open pangenomes such as K. pneumoniae and P. aeruginosa dominate atlas metal scores, reflecting genome size rather than metal biology. [src: metal_fitness_atlas]
