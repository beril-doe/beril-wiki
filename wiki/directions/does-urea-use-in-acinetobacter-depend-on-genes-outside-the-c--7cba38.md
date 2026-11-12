---
type: "Research direction"
description: "What genes make up the largely separate fitness profile for urea in Acinetobacter baylyi ADP1, and are they beyond the urease and nickel-handling genes?"
hypothesis: "Most genes needed specifically for urea growth lie outside the urease cluster, including transport and regulatory genes, and they are less conserved across Acinetobacter than genes needed on other carbon sources."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "Pangenome and BacDive tables are in the catalog, but the ADP1 growth matrix is not among the tables shown, so its location in the lakehouse is unconfirmed."
databases: ["kbase.ke_pangenome", "kescience.bacdive"]
tables: ["kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.genome", "kescience.bacdive.metabolite_utilization", "kescience.bacdive.strain"]
findings: ["acinetobacter_adp1_explorer--df385e36", "acinetobacter_adp1_explorer--886c47ff"]
conflicts: []
papers: ["18319726"]
builds_on: ["findings/acinetobacter_adp1_explorer--df385e36", "findings/acinetobacter_adp1_explorer--886c47ff"]
projects: ["acinetobacter_adp1_explorer"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Does urea use in Acinetobacter depend on genes outside the classical urease cluster?

What genes make up the largely separate fitness profile for urea in Acinetobacter baylyi ADP1, and are they beyond the urease and nickel-handling genes?

## Hypothesis

Most genes needed specifically for urea growth lie outside the urease cluster, including transport and regulatory genes, and they are less conserved across Acinetobacter than genes needed on other carbon sources.

## Why it matters

Urea fitness was nearly unrelated to fitness on other carbon sources. That fits a separate gene set, but the genes have not been named. Identifying them would show whether nitrogen-source use is a lineage-variable trait.

## How to test it

Step 1: from the ADP1 mutant growth data across eight carbon sources, rank genes by how much more their effect on urea differs from the other conditions, and check how many fall outside urease and nickel genes. Step 2: place those genes in the Acinetobacter pangenome and compare their conservation with genes specific to quinate or other carbon sources. Compare with BacDive urea-use calls for Acinetobacter strains. Step 3: delete the top non-urease candidates and measure growth on urea.

## What would support or refute it

Support: several top urea-specific genes are non-urease and are more often variable across genomes than genes specific to other sources, and deletions impair urea growth. Refute: the urea-specific set is just urease and its accessory genes, or the profile is no more distinct than for the other carbon sources once noise is accounted for.

## Data

Approach: analysis then experiment. Readiness: unknown. Pangenome and BacDive tables are in the catalog, but the ADP1 growth matrix is not among the tables shown, so its location in the lakehouse is unconfirmed.

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--df385e36|Urea fitness nearly independent of other carbon-source fitness]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--886c47ff|ADP1 is absent from the Fitness Browser]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.

PMID 18319726 built the single-gene deletion collection for ADP1 but did not ask which genes are specific to urea.
