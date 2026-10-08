<!-- tension-hash: b4822dc29b20b644 -->
# Do environmental and geographic signals in microbial genomic patterns hold up as ecological inference?

The [[concepts/environment-embedding-geography]] page asks whether environmental metadata, field abundance and genomic data capture ecological variation at a resolution that matters for microbial genomes. Across five projects, environment-related results come paired with caveats. Cluster alignment is not causal. Global taxon representation differs from a local environmental clade. Treatment alone explains less variation than treatment combined with soil horizon. Laboratory metal tolerance was non-significant in field abundance. Some signals did not pass multiple-testing correction or rest on a small genome set. Whether these caveats are minor qualifications or undercut the environment–genome link as a general claim decides how much weight the corpus can give environmental and geographic structure.

## Evidence Sides

**Side A: an environment-linked interaction is reported.** In the Harvard Forest warming design, treatment × horizon (treatment crossed with soil layer) explained 41%. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]

**Side B: each signal carries a caveat that limits inference.**
- Cluster alignment is not causal. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]
- Global Pseudomonas representation differs from the environmental clade of ENIGMA (the Oak Ridge contaminated-subsurface research program). [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]
- Treatment alone explained 7.6% (p=0.069; p is the probability of a result at least this extreme if there were no effect), versus 41% for treatment × horizon. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]
- Laboratory metal tolerance was non-significant in field abundance. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]
- Samples affected by rare earth elements (REE) did not pass FDR (false discovery rate, a multiple-testing correction). [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]
- The REE–acid mine drainage (REE-AMD) set contained only 37 MAGs (metagenome-assembled genomes, reconstructed from community sequencing). [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]

## Possible Reconciliations

- *Hypothesis:* Environmental structure is real but conditional. It would appear mainly through interactions, such as treatment with horizon, rather than as main effects. On this view the 7.6% and 41% results are consistent. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]
- *Hypothesis:* Some non-significant results reflect limited power or sample composition rather than absent biology. The 37-MAG REE-AMD set and the failure to pass FDR fit this explanation but do not establish it. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]
- *Hypothesis:* Mismatches between global reference collections and local environmental clades, such as the difference between global Pseudomonas representation and ENIGMA's environmental clade, produce apparent disagreements that reflect taxonomic scope rather than ecological absence. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]

The supplied evidence does not establish any of these hypotheses.

## Resolving Work

- **Clusters:** Test whether cluster alignment survives controls for phylogeny and sampling composition. Use ecological-agora clusters with phylogeny-aware permutation models to ask whether alignment exceeds what shared ancestry alone predicts.
- **Pseudomonas:** Compare ENIGMA environmental Pseudomonas genomes with the global Pseudomonas collection by restricting analyses to the matched clade. This asks whether conclusions change once representation is harmonized.
- **Harvard Forest:** Run horizon-stratified models of treatment effects on the Harvard Forest community data. This asks whether warming effects exist within individual horizons or only in the combined interaction.
- **Oak Ridge:** Pair Oak Ridge field abundance with lab metal-tolerance phenotypes at strain or clade resolution rather than genus. This asks whether the non-significant result reflects taxonomic aggregation.
- **REE:** Expand REE-impacted and REE-AMD MAG sampling and run a power analysis before FDR testing. This asks whether the REE signal fails because of effect size or because of sample size.
