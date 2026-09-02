---
type: "Compound"
description: "Amino acid with a predicted biosynthesis gap in D. vulgaris"
sources: ["summaries/essential_metabolome__REPORT.md"]
---
# Serine

## What this entity is

**Canonical name:** Serine. [src: essential_metabolome]

**Known alias:** L-serine. [src: essential_metabolome]

**Stable external identifier:** None reported in this document. [src: essential_metabolome]

Serine is an amino acid whose biosynthesis was assessed with [[entities/gapmind]], a computational pathway-completeness method. [src: essential_metabolome]

## Evidence from Essential Metabolome

The serine-biosynthesis pathway was predicted to be complete in 6 of 7 analyzed organisms, or 85.7%. [src: essential_metabolome]

[[entities/desulfovibrio-vulgaris-hildenborough]] was the only analyzed organism lacking a complete serine-biosynthesis pathway under the report’s criterion of GapMind predictions categorized as complete or likely_complete. [src: essential_metabolome]

The result suggests the hypothesis that *Desulfovibrio vulgaris* may depend on externally supplied serine, but it does not establish serine auxotrophy because the evidence is computational and may reflect pathway-detection limitations. [src: essential_metabolome]

The report interprets the possible serine auxotrophy in the context of *D. vulgaris* as an anaerobic sulfate-reducing bacterium associated with organic-rich environments where amino acids may be available from protein degradation; the proposed ecological advantage of losing an energetically costly biosynthetic capacity is explicitly an interpretation rather than a demonstrated mechanism. [src: essential_metabolome]

## Limitations and validation

GapMind may miss non-canonical pathways, divergent enzymes below homology thresholds, or pathway genes absent from genome annotations, so *D. vulgaris* may possess an alternative or unannotated serine-biosynthesis route. [src: essential_metabolome]

The report recommends checking for lower-confidence *D. vulgaris* serine predictions with a `steps_missing` status, reviewing experimental literature, and testing growth on serine-free minimal medium to validate the predicted auxotrophy. [src: essential_metabolome]

## Related pages

- [[summaries/essential_metabolome__REPORT]] — source report containing the serine-biosynthesis analysis. [src: essential_metabolome]
- [[entities/gapmind]] — computational method used to assess pathway completeness. [src: essential_metabolome]
- [[entities/desulfovibrio-vulgaris-hildenborough]] — organism with the predicted serine-biosynthesis gap. [src: essential_metabolome]
- [[concepts/metabolic-model-gapfilling]] — cross-document concept covering pathway-completeness analysis and validation. [src: essential_metabolome]
