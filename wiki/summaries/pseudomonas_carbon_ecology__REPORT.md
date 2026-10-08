---
type: "Summary"
description: "Summary of a GapMind carbon-pathway analysis of 12,732 Pseudomonas genomes showing strong plant-sugar pathway loss in the P. aeruginosa group and a significant but modest ecological signal in carbon profiles among free-living species."
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

A Random Forest classifier trained on four environment classes—soil, freshwater, plant_surface, and rhizosphere—achieved balanced accuracy of 0.408 +/- 0.169 in 5-fold stratified cross-validation, above the 0.250 chance baseline. The filtered dataset contained 51 species: soil 13, freshwater 13, plant_surface 19, and rhizosphere 6. The most discriminating pathways were D-serine (importance 0.132), which the report associates with rhizosphere niches; arabinose (0.094), a plant-derived pentose sugar; rhamnose (0.086), a plant cell wall component; fucose (0.085), a plant/animal glycan sugar; and xylose (0.070), a hemicellulose-derived sugar. [src: pseudomonas_carbon_ecology]

The report assesses ecology prediction as partially supported: environment categories were non-random in carbon-pathway space, but the balanced accuracy of 0.408 indicates that carbon profiles alone are insufficient for fine-grained environment discrimination among free-living species. [src: pseudomonas_carbon_ecology]

### Pathway richness and the subgenus split

Across *Pseudomonas* species with at least 5 genomes, free-living and plant-associated species had higher carbon pathway richness than host-associated species, with a median of 57 pathways complete in more than 50% of genomes versus 55. Within *Pseudomonas_E*, plant-associated species averaged 56.7 pathways, free-living species 56.1, and host-associated species 55.2. [src: pseudomonas_carbon_ecology]

Across all species, the primary PCA axis separated *Pseudomonas* s.s. from *Pseudomonas_E*, driven by sugar-pathway loss; lifestyle categories substantially overlapped within *Pseudomonas_E*. The report therefore identifies the deep subgenus division as the dominant source of carbon-pathway variation rather than lifestyle differences within *Pseudomonas_E*. [src: pseudomonas_carbon_ecology]

### Interpretation and literature context

The report characterizes the scale of sugar-pathway loss as completeness differences of >50 pp for 7 pathways and >10 pp for 15 pathways between the host-associated and free-living subgenera. It notes that the specific pathways lost (xylose, arabinose, myo-inositol, galacturonate) are those involved in plant cell wall and rhizosphere carbon cycling. It interprets this as consistent with release from selection for plant-associated metabolism during a transition to animal host environments. That transition was not directly tested, so this remains a hypothesis. [src: pseudomonas_carbon_ecology]

The report cites Rossi et al. (2021), who documented progressive loss of metabolic versatility in chronic *P. aeruginosa* infections. It suggests the hypothesis that much of this "loss" is not acquired during infection but instead reflects ancestral metabolic streamlining of the *P. aeruginosa* lineage itself, because these pathways were already absent at the species level across thousands of isolates. The timing of loss is an interpretation, not a measured result. [src: pseudomonas_carbon_ecology]

The report places its results against earlier work on *P. fluorescens*-group metabolic diversity. It attributes to Silby et al. (2011) and Loper et al. (2012) the estimate that ~54% of the *P. fluorescens*-group pangenome encodes variable metabolic capabilities. It cites Belda et al. (2016) as documenting 92 catabolic pathways in the re-annotated *P. putida* KT2440 genome. It cites Nikel & de Lorenzo (2018) on *P. putida*'s broad carbon-source utilization spanning sugars, organic acids, and aromatics. The report states that its analysis quantifies this at genus scale: the *P. fluorescens/putida* group maintains mean richness 56.1, compared with ~50 in *P. aeruginosa*, particularly in sugar and sugar-alcohol catabolism. The 56.1 value matches the figure reported above for free-living species within *Pseudomonas_E*, and the report gives the *P. aeruginosa* value only as approximate. [src: pseudomonas_carbon_ecology]

The report cites Saati-Santamaria et al. (2022), who analyzed 3,274 *Pseudomonas* genomes and found niche-dependent functional divergence with environment-specific metabolic pathway sets. It describes the modest accuracy for fine-grained environment type (0.41) as consistent with Guo et al. (2026), who found hydrocarbon degradation genes concentrated in the accessory genome with strain-level rather than species-level variation. From this, the report hypothesizes that GapMind's 62 carbon pathways (Price et al. 2022) may be too coarse to capture niche-specific metabolic differences operating at the strain level within environmental species. [src: pseudomonas_carbon_ecology]

### Dataset scale and pathway profiles

