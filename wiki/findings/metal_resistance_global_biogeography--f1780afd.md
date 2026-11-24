---
type: "Finding"
description: "Rhizosphere environmental MAG metal-resistance prevalence is not significantly different from the global baseline: n=422 MAGs, prevalence 1.9%, OR=0.66, and q=0.30 (NS)."
finding_id: "metal_resistance_global_biogeography--f1780afd"
result: "null result"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "1.9%", "what": "prevalence in rhizosphere MAGs", "unit": "", "denominator": "", "scope": ""}, {"value": "OR=0.66", "what": "odds ratio", "unit": "", "denominator": "", "scope": ""}, {"value": "0.30", "what": "q-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Hotspot identification and sampling-effort correction are required before regional patterns among the 22,356 MAGs with coordinates can be interpreted."
first_added: "2026-11-24"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Rhizosphere MAGs show no significant metal-resistance difference

Rhizosphere environmental MAG metal-resistance prevalence is not significantly different from the global baseline: n=422 MAGs, prevalence 1.9%, OR=0.66, and q=0.30 (NS). [src: metal_resistance_global_biogeography]

## Key figures

- **1.9%**: prevalence in rhizosphere MAGs [src: metal_resistance_global_biogeography]
- **OR=0.66**: odds ratio [src: metal_resistance_global_biogeography]
- **0.30**: q-value [src: metal_resistance_global_biogeography]

## Evidence

> | Rhizosphere | 422 | 1.9% | 0.66 | 0.30 (NS) | [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

Hotspot identification and sampling-effort correction are required before regional patterns among the 22,356 MAGs with coordinates can be interpreted. [src: metal_resistance_global_biogeography]

> Among the 22,356 MAGs with coordinates, metal-resistant genomes are not uniformly distributed, but hotspot identification and sampling-effort correction are required before regional patterns can be interpreted (NB02). [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The report labels its status preliminary, with data extraction and coordinate retrieval complete in NB01 but NB02 spatial analysis and NB03 figures pending. [src: metal_resistance_global_biogeography]
- The drafted global map cell has a NameError caused by a missing import matplotlib.pyplot, which requires fixing before NB02. [src: metal_resistance_global_biogeography]
- The report initially interprets the 30.8% ENA coordinate gap as substantial geographic blind spots for public-archive global metal-resistance maps, independently of the biological question. [src: metal_resistance_global_biogeography]
- Which biomes are most underrepresented in geospatial metadata remains an open question in the report. [src: metal_resistance_global_biogeography]
- The spatial analysis corrects the ENA gap interpretation: the 30.8% gap (16,964/24,511 valid pairs) is per-sample rather than geographic, reflecting samples without coordinates rather than grid cells with no samples. [src: metal_resistance_global_biogeography]
