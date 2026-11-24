---
type: "Summary"
description: "Summary of the project Pan-Bacterial AMR Gene Landscape."
doc_type: "short"
full_text: "sources/amr_pangenome_atlas__REPORT.md"
---
# Pan-Bacterial AMR Gene Landscape

Summary of the project Pan-Bacterial AMR Gene Landscape.

## Key Findings

### AMR genes are depleted from the core genome

AMR genes are significantly less conserved than the pangenome average: 30.3% are core versus 46.8% baseline (odds ratio (OR)=0.49, chi-squared=23,117, p≈0). [src: amr_pangenome_atlas] The auxiliary genome is 2.2x enriched for AMR genes, at 33.6% versus 15.3%. [src: amr_pangenome_atlas] The depletion holds across species. In a paired test of 4,252 species with ≥5 AMR clusters each, 63.7% had AMR less core than their species baseline (Wilcoxon p=1.1e-130, mean difference -0.102). [src: amr_pangenome_atlas] The report claims its analysis across 14,723 species establishes the OR=0.49 depletion as a universal bacterial pattern, not one specific to individual pathogens. [src: amr_pangenome_atlas] It says this agrees with pangenome studies of Neisseria gonorrhoeae, Salmonella and Corynebacterium striatum, and claims confirmation of a universal pattern across 27K species. [src: amr_pangenome_atlas] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

### Conservation depends on mechanism

Beta-lactamases are 54.9% core (p=7.7e-74 for enrichment versus baseline). The report describes them as intrinsic resistance in the chromosomal backbone. [src: amr_pangenome_atlas] Regulatory AMR genes are only 6.5% core. [src: amr_pangenome_atlas] The mobile elements blaTEM, tet(C) and ant(2'')-Ia are 0% core, being fully accessory or singleton. [src: amr_pangenome_atlas] Efflux pumps split: intrinsic pumps such as emhABC are >95% core, while acquired efflux genes are accessory. [src: amr_pangenome_atlas]

The report interprets intrinsic resistance genes (ampC beta-lactamases, emhABC efflux systems, rox rifampin monooxygenases) as vertically inherited core residents present in >95% of genomes within a species. [src: amr_pangenome_atlas] It states they impose negligible fitness costs and form the species' baseline defensive repertoire. [src: amr_pangenome_atlas] It characterizes acquired genes (blaTEM, tet cassettes, ant(2'')-Ia) as fully accessory, often 0% core, appearing as singletons or in a minority of genomes. [src: amr_pangenome_atlas] It describes these as horizontally transferred elements spreading under antibiotic selection pressure. [src: amr_pangenome_atlas]

The mechanism census, built by keyword matching on AMRFinderPlus product descriptions, assigns hits as follows (hits, share of hits, percent core). [src: amr_pangenome_atlas]

- Other/Unclassified: 18,448 hits, 22.2%, 24.0% core. [src: amr_pangenome_atlas]
- Enzymatic inactivation: 15,755 hits, 19.0%, 28.2% core. [src: amr_pangenome_atlas]
- Efflux: 14,338 hits, 17.3%, 30.9% core. [src: amr_pangenome_atlas]
- Beta-lactamase: 12,824 hits, 15.4%, 54.9% core. [src: amr_pangenome_atlas]
- Target modification: 6,955 hits, 8.4%, 19.6% core. [src: amr_pangenome_atlas]
- Oxidoreductase: 6,852 hits, 8.3%, 15.4% core. [src: amr_pangenome_atlas]
- Cell wall modification: 4,964 hits, 6.0%, 45.2% core. [src: amr_pangenome_atlas]
- Regulatory: 2,848 hits, 3.4%, 6.5% core. [src: amr_pangenome_atlas]

### Taxonomic hotspots

Gammaproteobacteria contain 45% of all AMR clusters (37,752/83,008). [src: amr_pangenome_atlas] At the genus level, Klebsiella leads with 206 AMR clusters per species. [src: amr_pangenome_atlas] Salmonella has 198, Citrobacter 134 and Enterobacter 93. [src: amr_pangenome_atlas] The top hotspot families are Enterobacteriaceae (37.5 AMR/species) and Staphylococcaceae (37.3 AMR/species). Both are dominated by clinical pathogens. [src: amr_pangenome_atlas]