The analysis extracted GapMind carbon-pathway predictions for 12,732 genomes across 433 *Pseudomonas* species clades (GTDB r214). The genus spans 5 GTDB subgenera. Two of them dominate: *Pseudomonas* s.s. (19 species, 6,905 genomes, primarily *P. aeruginosa*) and *Pseudomonas_E* (398 species, 5,687 genomes, comprising the *P. fluorescens*, *P. putida*, and *P. syringae* groups). Isolation-source metadata were available for 64.2% of genomes (8,171/12,732 with classifiable sources). Keyword classification assigned genomes to 10 environment categories. The percentages below are the report's own and are shares of all 12,732 genomes: clinical 4,197 (33.0%), human (other) 1,659 (13.0%), freshwater 566 (4.4%), soil 551 (4.3%), plant surface 503 (4.0%), rhizosphere 275 (2.2%), food/dairy 141 (1.1%), animal 136 (1.1%), industrial 80 (0.6%), and marine 63 (0.5%). [src: pseudomonas_carbon_ecology]

Of 433 species, 387 had at least one classifiable genome, yielding majority-lifestyle assignments of 204 free-living, 109 host-associated, 59 plant-associated, and 15 food-associated species. Species-level pathway completeness was the fraction of genomes scored complete or likely_complete for each of 62 GapMind pathways; mean completeness across species was 0.882, and pathway richness ranged from 27 to 61 pathways, with mean 54.6. The generated genome-level carbon-pathway table contained 789,012 rows. [src: pseudomonas_carbon_ecology]

The inputs came from the `kbase_ke_pangenome` collection: the tables `pangenome`, `gapmind_pathways`, `genome`, `ncbi_env`, `sample`, `gtdb_metadata`, and `gtdb_taxonomy_r214v1`. Together these supplied species pangenome statistics, carbon pathway predictions, isolation-source metadata, and taxonomy. [src: pseudomonas_carbon_ecology]

## Figures

- `pathway_heatmap.png` — heatmap of pathway completeness across species, ordered by subgenus and lifestyle. [src: pseudomonas_carbon_ecology]
- `pathway_loss_barplot.png` — barplot of pathway-completeness differences between *Pseudomonas* s.s. and *Pseudomonas_E*. [src: pseudomonas_carbon_ecology]
- `pathway_pca_by_environment.png` — PCA of free-living species colored by isolation environment. [src: pseudomonas_carbon_ecology]
- `rf_importance.png` — Random Forest feature importance for environment prediction. [src: pseudomonas_carbon_ecology]
- `pathway_richness_by_lifestyle.png` — boxplots of pathway richness by lifestyle category. [src: pseudomonas_carbon_ecology]
- `pathway_pca_by_lifestyle.png` — PCA of all species colored by lifestyle category. [src: pseudomonas_carbon_ecology]
- `environment_by_subgenus.png` — environment distribution by GTDB subgenus. [src: pseudomonas_carbon_ecology]

## Caveats and Limitations

The report identifies sampling bias as a limitation: *P. aeruginosa* comprised 53% of all genomes (6,760/12,732) because of clinical importance, while many environmental species had fewer than 10 sequenced genomes. This imbalance affects the power of species-level comparisons. [src: pseudomonas_carbon_ecology]

Isolation-source classification was based on free-text keywords and introduced approximately 6.7% “unknown” and approximately 29.1% “other” classifications; misclassification could attenuate the ecological signal. Species-level majority-vote assignment also obscures genuinely generalist species that inhabit multiple environments. [src: pseudomonas_carbon_ecology]

GapMind’s 62 carbon pathways cover common carbon sources but omit genus-specific capabilities, particularly aromatic degradation pathways such as toluene, naphthalene, and benzoate degradation that are central to *P. putida* ecology. The report proposes extending the analysis with aromatic-pathway modules, including KEGG modules, to test whether they provide stronger environmental signal. [src: pseudomonas_carbon_ecology]

Phylogenetic confounding is substantial: the dominant PCA signal separates subgenera rather than lifestyles, and the analyses do not explicitly control for phylogenetic non-independence among species. The report proposes phylogenetic generalized least squares (PGLS), a regression method that accounts for phylogenetic relatedness, or phylogenetic logistic regression using the GTDB species tree. [src: pseudomonas_carbon_ecology]

