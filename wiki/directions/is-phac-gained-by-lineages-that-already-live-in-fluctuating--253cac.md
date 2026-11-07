---
type: "Research direction"
description: "Carbon-storage genes are common in plant, soil and wastewater species and rare in animal-associated ones, with the pattern in every genome-size class. In species carrying phaC outside its usual phyla, is the gene acquired after a move into variable habitats, or were those lineages already in such habitats?"
hypothesis: "Gains of phaC in discordant carriers are placed on branches whose environment was already highly variable. Closely related species without phaC are no more variable in habitat than those with it."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene clusters and habitat labels exist; the gene-tree reconciliation and sister-lineage comparison are not built."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["phb_granule_ecology--589de302", "phb_granule_ecology--f9008fe7", "phb_granule_ecology--ef20cc78"]
conflicts: []
papers: ["17113245", "24887088", "33350471", "42203387", "31151997"]
builds_on: ["findings/phb_granule_ecology--589de302", "findings/phb_granule_ecology--f9008fe7", "findings/phb_granule_ecology--ef20cc78"]
projects: ["phb_granule_ecology"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Is phaC gained by lineages that already live in fluctuating environments?

Carbon-storage genes are common in plant, soil and wastewater species and rare in animal-associated ones, with the pattern in every genome-size class. In species carrying phaC outside its usual phyla, is the gene acquired after a move into variable habitats, or were those lineages already in such habitats?

## Hypothesis

Gains of phaC in discordant carriers are placed on branches whose environment was already highly variable. Closely related species without phaC are no more variable in habitat than those with it.

## Why it matters

This separates habitat as a cause of storage-gene acquisition from habitat as a correlate of ancestry. It would show whether feast-and-famine ecology selects for the polymer, or only keeps it.

## How to test it

Build phaC gene trees and species trees for the 311 phylogenetically discordant carriers and their relatives in the Pangenome Collection. Reconcile them to place gains. Compare the environment class of recipient lineages with that of sister lineages lacking phaC, using NMDC BioSamples habitat labels. Repeat on complete genomes only, because metagenome-assembled genomes have uneven gene detection and could mimic absences.

## What would support or refute it

Support: recipient lineages come from high-variability habitats more than their phaC-lacking sisters do, in complete genomes too. Refutation: sisters match recipients in habitat, or the pattern disappears once metagenome-assembled genomes are excluded.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene clusters and habitat labels exist; the gene-tree reconciliation and sister-lineage comparison are not built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/phb_granule_ecology--589de302|Environmental PHB enrichment persists within every genome-size quartile]] (Extends retrieved work)
- Finding: [[findings/phb_granule_ecology--f9008fe7|Phylogenetically discordant phaC carriers are enriched for accessory-genome phaC]] (Extends retrieved work)
- Finding: [[findings/phb_granule_ecology--ef20cc78|PHB–niche-breadth association is confounded by genome size]] (Insufficient literature evidence)

## Closest published work

- [PMID 17113245](https://pubmed.ncbi.nlm.nih.gov/17113245/) Insight in to the phylogeny of polyhydroxyalkanoate biosynthesis: horizontal gene transfer.
- [PMID 24887088](https://pubmed.ncbi.nlm.nih.gov/24887088/) High polyhydroxybutyrate production in Pseudomonas extremaustralis is associated with differential expression of horizontally acquired and core genome polyhydroxyalkanoate synthase genes.
- [PMID 33350471](https://pubmed.ncbi.nlm.nih.gov/33350471/) Screening and characterization of polyhydroxyalkanoate granules, and phylogenetic analysis of polyhydroxyalkanoate synthase gene PhaC in cyanobacteria.
- [PMID 42203387](https://pubmed.ncbi.nlm.nih.gov/42203387/) Polyhydroxyalkanoates as ecological currencies across the microbial tree of life.
- [PMID 31151997](https://pubmed.ncbi.nlm.nih.gov/31151997/) Systematic Analysis of Metabolic Pathway Distributions of Bacterial Energy Reserves.

PMID 17113245, 24887088 and 33350471 infer horizontal transfer of phaC from tree incongruence within single groups. None asks whether recipients were already in variable habitats across the bacterial tree, and PMID 42203387 links the polymer to fluctuating environments without placing gains.
