---
type: Summary
description: DvH field-versus-lab fitness effects reveal conservation and accessory-resistance
  patterns.
doc_type: short
full_text: ../sources/field_vs_lab_fitness__REPORT.md
title: Field vs Lab Gene Importance in *Desulfovibrio vulgaris* Hildenborough
sources:
- id: field_vs_lab_fitness
  resource: ../sources/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
---
# Field vs Lab Gene Importance in *Desulfovibrio vulgaris* Hildenborough

## Overview

This analysis tested whether ecological relevance of experimental conditions changes the relationship between RB-TnSeq (random barcode transposon sequencing) fitness effects and pangenome conservation in *Desulfovibrio vulgaris* Hildenborough (DvH). It classified 757 Fitness Browser experiments, compared condition-specific gene importance with core/auxiliary status, and analyzed 52 ICA (independent component analysis) fitness modules. The main result is that condition type matters less than fitness importance for predicting conservation, although antibiotic and heavy-metal resistance functions are disproportionately accessory. [^field_vs_lab_fitness]

## Key Findings

### ENIGMA CORAL lacks DvH fitness data

A survey of the ENIGMA CORAL database found 47 tables but no DvH fitness data. Its single TnSeq library is for FW300-N2E2 (*Pseudomonas*), and DubSeq libraries cover *E. coli*, *P. putida*, and *B. thetaiotaomicron*. The database contains 6,705 genomes, 15,015 genes, 4,346 field samples with geochemistry data across 596 Oak Ridge locations, and 213,044 ASVs (amplicon sequence variants) for community composition, but these collections cannot currently support DvH gene-level fitness analysis. [^field_vs_lab_fitness]

### Condition classification

The 757 DvH experiments were assigned to six categories: lab-nutrient, 237 experiments (31.3%); field-core, 204 (26.9%); lab-other, 140 (18.5%); field-stress, 78 (10.3%); heavy-metals, 55 (7.3%); and lab-antibiotic, 43 (5.7%). The broad split was 337 field experiments (44.5%) versus 420 lab experiments (55.5%). Field-core conditions covered sulfate, lactate, formate, pyruvate, and H2 metabolism; field-stress conditions included uranium, mercury, nitrate, nitrite, oxygen, and NO; heavy-metals included cobalt, nickel, zinc, copper, manganese, selenium, molybdate, tungstate, and aluminum. [^field_vs_lab_fitness]

### Field-important genes are enriched in the core genome

Among 2,725 non-essential genes with both fitness data and pangenome links, 76.3% were core overall. A further 678 essential genes were 80.1% core but lacked fitness data because no transposon mutants were recovered. Genes classified as important at fitness < -2 showed the following conservation: field-stress, 298 genes and 83.6% core (OR=1.58 versus baseline, FDR q=0.026); field-core, 376 and 82.4% (OR=1.46, q=0.026); lab-other, 292 and 81.5% (OR=1.37, q=0.073); lab-nutrient, 452 and 81.4% (OR=1.36, q=0.037); lab-antibiotic, 109 and 73.4% (OR=0.86, q=0.49); and heavy-metals, 198 and 71.2% (OR=0.77, q=0.14). FDR means false discovery rate; after BH-FDR correction, field-stress, field-core, and lab-nutrient genes were significantly enriched in the core genome, while heavy-metals and lab-antibiotic genes were not significantly below baseline. [^field_vs_lab_fitness]

### Fitness importance, rather than ecological context, best explains conservation

The specificity analysis identified 50 lab-specific genes that were 96.0% core, 52 field-specific genes that were 88.5% core, 89 field-biased genes that were 83.1% core, 352 universal genes that were 79.8% core, and 2,083 neutral genes that were 74.5% core. Lab-specific genes were therefore more core than field-specific genes, counter to H1, but the comparison was not statistically significant (Fisher exact OR=0.32, p=0.27). Universal genes were significantly more core than neutral genes (OR=1.35, p=0.033), supporting the interpretation that any strong fitness importance predicts conservation more consistently than whether the condition is classified as field or lab. [^field_vs_lab_fitness]

Logistic regression with 10-fold cross-validated AUC found weak predictive performance for field fitness alone (CV-AUC 0.517, standard deviation 0.052), lab fitness alone (0.531, 0.052), and field plus lab fitness (0.548, 0.053). A full model that also included gene length reached 0.645 (0.068), indicating that gene length was substantially more predictive of core status than either fitness dimension. [^field_vs_lab_fitness]

The conservation pattern was robust across fitness thresholds from -1 to -3. Field-stress genes were 89.4%, 83.6%, 84.0%, and 82.1% core at thresholds -3.0, -2.0, -1.5, and -1.0, respectively; field-core genes were 84.4%, 82.4%, 81.9%, and 79.0%; lab-nutrient genes were 83.5%, 81.4%, 81.0%, and 79.5%; lab-other genes were 85.2%, 81.5%, 80.1%, and 77.5%; lab-antibiotic genes were 82.2%, 73.4%, 77.3%, and 76.2%; and heavy-metals genes were 70.6%, 71.2%, 76.7%, and 76.7%. Field-stress was highest at every threshold, while heavy-metals was consistently lowest; the lab-antibiotic dip at -2 was associated with a sample of n=109 at -2 versus n=45 at -3. [^field_vs_lab_fitness]

