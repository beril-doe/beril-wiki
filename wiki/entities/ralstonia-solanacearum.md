---
type: "Organism"
description: "Ralstonia solanacearum is one of the six species directly matched between the Fitness Browser and BacDive, and in a plant-microbiome ecotype analysis its subclade \u00d7 plant-host association passed Benjamini\u2013Hochberg FDR but not across-species Bonferroni correction."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
*Ralstonia solanacearum* appears in two projects in this corpus. The first cross-references Fitness Browser organisms against BacDive phenotype records. The second is a plant-microbiome ecotype analysis that tested whether subclades are associated with plant hosts, where its result depended on which multiple-testing correction was applied [src: bacdive_phenotype_metal_tolerance, plant_microbiome_ecotypes]. The assigned evidence records no NCBI taxid for it [src: bacdive_phenotype_metal_tolerance, plant_microbiome_ecotypes].

## Fitness Browser–BacDive taxonomy match

Twelve [[entities/kescience-fitnessbrowser]] organisms match [[entities/bacdive]] by taxonomy ID. Together they cover 6 unique species: *Cupriavidus basilensis*, *Methanococcus maripaludis*, *Ralstonia solanacearum*, *Pseudomonas simiae*, *Azospirillum brasilense* and *Pseudomonas fluorescens*. This makes *R. solanacearum* one of the few species whose fitness data and BacDive phenotype data can be linked directly [src: bacdive_phenotype_metal_tolerance].

## Plant microbiome ecotypes: subclade × host association (H6)

Hypothesis H6 in the plant microbiome ecotypes project tested for subclade × plant-host association. The scan used a Bonferroni correction within each species for the (subclade × host) pair search, plus a correction across species. *R. solanacearum* passes [[entities/benjamini-hochberg-fdr]] (Benjamini–Hochberg false discovery rate control, which limits the expected share of false positives among significant calls) but fails the stricter across-species [[entities/bonferroni-correction]]. The report gives p = 5.9×10⁻³ after the within-species pair-search Bonferroni correction, and a BH q-value of 1.8×10⁻² [src: plant_microbiome_ecotypes].

The association survives only the less conservative correction. It should therefore be treated as a tentative signal that depends on the correction used, not as an established host specialization. In contrast, the two *Xanthomonas* species in the same scan passed both corrections [src: plant_microbiome_ecotypes].

## Related pages

- [[entities/ralstonia]] — genus-level page
- [[summaries/bacdive_phenotype_metal_tolerance__REPORT]] — source of the Fitness Browser–BacDive species match [src: bacdive_phenotype_metal_tolerance]
- [[summaries/plant_microbiome_ecotypes__REPORT]] — source of the H6 subclade × host result [src: plant_microbiome_ecotypes]
