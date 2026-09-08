---
title: Ecological Genomic Inference Biases
type: Topic
sources:
- id: ecotype_analysis
  resource: ../../wiki/summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: euk_in_prok_correlates
  resource: ../../wiki/summaries/euk_in_prok_correlates__REPORT.md
  title: euk in prok correlates
- id: enigma_carbon_census_1
  resource: ../../wiki/summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
- id: bacdive_metal_validation
  resource: ../../wiki/summaries/bacdive_metal_validation__REPORT.md
  title: bacdive metal validation
- id: bacdive_phenotype_metal_tolerance
  resource: ../../wiki/summaries/bacdive_phenotype_metal_tolerance__REPORT.md
  title: bacdive phenotype metal tolerance
- id: microbeatlas_metal_ecology
  resource: ../../wiki/summaries/microbeatlas_metal_ecology__REPORT.md
  title: microbeatlas metal ecology
- id: plant_microbiome_ecotypes
  resource: ../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: env_embedding_explorer
  resource: ../../wiki/summaries/env_embedding_explorer__REPORT.md
  title: env embedding explorer
- id: ecotype_env_reanalysis
  resource: ../../wiki/summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
- id: pgp_pangenome_ecology
  resource: ../../wiki/summaries/pgp_pangenome_ecology__REPORT.md
  title: pgp pangenome ecology
- id: prophage_ecology
  resource: ../../wiki/summaries/prophage_ecology__REPORT.md
  title: prophage ecology
- id: functional_dark_matter
  resource: ../../wiki/summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: ecotype_functional_differentiation
  resource: ../../wiki/summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
- id: soil_metal_functional_genomics
  resource: ../../wiki/summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
- id: enigma_contamination_functional_potential
  resource: ../../wiki/summaries/enigma_contamination_functional_potential__REPORT.md
  title: enigma contamination functional potential
- id: pitfalls
  resource: ../../wiki/summaries/pitfalls.md
  title: pitfalls
---
# Ecological Genomic Inference Biases

Ecological genomic inference asks how environmental context, organismal traits, and genomic content are related, but the corpus shows that every stage of this chain is shaped by representation: which organisms are sampled, which metadata are recorded, which taxa and functions databases can recognize, and which ecological contrasts remain testable. Across comparative genomics, metagenomics, phenotype databases, pangenomes, and functional models, environmental signals are often detectable but are rarely portable, genome-wide, or directly interpretable as adaptation without explicit controls for lineage, coverage, callability, and study structure. [^ecotype_analysis][^euk_in_prok_correlates][^enigma_carbon_census_1]

## Literature Context

