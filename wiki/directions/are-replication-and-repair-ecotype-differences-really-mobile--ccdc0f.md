---
type: "Research direction"
description: "In species that split into gene-content ecotypes, is the difference in the replication, recombination and repair category carried by mobile-element genes (transposases, integrases) rather than genuine DNA-repair genes? Is the unknown-function category's difference carried by genes that sit beside mobile elements?"
hypothesis: "Most of the ecotype difference in the replication/recombination/repair category comes from transposase, integrase and recombinase genes, and the unknown-function genes that differ between ecotypes mostly lie next to those mobile elements. Core repair genes differ little between ecotypes."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Gene-cluster annotations and genome-level presence/absence for the ecotype species are in the Pangenome Collection; the work is a finer annotation split and a gene-neighbourhood check."
collections: ["kbase-ke-pangenome"]
findings: ["ecotype_functional_differentiation--69a046fd", "ecotype_functional_differentiation--667d861b", "ecotype_functional_differentiation--840b73cb"]
conflicts: ["conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1"]
papers: ["40644951", "37154706", "36853054", "33423895"]
builds_on: ["findings/ecotype_functional_differentiation--69a046fd", "findings/ecotype_functional_differentiation--667d861b", "findings/ecotype_functional_differentiation--840b73cb", "conflicts/conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1"]
projects: ["cog_analysis", "ecotype_functional_differentiation", "plant_microbiome_ecotypes"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Are replication-and-repair ecotype differences really mobile-element turnover in disguise?

In species that split into gene-content ecotypes, is the difference in the replication, recombination and repair category carried by mobile-element genes (transposases, integrases) rather than genuine DNA-repair genes? Is the unknown-function category's difference carried by genes that sit beside mobile elements?

## Hypothesis

Most of the ecotype difference in the replication/recombination/repair category comes from transposase, integrase and recombinase genes, and the unknown-function genes that differ between ecotypes mostly lie next to those mobile elements. Core repair genes differ little between ecotypes.

## Why it matters

These two categories showed the largest ecotype differences, but the differences are modest (about 3 to 4 percentage points in category proportions), and shared ancestry was not controlled, so they cannot yet be called adaptive. If mobile genes carry them, they would be read as mobile-element turnover, possibly reflecting lineage substructure, not habitat-specific repair. That would also help reconcile adaptive-looking categories with curated adaptive markers sitting in the core genome.

## How to test it

In the 12 species with valid ecotypes, split every gene in the replication/recombination/repair category into mobile (transposase, integrase, recombinase, phage-type) and housekeeping repair (e.g. mismatch and excision repair), using annotations in the Pangenome Collection. Recompute the ecotype difference for each part. For the unknown-function category, measure how often differing genes lie within a few genes of a mobile-element gene, and compare with size-matched random accessory genes. Repeat the comparison within the major lineages of each species, since ancestry was not controlled in the original result.

## What would support or refute it

Support: the category's ecotype difference largely disappears once mobile genes are removed, and unknown-function genes are enriched next to mobile genes, including within lineages. Refute: core repair genes carry the difference, or unknown-function genes are no closer to mobile elements than random accessory genes.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Gene-cluster annotations and genome-level presence/absence for the ecotype species are in the Pangenome Collection; the work is a finer annotation split and a gene-neighbourhood check.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/ecotype_functional_differentiation--69a046fd|Unknown-function and replication/repair categories show the largest ecotype differences]] (Extends retrieved work)
- Finding: [[findings/ecotype_functional_differentiation--667d861b|Adaptive COG categories show larger mean ecotype effect sizes than housekeeping categories]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_functional_differentiation--840b73cb|Most species-by-COG tests show ecotype differentiation, with every analyzed species affected]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1|Do Adaptive Functions Sit in the Accessory Genome or Inside the Core?]]

## Closest published work

- [PMID 40644951](https://pubmed.ncbi.nlm.nih.gov/40644951/) Genomic diversity of Cronobacter sakazakii across the food system to consumers at the global scale.
- [PMID 37154706](https://pubmed.ncbi.nlm.nih.gov/37154706/) Comparative Genomic Analyses of Lactococcus garvieae Isolated from Bovine Mastitis in China.
- [PMID 36853054](https://pubmed.ncbi.nlm.nih.gov/36853054/) Pan-Chromosome and Comparative Analysis of Agrobacterium fabrum Reveal Important Traits Concerning the Genetic Diversity, Evolutionary Dynamics, and Niche Adaptation of the Species.
- [PMID 33423895](https://pubmed.ncbi.nlm.nih.gov/33423895/) Mechanisms That Shape Microbial Pangenomes.

PMIDs 40644951 and 37154706 report enrichment of the replication/repair category in accessory or unique genes but do not ask whether mobile-element genes rather than repair genes drive it, and PMID 33423895 reviews how mobile elements shape pangenomes without testing this.
