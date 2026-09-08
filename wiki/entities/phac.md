---
type: Gene_Or_Pathway
description: PHA synthase gene central to PHB biosynthesis and ecological distribution
sources:
- id: phb_granule_ecology
  resource: ../summaries/phb_granule_ecology__REPORT.md
  title: phb granule ecology
title: phaC
---
# phaC

## What this entity is

**Canonical name:** phaC, the PHA synthase committed-step gene in polyhydroxybutyrate (PHB) biosynthesis. [^phb_granule_ecology]

**Known alias:** PHA synthase gene. [^phb_granule_ecology]

**Stable external identifier:** No stable external identifier was reported for phaC in the source document. [^phb_granule_ecology]

This entity is related to [polyhydroxybutyrate-biosynthesis](polyhydroxybutyrate-biosynthesis.md), [phb-granule-ecology](../concepts/phb-granule-ecology.md), [pangenome-integration](../concepts/pangenome-integration.md), [environment-embedding-geography](../concepts/environment-embedding-geography.md), [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md), and [phb_granule_ecology__REPORT](../summaries/phb_granule_ecology__REPORT.md). [^phb_granule_ecology]

## Key facts

Across 27,690 GTDB species, 21.9% carried phaC, and 21.7% carried a complete PHB pathway defined as phaC plus phaA and phaB. [^phb_granule_ecology]

The near-identical prevalence of phaC and complete PHB pathways indicates that nearly all phaC-carrying species also possessed the upstream biosynthetic enzymes used in the report's pathway definition. [^phb_granule_ecology]

The analysis identified 11,792 phaC gene clusters across 6,067 species using pangenome annotations connected to [eggnog](eggnog.md) and [gtdb](gtdb.md). [^phb_granule_ecology]

The 6,067 phaC-carrying species represented 95 of 142 GTDB phyla. [^phb_granule_ecology]

[pseudomonadota](pseudomonadota.md) contained 4,544 phaC-carrying species, representing 74.9% of all phaC-positive species and a 60.9% phaC prevalence among its 7,456 species. [^phb_granule_ecology]

The five most PHB-enriched phyla accounted for 85.5% of phaC-positive species while comprising 30.4% of total species diversity. [^phb_granule_ecology]

At the order level, 23 orders with more than 20 species exceeded 50% phaC prevalence; Azospirillales and Rhodospirillales each reached 100%, Caulobacterales reached 99.3%, and Sphingomonadales reached 95.9%. [^phb_granule_ecology]

Species-level pathway categories were 6,005 complete, 62 synthase-only, 12,869 precursors-only, 555 accessory-only, and 8,199 absent. [^phb_granule_ecology]

The 46.5% precursors-only category was interpreted cautiously because phaA and phaB also participate in general fatty-acid and thiolase metabolism rather than uniquely indicating PHB production. [^phb_granule_ecology]

PHB prevalence was highest in plant-associated species at 44.0% and soil species at 43.6%, and lowest in animal-associated species at 3.3%, human clinical species at 7.4%, and human-associated species at 11.1%. [^phb_granule_ecology]

A chi-squared test of PHB presence against environmental variability gave chi2 = 1,656.36, p ~ 0, and dof = 2. [^phb_granule_ecology]

After genome-size stratification, high-variability environments still had higher phaC prevalence than low-variability environments in every genome-size quartile: 10.7% versus 2.5% in Q1, 18.5% versus 4.0% in Q2, 34.3% versus 10.9% in Q3, and 50.9% versus 37.4% in Q4. [^phb_granule_ecology]

The corresponding enrichment ratios were 4.4x, 4.6x, 3.1x, and 1.4x, with p = 1.18 x 10^-11, p = 3.25 x 10^-47, p = 4.17 x 10^-70, and p = 3.21 x 10^-14, respectively. [^phb_granule_ecology]

Among 248 families tested with Fisher's exact tests and Bonferroni correction at alpha = 0.05, 41 were phaC-enriched, 62 were depleted, and 145 were not significant. [^phb_granule_ecology]

The report identified 311 potential phaC horizontal-acquisition events in species from families with less than 20% phaC prevalence and 278 potential loss events in species from families with more than 80% prevalence. [^phb_granule_ecology]

Among the 311 discordant phaC-positive species, 60.1% carried phaC as an accessory gene, compared with 32.3% of all phaC-carrying species. [^phb_granule_ecology]

Overall, 5,371 species carried phaC as a core gene and 1,959 carried it as an accessory gene, with some species carrying both core and accessory copies. [^phb_granule_ecology]

The elevated accessory fraction supports ongoing horizontal acquisition, but the inference is indirect because it used core/accessory status and phylogenetic discordance rather than a directly reconstructed phaC gene tree. [^phb_granule_ecology]

The principal putative recipient families included Lachnospiraceae with 38 acquisitions, Chitinophagaceae with 22, Pelagibacteraceae with 13, Enterobacteriaceae with 11, and Planococcaceae with 10. [^phb_granule_ecology]

In NMDC metagenomic cross-validation, 3,014 of 3,492 taxon columns, or 86.3%, were mapped to GTDB genera with known PHB status, and PHB inference scores were calculated for 6,365 samples using abundance-weighted genus-level phaC prevalence. [^phb_granule_ecology]

The median proportion of taxonomic abundance matched to pangenome genera was 87.2%. [^phb_granule_ecology]

In a genus-level comparison of 693 matched genera, genera with at least 50% phaC prevalence had significantly higher NMDC abundance than genera with lower prevalence by Mann–Whitney testing, with p = 8.41 x 10^-22. [^phb_granule_ecology]

The attempted PHA synthase class analysis classified all 11,792 phaC clusters as “other_pfam” because the eggNOG PFAMs column contained domain names such as Abhydrolase_1 and PhaC_N instead of the expected Pfam accession IDs PF00561 and PF07167. [^phb_granule_ecology]

Mapping PF00561 to Abhydrolase_1 and PF07167 to PhaC_N was identified as the required next step for classifying the 11,792 phaC clusters. [^phb_granule_ecology]

## Interpretation and limitations

The distribution of phaC supports environmental selection in variable environments, but the report also identifies genome size and phylogenetic history as important confounders. [^phb_granule_ecology]

The apparent PHB-positive association with environmental niche breadth had raw rho = 0.106 with p = 1.77 x 10^-06, but after controlling for genome size it became partial rho = -0.047 with p = 0.037, representing a 56.3% reduction in effect size and a sign reversal. [^phb_granule_ecology]

The report therefore treats genome size, rather than phaC specifically, as the primary correlate of the apparent niche-breadth association. [^phb_granule_ecology]

The environmental evidence remains limited because 34.9% of species were assigned to “other_unknown,” AlphaEarth embeddings covered 83K of 293K genomes, and only 2,008 species, or 7.2% of total species diversity, entered the niche-breadth analysis. [^phb_granule_ecology]

A directly reconstructed phaC gene tree, together with phylogenetic logistic regression or phylogenetic independent contrasts, was identified as necessary to test the horizontal-transfer and environmental-selection interpretations more rigorously. [^phb_granule_ecology]

[^phb_granule_ecology]: [phb granule ecology](../summaries/phb_granule_ecology__REPORT.md)
