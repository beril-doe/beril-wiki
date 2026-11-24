---
type: "Summary"
description: "Summary of the project GC Content as an Ecological Signal Across Bacterial Ecotypes."
doc_type: "short"
full_text: "sources/gc_ecotype_ecology__REPORT.md"
---
# GC Content as an Ecological Signal Across Bacterial Ecotypes

This report asks whether genome GC content carries an ecological signal within bacterial species once intra-species phylogeny is controlled. [src: gc_ecotype_ecology] Across 108 species in the KBase Data Lakehouse pangenome, 40 (37%) showed isolation-source-associated GC variation after controlling for ANI (average nucleotide identity) clusters at FDR (false discovery rate) < 0.05. [src: gc_ecotype_ecology] The signal survived several robustness checks, but effect sizes are small. [src: gc_ecotype_ecology] The report concludes that at least ~40% of well-sampled species carry a measurable ecological GC signal after phylogenetic control, and it is observational, not causal. [src: gc_ecotype_ecology] Two independent definitions of environment converge on similar species sets, with 59% overlap. [src: gc_ecotype_ecology] See [[concepts/genome-gc-content-as-an-ecological-signal]] for the wider topic.

## Key Findings

### Background and motivation

Across species, GC tracks lifestyle: obligate intracellular bacteria have low GC and soil and plant-associated bacteria tend to have high GC. [src: gc_ecotype_ecology] Within communities, GC tracks soil carbon, pH and metabolic strategy. [src: gc_ecotype_ecology] The dominant explanation is biased gene conversion plus ancient environmental adaptation. [src: gc_ecotype_ecology] Within-species tests have been rare because they need many genomes per species, per-genome environmental metadata and intra-species phylogenetic control. [src: gc_ecotype_ecology] The Lakehouse has 293,059 GTDB-r214 bacterial genomes, 84% with NCBI isolation_source, and a within-species ANI table. [src: gc_ecotype_ecology] A related project, ecotype_analysis, found that phylogeny dominates gene-content similarity in 60.5% of 172 species. [src: gc_ecotype_ecology] The report describes ANI ≥ 99% connected-components clustering as a tractable, pragmatic intra-species phylogenetic control on Lakehouse pangenomes. [src: gc_ecotype_ecology]

### Pooled cross-species sanity check

Pooled across species, mean GC followed the expected soil/plant > aquatic > host/gut order, which the report treats as a positive control validating its categories. [src: gc_ecotype_ecology] Mean GC (%) and genome counts by category:

| Category | Mean GC | Genomes |
|---|---|---|
| plant_microbiome | 60.9 [src: gc_ecotype_ecology] | 384 |
| plant_host | 56.2 [src: gc_ecotype_ecology] | 5,919 |
| soil | 55.0 [src: gc_ecotype_ecology] | 9,087 |
| freshwater | 53.3 [src: gc_ecotype_ecology] | 9,315 |
| wastewater | 52.2 [src: gc_ecotype_ecology] | 3,648 |
| extreme | 50.2 [src: gc_ecotype_ecology] | 724 |
| marine | 48.7 [src: gc_ecotype_ecology] | 4,974 |
| human_clinical | 48.1 [src: gc_ecotype_ecology] | 57,950 |
| animal_host | 46.9 [src: gc_ecotype_ecology] | 9,718 |
| gut_environmental | 46.0 [src: gc_ecotype_ecology] | 17,152 |
| food | 41.8 [src: gc_ecotype_ecology] | 6,679 |

### Within-species signal and its robustness

