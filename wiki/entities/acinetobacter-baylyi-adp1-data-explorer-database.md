---
type: Dataset
description: Integrated SQLite dataset for multi-omics analysis of Acinetobacter baylyi
  ADP1
sources:
- id: acinetobacter_adp1_explorer
  resource: ../summaries/acinetobacter_adp1_explorer__REPORT.md
  title: acinetobacter adp1 explorer
title: Acinetobacter baylyi ADP1 Data Explorer Database
---
# Acinetobacter baylyi ADP1 Data Explorer Database

## Identity

**Canonical name:** Acinetobacter baylyi ADP1 Data Explorer Database [^acinetobacter_adp1_explorer]

**Known aliases:** ADP1 Data Explorer database; user-provided ADP1 SQLite database [^acinetobacter_adp1_explorer]

**Stable external identifier:** None reported in the source document. [^acinetobacter_adp1_explorer]

This dataset is a user-provided SQLite database integrating genome features, [TnSeq](tnseq.md) essentiality, [flux balance analysis (FBA)](flux-balance-analysis.md), mutant growth fitness, proteomics, pangenome classification, functional annotations, metabolic reactions, and growth phenotypes for [Acinetobacter baylyi ADP1](acinetobacter-baylyi-adp1.md) and 13 related genomes. [^acinetobacter_adp1_explorer]

See the source summary at [acinetobacter_adp1_explorer__REPORT](../summaries/acinetobacter_adp1_explorer__REPORT.md).

## Key Facts

- The database contains 15 tables, 461,522 total rows, and 135 MB of data. [^acinetobacter_adp1_explorer]
- Its central `genome_features` table contains 5,852 genes and 51 annotation columns. [^acinetobacter_adp1_explorer]
- The six principal data modalities cover TnSeq essentiality at 58%, FBA metabolic flux at 15%, mutant growth fitness on 8 carbon sources at 39%, proteomics across 7 strains at 41%, pangenome classification at 54%, and functional annotations through COG, KO, Pfam, and UniRef at 34–55%. [^acinetobacter_adp1_explorer]
- No single gene has data across all six modalities, although pairwise overlaps are substantial, particularly among essentiality, pangenome, and proteomics. [^acinetobacter_adp1_explorer]
- The database documents 7 engineered ADP1 strains, including wild-type ADP1 and 6 derivatives with aromatic amino acid pathway modifications involving ΔaroF and ΔaroG or dgoA variants. [^acinetobacter_adp1_explorer]
- Proteomics data are available for all 7 strains, with protein abundance measured for 2,383 genes. [^acinetobacter_adp1_explorer]
- Cross-strain proteomic correlation was high, indicating targeted rather than global effects of the engineered modifications. [^acinetobacter_adp1_explorer]

## BERDL Connectivity

The database connects to the [KBase KE pangenome](kbase-ke-pangenome.md), [KBase MSD Biochemistry](kbase-msd-biochemistry.md), and [KE Science Fitness Browser](kescience-fitnessbrowser.md) collections. [^acinetobacter_adp1_explorer]

- 13 of 13 genome IDs matched the pangenome. [^acinetobacter_adp1_explorer]
- 1,210 of 1,330 reactions matched biochemistry. [^acinetobacter_adp1_explorer]
- 230 of 230 compounds matched biochemistry. [^acinetobacter_adp1_explorer]
- 4,891 of 4,891 cluster IDs matched the pangenome through mapping. [^acinetobacter_adp1_explorer]
- ADP1 had 0 matches among 1 Fitness Browser organism query and was absent from the Fitness Browser. [^acinetobacter_adp1_explorer]
- All 13 BERDL-format genomes belong to `s__Acinetobacter_baylyi` and the clade `s__Acinetobacter_baylyi--RS_GCF_000368685.1`. [^acinetobacter_adp1_explorer]
- The BERDL pangenome contains 3,207 core and 1,684 accessory gene clusters. [^acinetobacter_adp1_explorer]
- The 120 unmatched reactions represent 9% of the 1,330 reactions and may be custom or draft reactions not yet present in ModelSEED. [^acinetobacter_adp1_explorer]

## Pangenome Cluster Bridge

ADP1 uses mmseqs2-style cluster IDs such as `NHSXFYEX_mmseqsCluster_NNNN`, whereas BERDL uses centroid gene IDs such as `NC_005966.1_1024`; the two naming systems have 0% direct string match. [^acinetobacter_adp1_explorer]

A bridge through BERDL’s `gene_genecluster_junction` table links BERDL cluster IDs to member gene IDs, which match the `feature_id` column in the ADP1 `pan_genome_features` table and expose the ADP1-style `cluster_id`. [^acinetobacter_adp1_explorer]

- All 4,891 BERDL clusters mapped successfully to 4,081 unique ADP1 clusters. [^acinetobacter_adp1_explorer]
- The mapping yielded a 100% gene-level match across 43,754 genes. [^acinetobacter_adp1_explorer]
- The generated `data/cluster_id_mapping.csv` file enables BERDL pangenome annotations, including eggNOG and functional predictions, to be joined to ADP1 genes. [^acinetobacter_adp1_explorer]

