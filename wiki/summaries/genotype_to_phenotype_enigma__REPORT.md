---
type: "Summary"
description: "Summary of the project Genotype x Condition to Phenotype Prediction from ENIGMA Growth Curves."
doc_type: "short"
full_text: "sources/genotype_to_phenotype_enigma__REPORT.md"
---
# Genotype x Condition to Phenotype Prediction from ENIGMA Growth Curves

This report asks whether bacterial growth phenotype, from binary growth to continuous kinetics, can be predicted interpretably from genome content and growth condition. It also asks whether such predictions can guide experimental design at the ENIGMA Oak Ridge contaminated subsurface site. [src: genotype_to_phenotype_enigma] It builds a calibrated model from 46,389 (genome × condition) training pairs drawn from five datasets. [src: genotype_to_phenotype_enigma] The main answer is that binary growth is predictable for some condition classes but not others, and continuous kinetics are not predictable. [src: genotype_to_phenotype_enigma] A full-corpus genus-blocked holdout audit gave 65.1% overall accuracy. [src: genotype_to_phenotype_enigma]

## Key Findings

### Which growth phenotypes are predictable

Binary growth from KO (KEGG ortholog) presence/absence is predictable on nucleosides (0.780) and moderately predictable on carbon sources (0.695). [src: genotype_to_phenotype_enigma] The report also states that amino acids reach AUC (area under curve) 0.775, with tryptophan at 0.933, and that metals, antibiotics and nitrogen are not predictable from KO content alone. [src: genotype_to_phenotype_enigma] Across the report, 95 of 343 tested conditions achieve AUC > 0.75. [src: genotype_to_phenotype_enigma] The report reads the failure to predict continuous kinetics as a fundamental biological limitation: gene presence encodes capability, not kinetic rate. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content]] and [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content]].

### Interpretability and training-set size

SHAP (Shapley additive explanations) features are mechanistically coherent. A ribose transporter predicts ribose growth, and protocatechuate cycloisomerase predicts aromatic catabolism. [src: genotype_to_phenotype_enigma] Concordance with Fitness Browser is weak (1.19× enrichment). The report explains this by saying that gene presence across genera and gene essentiality within one strain are different biological questions. [src: genotype_to_phenotype_enigma] The report states that moving from genome-scale to gene-specific prediction requires 46K training pairs. With n=7 strains the model learns genome-size associations with amino-acid growth, and with n=46K pairs it learns condition-specific catabolic genes. [src: genotype_to_phenotype_enigma] See [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features]] and [[concepts/concordance-between-cross-genus-predictive-genes-and-within-strain-gene-fitness]].

### Exometabolomics

Exometabolomic prediction for Web of Microbes (WoM; 6 strains, 105 metabolites) fails under multivariate GBDT (gradient boosted decision tree). [src: genotype_to_phenotype_enigma] The report says the same data succeed under univariate per-metabolite correlation. [src: genotype_to_phenotype_enigma] The features come from a set of 156 KOs with significant rich-media fitness in Pseudomonas Fitness Browser anchors that vary across the 6 WoM strains. [src: genotype_to_phenotype_enigma] See [[concepts/gene-metabolite-association-discovery-in-small-exometabolomic-datasets]].

### Collection and ecology

The ENIGMA growth curves align with Fitness Browser RB-TnSeq (random barcode transposon sequencing) data through 486 anchor (strain × condition) pairs, covering 7 strains × 72 conditions. [src: genotype_to_phenotype_enigma] Of these pairs, 275 (56.6%) show measurable growth. [src: genotype_to_phenotype_enigma] In the full corpus, 15,227 of 27,632 wells (55.1%) show no detectable growth, which the report treats as biological signal and not measurement failure. [src: genotype_to_phenotype_enigma]

Worldwide, the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9°C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster. [src: genotype_to_phenotype_enigma] The report reads this as a global pH-driven niche partition that mirrors the Oak Ridge nitric acid gradient. [src: genotype_to_phenotype_enigma] It also hypothesizes that the two clusters should differ in pH-dependent growth. [src: genotype_to_phenotype_enigma] See [[concepts/ph-driven-niche-partitioning-and-genus-co-occurrence-in-contaminated-subsurface-communities]].

The report concludes that ENIGMA field isolates occupy niches underrepresented in the NCBI genome collection. [src: genotype_to_phenotype_enigma] See [[concepts/representativeness-of-reference-genome-collections-for-environmental-field-isolates]].

### Error audit and active learning

The full-corpus genus-blocked holdout audit of 42,771 predictions gave 65.1% accuracy. [src: genotype_to_phenotype_enigma] It had 7,844 false positives. [src: genotype_to_phenotype_enigma] Filtering to confident predictions isolated 1,276 high-confidence errors. [src: genotype_to_phenotype_enigma] The model performs worst on organic-acid and nitrogen-cycle classes, with AUC 0.654 for "other" carbon metabolism and 0.435 for nitrogen. [src: genotype_to_phenotype_enigma] Active learning identifies 50 conditions for next Oak Ridge experiments. They prioritize organic acids (fumaric, melibionic, itaconic), nitrate and low-pH-relevant substrates. [src: genotype_to_phenotype_enigma] Prescottella and Microbacterium are proposed as the most informative genera to test. [src: genotype_to_phenotype_enigma] See [[concepts/active-learning-for-selecting-growth-experiments-from-model-errors]].

## Executive Summary; Act I — Know the Collection

This part of the report gives its headline answers and then describes the ENIGMA collection the models are built on. The report asks whether bacterial growth phenotype, from binary growth through continuous kinetics, can be predicted interpretably from genome content and growth condition. It frames the question for experimental design at the ENIGMA Oak Ridge contaminated subsurface site. [src: genotype_to_phenotype_enigma] It builds a calibrated model from 46,389 (genome × condition) training pairs drawn from five datasets: ENIGMA growth curves, ENIGMA Genome Depot, Fitness Browser (FB), Web of Microbes (WoM) and Carbon Source Phenotypes. The work spans 11 notebooks and 50 figures. [src: genotype_to_phenotype_enigma]

### Headline results

Binary growth is predictable from KEGG ortholog (KO) presence/absence for some condition classes and not others. [src: genotype_to_phenotype_enigma] The areas under the curve (AUC) are 0.775 on amino acids, with tryptophan at 0.933, and 0.780 on nucleosides. [src: genotype_to_phenotype_enigma] Carbon sources are moderately predictable at 0.695. [src: genotype_to_phenotype_enigma] Metals, antibiotics and nitrogen are not predictable from KO content alone. [src: genotype_to_phenotype_enigma] In this analysis, 95 of 343 tested conditions reach AUC > 0.75. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content]].

Continuous growth parameters (µmax, lag, yield) are not predictable from KO content or bulk genomic features under cross-genus holdout. [src: genotype_to_phenotype_enigma] The report reads this as a fundamental biological limitation, because gene presence encodes capability rather than kinetic rate. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content]].

Shapley additive explanations (SHAP) features are mechanistically coherent. A ribose transporter predicts ribose growth, and protocatechuate cycloisomerase predicts aromatic catabolism. [src: genotype_to_phenotype_enigma] Concordance with FB is weak, at 1.19× enrichment. The report attributes this to gene presence across genera and gene essentiality within one strain being different biological questions. [src: genotype_to_phenotype_enigma] The report also states that moving from genome-scale to gene-specific prediction takes 46K training pairs. With n=7 strains the model learns genome-size associations with amino-acid growth, and with n=46K pairs it learns condition-specific catabolic genes. [src: genotype_to_phenotype_enigma] See [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features]] and [[concepts/concordance-between-cross-genus-predictive-genes-and-within-strain-gene-fitness]].

Exometabolomic prediction for WoM (6 strains, 105 metabolites) fails under multivariate gradient boosted decision trees (GBDT). [src: genotype_to_phenotype_enigma] Univariate per-metabolite correlation succeeds, recovering 940 mechanistic gene-metabolite associations (454 production, 486 consumption) across all 62 variable metabolites. [src: genotype_to_phenotype_enigma] These come from an FB-cognate feature set of 156 KOs. These are KOs with significant rich-media fitness in Pseudomonas FB anchors that also vary across the 6 WoM strains. [src: genotype_to_phenotype_enigma] See [[concepts/gene-metabolite-association-discovery-in-small-exometabolomic-datasets]].

