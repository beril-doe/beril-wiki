---
type: "Finding"
description: "Under continuous phylogenetic regression (top-10 PCoA axes of pairwise branch distance in place of the ANI cluster dummy), 32 species (82%) of 39 testable species remain p < 0.05, which the report reads as showing the signal is not an artifact of the clone-cluster definition."
finding_id: "gc_ecotype_ecology--3541499c"
result: "observation"
source: "gc_ecotype_ecology"
quantities: [{"value": "32", "what": "species remaining significant", "unit": "species", "denominator": "39 testable species", "scope": "phylogenetic regression"}, {"value": "82%", "what": "share remaining significant", "unit": "", "denominator": "39 testable species", "scope": ""}]
caveat: "One primary-significant species had insufficient phylogenetic coverage, so only 39 species were testable."
first_added: "2026-11-24"
source_hash: "f773608a1dd497c1ffa1608a83b6cc60f67d2e65041b491508a5d0dcc30163d6"
---
# Signal persists under continuous phylogenetic regression instead of ANI clusters

Under continuous phylogenetic regression (top-10 PCoA axes of pairwise branch distance in place of the ANI cluster dummy), 32 species (82%) of 39 testable species remain p < 0.05, which the report reads as showing the signal is not an artifact of the clone-cluster definition. [src: gc_ecotype_ecology]

## Key figures

- **32 species**: species remaining significant (denominator 39 testable species; scope phylogenetic regression) [src: gc_ecotype_ecology]
- **82%**: share remaining significant (denominator 39 testable species) [src: gc_ecotype_ecology]

## Evidence

> - **Phylogenetic regression** (continuous PCoA from per-species pairwise `branch_distance` in `phylogenetic_tree_distance_pairs`, top-10 axes used in place of the ANI cluster dummy): of 39 species testable (one had insufficient phylo coverage), **32 species (82%) remain p < 0.05**. The signal is not an artifact of the clone-cluster definition. [src: gc_ecotype_ecology]

From the report [[summaries/gc_ecotype_ecology__REPORT]].

## Caveat

One primary-significant species had insufficient phylogenetic coverage, so only 39 species were testable. [src: gc_ecotype_ecology]

> of 39 species testable (one had insufficient phylo coverage) [src: gc_ecotype_ecology]

## Other caveats in this report

- The report states that prior within-species testing has been rare because it requires many genomes per species, genome-level environmental metadata and intra-species phylogenetic control. [src: gc_ecotype_ecology]
- The report dropped 7 species whose genomes collapsed to a single ANI cluster, and 108 species produced valid p-values. [src: gc_ecotype_ecology]
- The report attributes the largest partial R² values to species with many small ANI clusters, where phylogenetic control consumes most degrees of freedom and leaves small but well-determined residual variance, exemplified by Aeromonas veronii with 87 clusters of 122 genomes. [src: gc_ecotype_ecology]
- The proposed mechanistic explanations for ecological GC shifts were not directly tested in this report. [src: gc_ecotype_ecology]
- The ecological GC result is observational and associational, and without strain-replicate transplant experiments the report cannot exclude hidden confounders such as geographic sampling bias correlated with isolation source. [src: gc_ecotype_ecology]
