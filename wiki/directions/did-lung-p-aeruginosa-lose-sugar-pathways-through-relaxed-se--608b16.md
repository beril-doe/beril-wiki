---
type: "Research direction"
description: "Does the lower sugar-pathway completeness in lung P. aeruginosa reflect decay within lineages after colonization, or a clade composition effect?"
hypothesis: "Within matched phylogenetic subclades, lung/CF genomes keep lower sorbitol, mannitol and gluconate pathway scores than non-lung genomes, with pseudogenization or relaxed-constraint signatures in the pathway genes. This is the evolutionary interpretation the report infers but did not measure."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "GapMind scores and metadata exist for 5,199 genomes, but phylogeny-aware regression and selection tests have to be run."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["cf_formulation_design--460ed03a", "cf_formulation_design--1799127b", "pseudomonas_carbon_ecology--9c42f41a"]
conflicts: []
papers: ["25409940", "31214142", "17873029"]
builds_on: ["findings/cf_formulation_design--460ed03a", "findings/cf_formulation_design--1799127b", "findings/pseudomonas_carbon_ecology--9c42f41a"]
projects: ["cf_formulation_design", "pseudomonas_carbon_ecology"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Did lung P. aeruginosa lose sugar pathways through relaxed selection or lineage composition?

Does the lower sugar-pathway completeness in lung P. aeruginosa reflect decay within lineages after colonization, or a clade composition effect?

## Hypothesis

Within matched phylogenetic subclades, lung/CF genomes keep lower sorbitol, mannitol and gluconate pathway scores than non-lung genomes, with pseudogenization or relaxed-constraint signatures in the pathway genes. This is the evolutionary interpretation the report infers but did not measure.

## Why it matters

Separating lineage from habitat tells us whether lung metabolic streamlining is real adaptation, which bears on CF formulations that rely on retained amino acid catabolism.

## How to test it

Among the 5,199 of 6,760 P. aeruginosa genomes with environmental metadata (1,796 lung/respiratory or CF), compare GapMind scores for sorbitol (difference -0.165), mannitol (-0.204) and gluconate (-0.185) between lung and non-lung genomes within phylogenetic subclades, using phylogenetic regression. Also test for pseudogenization and dN/dS in the pathway genes, and contrast with the Pseudomonas_E repertoire, where 43 of 62 carbon pathways differ.

## What would support or refute it

Support: differences persist within subclades together with pseudogene or dN/dS evidence of relaxed constraint. Refute: differences vanish after clade control, or lung genomes cluster in sugar-poor clades, pointing to lineage composition.

## Data

Approach: lakehouse analysis. Readiness: needs compute. GapMind scores and metadata exist for 5,199 genomes, but phylogeny-aware regression and selection tests have to be run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/cf_formulation_design--460ed03a|Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes]] (Extends retrieved work)
- Finding: [[findings/cf_formulation_design--1799127b|Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain]] (Extends retrieved work)
- Finding: [[findings/pseudomonas_carbon_ecology--9c42f41a|P. aeruginosa group has lost most plant-sugar catabolism relative to Pseudomonas_E]] (Candidate novel)

## Closest published work

- [PMID 25409940](https://pubmed.ncbi.nlm.nih.gov/25409940/) Impact of glycerol-3-phosphate dehydrogenase on virulence factor production by Pseudomonas aeruginosa.
- [PMID 31214142](https://pubmed.ncbi.nlm.nih.gov/31214142/) Catabolism of Nucleic Acids by a Cystic Fibrosis Pseudomonas aeruginosa Isolate: An Adaptive Pathway to Cystic Fibrosis Sputum Environment.
- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.

PMID 25409940 and 31214142 describe individual CF isolates with altered substrate use, but neither tests genome-wide sugar-pathway decay against a phylogenetically matched non-lung background.