The report states that a global pH-driven niche partition across 464K samples explains local Oak Ridge co-occurrence. [src: genotype_to_phenotype_enigma] Worldwide, the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9°C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster. [src: genotype_to_phenotype_enigma] See [[concepts/ph-driven-niche-partitioning-and-genus-co-occurrence-in-contaminated-subsurface-communities]].

Active learning picks 50 conditions for the next Oak Ridge experiments. They favor organic acids (fumaric, melibionic, itaconic), nitrate and low-pH-relevant substrates, where the model is least confident and field relevance is highest. [src: genotype_to_phenotype_enigma] See [[concepts/active-learning-for-selecting-growth-experiments-from-model-errors]].

### Act I: the growth-curve collection and its link to the Fitness Browser

The ENIGMA corpus has 27,632 curves across 123 strains and 195 molecules. It links to Fitness Browser random barcode transposon sequencing (RB-TnSeq) data through 486 (strain × condition) anchor pairs. These cover 7 strains × 72 conditions where growth curves, gene fitness and genome annotations all coexist. [src: genotype_to_phenotype_enigma] The media names RCH2_defined_noCarbon, LB, R2A and M9 match exactly between ENIGMA and FB. [src: genotype_to_phenotype_enigma] A further 42 molecules align by normalized compound name. [src: genotype_to_phenotype_enigma] Of the 486 anchor pairs, 275 (56.6%) show measurable growth, which gives balanced positive and negative labels for binary prediction. [src: genotype_to_phenotype_enigma]

Five conditions (cytidine, glycine, inosine, thymidine, uridine) occur in all four datasets: ENIGMA, FB, the carbon source phenotype corpus and WoM. Thirty conditions occur in three. [src: genotype_to_phenotype_enigma] An additional 795-genome carbon source phenotype corpus (`globalusers_carbon_source_phenotypes`) is available for pretraining. It has 379 binary phenotypes and pre-computed KofamScan KO and BacFormer embeddings (Dileep et al., preprint in preparation). [src: genotype_to_phenotype_enigma] The ENIGMA full coverage matrix spans 13,632 (strain × condition) pairs across all 123 strains × 194 conditions. [src: genotype_to_phenotype_enigma]

### Growth-curve behavior

More than half of ENIGMA wells show no growth. Of 27,632 wells across 303 plates, 15,227 (55.1%) show no detectable growth. The report reads this as a biological signal of substrate incompatibility or stress lethality, not a measurement failure. [src: genotype_to_phenotype_enigma] It treats the no-growth fraction as a prediction target, namely conditions where the genome predicts that growth should not occur. [src: genotype_to_phenotype_enigma]

Among the 9,861 fit-ok curves (35.7%), modified Gompertz fitting gives a median R² of 0.98. [src: genotype_to_phenotype_enigma] The median mumax is 0.028 h^-1, a doubling time of about 24.5 h. [src: genotype_to_phenotype_enigma] The median lag is 11.4 h. [src: genotype_to_phenotype_enigma] The median asymptotic optical density (OD) increase (A) is 0.315. [src: genotype_to_phenotype_enigma] Diauxy looks common. 40% of fit-ok curves show ≥2 growth phases in their smoothed derivative. The report suggests sequential substrate utilization is widespread among Oak Ridge isolates. [src: genotype_to_phenotype_enigma]

Growth breadth differs by genus. Pseudomonas anchor strains grow in 43-61% of conditions and are described as metabolic generalists. [src: genotype_to_phenotype_enigma] Pedobacter (23.5%) and Acidovorax (22.4%) grow far less, which the report calls consistent with more specialized metabolic repertoires. [src: genotype_to_phenotype_enigma]

### Genomic guilds

Hierarchical clustering of KO presence/absence (Jaccard distance, 7,167 unique KOs across 123 strains) identifies 8 metabolic guilds spanning 20 taxonomic orders. [src: genotype_to_phenotype_enigma] The guilds align with taxonomy but are not identical to it, because functional gene content, not phylogeny, defines them. [src: genotype_to_phenotype_enigma] Genome sizes range from 2.6 to 11.4 Mb and correlate strongly with KO diversity. Strains carry 1,256-3,014 unique KOs, with a median of 2,121. [src: genotype_to_phenotype_enigma]

The Pseudomonas_E guild has 27 strains and an average of 2,658 KOs. It contains 5 of the 7 FB-anchor strains, so it is the best-sampled guild for modeling. [src: genotype_to_phenotype_enigma] The Flavobacteriales guild has 6 strains and an average of 1,372 KOs. It has the fewest functional genes and is the hardest out-of-distribution prediction target. [src: genotype_to_phenotype_enigma] Clusters of orthologous groups (COG) class profiles differ by guild, most in categories L (replication/repair/recombination) and M (cell wall/membrane biogenesis). [src: genotype_to_phenotype_enigma]

### Representativeness and field distribution

Environmental profiling across all GTDB genomes shows that Pseudomonas is 37.8% clinical globally, driven by P. aeruginosa. It is 12.9% soil/plant and 9.4% aquatic. [src: genotype_to_phenotype_enigma] All ENIGMA Pseudomonas belong to Pseudomonas_E, the fluorescens/protegens clade, which is environmental rather than clinical. [src: genotype_to_phenotype_enigma] Rhodanobacter is described as purely aquatic/contaminated, with 55% aquatic, 10% contaminated and 0% clinical assignments. [src: genotype_to_phenotype_enigma] The report concludes that ENIGMA subsurface isolates occupy niches underrepresented in the NCBI genome collection. [src: genotype_to_phenotype_enigma] It cautions that transfer learning from clinical phenotype databases may therefore be biased. [src: genotype_to_phenotype_enigma] See [[concepts/representativeness-of-reference-genome-collections-for-environmental-field-isolates]].

All 14 ENIGMA genera are globally ubiquitous. They are detected in 4,086-288,686 of 464,000 samples in the Microbial Atlas 16S database. [src: genotype_to_phenotype_enigma] Caulobacter is the most widespread (289K samples), followed by Rhodanobacter (228K) and Pseudomonas (206K). [src: genotype_to_phenotype_enigma]

## Act I — Know the Collection: Act II — Predict and Explain

This part of the report characterizes the ENIGMA collection: where its genera occur, how they co-occur and sort by pH, how strains were linked to the pangenome, and how preliminary models on a small strain set performed. The co-occurrence results come from Spearman analysis of 587 communities plus a global 16S survey. [src: genotype_to_phenotype_enigma] The preliminary modeling used 7 strains, or 6 in the metabolite analysis. [src: genotype_to_phenotype_enigma]

### Genus occurrence and pH-driven co-occurrence

The report describes the ENIGMA genera as ecologically significant rather than rare specialists. [src: genotype_to_phenotype_enigma] In the Microbial Atlas context, Caulobacter is the most widespread genus with 289K samples. Rhodanobacter follows with 228K samples [src: genotype_to_phenotype_enigma] and Pseudomonas with 206K. [src: genotype_to_phenotype_enigma]

Spearman analysis of 587 Oak Ridge 100-Well-Survey communities finds two anti-correlated genus clusters with 47 significant pairs (|rho| > 0.2, p < 0.01). [src: genotype_to_phenotype_enigma] Cluster A is Brevundimonas, Caulobacter, Sphingomonas, Variovorax and Sphingobium, with strongest pair rho = +0.56. [src: genotype_to_phenotype_enigma] Cluster B is Rhodanobacter, Ralstonia, Dyella, Serratia and Comamonas, with rho = +0.40. [src: genotype_to_phenotype_enigma] The clusters are negatively correlated with each other, for example Brevundimonas–Rhodanobacter rho = -0.34. [src: genotype_to_phenotype_enigma]