The main result survived the permutation, phylogenetic-regression and geographic checks, though not in every species tested. Effect sizes are small: typical max-minus-min mean GC across categories is 0.1 – 0.9%. [src: gc_ecotype_ecology] They are reproducible across two environment definitions and three phylogenetic-control definitions. [src: gc_ecotype_ecology] Across the 40 significant species, isolation-category partial R² given ANI cluster had median 12.3% (IQR 4.3 – 22.7%). [src: gc_ecotype_ecology] Max-minus-min mean GC had median 0.15% (IQR 0.09 – 0.30%, max 0.88%). [src: gc_ecotype_ecology] The report calls these effects small next to the ≈ 30% across-species GC range, but statistically robust and reproducible. [src: gc_ecotype_ecology] It judges them biologically meaningful. [src: gc_ecotype_ecology] The signal is broadly distributed across taxa and habitats, not concentrated in one clade [src: gc_ecotype_ecology], and the report states it survives ANI cluster fixed effects, a permutation null and an alternative continuous environmental measure. [src: gc_ecotype_ecology] The within-species categorical test identifies 40 significant species. [src: gc_ecotype_ecology]

- Label-permutation null: 39/40 species survived. [src: gc_ecotype_ecology] Specifically, 39/40 retained empirical p < 0.05 and 29/40 retained p < 0.01. [src: gc_ecotype_ecology] The report reads this as ruling out a confound from random label/cluster co-occurrence. [src: gc_ecotype_ecology] It also reads it as excluding chance exploitation of within-cluster labels when ANI clusters are ecology-defined. [src: gc_ecotype_ecology]
- Continuous phylogenetic regression: notebook 06 replaces the connected-components ANI cluster fixed effect with continuous principal coordinates from per-species pairwise branch_distance in phylogenetic_tree_distance_pairs. [src: gc_ecotype_ecology] 32 of 39 testable species (82%) stayed significant. [src: gc_ecotype_ecology] The report reads this as evidence against a clone-cluster artifact, and as showing the original ANI cluster choice was not driving the result. [src: gc_ecotype_ecology] One species had insufficient phylogenetic coverage and could not be tested. [src: gc_ecotype_ecology]
- Geographic covariates: 12 of 16 testable species (75%) stayed significant. [src: gc_ecotype_ecology] The report concludes the isolation-category effect is not just a proxy for geographic structure. [src: gc_ecotype_ecology] Geographic sensitivity could be tested for only 16 of 40 species, because the other 24 had < 30 genomes with parseable lat_lon. [src: gc_ecotype_ecology] The report cannot rule out residual geographic confounding in untested species, although 75% of testable species remained significant. [src: gc_ecotype_ecology]

The largest partial R² values come from species with many small ANI clusters, such as Aeromonas veronii (87 clusters of 122 genomes). There the ANI control uses up most degrees of freedom and leaves small but well-determined residual variance. [src: gc_ecotype_ecology] Example strong species are listed below.

| Species | n | ANI clusters | Categories | Mean GC | Partial R² | Max-min GC | q |
|---|---|---|---|---|---|---|---|
| Aeromonas veronii | 122 | 87 | gut, clinical, freshwater, animal | 58.7 | 64% | 0.28 | 5.4e-08 [src: gc_ecotype_ecology] |
| Citrobacter braakii | 84 | 22 | wastewater, clinical, food, plant | 52.1 | 59% | 0.43 | 2.1e-10 [src: gc_ecotype_ecology] |
| Mediterraneibacter faecis | 67 | 37 | gut, clinical | 40.7 | 30% | 0.06 | 5.8e-03 [src: gc_ecotype_ecology] |
| Sarcina perfringens | 104 | 44 | gut, clinical, animal, food | 28.2 | 28% | 0.21 | 1.2e-03 [src: gc_ecotype_ecology] |
| Escherichia fergusonii | 93 | 28 | animal, gut | 49.8 | 27% | 0.13 | 5.6e-05 [src: gc_ecotype_ecology] |
| Enterococcus B hirae | 50 | 12 | gut, clinical, food | 36.8 | 27% | 0.11 | 1.3e-02 [src: gc_ecotype_ecology] |
| Listeria monocytogenes_C | 72 | 36 | soil, animal | 38.0 | 26% | 0.09 | 5.8e-03 [src: gc_ecotype_ecology] |
| Burkholderia vietnamiensis | 101 | 12 | clinical, soil, plant | 67.0 | 23% | 0.36 | 6.1e-05 [src: gc_ecotype_ecology] |
| Enterococcus B faecium | 1633 | 2 | clinical, gut, animal, food, ww, fw | 37.8 | 23% | 0.35 | 3.1e-89 [src: gc_ecotype_ecology] |
| Vibrio parahaemolyticus | 999 | 346 | clinical, animal, gut, food, fw, marine | 45.3 | 23% | 0.36 | 1.3e-32 [src: gc_ecotype_ecology] |
| Klebsiella quasipneumoniae | 400 | 6 | clinical, gut, food, ww, marine | 57.7 | 23% | 0.88 | 1.7e-19 [src: gc_ecotype_ecology] |
| Streptococcus thermophilus | 135 | 5 | food, clinical | 39.0 | 22% | 0.30 | 1.4e-07 [src: gc_ecotype_ecology] |
| Dorea formicigenerans | 63 | 35 | gut, clinical | 40.8 | 20% | 0.13 | 4.5e-02 [src: gc_ecotype_ecology] |
| Cronobacter sakazakii | 181 | 38 | food, clinical, gut | 56.9 | 19% | 0.18 | 2.7e-06 [src: gc_ecotype_ecology] |
| Leuconostoc mesenteroides | 66 | 6 | food, marine | 37.8 | 17% | 0.02 | 4.7e-03 [src: gc_ecotype_ecology] |

