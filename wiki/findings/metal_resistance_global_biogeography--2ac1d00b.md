---
type: "Finding"
description: "2.8% of the 22,356 MAGs with coordinates carry \u22651 metal resistance type, which the report says is substantially lower than implied by reporting on the 30,497 filtered MAG set."
finding_id: "metal_resistance_global_biogeography--2ac1d00b"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "2.8%", "what": "MAGs carrying \u22651 metal resistance type", "unit": "%", "denominator": "22,356 MAGs with coordinates", "scope": "global"}, {"value": "30,497", "what": "filtered MAG set that would imply a higher figure", "unit": "MAGs", "denominator": "", "scope": "filtered MAG set"}]
caveat: "The report is labelled preliminary, with NB02 spatial analysis and NB03 figures described as pending, although later sections present NB02 results."
first_added: "2026-10-27"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Metal resistance is rare among geolocated environmental MAGs

2.8% of the 22,356 MAGs with coordinates carry ≥1 metal resistance type, which the report says is substantially lower than implied by reporting on the 30,497 filtered MAG set. [src: metal_resistance_global_biogeography]

## Key figures

- **2.8%**: MAGs carrying ≥1 metal resistance type (denominator 22,356 MAGs with coordinates; scope global) [src: metal_resistance_global_biogeography]
- **30,497 MAGs**: filtered MAG set that would imply a higher figure (scope filtered MAG set) [src: metal_resistance_global_biogeography]

## Evidence

> **Global metal resistance prevalence:** 2.8% of 22,356 MAGs with coordinates carry ≥1 metal resistance type — substantially lower than implied by reporting on the 30,497 filtered MAG set. Metal resistance is rare in the global environmental MAG pool. [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

The report is labelled preliminary, with NB02 spatial analysis and NB03 figures described as pending, although later sections present NB02 results. [src: metal_resistance_global_biogeography]

> Preliminary — data extraction and coordinate retrieval complete (NB01). NB02 spatial analysis and NB03 figures pending. [src: metal_resistance_global_biogeography]

## Other caveats in this report

- Draft map code distinguishes MAGs with n_metal_types > 0 from susceptible MAGs and colours them by metal diversity; this describes code, not a completed map result. [src: metal_resistance_global_biogeography]
- The map cell has a reported NameError because it lacks an import of matplotlib.pyplot. [src: metal_resistance_global_biogeography]
- The report describes a nonuniform distribution among 22,356 geolocated MAGs but cautions that regional interpretation requires hotspot identification and sampling-effort correction. [src: metal_resistance_global_biogeography]
- The interpretation section warns that the 30.8% ENA per-sample coordinate gap may bias global maps and leaves biome underrepresentation unresolved; later results narrow the claim that this is a geographic coverage gap. [src: metal_resistance_global_biogeography]
- Expedition-level clustering remains untested; the proposed check is whether the Atacama (OR=9.8) and USA clusters are single-study artefacts, using distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography]
