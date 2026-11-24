---
type: "Finding"
description: "In the 22,356 environmental MAGs with coordinates, 2.8% carry \u22651 metal resistance type, substantially lower than implied by reporting on the 30,497 filtered MAG set, so metal resistance is rare in the global environmental MAG pool."
finding_id: "metal_resistance_global_biogeography--2ac1d00b"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "2.8%", "what": "MAGs carrying \u22651 metal resistance type", "unit": "", "denominator": "22,356 MAGs with coordinates", "scope": "global environmental MAGs"}, {"value": "30,497", "what": "filtered MAG set the lower figure is contrasted with", "unit": "MAGs", "denominator": "", "scope": ""}]
caveat: "The report is preliminary: data extraction and coordinate retrieval are complete (NB01), but NB02 spatial analysis and NB03 figures are pending."
first_added: "2026-11-24"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Metal resistance is rare in georeferenced environmental MAGs

In the 22,356 environmental MAGs with coordinates, 2.8% carry ≥1 metal resistance type, substantially lower than implied by reporting on the 30,497 filtered MAG set, so metal resistance is rare in the global environmental MAG pool. [src: metal_resistance_global_biogeography]

## Key figures

- **2.8%**: MAGs carrying ≥1 metal resistance type (denominator 22,356 MAGs with coordinates; scope global environmental MAGs) [src: metal_resistance_global_biogeography]
- **30,497 MAGs**: filtered MAG set the lower figure is contrasted with [src: metal_resistance_global_biogeography]

## Evidence

> **Global metal resistance prevalence:** 2.8% of 22,356 MAGs with coordinates carry ≥1 metal resistance type — substantially lower than implied by reporting on the 30,497 filtered MAG set. Metal resistance is rare in the global environmental MAG pool. [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

The report is preliminary: data extraction and coordinate retrieval are complete (NB01), but NB02 spatial analysis and NB03 figures are pending. [src: metal_resistance_global_biogeography]

> Preliminary — data extraction and coordinate retrieval complete (NB01). NB02 spatial analysis and NB03 figures pending. [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The drafted global map cell has a NameError caused by a missing import matplotlib.pyplot, which requires fixing before NB02. [src: metal_resistance_global_biogeography]
- The report requires hotspot identification and sampling-effort correction before interpreting regional metal-resistance patterns in the georeferenced environmental MAG dataset. [src: metal_resistance_global_biogeography]
- The report initially interprets the 30.8% ENA coordinate gap as substantial geographic blind spots for public-archive global metal-resistance maps, independently of the biological question. [src: metal_resistance_global_biogeography]
- Which biomes are most underrepresented in geospatial metadata remains an open question in the report. [src: metal_resistance_global_biogeography]
- The spatial analysis corrects the ENA gap interpretation: the 30.8% gap (16,964/24,511 valid pairs) is per-sample rather than geographic, reflecting samples without coordinates rather than grid cells with no samples. [src: metal_resistance_global_biogeography]
