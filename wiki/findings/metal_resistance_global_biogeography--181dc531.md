---
type: "Finding"
description: "The top environmental MAG metal-resistance hotspot is the Atacama/Andean region, Chile (lat=-25\u00b0, lon=-70\u00b0), with 21.8% prevalence, OR=9.83, q=7.6e-12, and n=101 MAGs."
finding_id: "metal_resistance_global_biogeography--181dc531"
result: "observation"
source: "metal_resistance_global_biogeography"
quantities: [{"value": "21.8%", "what": "metal resistance prevalence at hotspot", "unit": "", "denominator": "", "scope": ""}, {"value": "OR=9.83", "what": "odds ratio", "unit": "", "denominator": "", "scope": ""}, {"value": "q=7.6e-12", "what": "significance", "unit": "", "denominator": "", "scope": ""}, {"value": "n=101", "what": "MAGs in the cell", "unit": "MAGs", "denominator": "", "scope": ""}]
caveat: "The report plans to test whether the Atacama hotspot (OR=9.8) and USA clusters are single-study artefacts by checking distinct sample_accession prefixes per hotspot."
first_added: "2026-11-24"
source_hash: "b0f55ad895a38acb546b33895f438128175fe7ebe53480136798c601a8137317"
---
# Atacama/Andean Chile is the top metal-resistance hotspot

The top environmental MAG metal-resistance hotspot is the Atacama/Andean region, Chile (lat=-25°, lon=-70°), with 21.8% prevalence, OR=9.83, q=7.6e-12, and n=101 MAGs. [src: metal_resistance_global_biogeography]

## Key figures

- **21.8%**: metal resistance prevalence at hotspot [src: metal_resistance_global_biogeography]
- **OR=9.83**: odds ratio [src: metal_resistance_global_biogeography]
- **q=7.6e-12**: significance [src: metal_resistance_global_biogeography]
- **n=101 MAGs**: MAGs in the cell [src: metal_resistance_global_biogeography]

## Evidence

> - Top hotspot: Atacama/Andean region, Chile (lat=-25°, lon=-70°): 21.8% prevalence, OR=9.83, q=7.6e-12, n=101 MAGs. [src: metal_resistance_global_biogeography]

From the report [[summaries/metal_resistance_global_biogeography__REPORT]].

## Caveat

The report plans to test whether the Atacama hotspot (OR=9.8) and USA clusters are single-study artefacts by checking distinct sample_accession prefixes per hotspot. [src: metal_resistance_global_biogeography]

> 1. Expedition-level clustering: test if Atacama (OR=9.8) and USA clusters are single-study artefacts (check distinct sample_accession prefixes per hotspot) [src: metal_resistance_global_biogeography]

## Other caveats in this report

- The report labels its status preliminary, with data extraction and coordinate retrieval complete in NB01 but NB02 spatial analysis and NB03 figures pending. [src: metal_resistance_global_biogeography]
- The drafted global map cell has a NameError caused by a missing import matplotlib.pyplot, which requires fixing before NB02. [src: metal_resistance_global_biogeography]
- The report requires hotspot identification and sampling-effort correction before interpreting regional metal-resistance patterns in the georeferenced environmental MAG dataset. [src: metal_resistance_global_biogeography]
- The report initially interprets the 30.8% ENA coordinate gap as substantial geographic blind spots for public-archive global metal-resistance maps, independently of the biological question. [src: metal_resistance_global_biogeography]
- Which biomes are most underrepresented in geospatial metadata remains an open question in the report. [src: metal_resistance_global_biogeography]
