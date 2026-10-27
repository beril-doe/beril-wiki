---
type: "Finding"
description: "No convincing gene candidate was identified for 105 pairs (52.2%)."
finding_id: "annotation_gap_discovery--ccaed616"
result: "null result"
source: "annotation_gap_discovery"
quantities: [{"value": "105 (52.2%)", "what": "pairs left unresolved", "unit": "pairs", "denominator": "", "scope": ""}]
caveat: "Gene fitness significance depends on the chosen |fitness| threshold and number of experiments, and organisms with fewer carbon source experiments have less statistical power."
first_added: "2026-10-23"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Over half of gapfilled pairs remain without a convincing gene candidate

No convincing gene candidate was identified for 105 pairs (52.2%). [src: annotation_gap_discovery]

## Key figures

- **105 (52.2%) pairs**: pairs left unresolved [src: annotation_gap_discovery]

## Evidence

> - **Unresolved**: 105 pairs (52.2%) — no convincing gene candidate identified [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

Gene fitness significance depends on the chosen |fitness| threshold and number of experiments, and organisms with fewer carbon source experiments have less statistical power. [src: annotation_gap_discovery]

> 4. **Fitness threshold sensitivity**: Gene fitness significance depends on the chosen |fitness| threshold and number of experiments. Organisms with fewer carbon source experiments have less statistical power [src: annotation_gap_discovery]

## Other caveats in this report

- Thirty-three pairs (16.4%) had only single-stream, low-confidence support. [src: annotation_gap_discovery]
- The available GapMind output gives pathway step counts rather than individual step identities, limiting reaction-level concordance assessment. [src: annotation_gap_discovery]
- The Key Findings passage describes DIAMOND v2.1.16 blastp searches against 328 reviewed Swiss-Prot bacterial exemplars for 75/84 unique ECs, yielding 154 hits. Its stated search direction conflicts with the NB06 pipeline description. [src: annotation_gap_discovery]
- The NB06 pipeline passage instead says DIAMOND BLAST searched concatenated proteomes using 328 downloaded Swiss-Prot exemplars. The report leaves the search direction inconsistent with its Key Findings passage; both descriptions report 154 hits. [src: annotation_gap_discovery]
- The report labels baseline flux balance analysis across 574 combinations as 42.5% overall accuracy, gives recall as 86.5% (244 of 282) and precision as 42.5% (244 of 574), and reports 330 false positives. The repeated accuracy and precision value should not be silently treated as independently verified metrics. [src: annotation_gap_discovery]
