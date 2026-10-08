---
type: "Summary"
description: "Summary of the annotation_gap_discovery project, which triangulated gapfilling, Fitness Browser fitness, pangenome, GapMind and BLAST evidence to assign candidate genes to gapfilled metabolic reactions across 14 bacteria."
doc_type: "short"
full_text: "sources/annotation_gap_discovery__REPORT.md"
---
# Annotation-Gap Discovery via Phenotype-Fitness-Pangenome-Gapfilling Integration

## Overview

This study integrated metabolic-model gapfilling, Fitness Browser phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology to identify genes underlying gapfilled reactions across 14 organisms and 18 carbon sources. Draft models were evaluated with flux-balance analysis (FBA), a constraint-based method for predicting metabolic flux and growth, and the resulting evidence was combined into confidence-scored candidate gene assignments. [src: annotation_gap_discovery]

## Key Findings

### 1. Evidence triangulation resolved 47.8% of annotation gaps

Among 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources, 96 (47.8%) received candidate genes with confidence scoring, exceeding the pre-specified H1 threshold of 30%. The assignments comprised 44 high-confidence pairs (21.9%), supported by BLAST homology, fitness evidence, and pangenome conservation; 19 medium-confidence pairs (9.5%), supported by BLAST homology with partial additional evidence; and 33 low-confidence pairs (16.4%), supported by a single evidence stream. A total of 105 pairs (52.2%) remained unresolved. [src: annotation_gap_discovery]

### 2. No single evidence stream exceeded 35% resolution

Leave-one-out cross-validation gave 96 resolved pairs (47.8%) for the full pipeline, 86 (42.8%) without NB03 EC matching, 80 (39.8%) without NB04 Bakta annotations, and 73 (36.3%) without NB06 BLAST. Individual streams resolved 51 pairs (25.4%) for NB03 alone, 22 (10.9%) for NB04 alone, and 70 (34.8%) for BLAST alone. BLAST homology was therefore the strongest single stream, while the full pipeline added 13 percentage points over BLAST alone. The report also notes that removing any single tested stream still kept resolution above 36%, which it presents as evidence of robustness. [src: annotation_gap_discovery]

### 3. Resolution varied 3.5-fold across organisms

Resolution rates ranged from 20% in *Bacteroides thetaiotaomicron* to 71% in *Klebsiella michiganensis*. The reported organism-level results were *K. michiganensis* (Koxy), 7 total gaps and 5 resolved (71.4%); *Marinobacter* (Marino), 12 and 8 (66.7%); *Azospirillum brasilense* (azobra), 21 and 13 (61.9%); *Herbaspirillum seropedicae* (HerbieS), 17 and 10 (58.8%); *E. coli* Keio (Keio), 7 and 4 (57.1%); and *B. thetaiotaomicron* (Btheta), 15 and 3 (20.0%). The report observes that organisms with better-annotated reference genomes and stronger Fitness Browser coverage showed higher resolution, and that the Bacteroidetes organism's lower resolution was consistent with greater phylogenetic and metabolic divergence from the proteobacterial majority. These links to reference annotation, coverage and phylogenetic distance are the report's interpretations, not controlled tests. [src: annotation_gap_discovery]

### 4. Two reactions dominated high-confidence assignments

Reaction rxn02185, 2-acetolactate pyruvate-lyase (EC 2.2.1.6), and reaction rxn03436, acetohydroxy acid isomeroreductase (EC 1.1.1.86), were each resolved with high confidence in 9 of 14 organisms. These reactions catalyze sequential steps in branched-chain amino acid biosynthesis, and their co-resolution is consistent with the report's inference that identifying one pathway gene often enables recovery of the adjacent step's gene. This co-resolution shows computational consistency, not independent experimental validation. [src: annotation_gap_discovery]

### 5. Dark reactions resisted resolution

