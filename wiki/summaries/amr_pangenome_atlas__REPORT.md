---
type: "Summary"
description: "Pan-bacterial atlas of AMRFinderPlus antimicrobial-resistance genes across 27,690 pangenome species, covering core-versus-accessory conservation, mechanisms, taxonomic hotspots, environment associations, Fitness Browser fitness effects, caveats and proposed follow-up analyses."
doc_type: "short"
full_text: "sources/amr_pangenome_atlas__REPORT.md"
---
# Pan-Bacterial AMR Gene Landscape

## Overview

This report analyzes antimicrobial-resistance (AMR) genes across 27,690 pangenome species using uniform Bakta and AMRFinderPlus annotations, conservation and functional data from the KBase KE pangenome collection, environmental metadata and AlphaEarth embeddings, and fitness measurements linked to the KBase Fitness Browser. The analysis identifies 83,008 AMRFinderPlus hits on gene-cluster representatives, spanning 82,908 distinct clusters, 1,939 AMR gene families, 2,079 AMR products, and 14,723 species; 53.2% of the 27,690 pangenome species carried at least one AMR hit. The hits were detected by HMM (51.5%), BLASTP (22.7%), EXACTP (13.0%), PARTIALP (9.7%), and ALLELEP (3.0%). [src: amr_pangenome_atlas]

## Key Findings

### AMR is depleted from the core genome

Only 30.3% of AMR genes were core compared with 46.8% for the pangenome baseline (OR=0.49, chi-squared=23,117, p≈0), while the auxiliary genome was 2.2x enriched for AMR (33.6% versus 15.3%). In a paired test of 4,252 species with at least 5 AMR clusters, 63.7% had AMR less core than their species baseline (Wilcoxon p=1.1e-130, mean difference -0.102). [src: amr_pangenome_atlas]

### Conservation differs between intrinsic and acquired resistance

Beta-lactamases were 54.9% core (p=7.7e-74 for enrichment versus baseline), whereas regulatory genes were 6.5% core; blaTEM, tet(C), and ant(2'')-Ia were 0% core. Intrinsic efflux pumps such as emhABC were >95% core, while acquired efflux genes were accessory. The report interprets these contrasting patterns as an intrinsic-acquired dichotomy. In that interpretation, intrinsic resistance genes are vertically inherited core residents present in >95% of genomes within a species and make up the species' baseline defensive repertoire. Examples are beta-lactamases like ampC, efflux systems like emhABC, and rifampin monooxygenases like rox. The report also says these genes impose negligible fitness costs, but this is an interpretation rather than a direct per-gene measurement. Acquired resistance genes are described as fully accessory, often 0% core, and appearing as singletons or in a minority of genomes. Examples are blaTEM, tet cassettes, and aminoglycoside-modifying enzymes like ant(2'')-Ia. The report's description of these genes as horizontally transferred elements that spread under antibiotic selection pressure is also interpretive. [src: amr_pangenome_atlas]

The AMR mechanism table contained 18,448 Other/Unclassified hits (22.2%; 24.0% core), 15,755 enzymatic-inactivation hits (19.0%; 28.2% core), 14,338 efflux hits (17.3%; 30.9% core), 12,824 beta-lactamase hits (15.4%; 54.9% core), 6,955 target-modification hits (8.4%; 19.6% core), 6,852 oxidoreductase hits (8.3%; 15.4% core), 4,964 cell-wall-modification hits (6.0%; 45.2% core), and 2,848 regulatory hits (3.4%; 6.5% core). Classification used keyword matching against AMRFinderPlus product descriptions rather than the CARD Antibiotic Resistance Ontology (ARO). [src: amr_pangenome_atlas]

### AMR hotspots are concentrated in clinical-pathogen-associated taxa

At the genus level, Klebsiella led with 206 AMR clusters per species, followed by Salmonella with 198, Citrobacter with 134, and Enterobacter with 93. Gammaproteobacteria contained 45% of all AMR clusters (37,752/83,008), while the top hotspot families were Enterobacteriaceae (37.5 AMR/species) and Staphylococcaceae (37.3 AMR/species). [src: amr_pangenome_atlas]

