---
type: "Finding"
description: "The association between prophage proximity and AMR accessory status is absent or reversed at very close range, with OR=0.78 at 3 genes."
finding_id: "prophage_amr_comobilization--6abb4f27"
result: "observation"
source: "prophage_amr_comobilization"
quantities: [{"value": "OR=0.78", "what": "odds ratio for accessory status at 3 genes threshold", "unit": "", "denominator": "", "scope": ""}]
caveat: "While statistically significant in aggregate, the effect is modest (2.1 percentage point difference in accessory fraction) and heterogeneous across species."
first_added: "2026-11-24"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Prophage proximity and accessory AMR status reverse at very close range

The association between prophage proximity and AMR accessory status is absent or reversed at very close range, with OR=0.78 at 3 genes. [src: prophage_amr_comobilization]

## Key figures

- **OR=0.78**: odds ratio for accessory status at 3 genes threshold [src: prophage_amr_comobilization]

## Evidence

> The effect is threshold-dependent: it is absent or reversed at very close range (OR=0.78 at 3 genes, OR=0.92 at 5 genes) and strengthens at broader thresholds (OR=1.19 at 15 genes, OR=1.28 at 50 genes). [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

While statistically significant in aggregate, the effect is modest (2.1 percentage point difference in accessory fraction) and heterogeneous across species. [src: prophage_amr_comobilization]

> While statistically significant in aggregate, the effect is modest (2.1 percentage point difference in accessory fraction) and heterogeneous across species. [src: prophage_amr_comobilization]

## Other caveats in this report

- Species-level H1 effects are heterogeneous: only 33 of 74 testable species have OR>1, and the median species-level OR is 0.85. [src: prophage_amr_comobilization]
- The KBase Data Lakehouse fitness browser covers only 48 model organisms with RB-TnSeq data, which overlap poorly with the GTDB pangenome species analyzed in the report. [src: prophage_amr_comobilization]
- The report measures AMR–prophage distances in ordinal gene positions parsed from gene_id rather than base pairs, so true genomic distances may differ. [src: prophage_amr_comobilization]
- The report identifies prophages through keyword/Pfam matching on bakta_annotations rather than dedicated tools such as PHASTER or geNomad, potentially including false positives such as phage-defense systems and missing divergent prophages. [src: prophage_amr_comobilization]
- The co-localization analysis sampled 20 genomes per species, and the report says exhaustive analysis of all 293K genomes would strengthen its findings. [src: prophage_amr_comobilization]
