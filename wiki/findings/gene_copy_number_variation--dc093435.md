---
type: "Finding"
description: "A binary any-multi-copy-in-\u22651-genome flag gave a 1.4\u00d7 effect in pilot NB01 cell 15, whereas cluster-carrier-weighted rate gave 3.3\u00d7 (NB01b, cell 9) and 8.1\u00d7 at scale (NB03, cell 6)."
finding_id: "gene_copy_number_variation--dc093435"
result: "correction"
source: "gene_copy_number_variation"
quantities: [{"value": "1.4\u00d7", "what": "effect with binary flag", "unit": "", "denominator": "", "scope": ""}, {"value": "3.3\u00d7", "what": "effect with carrier-weighted rate on pilot data", "unit": "", "denominator": "", "scope": ""}, {"value": "8.1\u00d7", "what": "effect with carrier-weighted rate at scale", "unit": "", "denominator": "", "scope": ""}]
caveat: "The binary flag is dominated by rare clusters with a single accidental multi-copy occurrence."
first_added: "2026-11-24"
source_hash: "d13f78106dca898b743f95cd91a3768261ab5a3ffaa02907ebf80a0bbbf3d416"
---
# Binary multi-copy flags understate the class effect compared with carrier-weighted rates

A binary any-multi-copy-in-≥1-genome flag gave a 1.4× effect in pilot NB01 cell 15, whereas cluster-carrier-weighted rate gave 3.3× (NB01b, cell 9) and 8.1× at scale (NB03, cell 6). [src: gene_copy_number_variation]

## Key figures

- **1.4×**: effect with binary flag [src: gene_copy_number_variation]
- **3.3×**: effect with carrier-weighted rate on pilot data [src: gene_copy_number_variation]
- **8.1×**: effect with carrier-weighted rate at scale [src: gene_copy_number_variation]

## Evidence

> A binary "any multi-copy in ≥1 genome" flag gave a 1.4× effect (pilot NB01, cell 15); the same data using cluster-carrier-weighted multi-copy rate (SUM(multicopy) / SUM(carriers)) gave a 3.3× effect (NB01b, cell 9) and a 8.1× effect at scale (NB03, cell 6). [src: gene_copy_number_variation]

From the report [[summaries/gene_copy_number_variation__REPORT]].

## Caveat

The binary flag is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation]

> The binary flag is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation]

## Other caveats in this report

- The report says bacterial copy-number analyses should stratify by is_core before inferring functional constraint because an unstratified 8× class effect becomes 2× within core and 5× within accessory clusters. [src: gene_copy_number_variation]
- The report argues that defining bacterial housekeeping COGs as F and H is stricter than the textbook informational-versus-operational divide, because translation category J is intermediate rather than strictly dosage-constrained. [src: gene_copy_number_variation]
- The report estimates ~80 min total for the 24-species pilot join and recommends CTS batch processing rather than a JupyterHub notebook loop for scaling to 100+ species. [src: gene_copy_number_variation]
- During bacterial pangenome extraction, background jupyter nbconvert execution of the long-running Spark loop died silently after ~1.5 hr, leaving the notebook unchanged and only an intermediate CSV written. [src: gene_copy_number_variation]
- Binary any-multi-copy flags underestimate the bacterial copy-number class effect by ~6× at pilot scale. [src: gene_copy_number_variation]
