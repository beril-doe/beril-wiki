---
type: "Place"
description: "Nine-well 3×3 groundwater grid used to delineate contamination plume flow paths from 16S community data."
sources: ["summaries/discoveries.md", "summaries/enigma_sso_asv_ecology__REPORT.md"]
aliases: ["SSO"]
---
# Subsurface Observatory well grid

The Subsurface Observatory (SSO) well grid is a nine-well 3×3 groundwater grid, used to delineate contamination plume flow paths from 16S community data. The report concludes that 16S community data can delineate subsurface contamination flow paths at sub-decameter resolution. [src: discoveries] The plume model is inferred from community data. The report names geochemistry measurements as the key validation dataset, and those measurements were never ingested. [src: discoveries]

## Key facts

- The grid spans about 6 m. The analysis used 9 wells, 23,458 amplicon sequence variants (ASVs) and 37 sediment core samples aggregated per well. [src: discoveries, enigma_sso_asv_ecology]
- Communities show significant distance-decay (Mantel ρ=0.323, p=0.029). The east-west axis drives it, not the hillslope gradient. See [[concepts/meter-scale-spatial-structure-and-distance-decay-of-subsurface-communities]]. [src: discoveries]
- Groundwater communities are temporally stable: well R²=49.9% and date R²=0.8% over 9 days. See [[concepts/temporal-stability-of-groundwater-communities]]. [src: discoveries]

## Plume model

The report proposes one explanatory model. A contamination plume enters from the northeast and flows southwest through the saturated zone, and this governs the spatial structure of the communities. [src: enigma_sso_asv_ecology] The plume enters near U3 (upper-east) and flows diagonally toward L7 (lower-west). This creates the Column 3 corridor. [src: enigma_sso_asv_ecology] Wells U3-M6-L7 share community composition along that path. [src: discoveries] The report says this corridor, identified purely from Bray-Curtis dissimilarity, matches the expected plume trajectory. It concludes that 16S similarity can map subsurface hydrology at meter scale. [src: enigma_sso_asv_ecology] See [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].

## Process mapping

Genus-level functional inference maps the redox ladder (denitrification → iron reduction → fermentation) onto the grid. [src: discoveries] The report claims this is the first spatially explicit mapping of biogeochemical process distributions across the grid. It inferred the processes from 16S composition at phylum, class and genus resolution. [src: enigma_sso_asv_ecology] See [[concepts/taxonomy-based-functional-inference-of-biogeochemical-processes-and-the-redox-ladder]].

- **M5:** This well hosts a [[entities/rhodanobacter]] denitrification hotspot (7.7%) at the plume mixing zone. [src: discoveries] The report explains it as nitrate-rich plume water meeting native organic carbon. [src: enigma_sso_asv_ecology]
- **M6:** This well is consistently lowest for iron oxidation, sulfur oxidation and nitrification. The report calls it an anaerobic dead zone, where the plume core has consumed all terminal electron acceptors. [src: enigma_sso_asv_ecology]
- **U3:** Candidatus Nitrosotalea (an archaeal ammonia oxidizer) and [[entities/sideroxydans]] (an iron oxidizer) co-occur almost perfectly across the 9 wells (ρ=+0.95), concentrated at U3. [src: discoveries] The report calls both chemolithotrophs exploiting reduced compounds arriving in the plume. [src: discoveries] It suggests the tight coupling reflects a shared niche at the oxic plume fringe. [src: discoveries] See [[concepts/metabolic-guild-co-occurrence-and-redox-driven-segregation]].

## Caveats

- Only 5 of 9 wells have groundwater ASV data (L7, L9, M4, M6, U2). The critical wells M5 (denitrification hotspot) and U3 (plume entry) are missing from that data. [src: enigma_sso_asv_ecology]
- For the SSO campaign, 221 METALS/ICTOC/ISOTOPES/NH3NO2 sample tubes are registered in ENIGMA CORAL (`sdt_sample`). Zero Assay Geochemistry processes are linked, so the analytical values were never ingested into the KBase Data Lakehouse. [src: discoveries] The report calls this the key validation dataset for the plume model. [src: discoveries] See annotation and environmental metadata table gaps in the data lakehouse and [[entities/enigma]].

See also [[summaries/discoveries]] and [[summaries/enigma_sso_asv_ecology__REPORT]].
