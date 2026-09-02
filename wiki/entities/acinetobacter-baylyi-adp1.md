---
type: "Organism"
description: "Acinetobacter baylyi ADP1 genome, fitness, metabolism, and respiratory wiring"
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Acinetobacter baylyi ADP1

## Identity

**Canonical name:** *Acinetobacter baylyi* ADP1. [src: acinetobacter_adp1_explorer]

**Known aliases:** ADP1; *A. baylyi*. [src: acinetobacter_adp1_explorer]

**Stable external identifier:** No stable external identifier is provided in the report. [src: acinetobacter_adp1_explorer]

## Key Facts

The analyzed database contains data for *Acinetobacter baylyi* ADP1 and 13 related genomes, with 15 tables, 461,522 total rows, and 135 MB of data. [src: acinetobacter_adp1_explorer]

The database integrates genome features, [[entities/tnseq]] essentiality, [[entities/flux-balance-analysis]] (FBA, a growth-optimizing metabolic modeling method), mutant growth fitness, proteomics, pangenome classification, functional annotations, metabolic reactions, and growth phenotypes. [src: acinetobacter_adp1_explorer]

The central `genome_features` table contains 5,852 genes and 51 annotation columns. [src: acinetobacter_adp1_explorer] Its six major modalities cover TnSeq essentiality (58%), FBA metabolic flux (15%), mutant growth fitness on 8 carbon sources (39%), proteomics across 7 strains (41%), pangenome classification (54%), and functional annotations through COG, KO, Pfam, and UniRef (34–55%). [src: acinetobacter_adp1_explorer] No single gene has data across all six modalities, although pairwise overlaps are substantial, particularly among essentiality, pangenome, and proteomics. [src: acinetobacter_adp1_explorer]

The database documents 7 engineered ADP1 strains, including wild-type ADP1 and 6 derivatives with aromatic amino acid pathway modifications involving ΔaroF and ΔaroG or dgoA variants. [src: acinetobacter_adp1_explorer] Proteomics covers all 7 strains and 2,383 genes; cross-strain correlation was high and indicated targeted rather than global effects of the engineered modifications. [src: acinetobacter_adp1_explorer]

The new respiratory-chain analysis **extends** this multi-omic profile: ADP1 has 62 respiratory-chain genes across 8 subsystems, and condition-specific gene phenotypes, FBA, theoretical stoichiometry, cross-species fitness, and proteomics support substrate-dependent respiratory configurations. [src: respiratory_chain_wiring]

## BERDL Integration

All 13 BERDL-format genomes belong to *s__Acinetobacter_baylyi* and the clade `s__Acinetobacter_baylyi--RS_GCF_000368685.1`. [src: acinetobacter_adp1_explorer]

The BERDL pangenome contains 3,207 core and 1,684 accessory gene clusters. [src: acinetobacter_adp1_explorer]

Four of five tested connection types matched BERDL at greater than 90%: 13 of 13 genome IDs matched the pangenome, 1,210 of 1,330 reactions matched [[entities/kbase-msd-biochemistry]], 230 of 230 compounds matched biochemistry, and 4,891 of 4,891 cluster IDs matched the pangenome through mapping. [src: acinetobacter_adp1_explorer]

ADP1 had 0 matches among 1 Fitness Browser organism query and was absent from [[entities/kescience-fitnessbrowser]]. [src: acinetobacter_adp1_explorer] The ADP1 database was connected to [[entities/kbase-ke-pangenome]], [[entities/kbase-msd-biochemistry]], and [[entities/kescience-fitnessbrowser]] collections. [src: acinetobacter_adp1_explorer]

## Essentiality and Metabolism

Among 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639 genes, or 73.8%, were concordant and 227 were discordant. [src: acinetobacter_adp1_explorer] Essentiality was condition-specific: 499 genes were essential on minimal media compared with 346 on LB, and FBA flux classes changed between rich and minimal media for 177 of 866 genes, or 20%. [src: acinetobacter_adp1_explorer]

Essential genes were more annotation-rich and more likely to belong to the core pangenome than dispensable genes: 33% of essential genes had COG assignments versus 5% of dispensable genes, 92% had KEGG KO assignments versus 53%, and approximately 8% lacked KO assignments and were potential novel essential functions. [src: acinetobacter_adp1_explorer]

