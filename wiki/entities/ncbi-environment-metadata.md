---
type: Dataset
description: Genome-associated environmental metadata used for habitat classification
  and ecological analysis
sources:
- id: amr_environmental_resistome
  resource: ../summaries/amr_environmental_resistome__REPORT.md
  title: amr environmental resistome
- id: amr_pangenome_atlas
  resource: ../summaries/amr_pangenome_atlas__REPORT.md
  title: amr pangenome atlas
- id: amr_strain_variation
  resource: ../summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: ecotype_env_reanalysis
  resource: ../summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
- id: env_embedding_explorer
  resource: ../summaries/env_embedding_explorer__REPORT.md
  title: env embedding explorer
- id: pgp_pangenome_ecology
  resource: ../summaries/pgp_pangenome_ecology__REPORT.md
  title: pgp pangenome ecology
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
- id: plant_microbiome_ecotypes
  resource: ../summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: prophage_ecology
  resource: ../summaries/prophage_ecology__REPORT.md
  title: prophage ecology
title: NCBI Environment Metadata
---
# NCBI Environment Metadata

## What this entity is

**Canonical name:** NCBI environment metadata. [^amr_environmental_resistome]

**Known aliases:** NCBI environmental metadata; genome environment metadata. [^amr_environmental_resistome]

**Stable external identifier:** Not reported in the source documents. [^amr_environmental_resistome][^env_embedding_explorer]

NCBI environment metadata is genome-associated environmental information used to classify bacterial genomes into categories such as clinical, human gut, soil, aquatic, host-associated, and other environmental sources. [^amr_environmental_resistome] It includes fields such as geo_loc_name, isolation_source, host, env_broad_scale, env_local_scale, and env_medium, supporting habitat harmonization and continuous-environment analyses. [^env_embedding_explorer]

The [pgp_pangenome_ecology__REPORT](../summaries/pgp_pangenome_ecology__REPORT.md) **extends** these uses to plant-growth-promoting gene distributions: its BERDL pangenome analysis used isolation-source metadata for 291,279 genomes, of which 93.5% were classifiable, and conservatively identified 1,637 species (5.9% of species with an environment label) as soil/rhizosphere dominant. [^pgp_pangenome_ecology] The plant-microbiome analysis **extends** this use to compartment-specific classification, identifying 7,995 plant-associated genomes among 293,059 GTDB r214 genomes across root, rhizosphere, phyllosphere, endophyte, and other plant contexts. [^plant_microbiome_ecotypes] This **supports** concerns that free-text environmental metadata are incomplete and noisy, while showing that the resource can test soil-associated gene enrichment and plant-compartment associations. [^pgp_pangenome_ecology][^plant_microbiome_ecotypes]

## Key facts in the source

The assembled dataset contained 280,337 genomes with NCBI environment metadata. [^amr_environmental_resistome] Of those genomes, 93.5% were classified at the genome level. [^amr_environmental_resistome] Species-level majority-vote environment classifications covered 95% of species, corresponding to 13,981 species. [^amr_environmental_resistome]

These classifications were used to compare AMR gene-cluster diversity across environments in the [amr_environmental_resistome__REPORT](../summaries/amr_environmental_resistome__REPORT.md). [^amr_environmental_resistome] Clinical-source species had a median of 5 AMR gene clusters, compared with 2 in soil, aquatic, and host-associated species. [^amr_environmental_resistome] The environment–AMR association remained present at 50%, 60%, 75%, and 90% majority-vote thresholds, with η² values from 0.044 to 0.056. [^amr_environmental_resistome]

Environment classifications were integrated with [kbase-ke-pangenome](kbase-ke-pangenome.md) to analyze 82,908 AMR gene clusters across 14,723 bacterial species and 293K genomes. [^amr_environmental_resistome] The newer atlas **refines** this integration: among 14,723 AMR-carrying species, 7,838 (53.2%) received a non-Other/Unknown classification across 6 categories, while 46.8% remained Other/Unknown because of sparse and inconsistent free-text isolation_source metadata in NCBI BioSample records. [^amr_pangenome_atlas]

