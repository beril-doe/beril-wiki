---
type: "Finding"
description: "The report could not test the fitness-cost hypothesis H3 because of limited overlap between Fitness Browser organisms and GTDB species."
finding_id: "prophage_amr_comobilization--22ee9735"
result: "null result"
source: "prophage_amr_comobilization"
quantities: []
caveat: "The KBase Data Lakehouse fitness browser covers only 48 model organisms with RB-TnSeq data, which do not overlap well with the GTDB pangenome species analyzed."
first_added: "2026-11-24"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Fitness cost of prophage-linked AMR could not be tested

The report could not test the fitness-cost hypothesis H3 because of limited overlap between Fitness Browser organisms and GTDB species. [src: prophage_amr_comobilization]

## Evidence

> **Fitness data gap**: H3 could not be tested due to limited overlap between fitness browser organisms and GTDB species. [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

The KBase Data Lakehouse fitness browser covers only 48 model organisms with RB-TnSeq data, which do not overlap well with the GTDB pangenome species analyzed. [src: prophage_amr_comobilization]

> The BERDL fitness browser covers only 48 model organisms with RB-TnSeq data, which do not overlap well with the GTDB pangenome species analyzed here. [src: prophage_amr_comobilization]

## Other caveats in this report

- Species-level H1 effects are heterogeneous: only 33 of 74 testable species have OR>1, and the median species-level OR is 0.85. [src: prophage_amr_comobilization]
- The report characterizes the aggregate H1 effect as modest, with a 2.1 percentage point accessory-fraction difference and heterogeneity across species. [src: prophage_amr_comobilization]
- The report measures AMR–prophage distances in ordinal gene positions parsed from gene_id rather than base pairs, so true genomic distances may differ. [src: prophage_amr_comobilization]
- The report identifies prophages through keyword/Pfam matching on bakta_annotations rather than dedicated tools such as PHASTER or geNomad, potentially including false positives such as phage-defense systems and missing divergent prophages. [src: prophage_amr_comobilization]
- The co-localization analysis sampled 20 genomes per species, and the report says exhaustive analysis of all 293K genomes would strengthen its findings. [src: prophage_amr_comobilization]
