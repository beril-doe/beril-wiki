---
type: "Concept"
description: "How clinical sampling bias can distort ecological genomic inference"
sources: ["summaries/ecotype_env_reanalysis__REPORT.md"]
---
# Clinical Sampling Bias and the Interpretation of Ecological Genomic Patterns

Clinical sampling bias is the overrepresentation of human-associated genomes in a comparative collection, which can make genomic patterns appear ecological when they instead reflect epidemiological structure, sampling composition, or unequal statistical power. [src: ecotype_env_reanalysis]

The [[summaries/ecotype_env_reanalysis__REPORT]] directly tested whether this bias explained the weak relationship between environmental context and bacterial gene-content variation. [src: ecotype_env_reanalysis] The reanalysis supports the conclusion that clinical sampling bias is real, but contradicts the hypothesis that removing or accounting for it would reveal substantially stronger environment–gene-content correlations. [src: ecotype_env_reanalysis]

## Evidence for Clinical Sampling Bias

Among 224 species selected using a requirement of at least 20 genomes with AlphaEarth embeddings and at least 30% coverage, 106 species (47%) were majority human-associated, 47 (21%) were majority environmental, and 71 (32%) were Mixed/Other. [src: ecotype_env_reanalysis] Environmental categories included Soil, Marine, Freshwater, Extreme, and Plant, and classification used a harmonized env_category mapping followed by majority voting over genome-level isolation_source assignments. [src: ecotype_env_reanalysis]

This composition demonstrates a strong clinical sampling bias in the AlphaEarth subset, because human-associated species were the largest classification group. [src: ecotype_env_reanalysis] The majority-vote rule can classify a species with 51% gut genomes as Human-associated, so the analysis also used the continuous fraction of environmental or human-associated genomes to reduce dependence on a categorical threshold. [src: ecotype_env_reanalysis]

## Bias Does Not Explain the Weak Environment–Gene-Content Signal

Environmental species had a median partial correlation of 0.051, a mean of 0.073, a standard deviation of 0.299, and a range of [-0.50, 0.78]. [src: ecotype_env_reanalysis] Human-associated species had a median of 0.084, a mean of 0.110, a standard deviation of 0.226, and a range of [-0.30, 0.73]. [src: ecotype_env_reanalysis] Mixed/Other species had a median of 0.109, a mean of 0.148, a standard deviation of 0.261, and a range of [-0.38, 0.69]. [src: ecotype_env_reanalysis]

The environmental group therefore did not show stronger environment–gene-content correlations than the human-associated group; the human-associated group had a slightly higher median and mean. [src: ecotype_env_reanalysis] A one-sided Mann–Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83, so the null hypothesis was not rejected. [src: ecotype_env_reanalysis]

The continuous Spearman analysis likewise found no relationship between the fraction of environmental genomes per species and partial-correlation strength, with rho=-0.085 and p=0.25. [src: ecotype_env_reanalysis] The corresponding analysis for the fraction of human-associated genomes found rho=0.030 and p=0.69. [src: ecotype_env_reanalysis] Together, these within-method comparisons weaken the explanation that clinical sampling composition alone caused the weak ecological signal. [src: ecotype_env_reanalysis]

This finding **supports** [[concepts/ecotype-environment-gene-content]], which addresses the null relationship between environment classification and bacterial gene-content variation. [src: ecotype_env_reanalysis] It also **refines** [[concepts/pangenome-integration]] by showing that integrating genome metadata, AlphaEarth embeddings, ANI distances, and gene-cluster memberships does not by itself establish an ecological interpretation of gene-content correlations. [src: ecotype_env_reanalysis]

## Missingness and Unequal Statistical Power

NaN filtering removed 10 of 47 Environmental species, or 21%, 13 of 66 Mixed/Other species, or 20%, and 7 of 100 Human-associated species, or 7%. [src: ecotype_env_reanalysis] Environmental species were therefore disproportionately lost to NaN filtering rather than human-associated species. [src: ecotype_env_reanalysis]

The report argues that this filtering pattern would, if anything, bias the comparison toward finding a stronger environmental signal, yet the environmental group still did not show stronger correlations. [src: ecotype_env_reanalysis] This result **supports** the use of explicit missingness audits when interpreting ecological genomic comparisons and connects to [[concepts/nonrandom-missingness-in-comparative-genomics]]. [src: ecotype_env_reanalysis]

Species with more genomes, which were often clinical species, may have greater statistical power to detect weak correlations. [src: ecotype_env_reanalysis] The Mixed/Other group had the highest median partial correlation, 0.109, possibly because it includes diverse sampling campaigns, but this explanation was not demonstrated. [src: ecotype_env_reanalysis]

