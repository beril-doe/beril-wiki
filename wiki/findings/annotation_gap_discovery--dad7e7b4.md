---
type: "Finding"
description: "Resolution rates ranged from 20% (Bacteroides thetaiotaomicron) to 71% (Klebsiella michiganensis)."
finding_id: "annotation_gap_discovery--dad7e7b4"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "20%", "what": "resolution rate in Bacteroides thetaiotaomicron", "unit": "", "denominator": "", "scope": ""}, {"value": "71%", "what": "resolution rate in Klebsiella michiganensis", "unit": "", "denominator": "", "scope": ""}]
caveat: "The sole Bacteroidetes (B. thetaiotaomicron) had the lowest resolution rate, suggesting the approach may be less effective for phylogenetically distant clades with divergent metabolism."
first_added: "2026-11-24"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Resolution varied widely across organisms, lowest in the Bacteroidetes

Resolution rates ranged from 20% (Bacteroides thetaiotaomicron) to 71% (Klebsiella michiganensis). [src: annotation_gap_discovery]

## Key figures

- **20%**: resolution rate in Bacteroides thetaiotaomicron [src: annotation_gap_discovery]
- **71%**: resolution rate in Klebsiella michiganensis [src: annotation_gap_discovery]

## Evidence

> Resolution rates ranged from 20% (*Bacteroides thetaiotaomicron*) to 71% (*Klebsiella michiganensis*). [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

The sole Bacteroidetes (B. thetaiotaomicron) had the lowest resolution rate, suggesting the approach may be less effective for phylogenetically distant clades with divergent metabolism. [src: annotation_gap_discovery]

> The sole Bacteroidetes (*B. thetaiotaomicron*) had the lowest resolution rate, suggesting the approach may be less effective for phylogenetically distant clades with divergent metabolism [src: annotation_gap_discovery]

## Other caveats in this report

- Dark reactions are known only by stoichiometry rather than enzyme classification, making sequence homology searches and functional annotation cross-referencing far more difficult. [src: annotation_gap_discovery]
- Exact GapMind-gapfilling concordance was limited because available KBase Data Lakehouse data report pathway step counts rather than individual step identities. [src: annotation_gap_discovery]
- The report describes zero wildtype growth in knockout validation as an expected limitation because the models need the gapfilled reactions themselves for growth on those carbon sources. [src: annotation_gap_discovery]
- Draft models built from automated RAST annotations contain systematic errors; the 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- Multiple valid gapfill solutions may exist for each false-negative case, and the report's default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]
