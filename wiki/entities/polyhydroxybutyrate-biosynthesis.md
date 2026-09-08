---
type: Gene_Or_Pathway
description: PHB pathway defined by phaA, phaB, and phaC
sources:
- id: phb_granule_ecology
  resource: ../summaries/phb_granule_ecology__REPORT.md
  title: phb granule ecology
title: Polyhydroxybutyrate biosynthesis
---
# Polyhydroxybutyrate biosynthesis

## Identity

**Canonical name:** Polyhydroxybutyrate biosynthesis. **Known aliases:** PHB biosynthesis; complete PHB pathway. [^phb_granule_ecology]

The pathway is defined in this report as the combination of phaC, the PHA synthase committed step, with phaA and phaB. [^phb_granule_ecology] No stable external identifier was reported for the pathway. [^phb_granule_ecology]

Related gene entities are [phaa](phaa.md), [phab](phab.md), and [phac](phac.md). The pathway is discussed in the broader context of [phb-granule-ecology](../concepts/phb-granule-ecology.md), [pangenome-integration](../concepts/pangenome-integration.md), [environment-embedding-geography](../concepts/environment-embedding-geography.md), and [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md). [^phb_granule_ecology]

## Distribution across GTDB species

Across 27,690 GTDB species, 21.9% carried phaC and 21.7% carried a complete PHB pathway defined as phaC plus phaA/phaB. [^phb_granule_ecology] The analysis identified 118,513 PHB-related gene clusters across 19,496 species using eggNOG annotations. [^phb_granule_ecology] The near-identical prevalence of phaC and complete pathways indicates that nearly all phaC-carrying species also possessed the upstream biosynthetic enzymes. [^phb_granule_ecology]

PHB prevalence was 60.9% in Pseudomonadota (4,544/7,456 species), 52.9% in Myxococcota (83/157), 34.4% in Halobacteriota (89/259), 27.9% in Thermoproteota (65/233), 21.9% in Desulfobacterota (70/319), and 18.5% in Actinomycetota (587/3,172). [^phb_granule_ecology] Campylobacterota (0/271), Gemmatimonadota (0/102), Nanoarchaeota (0/135), and Marinisomatota (0/90) had no detected PHB, while Patescibacteria had 0.4% prevalence (4/981). [^phb_granule_ecology]

The 6,067 phaC-carrying species spanned 95 of 142 GTDB phyla. [^phb_granule_ecology] Pseudomonadota contributed 74.9% of phaC-carrying species (4,544/6,067), and the five most PHB-enriched phyla—Pseudomonadota, Myxococcota, Halobacteriota, Thermoproteota, and Desulfobacterota—accounted for 85.5% of phaC-positive species while comprising 30.4% of total species diversity. [^phb_granule_ecology]

At the order level, 23 orders with more than 20 species exceeded 50% phaC prevalence; Azospirillales and Rhodospirillales each had 100% prevalence, Caulobacterales had 99.3%, and Sphingomonadales had 95.9%. [^phb_granule_ecology] In contrast, 117 orders had less than 10% phaC prevalence. [^phb_granule_ecology]

## Gene-level composition

The gene-level census identified 86,318 phaA clusters across 17,969 species, 11,792 phaC clusters across 6,067 species, 9,617 phaB clusters across 6,977 species, 6,130 phaP clusters across 4,571 species, and 4,656 phaZ clusters across 3,151 species. [^phb_granule_ecology] No phaR clusters were detected among 0 species. [^phb_granule_ecology]

Species-level categories were complete (6,005), synthase-only (62), precursors-only (12,869), accessory-only (555), and absent (8,199). [^phb_granule_ecology] The 46.5% precursors-only category likely overestimates partial PHB capability because phaA and phaB also participate in general fatty-acid and thiolase metabolism. [^phb_granule_ecology] The absence of phaR may reflect incomplete annotation or misassignment of K18080. [^phb_granule_ecology]

## Environmental distribution and genome-size effects

PHB prevalence was highest among plant-associated species at 44.0% (625 total) and soil species at 43.6% (1,484 total), followed by wastewater/engineered species at 34.5% (1,124 total), freshwater species at 25.5% (3,263 total), sediment species at 20.1% (1,020 total), marine species at 18.7% (3,010 total), human-associated species at 11.1% (1,237 total), human clinical species at 7.4% (2,472 total), and animal-associated species at 3.3% (3,711 total). [^phb_granule_ecology]

A chi-squared test of PHB presence against environmental variability category yielded chi2 = 1,656.36, p ~ 0, dof = 2. [^phb_granule_ecology] This result supports enrichment of PHB genes in temporally variable “feast/famine” environments and depletion in stable or host-associated environments. [^phb_granule_ecology]

The environmental enrichment persisted after genome-size stratification. [^phb_granule_ecology] In Q1 (0.4–1.8 Mbp), high-variability environments had 10.7% phaC-positive species versus 2.5% in low-variability environments, a 4.4x enrichment with p = 1.18 x 10^-11. [^phb_granule_ecology] In Q2, the corresponding values were 18.5% versus 4.0%, a 4.6x enrichment with p = 3.25 x 10^-47. [^phb_granule_ecology] In Q3, they were 34.3% versus 10.9%, a 3.1x enrichment with p = 4.17 x 10^-70. [^phb_granule_ecology] In Q4 (3.7–14.0 Mbp), they were 50.9% versus 37.4%, a 1.4x enrichment with p = 3.21 x 10^-14. [^phb_granule_ecology]

