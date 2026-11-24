---
type: "Summary"
description: "Summary of the project KBase Data Lakehouse: Common Pitfalls & Gotchas."
doc_type: "short"
full_text: "sources/pitfalls.md"
---
# KBase Data Lakehouse: Common Pitfalls & Gotchas

This page summarises the KBase Data Lakehouse pitfalls report, a quick reference for avoiding common issues when querying KBase Data Lakehouse databases. [src: pitfalls]

## Key Findings

### Identifiers, joins and table schemas
Many pitfalls come from tables that do not hold the key or format a query assumes. See [[concepts/join-key-validity-and-identifier-format-mismatches]].
- gapmind_pathways.clade_name stores the full gtdb_species_clade_id with the representative genome accession suffix, not the short GTDB_species name. [src: pitfalls] The GapMind table is genome-level, one row per genome-pathway pair, so the report says to aggregate with MAX(score_simplified) GROUP BY clade_name, pathway before joining to species data. [src: pitfalls] See [[entities/gapmind]].
- In pangenome_pathway_geography, a search for the nonexistent score_category 'present' made the first analysis count exactly 80 pathways for every species with 0% present. [src: pitfalls]
- gene_cluster has gtdb_species_clade_id, not clade_name. [src: pitfalls]
- Genome metadata needs a join from genome.ncbi_biosample_id to ncbi_env.accession. [src: pitfalls] ncbi_env is in Entity-Attribute-Value format with multiple rows per sample. [src: pitfalls] It must be pivoted or filtered by harmonized_name. [src: pitfalls]
- GenomeDepot browser_protein_cog_classes uses cog_class_id, not cogclass_id. [src: pitfalls]
- In snipe_defense_system, a PFAMs search for PF13250 returned 0 rows. [src: pitfalls] DUF4041 is PF13250 (IPR025280), not PF13291 (ACT_4). [src: pitfalls]
- In fitness_modules, the fitbyexp_* tables are long format (expName, locusId, fit, t), not pre-pivoted wide tables. The report advises using genefitness with an orgId filter. [src: pitfalls] It recommends seedannotation for functional descriptions. [src: pitfalls] See [[entities/fitness-browser]].
- BacDive metabolite_utilization.utilization has four values: +, -, produced and +/-. [src: pitfalls] See [[entities/bacdive]].
- In nmdc_arkin, file_id is the recommended join key for classifier and metabolomics tables. [src: pitfalls] Metabolomics files use nmdc:dobj-12-* identifiers. [src: pitfalls] Most abiotic_features numeric columns carry a _has_numeric_value suffix. [src: pitfalls] trait_features holds about 90 functional_group:* columns, so long form needs stack(...), not GROUP BY. [src: pitfalls] See [[entities/nmdc-integrated-collections]].
- Pandas index lookup in metal_specificity silently treated a gene as absent when locusId types differed. [src: pitfalls]

### Coverage gaps and denominators
Missing tables, partial annotation and the choice of denominator change results. See [[concepts/annotation-and-environmental-metadata-table-gaps-in-the-data-lakehouse]] and [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].
- The pangenome IMG_env table was not found. [src: pitfalls] BiGG_Reaction appears in eggNOG annotations but not in ModelSEED tables, so no biochemistry-side BiGG mapping exists. [src: pitfalls]
- AlphaFold pLDDT confidence is in the structure files, not in the kescience_alphafold metadata. [src: pitfalls]
- In env_embedding_explorer, 3,838 of 83,287 genomes (4.6%) have NaN in at least one of the 64 embedding dimensions. [src: pitfalls] See [[entities/alphaearth-environmental-embeddings]].
- In conservation_fitness_synthesis, essential genes were 82% core using all genes including unmapped, and 86% core using mapped genes only. [src: pitfalls]
- In fitness_modules, min_annotated=2 with FDR correction plus PFam domains (814 terms with 2+ genes) alongside TIGRFam (88 terms) raised module annotation from 8% to 80%. [src: pitfalls]
- For Psl detection, KEGG orthologs K20997–K21005 via eggnog_mapper_annotations gave ~95% prevalence, against <1% by gene name alone. [src: pitfalls] See [[concepts/domain-based-marker-detection-and-annotation-method-bias]].
- The report warns against assuming NMDC pfam_annotation_gff fills the gap left by annotation_kegg_orthology. [src: pitfalls] In NEON, benthic generalists (Ferruginibacter, Flavobacterium, UBA953) have ~85% per-gene KO coverage. [src: pitfalls]
- In enigma_carbon_census_1, a genus-name filter matched only genus-rank reference rows. This falsely showed 0/68 genera in Planet Microbe. [src: pitfalls]
- In bacdive_metal_validation, the unmatched 56.6% are different species concepts or genera not yet in GTDB r214. [src: pitfalls]
- BacDive NCBI taxid links to Fitness Browser at species level, not strain level, so the match is many-to-one. [src: pitfalls]

### Taxonomy and name matching
Name mismatches across databases can create false matches or false absences. See [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]].
- ENIGMA MT20 is a different organism from GTDB's MT20. The report describes the erroneous match as covering 8,434 genomes, 1,751 clinical. [src: pitfalls]
- Reclassification splits matter for CrohnsPhage cross-cohort matching, for example E. eligens to Lachnospira eligens. [src: pitfalls] NB00 in ibd_phage_targeting ships a 23-entry SYNONYM_MAP, enough for a targeted species battery. [src: pitfalls] See [[entities/crohnsphage-data-mart]].
- For ENIGMA bridging, the report suggests data sources with species/strain resolution, such as metagenomes and an ASV reclassification pipeline. [src: pitfalls]

### Cohort design and clustering leakage
See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]] and [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].
- Among 8,489 ecotype-assigned CrohnsPhage samples, 45 sub-studies have ≥ 10 HC samples. [src: pitfalls]
- Short-prefix regex on curatedMetagenomicData sample IDs covers < 20 % of samples and produces mostly noise categories. [src: pitfalls]
- NB04 called C. scindens nonsignificant within both ecotypes, the basis of its "paradox resolved" claim. [src: pitfalls] The report's later analysis found this was a self-selection effect. [src: pitfalls]
- The same-feature leakage warning extends to enterotypes and single-cell clustering followed by within-cluster testing of the clustering features. [src: pitfalls]
- In cf_formulation_design, NB08 pivoted to the RFU-based competition assay only, after finding the endpoint OD limitation. [src: pitfalls]

### Spark, pandas and compute environment
See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]] and [[entities/spark-connect]].
- The gene and gene_genecluster_junction tables have ~1B rows each. They should be prefiltered by gtdb_species_clade_id or genome_id. [src: pitfalls] A two-stage presence-matrix approach, filtering the junction first and then looking up genome_ids, took ~310s with no improvement. [src: pitfalls]
- .toPandas() pulls all data to the driver, so the report recommends filtering, joining and aggregating in Spark first. [src: pitfalls] In gene_function_ecological_agora, a merged DataFrame of ~24M rows × 9 columns (≈ 9 GB working set) exhausted a 16 GB driver. [src: pitfalls]
- The literal 1.0 is DECIMAL(2,1) in Spark, so AVG(CASE WHEN ... THEN 1.0 ELSE 0.0 END) returns DECIMAL. [src: pitfalls]
- For long jobs, the report recommends converting notebooks to scripts run with nohup from a terminal. [src: pitfalls] It also recommends checkpointing. [src: pitfalls]
- In essential_genome, fillna(False) after a left merge gives object dtype, not boolean. [src: pitfalls]
- JupyterHub CLI scripts can import get_spark_session from berdl_notebook_utils.setup_spark_session. [src: pitfalls] os.makedirs(exist_ok=True) can raise FileExistsError on a symlink with a missing target. [src: pitfalls] Using statsmodels.formula.api avoids the problematic graphics import path. [src: pitfalls]
- A REST API 524 Origin Timeout means the server did not respond, and the remedy is to retry after a few seconds. [src: pitfalls] In essential_metabolome, off-cluster mc commands time out unless proxy variables are set. [src: pitfalls] See [[entities/kbase-data-lakehouse]].

### Workflow and provenance
See [[concepts/notebook-provenance-and-session-isolation-in-agent-assisted-analysis]].
- On 2026-04-24, a concurrent Claude process (PID 22230) checked out the plant_microbiome_ecotypes branch during an ibd_phage_targeting NB00 run. The first session's commit then landed on the wrong branch. [src: pitfalls]
- The report recommends checking git history for every referenced notebook before submission or a milestone commit. [src: pitfalls] For notebooks, it shows filling missing code-cell outputs with an empty list and execution_count with None. [src: pitfalls]
- For Codex CLI reviewers, run a minimal smoke test with network-enabled permissions before the full command. [src: pitfalls]

### Other reference notes
- Ingestion config for kbase_ke_pangenome uses tenant "kbase" and dataset "ke_pangenome". [src: pitfalls] See [[entities/kbase-ke-pangenome]].
- For mysqldump ingest, stream with comma-delimited csv.reader (doublequote=True), replace \N with an empty string, and write TSV with a header derived from CREATE TABLE. [src: pitfalls]
- In kescience_webofmicrobes, E and I action codes are mutually exclusive across organism observations, with zero overlap. [src: pitfalls] See [[entities/web-of-microbes]].

## General KBase Data Lakehouse Pitfalls: [ibd_phage_targeting] MetaPhlAn3 Cross-Cohort Taxon Names Need a …

This part of the report is a quick reference for avoiding common issues when querying KBase Data Lakehouse databases. [src: pitfalls] It covers the namespace change from underscores to dots [src: pitfalls], ENIGMA strain-name collisions [src: pitfalls], notebooks that exist only as outputs [src: pitfalls], Web of Microbes action codes [src: pitfalls], concurrent agent sessions in one git clone [src: pitfalls], and taxon-name drift in cross-cohort microbiome tables. [src: pitfalls]

### Namespace convention: underscores to dots

KBase Data Lakehouse collections are migrating from Delta to Iceberg. Iceberg tables are addressed as `catalog.namespace.table`, whereas the old Delta convention joined these parts into one underscore-joined identifier. For example, `kbase.ke_pangenome.genome` was previously `kbase_ke_pangenome.genome`. [src: pitfalls] Only the leading underscore changes, and the table name stays the same. [src: pitfalls] See [[concepts/lakehouse-namespace-migration-tenancy-and-authentication]] and [[entities/kbase-ke-pangenome]].

Queries copied verbatim from older READMEs, reports, notebooks or `.py` files use the underscore form. They can fail on migrated catalogs with `TABLE_OR_VIEW_NOT_FOUND` or an unresolved-relation error. [src: pitfalls] Hundreds of completed-project files use underscore-form names such as `kbase_ke_pangenome`, `kescience_fitnessbrowser`, `nmdc_arkin`, `kescience_mgnify` and `enigma_genome_depot_enigma`. The report leaves these historical files unrewritten on purpose. [src: pitfalls]

Migration is still ongoing. If a dotted namespace is not found, the collection may still be Delta-only, and the underscore form is then correct. [src: pitfalls] The report therefore advises against hardcoding either form. It recommends live, access-aware catalog discovery, either `SET` plus parsing `spark.sql.catalog.*` or the notebook helpers. [src: pitfalls] Use the dotted form for migrated collections and fall back to the underscore form when the dotted name is not found. [src: pitfalls]

### ENIGMA strain-name collisions

Short ENIGMA field-isolate names (MT20, MT42, GW460-LB6, FW507-14TSA) are not globally unique. Matched against `kbase.ke_pangenome.gtdb_metadata.ncbi_strain_identifiers`, they can hit unrelated NCBI organisms. [src: pitfalls] ENIGMA MT20 is *Rhodanobacter glycinis* (Xanthomonadales, groundwater). GTDB's MT20 is clinical *Streptococcus pneumoniae* (Lactobacillales). [src: pitfalls] The report describes that GTDB match as 8,434 genomes, 1,751 clinical. [src: pitfalls] This contaminated genus-environment profiles with spurious clinical data. [src: pitfalls] In genotype_to_phenotype_enigma, 12 of 32 pangenome linkages made through `ncbi_strain_identifiers` were incorrect genus matches. [src: pitfalls]

The fix is to cross-check the genus from the source database (for example `enigma.genome_depot_enigma.browser_taxon`) against the GTDB genus. Reject linkages where the genera disagree. [src: pitfalls] Where possible, match on assembly accession (GCF_*) instead, because it is unambiguous. [src: pitfalls] See [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]] and [[entities/enigma]].

### Notebooks that exist only as outputs

Analyses run in an interactive Claude Code REPL can leave committed figures and data while the producing code stays in the session transcript. The project then looks reproducible: the README cites NB08, NB09 and NB10 and the REPORT cites their findings. Yet `git log` shows no history for those notebooks. [src: pitfalls] Downstream reviewers who read the plan and REPORT at face value miss the gap. [src: pitfalls] In genotype_to_phenotype_enigma, three notebooks (NB08, NB09, NB10), which made up the entire Act II/III closing, existed only as outputs. [src: pitfalls] Reconstruction took a few hours once the gap was found. [src: pitfalls] The report says this is especially easy to trip over late in a project, when the user is synthesizing and no longer creating fresh notebooks for each analytical step. [src: pitfalls]

Recommended practice:
- When an analysis is worth committing artifacts for, commit it as a notebook. If you are building figures in a REPL, move the logic into a numbered notebook before saving results. [src: pitfalls]
- Before `/submit` or any milestone commit, run `git log --all --oneline -- projects/{project_id}/notebooks/NB*.ipynb`. This checks that every NBxx named in the README or plan has real notebook history. [src: pitfalls]
- If you inherit such a gap, reconstruct the notebooks from the committed artifacts. Record this in the `RESEARCH_PLAN.md` revision history, so reviewers can tell "interactive original" counts from "reproducible re-run" counts. [src: pitfalls]

See [[concepts/notebook-provenance-and-session-isolation-in-agent-assisted-analysis]].

### Web of Microbes action codes

`kescience.webofmicrobes.observation.action` is a single-letter code: `I` increased, `E` emerged, `N` no change, and occasionally `D` decreased. [src: pitfalls] A naive `SELECT action` returns raw codes, not a binary produced/consumed label. [src: pitfalls] NB02 and NB08 of genotype_to_phenotype_enigma define `produced = action IN ('I', 'E')`. A compound counts as produced if it increased in supernatant or emerged from below the detection limit to reach it. [src: pitfalls] Including `N` makes every strain look like a production generalist and collapses the signal. [src: pitfalls] Excluding `E` misses genuinely novel production. [src: pitfalls] See [[entities/web-of-microbes]].

