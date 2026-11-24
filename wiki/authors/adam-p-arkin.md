# Adam P. Arkin

ORCID: [0000-0002-4999-2931](https://orcid.org/0000-0002-4999-2931)

## Contributions

Platform inventory and use-case validation. The [[summaries/berdl_data_atlas__REPORT]] inventory reports 1,740 deduplicated tables across 119 databases in the KBase Data Lakehouse. [src: berdl_data_atlas] Its schema-level audit found 536 cross-tenant bridges, defined by 29 canonical join keys. [src: berdl_data_atlas] Realized cross-tenant use is concentrated on the `kbase × kescience` axis, which accounts for 36 projects. [src: berdl_data_atlas] Five high-leverage bridges had zero realized use at audit time. [src: berdl_data_atlas] UC1 was sample-validated on the live cluster. The original recipe's `protein_id` bridge column was wrong, because FitnessBrowser uses a composite `(orgId, locusId)` key. [src: berdl_data_atlas] The corrected join gives 55,454 FitnessBrowser genes across 48 organisms with both fitness data and an AlphaFold model. [src: berdl_data_atlas]

Dark genes and gene function. The [[summaries/functional_dark_matter__REPORT]] project found 57,011 (24.9%) of 228,709 genes lacking functional annotation across 48 Fitness Browser organisms. [src: functional_dark_matter] It reported pangenome links for 39,532 (69.3%) of these dark genes. [src: functional_dark_matter] The [[summaries/truly_dark_genes__REPORT]] project split the 57,011 dark genes into 33,105 annotation-lag genes, 6,427 truly dark genes and 17,479 unlinked genes that could not be assessed with bakta. [src: truly_dark_genes] Methanococcus strains S2 and JJ account for 55% of the truly dark genes. [src: truly_dark_genes] In [[summaries/gene_function_ecological_agora__REPORT]], the Alm 2006 r ≈ 0.74 was not reproduced at full GTDB scale. Four framings gave r=0.10–0.29 (n=18,989). [src: gene_function_ecological_agora]

Phenotype prediction and ENIGMA field-site work. [[summaries/genotype_to_phenotype_enigma__REPORT]] built a model from 46,389 (genome × condition) training pairs. It found binary growth predictable on nucleosides (0.780) and moderately predictable on carbon sources (0.695). Continuous kinetics were not predictable. [src: genotype_to_phenotype_enigma] The genus-blocked holdout audit gave 65.1% accuracy. [src: genotype_to_phenotype_enigma] [[summaries/enigma_carbon_census_1__REPORT]] found only 9 of 83 enrichment compounds callable. H1 was not formally supported. [src: enigma_carbon_census_1] [[summaries/enigma_sso_asv_ecology__REPORT]] reported significant distance-decay (Mantel ρ = 0.323, p = 0.029) across 9 wells. Procrustes correspondence with the physical grid was only marginal (m² = 0.379, p = 0.080). [src: enigma_sso_asv_ecology] Hydrogeological zone explained 27.5% of sediment community variance (F = 4.05, p = 0.0001). [src: enigma_sso_asv_ecology]

Ecology of gene content and host-associated systems. [[summaries/phb_granule_ecology__REPORT]] found phaC in 21.9% of 27,690 GTDB species. Enrichment in variable environments was strongly supported (chi2 = 1,656.36). [src: phb_granule_ecology] [[summaries/prophage_ecology__REPORT]] found genome size the dominant predictor of prophage module content (rho=0.717), followed by environment and then phylogeny. No individual TerL lineage showed environment-specific enrichment after FDR correction. [src: prophage_ecology] [[summaries/plant_microbiome_ecotypes__REPORT]] gave a refined location-only R² = 0.060 (p = 0.001) in 607 plant-compartment species. It reported the original R² of 0.527 as largely a taxonomic-sampling artifact. [src: plant_microbiome_ecotypes] [[summaries/ibd_phage_targeting__REPORT]] identified six actionable Tier-A targets. A 5-phage cocktail covered 94.7% of 188 E. coli strains. [src: ibd_phage_targeting] [[summaries/cf_formulation_design__REPORT]] found that metabolic overlap with PA14 predicts inhibition (r = 0.384) but explains only 27% of variance. [src: cf_formulation_design] [[summaries/caulobacter_fur_lipida_loss__REPORT]] found 53 of 93 Leaden Δ*fur* DEGs buffered at logFC ~0. Its outer-membrane proteome is single-replicate, so Lpt conclusions stay open. [src: caulobacter_fur_lipida_loss]

## Projects (13)

- [[summaries/berdl_data_atlas__REPORT|berdl_data_atlas]]
- [[summaries/caulobacter_fur_lipida_loss__REPORT|caulobacter_fur_lipida_loss]]
- [[summaries/cf_formulation_design__REPORT|cf_formulation_design]]
- [[summaries/enigma_carbon_census_1__REPORT|enigma_carbon_census_1]]
- [[summaries/enigma_sso_asv_ecology__REPORT|enigma_sso_asv_ecology]]
- [[summaries/functional_dark_matter__REPORT|functional_dark_matter]]
- [[summaries/gene_function_ecological_agora__REPORT|gene_function_ecological_agora]]
- [[summaries/genotype_to_phenotype_enigma__REPORT|genotype_to_phenotype_enigma]]
- [[summaries/ibd_phage_targeting__REPORT|ibd_phage_targeting]]
- [[summaries/phb_granule_ecology__REPORT|phb_granule_ecology]]
- [[summaries/plant_microbiome_ecotypes__REPORT|plant_microbiome_ecotypes]]
- [[summaries/prophage_ecology__REPORT|prophage_ecology]]
- [[summaries/truly_dark_genes__REPORT|truly_dark_genes]]
