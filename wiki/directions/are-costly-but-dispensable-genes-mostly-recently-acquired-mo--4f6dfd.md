---
type: "Research direction"
description: "Genes that burden growth in the lab yet are absent from many relatives are mostly mobile-element genes. Are they young arrivals that selection has not yet purged, or do they include metabolic genes whose loss pattern points to adaptive loss?"
hypothesis: "Costly dispensable genes are concentrated in rare, recently gained gene clusters (singleton or low-prevalence). The few metabolic genes among them show no more loss than matched metabolic genes, so the set mostly reflects gene gain rather than adaptive loss."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The catalog shows fitness, cluster-status and annotation tables, but linking Fitness Browser genes to pangenome clusters needs a new join."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.bakta_annotations"]
findings: ["costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--e1254d2a", "costly_dispensable_genes--f3a85492"]
conflicts: ["conflict--gene-loss-and-black-queen-hypothesis-tests--59d3cb46"]
papers: ["22448042", "22761588", "36097170", "24910088", "29769716"]
builds_on: ["findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--e1254d2a", "findings/costly_dispensable_genes--f3a85492", "conflicts/conflict--gene-loss-and-black-queen-hypothesis-tests--59d3cb46"]
projects: ["costly_dispensable_genes", "metabolic_capability_dependency"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Are costly but dispensable genes mostly recently acquired mobile elements rather than eroding metabolic pathways?

Genes that burden growth in the lab yet are absent from many relatives are mostly mobile-element genes. Are they young arrivals that selection has not yet purged, or do they include metabolic genes whose loss pattern points to adaptive loss?

## Hypothesis

Costly dispensable genes are concentrated in rare, recently gained gene clusters (singleton or low-prevalence). The few metabolic genes among them show no more loss than matched metabolic genes, so the set mostly reflects gene gain rather than adaptive loss.

## Why it matters

It would show whether lab-measured gene burden mainly reflects horizontal acquisition of selfish elements. That would narrow which genes can be treated as candidates for adaptive gene loss, which would additionally need evidence that a partner supplies the function.

## How to test it

For Fitness Browser organisms, link each costly dispensable and costly conserved gene to its pangenome cluster. Compare cluster prevalence and singleton share, and annotate mobile versus metabolic content with Bakta annotations. For the metabolic remainder, describe the loss pattern across close relatives only as a gene-loss pattern. Calling it Black Queen loss would need community or provider-presence data, so test whether relatives lacking the gene co-occur with others carrying it.

## What would support or refute it

Support: costly dispensable genes are strongly enriched in rare clusters and the metabolic remainder is small and no more lost than controls. Refute: a sizable metabolic group is lost in related genomes. Even then it would only be a gene-loss pattern until a provider test links it to the Black Queen idea.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The catalog shows fitness, cluster-status and annotation tables, but linking Fitness Browser genes to pangenome clusters needs a new join.

## Builds on

- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--e1254d2a|Costly non-conserved genes are mostly mobile-element debris from horizontal transfer]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--f3a85492|SEED phage and transposable element category enriched among costly dispensable genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--gene-loss-and-black-queen-hypothesis-tests--59d3cb46|Clade-Level Support Versus Pathway-Level and Gene-Class Doubts in Black Queen Gene Loss]]

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

22448042 and 22761588 describe adaptive and selection-driven gene loss, and 29769716 supplies the fitness data. None tests the age or mobility of costly dispensable genes.