### Concurrent agent sessions in one clone

Two sessions in the same clone share one `.git` directory and one working tree. A `git checkout` in one silently removes branch-specific files from the other's tree. Later commits land on whichever branch HEAD points at. [src: pitfalls]

On 2026-04-24, during `ibd_phage_targeting` NB00 work, a second `claude` process (PID 22230) ran `git checkout projects/plant_microbiome_ecotypes` during a long `jupyter nbconvert --execute` run. The first session's next commit landed on the plant-microbiome branch. `README.md` and `RESEARCH_PLAN.md` appeared missing from `projects/ibd_phage_targeting/`. [src: pitfalls] Both files were still safe in git on the ibd branch. [src: pitfalls] The report says a "missing" file the agent thought it had just committed is almost always a wrong-branch commit or a background checkout, not a deletion. [src: pitfalls]

Recommended practice:
- Note the intended branch at session start. Run `git branch --show-current` before every commit, and investigate if it differs. [src: pitfalls]
- To recover, cherry-pick the commit onto the correct branch, then reset the stray branch with `git branch -f <stray> origin/<stray>`. No data is lost as long as the stranded commit is recoverable via `git reflog`. [src: pitfalls]
- Use git worktrees. Each has its own `HEAD` and working tree but shares one object store, so a checkout in one does not affect the others. [src: pitfalls]

### Taxon-name drift in cross-cohort microbiome tables

Pivoting cross-cohort data on `taxon_name_original` or any string key can silently split one species into two non-overlapping rows when cohorts use different MetaPhlAn3 database vintages or curatedMetagenomicData processing stages. [src: pitfalls] In the CrohnsPhage mart, the divergences include:
- **Format.** The short name `Faecalibacterium prausnitzii` appears alongside full lineage strings ending in `s__Faecalibacterium_prausnitzii`. [src: pitfalls]
- **Genus renames (GTDB r214+).** CMD_HEALTHY `Bacteroides vulgatus` and CMD_IBD `Phocaeicola vulgatus` share one NCBI taxid but are treated as separate species. [src: pitfalls] The report says this also affects *B. dorei / coprocola / plebeius / salanitronis / sartorii / massiliensis / coprophilus*, all now *Phocaeicola*. [src: pitfalls]
- **Other splits.** *Eubacterium rectale* became *Agathobacter rectalis*, *E. eligens* became *Lachnospira eligens*, and *E. hallii* became *Anaerobutyricum hallii*. [src: pitfalls] *Ruminococcus gnavus* became *Mediterraneibacter gnavus*. [src: pitfalls] The report lists *Clostridium bolteae / clostridioforme / symbiosum / innocuum / asparagiforme / hathewayi / citroniae / aldenense* as moved to *Enterocloster*, *Hungatella* or *Erysipelatoclostridium*. [src: pitfalls] *Lactobacillus mucosae / ruminis* moved to *Limosilactobacillus* or *Ligilactobacillus*. [src: pitfalls]

CMD_IBD uses modern names and CMD_HEALTHY uses legacy names. A naive pivot therefore gives log₂FC ≈ 28 (≈ 2.68 × 10⁸ fold) for every renamed species, because one cohort's mean abundance collapses to pseudocount. [src: pitfalls] The committed `ref_taxonomy_crosswalk` does not fully fix this. It lists *B. vulgatus* and *P. vulgatus* as separate rows with different `canonical_name` values. [src: pitfalls] Legacy `Bacteroides_X` rows have `ncbi_taxid` = NaN (not a number), so a taxid join leaves them orphaned. [src: pitfalls] See [[entities/crohnsphage-data-mart]] and [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

## General KBase Data Lakehouse Pitfalls: [ibd_phage_targeting] curatedMetagenomicData Sub-Studies Are …

This part of the report covers MetaPhlAn3 taxon-name synonymy, sub-study confounding in curatedMetagenomicData, and same-feature clustering leakage in ibd_phage_targeting. [src: pitfalls] See [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]] and [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]] for the wider context.

### Taxon-name synonymy across cohorts

A curated synonym map suffices for a small species battery, but the full taxonomy needs a systematic layer. [src: pitfalls]

- Format normalization parses the `s__Genus_species` component from full lineage strings and strips brackets from short names, giving a canonical "Genus species". [src: pitfalls]
- NB00 in ibd_phage_targeting ships a 23-entry `SYNONYM_MAP` covering the major renames. The report calls this enough for a targeted species battery. [src: pitfalls]
- Before any cross-cohort aggregation over the full taxonomy, the report requires an NCBI-taxid-backed synonymy layer with GTDB-version-aware rename tables. It names this an NB01 dependency in ibd_phage_targeting. [src: pitfalls]
- The problem applies to `fact_taxon_abundance` and other MetaPhlAn3-derived tables that span cohorts processed at different times. It also applies when MetaPhlAn outputs are merged with GTDB-r214+ analyses. [src: pitfalls]

### Sub-study confounding in curatedMetagenomicData

In the reported comparison, no sub-study contains both Crohn's disease (CD) and healthy control (HC) samples, so a pooled contrast cannot be adjusted by a random effect. [src: pitfalls]

curatedMetagenomicData bundles samples from ~50+ published studies into `CMD_HEALTHY` and `CMD_IBD` buckets. [src: pitfalls] Every CMD_HEALTHY sample comes from a healthy-cohort study, such as LifeLinesDeep_2016, AsnicarF_2021, YachidaS_2019 and HansenLBS_2018. [src: pitfalls] Every CMD_IBD CD sample comes from an IBD-cohort study: HallAB_2017, VilaAV_2018, LiJ_2014, IjazUZ_2017 or NielsenHB_2014. [src: pitfalls] No sub-study contains both CD and HC samples. [src: pitfalls]

A pooled `log_abundance ~ diagnosis + (1 | substudy)` mixed model on this contrast is structurally unidentifiable. The sub-study random effect perfectly predicts diagnosis. The model either fails silently to converge or absorbs the whole CD effect into the random intercept. [src: pitfalls] On this design, `statsmodels.mixedlm` with `lbfgs` returns without error but gives no usable fixed-effect estimate. [src: pitfalls]

The same pattern appears in the CrohnsPhage integrated mart scoped to ecotype-assigned samples (8,489 total). [src: pitfalls] There, 45 sub-studies have ≥ 10 HC samples. [src: pitfalls] Five sub-studies have ≥ 10 CD samples. [src: pitfalls] None has both ≥ 10 HC and ≥ 10 CD. [src: pitfalls]

The report cites Vujkovic-Cvijin 2020 on this kind of structural confounding as the reason to adjust. It says a standard random-effects model cannot do so on the pooled curatedMetagenomicData contrast. [src: pitfalls]

### Recommended handling

- Four IBD sub-studies have both CD and nonIBD samples with ≥ 10 each: HallAB_2017, LiJ_2014, IjazUZ_2017 and NielsenHB_2014. Together they hold 242 CD and 369 nonIBD samples. [src: pitfalls]
- Within each of these, the report recommends a within-study CLR-Δ or regression, combined by inverse-variance weighted meta-analysis. It calls this the clean CD-effect estimate. [src: pitfalls]
- That meta-analysis is the benchmark against which any pooled effect should be sanity-checked. [src: pitfalls]
- If a pooled CD-vs-HC effect must be reported, the report says not to rely on sub-study random effects to adjust it. The effect should carry an explicit caveat that study, cohort, sequencing center and sample prep are all collinear with diagnosis. [src: pitfalls]
- For IBD samples, a participant_id such as `CMD:HallAB_2017:SKST006` encodes the sub-study in its middle colon-separated token. [src: pitfalls]
- For HC samples, the sub-study sits under the key `"study"` in the `dim_samples.external_ids` JSON blob, for example `"AsnicarF_2021"`. [src: pitfalls]
- Together these two routes cover ≈ 80 % of curatedMetagenomicData samples. [src: pitfalls] A short-prefix regex on sample IDs covers < 20 % and produces mostly noise categories. [src: pitfalls]
- The report says the problem extends to the KBase Data Lakehouse `fact_taxon_abundance` analyses. It also extends to any pooled public dataset, such as SRA study inventories or Qiita studies, where different groups collected cases and controls. [src: pitfalls]

### Same-feature clustering leakage

The report argues that clustering samples on taxon abundances and then testing those same abundances selects samples on the outcome. [src: pitfalls] In ibd_phage_targeting, this reversed at least one call and shrank the candidate list sharply. [src: pitfalls]

Cluster membership is a function of the same abundances that the second step tests. Within-cluster effect sizes are mechanically inflated for cluster-defining taxa. The within-cluster top-N list is then largely the cluster definition itself. [src: pitfalls]

In NB04, K=4 LDA ecotypes were trained on MetaPhlAn3 species abundances. Within-ecotype CD-vs-HC CLR-Mann-Whitney tests then used the same species matrix. [src: pitfalls] NB04 reported a 33-species within-ecotype Tier-A list with effect sizes of +0.5 to +3.0 CLR-Δ. [src: pitfalls]

### Sensitivity checks in NB04b

- **Held-out-species test.** It used 5 random 50/50 species splits. LDA was refit on half A and half B was tested. The Jaccard index compared the refit top-30 with the original top-30 ∩ half-B. [src: pitfalls] The heuristic bound treats Jaccard > 0.5 as leakage bounded and < 0.3 as leakage dominating. [src: pitfalls] Observed values were E1 = 0.230 [src: pitfalls] and E3 = 0.064. [src: pitfalls] Both fall below the 0.3 threshold, which on that heuristic means leakage dominates. [src: pitfalls]
- **Leave-one-species-out (LOO) refit.** For each battery species, ecotypes were refit on all other species. Cluster labels were re-derived and the held-out species was retested. [src: pitfalls]
- **C. scindens.** NB04 called it nonsignificant within both ecotypes, which was the basis for its "paradox RESOLVED" claim. [src: pitfalls] Under LOO it was CD-increased in E1 (CI +0.68, +0.87) [src: pitfalls] and in E3 (CI +1.13, +1.71). [src: pitfalls] The report attributes the earlier nonsignificant call to a self-selection effect. [src: pitfalls]
- **Independent cross-check.** A confound-free within-IBD-substudy CD-vs-nonIBD analysis found that most NB04 Tier-A E1 candidates had negative within-study effects. The report interprets them as ecotype markers, not CD drivers. [src: pitfalls]

### Fixes and scope

- In NB04c, the within-ecotype Tier-A list was gated with an independent, confound-free within-substudy CD-vs-nonIBD evidence stream. [src: pitfalls] Requiring both within-ecotype differential abundance and the independent contrast shrank Tier-A from 33 to 3 candidates. [src: pitfalls]
- Rebuilding Pillar 1 on a functional feature matrix was flagged as future work and not performed. [src: pitfalls]
- The report recommends leave-one-feature-out refitting for any feature whose differential-abundance call would drive a decision. [src: pitfalls]
- It also proposes defining clusters on a functional matrix (KEGG pathways, MetaCyc or Enzyme Commission numbers) and then testing taxonomic differential abundance. Leakage then becomes structurally impossible rather than empirically bounded. [src: pitfalls]
- The warning extends to microbiome enterotypes and to single-cell type-stratified differential expression. It covers any analysis where cluster labels are a function of the features being tested. [src: pitfalls]

## General KBase Data Lakehouse Pitfalls: [genotype_to_phenotype_enigma] Fitness Browser KO Mapping Is a …

This part of the report covers pitfalls in the Fitness Browser, KBase Data Lakehouse tenancy and access, the REST API, authentication tokens, numeric typing, and ingest and Spark conversion bugs. [src: pitfalls]

### Fitness Browser (FB) schema traps

Mapping an FB locus to a KEGG ortholog (KO) takes two joins, because the database has no single (orgId, locusId)-to-KO table. [src: pitfalls] `besthitkegg` maps each locus to a KEGG organism and gene (`keggOrg`, `keggId`) by best hit. [src: pitfalls] `keggmember` maps each (`keggOrg`, `keggId`) pair to its KEGG ortholog group (`kgroup`, the KO). Neither table alone is sufficient. [src: pitfalls] Three column-name and type traps also appear:
- `kgroupdesc` uses the column `desc`, not `description`. [src: pitfalls]
- `genefitness.fit` and `.t` are strings, so `t` must be cast with `CAST(t AS DOUBLE)` before `ABS` or any comparison. [src: pitfalls]
- `experiment.expGroup` holds the experiment class. `SELECT Group` fails with `UNRESOLVED_COLUMN`. [src: pitfalls]

Strings holding numbers are a wider problem. Many databases store numeric values as strings, which affects all `kescience_fitnessbrowser` columns and the coordinates and lengths in `kbase_genomes`. [src: pitfalls] Comparisons such as `fit < -2` need a cast, for example `CAST(fit AS FLOAT) < -2`. [src: pitfalls]

### Tenancy and access

The tenant is the database prefix. For example, `kbase_ke_pangenome` has tenant `kbase`, and `kescience_mgnify` has tenant `kescience`. [src: pitfalls] In the `bakta_reannotation` project, the `tenant` field of a `data_lakehouse_ingest` config is the MinIO governance group name, not the database name prefix. The library prepends the tenant to the `dataset` field to form the namespace. [src: pitfalls] Two mistakes follow from this:
- `tenant="kbase_ke"` leaves the user without access and falls back to the personal warehouse. [src: pitfalls]
- `dataset="kbase_ke_pangenome"` with `tenant="kbase"` creates `kbase_kbase_ke_pangenome`. [src: pitfalls]

The working configuration is tenant `kbase` and dataset `ke_pangenome`. [src: pitfalls] See [[concepts/lakehouse-namespace-migration-tenancy-and-authentication]] and [[entities/kbase-ke-pangenome]].

To check access, call `get_group_sql_warehouse(tenant_name)`. An `ErrorResponse` with error 20040 means the user is not in that group. [src: pitfalls] If an error shows the physical path, the tenant is the segment after `tenant-sql-warehouse/`. [src: pitfalls]

Failed table access can surface as `S3 access denied`, `403 Forbidden`, `Token denied` or `AccessControlException`. These are authorization signals, not technical faults. [src: pitfalls] Such errors are expected when exploring databases the user has not been granted, and the report says to treat them as a permissions prompt. [src: pitfalls] The report names the Tenant Browser as the route to request table access. [src: pitfalls]

### REST API behaviour

The report lists these REST API (representational state transfer, application programming interface) failure signatures and remedies:

| Symptom | Meaning | Remedy |
|---|---|---|
| 504 Gateway Timeout | Query took too long [src: pitfalls] | Simplify the query, add filters, or use direct Spark [src: pitfalls] |
| 524 Origin Timeout | Server did not respond [src: pitfalls] | Retry after a few seconds [src: pitfalls] |
| 503 "cannot schedule new futures after shutdown" | Spark executor restarting [src: pitfalls] | Wait 30s, retry [src: pitfalls] |
| Empty response | Query failed silently [src: pitfalls] | Check query syntax [src: pitfalls] |

The report's rule of thumb is to prefer direct Spark SQL (`get_spark_session()`). The REST API is acceptable for small one-off queries, but loops over many tables, such as row counts for all `sdt_*` tables, should use Spark. [src: pitfalls] The `/count` endpoint frequently errors or times out on tables that Spark handles instantly. [src: pitfalls] The `/schema` endpoint frequently times out for large tables, and `DESCRIBE database.table` through `/query` is more reliable. [src: pitfalls]

### Authentication tokens

The `.env` variable is `KBASE_AUTH_TOKEN`, not `KB_AUTH_TOKEN`. [src: pitfalls] On JupyterHub, a fresh token is always at `~/.berdl_kbase_session`. The IPython startup script `~/.ipython/profile_default/startup/05-token-sync.py` syncs it every 30 seconds. [src: pitfalls] The `.env` file is not updated automatically, so long CLI sessions outside JupyterHub need a manual re-export. [src: pitfalls] In `essential_metabolome`, off-cluster `mc` (MinIO client) commands time out unless proxy environment variables are set. [src: pitfalls]

### Ingest and conversion bugs

In `kescience_paperblast`, exporting SQLite to TSV failed because Python's `sqlite3` decodes TEXT columns as strict UTF-8. Non-UTF-8 bytes raised `OperationalError` during cursor iteration, before any cleaning such as `_clean()` ran. [src: pitfalls] The fix is to set `conn.text_factory = lambda b: b.decode('utf-8', errors='replace')`, which lets iteration succeed and turns invalid bytes into U+FFFD. [src: pitfalls] The report says to set it right after connecting, before any query. [src: pitfalls]

A second paperblast problem was in `parse_sql_schema()`, which uses regex to extract column definitions from `CREATE TABLE` statements. [src: pitfalls] If the table body begins with an inline comment, the parser treats `/*` as a column name. This gives an invalid schema, and the ingest silently skips the whole table with no error message or quarantine entry. [src: pitfalls] The report's solution is to strip both `/* ... */` and `--` comments before splitting tokens. [src: pitfalls]

In `prophage_ecology`, `np.random.choice()` on Python strings returns numpy `str_` objects. PySpark's `createDataFrame()` cannot infer a schema for them and raises `PySparkTypeError: [CANNOT_INFER_TYPE_FOR_FIELD]`. [src: pitfalls] The fix is to cast to native Python `str` before building DataFrames. [src: pitfalls]

In `nmdc_community_metabolic_ecology`, Spark SQL `DECIMAL` columns, such as `abundance` in `kbase.nmdc_arkin.centrifuge_gold`, come back as Python `decimal.Decimal` objects from `.toPandas()`. [src: pitfalls] Arithmetic with floats, such as from `AVG()`, then raises `TypeError`. [src: pitfalls] A second case is that `AVG(CASE WHEN condition THEN 1.0 ELSE 0.0 END)` also returns `DECIMAL`, because Spark treats `1.0` as `DECIMAL(2,1)`, not `DOUBLE`. [src: pitfalls] The fixes are `CAST(col AS DOUBLE)` in SQL or `.astype(float)` after collection. [src: pitfalls] As a rule, wrap any `AVG()` over integers or decimal literals in `CAST(... AS DOUBLE)`, and add `.astype(float)` after `.toPandas()` as a safety net. [src: pitfalls] The issue was observed in NB03 for `centrifuge_gold.abundance` (cell-15) and `gapmind_pathways` AVG aggregates (cell-11/18). [src: pitfalls]

## General KBase Data Lakehouse Pitfalls; Pangenome (kbase_ke_pangenome) Pitfalls

This part of the report collects general pitfalls in the KBase Data Lakehouse queries, including the pangenome collection (kbase_ke_pangenome), the NMDC and Planet Microbe abundance tables, the REST API, Spark Connect and `ncbi_env`. Many of them return zero rows or plausible but wrong numbers without an error. [src: pitfalls] See also [[concepts/join-key-validity-and-identifier-format-mismatches]] and [[entities/spark-connect]].

### SQL syntax and reserved words

Spark Connect rejects `SELECT DISTINCT` combined with an aggregate when there is no `GROUP BY` (`MISSING_GROUP_BY`, SQLSTATE 42803). [src: pitfalls] This is a strict standard-SQL reading, and DuckDB and SQLite accept the syntax. [src: pitfalls] It was observed in nmdc_community_metabolic_ecology NB03 cell-9, while checking the `score_category` distribution in `gapmind_pathways`. [src: pitfalls] The report's rule is to use `GROUP BY` for grouped aggregations, because `SELECT DISTINCT col, COUNT(*)` is always wrong. [src: pitfalls]

The `gtdb_taxonomy_r214v1` table has a column named `order`, which is a taxonomic rank. [src: pitfalls] In Spark SQL, `order` is a reserved keyword, and using it unquoted in a SELECT or JOIN causes a parse error (from pgp_pangenome_ecology). It needs backticks. [src: pitfalls] The report extends this to other reserved words used as column names, such as `class`, `select` and `from`. [src: pitfalls]

### Taxonomy tables and genus-level abundance

In enigma_carbon_census_1, the NMDC `covstats_taxonomy_rollup` and Planet Microbe `run_to_taxonomy` abundance tables key on a species-level `taxonomy.name`, not a genus-level one. [src: pitfalls] Filtering them by a bare genus name matches only the near-zero rows that carry the genus rank as a literal name. It does not sum the species in that genus. [src: pitfalls] The failure is silent: the query returns rows and non-null numbers, but abundances are ~0 and whole genera look absent. [src: pitfalls] In that project, an early marine-abundance contrast showed 0/68 genera present in Planet Microbe for this reason. [src: pitfalls]

The fix is to derive the genus from the species `name`, `GROUP BY genus`, `SUM(abundance)`, and only then filter to the genera of interest. [src: pitfalls] A genus filter that returns rows is not evidence that the rollup happened. [src: pitfalls] See [[entities/nmdc-integrated-collections]].

In the pangenome collection, `genome.gtdb_taxonomy_id` is truncated at genus level. [src: pitfalls] `gtdb_taxonomy_r214v1.gtdb_taxonomy_id` includes species. [src: pitfalls] The prophage_ecology report found that joining the two on `gtdb_taxonomy_id` returns zero rows, and it recommends joining on `genome_id`. [src: pitfalls]

### Identifier formats and join failures

Several joins fail because the identifier formats differ. The report gives these formats:

| Identifier | Format | Example |
|---|---|---|
| `genome_id` | `RS_GCF_XXXXXXXXX.X` or `GB_GCA_XXXXXXXXX.X` | `RS_GCF_000005845.2` [src: pitfalls] |
| `gtdb_species_clade_id` | `s__Genus_species--{representative_genome_id}` | `s__Escherichia_coli--RS_GCF_000005845.2` [src: pitfalls] |
| `gene_cluster_id` | `{contig}_{number}` or `{prefix}_mmseqsCluster_{number}` | `NZ_CP095497.1_1766` [src: pitfalls] |

**Double hyphen in clade IDs.** Species clade IDs contain `--`. [src: pitfalls] In direct Spark SQL this is not a problem when the ID is inside a quoted string literal. [src: pitfalls] The REST (representational state transfer) API (application programming interface) rejects any query containing `--` regardless of quoting. It treats the characters as a SQL (structured query language) comment and returns a 400 error. [src: pitfalls] The snipe_defense_system workaround is to query all rows unfiltered and filter locally with pandas. [src: pitfalls]

**Clade names in GapMind.** `gapmind_pathways.clade_name` stores the full `gtdb_species_clade_id`, including the representative genome accession suffix. It does not store the short `GTDB_species` name. [src: pitfalls] In nmdc_community_metabolic_ecology, joining `gapmind_pathways` to a temporary view built from `gtdb_species_clade.GTDB_species` returned 0 rows for this reason. [src: pitfalls] The `taxon_bridge.tsv` from NB02 already holds usable `gtdb_species_clade_id` values, so it can filter directly. [src: pitfalls]

**NCBI taxonomy IDs.** In metabolic_capability_dependency, joining `kescience.fitnessbrowser.organism` to `kbase.ke_pangenome.gtdb_metadata` on NCBI taxonomy IDs returned zero matches. [src: pitfalls] The report says the `ncbi_taxid` (or equivalent) column holds the string tokens `"t"` and `"f"` rather than numeric IDs. [src: pitfalls] The project's fallback was to match organisms directly by `orgId`, with no clade-level link. [src: pitfalls] See [[entities/fitness-browser]].

### GapMind table semantics

With `sequence_scope = 'core'`, `score_simplified` holds only `0.0` (incomplete pathway) or `1.0` (complete pathway). It is not a continuous confidence score. [src: pitfalls] The table is genome-level, with one row per genome-pathway pair. The report says to aggregate to species level with `MAX(score_simplified) GROUP BY clade_name, pathway` before joining to species data. [src: pitfalls]

Filtering on `metabolic_category == 'amino_acid'` returns 0 rows. [src: pitfalls] The stored values are `'aa'` for amino acid pathways and `'carbon'` for carbon source pathways. [src: pitfalls] See [[entities/gapmind]].

### Temporary views lost on reconnect

In nmdc_community_metabolic_ecology, a Spark temporary view registered in one cell may be silently destroyed if Spark Connect reconnects during that cell. An expensive 305M-row full-table scan is one example trigger. [src: pitfalls] Later cells that join against the view then return 0 rows with no error. [src: pitfalls] The report's remedy is to re-register the view immediately before any cell that joins on it. The Python variable holding the data persists in the kernel through reconnections. [src: pitfalls] To prevent the problem, avoid expensive scans between registration and use. For schema checks on large tables, use `LIMIT` or `TABLESAMPLE` rather than full `GROUP BY` counts. [src: pitfalls] See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

### Environmental metadata in `ncbi_env`

The amr_strain_variation report found that `ncbi_env` is not a flat table with columns like `genome_id, isolation_source, collection_date`. It is an Entity-Attribute-Value table with columns `accession` (BioSample ID), `attribute_name`, `content`, `display_name`, `harmonized_name`, `id` and `package_content`. [src: pitfalls] To get genome metadata, join `genome.ncbi_biosample_id` to `ncbi_env.accession`. [src: pitfalls] Then filter `attribute_name` to `isolation_source`, `collection_date`, `geo_loc_name` and `host`, and pivot from long to wide format. [src: pitfalls]

## Pangenome (kbase_ke_pangenome) Pitfalls; Data Sparsity Issues; Foreign Key Gotchas

This part of the report records pitfalls with ANI table names and query scale, sparse environmental metadata, orphan pangenome records, join keys and Pfam lookups. [src: pitfalls] The pitfalls bear on [[entities/kbase-ke-pangenome]] and related tables. [src: pitfalls]

### ANI table and query scale

The `genome_ani` table (ANI = average nucleotide identity) uses the columns `genome1_id`, `genome2_id` and `ANI`, not `genome_id_1`, `genome_id_2` and `ani`, and capitalization matters. [src: pitfalls] In amr_strain_variation, ANI queries for species with >500 genomes can take 30+ minutes per species and may time out Spark connections. [src: pitfalls] The report states that K. pneumoniae (14,240 genomes) and S. aureus (14,526 genomes) generate IN clauses with 14K+ IDs (IDs = identifiers) that overwhelm the query planner. [src: pitfalls] For ANI-based Mantel tests, it recommends capping at <=500 genomes or using subsampling. [src: pitfalls] See also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

### Sparse environmental metadata

Environmental metadata are sparse at the per-genome level, so the report advises species-level labels for cross-species work. [src: pitfalls] Parsing `isolation_source` and `host` from `ncbi_env` per genome gave 52.7% "Unknown" labels (94,957/180,025 genomes), because most BioSample records lack structured isolation metadata. [src: pitfalls] The report recommends species-level majority-vote environment labels, with 91% coverage via keyword classification of NCBI metadata. [src: pitfalls] The `ncbi_env` table uses Entity-Attribute-Value format, with multiple rows per sample. [src: pitfalls]

[[entities/alphaearth-environmental-embeddings]] cover only 83,227 of 293,059 genomes (28.4% coverage). [src: pitfalls] They need valid latitude/longitude coordinates, which are often missing in NCBI metadata, especially for clinical isolates. [src: pitfalls] The `ncbi_lat_lon` field in `gtdb_metadata` is most commonly NULL [src: pitfalls], often holds malformed strings such as "missing" or "not collected" [src: pitfalls], and is often low precision, for example "37.0 N 122.0 W". [src: pitfalls]

### Orphan pangenomes

12 pangenome records reference species clades that are not in `gtdb_species_clade`. [src: pitfalls] Examples are s__Portiera_aleyrodidarum--RS_GCF_000300075.1, s__Profftella_armatura--RS_GCF_000441555.1 and s__Nanosynbacter_sp022828325--RS_GCF_022828325.1; the report describes them as mostly symbionts and single-genome species. [src: pitfalls] They are valid pangenomes filtered from species metadata, and the report recommends a LEFT JOIN to keep them. [src: pitfalls]

### Join keys and cross-species comparison

`eggnog_mapper_annotations.query_name` joins to `gene_cluster.gene_cluster_id`, not to `gene.gene_id`. [src: pitfalls] Gene cluster IDs are meaningful only within a species and cannot be compared across species. [src: pitfalls] To compare gene content across species, the report recommends COG categories (COG = clusters of orthologous groups), KEGG orthologs in the `KEGG_ko` column, or PFAM domains. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

In snipe_defense_system, 2,962 DUF4041 eggNOG annotation records became 4,572 rows after joining `gene_cluster`. A `query_name` can map to clusters in several species pangenomes. [src: pitfalls] The post-JOIN count is the number of species-level gene clusters. The eggNOG count is the number of unique annotation records. Both are valid for different purposes, so the report says to state which one you report. [src: pitfalls]

### Pfam names versus accessions

The `eggnog_mapper_annotations.PFAMs` column stores Pfam domain names (for example `DUF4041`, `GIY-YIG`), not accession IDs (for example `PF13250`, `PF01541`). [src: pitfalls] In snipe_defense_system, searching for PF13250 returned 0 rows [src: pitfalls], while searching for DUF4041 returned 2,962. [src: pitfalls] The column holds comma-separated lists of names, so the report says to use `LIKE` with `%` wildcards, not exact equality. [src: pitfalls]

