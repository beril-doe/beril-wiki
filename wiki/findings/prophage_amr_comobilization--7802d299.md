---
type: "Finding"
description: "In the top-100 AMR-burdened species, 55.7% of AMR gene instances reside on contigs that also carry strict prophage markers, but the median distance to the nearest marker among these co-localized genes is 34 genes and only 10.4% of all AMR genes are within 10 genes."
finding_id: "prophage_amr_comobilization--7802d299"
result: "observation"
source: "prophage_amr_comobilization"
quantities: [{"value": "55.7%", "what": "AMR gene instances on contigs carrying strict prophage markers", "unit": "", "denominator": "AMR gene instances in the top-100 AMR-burdened species", "scope": "top-100 AMR-burdened species"}, {"value": "34", "what": "median distance to nearest prophage marker among co-localized AMR genes", "unit": "genes", "denominator": "co-localized AMR genes", "scope": "top-100 AMR-burdened species"}, {"value": "10.4%", "what": "AMR genes within 10 genes of a prophage marker", "unit": "", "denominator": "all AMR genes", "scope": "top-100 AMR-burdened species"}]
caveat: "Distances are in ordinal gene positions parsed from gene_id format, not base-pair resolution, so true genomic distances may differ."
first_added: "2026-10-27"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Many AMR genes share contigs with prophage markers

In the top-100 AMR-burdened species, 55.7% of AMR gene instances reside on contigs that also carry strict prophage markers, but the median distance to the nearest marker among these co-localized genes is 34 genes and only 10.4% of all AMR genes are within 10 genes. [src: prophage_amr_comobilization]

## Key figures

- **55.7%**: AMR gene instances on contigs carrying strict prophage markers (denominator AMR gene instances in the top-100 AMR-burdened species; scope top-100 AMR-burdened species) [src: prophage_amr_comobilization]
- **34 genes**: median distance to nearest prophage marker among co-localized AMR genes (denominator co-localized AMR genes; scope top-100 AMR-burdened species) [src: prophage_amr_comobilization]
- **10.4%**: AMR genes within 10 genes of a prophage marker (denominator all AMR genes; scope top-100 AMR-burdened species) [src: prophage_amr_comobilization]

## Evidence

> Over half (55.7%) of AMR gene instances in the top-100 AMR-burdened species reside on contigs that also carry strict prophage markers (terminase, phage structural proteins, holin/lysin). Among these co-localized AMR genes, the median distance to the nearest prophage marker is 34 genes, and 10.4% of all AMR genes are within 10 genes of a prophage marker. [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

Distances are in ordinal gene positions parsed from gene_id format, not base-pair resolution, so true genomic distances may differ. [src: prophage_amr_comobilization]

> - **Gene position proxy**: Distances are in ordinal gene positions parsed from gene_id format, not base-pair resolution. True genomic distances may differ. [src: prophage_amr_comobilization]

## Other caveats in this report

- The proximity–accessory association depends on the distance threshold and is heterogeneous across species: only 33 of 74 testable species had OR>1. [src: prophage_amr_comobilization]
- The fitness dataset covered only 48 model organisms with RB-TnSeq data and poorly overlapped the analyzed GTDB species. [src: prophage_amr_comobilization]
- The species-level association is consistent with two non-exclusive explanations—direct prophage transduction and shared gene-acquisition propensity—but does not distinguish them. [src: prophage_amr_comobilization]
- H1's aggregate difference was 2.1 percentage points and varied among species. Proposed explanations for the near-range reversal and broad-range strengthening are interpretations, not demonstrated mechanisms. [src: prophage_amr_comobilization]
- Keyword/Pfam-based prophage identification may count phage-defense systems falsely and miss divergent prophages; PHASTER and geNomad are named alternative methods. [src: prophage_amr_comobilization]
