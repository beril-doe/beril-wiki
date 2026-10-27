---
type: "Research direction"
description: "Among P. aeruginosa genomes, do the lower GapMind carbon-pathway scores in the 1,796 lung/respiratory or CF genomes persist after phylogenetic control, separately from the deeper loss shared by the whole P. aeruginosa group relative to Pseudomonas_E?"
hypothesis: "The zero completeness of xylose, arabinose and myo-inositol pathways is fixed across the P. aeruginosa group. Lung/CF-associated score reductions (sorbitol \u22120.165, mannitol \u22120.204, gluconate \u22120.185) will persist within P. aeruginosa clades after phylogenetic control, which would be consistent with relaxed selection in the lung."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "GapMind scores and isolation metadata exist for the genomes, but the decisive growth assays need new measurements."
collections: ["kbase-ke-pangenome"]
findings: ["pseudomonas_carbon_ecology--9c42f41a", "pseudomonas_carbon_ecology--a6ba828d", "cf_formulation_design--460ed03a"]
conflicts: []
papers: ["29607620", "3922954", "25409940", "31214142", "22576821"]
builds_on: ["findings/pseudomonas_carbon_ecology--9c42f41a", "findings/pseudomonas_carbon_ecology--a6ba828d", "findings/cf_formulation_design--460ed03a"]
projects: ["cf_formulation_design", "pseudomonas_carbon_ecology"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Are lung-associated drops in sugar-pathway scores lineage-driven or evidence of within-host streamlining?

Among P. aeruginosa genomes, do the lower GapMind carbon-pathway scores in the 1,796 lung/respiratory or CF genomes persist after phylogenetic control, separately from the deeper loss shared by the whole P. aeruginosa group relative to Pseudomonas_E?

## Hypothesis

The zero completeness of xylose, arabinose and myo-inositol pathways is fixed across the P. aeruginosa group. Lung/CF-associated score reductions (sorbitol −0.165, mannitol −0.204, gluconate −0.185) will persist within P. aeruginosa clades after phylogenetic control, which would be consistent with relaxed selection in the lung.

## Why it matters

GapMind scores are computational predictions, not demonstrated losses. Separating ancestral subgenus differences from lung-associated differences would show whether CF-adapted strains have genuinely narrowed carbon use. That in turn bears on whether sugar-based competition can be used against them.

## How to test it

In kbase-ke-pangenome, take GapMind carbon scores for P. aeruginosa lung/respiratory-or-CF versus non-lung genomes (5,199 with metadata) with Pseudomonas_E outgroups. Fit models that partition variance into subgenus, clade and lung effects, and reconstruct ancestral pathway states. Then grow matched lung and environmental P. aeruginosa isolates, plus a Pseudomonas_E strain, on sorbitol, mannitol, gluconate, xylose and arabinose to compare measured growth with predicted scores.

## What would support or refute it

Support: the lung effect remains after clade control and measured growth is lower on the three sugars in lung isolates. Refute: the lung difference disappears within clades, or scores do not predict measured growth, indicating lineage structure or annotation limits rather than adaptation.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. GapMind scores and isolation metadata exist for the genomes, but the decisive growth assays need new measurements.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/pseudomonas_carbon_ecology--9c42f41a|P. aeruginosa group has lost most plant-sugar catabolism relative to Pseudomonas_E]] (Candidate novel)
- Finding: [[findings/pseudomonas_carbon_ecology--a6ba828d|Xylose, arabinose and myo-inositol pathways are absent in the P. aeruginosa group]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--460ed03a|Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes]] (Extends retrieved work)

## Closest published work

- [PMID 29607620](https://pubmed.ncbi.nlm.nih.gov/29607620/) Regulation of carbohydrate degradation pathways in Pseudomonas involves a versatile set of transcriptional regulators.
- [PMID 3922954](https://pubmed.ncbi.nlm.nih.gov/3922954/) Cloning of genes specifying carbohydrate catabolism in Pseudomonas aeruginosa and Pseudomonas putida.
- [PMID 25409940](https://pubmed.ncbi.nlm.nih.gov/25409940/) Impact of glycerol-3-phosphate dehydrogenase on virulence factor production by Pseudomonas aeruginosa.
- [PMID 31214142](https://pubmed.ncbi.nlm.nih.gov/31214142/) Catabolism of Nucleic Acids by a Cystic Fibrosis Pseudomonas aeruginosa Isolate: An Adaptive Pathway to Cystic Fibrosis Sputum Environment.
- [PMID 22576821](https://pubmed.ncbi.nlm.nih.gov/22576821/) Identification of traits shared by rhizosphere-competent strains of fluorescent pseudomonads.

PMID 29607620 and PMID 3922954 describe sugar metabolism and glucokinase absence in some strains, and PMID 25409940 and PMID 31214142 show altered substrate use in CF isolates. None compares genome-wide pathway scores while separating a lung-specific signal from the subgenus divide.
