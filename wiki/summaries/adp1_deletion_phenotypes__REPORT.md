---
type: "Summary"
description: "Summary of the project ADP1 Deletion Collection Phenotype Analysis."
doc_type: "short"
full_text: "sources/adp1_deletion_phenotypes__REPORT.md"
---
# ADP1 Deletion Collection Phenotype Analysis

This page summarises the ADP1 Deletion Collection Phenotype Analysis. Growth phenotypes in the *Acinetobacter baylyi* ADP1 deletion collection form a continuum with about 5 independent dimensions, and only the quinate pathway module is discrete. [src: adp1_deletion_phenotypes] The evidence is one organism and one deletion dataset, analysed with PCA, correlation and clustering. [src: adp1_deletion_phenotypes] A cross-reference with KBase Data Lakehouse pangenome data adds that the 272 missing dispensable genes are less conserved across *Acinetobacter* species. [src: adp1_deletion_phenotypes] See [[entities/acinetobacter-baylyi-adp1]] and [[entities/de-berardinis-et-al-2008-adp1-deletion-mutant-collection]].

## Key Findings

### Condition tiers
The 8 carbon sources split into demanding, moderate and robust tiers, and the tiers hold across multiple defect thresholds. [src: adp1_deletion_phenotypes] The complete growth matrix has 2,034 genes measured on all 8 sources. [src: adp1_deletion_phenotypes] Growth ratios are mutant/wild-type; values below 1.0 mean defects, and values above 1.0 mean no defect or a slight advantage from normalization. [src: adp1_deletion_phenotypes] Mean growth ratio spans a 3.3-fold range, from 0.41 for urea to 1.36 for quinate. [src: adp1_deletion_phenotypes]

Urea is the most demanding condition, with 97.9% of genes showing severe defects at ratio < 0.5. [src: adp1_deletion_phenotypes] Quinate is the most robust, with only 1.6% of genes defective. [src: adp1_deletion_phenotypes] The demanding tier (urea, acetate, butanediol) has mean growth ratio 0.41–0.65, with defects at ratio < 0.8 in 95–100% of genes. [src: adp1_deletion_phenotypes] The moderate tier (asparagine, lactate) has mean growth ratio 0.80–0.82, with defects in 37–45% of genes. [src: adp1_deletion_phenotypes] The robust tier (glucarate, glucose, quinate) has mean growth ratio 1.25–1.36, with defects in 0.5–2.4% of genes. [src: adp1_deletion_phenotypes]

### Dimensionality of the phenotype
Together these results say the 8 conditions carry about 5 independent dimensions of information. [src: adp1_deletion_phenotypes]

- Conditions are only moderately correlated: the highest pair is acetate–butanediol at r = 0.58, and the median across all 28 pairs is r = 0.25. [src: adp1_deletion_phenotypes]
- PCA ([[entities/principal-component-analysis]]) of the 2,034×8 matrix needs 5 components to capture 82% of variance. [src: adp1_deletion_phenotypes]
- No single component captures more than 37% of variance. [src: adp1_deletion_phenotypes]
- PC1 (36.7%) is general growth sensitivity, with all conditions loading positively. [src: adp1_deletion_phenotypes]
- PC2 (12.7%) isolates urea (loading = +0.75) and separates nitrogen from carbon metabolism. [src: adp1_deletion_phenotypes]
- The remaining components distinguish specific carbon-source pairs. [src: adp1_deletion_phenotypes]
- The report concludes the 8 conditions give about 5 independent dimensions, more than a two-group demanding/robust model suggests. [src: adp1_deletion_phenotypes]
- It contrasts this with correlated fitness profiles in many *E. coli* chemical-genomics conditions (Nichols et al. 2011). [src: adp1_deletion_phenotypes]
- It proposes, as an explanation, that the carbon sources enter central metabolism at different points. [src: adp1_deletion_phenotypes]
- The report suggests that these ~5 dimensions from 8 conditions imply that more carbon sources, nitrogen sources or stress conditions would substantially increase phenotypic resolution. [src: adp1_deletion_phenotypes]

### Continuous landscape, one discrete module
Clustering finds no natural groups beyond one small quinate module. [src: adp1_deletion_phenotypes]

