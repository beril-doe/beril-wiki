---
type: "Research direction"
description: "Costly but dispensable genes are strongly enriched for transposase, integrase and prophage keywords, and Pseudomonas stutzeri RCH2 stands out with 21.5% of its genes in this class. Does the cost come from entire inserted elements acting as units, or from individual genes?"
hypothesis: "Costly dispensable genes occur in contiguous runs on the chromosome whose members share the same fitness gains when deleted, and removing a whole run restores more growth than removing any single member. A few element-level burdens, such as prophage activity, then account for most of the class."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Gene coordinates, annotations and experiments are in the catalog, but the per-gene fitness table was not shown and must be assembled from per-organism tables; the deletion step needs new measurements."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedannotation", "kescience.fitnessbrowser.experiment"]
findings: ["costly_dispensable_genes--81b8bf3d", "costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--f3a85492"]
conflicts: []
papers: ["22448042", "30809245", "29769716"]
builds_on: ["findings/costly_dispensable_genes--81b8bf3d", "findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--f3a85492"]
projects: ["costly_dispensable_genes"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Is the cost of dispensable genes carried by whole mobile islands rather than single genes?

Costly but dispensable genes are strongly enriched for transposase, integrase and prophage keywords, and Pseudomonas stutzeri RCH2 stands out with 21.5% of its genes in this class. Does the cost come from entire inserted elements acting as units, or from individual genes?

## Hypothesis

Costly dispensable genes occur in contiguous runs on the chromosome whose members share the same fitness gains when deleted, and removing a whole run restores more growth than removing any single member. A few element-level burdens, such as prophage activity, then account for most of the class.

## Why it matters

If whole elements carry the burden, loss of costly genes is a matter of losing intact islands, and the cost is not a property of individual genes. It would also explain why such genes are rare in other genomes and why one strain can be an extreme outlier. If runs form but no element-level burden appears, the cost lies in the individual genes.

## How to test it

Step 1, lakehouse analysis: in P. stutzeri RCH2 and Bacteroides thetaiotaomicron (14.0% costly dispensable), place costly dispensable genes on the chromosome using gene coordinates. Test whether they cluster into runs more than a shuffled placement of equally many genes predicts, whether neighbours within a run show correlated fitness across experiments, and whether runs carry mobile-element annotation. Use a conserved costly set as a control. Step 2, experiment: for one or two runs in RCH2 that pass step 1, delete the whole element and, separately, its individual member genes, and compare growth gains in the laboratory media where the genes were costly.

## What would support or refute it

Clustering and correlated fitness in step 1 support only the spatial part of the idea. The element-level mechanism is supported only if deleting the whole element gives a growth gain larger than the sum of single-gene deletions, or if one element-wide function (such as induced prophage activity) accounts for it. Refute: costly genes are scattered like random genes, or runs form but whole-element deletion gives no more gain than single-gene deletions.

## Data

Approach: analysis then experiment. Readiness: needs compute. Gene coordinates, annotations and experiments are in the catalog, but the per-gene fitness table was not shown and must be assembled from per-organism tables; the deletion step needs new measurements.

## Builds on

- Finding: [[findings/costly_dispensable_genes--81b8bf3d|Pseudomonas stutzeri RCH2 is an extreme outlier in costly dispensable gene share]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--f3a85492|Mobile-element and virulence SEED categories enriched versus costly conserved genes]] (Candidate novel)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 30809245](https://pubmed.ncbi.nlm.nih.gov/30809245/) Bacterial 'Grounded' Prophages: Hotspots for Genetic Renovation and Innovation.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

PMID 22448042 predicts that costly, dispensable functions are lost and PMID 30809245 describes prophage remnants as innovation hotspots, but neither measures whether the burden is concentrated in contiguous islands or tests whole-element against single-gene removal.
