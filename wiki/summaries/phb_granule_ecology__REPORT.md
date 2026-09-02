---
type: "Summary"
description: "Pangenome-scale analysis of PHB ecology, distribution, and horizontal transfer"
doc_type: "short"
full_text: "sources/phb_granule_ecology__REPORT.md"
---
# Polyhydroxybutyrate Granule Formation Pathways — Distribution Across Clades and Environmental Selection

## Overview

This report evaluates polyhydroxybutyrate (PHB) biosynthesis across 27,690 GTDB species using pangenome annotations, taxonomy, environmental metadata, AlphaEarth embeddings, and NMDC metagenomes. It finds that phaC and complete PHB pathways are phylogenetically concentrated, enriched in environmentally variable habitats, associated with larger genomes, and frequently accessory in phylogenetically discordant lineages, supporting environmental selection and widespread horizontal gene transfer (HGT) while qualifying the apparent PHB–niche-breadth association as largely genome-size driven. [src: phb_granule_ecology]

## Key Findings

### Phylogenetic distribution and pathway completeness

Across 27,690 GTDB species, 21.9% carry phaC, the PHA synthase committed step, and 21.7% have a complete PHB pathway defined as phaC plus phaA/phaB. A total of 118,513 PHB-related gene clusters were identified across 19,496 species using eggNOG annotations. The near-identical phaC-only and complete-pathway prevalence indicates that nearly all phaC-carrying species also possess upstream biosynthetic enzymes. [src: phb_granule_ecology]

PHB prevalence is highest in Pseudomonadota at 60.9% (4,544/7,456 species), followed by Myxococcota at 52.9% (83/157), Halobacteriota at 34.4% (89/259), Thermoproteota at 27.9% (65/233), Desulfobacterota at 21.9% (70/319), and Actinomycetota at 18.5% (587/3,172). Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135), and Marinisomatota (0/90) were entirely devoid of PHB, while Patescibacteria had 0.4% prevalence (4/981). [src: phb_granule_ecology]

The 6,067 phaC-carrying species span 95 of 142 GTDB phyla. Pseudomonadota accounts for 74.9% of phaC-carrying species (4,544/6,067), and the five most PHB-enriched phyla—Pseudomonadota, Myxococcota, Halobacteriota, Thermoproteota, and Desulfobacterota—account for 85.5% of phaC-positive species while comprising 30.4% of total species diversity. At order level, 23 orders with more than 20 species exceed 50% phaC prevalence; Azospirillales and Rhodospirillales are both at 100%, Caulobacterales at 99.3%, and Sphingomonadales at 95.9%, whereas 117 orders are below 10%. [src: phb_granule_ecology]

The gene-level census identified 86,318 phaA clusters across 17,969 species, 11,792 phaC clusters across 6,067 species, 9,617 phaB clusters across 6,977 species, 6,130 phaP clusters across 4,571 species, 4,656 phaZ clusters across 3,151 species, and 0 phaR clusters across 0 species. Species-level categories were complete (6,005), synthase-only (62), precursors-only (12,869), accessory-only (555), and absent (8,199). The 46.5% precursors-only category reflects the pleiotropic roles of phaA and phaB in general fatty-acid and thiolase metabolism, while the absence of phaR suggests incomplete annotation or misassignment of K18080. [src: phb_granule_ecology]

### Environmental enrichment and the feast/famine hypothesis

PHB prevalence follows an environmental gradient: plant-associated species, 625 total, have 44.0% phaC prevalence; soil species, 1,484 total, have 43.6%; wastewater/engineered species, 1,124 total, have 34.5%; freshwater species, 3,263 total, have 25.5%; sediment species, 1,020 total, have 20.1%; marine species, 3,010 total, have 18.7%; human-associated species, 1,237 total, have 11.1%; human clinical species, 2,472 total, have 7.4%; and animal-associated species, 3,711 total, have 3.3%. [src: phb_granule_ecology]

A chi-squared test of PHB presence against environmental variability category yielded chi2 = 1,656.36, p ~ 0, dof = 2. This strongly supports the report’s H1a hypothesis that PHB genes are enriched in temporally variable “feast/famine” environments and depleted in stable or host-associated environments. [src: phb_granule_ecology]

