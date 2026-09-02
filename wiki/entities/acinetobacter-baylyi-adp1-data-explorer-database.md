---
type: "Dataset"
description: "Integrated SQLite dataset for multi-omics analysis of Acinetobacter baylyi ADP1"
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md"]
---
# Acinetobacter baylyi ADP1 Data Explorer Database

## Identity

**Canonical name:** Acinetobacter baylyi ADP1 Data Explorer Database [src: acinetobacter_adp1_explorer]

**Known aliases:** ADP1 Data Explorer database; user-provided ADP1 SQLite database [src: acinetobacter_adp1_explorer]

**Stable external identifier:** None reported in the source document. [src: acinetobacter_adp1_explorer]

This dataset is a user-provided SQLite database integrating genome features, [[entities/tnseq|TnSeq]] essentiality, [[entities/flux-balance-analysis|flux balance analysis (FBA)]], mutant growth fitness, proteomics, pangenome classification, functional annotations, metabolic reactions, and growth phenotypes for [[entities/acinetobacter-baylyi-adp1|Acinetobacter baylyi ADP1]] and 13 related genomes. [src: acinetobacter_adp1_explorer]

See the source summary at [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Key Facts

- The database contains 15 tables, 461,522 total rows, and 135 MB of data. [src: acinetobacter_adp1_explorer]
- Its central `genome_features` table contains 5,852 genes and 51 annotation columns. [src: acinetobacter_adp1_explorer]
- The six principal data modalities cover TnSeq essentiality at 58%, FBA metabolic flux at 15%, mutant growth fitness on 8 carbon sources at 39%, proteomics across 7 strains at 41%, pangenome classification at 54%, and functional annotations through COG, KO, Pfam, and UniRef at 34–55%. [src: acinetobacter_adp1_explorer]
- No single gene has data across all six modalities, although pairwise overlaps are substantial, particularly among essentiality, pangenome, and proteomics. [src: acinetobacter_adp1_explorer]
- The database documents 7 engineered ADP1 strains, including wild-type ADP1 and 6 derivatives with aromatic amino acid pathway modifications involving ΔaroF and ΔaroG or dgoA variants. [src: acinetobacter_adp1_explorer]
- Proteomics data are available for all 7 strains, with protein abundance measured for 2,383 genes. [src: acinetobacter_adp1_explorer]
- Cross-strain proteomic correlation was high, indicating targeted rather than global effects of the engineered modifications. [src: acinetobacter_adp1_explorer]

## BERDL Connectivity

The database connects to the [[entities/kbase-ke-pangenome|KBase KE pangenome]], [[entities/kbase-msd-biochemistry|KBase MSD Biochemistry]], and [[entities/kescience-fitnessbrowser|KE Science Fitness Browser]] collections. [src: acinetobacter_adp1_explorer]

- 13 of 13 genome IDs matched the pangenome. [src: acinetobacter_adp1_explorer]
- 1,210 of 1,330 reactions matched biochemistry. [src: acinetobacter_adp1_explorer]
- 230 of 230 compounds matched biochemistry. [src: acinetobacter_adp1_explorer]
- 4,891 of 4,891 cluster IDs matched the pangenome through mapping. [src: acinetobacter_adp1_explorer]
- ADP1 had 0 matches among 1 Fitness Browser organism query and was absent from the Fitness Browser. [src: acinetobacter_adp1_explorer]
- All 13 BERDL-format genomes belong to `s__Acinetobacter_baylyi` and the clade `s__Acinetobacter_baylyi--RS_GCF_000368685.1`. [src: acinetobacter_adp1_explorer]
- The BERDL pangenome contains 3,207 core and 1,684 accessory gene clusters. [src: acinetobacter_adp1_explorer]
- The 120 unmatched reactions represent 9% of the 1,330 reactions and may be custom or draft reactions not yet present in ModelSEED. [src: acinetobacter_adp1_explorer]

## Pangenome Cluster Bridge

ADP1 uses mmseqs2-style cluster IDs such as `NHSXFYEX_mmseqsCluster_NNNN`, whereas BERDL uses centroid gene IDs such as `NC_005966.1_1024`; the two naming systems have 0% direct string match. [src: acinetobacter_adp1_explorer]

A bridge through BERDL’s `gene_genecluster_junction` table links BERDL cluster IDs to member gene IDs, which match the `feature_id` column in the ADP1 `pan_genome_features` table and expose the ADP1-style `cluster_id`. [src: acinetobacter_adp1_explorer]

- All 4,891 BERDL clusters mapped successfully to 4,081 unique ADP1 clusters. [src: acinetobacter_adp1_explorer]
- The mapping yielded a 100% gene-level match across 43,754 genes. [src: acinetobacter_adp1_explorer]
- The generated `data/cluster_id_mapping.csv` file enables BERDL pangenome annotations, including eggNOG and functional predictions, to be joined to ADP1 genes. [src: acinetobacter_adp1_explorer]

## Essentiality and Metabolic Modeling

The database compares [[entities/tnseq|TnSeq]] essentiality calls with [[entities/flux-balance-analysis|FBA]] flux predictions, where FBA is a constraint-based method for estimating metabolic fluxes. [src: acinetobacter_adp1_explorer]

- Of 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639, or 73.8%, were concordant and 227 were discordant. [src: acinetobacter_adp1_explorer]
- The 227 discordant genes are candidates for metabolic-model refinement or may reflect regulatory effects not represented by FBA. [src: acinetobacter_adp1_explorer]
- Essentiality was condition-specific, with 499 genes essential on minimal media compared with 346 on LB. [src: acinetobacter_adp1_explorer]
- FBA flux classes changed between rich and minimal media for 177 of 866 genes, or 20%. [src: acinetobacter_adp1_explorer]
- Essential genes were more annotation-rich than dispensable genes: 33% of essential genes had COG assignments compared with 5% of dispensable genes, while 92% of essential genes had KEGG KO assignments compared with 53% of dispensable genes. [src: acinetobacter_adp1_explorer]
- Approximately 8% of essential genes lacked KO assignments and were identified as potential novel essential functions. [src: acinetobacter_adp1_explorer]
- Essential genes were more likely to belong to the core pangenome. [src: acinetobacter_adp1_explorer]

## Condition-Specific Fitness

The database measures mutant growth fitness across 8 carbon sources and therefore contributes evidence to [[concepts/condition-specific-fitness]]. [src: acinetobacter_adp1_explorer]

- The mean pairwise correlation among carbon-source fitness profiles was 0.44. [src: acinetobacter_adp1_explorer]
- Urea fitness was nearly uncorrelated with quinate, at r = 0.11, and was weakly correlated with all other conditions, at r = 0.12–0.28. [src: acinetobacter_adp1_explorer]
- Butanediol-acetate and butanediol-lactate showed the strongest correlations, at r = 0.58 and r = 0.53, respectively. [src: acinetobacter_adp1_explorer]
- Because ADP1 is absent from the Fitness Browser, the 8 carbon-source mutant growth fitness measurements provide a resource not otherwise available in BERDL. [src: acinetobacter_adp1_explorer]

## Reactions and Gapfilling

The database contributes evidence to [[concepts/metabolic-model-gapfilling]] through reaction conservation and growth-phenotype prediction analyses. [src: acinetobacter_adp1_explorer]

- Of 1,330 unique metabolic reactions, 1,248, or 94%, were shared across all 14 genomes and classified as core. [src: acinetobacter_adp1_explorer]
- 62 reactions were variable, occurring in 2–13 genomes, and 20 reactions were genome-unique. [src: acinetobacter_adp1_explorer]
- Gapfilling accounted for 7.7% of reactions on average, with 243 missing functions cataloged. [src: acinetobacter_adp1_explorer]
- Of 121,519 growth phenotype predictions across 14 genomes, 105,376, or 87%, required at least one gapfilled reaction. [src: acinetobacter_adp1_explorer]
- False negatives had higher mean gap counts than correct predictions. [src: acinetobacter_adp1_explorer]

## Limitations

- FBA flux data cover only 15% of genes, and the FBA–TnSeq concordance analysis is limited to 866 genes. [src: acinetobacter_adp1_explorer]
- The pangenome cluster mapping is indirect and passes through 3 tables, so edge cases involving cluster splits or merges cannot be excluded. [src: acinetobacter_adp1_explorer]
- The 87% dependence of growth phenotype predictions on gapfilled reactions limits interpretation of those predictions, while the 243 missing functions represent gaps in genomic evidence that affect prediction reliability. [src: acinetobacter_adp1_explorer]
- The database covers only Acinetobacter baylyi, so cross-species comparisons require comparable databases for other organisms. [src: acinetobacter_adp1_explorer]

## Related Pages

- [[concepts/multi-omics-integration]] — incomplete overlap among six modalities and cross-strain proteomics. [src: acinetobacter_adp1_explorer]
- [[concepts/gene-essentiality]] — FBA–TnSeq concordance, condition-specific essentiality, and essentiality–pangenome relationships. [src: acinetobacter_adp1_explorer]
- [[concepts/condition-specific-fitness]] — carbon-source mutant fitness correlations. [src: acinetobacter_adp1_explorer]
- [[concepts/pangenome-integration]] — the BERDL-to-ADP1 cluster bridge. [src: acinetobacter_adp1_explorer]
- [[concepts/metabolic-model-gapfilling]] — reaction conservation and gapfilling-dependent growth predictions. [src: acinetobacter_adp1_explorer]
- [[entities/acinetobacter-baylyi-adp1]] — the organism analyzed by the database. [src: acinetobacter_adp1_explorer]
- [[entities/aromatic-amino-acid-biosynthesis]] — engineered ADP1 strains with aromatic amino acid pathway modifications. [src: acinetobacter_adp1_explorer]
- [[entities/quinate]] and [[entities/urea]] — carbon-source fitness conditions compared in the database. [src: acinetobacter_adp1_explorer]
