---
type: "Research direction"
description: "Gene families assigned to both regulatory and metabolic pathways show about twice the rate of cross-lineage exchange of purely regulatory or purely metabolic families (0.57% versus 0.27% and 0.28%), though the differences are small and the observation was exploratory. Is that excess due to many distinct domain combinations, or to bridging pathways being easy to transfer?"
hypothesis: "The extra exchange of bridging families is explained by how many distinct domain architectures they have. Families with many architectures are exchanged more regardless of category, and the bridging effect disappears once architecture count is matched."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The exchange classification exists, but the architecture census covered only a 376-family subset, so the full census needs compute."
collections: ["kbase-ke-pangenome", "kbase-uniref", "kbase-ontology-source"]
findings: ["gene_function_ecological_agora--e172b656", "gene_function_ecological_agora--c0bd8a1a", "cog_analysis--7a21065f"]
conflicts: ["conflict--composite-functional-annotation--e8b22b58"]
papers: ["16077904", "37485539", "37232518", "10097118", "21298028"]
builds_on: ["findings/gene_function_ecological_agora--e172b656", "findings/gene_function_ecological_agora--c0bd8a1a", "findings/cog_analysis--7a21065f", "conflicts/conflict--composite-functional-annotation--e8b22b58"]
projects: ["cog_analysis", "gene_function_ecological_agora"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do genes bridging regulation and metabolism cross lineages more because of modular domain architecture?

Gene families assigned to both regulatory and metabolic pathways show about twice the rate of cross-lineage exchange of purely regulatory or purely metabolic families (0.57% versus 0.27% and 0.28%), though the differences are small and the observation was exploratory. Is that excess due to many distinct domain combinations, or to bridging pathways being easy to transfer?

## Hypothesis

The extra exchange of bridging families is explained by how many distinct domain architectures they have. Families with many architectures are exchanged more regardless of category, and the bridging effect disappears once architecture count is matched.

## Why it matters

The complexity hypothesis predicts highly connected genes should transfer less, yet bridging genes appear to transfer more, though by small margins. Because the observation is exploratory, a matched test on independent data would show whether it is real and, if so, whether domain architecture and not pathway membership governs transferability. It also bears on whether multi-category annotations should be filtered out as noise.

## How to test it

For KEGG Orthology families in the Pangenome Collection, tabulate distinct domain architectures, pathway category (regulatory, metabolic, both) and the exchange classification from the gene-transfer atlas. Extend the architecture census beyond the 376-family subset. Compare bridging with single-category families matched for architecture count, and report the rates with uncertainty. Repeat for composite COG assignments such as the mobile-and-defense combination, and test on an independent clade subset not used to find the effect.

## What would support or refute it

Support: the bridging excess vanishes in architecture-matched comparisons. Refutation: it persists in matched comparisons, pointing to a pathway-level cause, or it fails to reappear on the independent clade subset, in which case the original contrast was probably noise.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The exchange classification exists, but the architecture census covered only a 376-family subset, so the full census needs compute.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]
- Collection: [[data/kbase-ontology-source|Ontologies]]

## Builds on

- Finding: [[findings/gene_function_ecological_agora--e172b656|Mixed regulatory-and-metabolic KOs show the highest Innovator-Exchange rate]] (Candidate novel)
- Finding: [[findings/gene_function_ecological_agora--c0bd8a1a|Function classes have distinct gene-acquisition depth profiles, CRISPR-Cas most recent-skewed]] (Insufficient literature evidence)
- Finding: [[findings/cog_analysis--7a21065f|Mobile elements dominate enrichment among novel genes across sampled species]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--composite-functional-annotation--e8b22b58|Composite COG Annotations: Biological Signal or Insufficiently Tested Interpretation?]]

## Closest published work

- [PMID 16077904](https://pubmed.ncbi.nlm.nih.gov/16077904/) Identification and categorization of horizontally transferred genes in prokaryotic genomes.
- [PMID 37485539](https://pubmed.ncbi.nlm.nih.gov/37485539/) Dissecting the HGT network of carbon metabolic genes in soil-borne microbiota.
- [PMID 37232518](https://pubmed.ncbi.nlm.nih.gov/37232518/) Empirical Evidence That Complexity Limits Horizontal Gene Transfer.
- [PMID 10097118](https://pubmed.ncbi.nlm.nih.gov/10097118/) Horizontal gene transfer among genomes: the complexity hypothesis.
- [PMID 21298028](https://pubmed.ncbi.nlm.nih.gov/21298028/) Horizontal transfer, not duplication, drives the expansion of protein families in prokaryotes.

PMID 16077904 and PMID 37485539 find regulatory and metabolic functions among transferred genes, and PMID 37232518 and PMID 10097118 argue complexity limits transfer. None tests a bridging category against domain architecture.
