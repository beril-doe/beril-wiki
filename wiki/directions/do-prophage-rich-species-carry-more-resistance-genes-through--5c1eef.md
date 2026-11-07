---
type: "Research direction"
description: "Species with more prophage markers carry broader resistance repertoires, yet resistance genes are only slightly more often accessory near prophages, and the effect depends on the distance cutoff. Do prophage-rich species gain resistance mainly through other mobile elements, rather than through prophages themselves?"
hypothesis: "If prophages were the vehicle, resistance genes in prophage-rich species would sit on prophage regions. Instead we predict they sit mostly on plasmid or integrative-element regions, and this holds equally in species with strong and weak prophage-AMR association."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Annotations exist, but dedicated element calling and base-pair-resolution placement over thousands of species still have to be run."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["prophage_amr_comobilization--02e63b0a", "prophage_amr_comobilization--4cead8a0"]
conflicts: ["conflict--environmental-resistome--e8ac0fe1"]
papers: ["30576310", "39333115", "38703011", "34232073"]
builds_on: ["findings/prophage_amr_comobilization--02e63b0a", "findings/prophage_amr_comobilization--4cead8a0", "conflicts/conflict--environmental-resistome--e8ac0fe1"]
projects: ["prophage_amr_comobilization", "t4ss_cazy_environmental_hgt"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do prophage-rich species carry more resistance genes through non-phage mobile DNA?

Species with more prophage markers carry broader resistance repertoires, yet resistance genes are only slightly more often accessory near prophages, and the effect depends on the distance cutoff. Do prophage-rich species gain resistance mainly through other mobile elements, rather than through prophages themselves?

## Hypothesis

If prophages were the vehicle, resistance genes in prophage-rich species would sit on prophage regions. Instead we predict they sit mostly on plasmid or integrative-element regions, and this holds equally in species with strong and weak prophage-AMR association.

## Why it matters

It would separate phages as vehicles of resistance from prophage density as a marker of a lineage that accumulates mobile DNA, and show which element types to monitor. The test distinguishes two predictions but cannot by itself prove why prophage density and resistance covary.

## How to test it

Re-call prophages in Pangenome Collection genomes with a dedicated prophage and plasmid caller, then compare with the keyword-based calls to measure false positives, such as anti-phage defense systems, and missed divergent prophages. Using base-pair positions, assign each AMR gene to prophage, plasmid, integrative-element or none. Ask whether the prophage-density relationship with AMR breadth is carried by genes on prophage regions or by genes on other elements, and whether this differs between species with few and many anti-phage defense systems.

## What would support or refute it

Support: most AMR genes in prophage-rich species lie on non-prophage elements, and prophage density loses explanatory power once other element classes are counted. Refute: AMR genes in prophage-rich species lie mainly on called prophage regions, and the association persists after counting other element classes.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Annotations exist, but dedicated element calling and base-pair-resolution placement over thousands of species still have to be run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/prophage_amr_comobilization--02e63b0a|Prophage density predicts AMR repertoire breadth across species]] (Extends retrieved work)
- Finding: [[findings/prophage_amr_comobilization--4cead8a0|Prophage-proximal AMR genes are only slightly more often accessory]] (Candidate novel)
- Conflict: [[conflicts/conflict--environmental-resistome--e8ac0fe1|Prophage and conjugative-machinery evidence for gene mobilization: genome-wide association versus local and mechanistic support]]

## Closest published work

- [PMID 30576310](https://pubmed.ncbi.nlm.nih.gov/30576310/) Genetic exchanges are more frequent in bacteria encoding capsules.
- [PMID 39333115](https://pubmed.ncbi.nlm.nih.gov/39333115/) Prophage-encoded antibiotic resistance genes are enriched in human-impacted environments.
- [PMID 38703011](https://pubmed.ncbi.nlm.nih.gov/38703011/) Streptococcus suis serotype 4: a population with the potential pathogenicity in humans and pigs.
- [PMID 34232073](https://pubmed.ncbi.nlm.nih.gov/34232073/) Distribution of Antimicrobial Resistance and Virulence Genes within the Prophage-Associated Regions in Nosocomial Pathogens.

PMID 30576310 links capsules to prophage and resistance load, and PMID 39333115 reports prophage-encoded ARGs in human-impacted environments; neither compares prophage with other mobile elements as carriers of the resistance genes.
