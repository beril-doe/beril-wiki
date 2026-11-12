---
type: "Research direction"
description: "Tail, head and anti-defense gene groups of prophages are more common in human-associated species, yet no single phage lineage tracked environment. Are these genes part of intact, potentially inducible prophages, or are they remnants kept by the host?"
hypothesis: "Human-associated genomes carry more intact prophage per megabase than soil or marine genomes, and their anti-defense genes sit inside those intact elements. If the enrichment is mostly remnants, the intact density will not differ between habitats."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Mobile-element and defense tables by habitat are listed, but per-genome normalization and overlap with gene groups must be computed, and the induction assays need new measurements."
databases: ["kescience.mgnify"]
tables: ["kescience.mgnify.gene_mobilome", "kescience.mgnify.gene_defense", "kescience.mgnify.genome", "kescience.mgnify.biome"]
findings: ["prophage_ecology--fc67e694", "prophage_ecology--3c13d0b7"]
conflicts: ["conflict--ecotype-clustering-validity--f884063a"]
papers: ["25092302", "34232073", "33606979", "40639337"]
builds_on: ["findings/prophage_ecology--fc67e694", "findings/prophage_ecology--3c13d0b7", "conflicts/conflict--ecotype-clustering-validity--f884063a"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "prophage_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Are phage tail and anti-defense genes enriched in human-associated bacteria carried by intact prophages?

Tail, head and anti-defense gene groups of prophages are more common in human-associated species, yet no single phage lineage tracked environment. Are these genes part of intact, potentially inducible prophages, or are they remnants kept by the host?

## Hypothesis

Human-associated genomes carry more intact prophage per megabase than soil or marine genomes, and their anti-defense genes sit inside those intact elements. If the enrichment is mostly remnants, the intact density will not differ between habitats.

## Why it matters

Intact prophages are a live source of gene transfer and host killing, while remnants are inert baggage. Telling them apart decides whether the human-associated pattern reflects ongoing phage-host conflict or past events that cost nothing now.

## How to test it

Use the mobile-element calls and defense annotations for the genome collection grouped by habitat. Count intact prophage and phage-type elements per megabase in human gut, soil and marine genomes, and check whether anti-defense and tail genes lie inside them. Compare the same genomes with the earlier annotation-based module counts. Follow with induction assays on a few human-gut isolates that carry the elements, to see whether virions are released.

## What would support or refute it

Support: intact prophage density is higher in human-associated genomes, anti-defense genes sit within them, and some isolates release virions. Refutation: intact density is similar across habitats and the enriched genes lie outside intact elements, which would favor domesticated remnants. Habitat sampling is uneven in the collection, and defense-table contents were not shown.

## Data

Approach: analysis then experiment. Readiness: needs compute. Mobile-element and defense tables by habitat are listed, but per-genome normalization and overlap with gene groups must be computed, and the induction assays need new measurements.

## Builds on

- Finding: [[findings/prophage_ecology--fc67e694|Tail, head and anti-defense modules enriched in human-associated genomes against null models]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--3c13d0b7|No individual TerL lineage shows environment-specific enrichment beyond host phylogeny]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--ecotype-clustering-validity--f884063a|Whole-genome gene content versus prophage modules: where does environmental structure appear?]]

## Closest published work

- [PMID 25092302](https://pubmed.ncbi.nlm.nih.gov/25092302/) Pervasive domestication of defective prophages by bacteria.
- [PMID 34232073](https://pubmed.ncbi.nlm.nih.gov/34232073/) Distribution of Antimicrobial Resistance and Virulence Genes within the Prophage-Associated Regions in Nosocomial Pathogens.
- [PMID 33606979](https://pubmed.ncbi.nlm.nih.gov/33606979/) Massive expansion of human gut bacteriophage diversity.
- [PMID 40639337](https://pubmed.ncbi.nlm.nih.gov/40639337/) Bacteriophage genomes encode both broad and specific counter-defense repertoires to overcome bacterial defense systems.

PMID 25092302 shows pervasive domestication of defective prophages, and PMID 40639337 describes phage counter-defense repertoires. Neither compares intact prophage density across habitats or places habitat-enriched anti-defense genes inside intact elements.
