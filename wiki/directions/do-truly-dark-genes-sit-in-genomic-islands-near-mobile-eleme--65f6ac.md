---
type: "Research direction"
description: "Are genes with no annotation and no fitness phenotype physically clustered in islands near mobile elements, as recent acquisition predicts, or is their accessory enrichment explained by gene length or composition?"
hypothesis: "Truly dark genes lie closer to mobile-element genes than length-matched annotated genes do, and this holds after controlling for GC deviation, which can also reflect membrane-protein composition."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Gene coordinates, pangenome class and Bakta calls appear in the catalog tables; ortholog links for uncovered organisms were not shown."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.organism", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.bakta_annotations"]
findings: ["truly_dark_genes--24c01fa9", "truly_dark_genes--46dcd62a"]
conflicts: ["conflict--reannotation-lag-versus-genuinely-unannotatable-dark-genes--58fe0e09"]
papers: ["29769716", "37821698", "12952534", "39472795"]
builds_on: ["findings/truly_dark_genes--24c01fa9", "findings/truly_dark_genes--46dcd62a", "conflicts/conflict--reannotation-lag-versus-genuinely-unannotatable-dark-genes--58fe0e09"]
projects: ["functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do truly dark genes sit in genomic islands near mobile elements, indicating recent acquisition?

Are genes with no annotation and no fitness phenotype physically clustered in islands near mobile elements, as recent acquisition predicts, or is their accessory enrichment explained by gene length or composition?

## Hypothesis

Truly dark genes lie closer to mobile-element genes than length-matched annotated genes do, and this holds after controlling for GC deviation, which can also reflect membrane-protein composition.

## Why it matters

If true, dark matter is partly a signature of recent horizontal acquisition, and annotation effort should focus on mobile-linked islands rather than assuming annotation lag.

## How to test it

In the Fitness Browser gene table, take truly dark genes and annotation-lag genes, using gene coordinates per organism. Compute distance to the nearest mobile-element-annotated gene and compare with length-matched annotated genes. Link to the pangenome gene clusters for core/accessory class and Bakta product calls. Stratify by organism so Methanococcus, which holds over half the dark genes, does not dominate.

## What would support or refute it

Support: dark genes are closer to mobile elements and more often accessory than matched controls, across several organisms. Refute: the proximity vanishes after length and composition matching, or comes only from Methanococcus, pointing to annotation lag or database bias.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Gene coordinates, pangenome class and Bakta calls appear in the catalog tables; ortholog links for uncovered organisms were not shown.

## Builds on

- Finding: [[findings/truly_dark_genes--24c01fa9|Truly dark genes look like novel acquired biology, not annotation lag]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--46dcd62a|Methanococcus strains account for over half of truly dark genes]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--reannotation-lag-versus-genuinely-unannotatable-dark-genes--58fe0e09|Reannotation Lag or Genuinely Unannotatable: Do Dark-Gene Counts Overstate the Unknown?]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 37821698](https://pubmed.ncbi.nlm.nih.gov/37821698/) Unraveling the functional dark matter through global metagenomics.
- [PMID 12952534](https://pubmed.ncbi.nlm.nih.gov/12952534/) Evolution of mosaic operons by horizontal gene transfer and gene displacement in situ.
- [PMID 39472795](https://pubmed.ncbi.nlm.nih.gov/39472795/) Large-scale genomic analysis of Elizabethkingia anophelis.

29769716 and 37821698 describe dark genes and unannotated families, but neither tests mobile-element proximity against matched annotated genes.
