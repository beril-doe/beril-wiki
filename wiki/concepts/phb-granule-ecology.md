---
type: "Concept"
description: "PHB ecology shaped by environmental variability, genome size, and horizontal transfer"
sources: ["summaries/phb_granule_ecology__REPORT.md"]
---
# Polyhydroxybutyrate pathway ecology, genome size, and horizontal transfer

Polyhydroxybutyrate (PHB) biosynthesis is unevenly distributed across bacterial and archaeal diversity, enriched in environmentally variable habitats, associated with larger genomes, and often accessory in phylogenetically unusual lineages. These results support environmental selection and widespread horizontal gene transfer (HGT), while showing that the apparent relationship between PHB and environmental niche breadth is largely explained by genome size. [src: phb_granule_ecology]

This synthesis is based on the [[summaries/phb_granule_ecology__REPORT]] analysis of 27,690 [[entities/gtdb]] species, pangenome annotations, environmental metadata, AlphaEarth embeddings, and [[entities/nmdc]] metagenomes. [src: phb_granule_ecology]

## Pathway distribution and completeness

The committed PHB biosynthesis step, phaC, occurred in 21.9% of 27,690 GTDB species, while 21.7% carried a complete PHB pathway defined as phaC plus phaA and phaB. [src: phb_granule_ecology] The analysis identified 118,513 PHB-related gene clusters across 19,496 species using eggNOG annotations. [src: phb_granule_ecology] The near-identical prevalence of phaC and complete pathways indicates that nearly all phaC-carrying species also possess the upstream biosynthetic enzymes. [src: phb_granule_ecology]

PHB prevalence was highest in Pseudomonadota at 60.9% (4,544/7,456 species), followed by Myxococcota at 52.9% (83/157), Halobacteriota at 34.4% (89/259), Thermoproteota at 27.9% (65/233), Desulfobacterota at 21.9% (70/319), and Actinomycetota at 18.5% (587/3,172). [src: phb_granule_ecology] Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135), and Marinisomatota (0/90) had no detected PHB, while Patescibacteria had 0.4% prevalence (4/981). [src: phb_granule_ecology]

The 6,067 phaC-carrying species spanned 95 of 142 GTDB phyla. [src: phb_granule_ecology] Pseudomonadota accounted for 74.9% of phaC-carrying species (4,544/6,067), and the five most PHB-enriched phyla accounted for 85.5% of phaC-positive species while comprising 30.4% of total species diversity. [src: phb_granule_ecology] At the order level, 23 orders with more than 20 species exceeded 50% phaC prevalence; Azospirillales and Rhodospirillales each reached 100%, Caulobacterales reached 99.3%, and Sphingomonadales reached 95.9%, whereas 117 orders were below 10%. [src: phb_granule_ecology]

The gene-level census found 86,318 phaA clusters across 17,969 species, 11,792 phaC clusters across 6,067 species, 9,617 phaB clusters across 6,977 species, 6,130 phaP clusters across 4,571 species, 4,656 phaZ clusters across 3,151 species, and 0 phaR clusters across 0 species. [src: phb_granule_ecology] Species-level categories were complete (6,005), synthase-only (62), precursors-only (12,869), accessory-only (555), and absent (8,199). [src: phb_granule_ecology] The 46.5% precursors-only category likely overestimates partial PHB capability because phaA and phaB also participate in general fatty-acid and thiolase metabolism. [src: phb_granule_ecology] The absence of phaR may reflect incomplete annotation or misassignment of K18080 rather than biological absence. [src: phb_granule_ecology]

## Environmental selection and the feast/famine hypothesis

PHB prevalence followed an environmental gradient: plant-associated species had 44.0% phaC prevalence (625 total), soil species had 43.6% (1,484 total), wastewater/engineered species had 34.5% (1,124 total), freshwater species had 25.5% (3,263 total), sediment species had 20.1% (1,020 total), marine species had 18.7% (3,010 total), human-associated species had 11.1% (1,237 total), human clinical species had 7.4% (2,472 total), and animal-associated species had 3.3% (3,711 total). [src: phb_granule_ecology]