Pangenome openness positively correlated with AMR count in 8/10 tested phyla, with the strongest correlations in Bacillota (rho=0.219, p=1.0e-16) and Bacillota_C (rho=0.374, p=3.1e-5). The overall correlation was near zero (rho=0.006), indicating that phylogeny dominated the aggregate signal. [src: amr_pangenome_atlas]

The taxonomic census included 4,992 Pseudomonadota species with AMR, 42,904 total AMR hits, 8.6 mean AMR hits per species, and 67.0% of species carrying AMR; 1,401 Bacillota species, 12,614 hits, 9.0 mean hits per species, and 65.3%; 2,036 Actinomycetota species, 9,027 hits, 4.4 mean hits per species, and 64.2%; 2,254 Bacillota_A species, 8,776 hits, 3.9 mean hits per species, and 57.5%; and 1,835 Bacteroidota species, 5,458 hits, 3.0 mean hits per species, and 50.6%. [src: amr_pangenome_atlas]

### AMR is enriched in defense and inorganic-ion transport functions

Among 77K AMR clusters with eggNOG annotations compared with an 86M-cluster baseline, COG V (Defense mechanisms) was 7.05x enriched (14.9% versus 2.1%), COG P (Inorganic ion transport) was 1.93x enriched (10.7% versus 5.6%), and COG J (Translation) was 1.50x enriched. COG L (Replication; 0.12x), COG I (Lipid metabolism; 0.10x), and COG N (Cell motility; 0.08x) were depleted. COG denotes the Cluster of Orthologous Groups functional classification. [src: amr_pangenome_atlas]

The five most abundant AMR gene families were bla (beta-lactamases, 6,115 hits), merA (mercury reductase, 4,506), arsD (arsenic metallochaperone, 2,611), merP (mercury-binding protein, 2,222), and vanR (vancomycin response regulator, 1,929). Mercury-resistance families collectively accounted for approximately 15,000 hits and 18% of all AMR annotations, while arsenic-resistance families added another approximately 6,000 hits; the report cautions that AMRFinderPlus's broad Reference Gene Catalog scope includes stress-response genes alongside classical antibiotic-resistance genes. The report also interprets heavy-metal and antibiotic resistance as genomically intertwined and often co-located on mobile elements, citing the COG P enrichment. It does not separately quantify this co-location. [src: amr_pangenome_atlas]

### Clinical species carry more and more-acquired AMR

Human/Clinical species carried 10.6 AMR clusters per species (n=2,248), compared with 4.6 for Soil/Terrestrial (n=2,469), 3.9 for Aquatic (n=1,827), and 3.0 for Animal (n=959). The difference was significant (Kruskal-Wallis H=440, p=7.0e-93). This Kruskal-Wallis test was restricted to the 7,838 of 14,723 AMR-carrying species (53.2%) that received a non-Other/Unknown environment classification, across 6 categories. The report's section heading describes this as clinical species carrying "2.7x More AMR", while its displayed Human/Clinical and Soil/Terrestrial means are 10.6 and 4.6 AMR clusters per species; both reported quantities are kept here and the source does not reconcile them. Clinical AMR was less core (30.8%) than soil AMR (58.1%) or plant AMR (63.1%), supporting the interpretation that clinical environments select for acquired or mobile resistance while environmental AMR is more predominantly intrinsic. [src: amr_pangenome_atlas]

Of the 14,723 AMR-carrying species, 7,838 (53.2%) received a non-Other/Unknown environment classification. The environment comparison was restricted to these well-classified species across 6 categories; the Other/Unknown bin contained 46.8% of species and reflected sparse and inconsistent free-text isolation_source metadata in NCBI BioSample records. [src: amr_pangenome_atlas]

Among 2,684 species with at least 3 genomes and AlphaEarth embeddings, environmental diversity predicted AMR count (Spearman rho=0.466, p=1.6e-144), while environmental diversity and AMR core fraction were negatively correlated (rho=-0.173, p=1.8e-19). From this correlation the authors propose, but do not directly establish, the hypothesis that niche breadth enables resistance accumulation. Under this hypothesis, species that encounter diverse environments and diverse microbial communities have more opportunities to acquire resistance genes via horizontal transfer, in line with the "environmental reservoir" hypothesis of AMR evolution (Larsson & Flach, 2022). The result is an association, and AlphaEarth coverage is limited. [src: amr_pangenome_atlas]

