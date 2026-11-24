---
type: "Dataset"
description: "64-dimension AlphaEarth geographic/environmental embeddings available for a subset of genomes, used to quantify environmental diversity and correlate environment with gene content."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/ecotype_analysis__REPORT.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/prophage_ecology__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["AlphaEarth", "AlphaEarth embeddings", "alphaearth_embeddings", "alphaearth_embeddings_all_years"]
---
# AlphaEarth environmental embeddings

AlphaEarth environmental embeddings (also AlphaEarth, alphaearth_embeddings, alphaearth_embeddings_all_years) are 64-dimension vectors that encode geographic and environmental context derived from satellite imagery at each genome's sampling location. [src: env_embedding_explorer] They exist for only a subset of genomes (28.4% of the pangenome database). [src: env_embedding_explorer] The discoveries report attributes the heavy clinical share of that subset to NCBI's bias toward pathogen sequencing. [src: discoveries] Many projects use the embeddings as a continuous environment measure and link environmental diversity to AMR (antimicrobial resistance), pathway content, prophage modules and PHB (polyhydroxybutyrate) ecology. The ecotype reanalysis finds that the clinical bias does not confound its environment–gene content relationship. [src: ecotype_env_reanalysis]

## Key facts

- The embeddings table covers 83,287 genomes, which is 28.4% of 293,059 total genomes in the pangenome database. [src: env_embedding_explorer] The KBase Data Lakehouse inventory also lists 83,287 embeddings indexed to KBase genomes. [src: berdl_data_atlas] Another report gives 83,227 of 293,059 genomes (28.4%) [src: pitfalls], and the GC ecotype study gives 83,227 genomes (28%). [src: gc_ecotype_ecology] These counts differ slightly and are stated as each report gave them.
- The table is part of the kbase_ke_pangenome collection. [src: berdl_data_atlas] See [[entities/kbase-ke-pangenome]].
- Of these genomes, 79,449 have valid embeddings in all 64 dimensions, and 3,838 have NaN (not a number) in at least one dimension. [src: env_embedding_explorer, discoveries] The pitfalls report gives the same figures: 3,838 of 83,287 genomes (4.6%), and filtering reduces the set from 83,287 to 79,449. [src: pitfalls]
- The dimensions A00–A63 have values in [-0.544, 0.544], mean near zero (-0.008), and mean standard deviation 0.109. [src: env_embedding_explorer]
- The embeddings span 135 phyla and 15,046 species. [src: env_embedding_explorer] They cover latitude -85 to +84 and longitude -178 to +180. [src: env_embedding_explorer]
- The env_embedding_explorer report describes itself as the first systematic characterization of this embedding space in the KBase Data Lakehouse. [src: env_embedding_explorer]
- The dimensions derive from satellite remote-sensing imagery at sample collection coordinates and capture signals such as vegetation, temperature, precipitation and land cover. [src: snipe_defense_system] The GC ecotype study describes them as a 64-d learned representation of remotely sensed local environment, with continuous climate, vegetation and land-cover gradients that only partly overlap with curator-supplied isolation labels. [src: gc_ecotype_ecology]
- The cause of the NaN values is unclear. The reports suggest missing satellite imagery or coordinates outside satellite coverage, such as polar regions or ocean. [src: discoveries, env_embedding_explorer] Affected genomes must be filtered before embedding-based analysis. [src: discoveries] Unfiltered NaNs can make UMAP, cosine distance and other operations fail or silently return NaN. [src: pitfalls]
- Loading the whole table (83K genomes × 65 columns) into pandas took under a minute in the GC ecotype study. [src: gc_ecotype_ecology]

## Coverage and sampling bias

Among genomes with embeddings, 38% are human-associated (clinical 20%, gut 16%, other 2%). Soil, marine and freshwater are 7% each. [src: discoveries] The discoveries report attributes this to NCBI's bias toward pathogen sequencing. Clinical isolates have good geographic metadata from epidemiological tracking, so they are over-represented. [src: discoveries] The pitfalls report says the embeddings need valid latitude/longitude, which NCBI metadata often lacks, especially for clinical isolates. [src: pitfalls] In contrast, the SNIPE defense-system report says coverage is biased toward environmental isolates with lat/lon data. [src: snipe_defense_system] These two descriptions of the bias point in different directions. See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]] and [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

At the species level, the gene function atlas audit of 18,989 species found AlphaEarth vectors for 27.2% (5,157 species). [src: gene_function_ecological_agora] The same report gives 27% species coverage as a caveat. [src: gene_function_ecological_agora] The audit also lists ncbi_env as 4.1M-row environment metadata. [src: gene_function_ecological_agora] See [[entities/ncbi-env-environmental-metadata]].

Other projects report the coverage limit on their own subsets:

