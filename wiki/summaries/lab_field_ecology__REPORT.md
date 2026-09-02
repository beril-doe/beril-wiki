---
type: "Summary"
description: "Tests whether laboratory fitness predicts Oak Ridge field ecology."
doc_type: "short"
full_text: "sources/lab_field_ecology__REPORT.md"
---
# Lab Fitness Predicts Field Ecology at Oak Ridge

## Overview

This report links Fitness Browser laboratory fitness measurements with [[entities/enigma-coral]] groundwater community composition and geochemistry across 108 [[entities/oak-ridge-field-research-center]] sites. Communities were characterized using 16S amplicon sequencing, a marker-gene method for profiling microbial composition, and compared with laboratory metal-tolerance scores. The study tests whether laboratory performance predicts field abundance and finds that aggregate tolerance is only suggestive, whereas several genera show statistically significant, bidirectional associations with uranium concentration. [src: lab_field_ecology]

## Key Findings

Of 26 unique genera represented in the [[entities/kescience-fitnessbrowser]], 14 were detected in Oak Ridge groundwater communities. *Sphingomonas* occurred at 93% of 108 sites, *Pseudomonas* at 91%, and *Caulobacter* at 82%. The ENIGMA model organism *Desulfovibrio* occurred at 34% of sites and reached a maximum relative abundance of 0.09%. [src: lab_field_ecology]

Eleven of the 14 detected Fitness Browser genera had prevalence of at least 10 sites and were tested for correlation with uranium. After Benjamini–Hochberg false-discovery-rate correction (BH-FDR), five genera had significant associations: *Herbaspirillum* increased with uranium (Spearman rho=+0.336, p=3.8e-4, FDR q=0.001); *Bacteroides* increased (rho=+0.264, p=0.006, q=0.013); *Caulobacter* decreased (rho=-0.411, p=1.0e-5, q=1.1e-4); *Sphingomonas* decreased (rho=-0.382, p=4.5e-5, q=2.5e-4); and *Pedobacter* decreased (rho=-0.266, p=0.005, q=0.013). [src: lab_field_ecology]

*Azospirillum* showed a marginal positive association with uranium (rho=+0.20, p=0.042, q=0.077). *Desulfovibrio* showed no correlation (rho=0.022, p=0.82), and *Pseudomonas* showed no correlation (rho=-0.059, p=0.55). *Shewanella*, *Dechlorosoma*, and *Marinobacter* were excluded because each had prevalence below 10 sites. [src: lab_field_ecology]

The correlation between laboratory-derived metal-tolerance score and the high-uranium/low-uranium field abundance ratio was positive but not statistically significant (Spearman rho=0.503, p=0.095, n=12 genera). The score was defined from negative mean fitness under stress, with higher values indicating greater tolerance. Thus, the direction was consistent with the prediction that more tolerant genera would be more abundant at contaminated sites, but the report treats the result as suggestive because the number of genera was small. [src: lab_field_ecology]

Sites divided at the median uranium concentration had distinct community compositions. High-uranium sites showed changes in top genera, with rare-biosphere taxa and subsurface specialists becoming more prominent. The report interprets this as broader ecological restructuring rather than a simple increase in metal-tolerant organisms, because redox conditions and carbon and energy sources also vary among sites. [src: lab_field_ecology]

The report therefore classifies H1 as not supported but suggestive, H2 as partially supported, and H3 as partially supported. H1 concerns the relationship between laboratory metal tolerance and field abundance ratio; H2 concerns genus-level abundance associations with uranium; and H3 concerns community-composition shifts between high- and low-uranium sites. Five of 11 tested genera passed the FDR threshold of q<0.05, with associations in both directions. [src: lab_field_ecology]

The proposed explanations for the laboratory–field disconnect are multidimensional niche requirements, community competition and cross-feeding, genus-level rather than strain-level resolution, temporal mismatch between geochemical snapshots and community history, and the low abundance of *Desulfovibrio*. In particular, 16S data cannot match Fitness Browser organisms at species or strain level, while a genus such as *Pseudomonas* contains thousands of species with different ecologies. [src: lab_field_ecology]

The report places the findings in the context of Oak Ridge studies showing selective inhibition of non-*Rhodanobacter* taxa by low pH together with elevated uranium and metals, heavy-metal-resistance acquisition by *Rhodanobacter* strains through horizontal gene transfer, reproducible microbial succession after carbon amendments, and limited predictability of coculture interactions from single-organism fitness data. It presents the study as the first direct test of whether Fitness Browser measurements predict field ecology at sites where many Fitness Browser organisms were originally isolated. [src: lab_field_ecology]

The analysis used ENIGMA CORAL geochemistry data for 108 samples, community data comprising 868K rows, ASV taxonomy data comprising 627K rows, and derived files including a 108-sample by 48-molecule concentration table, 132K non-zero ASV-by-community counts, 96K ASVs with genus and phylum assignments, and a genus-abundance matrix containing 1,391 genera across 108 samples. [src: lab_field_ecology]

## Caveats and Next Analyses

The report identifies several limitations: 16S amplicon sequencing resolves only to genus level; the 108 overlapping samples may not capture the full Oak Ridge geochemical range; geochemistry measurements are point-in-time observations; the aggregate metal-tolerance score is crude; multiple communities per sample, including different filter sizes and replicates, were aggregated; only 12 Fitness Browser genera had sufficient data for the metal-tolerance correlation; and pH, dissolved oxygen, carbon sources, and other confounders were not controlled. [src: lab_field_ecology]

The report proposes species- or strain-level matching using ENIGMA CORAL metagenomic genome or assembly tables, multivariate CCA or RDA analysis controlling for pH, redox, and carbon sources, temporal analysis across sampling dates, metal-specific fitness scores matched to corresponding site concentrations, and addition of *Rhodanobacter* to the Fitness Browser. [src: lab_field_ecology]

## Slots Into

- [[concepts/condition-specific-fitness]] — the non-significant aggregate metal-tolerance result motivates testing uranium-specific and other condition-specific fitness scores. [src: lab_field_ecology]
- [[concepts/environment-embedding-geography]] — genus abundance and community composition vary across the uranium contamination gradient, while field ecology reflects multiple geochemical and historical dimensions. [src: lab_field_ecology]
- [[concepts/environmental-resistome]] — the Oak Ridge context connects metal-contaminated environments, resistance-associated ecological sorting, and the proposed analysis of metal-specific tolerance. [src: lab_field_ecology]
