---
type: "Finding"
description: "Across 108 bacterial species in the KBase Data Lakehouse pangenome (each with \u2265 50 quality-filtered genomes across \u2265 2 environmental categories with \u2265 10 genomes each), 40 species (37%) show within-species GC content variation significantly associated with isolation source after controlling for intra-species phylogeny (ANI cluster) at FDR < 0.05."
finding_id: "gc_ecotype_ecology--407ce45e"
result: "observation"
source: "gc_ecotype_ecology"
quantities: [{"value": "108", "what": "bacterial species tested", "unit": "species", "denominator": "", "scope": "KBase Data Lakehouse pangenome"}, {"value": "40", "what": "species with significant isolation-source-associated GC variation", "unit": "species", "denominator": "108 species", "scope": "FDR < 0.05 after ANI cluster control"}, {"value": "37%", "what": "share of tested species significant", "unit": "", "denominator": "108 species", "scope": ""}]
caveat: "The result is associational and observational, and without strain-replicate transplant experiments hidden confounders such as geographic sampling bias correlated with isolation source cannot be ruled out."
first_added: "2026-11-24"
source_hash: "f773608a1dd497c1ffa1608a83b6cc60f67d2e65041b491508a5d0dcc30163d6"
---
# Within-species GC varies with isolation source in many bacterial species

Across 108 bacterial species in the KBase Data Lakehouse pangenome (each with ≥ 50 quality-filtered genomes across ≥ 2 environmental categories with ≥ 10 genomes each), 40 species (37%) show within-species GC content variation significantly associated with isolation source after controlling for intra-species phylogeny (ANI cluster) at FDR < 0.05. [src: gc_ecotype_ecology]

## Key figures

- **108 species**: bacterial species tested (scope KBase Data Lakehouse pangenome) [src: gc_ecotype_ecology]
- **40 species**: species with significant isolation-source-associated GC variation (denominator 108 species; scope FDR < 0.05 after ANI cluster control) [src: gc_ecotype_ecology]
- **37%**: share of tested species significant (denominator 108 species) [src: gc_ecotype_ecology]

## Evidence

> Across **108 bacterial species** spanning the BERDL pangenome (each represented by ≥ 50 quality-filtered genomes across ≥ 2 environmental categories with ≥ 10 genomes each), **40 species (37%)** show within-species GC content variation that is significantly associated with isolation source **after controlling for intra-species phylogeny (ANI cluster) at FDR < 0.05**. [src: gc_ecotype_ecology]

From the report [[summaries/gc_ecotype_ecology__REPORT]].

## Caveat

The result is associational and observational, and without strain-replicate transplant experiments hidden confounders such as geographic sampling bias correlated with isolation source cannot be ruled out. [src: gc_ecotype_ecology]

> **Boundary of the claim**: this is an associational, observational result. Without strain-replicate transplant experiments we cannot rule out hidden confounders — for example, geographic sampling bias correlated with isolation source. [src: gc_ecotype_ecology]

## Other caveats in this report

- The report states that prior within-species testing has been rare because it requires many genomes per species, genome-level environmental metadata and intra-species phylogenetic control. [src: gc_ecotype_ecology]
- The report dropped 7 species whose genomes collapsed to a single ANI cluster, and 108 species produced valid p-values. [src: gc_ecotype_ecology]
- One primary-significant species had insufficient phylogenetic coverage for the phylogenetic-regression robustness test. [src: gc_ecotype_ecology]
- The report attributes the largest partial R² values to species with many small ANI clusters, where phylogenetic control consumes most degrees of freedom and leaves small but well-determined residual variance, exemplified by Aeromonas veronii with 87 clusters of 122 genomes. [src: gc_ecotype_ecology]
- The proposed mechanistic explanations for ecological GC shifts were not directly tested in this report. [src: gc_ecotype_ecology]