The deletion-collection analysis **refines** these binary and TnSeq comparisons: among 2,034 genes measured across 8 carbon sources, growth ratios spanned 0.41 on urea to 1.36 on quinate, and 625 genes had condition-specificity scores ≥ 1.0. [src: adp1_deletion_phenotypes] Hierarchical clustering had optimal K = 3 but a silhouette score of 0.24, with no FDR-significant functional enrichment; only a 24-gene quinate-specific aromatic-degradation module was discrete. [src: adp1_deletion_phenotypes]

The triple-essentiality analysis **refines** the 866-gene binary comparison. Among 478 TnSeq-dispensable genes with FBA and mutant-growth data, FBA class was not associated with growth-defect status (chi-squared = 0.93, p = 0.63, 2 df), with defect rates of 73.1% (57/78), 73.5% (150/204), and 69.4% (136/196) for FBA-essential, FBA-variable, and FBA-blocked genes; the Kruskal-Wallis test was also non-significant (H = 1.67, p = 0.43). [src: adp1_triple_essentiality] The refined knockout comparison found moderate FBA concordance: rich media covered 724 genes with recall = 60.8%, precision = 64.0%, specificity = 79.7%, F1 = 0.624, and Cohen’s kappa = 0.486; minimal media covered 833 genes with recall = 65.6%, precision = 69.2%, specificity = 78.9%, F1 = 0.673, and Cohen’s kappa = 0.493. [src: adp1_triple_essentiality]

RB-TnSeq (random barcode transposon sequencing) **contradicts** complete-knockout essentiality in rich media across thresholds of 0.01, 0.025, 0.05, 0.10, and 0.20, where Cohen’s kappa was -0.139, -0.122, -0.081, -0.024, and -0.014, respectively. At 0.05, 1,933 genes yielded recall = 7.9%, precision = 5.8%, specificity = 82.8%, F1 = 0.067, and kappa = -0.081. [src: adp1_triple_essentiality] Continuous fitness **refines** binary essentiality: inverted fitness had AUC = 0.700 in rich media and AUC = 0.725 in minimal media, whereas essentiality fraction had AUC = 0.344 and AUC = 0.403. AUC means Area Under the ROC Curve, a threshold-independent classification measure. [src: adp1_triple_essentiality]

Of 1,330 unique metabolic reactions, 1,248, or 94%, were shared across all 14 genomes and classified as core; 62 were variable, occurring in 2–13 genomes, and 20 were genome-unique. [src: acinetobacter_adp1_explorer] Gapfilling accounted for 7.7% of reactions on average, with 243 missing functions cataloged; of 121,519 growth phenotype predictions across 14 genomes, 105,376, or 87%, required at least one gapfilled reaction. [src: acinetobacter_adp1_explorer]

The aromatic-catabolism analysis **refines** the FBA–fitness picture with a 51-gene quinate support network surrounding the [[entities/beta-ketoadipate-pathway]]. Its 44/51 assigned genes span 8 aromatic-pathway genes, 21 [[entities/complex-i]] genes, 7 iron-acquisition genes, and 2 [[entities/pqq-biosynthesis]] genes; 6 are transcriptional regulators and 7 remain unassigned. [src: aromatic_catabolism_network]

Complex I accounted for 21/51 genes (41%) and showed 1.76× higher FBA flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31, while the model predicted 0% essentiality. This **supports and extends** evidence that growth-optimizing FBA can miss infrastructure-level dependencies: 10/13 Complex I operon subunits independently produced quinate-specific growth defects, and 30/51 network genes had no FBA reaction mappings. [src: aromatic_catabolism_network]

The network **supports** assignments of PQQ-dependent [[entities/quinate-degradation-pathway]] and Fe²⁺-dependent protocatechuate ring cleavage, while retaining the caveat that PQQ-biosynthesis genes also appear as glucose-specific in deletion phenotypes because of PQQ-dependent glucose dehydrogenase. [src: aromatic_catabolism_network]

## Respiratory-Chain Wiring