Of 201 gapfilled reactions, 50 (24.9%) lacked an EC number in ModelSEED and were designated “dark reactions.” Only 8 of these 50 (16%) were resolved, compared with 88 of 151 (58.3%) reactions with known EC numbers. Because dark-reaction functions were represented by stoichiometry rather than enzyme classification, sequence homology and functional-annotation cross-referencing were more difficult. [src: annotation_gap_discovery]

### 6. GapMind and gapfilling showed partial concordance

Among 104 GapMind-gapfill pathway pairings, GapMind identified pathways as incomplete (`not_present` or `steps_missing`) for many of the same carbon sources where ModelSEED required gapfilling; the report does not quantify how many. Exact concordance was limited because GapMind reports pathway-level step counts rather than individual step identities in the available KBase Data Lakehouse data. [src: annotation_gap_discovery]

### 7. Resolved BLAST cases clustered at high identity

The study identified 154 BLAST hits using DIAMOND v2.1.16 blastp with `--evalue 1e-5 --max-target-seqs 20 --id 25 --query-cover 50 --outfmt 6` against Swiss-Prot exemplar sequences. The exemplar set contained 328 reviewed bacterial sequences for 75/84 unique ECs retrieved through the UniProt REST API. High-confidence thresholds were at least 30% identity, at least 70% coverage, and e-value at most 1e-10; medium-confidence thresholds were at least 25% identity, at least 50% coverage, and e-value at most 1e-5. The reactions with the most BLAST hits were rxn02185, rxn03436, and rxn15947, which encode well-characterized enzymes with broad phylogenetic distribution. Hits meeting the high-confidence thresholds were concentrated in branched-chain amino acid biosynthesis and polyamine metabolism reactions. [src: annotation_gap_discovery]

## Study Design and Evidence Pipeline

Fourteen Fitness Browser organisms with rich carbon-source random-barcode transposon sequencing (RB-TnSeq), a method that measures genome-wide mutant fitness using barcoded transposon libraries, were selected. Draft models were built from ModelSEED/RAST annotations and COBRApy. Across 574 organism-carbon source combinations, baseline FBA achieved 42.5% overall accuracy, with recall of 86.5% (244 of 282 growth-positive conditions correctly predicted) and precision of 42.5% (244 of 574 growth predictions correct); the models produced 330 false positives. Conditional gapfilling for 38 false-negative cases added 219 reactions: 201 enzymatic, 14 transport, and 12 exchange, averaging 5.8 reactions per case. [src: annotation_gap_discovery]

NB03 matched gapfilled reaction EC numbers to Fitness Browser gene annotations through pangenome gene clusters and resolved 51/201 pairs (25.4%) with 107 gene candidates. NB04 queried Bakta annotations for alternative EC numbers and product-name matches, added 22 newly resolved pairs (10.9%), and produced 1,459 Bakta EC candidate entries. NB05 constructed a 57-EC by 14-organism presence/absence matrix, calculated fitness-specificity z-scores, identified 11 strong co-occurrence cases, and found four carbon-source-specific fitness defects. NB06 downloaded 328 Swiss-Prot exemplar sequences for 75/84 unique ECs, identified 154 DIAMOND hits, and produced the final 96 resolved pairs through evidence triangulation. [src: annotation_gap_discovery]

For validation, 23 gene-protein-reaction (GPR) rules—formal links between genes and reactions—were inserted into SBML models for high- and medium-confidence NB03 candidates. Gene-knockout simulations produced zero wildtype growth on minimal carbon-source media, an expected limitation because the models required the gapfilled reactions themselves to grow on those carbon sources. [src: annotation_gap_discovery]

## Interpretation and Contribution

The study supports H1: integrating gapfilling, fitness, pangenome, GapMind, and BLAST evidence resolved 47.8% of gapfilled reaction-organism pairs, while the 21.9% high-confidence proportion was within the expected 15-25% range. The result indicates that annotation gaps are not uniformly intractable and that existing data sources can resolve a substantial fraction of them. [src: annotation_gap_discovery]

