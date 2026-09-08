---
type: Compound
description: Amino acid with a predicted biosynthesis gap in D. vulgaris
sources:
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
title: Serine
---
# Serine

## What this entity is

**Canonical name:** Serine. [^essential_metabolome]

**Known alias:** L-serine. [^essential_metabolome]

**Stable external identifier:** None reported in this document. [^essential_metabolome]

Serine is an amino acid whose biosynthesis was assessed with [gapmind](gapmind.md), a computational pathway-completeness method. [^essential_metabolome]

## Evidence from Essential Metabolome

The serine-biosynthesis pathway was predicted to be complete in 6 of 7 analyzed organisms, or 85.7%. [^essential_metabolome]

[desulfovibrio-vulgaris-hildenborough](desulfovibrio-vulgaris-hildenborough.md) was the only analyzed organism lacking a complete serine-biosynthesis pathway under the report’s criterion of GapMind predictions categorized as complete or likely_complete. [^essential_metabolome]

The result suggests the hypothesis that *Desulfovibrio vulgaris* may depend on externally supplied serine, but it does not establish serine auxotrophy because the evidence is computational and may reflect pathway-detection limitations. [^essential_metabolome]

The report interprets the possible serine auxotrophy in the context of *D. vulgaris* as an anaerobic sulfate-reducing bacterium associated with organic-rich environments where amino acids may be available from protein degradation; the proposed ecological advantage of losing an energetically costly biosynthetic capacity is explicitly an interpretation rather than a demonstrated mechanism. [^essential_metabolome]

## Limitations and validation

GapMind may miss non-canonical pathways, divergent enzymes below homology thresholds, or pathway genes absent from genome annotations, so *D. vulgaris* may possess an alternative or unannotated serine-biosynthesis route. [^essential_metabolome]

The report recommends checking for lower-confidence *D. vulgaris* serine predictions with a `steps_missing` status, reviewing experimental literature, and testing growth on serine-free minimal medium to validate the predicted auxotrophy. [^essential_metabolome]

## Related pages

- [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md) — source report containing the serine-biosynthesis analysis. [^essential_metabolome]
- [gapmind](gapmind.md) — computational method used to assess pathway completeness. [^essential_metabolome]
- [desulfovibrio-vulgaris-hildenborough](desulfovibrio-vulgaris-hildenborough.md) — organism with the predicted serine-biosynthesis gap. [^essential_metabolome]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — cross-document concept covering pathway-completeness analysis and validation. [^essential_metabolome]

[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
