---
type: Organism
description: Organism with predominantly accessory AMR and clinical-associated genomic
  variation
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
title: Staphylococcus aureus
---
# Staphylococcus aureus

## Identity

**Canonical name:** *Staphylococcus aureus*.[^amr_environmental_resistome]  
**Known aliases:** None specified in the source.[^amr_environmental_resistome]  
**Stable external identifier:** Not reported in the source.[^amr_environmental_resistome]

*Staphylococcus aureus* is an organism analyzed in the environmental resistome study and compared with [klebsiella-pneumoniae](klebsiella-pneumoniae.md), [salmonella-enterica](salmonella-enterica.md), [streptococcus-pneumoniae](streptococcus-pneumoniae.md), and [mycobacterium-tuberculosis](mycobacterium-tuberculosis.md).[^amr_environmental_resistome]

## AMR findings

The environmental-resistome dataset included 13,274 *Staphylococcus aureus* genomes and 642 AMR gene clusters.[^amr_environmental_resistome] Of these clusters, 9 were core and 633 were accessory, corresponding to 99% accessory AMR.[^amr_environmental_resistome] The species was clinical-dominant, with 85% of its genomes classified as originating from clinical sources.[^amr_environmental_resistome]

These results contribute to [environmental-resistome](../concepts/environmental-resistome.md), which synthesizes environment-associated AMR diversity and core/accessory composition at pangenome scale. The broader within-species analysis **supports** the clinical-association finding: human-clinical isolates had the highest AMR burden in comparisons of host-associated, terrestrial, and aquatic species, although the collection is biased toward clinical and human-associated genomes.[^amr_strain_variation] The analysis also used *S. aureus* as a case study in which UMAP—nonlinear dimensionality reduction—plots showed visible environmental structuring, but sparse metadata and underpowered tests mean this does not establish a general environment–ecotype association.[^amr_strain_variation]

The AMR clusters were identified using [amrfinderplus](amrfinderplus.md)-focused annotation and the [kbase-ke-pangenome](kbase-ke-pangenome.md) collection.[^amr_environmental_resistome]

## Integration with the pan-bacterial atlas

The pan-bacterial atlas refines the species-level findings with a family-level comparison: Staphylococcaceae was among the AMR hotspot families, averaging 37.3 AMR clusters per species.[^amr_pangenome_atlas] This broader result **supports** the existing interpretation that the strongly clinical-associated profile is coupled to substantial, predominantly accessory AMR, while not replacing the species-specific counts above.[^amr_pangenome_atlas]

## Source

See the full project summaries: [amr_environmental_resistome__REPORT](../summaries/amr_environmental_resistome__REPORT.md), [amr_pangenome_atlas__REPORT](../summaries/amr_pangenome_atlas__REPORT.md), and [amr_strain_variation__REPORT](../summaries/amr_strain_variation__REPORT.md).[^amr_environmental_resistome][^amr_pangenome_atlas][^amr_strain_variation]

[^amr_environmental_resistome]: [amr environmental resistome](../summaries/amr_environmental_resistome__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
[^amr_pangenome_atlas]: [amr pangenome atlas](../summaries/amr_pangenome_atlas__REPORT.md)
