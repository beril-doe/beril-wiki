---
type: "Concept"
description: "How gene length can distort fitness-based prediction of pangenome conservation"
sources: ["summaries/field_vs_lab_fitness__REPORT.md"]
---
# Gene length confounds fitness-based prediction of pangenome conservation

Gene length is a major confounder when using experimental fitness effects to predict whether a gene is conserved in a pangenome, because length affects both the reliability of transposon-fitness measurement and the probability that a gene is classified as core. [src: field_vs_lab_fitness] This means that an apparent relationship between fitness importance and conservation should not be interpreted as independent of gene length unless models explicitly control for it. [src: field_vs_lab_fitness]

## Key evidence

The analysis combined RB-TnSeq (random barcode transposon sequencing) fitness data from 757 *Desulfovibrio vulgaris* Hildenborough experiments with pangenome classifications for 2,725 non-essential genes that had both fitness measurements and pangenome links. [src: field_vs_lab_fitness] Of these genes, 76.3% were classified as core, establishing the baseline against which condition-specific conservation was compared. [src: field_vs_lab_fitness]

Models using field fitness alone had a cross-validated area under the receiver operating characteristic curve (CV-AUC) of 0.517 with standard deviation 0.052, while lab fitness alone reached 0.531 with standard deviation 0.052. [src: field_vs_lab_fitness] Combining field and lab fitness increased performance only to 0.548 with standard deviation 0.053. [src: field_vs_lab_fitness] Adding gene length increased the full-model CV-AUC to 0.645 with standard deviation 0.068, making gene length substantially more predictive of core status than either fitness dimension alone. [src: field_vs_lab_fitness]

This result supports [[concepts/condition-specific-fitness]] by showing that the predictive value of measured fitness is limited when conservation is modeled without accounting for gene-level structural covariates. [src: field_vs_lab_fitness] It also refines [[concepts/pangenome-integration]] because integrating fitness with core/auxiliary status requires adjustment for gene length rather than treating fitness as the sole explanatory variable. [src: field_vs_lab_fitness]

## Why the confounding arises

Short genes receive fewer transposon insertions, which can reduce the quality and stability of their fitness estimates. [src: field_vs_lab_fitness] Core genes also tend to be longer, so gene length is associated with the outcome being predicted as well as with the measurement process. [src: field_vs_lab_fitness] The resulting association can make gene length appear to explain conservation directly even when part of its predictive value reflects better fitness callability or other correlated genomic properties. [src: field_vs_lab_fitness]

The exclusion of 678 essential genes further limits interpretation of the fitness models because these genes lacked recovered transposon mutants and therefore had no condition-specific fitness data. [src: field_vs_lab_fitness] Those excluded essential genes were 80.1% core, compared with the 76.3% core fraction among the 2,725 non-essential genes analyzed with fitness and pangenome data. [src: field_vs_lab_fitness] Consequently, the reported AUC values describe prediction among genes with usable non-essential-gene fitness measurements, not prediction across the complete pangenome. [src: field_vs_lab_fitness] This limitation connects the concept to [[concepts/gene-essentiality]], where absence of perturbation data is itself informative rather than random. [src: field_vs_lab_fitness]

## Interpretation and scope

The weak performance of field and lab fitness alone indicates that ecological condition class is not sufficient to predict pangenome conservation in this dataset. [src: field_vs_lab_fitness] The stronger performance of the model containing gene length indicates that measurement and genomic-architecture effects must be separated from biological fitness effects before claiming that fitness importance predicts conservation. [src: field_vs_lab_fitness] This is a single-organism result from *Desulfovibrio vulgaris* Hildenborough, and its generalizability to organisms with larger accessory genomes has not been established. [src: field_vs_lab_fitness]

The analysis also found that field and lab fitness effects were correlated at approximately r ~ 0.7, so genes that were deleterious in one context were often deleterious in the other. [src: field_vs_lab_fitness] This correlation reduces the ability of separate field and lab fitness dimensions to distinguish ecological context, making adjustment for gene length especially important when comparing their predictive contributions. [src: field_vs_lab_fitness] The relevant inferential issue is therefore related to [[concepts/statistical-significance-versus-effect-size]]: the full-model performance difference is a predictive effect, but it does not by itself establish a causal role for gene length in evolutionary conservation. [src: field_vs_lab_fitness]

## Open Directions

- Use the `gene_fitness_conservation.csv` data for the 2,725 analyzed genes, together with insertion counts or other transposon-callability measures, in nested cross-validated models to test how much of gene length's CV-AUC 0.645 contribution remains after measurement quality is modeled explicitly. [src: field_vs_lab_fitness]
- Add the 678 essential genes through a missing-fitness or two-stage model, then test whether gene length predicts core status similarly among essential genes and genes with recovered transposon mutants. [src: field_vs_lab_fitness]
- Replace binary core/auxiliary labels with quantitative gene-cluster prevalence and fit length-adjusted regression models to ask whether gene length primarily predicts the core boundary or also predicts intermediate prevalence across the pangenome. [src: field_vs_lab_fitness]
- Reanalyze fitness across the reported thresholds from -1 to -3 with gene length, insertion coverage, and fitness uncertainty as covariates to test whether length confounding changes condition-specific conservation patterns. [src: field_vs_lab_fitness]
