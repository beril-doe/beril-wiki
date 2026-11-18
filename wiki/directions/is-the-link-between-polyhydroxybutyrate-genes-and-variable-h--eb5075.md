---
type: "Research direction"
description: "Species from highly variable environments carry the PHB synthase gene more often than species from stable ones, in every genome-size band. Does that reflect selection after repeated horizontal acquisition into variable-habitat lineages, rather than inheritance from a PHB-carrying ancestor?"
hypothesis: "Within genera that contain both carriers and non-carriers, carriers come from more variable environments than their non-carrying relatives. Their gene copy is more often accessory than core."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Annotations, taxonomy and environmental embeddings are in the catalog, but embeddings cover only a minority of genomes, so power per genus must be computed."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kbase.ke_pangenome.alphaearth_embeddings_all_years", "kbase.ke_pangenome.gtdb_metadata"]
findings: ["phb_granule_ecology--589de302", "phb_granule_ecology--ef20cc78", "phb_granule_ecology--f9008fe7"]
conflicts: []
papers: ["17113245", "24887088", "42203387", "14973198"]
builds_on: ["findings/phb_granule_ecology--589de302", "findings/phb_granule_ecology--ef20cc78", "findings/phb_granule_ecology--f9008fe7"]
projects: ["phb_granule_ecology"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Is the link between polyhydroxybutyrate genes and variable habitats caused by repeated gene gain?

Species from highly variable environments carry the PHB synthase gene more often than species from stable ones, in every genome-size band. Does that reflect selection after repeated horizontal acquisition into variable-habitat lineages, rather than inheritance from a PHB-carrying ancestor?

## Hypothesis

Within genera that contain both carriers and non-carriers, carriers come from more variable environments than their non-carrying relatives. Their gene copy is more often accessory than core.

## Why it matters

Ancestry and genome size are the two standing confounds of the feast-and-famine storage idea. A within-genus contrast removes most ancestry effects and would show whether variable habitats select for storage gain.

## How to test it

Identify genera with both PHB-synthase-positive and negative species. For each group, compare habitat variability, from the spread of environmental embeddings over genomes with coordinates, and genome size. Test whether carriers sit in more variable habitats than relatives. Check whether the gene copy is accessory in carriers from variable habitats.

## What would support or refute it

Support: carriers are consistently more variable-habitat within genera, beyond genome size, with accessory-gene copies. Refute: within-genus differences vanish or point the other way, so the global pattern is lineage inheritance.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Annotations, taxonomy and environmental embeddings are in the catalog, but embeddings cover only a minority of genomes, so power per genus must be computed.

## Builds on

- Finding: [[findings/phb_granule_ecology--589de302|Environmental PHB enrichment persists within every genome-size quartile]] (Extends retrieved work)
- Finding: [[findings/phb_granule_ecology--ef20cc78|PHB–niche-breadth association is confounded by genome size]] (Insufficient literature evidence)
- Finding: [[findings/phb_granule_ecology--f9008fe7|Phylogenetically discordant phaC carriers are enriched for accessory-genome phaC]] (Extends retrieved work)

## Closest published work

- [PMID 17113245](https://pubmed.ncbi.nlm.nih.gov/17113245/) Insight in to the phylogeny of polyhydroxyalkanoate biosynthesis: horizontal gene transfer.
- [PMID 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/) High polyhydroxybutyrate production in Pseudomonas extremaustralis is associated with differential expression of horizontally acquired and core genome polyhydroxyalkanoate synthase genes.
- [PMID 42203387](https://pubmed.ncbi.nlm.nih.gov/42203387/) Polyhydroxyalkanoates as ecological currencies across the microbial tree of life.
- [PMID 14973198](https://pubmed.ncbi.nlm.nih.gov/14973198/) Trends between gene content and genome size in prokaryotic species with larger genomes.

PMID 17113245 and PMID 24887088 infer horizontal transfer of PHA genes from individual phylogenies, and PMID 42203387 links PHA to fluctuating environments. None tests habitat variability among carriers and non-carriers inside the same genus.
