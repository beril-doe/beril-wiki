---
type: Summary
description: Multi-omics, BERDL connectivity, and metabolic analysis of Acinetobacter
  baylyi ADP1
doc_type: short
full_text: ../sources/acinetobacter_adp1_explorer__REPORT.md
title: Acinetobacter baylyi ADP1 Data Explorer
sources:
- id: acinetobacter_adp1_explorer
  resource: ../sources/acinetobacter_adp1_explorer__REPORT.md
  title: acinetobacter adp1 explorer
---
# Acinetobacter baylyi ADP1 Data Explorer

## Overview

This exploration analyzes a user-provided SQLite database containing 15 tables, 461,522 total rows, and 135 MB of data for *Acinetobacter baylyi* ADP1 and 13 related genomes. The database integrates genome features, TnSeq essentiality, flux balance analysis (FBA), mutant growth fitness, proteomics, pangenome classification, functional annotations, metabolic reactions, and growth phenotypes, and connects these data to multiple BERDL collections. [^acinetobacter_adp1_explorer]

## Key Findings

### Multi-omics database structure

The central `genome_features` table contains 5,852 genes and 51 annotation columns spanning six data modalities: TnSeq essentiality with 58% coverage, FBA metabolic flux with 15% coverage, mutant growth fitness on 8 carbon sources with 39% coverage, proteomics across 7 strains with 41% coverage, pangenome classification with 54% coverage, and functional annotations through COG, KO, Pfam, and UniRef with 34-55% coverage. No single gene has data across all six modalities, although pairwise overlaps are substantial, particularly among essentiality, pangenome, and proteomics. [^acinetobacter_adp1_explorer]

The database documents 7 engineered ADP1 strains, including wild-type ADP1 and 6 derivatives with aromatic amino acid pathway modifications involving ΔaroF and ΔaroG or dgoA variants; proteomics data are available for all 7 strains. Protein abundance was measured for 2,383 genes, and cross-strain correlation was high, indicating targeted rather than global effects of the engineered modifications. [^acinetobacter_adp1_explorer]

### BERDL connectivity

Four of five tested connection types matched BERDL at greater than 90%: 13 of 13 genome IDs matched the pangenome, 1,210 of 1,330 reactions matched biochemistry, 230 of 230 compounds matched biochemistry, and 4,891 of 4,891 cluster IDs matched the pangenome through mapping. ADP1 had 0 matches among 1 Fitness Browser organism query and was absent from the Fitness Browser. [^acinetobacter_adp1_explorer]

All 13 BERDL-format genomes belong to *s__Acinetobacter_baylyi* and the clade `s__Acinetobacter_baylyi--RS_GCF_000368685.1`. This BERDL pangenome contains 3,207 core and 1,684 accessory gene clusters. The 120 unmatched reactions, representing 9% of the 1,330 reactions, may be custom or draft reactions not yet present in ModelSEED. [^acinetobacter_adp1_explorer]

### Pangenome cluster-ID bridge

ADP1 uses mmseqs2-style cluster IDs such as `NHSXFYEX_mmseqsCluster_NNNN`, whereas BERDL uses centroid gene IDs such as `NC_005966.1_1024`; the two naming systems have 0% direct string match. A bridge through BERDL’s `gene_genecluster_junction` table links BERDL cluster IDs to member gene IDs, which match the `feature_id` column in ADP1’s `pan_genome_features` table and thereby expose the ADP1-style `cluster_id`. [^acinetobacter_adp1_explorer]

All 4,891 BERDL clusters mapped successfully to 4,081 unique ADP1 clusters, yielding a 100% gene-level match across 43,754 genes. The generated `data/cluster_id_mapping.csv` file enables BERDL pangenome annotations, including eggNOG and functional predictions, to be joined to ADP1 genes. [^acinetobacter_adp1_explorer]

### FBA and TnSeq essentiality

Of 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639, or 73.8%, were concordant and 227 were discordant. The discordant genes are candidates for metabolic-model refinement or may reflect regulatory effects not represented by FBA. [^acinetobacter_adp1_explorer]

Essentiality was condition-specific: 499 genes were essential on minimal media compared with 346 on LB, consistent with an additional biosynthetic burden under minimal-media growth. [^acinetobacter_adp1_explorer]

FBA flux classes changed between rich and minimal media for 177 of 866 genes, or 20%, indicating condition-dependent metabolic rewiring among the genes with flux data. [^acinetobacter_adp1_explorer]

### Condition-specific mutant fitness

