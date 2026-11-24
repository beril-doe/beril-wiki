---
type: "Research direction"
description: "Are environmental differences in prophage content due to modules or anti-defense genes being exchanged between unrelated prophages?"
hypothesis: "Tail, head and anti-defense modules from human-associated genomes have phylogenies discordant with their terminase lineage and host phylogeny, showing modular exchange."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Annotations and isolation metadata are in the catalog; trees and incongruence tests need computing, and metadata are sparse."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.bakta_pfam_domains"]
findings: ["prophage_ecology--4459b66b", "prophage_ecology--44d944a0", "prophage_ecology--3d5d045b"]
conflicts: []
papers: ["35746669", "28692019", "27533034", "25092302", "40639337"]
builds_on: ["findings/prophage_ecology--4459b66b", "findings/prophage_ecology--44d944a0", "findings/prophage_ecology--3d5d045b"]
projects: ["prophage_ecology"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do prophage modules move between hosts independently of the phage lineage that carries them?

Are environmental differences in prophage content due to modules or anti-defense genes being exchanged between unrelated prophages?

## Hypothesis

Tail, head and anti-defense modules from human-associated genomes have phylogenies discordant with their terminase lineage and host phylogeny, showing modular exchange.

## Why it matters

It would show that environment selects phage parts, not whole phages, which affects how phage ecology is modeled.

## How to test it

Build trees for tail, head and anti-defense modules and the TerL marker across genomes from human-associated and other isolation sources. Test incongruence with host and TerL trees. Compare human-associated versus other environments with genus-level controls and sampling-depth controls.

## What would support or refute it

Support: modules are discordant with TerL and host trees more than expected, and human-associated enrichment survives controls. Refute: module trees match TerL lineage, or enrichment vanishes with finer taxon strata or depth control.

## Data

Approach: analysis then experiment. Readiness: needs compute. Annotations and isolation metadata are in the catalog; trees and incongruence tests need computing, and metadata are sparse.

## Builds on

- Finding: [[findings/prophage_ecology--4459b66b|Module-level environment effects without lineage-level effects suggest modular exchange]] (Candidate novel)
- Finding: [[findings/prophage_ecology--44d944a0|No individual TerL lineage shows environment-specific enrichment]] (Candidate novel)
- Finding: [[findings/prophage_ecology--3d5d045b|Human-associated environments enriched for complete prophages and anti-defense genes beyond phylogeny]] (Candidate novel)

## Closest published work

- [PMID 35746669](https://pubmed.ncbi.nlm.nih.gov/35746669/) Whole-Genome Analysis Reveals That Bacteriophages Promote Environmental Adaptation of Staphylococcus aureus via Gene Exchange, Acquisition, and Loss.
- [PMID 28692019](https://pubmed.ncbi.nlm.nih.gov/28692019/) Bacteriophage evolution differs by host, lifestyle and genome.
- [PMID 27533034](https://pubmed.ncbi.nlm.nih.gov/27533034/) Uncovering Earth's virome.
- [PMID 25092302](https://pubmed.ncbi.nlm.nih.gov/25092302/) Pervasive domestication of defective prophages by bacteria.
- [PMID 40639337](https://pubmed.ncbi.nlm.nih.gov/40639337/) Bacteriophage genomes encode both broad and specific counter-defense repertoires to overcome bacterial defense systems.

35746669 and 28692019 show phage module mosaicism; this ties it to environment with a lineage-level null.