The work extends fitness-guided annotation by combining fitness evidence with gapfilling predictions, pangenome conservation, and sequence homology. Its stated contributions are cross-organism triangulation across 14 focal species, tiered confidence scoring for experimental prioritization, identification of 50 EC-less dark reactions and 105 unresolved pairs, and leave-one-out quantification showing that no single evidence type is sufficient. [src: annotation_gap_discovery]

The generated evidence included 109 carbon-source-to-ModelSEED-compound mappings, 574 baseline FBA results, 574 gapfilling results, 219 gapfilled reaction details, 107 NB03 candidates, 104 GapMind concordance records, 1,459 Bakta alternatives, 54,549 UniRef IDs extracted from Bakta target clusters, 57 presence/absence records, 71 expanded fitness profiles, 201 co-occurrence candidates, 154 BLAST hits, 201 master reaction-gene candidate records, 7 cross-validation configurations, 10 delta metrics, 23 knockout-validation results, and 23 GPR insertions. [src: annotation_gap_discovery]

## Caveats

The draft models were based on automated RAST annotations and contained systematic errors; the 42.5% baseline FBA accuracy, dominated by false positives, reflected overly permissive models that predicted growth on carbon sources the organisms could not use. [src: annotation_gap_discovery]

Gapfilling is non-unique: multiple valid solutions may exist for each false-negative case. The study used default ModelSEED gapfilling, which minimizes the number of added reactions but does not guarantee biological optimality. [src: annotation_gap_discovery]

The mapping between Fitness Browser experiment names and ModelSEED exchange reactions required manual curation of 109 carbon sources to compound IDs, so mapping errors could generate spurious false negatives. [src: annotation_gap_discovery]

Fitness significance depends on the selected absolute-fitness threshold and the number of experiments; organisms with fewer carbon-source experiments have less statistical power. [src: annotation_gap_discovery]

GapMind covers ~80 carbon and amino acid pathways rather than full metabolism, so many gapfilled reactions fall outside its coverage. [src: annotation_gap_discovery]

The FBA knockout validation was inconclusive because the models could not grow on carbon-source minimal media without the gapfilled reactions; consequently, the reactions being tested were themselves required for growth, making single-gene knockout analysis circular in this setting. [src: annotation_gap_discovery]

The dataset was phylogenetically biased: 12 of 14 organisms were Proteobacteria. The sole Bacteroidetes organism, *B. thetaiotaomicron*, had the lowest resolution rate, suggesting that the approach may be less effective for phylogenetically distant clades with divergent metabolism. Because this rests on a single organism, it should be read as a hypothesis rather than an established finding. [src: annotation_gap_discovery]

The report labels baseline FBA across 574 combinations as 42.5% overall accuracy. It also gives precision as 42.5% (244 of 574 growth predictions correct), along with recall of 86.5% (244 of 282) and 330 false positives. The report gives the same value for accuracy and precision, so the two should not be treated as independently verified metrics. [src: annotation_gap_discovery]

The report states that conditional gapfilling of 38 false-negative cases added 219 reactions, averaging 5.8 reactions per case. However, its listed categories (201 enzymatic, 14 transport, 12 exchange) do not add up to the stated 219 total, and the report does not resolve this inconsistency. [src: annotation_gap_discovery]

The report is internally inconsistent about BLAST search direction. Its Key Findings describe DIAMOND v2.1.16 blastp searches against the Swiss-Prot exemplar sequences (328 reviewed bacterial sequences for 75/84 unique ECs). The NB06 pipeline description instead says DIAMOND BLAST was run against concatenated proteomes using the 328 downloaded exemplars. Both descriptions report 154 hits, and the report does not reconcile them. [src: annotation_gap_discovery]

## Future Directions

