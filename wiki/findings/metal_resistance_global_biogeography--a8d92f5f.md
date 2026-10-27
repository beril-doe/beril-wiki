---
type: "Finding"
description: "Across 289 cells with \u22655 MAGs in the 5\u00b0 grid analysis, Fisher's exact tests with BH FDR correction identified 11 significant hotspots (OR>2, q<0.05) and 3 coldspots (OR<0.5, q<0.05)."
finding_id: "metal_resistance_global_biogeography--a8d92f5f"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "289", "what": "5\u00b0 grid cells with \u22655 MAGs tested", "unit": "cells", "denominator": "", "scope": ""}, {"value": "11", "what": "significant hotspots (OR>2, q<0.05)", "unit": "cells", "denominator": "", "scope": ""}, {"value": "3", "what": "coldspots (OR<0.5, q<0.05)", "unit": "cells", "denominator": "", "scope": ""}]
caveat: "Whether hotspots persist after correcting for sampling effort by normalising by log(n_MAGs) remains to be tested."
first_added: "2026-10-27"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Metal resistance clusters in a few significant grid-cell hotspots

Across 289 cells with ≥5 MAGs in the 5° grid analysis, Fisher's exact tests with BH FDR correction identified 11 significant hotspots (OR>2, q<0.05) and 3 coldspots (OR<0.5, q<0.05). [src: metal_resistance_global_biogeography]

## Key figures

- **289 cells**: 5° grid cells with ≥5 MAGs tested [src: metal_resistance_global_biogeography]
- **11 cells**: significant hotspots (OR>2, q<0.05) [src: metal_resistance_global_biogeography]
- **3 cells**: coldspots (OR<0.5, q<0.05) [src: metal_resistance_global_biogeography]

## Evidence

> **5° grid hotspot analysis** (289 cells with ≥5 MAGs; Fisher's exact, BH FDR): - **11 significant hotspots** (OR>2, q<0.05), **3 coldspots** (OR<0.5, q<0.05). [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

Whether hotspots persist after correcting for sampling effort by normalising by log(n_MAGs) remains to be tested. [src: metal_resistance_global_biogeography]

> 2. Sampling effort correction: confirm hotspots persist after normalising by log(n_MAGs) [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The status section calls the report preliminary and says NB02 spatial analysis and NB03 figures are pending, although later sections present NB02 results. [src: metal_resistance_global_biogeography]
- Draft map code distinguishes MAGs with n_metal_types > 0 from susceptible MAGs and colours them by metal diversity; this describes code, not a completed map result. [src: metal_resistance_global_biogeography]
- The map cell has a reported NameError because it lacks an import of matplotlib.pyplot. [src: metal_resistance_global_biogeography]
- The report describes a nonuniform distribution among 22,356 geolocated MAGs but cautions that regional interpretation requires hotspot identification and sampling-effort correction. [src: metal_resistance_global_biogeography]
- The interpretation section warns that the 30.8% ENA per-sample coordinate gap may bias global maps and leaves biome underrepresentation unresolved; later results narrow the claim that this is a geographic coverage gap. [src: metal_resistance_global_biogeography]
