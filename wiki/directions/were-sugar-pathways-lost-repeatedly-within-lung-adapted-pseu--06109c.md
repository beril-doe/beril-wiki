---
type: "Research direction"
description: "Is the weaker predicted sugar catabolism of lung and cystic fibrosis P. aeruginosa genomes a set of repeated losses inside the species, or does it only reflect the difference that already separates the P. aeruginosa group from the P. fluorescens group?"
hypothesis: "Within P. aeruginosa, the sorbitol, mannitol and gluconate pathways were lost several independent times on lung-associated branches, more often than on matched non-lung branches. This is a separate pattern from the group-wide predicted absence of xylose, arabinose and myo-inositol pathways."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The genome-level analysis uses existing pathway scores, but growth on the sugars needs new isolate assays."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["cf_formulation_design--460ed03a", "pseudomonas_carbon_ecology--9c42f41a", "pseudomonas_carbon_ecology--a6ba828d"]
conflicts: []
papers: ["25409940", "31214142", "26510267", "29607620", "3922954"]
builds_on: ["findings/cf_formulation_design--460ed03a", "findings/pseudomonas_carbon_ecology--9c42f41a", "findings/pseudomonas_carbon_ecology--a6ba828d"]
projects: ["cf_formulation_design", "pseudomonas_carbon_ecology"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Were sugar pathways lost repeatedly within lung-adapted Pseudomonas aeruginosa, independent of deeper lineage differences?

Is the weaker predicted sugar catabolism of lung and cystic fibrosis P. aeruginosa genomes a set of repeated losses inside the species, or does it only reflect the difference that already separates the P. aeruginosa group from the P. fluorescens group?

## Hypothesis

Within P. aeruginosa, the sorbitol, mannitol and gluconate pathways were lost several independent times on lung-associated branches, more often than on matched non-lung branches. This is a separate pattern from the group-wide predicted absence of xylose, arabinose and myo-inositol pathways.

## Why it matters

It would separate adaptation to the lung from inherited lineage history. It would also show which sugars a cystic fibrosis airway formulation can count on the pathogen being unable to use.

## How to test it

Using the Pangenome Collection, place the P. aeruginosa genomes on a within-species tree. Infer on which branches each of the seven lower-scoring carbon pathways changed from complete to incomplete. Ask whether such changes fall on lung-isolate branches more than on matched non-lung branches, and whether they recur in separate lineages. Then grow CF-derived and environmental P. aeruginosa isolates on sorbitol, mannitol and gluconate. Include xylose as a check on the genome-based prediction of absence: if some isolates do grow on it, the predicted absence is wrong for them and the check shows how far the pathway scores can be trusted.

## What would support or refute it

Support: losses fall repeatedly on separate lung branches, and CF isolates grow worse than environmental isolates on the three sugars. Refutation: the lower scores trace to a few deep lineages that happen to be over-sampled in the lung, or growth does not differ by isolate source.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The genome-level analysis uses existing pathway scores, but growth on the sugars needs new isolate assays.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/cf_formulation_design--460ed03a|Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes]] (Extends retrieved work)
- Finding: [[findings/pseudomonas_carbon_ecology--9c42f41a|P. aeruginosa group has lost most plant-sugar catabolism relative to Pseudomonas_E]] (Candidate novel)
- Finding: [[findings/pseudomonas_carbon_ecology--a6ba828d|Xylose, arabinose and myo-inositol pathways are absent in the P. aeruginosa group]] (Insufficient literature evidence)

## Closest published work

- [PMID 25409940](https://pubmed.ncbi.nlm.nih.gov/25409940/) Impact of glycerol-3-phosphate dehydrogenase on virulence factor production by Pseudomonas aeruginosa.
- [PMID 31214142](https://pubmed.ncbi.nlm.nih.gov/31214142/) Catabolism of Nucleic Acids by a Cystic Fibrosis Pseudomonas aeruginosa Isolate: An Adaptive Pathway to Cystic Fibrosis Sputum Environment.
- [PMID 26510267](https://pubmed.ncbi.nlm.nih.gov/26510267/) Pseudomonas aeruginosa displays an altered phenotype in vitro when grown in the presence of mannitol.
- [PMID 29607620](https://pubmed.ncbi.nlm.nih.gov/29607620/) Regulation of carbohydrate degradation pathways in Pseudomonas involves a versatile set of transcriptional regulators.
- [PMID 3922954](https://pubmed.ncbi.nlm.nih.gov/3922954/) Cloning of genes specifying carbohydrate catabolism in Pseudomonas aeruginosa and Pseudomonas putida.

PMID 25409940 and PMID 31214142 show that individual CF isolates use particular substrates differently, and PMID 29607620 and PMID 3922954 describe sugar handling in Pseudomonas. None asks whether loss is repeated within lung lineages as opposed to inherited from the wider group.
