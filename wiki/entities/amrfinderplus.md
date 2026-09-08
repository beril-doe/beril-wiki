---
type: Method
description: AMRFinderPlus annotates antimicrobial- and metal-resistance genes.
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
- id: metal_resistance_global_biogeography
  resource: ../summaries/metal_resistance_global_biogeography__REPORT.md
  title: metal resistance global biogeography
- id: microbeatlas_metal_ecology
  resource: ../summaries/microbeatlas_metal_ecology__REPORT.md
  title: microbeatlas metal ecology
title: AMRFinderPlus
---
# AMRFinderPlus

## What this entity is

**Canonical name:** AMRFinderPlus. [^amr_environmental_resistome]

**Known aliases:** No additional aliases were reported in the source. [^amr_environmental_resistome]

**Stable external identifier:** None was reported in the source. [^amr_environmental_resistome]

AMRFinderPlus was the focused annotation approach used to identify antimicrobial-resistance (AMR) genes and clusters in the environmental resistome analysis. [^amr_environmental_resistome]

## Key facts from the reports

The environmental-resistome analysis identified 82,908 AMR gene clusters across 14,723 bacterial species and 293K genomes using the KBase KE pangenome collection. [^amr_environmental_resistome]

The atlas **refines** that result by reporting 83,008 AMRFinderPlus hits on gene-cluster representatives, spanning 82,908 distinct clusters, 1,939 AMR gene families, 2,079 AMR products, and 14,723 species; 53.2% of 27,690 pangenome species carried at least one hit. [^amr_pangenome_atlas]

A total of 15,550 AMR clusters, representing 18.7% of all clusters, could not be assigned to a resistance mechanism from gene name or product annotation and were excluded from mechanism-fraction analyses. [^amr_environmental_resistome]

The atlas **supports** the concern that AMRFinderPlus-focused annotation can broaden AMR interpretation: its Reference Gene Catalog includes stress-response genes, including mercury- and arsenic-resistance genes, alongside classical antibiotic-resistance genes. [^amr_pangenome_atlas] A global environmental-MAG analysis **further supports** this interpretation by using AMRFinderPlus metal-resistance annotations, defined as MAGs with `n_metal_types > 0`, to assess geographic prevalence. [^metal_resistance_global_biogeography]

The MicrobeAtlas study **extends** this application from environmental MAG geography to genus-level ecological breadth: it used AMRFinderPlus pangenome annotations across 6,789 GTDB species and found that metal type diversity, rather than total AMR gene burden or core AMR fraction, was associated with broader inferred niche breadth after phylogenetic correction. [^microbeatlas_metal_ecology] This association is correlational and does not establish that AMRFinderPlus-detected resistance causes ecological generalism. [^microbeatlas_metal_ecology]

Its atlas hits were detected by HMM (51.5%), BLASTP (22.7%), EXACTP (13.0%), PARTIALP (9.7%), and ALLELEP (3.0%); 93.0% of AMR clusters had both Bakta product annotations and eggNOG hits, while 7.0% had Bakta annotations only. [^amr_pangenome_atlas]

The AMRFinderPlus-based annotations were also applied to 180,025 genomes from 1,305 species, producing 37,444 AMR gene-species prevalence records for within-species variation analysis. [^amr_strain_variation]

That study **supports** the existing coverage limitation: AMR detection relies on the AMRFinderPlus database, so novel resistance mechanisms absent from the database are missed. [^amr_strain_variation] The report also cautions that AMRFinderPlus-focused annotation may underestimate novel environmental resistance and may bias comparisons toward clinical enrichment, where resistance genes are better characterized. [^amr_environmental_resistome] The atlas **supports and extends** this limitation: keyword-based mechanism classification left 22% of hits in Other/Unclassified, and the report recommends systematic CARD ARO mapping to reduce that category. [^amr_pangenome_atlas]

The MicrobeAtlas analysis **refines** these limitations by noting possible cross-reactive false positives in HMM-based AMRFinderPlus detections, uncertainty in the “other” metal category, and the absence of manual validation; it recommends manual BLAST verification of 100 randomly sampled annotated gene clusters. [^microbeatlas_metal_ecology]

In the global biogeography analysis, only 2.8% of 22,356 coordinate-bearing environmental MAGs carried at least one AMRFinderPlus metal-resistance type. This result **refines** interpretation of the method’s scope: the measured feature was much rarer than the 21.8% T4SS prevalence reported for comparison, supporting the interpretation that AMRFinderPlus metal-resistance genes and T4SS horizontal-gene-transfer machinery are distinct features that are not uniformly co-distributed. [^metal_resistance_global_biogeography]

The AMRFinderPlus-based annotations were used to compare AMR diversity, core/accessory composition, and resistance-mechanism composition across ecological environments in [amr_environmental_resistome__REPORT](../summaries/amr_environmental_resistome__REPORT.md). [^amr_environmental_resistome] The atlas likewise uses AMRFinderPlus annotations to analyze conservation, taxonomy, function, environmental gradients, and Fitness Browser links across 27,690 pangenome species in [amr_pangenome_atlas__REPORT](../summaries/amr_pangenome_atlas__REPORT.md). [^amr_pangenome_atlas] The MicrobeAtlas study uses the annotations to connect metal-resistance type diversity with global 16S-based niche breadth and groundwater prevalence in [microbeatlas_metal_ecology__REPORT](../summaries/microbeatlas_metal_ecology__REPORT.md). [^microbeatlas_metal_ecology]

In the within-species study, these annotations supported analyses of prevalence classes, tightly co-inherited resistance islands, phylogenetic signal, and AMR ecotypes; co-occurrence findings remain association evidence rather than proof of co-selection or functional synergy. [^amr_strain_variation]

This method therefore contributes evidence to [environmental-resistome](../concepts/environmental-resistome.md), [pangenome-integration](../concepts/pangenome-integration.md), and [cofitness-network-architecture](../concepts/cofitness-network-architecture.md). Its database coverage limitation, the unclassified-hit category, and the preliminary spatial results are relevant to interpreting ecological and strain-level comparisons. [^amr_environmental_resistome] [^amr_strain_variation] [^amr_pangenome_atlas] [^metal_resistance_global_biogeography]

[^amr_environmental_resistome]: [amr environmental resistome](../summaries/amr_environmental_resistome__REPORT.md)
[^amr_pangenome_atlas]: [amr pangenome atlas](../summaries/amr_pangenome_atlas__REPORT.md)
[^metal_resistance_global_biogeography]: [metal resistance global biogeography](../summaries/metal_resistance_global_biogeography__REPORT.md)
[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../summaries/microbeatlas_metal_ecology__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