The report proposes several follow-up directions, none of which is a reported result. It describes the 44 high-confidence gene-reaction assignments as directly testable through targeted gene knockouts (e.g., CRISPRi) on specific carbon sources, with rxn02185 and rxn03436 across 9 organisms as priority targets; this is proposed validation, not a knockout result. It expects that extending the pipeline to all 48 Fitness Browser organisms would increase statistical power for pangenome co-occurrence analysis and might resolve additional gaps through phylogenetic proximity, which is anticipated rather than demonstrated. It suggests that using gapseq (Zimmermann et al. 2021) instead of RAST/ModelSEED for initial model reconstruction could reduce false-positive FBA predictions and yield a more targeted set of gapfill cases; this improvement is hypothetical. It names the 50 EC-less gapfilled reactions as high-priority targets for computational enzyme-prediction tools such as DeepEC and CLEAN and for experimental biochemistry, so their enzyme assignments remain to be characterized. It suggests that extending the approach to microbial communities could identify cross-feeding metabolic interactions mediated by annotation-gap reactions, which is a possible application only. It also proposes applying ICA-based approaches (Borchert et al. 2024), meaning independent component analysis, to the fitness data to identify functional gene modules that resolve gaps missed by per-gene analysis; this outcome is not established here. [src: annotation_gap_discovery]

## Literature Context and Data Sources

The project's literature context cites Price et al. (2022, *PLoS Genetics*), who used mutant fitness data to fill gaps in bacterial catabolic pathways and annotated 716 proteins across diverse bacteria. It also cites Benedict et al. (2014, *PLoS Comput Biol*), who developed likelihood-based gene annotations for gap filling using sequence homology and showed that probabilistic approaches improve metabolic model quality. These are results from earlier work, not findings of this project. [src: annotation_gap_discovery]

The report names gapseq (Zimmermann et al. 2021, *Genome Biology*) as the closest methodological comparator, since it uses curated pathway databases and informed gap-filling to build metabolic models. The report sets gapseq apart because it focuses on model reconstruction rather than post-hoc resolution of annotation gaps and does not integrate transposon fitness data. [src: annotation_gap_discovery]

Citing PubMed, the report states that Borchert et al. (2024, *mSystems*) applied independent component analysis to random-barcode transposon sequencing (RB-TnSeq) fitness data from *Pseudomonas putida* and identified 84 functional gene modules. It also states that Wetmore et al. (2015, *mBio*) established RB-TnSeq with 387 genome-wide fitness assays across 5 bacteria, identifying 5,196 genes with significant phenotypes. These figures come from earlier work. The report states that the Fitness Browser database that grew from this work covered 48 organisms at the time of the study. [src: annotation_gap_discovery]

The `kescience_fitnessbrowser` collection (tables `organism`, `experiment`, `genefitness`, `gene`) supplied carbon-source experiments, gene fitness scores and gene annotations. The `kbase_ke_pangenome` collection (tables `genome`, `gene_cluster`, `gene_genecluster_junction`, `eggnog_mapper_annotations`, `bakta_annotations`, `gapmind_pathways`) supplied pangenome gene clusters, EC/KEGG annotations and pathway-completeness data. The `kbase_msd_biochemistry` collection (tables `reaction`, `reagent`) supplied reaction definitions and stoichiometry for the gapfilled reactions. [src: annotation_gap_discovery]

## Figures

The report's main figures are `fig1_resolution_overview.png` (cumulative resolution by evidence stream plus a confidence pie chart), `fig2_cross_validation.png` (leave-one-out cross-validation and single-stream resolution bars), `fig3_organism_resolution.png` (per-organism stacked bar chart of confidence levels), `fig4_blast_quality.png` (BLAST hit percent identity versus coverage scatter plus top reactions), `fig5_gapmind_concordance.png` (GapMind score-category distribution plus gapfill concordance), and `fig6_conservation.png` (EC-group conservation histogram across 14 organisms). [src: annotation_gap_discovery]

The supplemental notebook figures are `nb04_candidate_sources.png` (evidence-source breakdown from NB04), `gapmind_score_categories.png` (GapMind score categories from NB04), `nb05_fitness_specificity.png` (fitness-specificity z-scores from NB05), `nb06_triangulated_evidence.png` (triangulated evidence summary from NB06), `annotation_gap_resolution_heatmap.png` (annotation-gap resolution heatmap from NB03), and `evidence_distribution.png` (evidence-stream distribution from NB03). [src: annotation_gap_discovery]