The report further notes that the moderate classifier accuracy may reflect small sample sizes per class, overlap between related environments such as soil and rhizosphere, and the coarse resolution of the 62 GapMind pathways. Several species, such as *P. fluorescens* and *P. putida*, are isolated from multiple environments, so the report proposes a within-species analysis of pathway variation to test whether it reveals metabolic ecotypes, meaning subpopulations adapted to different niches. Environment prediction in this report was conducted at species level. The report proposes moving to genome-level prediction using the full 789K genome-pathway matrix with genome-specific isolation sources, to increase statistical power. It also proposes cross-referencing carbon pathway predictions with RB-TnSeq (random barcode transposon sequencing) fitness data from the `kescience_fitnessbrowser` (Fitness Browser) collection. That comparison would experimentally test which pathways are functionally important on specific carbon sources. None of these analyses is reported as performed. [src: pseudomonas_carbon_ecology]

## Slots Into

- [[concepts/ecotype-environment-gene-content]] — Carbon pathway profiles, environment associations, and proposed within-species metabolic ecotypes connect gene content to ecological niche. [src: pseudomonas_carbon_ecology]
- [[concepts/environment-embedding-geography]] — PCA, permutation testing, and Random Forest results quantify how pathway profiles embed isolation environments, while the modest classifier accuracy defines the limits of that signal. [src: pseudomonas_carbon_ecology]
- [[concepts/pangenome-integration]] — The report uses species- and genome-scale pangenome pathway matrices and proposes integrating them with strain-level metadata and fitness data. [src: pseudomonas_carbon_ecology]
- [[concepts/metabolic-model-gapfilling]] — GapMind pathway completeness supplies standardized metabolic-capability predictions and motivates adding aromatic degradation pathways and experimental fitness validation. [src: pseudomonas_carbon_ecology]
- [[concepts/metabolic-capacity-specialization]] — Lineage-level loss of plant-sugar pathways in the *P. aeruginosa* group, the shared-core null pathways, and the non-significant rhamnose/fucose excess illustrate subgenus-scale metabolic specialization. [src: pseudomonas_carbon_ecology]
- [[concepts/within-species-conservation-between-species-functional-divergence]] — Large between-subgenus completeness differences contrast with species-level pathway conservation. [src: pseudomonas_carbon_ecology]
- [[concepts/two-speed-bacterial-genome]] — Near-universal amino-acid and core organic-acid pathways persist while sugar catabolism is lost. [src: pseudomonas_carbon_ecology]
- [[concepts/biosynthetic-prototrophy-and-auxotrophy]] — Retained amino-acid pathways in *P. aeruginosa* are interpreted as nutritional specialization. [src: pseudomonas_carbon_ecology]
- [[concepts/pangenome-openness-determinants]] — The report cites literature estimating that much of the *P. fluorescens*-group pangenome encodes variable metabolic capabilities. [src: pseudomonas_carbon_ecology]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — The dominant PCA axis separates subgenera, analyses lack phylogenetic control, and PGLS is proposed. [src: pseudomonas_carbon_ecology]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]] — Clinical over-representation of *P. aeruginosa* genomes and incomplete isolation-source metadata bias the ecological comparison. [src: pseudomonas_carbon_ecology]
- [[concepts/sampling-depth-and-downsampling-effects]] — Sparse genomes for environmental species and the proposed shift to genome-level prediction bear on statistical power. [src: pseudomonas_carbon_ecology]
- [[concepts/sample-size-aware-phenotype-consensus]] — Species-level completeness fractions, minimum-genome filters, and majority-vote environment assignment shape the consensus phenotype. [src: pseudomonas_carbon_ecology]
- [[concepts/ontology-and-category-schema-sensitivity]] — Keyword environment categories and the fixed GapMind pathway set constrain what can be detected. [src: pseudomonas_carbon_ecology]
- [[concepts/pathway-versus-reaction-evidence-resolution]] — The report hypothesizes that GapMind pathways are too coarse for strain-level niche differences. [src: pseudomonas_carbon_ecology]
- [[concepts/cross-condition-metabolic-comparability]] — Missing aromatic degradation pathways limit comparison across catabolic capabilities. [src: pseudomonas_carbon_ecology]
- [[concepts/computational-pathway-prediction-validation]] — Aromatic-module extension and RB-TnSeq validation are proposed but not performed. [src: pseudomonas_carbon_ecology]
- [[concepts/lab-field-fitness-concordance]] — Proposed Fitness Browser cross-reference would test predicted pathways against laboratory fitness. [src: pseudomonas_carbon_ecology]
- [[concepts/ecotype-clustering-validity]] — Within-species metabolic ecotypes in multi-environment species are proposed, not yet tested. [src: pseudomonas_carbon_ecology]
- [[concepts/taxonomic-resolution-dependent-functional-inference]] — Species-level prediction is proposed to move to genome level. [src: pseudomonas_carbon_ecology]