Across 464K global 16S samples, Cluster B environments average pH 5.4, which is 1.35 units more acidic than Cluster A's 6.8. [src: genotype_to_phenotype_enigma] They are also 6.9 degrees C warmer. [src: genotype_to_phenotype_enigma] The report reads this as a global pH-driven niche partition, not a site-specific pattern. It says the partition mirrors nitric acid leachate lowering pH in Oak Ridge plume wells. [src: genotype_to_phenotype_enigma] It characterizes Cluster B as acid-tolerant generalists enriched in contamination sites, peatlands and acidic soils. [src: genotype_to_phenotype_enigma] It says Cluster A prefers neutral, cooler conditions typical of uncontaminated groundwater. [src: genotype_to_phenotype_enigma] The report hypothesizes that Cluster B strains should have different pH-dependent growth profiles than Cluster A strains. It also hypothesizes that the genomic features distinguishing the clusters should predict pH tolerance. [src: genotype_to_phenotype_enigma] See [[concepts/ph-driven-niche-partitioning-and-genus-co-occurrence-in-contaminated-subsurface-communities]].

### Strain-to-pangenome linking pitfall

Matching ENIGMA strains to the KBase Data Lakehouse pangenome through `ncbi_strain_identifiers` caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma] For example, the short name MT20 (ENIGMA: Rhodanobacter glycinis) matched unrelated Streptococcus pneumoniae. Name collisions injected 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma] The fix used CORAL brick 522 (GTDB-Tk assignments) for authoritative taxonomy and checked genus consistency. This reduced verified linkages from 32 to 20 and eliminated all false matches. [src: genotype_to_phenotype_enigma] The report documents the pitfall in docs/pitfalls.md and says it affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma] See [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]].

### Feature design and the preliminary ENIGMA-only model

The report states that all planned modeling is complete. The full-corpus run used genus-blocked holdout on 46,389 pairs and 106 genera, with prediction quality evaluated for 343 conditions. [src: genotype_to_phenotype_enigma] The initial modeling table had 486 anchor pairs (7 strains x 72 conditions). Its features sat in four levels: L0 Phylogeny (28), L1 Bulk scalars (8), L2 Specific features (4,305 prevalence-filtered KOs + 23 COG classes) and L3 Condition class + concentration (7). [src: genotype_to_phenotype_enigma] The prevalence filter removed 456 core KOs (p > 0.95) for lacking discriminative power [src: genotype_to_phenotype_enigma] and 2,406 rare KOs (p < 0.05) as too sparse. [src: genotype_to_phenotype_enigma] It kept 4,305 informative KOs as named KEGG orthologs for SHAP interpretability. [src: genotype_to_phenotype_enigma]

Nested LightGBM GBDT models with leave-one-strain-out cross-validation on the 486 pairs reached AUC 0.633 for binary growth with the full feature set. [src: genotype_to_phenotype_enigma] SHAP analysis with correlation groups (|r| > 0.8 connected components) found a 63-feature genome-scale axis accounting for 25.3% of total SHAP. [src: genotype_to_phenotype_enigma] Condition class accounted for 45.9%. [src: genotype_to_phenotype_enigma] Specific KO blocks (membrane adaptation, tRNA modification, aromatic catabolism, flagellar motility) contributed ~2% each and are described as biologically coherent. [src: genotype_to_phenotype_enigma] Continuous targets (mumax, lag, max_A) showed negative R^2 and were not predictable cross-strain with n=7. [src: genotype_to_phenotype_enigma]

The report limits these results. The analysis used leave-one-strain-out on 7 strains: 4 Pseudomonas_E and 1 each of Cupriavidus, Acidovorax and Pedobacter. [src: genotype_to_phenotype_enigma] It did not test cross-genus generalization, analyze per-condition prediction quality or use condition-specific features. [src: genotype_to_phenotype_enigma] The report says the model effectively learns "big genomes grow on amino acids", which is biologically real but not the condition-specific prediction needed for practical use. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content]] and [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features]].

### Baselines and the coverage gap

The preliminary comparison for binary growth lists four models:

- ENIGMA-only GBDT with generic KO features and n=7: AUC 0.633, coverage 100%. [src: genotype_to_phenotype_enigma]
- GapMind baseline (pathway completeness for amino acids/carbon): AUC 0.646, accuracy 78.8%, coverage 24.3%. [src: genotype_to_phenotype_enigma]
- CSP transfer (CSP-trained KOs on matched conditions): AUC 0.800, accuracy 76.8%, coverage 23%. [src: genotype_to_phenotype_enigma]
- CSP internal 5-fold: AUC 0.858, presented as an achievable ceiling with sufficient data. [src: genotype_to_phenotype_enigma]

GapMind reaches 96.5% recall and 79% precision on 118 testable pairs. It almost never misses a grower but sometimes predicts growth when the pathway is present but unused. [src: genotype_to_phenotype_enigma] About 76% of ENIGMA conditions (metals, antibiotics, nitrogen, stress) have neither GapMind pathway coverage nor CSP training data. [src: genotype_to_phenotype_enigma] On these conditions prediction falls to AUC ~0.63, no better than generic KO features. [src: genotype_to_phenotype_enigma] See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

### Metabolite associations at n=6

In the ENIGMA-linked Web of Microbes metabolite analysis, multivariate GBDT fails at n=6 (AUC=0.500). [src: genotype_to_phenotype_enigma] Univariate per-metabolite point-biserial correlation instead finds 940 strong KO-presence/metabolite-production associations (|r| > 0.7) across all 62 variable metabolites. [src: genotype_to_phenotype_enigma] The feature set is 156 FB-cognate KOs. These are genes with significant rich-media fitness effects in Pseudomonas Fitness Browser anchor organisms, filtered to those variable across the 6 WoM strains. [src: genotype_to_phenotype_enigma] Of the associations, 454 are production, where KO presence accompanies metabolite production. [src: genotype_to_phenotype_enigma] Examples are K01048 PAPS synthase with taurine [src: genotype_to_phenotype_enigma] and K05710 thymidine phosphorylase with thymine. [src: genotype_to_phenotype_enigma] The other 486 are consumption, where KO presence accompanies consumption or degradation of the metabolite. [src: genotype_to_phenotype_enigma] Examples are K02613 lactate permease with lactate [src: genotype_to_phenotype_enigma] and K07334 xanthine oxidase with hypoxanthine. [src: genotype_to_phenotype_enigma]

The report concludes that multivariate GBDT identifies condition-specific features for cross-genus growth prediction at n=46K pairs. For within-genus metabolite prediction at n=6 strains, univariate correlation recovers signal that multivariate models miss. [src: genotype_to_phenotype_enigma] It also reports that growth-predictive cross-genus KOs and metabolite-production-associated within-genus KOs are different feature sets (Spearman rho=0.043). It treats them as answering different questions, "can it grow?" versus "what does it produce?". [src: genotype_to_phenotype_enigma] See [[concepts/gene-metabolite-association-discovery-in-small-exometabolomic-datasets]].

## Act I — Know the Collection: Act II — Predict and Explain (2)

This part of the report shows that gene content predicts binary growth across genera, and does so best for amino acids and nucleosides. It does not predict continuous growth parameters, and the model's top genes match within-strain fitness data only weakly. The report's overall conclusion is that gene content explains growth and metabolite production when the method fits the sample size and biological resolution. [src: genotype_to_phenotype_enigma]

### Binary growth prediction on the full corpus

The full-corpus model predicts binary growth modestly overall, and its accuracy varies a lot by condition class. It trained on 46,389 pairs (13,632 ENIGMA and 32,757 carbon source phenotypes, CSP), 727 genomes and 4,293 shared KEGG orthologs (KOs). Genus-blocked holdout across 106 genera gave an overall AUC (area under curve) of 0.620. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content]].

| Condition class | AUC | Pairs | Report's reading |
|---|---|---|---|
| Amino acids | 0.775 | 7,765 | genuinely predictable from KO content [src: genotype_to_phenotype_enigma] |
| Nucleosides | 0.780 | 829 | well predicted [src: genotype_to_phenotype_enigma] |
| Carbon sources | 0.695 | 8,965 | moderately predictable [src: genotype_to_phenotype_enigma] |
| Other | 0.654 | 24,590 | mixed [src: genotype_to_phenotype_enigma] |
| Antibiotics | 0.619 | 238 | marginal [src: genotype_to_phenotype_enigma] |
| Metals | 0.605 | 232 | trivially "predicted" because of a 98% growth rate [src: genotype_to_phenotype_enigma] |
| Nitrogen | 0.435 | 152 | worse than random [src: genotype_to_phenotype_enigma] |

