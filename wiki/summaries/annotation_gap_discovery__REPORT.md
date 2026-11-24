---
type: "Summary"
description: "Summary of the project Annotation-Gap Discovery via Phenotype-Fitness-Pangenome-Gapfilling Integration."
doc_type: "short"
full_text: "sources/annotation_gap_discovery__REPORT.md"
---
# Annotation-Gap Discovery via Phenotype-Fitness-Pangenome-Gapfilling Integration

This report asked whether combining several evidence types can assign genes to metabolic annotation gaps found by gapfilling. It reports that candidate genes were assigned to 96 (47.8%) of 201 gapfilled enzymatic reaction-organism pairs across 14 [[entities/fitness-browser]] organisms and 18 carbon sources. [src: annotation_gap_discovery] The evidence is computational. Knockout validation could not test the assignments (see the caveats). [src: annotation_gap_discovery] The report claims this is the first systematic integration of five evidence types (gapfilling, fitness, pangenome, GapMind and BLAST) to resolve metabolic annotation gaps across multiple organisms at once. [src: annotation_gap_discovery]

## Key Findings

### Overall resolution and hypothesis H1

The triangulation approach resolved 47.8% of pairs. The report says this exceeds the pre-specified H1 threshold of 30% and supports H1. [src: annotation_gap_discovery] See [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps]]. The confidence breakdown is below. High-confidence assignments (21.9%) closely match the 15-25% range expected in the research plan. [src: annotation_gap_discovery]

| Confidence | Pairs | Evidence |
|---|---|---|
| High | 44 (21.9%) | BLAST homology + fitness evidence + pangenome conservation [src: annotation_gap_discovery] |
| Medium | 19 (9.5%) | BLAST homology with partial supporting evidence [src: annotation_gap_discovery] |
| Low | 33 (16.4%) | single evidence stream only [src: annotation_gap_discovery] |
| Unresolved | 105 (52.2%) | no convincing gene candidate [src: annotation_gap_discovery] |

The report lists four contributions of the framework. Pangenome evidence is transferred across the 14 focal species rather than resolving gaps organism by organism. [src: annotation_gap_discovery] The high/medium/low tiers give actionable prioritization for experimental follow-up. [src: annotation_gap_discovery] The 50 EC-less gapfilled reactions and 105 unresolved pairs are high-value targets for experimental enzyme characterization. [src: annotation_gap_discovery] The leave-one-out analysis quantifies each stream's unique contribution and shows that no single data type is sufficient. [src: annotation_gap_discovery]

### Contribution of each evidence stream

Leave-one-out and single-stream runs show that BLAST homology matters most. Removing any one stream still left resolution above 36%, which the report reads as robustness. [src: annotation_gap_discovery] The full pipeline added 13 percentage points over BLAST alone. [src: annotation_gap_discovery]

| Configuration | Pairs resolved |
|---|---|
| Full pipeline | 96 (47.8%) [src: annotation_gap_discovery] |
| Without NB03 (EC match) | 86 (42.8%) [src: annotation_gap_discovery] |
| Without NB04 (Bakta) | 80 (39.8%) [src: annotation_gap_discovery] |
| Without NB06 (BLAST) | 73 (36.3%) [src: annotation_gap_discovery] |
| NB03 alone | 51 (25.4%) [src: annotation_gap_discovery] |
| NB04 alone | 22 (10.9%) [src: annotation_gap_discovery] |
| BLAST alone | 70 (34.8%) [src: annotation_gap_discovery] |

### Variation among organisms

Resolution ranged from 20% in *Bacteroides thetaiotaomicron* to 71% in *Klebsiella michiganensis*. [src: annotation_gap_discovery] Organisms with better-annotated reference genomes and stronger Fitness Browser coverage showed higher resolution. [src: annotation_gap_discovery] The report links the lowest rate to the divergent Bacteroidetes metabolism of *B. thetaiotaomicron* and its phylogenetic distance from the proteobacterial majority. [src: annotation_gap_discovery] It states that the sole Bacteroidetes had the lowest resolution rate, suggesting the approach may be less effective for phylogenetically distant clades with divergent metabolism. [src: annotation_gap_discovery] This is an interpretation, not a tested result. See [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]].

| Organism | Gaps | Resolved |
|---|---|---|
| *K. michiganensis* (Koxy) | 7 | 5 (71.4%) [src: annotation_gap_discovery] |
| *Marinobacter* (Marino) | 12 | 8 (66.7%) [src: annotation_gap_discovery] |
| *Azospirillum brasilense* (azobra) | 21 | 13 (61.9%) [src: annotation_gap_discovery] |
| *Herbaspirillum seropedicae* (HerbieS) | 17 | 10 (58.8%) [src: annotation_gap_discovery] |
| *E. coli* Keio (Keio) | 7 | 4 (57.1%) [src: annotation_gap_discovery] |
| *B. thetaiotaomicron* (Btheta) | 15 | 3 (20.0%) [src: annotation_gap_discovery] |

### Pathways resolved consistently