- Pathway geography: only 6.8% of species (1,872/27,690) have at least 5 genomes with embeddings. The cause is missing latitude/longitude metadata for most NCBI genomes, especially clinical isolates. [src: discoveries]
- AMR work: the report says embeddings are biased toward genomes with geographic metadata. [src: amr_pangenome_atlas]
- Dark genes: coverage of 28% (83K/293K) plus inconsistent NCBI isolation-source metadata limits biogeographic tests. [src: functional_dark_matter]
- PHB ecology: 28% coverage may skew niche breadth toward better-sampled lineages. [src: phb_granule_ecology] The 2,008 species analyzed represent 7.2% of total species diversity. [src: phb_granule_ecology]
- Prophage ecology: the 28% coverage biases the subsample toward clinically and environmentally well-sampled lineages. [src: prophage_ecology]
- Lanthanide methylotrophy: coverage of xoxF genomes is 39.5% (1,457 / 3,690), better than the 28% pangenome baseline. [src: lanthanide_methylotrophy_atlas] That still leaves 60.5% of xoxF carriers without environmental coordinates. [src: lanthanide_methylotrophy_atlas]
- In the AlphaEarth genome dataset, 30,469 genomes (36.6%) sit at coordinates with more than 50 genomes of more than 10 species. [src: discoveries]

See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Geographic structure

For environmental genomes (Soil, Marine, Freshwater, Extreme, Plant), mean cosine distance between embeddings rises from 0.27 at <100 km to 0.90 at >10,000 km, a 3.4x ratio. [src: env_embedding_explorer, discoveries] Human-associated genomes (gut, clinical, other) show a flatter gradient, from 0.37 nearby to 0.75 far, only a 2.0x ratio. [src: env_embedding_explorer, discoveries] The report quantifies the signal as 3.4x for environmental and 2.0x for human-associated samples. [src: env_embedding_explorer, pitfalls] The report attributes this to hospitals worldwide having similar satellite imagery, so human-associated embeddings are more homogeneous regardless of geography. [src: discoveries]

The pooled all-samples curve (2.0x) is dominated by the 38% human-associated fraction. [src: discoveries] It blends two populations and underestimates the true geographic signal. [src: pitfalls, discoveries] The report recommends stratifying by sample type, or at minimum excluding human-associated samples. [src: discoveries] The pitfalls report gives the same advice: stratify by environment category and consider excluding human-associated samples when embeddings are an environment proxy. [src: pitfalls] It concludes the embeddings are most informative for environmental samples and least informative for clinical isolates. [src: env_embedding_explorer] See [[concepts/distance-decay-of-environmental-embeddings-with-geographic-distance]].

UMAP (uniform manifold approximation and projection) reduction of the 64 dimensions to 2D reveals substantial structure. [src: env_embedding_explorer] DBSCAN identifies 320 clusters. [src: env_embedding_explorer] Many clusters are dominated by a single environment category. [src: env_embedding_explorer] Rare types (Air, Extreme, Plant) concentrate in a few clusters. Human gut and clinical samples span many clusters, likely reflecting geographic sub-structure. [src: env_embedding_explorer] Coloring by phylum shows some taxonomic clustering. This is partly confounded with environment, for example Campylobacterota are predominantly gut-associated. [src: env_embedding_explorer]

### Computing with UMAP

Cosine-metric UMAP on 83K genomes with 64 dimensions took more than 60 minutes without completing on a single-CPU JupyterHub pod. [src: pitfalls] The report's fix is to L2-normalize the embeddings and use Euclidean distance, which it says gives equivalent topology because Euclidean distance is monotonically related to cosine distance for normalized vectors. [src: pitfalls] Fitting UMAP on a 20K subsample and transforming the full dataset cut runtime from more than 60 min to about 7 min. [src: pitfalls] See [[entities/umap]].

## Use in antimicrobial resistance analyses

The amr_environmental_resistome report used the alphaearth_embeddings_all_years table as continuous environment embeddings. [src: amr_environmental_resistome]

- amr_environmental_resistome: Among 2,659 species with AMR data and embeddings, 52 of 64 dimensions correlate significantly with AMR diversity (FDR < 0.05, false discovery rate), with A34 the top dimension (rho = +0.24). [src: amr_environmental_resistome]
- A Mantel test finds that embedding cosine distance predicts Bray-Curtis distance of AMR mechanism fractions (r = 0.098, p = 0.001). [src: amr_environmental_resistome] See [[entities/mantel-test]].
- Coupling is strongest in clinical species (r = 0.177), moderate in soil (r = 0.129) and weakest in aquatic (r = 0.061). [src: amr_environmental_resistome]
- The report says this continuous analysis confirms the discrete findings but adds limited interpretability, because the dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- amr_pangenome_atlas: Across 2,684 species with at least 3 genomes and embeddings, environmental diversity predicts AMR count (Spearman rho=0.466, p=1.6e-144). [src: amr_pangenome_atlas] Species from more diverse environments carry AMR genes that are less core (rho=-0.173, p=1.8e-19). [src: amr_pangenome_atlas]
- That report hypothesizes that niche breadth enables resistance accumulation through more opportunities for horizontal transfer. [src: amr_pangenome_atlas]