Adding KEGG-pathway-based KO-by-condition interaction features raised mean AUC from 0.620 to 0.653 (+0.032). [src: genotype_to_phenotype_enigma] Of the 106 held-out genera, 80 improved. [src: genotype_to_phenotype_enigma] The largest gains were for Microbacterium (+0.088) and Sphingomonas (+0.074). [src: genotype_to_phenotype_enigma]

Per-condition analysis across 343 testable conditions found 95 with AUC > 0.75, which the report calls genuinely predictable from KO content. [src: genotype_to_phenotype_enigma] The best-predicted substrates were tryptophan (AUC 0.933), phenylalanine (0.932), valine (0.927), mannose (0.904) and galactose (0.895). [src: genotype_to_phenotype_enigma] The worst were turanose (0.059) and adonitol (0.010), which the report describes as complex sugars with rare catabolic pathways. [src: genotype_to_phenotype_enigma]

### Continuous growth parameters are not predictable

Growth rate (mumax), lag time and yield (max_A) all gave negative R² under genus-blocked holdout. This held for the full KO model (NB07, 46K pairs) and for a bulk-feature regression on genome size, rRNA/tRNA copies, GC%, coding density, KO count and operons. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content]].

Weak univariate correlations exist: n_unique_KOs vs mumax r=+0.42, and n_tRNA vs mumax r=+0.30. [src: genotype_to_phenotype_enigma] The report attributes both to phylogenetic confounding. It says large-genome Pseudomonas grow fast and small-genome Pedobacter grow slowly. [src: genotype_to_phenotype_enigma] Under cross-genus holdout these correlations gave zero predictive power. [src: genotype_to_phenotype_enigma]

The report calls this a fundamental biological limitation, not a data problem. KO presence or absence says whether an organism can use a substrate, not how fast. [src: genotype_to_phenotype_enigma] In its account, growth rate depends on enzyme kinetics (Kcat, Km), expression levels and ribosome efficiency captured by codon usage bias (CUB). [src: genotype_to_phenotype_enigma] Predicting continuous parameters would need expression data or CUB computed from GenBank files. Those files are on the CGCMS server but not reachable from JupyterHub. [src: genotype_to_phenotype_enigma]

### What the model uses: SHAP features

With only 7 strains (NB06), SHAP (Shapley additive explanations) importance was dominated by condition class (45.9%) and genome-scale features (25.3%). With the full 46K-pair corpus, condition-specific catabolic genes emerge. [src: genotype_to_phenotype_enigma] See [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features]]. The full-corpus SHAP features are:

- K03762 (proP), a proline/betaine transporter [src: genotype_to_phenotype_enigma]
- K10440 (rbsC), a ribose transporter [src: genotype_to_phenotype_enigma]
- K01857 (pcaB), a protocatechuate cycloisomerase for aromatic catabolism [src: genotype_to_phenotype_enigma]
- K13633 (ftrA), an AraC-family carbon catabolism regulator [src: genotype_to_phenotype_enigma]
- K01214 (treX), an isoamylase for complex carbohydrates [src: genotype_to_phenotype_enigma]

### Concordance with Fitness Browser

The model's top genes match within-strain fitness data only weakly. Condition-matched Fitness Browser (FB) concordance is the fraction of top SHAP KOs with significant fitness effects (|t|>4) in matched experiments. The KOs were expanded to correlated gene blocks at |r|>0.8, giving 57 KOs → 335 FB loci. [src: genotype_to_phenotype_enigma] Concordance was 18.7% against a 16.3% random baseline, a 1.19x enrichment. [src: genotype_to_phenotype_enigma] The report reads this as a weak positive: the features are barely more fitness-significant than random genes under matched conditions. [src: genotype_to_phenotype_enigma] Per-strain enrichment ranged from 1.72x (Cup4G11) to 0.83x (pseudo1_N1B4, no enrichment). [src: genotype_to_phenotype_enigma] See [[concepts/concordance-between-cross-genus-predictive-genes-and-within-strain-gene-fitness]].

The report argues that growth prediction (AUC 0.78 for amino acids) works through combinations of prevalence-variable KOs acting as genus-level proxies. It does not work through individually mechanistically causal genes. [src: genotype_to_phenotype_enigma] It still holds that K10440 predicting ribose growth is a real gene-function relationship, so the model does use condition-specific gene-level features. [src: genotype_to_phenotype_enigma]

The report gives three reasons weak concordance does not mean the features are non-mechanistic:
- Gene presence across genera and gene essentiality within one strain are different biological questions. [src: genotype_to_phenotype_enigma]
- A gene can matter for cross-genus prediction yet show no fitness defect in one strain. That strain may have redundant pathways, or the lab condition may differ from the growth assay. [src: genotype_to_phenotype_enigma]
- SHAP spreads credit across correlated features. The causal gene may be a correlated neighbor of the highlighted one, which dilutes the signal. [src: genotype_to_phenotype_enigma]

## Act III — Diagnose and Propose; Modeling Methodology

This part of the report audits the full-corpus growth model's errors, uses them to rank new experiments for Oak Ridge, and documents the data and features behind the growth model. The audit rests on a genus-blocked holdout. The experiment ranking is a proposal, and its retrospective validation is still pending. [src: genotype_to_phenotype_enigma]

### Error audit of the full-corpus growth model

The genus-blocked holdout of 42,771 per-pair predictions reached an overall accuracy of 65.1%. [src: genotype_to_phenotype_enigma] It made 7,844 false positives, where the model predicted growth but the organism did not grow. [src: genotype_to_phenotype_enigma] It made 7,101 false negatives, where the model predicted no growth but the organism grew. [src: genotype_to_phenotype_enigma] Filtering to predictions with |p − 0.5| > 0.25 isolated 1,276 high-confidence errors. The report says these are not borderline calls. [src: genotype_to_phenotype_enigma]

The confident errors cluster in particular genus × condition-class cells. Methylobacterium on amino acids [src: genotype_to_phenotype_enigma], Sphingomonas on other carbon sources [src: genotype_to_phenotype_enigma] and Microbacterium on nucleosides [src: genotype_to_phenotype_enigma] all show elevated confident-error rates. The report reads these errors as a possible missing gene-family feature, a regulatory mismatch, or a genuine biological oddity. It does not establish a single cause. [src: genotype_to_phenotype_enigma]

### Active-learning proposal

The candidate ranking pairs high-confidence errors with uncertainty-rich regions. [src: genotype_to_phenotype_enigma] The outputs are full-corpus predictions, active-learning candidates and proposed experiments. [src: genotype_to_phenotype_enigma] See [[concepts/active-learning-for-selecting-growth-experiments-from-model-errors]].

The 343 testable conditions are ranked by error rate × model uncertainty × field relevance weight. [src: genotype_to_phenotype_enigma] Field relevance doubles the weight for conditions matching Oak Ridge geochemistry. These include nitrogen sources such as nitrate, organic acids associated with necromass decomposition, low-pH-compatible substrates and aromatic compounds. [src: genotype_to_phenotype_enigma] The top 10 conditions are fumaric acid, melibionic acid, fumarate, itaconic acid, 2-hydroxypropanoic acid (lactic acid), hydroxy-glutaric acid γ-lactone, difumarate, L-glutamic acid, nitrate and pyruvic acid. [src: genotype_to_phenotype_enigma]

These conditions are mostly organic acids and nitrogen-cycle compounds. This is the class where the full-corpus model performs worst, with AUC (area under curve) 0.654 for "other" carbon metabolism and 0.435 for nitrogen. [src: genotype_to_phenotype_enigma] The report describes Oak Ridge contamination chemistry as nitric-acid-driven pH decline and organic acid accumulation in plume sediments. [src: genotype_to_phenotype_enigma]

