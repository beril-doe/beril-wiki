---
type: "Summary"
description: "Pangenome-scale analysis of how antimicrobial-resistance genes co-localize with prophage markers across GTDB species, finding a strong species-level link between prophage density and AMR repertoire breadth but only a modest, heterogeneous gene-level proximity effect."
doc_type: "short"
full_text: "sources/prophage_amr_comobilization__REPORT.md"
---
# Prophage-AMR Co-mobilization Atlas

## Overview

This report analyzes associations between antimicrobial-resistance (AMR) genes and prophage markers across the GTDB pangenome, combining gene-neighborhood co-localization, species-level repertoire comparisons, and an attempted fitness-cost comparison. The strongest result is a species-level association between prophage marker density and AMR repertoire breadth, whereas the gene-level proximity effect is modest and heterogeneous. [src: prophage_amr_comobilization]

## Key Findings

### AMR and prophage co-localization

Across the full pangenome inventory, 83,008 AMR gene clusters and 3,465,244 broad prophage marker clusters were identified; the strict prophage-marker count was 1,261,929. Prophage markers were 83.8% accessory and 53.8% singleton, while AMR genes were 69.7% accessory and 36.1% singleton. Of 27,702 species, 14,669 (52.9%) carried both AMR and prophage markers. [src: prophage_amr_comobilization]

In the top-100 AMR-burdened species (20 genomes sampled per species, 1,953 genomes total), 36,041 AMR gene instances were analyzed. Of these, 20,073 (55.7%) were located on contigs carrying strict prophage markers (terminase, phage structural proteins, holin/lysin), 12,026 (33.4%) were within 50 genes of a prophage marker, 7,137 (19.8%) were within 20 genes, 3,731 (10.4%) were within 10 genes, and 1,991 (5.5%) were within 5 genes. The median distance to the nearest prophage marker among co-localized AMR genes was 34 genes. [src: prophage_amr_comobilization]

### Prophage proximity and AMR accessory status

AMR genes within 10 genes of a prophage marker (the proximal stratum: 2,523 accessory and 1,208 core) were 67.6% accessory, compared with 65.5% for distal AMR genes more than 10 genes away (21,158 accessory and 11,152 core). Fisher's exact test gave an odds ratio of 1.10, one-sided p=0.005, with a bootstrap 95% confidence interval of [1.024, 1.185]. This statistically significant effect is modest, corresponding to a 2.1 percentage point difference in accessory fraction. [src: prophage_amr_comobilization]

The proximity effect was threshold-dependent: the odds ratio was 0.78 at 3 genes, 0.92 at 5 genes, 1.10 at 10 genes, 1.19 at 15 genes, and 1.28 at 50 genes. Only 33 of 74 testable species had species-level odds ratios above 1, and the median species-level odds ratio was 0.85. [src: prophage_amr_comobilization]

Although the gene-level (H1) result is statistically significant in aggregate, it is modest (a 2.1 percentage point difference in accessory fraction) and heterogeneous across species. The reversal at very close range may reflect that genes immediately adjacent to phage structural genes are core phage components rather than recently acquired cargo, while the stronger association at broader thresholds may capture genomic islands containing both prophage remnants and laterally transferred genes. These are interpretations and not direct tests of mobilization mechanisms. [src: prophage_amr_comobilization]

### Prophage density and AMR repertoire breadth

Across 4,770 species, prophage marker density was positively associated with AMR repertoire breadth (Spearman rho=0.572, p<10^-300, n=4,770 species). A log-log regression had a slope of 0.823 (SE=0.018), p<10^-300, and R²=0.30; the report states that a 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth. After controlling for genome count, the partial Spearman correlation remained rho=0.464 with p=1.0×10^-253. Genome-normalized counts (prophage markers per genome versus AMR genes per genome) correlated at Spearman rho=0.608, p<10^-300. [src: prophage_amr_comobilization]

The association was significant across all five reported major phyla: Pseudomonadota (rho=0.54), Bacillota_A (rho=0.55), Bacillota (rho=0.40), Bacteroidota (rho=0.59), and Actinomycetota (rho=0.29). The report interprets this cross-phylogenetic consistency as evidence against a purely phylogenetic explanation. [src: prophage_amr_comobilization]

The species-level result is consistent with two non-exclusive mechanisms: prophages may directly mobilize resistance genes through specialized or generalized transduction, and species with high recombination potential may independently acquire genes from multiple mobile elements. The correlation does not establish phage-mediated AMR transfer. [src: prophage_amr_comobilization]

### Fitness-cost comparison

The proposed fitness comparison could not be tested because the KBase Data Lakehouse fitness browser contains RB-TnSeq (random barcode transposon sequencing) data for only 48 model organisms, with poor overlap with the GTDB pangenome species analyzed here. Whether prophage-proximal AMR genes have distinct fitness costs therefore remains an open question. [src: prophage_amr_comobilization]

### Relation to prior studies

The report states that its species-level (H2) finding aligns with Rendueles et al. (2018), who showed across >100 pangenomes that capsule-encoding bacteria carry more prophages and more antibiotic resistance genes. The report describes its own analysis as extending this to 4,770 species versus ~100, and as controlling for genome count rather than capsule presence. [src: prophage_amr_comobilization]

Chen et al. (2018) found co-occurrence of antibiotic resistance genes and mobile genetic elements, including associations with prophages, on assembled contigs from river metagenomes. The report positions its pangenome analysis as a reference-genome counterpart, stating that the resistance-gene–prophage association is encoded in reference genomes and not only in environmental assemblies. [src: prophage_amr_comobilization]

