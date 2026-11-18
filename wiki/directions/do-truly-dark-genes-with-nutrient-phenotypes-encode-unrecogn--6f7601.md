---
type: "Research direction"
description: "Genes still uncharacterized after modern reannotation were less common in stress conditions than annotation-lag genes (28.7% versus 43.2%) and more common in nutrient, mixed-community and iron conditions. Is that nutrient signal a real, substrate-specific function, or a by-product of how conditions were sampled?"
hypothesis: "Truly dark genes with strong nutrient phenotypes are co-fit with annotated transporters or catabolic genes for the same substrate more often than annotation-lag genes with nutrient phenotypes are. Their stress phenotypes show no such substrate-matched partners."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Condition-class, gene and annotation tables for the 48 organisms are in the catalog; the co-fitness partner step and the substrate matching need new code, and the catalog did not show the co-fitness table's columns."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.specog", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedannotation"]
findings: ["truly_dark_genes--8c818410", "truly_dark_genes--947aec4f", "functional_dark_matter--cefca00d"]
conflicts: ["conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
papers: ["29769716", "25968644", "41984924", "22125499"]
builds_on: ["findings/truly_dark_genes--8c818410", "findings/truly_dark_genes--947aec4f", "findings/functional_dark_matter--cefca00d", "conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
projects: ["caulobacter_fur_lipida_loss", "functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do truly dark genes with nutrient phenotypes encode unrecognized substrate-specific transport or catabolic steps?

Genes still uncharacterized after modern reannotation were less common in stress conditions than annotation-lag genes (28.7% versus 43.2%) and more common in nutrient, mixed-community and iron conditions. Is that nutrient signal a real, substrate-specific function, or a by-product of how conditions were sampled?

## Hypothesis

Truly dark genes with strong nutrient phenotypes are co-fit with annotated transporters or catabolic genes for the same substrate more often than annotation-lag genes with nutrient phenotypes are. Their stress phenotypes show no such substrate-matched partners.

## Why it matters

It would turn a vague nutrient enrichment into concrete function predictions for the least-annotated genes. It would also show whether 'stress response' is the wrong default frame for ranking dark genes for experiments.

## How to test it

In the transposon-fitness compendium for 48 bacteria, define strong-phenotype truly dark genes and annotation-lag genes with one fixed definition of strong phenotype and of condition class, and record the resulting stress shares for both gene classes, since the two reported pairs differ (28.7% versus 43.2% in one comparison, 43.3% versus 54.7% in another). For each gene, find its most co-fit partners and the single carbon or nitrogen source behind its strongest phenotype. Ask whether the partners carry transporter or catabolic annotations for that same compound. Compare the two gene classes within each organism so that condition coverage is matched. Add a check that excludes the two Methanococcus strains, which hold most truly dark genes.

## What would support or refute it

Support: substrate-matched partners are clearly more common for truly dark nutrient genes than for annotation-lag nutrient genes, in several organisms. Refute: partners are no more substrate-matched than for annotation-lag genes, or the effect lives only in one or two organisms.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Condition-class, gene and annotation tables for the 48 organisms are in the catalog; the co-fitness partner step and the substrate matching need new code, and the catalog did not show the co-fitness table's columns.

## Builds on

- Finding: [[findings/truly_dark_genes--8c818410|Truly dark genes are depleted, not enriched, in stress conditions]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)
- Finding: [[findings/functional_dark_matter--cefca00d|Stress-condition dark genes are not more accessory than carbon/nitrogen genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c|Stress dominance versus stress depletion among strong-phenotype dark genes]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 41984924](https://pubmed.ncbi.nlm.nih.gov/41984924/) High-throughput characterization of Mycobacterium tuberculosis gene function across diverse conditions.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.

PMID 29769716 and PMID 22125499 tie poorly annotated genes to conditions but do not contrast truly dark genes with annotation-lag genes or test whether co-fit partners match the substrate.