For genus selection, Prescottella (16% growth rate across tested conditions) [src: genotype_to_phenotype_enigma] and Microbacterium (23%) [src: genotype_to_phenotype_enigma] are the most informative test subjects. Their predictions are among the least reliable in the current model. Combined with the condition ranking, this gives a 50-experiment proposal for ENIGMA's next growth screens. [src: genotype_to_phenotype_enigma]

The report's retrospective validation (H6) states that the 50 experiments correspond to 7,844 prediction failures in the current corpus. [src: genotype_to_phenotype_enigma] It argues that resolving even a fraction of them would move overall accuracy from 65.1% toward the per-class ceiling of ~78% seen on amino acids and nucleosides. [src: genotype_to_phenotype_enigma] This is an argument, not a test. A formal retrospective subsampling comparison of accuracy gain per experiment, active-learning-ranked versus random selection, is still the next validation step. [src: genotype_to_phenotype_enigma]

### Training data

The ENIGMA growth curves cover 123 strains × 194 conditions = 13,632 (strain × condition) pairs, taken from `enigma_coral` growth bricks. [src: genotype_to_phenotype_enigma] Growth phenotypes come from modified Gompertz fits. Binary growth means any optical density (OD) increase above 0.05. Mumax, lag and max_A are kept for fit-ok curves. [src: genotype_to_phenotype_enigma]

The carbon source phenotypes (CSP) set adds 795 genomes × 379 conditions = 53,301 pairs with literature-curated binary growth labels. It comes from `globalusers_carbon_source_phenotypes` (Dileep et al., preprint). [src: genotype_to_phenotype_enigma] The combined corpus has 46,389 pairs across 727 genomes and 363 conditions, with 4,293 shared KEGG orthologs (KOs) as features. [src: genotype_to_phenotype_enigma]

### Feature design

Per-genome features are derived from ENIGMA Genome Depot (`enigma_genome_depot_enigma`). [src: genotype_to_phenotype_enigma] The 4,293 KO presence/absence features come from genome depot protein-to-KO annotations. [src: genotype_to_phenotype_enigma] Prevalence filtering across the 727-genome corpus removes 456 core KOs present in >95% of genomes, which have no discriminative power. [src: genotype_to_phenotype_enigma] It also removes 2,406 rare KOs present in <5% of genomes, which are too sparse for statistical learning. [src: genotype_to_phenotype_enigma] Each retained feature is a named KO that keeps full interpretability. One example is K10440, the ribose transporter rbsC. [src: genotype_to_phenotype_enigma]

The report chose KOs for several reasons:
- Each KO ID represents a specific enzymatic reaction or transport function with a defined metabolic role. [src: genotype_to_phenotype_enigma]
- KOs give condition-specific mechanistic information, unlike genome-scale scalars.
- KOs are named gene functions that can be interpreted through KEGG maps and checked against independent fitness data, unlike PCA (principal component analysis) or embeddings. [src: genotype_to_phenotype_enigma]

Condition encoding has 7 features: one-hot condition type (amino acid, carbon source, metal, antibiotic, nitrogen, nucleoside, other) plus log10(concentration in mM). [src: genotype_to_phenotype_enigma] Three KEGG pathway interaction features count the genome's KOs that fall in the pathway relevant to the tested condition. Pathways are mapped by keyword matching to KEGG pathway descriptions. [src: genotype_to_phenotype_enigma] The three features are n_relevant_KOs, frac_relevant and has_any_relevant. [src: genotype_to_phenotype_enigma]

### Features planned but not used

GC%, codon usage bias and Morgan molecular fingerprints were planned but not computed. [src: genotype_to_phenotype_enigma] GC% was available for only 32/727 genomes. [src: genotype_to_phenotype_enigma] Codon usage bias requires nucleotide sequences that are not accessible from JupyterHub. [src: genotype_to_phenotype_enigma] Morgan fingerprints require RDKit. [src: genotype_to_phenotype_enigma] The report says these features would be needed for continuous growth-rate prediction. [src: genotype_to_phenotype_enigma]

## Modeling Methodology; Results

This part of the report describes how the models were built and validated, the datasets they draw on, and the descriptive statistics of the growth curves and environments. All models are gradient-boosted decision trees (GBDT) validated by holding out whole genera. [src: genotype_to_phenotype_enigma]

### Model and regularization

The report uses LightGBM v4.6 for all models, with regularization tuned for the 46K-pair corpus. [src: genotype_to_phenotype_enigma] Settings are listed below.

- num_leaves=31 and min_data_in_leaf=20, to prevent overfitting to small genera. [src: genotype_to_phenotype_enigma]
- feature_fraction=0.3, which subsamples 30% of 4,300 features per tree and acts as built-in feature selection. [src: genotype_to_phenotype_enigma]
- bagging_fraction=0.8 and bagging_freq=5, for row subsampling and variance reduction. [src: genotype_to_phenotype_enigma]
- reg_alpha=0.5 and reg_lambda=2.0, for L1 and L2 regularization on leaf weights. [src: genotype_to_phenotype_enigma]
- n_estimators=300 and learning_rate=0.05, a moderate ensemble with slow learning. [src: genotype_to_phenotype_enigma]

The report chose GBDT because growth depends on nonlinear gene interactions. It argues that linear models cannot capture interactions between gene presence and condition type, so they underestimate the contribution of specific KEGG orthologs (KOs). [src: genotype_to_phenotype_enigma] This is the report's rationale, not a head-to-head test in this part. GBDT handles the 4,293-dimensional binary feature space through tree splits, with no dimensionality reduction. [src: genotype_to_phenotype_enigma]

### Validation design

The main test is a genus-level blocked holdout. Each of 106 genera with ≥50 pairs is held out, and the model trains on all other genera. AUC (area under curve), accuracy and balanced F1 are reported per held-out genus. [src: genotype_to_phenotype_enigma] The report calls this the most stringent test of cross-genus generalization, because the model cannot use phylogenetic signal from the held-out genus. [src: genotype_to_phenotype_enigma]

Two further evaluations use the pooled holdout predictions. The first aggregates predictions by condition class (amino acid, carbon source, metal and others) and reports AUC and accuracy per class, to show where prediction works and where it fails. [src: genotype_to_phenotype_enigma] The second reports AUC separately for 343 conditions with ≥30 predictions and both growth classes. [src: genotype_to_phenotype_enigma] At this level, tryptophan is predictable (AUC 0.933). [src: genotype_to_phenotype_enigma] Turanose is not predictable (AUC 0.059). [src: genotype_to_phenotype_enigma]

Fitness Browser (FB) concordance is a biological validation, not training. The 7 FB anchor strains form the validation set. [src: genotype_to_phenotype_enigma] After training on the full corpus, the top SHAP (Shapley additive explanations) features are expanded into correlation-grouped blocks (connected components at |r|>0.8). These are mapped to FB loci through fb_pangenome_link.tsv. The test then asks whether the loci show significant fitness effects (|t|>4) in matched FB experiments. Enrichment over the genome-wide random baseline measures whether the model's features are mechanistically grounded. [src: genotype_to_phenotype_enigma]

### Interpretation

SHAP TreeExplainer splits each prediction into contributions from individual KOs and condition features. Global importance is the mean |SHAP| across predictions. [src: genotype_to_phenotype_enigma] Features correlated at |r|>0.8 are grouped into connected-component blocks. [src: genotype_to_phenotype_enigma] The largest block has 63 features: genome size, gene count, operons, rRNA/tRNA and co-inherited KOs. The report calls it the "genome scale axis." [src: genotype_to_phenotype_enigma]

Credit can be split among redundant features. The report therefore sums SHAP within groups to get group-level importance. It reads individual SHAP values within a group as "this group matters", not "this specific KO matters." [src: genotype_to_phenotype_enigma]

### Data sources

