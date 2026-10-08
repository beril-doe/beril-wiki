---
type: "Summary"
description: "Project report testing whether Fitness Browser laboratory metal-tolerance fitness predicts genus abundance and community composition across a uranium gradient in 108 Oak Ridge groundwater sites."
doc_type: "short"
full_text: "sources/lab_field_ecology__REPORT.md"
---
# Lab Fitness Predicts Field Ecology at Oak Ridge

## Overview

This report links Fitness Browser laboratory fitness measurements with [[entities/enigma-coral]] groundwater community composition and geochemistry across 108 [[entities/oak-ridge-field-research-center]] sites. Communities were characterized using 16S amplicon sequencing, a marker-gene method for profiling microbial composition, and compared with laboratory metal-tolerance scores. The study tests whether laboratory performance predicts field abundance and finds that aggregate tolerance is only suggestive, whereas several genera show statistically significant, bidirectional associations with uranium concentration. [src: lab_field_ecology]

## Key Findings

Of 26 unique genera represented in the [[entities/kescience-fitnessbrowser]], 14 were detected in Oak Ridge groundwater communities by 16S amplicon sequencing. *Sphingomonas* occurred at 93% of 108 sites, *Pseudomonas* at 91%, and *Caulobacter* at 82%. The ENIGMA model organism *Desulfovibrio* occurred at 34% of sites and reached a maximum relative abundance of 0.09%. [src: lab_field_ecology]

Eleven of the 14 detected Fitness Browser genera had prevalence of at least 10 sites and were tested for correlation with uranium. After Benjamini–Hochberg false-discovery-rate correction (BH-FDR), five genera had significant associations: *Herbaspirillum* increased with uranium (Spearman rho=+0.336, p=3.8e-4, FDR q=0.001); *Bacteroides* increased (rho=+0.264, p=0.006, q=0.013); *Caulobacter* decreased (rho=-0.411, p=1.0e-5, q=1.1e-4); *Sphingomonas* decreased (rho=-0.382, p=4.5e-5, q=2.5e-4); and *Pedobacter* decreased (rho=-0.266, p=0.005, q=0.013). [src: lab_field_ecology]

*Azospirillum* showed a marginal positive association with uranium (rho=+0.20, p=0.042, q=0.077). *Desulfovibrio* showed no correlation (rho=0.022, p=0.82), and *Pseudomonas* showed no correlation (rho=-0.059, p=0.55). *Shewanella*, *Dechlorosoma*, and *Marinobacter* were excluded because each had prevalence below 10 sites. [src: lab_field_ecology]

The correlation between laboratory-derived metal-tolerance score and the high-uranium/low-uranium field abundance ratio was positive but not statistically significant (Spearman rho=0.503, p=0.095, n=12 genera). The score was defined from negative mean fitness under stress, with higher values indicating greater tolerance. Thus, the direction was consistent with the prediction that more tolerant genera would be more abundant at contaminated sites, but the report treats the result as suggestive because the number of genera was small. [src: lab_field_ecology]

Sites divided at the median uranium concentration had distinct community compositions. High-uranium sites showed changes in top genera, with rare-biosphere taxa and subsurface specialists becoming more prominent. The report interprets this as broader ecological restructuring rather than a simple increase in metal-tolerant organisms, because redox conditions and carbon and energy sources also vary among sites. [src: lab_field_ecology]

The report therefore classifies H1 as not supported but suggestive, H2 as partially supported, and H3 as partially supported. H1 concerns the relationship between laboratory metal tolerance and field abundance ratio; H2 concerns genus-level abundance associations with uranium; and H3 concerns community-composition shifts between high- and low-uranium sites. Five of 11 tested genera passed the FDR threshold of q<0.05, with associations in both directions. The report labels H1 inconsistently. Its hypothesis-outcomes section calls H1 not supported but suggestive, while its novelty section calls H1 rejected. That novelty section also proposes that *Herbaspirillum* and *Bacteroides* may be tolerant colonizers. This is a hypothesis and not a tested result. [src: lab_field_ecology]

The proposed explanations for the laboratory–field disconnect are multidimensional niche requirements, community competition and cross-feeding, genus-level rather than strain-level resolution, temporal mismatch between geochemical snapshots and community history, and the low abundance of *Desulfovibrio*. Field sites vary in pH, redox potential, carbon sources, sulfate, nitrate and dozens of other parameters beyond uranium. An organism may therefore tolerate metals in the laboratory yet lack the metabolic capabilities needed at a particular field site. Field communities also involve competition, cross-feeding and syntrophy, whereas laboratory fitness measures single-organism performance in isolation. In particular, 16S data cannot match Fitness Browser organisms at species or strain level, while a genus such as *Pseudomonas* contains thousands of species with different ecologies. Geochemistry measurements are snapshots, but community composition reflects historical conditions and colonization history. *Desulfovibrio* is the ENIGMA model organism for uranium reduction. The report explicitly cautions that it is so rare in the 16S data (max 0.09% relative abundance) that its correlation analysis is unreliable. [src: lab_field_ecology]

The report places the findings in the context of Oak Ridge studies showing selective inhibition of non-*Rhodanobacter* taxa by low pH together with elevated uranium and metals, which the report cites (Carlson et al. 2019) as explaining *Rhodanobacter* dominance at contaminated wells; heavy-metal-resistance acquisition by *Rhodanobacter* strains through horizontal gene transfer (Peng et al. 2022). The report links that horizontal-transfer result to the `costly_dispensable_genes` finding that metal-resistance genes are enriched in the accessory genome. This connection is drawn by the report and has not been independently verified. The other studies show reproducible microbial succession after carbon amendments, and limited predictability of coculture interactions from single-organism fitness data. It presents the study as the first direct test of whether Fitness Browser measurements predict field ecology at sites where many Fitness Browser organisms were originally isolated. [src: lab_field_ecology]