The full table is in data/05_final_summary_table.csv, with significant species also in data/03_significant_species.csv. [src: gc_ecotype_ecology]

### Case studies of ecotype-spanning species

The report names Vibrio parahaemolyticus, Burkholderia vietnamiensis, Klebsiella quasipneumoniae, Lactiplantibacillus plantarum and Bacillus anthracis as ecotype-spanning species with particularly clear signals, because their genomes come from genuinely different niches. [src: gc_ecotype_ecology] It calls the first four particularly clean ecotype-spanning species in the Lakehouse and useful test beds for future within-species genotype × environment work. [src: gc_ecotype_ecology]

Vibrio parahaemolyticus is the cleanest case: 999 genomes across 6 categories, 346 ANI clusters, partial R² = 22.8%, max-min GC = 0.36%, q = 1.3e-32. [src: gc_ecotype_ecology] It is analyzed sensu stricto, and its epidemiology and host range span ecotypes. [src: gc_ecotype_ecology]

Burkholderia vietnamiensis is a high-GC (≈ 67%) plant- and soil-associated bacterium that also colonizes human cystic fibrosis airways. [src: gc_ecotype_ecology] The dataset has 101 quality-passing genomes across human_clinical, soil and plant_host, with ≥ 10 in each. [src: gc_ecotype_ecology] Its 12 ANI clusters give meaningful phylogenetic resolution. [src: gc_ecotype_ecology] Isolation category given ANI cluster gives partial R² = 23.4%, q = 6.1e-05 and max-min GC = 0.36%. [src: gc_ecotype_ecology] The independent AlphaEarth test gives r = -0.60, p = 3.2e-07, FDR < 0.05. [src: gc_ecotype_ecology] The report reads the two independent definitions of environment as converging on a non-trivial ecological GC signal beyond intra-species phylogeny. [src: gc_ecotype_ecology]

### Independent AlphaEarth environment

AlphaEarth gave a continuous definition of environment that uses no isolation_source text. [src: gc_ecotype_ecology] Residual GC correlated significantly with a top-5 principal component of within-cluster residual embeddings in 53 of 131 species (40%). [src: gc_ecotype_ecology] The test yielded 53 significant species at FDR < 0.05. [src: gc_ecotype_ecology] Agreement with the isolation-category test among jointly testable species was 59% (10 of 17). [src: gc_ecotype_ecology] The report calls this strong corroboration given how different the two definitions are. [src: gc_ecotype_ecology]

AlphaEarth-only hits include Streptococcus pneumoniae (r = -0.34 over 527 genomes) [src: gc_ecotype_ecology], Bacteroides xylanisolvens [src: gc_ecotype_ecology] and the archaeon Methanosarcina mazei (r = -0.59). [src: gc_ecotype_ecology] The report suggests this means the signal is not specific to a bacterial subset. [src: gc_ecotype_ecology]