| Dataset | Scale | Further detail |
|---|---|---|
| ENIGMA growth curves | 303 plates, 27,632 curves, 7.57M timepoints [src: genotype_to_phenotype_enigma] | 123 strains x 195 molecules [src: genotype_to_phenotype_enigma] |
| ENIGMA Genome Depot | 3,110 genomes, 6.8M proteins [src: genotype_to_phenotype_enigma] | 3.7M KO, 6.4M COG (clusters of orthologous groups) annotations [src: genotype_to_phenotype_enigma] |
| Fitness Browser | 7 anchor strains, 27M fitness scores [src: genotype_to_phenotype_enigma] | 486 anchor (strain x condition) pairs [src: genotype_to_phenotype_enigma] |
| Web of Microbes | 6 strains, 630 metabolite observations [src: genotype_to_phenotype_enigma] | 105 compounds per strain [src: genotype_to_phenotype_enigma] |
| Carbon Source Phenotypes | 795 genomes x 379 conditions [src: genotype_to_phenotype_enigma] | ~53K binary growth labels [src: genotype_to_phenotype_enigma] |
| Microbial Atlas (16S) | 464K samples, 260M OTU (operational taxonomic unit) counts [src: genotype_to_phenotype_enigma] | 14 ENIGMA genera in 4K-289K samples each [src: genotype_to_phenotype_enigma] |
| CORAL (local) | 596 locations, 587 ASV (amplicon sequence variant) communities [src: genotype_to_phenotype_enigma] | 123 strains mapped to 24 wells [src: genotype_to_phenotype_enigma] |

### Growth curve parameters

These are the distributions in the fit-ok subset (n=9,861). [src: genotype_to_phenotype_enigma]

| Parameter | Median | IQR | Range |
|---|---|---|---|
| mumax (h^-1) | 0.028 [src: genotype_to_phenotype_enigma] | 0.017-0.048 [src: genotype_to_phenotype_enigma] | 0.001-0.50 [src: genotype_to_phenotype_enigma] |
| Lag (h) | 11.4 [src: genotype_to_phenotype_enigma] | 5.2-18.5 [src: genotype_to_phenotype_enigma] | 0-48 [src: genotype_to_phenotype_enigma] |
| Asymptotic A (OD, optical density) | 0.315 [src: genotype_to_phenotype_enigma] | 0.14-0.66 [src: genotype_to_phenotype_enigma] | 0.05-2.77 [src: genotype_to_phenotype_enigma] |
| R^2 | 0.980 [src: genotype_to_phenotype_enigma] | 0.96-0.99 [src: genotype_to_phenotype_enigma] | 0.80-1.00 [src: genotype_to_phenotype_enigma] |
| AUC (OD*h) | 15.8 [src: genotype_to_phenotype_enigma] | 5.5-31.5 [src: genotype_to_phenotype_enigma] | 0.3-98 [src: genotype_to_phenotype_enigma] |

### Condition alignment across datasets

Few conditions are shared across datasets. Five compounds appear in all 4 datasets: cytidine, glycine, inosine, thymidine and uridine. [src: genotype_to_phenotype_enigma] Another 30 are shared by 3 datasets, including acetate, citrate, ethanol, glycerol, pyruvate and succinate. [src: genotype_to_phenotype_enigma] A further 107 are shared by 2 datasets, spanning carbon sources, amino acids, metals and antibiotics. [src: genotype_to_phenotype_enigma] The dense ENIGMA anchor set has 486 pairs across 7 FB-anchor strains x 72 conditions. [src: genotype_to_phenotype_enigma]

### Co-occurrence clusters A and B

The report compares two ENIGMA co-occurrence clusters on pH, temperature, sample counts and dominant environments. [src: genotype_to_phenotype_enigma]

| Measure | Cluster A | Cluster B |
|---|---|---|
| Mean pH | 6.78 [src: genotype_to_phenotype_enigma] | 5.43 (delta -1.35) [src: genotype_to_phenotype_enigma] |
| Mean temperature | 15.7 C [src: genotype_to_phenotype_enigma] | 22.6 C (delta +6.9 C) [src: genotype_to_phenotype_enigma] |
| Exclusive samples (global) | 179,023 [src: genotype_to_phenotype_enigma] | 3,720, described as 48x rarer [src: genotype_to_phenotype_enigma] |
| Dominant environments | aquatic 33%, plant 23%, soil 22% [src: genotype_to_phenotype_enigma] | aquatic 39%, soil 23%, plant 18% [src: genotype_to_phenotype_enigma] |

## Interpretation: What we have learned

This part of the report interprets its two phases. Act I built a multi-dataset foundation, and Act II delivered a calibrated genotype-to-phenotype model with a clear boundary on what gene content predicts. [src: genotype_to_phenotype_enigma]

### Act I foundation

Act I established 486 anchor pairs where growth curves, gene fitness and genome annotations coexist. [src: genotype_to_phenotype_enigma] It also set up 8 metabolic guilds across 123 strains. [src: genotype_to_phenotype_enigma] The report claims this is the first integration of ENIGMA growth curves with Fitness Browser (FB) gene fitness at condition-matched scale, and says previous work used these datasets separately. [src: genotype_to_phenotype_enigma] A global pH-driven niche partition connects local Oak Ridge co-occurrence to 464K global 16S samples. [src: genotype_to_phenotype_enigma] The contamination-gradient pattern recurs globally as a partition by pH (pH 5.4 vs 6.8). [src: genotype_to_phenotype_enigma] Green et al. (2012) showed Rhodanobacter dominance in acidic Oak Ridge wells, and Smith et al. (2015) showed that community composition predicts geochemistry. [src: genotype_to_phenotype_enigma] The report finds that the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic worldwide. It reads this as a fundamental niche axis, not site-specific adaptation. [src: genotype_to_phenotype_enigma] It argues that pH tolerance is a first-order phenotype that genotype-to-phenotype models must capture. [src: genotype_to_phenotype_enigma] See [[concepts/ph-driven-niche-partitioning-and-genus-co-occurrence-in-contaminated-subsurface-communities]].

The report also documented a strain-name collision pitfall. It calls this a systematic hazard for any project linking field isolates to reference databases by short strain identifiers. [src: genotype_to_phenotype_enigma]

### What gene content predicts

In full-corpus modelling (46K pairs, 106 genus-blocked holdouts), binary growth is predictable from KEGG ortholog (KO) content for some condition classes and not for others. [src: genotype_to_phenotype_enigma] The report summarises the amino acid and nucleoside result as AUC (area under curve) ~0.78 and the carbon source result as moderate, 0.70. [src: genotype_to_phenotype_enigma] Metals, antibiotics and nitrogen are not predictable from KO content. [src: genotype_to_phenotype_enigma] The full-corpus work spans 727 genomes. [src: genotype_to_phenotype_enigma]

The Act II verdict reports these AUCs separately: amino acids 0.775, nucleosides 0.780 and carbon sources 0.695. [src: genotype_to_phenotype_enigma] It again finds no prediction of binary growth on metals, antibiotics or nitrogen from KO content. [src: genotype_to_phenotype_enigma] These exact figures are not labelled in the quotes as the full-corpus values. See [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content]].

Continuous growth parameters (µmax, lag, yield) are not predictable from KO content or bulk genomic features under cross-genus holdout. [src: genotype_to_phenotype_enigma] The report calls this a biological limit, not a data problem. [src: genotype_to_phenotype_enigma] It reasons that 46K training pairs and 123 strains provide enough data. In its words, gene presence tells you IF an organism can use a substrate, not HOW FAST. [src: genotype_to_phenotype_enigma] Growth rate depends on enzyme kinetics, expression levels and ribosome efficiency, which binary KO presence/absence does not capture. [src: genotype_to_phenotype_enigma] Codon usage bias is proposed as the natural next feature. It correlates with maximum growth rate through ribosomal protein optimization, but it needs nucleotide sequences that are not currently accessible. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content]].

### Training-set size and feature meaning

With 7 anchor strains (NB06), the model learned genome scale (25.3%) and condition class (45.9%). [src: genotype_to_phenotype_enigma] With 46K pairs (NB07), it learned condition-specific KOs, such as the ribose transporter predicting ribose growth. [src: genotype_to_phenotype_enigma] Key predictors include the ribose transporter, protocatechuate cycloisomerase and AraC regulators. [src: genotype_to_phenotype_enigma] The n=7 → n=46K comparison quantifies the corpus size needed for this shift. [src: genotype_to_phenotype_enigma] The report concludes that hundreds of genomes per condition are needed, not a handful. [src: genotype_to_phenotype_enigma] Naive SHAP (Shapley additive explanations) on 4,305 KOs splits credit across correlated gene blocks. [src: genotype_to_phenotype_enigma] Grouping at |r|>0.8 reveals a 63-feature genome-scale axis that dominates with small training sets. [src: genotype_to_phenotype_enigma] See [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features]].

