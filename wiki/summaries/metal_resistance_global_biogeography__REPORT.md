---
type: Summary
description: Global map of environmental bacterial metal resistance and its spatial
  data gaps
doc_type: short
full_text: ../sources/metal_resistance_global_biogeography__REPORT.md
title: Global Biogeography of Environmental Bacterial Metal Resistance
sources:
- id: metal_resistance_global_biogeography
  resource: ../sources/metal_resistance_global_biogeography__REPORT.md
  title: metal resistance global biogeography
---
# Global Biogeography of Environmental Bacterial Metal Resistance

## Overview

This preliminary report maps the global distribution of environmental bacterial metal resistance using metagenome-assembled genomes (MAGs) extracted from MGnify and geospatial metadata retrieved through the ENA batch API. Data extraction, coordinate retrieval, and NB02 spatial analyses were completed; production figures and remaining validation analyses are pending. [^metal_resistance_global_biogeography]

## Key Findings

- The study extracted **260,652 environmental MAGs** from MGnify, of which **30,497** remained after filtering host-associated biomes. [^metal_resistance_global_biogeography]
- **22,356 MAGs** had usable geospatial coordinates, representing **73.3%** coordinate coverage of the environmental MAG set. [^metal_resistance_global_biogeography]
- ENA batch API retrieval returned **24,511 sample records**; **16,964 (69.2%)** had valid latitude/longitude pairs, leaving a **30.8% spatial data gap** in public metagenomic archives. [^metal_resistance_global_biogeography]
- Among the **22,356 MAGs with coordinates**, **2.8%** carried at least one metal-resistance type. Metal resistance was therefore rare in the global environmental MAG pool and substantially lower than implied by the **30,497-MAG** filtered set. [^metal_resistance_global_biogeography]
- A 5° grid analysis included **289 cells with at least 5 MAGs**. Using Fisher's exact tests with Benjamini–Hochberg false discovery rate (BH FDR) correction, it identified **11 significant hotspots** with **OR>2** and **q<0.05**, and **3 coldspots** with **OR<0.5** and **q<0.05**. [^metal_resistance_global_biogeography]
- The top hotspot was the Atacama/Andean region of Chile at **lat=-25°, lon=-70°**, with **21.8% prevalence**, **OR=9.83**, **q=7.6e-12**, and **n=101 MAGs**. Eastern and central USA clusters at **lat=40°, lon=-80° and -90°** had **OR=7.9** and **6.3**, while an East/Southeast Asia cluster at **lat=25-30°, lon=105-120°** had **OR=4.4–5.9**. [^metal_resistance_global_biogeography]
- Biome-stratified Fisher's exact tests against the global baseline, with BH FDR correction, found **soil** enriched for metal resistance at **5.8% prevalence**, **OR=5.05**, and **q=1.8e-82**; **rhizosphere** prevalence was **1.9%**, **OR=0.66**, and **q=0.30 (NS)**; and **marine** prevalence was **1.2%**, **OR=0.20**, and **q=9.2e-80**. [^metal_resistance_global_biogeography]

| Biome | n MAGs | Prevalence | OR | q |
|---|---:|---:|---:|---:|
| Soil | 7,939 | 5.8% | 5.05 | 1.8e-82 |
| Rhizosphere | 422 | 1.9% | 0.66 | 0.30 (NS) |
| Marine | 13,995 | 1.2% | 0.20 | 9.2e-80 |

These biome-specific values support [environmental-resistome](../concepts/environmental-resistome.md) by showing strong soil enrichment and marine depletion in the coordinate-filtered environmental MAG dataset. [^metal_resistance_global_biogeography]

- The ENA coordinate file covered all areas represented in the MAG coordinate dataset: **0 of 532 MAG grid cells** lacked ENA coordinate coverage. Thus, the **30.8%** gap of **16,964/24,511** valid pairs is a per-sample gap rather than a geographic gap; it reflects samples without coordinates, not grid cells with no samples. [^metal_resistance_global_biogeography]
- The drafted global map uses geopandas and matplotlib to distinguish metal-resistant MAGs, defined as those with **n_metal_types > 0**, from susceptible MAGs and to colour them by metal diversity. The map cell has a known `NameError` because `import matplotlib.pyplot` is missing from that cell. [^metal_resistance_global_biogeography]
- The report states that metal-resistant genomes are not uniformly distributed among the **22,356** MAGs with coordinates, but that hotspot identification and sampling-effort correction are required before regional patterns can be interpreted. [^metal_resistance_global_biogeography]
- The **2.8%** global metal-resistance prevalence is much lower than the **21.8%** T4SS prevalence reported for comparison, supporting the interpretation that AMRFinderPlus metal-resistance genes and T4SS horizontal-gene-transfer machinery are distinct features that are not uniformly co-distributed. [^metal_resistance_global_biogeography]

## Caveats and Pending Analyses

- The report is preliminary. Data extraction and coordinate retrieval were complete at NB01, while NB02 spatial analysis and NB03 figures were initially pending; NB02 results are now reported, but production figure completion remains pending. [^metal_resistance_global_biogeography]
- The **30.8%** per-sample coordinate gap is a substantial limitation for global mapping and creates geographic blind spots in public metagenomic archives. Which biomes are most underrepresented remains an open question. [^metal_resistance_global_biogeography]
- The Atacama/Andean and USA hotspots may reflect single-study or expedition-level artefacts. The report requires checking distinct `sample_accession` prefixes within each hotspot. [^metal_resistance_global_biogeography]
- Sampling-effort correction remains necessary; the report proposes testing whether hotspots persist after normalising by **log(n_MAGs)**. [^metal_resistance_global_biogeography]
- The matplotlib import must be fixed in the NB01 map cell before the production figure is generated. [^metal_resistance_global_biogeography]

## Slots Into

- [environmental-resistome](../concepts/environmental-resistome.md) — global prevalence, biome enrichment and depletion, and spatial hotspots provide evidence about the geographic structure of environmental metal resistance. [^metal_resistance_global_biogeography]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — coordinate coverage, the distinction between per-sample and geographic gaps, and pending sampling-effort correction identify limits on embedding resistance patterns geographically. [^metal_resistance_global_biogeography]

[^metal_resistance_global_biogeography]: [metal resistance global biogeography](../sources/metal_resistance_global_biogeography__REPORT.md)
