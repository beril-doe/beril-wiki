---
type: "Method"
description: "Tool annotating known resistance genes, which may underestimate novel environmental resistance."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/metal_resistance_global_biogeography__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
aliases: ["AMRFinder", "AMRFinderPlus metal resistance genes", "NCBI AMRFinderPlus"]
---
# AMRFinderPlus

This page covers AMRFinderPlus, a tool that annotates known resistance genes and may underestimate novel environmental resistance. It also goes by AMRFinder and NCBI AMRFinderPlus. Reports using it warn that it misses novel resistance and that its hits are not all antibiotic resistance. [src: amr_environmental_resistome, amr_pangenome_atlas]

## Key facts

- In [[entities/bakta-amr]], the table holds 83,008 AMRFinderPlus hits on gene cluster representatives. They cover 82,908 distinct clusters across 14,723 species, which is 53.2% of the 27,690 pangenome species. [src: amr_pangenome_atlas]
- The hits span 1,939 distinct AMR gene families and 2,079 AMR products. [src: amr_pangenome_atlas]
- Detection methods are HMM (51.5%), BLASTP (22.7%), EXACTP (13.0%), PARTIALP (9.7%) and ALLELEP (3.0%). [src: amr_pangenome_atlas]
- Metal AMR annotations in one report use AMRFinderPlus HMM-based detection against the NCBI Bacterial AMR Reference Gene Database. [src: microbeatlas_metal_ecology]
- For metal resistance, it uses curated Hidden Markov Models built from experimentally validated reference sequences. Examples are merA/merB for mercury, arsABCDR for arsenate and copABCD for copper. [src: microbeatlas_metal_ecology]
- HMM gathering thresholds are set during calibration to balance sensitivity and specificity. No additional identity threshold is applied, because HMM scores are not identity values. [src: microbeatlas_metal_ecology]

## Scope: more than antibiotic resistance

The Reference Gene Catalog includes stress response genes. [src: amr_pangenome_atlas] The 83K hits are therefore not all antibiotic resistance, because the scope includes mercury and arsenic genes. [src: amr_pangenome_atlas] That broad scope also shows that heavy metal and antibiotic resistance are genomically intertwined. They are often co-located on mobile elements, as reflected in the clusters of orthologous groups (COG) P enrichment. [src: amr_pangenome_atlas] See [[concepts/metal-resistance-genes-within-amr-catalogs]].

## Metal resistance in environmental genomes

In the georeferenced environmental metagenome assembled genome (MAG) dataset, 2.8% of 22,356 MAGs carry at least one metal resistance type. The report calls this rare in the global environmental MAG pool. [src: metal_resistance_global_biogeography] It contrasts this with 21.8% prevalence of the type IV secretion system (T4SS). It concludes that AMRFinderPlus metal-resistance genes and T4SS horizontal gene transfer (HGT) machinery are distinct features that are not uniformly co-distributed. [src: metal_resistance_global_biogeography] The report drafted a global map with geopandas and matplotlib. It shows metal-resistant MAGs (n_metal_types > 0) against susceptible MAGs, coloured by metal diversity. [src: metal_resistance_global_biogeography] See [[concepts/geographic-and-biome-distribution-of-environmental-metal-resistance]].

## Caveats

- AMRFinderPlus focuses on known resistance genes and may underestimate novel resistance in environmental bacteria. This would bias results toward more AMR in clinical species, whose resistance genes are well characterized. [src: amr_environmental_resistome]
- Novel resistance mechanisms absent from the database are missed. [src: amr_strain_variation]
- Cross-reactive metalloproteases or ABC (ATP-binding cassette) transporters with structural similarity to metal resistance proteins could be misclassified. AMRFinderPlus applies taxon-specific cutoffs to reduce this. [src: microbeatlas_metal_ecology]

See also [[concepts/validity-of-curated-metal-gene-annotation]].