The SHAP features are mechanistically coherent, but concordance with FB is weak (1.19×). The report reads this as cross-genus gene presence and within-strain gene essentiality being different biological questions. [src: genotype_to_phenotype_enigma] See [[concepts/concordance-between-cross-genus-predictive-genes-and-within-strain-gene-fitness]].

### Exometabolomics

Multivariate gradient boosted decision trees (GBDT) fail for Web of Microbes (WoM) exometabolomics at small n, and fail at n=6 in the report's analysis. [src: genotype_to_phenotype_enigma] Univariate per-metabolite correlation recovers 940 mechanistic gene-metabolite associations across all 62 variable metabolites. [src: genotype_to_phenotype_enigma] These comprise 454 production and 486 consumption associations. [src: genotype_to_phenotype_enigma] FB-cognate rich-media-significant KOs give a focused set of 156 genes. [src: genotype_to_phenotype_enigma] The report concludes that the method must match sample size and biological resolution. [src: genotype_to_phenotype_enigma] Growth-predictive KOs and metabolite-production KOs are different feature sets (ρ ≈ 0.04). [src: genotype_to_phenotype_enigma] See [[concepts/gene-metabolite-association-discovery-in-small-exometabolomic-datasets]].

### Errors and active learning

The model makes 1,276 high-confidence errors. They concentrate in genus × condition-class cells: Methylobacterium on amino acids, Sphingomonas on complex carbons and Microbacterium on nucleosides. [src: genotype_to_phenotype_enigma] Ranking by error × uncertainty × field relevance gives a 50-experiment list. It prioritizes the organic acids fumaric, melibionic and itaconic, plus nitrate and low-pH-relevant substrates. Prescottella and Microbacterium are the most informative test genera. [src: genotype_to_phenotype_enigma] The weighting turns generic uncertainty into bioremediation priorities: nitrogen cycle, organic acid metabolism and low-pH compatibility. [src: genotype_to_phenotype_enigma] The two genera have the least reliable current predictions (Prescottella 16%, Microbacterium 23%). [src: genotype_to_phenotype_enigma] Formal retrospective subsampling against random selection is still the next validation step. The ranking framework is in place. [src: genotype_to_phenotype_enigma] See [[concepts/active-learning-for-selecting-growth-experiments-from-model-errors]].

### Hypothesis verdicts

- H1 (feature resolution × phenotype resolution) is strongly supported. Condition-specific KOs best predict binary amino acid growth, while growth rate needs bulk features such as CUB that are not yet available. [src: genotype_to_phenotype_enigma]
- H2 (paradigm complementarity) is supported. GapMind (78.8% accuracy, 24% coverage, mechanistic) and GBDT (AUC 0.78 on amino acids, broader coverage, data-driven) complement each other. [src: genotype_to_phenotype_enigma]
- H3 (biological meaningfulness) is only partially addressable. Full FB concordance validation with correlation-group expansion remains undone. [src: genotype_to_phenotype_enigma]
- H4 (carbon source phenotype, CSP, transfer) is supported for matched conditions: AUC 0.800 vs 0.633 for ENIGMA-only on matched conditions, and full-corpus AUC 0.78 for amino acids. [src: genotype_to_phenotype_enigma]
- H5 (exometabolomic prediction) is revised, as described above. [src: genotype_to_phenotype_enigma]
- H6 (active learning) is partially supported. [src: genotype_to_phenotype_enigma]

## Interpretation; Data

This part of the report gives the interpretive caveats on the ENIGMA growth-curve, condition-alignment and biogeography analyses. It also lists the data collections and derived data tables the study used. The caveats concern condition matching, curve quality, taxonomic resolution and missing geochemistry. [src: genotype_to_phenotype_enigma]

### Interpretation and limits

**Condition alignment and curve quality.** Condition alignment is string-based. It gives 42 molecular matches through normalized names, and the report suggests ChEBI-ID canonicalization would likely expand this to 60-80 matches. [src: genotype_to_phenotype_enigma] Growth curve QC is a limit as well: 35.7% of curves pass Gompertz fitting. [src: genotype_to_phenotype_enigma] The report interprets the 55% no-growth fraction as biological. [src: genotype_to_phenotype_enigma] About 9% of curves fail fitting for technical reasons: monotone violations, short duration and edge-well effects. [src: genotype_to_phenotype_enigma]

**Biogeography.** The Microbial Atlas analysis is at genus level (16S resolution). [src: genotype_to_phenotype_enigma] Species-level biogeography is available for only 20 pangenome-linked strains with verified GTDB matches. [src: genotype_to_phenotype_enigma] Spearman co-occurrence suggests shared or exclusive niches but does not prove direct interaction. [src: genotype_to_phenotype_enigma] The report proposes compositionally aware SparCC analysis on the full 100WS ASV (amplicon sequence variant) matrix to strengthen these findings. [src: genotype_to_phenotype_enigma]

**Geochemistry.** The report has no geochemistry linkage yet. Well-level uranium, nitrate and metal concentrations are available in CORAL bricks 10/80, but sample-to-location name resolution is incomplete. [src: genotype_to_phenotype_enigma]

### Data collections

| Collection | Contents used |
|---|---|
| `enigma_coral` | Growth curves, strain metadata, isolation locations, ASV community data, GTDB-Tk taxonomy [src: genotype_to_phenotype_enigma] |
| `enigma_genome_depot_enigma` | Genome annotations (KO, COG, OG, EC, GO) for all 123 strains [src: genotype_to_phenotype_enigma] |
| `kescience_fitnessbrowser` | RB-TnSeq (random barcode transposon sequencing) fitness data for 7 anchor strains [src: genotype_to_phenotype_enigma] |
| `kescience_webofmicrobes` | Exometabolomics for 6 strains [src: genotype_to_phenotype_enigma] |
| `globalusers_carbon_source_phenotypes` | Binary growth phenotype pretraining corpus [src: genotype_to_phenotype_enigma] |
| `kbase_ke_pangenome` | Species-level biogeography, pangenome context [src: genotype_to_phenotype_enigma] |
| `arkinlab_microbeatlas` | Global 16S biogeography, co-occurrence, environmental metadata [src: genotype_to_phenotype_enigma] |

### Derived data tables

Reported sizes of the main derived tables, by theme:

- Growth and conditions: growth parameters from Gompertz fits per well (27,632) [src: genotype_to_phenotype_enigma]; cross-dataset condition alignment across 4 datasets (1,192) [src: genotype_to_phenotype_enigma]; dense anchor strain x condition pairs (486) [src: genotype_to_phenotype_enigma]; full strain x condition coverage matrix (13,632). [src: genotype_to_phenotype_enigma]
- Strain genomes: KO presence/absence (123 x 7,167) [src: genotype_to_phenotype_enigma]; COG class gene counts (123 x 23) [src: genotype_to_phenotype_enigma]; genome scalars, guild and GTDB taxonomy (123). [src: genotype_to_phenotype_enigma]
- Biogeography: genus-wide environment profiles from GTDB (52) [src: genotype_to_phenotype_enigma]; Spearman co-occurrence matrix for 100WS (15 x 15) [src: genotype_to_phenotype_enigma]; Jaccard co-occurrence over 464K samples (18 x 18) [src: genotype_to_phenotype_enigma]; strain to well to coordinates mapping (123). [src: genotype_to_phenotype_enigma]
- Modeling: full modeling table of features and targets (486 x 173) [src: genotype_to_phenotype_enigma]; leave-one-strain-out CV fold assignments (7). [src: genotype_to_phenotype_enigma]
- Feature layers: GTDB order plus guild one-hot (123 x 28) [src: genotype_to_phenotype_enigma]; genome size, genes, operons, rRNA, tRNA (123 x 8) [src: genotype_to_phenotype_enigma]; full KO presence/absence (123 x 7167) [src: genotype_to_phenotype_enigma]; COG class counts (123 x 23) [src: genotype_to_phenotype_enigma]; condition class plus concentration (72 x 7). [src: genotype_to_phenotype_enigma]
- Results: per-genus AUC/accuracy under genus-blocked holdout (106) [src: genotype_to_phenotype_enigma]; per-pair predictions from that holdout (~43K) [src: genotype_to_phenotype_enigma]; SHAP importance with KEGG annotations (4,300) [src: genotype_to_phenotype_enigma]; per-condition AUC/accuracy for 343 testable conditions (343) [src: genotype_to_phenotype_enigma]; AUC with and without interaction features per genus (106). [src: genotype_to_phenotype_enigma]
- Fitness Browser concordance: overall FB concordance per anchor strain (7) [src: genotype_to_phenotype_enigma]; condition-matched FB concordance with enrichment (7) [src: genotype_to_phenotype_enigma]; SHAP KO to FB locus mapping with correlation expansion (335). [src: genotype_to_phenotype_enigma]