### AMR genes were not burdensome under the tested laboratory conditions

Using a DIAMOND-based Fitness Browser pangenome link table with 177,863 links at 100% sequence identity, the analysis identified 178 AMR genes across 37 Fitness Browser organisms and 29,386 fitness measurements. AMR genes had slightly less fitness cost than the non-AMR baseline (median fitness -0.007 versus -0.012, Mann-Whitney p=3.7e-6), beta-lactamases were nearly neutral (median -0.001), and singleton AMR genes were costliest (median -0.019). The report reads this as suggesting that the AMR genes in these predominantly environmental Fitness Browser organisms are well-integrated intrinsic resistance genes, not recently acquired mobile elements. That is an interpretation of the sample, not a direct test. [src: amr_pangenome_atlas]

The report interprets the fitness result as consistent with well-integrated intrinsic resistance genes in predominantly environmental Fitness Browser organisms, not as evidence that recently acquired mobile resistance is cost-free in clinical pathogens. The source's generated-data table separately reports fitness data for 162 AMR genes in 36 Fitness Browser organisms, and the report does not reconcile these differing counts. [src: amr_pangenome_atlas]

### Annotation coverage and detection methods

Bakta product annotations and eggNOG hits were present for 93.0% of AMR clusters, while 7.0% had Bakta annotations only; 55.4% of sparsely annotated one-source clusters were singletons compared with 34.6% of two-source clusters. Zero AMR clusters had Pfam domain hits in the bakta_pfam_domains table. This is a null result: the report tentatively suggests that AMRFinderPlus and Pfam HMM scans appear to target non-overlapping sequence space for these gene families. [src: amr_pangenome_atlas]

## Caveats and Limitations

The report identifies sampling bias as a limitation because genome databases over-represent clinical pathogens, potentially inflating AMR counts for human-associated species. AMRFinderPlus also includes stress-response genes such as mercury- and arsenic-resistance genes, so the 83K hits are not all antibiotic resistance in the narrow sense. [src: amr_pangenome_atlas]

AlphaEarth embeddings covered only 28% of genomes and were biased toward genomes with geographic metadata. The Fitness Browser analysis covered only 37/48 Fitness Browser organisms with AMR genes, and these were predominantly environmental strains; consequently, it did not capture the cost of recently acquired mobile resistance in pathogens. [src: amr_pangenome_atlas]

In its limitations, the report says keyword-based mechanism classification left 22% of hits in Other/Unclassified. The mechanism section gives this category as 22.2%. It includes genes whose product descriptions do not match any keyword set, such as ribosomal protection proteins with non-standard names and novel resistance mechanisms. The report proposes reducing this fraction by mapping bakta_db_xrefs cross-references to CARD Antibiotic Resistance Ontology (ARO) terms, which would give a systematic, ontology-based classification. Singleton inflation may also cause some singleton AMR clusters to reflect annotation artifacts rather than true species-specific resistance genes. [src: amr_pangenome_atlas]

The six hypotheses involved many individual tests, including per-mechanism binomial tests, per-phylum correlations, and per-environment comparisons. Formal Bonferroni or FDR correction was not applied because the primary p-values were extreme, with many < 1e-100, and the report states that correction would not change the conclusions; per-gene and per-phylum tests remain exploratory and hypothesis-generating. FDR means false discovery rate. [src: amr_pangenome_atlas]

The 100% DIAMOND identity threshold used for Fitness Browser pangenome linking is conservative: it avoids paralog confusion but may miss closely related variants, including alleles differing by a single synonymous substitution, and may therefore undercount fitness effects. The Fitness Browser organisms are also mostly environmental isolates in which intrinsic resistance predominates. As a result, the fitness cost of recently acquired mobile resistance elements in clinical pathogens may differ substantially from these measurements. [src: amr_pangenome_atlas]

## Future Directions

