---
type: Dataset
description: Metagenomic dataset supporting global and soil functional ecology analyses
sources:
- id: metal_resistance_global_biogeography
  resource: ../summaries/metal_resistance_global_biogeography__REPORT.md
  title: metal resistance global biogeography
- id: plant_microbiome_ecotypes
  resource: ../summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: MGnify
---
# MGnify

## What it is

MGnify is the canonical name of the metagenomic dataset used in the reports; no additional alias or stable external identifier was reported in the sources. [^metal_resistance_global_biogeography][^plant_microbiome_ecotypes]

## Key facts from the sources

MGnify provided 260,652 environmental metagenome-assembled genomes (MAGs), meaning genomes reconstructed from metagenomic sequencing data. [^metal_resistance_global_biogeography]

After filtering out host-associated biomes, 30,497 MAGs remained in the environmental analysis. [^metal_resistance_global_biogeography]

Of these environmental MAGs, 22,356 had usable geospatial coordinates, corresponding to 73.3% coordinate coverage of the filtered environmental MAG set. [^metal_resistance_global_biogeography]

Among the 22,356 MAGs with coordinates, 2.8% carried at least one metal-resistance type. [^metal_resistance_global_biogeography]

The report combined MGnify MAG data with geospatial metadata retrieved through the [european-nucleotide-archive](european-nucleotide-archive.md) batch API. [^metal_resistance_global_biogeography]

The resulting analysis supports [environmental-resistome](../concepts/environmental-resistome.md) by identifying global prevalence, biome enrichment and depletion, and geographic hotspots of environmental bacterial metal resistance. [^metal_resistance_global_biogeography]

The coordinate coverage and sampling limitations inform [environment-embedding-geography](../concepts/environment-embedding-geography.md), particularly the distinction between per-sample coordinate gaps and geographic gaps. [^metal_resistance_global_biogeography]

In the plant-microbiome study, MGnify supplied metagenomic genus-level comparisons alongside pangenome-derived plant-association data. [^plant_microbiome_ecotypes] This **refines** the environmental-resistome use of MGnify by showing that the dataset also supports ecological comparisons of plant-associated communities, rather than only geospatial metal-resistance analysis. [^plant_microbiome_ecotypes]

MGnify detected 17 genera across all three analyzed crop rhizospheres; 117 genera were unique to tomato, 54 to maize, and 5 to barley. [^plant_microbiome_ecotypes] Its plant-associated genera had a higher median mobilome burden than non-plant genera, 3.7 versus 2.8 mobile elements per genome, with Mann–Whitney p = 1.49×10⁻⁵. [^plant_microbiome_ecotypes] This **supports** using MGnify for genus-scale ecological and mobile-element comparisons, while not establishing genome-level horizontal-transfer rates. [^plant_microbiome_ecotypes]

The MGnify and pangenome classifications had only 11.7% Jaccard overlap, reflecting different measurements: metagenomic detection versus isolation metadata. [^plant_microbiome_ecotypes] MGnify BGC, mobilome, and defense data were available only for the soil biome in that analysis, so its comparisons did not directly contrast rhizosphere with bulk soil. [^plant_microbiome_ecotypes]

The soil-metal functional-genomics analysis **extends** MGnify’s use from MAG-level resistance prevalence and genus-level ecology to functional gene-content analysis: its MGnify Spark-table inputs covered 51,748 soil samples, nine metals, and 2,355 significant COG–metal associations at FDR < 0.05. [^soil_metal_functional_genomics] The dominant transporter and biosynthesis signals are relevant to [environmental-resistome](../concepts/environmental-resistome.md), but the observational associations **refine** rather than establish the interpretation of MGnify-derived metal responses because co-contamination, conditional model fit, effect sizes, and spatial validation remain unresolved. [^soil_metal_functional_genomics]

## Source

- [metal_resistance_global_biogeography__REPORT](../summaries/metal_resistance_global_biogeography__REPORT.md) — report summary describing the MGnify-derived environmental MAG dataset and its global metal-resistance analysis. [^metal_resistance_global_biogeography]
- [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md) — report summary describing MGnify-based plant-associated genus, rhizosphere, and mobilome comparisons. [^plant_microbiome_ecotypes]
- [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md) — report summary describing MGnify-linked soil metal and functional gene-content associations. [^soil_metal_functional_genomics]

[^metal_resistance_global_biogeography]: [metal resistance global biogeography](../summaries/metal_resistance_global_biogeography__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../summaries/plant_microbiome_ecotypes__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
