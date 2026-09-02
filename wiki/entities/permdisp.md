---
type: "Method"
description: "Method for testing multivariate dispersion heterogeneity."
sources: ["summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# PERMDISP

## What this entity is

**Canonical name:** PERMDISP (permutational test of multivariate dispersion).

**Known aliases:** No additional aliases were identified in the source document. [src: plant_microbiome_ecotypes]

**Stable external identifier:** None was reported in the source document. [src: plant_microbiome_ecotypes]

PERMDISP is a method for testing whether ecological groups differ in the dispersion of multivariate observations around their group centroids, distinguishing heterogeneity of spread from differences in centroid location. [src: plant_microbiome_ecotypes]

## Use in the plant microbiome ecotypes analysis

The study applied PERMDISP to Jaccard distances among 607 root, rhizosphere, and phyllosphere species after refining the functional marker panel to 17 markers. [src: plant_microbiome_ecotypes]

PERMDISP detected significant dispersion heterogeneity, with F = 15.6 and p = 0.001. [src: plant_microbiome_ecotypes]

Root species were tightest around their centroid, with a mean distance of 0.452; phyllosphere species were intermediate, with a mean distance of 0.503; and rhizosphere species were most variable, with a mean distance of 0.528. [src: plant_microbiome_ecotypes]

These results qualify the significant group separation detected by [[entities/permanova]], because part of the PERMANOVA signal could reflect unequal within-group dispersion rather than only shifts in group centroids. [src: plant_microbiome_ecotypes]

A distance-based redundancy analysis (db-RDA), which isolates centroid or location shifts, produced a location-only R² = 0.060 with p = 0.001, compared with total PERMANOVA R² = 0.071. [src: plant_microbiome_ecotypes]

The location-only component represented 0.060 / 0.071 = 84% of the total PERMANOVA R², while 16% was attributed to dispersion. [src: plant_microbiome_ecotypes]

The study therefore interpreted plant compartments as having real but weak functional separation, with approximately 6% of variance associated with compartment-level centroid differences after accounting for the dispersion issue. [src: plant_microbiome_ecotypes]

## Related pages

PERMDISP contributes evidence to [[concepts/ecotype-environment-gene-content]] and [[concepts/environment-embedding-geography]] by separating ecological group location effects from differences in within-group variability. [src: plant_microbiome_ecotypes]

The full analysis is summarized in [[summaries/plant_microbiome_ecotypes__REPORT]]. [src: plant_microbiome_ecotypes]
