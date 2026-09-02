---
type: "Dataset"
description: "ENIGMA growth curves linking bacterial strains, conditions, and kinetics"
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# ENIGMA growth-curve corpus

## What this entity is

The ENIGMA growth-curve corpus is a dataset of bacterial strain-by-condition growth phenotypes and fitted kinetic measurements used to predict phenotype from genome content and growth condition. [src: genotype_to_phenotype_enigma]

- **Canonical name:** ENIGMA growth-curve corpus. [src: genotype_to_phenotype_enigma]
- **Known aliases:** ENIGMA growth data; ENIGMA growth-curve dataset. [src: genotype_to_phenotype_enigma]
- **Stable external identifier:** No stable external identifier is reported in the source document. [src: genotype_to_phenotype_enigma]

## Key facts

The corpus contains 27,632 growth curves from 123 strains, 195 molecules, and 303 plates, comprising 7.57M timepoints. [src: genotype_to_phenotype_enigma]

Of the 27,632 curves, 15,227 (55.1%) showed no detectable growth, 9,861 (35.7%) were fit-ok, and approximately 9% failed fitting for technical reasons including monotone violations, short duration, and edge-well effects. [src: genotype_to_phenotype_enigma]

Modified Gompertz fits for fit-ok curves had median R² = 0.98, median µmax = 0.028 h⁻¹, median lag = 11.4 h, and median asymptotic OD increase A = 0.315. [src: genotype_to_phenotype_enigma]

Forty percent of curves showed at least two growth phases in their smoothed derivative. [src: genotype_to_phenotype_enigma]

The corpus was integrated with the [[entities/enigma-genome-depot]], [[entities/kescience-fitnessbrowser]], [[entities/web-of-microbes]], [[entities/carbon-source-phenotypes]], pangenome data, and global [[entities/16s-amplicon-sequencing]] environmental data. [src: genotype_to_phenotype_enigma]

The integrated modeling corpus contains 46,389 genome × condition pairs from 727 genomes and 363 conditions, with 4,293 shared [[entities/kegg]] orthologs. [src: genotype_to_phenotype_enigma]

The ENIGMA growth data align with Fitness Browser data through 486 strain × condition anchor pairs covering 7 strains and 72 conditions; 275 pairs (56.6%) showed measurable growth. [src: genotype_to_phenotype_enigma]

Five conditions—cytidine, glycine, inosine, thymidine, and uridine—occur in all four aligned datasets, while 30 conditions occur in three datasets. [src: genotype_to_phenotype_enigma]

## Analytical use

The corpus distinguishes prediction of binary growth capability from prediction of continuous kinetics: binary growth was predictable for some condition classes, whereas continuous µmax, lag, and yield-related max_A were not predictable under genus-blocked holdout from KO presence/absence or bulk genomic features. [src: genotype_to_phenotype_enigma]

In the full-corpus model, binary-growth AUC was 0.620 across 46,389 pairs; adding KO × condition interaction features increased mean AUC to 0.653, an improvement of 0.032, with improvement in 80 of 106 held-out genera. [src: genotype_to_phenotype_enigma]

Across 343 individually testable conditions, 95 achieved AUC > 0.75; the best individual conditions were tryptophan (0.933), phenylalanine (0.932), valine (0.927), mannose (0.904), and galactose (0.895). [src: genotype_to_phenotype_enigma]

The corpus supports the hypothesis that gene content more reliably encodes whether an organism can use a substrate than the rate of growth, which also depends on enzyme kinetics, expression, regulatory context, and ribosome efficiency. [src: genotype_to_phenotype_enigma]

## Related pages

- [[summaries/genotype_to_phenotype_enigma__REPORT]] — source-project summary describing the corpus, integrations, modeling results, and limitations. [src: genotype_to_phenotype_enigma]
- [[concepts/condition-specific-fitness]] — connects condition-specific growth capability with fitness prediction and kinetic limitations. [src: genotype_to_phenotype_enigma]
- [[concepts/multi-omics-integration]] — places the growth curves within the integrated phenotype, genome, fitness, exometabolomics, and environmental-data workflow. [src: genotype_to_phenotype_enigma]
- [[concepts/gene-function-acquisition-depth]] — relates the corpus scale to the shift from genome-scale proxies toward substrate-specific predictors. [src: genotype_to_phenotype_enigma]
- [[entities/enigma-genome-depot]] — genome resource integrated with the growth-curve corpus. [src: genotype_to_phenotype_enigma]
- [[entities/kescience-fitnessbrowser]] — source of aligned RB-TnSeq fitness measurements. [src: genotype_to_phenotype_enigma]
- [[entities/web-of-microbes]] — source of integrated exometabolomics data. [src: genotype_to_phenotype_enigma]
- [[entities/carbon-source-phenotypes]] — complementary strain-by-condition phenotype corpus. [src: genotype_to_phenotype_enigma]
