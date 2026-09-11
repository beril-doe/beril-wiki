---
type: "Summary"
description: "Genus-scale analysis links Pseudomonas carbon pathways to ecology and lifestyle."
doc_type: "short"
full_text: "sources/pseudomonas_carbon_ecology__REPORT.md"
---
# Carbon Source Utilization Predicts Ecology and Lifestyle in Pseudomonas

## Overview

This report analyzes standardized GapMind carbon-pathway predictions from the KBase Data Lakehouse `kbase_ke_pangenome` collection across 12,732 genomes and 433 *Pseudomonas* species clades (GTDB r214), testing whether carbon utilization profiles distinguish host-associated, free-living, and plant-associated lifestyles and environments. It finds strong pathway loss in the *Pseudomonas* s.s. (*P. aeruginosa* group) relative to *Pseudomonas_E* (*P. fluorescens/putida* group), while carbon profiles retain a statistically significant but modest ecological signal among free-living species. [src: pseudomonas_carbon_ecology]

## Key Findings

### Host-associated sugar-pathway loss

Among 7 *Pseudomonas* s.s. species and 189 *Pseudomonas_E* species with at least 5 genomes, 43 of 62 pathways differed significantly by Mann-Whitney U testing with Benjamini-Hochberg false-discovery-rate correction (q < 0.05). The largest differences involved plant-derived sugars and sugar alcohols: xylose completeness was 0.0% versus 74.4% (+74.4 percentage points), ribose 27.9% versus 92.0% (+64.2 percentage points), arabinose 0.0% versus 62.6% (+62.6 percentage points), galacturonate 28.6% versus 88.4% (+59.8 percentage points), myo-inositol 0.0% versus 58.8% (+58.8 percentage points), mannitol 25.9% versus 77.5% (+51.6 percentage points), and sorbitol 25.9% versus 77.4% (+51.5 percentage points), respectively comparing the *P. aeruginosa* and *P. fluorescens* groups. [src: pseudomonas_carbon_ecology]

Amino-acid pathways, including arginine, histidine, serine, and glutamate, and core organic-acid pathways, including citrate, succinate, and pyruvate, remained near-universal (>99%) in both groups; arginine, histidine, serine, and glutamate pathways remained >99.5% complete in *P. aeruginosa*. Nineteen pathways showed no significant subgenus difference, including acetate, pyruvate, fructose, L-lactate, D-lactate, glycerol, alanine, sucrose, 2-oxoglutarate, propionate, phenylacetate, deoxyribonate, and glucose-6-phosphate. [src: pseudomonas_carbon_ecology]

Rhamnose and fucose were more complete in *P. aeruginosa* (66.8%) than in the *P. fluorescens* group (41.3% and 45.1%, respectively), although these differences were not statistically significant after FDR correction. The report interprets the overall result as strongly supporting the hypothesis of pathway loss in host-associated clades, while noting that the rhamnose pattern may reflect *P. aeruginosa* use of rhamnolipids as virulence factors. [src: pseudomonas_carbon_ecology]

### Carbon profiles contain ecological signal

Among 54 free-living and plant-associated species with at least 5 genomes and at least 60% majority-environment agreement, carbon pathway profiles were significantly associated with isolation environment. A PERMANOVA-like permutation test using 999 permutations produced p = 0.006, with between-group mean distance of 2.054 exceeding within-group mean distance of 1.890 and a between/within ratio of 1.087. Principal component analysis (PCA) of the 62-pathway profiles captured 74.9% of variance in the first 5 components; PC1 explained 31.2% and PC2 explained 17.9%. [src: pseudomonas_carbon_ecology]

A Random Forest classifier trained on four environment classes—soil, freshwater, plant_surface, and rhizosphere—achieved balanced accuracy of 0.408 +/- 0.169 in 5-fold stratified cross-validation, above the 0.250 chance baseline. The filtered dataset contained 51 species: soil 13, freshwater 13, plant_surface 19, and rhizosphere 6. The most discriminating pathways were D-serine (importance 0.132), arabinose (0.094), rhamnose (0.086), fucose (0.085), and xylose (0.070). [src: pseudomonas_carbon_ecology]

The report assesses ecology prediction as partially supported: environment categories were non-random in carbon-pathway space, but the balanced accuracy of 0.408 indicates that carbon profiles alone are insufficient for fine-grained environment discrimination among free-living species. [src: pseudomonas_carbon_ecology]

### Pathway richness and the subgenus split

