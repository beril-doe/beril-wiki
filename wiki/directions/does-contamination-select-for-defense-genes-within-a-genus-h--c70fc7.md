---
type: "Research direction"
description: "Within genera found in both contaminated and clean settings, do genomes from contaminated sources carry more defense-annotated genes than close relatives from other sources, even though genus-averaged Oak Ridge community profiles showed no link?"
hypothesis: "Within genera with genomes from both contaminated and non-contaminated sources, contaminated-source genomes carry a larger share of defense-category genes than their relatives. The earlier genus-level null arose because this signal sits within genera and was averaged away."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome, metadata, environmental-attribute and annotation tables are in the catalog, but contamination labels must be derived from free-text source fields and the catalog did not show how annotations link to genomes or how many genera have both source classes."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.eggnog_mapper_annotations"]
findings: ["enigma_contamination_functional_potential--a97faeef", "enigma_contamination_functional_potential--f4cd1747", "enigma_contamination_functional_potential--606b2ef6"]
conflicts: []
papers: ["26583008", "35107332", "30523276"]
builds_on: ["findings/enigma_contamination_functional_potential--a97faeef", "findings/enigma_contamination_functional_potential--f4cd1747", "findings/enigma_contamination_functional_potential--606b2ef6"]
projects: ["enigma_contamination_functional_potential"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does contamination select for defense genes within a genus, hidden by genus-level averaging?

Within genera found in both contaminated and clean settings, do genomes from contaminated sources carry more defense-annotated genes than close relatives from other sources, even though genus-averaged Oak Ridge community profiles showed no link?

## Hypothesis

Within genera with genomes from both contaminated and non-contaminated sources, contaminated-source genomes carry a larger share of defense-category genes than their relatives. The earlier genus-level null arose because this signal sits within genera and was averaged away.

## Why it matters

It would decide whether the earlier null means contamination does not select for defense, or only that the broad genus-level proxy cannot see it. That choice changes how contaminated-site metagenomes are interpreted.

## How to test it

Use the genome-level pangenome collection and its genome metadata. Label genomes as contaminated-site or other from the sample isolation-source and environmental attribute text, starting with Rhodanobacter and other genera known from Oak Ridge. Per genome, take the share of annotated genes in the defense functional category from the functional annotation table. Compare labels within each genus, controlling for genome size, and run a permutation test that shuffles source labels within genus.

## What would support or refute it

Support: a consistent excess of defense genes in contaminated-source genomes across several genera. Refute: no within-genus difference, which would back the genus-level null and leave the earlier covariate-adjusted positive signal as an abundance or coverage artefact.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome, metadata, environmental-attribute and annotation tables are in the catalog, but contamination labels must be derived from free-text source fields and the catalog did not show how annotations link to genomes or how many genera have both source classes.

## Builds on

- Finding: [[findings/enigma_contamination_functional_potential--a97faeef|Covariate-adjusted models give a positive defense-contamination signal in relaxed mapping]] (Candidate novel)
- Finding: [[findings/enigma_contamination_functional_potential--f4cd1747|No significant defense–contamination association in relaxed mapping]] (Insufficient literature evidence)
- Finding: [[findings/enigma_contamination_functional_potential--606b2ef6|Confirmatory defense null holds across alternative contamination index definitions]] (In tension with retrieved work)

## Closest published work

- [PMID 26583008](https://pubmed.ncbi.nlm.nih.gov/26583008/) Comparative metagenomics reveals impact of contaminants on groundwater microbiomes.
- [PMID 35107332](https://pubmed.ncbi.nlm.nih.gov/35107332/) Genomic Features and Pervasive Negative Selection in Rhodanobacter Strains Isolated from Nitrate and Heavy Metal Contaminated Aquifer.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.

PMID 26583008 compared two wells at community level and PMID 35107332 studied one genus; this tests defense content within shared genera across source types.
