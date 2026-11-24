---
type: "Concept"
description: "How missing or coarse isolation-source, geographic and embedding metadata, uneven sampling, keyword-based classification, NaN embeddings and incomplete per-gene annotation tables silently shrink or skew the cohorts that analyses actually test; stops at identifier mismatches."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md", "summaries/ecotype_analysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/metal_resistance_global_biogeography__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Metadata and annotation coverage gaps biasing environmental genome cohorts

This page covers how missing or coarse metadata and incomplete annotation shrink or skew the genome cohorts that analyses actually test, drawing on several reports using AlphaEarth and MAG (metagenome assembled genomes) datasets. The evidence is mostly direct coverage counts; the effects on conclusions are often only stated as likely or possible. A NEON per-MAG re-analysis adds a worked case: a habitat-biased gap in per-gene annotation tables cut a 246-MAG cohort to 73 MAGs. [src: env_embedding_explorer, neon_mag_functional_discovery, pitfalls] Prophage and Pseudomonas reports show sparse, coarse or keyword-derived isolation-source labels that leave large "other" or "unknown" classes, with uneven sampling. [src: prophage_ecology, pseudomonas_carbon_ecology] The plant microbiome report says its compartment classification rests on isolation_source metadata of variable quality and coverage. [src: plant_microbiome_ecotypes]

## Coverage of AlphaEarth embeddings

AlphaEarth embeddings cover a minority of genomes, and the covered genomes are not a random sample. The embeddings table covers 83,287 genomes, which is 28.4% of 293,059 genomes in the pangenome database. [src: env_embedding_explorer] Other reports give about 28% [src: amr_pangenome_atlas, functional_dark_matter, gc_ecotype_ecology], and one gives 83,227 genomes from alphaearth_embeddings_all_years. [src: gc_ecotype_ecology] The pitfalls digest also gives 83,227 of 293,059 genomes (28.4%). [src: pitfalls] The coverage is biased toward genomes with geographic metadata. [src: amr_pangenome_atlas, env_embedding_explorer] The prophage report likewise says only 28% of genomes have embeddings, creating a biased subsample toward clinically and environmentally well-sampled lineages. [src: prophage_ecology] See [[entities/alphaearth-environmental-embeddings]].

The embeddings need valid latitude/longitude, which NCBI metadata often lacks, especially for clinical isolates. [src: pitfalls] The PHB (polyhydroxybutyrate) report warns that the 28% coverage (83K/293K) may skew niche breadth analysis toward better-sampled lineages. [src: phb_granule_ecology] Its AlphaEarth analysis covers 2,008 species, 7.2% of total species diversity. [src: phb_granule_ecology]

Coverage is thinner still at species level. Only 6.8% of species (1,872/27,690) have at least 5 genomes with embeddings. [src: discoveries] The reason given is missing latitude/longitude for most NCBI genomes, especially clinical isolates. [src: discoveries] Among xoxF carriers, 39.5% (1,457/3,690) have AlphaEarth coverage. That is better than the 28% baseline but leaves 60.5% without environmental coordinates. [src: lanthanide_methylotrophy_atlas]

Some embeddings are unusable. Of the 83,287 genomes, 79,449 have valid values in all 64 dimensions, and 3,838 have NaN (not a number) in at least one. [src: env_embedding_explorer, discoveries] The pitfalls digest gives the same counts: 3,838 of 83,287 (4.6%). [src: pitfalls] The cause is unclear. Reports suggest missing satellite imagery or coordinates outside coverage, such as polar regions or ocean. [src: discoveries, env_embedding_explorer] NaN values can make UMAP (uniform manifold approximation and projection), cosine distance and other operations fail or silently return NaN. [src: pitfalls] The fix is to filter before any embedding-based computation, which reduces the dataset from 83,287 to 79,449 genomes. [src: pitfalls, discoveries]

Pooling can also hide signal. In env_embedding_explorer, the pooled geographic distance–embedding distance curve shows a 2.0x near-versus-far ratio. [src: pitfalls] Environmental samples show 3.4x, described as a strong signal, while human-associated samples show 2.0x, a weak signal. [src: pitfalls] The report states that the pooled curve underestimates the true geographic signal. [src: pitfalls] It recommends stratifying by environment category and considering excluding human-associated samples when embeddings serve as environment proxies. [src: pitfalls]

