---
type: "Summary"
description: "Summary of the project Field vs Lab Gene Importance in *Desulfovibrio vulgaris* Hildenborough."
doc_type: "short"
full_text: "sources/field_vs_lab_fitness__REPORT.md"
---
# Field vs Lab Gene Importance in *Desulfovibrio vulgaris* Hildenborough

Summary of the project Field vs Lab Gene Importance in *Desulfovibrio vulgaris* Hildenborough.

The report asked whether DvH genes important under field-relevant conditions are more conserved in the pangenome than genes important only in the lab. Field-stress, field-core and lab-nutrient important genes are significantly enriched in the core genome. [src: field_vs_lab_fitness] Fitness alone predicts core status poorly, and the field-specific versus lab-specific contrast is not significant. [src: field_vs_lab_fitness] The report concludes that the size of a fitness effect predicts conservation better than the ecological context that produces it. [src: field_vs_lab_fitness] The module-level hypothesis H2, that module conservation tracks field-condition activity, was not supported. [src: field_vs_lab_fitness] The evidence comes from one organism. [src: field_vs_lab_fitness]

## Key Findings

### Experiment classification
The report classified 757 DvH experiments into 6 condition categories. [src: field_vs_lab_fitness] They split broadly into 337 field experiments (44.5%) and 420 lab experiments (55.5%). [src: field_vs_lab_fitness]

| Class | Experiments | Share | Content |
|---|---|---|---|
| Lab-nutrient | 237 | 31.3% | Amino acids, organic acids, carbon sources [src: field_vs_lab_fitness] |
| Field-core | 204 | 26.9% | DvH primary metabolism (sulfate, lactate, formate, pyruvate, H2) [src: field_vs_lab_fitness] |
| Lab-other | 140 | 18.5% | Lab reagents (DMSO, PEG, osmotic stress, iron chelators) [src: field_vs_lab_fitness] |
| Field-stress | 78 | 10.3% | FRC contaminants (uranium, mercury, nitrate, nitrite, oxygen, NO) [src: field_vs_lab_fitness] |
| Heavy-metals | 55 | 7.3% | Metal stress (cobalt, nickel, zinc, copper, manganese, selenium) [src: field_vs_lab_fitness] |
| Lab-antibiotic | 43 | 5.7% | Antibiotics and respiratory inhibitors [src: field_vs_lab_fitness] |

The report classified cobalt, nickel, zinc, copper, manganese, selenium, molybdate, tungstate and aluminum as "field" heavy metals in the broad category, because DvH encounters them at Oak Ridge FRC sites. [src: field_vs_lab_fitness] The classification relies on manual mapping of `condition_1` labels, and edge cases such as zinc sulfate as a metal versus a sulfate source required subjective judgment. [src: field_vs_lab_fitness]

### Core-genome conservation by condition class
Genes important under field-stress conditions are significantly more conserved than baseline. [src: field_vs_lab_fitness] Among 2,725 non-essential genes with both fitness data and pangenome links, 76.3% are core overall. [src: field_vs_lab_fitness] The analysis excludes 678 essential genes (80.1% core) because no transposon mutants were recovered, so they lack fitness data. [src: field_vs_lab_fitness] Including them would raise the overall baseline slightly but would not change condition-class comparisons, which use only non-essential genes. [src: field_vs_lab_fitness] Important genes are those with fitness < -2. [src: field_vs_lab_fitness] This is the primary cutoff, and sensitivity analysis across -1 to -3 confirms the pattern is robust. [src: field_vs_lab_fitness]

| Class | Genes | % core | OR vs baseline | FDR q |
|---|---|---|---|---|
| Field-stress | 298 | 83.6% | 1.58 | 0.026 [src: field_vs_lab_fitness] |
| Field-core | 376 | 82.4% | 1.46 | 0.026 [src: field_vs_lab_fitness] |
| Lab-other | 292 | 81.5% | 1.37 | 0.073 [src: field_vs_lab_fitness] |
| Lab-nutrient | 452 | 81.4% | 1.36 | 0.037 [src: field_vs_lab_fitness] |
| Lab-antibiotic | 109 | 73.4% | 0.86 | 0.49 [src: field_vs_lab_fitness] |
| Heavy-metals | 198 | 71.2% | 0.77 | 0.14 [src: field_vs_lab_fitness] |

