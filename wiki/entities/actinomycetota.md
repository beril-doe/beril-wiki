---
type: "Organism"
description: "A bacterial phylum in which contamination isolates show higher metal tolerance scores than environmental isolates."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/bacdive_metal_validation__REPORT.md", "summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/harvard_forest_warming__REPORT.md", "summaries/phb_granule_ecology__REPORT.md"]
aliases: ["Actinobacteria"]
---
# Actinomycetota

Actinomycetota (also called Actinobacteria) is a bacterial phylum in which contamination isolates show higher metal tolerance scores than environmental isolates. [src: bacdive_metal_validation] Other reports add antimicrobial resistance (AMR), polyhydroxybutyrate (PHB) and soil-warming data for the phylum. [src: amr_pangenome_atlas, phb_granule_ecology, harvard_forest_warming]

## Key facts

- AMR: Actinomycetota has 2,036 species with AMR, 9,027 total AMR, a mean of 4.4 AMR per species, and 64.2% of species with AMR. [src: amr_pangenome_atlas]
- PHB: In the GTDB species analysis, PHB prevalence in Actinomycetota is 18.5% (587/3,172 species). [src: phb_granule_ecology] PHB-enriched families include Mycobacteriaceae and Nocardioidaceae. [src: phb_granule_ecology] See [[concepts/phylogenetic-distribution-of-phb-synthesis-across-bacteria-and-archaea]] and [[entities/mycobacteriaceae]].

## Metal tolerance

Within BacDive-linked Actinomycetota, 62 contamination isolates versus 772 environmental isolates show a metal tolerance score delta of +0.035 (p<0.001). [src: bacdive_metal_validation] The signal is real within Pseudomonadota and Actinomycetota but absent in Bacillota and Bacteroidota. [src: bacdive_metal_validation] The report proposes that this reflects real biology. Pseudomonadota and Actinomycetota include major soil bacteria exposed to metals, whereas Bacillota and Bacteroidota are primarily gut-associated. [src: bacdive_metal_validation] See [[concepts/isolation-environment-validation-of-genome-predicted-metal-tolerance]] and [[entities/pseudomonadota]].

A separate BacDive analysis limits trait associations. The Gram-stain association cannot be tested within taxonomic classes. It is almost entirely a between-lineage signal of Actinomycetes versus Proteobacteria. [src: bacdive_phenotype_metal_tolerance] Within Actinomycetes, catalase-negative species have higher metal scores (d = -0.62, p < 1e-5). [src: bacdive_phenotype_metal_tolerance] See [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]].

## Response to soil warming

In Harvard Forest organic soil, Actinobacteria relative abundance is 0.249 in control and 0.315 in heated samples, log2 FC +0.341, q (BH) 0.049. [src: harvard_forest_warming] FC is fold change and BH is Benjamini-Hochberg. The report states that this Actinobacteria-up and Acidobacteria-down signal directly reproduces the same team's published amplicon and metagenome warming signature. [src: harvard_forest_warming] It cites DeAngelis et al. (2015, Front. Microbiol.) for Actinobacteria, Alphaproteobacteria and Acidobacteria as the strongest warming-responsive phyla across 5/8/20-year warmed plots, especially in the organic horizon. [src: harvard_forest_warming] It also cites Pold et al. (2016, AEM) for warming increasing the fraction of carbohydrate-degrading genes affiliated with Actinobacteria. [src: harvard_forest_warming]

The report offers two interpretations:
- Published isolate pangenomes bear on reading the DNA-level enrichment as sub-clade selection rather than only a compositional shift. [src: harvard_forest_warming]
- It calls the heated-mineral RNA glyoxylate signature together with Actinobacteria enrichment mechanistically self-consistent. [src: harvard_forest_warming]

See [[concepts/warming-response-of-soil-microbial-community-composition]], [[entities/acidobacteria]] and [[entities/glyoxylate-cycle-isocitrate-lyase-and-malate-synthase]].
