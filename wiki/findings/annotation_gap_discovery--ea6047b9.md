---
type: "Finding"
description: "BLAST homology was the single most impactful stream (34.8% alone), the full pipeline adds 13 percentage points over BLAST alone, and removing any single stream still keeps resolution above 36%."
finding_id: "annotation_gap_discovery--ea6047b9"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "34.8%", "what": "resolution by BLAST alone", "unit": "%", "denominator": "", "scope": ""}, {"value": "13 percentage points", "what": "gain of the full pipeline over BLAST alone", "unit": "percentage points", "denominator": "", "scope": ""}, {"value": "36%", "what": "resolution remains above this level after removing any single stream", "unit": "%", "denominator": "", "scope": ""}]
caveat: "The report describes the BLAST search direction inconsistently between the Key Findings and the NB06 pipeline description, although both report 154 hits."
first_added: "2026-10-23"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Integration outperforms BLAST alone, and no single stream removal collapses resolution

BLAST homology was the single most impactful stream (34.8% alone), the full pipeline adds 13 percentage points over BLAST alone, and removing any single stream still keeps resolution above 36%. [src: annotation_gap_discovery]

## Key figures

- **34.8%**: resolution by BLAST alone [src: annotation_gap_discovery]
- **13 percentage points**: gain of the full pipeline over BLAST alone [src: annotation_gap_discovery]
- **36%**: resolution remains above this level after removing any single stream [src: annotation_gap_discovery]

## Evidence

> BLAST homology was the single most impactful stream (34.8% alone), but the full pipeline adds 13 percentage points over BLAST alone. Removing any single stream still keeps resolution above 36%, demonstrating robustness. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

The report describes the BLAST search direction inconsistently between the Key Findings and the NB06 pipeline description, although both report 154 hits. [src: annotation_gap_discovery]

> 4. **NB06 — BLAST triangulation**: Downloaded 328 Swiss-Prot exemplar sequences for 75/84 unique ECs. DIAMOND BLAST against concatenated proteomes yielded 154 hits. Evidence triangulation with confidence scoring produced the final 96 resolved pairs (47.8%). [src: annotation_gap_discovery]

## Other caveats in this report

- Thirty-three pairs (16.4%) had only single-stream, low-confidence support. [src: annotation_gap_discovery]
- The available GapMind output gives pathway step counts rather than individual step identities, limiting reaction-level concordance assessment. [src: annotation_gap_discovery]
- The Key Findings passage describes DIAMOND v2.1.16 blastp searches against 328 reviewed Swiss-Prot bacterial exemplars for 75/84 unique ECs, yielding 154 hits. Its stated search direction conflicts with the NB06 pipeline description. [src: annotation_gap_discovery]
- The report labels baseline flux balance analysis across 574 combinations as 42.5% overall accuracy, gives recall as 86.5% (244 of 282) and precision as 42.5% (244 of 574), and reports 330 false positives. The repeated accuracy and precision value should not be silently treated as independently verified metrics. [src: annotation_gap_discovery]
- Automated draft-model errors and false-positive growth predictions limit interpretation of the reported 42.5% baseline FBA result. [src: annotation_gap_discovery]
