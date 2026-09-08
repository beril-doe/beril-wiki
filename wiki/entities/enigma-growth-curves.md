---
type: Dataset
description: ENIGMA growth curves linking bacterial strains, conditions, and kinetics
sources:
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
title: ENIGMA growth-curve corpus
---
# ENIGMA growth-curve corpus

## What this entity is

The ENIGMA growth-curve corpus is a dataset of bacterial strain-by-condition growth phenotypes and fitted kinetic measurements used to predict phenotype from genome content and growth condition. [^genotype_to_phenotype_enigma]

- **Canonical name:** ENIGMA growth-curve corpus. [^genotype_to_phenotype_enigma]
- **Known aliases:** ENIGMA growth data; ENIGMA growth-curve dataset. [^genotype_to_phenotype_enigma]
- **Stable external identifier:** No stable external identifier is reported in the source document. [^genotype_to_phenotype_enigma]

## Key facts

The corpus contains 27,632 growth curves from 123 strains, 195 molecules, and 303 plates, comprising 7.57M timepoints. [^genotype_to_phenotype_enigma]

Of the 27,632 curves, 15,227 (55.1%) showed no detectable growth, 9,861 (35.7%) were fit-ok, and approximately 9% failed fitting for technical reasons including monotone violations, short duration, and edge-well effects. [^genotype_to_phenotype_enigma]

Modified Gompertz fits for fit-ok curves had median R² = 0.98, median µmax = 0.028 h⁻¹, median lag = 11.4 h, and median asymptotic OD increase A = 0.315. [^genotype_to_phenotype_enigma]

Forty percent of curves showed at least two growth phases in their smoothed derivative. [^genotype_to_phenotype_enigma]

The corpus was integrated with the [enigma-genome-depot](enigma-genome-depot.md), [kescience-fitnessbrowser](kescience-fitnessbrowser.md), [web-of-microbes](web-of-microbes.md), [carbon-source-phenotypes](carbon-source-phenotypes.md), pangenome data, and global [16s-amplicon-sequencing](16s-amplicon-sequencing.md) environmental data. [^genotype_to_phenotype_enigma]

The integrated modeling corpus contains 46,389 genome × condition pairs from 727 genomes and 363 conditions, with 4,293 shared [kegg](kegg.md) orthologs. [^genotype_to_phenotype_enigma]

The ENIGMA growth data align with Fitness Browser data through 486 strain × condition anchor pairs covering 7 strains and 72 conditions; 275 pairs (56.6%) showed measurable growth. [^genotype_to_phenotype_enigma]

Five conditions—cytidine, glycine, inosine, thymidine, and uridine—occur in all four aligned datasets, while 30 conditions occur in three datasets. [^genotype_to_phenotype_enigma]

## Analytical use

The corpus distinguishes prediction of binary growth capability from prediction of continuous kinetics: binary growth was predictable for some condition classes, whereas continuous µmax, lag, and yield-related max_A were not predictable under genus-blocked holdout from KO presence/absence or bulk genomic features. [^genotype_to_phenotype_enigma]

In the full-corpus model, binary-growth AUC was 0.620 across 46,389 pairs; adding KO × condition interaction features increased mean AUC to 0.653, an improvement of 0.032, with improvement in 80 of 106 held-out genera. [^genotype_to_phenotype_enigma]

Across 343 individually testable conditions, 95 achieved AUC > 0.75; the best individual conditions were tryptophan (0.933), phenylalanine (0.932), valine (0.927), mannose (0.904), and galactose (0.895). [^genotype_to_phenotype_enigma]

The corpus supports the hypothesis that gene content more reliably encodes whether an organism can use a substrate than the rate of growth, which also depends on enzyme kinetics, expression, regulatory context, and ribosome efficiency. [^genotype_to_phenotype_enigma]

## Related pages

- [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md) — source-project summary describing the corpus, integrations, modeling results, and limitations. [^genotype_to_phenotype_enigma]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — connects condition-specific growth capability with fitness prediction and kinetic limitations. [^genotype_to_phenotype_enigma]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — places the growth curves within the integrated phenotype, genome, fitness, exometabolomics, and environmental-data workflow. [^genotype_to_phenotype_enigma]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — relates the corpus scale to the shift from genome-scale proxies toward substrate-specific predictors. [^genotype_to_phenotype_enigma]
- [enigma-genome-depot](enigma-genome-depot.md) — genome resource integrated with the growth-curve corpus. [^genotype_to_phenotype_enigma]
- [kescience-fitnessbrowser](kescience-fitnessbrowser.md) — source of aligned RB-TnSeq fitness measurements. [^genotype_to_phenotype_enigma]
- [web-of-microbes](web-of-microbes.md) — source of integrated exometabolomics data. [^genotype_to_phenotype_enigma]
- [carbon-source-phenotypes](carbon-source-phenotypes.md) — complementary strain-by-condition phenotype corpus. [^genotype_to_phenotype_enigma]

[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
