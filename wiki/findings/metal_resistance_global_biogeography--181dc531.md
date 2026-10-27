---
type: "Finding"
description: "The top hotspot was the Atacama/Andean region of Chile (lat=-25\u00b0, lon=-70\u00b0), with 21.8% prevalence, OR=9.83, q=7.6e-12, n=101 MAGs."
finding_id: "metal_resistance_global_biogeography--181dc531"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "21.8%", "what": "metal resistance prevalence in the top hotspot cell", "unit": "%", "denominator": "101 MAGs in the cell", "scope": "Atacama/Andean region, Chile (lat=-25\u00b0, lon=-70\u00b0)"}, {"value": "9.83", "what": "odds ratio for the top hotspot", "unit": "", "denominator": "", "scope": "Atacama/Andean region, Chile (lat=-25\u00b0, lon=-70\u00b0)"}, {"value": "7.6e-12", "what": "q-value for the top hotspot", "unit": "", "denominator": "", "scope": "Atacama/Andean region, Chile (lat=-25\u00b0, lon=-70\u00b0)"}, {"value": "101", "what": "MAGs in the top hotspot cell", "unit": "MAGs", "denominator": "", "scope": "Atacama/Andean region, Chile (lat=-25\u00b0, lon=-70\u00b0)"}]
caveat: "Expedition-level clustering remains untested: it is not yet known whether the Atacama (OR=9.8) and USA clusters are single-study artefacts, which would be checked using distinct sample_accession prefixes per hotspot."
first_added: "2026-10-27"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Atacama/Andean Chile is the strongest metal-resistance hotspot

The top hotspot was the Atacama/Andean region of Chile (lat=-25°, lon=-70°), with 21.8% prevalence, OR=9.83, q=7.6e-12, n=101 MAGs. [src: metal_resistance_global_biogeography]

## Key figures

- **21.8%**: metal resistance prevalence in the top hotspot cell (denominator 101 MAGs in the cell; scope Atacama/Andean region, Chile (lat=-25°, lon=-70°)) [src: metal_resistance_global_biogeography]
- **9.83**: odds ratio for the top hotspot (scope Atacama/Andean region, Chile (lat=-25°, lon=-70°)) [src: metal_resistance_global_biogeography]
- **7.6e-12**: q-value for the top hotspot (scope Atacama/Andean region, Chile (lat=-25°, lon=-70°)) [src: metal_resistance_global_biogeography]
- **101 MAGs**: MAGs in the top hotspot cell (scope Atacama/Andean region, Chile (lat=-25°, lon=-70°)) [src: metal_resistance_global_biogeography]

## Evidence

> - Top hotspot: Atacama/Andean region, Chile (lat=-25°, lon=-70°): 21.8% prevalence, OR=9.83, q=7.6e-12, n=101 MAGs. [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

Expedition-level clustering remains untested: it is not yet known whether the Atacama (OR=9.8) and USA clusters are single-study artefacts, which would be checked using distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography]

> 1. Expedition-level clustering: test if Atacama (OR=9.8) and USA clusters are single-study artefacts (check distinct sample_accession prefixes per hotspot) [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The status section calls the report preliminary and says NB02 spatial analysis and NB03 figures are pending, although later sections present NB02 results. [src: metal_resistance_global_biogeography]
- Draft map code distinguishes MAGs with n_metal_types > 0 from susceptible MAGs and colours them by metal diversity; this describes code, not a completed map result. [src: metal_resistance_global_biogeography]
- The map cell has a reported NameError because it lacks an import of matplotlib.pyplot. [src: metal_resistance_global_biogeography]
- The report describes a nonuniform distribution among 22,356 geolocated MAGs but cautions that regional interpretation requires hotspot identification and sampling-effort correction. [src: metal_resistance_global_biogeography]
- The interpretation section warns that the 30.8% ENA per-sample coordinate gap may bias global maps and leaves biome underrepresentation unresolved; later results narrow the claim that this is a geographic coverage gap. [src: metal_resistance_global_biogeography]
