---
type: Summary
description: Pangenome-scale analysis links prophage density to AMR repertoire breadth.
doc_type: short
full_text: ../sources/prophage_amr_comobilization__REPORT.md
title: Prophage-AMR Co-mobilization Atlas
sources:
- id: prophage_amr_comobilization
  resource: ../sources/prophage_amr_comobilization__REPORT.md
  title: prophage amr comobilization
---
# Prophage-AMR Co-mobilization Atlas

## Overview

This report analyzes associations between antimicrobial-resistance (AMR) genes and prophage markers across the GTDB pangenome, combining gene-neighborhood co-localization, species-level repertoire comparisons, and an attempted fitness-cost comparison. The strongest result is a species-level association between prophage marker density and AMR repertoire breadth, whereas the gene-level proximity effect is modest and heterogeneous. [^prophage_amr_comobilization]

## Key Findings

### AMR and prophage co-localization

Across the full pangenome inventory, 83,008 AMR gene clusters and 3,465,244 broad prophage marker clusters were identified; the strict prophage-marker count was 1,261,929. Prophage markers were 83.8% accessory and 53.8% singleton, while AMR genes were 69.7% accessory and 36.1% singleton. Of 27,702 species, 14,669 (52.9%) carried both AMR and prophage markers. [^prophage_amr_comobilization]

Among 36,041 AMR gene instances from 1,953 genomes sampled across 100 species, 20,073 (55.7%) were located on contigs carrying strict prophage markers, 12,026 (33.4%) were within 50 genes of a prophage marker, 7,137 (19.8%) were within 20 genes, 3,731 (10.4%) were within 10 genes, and 1,991 (5.5%) were within 5 genes. The median distance to the nearest prophage marker among co-localized AMR genes was 34 genes. [^prophage_amr_comobilization]

### Prophage proximity and AMR accessory status

AMR genes within 10 genes of a prophage marker were 67.6% accessory, compared with 65.5% for distal AMR genes. Fisher's exact test gave an odds ratio of 1.10, one-sided p=0.005, with a bootstrap 95% confidence interval of [1.024, 1.185]. This statistically significant effect is modest, corresponding to a 2.1 percentage point difference in accessory fraction. [^prophage_amr_comobilization]

The proximity effect was threshold-dependent: the odds ratio was 0.78 at 3 genes, 0.92 at 5 genes, 1.10 at 10 genes, 1.19 at 15 genes, and 1.28 at 50 genes. Only 33 of 74 testable species had species-level odds ratios above 1, and the median species-level odds ratio was 0.85. [^prophage_amr_comobilization]

The reversal at very close range may reflect that genes immediately adjacent to phage structural genes are core phage components rather than recently acquired cargo, while the stronger association at broader thresholds may capture genomic islands containing both prophage remnants and laterally transferred genes. These are interpretations and not direct tests of mobilization mechanisms. [^prophage_amr_comobilization]

### Prophage density and AMR repertoire breadth

Across 4,770 species, prophage marker density was positively associated with AMR repertoire breadth (Spearman rho=0.572, p<10^-300, n=4,770 species). A log-log regression had a slope of 0.823 (SE=0.018), p<10^-300, and R²=0.30; the report states that a 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth. After controlling for genome count, the partial Spearman correlation remained rho=0.464 with p=1.0×10^-253. [^prophage_amr_comobilization]

The association was significant across all five reported major phyla: Pseudomonadota (rho=0.54), Bacillota_A (rho=0.55), Bacillota (rho=0.40), Bacteroidota (rho=0.59), and Actinomycetota (rho=0.29). The report interprets this cross-phylogenetic consistency as evidence against a purely phylogenetic explanation. [^prophage_amr_comobilization]

The species-level result is consistent with two non-exclusive mechanisms: prophages may directly mobilize resistance genes through specialized or generalized transduction, and species with high recombination potential may independently acquire genes from multiple mobile elements. The correlation does not establish phage-mediated AMR transfer. [^prophage_amr_comobilization]

### Fitness-cost comparison

The proposed fitness comparison could not be tested because the BERDL fitness browser contains RB-TnSeq (random barcode transposon sequencing) data for only 48 model organisms, with poor overlap with the GTDB pangenome species analyzed here. Whether prophage-proximal AMR genes have distinct fitness costs therefore remains an open question. [^prophage_amr_comobilization]

## Caveats and Limitations

Distances were calculated from ordinal gene positions parsed from gene_id formats rather than base-pair coordinates, so the reported gene distances may differ from true genomic distances. [^prophage_amr_comobilization]

Prophage markers were identified by keyword and Pfam matching in bakta_annotations rather than by dedicated prophage-prediction tools such as PHASTER or geNomad. This approach may include false positives, including phage-defense systems, and may miss divergent prophages. [^prophage_amr_comobilization]

The co-localization analysis sampled 20 genomes per species for the 100-species analysis rather than examining all 293K genomes; exhaustive analysis could strengthen the findings. [^prophage_amr_comobilization]

Core and accessory labels depend on species-level pangenome calling with motupan, so the same gene can have different conservation status in different species. [^prophage_amr_comobilization]

The fitness analysis was limited by the overlap between the 48 fitness-browser model organisms and GTDB pangenome species, preventing an H3 comparison. [^prophage_amr_comobilization]

The H2 association between prophage density and AMR breadth is correlational and does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes. [^prophage_amr_comobilization]

## Future Directions

The report proposes applying dedicated prophage predictors such as geNomad or PHASTER to BERDL genomes, using scaffold sequences for base-pair-resolution distances, revisiting fitness costs as fitness-browser coverage expands, separating phage from plasmid and ICE mobilization, and analyzing all available genomes from Klebsiella pneumoniae, Acinetobacter baumannii, Pseudomonas aeruginosa, and Escherichia coli. [^prophage_amr_comobilization]

## Slots Into

- [environmental-resistome](../concepts/environmental-resistome.md) — The pangenome-scale census and cross-species association connect prophage marker density with AMR repertoire breadth. [^prophage_amr_comobilization]
- [phage-defense-syndromes-and-arms-race](../concepts/phage-defense-syndromes-and-arms-race.md) — The report provides evidence about prophage-associated AMR neighborhoods and explicitly distinguishes prophage markers from possible phage-defense-system false positives. [^prophage_amr_comobilization]
- [pangenome-integration](../concepts/pangenome-integration.md) — The analysis integrates AMR clusters, prophage marker clusters, gene neighborhoods, species-level pangenomes, and taxonomy across 27,702 species. [^prophage_amr_comobilization]

[^prophage_amr_comobilization]: [prophage amr comobilization](../sources/prophage_amr_comobilization__REPORT.md)