## Embedding Signal Is Not Necessarily Ecological Signal

Environmental embeddings had a 3.4x geographic-signal ratio, whereas human-associated embeddings had a 2.0x geographic-signal ratio. [src: ecotype_env_reanalysis] Despite this stronger geographic signal, environmental embeddings did not correspond to stronger gene-content correlations. [src: ecotype_env_reanalysis]

This comparison **supports** [[concepts/environmental-embedding-ecological-validity]] by showing that embedding similarity should not automatically be interpreted as ecological similarity. [src: ecotype_env_reanalysis] The report proposes, as a hypothesis rather than an established mechanism, that human-associated species can show geographic structure because regional epidemiological patterns may cause different lineages of species such as Klebsiella or Enterococcus to dominate different regions. [src: ecotype_env_reanalysis] Under that hypothesis, AlphaEarth embeddings may capture regional epidemiological patterns rather than ecological differences. [src: ecotype_env_reanalysis]

The result therefore **refines** [[concepts/collection-site-versus-microenvironment-mismatch]]: geographic or collection-level context may encode real structure while remaining an imperfect proxy for the microenvironmental pressures that shape gene content. [src: ecotype_env_reanalysis]

## Methodological Comparability

The median partial correlation across all 183 species in this reanalysis was 0.081, compared with 0.003 in the original ecotype analysis, and the report characterized this as a 27x difference. [src: ecotype_env_reanalysis] The reanalysis used all genomes with embeddings, including up to 3,505 genomes per species, whereas the original analysis used diversity-maximizing downsampling with a maximum of 250 genomes. [src: ecotype_env_reanalysis]

The reanalysis also used different genome sets, which changed the distance distributions. [src: ecotype_env_reanalysis] Absolute correlation values are therefore not comparable across the two methodologies, although the Environmental versus Human-associated comparison was performed within one consistent methodology. [src: ecotype_env_reanalysis]

The original ecotype analysis reported that phylogeny dominated the environment-versus-host-associated comparison, with p=0.66, using a coarse manual classification. [src: ecotype_env_reanalysis] The reanalysis used genome-level harmonized classifications and obtained p=0.83, confirming the null result with a more systematic classification scheme. [src: ecotype_env_reanalysis] This methodological discrepancy **supports** [[concepts/condition-space-dimensionality]] and [[concepts/metadata-resolution-and-within-species-heterogeneity]] as relevant interpretive safeguards, because changing genome inclusion and metadata classification changed absolute correlations while preserving the within-method group comparison. [src: ecotype_env_reanalysis]

## Tensions

The analysis contains a tension between a confirmed clinical sampling bias and the absence of a stronger environmental correlation after group comparison. [src: ecotype_env_reanalysis] The evidence supports the claim that the AlphaEarth subset is clinically skewed, but it does not support the claim that this skew alone explains the weak environment–gene-content relationship. [src: ecotype_env_reanalysis]

A second tension concerns the direction of missingness bias: Environmental species had a 21% NaN rate compared with 7% for Human-associated species, yet removing more Environmental species did not produce the expected stronger environmental signal. [src: ecotype_env_reanalysis] This tension indicates that missingness, sampling depth, and ecological classification must be analyzed jointly rather than treated as interchangeable explanations. [src: ecotype_env_reanalysis]

## Open Directions

- Compare downsampled and full-genome gene-cluster extraction on the same species, using matched distance calculations, to determine why the median partial correlation changed from 0.003 to 0.081 and was characterized as a 27x difference. [src: ecotype_env_reanalysis]
- Add genome count as a covariate in the partial-correlation analysis to test whether unequal sampling depth inflates correlations in species with more genomes. [src: ecotype_env_reanalysis]
- Recompute correlations for transport, secondary-metabolism, and other functional gene subsets using the same environmental and human-associated groups to test whether whole-genome Jaccard distances mask ecological effects. [src: ecotype_env_reanalysis]
- Replace majority-vote categories with structured ENVO terms from env_broad_scale and repeat the group and continuous-fraction analyses to test whether finer environmental ontology changes the null result. [src: ecotype_env_reanalysis]
- Stratify or model NaN outcomes jointly with environment category, genome count, and phylogeny to test whether nonrandom missingness changes the Environmental versus Human-associated comparison. [src: ecotype_env_reanalysis]
- Compare AlphaEarth geographic signal with independent epidemiological and ecological metadata for species such as Klebsiella or Enterococcus to test whether embedding structure reflects regional epidemiology rather than ecological differentiation. [src: ecotype_env_reanalysis]
