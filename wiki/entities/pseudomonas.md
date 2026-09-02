---
type: "Organism"
description: "Pseudomonas carbon-pathway ecology and lifestyle test organism"
sources: ["summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Pseudomonas

## What this entity is

**Canonical name:** *Pseudomonas* genus. [src: pseudomonas_carbon_ecology]

**Known aliases and report labels:** *Pseudomonas* s.s.; *Pseudomonas_E*; the *P. aeruginosa* group; the *P. fluorescens/putida* group. [src: pseudomonas_carbon_ecology]

**Stable external identifier:** No stable external identifier was reported for the genus in this document. [src: pseudomonas_carbon_ecology]

The report uses *Pseudomonas* to test whether carbon-pathway content predicts ecology and lifestyle across genome-derived species clades. [src: pseudomonas_carbon_ecology]

## Evidence from pseudomonas_carbon_ecology

The analysis used standardized [[entities/gapmind]] carbon-pathway predictions from the [[entities/kbase-ke-pangenome]] collection for 12,732 genomes across 433 *Pseudomonas* species clades under [[entities/gtdb]] release r214. [src: pseudomonas_carbon_ecology]

*Pseudomonas* s.s. contained 19 species and 6,905 genomes, whereas *Pseudomonas_E* contained 398 species and 5,687 genomes. [src: pseudomonas_carbon_ecology]

Isolation-source metadata were available for 8,171 of 12,732 genomes, or 64.2%. [src: pseudomonas_carbon_ecology]

Of 433 species, 387 had at least one classifiable genome, producing majority-lifestyle assignments of 204 free-living, 109 host-associated, 59 plant-associated, and 15 food-associated species. [src: pseudomonas_carbon_ecology]

The generated genome-level carbon-pathway table contained 789,012 rows, and species-level mean completeness across the 62 pathways was 0.882, with pathway richness ranging from 27 to 61 pathways and a mean of 54.6. [src: pseudomonas_carbon_ecology]

### Subgenus differences in carbon pathways

Among 7 *Pseudomonas* s.s. species and 189 *Pseudomonas_E* species with at least 5 genomes, 43 of 62 pathways differed significantly by [[entities/mann-whitney-u-test]] with [[entities/benjamini-hochberg-fdr]] correction at q < 0.05. [src: pseudomonas_carbon_ecology]

The largest reported completeness differences between the *P. aeruginosa* and *P. fluorescens* groups were xylose, 0.0% versus 74.4% (+74.4 percentage points); ribose, 27.9% versus 92.0% (+64.2 percentage points); arabinose, 0.0% versus 62.6% (+62.6 percentage points); galacturonate, 28.6% versus 88.4% (+59.8 percentage points); myo-inositol, 0.0% versus 58.8% (+58.8 percentage points); mannitol, 25.9% versus 77.5% (+51.6 percentage points); and sorbitol, 25.9% versus 77.4% (+51.5 percentage points). [src: pseudomonas_carbon_ecology]

Arginine, histidine, serine, and glutamate pathways, together with citrate, succinate, and pyruvate pathways, remained near-universal at >99% in both groups, while the four amino-acid pathways remained >99.5% complete in *P. aeruginosa*. [src: pseudomonas_carbon_ecology]

Nineteen pathways showed no significant subgenus difference, including acetate, pyruvate, fructose, L-lactate, D-lactate, glycerol, alanine, sucrose, 2-oxoglutarate, propionate, phenylacetate, deoxyribonate, and glucose-6-phosphate. [src: pseudomonas_carbon_ecology]

Rhamnose and fucose were more complete in *P. aeruginosa*, at 66.8%, than in the *P. fluorescens* group, at 41.3% and 45.1%, respectively, although these differences were not statistically significant after FDR correction. [src: pseudomonas_carbon_ecology]

Across *Pseudomonas* species with at least 5 genomes, free-living and plant-associated species had a median of 57 pathways complete in more than 50% of genomes, compared with 55 for host-associated species. [src: pseudomonas_carbon_ecology]

Within *Pseudomonas_E*, plant-associated species averaged 56.7 pathways, free-living species averaged 56.1, and host-associated species averaged 55.2. [src: pseudomonas_carbon_ecology]

The report finds that the primary principal component analysis (PCA) axis separated *Pseudomonas* s.s. from *Pseudomonas_E* and was driven by sugar-pathway loss, while lifestyle categories substantially overlapped within *Pseudomonas_E*. [src: pseudomonas_carbon_ecology]

These results support pathway loss in host-associated clades, but the report treats the rhamnose pattern as potentially related to *P. aeruginosa* rhamnolipid use as a virulence factor rather than as a general lifestyle signature. [src: pseudomonas_carbon_ecology]

### Ecological signal

Among 54 free-living and plant-associated species with at least 5 genomes and at least 60% majority-environment agreement, carbon-pathway profiles were significantly associated with isolation environment in a 999-permutation test with p = 0.006. [src: pseudomonas_carbon_ecology]

Between-group mean distance was 2.054, within-group mean distance was 1.890, and the between/within ratio was 1.087. [src: pseudomonas_carbon_ecology]

PCA of the 62-pathway profiles captured 74.9% of variance in the first 5 components; PC1 explained 31.2% and PC2 explained 17.9%. [src: pseudomonas_carbon_ecology]

A [[entities/random-forest]] classifier using soil, freshwater, plant_surface, and rhizosphere classes achieved balanced accuracy of 0.408 +/- 0.169 in 5-fold stratified cross-validation, above the 0.250 chance baseline. [src: pseudomonas_carbon_ecology]

The filtered dataset contained 51 species: 13 soil, 13 freshwater, 19 plant_surface, and 6 rhizosphere species. [src: pseudomonas_carbon_ecology]

The most discriminating pathways were D-serine, with importance 0.132; arabinose, 0.094; rhamnose, 0.086; fucose, 0.085; and xylose, 0.070. [src: pseudomonas_carbon_ecology]

The report therefore supports a statistically detectable but modest ecological signal in carbon-pathway space and finds that carbon profiles alone are insufficient for fine-grained environment discrimination among free-living species. [src: pseudomonas_carbon_ecology]

## Limitations and next tests

*P. aeruginosa* comprised 6,760 of 12,732 genomes, or 53% of the dataset, while many environmental species had fewer than 10 sequenced genomes, creating sampling imbalance that affects species-level comparison power. [src: pseudomonas_carbon_ecology]

The report states that [[entities/gapmind]] covers 62 common carbon pathways but omits genus-specific capabilities, including aromatic degradation pathways for toluene, naphthalene, and benzoate that are central to *P. putida* ecology. [src: pseudomonas_carbon_ecology]

The report proposes adding aromatic-pathway modules, including KEGG modules, to test whether they provide stronger environmental signal. [src: pseudomonas_carbon_ecology]

Because the dominant PCA signal separates subgenera, the report proposes [[entities/phylogenetic-generalized-least-squares]] (PGLS), a regression method that accounts for phylogenetic relatedness, or phylogenetic logistic regression using the GTDB species tree. [src: pseudomonas_carbon_ecology]

It also proposes genome-level prediction using the full 789K genome-pathway matrix, within-species analysis of *P. fluorescens* and *P. putida* metabolic ecotypes, and cross-reference with [[entities/kescience-fitnessbrowser]] RB-TnSeq fitness data for experimental validation. [src: pseudomonas_carbon_ecology]

These findings connect *Pseudomonas* carbon-pathway variation to [[concepts/ecotype-environment-gene-content]], [[concepts/environment-embedding-geography]], [[concepts/pangenome-integration]], and [[concepts/metabolic-model-gapfilling]]. [src: pseudomonas_carbon_ecology]

## Source

- [[summaries/pseudomonas_carbon_ecology__REPORT]] — Summary of the *Pseudomonas* carbon-pathway and ecology analysis. [src: pseudomonas_carbon_ecology]