Coverage limits what the tests can show. The ecotype report found no significant environment effect in 156 species (90.7%). [src: ecotype_analysis] It notes that the 28.4% coverage limits the available signal. [src: ecotype_analysis] It also suggests that the embeddings may not fully capture ecologically relevant variation. [src: ecotype_analysis] It proposes trying other embedding distances or environmental metadata directly. [src: ecotype_analysis]

## Geographic coordinates

Coordinates are often missing or imprecise, which lowers the quality of environmental associations. [src: ecotype_analysis] The ncbi_lat_lon field in gtdb_metadata is most commonly NULL. [src: pitfalls] It also holds malformed strings such as "missing" or "not collected". [src: pitfalls] Some values have low precision, such as "37.0 N 122.0 W". [src: pitfalls] For host-associated organisms, coordinates reflect the collection site rather than the organism's microenvironment. [src: ecotype_analysis] Coordinate coverage is ~28% globally in the GC ecology dataset. [src: gc_ecotype_ecology] In its bacterial master table, lat_lon coverage is 47%. [src: gc_ecotype_ecology]

Missing coordinates also restrict the tests. Geographic sensitivity could be tested for only 16 of 40 bacterial species. The other 24 had fewer than 30 genomes with parseable lat_lon. [src: gc_ecotype_ecology] Residual geographic confounding in those species cannot be ruled out, although 75% of testable species stayed significant after geographic control. [src: gc_ecotype_ecology] Hidden confounders such as geographic sampling bias correlated with isolation source also cannot be excluded without transplant experiments. [src: gc_ecotype_ecology]

Public metagenomic archives show the same gap. ENA batch retrieval returned 24,511 sample records, and 16,964 (69.2%) had valid lat/lon pairs. That leaves a 30.8% gap. [src: metal_resistance_global_biogeography] A later spatial analysis corrected how this gap should be read. It is per-sample, not geographic. Samples lack coordinates, but 0 of 532 MAG grid cells lack ENA coverage. [src: metal_resistance_global_biogeography] The report first read it as a source of substantial geographic blind spots for global maps. [src: metal_resistance_global_biogeography] Which biomes are most underrepresented remains open. [src: metal_resistance_global_biogeography]

The environmental MAG set has 22,356 MAGs with usable coordinates, which is 73.3% coordinate coverage. [src: metal_resistance_global_biogeography] The hotspot analysis uses a 5° grid with 289 cells holding at least 5 MAGs. It applies Fisher's exact test with Benjamini–Hochberg (BH) false-discovery-rate (FDR) correction. [src: metal_resistance_global_biogeography] Hotspot identification and sampling-effort correction are required before regional patterns can be interpreted. [src: metal_resistance_global_biogeography] Two checks are still pending. One tests whether the Atacama (odds ratio, OR, 9.8) and USA clusters are single-study artefacts. [src: metal_resistance_global_biogeography] The other tests whether hotspots persist after normalising by log(n_MAGs). [src: metal_resistance_global_biogeography]

## Isolation source and environment labels

Among the AlphaEarth genomes, free-text and coordinate fields are well covered but ontology fields are not. Counts of genomes with each field:

- Lat/lon (cleaned): 83,286 (100.0%) [src: env_embedding_explorer]
- geo_loc_name: 83,270 (100.0%) [src: env_embedding_explorer]
- isolation_source: 76,295 (91.6%) [src: env_embedding_explorer]
- host: 53,091 (63.7%) [src: env_embedding_explorer]
- env_broad_scale: 34,800 (41.8%) [src: env_embedding_explorer]
- env_local_scale: 31,541 (37.9%) [src: env_embedding_explorer]
- env_medium: 31,483 (37.8%) [src: env_embedding_explorer]

Across the whole bacterial master table, coverage is isolation_source 84%, host 58%, env_broad_scale 30%, lat_lon 47% and AlphaEarth 28%. [src: gc_ecotype_ecology] See [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]].

Keyword classification adds its own losses. The isolation-source mapping labels 71% of genomes. Another 17% remain "Other" and 12.5% are "Unknown" because the field is missing or null. [src: env_embedding_explorer] Keyword matching misses site-specific labels and non-English terms. [src: env_embedding_explorer] The ENVO (Environment Ontology) env_broad_scale field is cleaner but covers only 42% of genomes. [src: env_embedding_explorer] Many of its values are bare ENVO identifiers (IDs) without labels, or generic terms such as "not applicable" and "missing". [src: env_embedding_explorer]