Looking up a Pfam name alone can give the wrong accession. [src: pitfalls] PF13250 and PF13291 are numerically close but unrelated families. [src: pitfalls] PF01541 (canonical GIY-YIG) and PF13455 (Mug113) are in the same clan but are distinct families. [src: pitfalls] Symptoms of a wrong accession are zero co-occurrence hits for domains that should co-occur (for example DUF4041 + GIY-YIG in SNIPE proteins) or unexpected functional annotations. [src: pitfalls] The fix is to verify accessions against a known protein in InterPro or UniProt. [src: pitfalls] For SNIPE, DUF4041 is PF13250 (IPR025280), not PF13291 (ACT_4). [src: pitfalls] The SNIPE nuclease is PF13455 (Mug113, GIY-YIG clan CL0418), not PF01541. [src: pitfalls] See also [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]].

## PhageFoundry (phagefoundry_) Pitfalls; Data Interpretation Issues; JupyterHub Environment …

PhageFoundry data in the KBase Data Lakehouse is split across two database types, and this part of the report warns that mistaking one for the other leads to wrong conclusions. [src: pitfalls] The same part gives guidance on pangenome table semantics, Spark session imports, notebook execution and MySQL dump ingest. [src: pitfalls]

### PhageFoundry databases

The GenomeDepot browser databases follow the pattern `phagefoundry_{species}_genome_browser_genomedepot`. They hold genome annotations only (eggNOG, COG (clusters of orthologous groups), Pfam) in `browser_*` tables, with 10+ tables each. [src: pitfalls] The `phagefoundry_strain_modelling` database holds experimental phage-host interaction data and an ML model across 18 tables, including organism, interaction and feature. [src: pitfalls] Exploring only the GenomeDepot databases can wrongly suggest PhageFoundry has no experimental data. The strain modelling database contains the experimental results (Gaborieau et al. 2024, Nature Microbiology). [src: pitfalls] See also [[entities/phagefoundry]].

- The `strainmodelling_gene` table has 933K genes but only `locus_tag` and `protein_seq` columns. It has no `gene_name`, `product` or functional annotation, so genes cannot be searched by name. [src: pitfalls]
- As a workaround, the `strainmodelling_feature` and `strainmodelling_protein_family` tables link gene clusters to ML model features with SHAP (Shapley additive explanations) importance scores. [src: pitfalls]
- The GenomeDepot table `browser_protein_cog_classes` uses `cog_class_id`, not `cogclass_id`. [src: pitfalls]

### Cold databases

For rarely accessed databases, including `phagefoundry_strain_modelling`, the Spark cluster needs warm-up time. `/count` often returns correct results while `/query` and `/sample` return 0 rows or empty results. [src: pitfalls] The recommended workaround is to confirm the data exist with `/count`, then retry `/query` with exponential backoff. Warm-up may take several minutes. [src: pitfalls]

### Pangenome table semantics

In the gene_cluster table, `is_core` = 1 means present in ≥95% of genomes. [src: pitfalls] `is_auxiliary` = 1 means present in <95% and >1 genome. [src: pitfalls] `is_singleton` = 1 means present in exactly 1 genome. [src: pitfalls] The three flags are mutually exclusive, with only one flag equal to 1 per row. [src: pitfalls] They are stored as integers (0/1), not booleans. `WHERE is_core = 1` is correct, while `WHERE is_core = true` may fail depending on the SQL (structured query language) dialect. [src: pitfalls]

In the pangenome table, `no_core` + `no_aux_genome` = `no_gene_clusters`, the total cluster count. [src: pitfalls] `no_singleton_gene_clusters` is a subset of `no_aux_genome`, so singletons are counted inside the auxiliary total. [src: pitfalls] See also [[entities/kbase-ke-pangenome]].

### Spark session imports by environment

The `get_spark_session` import pattern differs across three environments, and the wrong one causes `ImportError`. [src: pitfalls]

| Environment | Pattern |
|---|---|
| JupyterHub notebooks | `spark = get_spark_session()` with no import, injected by `/configs/ipython_startup/00-notebookutils.py` [src: pitfalls] |
| JupyterHub CLI/scripts | `from berdl_notebook_utils.setup_spark_session import get_spark_session`. The fitness_modules project found this works from regular Python scripts, not just notebooks. [src: pitfalls] |
| Local machine | `from get_spark_session import get_spark_session` [src: pitfalls] |

Each wrong choice fails in a predictable way:
- The local import on the cluster gives `ImportError`, because `scripts/get_spark_session.py` exists only on local machines. [src: pitfalls]
- The cluster import locally gives `ImportError`, because that package is only on the cluster. [src: pitfalls]
- Bare `get_spark_session()` in a JupyterHub CLI script gives `NameError`, because auto-import applies only to notebook kernels. [src: pitfalls]

For local-machine Spark Connect setup, `.venv-berdl` activation and kernel-restart retry patterns, the report points to `.claude/skills/berdl-query/references/off-cluster-mechanics.md`. [src: pitfalls] See also [[entities/spark-connect]].

### Spark Connect failure and recovery

The conservation_vs_fitness project reports that Spark Connect runs as a Java process on port 15002. [src: pitfalls] Killing Java processes, for example when cleaning up stale notebook processes, takes down Spark Connect. `get_spark_session()` then fails with `RETRIES_EXCEEDED` or `Connection refused`. [src: pitfalls] To recover, log out of JupyterHub and start a new session. Then run `get_spark_session()` from a notebook to restart the daemon. It cannot be restarted from the CLI. [src: pitfalls]

### Headless notebook execution

Notebooks can be run headlessly with `jupyter nbconvert --to notebook --execute`, and the spawned kernel has `get_spark_session()` available. [src: pitfalls] Long-running notebooks may time out, so `--ExecutePreprocessor.timeout` should be set appropriately. [src: pitfalls] For long pipelines, the report advises checkpointing: save intermediate files and skip steps that already have output. This allows re-running after interruptions without repeating completed work. [src: pitfalls]

The genome_depot_enigma project found a limit on `--inplace`. On its JupyterHub, `jupyter nbconvert --to notebook --execute --inplace ...` can exit with code 0 but leave the notebook on disk with zero cell outputs. The kernel runs the cells successfully, but the outputs are never written back. [src: pitfalls] This is worst when the pre-flight cell raises an intentional `RuntimeError` (the `CONFIRMED = False` pattern used by `/berdl-ingest`), because the plan that was meant to be inspected is lost. [src: pitfalls] Even with `--allow-errors`, outputs may still not be persisted. [src: pitfalls] The solution is not to rely on `--inplace`. Write to a separate file with `--output`, or for long production ingests run the equivalent logic as a standalone Python script that streams stdout/stderr to a log. [src: pitfalls]

The `/berdl-ingest` `initialize()` function is off-cluster-only. On JupyterHub, the report says to bypass it and build Spark/MinIO clients directly, following `.claude/skills/berdl-ingest/references/on-cluster-bypass.md`. [src: pitfalls]

### Ingesting MySQL dumps

The genome_depot_enigma project lists three mysqldump traits that break a naive ingest:
- The data files have no header row. Column names come from the `CREATE TABLE`. [src: pitfalls]
- NULL is the literal `\N`, not an empty string or `NULL`. [src: pitfalls]
- The MySQL-specific trailer `) ENGINE=InnoDB AUTO_INCREMENT=... DEFAULT CHARSET=utf8mb3;` defeats the regex `\)\s*;` in `ingest_lib.parse_sql_schema`. That regex needs the closing parenthesis followed only by whitespace and a semicolon. [src: pitfalls]

The recommended fix has two steps:
- For the schema, strip the `ENGINE=...;` trailer, keep just `CREATE TABLE name (cols);`, and concatenate all per-table `.sql` files into one `schema.sql`. [src: pitfalls]
- For the data, stream each `.txt` through a comma-delimited `csv.reader` with `doublequote=True`. Replace `\N` with an empty string, and write TSV with a header derived from the `CREATE TABLE`. [src: pitfalls]

The reference implementation, `~/data/genome_depot_enigma/preprocess.py`, handles 13 GB / 32 tables in ~5 minutes. [src: pitfalls]

## Pandas-Specific Issues: [gene_function_ecological_agora] Spark-Connect driver result-size …

This part of the report covers Spark-to-pandas pitfalls: result-size caps, driver memory exhaustion, a counterproductive Spark setting, notebook kernel timeouts, slow pandas loops and type problems. Most entries come from the gene_function_ecological_agora project, with a few general pandas rules. [src: pitfalls] See also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]] and [[entities/spark-connect]].

### Spark Connect result-size cap

Collecting very large joins with .toPandas() fails on the driver's result-size limit, and the report gives a workaround through Parquet staging. [src: pitfalls]

- In gene_function_ecological_agora, joining 1B-row tables filtered to >200K elements via broadcast, then calling .toPandas() on the Spark Connect result, hit spark.driver.maxResultSize = 1024 MB (megabytes). It raised a "Total size of serialized results" error. [src: pitfalls]
- The cap cannot be raised with SET spark.driver.maxResultSize at runtime, because the property is read-only after session start. [src: pitfalls]
- The workaround writes the result to MinIO with df.coalesce(N).write.mode("overwrite").parquet("s3a://cdm-lake/..."). It then reads it back with spark.read.parquet(path).toPandas(), which uses Spark Connect's Parquet streaming path and avoids the cap. [src: pitfalls]
- Reading with pyarrow.parquet.read_table(path) through s3fs is an alternative if pyarrow is configured. [src: pitfalls]
- Scale example: 218K Bacteroidota contigs × ~140 features/contig gives 30M+ rows × ~50 bytes serialized, about 1.5 GB. [src: pitfalls]
- The report calls this a standard pattern for genome-context cross-walks at >200 species. It was met in P4-D2 NB26b/c (per-cluster MGE (mobile genetic elements) machinery, atlas-wide) and NB26h/k (PUL (polysaccharide utilization locus) and mycolic gene neighborhoods at sampled scale). [src: pitfalls]

### Spatial-merge memory exhaustion

A Cartesian-product-then-filter merge in pandas can exhaust driver memory even after Spark has filtered to focal features. [src: pitfalls]

- 80K focal × 21K contigs × ~105 features/contig on average gave a merged DataFrame of ~24M rows × 9 columns, about a 9 GB working set. This ran out of memory on a 16 GB driver. [src: pitfalls]
- In NB26h (Bacteroidota PUL gene neighborhood), 723K focal × 210K contigs failed. Sampling to 309 species still ran out of memory at 80K × 21K. [src: pitfalls]
- The PSII (photosystem II) merge fit at 27K focal × 16K contigs (a 16M-row merge). PUL and mycolic analyses at full scale did not fit. [src: pitfalls]
- The report offers three remedies:
  - Process focal features in batches of ~10K and accumulate the aggregates. [src: pitfalls]
  - Apply the BETWEEN spatial filter in Spark and collect only per-feature aggregates. [src: pitfalls]
  - Reduce scope by sampling focal species or restricting to canonical-marker KOs (KEGG orthologs). [src: pitfalls]

### Disabling automatic broadcast

A defensive setting copied from earlier projects made a job hang. In NB10 (KO atlas), spark.sql.autoBroadcastJoinThreshold = -1 stalled a 13.7M × 18K join for 17+ minutes. [src: pitfalls] The job waited for a shuffle that never materialized. The small side (18,989 species_tax rows) was below the default 10MB broadcast threshold and would have been auto-broadcast at the default. [src: pitfalls] The report's workaround is to remove the disable, trust the optimizer, and use explicit F.broadcast(small_df) hints when it fails to detect the small table. [src: pitfalls] The general rule is that copied "defensive defaults" can be counterproductive, so configuration should be audited. [src: pitfalls]

### Kernel idle timeouts

KBase Data Lakehouse JupyterHub kernels time out after ~17–25 minutes without user activity. Long cells, such as 30+ minute Spark jobs or NB10b M22 attribution at 17M events, are killed silently with no error message. [src: pitfalls] The report recommends four steps:
- Convert the notebook to a .py script (jupytext). [src: pitfalls]
- Run it with nohup python3 -u from a terminal, not a JupyterHub kernel. [src: pitfalls]
- Write intermediate parquets at each stage. [src: pitfalls]
- Provide _finalize.py recovery scripts that resume from the intermediates. [src: pitfalls]

Timeouts hit NB10 (needing 10_finalize.py and 10_finalize2.py), NB10b (needing 10b_finalize.py), NB26b/c and NB28e (leaf_consistency build). [src: pitfalls]

### Pandas loops and explodes

- In NB26e Stage 6, iterrows with a per-row groupby lookup over 27K focal features × 218K contigs ran 30+ minutes without finishing. [src: pitfalls] A vectorized pd.merge on contig_id plus a boolean filter did the same work in ~10 seconds. [src: pitfalls] The report's rule is never to use iterrows() for >10K rows, and it states that the 1000× speedup is consistent across pandas use cases. [src: pitfalls]
- In NB28b (tree-based donor inference, M26), exploding 6.3M gain events × ~20 candidate-donor genera per event gave a 126M-row DataFrame of ~19 GB, which ran out of memory. [src: pitfalls]
- The workaround uses an algebraic identity. For family F × KO K with R_FK total recipient events, each genus G with K present is a candidate donor for R_FK − recipient_events_for_G. This is one join and a subtraction. [src: pitfalls] Stage 2b then ran in 142s instead of running out of memory. [src: pitfalls]
- The general rule is to look for sum-over-bins reformulations when an explode yields O(N×M) rows with bounded but large M. [src: pitfalls]

### General .toPandas() and type rules

.toPandas() pulls all data to the driver, which is slow for large results and can exhaust memory. The report advises doing filters, joins and aggregations in Spark first. [src: pitfalls] It recommends PySpark operations for intermediate steps. It reserves .toPandas() for local plotting, CSV export, or results of a few thousand rows. [src: pitfalls]

Two type pitfalls apply once data is in pandas:
- In cog_analysis, composite COG (clusters of orthologous groups) categories such as "LV" and "EGP" map to NaN (not a number) when missing from a description dictionary, and string operations on them fail. [src: pitfalls] The fix is to call pd.notna() or pd.isna() before slicing or other operations. [src: pitfalls]
- Numeric Spark columns can arrive in pandas as strings. [src: pitfalls] The report converts no_genomes, no_core and no_aux_genome with pd.to_numeric(errors='coerce'). [src: pitfalls]

