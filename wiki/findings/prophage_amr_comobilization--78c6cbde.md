---
type: "Finding"
description: "A species-level log-log regression predicts a ~6.6-fold increase in AMR breadth for a 10-fold increase in prophage density (slope=0.823, R\u00b2=0.30)."
finding_id: "prophage_amr_comobilization--78c6cbde"
result: "observation"
source: "prophage_amr_comobilization"
quantities: [{"value": "~6.6-fold", "what": "predicted increase in AMR breadth per 10-fold increase in prophage density", "unit": "", "denominator": "", "scope": ""}, {"value": "slope=0.823", "what": "log-log regression slope", "unit": "", "denominator": "", "scope": ""}, {"value": "R\u00b2=0.30", "what": "variance explained", "unit": "", "denominator": "", "scope": ""}]
caveat: "The H2 association does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes."
first_added: "2026-11-24"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Tenfold higher prophage density predicts much broader AMR repertoires

A species-level log-log regression predicts a ~6.6-fold increase in AMR breadth for a 10-fold increase in prophage density (slope=0.823, R²=0.30). [src: prophage_amr_comobilization]

## Key figures

- **~6.6-fold**: predicted increase in AMR breadth per 10-fold increase in prophage density [src: prophage_amr_comobilization]
- **slope=0.823**: log-log regression slope [src: prophage_amr_comobilization]
- **R²=0.30**: variance explained [src: prophage_amr_comobilization]

## Evidence

> A log-log regression reveals that a 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth (slope=0.823, R²=0.30). [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

The H2 association does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

> **Correlation vs causation**: The H2 association does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

## Other caveats in this report

- Species-level H1 effects are heterogeneous: only 33 of 74 testable species have OR>1, and the median species-level OR is 0.85. [src: prophage_amr_comobilization]
- The KBase Data Lakehouse fitness browser covers only 48 model organisms with RB-TnSeq data, which overlap poorly with the GTDB pangenome species analyzed in the report. [src: prophage_amr_comobilization]
- The report characterizes the aggregate H1 effect as modest, with a 2.1 percentage point accessory-fraction difference and heterogeneity across species. [src: prophage_amr_comobilization]
- The report measures AMR–prophage distances in ordinal gene positions parsed from gene_id rather than base pairs, so true genomic distances may differ. [src: prophage_amr_comobilization]
- The report identifies prophages through keyword/Pfam matching on bakta_annotations rather than dedicated tools such as PHASTER or geNomad, potentially including false positives such as phage-defense systems and missing divergent prophages. [src: prophage_amr_comobilization]
