---
type: Compound
description: Arsenic and its microbial resistance and soil-gene associations
sources:
- id: microbeatlas_metal_ecology
  resource: ../summaries/microbeatlas_metal_ecology__REPORT.md
  title: microbeatlas metal ecology
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: Arsenic
---
# Arsenic

## What it is

**Canonical name:** arsenic.  
**Known alias:** As. [^microbeatlas_metal_ecology]

This document does not report a stable external identifier for arsenic. [^microbeatlas_metal_ecology]

## Evidence from the MicrobeAtlas metal-ecology study

Arsenic was one of 7 metal types represented in genus-level AMRFinderPlus resistance annotations linked to GTDB data and MicrobeAtlas ecological niche breadth. [^microbeatlas_metal_ecology]

In the leave-one-metal-out sensitivity analysis, removing arsenic produced a positive but non-significant association between metal-type diversity and Levins' B_std niche breadth: β = +0.0039 and p = 0.518. [^microbeatlas_metal_ecology]

The study interpreted the persistence of a positive coefficient after excluding each of the 7 metals, including arsenic, as consistent with a distributed signal, while noting that reducing the maximum diversity score from 7 to 6 compresses predictor variance and reduces statistical power. [^microbeatlas_metal_ecology]

Arsenic was among the recommended stresses for proposed microcosm experiments targeting organisms with both broad inferred niche breadth and diverse metal-resistance repertoires. [^microbeatlas_metal_ecology]

## Evidence from soil functional genomics

A separate soil study included arsenic among 9 metals analyzed across 51,748 soil samples and identified 2,355 significant COG–metal associations at FDR < 0.05; because the results are aggregate and observational, they do not establish an arsenic-specific association. [^soil_metal_functional_genomics] This **refines** the MicrobeAtlas result by extending arsenic-related evidence from resistance annotations and niche breadth to soil functional-gene associations, while retaining the need to separate arsenic effects from co-contaminating metals. [^soil_metal_functional_genomics]

## Related pages

The study’s broader result—that diversity across metal types, rather than total AMR cluster count, was associated with broader inferred ecological ranges—feeds into [metal-cross-resistance](../concepts/metal-cross-resistance.md). [^microbeatlas_metal_ecology]

The soil study’s multi-metal associations **support** the relevance of environmental metal–gene relationships to [environmental-resistome](../concepts/environmental-resistome.md), but its co-contamination caveat prevents treating the observed signals as arsenic-specific resistance evidence. [^soil_metal_functional_genomics]

The arsenic analysis is part of the AMRFinderPlus-based environmental resistance study summarized in [microbeatlas_metal_ecology__REPORT](../summaries/microbeatlas_metal_ecology__REPORT.md). [^microbeatlas_metal_ecology]

The soil functional-gene analysis is summarized in [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md). [^soil_metal_functional_genomics]

Related methods and data resources include [amrfinderplus](amrfinderplus.md), [gtdb](gtdb.md), and [microbial-atlas](microbial-atlas.md). [^microbeatlas_metal_ecology]

[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../summaries/microbeatlas_metal_ecology__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