The environmental enrichment remains after genome-size stratification. In the smallest-genome quartile, Q1 (0.4–1.8 Mbp), high-variability environments had 10.7% phaC-positive species versus 2.5% in low-variability environments, a 4.4x enrichment with p = 1.18 x 10^-11. Q2 had 18.5% versus 4.0%, a 4.6x enrichment with p = 3.25 x 10^-47; Q3 had 34.3% versus 10.9%, a 3.1x enrichment with p = 4.17 x 10^-70; and Q4 (3.7–14.0 Mbp) had 50.9% versus 37.4%, a 1.4x enrichment with p = 3.21 x 10^-14. [src: phb_granule_ecology]

### Niche breadth and genome-size confounding

Among 2,008 species with sufficient AlphaEarth environmental-embedding representation, PHB-positive species had median embedding variance of 0.3295 (n = 531), compared with 0.2472 for PHB-negative species (n = 1,477); the Mann–Whitney U statistic was 446,546 with p = 1.88 x 10^-6. The raw PHB–niche-breadth association was rho = 0.106 with p = 1.77 x 10^-06. [src: phb_granule_ecology]

PHB-positive species had median genome size of 4.34 Mbp versus 2.44 Mbp for PHB-negative species, with rank-biserial r = -0.592 and p ~ 0. Genome size correlated with niche breadth at rho = 0.302 with p = 1.5e-43. After controlling for genome size using partial Spearman correlation, the PHB–niche-breadth association became partial rho = -0.047 with p = 0.037, a 56.3% reduction in effect size and a sign reversal. The report therefore treats genome size, rather than PHB specifically, as the primary correlate of the apparent niche-breadth association. [src: phb_granule_ecology]

### Subclade heterogeneity and horizontal transfer

Among 248 families tested with Fisher’s exact tests and Bonferroni correction at alpha = 0.05, 41 were PHB-enriched, 62 were depleted, and 145 were not significant. Enriched families included Burkholderiaceae, Burkholderiaceae_B, Rhodocyclaceae, Caulobacteraceae, Sphingomonadaceae, Xanthobacteraceae, Rhodanobacteraceae, Legionellaceae, Mycobacteriaceae, Nocardioidaceae, Haloarculaceae, Natrialbaceae, Nitrosopumilaceae, Microcystaceae, and Bacillaceae_G. Enriched families skewed toward freshwater (5/41) and wastewater (3/41), whereas depleted families skewed toward marine (18/62) and host-associated environments (12/62). The interpretation is limited because “other_unknown” represented 30/41 enriched families and 26/62 depleted families. [src: phb_granule_ecology]

Phylogenetically discordant phaC distribution identified 311 potential HGT acquisition events in species carrying phaC despite belonging to families with less than 20% phaC prevalence, and 278 potential HGT loss events in species lacking phaC despite belonging to families with more than 80% prevalence. Among the 311 discordant phaC-positive species, 60.1% carried phaC as accessory genome, compared with 32.3% of all phaC-carrying species. This elevated accessory fraction supports ongoing horizontal acquisition, although the analysis uses core/accessory status as a proxy rather than a directly reconstructed gene tree. [src: phb_granule_ecology]

The principal putative recipient families were Lachnospiraceae with 38 acquisitions and 3.1% family phaC prevalence, Chitinophagaceae with 22 and 12.4%, Pelagibacteraceae with 13 and 5.3%, Enterobacteriaceae with 11 and 2.3%, and Planococcaceae with 10 and 12.8%. Overall, 5,371 species carried phaC as core and 1,959 as accessory, with some species carrying both core and accessory copies. [src: phb_granule_ecology]

### NMDC metagenomic cross-validation

A two-tier taxonomy mapping connected 3,014/3,492 NMDC taxon columns (86.3%) to GTDB genera with known PHB status: 2,336 columns through the gtdb_metadata NCBI-taxid-to-GTDB-genus bridge and 678 additional columns through direct genus-name matching. PHB inference scores were calculated for 6,365 NMDC metagenomic samples as abundance-weighted sums of genus-level phaC prevalence, with a median 87.2% of taxonomic abundance matched to pangenome genera. [src: phb_granule_ecology]