A chi-squared test of PHB presence against environmental variability category yielded chi2 = 1,656.36, p ~ 0, dof = 2. [src: phb_granule_ecology] This strongly supports the hypothesis that PHB genes are enriched in temporally variable feast/famine environments and depleted in stable or host-associated environments. [src: phb_granule_ecology] PHB also has functions beyond carbon storage, including stress resistance, redox balance, and cryoprotection, so environmental variability is supported as a selective force but is not necessarily the sole driver of PHB distribution. [src: phb_granule_ecology]

The environmental enrichment supports, rather than replaces, the broader [[concepts/environment-embedding-geography]] interpretation of environmental specialization. [src: phb_granule_ecology] After stratification by genome size, high-variability environments still had higher phaC prevalence in every quartile: Q1 (0.4–1.8 Mbp) had 10.7% versus 2.5%, a 4.4x enrichment with p = 1.18 x 10^-11; Q2 had 18.5% versus 4.0%, a 4.6x enrichment with p = 3.25 x 10^-47; Q3 had 34.3% versus 10.9%, a 3.1x enrichment with p = 4.17 x 10^-70; and Q4 (3.7–14.0 Mbp) had 50.9% versus 37.4%, a 1.4x enrichment with p = 3.21 x 10^-14. [src: phb_granule_ecology]

## Genome size and niche breadth

Among 2,008 species with sufficient AlphaEarth environmental-embedding representation, PHB-positive species had median embedding variance of 0.3295 (n = 531), compared with 0.2472 for PHB-negative species (n = 1,477); the Mann–Whitney U statistic was 446,546 with p = 1.88 x 10^-6. [src: phb_granule_ecology] The raw PHB–niche-breadth association was rho = 0.106 with p = 1.77 x 10^-06. [src: phb_granule_ecology]

PHB-positive species had median genome size of 4.34 Mbp versus 2.44 Mbp for PHB-negative species, with rank-biserial r = -0.592 and p ~ 0. [src: phb_granule_ecology] Genome size correlated with niche breadth at rho = 0.302 with p = 1.5e-43. [src: phb_granule_ecology] After controlling for genome size using partial Spearman correlation, the PHB–niche-breadth association became partial rho = -0.047 with p = 0.037, representing a 56.3% reduction in effect size and a sign reversal. [src: phb_granule_ecology]

Thus, the analysis refines the raw association: genome size, rather than PHB specifically, is the primary correlate of the apparent niche-breadth relationship. [src: phb_granule_ecology] The environmental enrichment of PHB across genome-size quartiles nevertheless supports a genome-size-independent contribution from environmental variability. [src: phb_granule_ecology] Phylogenetic logistic regression or phylogenetic independent contrasts remain necessary because PHB presence is correlated with phylogeny and genome size. [src: phb_granule_ecology]

The AlphaEarth result should be interpreted cautiously because 83K/293K genomes, or 28%, had embeddings, and the 2,008 analyzed species represented 7.2% of total species diversity. [src: phb_granule_ecology] The analysis may therefore be biased toward better-sampled lineages. [src: phb_granule_ecology]

## Accessory status and horizontal transfer

Phylogenetically discordant phaC distribution identified 311 potential HGT acquisition events in phaC-carrying species from families with less than 20% phaC prevalence and 278 potential HGT loss events in phaC-lacking species from families with more than 80% prevalence. [src: phb_granule_ecology] Among the 311 discordant phaC-positive species, 60.1% carried phaC as accessory genome, compared with 32.3% of all phaC-carrying species. [src: phb_granule_ecology] This elevated accessory fraction supports ongoing horizontal acquisition, but core/accessory status is a proxy rather than a directly reconstructed gene tree. [src: phb_granule_ecology]

The principal putative recipient families were Lachnospiraceae with 38 acquisitions and 3.1% family phaC prevalence, Chitinophagaceae with 22 and 12.4%, Pelagibacteraceae with 13 and 5.3%, Enterobacteriaceae with 11 and 2.3%, and Planococcaceae with 10 and 12.8%. [src: phb_granule_ecology] Overall, 5,371 species carried phaC as core and 1,959 as accessory, with some species carrying both core and accessory copies. [src: phb_granule_ecology]

The HGT interpretation complements [[concepts/pangenome-integration]] and [[concepts/gene-function-acquisition-depth]] by connecting accessory pangenome status to a pathway-level ecological pattern. [src: phb_granule_ecology] It remains a hypothesis about transfer history until a directly reconstructed phaC gene tree identifies incongruent branches. [src: phb_granule_ecology]

