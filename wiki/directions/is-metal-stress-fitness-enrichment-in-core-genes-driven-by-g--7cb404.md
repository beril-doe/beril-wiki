---
type: "Research direction"
description: "Genes with fitness defects under metal stress are more often core than baseline. Is this because they are general stress-response genes, or do metal-specific genes also sit in the core?"
hypothesis: "Genes important for only one metal or a few metals are less core than genes important across many stresses, so the core enrichment comes from general stress genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness and cluster tables are in the catalog, but the per-gene specificity scores and gene-to-cluster join need computing."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.experiment", "kbase.ke_pangenome.gene_cluster"]
findings: ["metal_fitness_atlas--7bedd365", "metal_fitness_atlas--9bd179d0", "metal_fitness_atlas--b6961196"]
conflicts: []
papers: ["29769716", "12829273", "30523276", "24304895"]
builds_on: ["findings/metal_fitness_atlas--7bedd365", "findings/metal_fitness_atlas--9bd179d0", "findings/metal_fitness_atlas--b6961196"]
projects: ["metal_fitness_atlas"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Is metal-stress fitness enrichment in core genes driven by general stress genes?

Genes with fitness defects under metal stress are more often core than baseline. Is this because they are general stress-response genes, or do metal-specific genes also sit in the core?

## Hypothesis

Genes important for only one metal or a few metals are less core than genes important across many stresses, so the core enrichment comes from general stress genes.

## Why it matters

It would show whether specific metal tolerance is a core trait or an accessory one, which affects predicting tolerance from genomes. The earlier broad definition of metal-important genes limits that inference now.

## How to test it

In Fitness Browser data for the 22 organisms and 14 metals, score each gene by how many unrelated stress experiments (non-metal) and metal experiments show a defect. Compare core fraction for metal-specific, metal-plus-general, and general-only genes against baseline, separating essential from toxic metals. Use pangenome cluster status from the species clades.

## What would support or refute it

Support: core fraction is highest for general genes and near baseline for metal-specific genes. Refute: metal-specific genes are as core-enriched as general genes, or more so.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness and cluster tables are in the catalog, but the per-gene specificity scores and gene-to-cluster join need computing.

## Builds on

- Finding: [[findings/metal_fitness_atlas--7bedd365|Metal-stress fitness genes are enriched in the core genome]] (Candidate novel)
- Finding: [[findings/metal_fitness_atlas--9bd179d0|Essential-metal tolerance genes are more core-enriched than toxic-metal genes]] (Candidate novel)
- Finding: [[findings/metal_fitness_atlas--b6961196|Bioleaching genera are not enriched for metal-tolerance signature]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.
- [PMID 24304895](https://pubmed.ncbi.nlm.nih.gov/24304895/) BacMet: antibacterial biocide and metal resistance genes database.

29769716 and 25968644 supply the fitness method, and 12829273 and 24304895 catalog metal resistance. None splits core enrichment by metal-specific versus general stress genes.
