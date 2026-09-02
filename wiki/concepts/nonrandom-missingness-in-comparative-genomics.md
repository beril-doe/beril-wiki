---
type: "Concept"
description: "How group-dependent data loss can distort comparative genomic conclusions"
sources: ["summaries/ecotype_env_reanalysis__REPORT.md"]
---
# Nonrandom Missingness in Comparative Genomics

Nonrandom missingness occurs when observations are more likely to be absent in some biological or sampling groups than in others, potentially changing the apparent strength or direction of comparative-genomic associations. [src: ecotype_env_reanalysis]

## Evidence from the ecotype reanalysis

The ecotype reanalysis tested whether environmental species had stronger relationships between environmental context and gene-content variation than human-associated species, using partial correlations calculated within a consistent analysis method. [src: ecotype_env_reanalysis]

Environmental species had a NaN partial-correlation rate of 10/47 = 21%, compared with 13/66 = 20% for Mixed/Other species and 7/100 = 7% for Human-associated species. [src: ecotype_env_reanalysis]

Thus, environmental species were disproportionately removed by NaN filtering rather than human-associated species. [src: ecotype_env_reanalysis]

The observed environmental-versus-human-associated comparison nevertheless produced a median partial correlation of 0.051 for Environmental species and 0.084 for Human-associated species, with means of 0.073 and 0.110, respectively. [src: ecotype_env_reanalysis]

A one-sided Mann-Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83, so the null hypothesis was not rejected. [src: ecotype_env_reanalysis]

These results support the interpretation that missingness did not conceal a stronger environmental signal in this analysis; because the environmental group lost a larger fraction of observations, the filtering pattern would, if anything, have favored detection of a stronger environmental association rather than the observed null result. [src: ecotype_env_reanalysis]

## Why missingness matters

Comparative analyses can become biased when filtering removes more observations from one ecological or taxonomic group than another, because the retained observations may no longer represent the original group composition. [src: ecotype_env_reanalysis]

In this case, the NaN pattern is relevant to interpretation because the environmental and human-associated groups differed in both missingness rates and retained correlation values. [src: ecotype_env_reanalysis]

The missingness pattern does not by itself establish why environmental species had more NaN correlations, because the report does not demonstrate whether the cause was genome count, distance structure, gene-content variation, or another property of the analysis. [src: ecotype_env_reanalysis]

Unequal sampling depth is a plausible contributor because species with more genomes may have greater statistical power to detect weak correlations, but this explanation remains untested in the report. [src: ecotype_env_reanalysis]

## Interaction with methodological choices

The reanalysis used all genomes with AlphaEarth embeddings, including up to 3,505 genomes per species, whereas the original analysis used diversity-maximizing downsampling with a maximum of 250 genomes. [src: ecotype_env_reanalysis]

The median partial correlation across all 183 species was 0.081 in the reanalysis and 0.003 in the original analysis, a reported 27x difference. [src: ecotype_env_reanalysis]

The report states that absolute correlation values from the two methodologies are not comparable because the genome sets and distance distributions differed, while the Environmental-versus-Human-associated comparison remained valid because it was performed within one consistent methodology. [src: ecotype_env_reanalysis]

This distinction shows that nonrandom missingness must be evaluated together with extraction, downsampling, and filtering decisions rather than treated as an isolated quality-control detail. [src: ecotype_env_reanalysis]

## Relationship to broader integration problems

The result refines [[concepts/ecotype-environment-gene-content]] by showing that confirmed clinical sampling bias and differential NaN loss do not explain the weak environment–gene-content relationship. [src: ecotype_env_reanalysis]

It also connects to [[concepts/sampling-depth-and-downsampling-effects]], because the reanalysis used a substantially different genome-retention strategy and reported a 27x difference in the overall median partial correlation relative to the original analysis. [src: ecotype_env_reanalysis]

The analysis depended on combining genome metadata, AlphaEarth embeddings, ANI distances, and gene-cluster memberships, linking missingness assessment to [[concepts/cross-tenant-data-bridging]] and [[concepts/pangenome-integration]]. [src: ecotype_env_reanalysis]

## Practical interpretation

A null group comparison should not be interpreted as evidence that missingness is harmless when missingness rates differ across groups. [src: ecotype_env_reanalysis]

For this reanalysis, however, the direction of differential loss makes the simple explanation that clinical overrepresentation alone suppressed an environmental signal inconsistent with the reported results. [src: ecotype_env_reanalysis]

The strongest conclusion supported by the evidence is therefore conditional: within the reanalysis methodology, environmental species did not show stronger environment–gene-content correlations, despite having a higher NaN exclusion rate. [src: ecotype_env_reanalysis]

## Open Directions

- Use the complete species-by-genome table and a missingness model, such as logistic regression or inverse-probability weighting, to test whether genome count, environment category, and distance structure predict NaN status. [src: ecotype_env_reanalysis]
- Recalculate correlations after matched downsampling and full-genome extraction, then test whether the missingness-rate difference and the 27x overall correlation discrepancy persist. [src: ecotype_env_reanalysis]
- Add genome count as a covariate in the environment–gene-content association model to test whether unequal sampling depth explains part of the observed correlation pattern. [src: ecotype_env_reanalysis]
- Repeat the analysis using structured ENVO terms from env_broad_scale and compare missingness across ontology-defined environments to test whether coarse classification contributes to group-dependent loss. [src: ecotype_env_reanalysis]
- Analyze transport and secondary-metabolism gene subsets with the same missingness diagnostics to test whether whole-genome Jaccard distances mask environment-specific associations. [src: ecotype_env_reanalysis]
