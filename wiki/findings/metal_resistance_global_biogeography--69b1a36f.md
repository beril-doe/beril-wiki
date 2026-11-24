---
type: "Finding"
description: "Soil environmental MAGs are significantly enriched for metal resistance: n=7,939 MAGs, prevalence 5.8%, OR=5.05, and q=1.8e-82."
finding_id: "metal_resistance_global_biogeography--69b1a36f"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "5.8%", "what": "prevalence in soil MAGs", "unit": "", "denominator": "", "scope": ""}, {"value": "OR=5.05", "what": "odds ratio", "unit": "", "denominator": "", "scope": ""}, {"value": "7,939", "what": "soil MAGs", "unit": "MAGs", "denominator": "", "scope": ""}, {"value": "1.8e-82", "what": "q-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Hotspot identification and sampling-effort correction are required before regional patterns among the 22,356 MAGs with coordinates can be interpreted."
first_added: "2026-11-24"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Soil MAGs are enriched for metal resistance

Soil environmental MAGs are significantly enriched for metal resistance: n=7,939 MAGs, prevalence 5.8%, OR=5.05, and q=1.8e-82. [src: metal_resistance_global_biogeography]

## Key figures

- **5.8%**: prevalence in soil MAGs [src: metal_resistance_global_biogeography]
- **OR=5.05**: odds ratio [src: metal_resistance_global_biogeography]
- **7,939 MAGs**: soil MAGs [src: metal_resistance_global_biogeography]
- **1.8e-82**: q-value [src: metal_resistance_global_biogeography]

## Evidence

> | Soil | 7,939 | 5.8% | 5.05 | 1.8e-82 | | Rhizosphere | 422 | 1.9% | 0.66 | 0.30 (NS) | | Marine | 13,995 | 1.2% | 0.20 | 9.2e-80 | Soil is significantly enriched for metal resistance (5.8%, OR=5.05); Marine is significantly depleted (1.2%, OR=0.20). [src: metal_resistance_global_biogeography]

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