Among 20 top AlphaEarth-significant species, the GC-correlated component was decomposed into raw dimensions and tested against isolation category by ANOVA. [src: gc_ecotype_ecology] The recurrent top-loading dimensions were A06, A02, A48, A53, A50, A09, A15 and A40, each top in 4–6 of 20 species. [src: gc_ecotype_ecology] Only 5 of 20 (25%) of these components also discriminated isolation category. [src: gc_ecotype_ecology] For the other 75%, the report calls the AlphaEarth signal largely orthogonal to categorical isolation source. [src: gc_ecotype_ecology] It suggests that AlphaEarth, a 64-d learned representation of local environment, captures continuous climate, vegetation and land-cover gradients that only partly overlap with curator labels. [src: gc_ecotype_ecology] This explanation is the report's interpretation, not a direct test. See [[concepts/independent-continuous-environment-embeddings-versus-categorical-isolation-source]].

## Interpretation and Candidate Mechanisms

The report reads typical 0.1–0.9% GC shifts as consistent with fine-grained selective or mutational pressure rather than ancestral inheritance. [src: gc_ecotype_ecology] For a typical 3 Mbp genome, a 0.3% GC shift corresponds to ≈ 9,000 net biased substitutions. [src: gc_ecotype_ecology] It cites bacterial point-mutation rates of 10⁻⁹ to 10⁻¹⁰ per nucleotide per generation [src: gc_ecotype_ecology] and free-living effective population sizes commonly estimated at 10⁸–10¹⁰. [src: gc_ecotype_ecology] It argues that μN_e of ~10⁻¹ to 10¹ lets even very weakly selected GC-changing substitutions (|s| ≈ 10⁻⁷ to 10⁻⁹) be fixed by selection. [src: gc_ecotype_ecology] See [[concepts/mechanisms-of-ecology-linked-gc-shifts]].

The report's candidate mechanisms were not directly tested here [src: gc_ecotype_ecology]:

- Differential biased gene conversion (gBGC), established in bacteria and expected to vary with recombination rate. [src: gc_ecotype_ecology] Host-associated bacteria typically recombine less than environmental ones. [src: gc_ecotype_ecology] A 2× difference in bN_e between gut and free-living lineages could produce a fraction-of-a-percent GC offset over ≈ 10⁶ generations. [src: gc_ecotype_ecology] This could arise if gut and free-living recombination rates differ. [src: gc_ecotype_ecology]
- Nutrient-responsive codon-usage selection, particularly on nitrogen [src: gc_ecotype_ecology], building on Gralka et al. 2023, who found a cross-species GC relationship with sugar-versus-acid metabolism. [src: gc_ecotype_ecology]
- Mutational asymmetries from oxidative stress or replication-fork dynamics that differ between hosts and free-living environments. [src: gc_ecotype_ecology] Oxidative G→T transversions could give 0.1–1% GC shifts between aerobic soil and anaerobic gut. [src: gc_ecotype_ecology]

Burkholderia vietnamiensis, Vibrio parahaemolyticus, Klebsiella quasipneumoniae and Lactiplantibacillus plantarum show the largest effects and span niches that differ in recombination rate and likely oxidative environment. [src: gc_ecotype_ecology] The report finds the offsets consistent with a few hundred to a few thousand generations of differential pressure since recent divergence. [src: gc_ecotype_ecology] It reads the shifts as an ongoing niche-tunable mutation-and-selection balance on a phylogeny-dominated GC level, not noise. [src: gc_ecotype_ecology]

## Relation to Gene Content