## Essentiality and Metabolic Modeling

The database compares [TnSeq](tnseq.md) essentiality calls with [FBA](flux-balance-analysis.md) flux predictions, where FBA is a constraint-based method for estimating metabolic fluxes. [^acinetobacter_adp1_explorer]

- Of 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639, or 73.8%, were concordant and 227 were discordant. [^acinetobacter_adp1_explorer]
- The 227 discordant genes are candidates for metabolic-model refinement or may reflect regulatory effects not represented by FBA. [^acinetobacter_adp1_explorer]
- Essentiality was condition-specific, with 499 genes essential on minimal media compared with 346 on LB. [^acinetobacter_adp1_explorer]
- FBA flux classes changed between rich and minimal media for 177 of 866 genes, or 20%. [^acinetobacter_adp1_explorer]
- Essential genes were more annotation-rich than dispensable genes: 33% of essential genes had COG assignments compared with 5% of dispensable genes, while 92% of essential genes had KEGG KO assignments compared with 53% of dispensable genes. [^acinetobacter_adp1_explorer]
- Approximately 8% of essential genes lacked KO assignments and were identified as potential novel essential functions. [^acinetobacter_adp1_explorer]
- Essential genes were more likely to belong to the core pangenome. [^acinetobacter_adp1_explorer]

## Condition-Specific Fitness

The database measures mutant growth fitness across 8 carbon sources and therefore contributes evidence to [condition-specific-fitness](../concepts/condition-specific-fitness.md). [^acinetobacter_adp1_explorer]

- The mean pairwise correlation among carbon-source fitness profiles was 0.44. [^acinetobacter_adp1_explorer]
- Urea fitness was nearly uncorrelated with quinate, at r = 0.11, and was weakly correlated with all other conditions, at r = 0.12–0.28. [^acinetobacter_adp1_explorer]
- Butanediol-acetate and butanediol-lactate showed the strongest correlations, at r = 0.58 and r = 0.53, respectively. [^acinetobacter_adp1_explorer]
- Because ADP1 is absent from the Fitness Browser, the 8 carbon-source mutant growth fitness measurements provide a resource not otherwise available in BERDL. [^acinetobacter_adp1_explorer]

## Reactions and Gapfilling

The database contributes evidence to [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) through reaction conservation and growth-phenotype prediction analyses. [^acinetobacter_adp1_explorer]

- Of 1,330 unique metabolic reactions, 1,248, or 94%, were shared across all 14 genomes and classified as core. [^acinetobacter_adp1_explorer]
- 62 reactions were variable, occurring in 2–13 genomes, and 20 reactions were genome-unique. [^acinetobacter_adp1_explorer]
- Gapfilling accounted for 7.7% of reactions on average, with 243 missing functions cataloged. [^acinetobacter_adp1_explorer]
- Of 121,519 growth phenotype predictions across 14 genomes, 105,376, or 87%, required at least one gapfilled reaction. [^acinetobacter_adp1_explorer]
- False negatives had higher mean gap counts than correct predictions. [^acinetobacter_adp1_explorer]

## Limitations

- FBA flux data cover only 15% of genes, and the FBA–TnSeq concordance analysis is limited to 866 genes. [^acinetobacter_adp1_explorer]
- The pangenome cluster mapping is indirect and passes through 3 tables, so edge cases involving cluster splits or merges cannot be excluded. [^acinetobacter_adp1_explorer]
- The 87% dependence of growth phenotype predictions on gapfilled reactions limits interpretation of those predictions, while the 243 missing functions represent gaps in genomic evidence that affect prediction reliability. [^acinetobacter_adp1_explorer]
- The database covers only Acinetobacter baylyi, so cross-species comparisons require comparable databases for other organisms. [^acinetobacter_adp1_explorer]

## Related Pages

- [multi-omics-integration](../concepts/multi-omics-integration.md) — incomplete overlap among six modalities and cross-strain proteomics. [^acinetobacter_adp1_explorer]
- [gene-essentiality](../concepts/gene-essentiality.md) — FBA–TnSeq concordance, condition-specific essentiality, and essentiality–pangenome relationships. [^acinetobacter_adp1_explorer]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — carbon-source mutant fitness correlations. [^acinetobacter_adp1_explorer]
- [pangenome-integration](../concepts/pangenome-integration.md) — the BERDL-to-ADP1 cluster bridge. [^acinetobacter_adp1_explorer]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — reaction conservation and gapfilling-dependent growth predictions. [^acinetobacter_adp1_explorer]
- [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) — the organism analyzed by the database. [^acinetobacter_adp1_explorer]
- [aromatic-amino-acid-biosynthesis](aromatic-amino-acid-biosynthesis.md) — engineered ADP1 strains with aromatic amino acid pathway modifications. [^acinetobacter_adp1_explorer]
- [quinate](quinate.md) and [urea](urea.md) — carbon-source fitness conditions compared in the database. [^acinetobacter_adp1_explorer]

[^acinetobacter_adp1_explorer]: [acinetobacter adp1 explorer](../summaries/acinetobacter_adp1_explorer__REPORT.md)
