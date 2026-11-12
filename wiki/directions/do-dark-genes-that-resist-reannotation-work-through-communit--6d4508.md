---
type: "Research direction"
description: "Genes still unannotated after reannotation had fewer strong stress phenotypes than genes that merely lacked an annotation: 28.7% vs 43.2% in one comparison and 43.3% vs 54.7% in another, and the two pairs of figures have not been reconciled. Do these genes act in microbial interaction and iron scavenging rather than stress defence?"
hypothesis: "Genes that stay dark after reannotation mostly encode functions used in nutrient scavenging and microbe-microbe interaction, so their strong phenotypes shift toward mixed-community and iron conditions. Single-organism stress screens will keep missing them."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The within-organism comparison uses existing fitness data. Testing interaction functions needs new co-culture screens, since the Fitness Browser has few mixed-community experiments."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["truly_dark_genes--8c818410", "truly_dark_genes--947aec4f", "functional_dark_matter--cefca00d"]
conflicts: ["conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
papers: ["29769716", "25968644", "22125499", "41984924"]
builds_on: ["findings/truly_dark_genes--8c818410", "findings/truly_dark_genes--947aec4f", "findings/functional_dark_matter--cefca00d", "conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
projects: ["caulobacter_fur_lipida_loss", "functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do dark genes that resist reannotation work through community interactions rather than stress?

Genes still unannotated after reannotation had fewer strong stress phenotypes than genes that merely lacked an annotation: 28.7% vs 43.2% in one comparison and 43.3% vs 54.7% in another, and the two pairs of figures have not been reconciled. Do these genes act in microbial interaction and iron scavenging rather than stress defence?

## Hypothesis

Genes that stay dark after reannotation mostly encode functions used in nutrient scavenging and microbe-microbe interaction, so their strong phenotypes shift toward mixed-community and iron conditions. Single-organism stress screens will keep missing them.

## Why it matters

One project found that stress conditions dominate strong dark-gene phenotypes. Another found the hardest-to-annotate genes depleted in stress. If these genes are interaction functions, stress panels are the wrong way to characterise them and experimental prioritisation should change.

## How to test it

First, in the Fitness Browser, recompute both reported stress comparisons from the same gene sets, so the two pairs of figures are kept side by side and not treated as one settled result. Restrict to organisms with comparable numbers of stress, nutrient, iron and mixed-community experiments, and ask whether the shift away from stress holds within organisms. Then run barcoded-transposon fitness screens of a deeply profiled organism in monoculture versus defined co-culture with an Oak Ridge groundwater partner, and score whether dark genes gain strong effects specifically in co-culture. Use the Pangenome Collection to check whether co-culture-dependent genes are accessory and narrow in ortholog breadth.

## What would support or refute it

Support: under both reported comparisons, and within condition-matched organisms, dark genes shift away from stress, and their phenotypes concentrate in co-culture and iron conditions. Refute: the shift disappears once organisms are matched for condition coverage, or co-culture adds no dark-gene phenotypes beyond those of annotated genes.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The within-organism comparison uses existing fitness data. Testing interaction functions needs new co-culture screens, since the Fitness Browser has few mixed-community experiments.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/truly_dark_genes--8c818410|Truly dark genes are depleted, not enriched, in stress conditions]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)
- Finding: [[findings/functional_dark_matter--cefca00d|Stress-condition dark genes are not more accessory than carbon/nitrogen genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c|Stress dominance versus stress depletion among strong-phenotype dark genes]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.
- [PMID 41984924](https://pubmed.ncbi.nlm.nih.gov/41984924/) High-throughput characterization of Mycobacterium tuberculosis gene function across diverse conditions.

PMID 29769716 and PMID 22125499 tie poorly annotated genes to conditions but do not contrast persistently dark genes with annotation-lag genes by condition type. This direction tests an interaction-function explanation that neither paper examines.