The ecotype_analysis project found phylogeny dominates gene-content similarity within species. This project finds that in a non-trivial fraction of species, environment leaves a residual signature on GC after phylogeny is removed. [src: gc_ecotype_ecology] The report describes ecotype_analysis as the companion project addressing the gene-content version of the within-species ecology question. [src: gc_ecotype_ecology] It interprets nucleotide composition as appearing more environment-responsive within species than gene presence/absence, in tension with that finding. [src: gc_ecotype_ecology] The report hypothesizes that gene presence/absence is a "loud" event with large fitness effects, while GC is a "quiet" continuous trait responsive to ongoing micro-selection. [src: gc_ecotype_ecology]

## Data and Methods

The master table covers 293,059 GTDB-r214 bacterial genomes [src: gc_ecotype_ecology] and is built as genome_gc_env.parquet (293K x 18). [src: gc_ecotype_ecology] GC and genome size came from gtdb_metadata, cast from strings to numbers. [src: gc_ecotype_ecology] All genomes passed the quality flag (checkm_completeness ≥ 90, contamination ≤ 5). [src: gc_ecotype_ecology] Environmental metadata were pivoted from kbase_ke_pangenome.ncbi_env, where the value column is content. [src: gc_ecotype_ecology] AlphaEarth presence came from alphaearth_embeddings_all_years, covering 83,227 genomes (28%). [src: gc_ecotype_ecology] Coverage was GC 100%, isolation_source 84%, host 58%, env_broad_scale 30%, lat_lon 47% and AlphaEarth 28%. [src: gc_ecotype_ecology] Free-text isolation_source was mapped to 14 categories by conservative regex rules that favor "other" or unknown. [src: gc_ecotype_ecology]

Species qualified with n ≥ 50 genomes and ≥ 2 categories of ≥ 10 genomes each; 121 qualified. [src: gc_ecotype_ecology] ANI clusters were connected components of the ANI ≥ 99% graph from genome_ani, which is within-species by construction. [src: gc_ecotype_ecology] The test was a nested OLS (ordinary least squares) partial F-test comparing gc ~ ANI cluster against gc ~ ANI cluster + isolation category. [src: gc_ecotype_ecology] Large clinical species were stratified-subsampled to ≤ 5,000 genomes. [src: gc_ecotype_ecology] Benjamini–Hochberg (BH) FDR was applied across all tested species. [src: gc_ecotype_ecology] The report tested 108 species categorically and 131 continuously. [src: gc_ecotype_ecology] The permutation null shuffled labels 200 times within species with ANI clusters fixed [src: gc_ecotype_ecology], and the empirical p was the rank of the observed F. [src: gc_ecotype_ecology] The phylogenetic regression used the top-10 PCoA (principal coordinates analysis) axes of per-species branch_distance instead of ANI-cluster dummies. [src: gc_ecotype_ecology] The AlphaEarth analysis covered 197 species with ≥ 30 embedding-bearing genomes, 131 of them with ≥ 2 ANI clusters. [src: gc_ecotype_ecology] It used PCA (principal component analysis) plus Pearson correlation. [src: gc_ecotype_ecology]

Analysis runs on-cluster against the Lakehouse via berdl_notebook_utils.setup_spark_session. [src: gc_ecotype_ecology] End-to-end runtime is ≈ 45 minutes on the Lakehouse JupyterHub kernel, with notebook 06 adding ~10 min for per-species phylogenetic PCoA pulls. [src: gc_ecotype_ecology] genome_ani IN-clause queries scaled to ~5,000 genomes per species without trouble on the Spark Connect kernel. [src: gc_ecotype_ecology] Per-species ANI pulls ran in seconds for typical species with 50–500 genomes [src: gc_ecotype_ecology] and seconds-to-a-minute for the largest, a Staphylococcus aureus subsample at 5,000 genomes. [src: gc_ecotype_ecology] Pulling all of alphaearth_embeddings_all_years into pandas (83K genomes × 65 columns) finished in under a minute. [src: gc_ecotype_ecology] One pitfall: df.to_parquet on a Spark-Connect-derived pandas DataFrame fails with TypeError: Object of type PlanMetrics is not JSON serializable. [src: gc_ecotype_ecology] The workaround is to rebuild the frame as pd.DataFrame({c: df[c].to_numpy() for c in df.columns}) to strip Spark-side metadata before pyarrow serialization. [src: gc_ecotype_ecology]

