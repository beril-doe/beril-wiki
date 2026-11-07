---
type: "Finding"
description: "At a 10-gene threshold, prophage-proximal AMR genes were slightly more likely to be accessory (67.6%) than distal AMR genes (65.5%), a statistically significant but modest effect (Fisher's exact OR=1.10, p=0.005, bootstrap 95% CI [1.024, 1.185])."
finding_id: "prophage_amr_comobilization--4cead8a0"
result: "observation"
source: "prophage_amr_comobilization"
quantities: [{"value": "67.6%", "what": "accessory fraction of proximal AMR genes", "unit": "", "denominator": "proximal AMR genes (within 10 genes of a prophage marker)", "scope": "within 10 genes of a prophage marker"}, {"value": "65.5%", "what": "accessory fraction of distal AMR genes", "unit": "", "denominator": "distal AMR genes (more than 10 genes from a prophage marker)", "scope": "more than 10 genes from a prophage marker"}, {"value": "1.10", "what": "Fisher's exact odds ratio", "unit": "", "denominator": "", "scope": "10-gene threshold; p=0.005"}]
caveat: "The effect is threshold-dependent (OR=0.78 at 3 genes, OR=0.92 at 5 genes) and heterogeneous, with only 33 of 74 testable species showing OR>1 and a median species-level OR of 0.85."
first_added: "2026-10-27"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Prophage-proximal AMR genes are only slightly more often accessory

At a 10-gene threshold, prophage-proximal AMR genes were slightly more likely to be accessory (67.6%) than distal AMR genes (65.5%), a statistically significant but modest effect (Fisher's exact OR=1.10, p=0.005, bootstrap 95% CI [1.024, 1.185]). [src: prophage_amr_comobilization]

## Key figures

- **67.6%**: accessory fraction of proximal AMR genes (denominator proximal AMR genes (within 10 genes of a prophage marker); scope within 10 genes of a prophage marker) [src: prophage_amr_comobilization]
- **65.5%**: accessory fraction of distal AMR genes (denominator distal AMR genes (more than 10 genes from a prophage marker); scope more than 10 genes from a prophage marker) [src: prophage_amr_comobilization]
- **1.10**: Fisher's exact odds ratio (scope 10-gene threshold; p=0.005) [src: prophage_amr_comobilization]

## Evidence

> Prophage-proximal AMR genes (within 10 genes) are slightly more likely to be accessory (67.6%) than distal AMR genes (65.5%), yielding a statistically significant but modest effect (Fisher's exact OR=1.10, p=0.005, bootstrap 95% CI [1.024, 1.185]). [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

The effect is threshold-dependent (OR=0.78 at 3 genes, OR=0.92 at 5 genes) and heterogeneous, with only 33 of 74 testable species showing OR>1 and a median species-level OR of 0.85. [src: prophage_amr_comobilization]

> The effect is threshold-dependent: it is absent or reversed at very close range (OR=0.78 at 3 genes, OR=0.92 at 5 genes) and strengthens at broader thresholds (OR=1.19 at 15 genes, OR=1.28 at 50 genes). Per-species analysis reveals heterogeneity: only 33 of 74 testable species show OR>1, with a median species-level OR of 0.85. [src: prophage_amr_comobilization]

## Other caveats in this report

- The fitness dataset covered only 48 model organisms with RB-TnSeq data and poorly overlapped the analyzed GTDB species. [src: prophage_amr_comobilization]
- The species-level association is consistent with two non-exclusive explanations—direct prophage transduction and shared gene-acquisition propensity—but does not distinguish them. [src: prophage_amr_comobilization]
- H1's aggregate difference was 2.1 percentage points and varied among species. Proposed explanations for the near-range reversal and broad-range strengthening are interpretations, not demonstrated mechanisms. [src: prophage_amr_comobilization]
- Reported gene distances are ordinal positions parsed from gene identifiers, not base-pair distances. [src: prophage_amr_comobilization]
- Keyword/Pfam-based prophage identification may count phage-defense systems falsely and miss divergent prophages; PHASTER and geNomad are named alternative methods. [src: prophage_amr_comobilization]
