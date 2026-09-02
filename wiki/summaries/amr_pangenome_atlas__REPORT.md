---
type: "Summary"
description: "Pan-bacterial analysis reveals AMR is accessory, environment-structured, and mechanism-dependent."
doc_type: "short"
full_text: "sources/amr_pangenome_atlas__REPORT.md"
---
# Pan-Bacterial AMR Gene Landscape

## Overview

This report analyzes antimicrobial-resistance (AMR) genes across 27,690 pangenome species using uniform Bakta and AMRFinderPlus annotations, conservation and functional data from the KBase KE pangenome collection, environmental metadata and AlphaEarth embeddings, and fitness measurements linked to the KBase Fitness Browser. The analysis identifies 83,008 AMRFinderPlus hits on gene-cluster representatives, spanning 82,908 distinct clusters, 1,939 AMR gene families, 2,079 AMR products, and 14,723 species; 53.2% of the 27,690 pangenome species carried at least one AMR hit. [src: amr_pangenome_atlas]

## Key Findings

### AMR is depleted from the core genome

Only 30.3% of AMR genes were core compared with 46.8% for the pangenome baseline (OR=0.49, chi-squared=23,117, p≈0), while the auxiliary genome was 2.2x enriched for AMR (33.6% versus 15.3%). In a paired test of 4,252 species with at least 5 AMR clusters, 63.7% had AMR less core than their species baseline (Wilcoxon p=1.1e-130, mean difference -0.102). [src: amr_pangenome_atlas]

### Conservation differs between intrinsic and acquired resistance

Beta-lactamases were 54.9% core (p=7.7e-74 for enrichment versus baseline), whereas regulatory genes were 6.5% core; blaTEM, tet(C), and ant(2'')-Ia were 0% core. Intrinsic efflux pumps such as emhABC were >95% core, while acquired efflux genes were accessory. The report interprets these contrasting patterns as an intrinsic-acquired dichotomy: vertically inherited intrinsic resistance genes are core residents, whereas acquired resistance genes are often accessory, singleton, or present in a minority of genomes. [src: amr_pangenome_atlas]

The AMR mechanism table contained 18,448 Other/Unclassified hits (22.2%; 24.0% core), 15,755 enzymatic-inactivation hits (19.0%; 28.2% core), 14,338 efflux hits (17.3%; 30.9% core), 12,824 beta-lactamase hits (15.4%; 54.9% core), 6,955 target-modification hits (8.4%; 19.6% core), 6,852 oxidoreductase hits (8.3%; 15.4% core), 4,964 cell-wall-modification hits (6.0%; 45.2% core), and 2,848 regulatory hits (3.4%; 6.5% core). Classification used keyword matching against AMRFinderPlus product descriptions rather than the CARD Antibiotic Resistance Ontology (ARO). [src: amr_pangenome_atlas]

### AMR hotspots are concentrated in clinical-pathogen-associated taxa

At the genus level, Klebsiella led with 206 AMR clusters per species, followed by Salmonella with 198, Citrobacter with 134, and Enterobacter with 93. Gammaproteobacteria contained 45% of all AMR clusters (37,752/83,008), while the top hotspot families were Enterobacteriaceae (37.5 AMR/species) and Staphylococcaceae (37.3 AMR/species). [src: amr_pangenome_atlas]

Pangenome openness positively correlated with AMR count in 8/10 tested phyla, with the strongest correlations in Bacillota (rho=0.219, p=1.0e-16) and Bacillota_C (rho=0.374, p=3.1e-5). The overall correlation was near zero (rho=0.006), indicating that phylogeny dominated the aggregate signal. [src: amr_pangenome_atlas]

The taxonomic census included 4,992 Pseudomonadota species with AMR, 42,904 total AMR hits, 8.6 mean AMR hits per species, and 67.0% of species carrying AMR; 1,401 Bacillota species, 12,614 hits, 9.0 mean hits per species, and 65.3%; 2,036 Actinomycetota species, 9,027 hits, 4.4 mean hits per species, and 64.2%; 2,254 Bacillota_A species, 8,776 hits, 3.9 mean hits per species, and 57.5%; and 1,835 Bacteroidota species, 5,458 hits, 3.0 mean hits per species, and 50.6%. [src: amr_pangenome_atlas]

### AMR is enriched in defense and inorganic-ion transport functions

Among 77K AMR clusters with eggNOG annotations compared with an 86M-cluster baseline, COG V (Defense mechanisms) was 7.05x enriched (14.9% versus 2.1%), COG P (Inorganic ion transport) was 1.93x enriched (10.7% versus 5.6%), and COG J (Translation) was 1.50x enriched. COG L (Replication; 0.12x), COG I (Lipid metabolism; 0.10x), and COG N (Cell motility; 0.08x) were depleted. COG denotes the Cluster of Orthologous Groups functional classification. [src: amr_pangenome_atlas]

The five most abundant AMR gene families were bla (beta-lactamases, 6,115 hits), merA (mercury reductase, 4,506), arsD (arsenic metallochaperone, 2,611), merP (mercury-binding protein, 2,222), and vanR (vancomycin response regulator, 1,929). Mercury-resistance families collectively accounted for approximately 15,000 hits and 18% of all AMR annotations, while arsenic-resistance families added another approximately 6,000 hits; the report cautions that AMRFinderPlus's broad Reference Gene Catalog scope includes stress-response genes alongside classical antibiotic-resistance genes. [src: amr_pangenome_atlas]

### Clinical species carry more and more-acquired AMR

