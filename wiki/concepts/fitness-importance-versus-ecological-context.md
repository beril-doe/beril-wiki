---
type: "Concept"
description: "Fitness importance explains conservation better than field-versus-lab context"
sources: ["summaries/field_vs_lab_fitness__REPORT.md"]
---
# Fitness importance predicts genome conservation more strongly than field-versus-lab context

## Core claim

In *Desulfovibrio vulgaris* Hildenborough (DvH), strong fitness importance was more consistently associated with genome conservation than whether a condition was classified as field or laboratory. [src: field_vs_lab_fitness] This conclusion is based on 757 Fitness Browser experiments, 2,725 non-essential genes with both fitness data and pangenome links, and 52 independent component analysis (ICA) fitness modules. [src: field_vs_lab_fitness] The source analysis is summarized at [[summaries/field_vs_lab_fitness__REPORT]].

## Evidence from condition classes

Among genes with fitness below -2, field-stress genes had the highest core-genome fraction at 83.6% across 298 genes (OR=1.58 versus baseline, FDR q=0.026), followed by field-core genes at 82.4% across 376 genes (OR=1.46, q=0.026), lab-other genes at 81.5% across 292 genes (OR=1.37, q=0.073), and lab-nutrient genes at 81.4% across 452 genes (OR=1.36, q=0.037). [src: field_vs_lab_fitness] FDR means false discovery rate, and the reported q values were calculated after Benjamini–Hochberg correction. [src: field_vs_lab_fitness]

This **supports** [[concepts/condition-specific-fitness]] by showing that condition-specific fitness effects can be connected to pangenome conservation, but it **refines** that relationship: field classification did not consistently outperform laboratory classification as a predictor of conservation. [src: field_vs_lab_fitness] Lab-antibiotic genes were 73.4% core across 109 genes (OR=0.86, q=0.49), while heavy-metal genes were 71.2% core across 198 genes (OR=0.77, q=0.14), indicating lower conservation than the 76.3% baseline for all analyzed non-essential genes but no statistically significant depletion after correction. [src: field_vs_lab_fitness]

The ranking was stable across fitness thresholds from -1 to -3: field-stress genes were 89.4%, 83.6%, 84.0%, and 82.1% core at thresholds -3.0, -2.0, -1.5, and -1.0, respectively, while heavy-metal genes were 70.6%, 71.2%, 76.7%, and 76.7% core at those same thresholds. [src: field_vs_lab_fitness] Field-stress was highest at every tested threshold, whereas heavy-metals was consistently lowest. [src: field_vs_lab_fitness]

## Evidence from specificity and prediction

The specificity analysis found 50 lab-specific genes that were 96.0% core, 52 field-specific genes that were 88.5% core, 89 field-biased genes that were 83.1% core, 352 universal genes that were 79.8% core, and 2,083 neutral genes that were 74.5% core. [src: field_vs_lab_fitness] Universal genes were significantly more core than neutral genes (OR=1.35, p=0.033), whereas the difference between lab-specific and field-specific genes was not statistically significant (Fisher exact OR=0.32, p=0.27). [src: field_vs_lab_fitness] These results **support** the interpretation that repeated or strong fitness importance predicts conservation more reliably than the field-versus-lab label. [src: field_vs_lab_fitness]

Logistic regression with 10-fold cross-validated area under the receiver operating characteristic curve (CV-AUC) produced weak performance for field fitness alone (0.517, standard deviation 0.052), lab fitness alone (0.531, 0.052), and field plus lab fitness (0.548, 0.053). [src: field_vs_lab_fitness] Adding gene length increased performance to 0.645 (0.068), indicating that gene length was more predictive of core status than either fitness dimension in this model. [src: field_vs_lab_fitness] This result **refines** [[concepts/pangenome-integration]] by showing that integrating fitness and pangenome status does not make ecological context alone a strong conservation predictor. [src: field_vs_lab_fitness]

## Module-level evidence

Across 52 ICA fitness modules, the mean core fraction was 0.886 and the median was 1.000. [src: field_vs_lab_fitness] Module conservation was not significantly correlated with field-condition activity (Spearman rho=0.071, p=0.62). [src: field_vs_lab_fitness] Using 0.886 as the classification threshold, 21 ecological modules had a mean core fraction of 0.980, 17 conserved-quiet modules had 0.983, 5 field-variable modules had 0.829, and 9 lab modules had 0.516. [src: field_vs_lab_fitness]