The respiratory-chain report **supports and refines** ADP1’s condition-specific essentiality profile. Quinate requires [[entities/complex-i]] but not cytochrome bo3, cytochrome bd, succinate dehydrogenase, or other listed components; acetate requires Complex I, cytochrome bo3, ACIAD3522, and additional components, with no listed component dispensable; lactate specifically requires cytochrome bo3 while Complex I is mildly important and cytochrome bd is dispensable; glucose has no specifically required respiratory component; and urea is generally demanding across the reported respiratory profile. [src: respiratory_chain_wiring]

ADP1 contains three parallel NADH dehydrogenases: 13-subunit proton-pumping Complex I, single-subunit non-proton-pumping [[entities/ndh-2]], and single-subunit ACIAD3522, an NADH-FMN oxidoreductase. Complex I pumps 4 H⁺/NADH. Complex I growth ratios were 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate; ACIAD3522 growth ratios were 1.39 on quinate, 1.39 on glucose, and 0.013 on acetate. [src: respiratory_chain_wiring] The ACIAD3522 result **refines** the existing Complex I and aromatic-network evidence by identifying a condition-specific acetate dependency, although ACIAD3522 may not be a respiratory NADH dehydrogenase in the strict sense and could have another metabolic function. [src: respiratory_chain_wiring]

NDH-2 is ACIAD_RS16420 with KO K03885. It is TnSeq-dispensable but absent from the deletion collection, is a standalone core-genome gene rather than part of a respiratory operon, and has no growth data. [src: respiratory_chain_wiring] FBA predicts zero NDH-2 flux on all standard carbon sources because the model routes NADH through Complex I. [src: respiratory_chain_wiring]

The quinate–Complex I relationship **refines** the condition-specific fitness interpretation. Quinate produces 4 total NADH, or 0.57 NADH per carbon, whereas glucose produces 9 and 1.50, acetate 3 and 1.50, and lactate 5 and 1.67, respectively. [src: respiratory_chain_wiring] The proposed explanation is that β-ketoadipate-pathway ring cleavage produces succinyl-CoA and acetyl-CoA simultaneously, creating a concentrated TCA-cycle NADH burst that may exceed NDH-2 reoxidation capacity, whereas glucose distributes NADH production across Entner–Doudoroff-pathway steps and the TCA cycle. This is a biochemical interpretation based on theoretical pathway stoichiometry, not measured flux distributions. [src: respiratory_chain_wiring]

Cross-species data **contradict** the predicted general NDH-2 compensation pattern: after filtering likely false positives, 5 of 14 organisms had validated NDH-2, and those organisms had mean Complex I aromatic deficit −0.297 versus −0.156 without validated NDH-2 (p = 0.52). The comparison had only 4 organisms lacking NDH-2 and is underpowered; the ADP1 wiring pattern may therefore be species-specific. [src: respiratory_chain_wiring]

Proteomics **supports** a passive, flux-based rather than transcriptional wiring model. Under standard growth conditions, Complex I, NDH-2, and ACIAD3522 had similar protein levels: 27.6 at the 66th percentile, 27.0 at the 59th percentile, and 26.2 at the 48th percentile, respectively, versus a genome median of 26.4; the spread was 1.4 units. [src: respiratory_chain_wiring]

The 62 respiratory-chain genes comprise Complex I with 13 genes, NDH-2 with 1 gene, NADH-flavin oxidoreductases with 5 genes, cytochrome bo3 with 4 genes, cytochrome bd with 5 genes, Complex II/succinate dehydrogenase with 5 genes, ATP synthase with 9 genes, and other respiratory components with 20 genes. [src: respiratory_chain_wiring] Of these, 36 have growth data and 26 do not, including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]

## Condition-Specific Fitness

Mutant growth fitness across 8 carbon sources had a mean pairwise correlation of 0.44. [src: acinetobacter_adp1_explorer] [[entities/urea]] fitness was nearly uncorrelated with [[entities/quinate]], at r = 0.11, and weakly correlated with all other conditions, at r = 0.12–0.28. [src: acinetobacter_adp1_explorer] Butanediol-acetate and butanediol-lactate showed the strongest correlations, at r = 0.58 and r = 0.53. [src: acinetobacter_adp1_explorer]

