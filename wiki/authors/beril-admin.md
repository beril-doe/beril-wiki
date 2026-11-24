# Beril Admin

*Not a person — a BERIL service account. Listed as an author on the projects below.*

ORCID: [0009-0007-0287-2979](https://orcid.org/0009-0007-0287-2979)

## Contributions

The project [[summaries/acinetobacter_adp1_explorer__REPORT]] inventoried the Acinetobacter baylyi ADP1 SQLite database. The database holds 15 tables with 461,522 rows and 135 MB for ADP1 and 13 related genomes [src: acinetobacter_adp1_explorer]. Its genome_features table has 5,852 genes and 51 annotation columns across six modalities [src: acinetobacter_adp1_explorer]. Coverage per modality was TnSeq (transposon sequencing) essentiality 58%, mutant growth fitness on 8 carbon sources 39%, proteomics across 7 strains 41%, and pangenome classification 54% [src: acinetobacter_adp1_explorer]. FBA (flux balance analysis) flux covered 15% of genes. No gene has data in all six modalities [src: acinetobacter_adp1_explorer]. The findings come from one species and do not generalize beyond A. baylyi [src: acinetobacter_adp1_explorer].

The project also validated links to the KBase Data Lakehouse. Genome IDs matched the pangenome 13 of 13 (100%), reactions matched biochemistry 1,210 of 1,330 (91%), and compounds matched 230 of 230 (100%) [src: acinetobacter_adp1_explorer]. ADP1 was not found in the Fitness Browser [src: acinetobacter_adp1_explorer]. Direct string matching of cluster IDs gave 0%, because ADP1 uses mmseqs2-style IDs and the Lakehouse uses centroid gene IDs [src: acinetobacter_adp1_explorer]. A bridge through the gene_genecluster_junction table mapped all 4,891 Lakehouse clusters to 4,081 unique ADP1 clusters, with 100% gene-level match across 43,754 genes [src: acinetobacter_adp1_explorer]. The report notes the mapping may have edge cases where clusters split or merge [src: acinetobacter_adp1_explorer]. See [[concepts/join-key-validity-and-identifier-format-mismatches]].

On essentiality and fitness, 33% of essential genes have COG assignments versus 5% of dispensable genes, and 92% of essential genes have KO assignments versus 53% of dispensable genes [src: acinetobacter_adp1_explorer]. More genes are essential on minimal media (499) than on LB (346) [src: acinetobacter_adp1_explorer]. See [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality]]. Fitness across the 8 carbon sources had a mean pairwise r of 0.44. Butanediol-acetate was highest at r = 0.58, and urea fitness was nearly uncorrelated with quinate (r = 0.11) [src: acinetobacter_adp1_explorer].

On the metabolic model, 639 of 866 genes (73.8%) with both FBA flux and TnSeq calls were concordant [src: acinetobacter_adp1_explorer]. See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]]. Of 1,330 unique reactions, 1,248 (94%) are shared by all 14 Acinetobacter genomes [src: acinetobacter_adp1_explorer]. Gapfilling accounts for 7.7% of reactions on average. Of 121,519 growth predictions, 105,376 (87%) need at least one gapfilled reaction [src: acinetobacter_adp1_explorer].

## Projects (1)

- [[summaries/acinetobacter_adp1_explorer__REPORT|acinetobacter_adp1_explorer]]