Reactions rxn02185 (2-acetolactate pyruvate-lyase, EC 2.2.1.6, branched-chain amino acid biosynthesis) and rxn03436 (acetohydroxy acid isomeroreductase, EC 1.1.1.86, valine/isoleucine biosynthesis) were each resolved with high confidence in 9 of 14 organisms. [src: annotation_gap_discovery] The report reads this co-resolution of sequential steps as validating triangulation: when one pathway gene is found, the adjacent step's gene is typically recoverable. [src: annotation_gap_discovery] The report names these two reactions as priority targets across 9 organisms for experimental validation. [src: annotation_gap_discovery]

### Dark reactions

Of 201 gapfilled reactions, 50 (24.9%) had no ModelSEED EC number and were called dark reactions. [src: annotation_gap_discovery] Only 8 of these 50 (16%) were resolved, against 88 of 151 (58.3%) reactions with known EC numbers. [src: annotation_gap_discovery] Dark reactions are known only by stoichiometry, so homology searches and annotation cross-referencing are much harder. [src: annotation_gap_discovery]

### GapMind comparison

GapMind pathway predictions partially corroborated gapfilling across 104 GapMind-gapfill pathway pairings. [src: annotation_gap_discovery] GapMind called pathways incomplete (not_present or steps_missing) for many of the same carbon sources where ModelSEED needed gapfilling. [src: annotation_gap_discovery] Exact concordance was limited because the available data give step counts, not individual step identities. [src: annotation_gap_discovery] See [[entities/gapmind]].

### Evidence-stream details

- BLAST: DIAMOND v2.1.16 blastp gave 154 hits against Swiss-Prot exemplars (--evalue 1e-5 --max-target-seqs 20 --id 25 --query-cover 50 --outfmt 6). [src: annotation_gap_discovery] The exemplars were 328 reviewed bacterial sequences for 75/84 unique ECs, retrieved from the UniProt REST (representational state transfer) API (application programming interface). [src: annotation_gap_discovery] Separately, the triangulation pipeline description states that DIAMOND BLAST was run against concatenated proteomes. [src: annotation_gap_discovery] The report's wording does not reconcile these two target descriptions here.
- BLAST thresholds: medium confidence was >=25% identity, >=50% coverage and e-value <=1e-5. [src: annotation_gap_discovery] High-confidence hits (>=30% identity, >=70% coverage, e-value <=1e-10) were concentrated in branched-chain amino acid biosynthesis and polyamine metabolism. [src: annotation_gap_discovery]
- The top reactions by hit count (rxn02185, rxn03436, rxn15947) encode well-characterized enzymes with broad phylogenetic distribution. [src: annotation_gap_discovery]
- EC matching (NB03) matched gapfilled reaction EC numbers to Fitness Browser gene annotations via pangenome gene clusters. [src: annotation_gap_discovery] It resolved 51/201 pairs (25.4%) with 107 gene candidates. [src: annotation_gap_discovery]
- Bakta (NB04) queried alternative EC numbers and product-name matches for dark reactions. [src: annotation_gap_discovery] It added 22 newly resolved pairs (10.9%) and 1,459 Bakta EC candidate entries. [src: annotation_gap_discovery]
- Pangenome fitness profiling built a 57 EC x 14 organism presence/absence matrix and computed fitness specificity z-scores. [src: annotation_gap_discovery] It found 11 strong co-occurrence cases [src: annotation_gap_discovery] and four carbon-source-specific fitness defects. [src: annotation_gap_discovery]

### Relation to earlier work

The report's confidence scoring weights multiple evidence types and adds fitness and pangenome evidence absent from Benedict et al.'s framework. [src: annotation_gap_discovery] It names gapseq as its closest methodological comparator, because gapseq uses curated pathway databases and informed gap-filling to build metabolic models. [src: annotation_gap_discovery] gapseq focuses on model reconstruction rather than post-hoc annotation-gap resolution, and it does not integrate transposon fitness data. [src: annotation_gap_discovery] The report proposes its pipeline as complementary: gapseq could improve initial models, and triangulation would resolve the remaining gaps. [src: annotation_gap_discovery]

According to the report's PubMed account, Borchert et al. (2024, mSystems) applied independent component analysis to *Pseudomonas putida* RB-TnSeq fitness data and identified 84 functional gene modules. [src: annotation_gap_discovery] The report says this approach and its own per-gene, per-condition analysis both show functional information in RB-TnSeq beyond simple gene essentiality calls. [src: annotation_gap_discovery] According to the report's PubMed account, Wetmore et al. (2015, mBio) established RB-TnSeq, performed 387 genome-wide fitness assays across 5 bacteria and identified 5,196 genes with significant phenotypes. [src: annotation_gap_discovery] The Fitness Browser database grew from that work and now covers 48 organisms. [src: annotation_gap_discovery]

## Data and Methods

