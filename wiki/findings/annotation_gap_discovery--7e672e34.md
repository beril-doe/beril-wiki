---
type: "Finding"
description: "BLAST homology was the single most impactful stream (34.8% alone), but the full pipeline adds 13 percentage points over BLAST alone."
finding_id: "annotation_gap_discovery--7e672e34"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "34.8%", "what": "resolution by BLAST alone", "unit": "", "denominator": "", "scope": ""}, {"value": "13 percentage points", "what": "gain of full pipeline over BLAST alone", "unit": "", "denominator": "", "scope": ""}]
caveat: "Multiple valid gapfill solutions may exist for each false-negative case, and the default ModelSEED gapfilling minimizes added reactions but does not guarantee biological optimality."
first_added: "2026-11-24"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# BLAST homology is the strongest single evidence stream but not sufficient

BLAST homology was the single most impactful stream (34.8% alone), but the full pipeline adds 13 percentage points over BLAST alone. [src: annotation_gap_discovery]

## Key figures

- **34.8%**: resolution by BLAST alone [src: annotation_gap_discovery]
- **13 percentage points**: gain of full pipeline over BLAST alone [src: annotation_gap_discovery]

## Evidence

> BLAST homology was the single most impactful stream (34.8% alone), but the full pipeline adds 13 percentage points over BLAST alone. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

Multiple valid gapfill solutions may exist for each false-negative case, and the default ModelSEED gapfilling minimizes added reactions but does not guarantee biological optimality. [src: annotation_gap_discovery]

> 2. **Gapfilling non-uniqueness**: Multiple valid gapfill solutions may exist for each false-negative case. We used the default ModelSEED gapfilling, which minimizes the number of added reactions but does not guarantee biological optimality [src: annotation_gap_discovery]

## Other caveats in this report

- Dark reactions are known only by stoichiometry rather than enzyme classification, making sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]
- Exact GapMind-gapfilling concordance was limited because available KBase Data Lakehouse data report pathway step counts rather than individual step identities. [src: annotation_gap_discovery]
- The report describes zero wildtype growth in knockout validation as an expected limitation because the models need the gapfilled reactions themselves for growth on those carbon sources. [src: annotation_gap_discovery]
- Draft models built from automated RAST annotations contain systematic errors; the 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- The report manually mapped 109 Fitness Browser carbon source condition names to ModelSEED compound IDs, and mapping errors would produce spurious false negatives. [src: annotation_gap_discovery]
