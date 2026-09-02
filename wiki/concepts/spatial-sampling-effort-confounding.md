---
type: "Concept"
description: "How uneven sampling can create or distort geographic resistance hotspots"
sources: ["summaries/metal_resistance_global_biogeography__REPORT.md"]
---
# Spatial Sampling Effort and Geographic Hotspot Confounding

Geographic hotspot analyses of environmental bacterial metal resistance can be confounded by uneven sampling effort, incomplete coordinates, and concentration of samples from particular studies or expeditions. The [[summaries/metal_resistance_global_biogeography__REPORT]] provides a preliminary case in which resistance prevalence varies across grid cells, but the report explicitly requires sampling-effort correction and study-origin checks before regional patterns are interpreted. [src: metal_resistance_global_biogeography]

## Evidence from the Global Metal-Resistance Analysis

The study extracted **260,652 environmental MAGs** from MGnify and retained **30,497** after filtering host-associated biomes. [src: metal_resistance_global_biogeography] Of these, **22,356 MAGs** had usable geospatial coordinates, corresponding to **73.3%** coordinate coverage of the environmental MAG set. [src: metal_resistance_global_biogeography] ENA batch API retrieval returned **24,511 sample records**, of which **16,964 (69.2%)** had valid latitude/longitude pairs, leaving a **30.8%** per-sample spatial data gap. [src: metal_resistance_global_biogeography]

The coordinate gap does not indicate that entire geographic regions were absent from the archive: the ENA coordinate file covered every area represented in the MAG coordinate dataset, with **0 of 532 MAG grid cells** lacking ENA coordinate coverage. [src: metal_resistance_global_biogeography] The distinction is therefore between missing coordinates for individual samples and missing geographic grid cells, rather than evidence that the sampled map is geographically complete. [src: metal_resistance_global_biogeography]

Among the **22,356 MAGs with coordinates**, **2.8%** carried at least one metal-resistance type. [src: metal_resistance_global_biogeography] A 5° grid contained **289 cells with at least 5 MAGs**; Fisher's exact tests with Benjamini–Hochberg false discovery rate (BH FDR), a multiple-testing correction, identified **11 significant hotspots** with **OR>2** and **q<0.05**, and **3 coldspots** with **OR<0.5** and **q<0.05**. [src: metal_resistance_global_biogeography]

The strongest apparent hotspot was the Atacama/Andean region of Chile at **lat=-25°, lon=-70°**, where prevalence was **21.8%**, **OR=9.83**, **q=7.6e-12**, and **n=101 MAGs**. [src: metal_resistance_global_biogeography] Eastern and central USA cells at **lat=40°, lon=-80° and -90°** had **OR=7.9** and **6.3**, while an East/Southeast Asia cluster at **lat=25-30°, lon=105-120°** had **OR=4.4–5.9**. [src: metal_resistance_global_biogeography] These results identify statistical geographic contrasts, but they do not by themselves establish that the contrasts reflect regional environmental selection rather than differences in sampling composition, study representation, or sampling intensity. [src: metal_resistance_global_biogeography]

## Biome Composition as a Confounding Dimension

Biome-stratified tests show that resistance prevalence differs strongly among the sampled environmental categories: soil contained **7,939 MAGs** with **5.8%** prevalence, **OR=5.05**, and **q=1.8e-82**; rhizosphere contained **422 MAGs** with **1.9%** prevalence, **OR=0.66**, and **q=0.30 (NS)**; and marine samples contained **13,995 MAGs** with **1.2%** prevalence, **OR=0.20**, and **q=9.2e-80**. [src: metal_resistance_global_biogeography]

This biome structure supports [[concepts/environmental-resistome]] by showing soil enrichment and marine depletion in the coordinate-filtered environmental MAG dataset. [src: metal_resistance_global_biogeography] It also means that a geographic hotspot can be partly produced by where particular biomes were sampled, unless geographic comparisons account for biome composition. [src: metal_resistance_global_biogeography]

## Study-Origin and Sampling-Intensity Risks

The report identifies the Atacama/Andean and USA hotspots as possible single-study or expedition-level artefacts and requires checking distinct `sample_accession` prefixes within each hotspot. [src: metal_resistance_global_biogeography] Concentration of many MAGs from one study, expedition, or accession family could make a grid cell appear unusually enriched while measuring study-specific sampling rather than an independently replicated regional pattern. [src: metal_resistance_global_biogeography]

The report proposes testing whether hotspots persist after normalising by **log(n_MAGs)**, where `n_MAGs` is the number of MAGs represented in a grid cell. [src: metal_resistance_global_biogeography] This proposed correction directly tests whether hotspot status is robust to sampling effort, but the corrected results were not reported in the preliminary analysis. [src: metal_resistance_global_biogeography]

The findings therefore refine [[concepts/environment-embedding-geography]]: coordinate availability can support geographic mapping, but geographic interpretation remains conditional on sampling effort, study replication, and environmental composition. [src: metal_resistance_global_biogeography] They also connect to [[concepts/spatial-structure-versus-short-term-temporal-stability]], because spatial contrasts cannot be interpreted independently of how samples were distributed across locations and collection contexts. [src: metal_resistance_global_biogeography]

## Tensions

The analysis provides strong statistical evidence for geographic enrichment and depletion under its tested grid-cell model, including **11 hotspots** and **3 coldspots** after BH FDR correction. [src: metal_resistance_global_biogeography] At the same time, the report states that hotspot identification requires sampling-effort correction and that regional patterns should not yet be interpreted without checking study or expedition artefacts. [src: metal_resistance_global_biogeography] The tension is therefore between detected spatial association and unresolved representativeness of the samples contributing to each association. [src: metal_resistance_global_biogeography]

## Open Directions

- Use the MAG coordinate table and ENA sample records to classify distinct `sample_accession` prefixes within each reported hotspot, then test whether hotspot significance persists after removing or stratifying dominant studies; this would address the report's single-study or expedition-level artefact concern. [src: metal_resistance_global_biogeography]
- Recompute the 5°-grid Fisher's exact tests after normalising or modelling sampling effort with **log(n_MAGs)**, and ask whether the **11** hotspots and **3** coldspots remain significant under the effort-adjusted analysis. [src: metal_resistance_global_biogeography]
- Combine MAG resistance status, biome labels, grid-cell counts, and coordinate completeness in a stratified or matched model, and ask whether the Atacama/Andean, USA, and East/Southeast Asia signals persist after controlling for biome composition. [src: metal_resistance_global_biogeography]
- Compare the **22,356** coordinate-bearing MAGs with the **30,497-MAG** filtered set by biome and sample source, and ask whether the **30.8%** per-sample coordinate gap disproportionately excludes particular environmental categories. [src: metal_resistance_global_biogeography]
- Repeat hotspot analysis using study-aware resampling across the **532** represented grid cells, and ask whether regional enrichment is reproducible when no single accession family or sampling campaign dominates a cell. [src: metal_resistance_global_biogeography]
