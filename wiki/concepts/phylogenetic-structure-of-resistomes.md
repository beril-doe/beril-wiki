---
type: "Concept"
description: "How phylogeny structures antimicrobial-resistance repertoires within species"
sources: ["summaries/amr_strain_variation__REPORT.md"]
---
# Phylogenetic Structure of Within-Species Resistomes

Within a species, antimicrobial-resistance (AMR) gene repertoires are often structured by evolutionary relatedness: closely related strains tend to share more AMR genes than distantly related strains. This pattern links [[concepts/within-species-resistome-heterogeneity]] to lineage-associated inheritance, while also requiring caution because resistance-gene prevalence and distance-based statistics can create or obscure phylogenetic signals. [src: amr_strain_variation]

The analysis used average nucleotide identity (ANI) distance matrices and AMR Jaccard distance matrices across 1,261 species. Jaccard distance measures dissimilarity in gene repertoires based on shared and differing genes, while a Mantel test assesses correlation between two distance matrices. [src: amr_strain_variation]

## Key Evidence

A significant phylogenetic signal was detected in 701 of 1,261 species (55.6%) at false-discovery rate (FDR) < 0.05. [src: amr_strain_variation] The median Mantel correlation for all AMR genes was 0.247, and 87.8% of species showed a positive correlation between ANI distance and AMR Jaccard distance. [src: amr_strain_variation] Together, these results support the claim that closely related strains commonly have more similar AMR repertoires within the same species. [src: amr_strain_variation]

The signal was stronger for non-core, putatively acquired AMR genes than for core, intrinsic genes: the median Mantel correlation was 0.222 for non-core genes versus 0.117 for core genes, with a paired t-test of t = -8.35, p = 7.0e-16, and n = 489. [src: amr_strain_variation] This finding supports the hypothesis that acquired resistance elements can become stably maintained and vertically transmitted within particular lineages. [src: amr_strain_variation]

The result also refines a simple acquired-versus-intrinsic interpretation because core genes are nearly universal by definition and therefore have little Jaccard-distance variance. [src: amr_strain_variation] That restricted variance can suppress distance-based Mantel correlations independently of the underlying biology, so the larger non-core signal should not be interpreted as a direct estimate of greater biological heritability without additional controls. [src: amr_strain_variation]

## Relationship to Resistome Heterogeneity

The phylogenetic pattern occurs alongside extensive within-species AMR variation: among 37,444 AMR gene-species records, 51.3% were rare, 41.3% were variable, and 7.5% were fixed. [src: amr_strain_variation] The median variability index was 0.526, and the median pairwise AMR Jaccard distance was 0.435. [src: amr_strain_variation] These values indicate that a species-level label does not imply a uniform resistome and that lineage structure is one component of broader [[concepts/within-species-resistome-heterogeneity]]. [src: amr_strain_variation]

The finding is also relevant to [[concepts/phylogenetic-confounding-of-pangenome-associations]]: AMR associations with environment, host, or other genomic traits may partly reflect shared ancestry rather than independent ecological or functional effects. [src: amr_strain_variation] The present analysis establishes phylogenetic structure in AMR repertoires, but it does not by itself distinguish vertical inheritance from repeated acquisition, loss, or lineage-specific sampling. [src: amr_strain_variation]

## Scope and Limitations

ANI extraction for the Mantel analysis was limited to species with no more than 500 genomes, excluding mega-species such as Escherichia coli, which had 15,388 genomes, and Klebsiella pneumoniae, which had 14,240 genomes. [src: amr_strain_variation] Consequently, the reported phylogenetic proportions do not describe all species or all genomes in the resource. [src: amr_strain_variation]

The analysis used AMRFinderPlus-based AMR calls, so resistance mechanisms absent from that database were not represented. [src: amr_strain_variation] The collection was also heavily biased toward clinical and human-associated isolates, particularly for Klebsiella pneumoniae, Staphylococcus aureus, and Escherichia coli, while environmental species were underrepresented. [src: amr_strain_variation] These limitations may affect both the apparent strength of lineage structure and its generalization to environmental populations. [src: amr_strain_variation]

## Relation to Other Concepts

This result supports [[concepts/phylogenetic-structure-of-resistomes]] as a distinct interpretation of the broader [[concepts/environmental-resistome]]: host association and environment may organize AMR burden, but lineage composition can also organize which AMR genes co-occur within a species. [src: amr_strain_variation] It also complements [[concepts/resistance-island-coinheritance]], because tightly linked resistance islands provide a possible genomic mechanism through which lineage-associated AMR repertoires can be maintained. [src: amr_strain_variation]

## Open Directions

- Subsample species with more than 500 genomes and repeat ANI extraction and Mantel testing to determine whether the 55.6% significant-species estimate changes when mega-species are included. [src: amr_strain_variation]
- Combine phylogeny-aware models with AMR presence/absence matrices to test whether non-core AMR associations persist after separating lineage inheritance from repeated acquisition and loss. [src: amr_strain_variation]
- Map resistance-island genes to plasmids, chromosomes, integron boundaries, and insertion sequences, then test whether genomic context explains the observed median Mantel correlations of 0.222 for non-core genes and 0.117 for core genes. [src: amr_strain_variation]
- Reanalyze AMR phylogenetic structure using curated environmental and collection-date metadata to test whether lineage effects differ between clinical, host-associated, terrestrial, and aquatic sampling contexts. [src: amr_strain_variation]
- Compare AMR phylogenetic structure with virulence-factor profiles and metabolic pathway variation to test whether AMR-defined lineages are broader genomic ecotypes. [src: amr_strain_variation]

[[summaries/amr_strain_variation__REPORT]]
