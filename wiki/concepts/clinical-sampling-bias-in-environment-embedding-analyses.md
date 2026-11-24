---
type: "Concept"
description: "Whether the clinical over-representation in the AlphaEarth genome subset and the choice of species classification confound environment–gene content associations; stops at this ecotype comparison."
sources: ["summaries/discoveries.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md"]
---
# Clinical sampling bias in environment embedding analyses

This page covers whether clinical over-representation in the AlphaEarth genome subset, and the choice of species classification, confound environment–gene content associations. The clinical bias is real and large. [src: ecotype_env_reanalysis] In the ecotype reanalysis it did not explain the weak environment–gene content effect. [src: discoveries, ecotype_env_reanalysis] The evidence supports "bias present, not confounding" for this one comparison. See also [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]] and [[entities/alphaearth-environmental-embeddings]].

## The bias in the AlphaEarth subset

Human-associated sources make up a large share of genomes with embeddings, and environmental categories are much smaller. Of 83,287 genomes with AlphaEarth embeddings, 38% are human-associated. [src: discoveries, env_embedding_explorer] That 38% is human clinical (16,390; 20%), human gut (13,466; 16%) and human other (1,669; 2%). [src: env_embedding_explorer] Environmental categories are much smaller: soil 6,073 genomes (7%), marine 5,850 (7%) and freshwater 5,840 (7%). [src: discoveries, env_embedding_explorer]

The explorer report attributes the bias to NCBI's pathogen-sequencing bias. Clinical isolates tend to have good geographic metadata from epidemiological tracking, and that is why they have embeddings. [src: env_embedding_explorer, discoveries] It also attributes the geographic homogeneity of human-associated embeddings to hospitals and clinics worldwide sharing similar satellite imagery. [src: env_embedding_explorer] The pooled distance curve (2.0x ratio) blends two signals and is dominated by the 38% human-associated fraction. [src: env_embedding_explorer] The report says the bias is known in genomic databases but had not been quantified for satellite-derived embeddings. [src: env_embedding_explorer] It cites Saha et al., 2023 for public databases being heavily skewed toward pathogens and clinical isolates. [src: env_embedding_explorer]

## Hypothesis: bias dilutes the environment signal

The earlier ecotype_analysis found AlphaEarth-based environment similarity to be a weak predictor of gene content, with median partial correlation 0.0025. [src: env_embedding_explorer, discoveries] The explorer report hypothesized that bias may partly explain this weak signal. Its reasoning was that if 38% of compared genomes come from interchangeable hospital environments, the relationship would be diluted. [src: env_embedding_explorer] It proposed repeating the ecotype analysis on environmental-only samples, expecting a stronger signal. [src: env_embedding_explorer]

## Test in the ecotype reanalysis

The reanalysis did not support the hypothesis. It gave the first test of whether genome-level environment classification, rather than species-level manual assignment, changes the ecotype conclusion. [src: ecotype_env_reanalysis] Each species was classified by majority vote of its genomes' environments, using the harmonized env_category mapping from env_embedding_explorer. [src: ecotype_env_reanalysis] The harmonization reduced 5,774 isolation_source values to 12 categories. [src: discoveries] See [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]].

Of 224 species with at least 20 genomes with embeddings and at least 30% coverage, 106 (47%) were majority human-associated and 47 (21%) majority environmental (Soil, Marine, Freshwater, Extreme, Plant). The other 71 (32%) were mixed/other. [src: ecotype_env_reanalysis, discoveries]

Stratifying 213 species by dominant environment gave a higher median partial correlation in human-associated species (0.084) than in environmental species (0.051). The Mann-Whitney p was 0.83. [src: discoveries] The earlier project's coarse manual classification gave p=0.66, and the harmonized reanalysis confirmed the null at p=0.83. [src: ecotype_env_reanalysis] Continuous tests agree. The fraction of human-associated genomes did not correlate with partial correlation (Spearman rho=0.030, p=0.69). [src: ecotype_env_reanalysis] The fraction of environmental genomes also did not (rho=-0.085, p=0.25). [src: ecotype_env_reanalysis]

The report concludes that the clinical bias is real and significant for embedding-based analyses but does not confound the ecotype relationship. [src: ecotype_env_reanalysis, discoveries] Phylogeny dominates regardless of sample environment, and the geographic signal in embeddings and the environment–gene content relationship are distinct phenomena. [src: discoveries] For the wider question, see [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

## Caveats

- Majority vote labels a species with 51% gut genomes as human-associated. The report says the continuous Spearman analysis addresses this and confirms the null. [src: ecotype_env_reanalysis]
- AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid latitude/longitude. [src: env_embedding_explorer] The 38% human bias may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]
- The report proposes, as an explanation not tested here, that embeddings may capture regional epidemiological patterns. Human-associated taxa such as Klebsiella and Enterococcus have global patterns in which different lineages dominate different regions. [src: ecotype_env_reanalysis] Such associations would be real but epidemiological rather than ecological. [src: ecotype_env_reanalysis]
- The report also proposes that species with more genomes, often clinical, have more power to detect weak correlations. [src: ecotype_env_reanalysis] It cautions that such species may have inflated correlations and suggests genome count as a covariate. [src: ecotype_env_reanalysis] See [[concepts/genome-sampling-depth-and-downsampling-effects-on-partial-correlation-estimates]].

## Open Directions

- Add genome count as a covariate in the stratified partial-correlation comparison, to test whether sampling depth explains why human-associated species have higher medians (0.084 vs 0.051).
- Run the proposed environmental-only ecotype analysis directly, to test whether the signal strengthens when clinical genomes are excluded.
- Test whether regional epidemiological lineage structure in Klebsiella and Enterococcus drives the human-associated correlations, for example by comparing within-region and across-region lineage composition.
- Repeat the stratification with a non-majority-vote scheme, such as thresholds on the human fraction, to check sensitivity beyond the continuous Spearman tests.