The report's author is Justin Reese, Lawrence Berkeley National Laboratory. [src: gc_ecotype_ecology]

## Caveats and Open Work

- Seven species had all genomes collapse to a single ANI cluster and were dropped, and 108 species produced valid p-values. [src: gc_ecotype_ecology]
- The robustness tests cover fewer species than the primary test: 39 for phylogenetic regression and only 16 for the geographic test. [src: gc_ecotype_ecology]
- Some species have very few ANI clusters: Enterococcus faecium has only 2 among 1,633 genomes [src: gc_ecotype_ecology], and Streptococcus thermophilus has 5. [src: gc_ecotype_ecology] For these, connected-components control could partly reflect cluster-level confounds, and the phylogenetic-PCoA control mitigates this only for the subset retaining significance. [src: gc_ecotype_ecology] Such species need a stricter or alternative phylogenetic control before strong claims can be made. [src: gc_ecotype_ecology]
- The AlphaEarth–isolation agreement rests on only 17 jointly testable species. [src: gc_ecotype_ecology]
- Effect sizes are small in absolute terms. [src: gc_ecotype_ecology]
- The result is associational and observational. Without strain-replicate transplant experiments, hidden confounders such as geographic sampling bias correlated with isolation source cannot be excluded. [src: gc_ecotype_ecology]
- The permutation null rules out random label associations within species, but not all confounders. [src: gc_ecotype_ecology]
- Metadata are sparse: isolation_source is missing for ~16% of genomes and ~30% map only to "other". [src: gc_ecotype_ecology] The categorical scheme is coarse and conservative, and finer categories likely exist but were not extracted. [src: gc_ecotype_ecology] Sampling bias is substantial (57K clinical genomes versus 384 plant_microbiome). [src: gc_ecotype_ecology] Latitude/longitude coverage is ~28% globally. [src: gc_ecotype_ecology]
- The BH correction is appropriate for discovery, but per-species effect estimates are subject to selection bias if cherry-picked from the top. [src: gc_ecotype_ecology]
- The linear/categorical model does not capture possible nonlinear effects of environment on GC. [src: gc_ecotype_ecology] The AlphaEarth PCA plus Pearson analysis captures only linear monotone signals. [src: gc_ecotype_ecology]
- Only genome-level GC is analyzed. Within-genome heterogeneity (GC₃, gene-body versus intergenic, mobile elements) might amplify or contradict the genome-mean signal. [src: gc_ecotype_ecology]
- The mechanistic explanations above are candidates, not tested here. [src: gc_ecotype_ecology]
- The largest partial R² values come from species with many small ANI clusters, so they partly reflect the small residual variance left after control. [src: gc_ecotype_ecology]

## Slots Into

- [[concepts/genome-gc-content-as-an-ecological-signal]]: 40 of 108 species show within-species GC–isolation-source association after ANI-cluster control. [src: gc_ecotype_ecology]
- [[concepts/independent-continuous-environment-embeddings-versus-categorical-isolation-source]]: AlphaEarth found 53/131 significant species, but only 25% of GC-correlated components discriminated isolation category. [src: gc_ecotype_ecology]
- [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]]: gene content was phylogeny-dominated in the related ecotype_analysis project, whereas GC retains an environmental signal. [src: gc_ecotype_ecology]
- [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]]: free text was mapped to 14 categories, and the pooled GC order validated them. [src: gc_ecotype_ecology]
- [[concepts/mechanisms-of-ecology-linked-gc-shifts]]: gBGC, codon-usage and oxidative-mutation candidates were proposed but not directly tested. [src: gc_ecotype_ecology]
- [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]]: isolation_source is missing for ~16% of genomes and lat/lon coverage is ~28%. [src: gc_ecotype_ecology]
- [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]]: genome_ani IN-clause queries scaled to ~5,000 genomes per species, and Spark Connect pandas frames needed a rebuild before Parquet export. [src: gc_ecotype_ecology]
