---
type: "Finding"
description: "The FBA knockout validation was inconclusive because the models cannot grow on carbon source minimal media without the gapfilled reactions, making single-gene knockout analysis circular in this context."
finding_id: "annotation_gap_discovery--6aeabeda"
result: "null result"
source: "annotation_gap_discovery"
quantities: []
caveat: "Zero wildtype growth in knockout simulation is an expected limitation because the models require the gapfilled reactions themselves to enable growth on those carbon sources."
first_added: "2026-11-24"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Knockout validation was inconclusive because of circularity

The FBA knockout validation was inconclusive because the models cannot grow on carbon source minimal media without the gapfilled reactions, making single-gene knockout analysis circular in this context. [src: annotation_gap_discovery]

## Evidence

> 6. **Gene knockout simulation**: The FBA knockout validation was inconclusive because the models cannot grow on carbon source minimal media without the gapfilled reactions — the gapfilled reactions are themselves required to enable growth, making single-gene knockout analysis circular in this context [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

Zero wildtype growth in knockout simulation is an expected limitation because the models require the gapfilled reactions themselves to enable growth on those carbon sources. [src: annotation_gap_discovery]

> Gene knockout simulation showed zero wildtype growth on minimal carbon source media — an expected limitation because the models require the gapfilled reactions themselves to enable growth on those carbon sources. [src: annotation_gap_discovery]

## Other caveats in this report

- Dark reactions are known only by stoichiometry rather than enzyme classification, making sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]
- Exact GapMind-gapfilling concordance was limited because available KBase Data Lakehouse data report pathway step counts rather than individual step identities. [src: annotation_gap_discovery]
- Draft models built from automated RAST annotations contain systematic errors; the 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- Multiple valid gapfill solutions may exist for each false-negative case, and the report's default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]
- The report manually mapped 109 Fitness Browser carbon source condition names to ModelSEED compound IDs, and mapping errors would produce spurious false negatives. [src: annotation_gap_discovery]
