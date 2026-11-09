---
type: "Research direction"
description: "Phylogenetically discordant carriers of the polyhydroxybutyrate synthase gene phaC keep it in the accessory genome more often (60.1% of 311 species versus 32.3% overall). Does the gene move into lineages that live in more variable environments, or does genome size explain the association?"
hypothesis: "Within genera that contain both phaC-positive and phaC-negative species, the positive species come from more variable environments. Accessory phaC occurs mainly in those species, independent of genome size."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The species phaC calls and environment classes exist, but the within-genus design and gene trees have not been built."
collections: ["kbase-ke-pangenome"]
findings: ["phb_granule_ecology--f9008fe7", "phb_granule_ecology--589de302", "phb_granule_ecology--ef20cc78"]
conflicts: []
papers: ["17113245", "24887088", "42203387", "33350471", "14973198"]
builds_on: ["findings/phb_granule_ecology--f9008fe7", "findings/phb_granule_ecology--589de302", "findings/phb_granule_ecology--ef20cc78"]
projects: ["phb_granule_ecology"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Is polyhydroxybutyrate storage gained repeatedly by transfer in lineages facing fluctuating environments?

Phylogenetically discordant carriers of the polyhydroxybutyrate synthase gene phaC keep it in the accessory genome more often (60.1% of 311 species versus 32.3% overall). Does the gene move into lineages that live in more variable environments, or does genome size explain the association?

## Hypothesis

Within genera that contain both phaC-positive and phaC-negative species, the positive species come from more variable environments. Accessory phaC occurs mainly in those species, independent of genome size.

## Why it matters

The apparent link between storage and niche breadth was found to be confounded by genome size, which leaves the feast-and-famine explanation untested. A within-genus design could show whether environmental fluctuation selects for acquiring a storage trait.

## How to test it

Using the Pangenome Collection, select genera containing both phaC-positive and phaC-negative species. Compare environmental variability, genome size and phaC pangenome class (core versus accessory) between the two groups within genera. Fit genome size and phylogeny as covariates, and test environmental variability separately inside each genome-size quartile. Compare accessory phaC gene trees with the species tree for incongruence.

## What would support or refute it

Support: within genera, phaC-positive species come from more variable environments and carry accessory phaC. Refutation: no environmental difference within genera, or the difference vanishes after genome size and phylogeny are included.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The species phaC calls and environment classes exist, but the within-genus design and gene trees have not been built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/phb_granule_ecology--f9008fe7|Phylogenetically discordant phaC carriers are enriched for accessory-genome phaC]] (Extends retrieved work)
- Finding: [[findings/phb_granule_ecology--589de302|Environmental PHB enrichment persists within every genome-size quartile]] (Extends retrieved work)
- Finding: [[findings/phb_granule_ecology--ef20cc78|PHB–niche-breadth association is confounded by genome size]] (Insufficient literature evidence)

## Closest published work

- [PMID 17113245](https://pubmed.ncbi.nlm.nih.gov/17113245/) Insight in to the phylogeny of polyhydroxyalkanoate biosynthesis: horizontal gene transfer.
- [PMID 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/) High polyhydroxybutyrate production in Pseudomonas extremaustralis is associated with differential expression of horizontally acquired and core genome polyhydroxyalkanoate synthase genes.
- [PMID 42203387](https://pubmed.ncbi.nlm.nih.gov/42203387/) Polyhydroxyalkanoates as ecological currencies across the microbial tree of life.
- [PMID 33350471](https://pubmed.ncbi.nlm.nih.gov/33350471/) Screening and characterization of polyhydroxyalkanoate granules, and phylogenetic analysis of polyhydroxyalkanoate synthase gene PhaC in cyanobacteria.
- [PMID 14973198](https://pubmed.ncbi.nlm.nih.gov/14973198/) Trends between gene content and genome size in prokaryotic species with larger genomes.

PMID 17113245, PMID 24887088 and PMID 33350471 infer transfer of the gene from tree incongruence or islands in individual groups. PMID 42203387 links these storage polymers to fluctuating environments. None combines a within-genus environmental contrast with pangenome class.
