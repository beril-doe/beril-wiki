---
type: "Summary"
description: "ENIGMA genotype-to-phenotype modeling, ecology, failures, and experiments"
doc_type: "short"
full_text: "sources/genotype_to_phenotype_enigma__REPORT.md"
---
# Genotype × Condition to Phenotype Prediction from ENIGMA Growth Curves

## Overview

This project integrates ENIGMA growth curves, the ENIGMA Genome Depot, Fitness Browser RB-TnSeq data, Web of Microbes exometabolomics, Carbon Source Phenotypes, pangenome data, and global 16S environmental data to test whether bacterial growth phenotypes can be predicted from genome content and growth condition. The corpus contains 46,389 genome × condition training pairs, and the study distinguishes predictable binary growth capability from poorly predictable continuous kinetics. It also links model failures to a field-relevant active-learning proposal for the Oak Ridge contaminated subsurface site. [src: genotype_to_phenotype_enigma]

## Key Findings

- The integrated ENIGMA growth-curve corpus contains 27,632 curves across 123 strains, 195 molecules, 303 plates, and 7.57M timepoints. Of these, 15,227 curves (55.1%) showed no detectable growth, 9,861 (35.7%) were fit-ok, and modified Gompertz fits had median R² = 0.98. Fit-ok curves had median µmax = 0.028 h⁻¹, median lag = 11.4 h, and median asymptotic OD increase A = 0.315; 40% showed at least two growth phases in their smoothed derivative. [src: genotype_to_phenotype_enigma]

- ENIGMA growth data align with Fitness Browser data through 486 strain × condition anchor pairs covering 7 strains and 72 conditions; 275 pairs (56.6%) showed measurable growth. Five conditions—cytidine, glycine, inosine, thymidine, and uridine—occur in all four aligned datasets, while 30 occur in three datasets. A separate carbon-source phenotype corpus contains 795 genomes and 379 conditions, and the combined modeling corpus contains 46,389 pairs across 727 genomes and 363 conditions with 4,293 shared [[entities/kegg]] orthologs (KOs). [src: genotype_to_phenotype_enigma]

- Hierarchical clustering of 7,167 KO presence/absence features across 123 strains identified 8 metabolic guilds spanning 20 taxonomic orders. Guilds aligned with, but were not identical to, taxonomy; genome sizes ranged from 2.6 to 11.4 Mb, and strains contained 1,256–3,014 unique KOs with median 2,121. The Pseudomonas_E guild contained 27 strains and averaged 2,658 KOs, while the Flavobacteriales guild contained 6 strains and averaged 1,372 KOs. [src: genotype_to_phenotype_enigma]

- Genus-level environmental profiling found that globally sampled Pseudomonas was 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic, whereas all ENIGMA Pseudomonas belonged to the environmental Pseudomonas_E fluorescens/protegens clade. Rhodanobacter was 55% aquatic, 10% contaminated, and 0% clinical in the analyzed profiles. The 14 ENIGMA genera occurred in 4,086–288,686 of 464,000 global 16S samples; Caulobacter occurred in 289K samples, Rhodanobacter in 228K, and Pseudomonas in 206K. [src: genotype_to_phenotype_enigma]

- Local Oak Ridge co-occurrence and global environmental data support a pH-driven niche partition. Across 587 100-Well-Survey communities, two anti-correlated genus clusters produced 47 significant pairs with |rho| > 0.2 and p < 0.01. Cluster A comprised Brevundimonas, Caulobacter, Sphingomonas, Variovorax, and Sphingobium; Cluster B comprised Rhodanobacter, Ralstonia, Dyella, Serratia, and Comamonas. Across 464K global 16S samples, Cluster A averaged pH 6.78 and 15.7°C, while Cluster B averaged pH 5.43 and 22.6°C: a difference of 1.35 pH units and 6.9°C. [src: genotype_to_phenotype_enigma]

- A strain-name collision caused 12 of 32 genus-level mismatches when ENIGMA strains were matched to the BERDL pangenome through short identifiers such as MT20. One collision matched Rhodanobacter glycinis to Streptococcus pneumoniae and introduced 1,751 spurious clinical genomes into environmental profiles. Using CORAL brick 522 GTDB-Tk assignments and checking genus consistency reduced verified linkages from 32 to 20 and eliminated all false matches. [src: genotype_to_phenotype_enigma]

- The initial 7-strain model used 4,305 prevalence-filtered KO features, 23 COG classes, condition class, concentration, phylogeny, and bulk genome features. It achieved AUC 0.633 for binary growth under leave-one-strain-out validation. Here, AUC means area under the receiver-operating-characteristic curve. Correlation-grouped SHAP (SHapley Additive exPlanations) attributed 25.3% of total importance to a 63-feature genome-scale axis and 45.9% to condition class; specific KO blocks such as membrane adaptation, tRNA modification, aromatic catabolism, and flagellar motility contributed approximately 2% each. [src: genotype_to_phenotype_enigma]