The deletion analysis **refines** these correlations by identifying demanding conditions—urea, acetate, and butanediol—with mean growth ratios of 0.41–0.65, moderate conditions—asparagine and lactate—with mean ratios of 0.80–0.82, and robust conditions—glucarate, glucose, and quinate—with mean ratios of 1.25–1.36. [src: adp1_deletion_phenotypes] PCA (principal component analysis, a method summarizing correlated variation into orthogonal components) found that 5 components captured 82% of growth-matrix variance; PC1 explained 36.7% and PC2 explained 12.7%, with urea loading +0.75 on PC2. [src: adp1_deletion_phenotypes]

The triple-essentiality analysis **supports** condition-specific fitness: across eight carbon sources, 333 of 478 genes (70%) showed condition-specific growth defects, 10 genes (2%) showed defects across all eight, and 135 genes (28%) showed no defect on any condition; mean pairwise defect correlation was 0.38, ranging from -0.03 to 1.0. [src: adp1_triple_essentiality]

Because ADP1 is absent from the Fitness Browser, its mutant growth fitness measurements for 8 carbon sources constitute a resource not otherwise available in BERDL. [src: acinetobacter_adp1_explorer] Condition-specific genes map to expected architecture, including the [[entities/urease-complex]] on urea, [[entities/quinate-degradation-pathway]] and [[entities/pqq-biosynthesis]] on quinate, the [[entities/glyoxylate-shunt]] on acetate, and the [[entities/entner-doudoroff-pathway]] on glucose. [src: adp1_deletion_phenotypes]

Cross-species ortholog data **refine** quinate specificity: Complex I orthologs had mean fitness values of -1.35 on aromatic conditions versus -0.77 on comparison conditions (Mann-Whitney p < 0.0001), but the largest defects occurred on acetate (-1.55) and succinate (-1.39), while Complex I was dispensable on glucose and lactate. This suggests the hypothesis that dependence tracks high NADH flux rather than aromatic chemistry alone; the comparison is not definitive for ADP1 because respiratory architectures differ among organisms. [src: aromatic_catabolism_network]

The new respiratory analysis **supports** this NADH-flux hypothesis within ADP1: Complex I was required on quinate despite lower total NADH yield, while glucose was redundant, and theoretical pathway organization suggested that flux rate and capacity—not total reducing-equivalent yield alone—select respiratory configuration. [src: respiratory_chain_wiring]

The new lignin-enrichment experiment **supports** ecological relevance of ADP1 as a lignin-selected taxon: *Acinetobacter* represented 25.2% of bacterial reads after one lignin-enrichment round and 41.7% when lignin was supplemented with labile carbon, compared with its base-community abundance of 25.2% as reported for the enriched comparison. [src: lignin_community_enrichment] This taxonomic association is consistent with condition-specific selection but does not directly measure ADP1 identity, strain-level abundance, or lignin-degradation genes. [src: lignin_community_enrichment]

## Deletion-Collection Coverage and Pangenome

Of 2,593 TnSeq-dispensable genes, 272, or 10.5%, lacked deletion-collection growth data. Missing genes were less conserved and less annotated than present dispensable genes: pangenome-core status was 76.5% versus 93.3%, with p = 1.4×10⁻²⁰; 25 were completely unannotated with q = 2.4×10⁻²⁵, and 48 were annotated as “hypothetical protein” with q = 3.0×10⁻⁴. [src: adp1_deletion_phenotypes]

This **supports and extends** the observation that essential genes are more likely to belong to the core pangenome, while showing that deletion-collection coverage is also biased toward conserved genes. The 313 uncertain-class genes had a mean length of 361 bp, 42% annotation coverage, and 31% pangenome-core status, consistent with gene fragments or pseudogenes rather than true essential genes. [src: adp1_deletion_phenotypes] Pangenome status did not explain FBA discordance: genes were 93–100% core across discordance classes, with enrichment OR = 0.89, p = 0.80. [src: adp1_triple_essentiality]

## Model Gaps and Multi-omic Evidence