See [[concepts/environmental-structuring-of-antimicrobial-resistance-gene-content]].

## Use in pathway and ecotype analyses

In the pathway geography analysis, niche breadth from embedding diversity correlates with pathway completeness (r=0.392, p=7.1e-70), the strongest hypothesis signal. [src: discoveries] Embedding variance gives r=0.412, p=1.8e-77. [src: discoveries] Geographic distance alone gives r=0.360, p=1.8e-58, weaker than the embedding-based metrics. [src: discoveries]

The ecotype analysis used the alphaearth_embeddings table for environmental embeddings of geographic coordinates. [src: ecotype_analysis] It selected 224 species with at least 20 embedded genomes and at least 30% coverage. [src: ecotype_env_reanalysis] By genome-level isolation source, 106 (47%) are majority human-associated, 47 (21%) majority environmental and 71 (32%) mixed/other. [src: ecotype_env_reanalysis] The ecotype report notes 28.4% genome coverage limits the signal, and that the embeddings may not fully capture ecologically relevant variation. [src: ecotype_analysis]

The reanalysis predicted stronger environment–gene content correlations in environmental species, because their embeddings carry more geographic signal (3.4x vs 2.0x). [src: ecotype_env_reanalysis] It confirmed the clinical bias in the embedded subset but found the bias does not account for the weak environment signal. [src: ecotype_env_reanalysis] It concludes the bias does not confound the ecotype environment–gene content relationship. [src: ecotype_env_reanalysis] It proposes two explanations, both untested:

- The embeddings capture climate, vegetation and land use, which may not strongly predict gene content. [src: ecotype_env_reanalysis]
- They may capture regional epidemiological patterns, giving associations that are real but epidemiological rather than ecological. [src: ecotype_env_reanalysis]

The reanalysis drew on genome, alphaearth_embeddings_all_years, genome_ani, gene and gene_genecluster_junction tables. It also used env_embedding_explorer's data/alphaearth_with_env.csv for harmonized env_category per genome. [src: ecotype_env_reanalysis]

The GC ecotype study used AlphaEarth as a completely independent, continuous definition of environment, with no isolation_source text. [src: gc_ecotype_ecology] See [[concepts/independent-continuous-environment-embeddings-versus-categorical-isolation-source]] and [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

## Other uses

- Gene function atlas: NB25 used k-means to cluster 4,633 P1B species with AlphaEarth 64-dim embeddings into k=10 environmental clusters. [src: gene_function_ecological_agora] Separately, the data/p4d1_alphaearth_clusters.tsv dataset holds 5,157 rows of k=10 K-means environmental clusters. [src: gene_function_ecological_agora] The catalog lists 27.2% AlphaEarth coverage. [src: gene_function_ecological_agora]
- PHB ecology: embedding variance captures within-species variation in environmental context and serves as a proxy for niche breadth. [src: phb_granule_ecology] It gave a niche-breadth measure for 2,008 species with at least 5 genomes with embeddings per species. [src: phb_granule_ecology]
- Prophage ecology: across 2,008 species with at least 5 embedded genomes, niche breadth and prophage module count show a partial Spearman correlation controlling for genome size (rho=0.468, p=8.41e-110). [src: prophage_ecology] See [[concepts/environmental-structuring-of-prophage-gene-modules-beyond-host-phylogeny]].
- Dark genes: within-species carrier versus non-carrier tests controlling for phylogeny found AlphaEarth embedding divergence in 1/67 clusters. [src: functional_dark_matter] Of 151 testable accessory dark gene clusters across 31 species, 1 showed significant divergence. [src: functional_dark_matter]
- SNIPE defense system: the environmental analysis joins the 64-dimension, 83K-genome table to SNIPE species labels. [src: snipe_defense_system] It identifies statistical signals but does not map individual dimensions to named environmental variables. [src: snipe_defense_system] See [[concepts/environmental-niche-association-of-defense-system-carriers]].
- Lanthanide methylotrophy: embedding-based niche analysis of xoxF genomes was scoped out, although a coverage-restricted supplementary analysis is feasible. [src: lanthanide_methylotrophy_atlas] See [[concepts/environmental-association-of-lanthanide-dependent-methanol-oxidation-genes]].

## Proposed follow-up in the reports

The env_embedding_explorer report proposes correlating A00–A63 with latitude, temperature, precipitation, NDVI or land cover to learn what each dimension encodes. [src: env_embedding_explorer] The ecotype report proposes trying alternative embedding distance metrics, or using environmental metadata directly. [src: ecotype_analysis] The PHB report proposes using the full 64 dimensions with dimensionality reduction to map PHB+ and PHB- species in environmental space. [src: phb_granule_ecology] The discoveries report's stratification advice also implies repeating the AMR and pathway correlations by sample type. [src: discoveries]
