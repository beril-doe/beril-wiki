---
type: "Method"
description: "Distance-matrix correlation method used for ecological and genomic comparisons"
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Mantel test

## What this entity is

**Canonical name:** Mantel test. [src: amr_strain_variation]

**Known aliases:** Mantel test; Mantel correlation test. [src: amr_strain_variation]

**Stable external identifier:** None was reported in the source document. [src: amr_strain_variation]

The Mantel test assesses the correlation between two distance matrices. [src: amr_strain_variation] In the AMR strain-variation study, it compared average nucleotide identity (ANI) distance matrices with antimicrobial-resistance (AMR) Jaccard distance matrices across species. [src: amr_strain_variation] ANI is a measure of genome-wide nucleotide similarity, while Jaccard distance compares shared and differing gene repertoires. [src: amr_strain_variation]

## Use in genomic variation and ecology

Mantel tests were conducted for 1,261 species. [src: amr_strain_variation] Of these, 701/1,261 species (55.6%) showed significant phylogenetic signal at FDR < 0.05, where FDR is the false-discovery rate. [src: amr_strain_variation] The median Mantel r for all AMR genes was 0.247, and 87.8% of species showed a positive correlation. [src: amr_strain_variation] These results indicate that closely related strains generally tended to share more AMR genes. [src: amr_strain_variation]

In the SSO subsurface ecology study, a Mantel test correlated ecological and geographic distance matrices for 9 wells arranged across approximately 6 m. [src: enigma_sso_asv_ecology] It detected significant distance-decay of community similarity, with Spearman ρ = 0.323, p = 0.029, using 9,999 permutations. [src: enigma_sso_asv_ecology] This **supports** the existing use of Mantel testing to detect structure in distance relationships, while **refining** its application from genomic similarity to spatial community ecology. [src: enigma_sso_asv_ecology]

The SSO analysis found no significant association with the uphill–downhill direction (Mantel ρ = −0.049, p = 0.580), whereas the east–west association was weaker and non-significant (column Mantel ρ = 0.227, p = 0.092). [src: enigma_sso_asv_ecology] A second Mantel analysis comparing groundwater community-distance matrices across two dates produced ρ = 0.867, p = 0.001, indicating that well-to-well similarity rankings were nearly unchanged over the 9-day interval. [src: enigma_sso_asv_ecology] This **supports** persistent short-term spatial structure but does not establish long-term or seasonal stability. [src: enigma_sso_asv_ecology]

The AMR results support [[concepts/environmental-resistome]] by showing that lineage structure organizes within-species AMR repertoires. [src: amr_strain_variation] They also contribute to [[concepts/pangenome-integration]], which integrates pangenome structure with strain-level AMR variation. [src: amr_strain_variation] The SSO results additionally **support** [[concepts/ecotype-environment-gene-content]] by showing that community similarity varies with spatial arrangement, while the proposed contamination-plume explanation remains a hypothesis pending direct geochemistry. [src: enigma_sso_asv_ecology]

Non-core, putatively acquired AMR genes showed a stronger phylogenetic signal than core, intrinsic genes: the median Mantel r was 0.222 for non-core genes versus 0.117 for core genes. [src: amr_strain_variation] A paired t-test comparing these values gave t = -8.35, p = 7.0e-16, and n = 489. [src: amr_strain_variation] This pattern supports the hypothesis that acquired resistance elements can become stably maintained and vertically transmitted within lineages. [src: amr_strain_variation]

## Interpretation and limitations

The stronger non-core signal may be partly statistical because near-universal core genes have little Jaccard-distance variance, which can suppress Mantel correlations independently of biological processes. [src: amr_strain_variation] ANI extraction for the Mantel analysis was limited to species with <=500 genomes. [src: amr_strain_variation] This limitation excluded mega-species such as Escherichia coli, which had 15,388 genomes, and Klebsiella pneumoniae, which had 14,240 genomes, from phylogenetic-signal analysis. [src: amr_strain_variation]

The SSO Mantel associations do not by themselves demonstrate hydrological flow, contamination, or microbial interaction: the plume interpretation is based on community and geographic distances, and direct SSO geochemistry was unavailable. [src: enigma_sso_asv_ecology] The groundwater temporal result is also limited to 5 wells and a 9-day interval. [src: enigma_sso_asv_ecology]

The study generated 1,259 ANI matrices and 1,261 Mantel results. [src: amr_strain_variation] The report proposes subsampling species with >500 genomes as a future strategy for extending Mantel analysis to larger datasets. [src: amr_strain_variation]

## Related pages

- [[summaries/amr_strain_variation__REPORT]] — source report containing the Mantel-test analysis. [src: amr_strain_variation]
- [[summaries/enigma_sso_asv_ecology__REPORT]] — source report containing spatial and temporal community Mantel analyses. [src: enigma_sso_asv_ecology]
- [[entities/average-nucleotide-identity]] — distance measure used in the phylogenetic comparison. [src: amr_strain_variation]
- [[concepts/environmental-resistome]] — concept addressing lineage and environmental organization of AMR. [src: amr_strain_variation]
- [[concepts/pangenome-integration]] — concept addressing pangenome and strain-level AMR integration. [src: amr_strain_variation]
- [[concepts/ecotype-environment-gene-content]] — concept addressing environment-linked community structure. [src: enigma_sso_asv_ecology]
