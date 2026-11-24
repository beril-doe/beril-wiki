---
type: "Finding"
description: "Only 5 of 20 (25%) GC-correlated AlphaEarth PCs also discriminate isolation category by ANOVA, so for the other 75% the AlphaEarth-derived environmental signal is largely orthogonal to the categorical isolation_source signal."
finding_id: "gc_ecotype_ecology--169b6c86"
result: "null result"
source: "gc_ecotype_ecology"
quantities: [{"value": "5 of 20", "what": "GC-correlated AlphaEarth PCs also discriminating iso_category by ANOVA", "unit": "PCs", "denominator": "20 PCs", "scope": ""}, {"value": "25%", "what": "share discriminating", "unit": "", "denominator": "20 PCs", "scope": ""}]
caveat: "The AlphaEarth analysis used PCA plus Pearson, which captures only linear monotone signals and would miss nonlinear environmental relationships."
first_added: "2026-11-24"
source_hash: "f773608a1dd497c1ffa1608a83b6cc60f67d2e65041b491508a5d0dcc30163d6"
---
# AlphaEarth signal mostly orthogonal to categorical isolation source

Only 5 of 20 (25%) GC-correlated AlphaEarth PCs also discriminate isolation category by ANOVA, so for the other 75% the AlphaEarth-derived environmental signal is largely orthogonal to the categorical isolation_source signal. [src: gc_ecotype_ecology]

## Key figures

- **5 of 20 PCs**: GC-correlated AlphaEarth PCs also discriminating iso_category by ANOVA (denominator 20 PCs) [src: gc_ecotype_ecology]
- **25%**: share discriminating (denominator 20 PCs) [src: gc_ecotype_ecology]

## Evidence

> Only **5 of 20 (25%)** of the GC-correlated AE PCs simultaneously discriminate iso_category by ANOVA — meaning that for the other 75% of cases, the AlphaEarth-derived environmental signal is largely *orthogonal* to the categorical isolation_source signal. [src: gc_ecotype_ecology]

From the report [[summaries/gc_ecotype_ecology__REPORT]].

## Caveat

The AlphaEarth analysis used PCA plus Pearson, which captures only linear monotone signals and would miss nonlinear environmental relationships. [src: gc_ecotype_ecology]

> AlphaEarth analysis used PCA + Pearson which captures only linear monotone signals; non-linear environmental relationships would be missed. [src: gc_ecotype_ecology]

## Other caveats in this report

- The report states that prior within-species testing has been rare because it requires many genomes per species, genome-level environmental metadata and intra-species phylogenetic control. [src: gc_ecotype_ecology]
- The report dropped 7 species whose genomes collapsed to a single ANI cluster, and 108 species produced valid p-values. [src: gc_ecotype_ecology]
- One primary-significant species had insufficient phylogenetic coverage for the phylogenetic-regression robustness test. [src: gc_ecotype_ecology]
- The report attributes the largest partial R² values to species with many small ANI clusters, where phylogenetic control consumes most degrees of freedom and leaves small but well-determined residual variance, exemplified by Aeromonas veronii with 87 clusters of 122 genomes. [src: gc_ecotype_ecology]
- The proposed mechanistic explanations for ecological GC shifts were not directly tested in this report. [src: gc_ecotype_ecology]
