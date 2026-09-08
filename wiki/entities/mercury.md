---
type: Compound
description: Mercury, a metal assessed in fitness and soil functional-genomics studies
sources:
- id: metal_specificity
  resource: ../summaries/metal_specificity__REPORT.md
  title: metal specificity
- id: microbeatlas_metal_ecology
  resource: ../summaries/microbeatlas_metal_ecology__REPORT.md
  title: microbeatlas metal ecology
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: Mercury
---
# Mercury

## What this entity is

**Canonical name:** Mercury. [^metal_specificity]

**Known aliases:** None reported in the source. [^metal_specificity]

**Stable external identifier:** None reported in the source. [^metal_specificity]

Mercury is one of the metals evaluated in the comparison of metal-specific and general-stress genes. [^metal_specificity] It was also one of nine metals measured in a soil functional-genomics analysis spanning 51,748 samples and 2,355 significant COG–metal associations at FDR < 0.05. Here, COG means a Cluster of Orthologous Groups functional category and FDR means false discovery rate. [^soil_metal_functional_genomics]

## Key facts from metal_specificity

Among the mercury-important gene records analyzed, 35 of 107 (32.7%) were classified as metal-specific, meaning that they showed significant fitness defects under metal stress but a sick rate below 5% across 5,945 non-metal experiments. [^metal_specificity]

Mercury had the lowest metal-specific fraction among the 15 metals reported in the analysis, below iron at 21.9%? No—the mercury fraction was 32.7%, while iron's fraction was 21.9%. [^metal_specificity]

The mercury result contributes to the broader finding that metal-specificity varied substantially by metal, with reported fractions ranging from 21.9% for iron to 60.6% for manganese. [^metal_specificity]

The soil analysis **refines** this fitness-based view: mercury was included in a broad observational screen of metal-associated functional shifts, but chromium and lead produced the strongest signals, so the report does not establish mercury as a leading driver of soil COG variation. [^soil_metal_functional_genomics]

## Relation to metal-resistance ecology

The MicrobeAtlas analysis **refines** the fitness-based picture by testing mercury as one component of genus-level metal-type diversity rather than as an isolated metal-specific fitness category. In leave-one-metal-out sensitivity analysis, excluding mercury retained a positive association between remaining metal-type diversity and inferred niche breadth (β = +0.0082, p = 0.233), although it was not significant after the exclusion. [^microbeatlas_metal_ecology] The report interprets the consistently positive, but power-sensitive, exclusions across all 7 metals as consistent with a distributed signal rather than dependence on mercury alone. [^microbeatlas_metal_ecology]

The soil study **supports** examining mercury within multi-metal rather than isolated-metal models, because chromium, copper, lead, and zinc co-vary in many industrial soils; however, it leaves unresolved whether individual COG associations are mercury-specific or reflect generic multi-metal contamination. Partial-correlation analyses and spatial validation are planned. [^soil_metal_functional_genomics]

This ecological result **supports** considering mercury within broader cross-metal resistance repertoires, but it does not establish that mercury-specific resistance causes wider ecological range; the association is correlational and may also reflect genome size, metabolic versatility, or gene acquisition opportunities. [^microbeatlas_metal_ecology]

## Related pages

- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — compares metal-specific determinants with genes responding to metals and other stresses. [^metal_specificity]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — provides the cross-condition fitness classification used to define metal-specific genes. [^metal_specificity]
- [environmental-resistome](../concepts/environmental-resistome.md) — places metal-resistance determinants in the broader environmental resistance landscape. [^metal_specificity]
- [metal-fitness-atlas](metal-fitness-atlas.md) — related metal-fitness resource referenced by the analysis. [^metal_specificity]
- [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) — source-project summary. [^metal_specificity]
- [microbeatlas_metal_ecology__REPORT](../summaries/microbeatlas_metal_ecology__REPORT.md) — source-project summary of phylogenetic and environmental metal-resistance ecology. [^microbeatlas_metal_ecology]
- [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md) — source-project summary of soil metal–functional-gene associations and validation limits. [^soil_metal_functional_genomics]

[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../summaries/microbeatlas_metal_ecology__REPORT.md)