Published work increasingly treats microbiome and comparative-genomic inference as a measurement problem rather than a direct readout of ecological function. Robinson et al. explicitly warn that microbiome metrics can obscure ecological meaning, while Luo et al. show that DNA-based data do not necessarily provide straightforward abundance estimates. [PMID 42418242](https://pubmed.ncbi.nlm.nih.gov/42418242/) [PMID 35986714](https://pubmed.ncbi.nlm.nih.gov/35986714/) Yu et al. similarly identify database scope, heterogeneous sampling, validation, and transfer across systems as central obstacles for AI-based predictive ecosystems. [PMID 42208955](https://pubmed.ncbi.nlm.nih.gov/42208955/) Work on hidden viral diversity makes the same point from a discovery perspective: reservoir inference depends on where and how one looks, and poorly sampled hosts or environments can conceal substantial diversity. [PMID 32672814](https://pubmed.ncbi.nlm.nih.gov/32672814/) [PMID 40975788](https://pubmed.ncbi.nlm.nih.gov/40975788/) This literature is therefore consistent with the hub’s emphasis on callability, metadata completeness, classifier/database compatibility, and study-held-out validation.

The corpus extends that literature by quantifying how representation changes ecological-genomic conclusions across linked resources. Its BacDive bridges, AlphaEarth coverage analysis, and plant-associated genome comparisons show that missing metadata and uneven genome representation can alter effect sizes before ecological modeling begins. The finding that a large preliminary plant-compartment effect collapses after removing genome-rich species is a concrete genomic example of the metric-level “ecological mirage” described by Robinson et al., while the corpus’s distinction between detected environmental structure and transportable prediction operationalizes the validation concerns raised by Yu et al. [PMID 42418242](https://pubmed.ncbi.nlm.nih.gov/42418242/) [PMID 42217053](https://pubmed.ncbi.nlm.nih.gov/42217053/) The corpus also extends prior evolutionary work by showing that phylogeny can dominate genome-wide environmental similarity even when narrower gene or prophage signals remain detectable. That interpretation is compatible with evidence that bacterial genome diversity is shaped by mechanisms such as genetic competence and that evolutionary rates vary across bacterial lineages, rather than being determined by a single ecological axis. [PMID 29272410](https://pubmed.ncbi.nlm.nih.gov/29272410/) [PMID 28348834](https://pubmed.ncbi.nlm.nih.gov/28348834/)

Some corpus results are more specifically novel or remain in tension with the candidate literature. The corpus’s study-held-out failure for eukaryotic-read environment prediction, despite stronger random cross-validation performance, provides a direct cross-study portability test not established by the broader methodological warnings. Its result that environmental signals can persist in selected genes or prophage modules while disappearing at the whole-genome level also sharpens the distinction between localized adaptation and ecotype-wide structure. That distinction should be interpreted cautiously because phylogenetic reconstruction itself can be distorted by compositionally constrained sites and long-branch attraction. [PMID 36946562](https://pubmed.ncbi.nlm.nih.gov/36946562/) Finally, host- or system-specific experimental studies show why ecological associations should not automatically be generalized: cross-species engraftment can produce metabolic divergence in gnotobiotic mice, and plant or soil marker studies depend on which taxa and molecular features are detectable. [PMID 41277418](https://pubmed.ncbi.nlm.nih.gov/41277418/) [PMID 33051582](https://pubmed.ncbi.nlm.nih.gov/33051582/) Thus, the corpus is broadly consistent with published concerns about inference bias, but its integrated demonstrations of callability, sampling depth, lineage control, and transportability provide a more explicit framework for diagnosing when an environmental genomic signal is portable, localized, or representation-dependent.

## What the Corpus Shows

**The observed genome collection is not the ecological population.** Cultivated and publicly deposited genomes overrepresent organisms that are culturable, described, repeatedly studied, or accompanied by usable metadata. In the BacDive–pangenome bridge, 42,227 of 97,334 strains matched 6,426 GTDB species, while 55,107 strains remained unmatched; only 25,089 matched strains had isolation-source metadata. [^bacdive_metal_validation] A related phenotype bridge matched 37,368 strains to 5,647 GTDB species, but feature coverage varied sharply: 43,378 strains had isolation-source data, compared with 1,980 with acetate-utilization data. [^bacdive_phenotype_metal_tolerance] MicrobeAtlas likewise treats inferred niche breadth as a sequencing-effort proxy rather than confirmed ecological range; sequenced-genome coverage correlated with inferred metal-type diversity (r = 0.35, p = 2.6×10⁻¹⁹). [^microbeatlas_metal_ecology] Plant-associated inference begins from similarly sparse metadata: only 7,995 of 293,059 genomes (2.7%) had plant-associated annotations. [^plant_microbiome_ecotypes]

This means that a strong association may indicate that a lineage is better represented in a habitat, not that the measured trait is broadly selected there. In plant-associated comparisons, the preliminary compartment effect had R² = 0.527 but fell to R² = 0.072 after excluding three genome-rich species per compartment, an 86% loss. [^plant_microbiome_ecotypes] The refined effect remained statistically detectable, with PERMANOVA R² = 0.071 and location-only distance-based redundancy analysis (db-RDA) R² = 0.060, but most of the signal was attributable to centroid shifts rather than dispersion. [^plant_microbiome_ecotypes] The broader lesson is developed in [cultivation-collection-bias-in-ecological-genomics](../../wiki/concepts/cultivation-collection-bias-in-ecological-genomics.md) and [phenotype-database-coverage-bias](../../wiki/concepts/phenotype-database-coverage-bias.md).

**Environmental labels and embeddings are measurements, not neutral context.** Geographic coordinates may identify a collection site rather than the microenvironment experienced by a host-associated organism. [^ecotype_analysis] AlphaEarth embeddings covered 83,287 genomes, only 28.4% of 293,059 KBase pangenome genomes; the embedded subset was strongly human-associated, including 16,390 Human clinical, 13,466 Human gut, and 1,669 Human other genomes. [^env_embedding_explorer] Species-level labels can also conceal mixed sampling: in one reanalysis, 106 of 224 species (47%) were majority human-associated, 47 (21%) majority environmental, and 71 (32%) Mixed/Other. [^ecotype_env_reanalysis]

Sampling depth changes the apparent magnitude of ecological association. A reanalysis using all genomes with embeddings, including as many as 3,505 genomes per species, reported a median partial correlation of 0.081 across 183 species, compared with 0.003 in an earlier diversity-maximized analysis capped at 250 genomes per species; the report characterizes this as 27x, while warning that the absolute values are not comparable because genome sets and procedures differed. [^ecotype_env_reanalysis] Within the reanalysis method, however, environmental species did not show stronger environment–gene-content correlations than human-associated species: median partial correlations were 0.051 and 0.084, respectively, with one-sided Mann–Whitney U = 1536 and p = 0.83. [^ecotype_env_reanalysis] These findings motivate [sampling-depth-and-downsampling-effects](../../wiki/concepts/sampling-depth-and-downsampling-effects.md) and [environment-embedding-geography](../../wiki/concepts/environment-embedding-geography.md).

**Lineage and taxonomic resolution can dominate ecological interpretation.** Across 172 species, phylogeny generally explained genome-wide gene-content similarity better than environmental similarity: median partial correlations were 0.0143 for phylogeny and 0.0025 for environment; phylogeny dominated in 60.5% of species, and no significant environmental effect was detected in 156 species (90.7%). [^ecotype_analysis] This does not imply that ecological adaptation is absent. It suggests that broad ancestry can obscure signals concentrated in particular loci, pathways, or functional categories, as discussed in [genome-wide-versus-locus-specific-ecological-adaptation](../../wiki/concepts/genome-wide-versus-locus-specific-ecological-adaptation.md).

Functional and gene-level analyses indeed recover narrower ecological structure. In a plant-growth-promoting gene analysis, acdS prevalence was 15.8% in soil/rhizosphere species versus 2.6% in other environments, with OR = 7.02 and q = 5.1e-62; pqqC prevalence was 43.8% versus 21.2%, with OR = 2.90 and q = 2.8e-53. [^pgp_pangenome_ecology] Eight of 10 focal-gene pairs were significant after Benjamini–Hochberg false-discovery-rate correction, but co-occurrence does not establish physical linkage or complementary metabolism. [^pgp_pangenome_ecology][^plant_microbiome_ecotypes] Similarly, prophage-module composition retained an environmental effect after genome-size and family-level comparisons, although genome size was dominant (F = 212.99 versus environment F = 30.04 and phylogeny F = 6.17). [^prophage_ecology] The distinction between gene-specific guild signals and whole-genome ecotypes is developed in [gene-cooccurrence-ecological-guilds](../../wiki/concepts/gene-cooccurrence-ecological-guilds.md) and [ecotype-clustering-validity](../../wiki/concepts/ecotype-clustering-validity.md).

**Database callability creates unequal evidence, not evidence of absence.** “Callability” means that a feature can be connected through the queried resources to an organism, pathway, or measured phenotype; an uncalled feature is not necessarily biologically absent. [^enigma_carbon_census_1] In the ENIGMA Carbon Census, all 83 enrichment compounds were structure-resolved, 54 were KEGG-linked, and only 9 were initially callable through isolate-utilizer or measured-fitness evidence, leaving 74 organism-dark compounds. [^enigma_carbon_census_1] The dark set included 33 compounds with KEGG links but no reaction in queried genomes and 29 fully orphan compounds lacking a KEGG link. [^enigma_carbon_census_1] Thus, “organism-dark” marks a resource-defined boundary involving chemical identifiers, reaction mappings, literature, and genome annotation—not proof that a compound is unknown or unusable.

The same problem occurs in functional annotation. Across Fitness Browser organisms, 57,011 of 228,709 genes (24.9%) were classified as dark, while full GTDB pangenome propagation increased dark-gene conservation coverage from 32,791 (57.5%) to 37,997 (66.6%). [^functional_dark_matter] In ecotype-functional analysis, approximately 38% of gene clusters had COG annotations, leaving 62% unannotated; the unknown-function category was significantly differentiated in 11 of 12 species. [^ecotype_functional_differentiation] These patterns make database coverage part of the measurement model, not merely a preprocessing detail. See [callability-limited-comparative-inference](../../wiki/concepts/callability-limited-comparative-inference.md) and [taxonomic-resolution-dependent-functional-inference](../../wiki/concepts/taxonomic-resolution-dependent-functional-inference.md).

**Observed environmental signals may be real yet non-portable.** In the NMDC eukaryotic-read analysis, GOTTCHA2 detected eukaryotic reads in 77% of 2,759 runs, with a median eukaryotic fraction of 2.7% and a mean of 13.3%; Kraken2 and Centrifuge produced approximately 0 domain-level Eukaryota signal because their deployed databases were prokaryote-restricted. [^euk_in_prok_correlates] Freshwater, soil, and plant-root samples differed strongly in detection and plastid share, but each biome was approximately 80–100% nested within a single study. [^euk_in_prok_correlates] Random cross-validation gave environment-model R² = 0.35, whereas study-held-out GroupKFold gave R² = −0.30 and detection AUC = 0.56, approximately chance. [^euk_in_prok_correlates] GroupKFold holds out complete studies, testing portability to new batches rather than interpolation among related samples.

This is why classifier identity, reference-database composition, study, and batch must be treated as analytical variables. The issue is elaborated in [classifier-database-compatibility-in-taxonomic-quantification](../../wiki/concepts/classifier-database-compatibility-in-taxonomic-quantification.md) and [study-batch-confounding-of-environmental-associations](../../wiki/concepts/study-batch-confounding-of-environmental-associations.md). It also explains why a conditional soil-metal result—db-RDA R² = 0.799 and p = 0.005 after conditioning on batch and project effects—should not be treated as a universal environmental effect; the unconditional metal-only R² was not reported. [^soil_metal_functional_genomics]

## Tensions and Caveats

The central disagreement is whether weak whole-genome environmental associations reflect sampling artifacts or genuinely localized adaptation. The conflict [conflict--core_gene_tradeoffs--ecotype_analysis--ecotype_env_reanalysis--267f9584](../conflicts/conflict--core_gene_tradeoffs--ecotype_analysis--ecotype_env_reanalysis--267f9584.md) records that clinical sampling bias is real, but the within-method comparison did not show stronger environmental correlations after accounting for it: U = 1536 and p = 0.83. [^ecotype_env_reanalysis] Conversely, [conflict--ecotype_analysis--ecotype_env_reanalysis--env_embedding_explorer--ffd6c359](../conflicts/conflict--ecotype_analysis--ecotype_env_reanalysis--env_embedding_explorer--ffd6c359.md) emphasizes that environmental structure is detectable in embeddings and selected functional analyses even when its genome-wide magnitude is unstable. [^env_embedding_explorer][^ecotype_analysis][^ecotype_env_reanalysis]

A second tension concerns confirmatory nulls versus exploratory positives. Predeclared genus-level ENIGMA contamination–defense tests were non-significant: relaxed mapping gave rho = 0.0587, p = 0.546, q = 0.862, and strict mapping gave rho = 0.0682, p = 0.483, q = 0.849. [^enigma_contamination_functional_potential] A relaxed coverage-adjusted model nevertheless yielded q = 0.0462, while the strict model yielded q = 0.130. [^enigma_contamination_functional_potential] [conflict--cog_analysis--ecotype_functional_differentiation--enigma_contamination_functional_potential--9514b16e](../conflicts/conflict--cog_analysis--ecotype_functional_differentiation--enigma_contamination_functional_potential--9514b16e.md) frames this as resolution- and coverage-sensitive evidence, not a settled community-wide association.

Finally, conflict  ecotype_analysis  ecotype_env_reanalysis  euk_in_prok_correlates  ea9db9b363842e06 highlights the difference between within-collection structure and transportable inference. A classifier or embedding can detect genuine variation in one collection while failing when database scope, laboratory protocol, study composition, or ecological scale changes. Feature reuse adds another risk: clustering on gene content and then testing related COG profiles can inflate apparent confirmation unless held-out features or independent data are used. [^pitfalls][^ecotype_functional_differentiation] These limitations argue for matched genome universes, preregistered contrasts, study-held-out validation, explicit missingness analysis, and direct phenotype or activity measurements.

## Where to Go Deeper

- [sampling-depth-and-downsampling-effects](../../wiki/concepts/sampling-depth-and-downsampling-effects.md) — start here for genome inclusion, downsampling, clinical skew, and incomparable correlation magnitudes.
- [environment-embedding-geography](../../wiki/concepts/environment-embedding-geography.md) — examine coordinate validity, AlphaEarth coverage, and spatial structure.
- [classifier-database-compatibility-in-taxonomic-quantification](../../wiki/concepts/classifier-database-compatibility-in-taxonomic-quantification.md) — understand why taxonomic abundance depends on reference databases.
- [callability-limited-comparative-inference](../../wiki/concepts/callability-limited-comparative-inference.md) — trace how database representation turns ecological contrasts into untestable comparisons.
- [genome-wide-versus-locus-specific-ecological-adaptation](../../wiki/concepts/genome-wide-versus-locus-specific-ecological-adaptation.md) — distinguish ancestry-dominated genome-wide patterns from locus-specific adaptation.
- [taxonomic-resolution-dependent-functional-inference](../../wiki/concepts/taxonomic-resolution-dependent-functional-inference.md) — follow the effects of genus, species, and clade mapping on functional scores.
- [selection-on-outcome-leakage](../../wiki/concepts/selection-on-outcome-leakage.md) — assess whether feature reuse compromises ecotype confirmation.

Key entities: [kbase-ke-pangenome](../../wiki/entities/kbase-ke-pangenome.md), [gtdb](../../wiki/entities/gtdb.md), [alph-aearth](../../wiki/entities/alph-aearth.md), [kescience-fitnessbrowser](../../wiki/entities/kescience-fitnessbrowser.md), [gapmind](../../wiki/entities/gapmind.md), [eggnog](../../wiki/entities/eggnog.md), [ncbi-environment-metadata](../../wiki/entities/ncbi-environment-metadata.md), [benjamini-hochberg-fdr](../../wiki/entities/benjamini-hochberg-fdr.md), [bacdive](../../wiki/entities/bacdive.md)

Project reports: [ecotype_analysis__REPORT](../../wiki/summaries/ecotype_analysis__REPORT.md), [ecotype_env_reanalysis__REPORT](../../wiki/summaries/ecotype_env_reanalysis__REPORT.md), [env_embedding_explorer__REPORT](../../wiki/summaries/env_embedding_explorer__REPORT.md), [euk_in_prok_correlates__REPORT](../../wiki/summaries/euk_in_prok_correlates__REPORT.md), [enigma_carbon_census_1__REPORT](../../wiki/summaries/enigma_carbon_census_1__REPORT.md), [plant_microbiome_ecotypes__REPORT](../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md), [prophage_ecology__REPORT](../../wiki/summaries/prophage_ecology__REPORT.md), [pitfalls](../../wiki/summaries/pitfalls.md)

[^ecotype_analysis]: [ecotype analysis](../../wiki/summaries/ecotype_analysis__REPORT.md)
[^euk_in_prok_correlates]: [euk in prok correlates](../../wiki/summaries/euk_in_prok_correlates__REPORT.md)
[^enigma_carbon_census_1]: [enigma carbon census 1](../../wiki/summaries/enigma_carbon_census_1__REPORT.md)
[^bacdive_metal_validation]: [bacdive metal validation](../../wiki/summaries/bacdive_metal_validation__REPORT.md)
[^bacdive_phenotype_metal_tolerance]: [bacdive phenotype metal tolerance](../../wiki/summaries/bacdive_phenotype_metal_tolerance__REPORT.md)
[^microbeatlas_metal_ecology]: [microbeatlas metal ecology](../../wiki/summaries/microbeatlas_metal_ecology__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../../wiki/summaries/plant_microbiome_ecotypes__REPORT.md)
[^env_embedding_explorer]: [env embedding explorer](../../wiki/summaries/env_embedding_explorer__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../../wiki/summaries/ecotype_env_reanalysis__REPORT.md)
[^pgp_pangenome_ecology]: [pgp pangenome ecology](../../wiki/summaries/pgp_pangenome_ecology__REPORT.md)
[^prophage_ecology]: [prophage ecology](../../wiki/summaries/prophage_ecology__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../../wiki/summaries/functional_dark_matter__REPORT.md)
[^ecotype_functional_differentiation]: [ecotype functional differentiation](../../wiki/summaries/ecotype_functional_differentiation__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../../wiki/summaries/soil_metal_functional_genomics__REPORT.md)
[^enigma_contamination_functional_potential]: [enigma contamination functional potential](../../wiki/summaries/enigma_contamination_functional_potential__REPORT.md)
[^pitfalls]: [pitfalls](../../wiki/summaries/pitfalls.md)
