---
type: "Method"
description: "Index for identifying spatial gaps in soil genomic representation"
sources: ["summaries/soil_frontier_genomics__REPORT.md"]
---
# Genomic Discovery Index

## What this entity is

The **Genomic Discovery Index (GDI)** is a method for characterizing spatial gaps in genomic representation by dividing OTU richness by mean genome completeness plus 1. [src: soil_frontier_genomics]

**Canonical name:** Genomic Discovery Index (GDI). [src: soil_frontier_genomics]

**Known aliases:** None reported. [src: soil_frontier_genomics]

**Stable external identifier:** None reported. [src: soil_frontier_genomics]

The GDI was introduced in the [[summaries/soil_frontier_genomics__REPORT]] as a novel index without published precedent. [src: soil_frontier_genomics]

## Key facts from soil_frontier_genomics

The index was calculated at 1° spatial bins using the formula `GDI = OTU Richness / (Mean Genome Completeness + 1)`. [src: soil_frontier_genomics]

Forest had GDI = 902.36 and cropland had GDI = 890.82, while grassland had GDI = 503.42 and wetland had GDI = 525.13. [src: soil_frontier_genomics]

Forest and cropland were identified as jointly highest-GDI biomes, whereas grassland and wetland were relatively well-mapped. [src: soil_frontier_genomics]

Frontier areas with GDI > 1000 had mean pH = 6.74, compared with mean pH = 5.94 in mapped areas, a +0.8 pH unit gap. [src: soil_frontier_genomics]

The report interprets the pH difference as evidence of systematic under-sampling of alkaline soil microbiomes in public genomic databases, but notes that alkaline soils may instead be underrepresented because fewer samples from those pH ranges were sequenced. [src: soil_frontier_genomics]

The GDI can equal 902 even when there are zero genomes because completeness = 0 makes the denominator 1. [src: soil_frontier_genomics]

The index conflates sampling gap and OTU richness, potentially allowing the richness term to dominate. [src: soil_frontier_genomics]

The difference between Forest GDI = 902.36 and Cropland GDI = 890.82 is 1.3%; without bootstrap confidence intervals, these values are not meaningfully distinguishable. [src: soil_frontier_genomics]

## Interpretation and validation

The GDI results indicate that forest and cropland soils are diverse but poorly represented at the genomic level, which may limit functional inferences based on genome reference databases in these biomes. [src: soil_frontier_genomics]

The report recommends separately reporting OTU richness and genome completeness with a two-dimensional scatterplot because those components may be more interpretable than the composite index. [src: soil_frontier_genomics]

Required validation includes rarefaction-corrected GDI after uniform 16S sequencing-depth correction, bootstrap 95% confidence intervals for biome-level GDI rankings, and control for the number of 16S samples in each pH bin. [src: soil_frontier_genomics]

These validations require re-running analyses from the BERIL Observatory 16S tables and [[entities/kbase-ke-pangenome]] completeness data because no local CSV output is available. [src: soil_frontier_genomics]

The method therefore contributes to [[concepts/genomic-under-representation]] by quantifying potential genomic under-representation, to [[concepts/environment-embedding-geography]] by using spatial bins to compare discovery gaps, and to [[concepts/provenance-aware-resource-discovery]] by motivating separation of sampling, assembly, and annotation gaps. [src: soil_frontier_genomics]
