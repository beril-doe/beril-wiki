---
type: "Finding"
description: "0 of 532 MAG grid cells lack ENA coordinate coverage, so the ENA coordinate file already covers all areas represented in the MAG coordinate dataset, revising the earlier reading of the ENA gap as geographic blind spots."
finding_id: "metal_resistance_global_biogeography--64374219"
result: "correction"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "0 of 532", "what": "MAG grid cells lacking ENA coordinate coverage", "unit": "grid cells", "denominator": "", "scope": ""}]
caveat: "The 30.8% gap (16,964/24,511 valid pairs) is a per-sample gap, not a geographic gap; it reflects samples without coordinates, not grid cells with no samples at all."
first_added: "2026-11-24"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# ENA coordinate gap is per-sample, not geographic

0 of 532 MAG grid cells lack ENA coordinate coverage, so the ENA coordinate file already covers all areas represented in the MAG coordinate dataset, revising the earlier reading of the ENA gap as geographic blind spots. [src: metal_resistance_global_biogeography]

## Key figures

- **0 of 532 grid cells**: MAG grid cells lacking ENA coordinate coverage [src: metal_resistance_global_biogeography]

## Evidence

> **ENA coordinate gap:** 0 of 532 MAG grid cells lack ENA coordinate coverage — the ENA coordinate file already covers all areas represented in the MAG coordinate dataset. [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

The 30.8% gap (16,964/24,511 valid pairs) is a per-sample gap, not a geographic gap; it reflects samples without coordinates, not grid cells with no samples at all. [src: metal_resistance_global_biogeography]

> The 30.8% gap (16,964/24,511 valid pairs) is a per-sample gap, not a geographic gap; it reflects samples without coordinates, not grid cells with no samples at all. [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The report labels its status preliminary, with data extraction and coordinate retrieval complete in NB01 but NB02 spatial analysis and NB03 figures pending. [src: metal_resistance_global_biogeography]
- The drafted global map cell has a NameError caused by a missing import matplotlib.pyplot, which requires fixing before NB02. [src: metal_resistance_global_biogeography]
- The report requires hotspot identification and sampling-effort correction before interpreting regional metal-resistance patterns in the georeferenced environmental MAG dataset. [src: metal_resistance_global_biogeography]
- The report initially interprets the 30.8% ENA coordinate gap as substantial geographic blind spots for public-archive global metal-resistance maps, independently of the biological question. [src: metal_resistance_global_biogeography]
- Which biomes are most underrepresented in geospatial metadata remains an open question in the report. [src: metal_resistance_global_biogeography]