## Supporting Evidence; Future Directions; Authors

This part of the report says the Act I–III backbone of the project is complete. The remaining work is extensions that need outside data or formal validations of frameworks already delivered. [src: genotype_to_phenotype_enigma] It also lists the notebooks behind the analyses and names the author. [src: genotype_to_phenotype_enigma]

### Status and proposed extensions

The report separates two kinds of remaining work. One kind needs data outside JupyterHub reach. The other kind is formal validation of delivered frameworks. [src: genotype_to_phenotype_enigma]

**Codon usage bias.** The report proposes computing codon usage bias (gRodon S-value or ENC) from CDS nucleotide sequences. The aim is to test whether ribosomal efficiency explains the µmax variation that KO (KEGG ortholog) presence cannot. [src: genotype_to_phenotype_enigma] It cites Xu et al. (2025, Phydon) as showing this is the natural next feature. [src: genotype_to_phenotype_enigma] The computation needs GenBank files on the CGCMS server, which JupyterHub cannot currently reach. [src: genotype_to_phenotype_enigma] See [[entities/codon-usage-bias]].

**Condition canonicalization.** The current 42 molecular matches from string normalization could grow to 60–80 through programmatic ChEBI ID resolution. That would enlarge the cross-dataset anchor frame for FB (Fitness Browser) concordance checks. [src: genotype_to_phenotype_enigma] This is a proposal, not a measured result.

**Fitness Browser concordance.** The current enrichment is 1.19×, using correlation-expanded blocks. [src: genotype_to_phenotype_enigma] The report proposes expanding each top-SHAP (Shapley additive explanations) KO to all KOs in its KEGG module. This may recover more mechanistic signal and would separate "wrong feature, right pathway" from "wrong pathway". [src: genotype_to_phenotype_enigma] See [[concepts/concordance-between-cross-genus-predictive-genes-and-within-strain-gene-fitness]].

**Geochemistry linkage.** Uranium, nitrate and metal concentrations per well are available in CORAL bricks 10/80. [src: genotype_to_phenotype_enigma] Sample-to-location name resolution is incomplete, which limits this linkage. [src: genotype_to_phenotype_enigma] The report proposes linking strain-isolation-well coordinates in `coral_strain_locations.tsv` to per-well geochemistry. That would test whether acid-tolerant Cluster B strains come from higher-contamination wells locally, not just globally. [src: genotype_to_phenotype_enigma] See [[concepts/ph-driven-niche-partitioning-and-genus-co-occurrence-in-contaminated-subsurface-communities]].

### Active learning

The NB10 deliverable is a 50-experiment list that includes fumaric acid, melibionic acid, and nitrate paired with Prescottella/Microbacterium. [src: genotype_to_phenotype_enigma] It is ranked by error × uncertainty × field relevance. [src: genotype_to_phenotype_enigma] Running these experiments is an ENIGMA experimental decision, not an analytical one. [src: genotype_to_phenotype_enigma] The formal H6 active-learning test is still to be done, although the NB10 ranking framework is in place. [src: genotype_to_phenotype_enigma] The proposed test is retrospective subsampling of held-out current data. It would measure accuracy improvement per labeled pair when experiments are added in active-learning-ranked order versus random order. [src: genotype_to_phenotype_enigma] See [[concepts/active-learning-for-selecting-growth-experiments-from-model-errors]].

### Notebooks supporting the results

| Notebook | Content |
|---|---|
| NB00 | Five-dataset convergence mapping, data availability audit [src: genotype_to_phenotype_enigma] |
| NB01 | Modified Gompertz fitting of 27,632 growth curves [src: genotype_to_phenotype_enigma] |
| NB02 | Cross-dataset condition alignment, anchor set identification [src: genotype_to_phenotype_enigma] |
| NB03 | KO/COG (clusters of orthologous groups) profiling, metabolic guild clustering [src: genotype_to_phenotype_enigma] |
| NB04 | Biogeography (3 scales), co-occurrence, niche characterization [src: genotype_to_phenotype_enigma] |
| NB05 | 4-level feature hierarchy, modeling table assembly, CV (cross-validation) fold structure [src: genotype_to_phenotype_enigma] |
| NB06 | Nested GBDT (gradient boosted decision tree) M0-M3, SHAP, correlation grouping, variance decomposition [src: genotype_to_phenotype_enigma] |
| NB07 (condition-specific) | GapMind baseline, CSP (carbon source phenotypes) transfer comparison (preliminary) [src: genotype_to_phenotype_enigma] |
| NB07 (full corpus) | Full-corpus GBDT (46K pairs), genus-blocked holdout, per-condition analysis, SHAP [src: genotype_to_phenotype_enigma] |
| NB08 | Web of Microbes (WoM) exometabolomic prediction using per-metabolite point-biserial correlation [src: genotype_to_phenotype_enigma] |
| NB09 | Audit of 42,771 predictions against ground truth, with per-genus × condition-class error patterns and candidate ranking [src: genotype_to_phenotype_enigma] |
| NB10 | Active-learning proposal of 50 conditions, with top candidates for the next ENIGMA experiments [src: genotype_to_phenotype_enigma] |

NB08 records GBDT failure at n=6. [src: genotype_to_phenotype_enigma] It also records 940 mechanistic KO-metabolite associations across 62/62 variable metabolites. [src: genotype_to_phenotype_enigma] See [[concepts/gene-metabolite-association-discovery-in-small-exometabolomic-datasets]]. NB09 identifies 1,276 confident errors. [src: genotype_to_phenotype_enigma]

### Authors

The report lists Adam Arkin (ORCID: 0000-0002-4999-2931) of U.C. Berkeley / Lawrence Berkeley National Laboratory as author. [src: genotype_to_phenotype_enigma]

## Caveats and Open Work

- Short strain names caused false matches: MT20 (Rhodanobacter glycinis) matched Streptococcus pneumoniae, injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma] Authoritative taxonomy plus a genus-consistency check cut pangenome linkages from 32 to 20 and removed all false matches. [src: genotype_to_phenotype_enigma]
- The exometabolomic result rests on only 6 strains. [src: genotype_to_phenotype_enigma]
- The claim that resolving failures would raise accuracy from 65.1% toward a per-class ceiling of ~78% is a proposal, not a measured result. [src: genotype_to_phenotype_enigma]
- The pH-dependent growth difference between clusters is a hypothesis the report states for testing. [src: genotype_to_phenotype_enigma]

## Slots Into

- [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content]]: binary growth is predictable on amino acids and nucleosides but not on metals, antibiotics or nitrogen. [src: genotype_to_phenotype_enigma]
- [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content]]: kinetics are treated as a fundamental limitation. [src: genotype_to_phenotype_enigma]
- [[concepts/training-set-size-and-the-shift-from-genome-scale-to-gene-specific-predictive-features]]: 46K pairs are needed for gene-specific features. [src: genotype_to_phenotype_enigma]
- [[concepts/ph-driven-niche-partitioning-and-genus-co-occurrence-in-contaminated-subsurface-communities]]: the clusters differ by 1.35 pH units. [src: genotype_to_phenotype_enigma]
- [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]]: the MT20 name collision. [src: genotype_to_phenotype_enigma]
