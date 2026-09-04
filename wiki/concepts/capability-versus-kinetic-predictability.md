---
type: "Concept"
description: "Genomic capability is more transferable than continuous kinetic performance"
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md"]
---
# Genomic Capability Is More Predictable Than Continuous Growth Kinetics

The study distinguishes two genotype-to-phenotype tasks: predicting whether a strain can grow under a condition, and predicting continuous kinetic properties such as maximum growth rate, lag, or yield. [[summaries/genotype_to_phenotype_enigma__REPORT]] shows that genome content provides useful but condition-dependent information for the first task, whereas it provides little cross-genus predictive power for the second. [src: genotype_to_phenotype_enigma]

## Core distinction

Binary growth capability asks whether genomic content supports growth on or under a specified condition, while continuous kinetics asks how rapidly, how long after inoculation, or to what yield the organism grows. The distinction is central to [[concepts/condition-specific-fitness]] and to the definition of the prediction task in [[concepts/gene-essentiality]]. [src: genotype_to_phenotype_enigma]

The biological interpretation is that gene content can encode the presence of transporters, catabolic enzymes, biosynthetic pathways, and regulators needed to use a substrate, while growth rate also depends on enzyme kinetics, expression, regulatory state, and ribosome efficiency. The report therefore treats capability prediction as more directly encoded by comparative genome features than continuous kinetic prediction. [src: genotype_to_phenotype_enigma]

The [[summaries/pathway_capability_dependency__REPORT]] evidence **refines** this distinction by separating genomic capability from experimentally observed dependency: across 161 organism–pathway pairs, complete pathways could be either fitness-important or apparently dispensable under aggregate laboratory conditions. All 66 pairs classified as Latent Capability nevertheless became fitness-important under at least one condition type, although the median-based reclassification threshold can produce this result by construction. [src: pathway_capability_dependency] A broader analysis of 1,695 complete pathway–organism pairs similarly classified 267 (15.8%) as latent, 547 (32.3%) as intermediate, and 881 (51.9%) as active; carbon-source pathways were more often latent than amino-acid biosynthesis pathways, at 24.3% versus 6.5%. [src: metabolic_capability_dependency] Thus, genomic capability is not equivalent to either growth in a particular assay or permanent gene dispensability. [src: pathway_capability_dependency]

## Evidence from the ENIGMA growth corpus

The integrated corpus contained 27,632 growth curves from 123 strains, 195 molecules, and 303 plates, representing 7.57M timepoints. Of these curves, 15,227 (55.1%) showed no detectable growth, 9,861 (35.7%) were fit-ok, and fit-ok curves had median modified Gompertz R² = 0.98, median µmax = 0.028 h⁻¹, median lag = 11.4 h, and median asymptotic OD increase A = 0.315. [src: genotype_to_phenotype_enigma]

The continuous measurements were not uniformly simple: 40% of curves showed at least two growth phases in their smoothed derivative. This additional curve structure illustrates why a binary growth label and a kinetic parameter are different phenotype resolutions. [src: genotype_to_phenotype_enigma]

## Capability prediction is conditional, not universal

The initial seven-strain model achieved AUC 0.633 for binary growth under leave-one-strain-out validation, where AUC means area under the receiver-operating-characteristic curve. Its features included 4,305 prevalence-filtered KO features, 23 COG classes, condition class, concentration, phylogeny, and bulk genome features. [src: genotype_to_phenotype_enigma]

In the full corpus, LightGBM gradient-boosted decision-tree modeling used 46,389 genome × condition pairs from 727 genomes, 106 genus-blocked holdouts, and 4,293 shared [[entities/kegg]] orthologs. Overall binary-growth AUC was 0.620, but performance varied by condition class: amino acids reached AUC 0.775 across 7,765 pairs, nucleosides reached 0.780 across 829 pairs, carbon sources reached 0.695 across 8,965 pairs, other conditions reached 0.654 across 24,590 pairs, antibiotics reached 0.619 across 238 pairs, metals reached 0.605 across 232 pairs, and nitrogen reached 0.435 across 152 pairs. [src: genotype_to_phenotype_enigma]

Adding KO × condition interaction features increased mean AUC from 0.620 to 0.653, an improvement of 0.032, and improved performance in 80 of 106 held-out genera. Across 343 individually testable conditions, 95 achieved AUC > 0.75; the best individual conditions were tryptophan at 0.933, phenylalanine at 0.932, valine at 0.927, mannose at 0.904, and galactose at 0.895. [src: genotype_to_phenotype_enigma]

The pathway-capability analysis **supports** the interpretation that capability is condition-dependent rather than universal: its 66 aggregate Latent Capability pairs all showed fitness importance under at least one condition type, with nitrogen limitation, stress, and carbon limitation the most frequent triggers. [src: pathway_capability_dependency] However, this does not by itself validate each reclassification because the condition-specific median importance threshold can cause pathways to cross the threshold by construction. [src: pathway_capability_dependency] The newer analysis **refines** this result by showing that the latent fraction remained qualitatively non-trivial across 16 threshold combinations, ranging from 4.7% to 21.1%, while also identifying a large intermediate class. [src: metabolic_capability_dependency]

