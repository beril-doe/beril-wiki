---
type: Organism
description: Host-associated species with extensive accessory AMR and metabolic ecotype
  structure
sources:
- id: amr_environmental_resistome
  resource: ../summaries/amr_environmental_resistome__REPORT.md
  title: amr environmental resistome
- id: amr_pangenome_atlas
  resource: ../summaries/amr_pangenome_atlas__REPORT.md
  title: amr pangenome atlas
- id: amr_strain_variation
  resource: ../summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
title: Salmonella enterica
---
# Salmonella enterica

## What this entity is

**Canonical name:** Salmonella enterica. [^amr_environmental_resistome]

**Known aliases:** No aliases were reported in the source document. [^amr_environmental_resistome]

**Stable external identifier:** None was provided in the source document. [^amr_environmental_resistome]

## Key facts

Salmonella enterica was one of the deeply sampled species case studies in the environmental resistome analysis. [^amr_environmental_resistome] That dataset contained 10,097 Salmonella enterica genomes and 836 AMR gene clusters; 11 were classified as core and 825 as accessory, corresponding to 98% accessory AMR. [^amr_environmental_resistome] Salmonella enterica was host-associated-dominant, with host-associated genomes representing 31% of its environmental classification. [^amr_environmental_resistome] This case study illustrated extensive accessory AMR variation in a deeply sampled species. [^amr_environmental_resistome]

A separate metabolic-capability analysis used 11,396 Salmonella enterica genomes and identified six metabolic clusters with a silhouette score of 0.894, the strongest clustering reported among its 10 target species. [^metabolic_capability_dependency] This **supports** strain-level heterogeneity within the species, while the different genome counts and measurements mean that metabolic clustering should not be treated as a direct description of the AMR dataset. [^metabolic_capability_dependency] Metabolic cluster membership was significantly associated with isolation environment (χ²=1570.2, df=25, p<0.0001), consistent with differentiation across clinical, food, and environmental sources; this interpretation is observational and does not establish causality. [^metabolic_capability_dependency] Because explicit phylogenetic correction was not performed, the environment association may be confounded by phylogenetic structure. [^metabolic_capability_dependency]

The within-species strain-variation analysis included Salmonella enterica among its case-study UMAP plots, which showed visible environmental structuring; because the environmental tests were underpowered, this **refines** rather than establishes the general claim that environment determines AMR ecotypes. [^amr_strain_variation] The metabolic-cluster result **supports** investigating environmental structure in both metabolic and accessory AMR repertoires, but its stronger statistical association does not resolve the AMR-specific metadata and power limitations. [^metabolic_capability_dependency]

## Integration with the pan-bacterial atlas

The pan-bacterial atlas reports Salmonella as the second-highest genus for AMR density, with 198 AMR clusters per species. [^amr_pangenome_atlas] This **supports** the existing case-study interpretation of extensive AMR variation, while the two reports use different aggregation levels and should not be treated as directly equivalent counts. [^amr_pangenome_atlas]

Together, these results support [environmental-resistome](../concepts/environmental-resistome.md) by showing that a host-associated-dominant species can contain many AMR clusters while retaining very few core clusters. [^amr_environmental_resistome] They also contribute to [pangenome-integration](../concepts/pangenome-integration.md), where core/accessory AMR composition is analyzed across species and ecological environments. [^amr_environmental_resistome] The metabolic findings additionally **refine** this picture by showing that environment-linked within-species structure can be detected in pathway profiles, although the ecological interpretation remains non-causal and potentially confounded. [^metabolic_capability_dependency]

## Related pages

- [amr_environmental_resistome__REPORT](../summaries/amr_environmental_resistome__REPORT.md)
- [amr_pangenome_atlas__REPORT](../summaries/amr_pangenome_atlas__REPORT.md)
- [amr_strain_variation__REPORT](../summaries/amr_strain_variation__REPORT.md)
- [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md)
- [environmental-resistome](../concepts/environmental-resistome.md)
- [pangenome-integration](../concepts/pangenome-integration.md)
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md)
- [amrfinderplus](amrfinderplus.md)
- [kbase-ke-pangenome](kbase-ke-pangenome.md)

[^amr_environmental_resistome]: [amr environmental resistome](../summaries/amr_environmental_resistome__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
[^amr_pangenome_atlas]: [amr pangenome atlas](../summaries/amr_pangenome_atlas__REPORT.md)