## Pangenome: Missing Tables; Pangenome: API vs Direct Spark; Fitness Browser …

This part of the pitfalls report shows that billion-row pangenome joins are slow because the tables are unpartitioned [src: pitfalls] and that identifier formats differ between pangenome tables. [src: pitfalls] It also lists Fitness Browser schema details that a user must get right, including one case where the tables differ from the schema documentation. [src: pitfalls]

### Pangenome: table availability

As of 2026-02-11, `phylogenetic_tree` (species trees from core genes) was available. [src: pitfalls] `phylogenetic_tree_distance_pairs` (pairwise phylogenetic distances) was also available. [src: pitfalls] Three tables were not found: `pangenome_build_protocol` (build parameters, although a `protocol_id` column exists) [src: pitfalls], `genomad_mobile_elements` (plasmid/virus annotations) [src: pitfalls], and `IMG_env` (IMG environment metadata). [src: pitfalls]

### Pangenome: API versus direct Spark

The report recommends direct `spark.sql()` on the cluster when a query involves more than 1M rows, joins across large tables, or aggregations on billion-row tables, or when the representational state transfer (REST) application programming interface (API) keeps timing out. [src: pitfalls] In cog_analysis, joining gene → gene_genecluster_junction → gene_cluster → eggnog_mapper_annotations can be slow for species with more than 500 genomes. [src: pitfalls] The suggested fixes are to use direct Spark on JupyterHub, run separate queries per gene class, or pick species with 100-300 genomes. [src: pitfalls] For performance, use exact equality rather than `LIKE` patterns. [src: pitfalls]

### Identifier mismatch in phylogenetic distances

In cofitness_coinheritance, `phylogenetic_tree_distance_pairs` uses bare NCBI accessions (for example `GCA_001038305.1`). The `genome`, `gene` and `gene_genecluster_junction` tables use GTDB-prefixed identifiers (IDs) such as `GB_GCA_001038305.1`. Joining them without normalization gives zero matches. [src: pitfalls] The fix is to strip the `GB_` or `RS_` prefix, the first 3 characters, before joining. [src: pitfalls] After stripping, overlap was 100% for all tested species, including 399/399 for Koxy and 287/287 for Btheta. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Slow presence-matrix extraction

Joining `gene_genecluster_junction` (~1B rows) with `gene` (~1B rows) to build genome × cluster presence matrices takes 3-5 minutes per species. Neither table is partitioned by `gene_cluster_id` or `genome_id`, so each query scans the full table. [src: pitfalls] Profiling on Smeli (241 genomes, 6K target clusters) showed that tuning helps little:

- Without BROADCAST: ~300s per organism. [src: pitfalls]
- With `/*+ BROADCAST(tc), BROADCAST(tg) */` on the filter tables: ~274s, an 8% improvement. [src: pitfalls]
- Two-stage approach (filter junction first, then look up genome_ids): ~310s, no improvement. [src: pitfalls]
- `.toPandas()` on 1-2M result rows: <2s, so it is not the bottleneck. [src: pitfalls]

The report's recommendations are to:

- register target cluster and genome IDs as temporary views and use BROADCAST hints [src: pitfalls];
- cache extracted matrices as TSV and skip extraction on reruns [src: pitfalls];
- set `ExecutePreprocessor.timeout=3600` for `nbconvert --execute` [src: pitfalls];
- budget ~5 min per organism, so 11 organisms ≈ 55 min. [src: pitfalls]

The root cause is that `gene` and `gene_genecluster_junction` are unpartitioned parquet. Partitioning by `genome_id` (for `gene`) or `gene_cluster_id` (for the junction) would dramatically reduce scan time, but it requires rebuilding the KBase Data Lakehouse tables. [src: pitfalls] See also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

### Fitness Browser schema gotchas

Every Fitness Browser column is stored as a string, so cast before numeric comparisons. [src: pitfalls] `orgId` is case-sensitive: use `'Keio'`, not `'keio'`. [src: pitfalls] The `genefitness` table has 27M rows, so always filter at least by `orgId`. [src: pitfalls] See [[entities/fitness-browser]].

**Fitness modules.**
- The `fitbyexp_*` tables are long format (`expName, locusId, fit, t`), not pre-pivoted wide tables as the schema docs suggest. They equal a per-organism slice of `genefitness`, which the report advises using directly. [src: pitfalls]
- `keggmember` has `keggOrg, keggId, kgroup`, with no `orgId` or `locusId`. [src: pitfalls]
- To link genes to KEGG groups, join `besthitkegg` to `keggmember` on `keggOrg` and `keggId`, then left join `kgroupdesc` on `kgroup`. [src: pitfalls]
- `kgroupec` uses the column `ecnum`, not `ec`. [src: pitfalls]
- `seedclass` has `orgId, locusId, type, num` and stores Enzyme Commission (EC) numbers, not SEED subsystem categories. [src: pitfalls]
- `seedannotation` (`orgId, locusId, seed_desc`) is the table for functional descriptions. [src: pitfalls]

**Pathway capability and dependency.**
- The experiments table is `experiment`, not `exps`. Its columns are `expName`, `expGroup` and `condition_1`, not `name`, `Group` and `Condition_1`. [src: pitfalls]
- `expGroup` gives clean condition categories (carbon source, nitrogen source, stress, pH, temperature and others). Use it instead of pattern matching on `condition_1`. [src: pitfalls]
- `seedannotationtoroles` has only `seed_desc` and `seedrole`, with no `orgId` or `locusId`. [src: pitfalls]
- The SEED hierarchy join chain is `seedannotation` → `seedannotationtoroles` (on `seed_desc`) → `seedroles` (on `seedrole`). [src: pitfalls]
- The `seedroles` columns are `toplevel`, `category`, `subsystem` and `seedrole`, not `seed_role`, `seed_subsystem` or `seedroleId`. [src: pitfalls]

### Numerical pitfalls in fitness modules

For FastICA on fitness matrices, keep `n_components` ≤ 40% of `n_experiments`. Higher ratios often fail to converge, and each failed run reaches `max_iter`, which is very slow. [src: pitfalls] An organism with 150 experiments should use at most 60 components. [src: pitfalls] Pairwise cosine distance `1 - |cosine_similarity|` can come out slightly negative from floating-point precision. DBSCAN with `metric="precomputed"` rejects negative distances. [src: pitfalls] The fix is `np.clip(cos_dist, 0, 1, out=cos_dist)` before clustering. [src: pitfalls]

## Fitness Browser (kescience_fitnessbrowser) Pitfalls; Genomes (kbase_genomes) Pitfalls

This part of the report collects pitfalls from Fitness Browser (FB) projects and the kbase_genomes database. They cover ortholog extraction, module parameters, identifier mismatches, essential-gene handling and Spark query patterns. [src: pitfalls]

### Ortholog extraction and module annotation (fitness_modules)

Partial ortholog extraction and default parameters both distorted module results. The report recommends extracting bidirectional best-hit (BBH) pairs for all organisms in a cross-organism ortholog analysis, not a pilot subset. [src: pitfalls] Using 5-organism orthologs for a 32-organism analysis produced 6x fewer module families and missed all families spanning 5+ organisms. [src: pitfalls] The report explains that the ortholog graph gains transitive connections from each new organism, so partial extraction severely underestimates cross-organism conservation. [src: pitfalls]

Independent component analysis (ICA) weight distributions are intentionally heavy-tailed and non-Gaussian. The D'Agostino K² normality test therefore always rejects normality and picks a permissive z-threshold of 2.5, which lets 100-280 genes into each module. [src: pitfalls] The report recommends absolute weight thresholds instead (|Pearson r| ≥ 0.3 with the module profile, max 50 genes). It calls this the single most impactful parameter in the pipeline. [src: pitfalls] See [[concepts/construction-and-validity-of-cofitness-gene-groups]] for related module construction issues.

Enrichment settings also mattered. With min_annotated=3 and KEGG KOs (KEGG orthologs, ~1.2 genes per KO), only 8% of modules got any enrichment. Almost no KEGG term has 3+ genes in a single 5-50 gene module. [src: pitfalls] Lowering to min_annotated=2 (still valid with false discovery rate (FDR) correction) and adding PFam domains (814 terms with 2+ genes) alongside TIGRFam (88 terms) raises module annotation from 8% to 80%. [src: pitfalls]

### Identifier mismatches (conservation_vs_fitness)

FB protein sequences at fit.genomics.lbl.gov/cgi_data/aaseqs use RefSeq-style locus tags for some organisms, such as ABZR86_RS00005 for Dyella79. The FB gene table uses the original annotation tags, such as N515DRAFT_0001. [src: pitfalls] If you build DIAMOND databases from aaseqs and join the hit locusIds back to the gene table, the join can silently produce zero matches. [src: pitfalls] Dyella79 had 0% overlap between aaseqs and gene-table locusIds, while other organisms had >94% overlap. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Essential genes

FB has no direct essentiality field, so essential genes must be inferred. After checking all 45 tables in kescience_fitnessbrowser, the project found no explicit essentiality column, insertion count or "has fitness data" flag. [src: pitfalls] The gene.type column encodes feature type (1=CDS, 5=pseudo, 7=rRNA, 2=tRNA), not essentiality. [src: pitfalls] The report's workaround is to compare gene-table type='1' genes against genefitness. Genes absent from genefitness had no viable transposon mutants, and this is an upper bound on true essentiality. [src: pitfalls]

Querying only genefitness misses ~14.3% of protein-coding genes. These are essential genes with no transposon insertions and so no genefitness entries. [src: pitfalls] The report says these genes are 82% core. [src: pitfalls] It concludes that any fitness-versus-conservation analysis must include them or acknowledge that the most extreme fitness category is missing. [src: pitfalls]

The "% core" denominator also matters. In conservation_fitness_synthesis, essential genes were 82% core when all genes (including unmapped) were used, versus 86% with mapped genes only. [src: pitfalls] Inconsistent denominators caused a critical review issue, because figures showed 86%/78% while prose said 82%/66%. [src: pitfalls]

### Spark and pandas performance

Spark `LIMIT N OFFSET M` pagination re-scans all rows up to the offset on each query. [src: pitfalls] Extracting cluster representative FASTAs across 154 clades with paginated queries of 5000 rows per batch was orders of magnitude slower than one query per clade. [src: pitfalls] Because gene_cluster is partitioned by gtdb_species_clade_id, a single filtered query per clade is fast. The report advises paginating only when the result would exceed memory. [src: pitfalls] See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

In core_gene_tradeoffs, filtering a 961K-row DataFrame with a row-wise apply over (orgId, locusId) set membership was extremely slow. An inner merge on those keys gave the same result in seconds instead of minutes. [src: pitfalls] In module_conservation, merging module_families.csv with family_annotations.csv on familyId can create n_modules_x and n_modules_y column collisions. Explicit suffixes=('_obs', '_annot') avoid the ambiguity. [src: pitfalls]

### Workflow slip

In fitness_effects_conservation, the /submit reviewer subprocess can write REVIEW.md to projects/{id}/projects/{id}/REVIEW.md instead of projects/{id}/REVIEW.md. This happens if it resolves the path relative to its own working directory instead of the repository root. [src: pitfalls]

### Genomes (kbase_genomes)

All primary keys in kbase_genomes are CDM UUIDs. The name table maps external gene IDs (identifiers) to CDM UUIDs. [src: pitfalls] Most junction tables have ~1 billion rows, and the report warns never to query them without filters. [src: pitfalls]

## Python / Pandas Pitfalls; Skill / Workflow Pitfalls

This part of the report documents Python, pandas, Spark and workflow errors that gave wrong or stalled results, often with no error message. Examples include a 41,059 versus 7,084 orphan count [src: pitfalls], identical strict and relaxed features [src: pitfalls], and empty notebook outputs. [src: pitfalls] Each comes from a named project and carries a recommended fix.

### Pandas and data-handling errors

A boolean-flag error in essential_genome silently gave a wrong count. A left merge leaves NaN (not a number) in unmatched rows, and `fillna(False)` yields object dtype instead of boolean. [src: pitfalls] Bitwise NOT (`~`) on an object column then gives silently wrong results instead of boolean negation. [src: pitfalls] In that project the error gave an orphan essential gene count of 41,059 (total essentials) instead of 7,084 (actual orphans), with no error message. [src: pitfalls] The workaround is to cast to bool after `fillna(False)`. [src: pitfalls]

In enigma_contamination_functional_potential, the p-value correction can miss columns. Correction that targets only column names ending in `_p` misses names such as `adj_cov_p_contamination` and `adj_frac_p_contamination`. [src: pitfalls] The report recommends detecting p-value columns by substring pattern, excluding derived q-value columns, or using an explicit allowlist before BH-FDR (Benjamini-Hochberg false discovery rate) correction. [src: pitfalls]

### Spark and runtime limits

Large extractions and repeated joins can fail or stall (see also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]]).

- **Driver result size (ecotype_env_reanalysis).** Extracting *K. pneumoniae* gene-cluster memberships (250 genomes × ~5,500 genes per genome) through `gene` JOIN `gene_genecluster_junction` exceeds Spark's 1GB default `spark.driver.maxResultSize`. [src: pitfalls] The query succeeds in Spark but fails when results are collected to the driver. [src: pitfalls] For species with >200 genomes, the report recommends batches of 50-100 genomes, concatenated afterwards, or a larger `spark.driver.maxResultSize`. [src: pitfalls] The per-species extraction script catches the error with try/except and moves to the next species. [src: pitfalls]
- **Duplicate heavy joins (enigma_contamination_functional_potential).** Separate heavy joins and aggregations over `eggnog_mapper_annotations` for each mapping mode can stall notebooks on large tables. [src: pitfalls] The fix is to precompute per-clade total, defense, mobilome and metabolism annotation totals once. Genus feature fractions are then derived in pandas, which keeps the modes independent and cuts duplicate Spark work. [src: pitfalls]
- **Bootstrap cost (NB03).** Bootstrap confidence intervals (CI) across several outcomes and model families can slow NB03 when bootstrap counts are too high. [src: pitfalls] The report recommends moderate sizes such as 250-400, fixed seeds, and CIs only for key coefficients or endpoints. [src: pitfalls]

### Invalid sensitivity analysis and taxonomy resolution

In NB02 of enigma_contamination_functional_potential, `feats_relaxed = feats_strict.copy()` gives numerically identical strict and relaxed outputs. This invalidates any mapping-mode sensitivity conclusion, because the modes are no longer built independently. [src: pitfalls] The proposed fix is to precompute clade-level annotation counts once on the union of clades and aggregate them separately per mode. [src: pitfalls]

