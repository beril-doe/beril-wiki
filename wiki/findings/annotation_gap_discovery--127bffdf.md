---
type: "Finding"
description: "Only 8 of 50 dark reactions (16%) were resolved, compared to 88 of 151 (58.3%) for reactions with known EC numbers."
finding_id: "annotation_gap_discovery--127bffdf"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "8 of these 50 (16%)", "what": "dark reactions resolved", "unit": "", "denominator": "", "scope": ""}, {"value": "88 of 151 (58.3%)", "what": "reactions with known EC numbers resolved", "unit": "", "denominator": "", "scope": ""}]
caveat: "Dark reactions are known only by stoichiometry, not by enzyme classification, making both sequence homology searches and functional annotation cross-referencing far more difficult."
first_added: "2026-11-24"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Dark reactions without EC numbers are resolved far less often

Only 8 of 50 dark reactions (16%) were resolved, compared to 88 of 151 (58.3%) for reactions with known EC numbers. [src: annotation_gap_discovery]

## Key figures

- **8 of these 50 (16%)**: dark reactions resolved [src: annotation_gap_discovery]
- **88 of 151 (58.3%)**: reactions with known EC numbers resolved [src: annotation_gap_discovery]

## Evidence

> Only 8 of these 50 (16%) were resolved, compared to 88 of 151 (58.3%) for reactions with known EC numbers. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

Dark reactions are known only by stoichiometry, not by enzyme classification, making both sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]

> Dark reactions represent the hardest annotation gaps — their functions are known only by stoichiometry, not by enzyme classification, making both sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]

## Other caveats in this report

- Exact GapMind-gapfilling concordance was limited because available KBase Data Lakehouse data report pathway step counts rather than individual step identities. [src: annotation_gap_discovery]
- The report describes zero wildtype growth in knockout validation as an expected limitation because the models need the gapfilled reactions themselves for growth on those carbon sources. [src: annotation_gap_discovery]
- Draft models built from automated RAST annotations contain systematic errors; the 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- Multiple valid gapfill solutions may exist for each false-negative case, and the report's default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]
- The report manually mapped 109 Fitness Browser carbon source condition names to ModelSEED compound IDs, and mapping errors would produce spurious false negatives. [src: annotation_gap_discovery]
