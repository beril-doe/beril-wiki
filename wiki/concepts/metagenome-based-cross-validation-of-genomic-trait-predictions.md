---
type: "Concept"
description: "Using abundance-weighted genus-level trait prevalence to infer community traits in metagenomes and correlating them with abiotic variables; stops at inference-level evidence."
sources: ["summaries/functional_dark_matter__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
---
# Metagenome-based cross-validation of genomic trait predictions

This page covers metagenome-based cross-validation of genomic trait predictions. Abundance-weighted genus-level trait prevalence gives an inferred community trait, which is correlated with abiotic variables in metagenomes. In the functional_dark_matter project, all 4 testable pre-registered abiotic predictions were confirmed in NMDC (National Microbiome Data Collaborative) samples. [src: functional_dark_matter] In the PHB project, inferred PHB capacity showed small but significant abiotic correlations. [src: phb_granule_ecology] The prophage_ecology project applied the same taxonomy-based inference to prophage burden across 6,365 NMDC samples and found 57 significant module-abiotic correlations. [src: prophage_ecology] The evidence stops at inference: the functional_dark_matter report says compositional coupling inflates its NMDC signal [src: functional_dark_matter], and its trait correlations show co-occurrence, not causation. [src: functional_dark_matter] See also [[concepts/compositional-coupling-in-metagenomic-validation-of-carrier-abundance]] and [[entities/nmdc-integrated-collections]].

## Literature Context

The candidate papers show that linking taxonomy or marker genes to community function in environmental samples is common, but they offer only indirect support for the hub's specific method. That method infers a community trait from abundance-weighted genus-level prevalence and correlates it with abiotic variables in metagenomes. A global soil metagenomic study reports that taxonomic composition varies widely with climate and soil physicochemical gradients, while functional potentials based on metagenomic gene abundances are redundant [PMID 35586865](https://pubmed.ncbi.nlm.nih.gov/35586865/). If function is more conserved than taxonomy, a trait inferred from genus identity may not track community function evenly across sites. That bears on the genus-level conservation assumption the prophage_ecology report flags.

Several papers support the broader idea that environmental gradients shape traits at the genus or community level. In a Southern California reciprocal transplant experiment, site significantly affected Sphingomonas functional composition (R2 = 0.465) and clade composition (R2 = 0.400) (PERMANOVA, P < 0.001) [PMID 38572990](https://pubmed.ncbi.nlm.nih.gov/38572990/). A 25-site grassland nutrient-addition experiment found that N and P additions shifted bacterial life-history strategies, decreasing average genome size and raising copiotroph abundance. The metagenomes came from only a subset of sites [PMID 26283343](https://pubmed.ncbi.nlm.nih.gov/26283343/). Along an elevation gradient, phosphorus-cycling gene composition tracked pH, organic carbon and phosphate [PMID 41334926](https://pubmed.ncbi.nlm.nih.gov/41334926/). A study of Indian solar salterns reported salinity as a dominant filter on taxonomic and functional composition across four sites [PMID 42321634](https://pubmed.ncbi.nlm.nih.gov/42321634/). A SAR324 metapangenome showed depth-dependent differences in metabolic potential among ecotypes [PMID 34389059](https://pubmed.ncbi.nlm.nih.gov/34389059/). The depth result is the closest analogue to the PHB depth correlation (rho = -0.119) in the hub, though it concerns one marine lineage and not an abundance-weighted trait score.

The mining-stream study is a caution about inference. It predicted function from amplicon data with PICRUSt2, and it found that metal concentration structured bacteria, archaea and fungi [PMID 41539526](https://pubmed.ncbi.nlm.nih.gov/41539526/). Its authors read the greater stability of archaeal and fungal communities as indicating potential functional redundancy. Trait inference from taxonomy is also used outside the hub's setting. A bioreactor study used genome-resolved metagenomics to assign life-history strategies to communities under disturbance [PMID 42023670](https://pubmed.ncbi.nlm.nih.gov/42023670/).

The corpus findings are consistent with this literature in direction. Taxonomy and environment covary, and genomic traits shift along gradients. The hub's PHB and prophage correlations fit that pattern, with the modest PHB effects (|rho| < 0.12) and the pH and temperature predictors for prophage burden. They extend the literature by testing pre-registered predictions in NMDC, where all 4 testable abiotic predictions were confirmed. None of the candidates tested compositional coupling directly. The functional_dark_matter report's caution that coupling inflates its NMDC signal is therefore novel relative to these papers and remains unresolved by them. The redundancy finding in [PMID 35586865](https://pubmed.ncbi.nlm.nih.gov/35586865/) is a mild tension. It suggests that genus-level inference could overstate functional differences. None of these papers validates genus-level prophage inference, so the hub's caveat stands.

## Pre-registered abiotic predictions

All 4 testable pre-registered abiotic predictions were confirmed in NMDC. [src: functional_dark_matter] The report calls these independent confirmations, because the NMDC metagenomic samples are entirely separate from the pangenome-based carrier analysis. [src: functional_dark_matter] They were also presented as independent validation of the report's lab-field concordance. [src: functional_dark_matter] Results (FDR is false discovery rate):

| Carrier class | Abiotic variable | Spearman rho | n | FDR |
|---|---|---|---|---|
| nitrogen source | total nitrogen content | +0.109 | 1,231 | 2.3e-4 [src: functional_dark_matter] |
| nitrogen source | ammonium nitrogen | +0.231 | 1,230 | 8.0e-16 [src: functional_dark_matter] |
| pH phenotype | pH | +0.157 | 4,366 | 7.4e-25 [src: functional_dark_matter] |
| anaerobic | dissolved oxygen | -0.298 | 272 | 1.5e-6 [src: functional_dark_matter] |

Beyond these, 76 of 105 total Spearman tests reached FDR < 0.05 (72.4%). [src: functional_dark_matter] The report says this high rate likely reflects confounding, because the carrier genera (Pseudomonas, Klebsiella, Bacteroides) are abundant and ubiquitous and correlate broadly with abiotic variables. [src: functional_dark_matter] It treats the 4/4 directional rate as the more meaningful metric. [src: functional_dark_matter] The NMDC correlations give community-level corroboration across 6,365 metagenomic samples. [src: functional_dark_matter]

## Trait-condition predictions

All 7 pre-registered trait-condition predictions were confirmed at FDR < 10⁻²¹. [src: functional_dark_matter] Nitrogen-source carriers correlated with nitrogen_fixation (ρ=0.60) [src: functional_dark_matter] and nitrate_denitrification (ρ=0.52). [src: functional_dark_matter] Carbon-source carriers correlated with aerobic_chemoheterotrophy (ρ=0.73) [src: functional_dark_matter] and fermentation (ρ=0.59). [src: functional_dark_matter] Anaerobic carriers correlated with fermentation (ρ=0.59) [src: functional_dark_matter] and iron_respiration (ρ=0.45). [src: functional_dark_matter] A further 441/449 exploratory tests reached FDR < 0.05. [src: functional_dark_matter]

The report cautions that these correlations likely reflect compositional coupling. Genera abundant in a sample contribute to both the carrier abundance and the community trait score, so this is not independent gene-phenotype validation. [src: functional_dark_matter] It states that coupling inflates the NMDC signal. [src: functional_dark_matter] The correlations show ecological co-occurrence, not causal gene-phenotype links. [src: functional_dark_matter]

Partial null approximations quantify the problem:
- A sign test on 7/7 trait directions gives p = 0.0078. [src: functional_dark_matter]
- A sign test on 4/4 abiotic directions gives p = 0.0625. [src: functional_dark_matter]
- Fisher's combined probability across all 11 pre-registered tests gives p ≈ 0. [src: functional_dark_matter]
- The exploratory tests show an inflation factor of ~20× (441/449 significant vs. 22.5 expected). [src: functional_dark_matter]

## Polyhydroxybutyrate (PHB) capacity in NMDC

PHB capacity was inferred for 6,365 NMDC samples as the abundance-weighted sum of genus-level phaC prevalence. A median 87.2% of taxonomic abundance was matched to pangenome genera. [src: phb_granule_ecology] A two-tier taxonomy mapping covered 3,014/3,492 (86.3%) of NMDC taxon columns. [src: phb_granule_ecology] Tier 1 used a gtdb_metadata NCBI taxid bridge for 2,336 columns. Tier 2 used direct genus matching through taxonomy_dim for 678 more columns. [src: phb_granule_ecology]

Inferred PHB capacity showed small abiotic correlations (Spearman):
- depth: rho = -0.119, p = 1.14 x 10^-21 [src: phb_granule_ecology]
- temperature: rho = +0.088, p = 1.86 x 10^-12 [src: phb_granule_ecology]
- maximum depth: rho = +0.076, p = 1.15 x 10^-9 [src: phb_granule_ecology]
- minimum depth: rho = -0.055, p = 1.05 x 10^-5 [src: phb_granule_ecology]
- pH: rho = +0.049, p = 7.95 x 10^-5 [src: phb_granule_ecology]
- ammonium nitrogen: rho = +0.044, p = 4.49 x 10^-4 [src: phb_granule_ecology]

The report reads the depth result as consistent with the feast/famine hypothesis, since surface environments have more variable carbon inputs. [src: phb_granule_ecology] It reads the temperature result as consistent with higher metabolic turnover in warmer environments. [src: phb_granule_ecology]

A genus-level check in NB05 was stronger. Of 693 matched genera, PHB-high genera (>=50% phaC prevalence) were more abundant in NMDC than PHB-low genera (Mann-Whitney p = 8.41 x 10^-22). [src: phb_granule_ecology] Top PHB-high genera by NMDC abundance were Mycobacterium, Pseudomonas, Cupriavidus, Burkholderia and Methylobacterium, all described as well-characterized PHB producers. [src: phb_granule_ecology]

## Prophage burden in NMDC

The prophage_ecology project used taxonomy-based inference of prophage burden across 6,365 NMDC metagenomic samples, with 87.2% median matching coverage. It found 57 significant module-abiotic correlations (FDR < 0.05). [src: prophage_ecology] The report marks its hypothesis H1d (NMDC prophage burden correlates with abiotic variables) as supported, with pH and temperature the strongest predictors. [src: prophage_ecology] Cross-validation with pangenome results confirmed concordance for prophage modules B, C, and G. [src: prophage_ecology] Two caveats limit this. The inference assumes genus-level conservation of prophage content, which may fail for recently acquired or lost prophages. [src: prophage_ecology] The approach was validated for the PHB granule ecology project but has not been independently validated for prophage genes. [src: prophage_ecology]

## Other abundance-weighted community metrics

A related approach computed a community weighted mean (CWM) of genus-level metal-type diversity, weighted by OTU (operational taxonomic unit) abundance. It used OTUs with antimicrobial resistance data, which covered 16.8% of reads per sample on average in PRJNA1084851. [src: microbeatlas_metal_ecology] That CWM correlated with time point (ρ = +0.383, n = 133, p < 0.0001). [src: microbeatlas_metal_ecology] In ENIGMA Track B it was higher in contamination-plume wells FW215/FW216 (Kruskal-Wallis p = 0.0001). [src: microbeatlas_metal_ecology]

## Caveats

- PHB effect sizes are modest (|rho| < 0.12). [src: phb_granule_ecology] The report suggests this is likely because NMDC abiotic values are point-in-time snapshots, not measures of temporal variability. [src: phb_granule_ecology]
- NMDC studies are biased toward terrestrial/soil environments. [src: phb_granule_ecology]
- The pangenome includes complete genomes and MAGs (metagenome assembled genomes), which may differ in gene detection rates. [src: phb_granule_ecology]
- Genus-level inference of prophage burden is unvalidated for prophage genes. [src: prophage_ecology]

## Open Directions

- Test whether the carrier-abundance correlations survive after removing the shared genera from the trait scores. This would separate compositional coupling from real signal.
- Compare observed correlations with a permutation null that preserves genus abundance structure. This would replace the sign tests, which have few directions to test.
- Test PHB capacity against temporal-variability measures, not point-in-time values. This would test the feast/famine hypothesis directly.
- Repeat the analyses in non-soil NMDC subsets to address the terrestrial bias.
- Validate taxonomy-based prophage burden inference against measured prophage content in metagenome assemblies. This would test the genus-level conservation assumption.
