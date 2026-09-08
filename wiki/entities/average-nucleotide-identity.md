---
type: Method
description: Genome-comparison method for estimating relatedness through nucleotide
  identity.
sources:
- id: amr_strain_variation
  resource: ../summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: ecotype_env_reanalysis
  resource: ../summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
title: Average Nucleotide Identity
---
# Average Nucleotide Identity

## What this entity is

**Canonical name:** Average nucleotide identity. **Known alias:** ANI. ANI is a genome-comparison method represented in these reports as a distance matrix for comparing phylogenetic relatedness among strains and species. [^amr_strain_variation]

**Stable external identifier:** No stable external identifier is reported in the source documents. [^amr_strain_variation]

## Key facts

The study compared ANI distance matrices with antimicrobial-resistance (AMR) gene Jaccard-distance matrices across 1,261 species using a [Mantel test](mantel-test.md). [^amr_strain_variation]

Of the 1,261 species tested, 701 (55.6%) showed significant phylogenetic signal at FDR < 0.05, where FDR is the false-discovery rate. [^amr_strain_variation]

The median Mantel r for all AMR genes was 0.247, and 87.8% of species showed a positive correlation between ANI distance and AMR Jaccard distance. [^amr_strain_variation]

Non-core AMR genes had a median Mantel r of 0.222, compared with 0.117 for core AMR genes; the paired t-test result was t = -8.35, p = 7.0e-16, n = 489. [^amr_strain_variation]

The report interprets the stronger signal for non-core AMR genes as supporting the hypothesis that acquired resistance elements can become stably maintained and vertically transmitted within lineages, while noting that near-universal core genes have little Jaccard-distance variance and can therefore produce lower distance-based Mantel correlations independently of biology. [^amr_strain_variation]

ANI extraction for the Mantel analyses was limited to species with <=500 genomes. [^amr_strain_variation] The study generated 1,259 ANI matrices. [^amr_strain_variation] The <=500-genome limit excluded mega-species such as *Escherichia coli*, which had 15,388 genomes, and *Klebsiella pneumoniae*, which had 14,240 genomes, from the phylogenetic-signal analysis. [^amr_strain_variation]

The co-fitness/pangenome study **refines** ANI’s use as a relatedness measure by reporting near-clonal organisms at ANI 99.47% for Ddia6719 and ANI 99.66% for pseudo3_N2E3; both retained enough accessory-gene variation to detect co-inheritance. [^cofitness_coinheritance] It also found higher cofit-pair phi among near genomes (mean = 0.102) than medium-distance genomes (mean = 0.067), **supporting** a shared-ancestry contribution while noting that limited far-distance representation prevented full separation of phylogenetic and functional effects. [^cofitness_coinheritance]

The ecotype analysis **supports** ANI-based phylogenetic distance as a genome-wide relatedness measure: among 172 species, the median partial correlation—association between two variables while accounting for another variable—was 0.0143 for phylogeny versus 0.0025 for environment, and phylogeny dominated in 60.5% of species. [^ecotype_analysis] This result is reported in the context of 13,381 genomes across 224 species, with correlation results available for 172 species. [^ecotype_analysis]

The environmental reanalysis **supports** the original ecotype null conclusion within a consistent method: ANI distances were combined with AlphaEarth embeddings and gene-cluster memberships, and environmental species did not have stronger environment–gene-content partial correlations than human-associated species. [^ecotype_env_reanalysis] Environmental species had median partial correlation 0.051 versus 0.084 for human-associated species; the one-sided Mann–Whitney U test gave U=1536 and p=0.83. [^ecotype_env_reanalysis] The reanalysis **refines** the original result by showing that the clinical sampling bias was real but did not explain the weak signal, while its full-genome, non-downsampled extraction produced an all-species median of 0.081 versus 0.003 originally; these absolute values are not comparable across methodologies. [^ecotype_env_reanalysis]

## Relationships

ANI supplied the phylogenetic-distance component for the study's analysis of [environmentally and lineage-structured AMR variation](../concepts/environmental-resistome.md). [^amr_strain_variation]

It also connects the AMR analysis to [pangenome integration](../concepts/pangenome-integration.md), because ANI-based relatedness was compared with within-species AMR gene-repertoire differences. [^amr_strain_variation] The method is further used in the co-fitness analysis linking pangenome co-occurrence with phylogenetic distance; details are in [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md). [^cofitness_coinheritance]

The ecotype analysis further links ANI-derived phylogenetic distances to environmental-versus-ancestry tests of pangenome gene-content similarity; details are in [ecotype_analysis__REPORT](../summaries/ecotype_analysis__REPORT.md). [^ecotype_analysis] The reanalysis extends that link by integrating ANI distances with genome-level environment classifications and AlphaEarth embeddings; details are in [ecotype_env_reanalysis__REPORT](../summaries/ecotype_env_reanalysis__REPORT.md). [^ecotype_env_reanalysis]

## Limitations

The report cautions that the stronger phylogenetic signal for non-core AMR genes may be partly statistical because core genes are nearly universal and consequently provide little Jaccard-distance variance. [^amr_strain_variation]

The report proposes subsampling strategies for species with more than 500 genomes to extend ANI-based Mantel analyses to larger species collections. [^amr_strain_variation] The co-fitness study likewise had limited phylogenetic control: stratification was available for 7 of 9 organisms, and most lacked genomes in the far stratum (>0.05 branch distance). [^cofitness_coinheritance]

The ecotype analysis **refines** this interpretation by finding no significant environmental effect in 156 of 172 species (90.7%), but it also shows that the result is constrained by AlphaEarth embeddings covering only 28.4% of genomes and by partial correlations that assume linear relationships between distance matrices. [^ecotype_analysis] Thus, its weak environmental signal does not exclude effects on specific gene subsets or ecological effects not captured by the environmental representation. [^ecotype_analysis] The reanalysis adds that environmental species had a 21% NaN-correlation rate versus 7% for human-associated species and that a direct downsampled-versus-full-genome comparison is needed to explain the methodological discrepancy; its within-method group comparison remains valid despite the non-comparable absolute correlations. [^ecotype_env_reanalysis]

[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../summaries/ecotype_env_reanalysis__REPORT.md)