Field-stress (q=0.026), field-core (q=0.026) and lab-nutrient (q=0.037) genes are significantly enriched in the core genome after Benjamini-Hochberg false discovery rate (BH-FDR) correction. [src: field_vs_lab_fitness] Lab-nutrient enrichment means that field-relevant conditions are not the only ones that mark conserved genes. [src: field_vs_lab_fitness] Heavy-metals and lab-antibiotic genes trend below baseline but are not significant. [src: field_vs_lab_fitness]

The report describes lab-antibiotic (73.4%) and heavy-metal resistance (71.2%) genes as the least conserved, well below the 76.3% baseline. [src: field_vs_lab_fitness] It suggests that resistance functions are disproportionately accessory, consistent with recently acquired adaptive traits on mobile genetic elements. [src: field_vs_lab_fitness] It also hypothesizes that specific metal resistance mechanisms (efflux pumps, metal-binding proteins) are accessory traits. In contrast, the uranium and mercury responses would involve core pathways such as DNA repair and sulfate reduction. [src: field_vs_lab_fitness] The report describes sulfate reduction, lactate/formate/pyruvate utilization, and uranium, mercury and nitrate stress-response genes as deeply conserved. [src: field_vs_lab_fitness]

### Robustness to threshold
The report describes the pattern as robust across fitness thresholds of -1 to -3. [src: field_vs_lab_fitness] Field-stress genes are consistently the most conserved across those thresholds. [src: field_vs_lab_fitness] Core percentages at thresholds -3.0, -2.0, -1.5 and -1.0 were:

- Field-stress: 89.4%, 83.6%, 84.0%, 82.1% [src: field_vs_lab_fitness]
- Field-core: 84.4%, 82.4%, 81.9%, 79.0% [src: field_vs_lab_fitness]
- Lab-nutrient: 83.5%, 81.4%, 81.0%, 79.5% [src: field_vs_lab_fitness]
- Lab-other: 85.2%, 81.5%, 80.1%, 77.5% [src: field_vs_lab_fitness]
- Lab-antibiotic: 82.2%, 73.4%, 77.3%, 76.2% [src: field_vs_lab_fitness]
- Heavy-metals: 70.6%, 71.2%, 76.7%, 76.7% [src: field_vs_lab_fitness]

Field-stress consistently has the highest conservation across all thresholds, and heavy-metals the lowest. [src: field_vs_lab_fitness] The report attributes the lab-antibiotic dip at -2 to a small sample (n=109 at -2 vs n=45 at -3). [src: field_vs_lab_fitness]

### Field-specific versus lab-specific genes
Both lab-specific and field-specific genes are highly core, but the two groups do not differ significantly. The specificity classes were:

- Lab-specific (sick in lab only): 50 genes, 96.0% core [src: field_vs_lab_fitness]
- Field-specific (sick in field only): 52 genes, 88.5% core [src: field_vs_lab_fitness]
- Field-biased: 89 genes, 83.1% core [src: field_vs_lab_fitness]
- Universal (sick in both): 352 genes, 79.8% core [src: field_vs_lab_fitness]
- Neutral (no strong effects): 2,083 genes, 74.5% core [src: field_vs_lab_fitness]

The field-specific versus lab-specific comparison is not significant (Fisher exact OR=0.32, p=0.27, n=50-52 per group). [src: field_vs_lab_fitness] The universal versus neutral comparison is significant (OR=1.35, p=0.033), and the report calls it the strongest signal: any fitness importance predicts conservation. [src: field_vs_lab_fitness] The report interprets the high core fractions of both specific groups as suggesting that any fitness importance predicts conservation, regardless of ecological context. [src: field_vs_lab_fitness] Fitness effects vary by condition class, but conservation patterns do not cleanly separate field from lab conditions. [src: field_vs_lab_fitness] The report states that this was not anticipated, and suggests that the core genome reflects general functional importance rather than niche-specific selection. [src: field_vs_lab_fitness]