Across *Pseudomonas* species with at least 5 genomes, free-living and plant-associated species had higher carbon pathway richness than host-associated species, with a median of 57 pathways complete in more than 50% of genomes versus 55. Within *Pseudomonas_E*, plant-associated species averaged 56.7 pathways, free-living species 56.1, and host-associated species 55.2. [src: pseudomonas_carbon_ecology]

Across all species, the primary PCA axis separated *Pseudomonas* s.s. from *Pseudomonas_E*, driven by sugar-pathway loss; lifestyle categories substantially overlapped within *Pseudomonas_E*. The report therefore identifies the deep subgenus division as the dominant source of carbon-pathway variation rather than lifestyle differences within *Pseudomonas_E*. [src: pseudomonas_carbon_ecology]

### Dataset scale and pathway profiles

The analysis extracted GapMind carbon-pathway predictions for 12,732 genomes across 433 *Pseudomonas* species clades: *Pseudomonas* s.s. contained 19 species and 6,905 genomes, while *Pseudomonas_E* contained 398 species and 5,687 genomes. Isolation-source metadata were available for 64.2% of genomes (8,171/12,732 with classifiable sources). Keyword classification assigned 4,197 genomes to clinical sources, 1,659 to human (other), 566 to freshwater, 551 to soil, 503 to plant surface, 275 to rhizosphere, 141 to food/dairy, 136 to animal, 80 to industrial, and 63 to marine sources. [src: pseudomonas_carbon_ecology]

Of 433 species, 387 had at least one classifiable genome, yielding majority-lifestyle assignments of 204 free-living, 109 host-associated, 59 plant-associated, and 15 food-associated species. Species-level pathway completeness was the fraction of genomes scored complete or likely_complete for each of 62 GapMind pathways; mean completeness across species was 0.882, and pathway richness ranged from 27 to 61 pathways, with mean 54.6. The generated genome-level carbon-pathway table contained 789,012 rows. [src: pseudomonas_carbon_ecology]

## Caveats and Limitations

The report identifies sampling bias as a limitation: *P. aeruginosa* comprised 53% of all genomes (6,760/12,732) because of clinical importance, while many environmental species had fewer than 10 sequenced genomes. This imbalance affects the power of species-level comparisons. [src: pseudomonas_carbon_ecology]

Isolation-source classification was based on free-text keywords and introduced approximately 6.7% “unknown” and approximately 29.1% “other” classifications; misclassification could attenuate the ecological signal. Species-level majority-vote assignment also obscures genuinely generalist species that inhabit multiple environments. [src: pseudomonas_carbon_ecology]

GapMind’s 62 carbon pathways cover common carbon sources but omit genus-specific capabilities, particularly aromatic degradation pathways such as toluene, naphthalene, and benzoate degradation that are central to *P. putida* ecology. The report proposes extending the analysis with aromatic-pathway modules, including KEGG modules, to test whether they provide stronger environmental signal. [src: pseudomonas_carbon_ecology]

Phylogenetic confounding is substantial: the dominant PCA signal separates subgenera rather than lifestyles, and the analyses do not explicitly control for phylogenetic non-independence among species. The report proposes phylogenetic generalized least squares (PGLS), a regression method that accounts for phylogenetic relatedness, or phylogenetic logistic regression using the GTDB species tree. [src: pseudomonas_carbon_ecology]

The report further notes that the moderate classifier accuracy may reflect small sample sizes per class, overlap between related environments such as soil and rhizosphere, and the coarse resolution of the 62 GapMind pathways. It proposes genome-level prediction using the full 789K genome-pathway matrix, within-species analysis of *P. fluorescens* and *P. putida* metabolic ecotypes, and cross-reference with RB-TnSeq fitness data from the `kescience_fitnessbrowser` collection for experimental validation. [src: pseudomonas_carbon_ecology]

## Slots Into

- [[concepts/ecotype-environment-gene-content]] — Carbon pathway profiles, environment associations, and proposed within-species metabolic ecotypes connect gene content to ecological niche. [src: pseudomonas_carbon_ecology]
- [[concepts/environment-embedding-geography]] — PCA, permutation testing, and Random Forest results quantify how pathway profiles embed isolation environments, while the modest classifier accuracy defines the limits of that signal. [src: pseudomonas_carbon_ecology]
- [[concepts/pangenome-integration]] — The report uses species- and genome-scale pangenome pathway matrices and proposes integrating them with strain-level metadata and fitness data. [src: pseudomonas_carbon_ecology]
- [[concepts/metabolic-model-gapfilling]] — GapMind pathway completeness supplies standardized metabolic-capability predictions and motivates adding aromatic degradation pathways and experimental fitness validation. [src: pseudomonas_carbon_ecology]