Condition-specific FBA flux had weak, mixed correlations with measured growth: glucose ρ = -0.021 (p = 0.677; n = 387), acetate ρ = -0.153 (p = 0.004; n = 352), asparagine ρ = -0.257 (p < 0.001; n = 286), butanediol ρ = -0.145 (p = 0.092; n = 137), glucarate ρ = +0.246 (p = 0.005; n = 127), and lactate ρ = -0.160 (p = 0.065; n = 135). [src: adp1_triple_essentiality] The positive glucarate correlation is opposite the expected direction and **supports** the hypothesis that condition-specific model assumptions are inaccurate. [src: adp1_triple_essentiality]

The respiratory analysis **supports and specifies** this model-gap interpretation: FBA predicts zero flux through NDH-2 and ACIAD3522 on all standard media because growth optimization preferentially routes NADH through ATP-favorable Complex I, thereby missing alternative, suboptimal pathways and capacity constraints that can force their use. [src: respiratory_chain_wiring]

Aromatic degradation was strongly enriched among FBA-discordant genes: 9 of 11 genes were discordant, with OR = 9.70 and FDR-adjusted q = 0.012; directional enrichment for FBA under-prediction was OR = 12.0, q = 0.004. Lipid metabolism was depleted, with OR = 0.34 and q = 0.042; only 7 of 46 lipid-metabolism genes were discordant. [src: adp1_triple_essentiality] [[entities/beta-ketoadipate-pathway]] genes, including 4-carboxymuconolactone decarboxylase and beta-ketoadipate enol-lactone hydrolase, were predicted as blocked by FBA but associated with experimental growth defects; missing aromatic substrates or mismatched environmental assumptions are proposed explanations, not resolved mechanisms. [src: adp1_triple_essentiality]

The aromatic network **supports** this model-gap interpretation: 30/51 quinate-specific genes had no FBA reaction mappings, including cofactor-supply, iron-acquisition, regulatory, and Complex I-associated functions. Genomic independence of these subsystems—Complex I at 714–729 kb, pca/qui at 1,709–1,724 kb, PQQ biosynthesis at 2,461 kb, and iron-acquisition genes across 4 loci—contrasts with their metabolic coupling. [src: aromatic_catabolism_network]

Co-fitness assigns ACIAD3137 (UPF0234) and ACIAD2176 (DUF2280) to candidate Complex I accessory functions, with r > 0.98 correlations to Complex I genes; however, the analysis used only 8 conditions and 8-dimensional growth vectors, so these assignments may be indirect. [src: aromatic_catabolism_network]

Proteomics **supports** complementary evidence: across 7 *Acinetobacter* strains, essential genes (n = 464) among 2,288 genes had mean log2 expression = 28.43 ± 2.94 versus 25.73 ± 2.96 for dispensable genes (n = 1,824), a difference of 2.70 log2 units corresponding to 6.5-fold higher expression (Mann-Whitney U p = 9.91×10⁻⁵⁹). Expression correlated with knockout essentiality at Pearson r = 0.345 (p = 5.32×10⁻⁶⁵), Spearman ρ = 0.338 (p = 3.28×10⁻⁶²), and ROC AUC = 0.743. [src: adp1_triple_essentiality]

The paired 16S/ITS lignin experiment **extends** the multi-omic context to community composition: bacterial treatment separation had PERMANOVA R²=0.979, p=0.001, while fungal replicate variability was much greater and the planned Procrustes comparison was not completed. [src: lignin_community_enrichment] This supports ecological context for ADP1, not direct evidence for its metabolic function. [src: lignin_community_enrichment]

## Pangenome Cluster Bridge

ADP1 uses mmseqs2-style cluster IDs such as `NHSXFYEX_mmseqsCluster_NNNN`, whereas BERDL uses centroid gene IDs such as `NC_005966.1_1024`; the two naming systems have 0% direct string match. [src: acinetobacter_adp1_explorer] A bridge through BERDL’s `gene_genecluster_junction` table links BERDL cluster IDs to member gene IDs, which match the `feature_id` column in ADP1’s `pan_genome_features` table and expose the ADP1-style `cluster_id`. [src: acinetobacter_adp1_explorer]

