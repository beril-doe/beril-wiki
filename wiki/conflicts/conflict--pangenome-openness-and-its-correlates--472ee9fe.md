<!-- tension-hash: 472ee9fe47e2503e -->
# Pangenome Openness: Does It Track AMR, Pathway Variability, Ecology and Gene Gains?

Projects disagree on what pangenome openness (how much a species' gene repertoire keeps growing as genomes are added) correlates with. Correlations with antimicrobial resistance (AMR), pathway variability, ecology and gene gains differ in sign and size across reports. The overall AMR correlation is near zero (rho=0.006) [src: amr_pangenome_atlas], while the pathway partial correlation is rho=0.530 [src: discoveries]. Rho is Spearman rank correlation. This matters because the reports use different datasets and measures, so openness may not mean one thing. The page frames the tension for [[concepts/pangenome-openness-and-its-correlates]].

## Evidence Sides

**Openness links to other traits (positive or negative)**
- AMR: the correlation is positive within 8/10 phyla [src: amr_pangenome_atlas]. AMR variability within species is negatively related to openness (rho = -0.193). [src: amr_strain_variation]
- Pathways: the pan-bacterial partial correlation (a correlation controlling for a third variable) with genome count is rho=0.530. [src: discoveries]
- Pathway variability and latent-capability links to openness are reported. [src: metabolic_capability_dependency, pathway_capability_dependency]
- Niche breadth: openness correlates positively (r=0.324). [src: discoveries] PGP (plant-growth-promoting gene) richness correlates negatively (rho = −0.195). [src: pgp_pangenome_ecology]

**Openness is null, near zero or confounded**
- AMR: the overall correlation is near zero (rho=0.006). [src: amr_pangenome_atlas]
- Confound: in the CAZyme (carbohydrate-active enzyme) dataset, genome_count and cloud_fraction correlate at ρ = 0.913. [src: cazyme_pangenome_ecology] The reports use different datasets, so I do not reconcile this with the pathway result.
- Ecology: openness is uncorrelated with environment and phylogeny effects. [src: pangenome_openness]
- Gene gains: openness shows a null with recent gene gains, which the report attributes to the two measuring distinct phenomena. [src: gene_function_ecological_agora]

## Possible Reconciliations

- **Hypothesis: lineage structure.** Pooling phyla may cancel within-phylum positive AMR trends, giving a near-zero overall value. This is untested here.
- **Hypothesis: measure dependence.** Niche breadth, PGP richness, and environment/phylogeny effects capture different aspects of ecology, so signs need not conflict.
- **Hypothesis: sampling confounds.** Genome count may inflate openness in some datasets, so partial and raw correlations may not be comparable.
- **Hypothesis: timescale.** Openness reflects accumulated variation, whereas recent gene gains reflect a separate process, as the report suggests.

## Resolving Work

- Recompute openness with one definition and one genome-count control across the AMR, pathway, CAZyme and PGP datasets. Question: do the signs persist under a shared measure?
- Run within-phylum and pooled phylogenetically controlled models (for example PGLS, phylogenetic generalized least squares) on AMR count. Question: does phylogeny explain the gap between the 8/10 phyla and the overall value?
- Subsample genomes to equal depth per species and rerun the pathway-variability correlation. Question: does the result survive when genome count is fixed rather than regressed out?
- Apply the gene-gain method to the species used for pathway variability and latent capability. Question: do openness and recent gains diverge in the same species?
- Test niche breadth and PGP richness on the same species set with the same openness metric. Question: is the positive versus negative sign a measure artifact?
