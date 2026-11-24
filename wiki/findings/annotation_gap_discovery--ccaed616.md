---
type: "Finding"
description: "Unresolved: 105 pairs (52.2%) had no convincing gene candidate identified."
finding_id: "annotation_gap_discovery--ccaed616"
result: "null result"
source: "annotation_gap_discovery"
quantities: [{"value": "105 pairs (52.2%)", "what": "unresolved pairs", "unit": "", "denominator": "", "scope": ""}]
caveat: "GapMind covers ~80 carbon and amino acid pathways, not full metabolism, and many gapfilled reactions fall outside its coverage."
first_added: "2026-11-24"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Over half of gap pairs have no convincing gene candidate

Unresolved: 105 pairs (52.2%) had no convincing gene candidate identified. [src: annotation_gap_discovery]

## Key figures

- **105 pairs (52.2%)**: unresolved pairs [src: annotation_gap_discovery]

## Evidence

> - **Unresolved**: 105 pairs (52.2%) — no convincing gene candidate identified [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

GapMind covers ~80 carbon and amino acid pathways, not full metabolism, and many gapfilled reactions fall outside its coverage. [src: annotation_gap_discovery]

> 5. **GapMind scope**: GapMind covers ~80 carbon and amino acid pathways, not full metabolism. Many gapfilled reactions fall outside GapMind's pathway coverage [src: annotation_gap_discovery]

## Other caveats in this report

- Dark reactions are known only by stoichiometry rather than enzyme classification, making sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]
- Exact GapMind-gapfilling concordance was limited because available KBase Data Lakehouse data report pathway step counts rather than individual step identities. [src: annotation_gap_discovery]
- The report describes zero wildtype growth in knockout validation as an expected limitation because the models need the gapfilled reactions themselves for growth on those carbon sources. [src: annotation_gap_discovery]
- Draft models built from automated RAST annotations contain systematic errors; the 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- Multiple valid gapfill solutions may exist for each false-negative case, and the report's default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]