All 4,891 BERDL clusters mapped successfully to 4,081 unique ADP1 clusters, yielding a 100% gene-level match across 43,754 genes. [src: acinetobacter_adp1_explorer] The generated `data/cluster_id_mapping.csv` enables BERDL pangenome annotations, including eggNOG and functional predictions, to be joined to ADP1 genes. [src: acinetobacter_adp1_explorer]

## Limitations

The database covers only *A. baylyi*, so cross-species comparisons require comparable databases for other organisms. [src: acinetobacter_adp1_explorer] No gene has measurements across all 6 modalities, and FBA flux data cover only 15% of genes; consequently, FBA–TnSeq concordance is limited to 866 genes. [src: acinetobacter_adp1_explorer]

The original triple-essentiality analysis is restricted to 478 TnSeq-dispensable genes, so its null result concerns growth variation among dispensable genes and is not a whole-genome test of FBA lethality prediction. [src: adp1_triple_essentiality] The pangenome cluster mapping is indirect and passes through 3 tables, so the reported 100% gene-level mapping could still have edge cases where clusters split or merge. [src: acinetobacter_adp1_explorer]

The 87% dependence of growth phenotype predictions on gapfilled reactions limits interpretation, and the 243 missing functions represent genomic-evidence gaps affecting prediction reliability. [src: acinetobacter_adp1_explorer] The deletion matrix excludes 499 essential genes plus 316 genes with incomplete data, its single-timepoint growth ratios may contain technical noise, and only 8 carbon sources were tested. [src: adp1_deletion_phenotypes]

Proteomics was averaged across 7 *Acinetobacter* strains rather than measured in the exact knockout assay condition, so it is independent supporting evidence rather than a condition-matched causal test. [src: adp1_triple_essentiality] Proposed mechanisms for TnSeq/knockout discordance and aromatic-pathway FBA discordance remain hypotheses requiring condition-matched experiments, insertion-position and domain analyses, measured media composition, revised FBA constraints, and combined FBA-plus-fitness-plus-proteomics prediction. [src: adp1_triple_essentiality]

The 8-condition co-fitness matrix provides approximately 5 independent dimensions; cross-species ortholog data are confounded by organism-specific respiratory architectures, and non-core Complex I assignments rely on correlation rather than direct physical evidence. [src: aromatic_catabolism_network]

The respiratory conclusions have additional limitations: NDH-2 has no growth data; its proposed glucose compensation is untested; theoretical stoichiometry does not measure flux distributions; the cross-species comparison included only 4 organisms lacking NDH-2; annotation variation may cause missed orthologs; text matching generated false-positive NDH-2 calls; the planned pangenome KO co-occurrence analysis was not performed; and ACIAD3522 may have another metabolic function. [src: respiratory_chain_wiring] The wiring model can be tested with an NDH-2 deletion mutant, NADH/NAD⁺ measurements on each carbon source, expanded K03885 and K00330–K00343 searches across 27K species, ACIAD3522 characterization, and quinate-versus-succinate respiratory-chain proteomics. [src: respiratory_chain_wiring]

The lignin-enrichment taxon was measured by 16S amplicon sequencing rather than strain-resolved genomics; functional interpretation was taxonomic, no gene-level lignin-pathway enrichment was directly measured, and n=3 per group with significant PERMDISP means community-level PERMANOVA reflects both group location and dispersion. [src: lignin_community_enrichment]

## Related Pages

This organism is the subject of [[summaries/acinetobacter_adp1_explorer__REPORT]], [[summaries/adp1_deletion_phenotypes__REPORT]], [[summaries/adp1_triple_essentiality__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], [[summaries/lignin_community_enrichment__REPORT]], and [[summaries/respiratory_chain_wiring__REPORT]]. [src: acinetobacter_adp1_explorer] [src: lignin_community_enrichment] [src: respiratory_chain_wiring]

Its findings contribute to [[concepts/multi-omics-integration]], [[concepts/gene-essentiality]], [[concepts/condition-specific-fitness]], [[concepts/pangenome-integration]], [[concepts/metabolic-model-gapfilling]], [[concepts/cofitness-network-architecture]], and [[concepts/ecological-memory]]. [src: acinetobacter_adp1_explorer] [src: lignin_community_enrichment]
