---
type: "Finding"
description: "Marine environmental MAGs are significantly depleted for metal resistance: n=13,995 MAGs, prevalence 1.2%, OR=0.20, and q=9.2e-80."
finding_id: "metal_resistance_global_biogeography--44ee4a3c"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "1.2%", "what": "prevalence in marine MAGs", "unit": "", "denominator": "", "scope": ""}, {"value": "OR=0.20", "what": "odds ratio", "unit": "", "denominator": "", "scope": ""}, {"value": "13,995", "what": "marine MAGs", "unit": "MAGs", "denominator": "", "scope": ""}, {"value": "9.2e-80", "what": "q-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Hotspot identification and sampling-effort correction are required before regional patterns among the 22,356 MAGs with coordinates can be interpreted."
first_added: "2026-11-24"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Marine MAGs are depleted for metal resistance

Marine environmental MAGs are significantly depleted for metal resistance: n=13,995 MAGs, prevalence 1.2%, OR=0.20, and q=9.2e-80. [src: metal_resistance_global_biogeography]

## Key figures

- **1.2%**: prevalence in marine MAGs [src: metal_resistance_global_biogeography]
- **OR=0.20**: odds ratio [src: metal_resistance_global_biogeography]
- **13,995 MAGs**: marine MAGs [src: metal_resistance_global_biogeography]
- **9.2e-80**: q-value [src: metal_resistance_global_biogeography]

## Evidence

> | Marine | 13,995 | 1.2% | 0.20 | 9.2e-80 | Soil is significantly enriched for metal resistance (5.8%, OR=5.05); Marine is significantly depleted (1.2%, OR=0.20). [src: metal_resistance_global_biogeography]

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