The analysis used ENIGMA CORAL geochemistry data with metal concentrations for 108 sites (`enigma_coral.ddt_brick0000010`), community count data for ASVs (amplicon sequence variants, exact 16S sequence types) comprising 868K rows (`enigma_coral.ddt_brick0000459`), ASV-to-genus taxonomy data comprising 627K rows (`enigma_coral.ddt_brick0000454`), Fitness Browser per-gene fitness statistics across 43 organisms, and derived files including a 108-sample by 48-molecule concentration table, 132K non-zero ASV-by-community counts, 96K ASVs with genus and phylum assignments, and a genus-abundance matrix containing 1,391 genera across 108 samples. [src: lab_field_ecology]

The report's figures show the following:

- prevalence and maximum abundance of the 14 Fitness Browser genera at Oak Ridge (`fig_fb_genus_prevalence.png`);
- scatter plots of genus abundance versus uranium for the top 4 Fitness Browser genera (`fig_abundance_vs_uranium.png`);
- high-uranium versus low-uranium abundance together with the metal-tolerance correlation (`fig_metal_tolerance_score.png`);
- community composition at high- versus low-uranium sites (`fig_community_by_contamination.png`). [src: lab_field_ecology]

## Caveats and Next Analyses

The report identifies several limitations: 16S amplicon sequencing resolves only to genus level; the 108 overlapping samples may not capture the full Oak Ridge geochemical range; geochemistry measurements are point-in-time observations; the aggregate metal-tolerance score is crude and may obscure condition-specific responses, so condition-specific fitness scores such as uranium-only scores would be more informative; multiple communities per sample, including different filter sizes and replicates, were aggregated; only 12 Fitness Browser genera had sufficient data for the metal-tolerance correlation; and pH, dissolved oxygen, carbon sources, and other confounders were not controlled. [src: lab_field_ecology]

The report proposes several next analyses. The first is species- or strain-level matching using metagenomic data instead of 16S amplicons, if such data are available in ENIGMA CORAL genome or assembly tables. The second is multivariate CCA or RDA (canonical correspondence analysis or redundancy analysis, constrained ordinations that model community composition against several geochemical variables at once), controlling for pH, redox, and carbon sources. The report also proposes temporal analysis across sampling dates and metal-specific fitness scores matched to corresponding site concentrations. Finally, it proposes adding *Rhodanobacter* to the Fitness Browser as a high-impact target; this genus dominates contaminated Oak Ridge wells (Carlson et al. 2019) but is not in the Fitness Browser. [src: lab_field_ecology]

## Slots Into

- [[concepts/condition-specific-fitness]] — the non-significant aggregate metal-tolerance result motivates testing uranium-specific and other condition-specific fitness scores. [src: lab_field_ecology]
- [[concepts/environment-embedding-geography]] — genus abundance and community composition vary across the uranium contamination gradient, while field ecology reflects multiple geochemical and historical dimensions. [src: lab_field_ecology]
- [[concepts/environmental-resistome]] — the Oak Ridge context connects metal-contaminated environments, resistance-associated ecological sorting, and the proposed analysis of metal-specific tolerance. [src: lab_field_ecology]
- [[concepts/lab-field-fitness-concordance]] — aggregate lab metal tolerance showed a positive but non-significant relationship with the field high/low-uranium abundance ratio (rho=0.503, p=0.095, n=12 genera), and genus-uranium associations ran in both directions. [src: lab_field_ecology]
- [[concepts/laboratory-fitness-versus-natural-selection]] — multidimensional site conditions and community interactions are proposed to decouple single-organism lab fitness from field abundance. [src: lab_field_ecology]
- [[concepts/metal-cross-resistance]] — the project provides genus-level positive and negative uranium associations (*Herbaspirillum*, *Bacteroides*, *Caulobacter*) for comparison with lab metal responses. [src: lab_field_ecology]
- [[concepts/contaminant-selection-of-subsurface-communities]] — high- and low-uranium sites had distinct community compositions, and *Rhodanobacter* dominance is attributed to selective inhibition of other taxa. [src: lab_field_ecology]
- [[concepts/callability-limited-comparative-inference]] — low prevalence excluded three genera, and *Desulfovibrio* rarity made its correlation unreliable. [src: lab_field_ecology]
- [[concepts/confirmatory-exploratory-ecological-association-discordance]] — the *Azospirillum* association was nominally significant but marginal after FDR correction. [src: lab_field_ecology]
- [[concepts/composite-resistance-score-limitations]] — the crude aggregate metal-tolerance score may obscure condition-specific responses. [src: lab_field_ecology]
- [[concepts/taxonomic-resolution-dependent-functional-inference]] — genus-level 16S data cannot match Fitness Browser strains. [src: lab_field_ecology]
- [[concepts/costly-dispensable-gene-loss]] — the report links horizontal transfer of metal resistance in *Rhodanobacter* to accessory-genome enrichment of metal-resistance genes. [src: lab_field_ecology]
- [[concepts/adversarial-research-quality-assurance]] — the report labels H1 both as not supported but suggestive and as rejected. [src: lab_field_ecology]
- [[concepts/pooled-run-pseudoreplication-and-metadata-label-noise]] — communities from different filter sizes and replicates were aggregated within samples. [src: lab_field_ecology]
- [[concepts/genetic-perturbation-coverage-bias]] — the dominant contaminated-well genus *Rhodanobacter* is absent from the Fitness Browser. [src: lab_field_ecology]
