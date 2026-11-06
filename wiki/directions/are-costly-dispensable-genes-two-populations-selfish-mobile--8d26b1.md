---
type: "Research direction"
description: "Do costly-dispensable genes split into recently acquired mobile elements being purged and leaky functions lost under Black Queen dynamics, and does this explain the Pseudomonas stutzeri RCH2 outlier at 21.5%?"
hypothesis: "Costly-dispensable genes with mobile-element keywords (7.45x enriched) are patchily present in close relatives and island-associated, whereas those without mobile annotation are retained more widely. The report gives 14.1% condition-specific phenotypes for all costly-dispensable genes without a mobile split, so the hypothesis is that this phenotype share is concentrated in the non-mobile subset. RCH2's excess reflects a lineage-specific element expansion."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene-level classes and pangenome data exist, but genomic-context, relative-presence and mobile-split phenotype analyses must be built."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome", "kbase-genomes"]
findings: ["costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--f3a85492", "costly_dispensable_genes--81b8bf3d", "costly_dispensable_genes--7f8211ca", "costly_dispensable_genes--f4e2ff44"]
conflicts: []
papers: ["22448042", "30809245", "28344773", "36097170"]
builds_on: ["findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--f3a85492", "findings/costly_dispensable_genes--81b8bf3d", "findings/costly_dispensable_genes--7f8211ca", "findings/costly_dispensable_genes--f4e2ff44"]
projects: ["costly_dispensable_genes"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Are costly dispensable genes two populations: selfish mobile elements and leaky public-good functions?

Do costly-dispensable genes split into recently acquired mobile elements being purged and leaky functions lost under Black Queen dynamics, and does this explain the Pseudomonas stutzeri RCH2 outlier at 21.5%?

## Hypothesis

Costly-dispensable genes with mobile-element keywords (7.45x enriched) are patchily present in close relatives and island-associated, whereas those without mobile annotation are retained more widely. The report gives 14.1% condition-specific phenotypes for all costly-dispensable genes without a mobile split, so the hypothesis is that this phenotype share is concentrated in the non-mobile subset. RCH2's excess reflects a lineage-specific element expansion.

## Why it matters

It would show that lab-measured burden marks two different evolutionary processes, parasitic DNA purging and adaptive loss of leaky functions. That would stop them being interpreted as one class.

## How to test it

Using genome assemblies (KBase Genomes) and the Pangenome Collection, annotate costly-dispensable genes with genomic context (islands, tRNA flanks, phage or plasmid proximity). Relate that context to singleton status (24.2% of these genes) and presence across close relatives. Split genes into mobile versus non-mobile, using the 11.7x SEED phage/transposon enrichment as the starting marker. Compare retention between the groups, and for the first time compute the condition-specific phenotype fraction (14.1% across all costly-dispensable genes) separately within each group. Compare RCH2 with B. thetaiotaomicron (14.0%). The mobile/virulence annotations rest on keyword and SEED categories, which are not direct provenance measurements.

## What would support or refute it

Support: mobile genes cluster in islands and are patchy in relatives, non-mobile genes are retained more widely and carry a higher share of condition-specific phenotypes than the mobile subset, and RCH2 shows an element expansion. Refute: both subsets are evenly distributed in stable regions, present across relatives, with similar phenotype shares.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene-level classes and pangenome data exist, but genomic-context, relative-presence and mobile-split phenotype analyses must be built.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--f3a85492|Mobile-element and virulence SEED categories enriched versus costly conserved genes]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--81b8bf3d|Pseudomonas stutzeri RCH2 is an extreme outlier in costly dispensable gene share]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--7f8211ca|Costly dispensable genes are not inert: some have condition-specific phenotypes]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--f4e2ff44|Singleton fraction contrast with costly conserved genes is partly structural]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 30809245](https://pubmed.ncbi.nlm.nih.gov/30809245/) Bacterial 'Grounded' Prophages: Hotspots for Genetic Renovation and Innovation.
- [PMID 28344773](https://pubmed.ncbi.nlm.nih.gov/28344773/) Escherichia coli ST131: a multidrug-resistant clone primed for global domination.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 22448042 predicts loss of costly leaky functions and PMID 28344773 links mobile elements to virulence; neither tests whether lab-costly dispensable genes divide into mobile and leaky classes with different retention.