Phylum-level values (species with AMR, total AMR, mean AMR per species, percent of species with AMR):

| Phylum | Species with AMR | Total AMR | Mean AMR/sp | % species with AMR |
|---|---|---|---|---|
| Pseudomonadota | 4,992 | 42,904 | 8.6 | 67.0% [src: amr_pangenome_atlas] |
| Bacillota | 1,401 | 12,614 | 9.0 | 65.3% [src: amr_pangenome_atlas] |
| Actinomycetota | 2,036 | 9,027 | 4.4 | 64.2% [src: amr_pangenome_atlas] |
| Bacillota_A | 2,254 | 8,776 | 3.9 | 57.5% [src: amr_pangenome_atlas] |
| Bacteroidota | 1,835 | 5,458 | 3.0 | 50.6% [src: amr_pangenome_atlas] |

### Pangenome openness

Within phyla, pangenome openness correlates positively with AMR count in 8/10 tested phyla. [src: amr_pangenome_atlas] The strongest cases are Bacillota (rho=0.219, p=1.0e-16) and Bacillota_C (rho=0.374, p=3.1e-5). [src: amr_pangenome_atlas] The overall correlation is near zero (rho=0.006), which the report interprets as phylogeny dominating the signal. [src: amr_pangenome_atlas]

### Functional categories and gene families

Among 77K AMR clusters with eggNOG annotations versus an 86M baseline, COG V (Defense mechanisms; COG = clusters of orthologous groups) is 7.05x enriched (14.9% versus 2.1%). [src: amr_pangenome_atlas] COG P (Inorganic ion transport) is 1.93x enriched (10.7% versus 5.6%). This reflects mercury (merA, merP, merC) and arsenic (arsD, arsC) resistance families. [src: amr_pangenome_atlas] COG J (Translation) is 1.50x enriched, consistent with ribosomal protection proteins (erm, helR). [src: amr_pangenome_atlas] Replication (L: 0.12x), lipid metabolism (I: 0.10x) and cell motility (N: 0.08x) are strongly depleted. [src: amr_pangenome_atlas]

The top gene families are bla (beta-lactamases, 6,115 hits), merA (mercury reductase, 4,506), arsD (arsenic metallochaperone, 2,611), merP (mercury binding protein, 2,222) [src: amr_pangenome_atlas] and vanR (vancomycin response regulator, 1,929). [src: amr_pangenome_atlas]

Heavy-metal resistance genes are prominent, reflecting the broad AMR definition of the NCBI Reference Gene Catalog, which includes stress response genes. [src: amr_pangenome_atlas] Mercury genes (merA, merP, merC, merE, merF, merR, merD, merB, merT) account for ~15,000 hits, or 18% of all AMR annotations. [src: amr_pangenome_atlas] Arsenic genes (arsD, arsN1, arsN2, arsC) add ~6,000. [src: amr_pangenome_atlas] The report reads the COG P enrichment as showing that heavy metal and antibiotic resistance are genomically intertwined, often co-located on mobile elements. [src: amr_pangenome_atlas]

### Annotation depth

93.0% of AMR clusters have both Bakta product annotations and eggNOG hits (2 annotation sources). [src: amr_pangenome_atlas] The remaining 7.0% have Bakta annotations only. [src: amr_pangenome_atlas] Zero AMR clusters have Pfam domain hits in bakta_pfam_domains. The report suggests AMRFinderPlus and Pfam HMM scans target non-overlapping sequence space for these families. [src: amr_pangenome_atlas] Sparsely annotated (1-source) AMR clusters are enriched for singletons (55.4% vs 34.6%). [src: amr_pangenome_atlas]

### Environment and clinical association

