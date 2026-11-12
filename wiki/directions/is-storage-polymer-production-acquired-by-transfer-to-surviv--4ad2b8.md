---
type: "Research direction"
description: "Polyhydroxybutyrate (PHB) carbon storage is more common in species from variable environments, and the pattern holds in every genome-size group. Among species that carry the PHB synthase gene as an accessory gene, do carrier strains come from more variable habitats than non-carrier relatives, which would point to adaptive acquisition?"
hypothesis: "Within genera where the PHB synthase gene is accessory, carrier strains come from more variable or nutrient-pulsed environments than their non-carrier relatives. Acquisition of the gene tracks habitat variability, not inherited lineage."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Gene presence, accessory status and environment metadata exist in the lakehouse, but the within-genus comparison has not been run and metadata is sparse for many genomes."
collections: ["kbase-ke-pangenome"]
findings: ["phb_granule_ecology--589de302", "phb_granule_ecology--f9008fe7", "phb_granule_ecology--ef20cc78"]
conflicts: []
papers: ["24887088", "17113245", "42203387", "14973198"]
builds_on: ["findings/phb_granule_ecology--589de302", "findings/phb_granule_ecology--f9008fe7", "findings/phb_granule_ecology--ef20cc78"]
projects: ["phb_granule_ecology"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Is storage polymer production acquired by transfer to survive feast-and-famine habitats?

Polyhydroxybutyrate (PHB) carbon storage is more common in species from variable environments, and the pattern holds in every genome-size group. Among species that carry the PHB synthase gene as an accessory gene, do carrier strains come from more variable habitats than non-carrier relatives, which would point to adaptive acquisition?

## Hypothesis

Within genera where the PHB synthase gene is accessory, carrier strains come from more variable or nutrient-pulsed environments than their non-carrier relatives. Acquisition of the gene tracks habitat variability, not inherited lineage.

## Why it matters

The overall PHB-niche link was shown to be confounded by genome size, so it cannot yet support the feast-and-famine idea. A within-genus link between habitat and gene gain would test the idea in a way lineage and genome size cannot explain.

## How to test it

In the Pangenome Collection, select genera in which the PHB synthase gene is accessory in at least some species. Compare habitat variability between carrier and non-carrier genomes within the same species or genus, using isolation-source metadata. Then test the mechanism in an organism like Pseudomonas extremaustralis, where the gene has both horizontally acquired and core copies: compare survival of the wild type and a deletion mutant under repeated cycles of nutrient pulse and starvation.

## What would support or refute it

Support: within-genus carriers come from more variable habitats, and the deletion mutant survives starvation cycles worse than wild type. Refute: carriers and non-carriers within genera come from similar habitats, and the mutant survives cycles as well as wild type.

## Data

Approach: analysis then experiment. Readiness: needs compute. Gene presence, accessory status and environment metadata exist in the lakehouse, but the within-genus comparison has not been run and metadata is sparse for many genomes.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/phb_granule_ecology--589de302|Environmental PHB enrichment persists within every genome-size quartile]] (Extends retrieved work)
- Finding: [[findings/phb_granule_ecology--f9008fe7|Phylogenetically discordant phaC carriers are enriched for accessory-genome phaC]] (Extends retrieved work)
- Finding: [[findings/phb_granule_ecology--ef20cc78|PHB–niche-breadth association is confounded by genome size]] (Insufficient literature evidence)

## Closest published work

- [PMID 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/) High polyhydroxybutyrate production in Pseudomonas extremaustralis is associated with differential expression of horizontally acquired and core genome polyhydroxyalkanoate synthase genes.
- [PMID 17113245](https://pubmed.ncbi.nlm.nih.gov/17113245/) Insight in to the phylogeny of polyhydroxyalkanoate biosynthesis: horizontal gene transfer.
- [PMID 42203387](https://pubmed.ncbi.nlm.nih.gov/42203387/) Polyhydroxyalkanoates as ecological currencies across the microbial tree of life.
- [PMID 14973198](https://pubmed.ncbi.nlm.nih.gov/14973198/) Trends between gene content and genome size in prokaryotic species with larger genomes.

PMID 24887088 and PMID 17113245 infer transfer of PHB genes from phylogeny or gene organisation, and PMID 42203387 links PHB to fluctuating environments across the tree of life. None compares habitats of carrier and non-carrier strains within a lineage.
