---
type: "Finding"
description: "In the bacterial pangenome core/accessory analysis, adaptive accessory clusters have median multi-copy rate 1.55%, 25\u00d7 higher than adaptive core clusters at 0.06% (Wilcoxon p = 5.96 \u00d7 10\u207b\u2078)."
finding_id: "gene_copy_number_variation--da7adcbb"
result: "observation"
source: "gene_copy_number_variation"
quantities: [{"value": "1.55%", "what": "median multi-copy rate of adaptive accessory clusters", "unit": "", "denominator": "", "scope": ""}, {"value": "0.06%", "what": "multi-copy rate of adaptive core clusters", "unit": "", "denominator": "", "scope": ""}, {"value": "25\u00d7", "what": "accessory to core ratio for adaptive clusters", "unit": "", "denominator": "", "scope": ""}]
caveat: "The report does not test direct positive selection on copy number; its results fit purifying selection against dosage imbalance, neutral tolerance plus some positive selection, or proximity to mobile elements."
first_added: "2026-11-24"
source_hash: "d13f78106dca898b743f95cd91a3768261ab5a3ffaa02907ebf80a0bbbf3d416"
---
# Adaptive accessory clusters carry most copy-number variation compared with adaptive core clusters

In the bacterial pangenome core/accessory analysis, adaptive accessory clusters have median multi-copy rate 1.55%, 25× higher than adaptive core clusters at 0.06% (Wilcoxon p = 5.96 × 10⁻⁸). [src: gene_copy_number_variation]

## Key figures

- **1.55%**: median multi-copy rate of adaptive accessory clusters [src: gene_copy_number_variation]
- **0.06%**: multi-copy rate of adaptive core clusters [src: gene_copy_number_variation]
- **25×**: accessory to core ratio for adaptive clusters [src: gene_copy_number_variation]

## Evidence

> **Adaptive accessory clusters** (median 1.55%) show **25× more** copy number variation than adaptive core clusters (0.06%; Wilcoxon p = 5.96 × 10⁻⁸). [src: gene_copy_number_variation]

From the report [[summaries/gene_copy_number_variation__REPORT]].

## Caveat

The report does not test direct positive selection on copy number; its results fit purifying selection against dosage imbalance, neutral tolerance plus some positive selection, or proximity to mobile elements. [src: gene_copy_number_variation]

> **We do not test for direct positive selection on copy number.** Our observations are consistent with either (a) purifying selection against dosage imbalance for housekeeping paralogs, or (b) neutral tolerance for adaptive paralogs plus positive selection on some of them, or (c) mechanistic bias (adaptive genes physically near mobile elements). [src: gene_copy_number_variation]

## Other caveats in this report

- The report says bacterial copy-number analyses should stratify by is_core before inferring functional constraint because an unstratified 8× class effect becomes 2× within core and 5× within accessory clusters. [src: gene_copy_number_variation]
- The report argues that defining bacterial housekeeping COGs as F and H is stricter than the textbook informational-versus-operational divide, because translation category J is intermediate rather than strictly dosage-constrained. [src: gene_copy_number_variation]
- The report warns that the binary multi-copy flag in bacterial pangenome data is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation]
- The report estimates ~80 min total for the 24-species pilot join and recommends CTS batch processing rather than a JupyterHub notebook loop for scaling to 100+ species. [src: gene_copy_number_variation]
- During bacterial pangenome extraction, background jupyter nbconvert execution of the long-running Spark loop died silently after ~1.5 hr, leaving the notebook unchanged and only an intermediate CSV written. [src: gene_copy_number_variation]
