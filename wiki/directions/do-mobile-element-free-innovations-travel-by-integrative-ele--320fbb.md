---
type: "Research direction"
description: "Does the strong mobile-element enrichment among novel genes sit alongside transfers that show no MGE cargo, because those move by integrative and conjugative routes or because their signature fades with time?"
hypothesis: "Within each focal gene class (PSII, PUL, mycolic acid, GT2), gains older by measured acquisition depth show lower MGE-neighbourhood rates, while integrative-element calls stay elevated near the loci. Fading therefore explains the missing phage signal."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "It needs Spark-scale neighbourhood scans, ICE detection and the permutation tests the reports describe as pending."
collections: ["kbase-ke-pangenome", "kbase-genomes", "kbase-uniref"]
findings: ["cog_analysis--7a21065f", "t4ss_cazy_environmental_hgt--5d73bfde", "t4ss_cazy_environmental_hgt--a2b33180", "t4ss_cazy_environmental_hgt--44ad24db", "costly_dispensable_genes--f3a85492"]
conflicts: ["conflict--horizontal-gene-transfer-driven-innovation--60dc31ce"]
papers: ["21298028", "30809245", "40298401"]
builds_on: ["findings/cog_analysis--7a21065f", "findings/t4ss_cazy_environmental_hgt--5d73bfde", "findings/t4ss_cazy_environmental_hgt--a2b33180", "findings/t4ss_cazy_environmental_hgt--44ad24db", "findings/costly_dispensable_genes--f3a85492", "conflicts/conflict--horizontal-gene-transfer-driven-innovation--60dc31ce"]
projects: ["cog_analysis", "costly_dispensable_genes", "gene_function_ecological_agora", "t4ss_cazy_environmental_hgt"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do mobile-element-free innovations travel by integrative elements whose signature fades with gene age?

Does the strong mobile-element enrichment among novel genes sit alongside transfers that show no MGE cargo, because those move by integrative and conjugative routes or because their signature fades with time?

## Hypothesis

Within each focal gene class (PSII, PUL, mycolic acid, GT2), gains older by measured acquisition depth show lower MGE-neighbourhood rates, while integrative-element calls stay elevated near the loci. Fading therefore explains the missing phage signal.

## Why it matters

It would show whether absence of an MGE signal rules out mobile transfer or reflects gene age and route, changing how mobile-element content is used as a marker of gene gain.

## How to test it

For each class, bin gain events by acquisition depth and compare MGE-neighbourhood rates across bins, without assuming classes share an age. Run ICE/IME detection around PSII, PUL and mycolic-acid loci and around the 376 GT2-neighbourhood MAGs. Add a housekeeping-gene null, run the pending T4SS-CAZy synteny permutation test, and BLAST Node_4915 (8 phyla) against NCBI nr.

## What would support or refute it

Support: MGE-neighbourhood rate falls with depth within classes and ICE/IME calls exceed the housekeeping null. Refute: rates are flat with depth and ICE/IME calls sit at null level, which would favour transfer without mobile-element involvement.

## Data

Approach: lakehouse analysis. Readiness: needs compute. It needs Spark-scale neighbourhood scans, ICE detection and the permutation tests the reports describe as pending.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/cog_analysis--7a21065f|Mobile elements dominate enrichment among novel genes across sampled species]] (Extends retrieved work)
- Finding: [[findings/t4ss_cazy_environmental_hgt--5d73bfde|No plasmid-borne CAZy genes found; transfer appears chromosomal or integrative]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--a2b33180|GT2 gene tree shows many cross-phylum horizontal transfer events]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--44ad24db|GT2-neighbourhood genomes carry more metal resistance genes]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--f3a85492|Mobile-element and virulence SEED categories enriched versus costly conserved genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--horizontal-gene-transfer-driven-innovation--60dc31ce|Do Mobile Elements Carry Most Bacterial Gene Novelty, or Do Focal Innovations Arrive Without an MGE-Cargo Signal?]]

## Closest published work

- [PMID 21298028](https://pubmed.ncbi.nlm.nih.gov/21298028/) Horizontal transfer, not duplication, drives the expansion of protein families in prokaryotes.
- [PMID 30809245](https://pubmed.ncbi.nlm.nih.gov/30809245/) Bacterial 'Grounded' Prophages: Hotspots for Genetic Renovation and Innovation.
- [PMID 40298401](https://pubmed.ncbi.nlm.nih.gov/40298401/) Mobile genetic elements in Klebsiella pneumoniae.

PMID 21298028 argues horizontal transfer drives protein-family expansion and PMID 30809245 describes prophage hotspots. Neither tests whether the mobile signal fades with gene age within a gene class.