The report cites two external experimental studies as mechanistic support: Bearson & Brunelle (2015) showed that fluoroquinolone exposure induces prophage in multidrug-resistant Salmonella, enabling phage-mediated transduction of resistance plasmids, and Fisarova et al. (2021) showed that Staphylococcus epidermidis phages transduce antimicrobial resistance plasmids at high frequency. These are separate studies; this project's own prophage–AMR results remain correlative. [src: prophage_amr_comobilization]

## Data Sources and Figures

AMR and prophage markers were identified from the bakta_amr, bakta_annotations, and bakta_pfam_domains tables of the [[data/kbase-ke-pangenome]] collection, and the attempted H3 fitness-cost comparison used the genefitness, gene, and organism tables of the [[data/kescience-fitnessbrowser]] collection. [src: prophage_amr_comobilization]

Report figures: nb01_census_overview.png (AMR and prophage marker census bar charts); nb01_amr_prophage_phylum_distribution.png (distribution of AMR and prophage across phyla); nb02_distance_distribution.png (AMR–prophage distance histogram and CDF); nb02_proximal_fraction.png (per-species fraction of AMR genes proximal to prophage); nb03_h1_contingency.png (H1 contingency table heatmap and threshold sensitivity); nb03_h1_species_odds.png (per-species odds ratios for H1); nb04_h2_breadth_regression.png (H2 scatter plots and partial correlation); nb05_synthesis.png (multi-panel synthesis summary). [src: prophage_amr_comobilization]

## Caveats and Limitations

Distances were calculated from ordinal gene positions parsed from gene_id formats rather than base-pair coordinates, so the reported gene distances may differ from true genomic distances. [src: prophage_amr_comobilization]

Prophage markers were identified by keyword and Pfam matching in bakta_annotations rather than by dedicated prophage-prediction tools such as PHASTER or geNomad. This approach may include false positives, including phage-defense systems, and may miss divergent prophages. [src: prophage_amr_comobilization]

The co-localization analysis sampled 20 genomes per species for the 100-species analysis rather than examining all 293K genomes; exhaustive analysis could strengthen the findings. [src: prophage_amr_comobilization]

Core and accessory labels depend on species-level pangenome calling with motupan, so the same gene can have different conservation status in different species. [src: prophage_amr_comobilization]

The fitness analysis was limited by the overlap between the 48 fitness-browser model organisms and GTDB pangenome species, preventing an H3 comparison. [src: prophage_amr_comobilization]

The H2 association between prophage density and AMR breadth is correlational and does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

## Future Directions

The report proposes applying dedicated prophage predictors such as geNomad or PHASTER to the KBase Data Lakehouse genomes, using contig sequences (scaffoldseq) to calculate base-pair genomic distances rather than ordinal gene positions, revisiting H3 as fitness-browser coverage expands, to test whether prophage-proximal AMR genes have distinct fitness costs (a question that stays untested until expanded fitness data are available), distinguishing AMR genes mobilized by prophages from those mobilized by plasmids or ICEs (integrative and conjugative elements), which the current co-localization analysis does not partition, and analyzing all available genomes from the WHO priority pathogen subset (Klebsiella pneumoniae, Acinetobacter baumannii, Pseudomonas aeruginosa, and Escherichia coli). These pathogens are named only for proposed follow-up and were not analyzed separately. [src: prophage_amr_comobilization]

## Slots Into

- [[concepts/environmental-resistome]] — The pangenome-scale census and cross-species association connect prophage marker density with AMR repertoire breadth. [src: prophage_amr_comobilization]
- [[concepts/phage-defense-syndromes-and-arms-race]] — The report provides evidence about prophage-associated AMR neighborhoods and explicitly distinguishes prophage markers from possible phage-defense-system false positives. [src: prophage_amr_comobilization]
- [[concepts/pangenome-integration]] — The analysis integrates AMR clusters, prophage marker clusters, gene neighborhoods, species-level pangenomes, and taxonomy across 27,702 species. [src: prophage_amr_comobilization]
- [[concepts/scale-dependent-mobile-element-associations]] — The prophage–AMR association is strong at species level but modest, threshold-dependent and heterogeneous at gene-neighborhood scale, with reversal at very close range. [src: prophage_amr_comobilization]
- [[concepts/horizontal-gene-transfer-driven-innovation]] — Prophage density predicts AMR repertoire breadth, consistent with either direct transduction or a shared gene-acquisition propensity, which the data do not distinguish. [src: prophage_amr_comobilization]
- [[concepts/antimicrobial-resistance-fitness-cost]] — The planned fitness-cost test of prophage-proximal AMR genes (H3) could not be run, a null due to data coverage. [src: prophage_amr_comobilization]
- [[concepts/genetic-perturbation-coverage-bias]] — Limited fitness-browser organism coverage and poor overlap with GTDB pangenome species blocked the fitness comparison. [src: prophage_amr_comobilization]
- [[concepts/functional-marker-validation]] — Keyword/Pfam prophage markers may include phage-defense false positives and miss divergent prophages compared with dedicated predictors. [src: prophage_amr_comobilization]
- [[concepts/sampling-depth-and-downsampling-effects]] — Co-localization relied on a fixed per-species genome sample rather than all genomes. [src: prophage_amr_comobilization]
- [[concepts/pangenome-core-boundary-and-clade-size-bias]] — Core/accessory labels depend on species-level motupan calls and can differ for the same gene across species. [src: prophage_amr_comobilization]
- [[concepts/pangenome-openness-determinants]] — Open pangenomes may independently accumulate both prophages and AMR genes, an alternative explanation for the species-level correlation. [src: prophage_amr_comobilization]