### Predicting core status
Logistic regression with 10-fold cross-validated area under curve (CV-AUC) tested how well fitness predicts core status. [src: field_vs_lab_fitness]

| Model | CV-AUC | Std |
|---|---|---|
| Field fitness only | 0.517 | 0.052 [src: field_vs_lab_fitness] |
| Lab fitness only | 0.531 | 0.052 [src: field_vs_lab_fitness] |
| Field + Lab | 0.548 | 0.053 [src: field_vs_lab_fitness] |
| Full (+ gene length) | 0.645 | 0.068 [src: field_vs_lab_fitness] |

Neither fitness dimension alone is informative (CV-AUC near 0.5). [src: field_vs_lab_fitness] Gene length is a much stronger predictor of core status than fitness effects from either field or lab conditions. [src: field_vs_lab_fitness] Cross-validation confirms the in-sample estimates are not inflated. [src: field_vs_lab_fitness] Gene length is itself confounded with fitness measurement quality, since short genes get fewer transposon insertions, and with core status, since core genes tend to be longer. [src: field_vs_lab_fitness] Field and lab fitness effects are correlated (r ~ 0.7 from the scatter plot), so most genes that are sick in one context are sick in the other. [src: field_vs_lab_fitness]

### Independent component analysis (ICA) fitness modules
Across 52 ICA fitness modules, the mean core fraction is 0.886 and the median is 1.000. [src: field_vs_lab_fitness] Module conservation does not correlate significantly with field condition activity (Spearman rho=0.071, p=0.62), so H2 is not supported. [src: field_vs_lab_fitness] Using the mean core fraction (0.886) as the threshold, [src: field_vs_lab_fitness] modules partition as follows:

- Ecological (field-active + conserved): 21 modules, mean core fraction 0.980 [src: field_vs_lab_fitness]
- Conserved-quiet (low field activity + conserved): 17 modules, 0.983 [src: field_vs_lab_fitness]
- Field-variable (field-active + less conserved): 5 modules, 0.829 [src: field_vs_lab_fitness]
- Lab (low field + less conserved): 9 modules, 0.516 [src: field_vs_lab_fitness]

The lab modules are notably less conserved and contain accessory-genome genes. [src: field_vs_lab_fitness] The revised classification, which uses the mean rather than the median core fraction, finds 9 lab modules with mean core fraction 0.516. This suggests that accessory-genome modules exist and tend to respond to lab-type conditions. [src: field_vs_lab_fitness] The 21 ecological modules contain 239 member genes, of which 52 are unannotated. The report proposes these as candidates for novel environmental adaptation functions. [src: field_vs_lab_fitness] It regards them as distinct from the 9 lab modules and as supporting a functional core relevant to environmental survival. [src: field_vs_lab_fitness]

### Context in the literature
The report builds on Trotter et al. (2023), who generated the DvH barcoded transposon library used here, and adds a pangenome conservation dimension to their fitness measurements. [src: field_vs_lab_fitness] Price et al. (2018) generated the Fitness Browser data underpinning the analysis. [src: field_vs_lab_fitness] The report cites several studies as related work:

- Rosconi et al. (2022): strain-dependent gene essentiality influenced by accessory-genome composition in *S. pneumoniae*. [src: field_vs_lab_fitness]
- Lee et al. (2015): 352 general and 199 condition-specific essential genes in *P. aeruginosa* across six growth media. [src: field_vs_lab_fitness]
- Akusobi et al. (2025): 259 core essential genes and 425 differentially required genes across 21 *M. abscessus* clinical isolates. [src: field_vs_lab_fitness]
- Shi et al. (2021): pre-existing genetic variation in DvH influences chromate tolerance, with chromate transporter DVU0426 crucial for Cr(VI) resistance. [src: field_vs_lab_fitness]
- Huang et al. (2022): genomic islands and prophages as major drivers of evolution and environmental adaptation in *S. algae*. [src: field_vs_lab_fitness]

The report claims to be the first analysis to stratify RB-TnSeq (random barcode transposon sequencing) fitness effects by ecological relevance and test whether field-relevant conditions predict conservation differently from lab conditions. [src: field_vs_lab_fitness]