### Module-level analysis does not separate field and lab conservation

Across 52 ICA fitness modules, the mean core fraction was 0.886 and the median was 1.000. Module conservation did not significantly correlate with field-condition activity (Spearman rho=0.071, p=0.62). Using the mean core fraction of 0.886 as the classification threshold, 21 ecological modules had a mean core fraction of 0.980, 17 conserved-quiet modules had 0.983, 5 field-variable modules had 0.829, and 9 lab modules had 0.516. The ecological modules contained 239 member genes, including 52 unannotated genes that are candidates for environmental-adaptation functions. [^field_vs_lab_fitness]

The module results did not support H2: field activity and module conservation were not correlated. H3 was partially supported because the 21 field-active, conserved ecological modules were distinguishable from the 9 lower-conservation lab modules, although this classification does not establish that the unannotated genes mediate environmental adaptation. [^field_vs_lab_fitness]

### Biological interpretation

Lab-antibiotic and heavy-metal resistance genes had the lowest conservation values, 73.4% and 71.2%, respectively, compared with the 76.3% all-gene baseline. The report interprets this as consistent with resistance functions being disproportionately accessory and potentially associated with recently acquired mobile genetic elements. In contrast, genes involved in sulfate reduction, lactate/formate/pyruvate utilization, and FRC-relevant stress responses were more conserved, consistent with their importance to DvH ecology; this interpretation is an inference from the conservation pattern rather than a direct mobile-element measurement. [^field_vs_lab_fitness]

The heavy-metals category was treated as field-relevant because DvH encounters those metals at Oak Ridge FRC sites, yet its 71.2% core fraction contrasted with the 83.6% core fraction for uranium/mercury-related field-stress genes. The report suggests the hypothesis that specific metal-resistance mechanisms such as efflux pumps and metal-binding proteins are accessory, whereas uranium and mercury responses may involve more fundamental stress pathways, including DNA repair and sulfate reduction. [^field_vs_lab_fitness]

## Data and Supporting Evidence

The analysis used `kescience_fitnessbrowser` RB-TnSeq data for 757 DvH experiments and 2,741 genes, plus `kbase_ke_pangenome` gene clusters classified as core, auxiliary, or singleton. Generated data included `experiment_classification.csv`, `gene_fitness_conservation.csv` for 2,725 genes, and `module_characterization.csv` for 52 ICA modules. Supporting notebooks covered ENIGMA discovery, condition classification, fitness-conservation analysis, and module analysis. [^field_vs_lab_fitness]

## Caveats

The fitness analysis excludes 678 essential genes, 80.1% of which are core, because they lacked transposon mutants. Including them would raise the overall baseline slightly but would not change condition-class comparisons among non-essential genes. [^field_vs_lab_fitness]

This is a single-organism analysis of DvH, so generalizability is limited, particularly to organisms with larger accessory genomes. The *Nitratidesulfovibrio vulgaris* pangenome contains relatively few genomes, producing a coarse core/auxiliary classification with a high 76.3% baseline core fraction that compresses effect sizes. [^field_vs_lab_fitness]

Condition classification was manually mapped from `condition_1` labels, and edge cases such as zinc sulfate as a metal versus sulfate source required subjective judgment. The primary fitness threshold was < -2, although sensitivity analysis from -1 to -3 supported the reported pattern. [^field_vs_lab_fitness]

Gene length is confounded with both fitness-measurement quality, because short genes receive fewer transposon insertions, and core status, because core genes tend to be longer. The field-specific and lab-specific gene sets were small (n=50-52 per group), limiting power for their comparison. Field and lab fitness effects were correlated (r ~ 0.7 from the scatter plot), so most genes that were sick in one context were also sick in the other. [^field_vs_lab_fitness]

The ENIGMA CORAL field samples and ASVs may enable future community and geochemistry analyses, but the current database survey does not provide DvH gene-level fitness data. Proposed extensions include applying the classification to other ENIGMA organisms with environmental relevance and Fitness Browser data, replacing binary core/auxiliary status with quantitative gene-cluster prevalence, linking ENIGMA community composition to geochemistry, characterizing the genomic context and acquisition history of accessory resistance genes, and using continuous fitness scores in prediction models. [^field_vs_lab_fitness]

## Slots Into

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — field, lab, and stress-condition fitness effects show that fitness importance predicts conservation more strongly than ecological condition class. [^field_vs_lab_fitness]
- [gene-essentiality](../concepts/gene-essentiality.md) — the analysis separates 678 essential genes lacking transposon fitness data from conditionally important non-essential genes and tests condition-dependent importance. [^field_vs_lab_fitness]
- [pangenome-integration](../concepts/pangenome-integration.md) — pangenome core/auxiliary status is integrated with fitness effects, revealing 76.3% baseline core conservation and context-specific enrichment. [^field_vs_lab_fitness]
- [environmental-resistome](../concepts/environmental-resistome.md) — lab-antibiotic and heavy-metal-important genes show low core fractions of 73.4% and 71.2%, motivating analysis of accessory resistance functions. [^field_vs_lab_fitness]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — the ENIGMA CORAL survey establishes that its field geochemistry and community datasets are available for future integration but contain no DvH gene-level fitness data. [^field_vs_lab_fitness]

[^field_vs_lab_fitness]: [field vs lab fitness](../sources/field_vs_lab_fitness__REPORT.md)