The report states that clinical species carry 2.7x more AMR, and that it is more acquired. [src: amr_pangenome_atlas] Human/Clinical species carry 10.6 AMR clusters per species (n=2,248). The other groups are Soil/Terrestrial at 4.6 (n=2,469), Aquatic at 3.9 (n=1,827) and Animal at 3.0 (n=959). [src: amr_pangenome_atlas] The difference is highly significant (Kruskal-Wallis H=440, p=7.0e-93). [src: amr_pangenome_atlas] Clinical AMR is less core (30.8%) than soil AMR (58.1%) or plant AMR (63.1%). The report interprets this as clinical environments selecting for acquired or mobile resistance, while environmental AMR is predominantly intrinsic. [src: amr_pangenome_atlas] It frames this as an ecological gradient: antibiotic-exposed environments (hospitals, animal husbandry) select for acquired resistance, while environmental species keep mainly intrinsic defenses. [src: amr_pangenome_atlas] The report says this extends Hua et al.'s US isolate findings to 7,838 species with text-classified isolation sources. [src: amr_pangenome_atlas]

An AlphaEarth embedding analysis covered 2,684 species with ≥3 genomes and embeddings. It found that environmental diversity strongly predicts AMR count (Spearman rho=0.466, p=1.6e-144). [src: amr_pangenome_atlas] Species sampled from more diverse environments also have less-core AMR genes (rho=-0.173, p=1.8e-19). [src: amr_pangenome_atlas] The report takes this to suggest the hypothesis that niche breadth enables resistance accumulation through more horizontal-transfer opportunities. [src: amr_pangenome_atlas] It says this aligns with the environmental reservoir hypothesis of AMR evolution. [src: amr_pangenome_atlas]

### Fitness cost in the Fitness Browser

A DIAMOND-based Fitness Browser (FB)–pangenome link table (177,863 links at 100% sequence identity) identified 178 AMR genes across 37 FB organisms. These gave 29,386 fitness measurements. [src: amr_pangenome_atlas] Surprisingly, AMR genes show slightly less fitness cost than the non-AMR baseline (median fitness -0.007 versus -0.012, Mann-Whitney p=3.7e-6). [src: amr_pangenome_atlas] Beta-lactamases are nearly neutral (median -0.001). [src: amr_pangenome_atlas] Singleton AMR genes are costliest (median -0.019). [src: amr_pangenome_atlas] The report suggests that AMR genes in these predominantly environmental organisms are well-integrated intrinsic resistance genes, not recently acquired mobile elements. [src: amr_pangenome_atlas] It sees this as an exception to its earlier finding that core genes are more burdensome overall, since core AMR appears less costly than non-AMR core genes. [src: amr_pangenome_atlas]

### Claimed novelty

The report claims to be the first to quantify AMR conservation across 14,723 species with uniform Bakta + AMRFinderPlus annotation. [src: amr_pangenome_atlas] It also claims novelty in demonstrating the mechanism-specific intrinsic–acquired dichotomy at pan-bacterial scale, [src: amr_pangenome_atlas] in linking AlphaEarth environmental diversity to AMR accumulation (rho=0.466), [src: amr_pangenome_atlas] and in showing that clinical AMR is more acquired and less core than environmental AMR. [src: amr_pangenome_atlas]

## Data and Methods

The bakta_amr table contains 83,008 AMRFinderPlus hits on gene cluster representatives. They cover 82,908 distinct clusters across 14,723 species, which is 53.2% of the 27,690 pangenome species. [src: amr_pangenome_atlas] Detection methods were HMM (51.5%), BLASTP (22.7%), EXACTP (13.0%), PARTIALP (9.7%) and ALLELEP (3.0%). [src: amr_pangenome_atlas] The hits span 1,939 distinct AMR gene families and 2,079 AMR products. [src: amr_pangenome_atlas] AMR annotations, conservation flags, functional context, taxonomy and environment come from the kbase_ke_pangenome collection of the KBase Data Lakehouse. [src: amr_pangenome_atlas] Fitness effects come from the kescience_fitnessbrowser collection (organism, gene and genefitness tables). [src: amr_pangenome_atlas]

## Caveats and Open Work