- Hierarchical clustering gives an optimal K = 3 with a low silhouette score of 0.24. [src: adp1_deletion_phenotypes]
- The score stays low across all tested k values from 2 to 25, which the report reads as a lack of natural cluster boundaries. [src: adp1_deletion_phenotypes]
- The two large modules, with 1,160 and 850 genes, are broadly "generally sensitive" and "generally tolerant" groups. [src: adp1_deletion_phenotypes]
- Neither has functional enrichment that survives false discovery rate (FDR) correction. [src: adp1_deletion_phenotypes]
- The module enrichment output file has 0 rows because no enrichments are significant after FDR correction. [src: adp1_deletion_phenotypes]
- The report treats this null result as informative: the phenotype landscape is a continuum. [src: adp1_deletion_phenotypes]
- It interprets essentiality as varying continuously across conditions rather than in discrete functional categories. [src: adp1_deletion_phenotypes]
- This agrees with Guzman et al. (2018)'s proposal of continuous essentiality, seen here as a gradient across conditions. [src: adp1_deletion_phenotypes]
- It also supports their "adaptive flexibility" framework. [src: adp1_deletion_phenotypes]
- The one exception is a small module of 24 aromatic-degradation genes, with mean z-score -7.28 on quinate and near zero on other conditions. [src: adp1_deletion_phenotypes]
- It is the only discrete phenotypic module. [src: adp1_deletion_phenotypes]
- The report finds no other discrete modules in ADP1. [src: adp1_deletion_phenotypes]
- This differs from the *E. coli* phenotypic modules of Nichols et al. (2011), which extend beyond operon boundaries. [src: adp1_deletion_phenotypes]
- The report suggests the difference may come from deletion versus chemical perturbation, or from more interconnected ADP1 metabolism. [src: adp1_deletion_phenotypes]

### Condition-specific genes
In ADP1, 625 genes (31%) have a condition specificity score ≥ 1.0, so their importance is concentrated on one carbon source. [src: adp1_deletion_phenotypes] The report reads this as nearly one-third of the dispensable genome having condition-specific importance. [src: adp1_deletion_phenotypes] It says the top genes for each carbon source match the expected pathways. [src: adp1_deletion_phenotypes]

The top quinate genes are pcaC, pcaG, pcaH, pcaB, quiA, quiB, pqqC and pqqD, covering protocatechuate/quinate degradation and PQQ biosynthesis. [src: adp1_deletion_phenotypes] The top urea genes are ureA to ureG, all 7 urease subunits and accessory proteins. [src: adp1_deletion_phenotypes] For asparagine they are aspartate ammonia-lyase and L-asparaginase. [src: adp1_deletion_phenotypes] For acetate they are fadB, malate synthase G and citB, covering β-oxidation and the glyoxylate shunt. [src: adp1_deletion_phenotypes] For glucarate they are gudD, a D-glucarate transporter and 2,5-dioxovalerate dehydrogenase. [src: adp1_deletion_phenotypes] For glucose they are eda, gntT, gluconokinase and PQQ-dependent glucose dehydrogenase. [src: adp1_deletion_phenotypes] For butanediol they are 2,3-butanediol dehydrogenase and E2 acetyltransferase. [src: adp1_deletion_phenotypes] For lactate they are lldR and cyoC/cyoD. [src: adp1_deletion_phenotypes]

The quinate-specific set has 51 genes at spec > 0.5, z < -1, and extends to Complex I NADH-ubiquinone oxidoreductase subunits, suggesting unique electron-transport demands of aromatic catabolism. [src: adp1_deletion_phenotypes] PQQ (pyrroloquinoline quinone) biosynthesis genes are specific for both quinate and glucose, consistent with PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [src: adp1_deletion_phenotypes] The quinate result aligns with Fischer et al. (2008) on coordinated, carbon-source-dependent regulation of aromatic degradation operons. [src: adp1_deletion_phenotypes]

The report concludes that condition-specific phenotyping greatly increases functional annotation yield. [src: adp1_deletion_phenotypes] Many of the 625 genes have known functions that a single carbon source would miss. [src: adp1_deletion_phenotypes] Wetmore et al. (2015) showed that RB-TnSeq (random barcode transposon sequencing) across diverse conditions identifies condition-specific gene functions. [src: adp1_deletion_phenotypes]

### Genes missing from the collection
Of 2,593 TnSeq-dispensable genes (TnSeq is transposon sequencing), 272 (10.5%) lack deletion-collection growth data, and 2,321 have data. [src: adp1_deletion_phenotypes] Missing genes have mean length 813 bp against 981 bp for present genes. [src: adp1_deletion_phenotypes] RAST annotation covers 91% of missing genes against 100% of present genes. [src: adp1_deletion_phenotypes] KO (KEGG ortholog) annotation covers 49% against 59%. [src: adp1_deletion_phenotypes] Pangenome-core membership is 76.5% for missing genes against 93.3% for present genes (p = 1.4×10⁻²⁰). [src: adp1_deletion_phenotypes]

Missing genes are enriched for completely unannotated proteins (25 genes, q = 2.4×10⁻²⁵). [src: adp1_deletion_phenotypes] They are also enriched for "hypothetical protein" annotations (48 genes, q = 3.0×10⁻⁴). [src: adp1_deletion_phenotypes] The 313 uncertain-class genes have 361 bp mean length, 42% annotated and 31% core, consistent with fragments or pseudogenes rather than true essential genes. [src: adp1_deletion_phenotypes]