PHB inference scores correlated with depth at rho = -0.119 and p = 1.14 x 10^-21, temperature at rho = +0.088 and p = 1.86 x 10^-12, maximum depth at rho = +0.076 and p = 1.15 x 10^-9, minimum depth at rho = -0.055 and p = 1.05 x 10^-5, pH at rho = +0.049 and p = 7.95 x 10^-5, and ammonium nitrogen at rho = +0.044 and p = 4.49 x 10^-4. These effect sizes are modest, with |rho| < 0.12, and are consistent with but do not directly measure temporal environmental variability. [src: phb_granule_ecology]

In a genus-level cross-validation, 693 genera were matched between pangenome and NMDC metagenomes. PHB-high genera, defined as having at least 50% phaC prevalence, had significantly higher NMDC abundance than PHB-low genera by Mann–Whitney testing (p = 8.41 x 10^-22). The most abundant PHB-high genera included Mycobacterium, Pseudomonas, Cupriavidus, Burkholderia, and Methylobacterium. [src: phb_granule_ecology]

The attempted PHA synthase class analysis classified all 11,792 phaC clusters as “other_pfam” because the eggNOG PFAMs column contained domain names such as Abhydrolase_1 and PhaC_N rather than the expected Pfam accession IDs PF00561 and PF07167. [src: phb_granule_ecology]

## Caveats and Limitations

NMDC cross-validation correlations were statistically significant but small (|rho| < 0.12). NMDC abiotic measurements are point-in-time values rather than measures of temporal variability, and the studies are biased toward terrestrial and soil environments, limiting direct testing of the feast/famine hypothesis. [src: phb_granule_ecology]

PHA synthase class analysis failed because Pfam accession IDs were not mapped to eggNOG domain names; mapping PF00561 to Abhydrolase_1 for Class I/II and PF07167 to PhaC_N for Class III/IV is required to classify the 11,792 phaC clusters. [src: phb_granule_ecology]

Environment metadata are sparse: 34.9% of species have “other_unknown” as their primary environment, so environmental enrichment may be underestimated. AlphaEarth coverage is also limited: 83K/293K genomes, or 28%, have embeddings, and the 2,008 species analyzed represent 7.2% of total species diversity, potentially biasing niche-breadth analyses toward better-sampled lineages. [src: phb_granule_ecology]

Because phaA and phaB participate in general metabolism beyond PHB biosynthesis, the 46.5% precursors-only category likely overestimates partial PHB capability. The pangenome includes complete genomes and MAGs with variable genome quality and gene-detection rates. [src: phb_granule_ecology]

PHB presence is correlated with phylogeny and genome size, and the PHB–niche-breadth association falls from raw rho = 0.106 with p = 1.77e-06 to partial rho = -0.047 with p = 0.037 after controlling for genome size. Although PHB environmental enrichment persists across all four genome-size quartiles with 1.4–4.6x enrichment and all p < 1e-11, phylogenetic logistic regression or phylogenetic independent contrasts are still needed to account for shared ancestry. [src: phb_granule_ecology]

PHB has functions beyond carbon storage, including stress resistance, redox balance, and cryoprotection, so environmental variability is supported as a selective force but is not necessarily the sole driver of PHB distribution. The HGT inference is likewise based on phylogenetic discordance and core/accessory status; a directly reconstructed phaC gene tree is needed to identify incongruent branches. [src: phb_granule_ecology]

## Slots Into

- [[concepts/phb-granule-ecology]] — Central synthesis of PHB pathway distribution, environmental selection, genome-size confounding, and HGT; this finding requires a dedicated cross-project concept.
- [[concepts/environment-embedding-geography]] — AlphaEarth embedding variance, environmental breadth, and the genome-size-controlled interpretation of PHB–niche association.
- [[concepts/pangenome-integration]] — Pangenome-scale PHB prevalence, core/accessory phaC status, and NMDC metagenomic cross-validation.
- [[concepts/gene-function-acquisition-depth]] — Putative phaC acquisition and loss events, elevated accessory status among discordant species, and the need for gene-tree validation.
