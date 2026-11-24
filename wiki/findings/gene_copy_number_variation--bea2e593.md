---
type: "Finding"
description: "The bacterial species-level 8\u00d7 adaptive-versus-housekeeping effect collapses to 2\u00d7 when restricted to fixation-level clusters."
finding_id: "gene_copy_number_variation--bea2e593"
result: "correction"
source: "gene_copy_number_variation"
quantities: [{"value": "8\u00d7", "what": "species-level adaptive vs housekeeping effect", "unit": "", "denominator": "", "scope": ""}, {"value": "2\u00d7", "what": "effect among fixation-level clusters", "unit": "", "denominator": "", "scope": ""}]
caveat: "An unstratified 8\u00d7 class effect becomes a 2\u00d7 within-core effect and 5\u00d7 within-accessory effect, so copy-number analyses should stratify by is_core."
first_added: "2026-11-24"
source_hash: "d13f78106dca898b743f95cd91a3768261ab5a3ffaa02907ebf80a0bbbf3d416"
---
# Species-level class effect shrinks sharply once restricted to core clusters

The bacterial species-level 8× adaptive-versus-housekeeping effect collapses to 2× when restricted to fixation-level clusters. [src: gene_copy_number_variation]

## Key figures

- **8×**: species-level adaptive vs housekeeping effect [src: gene_copy_number_variation]
- **2×**: effect among fixation-level clusters [src: gene_copy_number_variation]

## Evidence

> The 8× species-level class effect reported in Finding 1 collapses to a 2× effect once we restrict to fixation-level clusters. [src: gene_copy_number_variation]

From the report [[summaries/gene_copy_number_variation__REPORT]].

## Caveat

An unstratified 8× class effect becomes a 2× within-core effect and 5× within-accessory effect, so copy-number analyses should stratify by is_core. [src: gene_copy_number_variation]

> Any future BERIL project analyzing copy number should stratify by `is_core` before drawing conclusions about functional constraint — an unstratified 8× class effect becomes a 2× within-core effect and 5× within-accessory effect. [src: gene_copy_number_variation]

## Other caveats in this report

- The report argues that defining bacterial housekeeping COGs as F and H is stricter than the textbook informational-versus-operational divide, because translation category J is intermediate rather than strictly dosage-constrained. [src: gene_copy_number_variation]
- The report warns that the binary multi-copy flag in bacterial pangenome data is dominated by rare clusters with a single accidental multi-copy occurrence. [src: gene_copy_number_variation]
- The report estimates ~80 min total for the 24-species pilot join and recommends CTS batch processing rather than a JupyterHub notebook loop for scaling to 100+ species. [src: gene_copy_number_variation]
- During bacterial pangenome extraction, background jupyter nbconvert execution of the long-running Spark loop died silently after ~1.5 hr, leaving the notebook unchanged and only an intermediate CSV written. [src: gene_copy_number_variation]
- Binary any-multi-copy flags underestimate the bacterial copy-number class effect by ~6× at pilot scale. [src: gene_copy_number_variation]
