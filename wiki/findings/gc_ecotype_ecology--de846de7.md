---
type: "Finding"
description: "The report interprets nucleotide composition as appearing more environment-responsive within species than gene presence/absence, in tension with the ecotype_analysis finding that phylogeny dominates within-species gene-content similarity."
finding_id: "gc_ecotype_ecology--de846de7"
result: "inference"
source: "gc_ecotype_ecology"
quantities: []
caveat: "The proposed mechanistic explanations for ecological GC shifts were not directly tested in this report."
first_added: "2026-11-24"
source_hash: "f773608a1dd497c1ffa1608a83b6cc60f67d2e65041b491508a5d0dcc30163d6"
---
# GC appears more environment-responsive than gene content within species

The report interprets nucleotide composition as appearing more environment-responsive within species than gene presence/absence, in tension with the ecotype_analysis finding that phylogeny dominates within-species gene-content similarity. [src: gc_ecotype_ecology]

## Evidence

> This sits in interesting tension with prior BERDL work (`ecotype_analysis`) showing phylogeny dominates *gene content* similarity within species — nucleotide composition appears more environment-responsive within species than gene presence/absence is. [src: gc_ecotype_ecology]

From the report [[summaries/gc_ecotype_ecology__REPORT]].

## Caveat

The proposed mechanistic explanations for ecological GC shifts were not directly tested in this report. [src: gc_ecotype_ecology]

> **Mechanistic candidates** (not directly tested here): [src: gc_ecotype_ecology]

## Other caveats in this report

- The report states that prior within-species testing has been rare because it requires many genomes per species, genome-level environmental metadata and intra-species phylogenetic control. [src: gc_ecotype_ecology]
- The report dropped 7 species whose genomes collapsed to a single ANI cluster, and 108 species produced valid p-values. [src: gc_ecotype_ecology]
- One primary-significant species had insufficient phylogenetic coverage for the phylogenetic-regression robustness test. [src: gc_ecotype_ecology]
- The report attributes the largest partial R² values to species with many small ANI clusters, where phylogenetic control consumes most degrees of freedom and leaves small but well-determined residual variance, exemplified by Aeromonas veronii with 87 clusters of 122 genomes. [src: gc_ecotype_ecology]
- The ecological GC result is observational and associational, and without strain-replicate transplant experiments the report cannot exclude hidden confounders such as geographic sampling bias correlated with isolation source. [src: gc_ecotype_ecology]
