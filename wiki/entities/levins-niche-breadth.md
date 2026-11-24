---
type: "Method"
description: "A standardised index (B_std) of how evenly a taxon is distributed across habitat categories, here computed per genus from MicrobeAtlas habitat categories."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
aliases: ["B_std", "Levins' B", "Levins' B_std"]
---
# Levins' niche breadth

Levins' B_std was computed per genus from MicrobeAtlas Env_Level_1 habitat categories rather than from soil chemistry. [src: comprehensive_metal_ecology] The evidence on this page is methodological: how the index was built, how it behaved, and what limits it.

## Key facts

- The choice of habitat categories keeps the niche-breadth and metal-concentration axes independent. [src: comprehensive_metal_ecology]
- In the microbeatlas_metal_ecology report, bacterial Levins' B_std has Pagel's λ of 0.787 (p = 7.9×10⁻¹⁰² by likelihood ratio test, LRT) across 1,264 genera. [src: microbeatlas_metal_ecology]
- The raw ordinary least squares (OLS) correlation between mean metal type diversity and Levins' B_std is modest (r ≈ 0.21). The report says this reflects baseline phylogenetic structure in both variables. [src: microbeatlas_metal_ecology]
- The report's leave-one-environment-out analysis excluded each of 13 [[entities/microbeatlas]] categories in turn. It row-normalised prevalences over the remaining 12 environments, recomputed B_std with J=12, and reran phylogenetic generalized least squares (PGLS). [src: microbeatlas_metal_ecology]
- A stricter variant counts an operational taxonomic unit (OTU) as present in an environment only if it appears in ≥5% of samples in that category. This is meant to reduce detections from contamination, cross-sample bleed-through, or rare transient events. [src: microbeatlas_metal_ecology]

## Caveats

- B_std corrects for unequal environment sizes. It cannot correct for missing environments or for differing detection probabilities. [src: microbeatlas_metal_ecology]
- B_std from 16S OTUs may contain noise from coarse OTU–genus matching and MicrobeAtlas annotations. [src: comprehensive_metal_ecology]
- Genera detected in fewer MicrobeAtlas samples may have less reliable estimates. [src: comprehensive_metal_ecology]
- Genus-level aggregation of OTU niche scores is a proxy. A genus may look broad-niched because different species occupy different habitats, not because any one organism is a true generalist. [src: microbeatlas_metal_ecology]

See [[concepts/robustness-and-replication-of-niche-breadth-associations]] and [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]] for how the index is used.
