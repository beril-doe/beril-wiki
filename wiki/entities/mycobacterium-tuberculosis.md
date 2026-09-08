---
type: Organism
description: Tuberculosis pathogen with accessory AMR and extensive literature coverage.
sources:
- id: amr_environmental_resistome
  resource: ../summaries/amr_environmental_resistome__REPORT.md
  title: amr environmental resistome
- id: amr_pangenome_atlas
  resource: ../summaries/amr_pangenome_atlas__REPORT.md
  title: amr pangenome atlas
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: paperblast_explorer
  resource: ../summaries/paperblast_explorer__REPORT.md
  title: paperblast explorer
title: Mycobacterium tuberculosis
---
# Mycobacterium tuberculosis

## What this entity is

**Canonical name:** Mycobacterium tuberculosis. [^amr_environmental_resistome]

**Known aliases:** None are stated in the report. [^amr_environmental_resistome]

**Stable external identifier:** None is provided in the report. [^amr_environmental_resistome]

## Key facts from the reports

Mycobacterium tuberculosis was one of the deeply sampled case studies in the [amr_environmental_resistome__REPORT](../summaries/amr_environmental_resistome__REPORT.md) analysis of environmental associations with antimicrobial resistance (AMR). [^amr_environmental_resistome]

The case study included **6,673 genomes** and identified **44 AMR gene clusters**. [^amr_environmental_resistome] Of these, **4 were core** and **40 were accessory**, giving an accessory fraction of **91%**. [^amr_environmental_resistome]

The species was **clinical-dominant at 98%**, meaning that 98% of its sampled genomes were classified as originating from clinical sources in the report's species-level environmental classification. [^amr_environmental_resistome]

The PaperBLAST analysis found *Mycobacterium tuberculosis* H37Rv to be the most literature-linked bacterium in its collection, with **9,079 papers**, ahead of *Escherichia coli* K-12 (**8,860**) and *Pseudomonas aeruginosa* PAO1 (**5,928**). [^paperblast_explorer] This **supports** the clinical/model-organism interpretation of the AMR case study while also showing that its literature prominence is not evidence of representative coverage: among **15,312** bacterial organisms, the top **100** captured **44.3%** of bacterial literature. [^paperblast_explorer]

The newer [amr_pangenome_atlas__REPORT](../summaries/amr_pangenome_atlas__REPORT.md) found that clinical species averaged **10.6 AMR clusters per species**, versus **4.6** for Soil/Terrestrial species, and that clinical AMR was **30.8% core** versus **58.1%** for soil AMR. This broader comparison **supports** the existing interpretation that clinically associated AMR tends to be more accessory and **refines** it by placing the M. tuberculosis case study within a wider clinical–environmental gradient. [^amr_pangenome_atlas]

The metabolic-capability study reported that M. tuberculosis had **97.4% open** and **2.6% core genes** in its pangenome, making it the most closed among well-sampled pathogens with more than **2,500 genomes** in that comparison. [^metabolic_capability_dependency] This **refines** the AMR result: although both the broader pangenome and AMR complement are predominantly accessory by the reported measures, the 91% accessory AMR fraction should not be interpreted as evidence that M. tuberculosis has the most open pangenome. [^metabolic_capability_dependency]

Its 91% accessory AMR fraction is consistent with the report's broader finding that clinically associated species tend to carry predominantly accessory rather than core AMR, although this case study is observational and the report cautions that sampling and annotation biases limit causal interpretation. [^amr_environmental_resistome]

The result contributes to the report's [environmental-resistome](../concepts/environmental-resistome.md) synthesis and its [pangenome-integration](../concepts/pangenome-integration.md) analysis of core/accessory AMR across bacterial species. [^amr_environmental_resistome]

[^amr_environmental_resistome]: [amr environmental resistome](../summaries/amr_environmental_resistome__REPORT.md)
[^paperblast_explorer]: [paperblast explorer](../summaries/paperblast_explorer__REPORT.md)
[^amr_pangenome_atlas]: [amr pangenome atlas](../summaries/amr_pangenome_atlas__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
