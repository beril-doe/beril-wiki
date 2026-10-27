---
type: "Research direction"
description: "Why are truly dark genes shorter, more accessory and narrower in ortholog breadth than annotation-lag genes, and are they a distinct class of lineage-restricted genes? Does that class explain their depletion in stress conditions among strong-phenotype genes (|f| \u2265 2)?"
hypothesis: "Truly dark genes are enriched for lineage-restricted, island- or mobile-element-associated genes whose accessory status and narrow ortholog breadth persist after controlling for gene length, condition coverage and organism. The same class accounts for their stress depletion among strong-phenotype genes."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The truly dark set, fitness data and pangenome links are in the lakehouse, but the decisive phenotype assays of candidate genes need new measurements."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["truly_dark_genes--947aec4f", "truly_dark_genes--8c818410", "truly_dark_genes--92c362cf", "functional_dark_matter--cefca00d"]
conflicts: ["conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
papers: ["29769716", "38977308", "22125499", "37821698"]
builds_on: ["findings/truly_dark_genes--947aec4f", "findings/truly_dark_genes--8c818410", "findings/truly_dark_genes--92c362cf", "findings/functional_dark_matter--cefca00d", "conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
projects: ["caulobacter_fur_lipida_loss", "functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Truly dark genes may be recently acquired, lineage-restricted genes, not stress-response specialists

Why are truly dark genes shorter, more accessory and narrower in ortholog breadth than annotation-lag genes, and are they a distinct class of lineage-restricted genes? Does that class explain their depletion in stress conditions among strong-phenotype genes (|f| ≥ 2)?

## Hypothesis

Truly dark genes are enriched for lineage-restricted, island- or mobile-element-associated genes whose accessory status and narrow ortholog breadth persist after controlling for gene length, condition coverage and organism. The same class accounts for their stress depletion among strong-phenotype genes.

## Why it matters

If persistent dark genes are a distinct, partly acquired class, ortholog-transfer and stress-response framings are the wrong tools for them. Effort would shift toward niche-specific functions. If length and coverage explain the contrasts, the 'distinct class' reading fails.

## How to test it

In the Fitness Browser and Pangenome Collection, take the 6,427 truly dark genes and the annotation-lag genes. Model darkness status on core-genome fraction (43.1% vs 72.7%) and ortholog breadth (median 1 vs 4 organisms), with gene length (121 vs 194 aa, d = −0.432) as covariate, plus organism and genomic context for island or mobile-element signal. Apply the strong-phenotype restriction (|f| ≥ 2) only to the stress comparison, and repeat it in deeply covered organisms (e.g. MR-1, 121 conditions). The report gives two unreconciled stress comparisons, 28.7% vs 43.2% (OR = 0.53) and 43.3% vs 54.7%; first trace which gene set each uses. Then assay the strongest island-associated candidates by deletion under their phenotype-bearing condition.

## What would support or refute it

Support: after adjusting for length, truly dark genes stay more accessory and island-associated, and the stress depletion persists once organism coverage is modelled. Refute: length, organism or condition coverage absorb the contrasts, or the stress depletion vanishes. The 17,479 unlinked dark genes are not assessed, and short genes are harder to measure.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The truly dark set, fitness data and pangenome links are in the lakehouse, but the decisive phenotype assays of candidate genes need new measurements.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--8c818410|Truly dark genes are depleted, not enriched, in stress conditions]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--92c362cf|Reannotation resolves most dark genes, leaving small truly dark core]] (Insufficient literature evidence)
- Finding: [[findings/functional_dark_matter--cefca00d|Stress-condition dark genes are not more accessory than carbon/nitrogen genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c|Stress dominance versus stress depletion among strong-phenotype dark genes]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 38977308](https://pubmed.ncbi.nlm.nih.gov/38977308/) Large-scale investigation of species-specific orphan genes in the human gut microbiome elucidates their evolutionary origins.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.
- [PMID 37821698](https://pubmed.ncbi.nlm.nih.gov/37821698/) Unraveling the functional dark matter through global metagenomics.

PMID 29769716 and PMID 22125499 assign condition-specific phenotypes to poorly annotated genes, and PMID 38977308 contrasts orphan with conserved genes, but none compares persistent dark genes with annotation-lag genes on pangenome class and condition category.