Capability prediction was also constrained by annotation and training coverage. GapMind achieved AUC 0.646, 78.8% accuracy, and 24.3% coverage on 118 testable pairs, with 96.5% recall and 79% precision. Matched-condition Carbon Source Phenotypes transfer achieved AUC 0.800 and 76.8% accuracy at 23% coverage, while internal five-fold Carbon Source Phenotypes validation achieved AUC 0.858. Approximately 76% of ENIGMA conditions lacked GapMind pathway coverage or Carbon Source Phenotypes training data, and prediction on those conditions fell to approximately AUC 0.63. [src: genotype_to_phenotype_enigma]

These results support [[concepts/computational-pathway-prediction-validation]] and [[concepts/environmental-resistome]] as related methodological concerns: a capability prediction can be limited not only by biology but also by whether the relevant pathway and condition are represented in the annotation and training resources. [src: genotype_to_phenotype_enigma] The pathway-capability analysis **refines** this concern: it used SEED subsystem roles as a proxy for GapMind pathway membership, excluded two pathways without matching SEED descriptions, excluded alanine because fewer than 3 SEED-annotated genes met the coverage threshold, and notes that direct GapMind per-step gene assignments would improve precision. [src: metabolic_capability_dependency] Thus, apparent capability or dependency can reflect annotation resolution as well as genotype.

## Continuous kinetics did not transfer across genera

Continuous µmax, lag, and yield-related max_A were not predictable under genus-blocked holdout from KO presence/absence or bulk genomic features in either the 46K-pair model or a dedicated bulk-feature regression, producing negative R² in both analyses. [src: genotype_to_phenotype_enigma]

Weak univariate associations did not overcome this limitation: n_unique_KOs correlated with µmax at r = +0.42 and n_tRNA correlated with µmax at r = +0.30, but both relationships were phylogenetically confounded and provided zero cross-genus predictive power. [src: genotype_to_phenotype_enigma]

This result refines [[concepts/cross-species-fitness-transferability]] and [[concepts/lab-field-fitness-concordance]] by showing that even when broad genomic features correlate with a kinetic measurement within the analyzed data, those features need not support prediction in held-out genera. The result is consistent with a distinction between conserved capability and context-dependent performance, rather than evidence that kinetics are unrelated to genotype. [src: genotype_to_phenotype_enigma] The metabolic-capability analysis **supports** the same separation: pathway completeness did not distinguish latent capabilities from active dependencies, with mean conservation values of 0.869 and 0.829, respectively, and Mann–Whitney U p = 0.94. [src: metabolic_capability_dependency] This is pathway-level evidence that encoded capability need not predict measured fitness importance, not a direct test of kinetic transfer.

## Training scale changes what the model learns

Comparing the seven-strain analysis with the 46K-pair analysis showed a qualitative shift from genome-scale to condition-specific prediction. With seven strains, the model learned a genome-size and condition-class pattern equivalent to “big genomes grow on amino acids”; with 46K pairs, it identified substrate-relevant transporters, catabolic enzymes, and regulators. [src: genotype_to_phenotype_enigma]

Correlation-grouped SHAP, where SHAP means SHapley Additive exPlanations, attributed 25.3% of total importance in the initial model to a 63-feature genome-scale axis and 45.9% to condition class. Individual KO blocks involving membrane adaptation, tRNA modification, aromatic catabolism, and flagellar motility contributed approximately 2% each. [src: genotype_to_phenotype_enigma]

The full-corpus model identified condition-specific predictors including K03762 (proP), K10440 (rbsC), K01857 (pcaB), K13633 (ftrA), and K01214 (treX). The report concludes that mechanistic gene-specific prediction requires hundreds of genomes per condition rather than a small number of anchor strains. [src: genotype_to_phenotype_enigma]

This scale dependence connects the concept to [[concepts/gene-function-acquisition-depth]], [[concepts/fitness-condition-coverage-prioritization-bias]], and [[concepts/condition-space-dimensionality]]: broad genomic proxies dominate when the training design is small, while substrate-relevant features become identifiable when genome and condition coverage expand. [src: genotype_to_phenotype_enigma] The pathway-capability analysis **supports** this emphasis on broader genome sampling: across 2,810 GTDB species, variable pathway count was associated with pangenome openness after controlling for genome count (partial Spearman rho=0.530, p=2.83e-203), while metabolic ecotype count also correlated with openness after that control (partial rho=0.322, p=8.0e-07). [src: pathway_capability_dependency] These associations motivate pathway-level capability models, but do not establish improved kinetic prediction. [src: pathway_capability_dependency]

The same analysis found metabolic clustering in all 10 target species, but environment–cluster associations were significant only for *Salmonella enterica* and *Phenylobacterium* sp.; the absence of explicit phylogenetic correction and the coarse metadata make these ecological interpretations observational. [src: metabolic_capability_dependency] This **refines** the training-scale argument: larger genome collections can reveal metabolic structure, but environmental transfer still depends on metadata quality, taxonomic control, and pathway resolution.

