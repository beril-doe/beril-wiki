---
type: "Summary"
description: "Summary of the project Acinetobacter baylyi ADP1 Data Explorer."
doc_type: "short"
full_text: "sources/acinetobacter_adp1_explorer__REPORT.md"
---
# Acinetobacter baylyi ADP1 Data Explorer

This report asks what data the Acinetobacter baylyi ADP1 SQLite database holds, how it connects to the KBase Data Lakehouse, and what it shows about essentiality, fitness, and metabolic models. The database has six data modalities for ADP1 genes, and its identifiers link well to Lakehouse pangenome and biochemistry tables. The findings come from direct counts and correlations in one species, so they do not generalize beyond A. baylyi. [src: acinetobacter_adp1_explorer]

## Key Findings

### Database contents and coverage

The database is large but uneven across modalities. It holds 15 tables with 461,522 rows and 135 MB for ADP1 and 13 related genomes. [src: acinetobacter_adp1_explorer] The user-provided berdl_tables.db supplies all 15 tables, covering the ADP1 genome, annotations, metabolic model, phenotypes, and proteomics. [src: acinetobacter_adp1_explorer] Its genome_features table has 5,852 genes and 51 annotation columns across six modalities. [src: acinetobacter_adp1_explorer] Coverage per modality:

- TnSeq (transposon sequencing) essentiality: 58%. [src: acinetobacter_adp1_explorer]
- Mutant growth fitness on 8 carbon sources: 39%. [src: acinetobacter_adp1_explorer]
- Proteomics across 7 strains: 41%. [src: acinetobacter_adp1_explorer]
- Pangenome classification: 54%. [src: acinetobacter_adp1_explorer]
- Functional annotation via COG (clusters of orthologous groups), KO (KEGG ortholog), Pfam and UniRef: 34-55%. [src: acinetobacter_adp1_explorer]
- FBA (flux balance analysis) flux: 15%. [src: acinetobacter_adp1_explorer]

No gene has data in all six modalities. Pairwise overlaps are substantial, especially between essentiality, pangenome, and proteomics. [src: acinetobacter_adp1_explorer] FBA is the sparsest modality and limits concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]

The 15 tables have 27 shared-column relationship pairs. [src: acinetobacter_adp1_explorer] The core flow runs from genome to genome_features, pan_genome_features, genome_reactions, gene_phenotypes, and growth_phenotypes_detailed. [src: acinetobacter_adp1_explorer] See adp1 sqlite database berdl tables db.

The analysis is organized in five notebooks. They cover the database inventory (tables, schemas, NULL coverage, distributions), Lakehouse connection validation through Spark queries, cluster ID bridge construction, multi-omics analysis (essentiality, FBA concordance, fitness, proteomics), and the metabolic model (gapfilling, reaction conservation, growth predictions). [src: acinetobacter_adp1_explorer]

### Links to the KBase Data Lakehouse

Four connection types validate: genome IDs (identifiers), reactions, compounds, and pangenome clusters. [src: acinetobacter_adp1_explorer] The match rates were:

| Connection | Matched |
|---|---|
| Genome IDs to pangenome | 13 of 13 (100%) [src: acinetobacter_adp1_explorer] |
| Reactions to biochemistry | 1,210 of 1,330 (91%) [src: acinetobacter_adp1_explorer] |
| Compounds to biochemistry | 230 of 230 (100%) [src: acinetobacter_adp1_explorer] |
| Cluster IDs to pangenome | 4,891 of 4,891 (100%, via mapping) [src: acinetobacter_adp1_explorer] |
| ADP1 to Fitness Browser | 0 of 1 (not present) [src: acinetobacter_adp1_explorer] |