The report lists six proposed follow-up analyses; none of them reports a result [src: amr_pangenome_atlas]:
- **NMDC/MGnify integration**: map AMR gene prevalence in environmental metagenome communities using [[entities/nmdc]] and [[entities/mgnify]] data, asking whether the accessory AMR genes seen in isolate genomes are also prevalent in community DNA. This question remains untested. [src: amr_pangenome_atlas]
- **Temporal analysis**: use phylogenetic tree distances to estimate AMR gene gain and loss rates and ask whether acquired resistance genes are being gained faster than lost. No rate estimate is given. [src: amr_pangenome_atlas]
- **Co-localization analysis**: test whether AMR genes cluster in genomic islands and co-localize with mobile-element markers such as IS elements and integrons. This remains a proposed analysis, so the report's interpretation that metal and antibiotic resistance co-locate on mobile elements is not directly tested. [src: amr_pangenome_atlas]
- **CARD ontology mapping**: replace keyword-based mechanism classification with systematic [[entities/card]] Antibiotic Resistance Ontology (ARO) mapping to reduce the 22% "Other/Unclassified" category. [src: amr_pangenome_atlas]
- **Structural analysis**: cross-reference AMR proteins with AlphaFold ([[entities/kescience-alphafold]]) and [[entities/protein-data-bank]] (PDB) structures to identify novel resistance folds. No novel folds are reported. [src: amr_pangenome_atlas]
- **Expanded fitness analysis**: use the full Fitness Browser pangenome link table to test fitness costs specifically under antibiotic stress conditions, not just standard lab media. The report supplies no antibiotic-stress fitness result. [src: amr_pangenome_atlas]

## Figures

The report's figures are listed below. [src: amr_pangenome_atlas]
- AMR conservation class versus the pangenome baseline (figures/amr_conservation_vs_baseline.png). [src: amr_pangenome_atlas]
- Per-species AMR core fraction scatter and enrichment distribution (figures/amr_conservation_per_species.png). [src: amr_pangenome_atlas]
- Stacked bar of conservation by AMR mechanism (figures/amr_mechanism_conservation.png). [src: amr_pangenome_atlas]
- Top 30 AMR gene families ranked by % core (figures/amr_gene_families_core_fraction.png). [src: amr_pangenome_atlas]
- AMRFinderPlus identity and coverage distributions (figures/amr_hit_quality_distributions.png). [src: amr_pangenome_atlas]
- Distribution of AMR clusters per species (figures/amr_species_density_distribution.png). [src: amr_pangenome_atlas]
- Phylum-level AMR prevalence and density (figures/amr_phylum_distribution.png). [src: amr_pangenome_atlas]
- AMR count versus openness, pangenome size, and genome count (figures/amr_vs_pangenome_structure.png). [src: amr_pangenome_atlas]
- Top 20 AMR hotspot families (figures/amr_hotspot_families.png). [src: amr_pangenome_atlas]
- AMR mechanism composition by phylum (figures/amr_mechanism_by_phylum.png). [src: amr_pangenome_atlas]
- Faceted scatter of AMR versus pangenome openness by phylum (figures/amr_openness_by_phylum.png). [src: amr_pangenome_atlas]
- COG category enrichment in AMR genes (figures/amr_cog_enrichment.png). [src: amr_pangenome_atlas]
- AMR count by isolation environment (figures/amr_by_environment.png). [src: amr_pangenome_atlas]
- AlphaEarth environmental diversity versus AMR (figures/amr_alphaearth_diversity.png). [src: amr_pangenome_atlas]
- AMR versus non-AMR fitness distributions and fitness by mechanism (figures/amr_fitness_distribution.png). [src: amr_pangenome_atlas]
- A 4-panel AMR overview figure (figures/fig1_amr_overview.png). [src: amr_pangenome_atlas]

## Slots Into

