---
type: "Method"
description: "geNomad is a mobile-genetic-element prediction tool that BERIL projects used for mobilome detection or named as a dedicated alternative for prophage identification."
sources: ["summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_amr_comobilization__REPORT.md"]
---
# geNomad

geNomad (also written GeNomad) is a computational method for predicting mobile genetic elements. In this corpus it appears in two roles. It is one of the tools used for mobilome detection in [[summaries/plant_microbiome_ecotypes__REPORT]]. In [[summaries/prophage_amr_comobilization__REPORT]] it is named as a dedicated prophage prediction tool that the project did not use. [src: plant_microbiome_ecotypes, prophage_amr_comobilization]

## Use in mobilome detection

The plant_microbiome_ecotypes project ran mobilome analysis on the soil biome for 563 pangenome genera with data. geNomad, ISEScan and [[entities/icefinder]] together detected 17,323 mobilome entries. The element types included IS elements (IS110, IS701, IS1634, IS256, IS3), plasmids, prophages, terminal inverted repeats and viral sequences. The report gives the count for the three tools combined, not for geNomad alone. [src: plant_microbiome_ecotypes]

The same project names "GeNomad mobile-element predictions" as the source of proposed direct mobile-element predictions. [src: plant_microbiome_ecotypes]

## As an alternative to keyword-based prophage calling

The prophage_amr_comobilization project identified prophages by keyword and [[entities/pfam]] matching on [[entities/bakta]] annotations, not with dedicated prophage prediction tools such as PHASTER or geNomad. The project flags two consequences of that choice: the keyword approach may produce false positives, such as phage-defense systems, and may miss divergent prophages. This caveat comes from that project's own limitations statement. It is not a measured comparison against geNomad. [src: prophage_amr_comobilization]