Fourteen Fitness Browser organisms with rich carbon-source RB-TnSeq (random barcode transposon sequencing) coverage were selected. [src: annotation_gap_discovery] Draft models were built with ModelSEED/RAST annotations and COBRApy. [src: annotation_gap_discovery] Baseline FBA (flux balance analysis) over 574 organism-carbon source combinations gave 42.5% overall accuracy. [src: annotation_gap_discovery] Recall was 86.5% (244 of 282 growth-positive conditions correctly predicted). [src: annotation_gap_discovery] Precision was only 42.5% (244 of 574 growth predictions correct), with 330 false positives attributed to overly permissive draft models. [src: annotation_gap_discovery] Conditional gapfilling on 38 false-negative cases (observed growth, predicted no growth) added 219 reactions (201 enzymatic, 14 transport, 12 exchange), averaging 5.8 per case. [src: annotation_gap_discovery] See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

The report uses the KBase Data Lakehouse collection kescience_fitnessbrowser (tables organism, experiment, genefitness, gene) for carbon source experiments, gene fitness scores and gene annotations. [src: annotation_gap_discovery] It uses kbase_ke_pangenome (tables genome, gene_cluster, gene_genecluster_junction, eggnog_mapper_annotations, bakta_annotations, gapmind_pathways) for gene clusters, EC/KEGG annotations and pathway completeness. [src: annotation_gap_discovery] It uses kbase_msd_biochemistry (tables reaction, reagent) for gapfilled reaction definitions and stoichiometry. [src: annotation_gap_discovery]

The report places its work against two earlier studies. Price et al. (2022, PLoS Genetics) used mutant fitness data to fill gaps in bacterial catabolic pathways, annotating 716 proteins. [src: annotation_gap_discovery] This study extends that work by integrating fitness with gapfilling predictions, pangenome conservation and sequence homology, rather than relying mainly on fitness. [src: annotation_gap_discovery] Benedict et al. (2014, PLoS Comput Biol) developed likelihood-based gene annotations for gap filling using sequence homology. They showed that probabilistic approaches improve metabolic model quality. [src: annotation_gap_discovery]

## Caveats and Open Work

- Validation inserted 23 gene-protein-reaction rules into SBML models for high/medium-confidence EC-matching candidates. [src: annotation_gap_discovery] Gene knockout simulation then showed zero wildtype growth on minimal carbon source media. [src: annotation_gap_discovery] The report calls this an expected limitation, because the models need the gapfilled reactions themselves for growth on those carbon sources. [src: annotation_gap_discovery] The knockout validation was inconclusive, because single-gene knockout analysis is circular in this context. [src: annotation_gap_discovery]
- Draft models from automated RAST annotations contain systematic errors. The 42.5% baseline FBA accuracy is dominated by false positives from overly permissive growth predictions. [src: annotation_gap_discovery]
- Multiple valid gapfill solutions may exist for each false-negative case. The default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery]
- The report manually mapped 109 Fitness Browser carbon source condition names to ModelSEED compound IDs (identifiers). Mapping errors would produce spurious false negatives. [src: annotation_gap_discovery]
- Gene fitness significance depends on the |fitness| threshold and experiment count. Organisms with fewer carbon source experiments have less statistical power. [src: annotation_gap_discovery]
- GapMind covers ~80 carbon and amino acid pathways rather than full metabolism, so many gapfilled reactions fall outside its coverage. [src: annotation_gap_discovery]
- Twelve of 14 organisms are Proteobacteria, which limits generalizability. [src: annotation_gap_discovery]
- Dark reactions were resolved far less often, so the hardest gaps remain largely open. [src: annotation_gap_discovery]
- Exact GapMind concordance could not be assessed at step level. [src: annotation_gap_discovery]
- 105 pairs (52.2%) remain unresolved. [src: annotation_gap_discovery]

The report proposes these next steps:
- Test the 44 high-confidence gene-reaction assignments by targeted gene knockouts, such as CRISPR interference (CRISPRi), on specific carbon sources. [src: annotation_gap_discovery]
- Extend the pipeline to all 48 Fitness Browser organisms. This would increase statistical power for pangenome co-occurrence analysis and may resolve more gaps through phylogenetic proximity. [src: annotation_gap_discovery]
- Use gapseq instead of RAST/ModelSEED for initial reconstruction. This could reduce false-positive FBA predictions and yield more targeted gapfill cases. [src: annotation_gap_discovery]
- Target the 50 EC-less gapfilled reactions with computational enzyme prediction tools (e.g., DeepEC, CLEAN) and experimental biochemistry. [src: annotation_gap_discovery]
- Extend the approach to microbial communities to identify cross-feeding interactions mediated by annotation-gap reactions. [src: annotation_gap_discovery]
- Apply ICA-based approaches (Borchert et al. 2024) to the fitness data to find functional gene modules that resolve gaps missed by per-gene analysis. [src: annotation_gap_discovery]

## Slots Into

- [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps]]: 47.8% of pairs resolved, above the 30% H1 threshold, with BLAST the strongest single stream. [src: annotation_gap_discovery]
- [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]]: resolution was lowest in *B. thetaiotaomicron* (20%) and higher in organisms with better annotation. [src: annotation_gap_discovery]
- [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]]: baseline FBA had 86.5% recall but 42.5% precision. [src: annotation_gap_discovery]
- [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]]: GapMind only partially corroborated gapfilling, and its step counts limited concordance. [src: annotation_gap_discovery]