The atlas reports 10.6 AMR clusters per Human/Clinical species, versus 4.6 for Soil/Terrestrial, 3.9 for Aquatic, and 3.0 for Animal; this **supports** the clinical-versus-environmental contrast while its restricted classification coverage qualifies the comparison. [^amr_pangenome_atlas] A separate NCBI keyword-based classifier assigned environments to 1,190/1,307 species (91%) and found higher AMR burden in host-associated species than in terrestrial or aquatic species, with Kruskal-Wallis p < 0.05; human-clinical isolates had the highest burden. [^amr_strain_variation] A rule-based approximation of BacDive categories classified 459/1,307 species (35%) and agreed in direction, but both classifiers are approximate. [^amr_strain_variation]

The ecotype analysis **extends** metadata use from categorical AMR comparisons to genome-wide gene-content similarity: among 172 species with sufficient data, the median partial correlation was 0.0025 for environment versus 0.0143 for phylogeny, and phylogeny dominated in 60.5% of species. [^ecotype_analysis] A significant positive environmental effect occurred in 12 species (7.0%), a significant negative effect in 4 species (2.3%), and no significant effect in 156 species (90.7%). [^ecotype_analysis] This **refines** interpretation by suggesting that environmental effects may be concentrated in specific gene subsets rather than genome-wide gene content. [^ecotype_analysis]

The reanalysis **supports** the original ecotype null conclusion while **refining** classification: among 224 species meeting thresholds of >=20 genomes with AlphaEarth embeddings and >=30% coverage, 106 (47%) were majority human-associated, 47 (21%) majority environmental, and 71 (32%) Mixed/Other. [^ecotype_env_reanalysis] Environmental species had a median partial correlation of 0.051, versus 0.084 for human-associated and 0.109 for Mixed/Other species; the one-sided Mann-Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83. [^ecotype_env_reanalysis] Continuous Spearman analyses found no relationship between environmental fraction and partial-correlation strength (rho=-0.085, p=0.25), or between human-associated fraction and correlation strength (rho=0.030, p=0.69). [^ecotype_env_reanalysis]

These results **contradict** the hypothesis that clinical sampling bias in the AlphaEarth subset explains the weak environment–gene-content relationship. [^ecotype_env_reanalysis] Of 30 species with NaN partial correlations, the NaN rate was 10/47 = 21% for Environmental, 13/66 = 20% for Mixed/Other, and 7/100 = 7% for Human-associated species. [^ecotype_env_reanalysis]

The AlphaEarth environment explorer **refines** the metadata context by analyzing 83,287 pangenome genomes with 64-dimensional satellite-derived embeddings: 38% were human-associated, including 16,390 Human clinical, 13,466 Human gut, and 1,669 Human other genomes; Soil, Marine, and Freshwater contributed 6,073, 5,850, and 5,840 genomes, respectively. [^env_embedding_explorer] Isolation_source was available for 76,295 (91.6%), host for 53,091 (63.7%), env_broad_scale for 34,800 (41.8%), env_local_scale for 31,541 (37.9%), and env_medium for 31,483 (37.8%). [^env_embedding_explorer]

A keyword workflow mapped 5,774 unique isolation_source values to 12 broad categories, capturing 71% of genomes with a label; 17% were Other and 12.5% were Unknown because isolation_source was missing or null. [^env_embedding_explorer] The NCBI ncbi_env table contained 334 distinct harmonized attribute names across 4.1M rows; collection_date, geo_loc_name, and isolation_source were populated for 273K, 272K, and 245K genomes, respectively. [^env_embedding_explorer] These figures **support** metadata-sparsity concerns while showing that structured fields provide a cleaner but incomplete fallback. [^env_embedding_explorer]

The [prophage_ecology__REPORT](../summaries/prophage_ecology__REPORT.md) **extends** these metadata applications from AMR and ecotype analyses to prophage-module ecology: across 27,702 bacterial species, environmental categories derived from genome-associated metadata were tested alongside genome size and family-level phylogeny. [^prophage_ecology] In a 1,773-species subsample, environment significantly affected prophage-module composition (PERMANOVA p=0.01, F=30.04) beyond phylogeny (F=6.17), while genome size was dominant (F=212.99); within genome-size quartiles, environmental effects remained significant with all p < 6.5e-78. [^prophage_ecology] Constrained analysis across 18,031 species identified 8 significant module-by-environment enrichments at FDR < 0.05, including tail, head morphogenesis, and anti-defense enrichment in human-associated environments. [^prophage_ecology] This **supports** the use of environment metadata for module-level ecological comparisons, while the source's 9,659-species (35%) other_unknown category **refines** interpretation by showing that coarse or missing labels still limit resolution. [^prophage_ecology]

