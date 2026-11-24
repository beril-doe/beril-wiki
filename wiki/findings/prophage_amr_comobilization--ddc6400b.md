---
type: "Finding"
description: "Over half (55.7%) of AMR gene instances in the top-100 AMR-burdened species reside on contigs that also carry strict prophage markers (terminase, phage structural proteins, holin/lysin)."
finding_id: "prophage_amr_comobilization--ddc6400b"
result: "observation"
source: "prophage_amr_comobilization"
quantities: [{"value": "55.7%", "what": "AMR gene instances on contigs with strict prophage markers", "unit": "", "denominator": "", "scope": "top-100 AMR-burdened species"}]
caveat: "Prophages are identified by keyword/Pfam matching on bakta_annotations rather than tools such as PHASTER or geNomad, which may include false positives such as phage-defense systems and miss divergent prophages."
first_added: "2026-11-24"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Over half of AMR genes share contigs with prophage markers

Over half (55.7%) of AMR gene instances in the top-100 AMR-burdened species reside on contigs that also carry strict prophage markers (terminase, phage structural proteins, holin/lysin). [src: prophage_amr_comobilization]

## Key figures

- **55.7%**: AMR gene instances on contigs with strict prophage markers (scope top-100 AMR-burdened species) [src: prophage_amr_comobilization]

## Evidence

> Over half (55.7%) of AMR gene instances in the top-100 AMR-burdened species reside on contigs that also carry strict prophage markers (terminase, phage structural proteins, holin/lysin). [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

Prophages are identified by keyword/Pfam matching on bakta_annotations rather than tools such as PHASTER or geNomad, which may include false positives such as phage-defense systems and miss divergent prophages. [src: prophage_amr_comobilization]

> **Prophage identification**: Uses keyword/Pfam matching on bakta_annotations rather than dedicated prophage prediction tools (e.g., PHASTER, geNomad). May include false positives (e.g., phage-defense systems) and miss divergent prophages. [src: prophage_amr_comobilization]

## Other caveats in this report

- Species-level H1 effects are heterogeneous: only 33 of 74 testable species have OR>1, and the median species-level OR is 0.85. [src: prophage_amr_comobilization]
- The KBase Data Lakehouse fitness browser covers only 48 model organisms with RB-TnSeq data, which overlap poorly with the GTDB pangenome species analyzed in the report. [src: prophage_amr_comobilization]
- The report characterizes the aggregate H1 effect as modest, with a 2.1 percentage point accessory-fraction difference and heterogeneity across species. [src: prophage_amr_comobilization]
- The report measures AMR–prophage distances in ordinal gene positions parsed from gene_id rather than base pairs, so true genomic distances may differ. [src: prophage_amr_comobilization]
- The co-localization analysis sampled 20 genomes per species, and the report says exhaustive analysis of all 293K genomes would strengthen its findings. [src: prophage_amr_comobilization]
