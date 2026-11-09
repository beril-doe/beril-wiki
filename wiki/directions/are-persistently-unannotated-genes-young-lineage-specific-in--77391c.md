---
type: "Research direction"
description: "Genes that stay unannotated after modern reannotation are shorter, more accessory, and have narrower ortholog breadth than genes that were later annotated. Does that pattern mark recent origin (transfer or de novo birth), or old genes that evolve too fast to be recognised?"
hypothesis: "Truly dark genes are mostly recent additions. They differ from their host genome in GC and codon use and are patchily present among close relatives, even when compared with length-matched annotation-lag genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Truly dark gene lists and pangenome links exist, but composition and distribution metrics must be computed, and the 17,479 unlinked dark genes cannot be assessed."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser", "kbase-uniref"]
findings: ["truly_dark_genes--947aec4f", "truly_dark_genes--d1b84273", "truly_dark_genes--92c362cf", "functional_dark_matter--b069dc6a"]
conflicts: []
papers: ["38977308", "29769716", "37821698", "34739369", "42706541"]
builds_on: ["findings/truly_dark_genes--947aec4f", "findings/truly_dark_genes--d1b84273", "findings/truly_dark_genes--92c362cf", "findings/functional_dark_matter--b069dc6a"]
projects: ["functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Are persistently unannotated genes young lineage-specific inventions or fast-evolving old genes?

Genes that stay unannotated after modern reannotation are shorter, more accessory, and have narrower ortholog breadth than genes that were later annotated. Does that pattern mark recent origin (transfer or de novo birth), or old genes that evolve too fast to be recognised?

## Hypothesis

Truly dark genes are mostly recent additions. They differ from their host genome in GC and codon use and are patchily present among close relatives, even when compared with length-matched annotation-lag genes.

## Why it matters

More than half of the ortholog groups of dark genes were classed as kingdom-level, but that rests on 48 Fitness Browser organisms, mostly Pseudomonadota, with several major phyla absent. It also covers a different gene population from the truly dark set. Showing which kind of gene dominates the truly dark set tells experimenters whether to chase niche-specific gains or divergent core functions, and tells annotators whether structure-based search can recover them.

## How to test it

In the Pangenome Collection, compare truly dark genes with length-matched annotation-lag genes. Measure GC and codon-use deviation from the host genome, patchiness of presence among genomes of the same genus, and neighbouring mobile-element annotations. Treat the Methanococcus strains, which hold 55% of truly dark genes, as a separate stratum, and run the comparison again within Pseudomonadota only. Then check whether profile or structure searches find remote relatives for the host-typical, narrowly distributed subset.

## What would support or refute it

Support: truly dark genes deviate from the host genome in composition and are patchily present, within Pseudomonadota as well as overall. Refutation: they match the host genome and are present across relatives, which points to fast-evolving old genes. The 17,479 unlinked dark genes cannot be assessed, so the result applies only to the linked set.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Truly dark gene lists and pangenome links exist, but composition and distribution metrics must be computed, and the 17,479 unlinked dark genes cannot be assessed.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--d1b84273|Archaeal Methanococcus strains dominate the truly dark gene set]] (Insufficient literature evidence)
- Finding: [[findings/truly_dark_genes--92c362cf|Reannotation resolves most dark genes, leaving small truly dark core]] (Insufficient literature evidence)
- Finding: [[findings/functional_dark_matter--b069dc6a|Over half of dark-gene ortholog groups are pan-bacterial]] (Insufficient literature evidence)

## Closest published work

- [PMID 38977308](https://pubmed.ncbi.nlm.nih.gov/38977308/) Large-scale investigation of species-specific orphan genes in the human gut microbiome elucidates their evolutionary origins.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 37821698](https://pubmed.ncbi.nlm.nih.gov/37821698/) Unraveling the functional dark matter through global metagenomics.
- [PMID 34739369](https://pubmed.ncbi.nlm.nih.gov/34739369/) Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.
- [PMID 42706541](https://pubmed.ncbi.nlm.nih.gov/42706541/) Large-scale benchmarking of prokaryotic annotation tools across thousands of species.

PMID 38977308 compares species-specific orphan genes with conserved genes in gut genomes. This direction instead compares persistently dark genes with genes that were later annotated, in organisms with fitness data.