The prophage study also **extends** metadata integration to 6,365 NMDC metagenomic samples: taxonomy-based prophage-burden inference achieved 87.2% median matching coverage and found 57 significant module–abiotic correlations at FDR < 0.05, with the strongest reported association being packaging with pH (Spearman rho=0.519). [^prophage_ecology] This cross-collection result is an environmental association rather than a causal demonstration, and the indirect genus-level burden inference had not been independently validated for prophage genes. [^prophage_ecology]

The new [pitfalls](../summaries/pitfalls.md) **refines** these coverage estimates by documenting that `ncbi_env` is entity-attribute-value data rather than a flat genome-metadata table. [^pitfalls] Metadata extraction therefore requires joining `genome.ncbi_biosample_id` to `ncbi_env.accession`, filtering attributes, and pivoting the long format. [^pitfalls] A separate per-genome classification yielded 52.7% unknown labels, or 94,957 of 180,025 genomes, because most BioSample records lacked structured isolation metadata; species-level majority-vote keyword classification reached 91% coverage. [^pitfalls] These figures are dataset- and workflow-specific and **do not contradict** the higher coverage reported for the filtered AlphaEarth and pangenome subsets. [^pitfalls]

The plant-microbiome analysis **refines** the interpretation of compartment labels: among 607 root, rhizosphere, and phyllosphere species, refined Jaccard profiles produced PERMANOVA R² = 0.071 and db-RDA location-only R² = 0.060, with 84% of the PERMANOVA signal attributable to centroid shifts and 16% to dispersion. [^plant_microbiome_ecotypes] The earlier R² = 0.527 fell to R² = 0.072 after excluding three genome-rich species per compartment, indicating that much of the initial effect reflected taxonomic sampling rather than a community-wide compartment signal. [^plant_microbiome_ecotypes] This **supports** treating isolation_source-derived plant categories as weak, taxonomically confounded habitat evidence rather than species-level ecological discriminators. [^plant_microbiome_ecotypes]

AlphaEarth cosine distance increased monotonically with geographic distance, from 0.41 at <100 km to 0.82 at 10K–20K km, with a plateau above 5,000 km. [^env_embedding_explorer] Environmental samples showed a 3.4x geographic gradient, versus 2.0x for human-associated samples, **refining** interpretation of geographic interchangeability. [^env_embedding_explorer] The pitfalls analysis **supports** stratifying by environment category or excluding human-associated samples: the pooled geographic distance–embedding distance curve had a 2.0x near-versus-far ratio, compared with 3.4x for environmental samples and 2.0x for human-associated samples. [^pitfalls] This does not establish a stronger environment–gene-content relationship and instead motivates analyses of environmental-only samples with sampling and metadata-quality controls. [^env_embedding_explorer]

The PGP pangenome analysis **extends** environment-stratified gene-distribution analysis beyond AMR: among 1,039 soil/rhizosphere species and 10,233 species from other environments, acdS, pqqC, and hcnC were soil-enriched, whereas nifH was depleted; acdS enrichment remained strong after phylum-level fixed effects and in a strict rhizosphere-only sensitivity analysis. [^pgp_pangenome_ecology] This result is observational and does not remove the classification limitations described above. [^pgp_pangenome_ecology]

The plant-microbiome analysis further **extends** metadata-linked ecological analysis to host and plant-compartment structure: it identified 1,307 plant-associated species across 19 testable hosts, but only 11.7% Jaccard overlap between 487 pangenome-derived plant genera and 438 MGnify rhizosphere genera. [^plant_microbiome_ecotypes] This **supports** the existing warning that isolation metadata and metagenomic detection measure different phenomena and should not be treated as interchangeable habitat labels. [^plant_microbiome_ecotypes]

## Limitations in interpretation

