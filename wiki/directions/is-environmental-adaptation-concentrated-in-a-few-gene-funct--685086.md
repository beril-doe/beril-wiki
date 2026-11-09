---
type: "Research direction"
description: "When gene content is split by functional category, do mobile-element, defense and transport genes track habitat in species where whole-genome gene content does not?"
hypothesis: "Habitat signal sits mainly in adaptive categories (mobile elements, defense, transport) and is near zero in housekeeping categories, so whole-genome comparisons mask it. If so, species with a strong adaptive-category signal will still look unrelated to habitat on the whole-genome measure."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Per-category gene-cluster tables and genome embeddings exist in the lakehouse, but the category-wise distance calculations with phylogenetic control have not been run."
collections: ["kbase-ke-pangenome"]
findings: ["ecotype_analysis--9366534f", "ecotype_functional_differentiation--667d861b", "ecotype_analysis--d8dfb23b", "pangenome_openness--0e2125d9"]
conflicts: ["conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca", "conflict--genome-wide-versus-locus-specific-ecological-adaptation--29fec74b"]
papers: ["29975997", "33602135", "23332119", "40644951"]
builds_on: ["findings/ecotype_analysis--9366534f", "findings/ecotype_functional_differentiation--667d861b", "findings/ecotype_analysis--d8dfb23b", "findings/pangenome_openness--0e2125d9", "conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca", "conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--29fec74b"]
projects: ["ecotype_analysis", "ecotype_functional_differentiation", "pangenome_openness"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Is environmental adaptation concentrated in a few gene functions that whole-genome comparisons dilute?

When gene content is split by functional category, do mobile-element, defense and transport genes track habitat in species where whole-genome gene content does not?

## Hypothesis

Habitat signal sits mainly in adaptive categories (mobile elements, defense, transport) and is near zero in housekeeping categories, so whole-genome comparisons mask it. If so, species with a strong adaptive-category signal will still look unrelated to habitat on the whole-genome measure.

## Why it matters

The corpus mostly finds no environment effect on gene content. That could be real, or it could be dilution by genes that have no ecological role. Separating the two decides whether 'environment does not shape gene content' can be stated generally or only for whole genomes.

## How to test it

Using the Pangenome Collection, take the species from the ecotype analysis that have environmental embeddings. Compute habitat-versus-gene-content association separately for each functional category (COG), controlling for phylogenetic distance. Compare adaptive categories with housekeeping categories, and compare the same species' whole-genome result. Add a control of random gene sets matched in size and prevalence to each category.

## What would support or refute it

Support: adaptive categories show clear habitat association in species whose whole-genome result is null, and matched random gene sets do not. Refutation: category-level results are as weak as the whole-genome result, or random gene sets match the adaptive categories.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Per-category gene-cluster tables and genome embeddings exist in the lakehouse, but the category-wise distance calculations with phylogenetic control have not been run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/ecotype_analysis--9366534f|Environment effects on gene content are not significant in most species]] (Extends retrieved work)
- Finding: [[findings/ecotype_functional_differentiation--667d861b|Adaptive COG categories show larger mean ecotype effect sizes than housekeeping categories]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_analysis--d8dfb23b|Phylogenetic history is inferred to predict gene content better than environment]] (Insufficient literature evidence)
- Finding: [[findings/pangenome_openness--0e2125d9|Pangenome openness is not associated with the environment effect]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca|Weak Genome-Wide Environmental Signal: Locus-Specific Adaptation or Measurement Limits?]]
- Conflict: [[conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--29fec74b|Does Pangenome Openness Bear on Genome-Wide Versus Locus-Specific Ecological Adaptation?]]

## Closest published work

- [PMID 29975997](https://pubmed.ncbi.nlm.nih.gov/29975997/) Pan-Genomics of Lactobacillus plantarum Revealed Group-Specific Genomic Profiles without Habitat Association.
- [PMID 33602135](https://pubmed.ncbi.nlm.nih.gov/33602135/) Comparative genomics reveals broad genetic diversity, extensive recombination and nascent ecological adaptation in Micrococcus luteus.
- [PMID 23332119](https://pubmed.ncbi.nlm.nih.gov/23332119/) Horizontal gene transfer and the evolution of bacterial and archaeal population structure.
- [PMID 40644951](https://pubmed.ncbi.nlm.nih.gov/40644951/) Genomic diversity of Cronobacter sakazakii across the food system to consumers at the global scale.

PMID 29975997 and PMID 33602135 report weak habitat association in single species using whole-gene-content groupings; PMID 40644951 links one functional category to isolation source in one species. This direction asks, across many species, whether the weak whole-genome result hides category-specific signal.