Other projects report similar gaps. In amr_strain_variation, per-genome parsing of isolation_source and host from ncbi_env gave 52.7% "Unknown" labels (94,957/180,025 genomes), because most BioSample records lack structured isolation metadata. [src: pitfalls] For cross-species work, the pitfalls digest recommends species-level majority-vote labels, with 91% coverage via keyword classification of NCBI metadata. [src: pitfalls] In the PGP (plant growth promoting) analysis, 291,279 genomes have ncbi_isolation_source metadata and 93.5% were classifiable. [src: pgp_pangenome_ecology] Only 1,637 species (5.9% of species with an environment label) are soil/rhizosphere dominant, reflecting NCBI's clinical and host-associated sampling bias. [src: pgp_pangenome_ecology] The report considers the acdS and pqqC enrichment effects (ORs of 7.0 and 2.9) likely underestimates, since many soil isolates carry broader "environmental" labels. [src: pgp_pangenome_ecology] In the PHB analysis, 34.9% of species have "other_unknown" as primary environment, so enrichment results may underestimate the true signal. [src: phb_granule_ecology] Interpretation of PHB family patterns is limited by that category (30/41 enriched, 26/62 depleted). [src: phb_granule_ecology]

The prophage report gives the same warning. NCBI isolation_source metadata is sparse and inconsistently labeled, and its 10-category classification collapses substantial within-category variation. [src: prophage_ecology] The "other_unknown" category holds 9,659 species (35%) and limits statistical power. [src: prophage_ecology]

The plant microbiome study shows how thin plant-labelled cohorts can be. Only 7,995 of 293,059 genomes (2.7%) had plant-associated annotations. [src: plant_microbiome_ecotypes] Compartment classification rests on NCBI isolation_source metadata of variable quality and coverage. [src: plant_microbiome_ecotypes] BacDive isolation records identified 2,482 plant strains but yielded 0 new upgrades. [src: plant_microbiome_ecotypes] The report reads this as complete overlap with ncbi_env for the plant-associated genome set. [src: plant_microbiome_ecotypes] This is a null result: a second metadata source did not enlarge the cohort. See [[entities/bacdive]].

### Pseudomonas isolation-source classes

The Pseudomonas carbon-ecology report shows both uneven sampling and keyword losses in one cohort. Pseudomonas aeruginosa comprises 53% of all genomes (6,760/12,732) because of clinical importance, while many environmental species have <10 sequenced genomes, which affects the power of species-level comparisons. [src: pseudomonas_carbon_ecology] Classifiable isolation-source metadata was available for 64.2% of genomes (8,171/12,732). [src: pseudomonas_carbon_ecology] Keyword-based classification assigned genomes to 10 environment categories. [src: pseudomonas_carbon_ecology] It introduced ~6.7% "unknown" and ~29.1% "other" classifications, and misclassification could attenuate true ecological signal. [src: pseudomonas_carbon_ecology]

| Category | Genomes | Share of total |
|---|---|---|
| Clinical | 4,197 [src: pseudomonas_carbon_ecology] | 33.0% |
| Human (other) | 1,659 [src: pseudomonas_carbon_ecology] | 13.0% |
| Freshwater | 566 [src: pseudomonas_carbon_ecology] | 4.4% |
| Soil | 551 [src: pseudomonas_carbon_ecology] | 4.3% |
| Plant surface | 503 [src: pseudomonas_carbon_ecology] | 4.0% |
| Rhizosphere | 275 [src: pseudomonas_carbon_ecology] | 2.2% |
| Food/dairy | 141 [src: pseudomonas_carbon_ecology] | 1.1% |
| Animal | 136 [src: pseudomonas_carbon_ecology] | 1.1% |
| Industrial | 80 [src: pseudomonas_carbon_ecology] | 0.6% |
| Marine | 63 [src: pseudomonas_carbon_ecology] | 0.5% |

At species level, 387 of 433 species had at least one classifiable genome. [src: pseudomonas_carbon_ecology] Majority-lifestyle assignment gave 204 free-living [src: pseudomonas_carbon_ecology], 109 host-associated [src: pseudomonas_carbon_ecology], 59 plant-associated [src: pseudomonas_carbon_ecology] and 15 food-associated species. [src: pseudomonas_carbon_ecology] Assigning each species one category by majority vote obscures genuinely generalist species that inhabit multiple environments. [src: pseudomonas_carbon_ecology] The report proposes moving to genome-level analysis, using the full 789K genome-pathway matrix with genome-specific isolation sources, to increase statistical power. [src: pseudomonas_carbon_ecology] See [[concepts/carbon-pathway-profiles-as-predictors-of-environment-and-lifestyle]].