## Data and Methods

The analysis used 757 DvH experiments and fitness data linked to pangenome conservation. [src: field_vs_lab_fitness] The `kescience_fitnessbrowser` collection supplied RB-TnSeq fitness data for DvH (757 experiments, 2,741 genes). [src: field_vs_lab_fitness] The `kbase_ke_pangenome` collection supplied pangenome gene clusters classified as core, auxiliary or singleton. [src: field_vs_lab_fitness] The report also surveyed the ENIGMA CORAL database (47 tables, `enigma_coral` on the KBase Data Lakehouse) for complementary data. [src: field_vs_lab_fitness] DvH is completely absent from it. [src: field_vs_lab_fitness] Its single transposon sequencing (TnSeq) library is for FW300-N2E2 (*Pseudomonas*). Its DubSeq libraries cover *E. coli*, *P. putida* and *B. thetaiotaomicron*. [src: field_vs_lab_fitness] All 6,705 genomes and 15,015 genes are Oak Ridge environmental isolates, not DvH. [src: field_vs_lab_fitness]

## Caveats and Open Work

- ENIGMA CORAL holds 4,346 field samples with uranium and metals geochemistry across 596 Oak Ridge locations, and 213,044 amplicon sequence variants (ASVs) for community composition. [src: field_vs_lab_fitness] The report considers these potentially useful for future analyses but not for gene-level fitness analysis. [src: field_vs_lab_fitness]
- Essential genes are excluded from the fitness analysis because they have no fitness data. [src: field_vs_lab_fitness]
- The heavy-metals and lab-antibiotic results are not significant, and the lab-antibiotic dip at -2 reflects a small sample. [src: field_vs_lab_fitness]
- The single-organism scope limits generalizability, particularly to organisms with larger accessory genomes. [src: field_vs_lab_fitness]
- The *Nitratidesulfovibrio vulgaris* pangenome has relatively few genomes. This gives a coarse core/auxiliary classification and a high baseline core fraction (76.3%) that compresses effect sizes. [src: field_vs_lab_fitness]
- The field-specific and lab-specific gene sets are small (n=50-52), which limits statistical power for the key comparison. [src: field_vs_lab_fitness]
- Condition classification involved subjective judgment on edge cases, and gene length is confounded with both fitness measurement quality and core status. [src: field_vs_lab_fitness]
- Proposed next step: apply the field versus lab classification to other ENIGMA organisms with Fitness Browser data, such as *Pseudomonas* FW300 strains, to test whether the pattern generalizes. [src: field_vs_lab_fitness]
- Proposed next step: replace binary core/auxiliary status with the fraction of genomes carrying the gene cluster, to increase statistical power. [src: field_vs_lab_fitness]
- Proposed next step: use the 213K ASVs and 4,346 field samples in ENIGMA CORAL to ask whether *Desulfovibrio* abundance at Oak Ridge sites correlates with the geochemistry conditions tested in the Fitness Browser. [src: field_vs_lab_fitness]
- Proposed next step: examine whether antibiotic and heavy-metal resistance genes in the accessory genome are on mobile elements, recently acquired, or shared with co-occurring Oak Ridge species. [src: field_vs_lab_fitness]
- Proposed next step: use continuous fitness scores, such as mean or minimum fitness per condition class, instead of binary important/not-important status as logistic-regression predictors. [src: field_vs_lab_fitness]

## Slots Into

- [[concepts/field-relevant-versus-laboratory-fitness-as-a-predictor-of-gene-conservation]]: field-stress and field-core genes are significantly core-enriched, but field-specific versus lab-specific genes do not differ significantly. [src: field_vs_lab_fitness]
- [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]]: cross-validated AUC for fitness-only models is near 0.5, and gene length predicts better. [src: field_vs_lab_fitness]
- [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]]: ICA module mean core fraction is 0.886, with lab modules at 0.516. [src: field_vs_lab_fitness]
- [[concepts/accessory-conservation-of-metal-and-antibiotic-resistance-genes]]: lab-antibiotic (73.4%) and heavy-metal resistance (71.2%) genes are the least conserved, below the 76.3% baseline. [src: field_vs_lab_fitness]
