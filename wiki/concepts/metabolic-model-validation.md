---
type: "Concept"
description: "Empirical tests expose condition-dependent limits in metabolic-model predictions."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md"]
---
# Empirical validation reveals condition-dependent limits of metabolic-model predictions

Metabolic-model predictions in the *Acinetobacter baylyi* ADP1 database are constrained by growth condition, incomplete gene coverage, and reliance on gapfilled reactions. [src: acinetobacter_adp1_explorer] This page links the empirical comparison to [[summaries/acinetobacter_adp1_explorer__REPORT]], [[concepts/metabolic-model-gapfilling]], [[concepts/gene-essentiality]], and [[concepts/condition-specific-fitness]]. [src: acinetobacter_adp1_explorer]

## FBA–TnSeq agreement is substantial but incomplete

Flux balance analysis (FBA), a constraint-based method that predicts metabolic flux distributions, and TnSeq essentiality calls could be compared for 866 genes. [src: acinetobacter_adp1_explorer] The two approaches were concordant for 639 genes, or 73.8%, while 227 genes were discordant. [src: acinetobacter_adp1_explorer] This **supports** using empirical essentiality measurements as a validation layer for metabolic models, while the 227 discordant genes identify a defined set of cases where model predictions and mutant phenotypes diverge. [src: acinetobacter_adp1_explorer]

The discordant genes may reflect metabolic-model deficiencies or regulatory effects that are not represented by FBA, so they are candidates for model refinement rather than evidence that either method is universally correct. [src: acinetobacter_adp1_explorer] Because FBA data covered only 15% of genes and the comparison involved 866 genes, the concordance estimate is limited to the measured subset. [src: acinetobacter_adp1_explorer]

## Validation depends on growth condition

Essentiality calls differed between media: 499 genes were essential on minimal media, compared with 346 on LB. [src: acinetobacter_adp1_explorer] This **supports** the interpretation that minimal-media growth imposes an additional biosynthetic burden and that a model validated under one condition should not automatically be treated as validated under another. [src: acinetobacter_adp1_explorer]

FBA flux classes changed between rich and minimal media for 177 of 866 genes, or 20%. [src: acinetobacter_adp1_explorer] This **refines** the model-validation problem from a single accuracy comparison into a condition-specific test of whether predicted metabolic states track experimentally observed changes. [src: acinetobacter_adp1_explorer]

## Gapfilling is a major source of prediction dependence

Across 14 genomes, 1,330 unique metabolic reactions were assessed; 1,248, or 94%, were shared across all 14 genomes and classified as core, while 62 were variable and 20 were genome-unique. [src: acinetobacter_adp1_explorer] Gapfilling accounted for 7.7% of reactions on average, and 243 missing functions were cataloged. [src: acinetobacter_adp1_explorer]

Of 121,519 growth phenotype predictions, 105,376, or 87%, required at least one gapfilled reaction. [src: acinetobacter_adp1_explorer] This **supports** [[concepts/metabolic-model-gapfilling]] by showing that prediction performance is tightly coupled to the quality of inferred reactions rather than only to experimentally supported metabolism. [src: acinetobacter_adp1_explorer] False negatives had higher mean gap counts than correct predictions, providing an empirical signal that extensive gapfilling can be associated with unreliable phenotype predictions. [src: acinetobacter_adp1_explorer]

The 87% dependence on gapfilled reactions limits interpretation of the growth predictions because missing genomic evidence and inferred reactions are entangled in the prediction process. [src: acinetobacter_adp1_explorer] The 243 missing functions therefore represent specific targets for improving model evidence and testing whether revised reactions reduce false negatives. [src: acinetobacter_adp1_explorer]

## Implications for integrated validation

The ADP1 database combines TnSeq essentiality, FBA, mutant growth fitness, proteomics, pangenome classification, and functional annotations, but no gene had measurements across all six modalities. [src: acinetobacter_adp1_explorer] This **supports** [[concepts/multi-omics-integration]] as a validation strategy while also showing that empirical confirmation is necessarily partial when modality coverage is incomplete. [src: acinetobacter_adp1_explorer]

Carbon-source mutant fitness further indicates that validation should include multiple environments: mean pairwise fitness correlation across eight carbon sources was 0.44, urea fitness was nearly uncorrelated with quinate at r = 0.11, and butanediol-acetate and butanediol-lactate had the strongest correlations at r = 0.58 and r = 0.53, respectively. [src: acinetobacter_adp1_explorer] These results **support** [[concepts/condition-specific-fitness]] by showing that phenotype measurements can expose condition-specific gene requirements that a single metabolic condition may miss. [src: acinetobacter_adp1_explorer]

## Open Directions

- Use the 227 FBA–TnSeq-discordant genes with pathway enrichment and targeted inspection of regulatory annotations to ask whether discordance is concentrated in particular metabolic functions or reflects regulatory effects absent from the model. [src: acinetobacter_adp1_explorer]
- Refit and revalidate the ADP1 metabolic model separately on minimal media and LB using the 499-versus-346 essentiality calls and the 177 of 866 flux-class changes to ask which condition-specific constraints improve prediction agreement. [src: acinetobacter_adp1_explorer]
- Reassess the 121,519 growth phenotype predictions after removing or ranking the 243 missing functions by pangenome support, then test whether gapfill confidence reduces the false-negative excess associated with higher mean gap counts. [src: acinetobacter_adp1_explorer]
- Compare predictions across the eight carbon-source fitness conditions, prioritizing urea versus quinate and butanediol-acetate versus butanediol-lactate, to ask whether condition-specific mutant fitness can identify missing model reactions. [src: acinetobacter_adp1_explorer]
