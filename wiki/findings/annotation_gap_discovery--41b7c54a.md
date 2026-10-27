---
type: "Finding"
description: "Although 23 GPR rules were inserted into SBML models for high/medium-confidence NB03 candidates, gene knockout simulation showed zero wildtype growth on minimal carbon source media, because the models require the gapfilled reactions themselves to grow on those carbon sources."
finding_id: "annotation_gap_discovery--41b7c54a"
result: "null result"
source: "annotation_gap_discovery"
quantities: [{"value": "23", "what": "GPR rules inserted into SBML models", "unit": "rules", "denominator": "", "scope": "high/medium-confidence NB03 candidates"}, {"value": "zero", "what": "wildtype growth on minimal carbon source media in knockout simulation", "unit": "", "denominator": "", "scope": ""}]
caveat: "Draft models built from automated RAST annotations contain systematic errors, and the 42.5% baseline FBA accuracy, dominated by false positives, reflects overly permissive models."
first_added: "2026-10-23"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Knockout simulation could not validate candidate gene assignments

Although 23 GPR rules were inserted into SBML models for high/medium-confidence NB03 candidates, gene knockout simulation showed zero wildtype growth on minimal carbon source media, because the models require the gapfilled reactions themselves to grow on those carbon sources. [src: annotation_gap_discovery]

## Key figures

- **23 rules**: GPR rules inserted into SBML models (scope high/medium-confidence NB03 candidates) [src: annotation_gap_discovery]
- **zero**: wildtype growth on minimal carbon source media in knockout simulation [src: annotation_gap_discovery]

## Evidence

> 5. **NB07 — Validation**: Inserted 23 GPR rules into SBML models for high/medium-confidence NB03 candidates. Gene knockout simulation showed zero wildtype growth on minimal carbon source media — an expected limitation because the models require the gapfilled reactions themselves to enable growth on those carbon sources. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

Draft models built from automated RAST annotations contain systematic errors, and the 42.5% baseline FBA accuracy, dominated by false positives, reflects overly permissive models. [src: annotation_gap_discovery]

> 1. **Model quality**: Draft models built from automated RAST annotations contain systematic errors. The 42.5% baseline FBA accuracy (dominated by false positives) reflects overly permissive models that predict growth on carbon sources the organisms cannot use [src: annotation_gap_discovery]

## Other caveats in this report

- Thirty-three pairs (16.4%) had only single-stream, low-confidence support. [src: annotation_gap_discovery]
- The available GapMind output gives pathway step counts rather than individual step identities, limiting reaction-level concordance assessment. [src: annotation_gap_discovery]
- The Key Findings passage describes DIAMOND v2.1.16 blastp searches against 328 reviewed Swiss-Prot bacterial exemplars for 75/84 unique ECs, yielding 154 hits. Its stated search direction conflicts with the NB06 pipeline description. [src: annotation_gap_discovery]
- The NB06 pipeline passage instead says DIAMOND BLAST searched concatenated proteomes using 328 downloaded Swiss-Prot exemplars. The report leaves the search direction inconsistent with its Key Findings passage; both descriptions report 154 hits. [src: annotation_gap_discovery]
- The report labels baseline flux balance analysis across 574 combinations as 42.5% overall accuracy, gives recall as 86.5% (244 of 282) and precision as 42.5% (244 of 574), and reports 330 false positives. The repeated accuracy and precision value should not be silently treated as independently verified metrics. [src: annotation_gap_discovery]
