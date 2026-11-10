---
type: "Research direction"
description: "Truly dark genes with strong phenotypes appear less often in stress conditions than annotation-lag genes (28.7% versus 43.2%) and more often in nutrient, mixed-community and iron conditions. A second stress comparison from the same analysis gives 43.3% versus 54.7%. Does the pattern hold once definitions and condition coverage are aligned?"
hypothesis: "Within organisms that have deep condition panels, truly dark genes with strong phenotypes are co-fitness partners of uptake and transport genes more often than annotation-lag genes are, and show phenotypes more often in nutrient and iron screens than in matched stress screens."
approach: "analysis then experiment"
readiness: "data in the lakehouse"
readiness_basis: "The aligned comparison and co-fitness step use existing fitness data; the confirming screens would need new measurements."
collections: ["kescience-fitnessbrowser"]
findings: ["truly_dark_genes--8c818410", "functional_dark_matter--cefca00d"]
conflicts: ["conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
papers: ["29769716", "22125499", "25968644", "41984924", "39120137"]
builds_on: ["findings/truly_dark_genes--8c818410", "findings/functional_dark_matter--cefca00d", "conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
projects: ["caulobacter_fur_lipida_loss", "functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do truly dark genes act in nutrient and iron acquisition more than in stress defence?

Truly dark genes with strong phenotypes appear less often in stress conditions than annotation-lag genes (28.7% versus 43.2%) and more often in nutrient, mixed-community and iron conditions. A second stress comparison from the same analysis gives 43.3% versus 54.7%. Does the pattern hold once definitions and condition coverage are aligned?

## Hypothesis

Within organisms that have deep condition panels, truly dark genes with strong phenotypes are co-fitness partners of uptake and transport genes more often than annotation-lag genes are, and show phenotypes more often in nutrient and iron screens than in matched stress screens.

## Why it matters

Dark genes are ranked for experiments partly as stress-response candidates. If truly dark genes act mostly in acquisition, screens should be built around nutrient and metal shifts. The two analyses compare different groups (all dark genes versus truly dark against annotation-lag), and organisms were tested under different numbers of conditions, so the answer must come from a design that equalises both.

## How to test it

In the Fitness Browser, restrict to organisms with deep, comparable condition panels (for example Shewanella oneidensis MR-1 with 121 conditions). Within each organism, compute the stress share of strong-phenotype genes for truly dark and annotation-lag genes with one common definition and denominator, so that both reported comparisons can be traced. Then compute co-fitness of strong-phenotype truly dark genes with annotated genes and compare transport and iron-acquisition partners against stress-response partners. For the best candidates, run new fitness screens under iron limitation, alternative nitrogen sources and mixed carbon, and compare phenotype rates with a matched general-stress screen.

## What would support or refute it

Support: after alignment, truly dark genes still show less stress and more nutrient and iron phenotypes than annotation-lag genes, co-vary with uptake genes, and show phenotypes more often in nutrient and iron screens. Refutation: the contrast shrinks or reverses with common definitions or within deep-panel organisms, partners are mostly stress genes, or nutrient and iron screens find no more phenotypes than stress screens.

## Data

Approach: analysis then experiment. Readiness: data in the lakehouse. The aligned comparison and co-fitness step use existing fitness data; the confirming screens would need new measurements.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/truly_dark_genes--8c818410|Truly dark genes are depleted, not enriched, in stress conditions]] (Candidate novel)
- Finding: [[findings/functional_dark_matter--cefca00d|Stress-condition dark genes are not more accessory than carbon/nitrogen genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c|Stress dominance versus stress depletion among strong-phenotype dark genes]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 41984924](https://pubmed.ncbi.nlm.nih.gov/41984924/) High-throughput characterization of Mycobacterium tuberculosis gene function across diverse conditions.
- [PMID 39120137](https://pubmed.ncbi.nlm.nih.gov/39120137/) High-throughput genetics enables identification of nutrient utilization and accessory energy metabolism genes in a model methanogen.

PMID 29769716 and PMID 22125499 tie poorly annotated genes to conditions but do not compare condition classes between truly dark and annotation-lag genes. This direction adds a proposed function class and a targeted screen.