The GC ecology report finds isolation_source missing for ~16% of genomes and ~30% mapping only to "other". [src: gc_ecotype_ecology] Its scheme is coarse and conservative, and finer categories were likely not extracted. [src: gc_ecotype_ecology] Sampling is uneven, with 57K clinical genomes against 384 plant_microbiome genomes. [src: gc_ecotype_ecology] See [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]]. Prior within-species tests have been rare because they need many genomes per species, genome-level metadata and phylogenetic control. [src: gc_ecotype_ecology] Metadata sparsity and inconsistent isolation-source text limit the power of biogeographic tests of dark genes. [src: functional_dark_matter]

Species-level labels can also mislead. Majority-vote classification collapses within-species variation, so a "clinical" species may contain environmental strains. A sensitivity analysis at 60–90% thresholds mitigates this. [src: amr_environmental_resistome] Temporal metadata is also incomplete. Only 70% of genomes had parseable collection dates, and the report attributes its null temporal result likely to that gap. [src: amr_strain_variation]

## Incomplete per-gene annotation tables (NEON MAGs)

Annotation tables can be incomplete in a habitat-dependent way, and this shrinks cohorts as surely as missing metadata. In the NEON per-MAG re-analysis, nmdc_results.annotation_kegg_orthology covers only 57% of NEON MetagenomeAnnotation workflows (1,799 / 3,137). [src: neon_mag_functional_discovery, pitfalls] The pitfalls digest notes that annotation_kegg_orthology (1.83 B rows), pfam_annotation_gff (2.68 B rows) and annotation_enzyme_commission (1.23 B rows) do not cover every workflow present in functional_annotation_agg. [src: pitfalls] The 43% gap is non-random and strongly correlated with habitat and genus. [src: pitfalls] See [[entities/nmdc-results-annotation-kegg-orthology]].

Coverage by genus group, with the share of the NB04b cohort that survived:

| Group | Per-gene KO coverage | NB04b outcome |
|---|---|---|
| Surface-water cyanobacteria (Planktothrix, Dolichospermum, Rubrivivax) | 100% | All 27 MAGs survived [src: neon_mag_functional_discovery, pitfalls] |
| Benthic generalists (Ferruginibacter, Flavobacterium, UBA953) | ~85% | 16 / 19 survived [src: neon_mag_functional_discovery, pitfalls] |
| Soil acidobacteria (Sulfotelmatobacter, Palsa-465, Palsa-1447) | ~30% | 12 / 40 survived [src: neon_mag_functional_discovery, pitfalls] |
| Soil cultured genera (Mycobacterium, Bradyrhizobium, Acidoferrum) | ~10% | 5 / 65 survived [src: neon_mag_functional_discovery, pitfalls] |
| Soil unculturable / novel (Acidocella, BOG-234, Pseudolabrys, Pseudonocardia, Reyranella) | 0% | 0 / 28 survived [src: neon_mag_functional_discovery, pitfalls] |

The H4 cohort of 246 MAGs collapsed to 73 MAGs across 19 genera, biased toward water habitats. [src: pitfalls] The 73-MAG cohort is a non-random 30% subset of the 246-MAG target, with 173 MAGs missing. [src: neon_mag_functional_discovery] The cohort over-represents water habitats, with cyanobacteria at 100% per-gene KO coverage and soil at 0–30%. [src: neon_mag_functional_discovery] The report also states the loss as a "53% cohort-attrition". [src: neon_mag_functional_discovery] That figure does not match the 246-to-73 count (173 of 246 missing); the cited claims do not give the denominator behind 53%, so the two numbers are stated here side by side and not reconciled. The report says the H4b analysis supports the hypothesis on the available cohort. [src: neon_mag_functional_discovery] Analyses that need the members_id to gene_id join silently drop genera with zero coverage. [src: pitfalls]

Two consequences follow. Five soil genera with strong a-priori monoterpene-/lactone-catabolism relevance returned 0 MAGs with per-gene KO data. [src: neon_mag_functional_discovery] The report says the fully attrited genera are novel-lineage candidates flagged by NB02, most likely in workflows not yet fully processed into per-gene tables. [src: neon_mag_functional_discovery] It treats the 15-MAG K14731 cohort and the dissected pathway-class distribution as lower bounds, because the full sub-Arctic peat soil cohort likely holds more carriers hidden by the gap. [src: neon_mag_functional_discovery] See [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]].