The Lakehouse sources used were kbase_ke_pangenome, which gave pangenome context for 13 genomes and 4,891 clusters from the genome, gene_cluster, gene_genecluster_junction, gtdb_species_clade, and pangenome tables. [src: acinetobacter_adp1_explorer] The kbase_msd_biochemistry reaction and molecule tables gave ModelSEED reaction and compound name resolution. [src: acinetobacter_adp1_explorer] The kescience_fitnessbrowser organism table was checked for ADP1, which was not found. [src: acinetobacter_adp1_explorer] The phagefoundry_acinetobacter_genome_browser collection has 37 tables. It was identified but not deeply queried. [src: acinetobacter_adp1_explorer]

The 120 unmatched reactions (9%) may be custom or draft reactions not yet in ModelSEED. [src: acinetobacter_adp1_explorer] All 13 Lakehouse-format genomes belong to s__Acinetobacter_baylyi. Its pangenome has 3,207 core and 1,684 accessory gene clusters. [src: acinetobacter_adp1_explorer]

Cluster IDs needed a bridge. ADP1 uses mmseqs2-style cluster IDs and the Lakehouse uses centroid gene IDs, so direct string matching gave 0%. [src: acinetobacter_adp1_explorer] The bridge goes through the Lakehouse gene_genecluster_junction table. Its member gene IDs match feature_id in ADP1 pan_genome_features, which carries the ADP1 cluster_id. [src: acinetobacter_adp1_explorer] All 4,891 Lakehouse clusters mapped to 4,081 unique ADP1 clusters, with 100% gene-level match across 43,754 genes. [src: acinetobacter_adp1_explorer] The saved mapping, data/cluster_id_mapping.csv, has 4,891 rows and lets Lakehouse pangenome annotations be joined to ADP1 genes. [src: acinetobacter_adp1_explorer] A second output, data/berdl_connection_summary.csv, has 5 rows summarizing the connection scan. [src: acinetobacter_adp1_explorer] The mapping passes through 3 tables. It may have edge cases where clusters split or merge between the two pangenome analyses. [src: acinetobacter_adp1_explorer] See [[entities/adp1-to-pangenome-cluster-id-mapping]].

### Data unavailable elsewhere in the Lakehouse

ADP1 is absent from the Fitness Browser. The database is therefore the only source of condition-specific fitness data for this organism in the Lakehouse. [src: acinetobacter_adp1_explorer] It also supplies proteomics across 7 engineered strains. [src: acinetobacter_adp1_explorer] It supplies TnSeq essentiality calls on minimal and LB media. [src: acinetobacter_adp1_explorer] It supplies FBA predictions with gapfilling metadata. [src: acinetobacter_adp1_explorer]

The strains table documents seven strains. They are wild-type ADP1 and six aromatic amino acid pathway derivatives (ΔaroF, ΔaroG, dgoA variants). All seven have proteomics. [src: acinetobacter_adp1_explorer] Protein abundance was measured for 2,383 genes. [src: acinetobacter_adp1_explorer] High cross-strain correlation indicates targeted rather than global proteome effects of the modifications. [src: acinetobacter_adp1_explorer]

### Essentiality

Essential genes are better annotated than dispensable genes. In ADP1, 33% of essential genes have COG assignments versus 5% of dispensable genes. [src: acinetobacter_adp1_explorer] Also, 92% of essential genes have KO assignments versus 53% of dispensable genes. [src: acinetobacter_adp1_explorer] The report calls the ~8% of essential genes without KO "potential novel essential functions". [src: acinetobacter_adp1_explorer] Essential genes are also more likely to be core in the pangenome. [src: acinetobacter_adp1_explorer] More genes are essential on minimal media (499) than on LB (346). The report attributes this to the extra biosynthetic burden of minimal media. [src: acinetobacter_adp1_explorer] See [[concepts/essential-genes-and-core-genome-conservation]] and [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality]].

### Fitness across carbon sources

Fitness across the 8 carbon sources shows moderate overall correlation, with a mean pairwise r of 0.44, and notable outliers. [src: acinetobacter_adp1_explorer] Butanediol-acetate (r = 0.58) and butanediol-lactate (r = 0.53) correlate most strongly, consistent with shared central carbon metabolism. [src: acinetobacter_adp1_explorer] Urea fitness is nearly uncorrelated with quinate (r = 0.11). It correlates weakly with all other conditions (r = 0.12-0.28). The report suggests urea catabolism uses a largely independent gene set. [src: acinetobacter_adp1_explorer]

