---
type: "Research direction"
description: "Tail, head and anti-defense prophage modules were enriched in human-associated species while genome size dominated module composition. Within a host genus, do genomes with larger defense repertoires also carry more prophage anti-defense modules?"
hypothesis: "Anti-defense modules track the host's defense repertoire: within a genus, genomes with more defense systems carry more anti-defense modules, independently of genome size, and the pattern is stronger in human-associated than in freshwater genomes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Module calls rely on annotation proxies not validated with dedicated prophage detectors, defense calls must be generated for each genome, and environment labels are coarse with a large unknown category."
collections: ["kbase-ke-pangenome", "phagefoundry"]
findings: ["prophage_ecology--fc67e694", "prophage_ecology--9f2125cc", "prophage_ecology--3c13d0b7"]
conflicts: []
papers: ["40639337", "29371424", "25092302", "34232073"]
builds_on: ["findings/prophage_ecology--fc67e694", "findings/prophage_ecology--9f2125cc", "findings/prophage_ecology--3c13d0b7"]
projects: ["prophage_ecology"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do human-associated bacteria carry prophage anti-defense genes because of an arms race?

Tail, head and anti-defense prophage modules were enriched in human-associated species while genome size dominated module composition. Within a host genus, do genomes with larger defense repertoires also carry more prophage anti-defense modules?

## Hypothesis

Anti-defense modules track the host's defense repertoire: within a genus, genomes with more defense systems carry more anti-defense modules, independently of genome size, and the pattern is stronger in human-associated than in freshwater genomes.

## Why it matters

If so, the human enrichment reflects an arms race and not simply larger genomes accumulating prophages. If not, genome size is the better explanation, and anti-defense carriage is a by-product of prophage load.

## How to test it

In the Pangenome Collection, count defense systems and prophage anti-defense modules per genome for genera with many human-associated and freshwater isolates. Environment labels come from sparse, inconsistently labeled isolation-source text collapsed into 10 categories, with 9,659 species (35%) in an unknown category, so use only genomes with unambiguous sources and repeat with stricter and looser groupings. Model anti-defense count against defense count with genome size and genus as covariates, by environment. Check in PhageFoundry Browsers whether anti-defense-rich strains are infected by more phages.

## What would support or refute it

Support: anti-defense rises with defense repertoire within genera, beyond genome size, mostly in human-associated genomes, and this holds under stricter source labels. Refute: the relation vanishes once genome size is controlled, or it is the same across environments, or the environment contrast depends on how labels are grouped.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Module calls rely on annotation proxies not validated with dedicated prophage detectors, defense calls must be generated for each genome, and environment labels are coarse with a large unknown category.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/phagefoundry|PhageFoundry Browsers]]

## Builds on

- Finding: [[findings/prophage_ecology--fc67e694|Tail, head and anti-defense modules enriched in human-associated genomes against null models]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--9f2125cc|Genome size dwarfs environment and phylogeny as predictor of prophage module composition]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--3c13d0b7|No individual TerL lineage shows environment-specific enrichment beyond host phylogeny]] (Insufficient literature evidence)

## Closest published work

- [PMID 40639337](https://pubmed.ncbi.nlm.nih.gov/40639337/) Bacteriophage genomes encode both broad and specific counter-defense repertoires to overcome bacterial defense systems.
- [PMID 29371424](https://pubmed.ncbi.nlm.nih.gov/29371424/) Systematic discovery of antiphage defense systems in the microbial pangenome.
- [PMID 25092302](https://pubmed.ncbi.nlm.nih.gov/25092302/) Pervasive domestication of defective prophages by bacteria.
- [PMID 34232073](https://pubmed.ncbi.nlm.nih.gov/34232073/) Distribution of Antimicrobial Resistance and Virulence Genes within the Prophage-Associated Regions in Nosocomial Pathogens.

PMID 40639337 shows phage genomes encode counter-defense repertoires and PMID 29371424 maps defense systems across pangenomes. Neither relates prophage anti-defense carriage to host defense load across environments.
