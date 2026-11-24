---
type: "Finding"
description: "Within bacterial accessory clusters, adaptive clusters have multi-copy rate 1.55%, 5\u00d7 the housekeeping accessory rate of 0.29% (p = 3.3 \u00d7 10\u207b\u2076)."
finding_id: "gene_copy_number_variation--f45c10db"
result: "observation"
source: "gene_copy_number_variation"
quantities: [{"value": "1.55%", "what": "adaptive accessory multi-copy rate", "unit": "", "denominator": "", "scope": ""}, {"value": "0.29%", "what": "housekeeping accessory multi-copy rate", "unit": "", "denominator": "", "scope": ""}, {"value": "5\u00d7", "what": "adaptive to housekeeping ratio in accessory clusters", "unit": "", "denominator": "", "scope": ""}]
caveat: "If the L effect concentrates in IS elements, the story becomes transposition-mediated CNV rather than adaptive paralogy, which matters for the dosage-balance interpretation."
first_added: "2026-11-24"
source_hash: "d13f78106dca898b743f95cd91a3768261ab5a3ffaa02907ebf80a0bbbf3d416"
---
# Within accessory clusters the adaptive enrichment re-emerges

Within bacterial accessory clusters, adaptive clusters have multi-copy rate 1.55%, 5× the housekeeping accessory rate of 0.29% (p = 3.3 × 10⁻⁶). [src: gene_copy_number_variation]

## Key figures

- **1.55%**: adaptive accessory multi-copy rate [src: gene_copy_number_variation]
- **0.29%**: housekeeping accessory multi-copy rate [src: gene_copy_number_variation]
- **5×**: adaptive to housekeeping ratio in accessory clusters [src: gene_copy_number_variation]

## Evidence

> Within the accessory pool, the class effect re-emerges strongly: adaptive accessory (1.55%) is 5× housekeeping accessory (0.29%; p = 3.3 × 10⁻⁶). [src: gene_copy_number_variation]

From the report [[summaries/gene_copy_number_variation__REPORT]].

## Caveat

If the L effect concentrates in IS elements, the story becomes transposition-mediated CNV rather than adaptive paralogy, which matters for the dosage-balance interpretation. [src: gene_copy_number_variation]

> If the effect concentrates in IS elements, the story becomes "transposition-mediated CNV" rather than "adaptive paralogy". This distinction matters for the dosage-balance interpretation. [src: gene_copy_number_variation]

## Other caveats in this report

- The report says bacterial copy-number analyses should stratify by is_core before inferring functional constraint because an unstratified 8× class effect becomes 2× within core and 5× within accessory clusters. [src: gene_copy_number_variation]
- The report argues that defining bacterial housekeeping COGs as F and H is stricter than the textbook informational-versus-operational divide, because translation category J is intermediate rather than strictly dosage-constrained. [src: gene_copy_number_variation]
- The report warns that the binary multi-copy flag in bacterial pangenome data is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation]
- The report estimates ~80 min total for the 24-species pilot join and recommends CTS batch processing rather than a JupyterHub notebook loop for scaling to 100+ species. [src: gene_copy_number_variation]
- During bacterial pangenome extraction, background jupyter nbconvert execution of the long-running Spark loop died silently after ~1.5 hr, leaving the notebook unchanged and only an intermediate CSV written. [src: gene_copy_number_variation]