### Metabolic model and gapfilling

Of 866 genes with both FBA flux and TnSeq essentiality calls, 639 (73.8%) are concordant. [src: acinetobacter_adp1_explorer] The discordant 26% are candidates for model refinement. They may also reflect regulatory effects that FBA does not capture. [src: acinetobacter_adp1_explorer] The report counts 227 genes with discordant FBA and TnSeq calls. [src: acinetobacter_adp1_explorer] Also, 20% of genes (177/866) change FBA flux class between rich and minimal media. The report reads this as condition-dependent metabolic rewiring. [src: acinetobacter_adp1_explorer] See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

Of 1,330 unique reactions, 1,248 (94%) are shared by all 14 Acinetobacter genomes. Another 62 are variable (2-13 genomes), and 20 are genome-unique. [src: acinetobacter_adp1_explorer] Gapfilling accounts for 7.7% of reactions on average. [src: acinetobacter_adp1_explorer] The database catalogs 243 missing functions. [src: acinetobacter_adp1_explorer] Of 121,519 growth predictions across 14 genomes, 105,376 (87%) need at least one gapfilled reaction. [src: acinetobacter_adp1_explorer] This ties prediction accuracy tightly to gapfilling quality. [src: acinetobacter_adp1_explorer] False negatives have higher mean gap counts than correct predictions. [src: acinetobacter_adp1_explorer] The 243 missing functions are genuine gaps in genomic evidence that affect prediction reliability. [src: acinetobacter_adp1_explorer]

## Caveats and Open Work

- No gene has all six modalities, and FBA covers only 866 genes. [src: acinetobacter_adp1_explorer]
- The cluster mapping is indirect and may have split or merge edge cases. [src: acinetobacter_adp1_explorer]
- Predictions depend heavily on gapfilling. [src: acinetobacter_adp1_explorer]
- The database covers only A. baylyi. Cross-species work would need similar databases for other organisms. [src: acinetobacter_adp1_explorer]
- The PhageFoundry Acinetobacter genome browser was not deeply queried. [src: acinetobacter_adp1_explorer]

The report proposes these next analyses:

- Test whether the 227 FBA-TnSeq discordant genes are enriched for specific pathways or regulatory functions, to guide model refinement. [src: acinetobacter_adp1_explorer]
- Use the cluster ID mapping to compare ADP1 mutant growth with Fitness Browser data for related organisms, even though ADP1 is not in that dataset. [src: acinetobacter_adp1_explorer]
- Cross-reference the PhageFoundry Acinetobacter genome browser with phage susceptibility data. [src: acinetobacter_adp1_explorer]
- Identify urea-specific genes and examine their pangenome conservation. [src: acinetobacter_adp1_explorer]
- Assess gapfill confidence using pangenome conservation, given 243 missing functions and 87% of predictions depending on gapfilling, to improve prediction reliability. [src: acinetobacter_adp1_explorer]

## Slots Into

- [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]]: 639 of 866 genes (73.8%) are concordant between FBA and TnSeq. [src: acinetobacter_adp1_explorer]
- [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality]]: essential genes are richer in COG and KO annotation. [src: acinetobacter_adp1_explorer]
- [[concepts/essential-genes-and-core-genome-conservation]]: essential genes lean toward the core pangenome. [src: acinetobacter_adp1_explorer]
- [[concepts/condition-specific-fitness-correlation-across-carbon-sources]]: mean pairwise r is 0.44 across 8 carbon sources. [src: acinetobacter_adp1_explorer]
- [[concepts/join-key-validity-and-identifier-format-mismatches]]: cluster IDs had 0% direct string match and needed a bridge. [src: acinetobacter_adp1_explorer]