The module results did not support the hypothesis that field activity predicts module conservation. [src: field_vs_lab_fitness] They did, however, distinguish 21 field-active, conserved ecological modules from 9 lower-conservation lab modules, although this classification does not establish that the 52 unannotated genes among the 239 ecological-module members mediate environmental adaptation. [src: field_vs_lab_fitness] The unannotated module genes therefore provide candidates for testing, not confirmed ecological determinants. [src: field_vs_lab_fitness]

## Interpretation and boundaries

The analysis **supports** [[concepts/adaptive-versus-housekeeping-functional-differentiation]] insofar as broadly important genes were more conserved, but it does not establish that field-associated genes are generally more conserved than laboratory-associated genes. [src: field_vs_lab_fitness] Field and lab fitness effects were correlated at approximately r ~ 0.7 from the scatter plot, so most genes that were sick in one context were also sick in the other. [src: field_vs_lab_fitness]

The low conservation of lab-antibiotic and heavy-metal-important genes is consistent with resistance functions being disproportionately accessory and potentially associated with recently acquired mobile genetic elements, but the analysis did not directly measure mobile-element association. [src: field_vs_lab_fitness] The report therefore suggests the hypothesis that specific metal-resistance mechanisms such as efflux pumps and metal-binding proteins are accessory, whereas uranium and mercury responses may involve more fundamental stress pathways, including DNA repair and sulfate reduction. [src: field_vs_lab_fitness] This interpretation connects to [[concepts/environmental-resistome]] and [[concepts/metal-cross-resistance]] without establishing a causal mechanism for the observed conservation differences. [src: field_vs_lab_fitness]

The result is limited to a single-organism analysis of DvH, whose pangenome contains relatively few genomes and has a 76.3% baseline core fraction among the analyzed non-essential genes. [src: field_vs_lab_fitness] Fitness comparisons also excluded 678 essential genes, 80.1% of which were core, because no transposon mutants were recovered. [src: field_vs_lab_fitness] Gene length is confounded with both fitness-measurement quality, because short genes receive fewer transposon insertions, and core status, because core genes tend to be longer. [src: field_vs_lab_fitness] The field-specific and lab-specific gene sets were small, with n=50–52 per group, limiting statistical power for their comparison. [src: field_vs_lab_fitness]

## Relation to existing concepts

- This **supports and qualifies** [[concepts/condition-specific-fitness]]: condition-specific importance is informative, but condition category adds little predictive value beyond fitness importance. [src: field_vs_lab_fitness]
- This **extends** [[concepts/pangenome-integration]]: fitness effects and core/auxiliary status can be integrated, while gene length remains a stronger predictor in the reported model. [src: field_vs_lab_fitness]
- This **supports** [[concepts/gene-essentiality]]: essential genes were largely core but were absent from the transposon fitness comparison, separating constitutive essentiality from measured conditional importance. [src: field_vs_lab_fitness]
- This **refines** [[concepts/environmental-resistome]]: resistance-associated fitness importance can occur in relatively unconserved, accessory portions of the DvH pangenome. [src: field_vs_lab_fitness]

## Open Directions

- Use Fitness Browser experiments and quantitative gene-cluster prevalence across additional environmentally relevant organisms to test whether the weak field-versus-lab effect generalizes beyond DvH. [src: field_vs_lab_fitness]
- Add the 678 essential genes through an essentiality-aware model and test whether including their 80.1% core fraction changes the comparison between conditional fitness and conservation. [src: field_vs_lab_fitness]
- Fit continuous-fitness prediction models with gene length, transposon insertion coverage, and pangenome prevalence to determine whether continuous fitness improves on the reported CV-AUC values of 0.517, 0.531, and 0.548. [src: field_vs_lab_fitness]
- Combine genomic-context analyses with resistance-gene calls to test whether the 73.4% core fraction for lab-antibiotic genes and 71.2% for heavy-metal genes is associated with mobile genetic elements. [src: field_vs_lab_fitness]
- Reanalyze the 52 ICA modules using functional annotation and environmental metadata to test whether the 52 unannotated genes in ecological modules mediate adaptation rather than merely co-varying with conserved genes. [src: field_vs_lab_fitness]
- Link the 4,346 ENIGMA CORAL field samples with geochemistry and 213,044 ASVs to test ecological associations for DvH or other organisms with both environmental data and gene-level fitness measurements. [src: field_vs_lab_fitness]