NCBI sampling overrepresented clinical isolates, while soil and aquatic species were undersampled, which may inflate the clinical-versus-environmental AMR contrast. [^amr_environmental_resistome] Majority-vote species classifications collapsed within-species environmental variation, although threshold sensitivity analyses partly assessed this limitation. [^amr_environmental_resistome] Environment and phylogeny remained deeply entangled despite family-level controls, and only 14% of tested families showed significant within-family environment effects after false-discovery-rate correction. [^amr_environmental_resistome] The source supports an observational association rather than a causal conclusion about environmental exposure and AMR. [^amr_environmental_resistome]

The atlas **supports** metadata-sparsity concerns: 46.8% of AMR-carrying species were Other/Unknown, and comparison was restricted to 7,838 non-Other/Unknown species. [^amr_pangenome_atlas] The within-species analysis **refines** this limitation: 52.7% of genomes had no classifiable isolation_source, leaving only 2 species with sufficient within-species environmental diversity for strict environment–ecotype chi-squared tests. [^amr_strain_variation] AlphaEarth embeddings covered only 28% of genomes and were biased toward genomes with geographic metadata. [^amr_pangenome_atlas]

The prophage analysis **supports** these warnings: only 28% of genomes had AlphaEarth environmental embeddings, the 10 environmental categories collapsed substantial within-category variation, and other_unknown contained 9,659 species (35%). [^prophage_ecology] Its environmental effects therefore demonstrate metadata-linked association, not a fully resolved habitat mechanism; dedicated prophage detection was also absent, and NMDC burden estimates assumed genus-level conservation. [^prophage_ecology]

The ecotype analysis **supports** incomplete environmental representation: AlphaEarth embeddings covered only 28.4% of genomes, coordinates were often missing or imprecise, and host-associated coordinates may describe collection sites rather than actual microenvironments. [^ecotype_analysis] It found no significant difference in environmental effects between environmental and host-associated bacteria (p=0.66), but this result is limited by those constraints. [^ecotype_analysis] Its partial-correlation approach assumes linear relationships between distance matrices and may miss nonlinear effects. [^ecotype_analysis]

The explorer **refines** the coordinate limitation: among 83,286 genomes with coordinates, 50,109 (60.2%) were Good, 30,469 (36.6%) Suspicious cluster, and 2,708 (3.3%) Low precision. [^env_embedding_explorer] Suspicious-cluster heuristics can flag legitimate field sites as well as institutional addresses, so isolation_source homogeneity is needed before treating geographic metadata as reliable habitat evidence. [^env_embedding_explorer] Its AlphaEarth subset contained 3,838 genomes with at least one NaN among 64 dimensions, with cause unresolved. [^env_embedding_explorer] The pitfalls quality check likewise found 3,838 of 83,287 genomes, or 4.6%, with at least one NaN among 64 dimensions; filtering left 79,449 genomes. [^pitfalls]

The reanalysis **refines** cross-method interpretation: its median partial correlation across all 183 species was 0.081 versus 0.003 originally, characterized as a 27x difference, because it used all genomes with embeddings, including up to 3,505 genomes per species, rather than diversity-maximizing downsampling capped at 250 genomes. [^ecotype_env_reanalysis] Absolute correlations are not comparable across methodologies, but the Environmental versus Human-associated comparison used one consistent methodology. [^ecotype_env_reanalysis] Klebsiella pneumoniae was excluded after exceeding Spark's maxResultSize during gene-cluster extraction and consequently had no correlation data. [^ecotype_env_reanalysis]

The reanalysis suggests, rather than establishes, that AlphaEarth embeddings may capture regional epidemiological patterns in human-associated species rather than ecologically relevant variation; environmental embeddings had a 3.4x geographic-signal ratio versus 2.0x for human-associated embeddings. [^ecotype_env_reanalysis] Unresolved tests include downsampled versus full-genome extraction, functional gene subsets, structured ENVO terms, and genome-count covariate control. [^ecotype_env_reanalysis] The PGP analysis likewise notes that soil classification is conservative and noisy, and that its observed enrichment may underestimate true rhizosphere enrichment. [^pgp_pangenome_ecology]

