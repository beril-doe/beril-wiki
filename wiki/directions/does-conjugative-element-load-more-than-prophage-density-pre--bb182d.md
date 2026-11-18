---
type: "Research direction"
description: "Species with many prophage markers carry broader resistance repertoires, yet resistance genes sit only slightly more often near prophages than far from them. Which class of mobile element actually tracks resistance breadth?"
hypothesis: "When prophage, plasmid, integrative-conjugative element and insertion-sequence loads are modelled together, conjugative elements explain resistance breadth better than prophage density, and the prophage association largely disappears."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Mobile-element and resistance-gene tables with genome and biome identifiers are listed with columns in the catalog."
databases: ["kescience.mgnify"]
tables: ["kescience.mgnify.gene_mobilome", "kescience.mgnify.gene_amr", "kescience.mgnify.genome", "kescience.mgnify.biome"]
findings: ["prophage_amr_comobilization--02e63b0a", "prophage_amr_comobilization--4cead8a0", "prophage_amr_comobilization--7802d299", "t4ss_cazy_environmental_hgt--5d73bfde"]
conflicts: []
papers: ["30576310", "38703011", "39333115", "34232073"]
builds_on: ["findings/prophage_amr_comobilization--02e63b0a", "findings/prophage_amr_comobilization--4cead8a0", "findings/prophage_amr_comobilization--7802d299", "findings/t4ss_cazy_environmental_hgt--5d73bfde"]
projects: ["prophage_amr_comobilization", "t4ss_cazy_environmental_hgt"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Does conjugative-element load, more than prophage density, predict resistance repertoire breadth?

Species with many prophage markers carry broader resistance repertoires, yet resistance genes sit only slightly more often near prophages than far from them. Which class of mobile element actually tracks resistance breadth?

## Hypothesis

When prophage, plasmid, integrative-conjugative element and insertion-sequence loads are modelled together, conjugative elements explain resistance breadth better than prophage density, and the prophage association largely disappears.

## Why it matters

If prophages are only a proxy for general mobile-element load, surveillance should track conjugative elements as the carriers of resistance. If prophage density keeps its own signal, transduction deserves more attention.

## How to test it

Using the metagenome-assembled genome catalogues, count per genome each mobile-element type (prophage, plasmid, integrative-conjugative element, integron, insertion sequence) and the number of distinct resistance genes. Model resistance breadth on all element types at once, within biome and within taxonomic group, and compare each type's independent contribution. Sugar-transferase genes near type IV secretion loci had no plasmid-borne copies, so the plasmid contribution is expected to be small.

## What would support or refute it

Support: conjugative-element and plasmid load carry the association and prophage load adds little once they are included. Refute: prophage density keeps a clear independent association within biomes, favoring phage-mediated transfer or phage-linked retention.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Mobile-element and resistance-gene tables with genome and biome identifiers are listed with columns in the catalog.

## Builds on

- Finding: [[findings/prophage_amr_comobilization--02e63b0a|Prophage density predicts AMR repertoire breadth across species]] (Extends retrieved work)
- Finding: [[findings/prophage_amr_comobilization--4cead8a0|Prophage-proximal AMR genes are only slightly more often accessory]] (Candidate novel)
- Finding: [[findings/prophage_amr_comobilization--7802d299|Many AMR genes share contigs with prophage markers]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--5d73bfde|No plasmid-borne CAZy genes found; transfer appears chromosomal or integrative]] (Insufficient literature evidence)

## Closest published work

- [PMID 30576310](https://pubmed.ncbi.nlm.nih.gov/30576310/) Genetic exchanges are more frequent in bacteria encoding capsules.
- [PMID 38703011](https://pubmed.ncbi.nlm.nih.gov/38703011/) Streptococcus suis serotype 4: a population with the potential pathogenicity in humans and pigs.
- [PMID 39333115](https://pubmed.ncbi.nlm.nih.gov/39333115/) Prophage-encoded antibiotic resistance genes are enriched in human-impacted environments.
- [PMID 34232073](https://pubmed.ncbi.nlm.nih.gov/34232073/) Distribution of Antimicrobial Resistance and Virulence Genes within the Prophage-Associated Regions in Nosocomial Pathogens.

PMID 38703011 and PMID 39333115 present prophages as vehicles for resistance genes and PMID 30576310 links prophage and resistance load to capsule-bearing lineages; none compares mobile-element classes in one model to see which explains resistance breadth.
