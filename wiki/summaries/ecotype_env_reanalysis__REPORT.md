---
type: "Summary"
description: "Reanalysis tests whether clinical sampling bias explains weak environment signals."
doc_type: "short"
full_text: "sources/ecotype_env_reanalysis__REPORT.md"
---
# Ecotype Reanalysis — Environmental vs Human-Associated Species

## Overview

This reanalysis tests whether the clinical sampling bias in the AlphaEarth subset explains the weak relationship between environmental context and gene-content variation. Using genome-level environment classifications and the same within-analysis methodology for comparison groups, it finds no evidence that environmental species have stronger environment–gene content correlations than human-associated species. The result confirms the original ecotype-analysis null conclusion while showing that clinical bias is real but does not account for the weak signal. [src: ecotype_env_reanalysis]

## Key Findings

### Environmental versus human-associated correlations

Environmental species (n=37) had a median partial correlation of 0.051, mean 0.073, standard deviation 0.299, and range [-0.50, 0.78]. Human-associated species (n=93) had a median of 0.084, mean 0.110, standard deviation 0.226, and range [-0.30, 0.73]. Mixed/Other species (n=53) had a median of 0.109, mean 0.148, standard deviation 0.261, and range [-0.38, 0.69]. Thus, environmental species did not show stronger correlations; human-associated species showed slightly higher correlations, opposite to the stated hypothesis. [src: ecotype_env_reanalysis]

The one-sided Mann-Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83, so the null hypothesis was not rejected. [src: ecotype_env_reanalysis]

The continuous Spearman analysis likewise found no relationship between the fraction of environmental genomes per species and partial-correlation strength: rho=-0.085 and p=0.25. The corresponding analysis for the fraction of human-associated genomes gave rho=0.030 and p=0.69. [src: ecotype_env_reanalysis]

### Species composition and classification

Among 224 species selected for the ecotype analysis, requiring >=20 genomes with AlphaEarth embeddings and >=30% coverage, 106 species (47%) were majority human-associated, 47 (21%) were majority environmental, and 71 (32%) were Mixed/Other. The environmental categories included Soil, Marine, Freshwater, Extreme, and Plant. Classification used a harmonized env_category mapping and majority vote over genome-level isolation_source assignments. [src: ecotype_env_reanalysis]

The strong clinical sampling bias in the AlphaEarth subset is therefore confirmed, but it does not explain the weak environment–gene content relationship. [src: ecotype_env_reanalysis]

### NaN correlations

Of the 30 species with NaN partial correlations, the NaN rate was 10/47 = 21% for Environmental species, 13/66 = 20% for Mixed/Other species, and 7/100 = 7% for Human-associated species. Environmental species were therefore disproportionately lost to NaN filtering rather than human-associated species. Because this filtering would, if anything, bias toward finding a stronger environmental signal, the observed result remains inconsistent with the hypothesis that environmental species have stronger correlations. [src: ecotype_env_reanalysis]

### Difference from the original analysis

The median partial correlation across all 183 species in this reanalysis was 0.081, compared with 0.003 in the original ecotype analysis; the report characterizes this as a 27x difference. The reanalysis used all genomes with embeddings, including up to 3,505 genomes per species, rather than diversity-maximizing downsampling with a maximum of 250 genomes. It also used different genome sets, which changed the distance distributions. [src: ecotype_env_reanalysis]

The absolute correlation values are not comparable across the two methodologies, but the Environmental versus Human-associated comparison was performed within one consistent methodology, preserving the validity of that group comparison. [src: ecotype_env_reanalysis]

### Interpretation

The result suggests that embedding similarity is not equivalent to ecological relevance: environmental embeddings had a 3.4x geographic-signal ratio versus 2.0x for human-associated embeddings, but the captured environmental variation may not strongly predict bacterial gene content. [src: ecotype_env_reanalysis]

The report also proposes that human-associated species can have genuine geographic structure because global epidemiological patterns may cause different lineages of species such as Klebsiella or Enterococcus to dominate different regions. In that interpretation, AlphaEarth embeddings could capture regional epidemiological patterns rather than ecological differences. This is an explanation offered by the report, not a directly established mechanism. [src: ecotype_env_reanalysis]

Species with more genomes, often clinical species, may have greater statistical power to detect weak correlations. The Mixed/Other group had the highest median partial correlation, 0.109, possibly because it includes diverse sampling campaigns; this is likewise presented as a possible explanation rather than a demonstrated cause. [src: ecotype_env_reanalysis]

The original ecotype analysis reported that phylogeny dominated the environment-versus-host-associated comparison, with p=0.66, using a coarse manual classification. This reanalysis used genome-level harmonized classifications and obtained p=0.83, confirming the null result with a more systematic classification scheme. [src: ecotype_env_reanalysis]

## Caveats and Future Analyses

- **No downsampling:** The reanalysis produced partial correlations 27x higher overall than the original analysis. The report states that absolute values are not comparable, although the within-method group comparison is valid. [src: ecotype_env_reanalysis]
- **NaN exclusion:** Environmental species had a higher NaN rate, 21%, than human-associated species, 7%, so the environmental group was more filtered. The report states that this would bias toward finding a stronger environmental signal, which was not observed. [src: ecotype_env_reanalysis]
- **K. pneumoniae exclusion:** Klebsiella pneumoniae was excluded because it exceeded Spark's maxResultSize during gene-cluster extraction and consequently had no correlation data. [src: ecotype_env_reanalysis]
- **Majority-vote classification:** A species with 51% gut genomes would be classified as Human-associated. The continuous Spearman analysis was used to address this limitation and also found no relationship. [src: ecotype_env_reanalysis]
- **Unresolved methodological discrepancy:** A specific comparison of downsampled versus full-genome extraction is needed to explain the 27x partial-correlation discrepancy. [src: ecotype_env_reanalysis]
- **Functional specificity:** Testing gene subsets, including transport and secondary-metabolism categories, could determine whether environmental effects are masked by whole-genome Jaccard distances. [src: ecotype_env_reanalysis]
- **Environment ontology:** Repeating the analysis with structured ENVO terms from env_broad_scale could test whether more precise environmental classification changes the result. [src: ecotype_env_reanalysis]
- **Genome-count control:** Adding genome count as a covariate could test whether unequal sampling depth inflates correlations in species with more genomes. [src: ecotype_env_reanalysis]

## Slots Into

- [[concepts/pangenome-integration]] — supplies a genome-level environment classification and gene-content correlation reanalysis, showing that clinical sampling composition does not explain the weak environment–gene content signal. [src: ecotype_env_reanalysis]
- [[concepts/cross-tenant-data-bridging]] — demonstrates integration of genome metadata, AlphaEarth embeddings, ANI distances, and gene-cluster memberships from the KBase pangenome collection with parent-project correlation results. [src: ecotype_env_reanalysis]
- [[concepts/ecotype-environment-gene-content]] — proposed cross-project concept for the null relationship between environment classification and bacterial gene-content variation, including the methodological discrepancy with the original analysis. [src: ecotype_env_reanalysis]