The plant-microbiome analysis **refines** these limitations: only 7,995 of 293,059 genomes, or 2.7%, had plant-associated annotations, the endophyte category contained only 29 species, and plant labels were inferred primarily from variable NCBI isolation_source metadata. [^plant_microbiome_ecotypes] Its corrected compartment effect was weak, and its host/subclade analysis was testable for only 18 of 65 candidate species because of incomplete phylogenetic-tree coverage. [^plant_microbiome_ecotypes] Thus, plant-associated classifications provide useful hypotheses but do not establish causal habitat specialization or broad species-level ecotypes. [^plant_microbiome_ecotypes]

The pitfalls document further **refines** reproducibility requirements: NCBI environment joins should begin with live schema inspection, because table schemas, naming conventions, access, and metadata contents can change; missing attributes or zero joins must not be interpreted as biological absence. [^pitfalls] Free-text isolation-source labels require explicit keyword or synonym reconciliation, and classifications should retain the original accession, attribute, and transformation provenance. [^pitfalls]

## Related pages

- [kbase-ke-pangenome](kbase-ke-pangenome.md) — pangenome collection linked to environment metadata. [^amr_environmental_resistome]
- [amrfinderplus](amrfinderplus.md) — AMR annotation resource used in the resistance-gene analysis. [^amr_environmental_resistome]
- [alph-aearth](alph-aearth.md) — supplementary continuous environmental embedding dataset. [^amr_environmental_resistome]
- [environmental-resistome](../concepts/environmental-resistome.md) — cross-project synthesis of environment-associated AMR patterns. [^amr_environmental_resistome]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — environmental similarity and bacterial gene-content variation. [^env_embedding_explorer]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — geographic and environment-stratified AlphaEarth behavior. [^env_embedding_explorer]
- [provenance-aware-resource-discovery](../concepts/provenance-aware-resource-discovery.md) — live schema discovery, entity-attribute-value extraction, and provenance-preserving metadata joins. [^pitfalls]
- [amr_pangenome_atlas__REPORT](../summaries/amr_pangenome_atlas__REPORT.md) — pan-bacterial AMR atlas integrating environmental metadata, pangenomes, and fitness data. [^amr_pangenome_atlas]
- [amr_strain_variation__REPORT](../summaries/amr_strain_variation__REPORT.md) — within-species AMR variation and environmental classification. [^amr_strain_variation]
- [ecotype_analysis__REPORT](../summaries/ecotype_analysis__REPORT.md) — environmental and phylogenetic predictors of gene-content similarity. [^ecotype_analysis]
- [ecotype_env_reanalysis__REPORT](../summaries/ecotype_env_reanalysis__REPORT.md) — reanalysis of clinical sampling bias and environment–gene-content relationships. [^ecotype_env_reanalysis]
- [env_embedding_explorer__REPORT](../summaries/env_embedding_explorer__REPORT.md) — AlphaEarth embeddings, geography, coordinate quality, and environment harmonization. [^env_embedding_explorer]
- [pgp_pangenome_ecology__REPORT](../summaries/pgp_pangenome_ecology__REPORT.md) — plant-growth-promoting gene distribution across environments and pangenomes. [^pgp_pangenome_ecology]
- [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md) — plant compartments, host associations, and metadata-linked genomic ecology. [^plant_microbiome_ecotypes]
- [prophage_ecology__REPORT](../summaries/prophage_ecology__REPORT.md) — prophage-module composition, environmental gradients, TerL lineages, and NMDC validation. [^prophage_ecology]
- [pitfalls](../summaries/pitfalls.md) — database, metadata, join, coverage, and reproducibility pitfalls affecting environmental classification. [^pitfalls]

[^amr_environmental_resistome]: [amr environmental resistome](../summaries/amr_environmental_resistome__REPORT.md)
[^env_embedding_explorer]: [env embedding explorer](../summaries/env_embedding_explorer__REPORT.md)
[^pgp_pangenome_ecology]: [pgp pangenome ecology](../summaries/pgp_pangenome_ecology__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../summaries/plant_microbiome_ecotypes__REPORT.md)
[^amr_pangenome_atlas]: [amr pangenome atlas](../summaries/amr_pangenome_atlas__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../summaries/ecotype_env_reanalysis__REPORT.md)
[^prophage_ecology]: [prophage ecology](../summaries/prophage_ecology__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
