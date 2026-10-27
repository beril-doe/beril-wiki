---
type: "Finding"
description: "Of 201 gapfilled reactions, 50 (24.9%) had no EC number assigned by ModelSEED (\"dark reactions\"), and only 8 of these 50 (16%) were resolved, compared to 88 of 151 (58.3%) for reactions with known EC numbers."
finding_id: "annotation_gap_discovery--61f3d4be"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "8 of 50 (16%)", "what": "dark reactions resolved", "unit": "reactions", "denominator": "50 EC-less reactions", "scope": ""}, {"value": "88 of 151 (58.3%)", "what": "reactions with known EC numbers resolved", "unit": "reactions", "denominator": "151 reactions with EC numbers", "scope": ""}, {"value": "50 (24.9%)", "what": "gapfilled reactions with no EC number", "unit": "reactions", "denominator": "201 gapfilled reactions", "scope": ""}]
caveat: "The default ModelSEED gapfilling minimizes the number of added reactions but does not guarantee biological optimality, so multiple valid gapfill solutions may exist."
first_added: "2026-10-23"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Dark reactions without EC numbers are far harder to resolve

Of 201 gapfilled reactions, 50 (24.9%) had no EC number assigned by ModelSEED ("dark reactions"), and only 8 of these 50 (16%) were resolved, compared to 88 of 151 (58.3%) for reactions with known EC numbers. [src: annotation_gap_discovery]

## Key figures

- **8 of 50 (16%) reactions**: dark reactions resolved (denominator 50 EC-less reactions) [src: annotation_gap_discovery]
- **88 of 151 (58.3%) reactions**: reactions with known EC numbers resolved (denominator 151 reactions with EC numbers) [src: annotation_gap_discovery]
- **50 (24.9%) reactions**: gapfilled reactions with no EC number (denominator 201 gapfilled reactions) [src: annotation_gap_discovery]

## Evidence

> Of 201 gapfilled reactions, 50 (24.9%) had no EC number assigned by ModelSEED ("dark reactions"). Only 8 of these 50 (16%) were resolved, compared to 88 of 151 (58.3%) for reactions with known EC numbers. Dark reactions represent the hardest annotation gaps — their functions are known only by stoichiometry, not by enzyme classification, making both sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

The default ModelSEED gapfilling minimizes the number of added reactions but does not guarantee biological optimality, so multiple valid gapfill solutions may exist. [src: annotation_gap_discovery]

> 2. **Gapfilling non-uniqueness**: Multiple valid gapfill solutions may exist for each false-negative case. We used the default ModelSEED gapfilling, which minimizes the number of added reactions but does not guarantee biological optimality [src: annotation_gap_discovery]

## Other caveats in this report

- Thirty-three pairs (16.4%) had only single-stream, low-confidence support. [src: annotation_gap_discovery]
- The available GapMind output gives pathway step counts rather than individual step identities, limiting reaction-level concordance assessment. [src: annotation_gap_discovery]
- The Key Findings passage describes DIAMOND v2.1.16 blastp searches against 328 reviewed Swiss-Prot bacterial exemplars for 75/84 unique ECs, yielding 154 hits. Its stated search direction conflicts with the NB06 pipeline description. [src: annotation_gap_discovery]
- The NB06 pipeline passage instead says DIAMOND BLAST searched concatenated proteomes using 328 downloaded Swiss-Prot exemplars. The report leaves the search direction inconsistent with its Key Findings passage; both descriptions report 154 hits. [src: annotation_gap_discovery]
- The report labels baseline flux balance analysis across 574 combinations as 42.5% overall accuracy, gives recall as 86.5% (244 of 282) and precision as 42.5% (244 of 574), and reports 330 false positives. The repeated accuracy and precision value should not be silently treated as independently verified metrics. [src: annotation_gap_discovery]