- GapMind achieved AUC 0.646, 78.8% accuracy, and 24.3% coverage on 118 testable pairs, with 96.5% recall and 79% precision. Matched-condition Carbon Source Phenotypes transfer achieved AUC 0.800 and 76.8% accuracy at 23% coverage, while internal five-fold Carbon Source Phenotypes validation achieved AUC 0.858. Approximately 76% of ENIGMA conditions lacked GapMind pathway coverage or Carbon Source Phenotypes training data; on these conditions, prediction fell to approximately AUC 0.63. [src: genotype_to_phenotype_enigma]

- Full-corpus LightGBM gradient-boosted decision-tree modeling used 46,389 pairs from 727 genomes, 106 genus-blocked holdouts, and 4,293 shared KOs. Overall binary-growth AUC was 0.620, but performance varied by condition class: amino acids AUC 0.775 across 7,765 pairs, nucleosides AUC 0.780 across 829 pairs, carbon sources AUC 0.695 across 8,965 pairs, other conditions AUC 0.654 across 24,590 pairs, antibiotics AUC 0.619 across 238 pairs, metals AUC 0.605 across 232 pairs, and nitrogen AUC 0.435 across 152 pairs. [src: genotype_to_phenotype_enigma]

- Adding KO × condition interaction features increased mean AUC from 0.620 to 0.653, an improvement of 0.032, with improvement in 80 of 106 held-out genera. Across 343 individually testable conditions, 95 achieved AUC > 0.75. The best individual conditions were tryptophan (0.933), phenylalanine (0.932), valine (0.927), mannose (0.904), and galactose (0.895); the worst were turanose (0.059) and adonitol (0.010). Full-corpus SHAP identified condition-specific predictors including K03762 (proP), K10440 (rbsC), K01857 (pcaB), K13633 (ftrA), and K01214 (treX). [src: genotype_to_phenotype_enigma]

- Continuous µmax, lag, and yield-related max_A were not predictable under genus-blocked holdout from KO presence/absence or bulk genomic features, producing negative R² in both the 46K-pair model and dedicated bulk-feature regression. Weak univariate correlations—n_unique_KOs with µmax at r = +0.42 and n_tRNA with µmax at r = +0.30—were phylogenetically confounded and provided zero cross-genus predictive power. The report interprets this as a biological limitation: gene content encodes whether an organism can use a substrate, whereas rate depends on enzyme kinetics, expression, regulatory context, and ribosome efficiency. [src: genotype_to_phenotype_enigma]

- Comparing 7 strains with 46K pairs showed a qualitative shift from genome-scale to condition-specific prediction. With 7 strains, the model learned a genome-size and condition-class pattern equivalent to “big genomes grow on amino acids”; with 46K pairs, it identified substrate-relevant transporters, catabolic enzymes, and regulators. The report therefore concludes that mechanistic gene-specific prediction requires hundreds of genomes per condition rather than a small number of anchor strains. [src: genotype_to_phenotype_enigma]

- Fitness Browser concordance was weak but positive: 18.7% of top SHAP KOs expanded into correlation-grouped gene blocks showed significant matched-condition fitness effects, compared with a 16.3% random baseline, giving 1.19× enrichment. Enrichment ranged from 1.72× for Cup4G11 to 0.83× for pseudo1_N1B4. The report interprets this as a distinction between gene presence across genera and gene essentiality within one strain, rather than evidence that the SHAP features are non-mechanistic. [src: genotype_to_phenotype_enigma]

- In the Web of Microbes analysis, multivariate GBDT failed at n = 6 strains with AUC = 0.500, whereas univariate per-metabolite point-biserial correlations identified 940 strong associations with |r| > 0.7 across all 62 variable metabolites. The associations included 454 production relationships and 486 consumption relationships, using a focused set of 156 Fitness Browser-cognate KOs. Examples included K01048 with taurine production, K05710 with thymine production, K02613 with lactate consumption, and K07334 with hypoxanthine consumption. Growth-predictive KOs and metabolite-production-associated KOs had Spearman rho = 0.043, indicating different feature sets and biological questions. [src: genotype_to_phenotype_enigma]

- Auditing 42,771 genus-blocked holdout predictions gave 65.1% overall accuracy, 7,844 false positives, and 7,101 false negatives. Filtering to confident predictions with |p − 0.5| > 0.25 identified 1,276 high-confidence errors concentrated in genus × condition-class cells including Methylobacterium on amino acids, Sphingomonas on other carbon sources, and Microbacterium on nucleosides. [src: genotype_to_phenotype_enigma]

