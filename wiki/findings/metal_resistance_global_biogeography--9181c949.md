---
type: "Finding"
description: "The report finds soil significantly enriched for metal resistance (5.8%, OR=5.05) and marine significantly depleted (1.2%, OR=0.20)."
finding_id: "metal_resistance_global_biogeography--9181c949"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "5.8%", "what": "metal resistance prevalence in soil", "unit": "%", "denominator": "", "scope": "OR=5.05"}, {"value": "1.2%", "what": "metal resistance prevalence in marine samples", "unit": "%", "denominator": "", "scope": "OR=0.20"}]
caveat: "Hotspot identification and sampling-effort correction are required before regional patterns among the 22,356 geolocated MAGs can be interpreted."
first_added: "2026-10-27"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Soil is enriched and marine depleted for metal resistance

The report finds soil significantly enriched for metal resistance (5.8%, OR=5.05) and marine significantly depleted (1.2%, OR=0.20). [src: metal_resistance_global_biogeography]

## Key figures

- **5.8%**: metal resistance prevalence in soil (scope OR=5.05) [src: metal_resistance_global_biogeography]
- **1.2%**: metal resistance prevalence in marine samples (scope OR=0.20) [src: metal_resistance_global_biogeography]

## Evidence

> Soil is significantly enriched for metal resistance (5.8%, OR=5.05); Marine is significantly depleted (1.2%, OR=0.20). [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

Hotspot identification and sampling-effort correction are required before regional patterns among the 22,356 geolocated MAGs can be interpreted. [src: metal_resistance_global_biogeography]

> Among the 22,356 MAGs with coordinates, metal-resistant genomes are not uniformly distributed, but hotspot identification and sampling-effort correction are required before regional patterns can be interpreted (NB02). [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The status section calls the report preliminary and says NB02 spatial analysis and NB03 figures are pending, although later sections present NB02 results. [src: metal_resistance_global_biogeography]
- Draft map code distinguishes MAGs with n_metal_types > 0 from susceptible MAGs and colours them by metal diversity; this describes code, not a completed map result. [src: metal_resistance_global_biogeography]
- The map cell has a reported NameError because it lacks an import of matplotlib.pyplot. [src: metal_resistance_global_biogeography]
- The interpretation section warns that the 30.8% ENA per-sample coordinate gap may bias global maps and leaves biome underrepresentation unresolved; later results narrow the claim that this is a geographic coverage gap. [src: metal_resistance_global_biogeography]
- Expedition-level clustering remains untested; the proposed check is whether the Atacama (OR=9.8) and USA clusters are single-study artefacts, using distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography]