Mutant growth fitness across 8 carbon sources had a mean pairwise correlation of 0.44. Urea fitness was nearly uncorrelated with quinate, at r = 0.11, and was weakly correlated with all other conditions, at r = 0.12-0.28, suggesting that urea catabolism involves a largely independent set of genes. Butanediol-acetate and butanediol-lactate showed the strongest correlations, at r = 0.58 and r = 0.53, respectively, consistent with shared central carbon metabolism. [^acinetobacter_adp1_explorer]

Because ADP1 is absent from the Fitness Browser, its mutant growth fitness measurements for 8 carbon sources constitute a resource not otherwise available in BERDL. [^acinetobacter_adp1_explorer]

### Essentiality, annotation, and pangenome status

Essential genes were more annotation-rich than dispensable genes: 33% of essential genes had COG assignments compared with 5% of dispensable genes, while 92% of essential genes had KEGG KO assignments compared with 53% of dispensable genes. Approximately 8% of essential genes lacked KO assignments and were identified as potential novel essential functions. [^acinetobacter_adp1_explorer]

Essential genes were also more likely to belong to the core pangenome, consistent with the association between conservation and essentiality. [^acinetobacter_adp1_explorer]

### Metabolic reaction conservation and gapfilling

Of 1,330 unique metabolic reactions, 1,248, or 94%, were shared across all 14 genomes and classified as core; 62 were variable, occurring in 2-13 genomes, and 20 were genome-unique. Gapfilling accounted for 7.7% of reactions on average, with 243 missing functions cataloged. [^acinetobacter_adp1_explorer]

Of 121,519 growth phenotype predictions across 14 genomes, 105,376, or 87%, required at least one gapfilled reaction. Prediction accuracy was therefore tightly coupled to gapfilling quality in this analysis, and false negatives had higher mean gap counts than correct predictions. [^acinetobacter_adp1_explorer]

### BERDL-linked and novel data resources

The project connected the ADP1 database to the `kbase_ke_pangenome`, `kbase_msd_biochemistry`, and `kescience_fitnessbrowser` collections, and identified a 37-table Acinetobacter genome browser in `phagefoundry_acinetobacter_genome_browser` without deeply querying it. The user-provided database contributes mutant growth fitness on 8 carbon sources, proteomics across 7 engineered strains, TnSeq essentiality on minimal and LB media, and FBA predictions with gapfilling metadata. [^acinetobacter_adp1_explorer]

## Caveats and Limitations

No gene has measurements across all 6 data modalities, and FBA flux data cover only 15% of genes; consequently, the FBA-TnSeq concordance analysis is limited to 866 genes. [^acinetobacter_adp1_explorer]

The pangenome cluster mapping is indirect and passes through 3 tables. Although it is 100% complete at the reported gene level, the indirection could introduce edge cases where clusters split or merge between the BERDL and ADP1 pangenome analyses. [^acinetobacter_adp1_explorer]

The 87% dependence of growth phenotype predictions on gapfilled reactions limits interpretation of those predictions, and the 243 missing functions represent gaps in genomic evidence that affect prediction reliability. [^acinetobacter_adp1_explorer]

The database covers only *A. baylyi*, so cross-species comparisons require comparable databases for other organisms. [^acinetobacter_adp1_explorer]

The observed FBA-TnSeq discordance, urea-specific fitness pattern, core-metabolism conservation, and gapfilling dependence are primarily results from this ADP1-centered dataset. The report presents pathway enrichment of the 227 discordant genes, cross-species fitness comparison, PhageFoundry cross-referencing, urea-specific gene identification, and pangenome-informed gapfill confidence assessment as future analyses rather than completed findings. [^acinetobacter_adp1_explorer]

## Slots Into

- [multi-omics-integration](../concepts/multi-omics-integration.md) — the database’s six data modalities, incomplete modality overlap, and cross-strain proteomics provide an integrated multi-omics case study.
- [gene-essentiality](../concepts/gene-essentiality.md) — the FBA-TnSeq concordance, condition-specific essentiality, annotation enrichment, and essentiality-pangenome relationship provide evidence for comparing gene-essentiality predictors.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — carbon-source fitness correlations, especially the weak relationship of urea to other conditions, provide condition-specific mutant-growth evidence.
- [pangenome-integration](../concepts/pangenome-integration.md) — the 100% BERDL-to-ADP1 cluster bridge and core/accessory comparisons provide a cross-dataset pangenome integration example.
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — reaction conservation, 243 missing functions, FBA flux transitions, and the 87% gapfilling dependence of growth predictions constrain metabolic-model interpretation.

[^acinetobacter_adp1_explorer]: [acinetobacter adp1 explorer](../sources/acinetobacter_adp1_explorer__REPORT.md)