Whether other tables fill the gap is unknown. The report could not query pfam_annotation_gff and annotation_enzyme_commission per workflow with bounded SQL (structured query language), so it does not know if they cover the soil genera. [src: neon_mag_functional_discovery] Bounded queries on a single workflow_run_id time out because the tables have 2–3 B rows and the filter does not partition-prune cleanly. [src: pitfalls] The digest warns not to assume pfam_annotation_gff fills the gap. [src: pitfalls] The report proposes a PySpark scan on JupyterHub, estimated at ~30 minutes, to enable the H4 re-analysis for the soil genera that currently drop out. [src: neon_mag_functional_discovery] The report records the gap as a generalizable pitfall. [src: neon_mag_functional_discovery]

The digest's guidance is to document coverage per study and habitat first and treat effect sizes as cohort-conditional. [src: pitfalls] It prefers functional_annotation_agg for sample- or workflow-level KO/COG/Pfam analysis, because it covers essentially every workflow with annotation output. [src: pitfalls] It suits habitat-versus-chemistry analysis, PCoA (principal coordinates analysis) and PERMANOVA (permutational multivariate analysis of variance). [src: pitfalls] Per-gene tables should be used only when per-MAG resolution is essential, with cohort attrition reported. [src: pitfalls] See annotation and environmental metadata table gaps in the data lakehouse.

## Model and annotation limits

Some limits come from the analysis rather than the metadata. Partial correlations assume linear relationships between distance matrices. [src: ecotype_analysis] The GC linear/categorical model misses possible nonlinear effects. [src: gc_ecotype_ecology] GC is analysed at genome level only, so within-genome heterogeneity is not examined. [src: gc_ecotype_ecology]

Missing cohort members can be tested by sensitivity analysis. In NEON H4b, four estimators bound the effect of the 173 missing MAGs [src: neon_mag_functional_discovery]:

| Estimator | Median field-only KOs / MAG | Median Jaccard | Fraction of MAGs with ≥ 10 field-only KOs |
|---|---|---|---|
| Naive (observed only, n=73) | 371 | 0.43 | 100% [src: neon_mag_functional_discovery] |
| Inverse-coverage-reweighted (effective n=218) | 319 | 0.43 | 100% [src: neon_mag_functional_discovery] |
| Best-case imputation (missing MAGs = same-genus median) | 371 | not reported | 100% [src: neon_mag_functional_discovery] |
| Worst-case (missing MAGs = 0 field-only) | 0 | not reported | 29.7% [src: neon_mag_functional_discovery] |

The bootstrap 95% CI (confidence interval) on the reweighted median field-only KO (KEGG ortholog) count was 180–384, overlapping the naive 371 estimate. [src: neon_mag_functional_discovery] Only the worst-case scenario fails. It assigns zero field-only KOs to all 173 missing MAGs and drops the fraction with ≥10 to 29.7%, at the pre-registered 30% threshold. [src: neon_mag_functional_discovery] The report calls this unrealistic. None of the 5 fully attrited soil genera is a known monoterpene-naïve or aldehyde-dehydrogenase-only lineage. [src: neon_mag_functional_discovery] It places the realistic range between the inverse-coverage-reweighted and best-case scenarios, both of which fully support H4b. [src: neon_mag_functional_discovery]

## Open Directions

- Compare ENVO-based labels with keyword-harmonized labels on the 42% of genomes that have env_broad_scale. This would measure the accuracy of keyword classification.
- Test whether the 3,838 genomes lost to NaN embeddings differ by region or isolation source from the 79,449 valid ones. This would show whether filtering adds bias.
- Run the pending expedition-level clustering and log(n_MAGs) sampling-effort checks on the Atacama and USA hotspots.
- Tabulate per-biome coordinate loss in public archives, to answer which biomes are most underrepresented.
- Extract finer isolation-source categories and rerun the GC ecology model, to see whether the coarse scheme hides signal.
- Repeat the species-level environment tests with environmental metadata directly rather than embeddings.
- Run the PySpark per-workflow coverage scan of pfam_annotation_gff and annotation_enzyme_commission, to learn whether they fill the soil-genera gap.
- Stratify the AlphaEarth distance–embedding curves by environmental versus human-associated samples in other reports that pool them.
- Recompute the NEON attrition figure from the workflow counts to settle whether 53% or the 246-to-73 reduction is the right denominator.
- Rerun the Pseudomonas environment prediction at genome level with genome-specific isolation sources, and compare it with the majority-vote species result to see how many generalist species the vote hides.