## Implications for experimental design

The asymmetry between capability and kinetics implies that a useful prediction system should report binary capability, kinetic estimates, and uncertainty as separate outputs rather than treating them as interchangeable phenotypes. This separation is a hypothesis motivated by the negative kinetic R² values and the condition-dependent binary AUC results. [src: genotype_to_phenotype_enigma]

The study audited 42,771 genus-blocked holdout predictions and found 65.1% overall accuracy, 7,844 false positives, and 7,101 false negatives. Among predictions with |p − 0.5| > 0.25, 1,276 high-confidence errors were concentrated in genus × condition-class cells including Methylobacterium on amino acids, Sphingomonas on other carbon sources, and Microbacterium on nucleosides. [src: genotype_to_phenotype_enigma]

Active learning ranked 343 conditions using error rate × model uncertainty × field-relevance weight and proposed 50 next experiments. The top conditions included fumaric acid, melibionic acid, fumarate, itaconic acid, 2-hydroxypropanoic acid (lactic acid), hydroxy-glutaric acid γ-lactone, difumarate, L-glutamic acid, nitrate, and pyruvic acid. Prescottella, with 16% growth across tested conditions, and Microbacterium, with 23%, were selected as especially informative genera. [src: genotype_to_phenotype_enigma]

The metabolic-capability study **supports** prioritizing experiments that distinguish encoded potential from realized dependency: only 48 organisms were fitness-tested among 293,000 genomes with pathway predictions, and laboratory conditions may make environmentally important pathways appear latent. [src: metabolic_capability_dependency]

## Tensions and limits

The results do not establish that genomic capability is intrinsically easy to predict: overall binary-growth AUC was 0.620, nitrogen prediction was AUC 0.435, and approximately 76% of conditions lacked relevant GapMind or Carbon Source Phenotypes coverage. [src: genotype_to_phenotype_enigma]

The results also do not establish that continuous kinetics are genetically unpredictable in every setting. The negative R² values were obtained under genus-blocked holdout using KO presence/absence and bulk genomic features, and the report proposes adding GC%, codon usage bias, and Morgan molecular fingerprints; GC% was available for only 32 of 727 genomes, codon usage bias required inaccessible nucleotide sequences, and Morgan fingerprints required RDKit. [src: genotype_to_phenotype_enigma]

The pathway-capability result adds a related validation limit rather than resolving these uncertainties: the aggregate Active Dependency/Latent Capability labels were based on a median-based importance threshold, and the analysis recommends independent calibration against known essentials before treating every condition-specific reclassification as biological confirmation. [src: pathway_capability_dependency]

The newer pathway analysis also reports a positive association between latent capability rate and pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades), whereas pathway-level conservation did not distinguish latent from active classes. [src: metabolic_capability_dependency] This **refines** the conservation interpretation rather than contradicting the kinetic results: any relationship may operate through clade-level genome dynamics and community context, not direct pathway-level predictability.

## Open Directions

- Use GenBank nucleotide sequences to compute codon usage bias and test whether it improves genus-blocked prediction of µmax, lag, and max_A, closing the gap left by the current bulk-feature regressions. [src: genotype_to_phenotype_enigma]
- Expand condition canonicalization from normalized names to ChEBI-ID-based matching and test whether increasing the estimated 42 molecular matches to 60–80 improves capability-model training coverage. [src: genotype_to_phenotype_enigma]
- Collect hundreds of genomes per condition and compare KO × condition models with pathway-level models to test whether the observed shift from genome-scale proxies to substrate-specific predictors persists at larger sample sizes. [src: genotype_to_phenotype_enigma]
- Perform retrospective subsampling that compares the 50 active-learning-ranked additions with random selection, testing whether the proposed design reduces false positives and false negatives more efficiently. [src: genotype_to_phenotype_enigma]
- Fit hierarchical or mechanistic kinetic models using growth-curve time series, expression or proteomic measurements, and genomic features to test whether adding regulatory and enzyme-abundance information resolves the negative cross-genus R² values. [src: genotype_to_phenotype_enigma]
- Calibrate the pathway-dependency importance score against independently established essentials, then test whether condition-specific capability labels predict growth and kinetic outcomes without the median-threshold circularity. [src: pathway_capability_dependency]
- Extend pathway-level capability models across the 2,810-species GTDB set and test whether pangenome openness and metabolic ecotype structure improve transfer to held-out genera, while separately evaluating continuous kinetics. [src: pathway_capability_dependency]
- Replace SEED-proxy pathway membership with direct GapMind per-step gene assignments and test whether improved annotation precision changes capability-versus-dependency classification and downstream growth prediction. [src: metabolic_capability_dependency]
- Reanalyze the 22-clade latent-capability/open-pangenome association with explicit organism-to-clade linkage and independent fitness calibration, testing whether the association improves prediction beyond pathway completeness and whether it transfers to kinetic phenotypes. [src: metabolic_capability_dependency]
