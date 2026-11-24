---
type: "Concept"
description: "Mapping heterogeneous isolation_source and ENVO metadata onto consistent environment categories, with coverage and residual-ambiguity limits; stops at coordinate quality."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Harmonizing free-text isolation source and environment metadata

This page covers mapping heterogeneous isolation_source and ENVO (Environment Ontology) metadata onto consistent environment categories. Keyword mapping labels most genomes, but a long tail stays "Other" or "Unknown". [src: env_embedding_explorer] Coverage depends on the unit: species-level majority votes cover far more than per-genome parsing. [src: amr_strain_variation, pitfalls] The evidence is a set of project-specific mappings, not one validated standard. The page stops at coordinate quality.

## What the metadata look like

The NCBI ncbi_env table holds 334 distinct harmonized attribute names across 4.1M rows. [src: env_embedding_explorer] The most populated are collection_date (273K genomes), geo_loc_name (272K) and isolation_source (245K). [src: env_embedding_explorer] In the AlphaEarth subset of 83,286 genomes, coverage differs sharply by field [src: env_embedding_explorer]:

| Field | Genomes | Share |
|---|---|---|
| geo_loc_name | 83,270 | 100.0% [src: env_embedding_explorer] |
| isolation_source | 76,295 | 91.6% [src: env_embedding_explorer] |
| host | 53,091 | 63.7% [src: env_embedding_explorer] |
| env_broad_scale | 34,800 | 41.8% [src: env_embedding_explorer] |
| env_local_scale | 31,541 | 37.9% [src: env_embedding_explorer] |
| env_medium | 31,483 | 37.8% [src: env_embedding_explorer] |

A separate bacterial master table gave different coverage: isolation_source 84%, host 58%, env_broad_scale 30%, lat_lon 47% and AlphaEarth 28%. [src: gc_ecotype_ecology] These are different datasets, so the figures are not directly comparable.

## Keyword harmonization of isolation_source

Several projects used keyword rules to collapse free text into broad classes. One mapped 5,774 unique isolation_source values to 12 categories. [src: env_embedding_explorer] The ecotype reanalysis reused the same 12 categories from 5,774 values. [src: discoveries] Another project harmonized isolation_source, env_broad_scale, env_local_scale and host into 11 categories. [src: phb_granule_ecology] A sanity check on GC content used 14 categories from conservative regex rules that favour "other" or unknown. [src: gc_ecotype_ecology] The lanthanide atlas used text-mining classes with hierarchical regex priorities. [src: lanthanide_methylotrophy_atlas]

In the 12-category mapping, 71% of genomes with a label were captured. Another 17% remained "Other" and 12.5% were "Unknown" because isolation_source was missing or null. [src: env_embedding_explorer] The 13,944 "Other" genomes (17%) were site-specific labels such as underground research labs, generic terms such as "water", and clinical sites the keywords missed. [src: env_embedding_explorer] Keyword matching also misses site-specific labels and non-English terms. [src: env_embedding_explorer] The report proposes adding keywords for clinical body sites, underground labs and generic water sources, with env_broad_scale as a fallback when isolation_source is ambiguous. [src: env_embedding_explorer] In the pgp_pangenome_ecology dataset, 291,279 genomes had ncbi_isolation_source and 93.5% were classifiable. [src: pgp_pangenome_ecology]

## Residual ambiguity

- Missing values: isolation_source is missing for ~16% of genomes in one dataset, and ~30% map only to "other". [src: gc_ecotype_ecology]
- Per-genome parsing of isolation_source and host from ncbi_env gave 52.7% "Unknown" (94,957/180,025 genomes) in amr_strain_variation, because most BioSample records lack structured isolation metadata. [src: pitfalls]
- In the PHB (polyhydroxybutyrate) granule analysis, 34.9% of species had "other_unknown" as primary environment. The report says enrichment results may underestimate the true signal. [src: phb_granule_ecology] That analysis had environment metadata for 293,050 genomes spanning all 27,690 species. [src: phb_granule_ecology]
- The gc_ecotype_ecology scheme is coarse and conservative, and finer categories likely exist but were not extracted. [src: gc_ecotype_ecology]
- Broad classes hide contexts. The "host_associated" class includes gut, skin, oral and infections. [src: lanthanide_methylotrophy_atlas] The lanthanide report says misclassification is possible but soil/sediment enrichment and host depletion survive. [src: lanthanide_methylotrophy_atlas]
- In the clay cohort, compartment is keyword-inferred from isolation_source. Some bentonite or "rock" entries could be porewater or rock-attached. [src: clay_confined_subsurface] That cohort was built from ncbi_env using clay-related isolation_source and env_* keywords, joined through genome.ncbi_biosample_id. [src: clay_confined_subsurface]
- Marine isolates may show non-significant environment associations partly because NCBI isolation-source resolution is insufficient. The report offers this as a possible explanation. [src: metabolic_capability_dependency] The same report proposes supplementing NCBI isolation source with BacDive or GTDB environmental labels. [src: metabolic_capability_dependency]

## Species-level aggregation

Aggregating to species raises coverage. An NCBI keyword classifier assigned environments to 91% of species (1,190/1,307). A classifier approximating BacDive assigned 35% (459/1,307). [src: amr_strain_variation] The pitfalls digest therefore recommends species-level majority-vote labels for cross-species work, with 91% coverage. [src: pitfalls] The plant census likewise used majority vote, with mean confidence 0.88. [src: plant_microbiome_ecotypes] It combined isolation_source regex matching with ncbi_env cross-validation, which upgraded 695 genomes. [src: plant_microbiome_ecotypes]

Majority vote has a cost. A species with 51% gut genomes is labelled human-associated. The report says continuous Spearman analysis addresses this and confirms the null result. [src: ecotype_env_reanalysis] With the harmonized scheme, 106/224 species in the ecotype analysis are majority human-associated (gut + clinical). The discoveries digest calls this more systematic than the earlier manual species-level categorization. It says the scheme confirms the clinical bias without confounding the ecotype results. [src: discoveries]

## ENVO fields as an alternative

The env_broad_scale ENVO field is cleaner than isolation-source text but covers only 42% of genomes. [src: env_embedding_explorer] Many of its values are bare ENVO identifiers without labels, or generic terms such as "not applicable" and "missing". [src: env_embedding_explorer] The reports propose repeating the ecotype analysis with these structured terms. [src: ecotype_env_reanalysis] They also propose comparing ENVO-based and keyword-based classes for the genomes that have env_broad_scale. [src: env_embedding_explorer]

## Open Directions

- Add the missing keyword classes and an env_broad_scale fallback, then re-measure the 17% "Other" share. [src: env_embedding_explorer]
- Compare ENVO-based classes with keyword classes for genomes with env_broad_scale, to measure accuracy. [src: env_embedding_explorer]
- Repeat the ecotype analysis with ENVO terms. [src: ecotype_env_reanalysis]
- Add BacDive or GTDB environmental labels and test whether they resolve the marine null associations. [src: metabolic_capability_dependency]

See also [[entities/ncbi-env-environmental-metadata]] and [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].