ENIGMA taxonomy in `ddt_brick0000454` currently holds only Domain through Genus levels. [src: pitfalls] A species-level bridge built directly on it will either fail or silently reuse genus-level mappings while appearing higher resolution. [src: pitfalls] The report advises checking the available levels first. It then offers two routes. One is an explicit species-proxy mode using unique genus-to-single-GTDB-clade mappings, with the mapped-coverage loss reported. [src: pitfalls] The other is a switch to sources that resolve species or strains, namely metagenomes or an ASV (amplicon sequence variant) reclassification pipeline. [src: pitfalls]

### AlphaEarth pooling

In env_embedding_explorer, the pooled geographic distance–embedding distance curve shows a 2.0x near-versus-far ratio, but it blends two populations. [src: pitfalls] Environmental samples show 3.4x, described as a strong signal. [src: pitfalls] Human-associated samples show 2.0x, described as a weak signal. [src: pitfalls] The report says the pooled curve underestimates the true geographic signal. [src: pitfalls] It recommends stratifying AlphaEarth analyses by environment category, at minimum environmental versus human-associated. When embeddings stand in for environment, as in ecotype analysis, it suggests excluding human-associated samples entirely. [src: pitfalls] See [[entities/alphaearth-environmental-embeddings]].

### Project layout and documentation

In cofitness_coinheritance, computed phi coefficients and summary tables went into `data/results/` instead of flat in `data/`. [src: pitfalls] The BERIL pattern keeps all data files flat in `data/`, with subdirectories only for extracted data categories, so `data/results/` is non-standard. [src: pitfalls]

The `/synthesize` skill told the user to write detailed findings into README.md. That conflicts with the observatory's three-file structure and makes the README too long. [src: pitfalls] The three files are README (a concise overview with links), RESEARCH_PLAN (hypothesis and approach), and REPORT (full findings and interpretation). essential_genome is the canonical example. [src: pitfalls] The corrected workflow puts these in REPORT.md: Key Findings, Results, Interpretation, Literature Context, Limitations, Future Directions, Visualizations and Data Files. [src: pitfalls] README.md keeps a Status line, an Overview paragraph and Quick Links to RESEARCH_PLAN, REPORT and references. It also carries metadata for Data Sources, Structure, Reproduction, Dependencies and Authors. [src: pitfalls]

### Codex CLI reviewer

Running `codex exec` in a restricted sandbox can fail with DNS or connection errors, such as `chatgpt.com` resolution failures, because network egress is disabled. [src: pitfalls] The report recommends running with network-enabled permissions and first doing a minimal smoke test, `codex exec "Reply with exactly: ok"`, before rerunning the full reviewer command. [src: pitfalls] Long inline system prompts, for example from large shell substitutions, can make `codex exec` unstable or fail intermittently. [src: pitfalls] Compact CLI prompts that point to an on-disk prompt file and write to `projects/{id}/REVIEW.md` have been more reliable in BERIL submit workflows. [src: pitfalls]

### Environment and notebooks

In ecotype_analysis, the `data` directory was a symlink to a local Mac path, `/Users/paramvirdehal/...`. That path does not exist on JupyterHub. [src: pitfalls] There, `os.makedirs(path, exist_ok=True)` raises `FileExistsError`, because the symlink exists but its target is missing. [src: pitfalls] The report recommends removing a broken symlink first with `if os.path.islink(path): os.remove(path)`. Alternatively, avoid committing symlinks by using relative paths and ignoring data directories in `.gitignore`. [src: pitfalls]

In env_embedding_explorer, prototyping as Python scripts led to notebooks committed with empty output cells, which defeats their role as audit trail and methods documentation. [src: pitfalls] `/synthesize` reads notebook outputs to extract results, and the `/submit` reviewer checks them to verify claims. [src: pitfalls] The report states that empty notebooks fail result extraction, reviewer verification, and readers who follow the analysis without rerunning it. [src: pitfalls] The fix is to execute notebooks before committing, with `jupyter nbconvert --to notebook --execute --inplace` or Restart & Run All. Expensive steps such as UMAP (uniform manifold approximation and projection) can load cached results when the file exists. [src: pitfalls] See also [[concepts/notebook-provenance-and-session-isolation-in-agent-assisted-analysis]].

## Skill / Workflow Pitfalls: [aromatic_catabolism_network] Keyword-based gene …

This part of the pitfalls report covers NaN embeddings and slow UMAP runs in env_embedding_explorer, and GapMind and BacDive table handling errors. [src: pitfalls] It also covers keyword gene misclassification, a biased NaCl-importance threshold, and a Claude Code output-suppression bug. [src: pitfalls]

### AlphaEarth embeddings and UMAP (env_embedding_explorer)

In env_embedding_explorer, 3,838 of 83,287 genomes (4.6%) have NaN (not a number) in at least one of the 64 embedding dimensions. [src: pitfalls] NaN values can make UMAP (uniform manifold approximation and projection), cosine distance and other operations fail or silently return NaN. [src: pitfalls] The fix is to filter with `~df[EMB_COLS].isna().any(axis=1)` before any embedding computation. This reduces the dataset from 83,287 to 79,449 genomes. [src: pitfalls] See also [[entities/alphaearth-environmental-embeddings]].

Cosine-metric UMAP on 83K genomes with 64 dimensions ran for more than 60 minutes without finishing on a single-CPU JupyterHub pod. [src: pitfalls] The report states that the cosine metric needs O(n^2) pairwise precomputation. [src: pitfalls] It recommends L2-normalizing the embeddings and then using the Euclidean metric. It states that Euclidean distance is monotonically related to cosine distance for normalized vectors, so the UMAP topology is equivalent. [src: pitfalls] Fitting UMAP on a 20K subsample and then transforming the full dataset cut runtime from more than 60 minutes to about 7 minutes. [src: pitfalls]

### Plotly static export

kaleido is the Plotly static image export library. [src: pitfalls] Version 1.x needs Google Chrome, which headless JupyterHub pods lack, so `fig.write_image()` fails with `ChromeNotFoundError`. [src: pitfalls] The fix is `pip install kaleido==0.2.1`, which uses bundled Chromium and works on headless systems. [src: pitfalls]

### GapMind handling (pangenome_pathway_geography)

