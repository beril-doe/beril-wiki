---
type: "Finding"
description: "Of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources, 96 (47.8%) were assigned candidate genes with confidence scoring."
finding_id: "annotation_gap_discovery--d109c39d"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "96 (47.8%)", "what": "pairs assigned candidate genes with confidence scoring", "unit": "", "denominator": "201 gapfilled enzymatic reaction-organism pairs", "scope": "14 Fitness Browser organisms, 18 carbon sources"}]
caveat: "12 of 14 organisms are Proteobacteria, limiting generalizability."
first_added: "2026-11-24"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Nearly half of gapfilled reactions received candidate genes

Of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources, 96 (47.8%) were assigned candidate genes with confidence scoring. [src: annotation_gap_discovery]

## Key figures

- **96 (47.8%)**: pairs assigned candidate genes with confidence scoring (denominator 201 gapfilled enzymatic reaction-organism pairs; scope 14 Fitness Browser organisms, 18 carbon sources) [src: annotation_gap_discovery]

## Evidence

> Of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources, 96 (47.8%) were assigned candidate genes with confidence scoring. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

12 of 14 organisms are Proteobacteria, limiting generalizability. [src: annotation_gap_discovery]

> 7. **Phylogenetic bias**: 12 of 14 organisms are Proteobacteria, limiting generalizability. [src: annotation_gap_discovery]

## Other caveats in this report

- Dark reactions are known only by stoichiometry rather than enzyme classification, making sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]
- Exact GapMind-gapfilling concordance was limited because available KBase Data Lakehouse data report pathway step counts rather than individual step identities. [src: annotation_gap_discovery]
- The report describes zero wildtype growth in knockout validation as an expected limitation because the models need the gapfilled reactions themselves for growth on those carbon sources. [src: annotation_gap_discovery]
- Draft models built from automated RAST annotations contain systematic errors; the 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- Multiple valid gapfill solutions may exist for each false-negative case, and the report's default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]