- Of the 14,723 AMR-carrying species, 7,838 (53.2%) received a non-Other/Unknown environment classification. The Kruskal-Wallis test used only these species, across 6 categories. [src: amr_pangenome_atlas]
- The Other/Unknown bin holds 46.8% of species. This reflects sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- Genome databases over-represent clinical pathogens, inflating AMR counts for human-associated species. [src: amr_pangenome_atlas]
- The 83K AMRFinderPlus hits are not all antibiotic resistance, because the scope includes mercury and arsenic stress-response genes. [src: amr_pangenome_atlas]
- Only 28% of genomes have AlphaEarth embeddings, biased toward genomes with geographic metadata. [src: amr_pangenome_atlas]
- The 100% identity threshold avoids paralog confusion but may undercount fitness effects of closely related variants, such as alleles differing by a single synonymous substitution. [src: amr_pangenome_atlas]
- FB organisms are predominantly environmental isolates with intrinsic resistance. The fitness cost of recently acquired mobile resistance in clinical pathogens may differ substantially. [src: amr_pangenome_atlas] Only 37/48 FB organisms had AMR genes, so the fitness analysis does not capture those costs. [src: amr_pangenome_atlas]
- Mechanism classification uses keywords, not the CARD Antibiotic Resistance Ontology (ARO). The 22.2% Other/Unclassified category includes products matching no keyword set, such as ribosomal protection proteins with non-standard names and novel mechanisms. [src: amr_pangenome_atlas]
- Some singleton AMR clusters may be annotation artifacts rather than true species-specific resistance genes. [src: amr_pangenome_atlas]
- No Bonferroni or false discovery rate (FDR) correction was applied across the tests of the six hypotheses. The report argues the primary p-values are extreme (many < 1e-100) and correction would not change conclusions. [src: amr_pangenome_atlas] Per-gene and per-phylum tests are exploratory and hypothesis-generating. [src: amr_pangenome_atlas]
- Proposed next step: map bakta_db_xrefs cross-references to CARD ARO terms, for a systematic ontology-based classification that would reduce the unclassified fraction. [src: amr_pangenome_atlas]
- Proposed next step: replace keyword-based mechanism classification with systematic CARD ARO mapping to reduce the 22% "Other/Unclassified" category. [src: amr_pangenome_atlas]
- Proposed next step: map AMR gene prevalence in NMDC/MGnify environmental metagenomes to test whether accessory AMR genes seen in isolates are also prevalent in community DNA. [src: amr_pangenome_atlas]
- Proposed next step: use phylogenetic tree distances to estimate AMR gene gain/loss rates and ask whether acquired genes are gained faster than lost. [src: amr_pangenome_atlas]
- Proposed next step: a co-localization analysis to test whether AMR genes cluster in genomic islands or co-localize with mobile element markers such as IS elements and integrons. [src: amr_pangenome_atlas]
- Proposed next step: cross-reference AMR proteins with AlphaFold/PDB structures to identify novel resistance folds. [src: amr_pangenome_atlas]

## Slots Into

- [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]]: AMR genes are 30.3% core versus 46.8% baseline, and beta-lactamases (54.9% core) contrast with regulatory genes (6.5% core). [src: amr_pangenome_atlas]
- [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]]: Human/Clinical species carry 10.6 AMR clusters per species, and clinical AMR is 30.8% core. [src: amr_pangenome_atlas]
- [[concepts/functional-annotation-of-amr-genes-and-mechanism-classification]]: Keyword-based mechanism classification leaves 22.2% Other/Unclassified. [src: amr_pangenome_atlas]
- [[concepts/pangenome-openness-and-its-correlates]]: Openness correlates with AMR count in 8/10 phyla, but the overall rho is 0.006. [src: amr_pangenome_atlas]
- [[concepts/fitness-cost-of-antimicrobial-resistance-genes]]: AMR genes show slightly less fitness cost than baseline in Fitness Browser organisms. [src: amr_pangenome_atlas]
- [[concepts/sampling-bias-and-metadata-sparsity-in-amr-resistome-surveys]]: 46.8% of AMR-carrying species fall in Other/Unknown because of sparse isolation_source metadata. [src: amr_pangenome_atlas]
- [[concepts/metal-resistance-genes-within-amr-catalogs]]: Mercury genes account for ~15,000 hits, or 18% of all AMR annotations. [src: amr_pangenome_atlas]