The initial analysis searched for a GapMind score_category 'present' that does not exist. It therefore counted exactly 80 pathways for every species, with 0% present. [src: pitfalls] GapMind has exactly 80 pathways, and each genome-pathway pair has multiple rows, one per step or component. [src: pitfalls] The score categories are complete, likely_complete, steps_missing_low, steps_missing_medium and not_present, not a binary present flag. [src: pitfalls] The correct approach takes the best score for each genome-pathway pair before aggregating to species level. [src: pitfalls] See [[entities/gapmind]] and [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

A separate identifier problem affects joins. The `kbase.ke_pangenome.gapmind_pathways` table stores genome IDs (identifiers) without the GTDB `RS_` or `GB_` prefix, for example `GCF_001307155.1`. The pangenome `genome` table uses the prefixed form, for example `RS_GCF_001307155.1`. [src: pitfalls] A direct equality match therefore returns zero rows. [src: pitfalls] The report recommends stripping the prefix before matching, or using a fallback chain. [src: pitfalls] Its code tries the original ID, then the ID with RS_ and GB_ removed, then a substring search on the accession. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Keyword gene classification (aromatic_catabolism_network)

Keyword matching on RAST function descriptions misclassifies enzymes with non-obvious names. [src: pitfalls] ACIAD1710 is 4-carboxymuconolactone decarboxylase (EC 4.1.1.44, Enzyme Commission number) and a core pca pathway enzyme. [src: pitfalls] It was classified as "Other" because the keyword list included "muconate" but not "muconolactone". [src: pitfalls] Co-fitness analysis correctly recovered pcaC, with r=0.978 with the Aromatic pathway. [src: pitfalls] The report recommends using keywords as a first pass and validating them with co-fitness correlations. It also recommends testing classifiers against known category members and adding missing synonyms. [src: pitfalls] See [[concepts/construction-and-validity-of-cofitness-gene-groups]].

### Notebook editing

Replacing a code cell with `NotebookEdit` can yield a cell without the required `outputs` and `execution_count` fields. `jupyter nbconvert --execute` then fails with `NotebookValidationError: 'outputs' is a required property`. [src: pitfalls] The report recommends checking notebook JSON validity after editing. It also recommends setting missing code-cell `outputs` to an empty list and `execution_count` to None. [src: pitfalls]

### Claude Code `claude -p` output suppression

In Claude Code version 2.1.47, running `claude -p` in the foreground, or backgrounded with `wait`, suppresses all Bash output. This includes `echo` statements placed before the call. [src: pitfalls] The process still runs and produces correct output, but the Bash tool discards it. The report says this worked correctly in 2.1.45. [src: pitfalls] The workaround is to launch `claude -p` in the background with file redirection, return immediately, and read the output file in a separate Bash call. [src: pitfalls] Using `wait` on the PID triggers the same suppression. [src: pitfalls]

### NaCl importance threshold (counter_ion_effects)

Defining NaCl (sodium chloride) importance as `n_sick >= 1` is biased by the number of NaCl experiments per organism. Here n_sick >= 1 means at least one NaCl experiment with fit < -1. [src: pitfalls] Synechococcus elongatus (SynE) has 12 NaCl dose-response experiments at 0.5–250 mM. It flags 32.6% of genes as NaCl-important, 3× higher than the next organism. [src: pitfalls] Unequal experiment counts inflate cross-condition overlap statistics, and SynE shows 88.6% metal–NaCl shared-stress. [src: pitfalls] Excluding SynE lowers overall metal–NaCl overlap from 39.8% to 36.7%. The report calls this modest but worth documenting. [src: pitfalls] For comparisons with unequal experiment counts, the report recommends one of two options. The first is `n_sick >= 2` or `mean_fit < threshold`. The second is reporting results with and without outlier organisms. [src: pitfalls]

### BacDive utilization values

BacDive `metabolite_utilization.utilization` holds four values: `+` (can utilize), `-` (cannot utilize), `produced` (organism produces it) and `+/-` (variable or ambiguous). [src: pitfalls] Treating the field as binary inflates counts. For P. fluorescens, indole has 60 "produced" entries and only 1 actual utilization test. [src: pitfalls] Computing `pct_positive` without excluding `produced` and `+/-` entries gives incorrect species-level utilization rates. [src: pitfalls] The report's method divides `+` tests by the total of `+` and `-` tests. [src: pitfalls] It also recommends tracking positive, negative, produced and ambiguous counts separately. [src: pitfalls] See [[entities/bacdive]].

## NMDC (nmdc_arkin) Pitfalls: [nmdc_community_metabolic_ecology] abiotic_features Column …

This part of the report lists identifier, schema and type pitfalls in the nmdc_arkin collection of the KBase Data Lakehouse and in the metal_specificity project. Several cause failed queries or silent data loss. [src: pitfalls] Each comes with a fix or a detection rule. See also [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Identifiers and joins in nmdc_arkin

Classifier and metabolomics tables have separate file_id namespaces, so they link only through biosample sample_id. [src: pitfalls]

- metabolomics_gold, kraken_gold, centrifuge_gold and gottcha_gold use file_id and file_name as primary identifiers, not sample_id. [src: pitfalls] Queries with `WHERE sample_id = ...` or `COUNT(DISTINCT sample_id)` raise `AnalysisException: UNRESOLVED_COLUMN` and stop notebook execution. [src: pitfalls] The report recommends file_id as the join key for these tables within their respective file namespaces. [src: pitfalls]
- Joining the classifier tables directly to metabolomics_gold on file_id always returns zero rows, because the two sets of file_id values do not overlap. [src: pitfalls] Classifier files use `nmdc:dobj-11-*` (metagenomics workflow outputs). [src: pitfalls] Metabolomics files use `nmdc:dobj-12-*` (metabolomics workflow outputs). [src: pitfalls]
- Outputs for the same biosample can only be linked through the biosample sample_id, for example `nmdc:bsm-11-*`. [src: pitfalls] The abiotic_features table uses sample_id as its primary key. [src: pitfalls]
- The bridge is `kbase.nmdc_arkin.omics_files_table`, with 385,562 rows (confirmed). [src: pitfalls] It has file_id, sample_id, study_id, workflow_type and file_type columns. [src: pitfalls] NB02 of nmdc_community_metabolic_ecology scans systematically for tables that have both file_id and sample_id. [src: pitfalls]

### Taxonomy and metabolomics table layouts

- taxonomy_features has no sample_id or file_id column. Its columns are numeric NCBI taxon IDs such as 7, 11, 33 and 34. [src: pitfalls] Selecting sample_id from it fails immediately. [src: pitfalls] The report describes it as a pivoted matrix whose rows are likely samples and whose columns are taxon abundances. [src: pitfalls]
- For tidy-format joins, the report recommends the classifier tables kraken_gold, centrifuge_gold and gottcha_gold. They have file_id, rank, name/label and abundance columns. [src: pitfalls]
- metabolomics_gold has kegg (string KEGG compound ID), chebi (double ChEBI ID), name (string compound name), and inchi, inchikey and smiles. [src: pitfalls] Column names with spaces, such as `Molecular Formula` and `Area`, need backtick quoting. [src: pitfalls]
- annotation_terms_unified is a gene-annotation lookup (COG, EC, GO and KEGG terms). It cannot serve as a metabolite compound lookup. [src: pitfalls] Here COG means clusters of orthologous groups, EC means Enzyme Commission, and GO means Gene Ontology. [src: pitfalls]

### abiotic_features column naming and missing values

- Most numeric columns use a `_has_numeric_value` suffix, for example `annotations_tot_org_carb_has_numeric_value`. [src: pitfalls] The pH column, `annotations_ph`, has no suffix. The report says depth and temperature do have the suffix. [src: pitfalls] Using a bare name where the suffix is required raises `UNRESOLVED_COLUMN`. [src: pitfalls]
- `annotations_water_content` does not exist. [src: pitfalls] The report recommends `annotations_diss_org_carb_has_numeric_value` and `annotations_conduc_has_numeric_value` instead. [src: pitfalls]
- Numeric columns are already double type, so CAST is unnecessary but harmless. [src: pitfalls]
- The table stores `0.0` rather than NULL for unmeasured variables. The report recommends replacing zeros with NaN (not a number) before analysis. [src: pitfalls]
- The schema includes sample_id, annotations_ph, and temperature, depth, maximum-depth and minimum-depth fields. [src: pitfalls] It also has fields for total organic carbon, total nitrogen content, dissolved organic carbon, conductance, dissolved oxygen, ammonium, total phosphorus, soluble reactive phosphorus and carbon-nitrogen ratio. [src: pitfalls] Further fields cover chlorophyll, calcium, magnesium, potassium, manganese and sample size. [src: pitfalls]

### Spark Connect and pandas

A pandas DataFrame made with `.toPandas()` on a Spark Connect DataFrame has columns backed by PyArrow ChunkedArray objects. Passing it back to `spark.createDataFrame()` raises `TypeError: Cannot convert pyarrow.lib.ChunkedArray to pyarrow.lib.Array`. [src: pitfalls] This blocks the common pattern of pulling data to pandas, filtering it and registering it as a Spark temporary view. [src: pitfalls] The report recommends skipping the roundtrip. Keep filtering and joining in structured query language (SQL) with subqueries and the original table names, and use the full bridge table name directly rather than a temporary view. [src: pitfalls] If a small DataFrame must go back to Spark, convert each column first with `df[col] = df[col].tolist()`. [src: pitfalls] See [[entities/spark-connect]].

### metal_specificity pitfalls

**locusId types.** Fitness matrices from `fitness_modules/data/matrices/` use integer locusId indices (for example `206065`). Metal Atlas `metal_important_genes.csv` stores them as strings. [src: pitfalls] A pandas index lookup then silently treats the gene as absent and raises no error. [src: pitfalls] This completely dropped DvH (495 metal-important genes) and Btheta (276 genes) from the analysis without warning. [src: pitfalls] The loop reported "SKIPPED (no fitness matrix or no non-metal experiments)" even though the matrix existed. [src: pitfalls] The fix is to convert both sides to strings before matching. To detect the problem, compare organism counts in the output with the expected input. [src: pitfalls]

**z-score normalization.** Per-module z-scores across all experiments gave max |z| < 2.0 for metal experiments when metals are a small fraction of experiments, for example 12/176 for MR1. The non-metal majority dominates the standard deviation. [src: pitfalls] Metal Atlas NB05 avoided this with pre-computed z-scores from `metal_modules.csv`, standardized per module across all experiments rather than per experiment type. [src: pitfalls] Recomputing z-scores from raw `module_conditions.csv` activities does not reproduce the same responsiveness threshold. The report recommends using the upstream pre-computed z-scores. [src: pitfalls]

## NMDC (nmdc_arkin) Pitfalls: [neon_mag_functional_discovery] Per-gene NMDC annotation …

This part of the report covers three pitfalls. BacDive and GTDB species names often fail to match. Reused variable names in a notebook can mislabel statistical results. NMDC per-gene annotation tables cover only part of the workflows, and that gap is not random. [src: pitfalls]

### BacDive species names versus GTDB species names

GTDB, the taxonomy behind the pangenome, differs from the LPSN/DSMZ taxonomy that BacDive uses. GTDB adds suffixes such as `_A` and `_B`, splits genera, and draws species boundaries differently. [src: pitfalls] In bacdive_metal_validation, direct species-name matching captured 34.5% of strains. Stripping the GTDB suffixes added another 8.9%, for 43.4% in total. [src: pitfalls] The report says the remaining 56.6% are different species concepts or genera not yet in GTDB r214. [src: pitfalls]

The recommended fix is two-pass matching: exact species name first, then base name with the GTDB suffix stripped. For higher coverage, match the GCA genome accession to the pangenome `genome_id`. That route needs handling of the `GB_` prefix and the version suffix. [src: pitfalls]

Matching shrinks the usable sample. BacDive has 31 strains tagged cat3=#Heavy metal contamination, but only 10 match pangenome species that have metal tolerance scores. [src: pitfalls] The report advises computing post-matching sample sizes and power before interpreting results. It also says plans should not assume the full BacDive category size will survive matching. [src: pitfalls]

### Overwritten variables in sequential tests

In metal_specificity, sequential tests reused generic names such as `odds, p = stats.fisher_exact(table)`. The second Fisher exact test (H1d) overwrote the first (H1c), and a later summary cell printed the wrong values under the wrong labels. [src: pitfalls] The fix is a descriptive variable name for each test. [src: pitfalls]

### NMDC per-gene annotation coverage

NMDC per-gene tables do not cover every workflow. These are annotation_kegg_orthology (1.83 B rows), pfam_annotation_gff (2.68 B rows) and annotation_enzyme_commission (1.23 B rows). Not every MetagenomeAnnotation workflow in functional_annotation_agg appears in them. [src: pitfalls] On NEON, only 1,799 of 3,137 MetagenomeAnnotation workflows (57%) have rows in annotation_kegg_orthology. [src: pitfalls]

The 43% gap is non-random. It correlates strongly with habitat and genus. [src: pitfalls] Per-gene KO (KEGG ortholog) coverage by group:

| NEON group | Per-gene KO coverage |
|---|---|
| Surface-water cyanobacteria (Planktothrix, Dolichospermum, Rubrivivax) | 100% [src: pitfalls] |
| Benthic generalists (Ferruginibacter, Flavobacterium, UBA953) | ~85% [src: pitfalls] |
| Soil acidobacteria (Sulfotelmatobacter, Palsa-465, Palsa-1447) | ~30% [src: pitfalls] |
| Soil cultured genera (Mycobacterium, Bradyrhizobium, Acidoferrum) | ~10% [src: pitfalls] |
| Soil unculturable / novel (Acidocella, BOG-234, Pseudolabrys, Pseudonocardia, Reyranella) | 0% [src: pitfalls] |

Any per-MAG (metagenome assembled genome) functional analysis that needs the per-gene tables silently drops the zero-coverage genera. This applies to the `members_id` → `gene_id` chain. [src: pitfalls] In neon_mag_functional_discovery NB04b, the H4 cohort of 246 MAGs collapsed to 73 MAGs across 19 genera, biased toward water habitats. [src: pitfalls] The KEGG module enrichment that followed was driven heavily by cyanobacterial photosystem modules. The report calls this partly real biology and partly a habitat-skewed cohort. [src: pitfalls]

### Recommended practice

- Query coverage per study and per habitat before staking a hypothesis on per-MAG resolution. Treat downstream effect sizes as cohort-conditional. [src: pitfalls]
- Prefer `functional_annotation_agg` in `nmdc_metadata` for sample-level or workflow-level KO, COG (clusters of orthologous groups) and Pfam analysis. It covers essentially every workflow with annotation output. [src: pitfalls]
- Use `functional_annotation_agg` for habitat-versus-chemistry analysis, PCoA (principal coordinates analysis) and PERMANOVA (permutational multivariate analysis of variance), where per-gene resolution is not needed. [src: pitfalls]
- Use per-gene tables only when per-MAG resolution is essential, and report the cohort attrition explicitly. [src: pitfalls]
- Do not assume `pfam_annotation_gff` fills the gap left by `annotation_kegg_orthology`. [src: pitfalls]

Confirming Pfam coverage is hard. Bounded queries on a single `workflow_run_id` against either per-gene table time out at scan-only cost. The tables have 2–3 B rows, and `workflow_run_id` does not partition-prune cleanly through `WHERE … IN (…)`. [src: pitfalls] Confirming Pfam coverage for a specific workflow set requires JupyterHub PySpark, not `nbconvert`-bounded execution. [src: pitfalls] The report supplies a JupyterHub SQL (structured query language) check. It counts distinct NEON annotation workflows with per-gene KO data by joining staged NEON workflow IDs (identifiers) to annotation_kegg_orthology. The check compares that count with the total number of MetagenomeAnnotation workflows in workflow_execution_set. [src: pitfalls]

## BacDive (kescience_bacdive) Pitfalls; Additional Spark / Python Pitfalls …

This part of the report records pitfalls from plant_microbiome_ecotypes and cf_formulation_design: join-type mismatches, Spark result limits, query formats that return nothing, schema quirks and assay-design limits. [src: pitfalls]

### BacDive join types and Spark result size (plant_microbiome_ecotypes)

In plant_microbiome_ecotypes, BacDive `sequence_info.bacdive_id` is INT (integer) but `isolation.bacdive_id` is STRING. [src: pitfalls] A direct join returns zero rows because Spark does not implicitly cast across INT/STRING types. [src: pitfalls] The report's fix is `CAST(si.bacdive_id AS STRING) = iso.bacdive_id` for cross-table joins. [src: pitfalls] See also [[concepts/join-key-validity-and-identifier-format-mismatches]].

The 93M row `eggnog_mapper_annotations` table can produce results above `spark.driver.maxResultSize` (1024 MiB) when species×OG (ortholog group) matrices are collected to the driver. [src: pitfalls] The report recommends computing Fisher test contingency counts server-side in Spark SQL (structured query language) and collecting only the summary counts. [src: pitfalls] See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

### Python and annotation-table problems

`import statsmodels.api as sm` fails on Python 3.13 because a graphics import chain triggers an ImportError. [src: pitfalls] The report's workaround is `import statsmodels.formula.api as smf`, which avoids that import path. [src: pitfalls]

Querying `bakta_pfam_domains` with Pfam IDs such as 'PF00771' returned 0 hits across all 11 domains tested. [src: pitfalls] The report suggests, as a hypothesis, that the table may use domain names or versioned accessions such as `PF00771.1`, or may need different join logic. [src: pitfalls] The correct query format stayed unresolved. [src: pitfalls] The report's checklist says to verify Pfam accessions against InterPro/UniProt rather than assume them from names. [src: pitfalls] It also says to search the eggNOG PFAMs column by domain name, not accession. [src: pitfalls] See [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]].

Using `gapmind_pathways` with `sequence_scope = 'core'` for broad taxonomic comparisons gave 0% completeness across all compartments. [src: pitfalls] The report says the core-level threshold is too stringent for genus-level or cross-species comparisons, where pathway genes may not be universally present. [src: pitfalls] It recommends max-aggregation at the genus level instead. [src: pitfalls] See [[entities/gapmind]].

### cf_formulation_design: assay and data limits

In the PROTECT Gold tables, `fact_pairwise_interaction` and `fact_carbon_utilization` contain identical values (correlation = 1.0, mean difference = 0.0). [src: pitfalls] Endpoint OD (optical density) data do not capture co-culture metabolic interactions. Only the RFU-based competition assay gives pairwise interaction effects. [src: pitfalls] Per-substrate co-culture analysis is therefore impossible from endpoint OD data. [src: pitfalls] NB08 found this and pivoted to using only the RFU-based competition assay. [src: pitfalls]

Cross-species codon usage bias (CUB) comparisons, such as PA versus commensals, are confounded by GC content variation (31–73%). [src: pitfalls] The report says organisms with extreme GC composition have inflated CUB scores regardless of growth optimization. [src: pitfalls] It holds that CUB is only meaningful within species or across species with similar GC content. [src: pitfalls] For cross-species growth rate comparisons, it recommends lab growth data as ground truth. [src: pitfalls]

PA14 (ExoU+, Pel-only, ladS mutant) represents <5% of CF (cystic fibrosis) PA isolates by virulence genotype. [src: pitfalls] CF PA is 94% ExoS+ and 92% Pel+Psl+ (PAO1-like). [src: pitfalls] PA14 inhibition assays therefore test the formulation against a minority variant. [src: pitfalls] The report recommends validating PA14-based results against ExoS+ strains before generalizing to CF. [src: pitfalls]

Amino acid catabolism is identical across ExoU+ and ExoS+ strains, with no FDR-significant differences. [src: pitfalls] The report therefore expects the competitive exclusion mechanism to transfer, but says direct validation is needed. [src: pitfalls]

### Schema notes for pangenome and GenomeDepot tables

These notes concern the pangenome schema in the KBase Data Lakehouse (see [[entities/kbase-ke-pangenome]]).

- `gene_cluster` has `gtdb_species_clade_id`, not `clade_name`. [src: pitfalls]
- `gapmind_pathways` has `clade_name`. [src: pitfalls]
- `gene` has only `gene_id` and `genome_id`, with no species/clade column. [src: pitfalls]
- `eggnog_mapper_annotations` uses `query_name` as its identifier, and this maps to `gene_cluster_id` in `gene_cluster`. [src: pitfalls]
- `bakta_annotations` joins to `gene_cluster` directly on `gene_cluster_id`. [src: pitfalls]
- Gene-to-genome mapping goes through `gene_genecluster_junction`, joined to `gene` on `gene_id`. [src: pitfalls]

In `protect_genomedepot`, `browser_genome` has no `species` column, so species filtering requires a join through `browser_taxon`. [src: pitfalls] The report's query joins `browser_gene.genome_id` to `browser_genome.id`, then `browser_genome.taxon_id` to `browser_taxon.id`. [src: pitfalls]

### Psl gene detection

In `protect_genomedepot` and `phagefoundry_paeruginosa_genome_browser`, pslA-pslO genes are rarely annotated with canonical gene names. Only the PAO1 reference genome has them. [src: pitfalls] The pangenome `bakta_annotations` has better coverage, but pslA/pslG/pslK are still sparse. [src: pitfalls] The report recommends KEGG orthologs K20997–K21005 via `eggnog_mapper_annotations`, which give ~95% prevalence versus <1% by gene name alone. [src: pitfalls] See [[entities/phagefoundry]].

### Session and database checks

If the `.env` token fails, the report says to check `~/.berdl_kbase_session` for a fresh authentication token. [src: pitfalls] It also says to check all databases that share a project prefix, for example both GenomeDepot and strain_modelling for PhageFoundry. [src: pitfalls] See [[concepts/lakehouse-namespace-migration-tenancy-and-authentication]].

## kbase_ke_pangenome; kbase_msd_biochemistry

This part of the report lists practical pitfalls for the pangenome tables (kbase_ke_pangenome, see [[entities/kbase-ke-pangenome]]) and the ModelSEED biochemistry tables (kbase_msd_biochemistry) in the KBase Data Lakehouse. They cover identifier formats and join keys, table scale, coverage and orphan rows, and missing mappings. [src: pitfalls]

### Pangenome: identifiers and join keys

Identifier formats and join keys cause the most silent errors; see also [[concepts/join-key-validity-and-identifier-format-mismatches]]. Species clade IDs look like `s__<Genus_species>--<RS_GCF_XXXXXXXXX.X | GB_GCA_XXXXXXXXX.X>`. [src: pitfalls] The `--` is parsed as a SQL line comment inside `IN (...)` clauses, so the report recommends `LIKE 's__Genus_species%'` patterns instead of equality or `IN`. [src: pitfalls] Genome IDs use `RS_GCF_XXXXXXXXX.X` for RefSeq or `GB_GCA_XXXXXXXXX.X` for GenBank, and they match by exact equality only. [src: pitfalls]

Annotation tables join at cluster level, not gene level. `eggnog_mapper_annotations.query_name` joins to `gene_cluster.gene_cluster_id`, not to `gene.gene_id`. [src: pitfalls] The Bakta and InterProScan tables also join on `gene_cluster_id`, because their annotations sit at cluster-representative level. [src: pitfalls]

### Pangenome: scale

Several tables are too large to scan in full. The report advises always pre-filtering by `gtdb_species_clade_id` (or `genome_id`) before joining. [src: pitfalls] See also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]]. Approximate row counts:

| Table | Rows |
|---|---|
| `gene` | ~1B [src: pitfalls] |
| `gene_genecluster_junction` | ~1B [src: pitfalls] |
| `interproscan_domains` | ~833M [src: pitfalls] |
| `bakta_db_xrefs` | ~572M [src: pitfalls] |
| `genome_ani` | ~421M [src: pitfalls] |
| `gapmind_pathways` | ~305M [src: pitfalls] |
| `eggnog_mapper_annotations` | ~93M [src: pitfalls] |

Pagination with `LIMIT/OFFSET` and no `ORDER BY` returns inconsistent results. [src: pitfalls] The REST API can return transient 503 errors ("cannot schedule new futures after shutdown") and 504 errors on large queries. The report recommends retrying or splitting the work into per-species batches. [src: pitfalls]

### Pangenome: coverage, orphans and semantics

Several tables are incomplete or have unexpected semantics.

- `genome_ani` holds only within-species comparisons, so cross-species ANI (average nucleotide identity) is not stored. [src: pitfalls]
- The `is_core`, `is_auxiliary` and `is_singleton` flags on `gene_cluster` are mutually exclusive within their definitions. In counts, however, singletons are a subset of auxiliary, so Core + Auxiliary equals total clusters. [src: pitfalls]
- `alphaearth_embeddings_all_years` covers only ~28% of genomes (~83K/293K), because latitude/longitude metadata at NCBI are sparse. The report recommends `LEFT JOIN` and a coverage check. [src: pitfalls] See also [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].
- `pangenome` references 12 species clades that are absent from `gtdb_species_clade`. These are orphan single-genome species or symbionts, so an anti-join may be needed. [src: pitfalls]
- `gene_genecluster_junction` has 141 orphan genes relative to `gene`, and an `INNER JOIN` silently drops them. [src: pitfalls]
- `ncbi_env` is in entity-attribute-value format. Pivot it or filter by `harmonized_name`, and do not assume one row per sample. [src: pitfalls]
- `pangenome_build_protocol`, `genomad_mobile_elements` and `IMG_env` are referenced elsewhere but do not exist in the Lakehouse, so `protocol_id` is a dangling reference. [src: pitfalls]

### Biochemistry (kbase_msd_biochemistry)

The biochemistry tables lack several mappings that users tend to assume.

- The `reaction` table has no EC-number column, and no EC-to-reaction mapping exists in the Lakehouse. The report suggests bridging through eggNOG `KEGG_ko` or `KEGG_Reaction` to `reaction.abbreviation` (KEGG R-numbers), or using GapMind pathways for pathway-level analysis. [src: pitfalls]
- `reaction.abbreviation` holds KEGG R-numbers for only ~80% of reactions (44,904 / 56,012). The other 20% have no external ID. [src: pitfalls]
- `BiGG_Reaction` appears in eggNOG annotations but not in the ModelSEED tables, so there is no biochemistry-side BiGG mapping. [src: pitfalls]
- ModelSEED IDs use a prefix-colon form, such as `seed.reaction:rxn00001` and `seed.compound:cpd00001`, not bare `rxnNNNNN`. [src: pitfalls]

Query-level cautions also apply:

- `reaction_similarity` has ~671M rows and should always be filtered by `reaction_1` or `reaction_2`. [src: pitfalls]
- `deltag` has extreme outliers, so filter with a sanity bound such as `deltag > -10000000` for any aggregation. [src: pitfalls]
- Many `molecule` rows lack SMILES or InChIKey. Use `LEFT JOIN` to `structure`, not `INNER JOIN`. [src: pitfalls]

## kescience_fitnessbrowser; kescience_alphafold; kescience_pdb

This part of the report lists pitfalls for the Fitness Browser, AlphaFold, PDB, structural biology, BacDive and PaperBLAST collections. They are mostly type, key, coverage and sparsity notes, given as guidance for writing queries. [src: pitfalls] See also [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Fitness Browser (kescience_fitnessbrowser)

Numeric columns are stored as text, keys are composite, and the large tables need filters. Numeric columns, including fit, t, begin, end, cofit, rank, ratio and protein_length, are STRING, so they need a cast before any numeric comparison or sort. [src: pitfalls] The orgId column is case-sensitive, so 'Keio' is the exact form and 'keio' is not. [src: pitfalls] Joins must use (orgId, locusId), because locusId alone collides across organisms. [src: pitfalls] The genefitness table has ~27M rows and cofit has ~13.6M rows. The report advises filtering by orgId, and ideally locusId, before scanning. [src: pitfalls] The per-organism fitbyexp_{orgId} tables, such as fitbyexp_keio and fitbyexp_dvh, are pre-pivoted convenience tables with non-standard schemas, so each organism's schema must be discovered if they are used. [src: pitfalls] See [[entities/fitness-browser]].

### AlphaFold (kescience_alphafold)

The collection has coverage and confidence limits. Joining UniRef100 to UniProt requires stripping the UniRef100_ prefix with REPLACE(uniref100, 'UniRef100_', '') = uniprot_accession. This is a per-row string operation, so the report suggests materializing a mapping table for large joins. [src: pitfalls] About 9% of entries have MSA (multiple sequence alignment) depth < 30 and are low-confidence predictions. The report recommends filtering by msa_depth for structure-based analyses. [src: pitfalls] All entries are model version v6, so the model_version column currently has no variation. [src: pitfalls] Coverage is UniProt-only, so proteins absent from UniProt have no AlphaFold entry. [src: pitfalls] Per-residue pLDDT confidence is in the structure files, not in this metadata. [src: pitfalls]

### PDB (kescience_pdb)

Missing values depend on the experimental method, and chain-level and entry-level tables differ. The r_work and r_free columns are NULL for non-X-ray methods (EM, NMR), and resolution is NULL for NMR. Method-specific filters are needed before averaging. [src: pitfalls] In pdb_uniprot_mapping, pdb_beg and pdb_end are STRING and can literally be "None" for unmapped regions, so coerce or filter them before casting. [src: pitfalls] SIFTS coverage is SwissProt/TrEMBL only, so some PDB chains have no UniProt mapping. [src: pitfalls] Use pdb_uniprot_mapping for chain-level data, because pdb_entries has one row per entry, not per chain. [src: pitfalls] The pdb_entries.organism field reflects only the first polymer entity, so multi-organism complexes appear single-organism. [src: pitfalls]

### Structural biology (kescience_structural_biology)

All four tables start empty and grow with Phenix agent usage, so cross-project queries return nothing until projects accumulate. [src: pitfalls] In refinement_cycles, the X-ray metrics (r_work, r_free, r_gap) are NULL for cryo-EM rows. The cryo-EM metric map_model_cc is NULL for X-ray rows. The report advises filtering by method first, or expecting many NULLs. [src: pitfalls] The parameters_json column is a STRING holding JSON, so querying inner fields needs JSON parsing functions, not column access. [src: pitfalls]

### BacDive

BacDive has naming, identifier and sparsity traps. Taxonomy columns are renamed to tax_class and tax_order to avoid SQL (structured query language) reserved words. [src: pitfalls] The sequence_info.accession column uses GCA_*, while pangenome genome_id uses GB_GCA_* or RS_GCF_*. Prefix-match or strip prefixes before joining. [src: pitfalls] Linking by NCBI taxid to the Fitness Browser works at species level, not strain level, which gives many-to-one ambiguity. [src: pitfalls] Physiology fields are sparse, with Gram stain ~15K/97K and oxygen ~23K/97K, so IS NOT NULL filters are usually required. [src: pitfalls] The metabolite test panel is biased, with trehalose, arginine and glucose dominating, so frequency-based ranking is misleading. [src: pitfalls] See [[entities/bacdive]].

### PaperBLAST (kescience_paperblast)

Types, sparse flags and mixed identifier namespaces cause most problems. The year column is a STRING, so use CAST(year AS INT) for comparisons or ordering. [src: pitfalls] The protein_length column in curatedgene and uniq is also a STRING and needs casting for numeric operations. [src: pitfalls] The genepaper.isOpen column is mostly NULL, so do not use it to filter for open-access papers. [src: pitfalls] The genepaper table has ~3.2M rows, so filter by geneId or pmId instead of scanning it fully. [src: pitfalls] The geneId column spans several namespaces (RefSeq NP_*, UniProt-ish WP_*, VIMSS and others), so cross-namespace queries must go through seqtoduplicate. [src: pitfalls] The snippet.snippet column is raw PMC text with formatting artifacts and partial sentences, so do not display it unfiltered. [src: pitfalls] See [[entities/paperblast]].

## kescience_webofmicrobes; kbase_genomes; nmdc_arkin

This part of the report lists schema and content pitfalls for Web of Microbes (kescience_webofmicrobes), kbase_genomes, nmdc_arkin, enigma_coral, PhageFoundry, UniRef and PlanetMicrobe. [src: pitfalls]

### kescience_webofmicrobes

Action codes depend on who the actor is. For the "The Environment" control (organism_id = 1), D means Detected and N means Not detected. For organisms, I means Increased, E means Emerged (de novo) and N means No change, so the actor must be known before reading a code. [src: pitfalls] E and I are mutually exclusive across organism observations, with zero overlap. [src: pitfalls]

The 2018 snapshot has no Decreased or consumption action. The report says this is by design and not a query bug. [src: pitfalls] See [[concepts/production-versus-consumption-coverage-in-exometabolomic-databases]]. About 56% of compound.compound_name values are unidentified (Unk_* prefix), so filter them out of named-metabolite analyses. [src: pitfalls] The dataset is a 2018 frozen snapshot, and newer data lives in GNPS2. [src: pitfalls]

### kbase_genomes

All primary keys are CDM UUIDs. To map an external gene_id, such as a pangenome gene_id, to internal IDs, go through name.name and name.entity_id. [src: pitfalls] There is no direct genome_id column. Genomes are identified by contig_collection_id and can be cross-referenced via name or gtdb_taxon_id. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

Numeric columns (length, start, end, gc_content, coordinates) are stored as STRING, so cast them before comparing. [src: pitfalls] The feature, encoded_feature and *_x_* junction tables each have about 1B rows. Never scan them without filtering on a key first. [src: pitfalls] The protein table is deduplicated, with 253M unique sequences for about 1B features, so many features share a protein_id. [src: pitfalls]

### nmdc_arkin

Numeric measurement columns in abiotic_features are STRING, including annotations_ammonium_has_numeric_value, annotations_ph and annotations_temp_has_numeric_value. Cast them before numeric comparison. [src: pitfalls] trait_features exposes about 90 functional groups as individual functional_group:* columns instead of rows. Long-form conversion needs stack(...), not GROUP BY. [src: pitfalls] Embedding dimensions vary across tables: embeddings_v1 is 256-dim, and the abiotic, biochemical, taxonomy and trait embeddings differ. Do not assume a fixed dimensionality. [src: pitfalls]

### enigma_coral

Tables follow a strict prefix scheme. sdt_* tables hold scientific data, ddt_* tables hold numerical bricks or arrays, and sys_* tables hold system or metadata. The sys_* tables are not primary scientific data and should not be queried for biology. [src: pitfalls] The ddt_brick* columns are numerical arrays with a non-tabular shape, so standard SQL (structured query language) projections may not work as expected. [src: pitfalls] Many tables timed out during introspection at ingest. Expect partial schemas, and confirm them with DESCRIBE EXTENDED before writing queries. [src: pitfalls]

### PhageFoundry and protect_genomedepot

The report lists five databases: phagefoundry_acinetobacter_genome_browser, phagefoundry_klebsiella_genome_browser_genomedepot, phagefoundry_paeruginosa_genome_browser, phagefoundry_pviridiflava_genome_browser and phagefoundry_strain_modelling. The four genome browsers share the same GenomeDepot schema. phagefoundry_strain_modelling is separate, with an unknown schema. [src: pitfalls] Cross-species queries must run the same SQL once per database, because no unified table exists. [src: pitfalls] protect_genomedepot uses sampled table variants, browser_gene_sampled and browser_annotation_sampled, instead of full tables. Query the sampled tables, not the unsuffixed names. [src: pitfalls]

### UniRef and PlanetMicrobe

kbase_uniref50, kbase_uniref90 and kbase_uniref100 are partial or sample datasets, not the full UniRef releases. Do not assume completeness for any cluster lookup. [src: pitfalls] In planetmicrobe_planetmicrobe and planetmicrobe_planetmicrobe_raw, the project and library tables are empty (count=0), so joins through them return nothing. [src: pitfalls] The _raw database mirrors the curated one structurally, so pick one explicitly per query. [src: pitfalls]

## Caveats and Open Work
- Several items are described as specific incidents, such as one project's out-of-memory failure, one branch collision or one bad filter. [src: pitfalls]
- The ibd_phage_targeting synonym map is hand-curated and enough only for a targeted species battery. [src: pitfalls]
- Within ecotype-assigned CrohnsPhage samples, the report states that 0 sub-studies have both ≥ 10 HC and ≥ 10 CD samples. Only 5 have ≥ 10 CD. [src: pitfalls]
- Two-stage junction filtering gave no speedup, so this item offers no fix for presence-matrix cost. [src: pitfalls]
- The unmatched 56.6% of BacDive records are described as different species concepts or genera absent from GTDB r214. [src: pitfalls]

## Slots Into
- [[concepts/join-key-validity-and-identifier-format-mismatches]]: clade_name, clade-id and cog_class_id mismatches, and locusId type mismatches. [src: pitfalls]
- [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]]: ~1B-row tables, .toPandas() memory limits and the 16 GB driver OOM. [src: pitfalls]
- [[concepts/notebook-provenance-and-session-isolation-in-agent-assisted-analysis]]: the concurrent branch checkout. [src: pitfalls]
- [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]]: the MT20 collision and reclassification splits. [src: pitfalls]
- [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]]: the clustering-feature leakage warning and the C. scindens reversal. [src: pitfalls]
- [[concepts/annotation-and-environmental-metadata-table-gaps-in-the-data-lakehouse]]: the missing IMG_env table and the missing BiGG mapping. [src: pitfalls]
