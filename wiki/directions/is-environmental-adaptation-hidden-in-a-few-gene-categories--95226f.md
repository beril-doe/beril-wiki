---
type: "Research direction"
description: "Whole-genome gene content barely tracks environment in most species. Does environment instead select particular functional gene categories, such as defense or mobile elements, within species?"
hypothesis: "Within species whose whole-genome gene content shows no environment link, accessory genes in defense and mobile-element categories still track isolation environment after phylogeny is removed, while housekeeping categories do not."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Gene-cluster presence/absence and isolation-source labels already exist for the species analysed in the ecotype work."
collections: ["kbase-ke-pangenome"]
findings: ["ecotype_analysis--9366534f", "ecotype_analysis--d8dfb23b", "ecotype_functional_differentiation--667d861b"]
conflicts: ["conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca", "conflict--ecotype-environment-gene-content--744fe541"]
papers: ["23332119", "29975997", "33602135", "40644951"]
builds_on: ["findings/ecotype_analysis--9366534f", "findings/ecotype_analysis--d8dfb23b", "findings/ecotype_functional_differentiation--667d861b", "conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca", "conflicts/conflict--ecotype-environment-gene-content--744fe541"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "ecotype_functional_differentiation", "prophage_ecology", "soil_metal_functional_genomics"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Is environmental adaptation hidden in a few gene categories rather than whole genomes?

Whole-genome gene content barely tracks environment in most species. Does environment instead select particular functional gene categories, such as defense or mobile elements, within species?

## Hypothesis

Within species whose whole-genome gene content shows no environment link, accessory genes in defense and mobile-element categories still track isolation environment after phylogeny is removed, while housekeeping categories do not.

## Why it matters

It would show that the widespread 'environment does not matter' result comes from averaging over all genes. Ecotype studies would then need to be built around specific functions, not whole-genome similarity.

## How to test it

Take the species in the Pangenome Collection with enough genomes and direct isolation-source labels. Per species, test each accessory gene family and each functional category for association with environment, holding phylogenetic distance fixed. Compare the observed category-level association with a null built by shuffling environment labels among close relatives. Run this for the species, most of those analysed, in which the whole-genome environment effect was absent.

## What would support or refute it

Support: some categories, most likely defense and mobile elements, stand out against the shuffled null in species with no whole-genome environment effect. Refutation: no category beats the null, so the weak environment signal is genuinely weak or limited by the metadata.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Gene-cluster presence/absence and isolation-source labels already exist for the species analysed in the ecotype work.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/ecotype_analysis--9366534f|Environment effects on gene content are not significant in most species]] (Extends retrieved work)
- Finding: [[findings/ecotype_analysis--d8dfb23b|Phylogenetic history is inferred to predict gene content better than environment]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_functional_differentiation--667d861b|Adaptive COG categories show larger mean ecotype effect sizes than housekeeping categories]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca|Weak Genome-Wide Environmental Signal: Locus-Specific Adaptation or Measurement Limits?]]
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--744fe541|Broad Environmental Null versus Subsystem-Specific Environmental Signals in Gene Content]]

## Closest published work

- [PMID 23332119](https://pubmed.ncbi.nlm.nih.gov/23332119/) Horizontal gene transfer and the evolution of bacterial and archaeal population structure.
- [PMID 29975997](https://pubmed.ncbi.nlm.nih.gov/29975997/) Pan-Genomics of Lactobacillus plantarum Revealed Group-Specific Genomic Profiles without Habitat Association.
- [PMID 33602135](https://pubmed.ncbi.nlm.nih.gov/33602135/) Comparative genomics reveals broad genetic diversity, extensive recombination and nascent ecological adaptation in Micrococcus luteus.
- [PMID 40644951](https://pubmed.ncbi.nlm.nih.gov/40644951/) Genomic diversity of Cronobacter sakazakii across the food system to consumers at the global scale.

PMIDs 29975997 and 33602135 report weak habitat signal within single species; this tests, across many species at once, whether the signal sits in particular functional categories that a whole-genome measure averages away.
