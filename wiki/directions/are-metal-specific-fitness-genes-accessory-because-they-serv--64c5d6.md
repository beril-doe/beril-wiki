---
type: "Research direction"
description: "Genes needed specifically under metal stress are less often in the core genome than genes needed under stress in general. Does that follow from their being useful only in metal-impacted habitats, so that genomes from such sources carry them more often?"
hypothesis: "Within species that have genomes from both metal-impacted and other sources, accessory gene families that are metal-specific in the fitness data are more common in genomes from metal-impacted sources than general-stress families are."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene, genome, isolation-source and core-flag tables are shown; the gene-to-cluster link and the metal-specific labels from fitness values would need to be rebuilt, since fitness values sit outside the sample shown."
databases: ["kbase.ke_pangenome", "kescience.bacdive", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.organism", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env", "kescience.bacdive.isolation"]
findings: ["metal_specificity--fed6dcbd", "metal_cross_resistance--fdba2abe", "field_vs_lab_fitness--296eadf6"]
conflicts: []
papers: ["42262111", "29769716", "37065130", "30729256"]
builds_on: ["findings/metal_specificity--fed6dcbd", "findings/metal_cross_resistance--fdba2abe", "findings/field_vs_lab_fitness--296eadf6"]
projects: ["field_vs_lab_fitness", "metal_cross_resistance", "metal_specificity"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Are metal-specific fitness genes accessory because they serve only bacteria from metal-impacted sources?

Genes needed specifically under metal stress are less often in the core genome than genes needed under stress in general. Does that follow from their being useful only in metal-impacted habitats, so that genomes from such sources carry them more often?

## Hypothesis

Within species that have genomes from both metal-impacted and other sources, accessory gene families that are metal-specific in the fitness data are more common in genomes from metal-impacted sources than general-stress families are.

## Why it matters

It would explain the lower conservation of metal-specific genes as habitat-dependent selection rather than as a lab artifact or neutral drift. It would also point to which metal genes are worth screening for in contaminated sites.

## How to test it

Link fitness-collection genes classified as metal-specific or general-stress to pangenome gene clusters of the same species. Using isolation-source labels, split genomes of each species into metal-impacted, such as mine, contaminated or industrial, and other sources. Compare how often metal-specific and general-stress accessory clusters occur in each group, species by species, with genome sampling depth in mind. Check the finding in Desulfovibrio vulgaris Hildenborough, where heavy-metal genes were not clearly less core than baseline.

## What would support or refute it

Support: metal-specific accessory families are more prevalent in genomes from metal-impacted sources than general-stress families are, across several species. Refutation: both gene classes are equally prevalent across source types, which would leave lower conservation unexplained by habitat.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene, genome, isolation-source and core-flag tables are shown; the gene-to-cluster link and the metal-specific labels from fitness values would need to be rebuilt, since fitness values sit outside the sample shown.

## Builds on

- Finding: [[findings/metal_specificity--fed6dcbd|Metal-specific genes are less core-enriched than general-sick genes]] (Insufficient literature evidence)
- Finding: [[findings/metal_cross_resistance--fdba2abe|Pangenome conservation falls from general-stress to metal-shared to metal-specific genes]] (Insufficient literature evidence)
- Finding: [[findings/field_vs_lab_fitness--296eadf6|Heavy-metal fitness genes are not significantly less core than baseline]] (Insufficient literature evidence)

## Closest published work

- [PMID 42262111](https://pubmed.ncbi.nlm.nih.gov/42262111/) Systemic trade-offs between core and accessory genomes govern stress adaptation in Rhodococcus erythropolis.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.
- [PMID 30729256](https://pubmed.ncbi.nlm.nih.gov/30729256/) Gene function and expression regulation of RuvRCAB in bacterial Cr(VI), As(III), Sb(III), and Cd(II) resistance.

PMID 42262111 reports trade-offs between core and accessory genomes under stress in Rhodococcus erythropolis, and PMID 29769716 and PMID 37065130 give fitness data for single organisms. None tests whether metal-specific accessory genes track the metal exposure of the genomes' isolation sources.
