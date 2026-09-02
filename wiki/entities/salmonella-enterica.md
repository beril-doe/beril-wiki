---
type: "Organism"
description: "Host-associated species with extensive accessory AMR and metabolic ecotype structure"
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md"]
---
# Salmonella enterica

## What this entity is

**Canonical name:** Salmonella enterica. [src: amr_environmental_resistome]

**Known aliases:** No aliases were reported in the source document. [src: amr_environmental_resistome]

**Stable external identifier:** None was provided in the source document. [src: amr_environmental_resistome]

## Key facts

Salmonella enterica was one of the deeply sampled species case studies in the environmental resistome analysis. [src: amr_environmental_resistome] That dataset contained 10,097 Salmonella enterica genomes and 836 AMR gene clusters; 11 were classified as core and 825 as accessory, corresponding to 98% accessory AMR. [src: amr_environmental_resistome] Salmonella enterica was host-associated-dominant, with host-associated genomes representing 31% of its environmental classification. [src: amr_environmental_resistome] This case study illustrated extensive accessory AMR variation in a deeply sampled species. [src: amr_environmental_resistome]

A separate metabolic-capability analysis used 11,396 Salmonella enterica genomes and identified six metabolic clusters with a silhouette score of 0.894, the strongest clustering reported among its 10 target species. [src: metabolic_capability_dependency] This **supports** strain-level heterogeneity within the species, while the different genome counts and measurements mean that metabolic clustering should not be treated as a direct description of the AMR dataset. [src: metabolic_capability_dependency] Metabolic cluster membership was significantly associated with isolation environment (χ²=1570.2, df=25, p<0.0001), consistent with differentiation across clinical, food, and environmental sources; this interpretation is observational and does not establish causality. [src: metabolic_capability_dependency] Because explicit phylogenetic correction was not performed, the environment association may be confounded by phylogenetic structure. [src: metabolic_capability_dependency]

The within-species strain-variation analysis included Salmonella enterica among its case-study UMAP plots, which showed visible environmental structuring; because the environmental tests were underpowered, this **refines** rather than establishes the general claim that environment determines AMR ecotypes. [src: amr_strain_variation] The metabolic-cluster result **supports** investigating environmental structure in both metabolic and accessory AMR repertoires, but its stronger statistical association does not resolve the AMR-specific metadata and power limitations. [src: metabolic_capability_dependency]

## Integration with the pan-bacterial atlas

The pan-bacterial atlas reports Salmonella as the second-highest genus for AMR density, with 198 AMR clusters per species. [src: amr_pangenome_atlas] This **supports** the existing case-study interpretation of extensive AMR variation, while the two reports use different aggregation levels and should not be treated as directly equivalent counts. [src: amr_pangenome_atlas]

Together, these results support [[concepts/environmental-resistome]] by showing that a host-associated-dominant species can contain many AMR clusters while retaining very few core clusters. [src: amr_environmental_resistome] They also contribute to [[concepts/pangenome-integration]], where core/accessory AMR composition is analyzed across species and ecological environments. [src: amr_environmental_resistome] The metabolic findings additionally **refine** this picture by showing that environment-linked within-species structure can be detected in pathway profiles, although the ecological interpretation remains non-causal and potentially confounded. [src: metabolic_capability_dependency]

## Related pages

- [[summaries/amr_environmental_resistome__REPORT]]
- [[summaries/amr_pangenome_atlas__REPORT]]
- [[summaries/amr_strain_variation__REPORT]]
- [[summaries/metabolic_capability_dependency__REPORT]]
- [[concepts/environmental-resistome]]
- [[concepts/pangenome-integration]]
- [[concepts/ecotype-environment-gene-content]]
- [[entities/amrfinderplus]]
- [[entities/kbase-ke-pangenome]]