## Slots Into

- [[concepts/metabolic-model-gapfilling]] — Adds a cross-organism evidence-triangulation framework showing that 96 of 201 gapfilled enzymatic reaction-organism pairs (47.8%) can receive candidate genes, while documenting gapfilling non-uniqueness and model-quality limitations. [src: annotation_gap_discovery]
- [[concepts/condition-specific-fitness]] — Connects RB-TnSeq carbon-source fitness, four carbon-source-specific fitness defects, and fitness-specificity z-scores to metabolic annotation-gap resolution. [src: annotation_gap_discovery]
- [[concepts/pangenome-integration]] — Demonstrates transfer and validation of annotation evidence through a 57-EC by 14-organism presence/absence matrix and pangenome conservation. [src: annotation_gap_discovery]
- [[concepts/gene-essentiality]] — Provides gene-candidate prioritization and reports the circular limitation of single-gene knockout simulations in models dependent on the gapfilled reactions. [src: annotation_gap_discovery]
- [[concepts/multi-omics-integration]] — Extends annotation inference by combining sequence homology, gene annotations, pangenome conservation, fitness measurements, pathway completeness, and metabolic-model evidence. [src: annotation_gap_discovery]
- [[concepts/evidence-triangulation-for-functional-annotation]] — Tiered confidence assignments (44 high, 19 medium, 33 low, 105 unresolved of 201 pairs) and per-stream contributions show that combined evidence resolves more pairs than any single stream. [src: annotation_gap_discovery]
- [[concepts/ec-less-reaction-annotation]] — EC-less dark reactions resolved at 8 of 50 (16%) versus 88 of 151 (58.3%) for reactions with known EC numbers. [src: annotation_gap_discovery]
- [[concepts/pathway-versus-reaction-evidence-resolution]] — GapMind's pathway-level step counts limited reaction-level concordance, and the co-resolution of sequential steps rxn02185 and rxn03436 illustrates inference from pathway context. [src: annotation_gap_discovery]
- [[concepts/computational-pathway-prediction-validation]] — Partial GapMind-gapfill concordance across 104 pathway pairings and GapMind's ~80-pathway scope. [src: annotation_gap_discovery]
- [[concepts/circularity-in-metabolic-model-validation]] — Single-gene knockout simulations after 23 GPR insertions were inconclusive because the gapfilled reactions were themselves required for growth. [src: annotation_gap_discovery]
- [[concepts/genomic-under-representation]] — The proteobacterial bias (12 of 14 organisms) and the low 20.0% resolution in the sole Bacteroidetes organism, which is single-organism evidence for weaker transfer to distant clades. [src: annotation_gap_discovery]
- [[concepts/cross-condition-metabolic-comparability]] — Manual mapping of 109 carbon sources to ModelSEED compound IDs as an error source for spurious false negatives. [src: annotation_gap_discovery]
- [[concepts/fitness-condition-coverage-prioritization-bias]] — Fitness support depends on the absolute-fitness threshold and experiment count, so sparsely assayed organisms have less statistical power. [src: annotation_gap_discovery]
- [[concepts/experimental-prioritization-of-functional-dark-matter]] — The 44 high-confidence gene-reaction assignments are proposed for targeted knockout (e.g., CRISPRi) validation, with rxn02185 and rxn03436 across 9 organisms as priority targets. This is proposed and not yet validated. [src: annotation_gap_discovery]
- [[concepts/community-metabolic-interdependence]] — The report proposes extending the approach to microbial communities to find cross-feeding interactions mediated by annotation-gap reactions. This is a possible application, not a reported finding. [src: annotation_gap_discovery]
- [[concepts/fitness-module-detection-sensitivity]] — The report proposes ICA-based analysis (Borchert et al. 2024) of fitness data to find functional gene modules that per-gene analysis misses. This outcome is not established. [src: annotation_gap_discovery]