The cross-reference with pangenome data shows the 272 missing dispensable genes are significantly less conserved across *Acinetobacter* species. [src: adp1_deletion_phenotypes] The report suggests dispensability and pangenome status are linked through evolutionary retention pressure. [src: adp1_deletion_phenotypes] It links this to pangenome dynamics: the least conserved genes are the most likely to be missed in building a deletion collection. [src: adp1_deletion_phenotypes] It cites Rosconi et al. (2022), who showed that pangenome variation makes essentiality strain-dependent and evolvable. [src: adp1_deletion_phenotypes] It says its KBase Data Lakehouse-integrated analysis adds three insights beyond the original de Berardinis et al. (2008) data. [src: adp1_deletion_phenotypes]

## Data and Methods
The data are growth ratios for 2,034 ADP1 deletion mutants on 8 carbon sources. [src: adp1_deletion_phenotypes] They come from the user-provided SQLite database berdl_tables.db, whose genome_features table supplies growth ratios, TnSeq essentiality and functional annotations for 5,852 ADP1 genes. [src: adp1_deletion_phenotypes] Pangenome cluster IDs and core/accessory status come from kbase_ke_pangenome, cross-referenced through the pangenome_cluster_id column of genome_features. [src: adp1_deletion_phenotypes] The methods are PCA, pairwise correlation, hierarchical clustering with silhouette scoring, and FDR-corrected enrichment tests. [src: adp1_deletion_phenotypes]

Derived tables have these sizes:

| Table | Rows | Content |
|---|---|---|
| growth_matrix_complete | 2,034 | genes with growth data on all 8 conditions [src: adp1_deletion_phenotypes] |
| growth_matrix_all | 2,350 | genes with growth data on any condition [src: adp1_deletion_phenotypes] |
| all_genes_annotated | 5,852 | all genes with annotations and TnSeq classification [src: adp1_deletion_phenotypes] |
| gene_modules | 2,034 | gene-to-module assignments (K=3) [src: adp1_deletion_phenotypes] |
| condition_specific_genes | 2,034 | per-condition specificity scores [src: adp1_deletion_phenotypes] |
| tnseq_gap_analysis | 3,405 | TnSeq genes with gap classification [src: adp1_deletion_phenotypes] |

## Caveats and Open Work
- The clustering null result limits any claim of functional modules; the only discrete module is the 24-gene quinate group. [src: adp1_deletion_phenotypes]
- The ADP1 versus *E. coli* difference may reflect method, since this study used single-gene deletions and Nichols et al. used chemical perturbations. [src: adp1_deletion_phenotypes]
- 272 dispensable genes have no growth data, and the missing genes are biased toward short, less annotated, less conserved genes. [src: adp1_deletion_phenotypes]
- Growth ratios are single-timepoint measurements with unknown technical noise, and the specificity analysis assumes variation across conditions is biological, not measurement error. [src: adp1_deletion_phenotypes]
- The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing it toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]
- Only 8 carbon sources were tested, so the ~5 independent dimensions may increase with more conditions. [src: adp1_deletion_phenotypes]
- Pangenome core/accessory status comes from the species-level *A. baylyi* pangenome, which may have limited resolution compared with a population-level analysis. [src: adp1_deletion_phenotypes]
- Proposed next analyses: apply independent component analysis (ICA) instead of hierarchical clustering, since ICA may find latent factors that hierarchical clustering misses. [src: adp1_deletion_phenotypes]
- Compare ADP1 specificity profiles with Fitness Browser RB-TnSeq data for organisms grown on overlapping carbon sources such as glucose and lactate, to ask whether the same pathways are condition-specific across species. [src: adp1_deletion_phenotypes]
- Use the condition-specific gene sets to infer regulatory relationships, since genes co-specific for a condition may share transcriptional regulators. [src: adp1_deletion_phenotypes]
- Expand the condition panel with more carbon sources, nitrogen sources or stress conditions. [src: adp1_deletion_phenotypes]

## Slots Into
- [[concepts/continuous-versus-discrete-structure-of-condition-dependent-gene-essentiality]]: no discrete modules (silhouette 0.24), except the 24-gene quinate module. [src: adp1_deletion_phenotypes]
- [[concepts/condition-specific-gene-phenotypes-and-functional-annotation-yield]]: 625 condition-specific genes raise annotation yield. [src: adp1_deletion_phenotypes]
- [[concepts/coverage-gaps-in-deletion-collections-and-their-link-to-pangenome-conservation]]: missing dispensable genes are less conserved (76.5% core vs 93.3%). [src: adp1_deletion_phenotypes]
- [[concepts/condition-specific-gene-importance-across-carbon-sources]]: 625 genes (31%) have specificity ≥ 1.0. [src: adp1_deletion_phenotypes]
- [[concepts/condition-specific-fitness-correlation-across-carbon-sources]]: the median pairwise correlation is r = 0.25. [src: adp1_deletion_phenotypes]
- [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]]: quinate-specific genes include Complex I subunits. [src: adp1_deletion_phenotypes]
