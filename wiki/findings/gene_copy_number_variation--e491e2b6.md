---
type: "Finding"
description: "Across 24 bacterial species spanning 5 phyla with 50\u2013249 genomes each, adaptive COG categories L, V, M, K have higher cluster-carrier-weighted multi-copy rates than housekeeping categories F, H in 24 of 24 species, with median species-level ratio 8.14\u00d7 (paired Wilcoxon signed-rank, p = 5.96 \u00d7 10\u207b\u2078)."
finding_id: "gene_copy_number_variation--e491e2b6"
result: "observation"
source: "gene_copy_number_variation"
quantities: [{"value": "24 of 24 species", "what": "species with adaptive > housekeeping multi-copy rate", "unit": "", "denominator": "", "scope": ""}, {"value": "8.14\u00d7", "what": "median species-level ratio of adaptive to housekeeping rate", "unit": "", "denominator": "", "scope": ""}, {"value": "p = 5.96 \u00d7 10\u207b\u2078", "what": "paired Wilcoxon signed-rank p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Roughly 80% of clusters fall into \"other\" and are excluded from the primary test, so extrapolation to all bacterial genes is not automatic."
first_added: "2026-11-24"
source_hash: "d13f78106dca898b743f95cd91a3768261ab5a3ffaa02907ebf80a0bbbf3d416"
---
# Adaptive COG categories are multi-copy more often than housekeeping categories

Across 24 bacterial species spanning 5 phyla with 50–249 genomes each, adaptive COG categories L, V, M, K have higher cluster-carrier-weighted multi-copy rates than housekeeping categories F, H in 24 of 24 species, with median species-level ratio 8.14× (paired Wilcoxon signed-rank, p = 5.96 × 10⁻⁸). [src: gene_copy_number_variation]

## Key figures

- **24 of 24 species**: species with adaptive > housekeeping multi-copy rate [src: gene_copy_number_variation]
- **8.14×**: median species-level ratio of adaptive to housekeeping rate [src: gene_copy_number_variation]
- **p = 5.96 × 10⁻⁸**: paired Wilcoxon signed-rank p-value [src: gene_copy_number_variation]

## Evidence

> Across 24 bacterial species spanning 5 phyla (Pseudomonadota, Bacillota, Bacteroidota, Actinomycetota, Campylobacterota; 50–249 genomes each), the cluster-carrier-weighted multi-copy rate is systematically higher for adaptive COG categories (L, V, M, K) than for housekeeping categories (F, H). **24 of 24 species** show adaptive > housekeeping, with a **median species-level ratio of 8.14×** (paired Wilcoxon signed-rank, p = 5.96 × 10⁻⁸). [src: gene_copy_number_variation]

From the report [[summaries/gene_copy_number_variation__REPORT]].

## Caveat

Roughly 80% of clusters fall into "other" and are excluded from the primary test, so extrapolation to all bacterial genes is not automatic. [src: gene_copy_number_variation]

> Roughly 80% of clusters fall into "other" (poorly annotated, mixed, or intermediate function) and are excluded from the primary test. The class effect is real for the tested rows, but the extrapolation to "all bacterial genes" is not automatic. [src: gene_copy_number_variation]

## Other caveats in this report

- The report says bacterial copy-number analyses should stratify by is_core before inferring functional constraint because an unstratified 8× class effect becomes 2× within core and 5× within accessory clusters. [src: gene_copy_number_variation]
- The report argues that defining bacterial housekeeping COGs as F and H is stricter than the textbook informational-versus-operational divide, because translation category J is intermediate rather than strictly dosage-constrained. [src: gene_copy_number_variation]
- The report warns that the binary multi-copy flag in bacterial pangenome data is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation]
- The report estimates ~80 min total for the 24-species pilot join and recommends CTS batch processing rather than a JupyterHub notebook loop for scaling to 100+ species. [src: gene_copy_number_variation]
- During bacterial pangenome extraction, background jupyter nbconvert execution of the long-running Spark loop died silently after ~1.5 hr, leaving the notebook unchanged and only an intermediate CSV written. [src: gene_copy_number_variation]
