---
type: "Research direction"
description: "For Acinetobacter baylyi ADP1 genes where growth-model essentiality and transposon essentiality disagree, are the disagreements mostly genes with alternative enzymes or pathways that the model lacks, rather than regulation or missing annotation?"
hypothesis: "Genes predicted essential by the model but dispensable in the transposon data mostly have paralogs or alternative reactions absent from the model. Genes predicted dispensable but essential in transposon data are enriched for unannotated essential functions."
approach: "analysis then experiment"
readiness: "data in the lakehouse"
readiness_basis: "Both calls and annotations exist for 866 genes, though only 15% of genes have model flux data and growth predictions depend heavily on added gapfilled reactions."
collections: ["kbase-ke-pangenome", "kbase-msd-biochemistry", "kbase-genomes"]
findings: ["acinetobacter_adp1_explorer--1cfedc83", "acinetobacter_adp1_explorer--4460d103", "acinetobacter_adp1_explorer--c925d9c6"]
conflicts: []
papers: ["18840283", "18319726", "17437026", "36097170"]
builds_on: ["findings/acinetobacter_adp1_explorer--1cfedc83", "findings/acinetobacter_adp1_explorer--4460d103", "findings/acinetobacter_adp1_explorer--c925d9c6"]
projects: ["acinetobacter_adp1_explorer"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is disagreement between metabolic model and transposon data explained by hidden backup routes?

For Acinetobacter baylyi ADP1 genes where growth-model essentiality and transposon essentiality disagree, are the disagreements mostly genes with alternative enzymes or pathways that the model lacks, rather than regulation or missing annotation?

## Hypothesis

Genes predicted essential by the model but dispensable in the transposon data mostly have paralogs or alternative reactions absent from the model. Genes predicted dispensable but essential in transposon data are enriched for unannotated essential functions.

## Why it matters

It would show which kind of model error dominates, and mark where essential but uncharacterized functions are most likely to be found.

## How to test it

Take the 866 ADP1 genes with both calls, of which 639 are concordant and the remaining 26% discordant. Split the discordant genes by direction. Using the Pangenome Collection and ModelSEED Biochemistry, count paralogs and look for alternative reactions that could substitute. Test whether either direction is enriched for unannotated genes, using the ADP1 pattern that essential genes more often carry pathway assignments than dispensable ones, and use the genes that change flux class between rich and minimal media (177 of 866) as a comparison group. Select the best candidates for double-deletion tests.

## What would support or refute it

Support: backup routes are common in model-essential, transposon-dispensable genes, and the reverse set holds the unannotated essentials. Refutation: discordance is spread evenly across annotation status and redundancy, pointing to regulation or measurement.

## Data

Approach: analysis then experiment. Readiness: data in the lakehouse. Both calls and annotations exist for 866 genes, though only 15% of genes have model flux data and growth predictions depend heavily on added gapfilled reactions.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-msd-biochemistry|ModelSEED Biochemistry]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--1cfedc83|FBA and TnSeq essentiality agree for about three-quarters of shared genes]] (Extends retrieved work)
- Finding: [[findings/acinetobacter_adp1_explorer--4460d103|Unannotated essential genes are leads for novel essential functions]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--c925d9c6|A fifth of genes change FBA flux class between media]] (Extends retrieved work)

## Closest published work

- [PMID 18840283](https://pubmed.ncbi.nlm.nih.gov/18840283/) Iterative reconstruction of a global metabolic model of Acinetobacter baylyi ADP1 using high-throughput growth phenotype and gene essentiality data.
- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 17437026](https://pubmed.ncbi.nlm.nih.gov/17437026/) A genome-scale computational study of the interplay between transcriptional regulation and metabolism.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 18840283 used ADP1 knockouts to refine the model and report agreement after refinement. It did not ask which kind of hidden redundancy or missing annotation causes the remaining disagreements. PMID 36097170 shows that essentiality varies with pangenome content in another organism.
