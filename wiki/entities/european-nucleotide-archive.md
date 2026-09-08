---
type: Dataset
description: ENA archive used for sample-coordinate retrieval
sources:
- id: metal_resistance_global_biogeography
  resource: ../summaries/metal_resistance_global_biogeography__REPORT.md
  title: metal resistance global biogeography
title: European Nucleotide Archive
---
# European Nucleotide Archive

## What this entity is

The European Nucleotide Archive (ENA) is the canonical dataset name used here for the archive queried through its batch API. [^metal_resistance_global_biogeography]

Known alias: ENA. [^metal_resistance_global_biogeography]

No stable external identifier for ENA was specified in the source document. [^metal_resistance_global_biogeography]

## Role in the study

The study used the ENA batch API to retrieve geospatial metadata for environmental metagenomic samples associated with MAGs from [mgnify](mgnify.md). [^metal_resistance_global_biogeography]

ENA batch API retrieval returned **24,511 sample records**, of which **16,964 (69.2%)** had valid latitude/longitude pairs. [^metal_resistance_global_biogeography]

The resulting **30.8%** coordinate gap represents samples without valid coordinates rather than geographic regions lacking archive coverage. [^metal_resistance_global_biogeography]

The ENA coordinate file covered every area represented in the MAG coordinate dataset: **0 of 532 MAG grid cells** lacked ENA coordinate coverage. [^metal_resistance_global_biogeography]

These coordinate-retrieval results inform the geographic-embedding limitations discussed in [environment-embedding-geography](../concepts/environment-embedding-geography.md). [^metal_resistance_global_biogeography]

## Source

The ENA metadata retrieval and its implications are documented in [metal_resistance_global_biogeography__REPORT](../summaries/metal_resistance_global_biogeography__REPORT.md). [^metal_resistance_global_biogeography]

[^metal_resistance_global_biogeography]: [metal resistance global biogeography](../summaries/metal_resistance_global_biogeography__REPORT.md)
