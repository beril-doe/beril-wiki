---
type: "Finding"
description: "0 of 532 MAG grid cells lack ENA coordinate coverage, so the 30.8% gap (16,964/24,511 valid pairs) is a per-sample gap rather than a geographic gap, narrowing the earlier geographic-blind-spots interpretation."
finding_id: "metal_resistance_global_biogeography--a6cb44ef"
result: "null result"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "0 of 532", "what": "MAG grid cells lacking ENA coordinate coverage", "unit": "cells", "denominator": "532 MAG grid cells", "scope": ""}, {"value": "30.8%", "what": "per-sample ENA coordinate gap", "unit": "%", "denominator": "24,511 ENA sample records (16,964 valid pairs)", "scope": ""}]
caveat: "The interpretation section still warns that the 30.8% ENA coordinate gap may bias global maps and leaves unresolved which biomes are most underrepresented."
first_added: "2026-10-27"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# ENA coordinate gap is per-sample, not geographic

0 of 532 MAG grid cells lack ENA coordinate coverage, so the 30.8% gap (16,964/24,511 valid pairs) is a per-sample gap rather than a geographic gap, narrowing the earlier geographic-blind-spots interpretation. [src: metal_resistance_global_biogeography]

## Key figures

- **0 of 532 cells**: MAG grid cells lacking ENA coordinate coverage (denominator 532 MAG grid cells) [src: metal_resistance_global_biogeography]
- **30.8%**: per-sample ENA coordinate gap (denominator 24,511 ENA sample records (16,964 valid pairs)) [src: metal_resistance_global_biogeography]

## Evidence

> **ENA coordinate gap:** 0 of 532 MAG grid cells lack ENA coordinate coverage — the ENA coordinate file already covers all areas represented in the MAG coordinate dataset. The 30.8% gap (16,964/24,511 valid pairs) is a per-sample gap, not a geographic gap; it reflects samples without coordinates, not grid cells with no samples at all. [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

The interpretation section still warns that the 30.8% ENA coordinate gap may bias global maps and leaves unresolved which biomes are most underrepresented. [src: metal_resistance_global_biogeography]

> The 30.8% ENA coordinate gap is a data quality finding independent of the biological question: it implies that any global map of metal resistance distribution based on public archives is subject to substantial geographic blind spots. Which biomes are most underrepresented is a key open question. [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The status section calls the report preliminary and says NB02 spatial analysis and NB03 figures are pending, although later sections present NB02 results. [src: metal_resistance_global_biogeography]
- Draft map code distinguishes MAGs with n_metal_types > 0 from susceptible MAGs and colours them by metal diversity; this describes code, not a completed map result. [src: metal_resistance_global_biogeography]
- The map cell has a reported NameError because it lacks an import of matplotlib.pyplot. [src: metal_resistance_global_biogeography]
- The report describes a nonuniform distribution among 22,356 geolocated MAGs but cautions that regional interpretation requires hotspot identification and sampling-effort correction. [src: metal_resistance_global_biogeography]
- Expedition-level clustering remains untested; the proposed check is whether the Atacama (OR=9.8) and USA clusters are single-study artefacts, using distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography]
