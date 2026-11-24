---
type: "Research direction"
description: "Within bacterial species where GC content varies with isolation source, is the shift carried by core-genome sequence, by the accessory genes that are gained or lost, or by both?"
hypothesis: "If the GC shift is carried mainly by core genes shared by all strains, it points to sequence-level processes rather than gene gain and loss. If it vanishes once accessory genes are removed, it is a by-product of gene-content differences."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene cluster core/accessory flags and sequences are in the catalog, but per-genome partitioned GC would have to be computed; the catalog did not show a precomputed partition."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.phylogenetic_tree_distance_pairs"]
findings: ["gc_ecotype_ecology--de846de7", "gc_ecotype_ecology--407ce45e", "gc_ecotype_ecology--3541499c", "ecotype_analysis--38d98bec"]
conflicts: []
papers: ["33166245", "34100697", "37648438"]
builds_on: ["findings/gc_ecotype_ecology--de846de7", "findings/gc_ecotype_ecology--407ce45e", "findings/gc_ecotype_ecology--3541499c", "findings/ecotype_analysis--38d98bec"]
projects: ["ecotype_analysis", "gc_ecotype_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Does within-species GC variation with isolation source arise in core genes or in gene gain and loss?

Within bacterial species where GC content varies with isolation source, is the shift carried by core-genome sequence, by the accessory genes that are gained or lost, or by both?

## Hypothesis

If the GC shift is carried mainly by core genes shared by all strains, it points to sequence-level processes rather than gene gain and loss. If it vanishes once accessory genes are removed, it is a by-product of gene-content differences.

## Why it matters

GC appeared more environment-responsive within species than gene presence/absence, which sits in tension with phylogeny dominating gene content. Locating the GC signal would show which kind of variation tracks environment. Whether this reflects adaptation, mutation or recombination bias is a possible interpretation to test afterward, not something this analysis settles.

## How to test it

For the species with an isolation-source GC association after ANI-cluster control, compute per-genome GC separately for core gene clusters and for accessory gene clusters. Repeat the isolation-source association, with the same phylogenetic control, on each partition. Compare the share of species with an association in each partition. Also use the within-species tree distances to check that the result holds when phylogeny is modelled continuously.

## What would support or refute it

Support: the association persists in core-gene GC in most species and is weak in accessory GC. Refute: the association is confined to accessory-gene GC or disappears in both partitions. Either result is informative. Neither establishes the cause of a core-gene shift.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene cluster core/accessory flags and sequences are in the catalog, but per-genome partitioned GC would have to be computed; the catalog did not show a precomputed partition.

## Builds on

- Finding: [[findings/gc_ecotype_ecology--de846de7|GC appears more environment-responsive than gene content within species]] (Candidate novel)
- Finding: [[findings/gc_ecotype_ecology--407ce45e|Within-species GC varies with isolation source in many bacterial species]] (Insufficient literature evidence)
- Finding: [[findings/gc_ecotype_ecology--3541499c|Signal persists under continuous phylogenetic regression instead of ANI clusters]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_analysis--38d98bec|Phylogeny dominates gene-content similarity in most species analyzed]] (Insufficient literature evidence)

## Closest published work

- [PMID 33166245](https://pubmed.ncbi.nlm.nih.gov/33166245/) Plasmids encode niche-specific traits in Lactobacillaceae.
- [PMID 34100697](https://pubmed.ncbi.nlm.nih.gov/34100697/) Mining genome traits that determine the different gut colonization potential of Lactobacillus and Bifidobacterium species.
- [PMID 37648438](https://pubmed.ncbi.nlm.nih.gov/37648438/) Data-driven identification of major axes of functional variation in bacteria.

PMID 33166245 links plasmid GC to niche across Lactobacillaceae species, and PMID 34100697 links GC to lifestyle; neither splits within-species GC into core and accessory parts.
