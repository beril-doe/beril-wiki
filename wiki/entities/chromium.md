---
type: Compound
description: Metal associated with fitness specificity and soil functional-gene shifts
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
title: Chromium
---
# Chromium

## What this entity is

**Canonical name:** Chromium. [^metal_specificity]

**Known alias:** Cr. [^metal_specificity]

**Stable external identifier:** Not specified in the source report. [^metal_specificity]

## Key facts

Chromium was one of the metals evaluated in a comparison of metal-important genes with fitness defects across metal and non-metal experiments. [^metal_specificity]

Of the chromium-associated metal-important gene records analyzed, 132 of 268 (49.3%) were classified as metal-specific, meaning that they showed significant fitness defects under metal stress but a sick rate below 5% across 5,945 non-metal experiments. [^metal_specificity]

This chromium result contributes to the broader distinction between metal-specific determinants and general stress genes in [metal-cross-resistance](../concepts/metal-cross-resistance.md). [^metal_specificity]

A separate soil metagenomic analysis found chromium among nine metals associated with 2,355 significant COG–metal associations at FDR < 0.05 across 51,748 samples; chromium and lead produced the strongest signals, with transporters and biosynthesis genes dominating the top hits. These observational results **support** chromium’s relevance to environmental functional-gene distributions but **refine** the fitness-based specificity claims: co-varying chromium, copper, lead, and zinc leave it unresolved whether individual associations are chromium-specific or reflect multi-metal contamination. [^soil_metal_functional_genomics]

A separate genus-level PGLS analysis found that the association between metal-type diversity and inferred niche breadth remained positive after chromium was excluded (β = +0.0088, p = 0.173). This **refines** the cross-metal resistance interpretation: the overall signal was directionally distributed across metals, but exclusion of any one metal reduced significance and also compressed the maximum diversity score from 7 to 6, reducing predictor variance and power. [^microbeatlas_metal_ecology]

Chromium was also among the recommended stresses for follow-up microcosm experiments testing candidate broad-niche, metal-diverse OTUs. [^microbeatlas_metal_ecology]

The cross-condition classification of chromium-associated genes is part of the analysis summarized in [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) and relates to [condition-specific-fitness](../concepts/condition-specific-fitness.md). [^metal_specificity]

The ecological chromium analysis is summarized in [microbeatlas_metal_ecology__REPORT](../summaries/microbeatlas_metal_ecology__REPORT.md) and connects to [environmental-resistome](../concepts/environmental-resistome.md) and [environment-embedding-geography](../concepts/environment-embedding-geography.md). [^microbeatlas_metal_ecology]

The soil functional-genomics analysis is summarized in [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md). Its planned partial-correlation analysis and effect-size audit are needed before the chromium-associated COG signals can be interpreted as metal-specific or biologically substantial. [^soil_metal_functional_genomics]

## Related pages

- [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) — source-project summary.
- [microbeatlas_metal_ecology__REPORT](../summaries/microbeatlas_metal_ecology__REPORT.md) — cross-metal resistance and ecological niche-breadth analysis.
- [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md) — soil metal–functional-gene associations and validation caveats.
- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — metal-specific versus broadly stress-responsive fitness determinants.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — classification of fitness defects by experimental condition.
- [environmental-resistome](../concepts/environmental-resistome.md) — environmental distributions of resistance repertoires.
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — links between resistance traits and environmental distributions.
- [metal-fitness-atlas](metal-fitness-atlas.md) — related metal-fitness data resource.

[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../summaries/microbeatlas_metal_ecology__REPORT.md)
