---
type: "Method"
description: "Species-level metric of how open or closed a pangenome is, computed from core gene fraction."
sources: ["summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/discoveries.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pangenome_openness__REPORT.md"]
---
# Pangenome openness

This page covers pangenome openness, a species-level metric computed from core gene fraction. The evidence is mixed. Openness showed no link to environment or phylogeny effects [src: pangenome_openness], a positive link to latent capability fraction in 22 clades [src: metabolic_capability_dependency], and a strong sampling confound in one dataset. [src: cazyme_pangenome_ecology]

## Key facts

- The Lakehouse table kbase_ke_pangenome.pangenome supplied openness data for 7,334 species. [src: metabolic_capability_dependency] See [[entities/kbase-ke-pangenome]].
- The generated file data/pangenome_openness.csv holds 7,334 rows of species-level openness metrics. [src: metabolic_capability_dependency]
- Among well-sampled pathogens (>2,500 genomes), [[entities/klebsiella-pneumoniae|Klebsiella pneumoniae]] was most open (99.05% open; 0.95% core genes). [src: metabolic_capability_dependency]
- In the same group, [[entities/mycobacterium-tuberculosis|Mycobacterium tuberculosis]] was most closed (97.4% open; 2.6% core genes). [src: metabolic_capability_dependency]

## Relationship to environment and phylogeny

Openness did not predict whether environment or phylogeny dominates gene content. [src: pangenome_openness] Across species with pangenome statistics and ecotype results, Spearman rho against the environment effect was -0.05 (p = 0.54). [src: pangenome_openness, discoveries] Against the phylogeny effect it was 0.03 (p = 0.73). [src: pangenome_openness, discoveries] See [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

## Relationship to latent capabilities

This is a positive result in a small sample. The report aggregated 41 Fitness Browser organisms to 22 unique species clades, because strains in one clade share a single openness value. [src: metabolic_capability_dependency] The fraction of latent capabilities per clade then correlated positively with openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [src: metabolic_capability_dependency] See [[concepts/gene-loss-and-black-queen-hypothesis-tests]].

## Caveats

- In the cazyme report's bacterial dataset, genome_count and cloud_fraction correlate at ρ = 0.913. The report calls openness there largely a sampling artifact, which limits biological interpretation. [src: cazyme_pangenome_ecology]
- The report offers this as a caution for all openness studies using MGnify-scale catalogs. [src: cazyme_pangenome_ecology]
- Species with few sequenced genomes appear closed regardless of true gene flux. [src: cazyme_pangenome_ecology] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].
- Openness is a single summary metric that may not capture the full complexity of pangenome structure. [src: pangenome_openness]
- The report proposes auxiliary fraction, Heap's law alpha and pangenome fluidity as alternative openness metrics to test. [src: pangenome_openness]

## Open Directions

- Test the alternative metrics named above, to see whether the null results with environment and phylogeny depend on the core-fraction metric.
- Repeat the latent-capability correlation after controlling for genome count, to see whether the ρ = 0.69 result survives the sampling confound.
- Rerun the environment and phylogeny comparison on species stratified by genome count.

Source summaries: [[summaries/pangenome_openness__REPORT]], [[summaries/cazyme_pangenome_ecology__REPORT]], [[summaries/metabolic_capability_dependency__REPORT]], [[summaries/discoveries]].
