---
type: "Finding"
description: "Of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources, 96 (47.8%) were assigned candidate genes with confidence scoring, exceeding the pre-specified H1 threshold of 30%."
finding_id: "annotation_gap_discovery--fa3a9dc4"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "96 (47.8%)", "what": "pairs assigned candidate genes with confidence scoring", "unit": "pairs", "denominator": "201 gapfilled enzymatic reaction-organism pairs", "scope": "14 Fitness Browser organisms, 18 carbon sources"}, {"value": "30%", "what": "pre-specified H1 threshold", "unit": "", "denominator": "", "scope": ""}]
caveat: "Thirty-three pairs (16.4%) had only single-stream, low-confidence support."
first_added: "2026-10-23"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Integrated evidence assigned candidate genes to nearly half of gapfilled reactions

Of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources, 96 (47.8%) were assigned candidate genes with confidence scoring, exceeding the pre-specified H1 threshold of 30%. [src: annotation_gap_discovery]

## Key figures

- **96 (47.8%) pairs**: pairs assigned candidate genes with confidence scoring (denominator 201 gapfilled enzymatic reaction-organism pairs; scope 14 Fitness Browser organisms, 18 carbon sources) [src: annotation_gap_discovery]
- **30%**: pre-specified H1 threshold [src: annotation_gap_discovery]

## Evidence

> Of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources, 96 (47.8%) were assigned candidate genes with confidence scoring. This exceeds the pre-specified H1 threshold of 30%, supporting the hypothesis that integrating multiple evidence types can resolve a significant fraction of metabolic annotation gaps. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

Thirty-three pairs (16.4%) had only single-stream, low-confidence support. [src: annotation_gap_discovery]

> - **Low confidence**: 33 pairs (16.4%) — single evidence stream only [src: annotation_gap_discovery]

## Other caveats in this report

- The available GapMind output gives pathway step counts rather than individual step identities, limiting reaction-level concordance assessment. [src: annotation_gap_discovery]
- The Key Findings passage describes DIAMOND v2.1.16 blastp searches against 328 reviewed Swiss-Prot bacterial exemplars for 75/84 unique ECs, yielding 154 hits. Its stated search direction conflicts with the NB06 pipeline description. [src: annotation_gap_discovery]
- The NB06 pipeline passage instead says DIAMOND BLAST searched concatenated proteomes using 328 downloaded Swiss-Prot exemplars. The report leaves the search direction inconsistent with its Key Findings passage; both descriptions report 154 hits. [src: annotation_gap_discovery]
- The report labels baseline flux balance analysis across 574 combinations as 42.5% overall accuracy, gives recall as 86.5% (244 of 282) and precision as 42.5% (244 of 574), and reports 330 false positives. The repeated accuracy and precision value should not be silently treated as independently verified metrics. [src: annotation_gap_discovery]
- Automated draft-model errors and false-positive growth predictions limit interpretation of the reported 42.5% baseline FBA result. [src: annotation_gap_discovery]
