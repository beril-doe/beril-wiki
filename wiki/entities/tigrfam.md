---
type: "Dataset"
description: "TIGRFam annotation dataset used for fitness-module predictions"
sources: ["summaries/fitness_modules__REPORT.md"]
---
# TIGRFam

## What this entity is

**Canonical name:** TIGRFam.  
**Known aliases:** None stated in the source.  
**Stable external identifier:** None reported in the source. [src: fitness_modules]

TIGRFam was one of the annotation sources used alongside KEGG, SEED, and PFam to generate function predictions from fitness modules. [src: fitness_modules]

## Key facts from fitness_modules

The report used TIGRFam enrichment to support function predictions for hypothetical proteins across 32 organisms, contributing to a total of 6,691 predictions. [src: fitness_modules]

Of the 6,691 hypothetical-protein predictions, 2,455 were family-backed predictions, representing 37% of the total and carrying cross-organism conservation support; the source does not provide a TIGRFam-specific count within these categories. [src: fitness_modules]

TIGRFam was applied in a workflow where [[entities/independent-component-analysis|independent component analysis]] identified process-level fitness modules, while sequence-based ortholog transfer remained substantially stronger for predicting specific molecular functions. [src: fitness_modules]

The report cautions that module-based predictions should be interpreted as biological-process context rather than definitive gene-level function assignments, because Module-ICA had less than 1% strict precision for KEGG KO assignments. [src: fitness_modules]

## Related pages

- [[summaries/fitness_modules__REPORT]] — source summary for the TIGRFam-enabled fitness-module analysis. [src: fitness_modules]
- [[concepts/cofitness-network-architecture]] — cofitness modules and their process-level annotation context. [src: fitness_modules]
- [[concepts/pangenome-integration]] — cross-organism ortholog alignment and conserved module families. [src: fitness_modules]