Among 2,008 species with sufficient AlphaEarth environmental-embedding representation, PHB-positive species had median embedding variance of 0.3295 (n = 531), compared with 0.2472 for PHB-negative species (n = 1,477); the Mann–Whitney U statistic was 446,546 with p = 1.88 x 10^-6. [^phb_granule_ecology] The raw PHB–niche-breadth association was rho = 0.106 with p = 1.77 x 10^-06. [^phb_granule_ecology]

PHB-positive species had median genome size of 4.34 Mbp versus 2.44 Mbp for PHB-negative species, with rank-biserial r = -0.592 and p ~ 0. [^phb_granule_ecology] Genome size correlated with niche breadth at rho = 0.302 with p = 1.5e-43. [^phb_granule_ecology] After controlling for genome size using partial Spearman correlation, the PHB–niche-breadth association became partial rho = -0.047 with p = 0.037, representing a 56.3% reduction in effect size and a sign reversal. [^phb_granule_ecology] These results support genome size, rather than PHB specifically, as the primary correlate of the apparent niche-breadth association. [^phb_granule_ecology]

## Accessory status and putative horizontal transfer

Phylogenetically discordant phaC distribution identified 311 potential HGT acquisition events in species carrying phaC despite belonging to families with less than 20% phaC prevalence, and 278 potential HGT loss events in species lacking phaC despite belonging to families with more than 80% prevalence. [^phb_granule_ecology] Among the 311 discordant phaC-positive species, 60.1% carried phaC as accessory genome, compared with 32.3% of all phaC-carrying species. [^phb_granule_ecology] This elevated accessory fraction supports ongoing horizontal acquisition, although the analysis used core/accessory status as a proxy rather than a directly reconstructed gene tree. [^phb_granule_ecology]

The principal putative recipient families were Lachnospiraceae with 38 acquisitions and 3.1% family phaC prevalence, Chitinophagaceae with 22 and 12.4%, Pelagibacteraceae with 13 and 5.3%, Enterobacteriaceae with 11 and 2.3%, and Planococcaceae with 10 and 12.8%. [^phb_granule_ecology] Overall, 5,371 species carried phaC as core and 1,959 carried it as accessory, with some species carrying both core and accessory copies. [^phb_granule_ecology]

## NMDC cross-validation

A two-tier taxonomy mapping connected 3,014/3,492 NMDC taxon columns (86.3%) to GTDB genera with known PHB status. [^phb_granule_ecology] PHB inference scores were calculated for 6,365 NMDC metagenomic samples as abundance-weighted sums of genus-level phaC prevalence, with a median 87.2% of taxonomic abundance matched to pangenome genera. [^phb_granule_ecology]

PHB inference scores correlated with depth at rho = -0.119 and p = 1.14 x 10^-21, temperature at rho = +0.088 and p = 1.86 x 10^-12, maximum depth at rho = +0.076 and p = 1.15 x 10^-9, minimum depth at rho = -0.055 and p = 1.05 x 10^-5, pH at rho = +0.049 and p = 7.95 x 10^-5, and ammonium nitrogen at rho = +0.044 and p = 4.49 x 10^-4. [^phb_granule_ecology] These correlations were modest, with |rho| < 0.12, and did not directly measure temporal environmental variability. [^phb_granule_ecology]

In a genus-level cross-validation, 693 genera were matched between pangenome and NMDC metagenomes. [^phb_granule_ecology] PHB-high genera, defined as having at least 50% phaC prevalence, had significantly higher NMDC abundance than PHB-low genera by Mann–Whitney testing (p = 8.41 x 10^-22). [^phb_granule_ecology] The most abundant PHB-high genera included Mycobacterium, Pseudomonas, Cupriavidus, Burkholderia, and Methylobacterium. [^phb_granule_ecology]

## Limitations

The PHA synthase class analysis classified all 11,792 phaC clusters as “other_pfam” because the eggNOG PFAMs column contained domain names such as Abhydrolase_1 and PhaC_N rather than the expected Pfam accession IDs PF00561 and PF07167. [^phb_granule_ecology] Mapping PF00561 to Abhydrolase_1 for Class I/II and PF07167 to PhaC_N for Class III/IV was identified as the required correction. [^phb_granule_ecology]

Environmental metadata were sparse, with 34.9% of species assigned “other_unknown” as their primary environment. [^phb_granule_ecology] AlphaEarth coverage included 83K/293K genomes, or 28%, and the 2,008 species analyzed represented 7.2% of total species diversity. [^phb_granule_ecology] The pangenome included complete genomes and MAGs with variable genome quality and gene-detection rates. [^phb_granule_ecology]

PHB has functions beyond carbon storage, including stress resistance, redox balance, and cryoprotection, so environmental variability is supported as a selective force but is not necessarily the sole driver of pathway distribution. [^phb_granule_ecology] Phylogenetic logistic regression or phylogenetic independent contrasts are still needed to account for shared ancestry, and a directly reconstructed phaC gene tree is needed to identify incongruent branches. [^phb_granule_ecology]

## Source

See the full project summary: [phb_granule_ecology__REPORT](../summaries/phb_granule_ecology__REPORT.md). [^phb_granule_ecology]

[^phb_granule_ecology]: [phb granule ecology](../summaries/phb_granule_ecology__REPORT.md)