- [[concepts/two-speed-bacterial-genome]] — AMR is depleted from the core genome and enriched in the auxiliary genome; intrinsic resistance genes are core and acquired genes are accessory. [src: amr_pangenome_atlas]
- [[concepts/antimicrobial-resistance-fitness-cost]] — Conservation differs by mechanism, and the report interprets intrinsic genes as having negligible cost. Its fitness data cover only environmental Fitness Browser strains, linked at a 100% identity threshold. [src: amr_pangenome_atlas]
- [[concepts/laboratory-fitness-versus-natural-selection]] — Laboratory fitness in mostly environmental strains may not reflect the costs of recently acquired mobile resistance in clinical pathogens. [src: amr_pangenome_atlas]
- [[concepts/pangenome-openness-determinants]] — Openness correlates with AMR count within 8/10 tested phyla. [src: amr_pangenome_atlas]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — The overall openness-AMR correlation is near zero (rho=0.006), which the report attributes to phylogeny dominating the signal. [src: amr_pangenome_atlas]
- [[concepts/horizontal-gene-transfer-driven-innovation]] — The report interprets blaTEM, tet cassettes, and ant(2'')-Ia as horizontally transferred, fully accessory resistance genes. [src: amr_pangenome_atlas]
- [[concepts/ontology-and-category-schema-sensitivity]] — Keyword-based mechanism classification left 22.2% of hits in Other/Unclassified; the report proposes CARD ARO mapping through bakta_db_xrefs as a systematic alternative. [src: amr_pangenome_atlas]
- [[concepts/evidence-triangulation-for-functional-annotation]] — Bakta/eggNOG coverage, zero Pfam hits for AMR clusters, and singleton enrichment among one-source clusters. [src: amr_pangenome_atlas]
- [[concepts/functional-marker-validation]] — AMRFinderPlus hits include mercury and arsenic stress-response genes, and some singleton AMR clusters may be annotation artifacts. [src: amr_pangenome_atlas]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]] — Over-representation of clinical pathogens may inflate AMR counts for human-associated species. [src: amr_pangenome_atlas]
- [[concepts/environment-embedding-geography]] — AlphaEarth embeddings cover only 28% of genomes and favor records with geographic metadata. [src: amr_pangenome_atlas]
- [[concepts/confirmatory-exploratory-ecological-association-discordance]] — No formal multiple-testing correction was applied; the report treats per-gene and per-phylum tests as exploratory. [src: amr_pangenome_atlas]
- [[concepts/homology-search-negative-evidence]] — The 100% DIAMOND identity threshold may miss closely related alleles and undercount fitness effects. [src: amr_pangenome_atlas]
- [[concepts/environmental-resistome]] — AMR density, core-versus-accessory structure, clinical and environmental gradients, environmental diversity, and heavy-metal resistance provide pan-bacterial evidence for an environmental resistome. [src: amr_pangenome_atlas]
- [[concepts/pangenome-integration]] — The report links AMR conservation classes, pangenome openness, gene-family distributions, taxonomy, and cross-dataset annotations across 27,690 species. [src: amr_pangenome_atlas]
- [[concepts/condition-specific-fitness]] — Fitness Browser cross-referencing shows that AMR fitness effects depend on gene class, organismal context, and the tested laboratory condition, while leaving recently acquired clinical resistance undermeasured. [src: amr_pangenome_atlas]
- [[concepts/cofitness-network-architecture]] — The report's cross-reference of AMR genes to Fitness Browser measurements supplies gene-level fitness evidence relevant to interpreting resistance-associated functional architecture. [src: amr_pangenome_atlas]
- [[concepts/pangenome-conservation-fitness-decoupling]] — AMR genes, which are depleted from the core, show a slightly less negative median fitness than non-AMR genes in Fitness Browser organisms. [src: amr_pangenome_atlas]
- [[concepts/lab-field-fitness-concordance]] — Whether accessory AMR genes seen in isolate genomes are also prevalent in environmental community DNA is posed as an untested NMDC/MGnify question. [src: amr_pangenome_atlas]
- [[concepts/chromosomal-and-integrative-gene-transfer]] — AMR gene gain and loss rates are proposed for estimation from phylogenetic distances, but no rates are reported. [src: amr_pangenome_atlas]
- [[concepts/resistance-island-coinheritance]] — Clustering of AMR genes in genomic islands remains a proposed analysis. [src: amr_pangenome_atlas]
- [[concepts/scale-dependent-mobile-element-associations]] — Co-localization of AMR genes with IS elements and integrons remains a proposed analysis. [src: amr_pangenome_atlas]
- [[concepts/structural-annotation-gap]] — The report proposes AlphaFold/PDB cross-referencing to find novel resistance folds, with no result yet. [src: amr_pangenome_atlas]
