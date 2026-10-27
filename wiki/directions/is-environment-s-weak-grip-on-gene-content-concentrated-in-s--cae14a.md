---
type: "Research direction"
description: "Do within-species environment effects on gene content appear when whole-genome distances are replaced by specific functional subsets, using organism-proximal habitat measurements?"
hypothesis: "The near-null whole-genome environment effect (not significant in 156 species, 90.7%) hides category-restricted signal, so V, L or transport subsets show more species with significant phylogeny-controlled environment partial correlations than size-matched random gene sets."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pangenome gene clusters, COG annotations and sample metadata exist; per-category partial-correlation runs have not been performed."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["ecotype_analysis--9366534f", "ecotype_analysis--aa4707c1", "ecotype_env_reanalysis--82307b2c", "ecotype_env_reanalysis--1cadc0c9", "ecotype_functional_differentiation--667d861b"]
conflicts: ["conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca", "conflict--ecotype-environment-gene-content--744fe541", "conflict--ecotype-environment-gene-content--66537c9c"]
papers: ["29975997", "33602135", "23332119", "31227022"]
builds_on: ["findings/ecotype_analysis--9366534f", "findings/ecotype_analysis--aa4707c1", "findings/ecotype_env_reanalysis--82307b2c", "findings/ecotype_env_reanalysis--1cadc0c9", "findings/ecotype_functional_differentiation--667d861b", "conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca", "conflicts/conflict--ecotype-environment-gene-content--744fe541", "conflicts/conflict--ecotype-environment-gene-content--66537c9c"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "ecotype_functional_differentiation", "env_embedding_explorer", "prophage_ecology", "soil_metal_functional_genomics"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Is environment's weak grip on gene content concentrated in specific functional categories?

Do within-species environment effects on gene content appear when whole-genome distances are replaced by specific functional subsets, using organism-proximal habitat measurements?

## Hypothesis

The near-null whole-genome environment effect (not significant in 156 species, 90.7%) hides category-restricted signal, so V, L or transport subsets show more species with significant phylogeny-controlled environment partial correlations than size-matched random gene sets.

## Why it matters

It would decide whether species-level 'no environment effect' statements should be limited to whole-genome similarity, and whether locus-specific adaptation is the better description.

## How to test it

For the species of ecotype_analysis, compute phylogeny-controlled partial correlations between environment and gene-content distance per COG category, including V and L, using kbase-ke-pangenome and structured env_broad_scale terms. Compare each with permutation nulls from random gene subsets matched for size and prevalence, and report power per species. Repeat on the ecotype_env_reanalysis set (environmental n=37, median 0.051; human-associated n=93, median 0.084) and with alternative functional groupings.

## What would support or refute it

Support: some categories show significantly more species with environment effects than matched random subsets. A null across categories would be uninformative about cause: genuinely weak structuring, low power, unsuitable functional groupings and AlphaEarth or coordinate measurement limits all remain possible, and only paired direct habitat measurements could separate the last.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pangenome gene clusters, COG annotations and sample metadata exist; per-category partial-correlation runs have not been performed.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/ecotype_analysis--9366534f|Environment effects on gene content are not significant in most species]] (Extends retrieved work)
- Finding: [[findings/ecotype_analysis--aa4707c1|No significant difference in environment effects between free-living and host-associated bacteria]] (In tension with retrieved work)
- Finding: [[findings/ecotype_env_reanalysis--82307b2c|Environmental species show no stronger environment–gene-content correlation than human-associated species]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_env_reanalysis--1cadc0c9|Greater geographic signal in environmental embeddings did not strengthen gene-content correlations]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_functional_differentiation--667d861b|Adaptive COG categories show larger mean ecotype effect sizes than housekeeping categories]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca|Weak Genome-Wide Environmental Signal: Locus-Specific Adaptation or Measurement Limits?]]
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--744fe541|Broad Environmental Null versus Subsystem-Specific Environmental Signals in Gene Content]]
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--66537c9c|Does a Strong Geographic Signal in AlphaEarth Embeddings Mean Environment Shapes Gene Content More Strongly?]]

## Closest published work

- [PMID 29975997](https://pubmed.ncbi.nlm.nih.gov/29975997/) Pan-Genomics of Lactobacillus plantarum Revealed Group-Specific Genomic Profiles without Habitat Association.
- [PMID 33602135](https://pubmed.ncbi.nlm.nih.gov/33602135/) Comparative genomics reveals broad genetic diversity, extensive recombination and nascent ecological adaptation in Micrococcus luteus.
- [PMID 23332119](https://pubmed.ncbi.nlm.nih.gov/23332119/) Horizontal gene transfer and the evolution of bacterial and archaeal population structure.
- [PMID 31227022](https://pubmed.ncbi.nlm.nih.gov/31227022/) Microbial indicators of environmental perturbations in coral reef ecosystems.

PMID 29975997 and 33602135 report weak habitat association in single species; PMID 23332119 argues habitat structures gene transfer. None partitions environment signal by functional category across many species.