- Active learning ranked 343 conditions using error rate × model uncertainty × field-relevance weight and proposed 50 next experiments. The top conditions included fumaric acid, melibionic acid, fumarate, itaconic acid, 2-hydroxypropanoic acid (lactic acid), hydroxy-glutaric acid γ-lactone, difumarate, L-glutamic acid, nitrate, and pyruvic acid. Prescottella, with 16% growth across tested conditions, and Microbacterium, with 23%, were selected as especially informative genera. The proposed experiments correspond to 7,844 current prediction failures, but formal retrospective comparison with random selection remains outstanding. [src: genotype_to_phenotype_enigma]

## Caveats

- Condition alignment was based on normalized names and produced 42 molecular matches; the report estimates that ChEBI-ID-based canonicalization could expand this to 60–80 matches. [src: genotype_to_phenotype_enigma]

- Only 35.7% of growth curves were fit-ok. Although the 55.1% no-growth fraction is interpreted as biological, approximately 9% of curves failed fitting for technical reasons including monotone violations, short duration, and edge-well effects. [src: genotype_to_phenotype_enigma]

- Genus-level biogeography used Microbial Atlas 16S data. Species-level biogeography was available for only 20 pangenome-linked strains with verified GTDB matches. [src: genotype_to_phenotype_enigma]

- Spearman co-occurrence measures correlation rather than causation. The report recommends SparCC analysis on the full 100WS ASV matrix to strengthen the niche-partition result. [src: genotype_to_phenotype_enigma]

- Uranium, nitrate, and metal concentrations are available in CORAL bricks 10/80, but sample-to-location name resolution is incomplete, preventing a completed local test of contamination levels for the acidic Cluster B strains. [src: genotype_to_phenotype_enigma]

- GC%, codon usage bias (CUB), and Morgan molecular fingerprints were not used: GC% was available for only 32 of 727 genomes, CUB required nucleotide sequences inaccessible from JupyterHub, and Morgan fingerprints required RDKit. CUB computation from GenBank files is proposed as the next test of continuous growth-rate prediction. [src: genotype_to_phenotype_enigma]

- The Fitness Browser concordance analysis produced 1.19× enrichment after correlation-group expansion, but full validation with KEGG-module expansion remains to be done. The report also notes that the n = 7 initial analysis did not test cross-genus generalization, per-condition prediction quality, or condition-specific features. [src: genotype_to_phenotype_enigma]

- The active-learning framework is actionable but H6 is only partially supported. A formal retrospective subsampling test comparing AL-ranked additions with random selection, followed by wet-lab execution of the 50-condition proposal, remains necessary. [src: genotype_to_phenotype_enigma]

## Slots Into

- [[concepts/condition-specific-fitness]] — binary growth is predictable for some condition classes and individual substrates, while metals, antibiotics, and nitrogen remain weakly predictable; the result also separates condition-specific growth capability from continuous kinetics. [src: genotype_to_phenotype_enigma]
- [[concepts/gene-function-acquisition-depth]] — the 7-strain to 46K-pair comparison shows that larger training corpora shift predictors from genome-scale proxies to substrate-specific catabolic genes. [src: genotype_to_phenotype_enigma]
- [[concepts/gene-essentiality]] — weak 1.19× Fitness Browser concordance demonstrates that cross-genus gene presence and within-strain gene essentiality answer different questions. [src: genotype_to_phenotype_enigma]
- [[concepts/multi-omics-integration]] — growth curves, KO annotations, RB-TnSeq fitness, exometabolomics, pangenomes, and environmental metadata are integrated, with method choice matched to sample size and phenotype resolution. [src: genotype_to_phenotype_enigma]
- [[concepts/environment-embedding-geography]] — global 16S data connect Oak Ridge co-occurrence to a pH difference of 1.35 units and a temperature difference of 6.9°C between genus clusters. [src: genotype_to_phenotype_enigma]
- [[concepts/ecotype-environment-gene-content]] — eight functional metabolic guilds, ENIGMA environmental outlier status, and the pH-partitioned Cluster A/Cluster B ecology link gene content to environmental distribution. [src: genotype_to_phenotype_enigma]
- [[concepts/cross-tenant-data-bridging]] — the study establishes 486 condition-matched Fitness Browser anchors and documents a strain-name collision that generated 1,751 spurious clinical genomes. [src: genotype_to_phenotype_enigma]
- [[concepts/subsurface-bacillota-specialization]] — the Oak Ridge-focused active-learning proposal prioritizes acidic, nitrogen-related, and organic-acid conditions relevant to contaminated subsurface physiology. [src: genotype_to_phenotype_enigma]