Human/Clinical species carried 10.6 AMR clusters per species (n=2,248), compared with 4.6 for Soil/Terrestrial (n=2,469), 3.9 for Aquatic (n=1,827), and 3.0 for Animal (n=959). The difference was significant (Kruskal-Wallis H=440, p=7.0e-93). Clinical AMR was less core (30.8%) than soil AMR (58.1%) or plant AMR (63.1%), supporting the interpretation that clinical environments select for acquired or mobile resistance while environmental AMR is more predominantly intrinsic. [src: amr_pangenome_atlas]

Of the 14,723 AMR-carrying species, 7,838 (53.2%) received a non-Other/Unknown environment classification. The environment comparison was restricted to these well-classified species across 6 categories; the Other/Unknown bin contained 46.8% of species and reflected sparse and inconsistent free-text isolation_source metadata in NCBI BioSample records. [src: amr_pangenome_atlas]

Among 2,684 species with at least 3 genomes and AlphaEarth embeddings, environmental diversity predicted AMR count (Spearman rho=0.466, p=1.6e-144), while environmental diversity and AMR core fraction were negatively correlated (rho=-0.173, p=1.8e-19). The report presents this as evidence that niche breadth may enable resistance accumulation, while noting that the result is an association and that AlphaEarth coverage is limited. [src: amr_pangenome_atlas]

### AMR genes were not burdensome under the tested laboratory conditions

Using a DIAMOND-based Fitness Browser pangenome link table with 177,863 links at 100% sequence identity, the analysis identified 178 AMR genes across 37 Fitness Browser organisms and 29,386 fitness measurements. AMR genes had slightly less fitness cost than the non-AMR baseline (median fitness -0.007 versus -0.012, Mann-Whitney p=3.7e-6), beta-lactamases were nearly neutral (median -0.001), and singleton AMR genes were costliest (median -0.019). [src: amr_pangenome_atlas]

The report interprets the fitness result as consistent with well-integrated intrinsic resistance genes in predominantly environmental Fitness Browser organisms, not as evidence that recently acquired mobile resistance is cost-free in clinical pathogens. The source's generated-data table separately reports fitness data for 162 AMR genes in 36 Fitness Browser organisms, and the report does not reconcile these differing counts. [src: amr_pangenome_atlas]

### Annotation coverage and detection methods

The 83,008 AMRFinderPlus hits were detected by HMM (51.5%), BLASTP (22.7%), EXACTP (13.0%), PARTIALP (9.7%), and ALLELEP (3.0%). Bakta product annotations and eggNOG hits were present for 93.0% of AMR clusters, while 7.0% had Bakta annotations only; 55.4% of sparsely annotated one-source clusters were singletons compared with 34.6% of two-source clusters. Zero AMR clusters had Pfam domain hits in the bakta_pfam_domains table, indicating non-overlapping target sequence space for these AMRFinderPlus and Pfam scans. [src: amr_pangenome_atlas]

## Caveats and Limitations

The report identifies sampling bias as a limitation because genome databases over-represent clinical pathogens, potentially inflating AMR counts for human-associated species. AMRFinderPlus also includes stress-response genes such as mercury- and arsenic-resistance genes, so the 83K hits are not all antibiotic resistance in the narrow sense. [src: amr_pangenome_atlas]

AlphaEarth embeddings covered only 28% of genomes and were biased toward genomes with geographic metadata. The Fitness Browser analysis covered only 37/48 Fitness Browser organisms with AMR genes, and these were predominantly environmental strains; consequently, it did not capture the cost of recently acquired mobile resistance in pathogens. [src: amr_pangenome_atlas]

Keyword-based mechanism classification left 22% of hits in Other/Unclassified; systematic mapping through CARD ARO terms could reduce this category. Singleton inflation may also cause some singleton AMR clusters to reflect annotation artifacts rather than true species-specific resistance genes. [src: amr_pangenome_atlas]

The six hypotheses involved many individual tests, including per-mechanism binomial tests, per-phylum correlations, and per-environment comparisons. Formal Bonferroni or FDR correction was not applied because the primary p-values were extreme, with many < 1e-100, and the report states that correction would not change the conclusions; per-gene and per-phylum tests remain exploratory and hypothesis-generating. FDR means false discovery rate. [src: amr_pangenome_atlas]

The 100% DIAMOND identity threshold used for Fitness Browser pangenome linking is conservative: it avoids paralog confusion but may miss closely related variants, including alleles differing by a single synonymous substitution, and may therefore undercount fitness effects. [src: amr_pangenome_atlas]

## Future Directions

The report proposes mapping AMR prevalence in environmental metagenome communities using NMDC/MGnify, estimating AMR gene gain and loss rates from phylogenetic distances, testing co-localization with genomic islands, insertion sequences, and integrons, replacing keyword mechanism classification with CARD ARO mapping, cross-referencing AMR proteins with AlphaFold and PDB structures, and testing fitness costs under antibiotic stress conditions using the full Fitness Browser pangenome link table. [src: amr_pangenome_atlas]

## Slots Into

- [[concepts/environmental-resistome]] — AMR density, core-versus-accessory structure, clinical and environmental gradients, environmental diversity, and heavy-metal resistance provide pan-bacterial evidence for an environmental resistome. [src: amr_pangenome_atlas]
- [[concepts/pangenome-integration]] — The report links AMR conservation classes, pangenome openness, gene-family distributions, taxonomy, and cross-dataset annotations across 27,690 species. [src: amr_pangenome_atlas]
- [[concepts/condition-specific-fitness]] — Fitness Browser cross-referencing shows that AMR fitness effects depend on gene class, organismal context, and the tested laboratory condition, while leaving recently acquired clinical resistance undermeasured. [src: amr_pangenome_atlas]
- [[concepts/cofitness-network-architecture]] — The report's cross-reference of AMR genes to Fitness Browser measurements supplies gene-level fitness evidence relevant to interpreting resistance-associated functional architecture. [src: amr_pangenome_atlas]
