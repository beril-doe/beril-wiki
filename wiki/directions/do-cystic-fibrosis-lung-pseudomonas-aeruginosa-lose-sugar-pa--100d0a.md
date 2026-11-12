---
type: "Research direction"
description: "Is the lower sugar-pathway completeness in lung and cystic fibrosis P. aeruginosa the result of repeated, independent losses in many lineages, or of a few lung-adapted clades inheriting the losses?"
hypothesis: "Sugar-pathway losses (sorbitol, mannitol, gluconate) arise repeatedly on separate branches of the P. aeruginosa tree in lung isolates, and lung isolates grow worse on those sugars than environmental isolates from the same clades."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Pathway scores, genome-to-genome similarity and isolation-source labels are in the catalog, but tree-based loss reconstruction and the growth assays still have to be run."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.genome_ani", "kbase.ke_pangenome.ncbi_env"]
findings: ["cf_formulation_design--460ed03a", "pseudomonas_carbon_ecology--9c42f41a"]
conflicts: ["conflict--ecotype-environment-gene-content--30e389f5"]
papers: ["25409940", "31214142", "17873029", "26510267"]
builds_on: ["findings/cf_formulation_design--460ed03a", "findings/pseudomonas_carbon_ecology--9c42f41a", "conflicts/conflict--ecotype-environment-gene-content--30e389f5"]
projects: ["cf_formulation_design", "pseudomonas_carbon_ecology"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do cystic fibrosis lung Pseudomonas aeruginosa lose sugar pathways repeatedly and independently?

Is the lower sugar-pathway completeness in lung and cystic fibrosis P. aeruginosa the result of repeated, independent losses in many lineages, or of a few lung-adapted clades inheriting the losses?

## Hypothesis

Sugar-pathway losses (sorbitol, mannitol, gluconate) arise repeatedly on separate branches of the P. aeruginosa tree in lung isolates, and lung isolates grow worse on those sugars than environmental isolates from the same clades.

## Why it matters

The lung-streamlining idea is an evolutionary inference from genome scores, not a measured loss. Repeated independent loss would support relaxed selection in the lung, and it would tell formulation designers which substrates lung strains can no longer use.

## How to test it

Step 1: from the pathway scores and isolation-source labels for the 6,760 P. aeruginosa genomes, build a similarity tree from pairwise genome distances. Reconstruct where each of the seven lower-scoring carbon pathways was lost, and count independent losses in lung versus non-lung genomes. Step 2: choose matched lung and environmental isolate pairs from the same clades and measure growth on sorbitol, mannitol and gluconate, with glycerol as a positive control.

## What would support or refute it

Support: many independent losses concentrated in lung isolates, plus reduced growth on those sugars in the lung members of matched pairs. Refute: the losses fall in a few clades regardless of source, or growth does not differ between matched pairs.

## Data

Approach: analysis then experiment. Readiness: needs compute. Pathway scores, genome-to-genome similarity and isolation-source labels are in the catalog, but tree-based loss reconstruction and the growth assays still have to be run.

## Builds on

- Finding: [[findings/cf_formulation_design--460ed03a|Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes]] (Extends retrieved work)
- Finding: [[findings/pseudomonas_carbon_ecology--9c42f41a|P. aeruginosa group has lost most plant-sugar catabolism relative to Pseudomonas_E]] (Candidate novel)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--30e389f5|Carbon-Pathway Habitat Signal vs. the Broad Species-Level Null on Environment and Gene Content]]

## Closest published work

- [PMID 25409940](https://pubmed.ncbi.nlm.nih.gov/25409940/) Impact of glycerol-3-phosphate dehydrogenase on virulence factor production by Pseudomonas aeruginosa.
- [PMID 31214142](https://pubmed.ncbi.nlm.nih.gov/31214142/) Catabolism of Nucleic Acids by a Cystic Fibrosis Pseudomonas aeruginosa Isolate: An Adaptive Pathway to Cystic Fibrosis Sputum Environment.
- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 26510267](https://pubmed.ncbi.nlm.nih.gov/26510267/) Pseudomonas aeruginosa displays an altered phenotype in vitro when grown in the presence of mannitol.

PMIDs 25409940 and 31214142 describe single cystic fibrosis isolates with altered carbon use; this direction asks whether the pattern is convergent across the species and tests it by growth measurements.