## NMDC cross-validation

A two-tier taxonomy mapping connected 3,014/3,492 NMDC taxon columns (86.3%) to GTDB genera with known PHB status: 2,336 columns through the gtdb_metadata NCBI-taxid-to-GTDB-genus bridge and 678 through direct genus-name matching. [src: phb_granule_ecology] PHB inference scores were calculated for 6,365 NMDC metagenomic samples as abundance-weighted sums of genus-level phaC prevalence, with a median 87.2% of taxonomic abundance matched to pangenome genera. [src: phb_granule_ecology]

PHB inference scores correlated with depth at rho = -0.119 and p = 1.14 x 10^-21, temperature at rho = +0.088 and p = 1.86 x 10^-12, maximum depth at rho = +0.076 and p = 1.15 x 10^-9, minimum depth at rho = -0.055 and p = 1.05 x 10^-5, pH at rho = +0.049 and p = 7.95 x 10^-5, and ammonium nitrogen at rho = +0.044 and p = 4.49 x 10^-4. [src: phb_granule_ecology] These effect sizes were modest, with |rho| < 0.12, and the measured abiotic values were point-in-time observations rather than direct measures of temporal variability. [src: phb_granule_ecology]

In genus-level cross-validation, 693 genera matched between pangenome and NMDC metagenomes. [src: phb_granule_ecology] Genera with at least 50% phaC prevalence had significantly higher NMDC abundance than genera with lower prevalence by Mann–Whitney testing (p = 8.41 x 10^-22). [src: phb_granule_ecology] The most abundant PHB-high genera included Mycobacterium, Pseudomonas, Cupriavidus, Burkholderia, and Methylobacterium. [src: phb_granule_ecology]

The NMDC results support ecological relevance of the pangenome pattern, but they do not directly validate the feast/famine mechanism because NMDC studies were biased toward terrestrial and soil environments and their abiotic measurements did not quantify temporal variability. [src: phb_granule_ecology]

## Tensions and analytical limits

The results support both a genome-size explanation for the apparent PHB–niche-breadth association and an environmental-selection explanation for PHB prevalence. [src: phb_granule_ecology] These claims address different contrasts: genome size largely explains the cross-species embedding association, whereas environmental enrichment persists within all four genome-size quartiles. [src: phb_granule_ecology]

Environmental interpretation is limited by sparse metadata: 34.9% of species had “other_unknown” as their primary environment. [src: phb_granule_ecology] The pangenome also included complete genomes and MAGs with variable genome quality and gene-detection rates. [src: phb_granule_ecology] The attempted PHA synthase class analysis classified all 11,792 phaC clusters as “other_pfam” because the eggNOG PFAMs column contained domain names such as Abhydrolase_1 and PhaC_N rather than the expected Pfam accession IDs PF00561 and PF07167. [src: phb_granule_ecology]

## Open Directions

- Reconstruct a directly aligned phaC gene tree and test gene-tree/species-tree incongruence to distinguish horizontal acquisition from lineage sorting or annotation error. [src: phb_granule_ecology]
- Apply phylogenetic logistic regression or phylogenetic independent contrasts to the 27,690-species pangenome table to test whether environmental variability predicts phaC presence after shared ancestry and genome size are controlled. [src: phb_granule_ecology]
- Map PF00561 to Abhydrolase_1 and PF07167 to PhaC_N, then classify the 11,792 phaC clusters by PHA synthase class to test whether ecological distributions differ among synthase classes. [src: phb_granule_ecology]
- Combine repeated environmental measurements with NMDC taxonomic abundances and PHB inference scores to test temporal variability directly rather than using point-in-time abiotic measurements. [src: phb_granule_ecology]
- Reanalyze the AlphaEarth association after expanding embedding coverage beyond 83K/293K genomes and testing lineage-balanced sampling, asking whether the partial rho = -0.047 association is reproducible across underrepresented clades. [src: phb_granule_ecology]
- Use genome-quality filtering and independent pathway evidence to test whether the 46.5% precursors-only category reflects genuine partial PHB capability or pleiotropic phaA/phaB metabolism. [src: phb_granule_ecology]
